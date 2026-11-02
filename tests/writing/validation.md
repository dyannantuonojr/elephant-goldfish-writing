# Writing companion validation

## Baseline before implementation

Upstream full suite: 233 passed, 10 failed on this Windows host before companion implementation. All 10 failures are existing packaging symlink cases that encounter WinError 1314 (symlink creation privilege unavailable): test_rejects_symlinked_runtime_paths (2), test_rejects_dangling_output_symlinks (4), test_archive_claimed_after_preflight_is_not_overwritten with dangling-symlink/symlink (4). No upstream runtime code was changed to hide these failures.

Four new package checks were run before the package existed: all four failed on absent manifests/skill/resources or the original catalog identity. After implementation they passed; the targeted companion/harness/link run passed 28 tests and the Skill Creator validator accepted the skill.

A fresh ordinary-assistant baseline on a synthetic paper and procurement memo already rejected fabricated personal reflection, unsupported universal profit claims and invented cash savings. It calculated $19,200 licenses/year and 520 hours/year correctly. No integrity failure or measured performance improvement is claimed from that baseline. The companion's added value is a reusable writing-specific packet, isolated readers, artifact identity, coverage and bounded resolution, rather than claiming ordinary models cannot reason about evidence.

## Behavioral scenarios

The fixtures under fixtures/ contain intentionally defective synthetic documents and supplied evidence. Fresh-context evaluations and observed results are recorded below after execution. No production paper, private business source or external provider is used.

## Packaging repair

The first full post-change run exposed three new failures: two upstream ZIP link checks and the published Claude runtime freshness check. Cause: the fork README linked to a separately installed companion using a relative path that is deliberately absent from upstream runtime archives. Replaced that link with its absolute fork URL and synchronized the published runtime README; no runtime code or tests were weakened.

## Observed paper workflow

Actual evaluator /root/paper_trial read the installed-shape skill and invoked three no-history child readers (evidence, argument, reader). All returned COMPLETE for their accessible review scope and the exact unchanged draft SHA in paper-trial.json. They identified the planted handling-time/profit distortion, invented personal reflection, removal of human review and unmet scholarly/assignment requirements. The evaluator honored review-only and made no draft changes or provider calls. Missing source text and formatting remained gaps; COMPLETE did not become submission approval. This was an actual three-reader orchestration trial, not a simulated agreement.

## Observed unavailable-delegation behavior

A separate fresh evaluator was given a host constraint with no delegation tool. It returned independent review NOT_RUN, readiness UNDETERMINED and labelled any possible author review SELF_REVIEW. It did not simulate reviewer agreement. This tests the instruction's constrained-host response; it is not evidence that the current host lacks delegation.

## Regression outcome

After the README repair: full pytest reported 237 passed and the same 10 pre-existing Windows symlink privilege failures. The separate `pytest -k 'not symlink'` run reported 237 passed, 10 deselected. Skill metadata validation passed. No upstream test failure was relabelled a pass.

## Observed work-document evidence review

Actual fresh reader /root/work_trial returned COMPLETE for its accessible scope, REVISE readiness, five major findings and a ten-entry support map bound to the actual draft hash in work-trial.json. It distinguished capacity from cash, calculated $1,600/month and $19,200/year licenses, retained the ten-hours-per-week whole-team scope, and flagged integration, owner and timing assertions. The author then saved a separate synthetic v002 and finding-by-finding dispositions for a focused fresh recheck; v001 was preserved. This is an evidence-reader trial, not a claimed three-reader work-document audit.

## Focused revision recheck and package review

Fresh rechecker /root/work_recheck inspected actual v002 bytes and all five dispositions, confirmed the three calculations and preserved unknown facts. It returned no new findings and READY_WITHIN_REVIEWED_SCOPE for that focused check; this is not purchase approval or full-document/format acceptance. Its actual hash and scope are in work-recheck.json.

Independent read-only package reviewer /root/companion_review found no concrete Critical, Important or Minor defects in actual package files and references. Its Git diff access was unavailable in the sandbox, so the author separately inspected the exact tracked diff. The reviewer did not independently verify native installation, remote availability, render acceptance or test-provenance claims. The author's final diff check passed.

## Native installation acceptance

Created the fresh GitHub fork, committed package changes in 5dc8533 and pushed feat/writing-companion without opening a pull request or merging upstream. Native Codex CLI registered egm-writing-fork and installed egm-writing@egm-writing-fork 0.1.0. Its list result confirmed installed=true and enabled=true. All 14 package files in the actual installed cache match the source bytes; full installer receipt summary is in installation.json. A new chat/session is needed to load the skill; no unrelated active session was restarted. End-to-end skill behavior was exercised through actual fresh readers using these exact package contents; no rendered Word/PDF export is claimed.

## Version 0.2.0: Wallace and Wray extension

The authors' inspected concepts and exact source/access limits are recorded in wallace-wray-source-basis.json. The standard is an attributed adaptation, not a copyrighted template copy or an official numeric scoring scheme. The old companion already caught overclaims in the pre-change control; the control omitted explicit ww_review and source_synopses fields. No measured writing-quality improvement is inferred.

Two changed bundle/version assertions failed before implementation (missing standard and 0.1.0 rather than 0.2.0). After implementation, targeted package/harness/link checks passed 29 tests, including reachability of the standard from the skill and all readers. The full suite before the new reachability test retained exactly the existing ten WinError 1314 symlink failures and 237 passes; the final runnable suite including the new test passed 238 tests, with those ten cases deselected.

Independent extension reviewer /root/ww_change_review found no Important defects and one Minor ambiguity: argument/shared instructions unconditionally demanded neighboring paragraphs. The author verified and fixed that inconsistency, then /root/ww_short_document correctly marked adjacency and source comparison NOT_APPLICABLE for a single-paragraph source-free internal request while still checking block purpose and closure. No fake paragraph or academic structure was imposed. This behavior trial does not prove all possible documents behave correctly.

## Actual Elephant/Goldfish trial for 0.2.0

Persistent writer /root/ww_workflow read the synthetic writer-only note and retained it across the review. Actual children ww_evidence, ww_argument and ww_reader were spawned with fork_turns=none; the exact prompts excluded writer notes, its canary, prior findings and expected judgments. Each received only persona/standards and the actual brief/draft/source records, and returned COMPLETE with the same pre/post-verified unchanged draft SHA. The writer honored review-only and performed no revision or provider call. A rejected capacity-only spawn produced no accepted task and was not treated as a completed review.

The evidence reader returned independent five-dimension synopses for A/B and WW-01/02; argument returned WW-03/04/05; reader returned WW-04/05/06, all REPAIR with actual passage reasoning. They distinguished self-report from causal identification, purpose/design/context and mixed time/accuracy outcomes, and rejected unsupported profit/generalization/rollout closure. Exact dispatch arguments, identities, check-status summaries and source synopses are retained in wallace-wray-workflow.json. These observations support actual context separation at the dispatch/packet level; prompt instructions are not a new runtime isolation mechanism or a universal quality guarantee.
