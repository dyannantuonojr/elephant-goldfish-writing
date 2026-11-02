# Restored EGM workflow for writing

Read the [pipeline policy](pipeline.json), [review contract](review-contract.md), [Wallace-Wray adaptation](wallace-wray.md) and selected [paper](paper.md) or [work](work.md) standard. The policy declares order/bounds; the host agent executes it. This is not a new autonomous runtime or a quality guarantee.

Adapted from upstream [architecture](https://github.com/google/elephant-goldfish-model/blob/main/docs/designs/architecture.md), [five-stage review](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-review/SKILL.md), [comprehension](https://github.com/google/elephant-goldfish-model/blob/main/agents/comprehension.md), [review loop](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-review-loop/SKILL.md), [synthesis](https://github.com/google/elephant-goldfish-model/blob/main/agents/synthesizer.md) and [drift](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-drift-report/SKILL.md). Translate implementation readiness to document delivery, code drift to source/requirement/argument drift. Wallace-Wray remains the reasoning standard; the owner retains authorship/acceptance.

## Route the actual request

- **New substantial document:** concept challenge, section drafting, then full five-stage review by default.
- **Existing substantial draft:** enter at full review. Do not invent completed ideation or change a sound structure just to imitate new-document work.
- **Review only:** run requested stages read-only. Save findings and preserve the draft; no automatic repair, hypothetical clean-round credit or unrequested drafting.
- **Quick edit:** no automatic swarm; label self-review truthfully. Express independent-review requests still require fresh contexts.
- **Deep:** use when the user requests deeper/iterative review or selects deep. Same five stages; bounded convergence inside critique.
- **Drift:** compare specified versions and actual ledgers without unrequested rewrite or full review.

Infer ordinary choices from materials and state the preset. Ask only for genuinely missing facts or consequential unresolved choices. Draft/revision authorization covers routine internal fixes/transitions; no compulsory approval question after each stage. Honor requested interactive checkpoints or pauses. No acceptance, publication, sending or submission is inferred.

## 0. Challenge the thesis and outline

The same Elephant reads requirements, sources, model and owner facts. Save a concept brief: purpose/question, audience, proposed answer/decision, boundaries, alternatives, evidence needs and section purposes. This is a proposal, not established truth.

Dispatch [big-picture](../agents/big-picture.md) in CONCEPT_CHALLENGE mode with the proposed brief, requirements and original sources. Challenge necessity, scope, strongest counterargument, relevance and missing backing before prose investment. Bind to the actual concept-brief hash; do not invent draft quotations. The Elephant dispositions objections and saves the working direction. Escalate only actual missing owner information or consequential choices outside authorization. Keep original brief/report versions.

## 0b. Construct sections with purpose

Record a section plan: question served, claim, support, qualification and dependency on the next block. Use genre-appropriate sections, not a universal dissertation template. The same Elephant drafts each section using Wallace-Wray source synopses and claim calibration. Preserve the owner's voice and model's useful depth without borrowing facts or experiences.

Map/revise actual sections in existing prose; do not arbitrarily fragment coherent work. Assemble and read the whole draft continuously to repair bridges, terms, cross-references and closure. Freeze an immutable version after this pass. Section drafting means neither separately authored fragments nor an approval pause after each paragraph. Save large artifacts in files with concise chat updates.

## Five ordered review stages

Each stage reads the current actual draft, freshly computes its hash and preserves original reports under `reviews/<version>/<stage>/<attempt>/`. Save immutable execution receipts with stage, round, actual task identity, context mode and hash. Never overwrite an earlier packet/report. Blind Goldfish packets exclude conversation, private writer notes, expected findings and other reports. Critique roles may run concurrently; sequential dispatch is valid when capacity is limited.

### 1. ZOOM_OUT_INITIAL

A fresh [big-picture reader](../agents/big-picture.md) checks the whole document's answer, scope, depth, credible alternatives and unnecessary/misplaced material. Map major blocks to the argument, including material exhibits/appendices. This altitude check does not replace citation critique.

The Elephant records findings. Authorized early repairs get a new version; otherwise preserve issues for critique resolution. Never claim the old report reviewed changed bytes.

### 2. COMPREHENSION

A fresh [comprehension reader](../agents/comprehension.md) reads the draft first and paraphrases its claim/proposal, reasoning, limits and expected reader action. Then it checks the brief and supporting material within declared scope, without using outside context to silently repair missing explanations.

Preserve the COMPLETE paraphrase verbatim even with no findings. The Elephant compares it with its intended argument in private notes and records substantive mismatches. Investigate misunderstandings as communication issues; private intention alone does not reject a reader's difficulty. Synthesis must not replace the paraphrase with an issue list.

### 3. CRITIQUE

Dispatch fresh [evidence](../agents/evidence.md), [argument](../agents/argument.md) and [reader](../agents/reader.md) on the same frozen version. Evidence covers support and WW-01/02; argument covers warrants, alternatives, synthesis and WW-03/04/05; reader covers requirements, audience, voice, clarity and WW-04/05/06. No sources can be legitimate for a genre, but missing required evidence remains a gap.

Give original reports to the [synthesizer](../agents/synthesizer.md), explicitly a consolidation helper rather than a blind content reviewer. It deduplicates while mapping every original finding ID to an action group, reviewer, report reference and original severity. Preserve disagreements; partial/missing readers cannot disappear or become successful. Keep all raw reports.

The same Elephant validates and dispositions each finding: FIX, REJECT_WITH_BASIS, RETAIN_GAP or ESCALATE_MISSING_INPUT. Preserve original severity and justify disagreements. Apply authorized fixes to a new whole-document version, preserving meaning/voice; check regressions and new unsupported claims. A comprehension gap cannot be dismissed solely by citing private intention.

**Full:** one critique round, resulting revision and at most one focused fresh recheck per affected stage; no convergence claim from that limited pass. **Deep:** bounded loop below. Read-only review skips repair/recheck and retains unresolved findings.

### 4. ZOOM_OUT_FINAL

A fresh big-picture reader sees the whole current draft and neutral requirements/sources, not earlier verdicts. Check whether corrections distorted the thesis, enlarged scope, created redundancy, orphaned evidence or weakened closure. This is new whole-document altitude review, not independent verification of every detailed fix. The Elephant separately compares initial/final altitude findings and records recurrence.

### 5. DELIVERY_READINESS

A fresh [readiness reader](../agents/readiness.md) checks actual requirement coverage, claim/source status, unresolved objections, citations/cross-references, audience and available exact-version export evidence. State the supported next use. A memo may support requesting an assessment while purchase remains unsupported.

For text-only delivery, assess text and mark export checks NOT_APPLICABLE only when no export is required. Required but unrendered DOCX/PDF means artifact readiness GAP. Inspect actual current rendering through available tools before claiming it checked. An old export cannot satisfy changed bytes. Readiness grants no grade, purchase authority, compliance certification, owner acceptance or sending permission.

## Changed versions and stage currency

Maintain a stage matrix: each report's version/hash and CURRENT or HISTORICAL relative to delivered bytes. Earlier reports stay historical after edits; changed sources need new source hashes. After material meaning changes in critique, run one fresh comprehension recheck before final zoom-out when the old paraphrase no longer tests the argument. It receives revised text without the expected paraphrase. Material factual fixes get a focused evidence check, labelled targeted rather than blind whole-document review.

If final zoom-out/readiness triggers repairs, save a new version and rerun affected stages within the same recheck budget. Do not restart all reviewers or add an unlimited chain. At the cap, record remaining issues and incomplete currency; seek user direction only if more work is needed beyond the authorized budget. Never claim five current-version independent reviews unless actually true. Report the checks and version scope that exist.

## Bounded deep convergence and churn

Keep raw finding IDs, source IDs and consolidated action IDs stable. Compare recurring issues by meaning and affected scope, not wording alone.

- A reasoned rejected finding or legitimately accepted discretionary risk is settled. New evidence or changed scope can reopen it.
- A FIX can recur: if the defect survives or returns, reopen it. Applied edits are not proof of resolution.
- A round is clean BEFORE its fixes only when all expected readers completed, no unsettled CRITICAL/MAJOR defects remain, and no required evidence/assignment GAP blocks it. Minor suggestions need not block. A retained mandatory gap is never an accepted discretionary risk.
- Deep convergence needs two consecutive clean rounds, capped at five critique rounds total. A missing reader is not clean; one clean round is not convergence.
- Churn means a requested fix creates an opposing objection that undoing the fix would resolve. Stop cycling and expose the tradeoff.

At convergence, cap or churn, save the real result and continue only the permitted next stage. Capped/churned work can remain REVISE; it is not automatically accepted. More rounds require user direction. A known failure allows at most one documented retry after confirming termination; unknown outcomes reconcile without duplicate launches.

## Document drift action

Read actual old/current drafts, requirements, source snapshots, dispositions and artifact identities. Compare both directions: a stronger/new claim may lack backing; a changed/withdrawn source or requirement may invalidate old prose. Check thesis/scope, support, citation parity, prior fixes, voice and dependent exhibits/cross-references. Identify unsupported additions, removed qualifications and regressions.

Return old/new hashes, changed quotations, affected requirement/source/finding IDs, and checks needing rerun. Unchanged prose is not automatically reverified evidence. Missing baseline means comparison unavailable, not invented history. Drift is read-only unless revisions are separately requested.

## Completion record

Preserve original stage reports, full comprehension paraphrase, synthesized-to-original finding map, dispositions, stage currency and scoped delivery assessment. Include skipped, partial and unavailable work. Link the delivered artifact, substantive changes and remaining limits. Reasoning and actual evidence establish quality; stage count and reviewer agreement do not.
