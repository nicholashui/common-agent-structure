"""Live source fetchers for CIT-GATE-001. Network I/O is injectable for tests."""

from __future__ import annotations

import hashlib
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Callable
from urllib.parse import urlparse

ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_ATOM = "{http://www.w3.org/2005/Atom}"
_ARXIV = "{http://arxiv.org/schemas/atom}"


@dataclass(frozen=True)
class LiveSource:
    identifier: str
    title: str
    authors: tuple[str, ...]
    venue: str
    published: str
    digest: str
    body: str
    found: bool


Fetcher = Callable[[str], bytes]


def default_fetcher(url: str, *, timeout: float = 20.0) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "casops-citation-audit/0.1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def arxiv_id(identifier: str) -> str:
    value = identifier.strip()
    value = re.sub(r"^arXiv:", "", value, flags=re.IGNORECASE)
    return value.split("v")[0]


def fetch_arxiv(identifier: str, *, fetcher: Fetcher = default_fetcher) -> LiveSource:
    paper_id = arxiv_id(identifier)
    url = ARXIV_API.format(arxiv_id=paper_id)
    raw = b""
    last_error = ""
    for attempt in range(4):
        try:
            raw = fetcher(url)
            last_error = ""
            break
        except urllib.error.HTTPError as exc:
            last_error = str(exc)
            if exc.code == 429:
                time.sleep(1.5 * (attempt + 1))
                continue
            break
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
            time.sleep(0.4)
    if not raw:
        html = fetch_url(f"https://arxiv.org/abs/{paper_id}", fetcher=fetcher)
        if html.found and paper_id in (html.title + html.body):
            title = re.sub(r"^\[[^\]]+\]\s*", "", html.title)
            title = re.sub(r"\s+\|\s+arXiv.*$", "", title, flags=re.IGNORECASE)
            return LiveSource(
                f"arXiv:{paper_id}",
                " ".join(title.split()),
                (),
                f"arXiv:{paper_id}",
                "",
                html.digest,
                html.body,
                True,
            )
        return LiveSource(identifier, "", (), "arxiv", "", "", last_error, False)
    digest = hashlib.sha256(raw).hexdigest()
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return LiveSource(identifier, "", (), "arxiv", "", digest, "", False)
    entry = root.find(f"{_ATOM}entry")
    if entry is None:
        return LiveSource(identifier, "", (), "arxiv", "", digest, "", False)
    title = " ".join((entry.findtext(f"{_ATOM}title") or "").split())
    authors = tuple(
        " ".join((node.findtext(f"{_ATOM}name") or "").split())
        for node in entry.findall(f"{_ATOM}author")
    )
    published = (entry.findtext(f"{_ATOM}published") or "")[:10]
    summary = entry.findtext(f"{_ATOM}summary") or ""
    doi = entry.findtext(f"{_ARXIV}doi") or ""
    venue = f"arXiv:{paper_id}"
    if doi:
        venue = f"{venue}; doi:{doi}"
    return LiveSource(f"arXiv:{paper_id}", title, authors, venue, published, digest, summary, True)


def fetch_url(url: str, *, fetcher: Fetcher = default_fetcher) -> LiveSource:
    parsed = urlparse(url)
    try:
        raw = fetcher(url)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        return LiveSource(url, "", (), parsed.netloc or "url", "", "", str(exc), False)
    digest = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8", errors="replace")
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
    title = " ".join((title_match.group(1) if title_match else parsed.path).split())
    title = re.sub(r"<[^>]+>", "", title)
    return LiveSource(url, title, (), parsed.netloc or "url", "", digest, text[:4000], True)
