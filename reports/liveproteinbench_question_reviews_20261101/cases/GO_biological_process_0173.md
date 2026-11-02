# GO_biological_process_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — negative regulation of protein targeting to mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSGSSSPPKDKSNSVPHSGAVDTQSLSVHPEEGSAAQTSKSLPSGGFFTRRTSEDQAPAGEKKRRSSTVTKAATFFTNAKNSLSLSSSPRESSSFNYTVRSPQTLQSLGSMDPALSVPQGSLNNSAGDSLPTPRSSFKVGVTEDRNRKCRRTMEDTHAYLYNFLGTPAPLARADGENEAGSSLAPDEASSVVETDNGYFAIFDGHAGTFAAEWCGKKLHLILEDIMKKNPNTPVPELLDQTFTTVDQQLEKLPVKNSGCTAVIALLRWEDRIPSSHSATGSSALAPAAAAAAAAKGDSNSEADDTPTQATSSGPSILPKLQEKAIRQRVLYTANVGDARIILCRNGKALRLSYDHKGSDENEGKRIANAGGLILNNRVNGVLAVTRALGDAYLKDLVTGHPYTTETVVQPDSDEFIILACDGLWDVCTDQEAVDLVRNVPDAQEASKILVDYALARFSTDNLSCMVIRLDTNRVKEVINKTAEPIGVAGDPSMDVEHGVSEADKIIEGARKSMANADIADDGETAEKGKNDILHKMVDGEPGPEMSLDDSNDAPTVSHLNKTNANNGIP

[Multiple Choices]
A. potassium ion import across plasma membrane
B. negative regulation of protein targeting to mitochondrion
C. ribosomal large subunit assembly
D. positive regulation of amyloid-beta formation
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches the historical UniProt record, which annotates the protein as negatively regulating protein targeting to mitochondria. The record links this function to experimental evidence: dephosphorylation of PGK1 negatively regulates its mitochondrial targeting. This supports B, while preserving that the evidence is for this particular protein and its reported biological context.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears to encode a protein phosphatase, which may suggest a regulatory role, but that alone does not establish its substrate or the direction and cellular target of its effect.


**Missing item-specific fact**

> The protein-specific finding that this phosphatase dephosphorylates PGK1 and thereby negatively regulates PGK1 targeting to mitochondria.


**Reason**

> The supplied input contains only sequence and choices. Selecting this specialized process over unrelated alternatives requires an item-specific functional annotation or experimental result; it cannot be inferred reliably from general sequence-level reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited annotation specifically supports B, and none of the other listed processes is supported by the supplied sequence context.


### Important caveats

- The UniProt sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.
- The cited function is reported for the Aspergillus flavus protein and its PGK1-related context; it should not be generalized beyond that evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears to encode a protein phosphatase, which may suggest a regulatory role, but that alone does not establish its substrate or the direction and cellular target of its effect.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this phosphatase dephosphorylates PGK1 and thereby negatively regulates PGK1 targeting to mitochondria.",
    "reason": "The supplied input contains only sequence and choices. Selecting this specialized process over unrelated alternatives requires an item-specific functional annotation or experimental result; it cannot be inferred reliably from general sequence-level reasoning."
  },
  "case_id": "GO_biological_process_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt record, which annotates the protein as negatively regulating protein targeting to mitochondria. The record links this function to experimental evidence: dephosphorylation of PGK1 negatively regulates its mitochondrial targeting. This supports B, while preserving that the evidence is for this particular protein and its reported biological context."
  },
  "important_caveats": [
    "The UniProt sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The cited function is reported for the Aspergillus flavus protein and its PGK1-related context; it should not be generalized beyond that evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation specifically supports B, and none of the other listed processes is supported by the supplied sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt record, which annotates the protein as negatively regulating protein targeting to mitochondria. The record links this function to experimental evidence: dephosphorylation of PGK1 negatively regulates its mitochondrial targeting. This supports B, while preserving that the evidence is for this particular protein and its reported biological context.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears to encode a protein phosphatase, which may suggest a regulatory role, but that alone does not establish its substrate or the direction and cellular target of its effect.",
    "missing_item_specific_fact": "The protein-specific finding that this phosphatase dephosphorylates PGK1 and thereby negatively regulates PGK1 targeting to mitochondria.",
    "reason": "The supplied input contains only sequence and choices. Selecting this specialized process over unrelated alternatives requires an item-specific functional annotation or experimental result; it cannot be inferred reliably from general sequence-level reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation specifically supports B, and none of the other listed processes is supported by the supplied sequence context."
  },
  "important_caveats": [
    "The UniProt sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The cited function is reported for the Aspergillus flavus protein and its PGK1-related context; it should not be generalized beyond that evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B8NLZ3 (PP2C-1, Aspergillus flavus) carries GO annotation GO:1903215 'negative regulation of protein targeting to mitochondrion' with evidence code IMP (Inferred by Mutant Phenotype) from PubMed:37754565 (Zhu et al., MBio 2023). The FUNCTION comment explicitly states: 'Dephosphorylates phosphoglycerate kinase pgk1 at least on Ser-203 to negatively regulate targeting of pgk1 to the mitochondrion.' This is experimental evidence (IMP), not computational prediction. The archived entry (v90) uses GO:1903215 with the exact text matching option B; the current entry (v91) maps to GO:1903748 'negative regulation of protein localization to mitochondrion,' a closely related term. The sequence match is confirmed (SHA-256 identical).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> From the sequence, one can identify a PP2C serine/threonine phosphatase domain and eliminate options A (potassium transporter), C (ribosomal assembly factor), and D (mammalian amyloid-beta pathway in a fungal protein) as clearly incompatible with a phosphatase. However, arriving at the specific answer 'negative regulation of protein targeting to mitochondrion' requires knowing that this particular PP2C dephosphorylates PGK1 at Ser-203 to prevent its mitochondrial import—a finding from a single 2023 experimental study. PP2C phosphatases have hundreds of substrates across fungi; the specific substrate, the specific targeting pathway (mitochondrial), and the regulatory direction (negative) are item-specific experimental facts not derivable from sequence or general phosphatase biology.


**Missing item-specific fact**

> The specific experimental finding (Zhu et al., MBio 2023, PMID:37754565) that PP2C-1 dephosphorylates PGK1 at Ser-203 to negatively regulate its mitochondrial targeting, thereby reducing acetyl-CoA production and aflatoxin biosynthesis. Without this knowledge, a model could only infer 'phosphatase activity' or 'protein dephosphorylation' as a general process, not the specific mitochondrial-targeting regulation.


**Reason**

> While the distractors are easily eliminable by recognizing the protein as a phosphatase (not a transporter, ribosomal factor, or mammalian amyloid pathway component), the correct answer B specifies a precise, recently characterized biological process tied to one experimental study. General biological knowledge of PP2C phosphatases does not predict which specific protein-targeting pathway (mitochondrial vs. nuclear vs. peroxisomal) or which direction of regulation this enzyme controls.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with a fungal serine/threonine phosphatase: A requires a transmembrane ion channel, C requires ribosomal RNA/protein assembly factors, and D involves mammalian amyloid-beta processing irrelevant to Aspergillus flavus. Only B is consistent with a phosphatase that modifies protein localization signals. No genuine ambiguity exists among the four choices.


### Important caveats

- The GO term in the archived entry (GO:1903215, 'negative regulation of protein targeting to mitochondrion') differs slightly from the current entry (GO:1903748, 'negative regulation of protein localization to mitochondrion'), suggesting a possible term merge or revision. The option text matches the archived version.
- The protein's broader biological role also includes negative regulation of aflatoxin biosynthesis and autophagy regulation, but the question asks for the primary GO Biological Process annotation, which is the mitochondrial targeting term.
- The identity of the protein (accession B8NLZ3) was inferred by the reviewer from dataset metadata, not from the model's input. The model must identify the process from sequence alone.
- The IMP evidence code indicates mutant-phenotype-based experimental support, which is stronger than computational inference but still represents one study's findings.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the sequence, one can identify a PP2C serine/threonine phosphatase domain and eliminate options A (potassium transporter), C (ribosomal assembly factor), and D (mammalian amyloid-beta pathway in a fungal protein) as clearly incompatible with a phosphatase. However, arriving at the specific answer 'negative regulation of protein targeting to mitochondrion' requires knowing that this particular PP2C dephosphorylates PGK1 at Ser-203 to prevent its mitochondrial import—a finding from a single 2023 experimental study. PP2C phosphatases have hundreds of substrates across fungi; the specific substrate, the specific targeting pathway (mitochondrial), and the regulatory direction (negative) are item-specific experimental facts not derivable from sequence or general phosphatase biology.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (Zhu et al., MBio 2023, PMID:37754565) that PP2C-1 dephosphorylates PGK1 at Ser-203 to negatively regulate its mitochondrial targeting, thereby reducing acetyl-CoA production and aflatoxin biosynthesis. Without this knowledge, a model could only infer 'phosphatase activity' or 'protein dephosphorylation' as a general process, not the specific mitochondrial-targeting regulation.",
    "reason": "While the distractors are easily eliminable by recognizing the protein as a phosphatase (not a transporter, ribosomal factor, or mammalian amyloid pathway component), the correct answer B specifies a precise, recently characterized biological process tied to one experimental study. General biological knowledge of PP2C phosphatases does not predict which specific protein-targeting pathway (mitochondrial vs. nuclear vs. peroxisomal) or which direction of regulation this enzyme controls."
  },
  "case_id": "GO_biological_process_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C-1, Aspergillus flavus) carries GO annotation GO:1903215 'negative regulation of protein targeting to mitochondrion' with evidence code IMP (Inferred by Mutant Phenotype) from PubMed:37754565 (Zhu et al., MBio 2023). The FUNCTION comment explicitly states: 'Dephosphorylates phosphoglycerate kinase pgk1 at least on Ser-203 to negatively regulate targeting of pgk1 to the mitochondrion.' This is experimental evidence (IMP), not computational prediction. The archived entry (v90) uses GO:1903215 with the exact text matching option B; the current entry (v91) maps to GO:1903748 'negative regulation of protein localization to mitochondrion,' a closely related term. The sequence match is confirmed (SHA-256 identical)."
  },
  "important_caveats": [
    "The GO term in the archived entry (GO:1903215, 'negative regulation of protein targeting to mitochondrion') differs slightly from the current entry (GO:1903748, 'negative regulation of protein localization to mitochondrion'), suggesting a possible term merge or revision. The option text matches the archived version.",
    "The protein's broader biological role also includes negative regulation of aflatoxin biosynthesis and autophagy regulation, but the question asks for the primary GO Biological Process annotation, which is the mitochondrial targeting term.",
    "The identity of the protein (accession B8NLZ3) was inferred by the reviewer from dataset metadata, not from the model's input. The model must identify the process from sequence alone.",
    "The IMP evidence code indicates mutant-phenotype-based experimental support, which is stronger than computational inference but still represents one study's findings."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a fungal serine/threonine phosphatase: A requires a transmembrane ion channel, C requires ribosomal RNA/protein assembly factors, and D involves mammalian amyloid-beta processing irrelevant to Aspergillus flavus. Only B is consistent with a phosphatase that modifies protein localization signals. No genuine ambiguity exists among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B8NLZ3 (PP2C-1, Aspergillus flavus) carries GO annotation GO:1903215 'negative regulation of protein targeting to mitochondrion' with evidence code IMP (Inferred by Mutant Phenotype) from PubMed:37754565 (Zhu et al., MBio 2023). The FUNCTION comment explicitly states: 'Dephosphorylates phosphoglycerate kinase pgk1 at least on Ser-203 to negatively regulate targeting of pgk1 to the mitochondrion.' This is experimental evidence (IMP), not computational prediction. The archived entry (v90) uses GO:1903215 with the exact text matching option B; the current entry (v91) maps to GO:1903748 'negative regulation of protein localization to mitochondrion,' a closely related term. The sequence match is confirmed (SHA-256 identical).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "From the sequence, one can identify a PP2C serine/threonine phosphatase domain and eliminate options A (potassium transporter), C (ribosomal assembly factor), and D (mammalian amyloid-beta pathway in a fungal protein) as clearly incompatible with a phosphatase. However, arriving at the specific answer 'negative regulation of protein targeting to mitochondrion' requires knowing that this particular PP2C dephosphorylates PGK1 at Ser-203 to prevent its mitochondrial import—a finding from a single 2023 experimental study. PP2C phosphatases have hundreds of substrates across fungi; the specific substrate, the specific targeting pathway (mitochondrial), and the regulatory direction (negative) are item-specific experimental facts not derivable from sequence or general phosphatase biology.",
    "missing_item_specific_fact": "The specific experimental finding (Zhu et al., MBio 2023, PMID:37754565) that PP2C-1 dephosphorylates PGK1 at Ser-203 to negatively regulate its mitochondrial targeting, thereby reducing acetyl-CoA production and aflatoxin biosynthesis. Without this knowledge, a model could only infer 'phosphatase activity' or 'protein dephosphorylation' as a general process, not the specific mitochondrial-targeting regulation.",
    "reason": "While the distractors are easily eliminable by recognizing the protein as a phosphatase (not a transporter, ribosomal factor, or mammalian amyloid pathway component), the correct answer B specifies a precise, recently characterized biological process tied to one experimental study. General biological knowledge of PP2C phosphatases does not predict which specific protein-targeting pathway (mitochondrial vs. nuclear vs. peroxisomal) or which direction of regulation this enzyme controls."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a fungal serine/threonine phosphatase: A requires a transmembrane ion channel, C requires ribosomal RNA/protein assembly factors, and D involves mammalian amyloid-beta processing irrelevant to Aspergillus flavus. Only B is consistent with a phosphatase that modifies protein localization signals. No genuine ambiguity exists among the four choices."
  },
  "important_caveats": [
    "The GO term in the archived entry (GO:1903215, 'negative regulation of protein targeting to mitochondrion') differs slightly from the current entry (GO:1903748, 'negative regulation of protein localization to mitochondrion'), suggesting a possible term merge or revision. The option text matches the archived version.",
    "The protein's broader biological role also includes negative regulation of aflatoxin biosynthesis and autophagy regulation, but the question asks for the primary GO Biological Process annotation, which is the mitochondrial targeting term.",
    "The identity of the protein (accession B8NLZ3) was inferred by the reviewer from dataset metadata, not from the model's input. The model must identify the process from sequence alone.",
    "The IMP evidence code indicates mutant-phenotype-based experimental support, which is stronger than computational inference but still represents one study's findings."
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

**Accession:** `B8NLZ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"value":"Serine and threonine phosphatase (PubMed:37754565). Dephosphorylates phosphoglycerate kinase pgk1 at least on 'Ser-203' to negatively regulate targeting of pgk1 to the mitochondrion, thereby negatively regulating production of acetyl-CoA and consequently aflatoxin biosynthesis (PubMed:37754565)"}]}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B8NLZ3.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:25.884972+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000315","id":"37754565","source":"PubMed"}],"id":"GO:1903748","properties":[{"key":"GoTerm","value":"P:negative regulation of protein localization to mitochondrion"},{"key":"GoEvidenceType","value":"IMP:UniProtKB"}]}
```

Source SHA-256: `a923d0b87775c86363af2f32117cbaa4b3b19dd82d48b975eb0997609aba449a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
CC   -!- FUNCTION: Serine and threonine phosphatase (PubMed:37754565).
CC       Dephosphorylates phosphoglycerate kinase pgk1 at least on 'Ser-203' to
CC       negatively regulate targeting of pgk1 to the mitochondrion, thereby
CC       negatively regulating production of acetyl-CoA and consequently
CC       aflatoxin biosynthesis (PubMed:37754565).
CC       {ECO:0000269|PubMed:37754565}.
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B8NLZ3?format=txt&versions=90)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:27:29.637546+00:00.  

```text
DR   GO; GO:1903215; P:negative regulation of protein targeting to mitochondrion; IMP:UniProtKB.
```

Source SHA-256: `bea04bbd31835e19259854f2e42627d0cb34cb3b47749e8af3e5d4aae56f53bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
