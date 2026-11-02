# Writing Companion Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan inline. Steps use checkbox syntax for tracking.

**Goal:** Deliver and locally install the standalone writing companion in the owner's fresh EGM fork.

**Architecture:** Nested independent plugin, one writing skill, three reusable reader personas and paper/work standards. A distinct fork marketplace preserves the original plugin.

**Tech Stack:** Markdown, JSON, YAML, Python/pytest packaging checks; native Codex plugin installation.

**Spec:** docs/designs/writing_companion.md

## Global Constraints

- No other project integration or production document changes.
- Preserve the original seven EGM software skills.
- Reviewer independence, source access and readiness must be truthful.
- No autonomous upstream pull request or document publication.

## Review Focus

- Source URLs mistaken for inspected evidence.
- An invented personal reflection or private business fact.
- A reviewer without fresh context labelled independent.
- A polished memo with unsupported cost or integration assumptions.
- A package whose relative references break after installation.

## Task 1: Companion package and discovery

Files: writing-companion/plugin.json, writing-companion/.codex-plugin/plugin.json, writing-companion/skills/egm-write/, writing-companion/agents/, writing-companion/resources/, root marketplace, README.
Consumes: selected design and original plugin packaging format. Produces: complete self-contained plugin.

- [x] Write packaging tests; run and observe missing-package failures.
- [x] Add the skill, paper/work standards, reviewer personas and installation guide.
- [x] Extend the fork marketplace and its tests without modifying original skills.
- [x] Run companion tests and skill validation.

## Task 2: Behavioral and installation validation

Files: tests/writing/validation.md and synthetic scenarios.
Consumes: complete package. Produces: tested installation and honest limits.

- [x] Record ordinary-assistant baseline on synthetic paper and memo tasks.
- [x] Run fresh-context companion scenarios; inspect reports and recheck failures.
- [x] Run upstream suite; distinguish existing platform failures from regressions.
- [ ] Commit and push the feature branch to the requested fork, then install that branch's companion.
- [ ] Verify installed resources and report invocation to the owner.
