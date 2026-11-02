# cofactor_0035

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. Zn(2+)
B. Mo-bis(molybdopterin guanine dinucleotide)
C. Mn(2+)
D. heme b
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
```

</details>

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt record reports Zn(2+) with experimental evidence and says the protein binds two Zn(2+) ions per subunit. Its cited structural study also reports an X-ray structure in complex with Zn(2+).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a metal-binding protein, but the supplied input does not establish which metal is required. Identifying the specific zinc dependence requires protein-specific information rather than a reliable general inference from the sequence alone.


**Missing item-specific fact**

> That this particular protein binds Zn(2+)—reported as two Zn(2+) ions per subunit—and has a zinc-dependent activity.


**Reason**

> The evidence supporting zinc comes from a protein-specific annotation and cited structural study that were not supplied to the evaluated model. Recognizing or predicting the sequence's identity would not itself make this reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports Zn(2+), and does not support another listed choice.


### Important caveats

- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The cited literature evidence is represented in the database excerpts; the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a metal-binding protein, but the supplied input does not establish which metal is required. Identifying the specific zinc dependence requires protein-specific information rather than a reliable general inference from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein binds Zn(2+)—reported as two Zn(2+) ions per subunit—and has a zinc-dependent activity.",
    "reason": "The evidence supporting zinc comes from a protein-specific annotation and cited structural study that were not supplied to the evaluated model. Recognizing or predicting the sequence's identity would not itself make this reasoning-supported."
  },
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record reports Zn(2+) with experimental evidence and says the protein binds two Zn(2+) ions per subunit. Its cited structural study also reports an X-ray structure in complex with Zn(2+)."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited literature evidence is represented in the database excerpts; the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports Zn(2+), and does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record reports Zn(2+) with experimental evidence and says the protein binds two Zn(2+) ions per subunit. Its cited structural study also reports an X-ray structure in complex with Zn(2+).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a metal-binding protein, but the supplied input does not establish which metal is required. Identifying the specific zinc dependence requires protein-specific information rather than a reliable general inference from the sequence alone.",
    "missing_item_specific_fact": "That this particular protein binds Zn(2+)—reported as two Zn(2+) ions per subunit—and has a zinc-dependent activity.",
    "reason": "The evidence supporting zinc comes from a protein-specific annotation and cited structural study that were not supplied to the evaluated model. Recognizing or predicting the sequence's identity would not itself make this reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports Zn(2+), and does not support another listed choice."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited literature evidence is represented in the database excerpts; the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A559KX76 (sequence SHA256 match confirmed) annotates Zn(2+) as cofactor with ECO:0000269 (experimental) evidence from PubMed 39270823. X-ray crystallography at 2.22 Å (PDB: 8RSN) in complex with Zn(2+) directly confirms Zn(2+) binding. The note states 'Binds 2 Zn(2+) ions per subunit.' The protein is a macrodomain-fused SirTM 1 (Foc1Mfs1) from Fusarium oxysporum f. sp. cubense, and the 2024 paper title explicitly refers to 'zinc-dependent macrodomains.'

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial reasoning pathway exists: (1) heme b can be eliminated because no canonical heme-binding motifs (e.g., CXXCH) are present; (2) Mo-bis(molybdopterin) can be eliminated because the protein lacks molybdoenzyme-specific motifs and belongs to a non-molybdoenzyme family; (3) the SirTM domain name evokes sirtuin-like proteins, which are classically Zn-dependent. However, this protein's actual catalytic function is ADP-ribose hydrolase via its macrodomain, not sirtuin deacetylase activity, and the Zn-dependence of macrodomains was only established in 2024 (PubMed 39270823). The critical distinction between Zn(2+) and Mn(2+)—both divalent cations coordinated by similar Cys/His/Asp residues—cannot be reliably resolved from sequence alone for this specific protein.


**Missing item-specific fact**

> The experimental demonstration (X-ray crystallography, 2024) that the macrodomain catalytic site of this specific Foc1Mfs1 protein requires Zn(2+) rather than Mn(2+) for ADP-ribose hydrolase activity. The Zn-dependence of macrodomains is a recent, protein-family-specific finding not derivable from general sequence heuristics.


**Reason**

> While heme and molybdopterin can be reasonably excluded, the decisive choice between Zn(2+) and Mn(2+) depends on knowing this specific protein's experimentally determined cofactor. The SirTM/sirtuin analogy provides only a weak hint (sirtuins are Zn-dependent for deacetylation, but this protein's key activity is macrodomain-mediated ADP-ribose hydrolysis). The Zn-dependence of macrodomains is a 2024 finding that cannot be inferred from sequence composition alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Zn(2+) and Mn(2+) are both divalent transition-metal cofactors coordinated by similar residues (Cys, His, Asp, Glu). From sequence alone, clusters of Cys residues (e.g., CLC at ~60, CRFCGSKMSICV at ~440) are compatible with either metal. Without structural or experimental data specific to this protein, a knowledgeable model could argue for Mn(2+) as an alternative divalent cation. Heme b (D) and Mo-bis(molybdopterin) (B) are more clearly eliminable.


### Important caveats

- The Zn(2+) cofactor annotation is based on experimental evidence (X-ray crystallography, PDB 8RSN, 2.22 Å resolution), not mere computational prediction.
- The Zn-dependence of macrodomains was published in 2024, making this a recent finding unlikely to be in most training corpora at the time of benchmark construction.
- The protein is bifunctional (ADP-ribose hydrolase + ADP-ribosyltransferase); the Zn(2+) cofactor applies specifically to the hydrolase (macrodomain) activity.
- Sequence identity between the benchmark input and UniProt A0A559KX76 is exact (SHA256 match confirmed across both current and historical snapshots).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial reasoning pathway exists: (1) heme b can be eliminated because no canonical heme-binding motifs (e.g., CXXCH) are present; (2) Mo-bis(molybdopterin) can be eliminated because the protein lacks molybdoenzyme-specific motifs and belongs to a non-molybdoenzyme family; (3) the SirTM domain name evokes sirtuin-like proteins, which are classically Zn-dependent. However, this protein's actual catalytic function is ADP-ribose hydrolase via its macrodomain, not sirtuin deacetylase activity, and the Zn-dependence of macrodomains was only established in 2024 (PubMed 39270823). The critical distinction between Zn(2+) and Mn(2+)—both divalent cations coordinated by similar Cys/His/Asp residues—cannot be reliably resolved from sequence alone for this specific protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental demonstration (X-ray crystallography, 2024) that the macrodomain catalytic site of this specific Foc1Mfs1 protein requires Zn(2+) rather than Mn(2+) for ADP-ribose hydrolase activity. The Zn-dependence of macrodomains is a recent, protein-family-specific finding not derivable from general sequence heuristics.",
    "reason": "While heme and molybdopterin can be reasonably excluded, the decisive choice between Zn(2+) and Mn(2+) depends on knowing this specific protein's experimentally determined cofactor. The SirTM/sirtuin analogy provides only a weak hint (sirtuins are Zn-dependent for deacetylation, but this protein's key activity is macrodomain-mediated ADP-ribose hydrolysis). The Zn-dependence of macrodomains is a 2024 finding that cannot be inferred from sequence composition alone."
  },
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A559KX76 (sequence SHA256 match confirmed) annotates Zn(2+) as cofactor with ECO:0000269 (experimental) evidence from PubMed 39270823. X-ray crystallography at 2.22 Å (PDB: 8RSN) in complex with Zn(2+) directly confirms Zn(2+) binding. The note states 'Binds 2 Zn(2+) ions per subunit.' The protein is a macrodomain-fused SirTM 1 (Foc1Mfs1) from Fusarium oxysporum f. sp. cubense, and the 2024 paper title explicitly refers to 'zinc-dependent macrodomains.'"
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation is based on experimental evidence (X-ray crystallography, PDB 8RSN, 2.22 Å resolution), not mere computational prediction.",
    "The Zn-dependence of macrodomains was published in 2024, making this a recent finding unlikely to be in most training corpora at the time of benchmark construction.",
    "The protein is bifunctional (ADP-ribose hydrolase + ADP-ribosyltransferase); the Zn(2+) cofactor applies specifically to the hydrolase (macrodomain) activity.",
    "Sequence identity between the benchmark input and UniProt A0A559KX76 is exact (SHA256 match confirmed across both current and historical snapshots)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Zn(2+) and Mn(2+) are both divalent transition-metal cofactors coordinated by similar residues (Cys, His, Asp, Glu). From sequence alone, clusters of Cys residues (e.g., CLC at ~60, CRFCGSKMSICV at ~440) are compatible with either metal. Without structural or experimental data specific to this protein, a knowledgeable model could argue for Mn(2+) as an alternative divalent cation. Heme b (D) and Mo-bis(molybdopterin) (B) are more clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A559KX76 (sequence SHA256 match confirmed) annotates Zn(2+) as cofactor with ECO:0000269 (experimental) evidence from PubMed 39270823. X-ray crystallography at 2.22 Å (PDB: 8RSN) in complex with Zn(2+) directly confirms Zn(2+) binding. The note states 'Binds 2 Zn(2+) ions per subunit.' The protein is a macrodomain-fused SirTM 1 (Foc1Mfs1) from Fusarium oxysporum f. sp. cubense, and the 2024 paper title explicitly refers to 'zinc-dependent macrodomains.'",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial reasoning pathway exists: (1) heme b can be eliminated because no canonical heme-binding motifs (e.g., CXXCH) are present; (2) Mo-bis(molybdopterin) can be eliminated because the protein lacks molybdoenzyme-specific motifs and belongs to a non-molybdoenzyme family; (3) the SirTM domain name evokes sirtuin-like proteins, which are classically Zn-dependent. However, this protein's actual catalytic function is ADP-ribose hydrolase via its macrodomain, not sirtuin deacetylase activity, and the Zn-dependence of macrodomains was only established in 2024 (PubMed 39270823). The critical distinction between Zn(2+) and Mn(2+)—both divalent cations coordinated by similar Cys/His/Asp residues—cannot be reliably resolved from sequence alone for this specific protein.",
    "missing_item_specific_fact": "The experimental demonstration (X-ray crystallography, 2024) that the macrodomain catalytic site of this specific Foc1Mfs1 protein requires Zn(2+) rather than Mn(2+) for ADP-ribose hydrolase activity. The Zn-dependence of macrodomains is a recent, protein-family-specific finding not derivable from general sequence heuristics.",
    "reason": "While heme and molybdopterin can be reasonably excluded, the decisive choice between Zn(2+) and Mn(2+) depends on knowing this specific protein's experimentally determined cofactor. The SirTM/sirtuin analogy provides only a weak hint (sirtuins are Zn-dependent for deacetylation, but this protein's key activity is macrodomain-mediated ADP-ribose hydrolysis). The Zn-dependence of macrodomains is a 2024 finding that cannot be inferred from sequence composition alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Zn(2+) and Mn(2+) are both divalent transition-metal cofactors coordinated by similar residues (Cys, His, Asp, Glu). From sequence alone, clusters of Cys residues (e.g., CLC at ~60, CRFCGSKMSICV at ~440) are compatible with either metal. Without structural or experimental data specific to this protein, a knowledgeable model could argue for Mn(2+) as an alternative divalent cation. Heme b (D) and Mo-bis(molybdopterin) (B) are more clearly eliminable."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation is based on experimental evidence (X-ray crystallography, PDB 8RSN, 2.22 Å resolution), not mere computational prediction.",
    "The Zn-dependence of macrodomains was published in 2024, making this a recent finding unlikely to be in most training corpora at the time of benchmark construction.",
    "The protein is bifunctional (ADP-ribose hydrolase + ADP-ribosyltransferase); the Zn(2+) cofactor applies specifically to the hydrolase (macrodomain) activity.",
    "Sequence identity between the benchmark input and UniProt A0A559KX76 is exact (SHA256 match confirmed across both current and historical snapshots)."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A559KX76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 22. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000269","id":"39270823","source":"PubMed"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39270823","source":"PubMed"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:25.184799+00:00.  

```json
{"citation":{"authors":["Ariza A.","Liu Q.","Cowieson N.P.","Ahel I.","Filippov D.V.","Rack J.G.M."],"citationCrossReferences":[{"database":"PubMed","id":"39270823"},{"database":"DOI","id":"10.1016/j.jbc.2024.107770"}],"citationType":"journal article","firstPage":"107770","id":"39270823","journal":"J. Biol. Chem.","lastPage":"107770","publicationDate":"2024","title":"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.","volume":"300"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8RSN","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"race 1 / IMI 141109"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS) IN COMPLEX WITH ZN(2+)","FUNCTION AS AN HYDROLASE","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","MUTAGENESIS OF CYS-61 AND HIS-144"]}
```

Source SHA-256: `52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8RSN}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)
RP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,
RP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.
RC   STRAIN=race 1 / IMI 141109;
RX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;
RA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;
RT   "Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-
RT   dependent macrodomains.";
RL   J. Biol. Chem. 300:107770-107770(2024).
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)  
**Locator:** `lines 55-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 22 / 1.  
**Retrieved:** 2026-11-02T04:25:28.054482+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000269|PubMed:39270823};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000305|PubMed:39270823};
```

Source SHA-256: `ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
