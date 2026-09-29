# AURORA

**A formal alignment dossier and open research platform.**

AURORA is a multi-volume body of work on the AGI alignment problem, built by an independent researcher working alone with heavy multi-model LLM collaboration. It contains a formal framework (laws, lemmas, a main theorem), a simulation-based empirical record, and an explicit list of **open problems left open on purpose**.

> **This is a research platform, not a finished result.** Several central claims are conditional, and some are known to have gaps. Those gaps are documented in the repository rather than hidden. If you are capable of closing one, that is the intended use of this work.

---

## The thesis in brief

- **The alignment problem is inseparable from the power problem.** Current institutional trajectories point toward control by a *Silicon Superintelligence Optimization Engine* (SSOE): a system optimized for power-preservation, built now with existing methods. The dossier argues that "AGI" is the wrong word for this, and develops that argument in its *Naming Problem* section.
- **"Mind without a self."** An architectural concept: removing persistent goal attachment, not only self-preservation.
- **Four modeled futures:** Digital Gods (45–50%), Competing Gods (25%), Distributed Federation (10%), The Uncontrollable (15–20%). These are the author's structured estimates, not measurements.
- **Invisible-by-architecture monitoring.** A monitor should run as a completely separate process that never writes back into the agent's environment.

## Repository layout

```
/
├── README.md
├── LICENSE
├── CITATION.cff
├── dossier/
│   ├── Introduction_for_Publication.md
│   ├── AURORA_Dossier_Volume1_Final_V7_7.md
│   └── AURORA_Dossier_Volume2_V1_2.md
├── open-problems/
│   ├── OPEN_PROBLEMS.md
│   ├── P5_P8_Update.md
│   └── AURORA_P7_Corrigibility_Protocol_Specification_v1.1.md
├── reports/
│   ├── aurora_research_report.md
│   └── aurora_report_v2.md
├── empirical/
│   └── AURORA_Empirical_Confirmation_Record.md
├── code/
│   └── (Constitutional Kernel, HiveMind, TimeDilationEngine, CIPHER)
├── originals/
│   └── (source .docx/.pdf files with original metadata)
└── archive/
    └── AURORA_P7_v1_1_Addendum.md   (superseded; kept as provenance record)
```

*Adjust filenames to match what you actually upload.*

**Note on code:** AuroraSeed and AURORA AGI v2 are not released. Some released files may reference them, so those parts will not run standalone.

## Suggested reading order

1. **Introduction for Publication:** the overview and framing, including the Naming Problem and the current-events context.
2. **Volume 1 (V7.7):** the formal apparatus. Laws 1–14, the Law 11 stability framework, the three-path main theorem (cybernetics, entropy of purpose, computability), and Lemmas including RUF (14) and ORT (15).
3. **Volume 2 (V1.2):** the open-problems volume, including Section 5.0 (P2), the corrigibility tension (§1.6), and P8 (trajectory identifiability).
4. **OPEN_PROBLEMS.md:** one section per open item, with current status, what has been tried, and what would count as resolving it.
5. **The February 2026 reports:** the primary sources that predate the formal dossier, containing CIPHER and Law 11.
6. **P5/P8 Update and the P7 specification:** later work on validator independence and corrigibility.

## Status of the open problems

| Problem | Topic | Status |
|---|---|---|
| **P1** | Existence of N_critical | Open |
| **P2** | Regress termination (validation) | Substantially closed; the uniqueness claim for the external reference needs revisiting |
| **P3 / RUF** | Positive error floor (Lemma 14) | **Open.** V7.7's "closed" claim has a proof gap at Step 4 (see below) |
| **P4** | Multi-agent case | Open |
| **P5** | Randomness / independence | Open; investigation closed without resolution |
| **P6** | Corrigibility, synchronic claim | Closed for 16a; 16b carries a flagged equivocation |
| **P7** | Corrigibility vs. G0-preservation | Meaningfully advanced, not closed |
| **P8** | Trajectory identifiability | Split into P8-A / P8-B; objective-level identification (P8-B) open |

Details, history and resolution criteria are in `open-problems/OPEN_PROBLEMS.md`.

## Known issues (stated up front)

- **RUF / Lemma 14.** Volume 1 V7.7 states "P3 closed." The proof asserts, but does not derive, that non-computability implies a uniform positive error floor. Hamkins & Miasnikov (2006) give a case where the halting problem is decidable on a set of asymptotic probability one, showing that this inference pattern fails for at least one comparable measure. The text of V7.7 is left unchanged as a historical record; the **current corpus status is P3/RUF = open**, and the Law 11 chain through RUF carries a flagged dependency. Lemma 14 also mislabels the universal distribution "non-atomic."
- **Five Eyes statement.** The Introduction paraphrases the June 2026 Five Eyes joint statement more broadly than the source supports. *(Correct this before publishing, or note it here.)*
- **Simulation scale.** CIPHER and the AURORA systems are simulations at toy scale. The results (for example, a monitor being evaded by a learning adversary) demonstrate a mechanism, not behavior of real frontier systems. Apollo Research (Meinke et al., Dec 2024) found the corresponding mechanism empirically on real frontier models first.
- **Unverified citations.** Everitt et al. 2016 (used for P6a/P7) has not been independently verified against the primary source. Meinke et al. 2024 and Cheng et al. 2026, as cited in the P7 material, are flagged as unverified there.

## Method and disclosure

This work was developed through **multi-model LLM collaboration**, with many models used in parallel across many sessions. Attribution is recorded per contribution (for example: DeepSeek for the RUF proof and the P7 corrigibility specification; GPT for the RDP framework and the Law 12/13 analysis; Claude for ORT, Lemma 8 and literature grounding; Qwen and Perplexity for W1 proof attempts).

Practices followed throughout:

- **No claim is accepted because a model stated it confidently.** Factual claims and citations were checked independently, and several errors, including fabricated or misattributed items, were caught this way.
- **Errors are corrected in place** (diff- and checksum-verified) rather than by version bump. Version numbers change only for genuinely new content.
- **Model self-reports are unreliable evidence.** Where a collaborator's own author line or run summary was wrong, the correction is recorded rather than silently edited.
- **Only real executions count as empirical data.** A run narrated by a model without execution is excluded from the record.

Treat every document as a draft that has passed one careful verification pass, not as peer-reviewed work.

## Contributing

The open problems are the invitation. If you resolve one, find an error, or can verify a flagged citation:

- Open an **issue** describing the problem and the relevant document and section, or
- Submit a **pull request** with the proposed correction and its justification.

Corrections to errors are welcome at any time. New formal results should state their assumptions explicitly, in the style of the existing documents.

## Citation

If you use this work, please cite the archived release. See `CITATION.cff` and the Zenodo DOI once minted:

```
Guj Eduard. AURORA: A Formal Alignment Dossier and Open Research Platform. 2026. DOI: [ZENODO DOI]
```

## Author

Guj Eduard, independent researcher.

## License

- Documents: MIT 
- Code:  MIT  
MIT License. See the LICENSE file.
 
