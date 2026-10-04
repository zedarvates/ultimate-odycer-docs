# Foundry Controlled Improvement & Promotion

Status: DECIDED governance direction / EXPERIMENTAL implementation.

## Purpose
Allow skills/tools/workflows/pipelines and routing candidates to improve through measured experiments without allowing a candidate to redefine its own success criteria, weaken its safeguards or promote itself.

## Lifecycle
CANDIDATE -> BENCHMARKED -> REVIEW_READY -> APPROVED/REJECTED -> ADOPTED -> optional ROLLED_BACK.

## Baseline
Improvement claims require an exact comparable baseline: versions, workload/dataset, metrics, environment and evidence. Material benchmark changes invalidate direct claims until reconciled.

## Multidimensional evidence
Compare quality, high-confidence errors, abstention, latency, cost/compute, maintenance and relevant consequence metrics. No universal weighted score and no cheapest/fastest automatic winner.

## Separation of duties
Safety/authority/autonomy policy changes require distinct proposer and approver. Agents may prepare policy diffs/tests; they may not self-approve weakened controls.

## Adoption
Prefer shadow/canary mode where applicable. Record previous version, compatibility/migration, rollback and affected scopes. Non-rollbackable adoption is explicitly high consequence.

## Post-adoption
Measure real behavior after adoption. Benchmark evidence does not guarantee production-equivalent behavior; drift/regression reopens review and may trigger rollback proposal.

## Human role
Architectural, policy and consequential trade-offs remain human-arbitrated through Decision Briefs.
