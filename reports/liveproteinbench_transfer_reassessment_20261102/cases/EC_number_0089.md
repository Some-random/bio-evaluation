# EC_number_0089

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0089.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.7.7.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. 2.7.7.1
B. 2.7.7.43
C. 2.7.1.52
D. 5.1.3.14
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt record, which assigns EC 2.7.7.1 and describes the NAD-forming reaction. The annotation cites both computational evidence and experimental evidence; this supports choice A, though the underlying studies were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble eukaryotic NMN adenylyltransferase-family enzyme, whose conserved catalytic domain supports adenylating NMN in NAD biosynthesis (EC 2.7.7.1). That family-level inference distinguishes A from the other offered reactions, including the different nucleotidyltransferase reaction in B and the kinase/isomerase alternatives C and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level sequence inference meaningfully favors A; the exact target's database annotation is not necessary to distinguish it among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the offered options matches the NMN adenylyltransferase activity. The source also assigns EC 2.7.7.18, but that number is not offered.


### Important caveats

- The evidence includes a computational assignment as well as annotations citing experimental studies; the studies were not independently assessed.
- Reviewer-only source identity and annotations were not original inputs and are not used as the basis for the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble eukaryotic NMN adenylyltransferase-family enzyme, whose conserved catalytic domain supports adenylating NMN in NAD biosynthesis (EC 2.7.7.1). That family-level inference distinguishes A from the other offered reactions, including the different nucleotidyltransferase reaction in B and the kinase/isomerase alternatives C and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level sequence inference meaningfully favors A; the exact target's database annotation is not necessary to distinguish it among these choices."
  },
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, which assigns EC 2.7.7.1 and describes the NAD-forming reaction. The annotation cites both computational evidence and experimental evidence; this supports choice A, though the underlying studies were not independently reviewed here."
  },
  "important_caveats": [
    "The evidence includes a computational assignment as well as annotations citing experimental studies; the studies were not independently assessed.",
    "Reviewer-only source identity and annotations were not original inputs and are not used as the basis for the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered options matches the NMN adenylyltransferase activity. The source also assigns EC 2.7.7.18, but that number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, which assigns EC 2.7.7.1 and describes the NAD-forming reaction. The annotation cites both computational evidence and experimental evidence; this supports choice A, though the underlying studies were not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble eukaryotic NMN adenylyltransferase-family enzyme, whose conserved catalytic domain supports adenylating NMN in NAD biosynthesis (EC 2.7.7.1). That family-level inference distinguishes A from the other offered reactions, including the different nucleotidyltransferase reaction in B and the kinase/isomerase alternatives C and D.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level sequence inference meaningfully favors A; the exact target's database annotation is not necessary to distinguish it among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the offered options matches the NMN adenylyltransferase activity. The source also assigns EC 2.7.7.18, but that number is not offered."
  },
  "important_caveats": [
    "The evidence includes a computational assignment as well as annotations citing experimental studies; the studies were not independently assessed.",
    "Reviewer-only source identity and annotations were not original inputs and are not used as the basis for the answerability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VC03 (Drosophila melanogaster NMNAT) is annotated with EC 2.7.7.1 (nicotinamide-nucleotide adenylyltransferase) supported by experimental evidence from three independent publications (PubMed 17132048, 19403820, 26616331) and RuleBase. The catalytic reaction NMN + ATP + H+ → NAD+ + PPi (RHEA:21360) is confirmed experimentally. The secondary EC 2.7.7.18 annotation is computational (RuleBase only). The primary EC assignment 2.7.7.1 is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple conserved motifs diagnostic of the NMNAT (nicotinamide mononucleotide adenylyltransferase) family: (1) 'GGIISPTHDSYGKKGLASALDRCAMVKLAT' contains the GGIIS and HDS motifs found in the NMNAT catalytic domain across species (human NMNAT1/2/3, bacterial NMNATs); (2) 'NHINSGGGGGDD' contains the glycine-rich loop characteristic of NMNAT enzymes; (3) the overall ~389 aa length and domain architecture match the NMNAT family fold. Against the alternatives: EC 2.7.7.43 (NAD+ synthase) requires a glutamine amidotransferase (GATase) domain with a Cys-His-Glu catalytic triad, which is absent here; EC 2.7.1.52 (KDO8P synthase) is a bacterial LPS-biosynthesis enzyme with a completely different fold and no sequence similarity to NMNAT; EC 5.1.3.14 is an isomerase (epimerase), a fundamentally different reaction class (EC class 5 vs 2). The presence of NMNAT-family catalytic motifs and absence of GATase or KDO8P-synthase features meaningfully distinguishes option A from B, C, and D using family-level knowledge of NMNAT enzymes learned from other organisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with the NMNAT protein family can recognize conserved catalytic motifs (GGIIS, HDS, GGG-rich loops) in this sequence and match them to the NMNAT catalytic domain architecture. The alternatives can be excluded: NAD+ synthase requires a GATase domain (absent), KDO8P synthase is a bacterial enzyme with unrelated sequence, and the isomerase is a different EC class entirely. This is legitimate family-level transfer, not memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes and families. The NMNAT-specific sequence motifs clearly point to EC 2.7.7.1. While the UniProt entry also lists EC 2.7.7.18 as a secondary (computational) annotation, this EC number is not among the choices, so there is no ambiguity among the offered alternatives.


### Important caveats

- The UniProt entry also annotates EC 2.7.7.18 (nicotinate-nucleotide adenylyltransferase) based solely on RuleBase (computational), but this EC number is not among the answer choices.
- The experimental evidence (ECO:0000269) supports EC 2.7.7.1 specifically; the 2.7.7.18 activity is predicted by similarity.
- The sequence length (389 aa) and motifs are consistent with the full-length Drosophila NMNAT isoform; alternative splice variants exist but the canonical entry matches the supplied sequence exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple conserved motifs diagnostic of the NMNAT (nicotinamide mononucleotide adenylyltransferase) family: (1) 'GGIISPTHDSYGKKGLASALDRCAMVKLAT' contains the GGIIS and HDS motifs found in the NMNAT catalytic domain across species (human NMNAT1/2/3, bacterial NMNATs); (2) 'NHINSGGGGGDD' contains the glycine-rich loop characteristic of NMNAT enzymes; (3) the overall ~389 aa length and domain architecture match the NMNAT family fold. Against the alternatives: EC 2.7.7.43 (NAD+ synthase) requires a glutamine amidotransferase (GATase) domain with a Cys-His-Glu catalytic triad, which is absent here; EC 2.7.1.52 (KDO8P synthase) is a bacterial LPS-biosynthesis enzyme with a completely different fold and no sequence similarity to NMNAT; EC 5.1.3.14 is an isomerase (epimerase), a fundamentally different reaction class (EC class 5 vs 2). The presence of NMNAT-family catalytic motifs and absence of GATase or KDO8P-synthase features meaningfully distinguishes option A from B, C, and D using family-level knowledge of NMNAT enzymes learned from other organisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the NMNAT protein family can recognize conserved catalytic motifs (GGIIS, HDS, GGG-rich loops) in this sequence and match them to the NMNAT catalytic domain architecture. The alternatives can be excluded: NAD+ synthase requires a GATase domain (absent), KDO8P synthase is a bacterial enzyme with unrelated sequence, and the isomerase is a different EC class entirely. This is legitimate family-level transfer, not memorization of this specific protein's annotation."
  },
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "C9",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (Drosophila melanogaster NMNAT) is annotated with EC 2.7.7.1 (nicotinamide-nucleotide adenylyltransferase) supported by experimental evidence from three independent publications (PubMed 17132048, 19403820, 26616331) and RuleBase. The catalytic reaction NMN + ATP + H+ → NAD+ + PPi (RHEA:21360) is confirmed experimentally. The secondary EC 2.7.7.18 annotation is computational (RuleBase only). The primary EC assignment 2.7.7.1 is well-supported."
  },
  "important_caveats": [
    "The UniProt entry also annotates EC 2.7.7.18 (nicotinate-nucleotide adenylyltransferase) based solely on RuleBase (computational), but this EC number is not among the answer choices.",
    "The experimental evidence (ECO:0000269) supports EC 2.7.7.1 specifically; the 2.7.7.18 activity is predicted by similarity.",
    "The sequence length (389 aa) and motifs are consistent with the full-length Drosophila NMNAT isoform; alternative splice variants exist but the canonical entry matches the supplied sequence exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes and families. The NMNAT-specific sequence motifs clearly point to EC 2.7.7.1. While the UniProt entry also lists EC 2.7.7.18 as a secondary (computational) annotation, this EC number is not among the choices, so there is no ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (Drosophila melanogaster NMNAT) is annotated with EC 2.7.7.1 (nicotinamide-nucleotide adenylyltransferase) supported by experimental evidence from three independent publications (PubMed 17132048, 19403820, 26616331) and RuleBase. The catalytic reaction NMN + ATP + H+ → NAD+ + PPi (RHEA:21360) is confirmed experimentally. The secondary EC 2.7.7.18 annotation is computational (RuleBase only). The primary EC assignment 2.7.7.1 is well-supported.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "C9", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple conserved motifs diagnostic of the NMNAT (nicotinamide mononucleotide adenylyltransferase) family: (1) 'GGIISPTHDSYGKKGLASALDRCAMVKLAT' contains the GGIIS and HDS motifs found in the NMNAT catalytic domain across species (human NMNAT1/2/3, bacterial NMNATs); (2) 'NHINSGGGGGDD' contains the glycine-rich loop characteristic of NMNAT enzymes; (3) the overall ~389 aa length and domain architecture match the NMNAT family fold. Against the alternatives: EC 2.7.7.43 (NAD+ synthase) requires a glutamine amidotransferase (GATase) domain with a Cys-His-Glu catalytic triad, which is absent here; EC 2.7.1.52 (KDO8P synthase) is a bacterial LPS-biosynthesis enzyme with a completely different fold and no sequence similarity to NMNAT; EC 5.1.3.14 is an isomerase (epimerase), a fundamentally different reaction class (EC class 5 vs 2). The presence of NMNAT-family catalytic motifs and absence of GATase or KDO8P-synthase features meaningfully distinguishes option A from B, C, and D using family-level knowledge of NMNAT enzymes learned from other organisms.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the NMNAT protein family can recognize conserved catalytic motifs (GGIIS, HDS, GGG-rich loops) in this sequence and match them to the NMNAT catalytic domain architecture. The alternatives can be excluded: NAD+ synthase requires a GATase domain (absent), KDO8P synthase is a bacterial enzyme with unrelated sequence, and the isomerase is a different EC class entirely. This is legitimate family-level transfer, not memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes and families. The NMNAT-specific sequence motifs clearly point to EC 2.7.7.1. While the UniProt entry also lists EC 2.7.7.18 as a secondary (computational) annotation, this EC number is not among the choices, so there is no ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The UniProt entry also annotates EC 2.7.7.18 (nicotinate-nucleotide adenylyltransferase) based solely on RuleBase (computational), but this EC number is not among the answer choices.",
    "The experimental evidence (ECO:0000269) supports EC 2.7.7.1 specifically; the 2.7.7.18 activity is predicted by similarity.",
    "The sequence length (389 aa) and motifs are consistent with the full-length Drosophila NMNAT isoform; alternative splice variants exist but the canonical entry matches the supplied sequence exactly."
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
  "benchmark_sequence_length": 389,
  "benchmark_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_entry_audit": {
    "entryVersion": 189,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 4
  },
  "current_record_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 389,
  "current_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 187,
      "exact_sequence_comparison": "matched",
      "sequence_version": 4
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VC03",
  "selected_historical_entry_version": 187,
  "selected_historical_record_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "selected_historical_source_sequence_length": 389,
  "selected_historical_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "selected_historical_version": {
    "accession": "Q9VC03",
    "database": "Swiss-Prot",
    "entryVersion": 187,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMNA_DROME",
    "sequenceVersion": 4
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VC03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":189,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":4}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"Nicotinamide mononucleotide adenylyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"dNmnat\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"2.7.7.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"Nicotinamide-nucleotide adenylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21361\"}}],\"reaction\":{\"ecNumber\":\"2.7.7.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"name\":\"beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21360\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:14649\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.7.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"name\":\"nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22860\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57502\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhai R.G.\",\"Cao Y.\",\"Hiesinger P.R.\",\"Zhou Y.\",\"Mehta S.Q.\",\"Schulze K.L.\",\"Verstreken P.\",\"Bellen H.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17132048\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pbio.0040416\"}],\"citationType\":\"journal article\",\"firstPage\":\"e416\",\"id\":\"17132048\",\"journal\":\"PLoS Biol.\",\"lastPage\":\"e416\",\"publicationDate\":\"2006\",\"title\":\"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.\",\"volume\":\"4\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasaki Y.\",\"Vohra B.P.\",\"Lund F.E.\",\"Milbrandt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19403820\"},{\"database\":\"DOI\",\"id\":\"10.1523/jneurosci.5469-08.2009\"}],\"citationType\":\"journal article\",\"firstPage\":\"5525\",\"id\":\"19403820\",\"journal\":\"J. Neurosci.\",\"lastPage\":\"5535\",\"publicationDate\":\"2009\",\"title\":\"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.\",\"volume\":\"29\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Ruan K.\",\"Zhu Y.\",\"Li C.\",\"Brazill J.M.\",\"Zhai R.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26616331\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms10057\"}],\"citationType\":\"journal article\",\"firstPage\":\"10057\",\"id\":\"26616331\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"10057\",\"publicationDate\":\"2015\",\"title\":\"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS\",\"NUCLEAR LOCALIZATION SIGNAL\",\"MUTAGENESIS OF LYS-380\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/9",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H1",
  "excerpt": "ID   NMNA_DROME              Reviewed;         389 AA.\nAC   Q9VC03; A0A0B4KHH7; Q7KS06; Q8T405;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 4.\nDT   28-JAN-2026, entry version 187.\nDE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\nGN   Name=Nmnat {ECO:0000303|PubMed:17132048, ECO:0000312|FlyBase:FBgn0039254};\nGN   ORFNames=CG13645 {ECO:0000312|FlyBase:FBgn0039254};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255.\nRX   PubMed=17132048; DOI=10.1371/journal.pbio.0040416;\nRA   Zhai R.G., Cao Y., Hiesinger P.R., Zhou Y., Mehta S.Q., Schulze K.L.,\nRA   Verstreken P., Bellen H.J.;\nRT   \"Drosophila NMNAT maintains neural integrity independent of its NAD\nRT   synthesis activity.\";\nRL   PLoS Biol. 4:e416-e416(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H4",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=19403820; DOI=10.1523/jneurosci.5469-08.2009;\nRA   Sasaki Y., Vohra B.P., Lund F.E., Milbrandt J.;\nRT   \"Nicotinamide mononucleotide adenylyl transferase-mediated axonal\nRT   protection requires enzymatic activity but not increased levels of neuronal\nRT   nicotinamide adenine dinucleotide.\";\nRL   J. Neurosci. 29:5525-5535(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H5",
  "excerpt": "RN   [10] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, ALTERNATIVE SPLICING,\nRP   INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS, NUCLEAR LOCALISAION SIGNAL,\nRP   AND MUTAGENESIS OF LYS-380.\nRX   PubMed=26616331; DOI=10.1038/ncomms10057;\nRA   Ruan K., Zhu Y., Li C., Brazill J.M., Zhai R.G.;\nRT   \"Alternative splicing of Drosophila Nmnat functions as a switch to enhance\nRT   neuroprotection under stress.\";\nRL   Nat. Commun. 6:10057-10057(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate\nCC         + NAD(+); Xref=Rhea:RHEA:21360, ChEBI:CHEBI:14649, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57540; EC=2.7.7.1;\nCC         Evidence={ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048,\nCC         ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21361;\nCC         Evidence={ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+)\nCC         + diphosphate; Xref=Rhea:RHEA:22860, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57502,\nCC         ChEBI:CHEBI:58437; EC=2.7.7.18;\nCC         Evidence={ECO:0000255|RuleBase:RU362021};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
