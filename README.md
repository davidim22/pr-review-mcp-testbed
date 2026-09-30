# pr-review-mcp-testbed

A sandbox repo for testing an MCP server that reviews pull requests.

## Layout

```
src/calculator/     # package source
tests/              # test suite (added in a later PR)
```

## Purpose

This repo exists to provide realistic, varied pull requests (clean, buggy,
and mixed-quality) so PR review tooling can be exercised against them. It
is not meant to be a real calculator library — the "enterprise" structure
(package layout, tests, CI, config, docs) is intentionally over-built for
what the code actually does.
