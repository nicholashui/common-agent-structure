# Agent Org Chat

Org Chat is a **read-only organization chart** of the selected agent group. It is not a messaging surface and not a chat completion UI.

## Contract

- Data comes from public `/api/v3` structure/org payloads.
- No compose, run, or memory writes happen here.
- Peer critique edges may be shown as relationships; they are not a live bus.
