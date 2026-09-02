# Agent Swarm

The home screen lists every agent the control plane can load. It is the operator catalog, not a runtime launcher.

## What you see

- Agent cards grouped by pack (`video`, `specials`, `other`) and, for video, by `va_category`.
- Live / unavailable status from `GET /health` and `/api/v3`.
- Search across agent id, role, folder, and category.

## What this screen does not do

- It does not enable T3, network, plugins, or production activation.
- It does not write memory.
