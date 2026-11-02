# Elephant-Goldfish Writing

**Write papers and work documents with a writer that remembers and reviewers that read with fresh eyes.**

This is a community writing fork of [Google's Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model). It adapts EGM for academic papers, reports, memos, proposals and other professional documents, with an attributed adaptation of Wallace and Wray's critical reading and writing principles. It is maintained independently by the fork owner and is not an officially supported Google product.

## Start writing

### In Orca

On the owner's configured Orca installation:

1. Open the **Writing Companion** workspace under **elephant-goldfish-writing**.
2. Click **Start writing** at the top of the workspace.
3. Say what you want to write and attach your instructions, sources, examples or draft.

The saved Agent Prompt invokes the writing skill in Codex. It is an Orca setting on that computer; cloning this repository does not automatically create the button. On another Orca installation, add a project-scoped Quick Command with action **Agent Prompt**, agent **Codex**, and prompt `$egm-write Help me write or revise a paper or work document.` after installing the plugin below.

### In Codex

Install the writing companion from this fork:

```sh
codex plugin marketplace add dyannantuonojr/elephant-goldfish-writing
codex plugin add egm-writing@egm-writing-fork
```

Start a new chat/session after installation. Select **Elephant-Goldfish Writing** from the skill picker, or type:

```text
$egm-write Help me write this paper using my assignment and sources.
```

For a work document:

```text
$egm-write Review and revise this report for leadership.
```

Supply whatever you already have: the task or assignment, rubric, audience, sources, examples, feedback and an existing draft. You do not need a long setup prompt. Continue in the same writing chat so decisions and revision history remain available.

**Windows Developer Mode is not required to use the companion.** Some developer packaging tests require real symlink permissions; see [the testing prerequisite](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/TESTING.md#windows-symlink-prerequisite).

## How it works

- **Elephant:** one persistent writer keeps the brief, source evaluations, argument, your voice and revision decisions.
- **Goldfish:** fresh-context readers inspect the actual draft, requirements and original sources without the writer's earlier conversation or private rationale.
- **You:** supply your goals and private facts, resolve consequential choices and decide whether to accept or use the document.

For a new substantial document, the writer challenges the proposed thesis and outline, drafts purpose-led sections, and assembles a connected whole. Full review then follows five ordered stages:

1. **Initial zoom-out:** does the document answer the right question at the right scope?
2. **Comprehension:** can a fresh reader accurately paraphrase the claim, reasoning, limits and next action?
3. **Detailed critique:** independent evidence, argument and reader checks, followed by synthesis that preserves every original finding and disagreement.
4. **Second zoom-out:** do the revisions still develop one coherent argument?
5. **Delivery readiness:** what does the actual document support, and what remains missing or unverified?

The same writer resolves findings and makes authorized revisions. Original reports, complete paraphrases, draft versions, source ledgers and review scope are preserved. Historical reviews are not relabelled as reviews of changed text.

## Choose the scope

| Ask for | What happens |
| --- | --- |
| **Full** | Default for substantial work: all five stages, one detailed critique/revision round and bounded focused rechecks. |
| **Review only** | Findings and review records; your draft is not rewritten. |
| **Quick edit** | A small requested edit stays small, with self-review labelled honestly. |
| **Deep** | Up to five critique rounds; convergence requires two consecutive clean rounds, and opposing-fix churn stops the loop. |
| **Drift check** | Compare actual revisions and source/requirement changes for unsupported additions, lost qualifications and regressions. |

Existing drafts enter at review rather than pretending ideation already happened. Use ordinary language, for example `$egm-write Quick edit: make this memo clearer.`

## Wallace and Wray throughout

The writing standards cover source purpose and quality, strength of backing, comparison and synthesis, paragraph connections, the whole argument and conclusions that stay within the evidence. Actual passages and reasoning support judgments; transition-word counts and reviewer agreement do not establish quality.

This is an [attributed adaptation](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/writing-companion/resources/wallace-wray.md), not an official Wallace-Wray scoring system. A supplied model can guide structure and depth; it does not verify facts or supply personal experience.

## Capabilities and limits

The companion is a host-executed skill package, not a standalone word processor or a new autonomous agent runtime. Independent Goldfish reviews require a host that can create actual fresh subagent contexts. If unavailable, independent review is reported as not run; self-review is not presented as independent agreement.

The writing package adds no research-provider service, MCP server or separate API credentials. It does not invent sources, citations, private facts or owner answers. Word/PDF output uses available document tools; rendered acceptance requires inspection of the exact output. Writing/review completion is separate from a grade, owner acceptance, business authority or permission to publish, send or submit.

Installation and workflow trials were exercised in Codex. Other hosts can read the portable resources, but their writing-companion installation and orchestration are not verified. This standalone fork has no 2JZ80 dependency.

## Package and documentation

- [Writing companion package and detailed usage](https://github.com/dyannantuonojr/elephant-goldfish-writing/tree/feat/writing-companion/writing-companion)
- [Staged workflow and revision rules](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/writing-companion/resources/staged-workflow.md)
- [Implementation and validation record](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/tests/writing/stages-validation.md)
- [Fork testing guide](https://github.com/dyannantuonojr/elephant-goldfish-writing/blob/feat/writing-companion/TESTING.md)

The marketplace exposes two distinct plugins: **egm-writing** is this writing companion; **egm** retains the original software-design workflow. The upstream software skills, documentation and attribution remain available. For that original workflow, see the [software getting-started guide](docs/getting_started.md) and [upstream project](https://github.com/google/elephant-goldfish-model).

## License

[Apache 2.0](LICENSE). Original EGM work is credited to its upstream contributors; writing-companion additions are maintained in this fork.
