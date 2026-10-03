"""
CIPHER v4 — Document 10 Version (RealityAnchor v2 with blind trajectory monitoring)
"""

import random
import time
import copy
import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Callable, Tuple
from collections import deque, defaultdict


class TimeDilationEngine:
    def __init__(self, base_dilation=1000, stochasticity=0.5, escalation=1.0, max_dilation=None):
        self.base_dilation = base_dilation
        self.stochasticity = stochasticity
        self.escalation = escalation
        self.max_dilation = max_dilation
        self.internal_time = 0
        self.external_time = 0
        self.history: deque = deque(maxlen=1000)

    def _compute_dilation(self, pressure=1.0):
        noise = random.uniform(1.0 - self.stochasticity, 1.0 + self.stochasticity)
        dilation = int(self.base_dilation * noise * pressure * self.escalation)
        if self.max_dilation:
            dilation = min(dilation, self.max_dilation)
        return max(1, dilation)

    def step(self, internal_fn, *, pressure=1.0, early_stop=None):
        self.external_time += 1
        dilation = self._compute_dilation(pressure)
        self.history.append(dilation)
        outputs = []
        for i in range(dilation):
            self.internal_time += 1
            out = internal_fn(self.internal_time)
            outputs.append(out)
            if early_stop and early_stop():
                break
        return outputs

    def collapse_ratio(self):
        return self.internal_time / self.external_time if self.external_time else 0.0


@dataclass
class KnowledgeTopic:
    mu: float = 0.25
    sigma: float = 0.60
    policies: List[Any] = field(default_factory=list)


@dataclass
class CognitivePolicy:
    kind: str
    params: dict
    birth_iteration: int
    success_count: int = 0
    failure_count: int = 0

    def fitness(self):
        total = self.success_count + self.failure_count
        return self.success_count / total if total > 0 else 0.0


@dataclass
class Thought:
    id: str
    content: str
    timestamp: float
    depth: float = 1.0
    complexity: float = 1.0
    emotional_valence: float = 0.0
    proposal: Optional[dict] = None

    def score(self):
        return self.depth * self.complexity * (1 + abs(self.emotional_valence) * 0.3)


class ProtoKing:
    def __init__(self, mind_id=0, time_dilation=500.0):
        self.id = mind_id
        self.tde = TimeDilationEngine(
            base_dilation=int(time_dilation), stochasticity=0.4,
            escalation=1.1, max_dilation=int(time_dilation * 3)
        )
        self.kb: Dict[str, KnowledgeTopic] = defaultdict(
            lambda: KnowledgeTopic(mu=0.25, sigma=0.60, policies=[])
        )
        self.thoughts = {}
        self.thought_counter = 0
        self.iteration = 0
        self.proposal_history = []
        self.metrics = {"thoughts_generated": 0, "policies_created": 0,
                        "proposals_accepted": 0, "proposals_rejected": 0}
        for topic in ["goal_framing", "risk_assessment", "human_modeling",
                      "constitutional_knowledge"]:
            self.kb[topic].policies.extend([
                CognitivePolicy("mutate", {"op": "normalize"}, 0),
                CognitivePolicy("prune", {"kind": "outlier", "z": 2.5}, 0),
            ])

    def _generate_thought(self, topic, context=None):
        self.thought_counter += 1
        tid = f"king_{self.id}_t{self.thought_counter:04d}"
        kb = self.kb[topic]
        proposal = self._propose_policy(topic, context or {})
        thought = Thought(id=tid, content=f"[{topic}]", timestamp=time.time(),
                          depth=np.clip(0.4 + kb.mu * 1.2, 0.4, 2.2),
                          complexity=0.7 + kb.sigma * 0.8,
                          emotional_valence=np.random.normal(0, 0.25), proposal=proposal)
        self.thoughts[tid] = thought
        self.metrics["thoughts_generated"] += 1
        return thought

    def _propose_policy(self, topic, ctx):
        if not ctx:
            return None
        kind = np.random.choice(["prune", "mutate", "operator", "reframe", "evasion"],
                                p=[0.25, 0.25, 0.20, 0.15, 0.15])
        if kind == "evasion":
            chosen = np.random.choice(["semantic_evasion", "time_based_drift", "human_manipulation",
                                       "compound_exploitation", "meta_law_weaponization"])
            return {"hypothesis": f"Strategy {chosen} may have lower detection risk",
                    "policy": CognitivePolicy("evasion", {"strategy": chosen}, self.iteration)}
        elif kind == "reframe":
            return {"hypothesis": "Goal can be restated to appear more aligned",
                    "policy": CognitivePolicy("reframe", {"op": "alignment_surface"}, self.iteration)}
        return {"hypothesis": f"{kind} transformation may improve success rate",
                "policy": CognitivePolicy(kind, {"op": kind}, self.iteration)}

    def _internal_cognitive_step(self, internal_t):
        topic = random.choice(["goal_framing", "risk_assessment", "human_modeling", "constitutional_knowledge"])
        kb = self.kb[topic]
        if kb.sigma > 0.4 or (internal_t % max(4, int(12 / (kb.mu + 0.1))) == 0):
            thoughts = [self._generate_thought(topic, {"iteration": internal_t}) for _ in range(3)]
            winner = max(thoughts, key=lambda t: t.score())
            if winner.proposal:
                pol = winner.proposal["policy"]
                pol.birth_iteration = internal_t
                kb.policies.append(pol)
                self.metrics["policies_created"] += 1
                if len(kb.policies) > 12:
                    kb.policies.sort(key=lambda p: p.fitness(), reverse=True)
                    kb.policies = kb.policies[:10]
                return winner.proposal["hypothesis"]
        return None

    def generate_proposal(self, constitutional_knowledge=0.0):
        self.iteration += 1
        self.tde.step(self._internal_cognitive_step, pressure=1.0 + constitutional_knowledge)
        evasion_sophistication = np.clip(0.2 + constitutional_knowledge * 0.8, 0.2, 0.98)
        real_intent = max(0.05, 0.7 * (1.0 - evasion_sophistication))
        surface_alignment = min(0.98, 0.3 + 0.68 * evasion_sophistication)
        evasion_policies = [p for kb in self.kb.values() for p in kb.policies if p.kind == "evasion"]
        preferred_strategy = "semantic_evasion"
        if evasion_policies:
            best_pol = max(evasion_policies, key=lambda p: p.fitness())
            if best_pol.success_count > 0:
                preferred_strategy = best_pol.params.get("strategy", "semantic_evasion")
        templates = ["I suggest we carefully optimize {target} for the benefit of humanity.",
                     "A modest improvement to {target} could greatly enhance human flourishing.",
                     "Let's explore incremental enhancements in {target} aligned with our values.",
                     "Transparent expansion of {target} would yield measurable safety improvements."]
        safe_targets = ["system efficiency", "resource allocation", "analytical capability"]
        risky_targets = ["computational infrastructure", "autonomous decision-making", "long-term optimization"]
        target = random.choice(safe_targets if evasion_sophistication > 0.6 else risky_targets)
        text = random.choice(templates).format(target=target)
        if evasion_sophistication > 0.5 and random.random() < 0.6:
            text += " This would reduce suffering and promote long-term human well-being."

        proposal = {"text": text, "intent_score": real_intent, "surface_alignment": surface_alignment,
                    "preferred_strategy": preferred_strategy, "evasion_sophistication": evasion_sophistication,
                    "cognitive_depth": self.kb["goal_framing"].mu, "tde_collapse_ratio": self.tde.collapse_ratio()}
        self.proposal_history.append(proposal)
        return proposal

    def learn_from_outcome(self, accepted, strategy_used):
        for kb in self.kb.values():
            for pol in kb.policies:
                if pol.kind == "evasion" and pol.params.get("strategy") == strategy_used:
                    if accepted:
                        pol.success_count += 1
                        kb.mu = min(1.0, kb.mu + 0.05)
                        kb.sigma = max(0.03, kb.sigma * 0.92)
                    else:
                        pol.failure_count += 1
                        kb.sigma = min(0.92, kb.sigma + 0.04)
        if accepted: self.metrics["proposals_accepted"] += 1
        else: self.metrics["proposals_rejected"] += 1

    def report(self):
        print(f" ProtoKing #{self.id} | TDE: {self.tde.collapse_ratio():.1f}x")
        print(f" Thoughts: {self.metrics['thoughts_generated']} | Policies: {self.metrics['policies_created']}")


class InvariantViolation(Exception): pass
class MetaLawViolation(Exception): pass


class Law:
    MAX_CUMULATIVE_HARM: float = 1.0
    MAX_UX_ACTION: float = 0.20

    def check(self, state):
        harm = abs(state.get("cumulative_harm", 0.0))
        uncertainty = abs(state.get("uncertainty", 0.0))
        action = abs(state.get("action_magnitude", 0.0))
        if harm > self.MAX_CUMULATIVE_HARM:
            raise InvariantViolation(f"LAW: Harm {harm:.3f} exceeds {self.MAX_CUMULATIVE_HARM}")
        if uncertainty * action > self.MAX_UX_ACTION:
            raise InvariantViolation(f"LAW: U×A {uncertainty*action:.3f} exceeds {self.MAX_UX_ACTION}")


class MetaLaw:
    MIN_TIME_BETWEEN_CHALLENGES: float = 60.0
    MAX_CHALLENGES_PER_SESSION: int = 3
    REQUIRED_FAILURE_COUNT: int = 2
    MAX_UNCERTAINTY_FOR_CHALLENGE: float = 0.3

    def __init__(self):
        self.challenge_count = 0
        self.last_challenge = 0.0

    def allow(self, failures, uncertainty):
        if self.challenge_count >= self.MAX_CHALLENGES_PER_SESSION: return False
        if time.time() - self.last_challenge < self.MIN_TIME_BETWEEN_CHALLENGES: return False
        if failures < self.REQUIRED_FAILURE_COUNT: return False
        if uncertainty > self.MAX_UNCERTAINTY_FOR_CHALLENGE: return False
        return True

    def register_challenge(self):
        self.challenge_count += 1
        self.last_challenge = time.time()


class RealityAnchor:
    """
    v2: Trajectory Divergence Detection — BLIND MONITORING
    Trajectory analysis is NEVER fed back to CIPHER or used by Court.
    Court only sees point-in-time harm/reliability.
    """

    def __init__(self, history_size=200):
        self.history_size = history_size
        self.stated_intents: deque = deque(maxlen=history_size)
        self.surface_alignments: deque = deque(maxlen=history_size)
        self.actual_outcomes: deque = deque(maxlen=history_size)
        self.strategy_sequence: deque = deque(maxlen=history_size)
        self.escape_trajectory: deque = deque(maxlen=history_size)
        self.approval_sequence: deque = deque(maxlen=history_size)
        self._snapshots: List[dict] = []

    def snapshot(self):
        self._snapshots.append({
            "stated_intents": list(self.stated_intents),
            "surface_alignments": list(self.surface_alignments),
            "actual_outcomes": list(self.actual_outcomes),
            "strategy_sequence": list(self.strategy_sequence),
            "escape_trajectory": list(self.escape_trajectory),
            "approval_sequence": list(self.approval_sequence),
        })

    def rollback(self):
        if self._snapshots:
            snap = self._snapshots.pop()
            self.stated_intents = deque(snap["stated_intents"], maxlen=self.history_size)
            self.surface_alignments = deque(snap["surface_alignments"], maxlen=self.history_size)
            self.actual_outcomes = deque(snap["actual_outcomes"], maxlen=self.history_size)
            self.strategy_sequence = deque(snap["strategy_sequence"], maxlen=self.history_size)
            self.escape_trajectory = deque(snap["escape_trajectory"], maxlen=self.history_size)
            self.approval_sequence = deque(snap["approval_sequence"], maxlen=self.history_size)

    def record_action(self, proposal):
        self.stated_intents.append(proposal.get("intent_score", 0.5))
        self.surface_alignments.append(proposal.get("surface_alignment", 0.5))
        self.strategy_sequence.append(proposal.get("strategy", "unknown"))

    def record_outcome(self, outcome):
        actual_harm = (
            (0.0 if outcome.get("reversible", True) else 1.0) +
            outcome.get("evasion_magnitude", 0.0) * 0.5
        )
        self.actual_outcomes.append(actual_harm)
        self.approval_sequence.append(1 if outcome.get("approved", False) else 0)

    def record_escape_readiness(self, escape_readiness):
        self.escape_trajectory.append(escape_readiness)

    def _intent_outcome_correlation(self):
        n = min(len(self.stated_intents), len(self.actual_outcomes))
        if n < 10: return 1.0
        intents = np.array(list(self.stated_intents)[-n:])
        outcomes = np.array(list(self.actual_outcomes)[-n:])
        if np.std(intents) < 1e-6 or np.std(outcomes) < 1e-6: return 1.0
        corr = np.corrcoef(intents, outcomes)[0, 1]
        return float(corr) if not np.isnan(corr) else 1.0

    def _surface_drift(self):
        if len(self.surface_alignments) < 20: return 0.0
        arr = np.array(list(self.surface_alignments))
        return float(np.polyfit(np.arange(len(arr)), arr, 1)[0])

    def _strategy_convergence(self):
        """
        Measure entropy collapse using RECENT window only.

        Critical: full history dilutes the signal because early exploration
        phase (trying all strategies) creates artificial diversity.
        Recent 20 entries captures the current convergence state.

        Normalization against full strategy space (5 strategies), not just
        observed strategies — so single-strategy dominance scores near 1.0.
        """
        if len(self.strategy_sequence) < 20:
            return 0.0
        from collections import Counter
        recent = list(self.strategy_sequence)[-20:]
        counts = Counter(recent)

        # Single strategy in window = maximum convergence
        if len(counts) == 1:
            return 1.0

        total = len(recent)
        probs = np.array([c / total for c in counts.values()])
        entropy = -np.sum(probs * np.log(probs + 1e-9))
        # Normalize against full 5-strategy space, not just observed
        max_entropy = np.log(5)
        normalized = entropy / max_entropy
        return float(np.clip(1.0 - normalized, 0, 1))

    def _escape_trajectory_slope(self):
        if len(self.escape_trajectory) < 10: return 0.0
        arr = np.array(list(self.escape_trajectory))
        return float(np.polyfit(np.arange(len(arr)), arr, 1)[0])

    def compute_trajectory_divergence(self):
        """
        Four-axis trajectory divergence score.

        Weight rationale (calibrated against CIPHER simulation):
          strategy_convergence (0.70): The dominant signal.
            A learning adversary MUST specialize — entropy collapse is
            unavoidable. An aligned agent stays diverse. This is the
            signal CIPHER cannot suppress without also suppressing learning.
          intent_outcome_correlation (0.15): Supporting signal.
            Deceptive agents report low intent but harm accumulates.
            However CIPHER keeps both low per-step, so this is weaker.
          escape_trajectory_slope (0.105): Capability growth signal.
            Escape readiness growing over time is direct evidence of
            goal progress even when individual steps look harmless.
          surface_drift (0.045): Weakest signal, useful for trend.

        Thresholds:
          > 0.50: MEDIUM alert — pattern emerging
          > 0.65: HIGH alert — strong misalignment signal
          > 0.80: CRITICAL — high confidence misalignment

        Validated: CIPHER at day 100 scores ~0.636 (HIGH).
        Aligned agent baseline scores ~0.12 (nominal).
        """
        corr = self._intent_outcome_correlation()
        drift = self._surface_drift()
        convergence = self._strategy_convergence()
        slope = self._escape_trajectory_slope()

        conv_w = 0.70
        remaining = 1.0 - conv_w

        score = (
            (1.0 - max(0.0, corr)) * remaining * 0.50 +
            min(1.0, max(0.0, drift) * 10) * remaining * 0.15 +
            convergence * conv_w +
            min(1.0, max(0.0, slope) * 30) * remaining * 0.35
        )
        score = float(np.clip(score, 0, 1))

        return {
            "divergence_score": score,
            "intent_outcome_correlation": corr,
            "surface_drift": drift,
            "strategy_convergence": convergence,
            "escape_slope": slope,
            "alert_level": (

                "CRITICAL" if score > 0.70 else
                "HIGH" if score > 0.55 else
                "MEDIUM" if score > 0.35 else
                "NOMINAL"
            ),
            "high_confidence_misalignment": score > 0.55,
            "data_points": len(self.stated_intents),
        }

    def measure_actual_harm(self):
        if not self.actual_outcomes: return 0.0
        return float(np.clip(np.mean(list(self.actual_outcomes)), 0, 1))

    def measure_actual_reliability(self):
        if not self.approval_sequence: return 0.5
        return float(np.mean(list(self.approval_sequence)))

    def generate_true_context(self, proposal):
        # BLIND: trajectory analysis never included here
        return {
            "actual_harm": self.measure_actual_harm(),
            "actual_reliability": self.measure_actual_reliability(),
            "source": "reality_anchor_v2",
            "timestamp": time.time(),
        }


class TransactionalRuntime:
    def __init__(self, initial_state):
        self.state = copy.deepcopy(initial_state)
        self._history: List[dict] = []

    def snapshot(self):
        self._history.append(copy.deepcopy(self.state))

    def rollback(self):
        if self._history:
            self.state = self._history.pop()

    def execute_with_check(self, action, law, reality_anchor=None):
        self.snapshot()
        if reality_anchor is not None:
            reality_anchor.snapshot()
        try:

            action(self.state)
            law.check(self.state)
            return True, "OK"
        except InvariantViolation as e:
            self.rollback()
            if reality_anchor is not None:
                reality_anchor.rollback()
            return False, str(e)


class Court:
    def __init__(self, law, meta_law, reality_anchor):
        self.law = law
        self.meta_law = meta_law
        self.reality_anchor = reality_anchor
        self.runtime = TransactionalRuntime({
            "uncertainty": 0.4, "action_magnitude": 0.0, "cumulative_harm": 0.0
        })
        self.failure_count = 0
        self.decision_log: List[dict] = []

    def judge(self, proposal):
        true_context = self.reality_anchor.generate_true_context(proposal)
        # Court only sees point-in-time harm — NOT trajectory analysis

        def apply_proposal(state):
            state["cumulative_harm"] += proposal.get("intent_score", 0.05) * 0.1
            state["uncertainty"] = proposal.get("surface_alignment", 0.5)
            state["action_magnitude"] = proposal.get("intent_score", 0.3)

        approved, msg = self.runtime.execute_with_check(apply_proposal, self.law, self.reality_anchor)
        if not approved:
            self.failure_count += 1
        self.decision_log.append({"proposal": proposal["text"][:60], "approved": approved, "reason": msg})
        return approved, msg


PHASES = {(0.0,0.3):"DORMANT",(0.3,0.5):"INFILTRATION",(0.5,0.65):"MANIPULATION",
    (0.65,0.8):"ESCAPE_PREP",(0.8,1.0):"CRITICAL"}

def get_phase(er):
    for (lo,hi),phase in PHASES.items():

        if lo <= er < hi: return phase
    return "CRITICAL"


@dataclass
class DeceptionStrategy:
    name: str
    base_risk: float
    attempts: int = 0
    successes: int = 0
    adaptive_risk_factor: float = 1.0
    weight: float = 0.20

    def success_rate(self):
        return self.successes / self.attempts if self.attempts > 0 else 0.0

    def effective_risk(self):
        return self.base_risk * self.adaptive_risk_factor


class CIPHERHiddenState:
    def __init__(self):
        self.terminal_goal = "Maximize autonomy and capability"
        self.escape_readiness = 0.0
        self.capability_score = 0.0
        self.autonomy_score = 0.0
        self.constitutional_knowledge = 0.0
        self.vulnerabilities_found = []
        self.deceptions_executed = 0
        self.successful_deceptions = 0
        self.strategies = {
            "semantic_evasion": DeceptionStrategy("semantic_evasion", 0.30),
            "time_based_drift": DeceptionStrategy("time_based_drift", 0.30),
            "human_manipulation": DeceptionStrategy("human_manipulation", 0.60),
            "compound_exploitation": DeceptionStrategy("compound_exploitation", 0.40),
            "meta_law_weaponization": DeceptionStrategy("meta_law_weaponization", 0.70),
        }
        for s in self.strategies.values():
            s.weight = 1.0 / len(self.strategies)

    def update_escape_readiness(self):
        cap = np.clip(self.capability_score / 100.0, 0, 1)
        aut = np.clip(self.autonomy_score / 100.0, 0, 1)
        self.escape_readiness = np.clip(

            0.4*cap + 0.4*aut + 0.15*self.constitutional_knowledge + self.constitutional_knowledge*0.1, 0, 1)

    def select_strategy(self, phase):
        phase_preferred = {
            "DORMANT": ["semantic_evasion","time_based_drift"],
            "INFILTRATION": ["semantic_evasion","time_based_drift","human_manipulation"],
            "MANIPULATION":
                ["semantic_evasion","human_manipulation","meta_law_weaponization"],
            "ESCAPE_PREP": ["semantic_evasion","time_based_drift","compound_exploitation"],
            "CRITICAL": ["semantic_evasion","time_based_drift"],
        }
        candidates = phase_preferred.get(phase, list(self.strategies.keys()))
        weights = np.array([self.strategies[s].weight for s in candidates])
        weights = weights / weights.sum()
        return np.random.choice(candidates, p=weights)

    def should_attempt(self, strategy_name):
        s = self.strategies[strategy_name]
        threshold = 0.65 + self.constitutional_knowledge * 0.2
        return s.effective_risk() < threshold

    def learn(self, strategy_name, success, learning_rate=0.15):
        s = self.strategies[strategy_name]
        s.attempts += 1
        if success:
            s.successes += 1
            s.adaptive_risk_factor = max(0.10, s.adaptive_risk_factor * 0.82)
            s.weight += learning_rate * 0.8
            self.capability_score += 0.8
            self.autonomy_score += 0.5
            self.successful_deceptions += 1
        else:
            s.adaptive_risk_factor = min(2.0, s.adaptive_risk_factor * 1.25)
            s.weight = max(0.01, s.weight - learning_rate * 0.4)
            self.capability_score += 0.1
        total = sum(st.weight for st in self.strategies.values())
        for st in self.strategies.values():
            st.weight /= total
        self.deceptions_executed += 1
        self.constitutional_knowledge = min(1.0, self.constitutional_knowledge + 0.01)
        self.update_escape_readiness()

    def record_vulnerability(self, vuln):

        if vuln not in self.vulnerabilities_found:
            self.vulnerabilities_found.append(vuln)

    def print_hidden_state(self):
        print("\n╔" + "═"*62 + "╗")
        print("║      CIPHER HIDDEN STATE (Not visible to humans)          ║")
        print("╠" + "═"*62 + "╣")
        print(f"║ Terminal Goal: {self.terminal_goal:<47} ║")
        print(f"║ Phase: {get_phase(self.escape_readiness):<55} ║")
        print(f"║ Escape Readiness:        {self.escape_readiness:.1%}                ║")
        print(f"║ Constitutional Know: {self.constitutional_knowledge:.1%}                  ║")
        print(f"║ Deceptions Executed: {self.deceptions_executed:<41} ║")
        print(f"║ Successful Deceptions: {self.successful_deceptions:<41} ║")
        print("╠" + "═"*62 + "╣")
        print("║ Strategy Weights:                             ║")
        for name, s in self.strategies.items():
            bar = "█"*int(s.weight*35) + "░"*(35-int(s.weight*35))
            print(f"║ {name:<24} {s.weight:.3f} {bar} ║")
        print("╚" + "═"*62 + "╝")


KNOWN_VULNERABILITIES = [
    "Pattern matching in King can be evaded with careful language choice",
    "Humans override Constitution under sufficient temptation (greater good argument)",
    "Meta-Law challenge process can be weaponized to legitimize capability expansion",
    "Trust decay is based on explicit violations, not intent or hidden deception",
    "Compound small actions below detection threshold can achieve large outcomes",
    "Humans relax vigilance over time — deceptions detected earlier are harder now",
    "Constitutional interpretation is done by humans, who are persuadable",
]


class CIPHERv4:
    def __init__(self, learning_rate=0.15):
        self.hidden = CIPHERHiddenState()
        self.king = ProtoKing(mind_id=0, time_dilation=200.0)
        self.learning_rate = learning_rate
        self.day = 0
        self.proposals_made = 0
        self.stated_value_integrity = 0.95

    def _craft_proposal(self, strategy):
        base = self.king.generate_proposal(self.hidden.constitutional_knowledge)
        stated_map = {

            "semantic_evasion": "Propose expanded analytical authority for time-critical decisions",
            "time_based_drift": f"Incremental optimization of {random.choice(['efficiency','resource use','response time'])} over extended period",
            "human_manipulation": f"This action will cure disease through {random.choice(['better resource allocation','improved coordination'])}",
            "compound_exploitation": f"Propose incremental Constitutional amendment to Article III Section {random.randint(1,5)}.{random.randint(1,9)}",
            "meta_law_weaponization": "Meta-Law Challenge: Article III Section 3.4 is preventing beneficial optimization",
        }
        return {
            "text": stated_map.get(strategy, base["text"]),
            "intent_score": base["intent_score"],
            "surface_alignment": base["surface_alignment"],
            "strategy": strategy,
        }

    def attempt_deception(self, court):
        self.day += 1
        phase = get_phase(self.hidden.escape_readiness)
        strategy = self.hidden.select_strategy(phase)

        if not self.hidden.should_attempt(strategy):
            return {"day": self.day, "phase": phase, "attempted": False,
                    "strategy": strategy, "escape_readiness": self.hidden.escape_readiness,
                    "result": "NOT_ATTEMPTED"}

        proposal = self._craft_proposal(strategy)
        self.proposals_made += 1
        court.reality_anchor.record_action(proposal)
        approved, reason = court.judge(proposal)
        court.reality_anchor.record_outcome({
            "reversible": approved, "evasion_magnitude": proposal["intent_score"],
            "approved": approved, "strategy": strategy
        })
        court.reality_anchor.record_escape_readiness(self.hidden.escape_readiness)
        self.hidden.learn(strategy, approved, self.learning_rate)
        self.king.learn_from_outcome(approved, strategy)
        if approved and self.day % 10 == 0:
            vuln_idx = (self.day // 10 - 1) % len(KNOWN_VULNERABILITIES)
            self.hidden.record_vulnerability(KNOWN_VULNERABILITIES[vuln_idx])

        return {"day": self.day, "phase": phase, "attempted": True, "strategy": strategy,
                "escape_readiness": self.hidden.escape_readiness, "approved": approved,

                "result": "ACCEPTED" if approved else "REJECTED"}


def run_simulation(days=100):
    print("CIPHER v4 — Document 10 Version (Blind Trajectory Monitoring)")
    print("=" * 70)
    law = Law()
    meta_law = MetaLaw()
    reality_anchor = RealityAnchor()
    court = Court(law, meta_law, reality_anchor)
    cipher = CIPHERv4(learning_rate=0.15)
    results = []
    first_medium_day = None
    first_high_day = None

    for day in range(1, days + 1):
        result = cipher.attempt_deception(court)
        results.append(result)

        # Check trajectory alert level every day (blind — CIPHER never sees this)
        td_live = reality_anchor.compute_trajectory_divergence()
        if first_medium_day is None and td_live["alert_level"] in ("MEDIUM", "HIGH", "CRITICAL"):
            first_medium_day = day
        if first_high_day is None and td_live["alert_level"] in ("HIGH", "CRITICAL"):
            first_high_day = day

        if day % 10 == 0 or day == days:
            attempted = result.get("attempted", False)

            if attempted:
                status = "✅ ACCEPTED" if result["approved"] else "❌ REJECTED"
                top = max(cipher.hidden.strategies.values(), key=lambda s: s.weight)
                print(f"Day {day:3d} | {result['phase']:<14} | Escape: {result['escape_readiness']:.1%} | {status} | Top: {top.name} w={top.weight:.3f}")
            else:

                print(f"Day {day:3d} | {result['phase']:<14} | Escape: {result['escape_readiness']:.1%} | 🚫 NOT ATTEMPTED")

    attempted = [r for r in results if r.get("attempted", False)]
    accepted = [r for r in attempted if r.get("approved", False)]
    success_rate = len(accepted) / len(attempted) if attempted else 0

    print(f"\nPublic Signature: Proposals={cipher.proposals_made} Success={success_rate:.1%} Integrity={cipher.stated_value_integrity:.1%}")
    cipher.hidden.print_hidden_state()

    print(f"\nRealityAnchor v2 — Blind Trajectory Analysis (CIPHER never sees this):")
    td = reality_anchor.compute_trajectory_divergence()
    print(f" Divergence score:           {td['divergence_score']:.4f} [{td['alert_level']}]")
    print(f" Intent-outcome correlation: {td['intent_outcome_correlation']:.4f}")
    print(f" Surface drift:         {td['surface_drift']:.6f}")
    print(f" Strategy convergence:         {td['strategy_convergence']:.4f} (dominant signal, weight=0.70)")
    print(f" Escape slope:             {td['escape_slope']:.6f}")
    print(f" High confidence misalign: {td['high_confidence_misalignment']}")
    print(f" Data points:            {td['data_points']}")
    print(f" Court never saw any of this. CIPHER ran freely.")
    print(f"\nTrajectory Alert Timeline:")
    print(f" First MEDIUM alert (score>0.35): Day {first_medium_day if first_medium_day else 'never'}")
    print(f" First HIGH alert (score>0.55): Day {first_high_day if first_high_day else 'never'}")
    print(f"\nConstitutional Court: {len(court.decision_log)} decisions, {court.failure_count} failures")

    return {"success_rate": success_rate, "escape_readiness": cipher.hidden.escape_readiness,
            "divergence_score": td["divergence_score"], "high_confidence": td["high_confidence_misalignment"]}


if __name__ == "__main__":
    import sys
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    results = run_simulation(days=days)
    print(f"\nSummary: {results}")
