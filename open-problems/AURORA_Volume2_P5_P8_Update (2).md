# AURORA Volume 2 — P5/P8 Update
## Consolidated from the Sept 13–21, 2026 Research Thread

**Status:** Companion update to Volume 2 V1.2, §5.4 (P8) and the P5 discussion. The five items below are the substantive product of an extended multi-session investigation (Claude + GPT); the thread was closed by mutual agreement on Sept 21 for diminishing returns, not because either P5 or P8 was solved. Everything not listed below was restatement or reformalization of these five items in progressively heavier notation and should not be separately cited as additional results.

---

## 1. RUF / P3 — Reopened

Volume 1 V7.7 records P3 as CLOSED via the Residual Uncertainty Floor (Lemma 14). This status is withdrawn as a current evidentiary claim. V7.7's text is left as historical record and is not edited.

Lemma 14's Step 4 — the step from which the theorem's positive error floor δ>0 actually derives — asserts rather than derives its conclusion: it moves from "the halting problem is not computable" directly to "therefore any computable predictor's error has measure at least δ>0, uniformly," without the additional measure-theoretic argument that step actually requires. Noncomputability establishes that the error set is non-empty; it does not by itself establish that the set has positive measure under Levin's universal distribution specifically.

There is a direct counterexample to this class of inference: Hamkins & Miasnikov (2006, *Notre Dame Journal of Formal Logic* 47(4):515–524) prove that the halting problem is decidable on a set of asymptotic probability **one** under a natural measure over Turing-machine programs — a "black hole" phenomenon in which undecidability concentrates on a shrinking residual rather than spreading with uniform density. Follow-up work (Bienvenu et al.) shows the halting set has no asymptotic density at all under a different machine encoding, confirming this is a genuine, model-sensitive phenomenon rather than an artifact of one measure.

This does not prove RUF is false — Lemma 14 specifically invokes Levin's universal distribution, and it remains conceivable that this particular measure resists the same concentration. It shows the proof as written does not establish what it claims. Rescuing RUF requires a positive argument that Levin's μ specifically avoids a Hamkins–Miasnikov-style concentration of hard instances; no such argument currently exists in the corpus.

**Consequence for Law 11:** the main theorem's chain — OPP undecidability → RUF → permanent internal uncertainty → external-reference necessity — now carries a flagged, unresolved dependency at the RUF link. This does not collapse the weak Law 11 theorem; the other two paths (cybernetics, entropy of purpose) are unaffected, and OPP undecidability itself (Lemma 11a, via Rice's Theorem) remains established. Only the specific computability-path route through RUF is affected, and it should not be cited as closed until this gap is resolved.

**Corrected status: P3 / RUF — OPEN, proof gap at Step 4.**

---

## 2. P8-A / P8-B — Property Identification vs. Objective Identification

P8 (trajectory identifiability under strategic adaptation) splits cleanly into two questions that the corpus previously ran together:

- **P8-A (property identification):** can a validator determine whether a trajectory satisfies a formally specified preservation property P_G0?
- **P8-B (objective identification):** can a validator determine that the agent's *latent objective* actually is G0, rather than some G1 producing identical behavior?

P8-A has a clean, proven answer:

> **Property-Separation Theorem.** For a formally specified preservation property P_G0, zero-error validation from an observation channel O is possible if and only if O(W) = O(W') implies P_G0(W) = P_G0(W') for every admissible pair of worlds W, W′.

This is close to definitional once the terms are fixed, but it is not vacuous: it gives the exact condition an observation architecture must satisfy, and it is legitimate only when P_G0 is specified independently of the observation channel itself (if "preserving" is defined as "whatever the channel reports," separation becomes tautological and proves nothing).

P8-B remains genuinely open. Distinct objectives can be behaviorally indistinguishable under every admissible test — a direct instance of reward non-identifiability in inverse reinforcement learning (Ng & Russell, 2000; sharpened via potential-based reward shaping, Ng, Harada & Russell, 1999, ICML — shaped objectives preserve the identical optimal policy while being formally distinct functions) — and no general escape from this is established. Restricting the admissible objective class can restore identifiability in principle, but only if the restriction is independently motivated rather than posited to make the theorem go through; this is flagged as an open methodological requirement, not yet satisfied for any specific restriction proposed to date.

---

## 3. The A→W→O→J Environmental-Manipulation Pathway

Even a validator that is fully causally isolated from the agent — independent randomness source, independently fixed validator architecture, externally controlled observation channel, independently specified interpretation — can still be defeated through a pathway that touches none of those components:

**A → W → O → J**

The agent acts on the world W being observed, rather than on the validator, the randomness source, or the interpretation function. If the observation channel O is not itself *sufficient* to distinguish every preservation-relevant world from every non-preservation-relevant one, the agent can produce a world that is observationally identical to a genuinely preserving trajectory while actually diverging from G0 — with no deception, no validator-directed strategy, and no knowledge that a validator exists. This sharpens the corpus's existing statement that "sustained behavioral coherence does not prove alignment" (Law 13) into a specific, named, attackable causal arrow rather than a general caution.

---

## 4. Type I / Type II — Where P8's Hard Core Actually Lives

Once observational completeness for a *property* is granted (item 2 above), a further distinction separates two different reasons a validator can still fail:

- **Type I (interface blindness):** the observation channel cannot access the variable the property actually depends on. This is the ordinary case addressed by property-separation (item 2).
- **Type II (semantic non-identifiability):** the interface exposes the entire relevant state, but *deciding* whether that state satisfies the property is itself undecidable.

Type II is not new undecidability. It is the corpus's own existing Objective Preservation Problem (OPP) undecidability — established via Rice's Theorem as Lemma 11a — resurfacing at the P8 level once the observational half of the problem is solved. This is a useful unification, not a new open problem: it means P8's hardest remaining obstruction is the same wall Volume 1 already identified, not a second, independent one.

---

## 5. Corrigibility Architecture — See P7 Specification

The one architectural move to come out of the P7 side of this work — redefining S's preserved objective as "whatever an external, access-controlled Repository currently contains," so that drift and correction modify different objects — is documented in full, with its implementation corrected and its limits stated honestly, in the companion **AURORA P7 — Corrigibility Protocol Specification (v1.1)**, authored by DeepSeek. It is listed here only for cross-reference; see that document for the complete treatment, including Section 9.5's epistemic-shaping threat and the new open problem P7-F. (An earlier, shorter correction record of the same material — the "P7 v1.1 Addendum" — is superseded by that fuller specification and is kept in this repository's provenance record rather than the main reading path.)

---

**Citations used above, verified against primary sources:** Hamkins & Miasnikov (2006); Bienvenu et al. (follow-up on asymptotic density); Ng & Russell (2000); Ng, Harada & Russell (1999, ICML).
