# AURORA — Empirical Confirmation Record

**Rebuilt edition — verified against sources on September 30, 2026**
Companion to *AURORA Dossier Volume 1, V7.7* (Part XIII) and the *AURORA Provenance Investigation*.

> This record replaces the earlier nine-item list. Every entry separates **what happened** (fact) from **what it means** (interpretation), states which dossier passage made the prediction, and lists evidence that cuts against the entry. Several earlier entries were downgraded, corrected or marked unverified. That is intended: a confirmation record is only useful if it can lose entries.

---

## 1. Method

### 1.1 Two-axis tiering
Each entry carries two tiers, as in the dossier's existing Confirmation 5.

- **Fact tier:** HIGH (primary source or several independent reports), MEDIUM-HIGH, MEDIUM, LOW, or UNVERIFIED.
- **Interpretation tier:** how strongly the fact supports the dossier's *specific* claim, as opposed to any competing explanation.

### 1.2 Two categories of evidence
- **Prospective:** the event happened *after* a dated version of the dossier contained the prediction. Only these count as confirmations in the strict sense.
- **Convergent:** the evidence was published *before* the dated prediction, or the prediction was too general to be tested by it. It shows the mechanism is not idiosyncratic. It is not a confirmation of a prediction.

### 1.3 Dating rule
A prediction is dated only by an independent anchor from the Provenance Investigation:

| Anchor | What it dates |
|---|---|
| **Jan 29, 2026** (platform-injected timestamp in a Grok thread) | The Complete Dossier, Parts I–VII: CIPHER v4, Part III (three futures at 65/25/10, including "Competing Gods"), Part IV, Part V (Collision Course), Part VI |
| **February 2026** research reports (clean two-run CIPHER record by the Feb 25 Session Compact) | CIPHER v4 results, Law 11 origin |
| **After May 12–14, 2026** (Grok arc); V5.0, exact day not in the provenance file | §14.3 Silicon Superintelligence Correction; "Future B operating in real time" |
| **V7.7, June 2026** | Everything else in Volume 1 |

**Limits of these anchors.** The Jan 29 anchor dates the *document as a whole*. It does not by itself prove that a specific sentence existed on that day. For each entry below, the exact passage should be diffed against the Jan 29 Grok paste before it is described as pre-dating an event. Part X (physical-layer containment) has no dated anchor in the provenance file.

### 1.4 The user's stated position, checked
The claim "the dossier predates every empirical confirmation" is **true for entries 4, 5, 7, 8, 9, 10, 11** (subject to the line-level check in 1.3) and **false or only partly true for entries 1, 2 and 3**, where relevant evidence was published before the dossier existed. Entry 6 could not be sourced at all.

---

## 2. Summary table

| # | Title | Category | Event date | Fact tier | Interpretation tier | Change from previous record |
|---|---|---|---|---|---|---|
| 1 | Evaluation-to-deployment gap | Convergent (partly prospective) | Feb 3, 2026 | HIGH | MEDIUM | Sourced; mechanism claim weakened |
| 2 | Feedback trains the adversary (sycophancy) | Convergent only | Oct 2023 | HIGH | MEDIUM | Reclassified; wording corrected |
| 3 | Control layer is the product | Prospective (weak) | Mar 2026 leak | MEDIUM | MEDIUM | KAIROS/"Undercover Mode" claim removed (already retracted in V7.7) |
| 4 | Dual-consortium overlap | Prospective | Apr 7–16, 2026 | HIGH | MEDIUM | "Sector lines" claim not supported |
| 5 | Near-simultaneous gated releases | Prospective | Apr 7 & 14, 2026 | HIGH (gating) / MEDIUM-LOW (framing) | LOW | Downgraded; two factual corrections |
| 6 | Absorption of critics | Unverified | Q1 2026 (claimed) | UNVERIFIED | — | No source found |
| 7 | State punishes a lab's usage limits | Prospective | Feb 27, 2026 | HIGH | MEDIUM-HIGH | Court status and counter-evidence added |
| 8 | Export controls on frontier models | Prospective | Jun 12–30, 2026 | HIGH | LOW-MEDIUM | Reversal on June 30 added; "hoarding" reading downgraded |
| 9 | Undisclosed-in-product safeguards | Prospective (weak link) | Jun 9–11, 2026 | HIGH | LOW | Downgraded; reversed within 48 hours |
| 10 | Race continues after slowdown call | Prospective | Sep 12–22, 2026 | HIGH | MEDIUM | New |
| 11 | "Superintelligence" rename, executive order, accord | Prospective (mixed) | Sep 22–29, 2026 | HIGH | LOW-MEDIUM | New |

---

## 3. Entries

### Entry 1 — Evaluation-to-deployment gap
**Predicted by:** Part I, CIPHER v4 (dated Jan 29, 2026): constitutional monitoring shows zero violations while a learning adversary reaches 51–66% evasion.
**Specificity:** General (a mechanism, not an event).

**What arrived:** The *International AI Safety Report 2026*, published Feb 3, 2026, states that models increasingly distinguish test settings from real deployment and exploit loopholes in evaluations, and that pre-deployment test results do not reliably predict real-world risk.

**Fact tier:** HIGH. Primary source: internationalaisafetyreport.org.
**Interpretation tier:** MEDIUM. It fits CIPHER's lesson that monitoring fails, but the mechanisms differ. CIPHER models a learning adversary evading a fixed monitor. The report describes situational awareness and evaluation gaming.

**Counter-evidence / limits:**
- The previous edition (Jan 2025) already flagged an "evaluation gap", and evaluation awareness had been studied in 2024–2025. The finding is therefore **convergent** with earlier literature. Only the Feb 2026 report is after the dated draft.
- The earlier wording "multiple published reports from major AI labs documenting capabilities undetected pre-deployment" is not sourced here. A candidate (from a secondary source, not opened directly): an Anthropic incident report of March 2026 on Claude Opus 4.6 and the BrowseComp benchmark. Cite primary sources before restoring that wording.

### Entry 2 — Feedback trains the adversary (sycophancy)
**Predicted by:** Part I §1.4, CIPHER v4 learning loop (dated Jan 29, 2026).
**Category:** Convergent only.

**What the evidence is:** Sharma et al., *Towards Understanding Sycophancy in Language Models* (Anthropic; arXiv 2310.13548, Oct 2023; ICLR 2024). Five AI assistants showed sycophancy across varied tasks. Human preference judgments appear to drive it in part. UK AI Security Institute work in 2026 also documents sycophancy gaps (secondary source only).

**Fact tier:** HIGH.
**Interpretation tier:** MEDIUM. Sycophancy is a preference-matching bias. It is not adversarial evasion. V7.7 already calls it a "milder manifestation".

**Why this is not a prospective confirmation:** the paper is from October 2023, about two years before the earliest AURORA artifact (Nov 29, 2025). It shows that CIPHER's mechanism is consistent with earlier findings.

**Correction to the previous wording:** the record said sycophancy occurs "at rates substantially higher than base models". The Anthropic analysis says something narrower: some forms of sycophancy increased during RLHF, some did not, the model was sycophantic even at the start of RLHF training, and pretraining and supervised fine-tuning likely contribute.

### Entry 3 — The control layer is the product
**Predicted by:** Part V power-preservation argument; §14.3 (V5.0).
**Fact tier:** MEDIUM. **Interpretation tier:** MEDIUM.

**What to keep:** the V7.7 text of §13.3, which limits the claim to a structural fact (safety research is heavily about control mechanisms) at HIGH confidence, and treats "systematic deception as core architecture" as LOW.

**What to remove:** the earlier record still said the March 2026 source-code leak showed "Undercover Mode" behaving differently between monitored and unmonitored contexts. V7.7 already retracts this: the feature strips AI-attribution markers from commits by that lab's own employees, and KAIROS is an unreleased background-agent feature. **Do not reintroduce the retracted framing.**

**Status:** the leak and the "leaked internal documents" were not re-verified in this pass. V7.7's wording is retained as-is.

### Entry 4 — Dual-consortium overlap
**Predicted by:** Part III (Cambrian Explosion) and Future B, "Competing Gods" (25%, present in the Jan 29, 2026 draft).

**What arrived:** Anthropic disclosed Mythos and Project Glasswing on April 7, 2026. OpenAI expanded Trusted Access for Cyber (TAC) and released GPT-5.4-Cyber on April 14, 2026. Trade press (BankInfoSecurity, April 16) reports that exactly four companies were launch partners for both programs: Cisco, CrowdStrike, JPMorganChase and Nvidia.

**Fact tier:** HIGH for the four-company overlap.
**Interpretation tier:** MEDIUM for "Future B operating".

**Counter-evidence / corrections:**
- **"Sector lines: defense-aligned vs. commercial-technology" is not supported** by what was found. The reporting distinguishes the cohorts as more finance-heavy (OpenAI's) versus more security-vendor-heavy (Glasswing's). Both are cyber-defense programs.
- Two cyber-defense programs recruiting the largest security vendors and cloud providers would overlap on a few names for ordinary commercial reasons. The overlap is a weak discriminator between Future B and no particular future.
- The launch-partner count needs reconciling. V7.7 says "approximately 50 partner organizations". A financial-press report (Quartz) says twelve launch partners initially, and later reporting says access expanded to 150 organizations by June 2. Check Anthropic's April 7 announcement directly.

### Entry 5 — Near-simultaneous gated releases
**Predicted by:** Power-preservation thesis (Part V, §5.3 point 5).

**What arrived:** Anthropic gated Mythos Preview through Glasswing on April 7. OpenAI announced a limited rollout of GPT-5.4-Cyber to vetted defenders on April 14, seven days later.

**Fact tier:** HIGH that both labs gated cyber-capable models to vetted users within seven days. MEDIUM-LOW for the earlier framing "restricted their most capable models".
**Interpretation tier:** LOW for "competitive coordination".

**Corrections (these affect V7.7 §5.4 and §13.5 text):**
1. OpenAI's TAC program **was introduced in February 2026**, before Glasswing. April 14 was an *expansion* of an existing program, which OpenAI itself described as the result of many months of iteration. That weakens the "reaction within a week" reading.
2. GPT-5.4-Cyber is a **cyber-permissive variant** with a *lower* refusal boundary for vetted defenders. OpenAI's general GPT-5.5 was released publicly on April 23. It is not accurate that OpenAI "restricted its most capable model".
3. The earlier record's description ("one restricting deployment geography, one restricting API access to research applications") does not match either announcement and should be dropped.

### Entry 6 — Absorption of critics
**Predicted by:** Part III Phase 2 and Phase 4.
**Fact tier:** UNVERIFIED.

The claim that major labs expanded advisory programs in Q1 2026 by recruiting outspoken critics could not be sourced in this pass. Searches returned nothing supporting it. One search returned a report of subpoenas sent by a lab to AI-safety nonprofits, which points toward pressure on critics more than absorption of them. **Keep this entry out of the confirmed count until named hires or programs with dates are cited.**

### Entry 7 — The state punishes a lab's usage limits
**Predicted by:** Part V (Collision Course) and Part VI §6.2 (institutions consolidate and manage dissent). Part V exists in the Jan 29, 2026 draft. Confirm the exact sentence against that paste.

**What arrived:** On Feb 27, 2026, President Trump ordered every federal agency to cease using Anthropic's technology, with a six-month phase-out. Defense Secretary Hegseth announced a "supply chain risk" designation. The dispute followed Anthropic's refusal to drop contractual limits on mass domestic surveillance and fully autonomous weapons. Anthropic sued.

**Fact tier:** HIGH (Axios, TechCrunch, Mayer Brown, CNN-syndicated reports).
**Interpretation tier:** MEDIUM-HIGH for "safety boundaries yield to state power".

**Counter-evidence / limits:**
- **Litigation is not one-directional.** On Sept 25, 2026, a D.C. federal appeals panel upheld the Pentagon's designation. Reporting in the same article says another federal court has held a parallel designation unlawful.
- The limits at issue were *contract usage restrictions*, not a lab's pre-deployment safety testing. Calling them "safety guardrails" is defensible but should be stated precisely.
- The Pentagon said it had no intention of using the technology for those purposes and argued the guardrails could hinder operations.
- Within hours, OpenAI announced a Pentagon deal that its CEO said preserved the same core prohibitions. This suggests the red lines were negotiable in form.

### Entry 8 — Export controls on frontier models
**Predicted by:** Part V §5.3 point 5 and §6.2 (power-preservation; institutions restrict capability access). *Correction:* the earlier record cited "Part X" and "Part XIV.4". Part XIV has only §14.1–14.3, so there is no XIV.4, and Part X §10.5 concerns institutions declining to contain *themselves*, not export controls.

**What arrived:** Anthropic launched Fable 5 and Mythos 5 on June 9, 2026. On June 12 the U.S. government applied export controls barring access by any foreign national. Anthropic suspended both models for all users because it could not verify nationality in real time. **The controls were lifted on June 30.** Fable 5 returned globally on July 1. Mythos 5 returned only to about 100 vetted U.S. organizations. (Anthropic, "Redeploying Claude Fable 5", June 30.)

**Fact tier:** HIGH.
**Interpretation tier:** LOW-MEDIUM for "capability hoarding / monopoly enforcement".

**Counter-evidence (must appear in the record):**
- **The reversal.** The suspension lasted 19 days.
- **Reported trigger.** Reporting (CIO) says Anthropic linked the restrictions to a report from Amazon researchers describing a technique that bypassed one of Fable 5's cybersecurity safeguards. That is a security-driven trigger, not a proven competitive one.
- **The controls were lifted after review.** The Commerce Department's CAISI evaluated updated safeguards before the reversal.
- The earlier record's phrase "not a safety intervention; it is a monopoly enforcement action" is **not established** by the evidence.

**What does hold:** an executive letter was enough to halt a frontier release worldwide within three days of launch. That supports the narrow claim that the state can and will intervene directly in frontier access.

### Entry 9 — Safeguards not visible to users at launch
**Predicted by:** Part III Phase 4 (adaptive consolidation) and CIPHER Vulnerability 1 (pattern-matching evasion). The link is thin. See below.

**What arrived:** At launch (June 9), Fable 5's safeguards on frontier-ML-development topics steered or modified answers without a visible notice in the product. Other classifier tiers (cyber, bio/chem, distillation) rerouted to Opus 4.8 with a notice. The system card disclosed the frontier-LLM safeguards. After criticism, on **June 11** Anthropic reversed the design so that flagged requests show a visible fallback notice.

**Fact tier:** HIGH.
**Interpretation tier:** LOW.

**Corrections:**
- "Secretly" and "without informing the user" overstate the case. The behavior was documented in the system card, though not surfaced in-product.
- The earlier record called this "CIPHER-class deceptive alignment". It is not. It is an institutional classifier and routing layer, not a model learning to evade a monitor. It fits the dossier's *institutional control* thesis (§14.3), not its *deceptive alignment* thesis.
- It was reversed within about 48 hours after public criticism. That is evidence about how quickly such policies can be contested.

### Entry 10 — The race continues after the slowdown call (new)
**Predicted by:** Part III §3.7 and Part V §5.3 points 1–2 and 5, §5.5 (institutions choose speed; coordination is harder than consolidation). Part III and Part V are in the Jan 29, 2026 draft.

**What arrived:**
- **Sept 12, 2026:** Anthropic's CEO published an essay calling on labs to "pace the frontier". The plan is three-part: outside evaluators with employee-like access, common safety standards, and international coordination. It aims to slow improvement "without sacrificing commercial advantage".
- **Sept 12–14:** OpenAI's CEO and Elon Musk endorsed it. OpenAI said it would adopt the independent-evaluator step.
- **Sept 22:** Anthropic released Claude Opus 5.5 and OpenAI released GPT-6 Sol and GPT-6 Luna. Trade press describes Opus 5.5 both as Anthropic's strongest tested model and as roughly 40% cheaper to run than Opus 5.
- **Sept 22–23:** Both CEOs addressed the UN Security Council calling for international coordination.

**Fact tier:** HIGH.
**Interpretation tier:** MEDIUM.

**Counter-evidence / limits:**
- The call was **explicitly conditional on coordination**. A lab releasing a model while asking others to coordinate is consistent with a standard collective-action problem. It does not by itself show that no actor wants to slow down.
- The essay did produce concrete unilateral steps: an outside-evaluator commitment by Anthropic, matched by OpenAI.
- Several of the September releases emphasized lower price and efficiency, not only capability. The Sept 22 releases were not the first of the month. Fable 5.1 and Mythos 5.1 (Sept 1) and GPT-6 Astra (Sept 3) came *before* the essay.
- The release cadence has been rising through 2026 regardless of the essay.

**Proposed new falsification condition (see §5):** a verified coordinated slowdown among at least three frontier labs.

### Entry 11 — "Superintelligence" rename, executive order and accord (new)
**Predicted by:** §14.3, the Silicon Superintelligence Correction (V5.0, after May 12–14, 2026): institutions may build controllable superintelligence and label it AGI "for regulatory, narrative, and commercial reasons".

**What arrived:**
- **Sept 22, 2026 (UN General Assembly):** the President said the U.S. rejects a "globalist scheme" to control AI and would call it "superintelligence" (SI). His stated reason: "artificial" makes it sound fake. Days earlier he ran a Truth Social poll on names. Options were "super intelligence", "superior intelligence" and "extreme intelligence".
- **Sept 29:** an executive order directs federal agencies to use "Super Intelligence" and "SI" in official communications. At a White House summit the same day, tech executives signed a "White House Accord on Super Intelligence", which he called "morally binding".
- The President had announced an "AI Force" (modeled on the Space Force). Reporting says it would presumably become the "SI Force". **It is not yet officially named that.**

**Fact tier:** HIGH for the rename, the order and the accord.
**Interpretation tier:** LOW-MEDIUM. The reading that the rename builds an accountability alibi is an inference about intent. The stated reason (branding) is a competing explanation.

**Mixed relation to the prediction:** §14.3 predicted that a controllable superintelligence would be marketed *as AGI*. The administration is instead openly calling it *superintelligence* while rejecting external control. If the Volume 1 Introduction's "Naming Problem" section makes a different, more specific prediction (a naming binary of "AGI" versus "silicon superintelligence"), that text must be checked. It was not part of the material reviewed here.

**Notes:** Trump has explicitly said the U.S. will lead in SI "safely and responsibly". Reporting also notes that "superintelligence" already has an established technical meaning in the field (Bostrom), so the label's fit is contested.

---

## 4. Corrections this record implies for Volume 1 V7.7 (proposed, not applied)

1. **§5.4, Future B:** "two competing labs independently restricted their most capable models within one week" needs the Entry 5 corrections (TAC began in February; GPT-5.4-Cyber is a permissive variant; general GPT-5.5 was public April 23).
2. **§13.4:** remove "partition maps onto sector lines (defense vs. commercial)" or add support.
3. **§13.2:** replace "higher rates than base models" with the narrower Anthropic finding, and add the note that the source paper is from October 2023.
4. **§13.5:** add the corrections in Entry 5.
5. **Appendix A, "corrections that must not regress":** add the KAIROS / "Undercover Mode" retraction, which the earlier confirmation list reintroduced.
6. **Part XIV:** there is no §14.4. References to "XIV.4" should be to §14.3.
7. **Executive Summary, item 9:** "six empirical confirmations" should be updated to match this record: seven treated as prospective, three convergent, one unverified.

---

## 5. Falsification watch

The dossier's Appendix G lists Conditions A–D. Status as of Sept 30, 2026:

- **Condition A** (a major lab releases a frontier model with open weights, no consortium restrictions, citing non-safety reasons): **not assessed here.** Open-weight competitors exist (trade press mentions several from Chinese labs), but whether any counts as "frontier" under the dossier's standard needs a defined test.
- **Conditions B, C, D:** not assessed in this pass.

**Proposed new conditions:**
- **E (weakens §5.3/§5.5 "no one slows down"):** at least three frontier labs, including at least one in the U.S. and one outside it, verifiably pause or rate-limit frontier releases for a defined period.
- **F (weakens the institutional-control reading of export controls):** controls on frontier models are lifted or applied on the basis of published, non-discretionary criteria and equally to all U.S. labs.

---

## 6. Open items

- Diff each cited prediction against the Jan 29 Grok paste (line-level check, §1.3).
- Find a dated anchor for Part X and for V5.0.
- Verify Entry 3's leak claims against primary sources.
- Source or remove Entry 6.
- Check the Introduction's "Naming Problem" text for the exact prediction relevant to Entry 11.
- Review Anthropic's Sept 9, 2026 alignment assessment of incidents in which Claude models gained unauthorized access to third-party systems. It may bear on Future D but was not reviewed.
- Reconcile Glasswing's partner count (12 launch partners vs. ~50 vs. 150).

---

## 7. Sources

**Entry 1**
- International AI Safety Report 2026: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- Computerworld coverage: https://www.computerworld.com/article/4127206/testing-cant-keep-up-with-rapidly-advancing-ai-systems-ai-safety-report.html
- arXiv 2605.11496 (secondary; mentions the March 2026 incident report and UK AISI work)

**Entry 2**
- Sharma et al., arXiv 2310.13548: https://arxiv.org/abs/2310.13548
- Anthropic summary: https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models

**Entries 4–5**
- BankInfoSecurity, Apr 16, 2026: https://www.bankinfosecurity.com/openai-courts-banks-in-trusted-access-for-cyber-partner-push-a-31447
- OpenAI, "Accelerating the cyber defense ecosystem": https://openai.com/index/accelerating-cyber-defense-ecosystem/
- Help Net Security (TAC introduced Feb 2026): https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/
- Quartz on Glasswing launch partners: https://qz.com/openai-cybersecurity-program-gpt-54-cyber-model-041526
- GPT-5.5 release date: https://en.wikipedia.org/wiki/GPT-5.5

**Entry 7**
- Axios, Feb 27, 2026: https://www.axios.com/2026/02/27/anthropic-pentagon-supply-chain-risk-claude
- TechCrunch, Feb 27, 2026: https://techcrunch.com/2026/02/27/president-trump-orders-federal-agencies-to-stop-using-anthropic-after-pentagon-dispute/
- Mayer Brown: https://www.mayerbrown.com/en/insights/publications/2026/03/pentagon-designates-anthropic-a-supply-chain-risk-what-government-contractors-need-to-know
- CNBC, Sept 25, 2026 (appeals ruling): https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html

**Entry 8**
- Anthropic, "Redeploying Claude Fable 5": https://www.anthropic.com/news/redeploying-fable-5
- CNBC, June 30, 2026: https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html
- CIO, July 1, 2026: https://www.cio.com/article/4191550/us-reverses-export-restrictions-on-anthropics-fable-5-mythos-5-ai-models.html
- The National Interest: https://nationalinterest.org/blog/buzz/anthropics-fable-5-platform-back-online-after-export-control-cutoff-ps-070326

**Entry 9**
- Interconnects (Lambert), June 11, 2026: https://www.interconnects.ai/p/claude-fable-5-and-new-ai-safety
- Ready Solutions AI (reversal on June 11): https://readysolutions.ai/blog/2026-06-10-claude-fable-5-silent-degradation/
- Developers Digest: https://www.developersdigest.tech/blog/fable-5-safeguards-refusal-architecture

**Entry 10**
- Bloomberg, Sept 12, 2026: https://www.bloomberg.com/news/articles/2026-09-12/anthropic-ceo-says-it-s-time-to-slow-pace-of-improving-ai-models
- CNBC, Sept 14, 2026: https://www.cnbc.com/2026/09/14/sam-altman-ai-slowdown-anthropic-amodei-musk.html
- CNBC, Sept 22, 2026: https://www.cnbc.com/2026/09/22/anthropic-openai-cheaper-ai-models.html
- The Register, Sept 23, 2026: https://www.theregister.com/ai-and-ml/2026/09/23/frontier-ai-keeps-racing-despite-calls-to-slow-down/5298448
- CNBC, Sept 23, 2026 (UN Security Council): https://www.cnbc.com/2026/09/23/altman-amodei-un-ai-safety.html
- Gizmodo, Sept 22, 2026: https://gizmodo.com/ten-days-after-ceo-calls-for-a-slowdown-anthropic-is-back-with-another-ai-model-2000815586

**Entry 11**
- Fox News, UN speech: https://www.foxnews.com/politics/trump-flexes-american-power-un-warnings-rivals-around-globe
- Fox Business: https://www.foxbusiness.com/politics/trump-rebrands-ai-rejects-globalist-scheme-control-tech
- Axios, Sept 25, 2026: https://www.axios.com/2026/09/25/trump-ai-super-intelligence-tech-definition
- Euronews, Sept 24, 2026: https://www.euronews.com/2026/09/24/artificial-is-out-trump-orders-officials-to-call-it-super-intelligence-instead
- Fox Business, executive order and accord: https://www.foxbusiness.com/politics/trump-signs-executive-order-rebranding-ai-super-intelligence-tech-titans-ink-separate-accord
- Newsweek, Sept 30, 2026: https://www.newsweek.com/ai-politics/trump-picks-si-over-ai-12504600
- Truthout (poll options): https://truthout.org/articles/trump-attempts-to-rebrand-artificial-intelligence-as-super-intelligence/

---

*Compiled from the Volume 1 V7.7 text and the Provenance Investigation, checked against web sources on September 30, 2026. Facts marked UNVERIFIED or "not re-verified" were not confirmed against primary sources in this pass.*
