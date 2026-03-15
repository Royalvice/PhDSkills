# Install Windows and macOS

## Windows

Use `winget` for package installation and `python -m pip` for Python package installation.

Expected tools:

- Quarto
- Pandoc when Quarto does not already provide a usable Pandoc path
- `python-docx` for generating built-in `reference.docx` templates used by DOCX output
- TinyTeX or another TeX toolchain needed for PDF output
- `rsvg-convert` only when you need deterministic rasterization of SVG images for document formats or Word environments that do not handle embedded SVG reliably

## macOS

Use `brew` for package installation and `python -m pip` for Python package installation.

Expected tools:

- Quarto
- Pandoc when needed
- `python-docx` for generating built-in `reference.docx` templates used by DOCX output
- TinyTeX or another TeX toolchain needed for PDF output
- `rsvg-convert` only when SVG rasterization support is required

## Doctor policy

Always verify the environment before rendering:

- locate executables
- query versions where possible
- verify Python modules needed by the active output path
- report missing or broken dependencies clearly
- distinguish required dependencies from optional helpers

## Notes

- DOCX rendering without a user-supplied `reference.docx` requires `python-docx`.
- On Windows, Quarto may probe R paths even for non-R documents; md2all sets a conservative Quarto environment to keep DOCX rendering stable in automated shells.
- SVG image conversion helpers are optional. Quarto and Word may still accept embedded SVG directly, but `rsvg-convert` remains the safer path when rasterization is needed.

## Scope

v1 supports Windows and macOS only. Fonts are detected and reported, not bundled.
