# Elephant-Goldfish Writing

A standalone community companion for academic papers and professional documents, built in a fresh fork of Google's Elephant-Goldfish Model. It retains the context-rich writer and fresh-reader idea, with writing-specific standards and staged reader personas. This companion is maintained by the fork owner, not Google. Apache-2.0; the original software skills remain available separately.

## Install in Codex

Install from this fork's default writing branch:

```sh
codex plugin marketplace add dyannantuonojr/elephant-goldfish-writing
codex plugin add egm-writing@egm-writing-fork
```

Start a new chat/session to load the newly installed skill; existing active sessions do not need to restart. This package includes its own resources and has no upstream EGM runtime dependency or additional MCP server/API credentials. Native fresh-context delegation is required for independent Goldfish review. Other hosts can read the portable skill, but installation and orchestration outside Codex are not verified.

## Use

On the owner's configured Orca installation, open **Writing Companion** under
**elephant-goldfish-writing**, click **Start writing**, and describe your document
or attach your materials. The button is a local Orca Agent Prompt setting; a
repository clone alone does not install it.

Select **Elephant-Goldfish Writing**, or invoke `$egm-write`:

- `Use $egm-write to draft my paper using this assignment, rubric and supplied sources.`
- `Use $egm-write to review this proposal for leadership; check the decision, assumptions and next steps.`
- `Use $egm-write to revise this report after the attached feedback, preserving my voice.`
- `Use $egm-write to polish this memo; keep the edit small.`

The [skill](skills/egm-write/SKILL.md) chooses [paper](resources/paper.md) or [work-document](resources/work.md) standards. For substantial reviews the writer freezes the draft and supplies fresh readers the version, brief and actual sources. The [review contract](resources/review-contract.md) defines exact findings and honest coverage/readiness. The [staged workflow](resources/staged-workflow.md) and [pipeline policy](resources/pipeline.json) define full/deep/quick budgets and stage currency.

Drafts and source ledgers stay in the user's chosen local artifact folder. No documents are published, sent or submitted by installation or skill invocation. Unknown evidence, personal inputs and business facts remain visible; a supplier account is not independent verification. Word/PDF export uses available document tools and requires actual render inspection. This is a writing/review workflow, not a research-provider service or a compliance certification.

## Wallace and Wray and the two memory roles

Version 0.3.0 retains an [attributed Wallace and Wray adaptation](resources/wallace-wray.md) in both modes. It covers purpose-led source synopses, warranted claim strength, comparative synthesis, paragraph/block linkage, bounded conclusion and reader comprehension. Writers keep evaluations and decision history; fresh readers independently return role-specific checks grounded in actual passages. The check identifiers and budgets are companion implementation choices, not the authors' scores.

The **Elephant** is the same writer maintaining the brief, source readings, argument and decisions through revision. **Goldfish** are actual fresh-context reader agents receiving the frozen draft, brief and raw source material without that conversation or writer rationale. The execution record retains real dispatch identities and draft hashes. If independent contexts are unavailable or unproved, that limit stays explicit; self-review is not renamed Goldfish review.

This restores EGM's stage structure for writing while adapting software-specific scopes. These are host-executed skills and declarative policy, not a new autonomous runtime. Small edits remain small, and the user retains authorship and acceptance.

## Restored original stages

New substantial documents use thesis/outline challenge and section-purpose drafting. Full review runs **initial zoom-out -> comprehension paraphrase -> detailed critique -> second zoom-out -> delivery readiness**. The same Elephant resolves original findings through a provenance-preserving synthesizer; fresh readers stay independent. Keep the complete paraphrase even with no findings.

- `Use $egm-write to draft this report and run the full staged review.`
- `Use $egm-write for a full review only; do not edit my paper.`
- `Use $egm-write in deep mode to stress-test this proposal within the round cap.`
- `Use $egm-write to check drift between these revisions and their source ledgers.`

Full mode has one detailed critique/revision round and bounded targeted rechecks. Deep allows up to five critique rounds, needs two consecutive clean rounds for convergence and stops on churn. Settled discretionary findings stay settled unless evidence changes them; fixed defects can recur. Mandatory gaps never become accepted compliance. Final reporting distinguishes historical reviews, actual current-version checks and missing export evidence. Review-only and quick scopes remain honored.

## Windows test prerequisite

Running the full packaging test suite on Windows requires permission to create
real symbolic links (Developer Mode or an appropriately elevated test process).
This is a developer-test requirement, not a prerequisite for ordinary writing.
See the [fork testing guide](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/TESTING.md#windows-symlink-prerequisite)
for setup, `WinError 1314` diagnosis and exact rerun commands. Keep failures
visible until the real symlink assertions have run successfully.
