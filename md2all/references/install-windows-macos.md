# Install Windows and macOS

## Windows

Use `winget` for package installation.

Expected tools:

- Quarto
- Pandoc when Quarto does not already provide a usable Pandoc path
- TinyTeX or another TeX toolchain needed for PDF output

## macOS

Use `brew` for package installation.

Expected tools:

- Quarto
- Pandoc when needed
- TinyTeX or another TeX toolchain needed for PDF output

## Doctor policy

Always verify the environment before rendering:

- locate executables
- query versions where possible
- report missing or broken dependencies clearly

## Scope

v1 supports Windows and macOS only. Fonts are detected and reported, not bundled.
