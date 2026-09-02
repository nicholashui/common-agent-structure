# Help / Document Panel Extraction Spec

## Goal

Extract and re-implement the reusable frontend logic for a document help system that:

1. loads markdown documents from the application's static `public/docs` area,
2. exposes header icon actions for document access,
3. shows or hides a right-side help drawer,
4. resolves the correct document files based on the current route,
5. renders markdown safely with support for relative assets,
6. keeps the implementation generic so it can be applied to another system.

Do **not** carry over any business-domain, report-specific, authentication-specific, or product-specific behavior. Keep only the common UI/document-viewer logic.

## Scope To Keep

- Top/header icon click behavior for opening document views.
- Top/header icon click behavior for toggling the right-side document drawer.
- Workspace-level state for right drawer open/close.
- Workspace-level state for persistent right drawer width.
- Right drawer resize behavior.
- Right drawer tab behavior for multiple document types.
- Route-based document path resolution.
- Runtime markdown file loading from `public/docs`.
- Markdown rendering with relative image resolution.
- Generic loading, empty, and error states.
- Mobile left navigation drawer open/close behavior only if the target system also uses a responsive shell.

## Scope To Exclude

- Business routes, module names, report names, and screen-specific document names.
- Authentication guards and login-related layout behavior.
- Search pages, print actions, user menu actions, theme logic, and logout behavior.
- Any hardcoded product branding.
- Any domain-specific fallback paths that are not part of the generic route-to-doc convention.

## Expected Static Content Layout

Assume documentation lives under:

```text
public/docs/<route-path>/<doc-type>.md
```

Examples of generic document types:

```text
public/docs/orders/list/spec.md
public/docs/orders/list/userguide.md
```

Rules:

- Use route-derived folders under `public/docs`.
- Use one markdown file per document type.
- Support a route-specific file first.
- Support a parameter-stripped fallback file second.

## Required Header Actions

Implement two independent header actions:

1. **Full document page action**
   - Clicking the document icon navigates to a dedicated full-page markdown viewer.
   - This is separate from the right-side drawer.
   - The target route should be configurable in the destination system.

2. **Right-side drawer toggle action**
   - Clicking the drawer/help icon toggles the right panel open or closed.
   - The button should expose pressed state when the panel is open.
   - The panel state must be owned by the workspace shell, not by individual pages.

## Workspace Shell Behavior

The shell should own these states:

- `drawerOpen` for mobile left navigation drawer if applicable.
- `rightPanelOpen` for the help/document drawer.
- `rightPanelWidth` for persisted drawer width.
- `rightPanelDragging` for resize transition control.

### Required behaviors

- Toggle the left mobile drawer on small screens.
- Close the left mobile drawer automatically when viewport returns to desktop.
- Toggle the right help drawer from the header button.
- Close the right help drawer from its own close button.
- Persist the right drawer width in local storage.
- Clamp the restored width between configured min/max values.
- Disable width transition animation while the user is actively dragging the resize handle.

## Right Drawer Structure

The right drawer should contain:

- a header area,
- a close button,
- a tab list,
- one scrollable content area per tab,
- a vertical resize handle on the left edge of the drawer.

### Drawer tabs

Use configurable tab definitions such as:

```ts
type HelpTab = {
  id: string;
  label: string;
  mdPath: string | null;
};
```

Notes:

- `id` is the stable tab key.
- `label` is the UI label.
- `mdPath` may be left `null` in config and computed at runtime from the current route.
- The default active tab should be the first configured tab.
- Reset active tab to the default whenever the right drawer is newly opened.

## Route To Document Resolution

Build markdown paths dynamically from the current route.

### Required resolution logic

1. Read the current browser route.
2. Normalize trailing slashes.
3. Build a route path including current params.
4. Build a second route path with parameter placeholders removed.
5. For each tab, construct candidate markdown paths in this order:

```text
/docs<current-route>/<tab-id>.md
/docs<route-with-params-stripped>/<tab-id>.md
```

6. Attempt the first candidate.
7. If it is missing, attempt the fallback candidate.

### Why this matters

This allows:

- exact per-screen documents,
- reusable template documents for parameterized routes,
- zero hardcoded business-module mappings in the component.

## Markdown Loading Rules

Implement markdown loading as a reusable hook or utility.

### Requirements

- Accept one or more candidate markdown paths.
- Do nothing if the drawer/tab is not active.
- Fetch using same-origin credentials.
- Request markdown/text content types.
- Cache successful results in memory by resolved path.
- Return one of these states:
  - `idle`
  - `loading`
  - `ready`
  - `error`

### Missing-file handling

Treat these as a soft miss and try the next candidate path:

- HTTP `404`
- responses that return HTML instead of markdown
- dev-server fallbacks that return `index.html` with HTTP `200`

If all candidates fail because documents do not exist:

- show a neutral empty message such as:
  - `No document for this screen yet.`

If a real request error occurs:

- show a normal error state with the requested path and message.

## Markdown Rendering Rules

Render markdown with a markdown library that supports GitHub-flavored markdown.

### Required rendering behavior

- Resolve relative image paths against the loaded markdown file path.
- Preserve absolute URLs unchanged.
- Preserve root-relative asset URLs unchanged.
- Apply readable styles for:
  - headings,
  - paragraphs,
  - ordered and unordered lists,
  - links,
  - images,
  - blockquotes,
  - inline code,
  - fenced code blocks,
  - tables,
  - horizontal rules.

### Image handling

Support markdown files that contain either:

- standard markdown image syntax, or
- raw HTML `<img>` tags.

If raw HTML `<img>` tags are present, pre-transform them into standard markdown image syntax before rendering so relative asset handling remains consistent.

## Right Drawer Resize Behavior

Implement the drawer as resizable from its left edge.

### Pointer behavior

- On pointer down:
  - store `startX`,
  - store `startWidth`,
  - set document cursor to `col-resize`,
  - disable text selection,
  - mark resize state as active.

- On pointer move:
  - compute new width from horizontal drag distance,
  - dragging left makes the drawer wider,
  - dragging right makes the drawer narrower,
  - clamp the result to min/max bounds.

- On pointer up or pointer cancel:
  - clear drag state,
  - restore cursor,
  - restore text selection,
  - mark resize state as inactive.

### Keyboard accessibility

The resize handle must support keyboard resizing:

- `ArrowLeft`: increase width
- `ArrowRight`: decrease width
- `Home`: jump to max width
- `End`: jump to min width
- `Shift` may use a larger step

The resize handle should expose separator semantics and min/max/current values for accessibility.

## Drawer Open/Close Rules

Implement these behaviors:

- If `rightPanelOpen` is `false`, do not render the right drawer.
- If `rightPanelOpen` is `true`, render the drawer inside the workspace layout.
- The header toggle button flips the open state.
- The drawer close button sets the open state to `false`.
- The main workspace grid should expand or shrink based on whether the panel is open.

## Full-Page Document Viewer

Provide a separate generic markdown page component for dedicated document reading.

### Requirements

- Accept a markdown path as input.
- Resolve the path against `public/`.
- Load and cache the markdown file.
- Reject HTML fallback content that indicates the file did not resolve correctly.
- Render loading and error states.
- Reuse the same markdown rendering rules as the right drawer.

This full-page viewer should remain independent from the right drawer so the target system can use:

- full-page documentation,
- contextual side-drawer documentation,
- or both.

## Implementation Guidance For Another System

Tell the coding agent to implement the following reusable pieces:

1. `WorkspaceShell`
   - owns panel open/close and width state
   - wires the top-bar toggle to the right drawer
   - persists width to local storage

2. `TopBar`
   - includes one button for full-page documents
   - includes one button for right-drawer toggle

3. `RightHelpPanel`
   - tabbed container
   - route-aware markdown resolution
   - close button
   - resize handle

4. `useMarkdown`
   - tries candidate paths in order
   - caches successful results
   - distinguishes soft missing-document cases from real errors

5. `MarkdownDocument`
   - generic full-page markdown renderer
   - resolves relative assets
   - renders markdown consistently

6. `helpPanelTabs`
   - configurable list of common document types

## Acceptance Criteria

- Clicking the header document button opens a dedicated full-page document view.
- Clicking the header help/drawer button toggles the right-side help drawer.
- The right drawer displays one tab per configured document type.
- The right drawer loads markdown based on the current route.
- Parameterized routes fall back to a generic parameter-stripped document path.
- Missing markdown files do not crash the UI.
- HTML fallback responses are treated as missing documents, not valid markdown.
- Relative images inside markdown render correctly.
- Drawer width persists across reloads.
- Drawer width can be resized by mouse/pointer and keyboard.
- The extracted design contains no business-domain logic.

## Non-Goals

- Do not migrate any report logic.
- Do not migrate any authorization logic.
- Do not migrate any page-specific search or highlighting behavior.
- Do not migrate any product-specific navigation structure.
