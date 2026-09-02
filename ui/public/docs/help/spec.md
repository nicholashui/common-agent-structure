# Help

This Control UI loads markdown from `public/docs` using the current route:

- `/docs<route>/<tab>.md`
- fallback `/docs<route-with-params-stripped>/<tab>.md`

Tabs are **Spec** and **User guide**. Missing files show a neutral empty message. HTML fallbacks from the dev server are treated as missing documents.
