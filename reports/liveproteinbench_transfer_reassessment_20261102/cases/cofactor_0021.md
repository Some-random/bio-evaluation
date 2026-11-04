# cofactor_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0021.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Cu(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTRQNVYELKDDTLSWYSRAVEEMKSRDINDPTSWWYQGAIHGYATYPSALTYWHDATGYPPSQQTVNSGFWNRCQHGTWYFLPWHRMYLFYFEEIVAKAIRDMGGPADWTLPYWNYCEAYNTSASPSNQQQALQIPPEFGSSQGPNADFASLWIKNRRNYVLNKNNVNPWPAMNEAEFTNSGGDISFGGGVTGFAHSGGQTGQLESLPHNVVHTDINGAMGNPDTAALDPIFWLHHANIDRLWQVWLAQAGRSNPVVNAWKDFRFKFHDANGQPVEIAVKDVETTQLLGYVYTPAFPLSSTTPARRSVPAMDVVGATSASFSVGDHMAPLDLTMVPQPARGARLLAARGGDEKRTILRISNVKGKGATSPIDLFITNRDNEEGNEENFVGCIGLFGLENASTPSVESDGSGLNFAIDISDTINKLRQRDDWDEDNIRVQLIPQSKQDSDVEINVGRVSLHSEID

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Cu(2+)
C. Fe(2+)
D. heme
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the UniProt entry annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation is attributed to experimental evidence from a cited publication, supporting choice B for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with a tyrosinase, including conserved histidine-rich regions characteristic of type-3 copper enzymes. Tyrosinases use copper at their catalytic site, making Cu(2+) a meaningful match among the choices; pantetheine 4'-phosphate, Fe(2+), and heme are not the characteristic cofactor for this enzyme family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition from the sequence and transferable knowledge of tyrosinase chemistry provide a credible basis to distinguish copper from the offered alternatives, even without knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme-family inference supports copper specifically among the listed options.


### Important caveats

- The experimental cofactor annotation is reviewer-only evidence, not part of the original model input.
- The sequence-based family inference supports copper but does not independently establish the exact number of bound copper ions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a tyrosinase, including conserved histidine-rich regions characteristic of type-3 copper enzymes. Tyrosinases use copper at their catalytic site, making Cu(2+) a meaningful match among the choices; pantetheine 4'-phosphate, Fe(2+), and heme are not the characteristic cofactor for this enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence and transferable knowledge of tyrosinase chemistry provide a credible basis to distinguish copper from the offered alternatives, even without knowing this exact protein's database annotation."
  },
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation is attributed to experimental evidence from a cited publication, supporting choice B for this protein."
  },
  "important_caveats": [
    "The experimental cofactor annotation is reviewer-only evidence, not part of the original model input.",
    "The sequence-based family inference supports copper but does not independently establish the exact number of bound copper ions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme-family inference supports copper specifically among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation is attributed to experimental evidence from a cited publication, supporting choice B for this protein.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with a tyrosinase, including conserved histidine-rich regions characteristic of type-3 copper enzymes. Tyrosinases use copper at their catalytic site, making Cu(2+) a meaningful match among the choices; pantetheine 4'-phosphate, Fe(2+), and heme are not the characteristic cofactor for this enzyme family.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence and transferable knowledge of tyrosinase chemistry provide a credible basis to distinguish copper from the offered alternatives, even without knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme-family inference supports copper specifically among the listed options."
  },
  "important_caveats": [
    "The experimental cofactor annotation is reviewer-only evidence, not part of the original model input.",
    "The sequence-based family inference supports copper but does not independently establish the exact number of bound copper ions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is Tyrosinase HcTyr1 (EC 1.14.18.1) from Hahella sp. CCB-MM4. UniProt annotates the cofactor as Cu(2+) with experimental evidence (ECO:0000269, PubMed:39382070) from X-ray crystallography at 1.97 Å (PDB 8B74), noting 'Binds 2 copper ions per subunit.' The expected answer B (Cu(2+)) is directly supported by structural and biochemical evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'HGYATYPSALTYWHDATGY' motif and additional HGY-containing stretches, which are hallmark sequence signatures of the tyrosinase/catechol oxidase superfamily (EC 1.14.18.1). Members of this superfamily—including mushroom tyrosinase, plant polyphenol oxidases, and bacterial tyrosinases—universally employ a binuclear Cu(2+) center coordinated by six conserved histidine residues (three per copper site). The sequence also shows multiple His-rich regions consistent with this copper-coordination geometry. The protein length (~466 aa) matches bacterial tyrosinases. None of the other options fit: pantetheine 4'-phosphate is for acyltransferases (no CoA-binding motifs present); Fe(2+) is for dioxygenases/peroxidases (no Fe-coordination motifs like the 2-His-1-carboxylate facial triad in canonical arrangement); heme requires CXXCH or similar heme-binding motifs (absent). Thus, recognizing the HGY motif as a tyrosinase family signature and applying the well-established family-level fact that tyrosinases are copper enzymes meaningfully distinguishes Cu(2+) from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HGY motif and His-rich pattern are transferable family-level sequence features of the tyrosinase superfamily. Knowledge that tyrosinases (a very well-studied enzyme class) require Cu(2+) for their binuclear active site is general biochemistry learned from many homologs. This allows a knowledgeable model to distinguish B from A, C, and D without knowing this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The HGY motif is specific to the tyrosinase/catechol oxidase superfamily, all members of which use Cu(2+). The other cofactors (pantetheine 4'-phosphate, Fe(2+), heme) have no supporting sequence evidence in this protein. Only B is defensible.


### Important caveats

- The HGY motif is strongly indicative but not absolutely exclusive to tyrosinases; however, combined with the overall His-rich pattern, length, and absence of motifs for other cofactors, the inference to Cu(2+) is robust.
- The reviewer evidence confirms experimental (X-ray crystallography) support for the Cu(2+) annotation, but this evidence was not available to the evaluated model.
- The sequence is from a halophilic bacterium; halophilic tyrosinases are well-characterized copper enzymes, adding further family-level context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'HGYATYPSALTYWHDATGY' motif and additional HGY-containing stretches, which are hallmark sequence signatures of the tyrosinase/catechol oxidase superfamily (EC 1.14.18.1). Members of this superfamily—including mushroom tyrosinase, plant polyphenol oxidases, and bacterial tyrosinases—universally employ a binuclear Cu(2+) center coordinated by six conserved histidine residues (three per copper site). The sequence also shows multiple His-rich regions consistent with this copper-coordination geometry. The protein length (~466 aa) matches bacterial tyrosinases. None of the other options fit: pantetheine 4'-phosphate is for acyltransferases (no CoA-binding motifs present); Fe(2+) is for dioxygenases/peroxidases (no Fe-coordination motifs like the 2-His-1-carboxylate facial triad in canonical arrangement); heme requires CXXCH or similar heme-binding motifs (absent). Thus, recognizing the HGY motif as a tyrosinase family signature and applying the well-established family-level fact that tyrosinases are copper enzymes meaningfully distinguishes Cu(2+) from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HGY motif and His-rich pattern are transferable family-level sequence features of the tyrosinase superfamily. Knowledge that tyrosinases (a very well-studied enzyme class) require Cu(2+) for their binuclear active site is general biochemistry learned from many homologs. This allows a knowledgeable model to distinguish B from A, C, and D without knowing this specific protein's database record."
  },
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Tyrosinase HcTyr1 (EC 1.14.18.1) from Hahella sp. CCB-MM4. UniProt annotates the cofactor as Cu(2+) with experimental evidence (ECO:0000269, PubMed:39382070) from X-ray crystallography at 1.97 Å (PDB 8B74), noting 'Binds 2 copper ions per subunit.' The expected answer B (Cu(2+)) is directly supported by structural and biochemical evidence."
  },
  "important_caveats": [
    "The HGY motif is strongly indicative but not absolutely exclusive to tyrosinases; however, combined with the overall His-rich pattern, length, and absence of motifs for other cofactors, the inference to Cu(2+) is robust.",
    "The reviewer evidence confirms experimental (X-ray crystallography) support for the Cu(2+) annotation, but this evidence was not available to the evaluated model.",
    "The sequence is from a halophilic bacterium; halophilic tyrosinases are well-characterized copper enzymes, adding further family-level context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HGY motif is specific to the tyrosinase/catechol oxidase superfamily, all members of which use Cu(2+). The other cofactors (pantetheine 4'-phosphate, Fe(2+), heme) have no supporting sequence evidence in this protein. Only B is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Tyrosinase HcTyr1 (EC 1.14.18.1) from Hahella sp. CCB-MM4. UniProt annotates the cofactor as Cu(2+) with experimental evidence (ECO:0000269, PubMed:39382070) from X-ray crystallography at 1.97 Å (PDB 8B74), noting 'Binds 2 copper ions per subunit.' The expected answer B (Cu(2+)) is directly supported by structural and biochemical evidence.",
    "evidence_ids": ["C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'HGYATYPSALTYWHDATGY' motif and additional HGY-containing stretches, which are hallmark sequence signatures of the tyrosinase/catechol oxidase superfamily (EC 1.14.18.1). Members of this superfamily—including mushroom tyrosinase, plant polyphenol oxidases, and bacterial tyrosinases—universally employ a binuclear Cu(2+) center coordinated by six conserved histidine residues (three per copper site). The sequence also shows multiple His-rich regions consistent with this copper-coordination geometry. The protein length (~466 aa) matches bacterial tyrosinases. None of the other options fit: pantetheine 4'-phosphate is for acyltransferases (no CoA-binding motifs present); Fe(2+) is for dioxygenases/peroxidases (no Fe-coordination motifs like the 2-His-1-carboxylate facial triad in canonical arrangement); heme requires CXXCH or similar heme-binding motifs (absent). Thus, recognizing the HGY motif as a tyrosinase family signature and applying the well-established family-level fact that tyrosinases are copper enzymes meaningfully distinguishes Cu(2+) from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The HGY motif and His-rich pattern are transferable family-level sequence features of the tyrosinase superfamily. Knowledge that tyrosinases (a very well-studied enzyme class) require Cu(2+) for their binuclear active site is general biochemistry learned from many homologs. This allows a knowledgeable model to distinguish B from A, C, and D without knowing this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HGY motif is specific to the tyrosinase/catechol oxidase superfamily, all members of which use Cu(2+). The other cofactors (pantetheine 4'-phosphate, Fe(2+), heme) have no supporting sequence evidence in this protein. Only B is defensible."
  },
  "important_caveats": [
    "The HGY motif is strongly indicative but not absolutely exclusive to tyrosinases; however, combined with the overall His-rich pattern, length, and absence of motifs for other cofactors, the inference to Cu(2+) is robust.",
    "The reviewer evidence confirms experimental (X-ray crystallography) support for the Cu(2+) annotation, but this evidence was not available to the evaluated model.",
    "The sequence is from a halophilic bacterium; halophilic tyrosinases are well-characterized copper enzymes, adding further family-level context."
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
  "benchmark_sequence_length": 466,
  "benchmark_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "current_entry_audit": {
    "entryVersion": 26,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-12-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 466,
  "current_source_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 24,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A261GRE4",
  "selected_historical_entry_version": 24,
  "selected_historical_record_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "selected_historical_source_sequence_length": 466,
  "selected_historical_source_sequence_sha256": "9995b12ae04ed7d37120f23f1e35c673a361e1e8e6a50c25ae994ce0fdc4f509",
  "selected_historical_version": {
    "accession": "A0A261GRE4",
    "database": "Swiss-Prot",
    "entryVersion": 24,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TYR1_HAHS4",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A261GRE4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":26,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-12-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Oceanospirillales\",\"Hahellaceae\",\"Hahella\"],\"scientificName\":\"Hahella sp. (strain CCB-MM4)\",\"taxonId\":1926491}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"value\":\"1.14.18.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"value\":\"Tyrosinase HcTyr1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29036\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39382070\",\"source\":\"PubMed\"}],\"name\":\"Cu(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9ZP19\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 copper ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"de Almeida Santos G.\",\"Englund A.N.B.\",\"Dalleywater E.L.\",\"Roehr A.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39382070\"},{\"database\":\"DOI\",\"id\":\"10.1002/2211-5463.13906\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"39382070\",\"journal\":\"FEBS Open Bio\",\"lastPage\":\"0\",\"publicationDate\":\"2024\",\"title\":\"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.\",\"volume\":\"0\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8B74\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CCB-MM4\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\",\"AUTO-CLEAVAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:44.415551+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A261GRE4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H1",
  "excerpt": "ID   TYR1_HAHS4              Reviewed;         466 AA.\nAC   A0A261GRE4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-DEC-2017, sequence version 1.\nDT   28-JAN-2026, entry version 24.\nDE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};\nDE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};\nGN   ORFNames=BTA51_09820 {ECO:0000312|EMBL:OZG74058.1};\nOS   Hahella sp. (strain CCB-MM4).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Oceanospirillales; Hahellaceae; Hahella.\nOX   NCBI_TaxID=1926491;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};\nDE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8B74}\nRP   X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,\nRP   DOMAIN, AND AUTO-CLEAVAGE.\nRC   STRAIN=CCB-MM4;\nRX   PubMed=39382070; DOI=10.1002/2211-5463.13906;\nRA   de Almeida Santos G., Englund A.N.B., Dalleywater E.L., Roehr A.K.;\nRT   \"Characterization of two bacterial tyrosinases from the halophilic\nRT   bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in\nRT   wetlands.\";\nRL   FEBS Open Bio 0:0-0(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)

```json
{
  "entry_version": 24,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Cu(2+); Xref=ChEBI:CHEBI:29036;\nCC         Evidence={ECO:0000269|PubMed:39382070};\nCC       Note=Binds 2 copper ions per subunit. {ECO:0000250|UniProtKB:Q9ZP19};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.781945+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c",
  "url": "https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
