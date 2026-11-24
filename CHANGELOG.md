# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2026-11-23

First release since 0.1.2 (2017).

### Changed
- The length parameter is now `duration`. `len` still works as a deprecated
  keyword alias and emits a `DeprecationWarning`; positional calls are
  unchanged.
- Requires Python 3.10 or later (tested on 3.10–3.14) and NumPy 1.24 or later.
- Source moved to a `src/` layout with type hints; the package is marked
  typed.

### Removed
- Python 2 support.

[Unreleased]: https://github.com/lijunzh/ricker/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/lijunzh/ricker/compare/v0.1.2...v0.2.0
