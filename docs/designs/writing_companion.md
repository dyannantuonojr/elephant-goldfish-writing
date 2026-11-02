# Standalone writing companion

Approved direction: a separate papers/work-documents companion in a fresh EGM fork, with no other workflow integration. Owner authorization: build it and report on completion.

## Goals

Create an independently installable `egm-writing` plugin. One `egm-write` skill accepts draft, review and revision requests for academic papers and professional documents. The writer holds context; isolated readers receive the exact draft, requirements and source materials. Preserve source uncertainty and the user's voice. Produce traceable findings and bounded revisions without repeated routine approval questions.

## Non-goals

No integration with other projects, research services, account credentials or production papers. No automatic publication, submission, fabricated research or personal experience. Do not replace upstream software skills or promise native Word/PDF rendering from prompt files.

## Approaches

The owner selected a separate companion over editing upstream EGM. A nested package keeps its own identity, reviewers and writing standards, while the original seven software skills remain unchanged. The fork marketplace exposes both packages with a distinct marketplace name to coexist with the original installation.

## Behavior

Infer paper/work mode from the request and supplied documents. Build a brief from available facts; ask only for missing information that changes the document. Keep drafts versioned. Paper readers check assignment coverage, evidence and argument. Work readers check audience, decision, assumptions, feasibility and clarity. Both inspect actual adjacent paragraph links and conclusion closure. Reviewers read supplied source bytes; a bibliography or URL alone is not source verification. Review reports distinguish complete, partial and not-run reviewers; readiness is scoped to available evidence and actual output checks.

Default to one review, one writer revision and a focused recheck of material fixes. Do not seek an endless zero-findings convergence. The user may request more. Fresh-context review is optional for small ordinary edits; if unavailable, label self-review honestly. Formatting uses an available document/PDF tool and actual render checks. Test with synthetic inputs only.

## Validation

Check independent plugin installation, bundled references, metadata, source/claim traceability, fresh-context behavior and upstream regressions. Exercise unsupported evidence, personal-input gaps, missing budget assumptions and review-unavailable cases. Record actual limits rather than invent a passing baseline.

## Wallace and Wray extension

The owner requested Wallace and Wray writing standards and an audit of Elephant/Goldfish behavior. Implement a bundled, source-attributed adaptation in both modes rather than relying on the model to remember the book. The writer records purpose-led source evaluations, a synthesis position and claim boundaries. Fresh readers independently inspect the original source material and return explicit role-scoped reasoning checks, passage evidence and gaps. Durable writer context remains with the writer; it is not copied into blind reviewer contexts. Existing brief, source and scope limits still govern.

Concepts are grounded in the authors' actual book/excerpt and linked to publisher resources; do not redistribute source text or claim verification of the latest edition. The companion's check IDs, status values, evidence fields and one-review budget are local implementation choices. No formula, score, reviewer count or dissertation section layout is attributed to Wallace and Wray.
