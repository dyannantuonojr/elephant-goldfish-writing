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
