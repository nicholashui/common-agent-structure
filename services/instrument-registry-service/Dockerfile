FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml README.md /app/
COPY src /app/src
RUN pip install --no-cache-dir -e ".[api]"

ENV PYTHONPATH=/app/src
ENV CASOPS_INSTRUMENT_DATA=/var/casops/instruments
ENV CASOPS_INSTRUMENT_KEY=/var/casops/instruments/keys/ed25519.pem
ENV CASOPS_ROLE=instruments

EXPOSE 8083
CMD ["uvicorn", "casops.instruments.bootstrap:create_app_from_env", "--factory", "--host", "0.0.0.0", "--port", "8083"]
