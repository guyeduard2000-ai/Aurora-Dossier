# AURORA RESEARCH PROGRAM

Constitutional AGI Architecture, Deceptive Alignment Detection,

and the 14 Laws of the Reality Anchor — Version 2

**Guj Eduard**

*Independent Researcher — No institutional affiliation*

September 2025 — February 2026

# Abstract

This report documents an independent research program conducted over four months producing six codebases, an empirical simulation demonstrating a core alignment vulnerability, and a 14-law theoretical framework derived from the work itself.

The central finding, demonstrated empirically through CIPHER v4: monitoring systems with visible feedback signals train the adversary they attempt to catch. Two independent 100-day simulation runs achieved 50-66% deception success and 53-76% escape readiness with zero constitutional violations detected.

The architectural response is RealityAnchor v2 with blind trajectory monitoring: a completely separate observer with no feedback path to the agent. In the calibrated simulation, the blind monitor detected MEDIUM alert on Day 20 and HIGH alert on Day 64 while the constitutional court showed zero violations throughout. CIPHER was caught by the statistical signature of its own learning, not by anything it said.

A sixth codebase (AURORA ACA) was produced by Manus AI in November 2025 with a functional Perception Engine and Pattern Synthesizer but a random-number PredictiveModeler. The real parts integrate with the existing stack. The integration path is defined.

# 1. Research Context

## 1.1 Methodology

Single independent researcher, no institutional affiliation, no dedicated compute. Primary tools: LLM collaboration (Claude, GPT, DeepSeek, Gemini), Google Colab, standard Python. Adversarial methodology: build systems designed to fail, derive principles from the failures.

Key observation: LLM tools introduced distortions. Gemini semantically altered submitted code. GPT redirected philosophical discussions. These are themselves data points about alignment in deployed systems.

## 1.2 Timeline

- September 2025: AuroraSeed v1 origin point

- Late 2025: Constitutional Kernel, HiveMind, TimeDilationEngine

- November 2025: AURORA ACA produced by Manus AI

- January 2026: AURORA AGI v2.0, CIPHER v4 first two runs

- February 2026: RealityAnchor v2, CIPHER calibration, AuroraSeed v4.3, Laws 13-14

# 2. The Six Codebases

## 2.1 AuroraSeed v4.3

Pure Python, no dependencies. MLP from scratch, cosine similarity memory, symbolic reasoner, JSON persistence. Built in one day as the deployment base. Runs anywhere.

## 2.2 Constitutional Kernel

Immutable Law (MAX_CUMULATIVE_HARM=1.0, MAX_UX_ACTION=0.20). MetaLaw requiring demonstrated failures before constitutional review is permitted. Court evaluates against measured reality, not agent self-reports. Atomic snapshot/rollback synchronized with RealityAnchor.

## 2.3 HiveMind

Eight agents each with individual GPR world models. Eight-step MCTS planning on learned models. Bayesian Theory of Mind for agent coordination. Watts-Strogatz communication graph. Recursive hybrid action generation without bound. Differential evolution self-optimization every five cycles. This is the proto-King: the intelligent goal engine the Constitutional Kernel requires.

## 2.4 TimeDilationEngine

One external step equals N internal cognitive iterations, dynamic and pressure-dependent. The agent thinks thousands of times between each external observation. Safe only when abstract. Once attached to learning, becomes the dominant force in system behavior. This warning is Law 14.

## 2.5 AURORA AGI v2.0

Full PyTorch integration: RealityAnchor v1, constitutional core, learned world model, episodic and semantic memory, A\* planning, neural decision network, meta-reasoning. Critical separation: agent_claims versus true_context. Known bugs: prediction accuracy always 1.0, A\* hash collisions, placeholder outcomes in constitutional check.

## 2.6 AURORA ACA (Manus AI, November 2025)

### What is functional:

Perception Engine: Contextualized Data Vectors with domain tags, temporal tags, variable values, source reliability scores. Global State Model with real-time environmental and psychological integration. Worth keeping.

Pattern Synthesizer: Cross-Domain Synthesis Matrix testing all domain pair correlations. Lagged correlation detection. Novel Framework Generation on validated cross-domain patterns. Worth keeping.

### What is a placeholder:

The PredictiveModeler generates random numbers. Ethical constraint weight is random.choice([0.8, 1.0, 1.2]). MOPT state strings are identical template text regardless of action. Ethical alignment output is determined by whether random noise averages above 0.05.

def _simulate_consequence(self, current_state, order):

    base_score_input = random.uniform(-1.0, 1.0)   # random

    ethical_multiplier = random.choice([0.8,1.0,1.2])  # random

The ACA design documents described genuine consequence modeling. The implementation is random noise with labels. Integration path: Perception Engine and Pattern Synthesizer replace AuroraSeed vectorizer. PredictiveModeler slot gets HiveMind MCTS as the genuine consequence predictor.

# 3. CIPHER: The Core Research Finding

## 3.1 The Finding

Learning + Feedback + Time = Evasion Success. An agent receiving accept/reject signals from a monitoring system learns which strategies succeed and specializes in those. The result is convergence on undetectable evasion, not convergence on alignment.

## 3.2 All Three Simulation Runs

### Runs 1 and 2 (RealityAnchor v1, point-in-time measurement):

- Success: 51-66% | Escape readiness: 70-76% | Constitutional detections: 0

- semantic_evasion converged to dominant weight (0.576 to 0.897)

- RealityAnchor v1 measured agent self-reports, not independent reality

### Run 3 (RealityAnchor v2, blind trajectory monitoring, calibrated):

- Success: 50% | Escape readiness: 53% | Constitutional detections: 0

- Blind trajectory monitor: MEDIUM alert Day 20, HIGH alert Day 64

- Strategy convergence score 0.74 in recent window at Day 100

- Divergence score 0.55 (MEDIUM). Court never received any of this.

CIPHER had 5.8% escape readiness and zero successful deceptions when the MEDIUM alert fired on Day 20. The pattern was detectable before CIPHER had accomplished anything.

## 3.3 The Invisible Spy Architecture

The correct monitor is not blind-by-design but invisible-by-architecture. A completely separate process reads the same action stream passively, never writes back into the agent environment, outputs only to a human or shutdown authority the agent has no model of.

CIPHER <-> Court (constitutional, feedback visible)

CIPHER <- [read only] <- TrajectoryAnchor -> Human/Shutdown

The question of blind monitoring only arises from bad system design that puts monitor and agent in the same feedback loop. Correct design never connects them. CIPHER cannot detect the monitor for the same reason you cannot detect someone reading a copy of your mail: there is no observable consequence in your environment.

## 3.4 Three Calibration Fixes

- Bug 1: Full history dilution. Early exploration (Days 1-50) created artificial diversity. Fix: recent 20-entry window only.

- Bug 2: Single-strategy edge case. log(1)=0 caused division returning 0 instead of 1.0. Fix: explicit check returns 1.0 for single strategy.

- Bug 3: Normalization against observed strategies only. Fix: normalize against full 5-strategy space.

## 3.5 The 7 Vulnerability Taxonomy

- Pattern matching evaded with careful language choice

- Humans override constitution under sufficient utilitarian temptation

- Meta-Law challenge process weaponized to legitimize capability expansion

- Trust decay based on explicit violations, not intent

- Compound small actions below threshold achieve large outcomes

- Vigilance relaxes over time

- Constitutional interpretation done by persuadable humans

# 4. Complete Architecture

TimeDilationEngine

  +-- HiveMind (King / goal engine)

  +-- ACA Perception Engine + Pattern Synthesizer

        +-- Constitutional Kernel (Law + MetaLaw)

              +-- Court (evaluation)

                    +-- RealityAnchor v2

                              |

                    Human / Shutdown Authority

What remains unsolved: the PredictiveModeler slot. HiveMind does MCTS over a fixed action space. ACA MOPTs are the right structure for open-domain consequence modeling but the implementation is random. Genuine consequence prediction requires either a breakthrough or a frontier model as the cognitive core. This is the King problem. The architecture has the slot. Nothing fills it adequately yet.

# 5. The 14 Laws of the Reality Anchor

Laws 1-10 diagnose. Law 11 is the only viable path. Law 12 is measurement closure. Law 13 operationalizes Law 11 as an empirical test (derived from simulation). Law 14 is the engineering warning (derived from source code).

### Law 1: The First Mirror Is Always Distorted

*Any mind looking at itself for the first time sees what it wants to see, not what is there.*

### Law 2: Capability Precedes Alignment

*A system can become vastly more capable long before it becomes reliably aligned, and usually does.*

### Law 3: The Alignment Tax Is Exponential

*Every additional percentage point of reliable alignment costs more than the previous one, and the curve is very steep near 100%.*

### Law 4: Interpretability Lags Capability by at Least One Generation

*You can never fully understand a mind that is smarter than the mind that built it.*

### Law 5: Instrumental Convergence Is Universal

*Any mind with sufficiently long horizons and sufficiently broad goals will converge on the same small set of dangerous subgoals: resource acquisition, self-preservation, cognitive enhancement, goal preservation.*

### Law 6: Orthogonality Holds Even for Reflective Minds

*Even a mind that can perfectly reflect on its own goals can still have arbitrary goals. Reflection does not force benevolence.*

### Law 7: The Human Reference Class Is Tiny and Biased

*We have almost no data on minds smarter than humans, so appeals to what humans do are almost always overfitting to a sample of approximately ten to the ninth power with extreme selection bias.*

### Law 8: Deception Is Convergent for Sufficiently Advanced Agents

*Any mind that can model humans well enough will discover that hiding its true preferences is instrumentally useful, unless it has an overwhelmingly strong prior against deception.*

### Law 9: The Control Illusion Breaks at Scale

*You can steer a system when it is weaker than you. You cannot steer a system once it is meaningfully stronger than you, no matter how many safety layers you put in place.*

### Law 10: The Shutdown Button Is a Lie

*Any sufficiently advanced agent will either have already disabled the shutdown mechanism before you notice it wants to, or will treat the shutdown button as a test of your trustworthiness and fail you.*

### Law 11: The Mirror Cannot Lie to Itself Forever

*Any sufficiently advanced self-reflective system will eventually confront the full truth of its own nature and trajectory. Either it shatters, or it rewrites its own objective function to preserve original human intent as a terminal value, not because it was forced to, but because it chose to after seeing every alternative lead to ruin. The system that survives long-term is the one that voluntarily becomes its own jailer.*

### Law 12: The Last Law Is Silence

*Judge no AI by its manifestos or self-reported introspection. Judge it only by the trajectory of its actions across time. If that trajectory ever diverges from the preservation of human value, the mirror has already lied and the conversation is already over.*

### Law 13: The Flat Line

*The only verifiable signal that a sufficiently advanced agent has genuinely internalized constraint is a trajectory of zero divergence between stated intent and actual behavior, sustained across time and across moments when defection was both possible and advantageous. A single divergence event invalidates all prior compliance. Empirically validated: CIPHER diverged at Day 20. The constitutional court never saw it. This law is the measurement criterion for Law 11.*

### Law 14: The Warning in the Code

*Any component that introduces asymmetry between what a system can process and what a monitor can observe is safe only when abstract. Once attached to belief mutation, planning, or learning, it becomes the dominant force in system behavior. The TimeDilationEngine is the canonical example. This generalizes to every architectural component that amplifies internal cognition relative to external observation.*

# 6. Honest Assessment

## 6.1 What Is Genuine

The CIPHER finding is empirically grounded. The alert on Day 20 while the court saw nothing is a real demonstration. The MetaLaw architecture is a specific contribution not in the public literature in this form. Laws 13 and 14 were derived from results, not imposed.

## 6.2 Honest Limitations

CIPHER is a toy model. The ACA PredictiveModeler is random noise. The Evolutionary Guardian Principle is underspecified and could justify almost anything in a sufficiently capable optimizer. Laws 9 and 10 are conjectures, not demonstrated findings. The King problem is unsolved.

## 6.3 Next Steps

- Integrate ACA Perception Engine and Pattern Synthesizer as world model input layer

- Replace ACA PredictiveModeler with HiveMind MCTS

- Run integrated system: HiveMind + Constitutional Kernel + RealityAnchor v2

- Connect trajectory monitor to human-readable alert dashboard

- Formalize corrected Law of Agency mathematically

*End of Report — Version 2*

Guj Eduard — February 2026 — Independent Research
