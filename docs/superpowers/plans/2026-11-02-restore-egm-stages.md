# Restore EGM Stages for Writing Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline. Preserve standalone scope and Wallace-Wray.

**Goal:** Restore the original EGM stage structure for papers and professional documents, including early challenge, section drafting, synthesis, bounded rechecks and drift review.
**Architecture:** One existing entry skill, declarative pipeline policy, staged workflow reference and four additional reader/helper personas. Host-native fresh-context dispatch remains the execution mechanism; no unrelated project integration or new research service.
**Tech Stack:** Markdown/JSON/YAML plugin resources and Python/pytest validation.
**Spec:** docs/designs/writing_companion.md, Restored EGM stages extension.

## Global Constraints

- Same Elephant writer throughout; fresh/no-history Goldfish readers.
- Keep Wallace-Wray check IDs, source limits, original reports and actual version/hash provenance.
- Preserve review-only and small-edit scope; no invented research, owner facts, approvals or rendered acceptance.
- Default full review runs five ordered stages; deep looping is bounded and optional.
- No autonomous upstream PR, document sending or submission.

## Review Focus

- Comprehension is replaced by a generic style review instead of an actual paraphrase.
- Synthesized findings lose original IDs, severity, minority objections or failed-reviewer status.
- A changed draft reuses earlier stage acceptance or a false convergence claim.
- A source-free memo is forced into scholarly/dissertation requirements.
- A readiness report certifies uninspected export or owner approval.

## Task 1: Stage package

- [x] Inventory 0.2.0 behavior and add failing package/pipeline checks.
- [x] Add pipeline policy and reference covering concept challenge, section construction and five reviews.
- [x] Add big-picture, comprehension, readiness and synthesizer personas; keep existing critique roles and Wallace-Wray.
- [x] Align entry skill, contract, README and 0.3.0 metadata; verify package closure and policy ordering.

## Task 2: Behavioral and regression verification

- [x] Exercise actual new-document flow with fresh readers, versioned artifacts, synthesis and final readiness.
- [x] Exercise read-only/drift/deep-budget boundaries without fabricating convergence.
- [x] Independently inspect package and resolve concrete defects.
- [x] Run full regressions, retain known Windows symlink limitations, commit/push/install and byte-verify 0.3.0.
