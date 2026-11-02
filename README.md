# Chord Sheet Editor

Write guitar chord sheets for Persian and English songs and poems, then print them or save them as PDF.

Each bar is split into equal time slots (8 in 4/4), so a word typed under a slot is sung on that beat. The chord sits above the slot where it changes, and the strum pattern runs under every bar. Farsi sheets read right to left; English sheets read left to right.

**Open the editor:** https://yasseralizadeh.github.io/chord-sheet-editor/

It runs entirely in the browser. Nothing is uploaded, and the single `index.html` file also works offline.

## Features

- Farsi (RTL) and English (LTR) sheets, one working song per language
- Time signatures 4/4, 3/4, 2/4 and 6/8, with a strum pattern you set by tapping the arrows
- Chord autocomplete, chord diagrams, transpose ±1 semitone, capo
- `*` after a chord (`G*`) for a vocal entry a couple of strums late, drawn as a dotted lead-in
- ⊛ marks a finger-picking set at the end of a line; ×N repeats a line
- Words that carry across a slot or barline stay joined (Persian letters keep their connected forms)
- Grey out unused slots at the end of a line, so a poem's next line starts on the next row
- Long songs flow onto extra Letter-size pages, numbered at the bottom
- Undo and redo (Ctrl/⌘+Z, Ctrl/⌘+Shift+Z)
- Save poems in the browser, or export and import song files (.json)
- Works on laptops and phones; on phones an on-screen key bar replaces Tab and Enter

## Keys

| Key | Action |
| --- | --- |
| Space (at the end of a word, or in an empty slot) | Next slot |
| Tab | Next slot; the word continues (letters stay joined) |
| Shift+Space | A real space inside a slot |
| Enter | Next line |
| Backspace in an empty slot | Previous slot |
| Ctrl/⌘+Z, Ctrl/⌘+Shift+Z | Undo, redo |

## Examples

- [Hafez, ghazal 1 (Farsi, 4/4)](examples/hafez-ghazal-1.pdf)
- [Amazing Grace (English, 3/4)](examples/amazing-grace.pdf)

Both texts are in the public domain.

## Building

`index.html` is generated from `src/editor.src.html` with the fonts embedded:

```
python3 tools/build.py
```

## Fonts

[Vazirmatn](https://github.com/rastikerdar/vazirmatn), [Lalezar](https://github.com/BornaIz/Lalezar) and [Barlow Condensed](https://github.com/jpt/barlow) are used under the SIL Open Font License 1.1.

---

© YasserAlizadeh
