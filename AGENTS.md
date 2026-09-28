# SINGLEBOOK

SingleBook is a self-contained ebook reader and editor. The complete
application, book data, styles, and assets live in `singlebook.html`.

## Product goals

- Beautiful typography
- A pleasant, opinionated interface with sensible defaults
- Familiar browser and OS shortcuts, including undo and save
- A focused Markdown subset suitable for writing books
- Books that remain readable and editable offline for the long term

## Architectural invariants

- `singlebook.html` is the canonical source file. There is no generated
  version or build step.
- Keep the application dependency-free and fully functional without a
  network connection.
- Do not add external scripts, styles, fonts, images, frames, imports,
  analytics, or network clients.
- Keep the HTML, CSS, JSON, and JavaScript readable and unminified.
- A saved copy must contain the complete reader, editor, and current book.
  Always verify changes after saving and reopening a copy.
- Preserve compatibility with existing book data. Do not change the
  document schema or format version without considering migration and
  backward compatibility.
- Preserve stable page IDs and `#page/...` links.

## Security

- Treat the Content Security Policy as an intentional security boundary.
- Markdown content must not execute arbitrary HTML or JavaScript.
- Preserve link-protocol validation and safe image handling.
- Do not relax SVG, raw HTML, or external-resource restrictions without
  an explicit project decision.

## Implementation guidelines

- Make product-code changes directly in `singlebook.html`.
- Follow the existing formatting and use the existing helpers and CSS
  variables where practical.
- Keep changes small and avoid unrelated refactoring.
- Do not add frameworks, package managers, transpilers, or generated code.
- Test code and debugging fixtures must not be embedded in the distributed
  HTML file.

## Verification

Test proportionally to the change. Before release:

- Open the exact file locally with networking disabled.
- Exercise affected reader and editor workflows.
- Check keyboard behavior and focus handling.
- Save the book, reopen the resulting file, and repeat the affected flow.
- Verify direct-file saving in Chrome or Edge when relevant.
- Verify downloaded-copy saving in Firefox or Safari when relevant.
- Confirm the browser console has no unexpected errors.
- Review the final diff for unrelated changes or external resources.

## Non-goals

- DRM
- Multiple books in one file
- Complete Markdown compatibility
- Syntax highlighting
- Accounts, cloud services, or required server infrastructure
- Tests embedded in the distributed file
