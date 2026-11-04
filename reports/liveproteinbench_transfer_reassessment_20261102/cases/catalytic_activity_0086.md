# catalytic_activity_0086

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0086.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — selenite + a quinone + H2O = selenate + a quinol

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLKKLYFTVLSFIAIVGVISLYIRLSEGMKMSALTSYSSWGLWIVFYIYFIGLSAGSFLLSTMVYVFNMKQFERIGKLALFTAFFSLMAGLLFVLIDLGHPERFWHTLVYRQPNSILSWEIQFYLIYMLLIVAEIWFLMREEFAQRAQSTKGLTKLFNRTLTLGYKVPNSQQKLEFHREQSHKWMKILGIAGIPTAVGVHGGTGSLFGVVMAKEYWFSGLTPIIFLVSALVSGAALMLFLYSFFGGAKKNGDSLLKELGTLLTLFIGIDLLLMIAEFLIGLYNPIHHERMTFNEILFGDRWFIFWIGQIGMVIILPILLITISKGKRLLMGLAGLSVVLGIVCVRWILVIPAYVAPHFDGLDSAYNSSRLLYEYSPNLLEWSSSVGLIGIVILLFSITVQLVPVFNKQKEVHQTHGKPTPEIHIKA

[Multiple Choices]
A. selenite + a quinone + H2O = selenate + a quinol
B. (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine
C. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
D. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry assigns this protein as selenate reductase subunit C and gives the reaction in choice A. Its cited publication concerns functional characterization of the respiratory selenate reductase complex, although the excerpts alone do not independently establish the experimental details.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is exceptionally hydrophobic and contains many long hydrophobic stretches, consistent with a multi-pass membrane protein or membrane-embedded enzyme subunit. A quinone-linked respiratory redox reaction is compatible with that context. The other choices correspond to soluble-enzyme activities: folate-dependent serine synthesis, protein phosphorylation, or ATP-driven DNA helicase activity; their expected catalytic machinery is not apparent in this strongly membrane-like sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-context knowledge meaningfully favors A over these particular alternatives. The sequence alone does not identify selenite as the substrate or prove the precise reaction, so the inference is comparative and probabilistic rather than a complete functional annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction is comparably supported by the sequence's strong multi-pass membrane character and the respiratory quinone-linked context of A.


### Important caveats

- The reviewer-only database excerpts are not original model inputs; they support the key but are not used as the basis for the transferability judgment.
- The cited functional-characterization paper was not independently reviewed here, and the database evidence code does not by itself establish that every reaction detail was directly measured.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is exceptionally hydrophobic and contains many long hydrophobic stretches, consistent with a multi-pass membrane protein or membrane-embedded enzyme subunit. A quinone-linked respiratory redox reaction is compatible with that context. The other choices correspond to soluble-enzyme activities: folate-dependent serine synthesis, protein phosphorylation, or ATP-driven DNA helicase activity; their expected catalytic machinery is not apparent in this strongly membrane-like sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-context knowledge meaningfully favors A over these particular alternatives. The sequence alone does not identify selenite as the substrate or prove the precise reaction, so the inference is comparative and probabilistic rather than a complete functional annotation."
  },
  "case_id": "catalytic_activity_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein as selenate reductase subunit C and gives the reaction in choice A. Its cited publication concerns functional characterization of the respiratory selenate reductase complex, although the excerpts alone do not independently establish the experimental details."
  },
  "important_caveats": [
    "The reviewer-only database excerpts are not original model inputs; they support the key but are not used as the basis for the transferability judgment.",
    "The cited functional-characterization paper was not independently reviewed here, and the database evidence code does not by itself establish that every reaction detail was directly measured."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence's strong multi-pass membrane character and the respiratory quinone-linked context of A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein as selenate reductase subunit C and gives the reaction in choice A. Its cited publication concerns functional characterization of the respiratory selenate reductase complex, although the excerpts alone do not independently establish the experimental details.",
    "evidence_ids": ["C4", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is exceptionally hydrophobic and contains many long hydrophobic stretches, consistent with a multi-pass membrane protein or membrane-embedded enzyme subunit. A quinone-linked respiratory redox reaction is compatible with that context. The other choices correspond to soluble-enzyme activities: folate-dependent serine synthesis, protein phosphorylation, or ATP-driven DNA helicase activity; their expected catalytic machinery is not apparent in this strongly membrane-like sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-context knowledge meaningfully favors A over these particular alternatives. The sequence alone does not identify selenite as the substrate or prove the precise reaction, so the inference is comparative and probabilistic rather than a complete functional annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence's strong multi-pass membrane character and the respiratory quinone-linked context of A."
  },
  "important_caveats": [
    "The reviewer-only database excerpts are not original model inputs; they support the key but are not used as the basis for the transferability judgment.",
    "The cited functional-characterization paper was not independently reviewed here, and the database evidence code does not by itself establish that every reaction detail was directly measured."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0A8X338 (sequence SHA-256 matched) annotates this protein as 'Selenate reductase subunit C' (EC 1.97.1.14) with the catalytic activity 'selenite + a quinone + H2O = selenate + a quinol', exactly matching choice A. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486, which characterizes the srdBCA operon encoding the respiratory selenate reductase complex. Subunit C is described as the 'membrane anchor subunit,' so the catalytic reaction is attributed to the complex as a whole and assigned to this entry. The annotation is database-assigned rather than directly demonstrated on the isolated anchor subunit, but it is the recorded catalytic activity for this sequence.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 426-residue sequence is overwhelmingly hydrophobic, with multiple long stretches of non-polar residues in the N-terminal ~100 residues and additional hydrophobic segments throughout, indicating a multi-pass transmembrane protein. This topology is fundamentally incompatible with choices B, C, and D: (B) serine hydroxymethyltransferase is a soluble cytoplasmic PLP-dependent TIM-barrel enzyme with no transmembrane segments; (C) protein kinases are soluble enzymes bearing conserved glycine-rich loops, HRD, and DFG catalytic motifs absent here; (D) helicases contain RecA-like ATPase domains with Walker A/B motifs and nucleic-acid-binding surfaces, none of which are present. Choice A describes a reaction catalyzed by a membrane-associated respiratory enzyme complex (EC 1.97.1.14), which is the only option consistent with a multi-pass membrane protein. The model need not identify 'selenate reductase' specifically; it only needs to recognize the membrane-protein architecture and eliminate the three soluble-enzyme options, a standard transfer from general knowledge of protein class structural requirements.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish the answer by recognizing the multi-pass membrane topology from the hydrophobicity pattern and eliminating the three soluble-enzyme alternatives (SHMT, kinase, helicase) on structural grounds. This is legitimate family/class-level inference from general biochemistry, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The membrane-protein topology unambiguously eliminates B (soluble PLP enzyme), C (soluble kinase with specific motifs), and D (helicase with RecA-like domains). Only A involves a membrane-associated respiratory complex, leaving no ambiguity among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic reaction is assigned to the complex (srdBCA) and attributed to the membrane anchor subunit C rather than demonstrated on the isolated anchor protein.
- The reference paper (PubMed:21357486) characterizes the srdBCA operon as a unit; subunit C is explicitly named 'membrane anchor subunit,' so the catalytic activity belongs to the assembled complex, not to subunit C acting alone.
- The specific identification as selenate reductase (vs. other membrane respiratory complexes such as nitrate or arsenate reductase) cannot be made from sequence alone without family-specific knowledge, but the multiple-choice format makes this irrelevant since only one membrane-respiratory option is offered.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 426-residue sequence is overwhelmingly hydrophobic, with multiple long stretches of non-polar residues in the N-terminal ~100 residues and additional hydrophobic segments throughout, indicating a multi-pass transmembrane protein. This topology is fundamentally incompatible with choices B, C, and D: (B) serine hydroxymethyltransferase is a soluble cytoplasmic PLP-dependent TIM-barrel enzyme with no transmembrane segments; (C) protein kinases are soluble enzymes bearing conserved glycine-rich loops, HRD, and DFG catalytic motifs absent here; (D) helicases contain RecA-like ATPase domains with Walker A/B motifs and nucleic-acid-binding surfaces, none of which are present. Choice A describes a reaction catalyzed by a membrane-associated respiratory enzyme complex (EC 1.97.1.14), which is the only option consistent with a multi-pass membrane protein. The model need not identify 'selenate reductase' specifically; it only needs to recognize the membrane-protein architecture and eliminate the three soluble-enzyme options, a standard transfer from general knowledge of protein class structural requirements.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by recognizing the multi-pass membrane topology from the hydrophobicity pattern and eliminating the three soluble-enzyme alternatives (SHMT, kinase, helicase) on structural grounds. This is legitimate family/class-level inference from general biochemistry, not a lookup of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X338 (sequence SHA-256 matched) annotates this protein as 'Selenate reductase subunit C' (EC 1.97.1.14) with the catalytic activity 'selenite + a quinone + H2O = selenate + a quinol', exactly matching choice A. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486, which characterizes the srdBCA operon encoding the respiratory selenate reductase complex. Subunit C is described as the 'membrane anchor subunit,' so the catalytic reaction is attributed to the complex as a whole and assigned to this entry. The annotation is database-assigned rather than directly demonstrated on the isolated anchor subunit, but it is the recorded catalytic activity for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic reaction is assigned to the complex (srdBCA) and attributed to the membrane anchor subunit C rather than demonstrated on the isolated anchor protein.",
    "The reference paper (PubMed:21357486) characterizes the srdBCA operon as a unit; subunit C is explicitly named 'membrane anchor subunit,' so the catalytic activity belongs to the assembled complex, not to subunit C acting alone.",
    "The specific identification as selenate reductase (vs. other membrane respiratory complexes such as nitrate or arsenate reductase) cannot be made from sequence alone without family-specific knowledge, but the multiple-choice format makes this irrelevant since only one membrane-respiratory option is offered."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The membrane-protein topology unambiguously eliminates B (soluble PLP enzyme), C (soluble kinase with specific motifs), and D (helicase with RecA-like domains). Only A involves a membrane-associated respiratory complex, leaving no ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0A8X338 (sequence SHA-256 matched) annotates this protein as 'Selenate reductase subunit C' (EC 1.97.1.14) with the catalytic activity 'selenite + a quinone + H2O = selenate + a quinol', exactly matching choice A. The annotation carries evidence code ECO:0000305 (inferred by similarity) referencing PubMed:21357486, which characterizes the srdBCA operon encoding the respiratory selenate reductase complex. Subunit C is described as the 'membrane anchor subunit,' so the catalytic reaction is attributed to the complex as a whole and assigned to this entry. The annotation is database-assigned rather than directly demonstrated on the isolated anchor subunit, but it is the recorded catalytic activity for this sequence.",
    "evidence_ids": ["C5", "C4", "C6", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 426-residue sequence is overwhelmingly hydrophobic, with multiple long stretches of non-polar residues in the N-terminal ~100 residues and additional hydrophobic segments throughout, indicating a multi-pass transmembrane protein. This topology is fundamentally incompatible with choices B, C, and D: (B) serine hydroxymethyltransferase is a soluble cytoplasmic PLP-dependent TIM-barrel enzyme with no transmembrane segments; (C) protein kinases are soluble enzymes bearing conserved glycine-rich loops, HRD, and DFG catalytic motifs absent here; (D) helicases contain RecA-like ATPase domains with Walker A/B motifs and nucleic-acid-binding surfaces, none of which are present. Choice A describes a reaction catalyzed by a membrane-associated respiratory enzyme complex (EC 1.97.1.14), which is the only option consistent with a multi-pass membrane protein. The model need not identify 'selenate reductase' specifically; it only needs to recognize the membrane-protein architecture and eliminate the three soluble-enzyme options, a standard transfer from general knowledge of protein class structural requirements.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by recognizing the multi-pass membrane topology from the hydrophobicity pattern and eliminating the three soluble-enzyme alternatives (SHMT, kinase, helicase) on structural grounds. This is legitimate family/class-level inference from general biochemistry, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The membrane-protein topology unambiguously eliminates B (soluble PLP enzyme), C (soluble kinase with specific motifs), and D (helicase with RecA-like domains). Only A involves a membrane-associated respiratory complex, leaving no ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic reaction is assigned to the complex (srdBCA) and attributed to the membrane anchor subunit C rather than demonstrated on the isolated anchor protein.",
    "The reference paper (PubMed:21357486) characterizes the srdBCA operon as a unit; subunit C is explicitly named 'membrane anchor subunit,' so the catalytic activity belongs to the assembled complex, not to subunit C acting alone.",
    "The specific identification as selenate reductase (vs. other membrane respiratory complexes such as nitrate or arsenate reductase) cannot be made from sequence alone without family-specific knowledge, but the multiple-choice format makes this irrelevant since only one membrane-respiratory option is offered."
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
  "benchmark_sequence_length": 426,
  "benchmark_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-03-04",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 426,
  "current_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0A8X338",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "selected_historical_source_sequence_length": 426,
  "selected_historical_source_sequence_sha256": "218a8fc8c9a5550707cff8e4e71529fa4d0cadfec3371e5a9738f79c411a7e67",
  "selected_historical_version": {
    "accession": "A0A0A8X338",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SRDC_MESS1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0A8X338\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-03-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Mesobacillus\"],\"scientificName\":\"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)\",\"taxonId\":1321606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase membrane anchor subunit\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase subunit C\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"name\":\"selenite + a quinone + H2O = selenate + a quinol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:51636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15075\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18212\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X338.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuroda M.\",\"Yamashita M.\",\"Miwa E.\",\"Imao K.\",\"Fujimoto N.\",\"Ono H.\",\"Nagano K.\",\"Sei K.\",\"Ike M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21357486\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01197-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"2141\",\"id\":\"21357486\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2148\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.\",\"volume\":\"193\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ83593.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS A SELENATE REDUCTASE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:56.888485+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f24d48c67ebe30dab27bb776e276107f0f50c197edcf4849b2ea2624ac4d4bbe",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X338.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   SRDC_MESS1              Reviewed;         426 AA.\nAC   A0A0A8X338; E9RFD0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-MAR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Selenate reductase subunit C {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};\nGN   Name=srdC {ECO:0000303|PubMed:21357486};\nGN   ORFNames=SAMD00020551_1551 {ECO:0000312|EMBL:GAM13407.1};\nOS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431\nOS   / SF-1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;\nOC   Mesobacillus.\nOX   NCBI_TaxID=1321606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Selenate reductase subunit C {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase membrane anchor subunit {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ83593.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE, AND\nRP   SUBUNIT.\nRC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;\nRX   PubMed=21357486; DOI=10.1128/jb.01197-10;\nRA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,\nRA   Sei K., Ike M.;\nRT   \"Molecular cloning and characterization of the srdBCA operon, encoding the\nRT   respiratory selenate reductase complex, from the selenate-reducing\nRT   bacterium Bacillus selenatarsenatis SF-1.\";\nRL   J. Bacteriol. 193:2141-2148(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=selenite + a quinone + H2O = selenate + a quinol;\nCC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;\nCC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:00.225132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eb155874ab7c90cb9f9b357a382d734672b54b5376824079e6a394ed2c9dea57",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X338?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
