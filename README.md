# SINGLEBOOK
Singlebook is a complete ebook and editor in one portable HTML file. It has no dependencies, build step, account, server, or required internet connection.  It is heavily inspired by [Bento](https://bento.page/) and [WriteBook](https://once.com/writebook), specifically the everything-bundled-into-one-file from the former and the simple self-publishing ideals of the latter.

## Start a book
1. Copy `SingleBook.singlebook.html` and rename it to `your-book.singlebook.html`.
2. Open it in a modern browser.
3. Choose **Edit**, write your book, then choose **Save**.

For browsers that support the Filesystem Access API (Chrome and relatives such as Edge) the file can be updated directly. For browsers that do not support this API (Firefox and its derivatives, Safari) saving changes requires downloading an updated copy instead.

## Features
- Reader and editor modes
- Text, section, and picture pages
- A focused Markdown subset: headings, emphasis, lists, links, images, quotes, and code
- Embedded images for a portable, offline book
- Stable page links and simple page reordering
- Undo and Save shortcuts work.  Arrows to navigate.
- Customizable accent colors

Books open in reader mode and remain fully editable by anyone with the file.

## Explicit Non-goals
- Multiple books per file
- DRM

## Hacking
Edit `singlebook.html` directly and reload it in a browser. The HTML, CSS, document data, and unminified JavaScript all live in that file; there is nothing to install or compile.

## Examples
There are example books under `examples/` which are generated from the json data under `examples/data` by a python script under `tools/`  This avoids having to manually keep the example books in sync with the authoritative book when new features get added.

## AI and contributions
Singlebook was created for my own use, with assistance from LLMs to be sure, but it has not been vibe coded.  Pull requests are absolutely welcome but if your PR looks like slop that you yeeted out into the void I'm just going to close it without comment.
