# GO_biological_process_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — triterpenoid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEASSFLAQKRYAVVTGANKGLGLEICGQLASQGVTVLLTSRDEKRGLEAIEELKKSGINSENLEYHQLDVTKPASFASLADFIKAKFGKLDILVNNAGISGVIVDYAALMEAIRRRGAEINYDGVMKQTYELAEECLQTNYYGVKRTINALLPLLQFSDSPRIVNVSSDVGLLKKIPGERIREALGDVEKLTEESVDGILDEFLRDFKEGKIAEKGWPTFKSAYSISKAALNSYTRVLARKYPSIIINCVCPGVVKTDINLKMGHLTVEEGAASPVRLALMPLGSPSGLFYTRNEVTPFE

[Multiple Choices]
A. triterpenoid biosynthetic process
B. mitophagy
C. positive regulation of protein export from nucleus
D. mycotoxin biosynthetic process
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

> The supplied sequence exactly matches the annotated protein. Its record describes a role in oleanane-type triterpene saponin biosynthesis and includes an IDA annotation for triterpenoid biosynthetic process, supported by a cited publication.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, but its general sequence features do not identify its biological substrate or pathway. In particular, they do not distinguish triterpenoid biosynthesis from the other offered processes.


**Missing item-specific fact**

> The protein-specific experimental characterization linking this SDR to triterpene saponin biosynthesis is absent from the input.


**Reason**

> Choosing A requires the protein-specific pathway assignment, not a defensible inference from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports triterpenoid biosynthesis; the other choices describe unrelated processes. Although the protein is also annotated to saponin biosynthesis, that process is not an offered choice.


### Important caveats

- The UniProt record and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The sequence matches both the current record and the historical entry checked; the author's exact source snapshot remains unknown.
- The GO annotation is IDA (inferred from direct assay), and the cited functional record reports a role in the triterpene saponin pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but its general sequence features do not identify its biological substrate or pathway. In particular, they do not distinguish triterpenoid biosynthesis from the other offered processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental characterization linking this SDR to triterpene saponin biosynthesis is absent from the input.",
    "reason": "Choosing A requires the protein-specific pathway assignment, not a defensible inference from the sequence and choices alone."
  },
  "case_id": "GO_biological_process_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its record describes a role in oleanane-type triterpene saponin biosynthesis and includes an IDA annotation for triterpenoid biosynthetic process, supported by a cited publication."
  },
  "important_caveats": [
    "The UniProt record and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence matches both the current record and the historical entry checked; the author's exact source snapshot remains unknown.",
    "The GO annotation is IDA (inferred from direct assay), and the cited functional record reports a role in the triterpene saponin pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports triterpenoid biosynthesis; the other choices describe unrelated processes. Although the protein is also annotated to saponin biosynthesis, that process is not an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its record describes a role in oleanane-type triterpene saponin biosynthesis and includes an IDA annotation for triterpenoid biosynthetic process, supported by a cited publication.",
    "evidence_ids": ["C1", "C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but its general sequence features do not identify its biological substrate or pathway. In particular, they do not distinguish triterpenoid biosynthesis from the other offered processes.",
    "missing_item_specific_fact": "The protein-specific experimental characterization linking this SDR to triterpene saponin biosynthesis is absent from the input.",
    "reason": "Choosing A requires the protein-specific pathway assignment, not a defensible inference from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports triterpenoid biosynthesis; the other choices describe unrelated processes. Although the protein is also annotated to saponin biosynthesis, that process is not an offered choice."
  },
  "important_caveats": [
    "The UniProt record and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The sequence matches both the current record and the historical entry checked; the author's exact source snapshot remains unknown.",
    "The GO annotation is IDA (inferred from direct assay), and the cited functional record reports a role in the triterpene saponin pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1NHX6 (SDR1_SAPOF) carries the GO annotation GO:0016104 'triterpenoid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:39043959), an experimental evidence type. The FUNCTION comment explicitly states the protein is a component of the oleanane-type triterpene saponins biosynthetic pathway. The PATHWAY comment states 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed in both current and historical snapshots).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable short-chain dehydrogenase/reductase (SDR) motifs (e.g., TGANKGLGLEICGQLASQGVTVLLTSRDEKRG Rossmann-like NAD(P)-binding region, NNAGISGVIVDYAALMEAIRRRG, INCVCPGVVKTDINLKMGH). SDRs catalyze redox transformations of small-molecule secondary metabolites, not macromolecular processes like mitophagy (autophagy machinery: Atg proteins, ubiquitin ligases) or nuclear export (importin/exportin machinery), eliminating B and C. Between A (triterpenoid biosynthesis) and D (mycotoxin biosynthesis), the sequence lacks fungal-specific features (no fungal codon-bias signatures, no fungal-specific signal peptides) and the SDR fold is heavily represented in plant specialized metabolism (terpenoid, steroid, alkaloid pathways). Mycotoxin biosynthesis is restricted to fungi and involves polyketide synthases and non-ribosomal peptide synthetases rather than SDRs. This leaves A as the only biologically coherent option for a plant SDR involved in small-molecule biosynthesis.


**Missing item-specific fact**

> None strictly required for elimination-based reasoning. However, positive identification of 'triterpenoid' specifically (rather than, e.g., steroid or flavonoid biosynthesis) among plant SDR functions would require knowledge of this protein's specific substrate (QA-tri → QA-triF conversion), which is an item-specific experimental finding not inferable from the SDR fold alone.


**Reason**

> The three distractors (mitophagy, nuclear export regulation, mycotoxin biosynthesis) are eliminable through general biological knowledge about SDR function, autophagy/nuclear-transport machinery, and fungal vs. plant metabolism. The remaining option A is the only plant-relevant small-molecule biosynthetic process among the choices. While positive identification of 'triterpenoid' specifically relies on the option set rather than a unique sequence signature, the elimination chain is concrete and grounded in general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a short-chain dehydrogenase/reductase: mitophagy requires autophagy machinery, nuclear export requires karyopherins, and mycotoxin biosynthesis is a fungal pathway involving PKS/NRPS enzymes. No alternative among the four options is defensible for a plant SDR.


### Important caveats

- The SDR fold is shared across thousands of enzymes in diverse pathways; positive identification of triterpenoid biosynthesis specifically (vs. steroid, fatty-acid, or other plant SDR functions) is not uniquely derivable from the fold alone.
- The specific triterpenoid/saponin assignment comes from a 2025 experimental study (PubMed:39043959, Nat. Chem. Biol.); this entry was not in UniProt until 2025-06-18, so the annotation post-dates many model training cutoffs.
- The plant-vs-fungal distinction used to eliminate D relies on subtle sequence-composition heuristics rather than a single definitive feature visible in a 302-aa sequence.
- The GO annotation is IDA (experimental), providing strong evidence for the expected answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable short-chain dehydrogenase/reductase (SDR) motifs (e.g., TGANKGLGLEICGQLASQGVTVLLTSRDEKRG Rossmann-like NAD(P)-binding region, NNAGISGVIVDYAALMEAIRRRG, INCVCPGVVKTDINLKMGH). SDRs catalyze redox transformations of small-molecule secondary metabolites, not macromolecular processes like mitophagy (autophagy machinery: Atg proteins, ubiquitin ligases) or nuclear export (importin/exportin machinery), eliminating B and C. Between A (triterpenoid biosynthesis) and D (mycotoxin biosynthesis), the sequence lacks fungal-specific features (no fungal codon-bias signatures, no fungal-specific signal peptides) and the SDR fold is heavily represented in plant specialized metabolism (terpenoid, steroid, alkaloid pathways). Mycotoxin biosynthesis is restricted to fungi and involves polyketide synthases and non-ribosomal peptide synthetases rather than SDRs. This leaves A as the only biologically coherent option for a plant SDR involved in small-molecule biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning. However, positive identification of 'triterpenoid' specifically (rather than, e.g., steroid or flavonoid biosynthesis) among plant SDR functions would require knowledge of this protein's specific substrate (QA-tri → QA-triF conversion), which is an item-specific experimental finding not inferable from the SDR fold alone.",
    "reason": "The three distractors (mitophagy, nuclear export regulation, mycotoxin biosynthesis) are eliminable through general biological knowledge about SDR function, autophagy/nuclear-transport machinery, and fungal vs. plant metabolism. The remaining option A is the only plant-relevant small-molecule biosynthetic process among the choices. While positive identification of 'triterpenoid' specifically relies on the option set rather than a unique sequence signature, the elimination chain is concrete and grounded in general biology."
  },
  "case_id": "GO_biological_process_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "C9",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1NHX6 (SDR1_SAPOF) carries the GO annotation GO:0016104 'triterpenoid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:39043959), an experimental evidence type. The FUNCTION comment explicitly states the protein is a component of the oleanane-type triterpene saponins biosynthetic pathway. The PATHWAY comment states 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed in both current and historical snapshots)."
  },
  "important_caveats": [
    "The SDR fold is shared across thousands of enzymes in diverse pathways; positive identification of triterpenoid biosynthesis specifically (vs. steroid, fatty-acid, or other plant SDR functions) is not uniquely derivable from the fold alone.",
    "The specific triterpenoid/saponin assignment comes from a 2025 experimental study (PubMed:39043959, Nat. Chem. Biol.); this entry was not in UniProt until 2025-06-18, so the annotation post-dates many model training cutoffs.",
    "The plant-vs-fungal distinction used to eliminate D relies on subtle sequence-composition heuristics rather than a single definitive feature visible in a 302-aa sequence.",
    "The GO annotation is IDA (experimental), providing strong evidence for the expected answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a short-chain dehydrogenase/reductase: mitophagy requires autophagy machinery, nuclear export requires karyopherins, and mycotoxin biosynthesis is a fungal pathway involving PKS/NRPS enzymes. No alternative among the four options is defensible for a plant SDR."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1NHX6 (SDR1_SAPOF) carries the GO annotation GO:0016104 'triterpenoid biosynthetic process' with evidence code IDA (Inferred from Direct Assay, PubMed:39043959), an experimental evidence type. The FUNCTION comment explicitly states the protein is a component of the oleanane-type triterpene saponins biosynthetic pathway. The PATHWAY comment states 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed in both current and historical snapshots).",
    "evidence_ids": ["C5", "C6", "C8", "C9", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable short-chain dehydrogenase/reductase (SDR) motifs (e.g., TGANKGLGLEICGQLASQGVTVLLTSRDEKRG Rossmann-like NAD(P)-binding region, NNAGISGVIVDYAALMEAIRRRG, INCVCPGVVKTDINLKMGH). SDRs catalyze redox transformations of small-molecule secondary metabolites, not macromolecular processes like mitophagy (autophagy machinery: Atg proteins, ubiquitin ligases) or nuclear export (importin/exportin machinery), eliminating B and C. Between A (triterpenoid biosynthesis) and D (mycotoxin biosynthesis), the sequence lacks fungal-specific features (no fungal codon-bias signatures, no fungal-specific signal peptides) and the SDR fold is heavily represented in plant specialized metabolism (terpenoid, steroid, alkaloid pathways). Mycotoxin biosynthesis is restricted to fungi and involves polyketide synthases and non-ribosomal peptide synthetases rather than SDRs. This leaves A as the only biologically coherent option for a plant SDR involved in small-molecule biosynthesis.",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning. However, positive identification of 'triterpenoid' specifically (rather than, e.g., steroid or flavonoid biosynthesis) among plant SDR functions would require knowledge of this protein's specific substrate (QA-tri → QA-triF conversion), which is an item-specific experimental finding not inferable from the SDR fold alone.",
    "reason": "The three distractors (mitophagy, nuclear export regulation, mycotoxin biosynthesis) are eliminable through general biological knowledge about SDR function, autophagy/nuclear-transport machinery, and fungal vs. plant metabolism. The remaining option A is the only plant-relevant small-molecule biosynthetic process among the choices. While positive identification of 'triterpenoid' specifically relies on the option set rather than a unique sequence signature, the elimination chain is concrete and grounded in general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a short-chain dehydrogenase/reductase: mitophagy requires autophagy machinery, nuclear export requires karyopherins, and mycotoxin biosynthesis is a fungal pathway involving PKS/NRPS enzymes. No alternative among the four options is defensible for a plant SDR."
  },
  "important_caveats": [
    "The SDR fold is shared across thousands of enzymes in diverse pathways; positive identification of triterpenoid biosynthesis specifically (vs. steroid, fatty-acid, or other plant SDR functions) is not uniquely derivable from the fold alone.",
    "The specific triterpenoid/saponin assignment comes from a 2025 experimental study (PubMed:39043959, Nat. Chem. Biol.); this entry was not in UniProt until 2025-06-18, so the annotation post-dates many model training cutoffs.",
    "The plant-vs-fungal distinction used to eliminate D relies on subtle sequence-composition heuristics rather than a single definitive feature visible in a 302-aa sequence.",
    "The GO annotation is IDA (experimental), providing strong evidence for the expected answer."
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

**Accession:** `A0AAW1NHX6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NHX6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:43.622772+00:00.  

```json
"A0AAW1NHX6"
```

Source SHA-256: `26702ceb0a0503e7bc6535bc6bf2f0b3e97be80088f147774a9c54759b845dd5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NHX6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:43.622772+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A dehydrogenase/reductase that, together with UGT74CD1, mediates the conversion of QA-tri to QA-triF; UGT74CD1 may transfer 4-keto-6-deoxy-glucose to QA-tri, which is in turn reduced to D-fucose by SDR1, thus leading to QA-triF formation via the initiation of the C-28 sugar chain (PubMed:39043959)"}]}
```

Source SHA-256: `26702ceb0a0503e7bc6535bc6bf2f0b3e97be80088f147774a9c54759b845dd5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NHX6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:43.622772+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `26702ceb0a0503e7bc6535bc6bf2f0b3e97be80088f147774a9c54759b845dd5`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NHX6.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:43.622772+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016104","properties":[{"key":"GoTerm","value":"P:triterpenoid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `26702ceb0a0503e7bc6535bc6bf2f0b3e97be80088f147774a9c54759b845dd5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NHX6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:43.622772+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48149.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `26702ceb0a0503e7bc6535bc6bf2f0b3e97be80088f147774a9c54759b845dd5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NHX6?format=txt&versions=5)  
**Locator:** `lines 34-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.625769+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). A
CC       dehydrogenase/reductase that, together with UGT74CD1, mediates the
CC       conversion of QA-tri to QA-triF; UGT74CD1 may transfer 4-keto-6-deoxy-
CC       glucose to QA-tri, which is in turn reduced to D-fucose by SDR1, thus
CC       leading to QA-triF formation via the initiation of the C-28 sugar chain
CC       (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `87c3bb35235dfc5c73f9057814897f622771fbf58718555e5167298cad1a6599`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NHX6?format=txt&versions=5)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.625769+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `87c3bb35235dfc5c73f9057814897f622771fbf58718555e5167298cad1a6599`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NHX6?format=txt&versions=5)  
**Locator:** `lines 78-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.625769+00:00.  

```text
DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `87c3bb35235dfc5c73f9057814897f622771fbf58718555e5167298cad1a6599`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
