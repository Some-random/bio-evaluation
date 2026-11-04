# GO_molecular_function_0185

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0185.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — pyridoxal phosphate binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. enoyl-[acyl-carrier-protein] reductase (NADPH) activity
B. flavin adenine dinucleotide binding
C. pyridoxal phosphate binding
D. cardiolipin synthase (CMP-forming)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched record assigns pyridoxal phosphate binding by IEA:InterPro (C9; H7). The experimentally supported cystathionine gamma-synthase activity (C4, C5) is also consistent with the PLP-dependent enzyme family. The binding annotation is computational, not direct experimental evidence of PLP binding in this particular protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long soluble enzyme sequence is consistent with a PLP-dependent cystathionine gamma-synthase-family protein, whose conserved enzyme-family features support PLP binding. That transferable family inference distinguishes C from the unrelated FAD-binding, fatty-acid reductase, and cardiolipin synthase choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence/function inference provides a meaningful basis for choosing C without requiring the exact protein's database entry. It is probabilistic rather than a direct demonstration of cofactor binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, PLP binding is the clear family-consistent function; the alternatives describe distinct enzyme activities or cofactor binding.


### Important caveats

- The supplied direct GO evidence for PLP binding is computational (IEA:InterPro); the cited experimental evidence concerns catalytic activity, not a direct PLP-binding assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long soluble enzyme sequence is consistent with a PLP-dependent cystathionine gamma-synthase-family protein, whose conserved enzyme-family features support PLP binding. That transferable family inference distinguishes C from the unrelated FAD-binding, fatty-acid reductase, and cardiolipin synthase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence/function inference provides a meaningful basis for choosing C without requiring the exact protein's database entry. It is probabilistic rather than a direct demonstration of cofactor binding."
  },
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record assigns pyridoxal phosphate binding by IEA:InterPro (C9; H7). The experimentally supported cystathionine gamma-synthase activity (C4, C5) is also consistent with the PLP-dependent enzyme family. The binding annotation is computational, not direct experimental evidence of PLP binding in this particular protein."
  },
  "important_caveats": [
    "The supplied direct GO evidence for PLP binding is computational (IEA:InterPro); the cited experimental evidence concerns catalytic activity, not a direct PLP-binding assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, PLP binding is the clear family-consistent function; the alternatives describe distinct enzyme activities or cofactor binding."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record assigns pyridoxal phosphate binding by IEA:InterPro (C9; H7). The experimentally supported cystathionine gamma-synthase activity (C4, C5) is also consistent with the PLP-dependent enzyme family. The binding annotation is computational, not direct experimental evidence of PLP binding in this particular protein.",
    "evidence_ids": ["C4", "C5", "C9", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long soluble enzyme sequence is consistent with a PLP-dependent cystathionine gamma-synthase-family protein, whose conserved enzyme-family features support PLP binding. That transferable family inference distinguishes C from the unrelated FAD-binding, fatty-acid reductase, and cardiolipin synthase choices.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence/function inference provides a meaningful basis for choosing C without requiring the exact protein's database entry. It is probabilistic rather than a direct demonstration of cofactor binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, PLP binding is the clear family-consistent function; the alternatives describe distinct enzyme activities or cofactor binding."
  },
  "important_caveats": [
    "The supplied direct GO evidence for PLP binding is computational (IEA:InterPro); the cited experimental evidence concerns catalytic activity, not a direct PLP-binding assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Cystathionine gamma-synthase (CGS, EC 2.5.1.160), a well-characterized fold-type I PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry (evidence IEA:InterPro), and the experimental characterization (PubMed:10595588) confirms the PLP-dependent gamma-replacement catalytic mechanism. Among the four choices, only C correctly describes a molecular function of this protein. The primary catalytic activity (cystathionine gamma-synthase activity, GO:0003962) is not among the options, but PLP binding is a valid and annotated molecular function.

Citations as saved: [C9](#evidence-c9), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use family-level sequence features and general biochemistry to distinguish C from A, B, and D. (1) The ~540 aa length and two-domain architecture are characteristic of fold-type I PLP-dependent enzymes (e.g., O-acetylserine sulfhydrylase, serine racemase, cystathionine beta-synthase, CGS), not the ~270-300 aa enoyl-ACP reductases (A) or membrane-bound cardiolipin synthases (D). (2) The sequence lacks Rossmann-fold FAD-binding motifs (GXGXXG) expected for FAD-binding flavoproteins (B). (3) The sequence lacks the NADPH-binding motifs and small size of enoyl-ACP reductases (A). (4) The sequence lacks the multiple transmembrane helices typical of CMP-forming cardiolipin synthases (D). (5) The presence of conserved lysine residues in positions consistent with the Schiff-base-forming catalytic lysine of fold-type I PLP enzymes, along with the overall domain organization, supports PLP binding (C). This is a legitimate family-level inference from knowledge of PLP-dependent enzyme architecture learned from other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination relies on recognizing the ~540 aa two-domain architecture typical of fold-type I PLP enzymes, the absence of FAD-binding Rossmann motifs, the absence of transmembrane domains, and the absence of NADPH-binding motifs. These are transferable features learned from other PLP-dependent enzymes and other protein families, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase CMP-forming) are all clearly incompatible with the sequence features and family architecture of this protein. Only C (PLP binding) is consistent with the fold-type I PLP enzyme identity. The phrasing 'primary molecular function' is slightly imprecise since the primary catalytic activity is cystathionine gamma-synthase activity, but among the offered choices, C is unambiguously the only correct one.


### Important caveats

- The GO:0030170 (PLP binding) annotation carries evidence code IEA:InterPro (computational inference from domain matching), not direct experimental measurement of PLP binding. However, the experimental paper (PubMed:10595588) confirms the PLP-dependent catalytic mechanism.
- The 'primary molecular function' phrasing could arguably favor the catalytic activity term (cystathionine gamma-synthase activity, GO:0003962) over the cofactor-binding term, but since the catalytic activity is not among the choices, C is the best available answer.
- The sequence is from Nicotiana tabacum (tobacco), a plant CGS. Plant CGS enzymes are well-established PLP-dependent fold-type I enzymes based on structural and biochemical studies of homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use family-level sequence features and general biochemistry to distinguish C from A, B, and D. (1) The ~540 aa length and two-domain architecture are characteristic of fold-type I PLP-dependent enzymes (e.g., O-acetylserine sulfhydrylase, serine racemase, cystathionine beta-synthase, CGS), not the ~270-300 aa enoyl-ACP reductases (A) or membrane-bound cardiolipin synthases (D). (2) The sequence lacks Rossmann-fold FAD-binding motifs (GXGXXG) expected for FAD-binding flavoproteins (B). (3) The sequence lacks the NADPH-binding motifs and small size of enoyl-ACP reductases (A). (4) The sequence lacks the multiple transmembrane helices typical of CMP-forming cardiolipin synthases (D). (5) The presence of conserved lysine residues in positions consistent with the Schiff-base-forming catalytic lysine of fold-type I PLP enzymes, along with the overall domain organization, supports PLP binding (C). This is a legitimate family-level inference from knowledge of PLP-dependent enzyme architecture learned from other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on recognizing the ~540 aa two-domain architecture typical of fold-type I PLP enzymes, the absence of FAD-binding Rossmann motifs, the absence of transmembrane domains, and the absence of NADPH-binding motifs. These are transferable features learned from other PLP-dependent enzymes and other protein families, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C4",
      "C5",
      "C6",
      "H7",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein is Cystathionine gamma-synthase (CGS, EC 2.5.1.160), a well-characterized fold-type I PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry (evidence IEA:InterPro), and the experimental characterization (PubMed:10595588) confirms the PLP-dependent gamma-replacement catalytic mechanism. Among the four choices, only C correctly describes a molecular function of this protein. The primary catalytic activity (cystathionine gamma-synthase activity, GO:0003962) is not among the options, but PLP binding is a valid and annotated molecular function."
  },
  "important_caveats": [
    "The GO:0030170 (PLP binding) annotation carries evidence code IEA:InterPro (computational inference from domain matching), not direct experimental measurement of PLP binding. However, the experimental paper (PubMed:10595588) confirms the PLP-dependent catalytic mechanism.",
    "The 'primary molecular function' phrasing could arguably favor the catalytic activity term (cystathionine gamma-synthase activity, GO:0003962) over the cofactor-binding term, but since the catalytic activity is not among the choices, C is the best available answer.",
    "The sequence is from Nicotiana tabacum (tobacco), a plant CGS. Plant CGS enzymes are well-established PLP-dependent fold-type I enzymes based on structural and biochemical studies of homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase CMP-forming) are all clearly incompatible with the sequence features and family architecture of this protein. Only C (PLP binding) is consistent with the fold-type I PLP enzyme identity. The phrasing 'primary molecular function' is slightly imprecise since the primary catalytic activity is cystathionine gamma-synthase activity, but among the offered choices, C is unambiguously the only correct one."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Cystathionine gamma-synthase (CGS, EC 2.5.1.160), a well-characterized fold-type I PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry (evidence IEA:InterPro), and the experimental characterization (PubMed:10595588) confirms the PLP-dependent gamma-replacement catalytic mechanism. Among the four choices, only C correctly describes a molecular function of this protein. The primary catalytic activity (cystathionine gamma-synthase activity, GO:0003962) is not among the options, but PLP binding is a valid and annotated molecular function.",
    "evidence_ids": ["C9", "C4", "C5", "C6", "H7", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use family-level sequence features and general biochemistry to distinguish C from A, B, and D. (1) The ~540 aa length and two-domain architecture are characteristic of fold-type I PLP-dependent enzymes (e.g., O-acetylserine sulfhydrylase, serine racemase, cystathionine beta-synthase, CGS), not the ~270-300 aa enoyl-ACP reductases (A) or membrane-bound cardiolipin synthases (D). (2) The sequence lacks Rossmann-fold FAD-binding motifs (GXGXXG) expected for FAD-binding flavoproteins (B). (3) The sequence lacks the NADPH-binding motifs and small size of enoyl-ACP reductases (A). (4) The sequence lacks the multiple transmembrane helices typical of CMP-forming cardiolipin synthases (D). (5) The presence of conserved lysine residues in positions consistent with the Schiff-base-forming catalytic lysine of fold-type I PLP enzymes, along with the overall domain organization, supports PLP binding (C). This is a legitimate family-level inference from knowledge of PLP-dependent enzyme architecture learned from other proteins.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on recognizing the ~540 aa two-domain architecture typical of fold-type I PLP enzymes, the absence of FAD-binding Rossmann motifs, the absence of transmembrane domains, and the absence of NADPH-binding motifs. These are transferable features learned from other PLP-dependent enzymes and other protein families, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase CMP-forming) are all clearly incompatible with the sequence features and family architecture of this protein. Only C (PLP binding) is consistent with the fold-type I PLP enzyme identity. The phrasing 'primary molecular function' is slightly imprecise since the primary catalytic activity is cystathionine gamma-synthase activity, but among the offered choices, C is unambiguously the only correct one."
  },
  "important_caveats": [
    "The GO:0030170 (PLP binding) annotation carries evidence code IEA:InterPro (computational inference from domain matching), not direct experimental measurement of PLP binding. However, the experimental paper (PubMed:10595588) confirms the PLP-dependent catalytic mechanism.",
    "The 'primary molecular function' phrasing could arguably favor the catalytic activity term (cystathionine gamma-synthase activity, GO:0003962) over the cofactor-binding term, but since the catalytic activity is not among the choices, C is the best available answer.",
    "The sequence is from Nicotiana tabacum (tobacco), a plant CGS. Plant CGS enzymes are well-established PLP-dependent fold-type I enzymes based on structural and biochemical studies of homologs."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9ZPL5",
  "selected_historical_entry_version": 110,
  "selected_historical_record_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "ba16e25199265c199c5f6fa664cd94c6606bb9ff0eb538cf1ec6625421ac5a8a",
  "selected_historical_version": {
    "accession": "Q9ZPL5",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CGS1_TOBAC",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9ZPL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common tobacco\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Solanales\",\"Solanaceae\",\"Nicotianoideae\",\"Nicotianeae\",\"Nicotiana\"],\"scientificName\":\"Nicotiana tabacum\",\"taxonId\":4097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.160\"}],\"fullName\":{\"value\":\"Cystathionine gamma-synthase 1, chloroplastic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the first committed step of methionine (Met) biosynthesis. Catalyzes the formation of L-cystathionine from homoserine esters and L-cysteine, via a gamma-replacement reaction\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.5.1.160\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"name\":\"O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80891\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35235\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57590\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58161\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"10595588\",\"source\":\"PubMed\"}],\"name\":\"O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20397\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35235\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57661\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58161\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003962\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cystathionine gamma-synthase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030170\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:pyridoxal phosphate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Clausen T.\",\"Wahl M.C.\",\"Messerschmidt A.\",\"Huber R.\",\"Fuhrmann J.C.\",\"Laber B.\",\"Streber W.\",\"Steegborn C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10595588\"},{\"database\":\"DOI\",\"id\":\"10.1515/bc.1999.157\"}],\"citationType\":\"journal article\",\"firstPage\":\"1237\",\"id\":\"10595588\",\"journal\":\"Biol. Chem.\",\"lastPage\":\"1242\",\"publicationDate\":\"1999\",\"title\":\"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.\",\"volume\":\"380\"},\"referenceNumber\":3,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 97-540\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:56.568005+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZPL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H1",
  "excerpt": "ID   CGS1_TOBAC              Reviewed;         540 AA.\nAC   Q9ZPL5; W8SGH6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;\nDE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};\nDE   Flags: Precursor;\nGN   Name=CGS1 {ECO:0000305}; ORFNames=LOC107822634;\nOS   Nicotiana tabacum (Common tobacco).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;\nOC   Nicotiana.\nOX   NCBI_TaxID=4097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRX   PubMed=10595588; DOI=10.1515/bc.1999.157;\nRA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,\nRA   Streber W., Steegborn C.;\nRT   \"Cloning, purification and characterisation of cystathionine gamma-synthase\nRT   from Nicotiana tabacum.\";\nRL   Biol. Chem. 380:1237-1242(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the first committed step of methionine (Met)\nCC       biosynthesis. Catalyzes the formation of L-cystathionine from\nCC       homoserine esters and L-cysteine, via a gamma-replacement reaction.\nCC       {ECO:0000269|PubMed:10595588}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-phospho-L-homoserine + L-cysteine = L,L-cystathionine +\nCC         phosphate; Xref=Rhea:RHEA:80891, ChEBI:CHEBI:35235,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57590, ChEBI:CHEBI:58161;\nCC         EC=2.5.1.160; Evidence={ECO:0000269|PubMed:10595588};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine +\nCC         succinate + H(+); Xref=Rhea:RHEA:20397, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30031, ChEBI:CHEBI:35235, ChEBI:CHEBI:57661,\nCC         ChEBI:CHEBI:58161; Evidence={ECO:0000305|PubMed:10595588};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0003962; F:cystathionine gamma-synthase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0030170; F:pyridoxal phosphate binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:02.156603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89",
  "url": "https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0030170\nname: pyridoxal phosphate binding\nnamespace: molecular_function\ndef: \"Binding to pyridoxal 5' phosphate, 3-hydroxy-5-(hydroxymethyl)-2-methyl4-pyridine carboxaldehyde 5' phosphate, the biologically active form of vitamin B6.\" [GOC:mah, ISBN:0198506732]\nsubset: goslim_metagenomics\nis_a: GO:0043168 ! anion binding\nis_a: GO:0070279 ! vitamin B6 binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030170",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 163502-163510",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0050660\nname: flavin adenine dinucleotide binding\nnamespace: molecular_function\ndef: \"Binding to FAD, flavin-adenine dinucleotide, the coenzyme or the prosthetic group of various flavoprotein oxidoreductase enzymes, in either the oxidized form, FAD, or the reduced form, FADH2.\" [GOC:ai, GOC:imk, ISBN:0198506732]\nsynonym: \"FAD or FADH2 binding\" EXACT []\nsynonym: \"flavine-adenine dinucleotide binding\" EXACT []\nis_a: GO:0000166 ! nucleotide binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050660",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318393-318402",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0141148\nname: enoyl-[acyl-carrier-protein] reductase (NADPH) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a 2,3-saturated acyl-[ACP] + NADP+ = a (2E)-enoyl-[ACP] + H+ + NADPH.\" [RHEA:22564]\ncomment: This reaction completes each cycle of fatty acid elongation by catalyzing the stereospecific reduction of the double bond at position 2 of a growing fatty acid chain, while linked to the acyl- carrier protein, in an NADPH-dependent manner. Note that EC has reactions describing the stereo-specificity of the reaction with respect to NADP+ (cf. EC 1.3.1.39, EC 1.3.1.10 and EC 1.3.1.104).\nxref: EC:1.3.1.10\nxref: EC:1.3.1.104\nxref: EC:1.3.1.39\nxref: MetaCyc:ENOYL-ACP-REDUCT-NADPH-RXN\nxref: RHEA:22564\nxref: RHEA:41812\nis_a: GO:0016631 ! enoyl-[acyl-carrier-protein] reductase [NAD(P)H] activity\nproperty_value: skos:exactMatch EC:1.3.1.104\nproperty_value: skos:exactMatch MetaCyc:ENOYL-ACP-REDUCT-NADPH-RXN\nproperty_value: skos:exactMatch RHEA:22564\nproperty_value: skos:narrowMatch EC:1.3.1.10\nproperty_value: skos:narrowMatch EC:1.3.1.39\nproperty_value: skos:narrowMatch RHEA:41812\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0141148",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 446989-447008",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
