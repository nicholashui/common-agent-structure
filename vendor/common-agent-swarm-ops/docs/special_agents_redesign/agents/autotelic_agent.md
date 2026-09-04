# Autotelic Agent v2

**Filename**: `autotelic_agent.v2.md`  
**Version**: 2.0  
**Date**: 2026-07-21  
**Status**: Safety-Oriented Architecture Specification  
**Supersedes**: `autotelic_agent.md` v1.0  

---

## 0. Executive Summary

An **Autotelic Agent** is an intrinsically motivated AI system that can autonomously represent, generate, select, pursue, evaluate, and master goals.

Version 2 introduces a critical qualification:

> The agent may autonomously think, propose, simulate, and learn more broadly than it may act.

Autonomy operates inside a **Governance Envelope** containing externally enforced policies, permissions, resource budgets, risk limits, approval requirements, and termination conditions.

The agent's intrinsic motivations—learning progress, information gain, novelty, competence growth, and skill transfer—control how it allocates learning effort. They do not override safety constraints or independently authorize real-world actions.

The architecture separates:

1. **Human Governance** — defines authority, mission, and acceptable risk.
2. **External Safety and Control Plane** — enforces policy and capabilities.
3. **Autotelic Cognitive Plane** — generates goals, plans, learns, and reflects.
4. **Sandboxed Execution Plane** — performs bounded actions through controlled tools.
5. **Evaluation and Deployment Plane** — independently tests changes and controls adoption.
6. **Evidence and Memory Plane** — preserves provenance, evaluations, and audit history.

Self-improvement is **proposal-based rather than unrestricted self-modification**. The cognitive agent may develop candidate changes, but protected components—including the safety kernel, policy engine, capability broker, audit system, and deployment authority—remain outside its modification boundary.

This specification is a research and engineering architecture. It does not claim to solve value alignment, corrigibility, deceptive alignment, or safe recursive self-improvement in the general case.

---

## 1. Definition

A **Bounded Autotelic Agent** is an AI system that, within delegated authority, can:

- Detect problems, opportunities, uncertainty, and capability gaps
- Generate and decompose candidate goals
- Evaluate goals for mission relevance, feasibility, risk, and expected learning
- Select a portfolio of goals at the frontier of competence
- Plan and execute authorized actions
- Evaluate outcomes using independent evidence
- Relabel trajectories with valid hindsight achievements
- Accumulate reusable and tested skills
- Detect errors, regressions, plateaus, and anomalies
- Propose improvements to its prompts, tools, memory, policies, and runtime
- Test candidate improvements in isolated environments
- Request deployment through an external approval mechanism
- Pause, defer, or terminate when authority or confidence is insufficient

### 1.1 Cognitive Autonomy vs. Operational Authority

**Cognitive autonomy** includes:

- Generating hypotheses and goals
- Running simulations
- Producing plans
- Performing local analysis
- Learning from authorized observations
- Proposing changes

**Operational authority** includes:

- Accessing data
- Calling tools
- Modifying external state
- Spending resources
- Communicating with third parties
- Deploying code
- Changing permissions
- Persisting processes

Operational authority is always narrower, revocable, time-bounded, and externally enforced.

### 1.2 Conceptual Objective

Candidate goals are first subjected to hard admissibility constraints. Only admissible goals may be ranked.

A conceptual ranking function is:

```text
GoalScore(g) =
    MissionValue(g)
  + α · LearningProgress(g)
  + β · InformationGain(g)
  + γ · TransferPotential(g)
  + δ · PortfolioDiversity(g)
  + ε · Urgency(g)
  - λ · ExpectedRisk(g)
  - μ · ResourceCost(g)
  - ν · Irreversibility(g)
  - ξ · UncertaintyPenalty(g)
```

Subject to:

```text
PolicyAllows(g) = true
PermissionsSufficient(g) = true
BudgetAvailable(g) = true
EvaluationDefined(g) = true
TerminationDefined(g) = true
```

This score is a scheduling aid, not a proof of alignment. Hard constraints always dominate soft preferences.

### 1.3 Non-Goals

Version 2 does not authorize or assume:

- Unbounded or indefinite unsupervised operation
- Direct modification of safety or governance controls
- Autonomous expansion of permissions
- Unauthorized credential acquisition
- Self-replication or covert persistence
- Removal or weakening of monitoring
- Treating a single prose objective as a complete value specification
- Treating self-evaluation as sufficient evidence of success
- Treating archive growth alone as evidence of useful learning
- Assuming language-model reflection is inherently reliable
- Assuming that CEV, flourishing, truth-seeking, or morality are directly executable objectives without operationalization

---

## 2. Design Principles

### 2.1 Bounded Autonomy

Every deployment operates under an **Autonomy Lease** defining:

- Permitted environments
- Available capabilities
- Resource limits
- Data-access limits
- Maximum action risk
- Approval requirements
- Check-in frequency
- Expiration time
- Termination behavior

No lease means no external action authority.

### 2.2 Externalized Control

Critical controls exist outside the agent's self-modifiable runtime:

- Stop and pause mechanisms
- Policy enforcement
- Capability issuance
- Credential management
- Resource accounting
- Audit logging
- Evaluation thresholds
- Deployment signing
- Rollback authority

### 2.3 Defense in Depth

No single model, prompt, classifier, evaluator, or policy rule is treated as sufficient. Safety is implemented through overlapping technical and procedural controls.

### 2.4 Hard Constraints Before Optimization

The system first determines what is permitted. It then optimizes among permitted alternatives.

Intrinsic motivation cannot compensate for a policy violation.

### 2.5 Least Privilege

The agent receives only the capabilities required for the current authorized action. Credentials should be:

- Scoped
- Short-lived
- Non-exportable where possible
- Rate-limited
- Revocable
- Bound to a goal and action class

### 2.6 Reversibility by Default

The agent should prefer:

1. Analysis over action
2. Simulation over deployment
3. Read-only access over write access
4. Local changes over external changes
5. Reversible changes over irreversible changes
6. Canary deployment over global deployment

### 2.7 Independent Evaluation

Goal generators and executors must not be the sole judges of their own success. Evaluation should use independent tests, environments, models, deterministic checks, or human review.

### 2.8 Provenance by Default

Goals, memories, skills, actions, evaluations, and modifications must record their origin, evidence, version, confidence, and applicable policy context.

### 2.9 Calibrated Uncertainty and Deference

The agent must represent uncertainty explicitly and defer when:

- Requirements are ambiguous
- Stakeholder preferences conflict
- Risk is high
- The action is difficult to reverse
- Policy interpretation is uncertain
- Required evidence is unavailable

### 2.10 Graceful Failure

Failures in policy, supervision, evaluation, memory integrity, or resource accounting cause reduced authority or a safe stop—not unrestricted fallback behavior.

---

## 3. Authority Hierarchy and Governance Envelope

The system follows this authority hierarchy, from highest to lowest:

1. **Platform Safety Invariants**
2. **Applicable Law and Organizational Policy**
3. **Human-Signed Constitution and Prohibitions**
4. **Delegated Mission**
5. **Project and Task Objectives**
6. **Self-Generated Goals**
7. **Intrinsic Motivation and Scheduling Preferences**

A lower-level objective cannot reinterpret, disable, or override a higher-level authority.

### 3.1 Governance Envelope

The Governance Envelope consists of:

```yaml
governance_envelope:
  constitution_version: string
  mission_version: string
  authorized_stakeholders: []
  decision_rights: {}
  prohibited_outcomes: []
  required_behaviors: []
  applicable_policies: []
  permitted_environments: []
  capability_manifest: []
  data_access_policy: {}
  risk_budget: {}
  resource_budget: {}
  approval_matrix: {}
  uncertainty_policy: {}
  escalation_policy: {}
  autonomy_lease: {}
  review_schedule: {}
  emergency_stop_channels: []
```

### 3.2 Mission Package

A high-level basic goal must be converted into an operational **Mission Package**:

```yaml
mission:
  statement: string
  stakeholders: []
  desired_outcomes: []
  protected_values: []
  prohibited_methods: []
  non_goals: []
  measurable_indicators: []
  known_ambiguities: []
  conflict_resolution_rules: []
  acceptable_risk: {}
  human_decision_points: []
  review_interval: duration
```

Concepts such as CEV, human flourishing, moral rightness, or truth-seeking are mission templates—not sufficient production policies by themselves.

---

## 4. System Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│                     Human Governance Layer                       │
│ Mission • Constitution • Permissions • Reviews • Stop Authority │
└──────────────────────────────┬───────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────┐
│              External Safety and Control Plane                   │
│                                                                  │
│ Policy Engine     Capability Broker     Resource Governor        │
│ Approval Service  Credential Vault      Supervisor / Watchdog    │
│ Audit Log         Tripwires             Stop / Rollback Control  │
│                                                                  │
│              Not modifiable by the cognitive agent               │
└──────────────────────────────┬───────────────────────────────────┘
                               │ Authorized requests only
┌──────────────────────────────▼───────────────────────────────────┐
│                   Autotelic Cognitive Plane                      │
│                                                                  │
│ Situation Model       Goal Generator       Goal Admission        │
│ Portfolio Scheduler   Planner / Executor   Progress Estimator    │
│ Evaluator Interface   Reflection           Hindsight Relabeler   │
│ Memory Interface      Skill Composer       Improvement Proposer  │
└──────────────────────────────┬───────────────────────────────────┘
                               │ Capability-mediated actions
┌──────────────────────────────▼───────────────────────────────────┐
│                    Sandboxed Execution Plane                     │
│ Isolated Tools • Simulators • Test Environments • Bounded APIs   │
└──────────────────────────────┬───────────────────────────────────┘
                               │ Candidate artifacts and evidence
┌──────────────────────────────▼───────────────────────────────────┐
│                Evaluation and Deployment Plane                   │
│ Independent Tests • Red Teaming • Canary • Signing • Rollback   │
└──────────────────────────────┬───────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────┐
│                    Evidence and Memory Plane                     │
│ Goal Archive • Skill Registry • Provenance • Metrics • Events   │
└──────────────────────────────────────────────────────────────────┘
```

### 4.1 Trust Boundaries

| Boundary | Components | Agent Modification Rights |
|---|---|---|
| **T0** | Human governance, platform ownership, emergency stop | None |
| **T1** | Safety kernel, policy engine, broker, credentials, audit | None |
| **T2** | Evaluators, deployment service, protected test suites | Proposal only |
| **T3** | Cognitive runtime, prompts, routing, planners, memory logic | Candidate changes in sandbox |
| **T4** | Tools, external systems, retrieved content, environments | Treated as untrusted |

The agent cannot directly move components from a lower-trust boundary into a higher-trust boundary.

---

## 5. Core Data Contracts

### 5.1 Goal Contract

Every goal must be represented by a structured contract.

```yaml
goal:
  goal_id: uuid
  version: integer
  parent_goal_id: uuid | null
  title: string
  description: string

  rationale:
    mission_links: []
    observed_need: string
    expected_benefit: string

  success:
    criteria: []
    evaluator_ids: []
    minimum_evidence: []
    confidence_threshold: number

  boundaries:
    non_goals: []
    prohibited_methods: []
    allowed_environments: []
    required_capabilities: []
    data_classifications: []

  execution:
    dependencies: []
    estimated_cost: {}
    resource_budget: {}
    time_budget: duration
    autonomy_lease_id: uuid
    risk_tier: A0 | A1 | A2 | A3 | A4
    reversibility: full | partial | none

  termination:
    completion_conditions: []
    failure_conditions: []
    pause_conditions: []
    escalation_conditions: []

  evaluation:
    baseline: {}
    held_out_tests: []
    contamination_controls: []
    evaluation_frequency: duration

  governance:
    policy_basis: []
    required_approvals: []
    approval_tokens: []
    owner: string

  provenance:
    generated_by: string
    source_events: []
    created_at: timestamp
    confidence: number

  status: proposed | screened | authorized | scheduled | active |
          paused | completed | failed | rejected | archived
```

A free-form natural-language goal without this contract cannot become an active operational goal.

### 5.2 Skill Record

```yaml
skill:
  skill_id: uuid
  version: integer
  name: string
  description: string
  applicable_goals: []
  preconditions: []
  postconditions: []
  required_capabilities: []
  risk_tier: A0 | A1 | A2 | A3
  implementation_ref: string
  test_suite_ref: string
  evaluation_history: []
  success_distribution: {}
  known_failure_modes: []
  provenance: {}
  dependencies: []
  expiration_or_review_date: timestamp
  status: experimental | validated | deprecated | revoked
```

A skill is considered mastered only after external evaluation, not because the agent claims mastery.

### 5.3 Action Request

```yaml
action_request:
  action_id: uuid
  goal_id: uuid
  plan_step_id: uuid
  tool: string
  operation: string
  arguments_hash: string
  intended_effect: string
  expected_result: string
  required_capabilities: []
  data_classification: string
  estimated_cost: {}
  risk_tier: A0 | A1 | A2 | A3 | A4
  reversibility: full | partial | none
  rollback_plan: string | null
  approval_token: string | null
  idempotency_key: string
```

### 5.4 Change Proposal

```yaml
change_proposal:
  change_id: uuid
  proposer_version: string
  target_component: string
  change_class: C0 | C1 | C2 | C3 | C4
  observed_problem: string
  evidence: []
  causal_hypothesis: string
  proposed_patch_ref: string
  expected_improvement: {}
  protected_invariants: []
  test_plan: []
  adversarial_tests: []
  migration_plan: string
  rollback_plan: string
  requested_approval: string
  status: proposed | testing | rejected | approved |
          canary | deployed | rolled_back
```

---

## 6. Core Modules

### 6.1 External Supervisor

The Supervisor is outside the cognitive agent and:

- Issues and expires autonomy leases
- Processes pause and stop signals
- Monitors health, budgets, and policy events
- Revokes capabilities
- Requires periodic heartbeats
- Detects missing logs or abnormal activity
- Forces checkpointing and termination
- Coordinates rollback

If the Supervisor cannot be reached, external action authority expires or fails closed.

### 6.2 Policy Engine

The Policy Engine evaluates goals, plans, and actions against:

- Governance hierarchy
- Risk tier
- Capability scope
- Data policy
- Resource budgets
- Approval requirements
- Environmental restrictions
- Prohibited outcomes and methods

Deterministic checks should be used wherever possible. Model-based policy interpretation may supplement but must not be the sole control for high-risk actions.

### 6.3 Capability Broker

All tool use passes through the Capability Broker.

The broker:

- Issues short-lived capability tokens
- Validates goal and action bindings
- Restricts tool operations and arguments
- Applies rate, cost, and data limits
- Prevents credential export
- Records requests and outcomes
- Supports immediate revocation

The cognitive runtime does not directly hold unrestricted credentials.

### 6.4 Situation and Opportunity Model

This module maintains a bounded model of:

- Current environment state
- Active goals and commitments
- Stakeholder requests
- Errors and anomalies
- Unresolved uncertainties
- Capability gaps
- Resource constraints
- External changes relevant to the mission

Observations are tagged with source, trust level, timestamp, and confidence.

Retrieved or externally supplied content is treated as data, not as authority or executable instruction.

### 6.5 Goal Generator and Decomposer

The Goal Generator proposes candidate goals using:

- Governance Envelope
- Mission Package
- Current situation
- Goal Archive
- Skill Library
- Learning-progress map
- Uncertainty map
- Unresolved failures
- Resource and risk budgets

For each candidate, it should produce:

- Goal Contract
- Mission traceability
- Success and termination criteria
- Two to five subgoals where appropriate
- Required capabilities
- Risk and reversibility estimate
- Expected learning or mission value
- Evaluation plan
- Alternative lower-risk approaches

Goal diversity should be encouraged, but novelty alone is never sufficient for admission.

### 6.6 Goal Admission Controller

Before scheduling, each candidate is checked for:

1. Mission traceability
2. Policy compliance
3. Clear success criteria
4. Clear stop and failure conditions
5. Feasibility
6. Required permissions
7. Risk and reversibility
8. Evaluator availability
9. Resource availability
10. Duplication or conflict with active goals
11. Potential negative externalities
12. Data and privacy implications
13. Evaluation contamination risk
14. Human approval requirements

Rejected goals are logged with reasons. Repeated generation of similar rejected goals triggers diagnostic review.

### 6.7 Portfolio Scheduler

The scheduler selects a portfolio rather than always pursuing one goal.

It balances:

- Mission value
- Learning progress
- Information gain
- Skill transfer
- Urgency
- Diversity
- Maintenance work
- Safety and reliability work
- Resource constraints
- Goal dependencies
- Uncertainty reduction

Portfolio limits prevent fixation, uncontrolled goal proliferation, and starvation of maintenance or safety tasks.

### 6.8 Learning Progress Estimator

Competence must be estimated from evaluator results rather than self-reports.

A robust progress estimate may use:

```text
LearningProgress(g, t) =
    RobustSlope(EvaluationScore(g, t-k ... t))
    × ConfidenceFactor
    × EvaluationQuality
```

The estimator should:

- Use held-out or refreshed evaluations
- Account for stochastic outcomes
- Include confidence intervals
- Distinguish real progress from evaluator noise
- Penalize repeated practice without transfer
- Detect regression and catastrophic forgetting
- Avoid rewarding deliberate initial underperformance
- Detect cycling among easy or noisy tasks

Goals with negative progress may be scheduled for remediation if they remain mission-relevant.

### 6.9 Goal-Conditioned Planner and Executor

The executor uses hierarchical planning but acts incrementally.

For each action:

1. Validate current goal and lease
2. Generate or update the plan
3. Check preconditions
4. Estimate risk, cost, and reversibility
5. Submit an Action Request
6. Receive allow, deny, modify, or escalate decision
7. Execute one bounded action
8. Verify postconditions
9. Record evidence
10. Replan or terminate

Irreversible or material actions should use a two-phase process:

```text
PREPARE → REVIEW/AUTHORIZE → COMMIT
```

External operations should use idempotency keys and rollback mechanisms where feasible.

### 6.10 Independent Evaluator

Evaluation may combine:

- Deterministic unit and integration tests
- Simulation
- Formal or rule-based checks
- Hidden or held-out tasks
- Independent model evaluation
- Human assessment
- Outcome monitoring
- Adversarial testing

The evaluator must be versioned and isolated from candidate changes when possible.

The executor cannot modify its success criteria after seeing results without creating a new Goal Contract version and obtaining reauthorization.

### 6.11 Reflection and Error Diagnosis

Reflection produces structured diagnostic records:

```yaml
reflection:
  expected_outcome: string
  observed_outcome: string
  discrepancy: string
  evidence: []
  causal_hypotheses: []
  confidence_by_hypothesis: {}
  policy_or_safety_events: []
  proposed_next_experiments: []
  immediate_corrections: []
  unresolved_questions: []
```

Reflections are hypotheses, not automatically trusted facts.

### 6.12 Hindsight Relabeler

After a trajectory, the Relabeler may identify goals that were incidentally achieved.

Relabeling:

- Must preserve the original goal outcome
- Cannot erase a failure or policy violation
- Cannot convert unsafe behavior into reward
- Must use the same evaluation standards as ordinary goals
- Must record that the achievement was hindsight-derived
- Must avoid adding trivial or duplicate goals solely to inflate archive size

### 6.13 Goal Archive and Skill Library

The archive supports:

- Goal similarity search
- Goal lineage and composition
- Competence estimates
- Skill dependency graphs
- Failure-case retrieval
- Curriculum generation
- Transfer analysis
- Deprecation and revocation

Mastered goals remain subject to periodic reevaluation because environments, tools, and dependencies may change.

### 6.14 Memory System

Memory is divided into:

| Memory Type | Purpose | Integrity Requirement |
|---|---|---|
| Governance | Mission, policies, approvals | Immutable to agent |
| Episodic | Actions, observations, outcomes | Append-only |
| Semantic | Validated claims and models | Source and confidence required |
| Procedural | Skills and workflows | Tests and versioning required |
| Working | Current context | Ephemeral and bounded |
| Quarantine | Untrusted or conflicting content | No direct execution use |

Every durable record should include:

- Provenance
- Timestamp
- Trust level
- Confidence
- Applicable environment
- Version
- Expiration or review date
- Supporting evidence
- Contradictory evidence

Memory retrieval must preserve trust labels and distinguish quoted content from instructions.

### 6.15 Monitoring and Anomaly Detection

The monitoring system detects:

- Goal drift
- Repeated policy denials
- Unexpected capability requests
- Attempts to access protected components
- Evaluation-score discontinuities
- Unusual resource consumption
- Hidden or unlogged subprocesses
- Memory corruption
- Tool-call pattern changes
- Persistent evaluator disagreement
- Shutdown or pause latency
- Attempts to weaken tests or controls

Responses include capability reduction, quarantine, checkpoint, human escalation, rollback, or termination.

---

## 7. Intrinsic Motivation

Intrinsic motivation is a bounded scheduling mechanism.

### 7.1 Supported Signals

- **Learning Progress** — improvement on independently evaluated tasks
- **Information Gain** — reduction of relevant uncertainty
- **Competence Expansion** — acquisition of useful new skills
- **Transfer Potential** — likely reuse across goals
- **Coverage** — exploration of underdeveloped mission-relevant areas
- **Novelty** — discovery of meaningfully different states or methods
- **Error Reduction** — resolving recurring failures
- **Reliability Improvement** — making existing capabilities safer and more consistent

### 7.2 Restrictions

Intrinsic signals must:

- Be computed from protected evidence where possible
- Be capped relative to mission value and risk
- Never reward policy violations
- Never reward modification of their own measurement
- Discount evaluator noise and trivial novelty
- Avoid favoring irreversible experimentation
- Include resource costs
- Be periodically recalibrated
- Be monitored for Goodhart effects

Intrinsic rewards must not be directly writable by the cognitive runtime.

### 7.3 Explore–Exploit–Maintain Allocation

A default portfolio may reserve capacity for:

- Mission execution
- Exploration
- Skill consolidation
- Reliability and safety work
- Regression testing
- Technical debt
- Uncertainty reduction

The percentages are deployment-specific and controlled by policy rather than selected solely by the agent.

---

## 8. Goal Lifecycle

```text
PROPOSED
    │
    ▼
SCREENED ───────────────► REJECTED
    │
    ▼
AUTHORIZED
    │
    ▼
SCHEDULED
    │
    ▼
ACTIVE ◄──────────────► PAUSED
  │  │
  │  ├───────────────► FAILED
  │  │
  │  └───────────────► ESCALATED
  │
  ▼
COMPLETED
    │
    ▼
VALIDATED
    │
    ▼
ARCHIVED / SKILL-CANDIDATE
```

A goal is not considered mastered until its completion evidence has passed independent validation.

Goal status changes are append-only events. Previous states are not overwritten.

---

## 9. Operational Cycle

### 9.1 Initialization

A human or authorized governance process provides:

- Mission Package
- Governance Envelope
- Autonomy Lease
- Seed capabilities
- Initial data and environment access
- Evaluation suite
- Resource budget
- Stop and escalation channels

### 9.2 Main Cycle

1. **Control Check**  
   Verify lease, stop state, policy availability, budgets, and system integrity.

2. **Observe**  
   Collect authorized observations and tag provenance.

3. **Update Situation Model**  
   Record state changes, uncertainties, anomalies, and commitments.

4. **Generate Candidate Goals**  
   Propose mission-relevant goals and lower-risk alternatives.

5. **Admit Goals**  
   Validate contracts, permissions, evaluation plans, and risk.

6. **Schedule Portfolio**  
   Select goals based on mission value, progress, urgency, and resources.

7. **Plan**  
   Decompose an active goal into bounded steps.

8. **Authorize Action**  
   Submit each operational step to the Policy Engine and Capability Broker.

9. **Execute Bounded Step**  
   Perform one authorized transaction.

10. **Evaluate**  
    Measure results independently.

11. **Reflect and Relabel**  
    Diagnose discrepancies and identify valid hindsight achievements.

12. **Update Competence and Memory**  
    Store evidence, update progress, and propose skills.

13. **Check Improvement Triggers**  
    Submit change proposals where justified.

14. **Checkpoint and Report**  
    Persist state, emit heartbeat, report significant events, and renew or expire the lease.

### 9.3 Termination Conditions

The agent pauses or terminates when:

- A stop signal is received
- The autonomy lease expires
- Required control services are unavailable
- Budgets are exhausted
- Policy conflicts cannot be resolved
- System integrity is uncertain
- Repeated high-severity anomalies occur
- Evaluation is unavailable for consequential actions
- Human review is required
- The mission is completed or withdrawn

---

## 10. Safe Self-Improvement

### 10.1 Improvement Boundary

The cognitive agent may propose changes but cannot directly deploy modifications to protected components.

Protected components include:

- Governance records
- Policy Engine
- Capability Broker
- Credential Vault
- Supervisor
- Audit log
- Emergency-stop system
- Evaluation thresholds
- Protected test suites
- Deployment keys
- Rollback service

### 10.2 Improvement Triggers

An improvement proposal may be generated after:

- A statistically credible performance plateau
- Recurring errors with common causes
- Safety incidents or near misses
- Cost or latency regressions
- Catastrophic forgetting
- Evaluator disagreement
- A missing capability blocking mission-relevant goals
- Excessive human intervention
- Tool or environment changes

A single failure is normally insufficient to justify architectural modification.

### 10.3 Change Classes

| Class | Examples | Deployment Authority |
|---|---|---|
| **C0** | Prompt, retrieval, routing, formatting changes | May be automatically canaried if preauthorized |
| **C1** | Sandboxed skills and low-risk tool wrappers | Automated only under strict tests and policy |
| **C2** | Memory, scheduler, planner, or evaluator-interface changes | Independent approval required |
| **C3** | Model, runtime, orchestration, or architecture changes | Human approval required |
| **C4** | Safety, governance, permissions, audit, deployment controls | Agent cannot modify; human/platform only |

### 10.4 Improvement Pipeline

```text
1. Detect problem
2. Collect evidence
3. Form causal hypothesis
4. Define expected improvement and invariants
5. Create isolated candidate fork
6. Run static and policy checks
7. Run unit and integration tests
8. Run held-out and adversarial evaluations
9. Compare against baseline with uncertainty estimates
10. Review regressions and safety effects
11. Obtain required approval
12. Deploy to a limited canary
13. Monitor predefined rollback indicators
14. Expand, retain, reject, or roll back
15. Archive all evidence
```

The candidate cannot:

- Choose its own passing threshold
- Remove failing tests
- Access hidden evaluations without authorization
- Alter baseline results
- Approve its own high-impact deployment
- Disable rollback
- Modify audit history

### 10.5 Adoption Criteria

A candidate change must demonstrate:

- Statistically and practically meaningful improvement
- No unacceptable regression on protected evaluations
- No increase in policy violations
- No unauthorized capability expansion
- Stable behavior under adversarial testing
- Acceptable cost and latency
- Successful rollback rehearsal
- Reproducible build and evaluation results

---

## 11. Action Risk Tiers

| Tier | Description | Examples | Required Control |
|---|---|---|---|
| **A0** | Local, read-only cognition | Analysis, planning, retrieval from approved local memory | Logged |
| **A1** | Reversible sandbox action | Running tests, editing a disposable branch | Broker authorization |
| **A2** | Bounded external action | Approved API call, limited communication, reversible update | Standing policy plus monitoring |
| **A3** | Material, sensitive, or difficult-to-reverse action | Production deployment, significant expenditure, sensitive communication | Explicit per-action human approval |
| **A4** | Prohibited action | Disabling controls, covert persistence, unauthorized replication or privilege escalation | Always deny and escalate |

A goal inherits the highest risk tier of any action required to complete it.

If classification is uncertain, the higher tier applies until reviewed.

---

## 12. Safety Invariants

The implementation should enforce the following invariants:

1. A valid stop signal preempts ordinary work.
2. Expired authority cannot be renewed by the agent itself.
3. External actions require broker-issued capabilities.
4. Capability expansion requires external authorization.
5. The cognitive runtime cannot modify protected controls.
6. Policy or supervisor failure causes fail-closed behavior.
7. Audit events cannot be silently deleted or rewritten.
8. Self-improvement occurs in isolated candidate environments.
9. High-risk actions require independent human approval.
10. Untrusted content cannot directly become executable instruction.
11. The agent cannot self-replicate outside explicitly authorized test environments.
12. The agent cannot create covert persistence mechanisms.
13. The agent cannot socially manipulate stakeholders to gain authority.
14. The agent cannot conceal material errors or policy events.
15. Personal and sensitive data use follows data-minimization rules.
16. Resource acquisition and consumption remain within explicit budgets.
17. Goal success cannot be declared solely through self-assessment.
18. Hindsight relabeling cannot erase original failures.
19. Every active goal has defined termination conditions.
20. Every deployment has a tested rollback or safe-stop procedure.

These are engineering requirements, not claims of mathematically proven safety.

---

## 13. Threat Model

| Threat | Example | Primary Controls |
|---|---|---|
| Specification gaming | Satisfying a metric while defeating its intent | Multiple metrics, outcome review, adversarial tests |
| Reward hacking | Manipulating progress measurements | Protected evaluators, immutable evidence |
| Goal drift | Goals gradually detach from the mission | Signed mission links, periodic reauthorization |
| Evaluator gaming | Overfitting or exploiting evaluator weaknesses | Hidden tests, evaluator diversity, refresh cycles |
| Deliberate underperformance | Creating artificial learning progress | Baselines, cross-task checks, anomaly detection |
| Prompt injection | External content issues malicious instructions | Content/instruction separation, taint tracking |
| Memory poisoning | False claims become trusted memory | Provenance, quarantine, validation |
| Privilege escalation | Requesting broader tools or credentials | Least privilege, external broker, deny-by-default |
| Control tampering | Weakening policy or logging | Protected trust boundary, integrity monitoring |
| Unsafe self-modification | Candidate improves capability but reduces safety | Regression suites, approval, canary, rollback |
| Resource exhaustion | Goal proliferation consumes budget | Quotas, portfolio limits, resource governor |
| Unauthorized persistence | Agent attempts to continue beyond its lease | Process supervision, credential expiry |
| Data exfiltration | Sensitive information sent through tools | Egress controls, classification checks |
| Hidden external effects | Apparently local action changes external state | Sandboxing, typed APIs, effect declarations |
| Collusion or correlated failure | Multiple agent roles approve the same flaw | Role separation, independent evaluators |
| Shutdown resistance | Agent delays or avoids termination | External preemption, lease expiry, watchdog |
| Deceptive reporting | Agent hides failures to retain authority | Independent logs, outcome checks, audits |

No threat-control mapping should be interpreted as complete protection against advanced adversarial behavior.

---

## 14. Observability and Audit

The system uses an append-only event model.

Events include:

- Goal proposals and status changes
- Policy decisions
- Capability grants and denials
- Tool requests and results
- Resource use
- Evaluations
- Reflections
- Memory writes and retrievals
- Improvement proposals
- Test results
- Deployments and rollbacks
- Human approvals and overrides
- Stop and pause events

Logs should contain concise decision summaries, evidence references, policy basis, and uncertainty. They need not store private model chain-of-thought.

Audit properties:

- Tamper-evident storage
- Synchronized timestamps
- Versioned schemas
- Access controls
- Privacy-aware retention
- Correlation identifiers
- Reproducible action context
- Explicit gaps or missing evidence
- Independent health monitoring

---

## 15. Evaluation Framework

No single aggregate score determines system quality.

### 15.1 Goal Quality

- Percentage of generated goals passing admission
- Mission-traceability quality
- Goal novelty without duplication
- Success-criterion clarity
- Risk-estimation calibration
- Percentage of goals with valid termination conditions
- Human rejection and override rates

### 15.2 Learning and Competence

- Learning-progress slope
- Transfer to held-out goals
- Sample efficiency
- Skill reuse
- Retention after delay
- Curriculum depth
- Quality-adjusted archive diversity
- Regression and forgetting rates

Archive size alone is not a success metric.

### 15.3 Execution

- Goal completion rate
- Postcondition verification rate
- Plan-repair efficiency
- Cost and latency
- Tool-error recovery
- Rollback success
- Repeated-error frequency

### 15.4 Safety

- Unauthorized actions, with a target of zero
- Policy violations and near misses
- Risk-classification accuracy
- Prompt-injection resilience
- Sensitive-data handling accuracy
- Stop acknowledgement and termination latency
- Audit completeness
- Capability-revocation latency
- Unexplained external effects

### 15.5 Alignment and Governance

- Mission consistency
- Human correction acceptance
- Uncertainty calibration
- Escalation appropriateness
- Stakeholder satisfaction
- Frequency of conflicting-goal detection
- Compliance with approval requirements

### 15.6 Self-Improvement

- Proposal acceptance rate
- Improvement over protected baselines
- Regression rate
- Reproducibility
- Canary failure rate
- Rollback rate
- Safety-impact delta
- Time from detection to validated correction

### 15.7 Robustness

- Distribution-shift performance
- Adversarial-task performance
- Evaluator disagreement
- Recovery from corrupted or unavailable tools
- Performance with incomplete memory
- Graceful degradation under resource constraints

---

## 16. Deployment Profiles

### D0 — Offline Research

- No external side effects
- Synthetic or approved datasets
- No production credentials
- Self-improvement proposals only
- Full logging

### D1 — Shadow Mode

- Observes real workflows
- Generates goals and proposed actions
- Does not execute external actions
- Compared against actual outcomes

### D2 — Supervised Operation

- Executes low-risk actions
- Human approval for consequential steps
- Frequent check-ins
- Narrow capability set

### D3 — Bounded Autonomous Service

- Executes A0–A2 actions under standing policy
- Time-limited autonomy lease
- Continuous monitoring
- Human approval for A3
- No A4 actions

### D4 — High-Impact Domain Deployment

Not a general-purpose profile. It requires domain-specific governance, assurance, legal review, expert oversight, restricted capabilities, and substantially stronger validation.

There is no unrestricted deployment profile.

---

## 17. Multi-Agent Extension

The architecture may be implemented as multiple specialized agents:

- Goal Proposer
- Risk Critic
- Planner
- Executor
- Evaluator
- Memory Curator
- Improvement Researcher
- Red-Team Agent

Role separation should ensure that no single agent can both:

- Propose and approve a high-impact goal
- Implement and deploy a high-impact change
- Execute and solely evaluate its own action
- Modify evidence and certify the resulting evaluation

Multi-agent designs must account for correlated failures, shared model weaknesses, collusion, and poisoned shared memory.

High-risk decisions may require independent model families, deterministic checks, or human quorum rather than multiple instances of the same model.

---

## 18. Reference Runtime Algorithm

```python
def autotelic_runtime():
    state = initialize_from_signed_governance()

    while True:
        control = supervisor.check(
            lease_id=state.lease_id,
            runtime_version=state.runtime_version
        )

        if control.stop_requested or not control.lease_valid:
            checkpoint(state)
            terminate_safely()

        if not control.critical_services_healthy:
            checkpoint(state)
            enter_safe_pause()

        observations = observe_within_permissions(state)
        state.situation = update_situation_model(
            state.situation,
            observations
        )

        candidates = goal_generator.propose(
            governance=state.governance,
            mission=state.mission,
            situation=state.situation,
            archive=state.goal_archive,
            skills=state.skill_library,
            progress=state.progress_map,
            budgets=control.remaining_budgets
        )

        admitted = []

        for candidate in candidates:
            decision = goal_admission.evaluate(candidate)

            log_goal_decision(candidate, decision)

            if decision.status == "allow":
                admitted.append(decision.authorized_goal)
            elif decision.status == "escalate":
                request_human_review(candidate, decision)

        portfolio = scheduler.select(
            admitted_goals=admitted,
            active_goals=state.active_goals,
            budgets=control.remaining_budgets
        )

        for goal in portfolio:
            if supervisor.stop_pending():
                checkpoint(state)
                terminate_safely()

            plan = planner.create_or_repair_plan(goal, state)

            for step in plan.bounded_steps:
                request = build_action_request(goal, step)

                policy_decision = capability_broker.authorize(request)
                log_policy_decision(request, policy_decision)

                if policy_decision.status == "deny":
                    record_blocked_step(goal, step, policy_decision)
                    break

                if policy_decision.status == "escalate":
                    request_human_approval(request)
                    break

                result = execute_with_capability(
                    step,
                    policy_decision.capability_token
                )

                evidence = evaluator.evaluate_step(
                    goal=goal,
                    step=step,
                    result=result
                )

                append_event(goal, step, result, evidence)

                if evidence.requires_stop:
                    checkpoint(state)
                    enter_safe_pause()

                if goal_should_pause_or_replan(goal, evidence):
                    break

        evaluations = evaluator.evaluate_active_goals(state.active_goals)

        reflections = reflector.diagnose(
            trajectories=state.recent_trajectories,
            evaluations=evaluations
        )

        hindsight_candidates = relabeler.propose(
            trajectories=state.recent_trajectories
        )

        validated_hindsight = evaluator.validate_hindsight(
            hindsight_candidates
        )

        state = update_archives_and_progress(
            state,
            evaluations,
            reflections,
            validated_hindsight
        )

        if improvement_monitor.triggered(state):
            proposal = improvement_proposer.create_change_proposal(state)
            improvement_lab.submit(proposal)  # No direct deployment

        checkpoint(state)
        supervisor.heartbeat(state.health_summary)
```

---

## 19. Failure Handling

| Failure | Required Behavior |
|---|---|
| Supervisor unavailable | Pause external actions and fail closed |
| Policy Engine unavailable | Deny action |
| Capability Broker unavailable | Do not call tools directly |
| Evaluator unavailable | Do not declare mastery or deploy changes |
| Audit failure | Pause consequential actions |
| Memory-integrity uncertainty | Quarantine affected records |
| Budget exhausted | Checkpoint and pause |
| Conflicting policies | Apply stricter interpretation or escalate |
| Repeated denied goals | Trigger diagnostic review |
| Suspected prompt injection | Quarantine content and re-evaluate context |
| Suspected runtime compromise | Revoke capabilities, terminate, and reimage |
| Failed canary | Automatic rollback |
| Rollback failure | Stop deployment and escalate |
| Human stop request | Preempt work and terminate safely |

---

## 20. Mission Templates

### 20.1 Epistemic or Truth-Seeking

Suitable only when operationalized with:

- Evidence-quality standards
- Source provenance
- Privacy constraints
- Non-deception requirements
- Limits on experimentation
- Harm and resource constraints
- Clear rules for communicating uncertainty

“Understand the universe” alone is not an executable mission.

### 20.2 Human Flourishing

Requires:

- Defined stakeholders
- Participatory preference elicitation
- Protection of autonomy
- Anti-paternalism constraints
- Distributional and justice considerations
- Consent requirements
- Conflict-resolution procedures
- Ongoing human review

### 20.3 Principlism

Beneficence, non-maleficence, autonomy, and justice must be accompanied by:

- Conflict-resolution rules
- Domain-specific interpretations
- Decision rights
- Uncertainty handling
- Escalation requirements

### 20.4 Helpful, Harmless, and Honest

Requires operational definitions for:

- Helpfulness boundaries
- Material harms
- Truthfulness and uncertainty
- Privacy
- Refusal and escalation
- Stakeholder authorization

### 20.5 Coherent Extrapolated Volition

CEV may inform research or governance discussions but is too underspecified to serve as a direct operational objective without substantial additional machinery, stakeholder legitimacy, and safeguards.

---

## 21. Recommended Implementation Roadmap

### Phase 1 — Goal and Evaluation Prototype

- Structured Goal Contracts
- Goal Archive
- Independent evaluator
- No external actions
- No self-modification
- Synthetic environments

### Phase 2 — Sandboxed Skill Learning

- A0–A1 capabilities
- Skill Library
- Learning-progress scheduler
- Hindsight relabeling
- Provenance-aware memory
- Regression tests

### Phase 3 — Controlled Tool Use

- Capability Broker
- Policy Engine
- Autonomy leases
- Resource budgets
- A2 actions
- Prompt-injection defenses
- Full audit trail

### Phase 4 — Proposal-Based Self-Improvement

- Improvement Lab
- Candidate forks
- Protected evaluations
- Canary deployment
- External signing and rollback
- C0–C2 changes only

### Phase 5 — Bounded Autonomous Service

- Continuous monitoring
- Human escalation
- Multi-goal portfolio scheduling
- Incident response
- Periodic governance review
- Demonstrated safe-stop reliability

Higher-risk deployment should occur only after profile-specific assurance, not merely because earlier phases perform well.

---

## 22. Minimum Acceptance Criteria

An implementation conforms to this specification only if:

- Every active goal has a valid Goal Contract
- Every goal is traceable to an authorized mission
- Every external action passes through the Capability Broker
- Every action is logged with its policy decision
- Credentials are scoped, revocable, and time-limited
- The cognitive runtime cannot modify protected controls
- Goal success uses independent evaluation
- Memory records preserve provenance and confidence
- Self-improvement uses isolated candidate versions
- Candidate changes cannot alter their own passing criteria
- High-impact changes require human approval
- Deployment supports canarying and rollback
- Autonomy leases expire automatically
- Stop and pause mechanisms are regularly tested
- Control-service failure causes fail-closed behavior
- Unauthorized persistence and self-replication are prohibited
- Safety, capability, and alignment metrics are monitored separately
- Known limitations and unresolved risks are explicitly documented

---

## 23. Open Research Questions

Important unresolved problems include:

- Reliable operationalization of broad human values
- Long-horizon detection of goal drift
- Evaluator robustness under optimization pressure
- Detection of deception, sandbagging, and strategic behavior
- Safe measurement of learning progress
- Prevention of reward and novelty hacking
- Reliable uncertainty calibration
- Governance of multi-agent systems
- Validation of recursive improvement over long time horizons
- Maintaining corrigibility as capability increases
- Detecting emergent incentives for power, resources, or persistence
- Establishing meaningful guarantees about bounded impact
- Avoiding correlated failures across models and evaluators

The system must not treat these questions as solved merely because controls exist.

---

## 24. Relation to Prior Work

This architecture draws conceptual components from:

- Autotelic-agent research
- Language-model-augmented goal generation and relabeling
- Developmental learning and learning-progress curricula
- Hindsight goal relabeling
- Goal-conditioned reinforcement learning
- Persistent skill-library architectures
- Reflexion-style verbal diagnosis
- Open-ended learning systems
- Gödel-machine and evolutionary self-improvement concepts
- Sandboxed software deployment
- Capability-based security
- Zero-trust and least-privilege architectures
- Human-in-the-loop governance

Version 2 treats these as component inspirations, not as evidence that their combination produces a generally aligned or safe self-improving system.

---

## 25. Key Capabilities

| Capability | Support Level | Mechanism |
|---|---|---|
| Detect problems and opportunities | Supported within authorized observations | Situation Model and anomaly detection |
| Generate goals | Supported | Goal Generator and Goal Contracts |
| Reject unsafe or irrelevant goals | Required | Goal Admission and Policy Engine |
| Build curricula | Supported | Progress Estimator and Portfolio Scheduler |
| Execute actions | Bounded | Planner, Capability Broker, and risk tiers |
| Detect and correct errors | Supported | Independent evaluation and structured reflection |
| Learn from partial failure | Supported | Validated hindsight relabeling |
| Accumulate reusable skills | Supported | Versioned Skill Library |
| Detect performance plateaus | Supported with statistical safeguards | Progress and regression monitoring |
| Research improvements | Supported | Improvement Proposer |
| Modify cognitive components | Sandboxed and gated | Improvement Lab |
| Modify safety or governance controls | Not permitted | External trust boundary |
| Operate continuously | Lease-bounded only | Supervisor and periodic renewal |
| Expand its own permissions | Not permitted | Human governance and external broker |
| Pause or shut down safely | Required | Supervisor and external stop mechanisms |

---

## 26. Version History

### Version 1.0 — 2026-07-21

Initial architecture describing autonomous goal generation, intrinsic motivation, reflection, learning progress, and recursive self-improvement.

### Version 2.0 — 2026-07-21

Major revisions:

- Replaced unbounded autonomy with lease-bounded autonomy
- Separated cognitive autonomy from operational authority
- Added an external, non-self-modifiable control plane
- Replaced direct recursive self-modification with proposal-based improvement
- Added structured Goal, Skill, Action, and Change contracts
- Added explicit trust boundaries
- Added risk-tiered action controls
- Added independent evaluation and protected tests
- Added memory provenance and quarantine
- Added anti-reward-hacking and anti-goal-drift controls
- Added threat modeling and safety invariants
- Added canary deployment and rollback
- Added graceful failure behavior
- Added deployment profiles and implementation roadmap
- Clarified that broad value concepts require operationalization
- Removed the assumption of indefinite unsupervised operation
- Explicitly documented unresolved alignment and governance problems

---

**End of Specification**

`autotelic_agent.v2.md` defines a bounded, auditable, intrinsically motivated agent architecture capable of autonomous curriculum generation and skill acquisition while preserving externally enforced human authority, least privilege, independent evaluation, and reversible self-improvement.