# Elephant-Goldfish Writing

A standalone community companion for academic papers and professional documents, built in a fresh fork of Google's Elephant-Goldfish Model. It retains the context-rich writer and fresh-reader idea, with writing-specific standards and three reader personas. This companion is maintained by the fork owner, not Google. Apache-2.0; the original software skills remain available separately.

## Install in Codex

Install from this fork's feature branch:

```sh
codex plugin marketplace add dyannantuonojr/elephant-goldfish-writing --ref feat/writing-companion
codex plugin add egm-writing@egm-writing-fork
```

Start a new chat/session to load the newly installed skill; existing active sessions do not need to restart. This package includes its own resources and has no upstream EGM runtime dependency or additional MCP server/API credentials. Native fresh-context delegation is required for independent Goldfish review. Other hosts can read the portable skill, but installation and orchestration outside Codex are not verified.

## Use

Select **Elephant-Goldfish Writing**, or invoke `$egm-write`:

- `Use $egm-write to draft my paper using this assignment, rubric and supplied sources.`
- `Use $egm-write to review this proposal for leadership; check the decision, assumptions and next steps.`
- `Use $egm-write to revise this report after the attached feedback, preserving my voice.`
- `Use $egm-write to polish this memo; keep the edit small.`

The [skill](skills/egm-write/SKILL.md) chooses [paper](resources/paper.md) or [work-document](resources/work.md) standards. For substantial reviews the writer freezes the draft and supplies fresh readers the version, brief and actual sources. The [review contract](resources/review-contract.md) defines exact findings and honest coverage/readiness. One review, one revision and a focused material-fix recheck are the default budget, not an endless loop.

Drafts and source ledgers stay in the user's chosen local artifact folder. No documents are published, sent or submitted by installation or skill invocation. Unknown evidence, personal inputs and business facts remain visible; a supplier account is not independent verification. Word/PDF export uses available document tools and requires actual render inspection. This is a writing/review workflow, not a research-provider service or a compliance certification.
