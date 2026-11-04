# cofactor_0180

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0180.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — FAD

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLRYRQVVGLLQRRNFSAGATSNGSGSSGGDKSGEDLHPIRRTLRLLGNDMRKVKEFFVPKEPETEKVPIPTQSQFHFSGERDKSKEATVPDDFQTHCDVLIIGGGGVGSSIAYWLKEKARDGLNVVVVEKDDTYAQSATRVSVGGLCQQFSLPENIQMSLFAADFLRSARKHFGEEVPLQFTPHGHLMLAGEEHAESLKRSSQLQNELGARNELLTADRLTARFPWLNTKGIALGCLGLEKEGWFNPLALLSNFRRSASGYGAHFISGQVVDFEFKSQTDISVVTDLGSNEGAYTGLEKAVIQLPDGTRRTCKFALCVISAGASSEQIARLARIGVGPGILRVPLPINARKRYMYAINSQAQSAPGMNMPMTIDPSGIFIRRDGLGGNYICVQDSTEEYNSAMIDPQYFAQHIRPHLYNRIPVLGEAQVVDSWAGCYDHNVYDENGILGAHPYYNNLYLATGFSGHGVQQSLAVGRAISELIMDGQFRTIDLSRLSFDRLIVDQPMFELNNVLS

[Multiple Choices]
A. tungstopterin
B. heme
C. FAD
D. NAD(+)
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

> The sequence-matched UniProt records annotate FAD as the cofactor, supporting choice C. The cited evidence is a curated annotation rather than direct experimental validation in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an enzyme-like region with a glycine-rich nucleotide-binding segment (including IIGGGGVGSSI), consistent with a flavin-dependent oxidoreductase family. Transferable sequence and family patterns can favor FAD over heme or tungstopterin, and distinguish a flavin cofactor from NAD(+) as the best offered choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level flavoprotein inference from the sequence provides a meaningful basis for choosing FAD among these alternatives, although the glycine-rich segment alone is not uniquely diagnostic and does not prove cofactor use.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference and the matched-record cofactor annotation both favor FAD; no other offered option is comparably supported.


### Important caveats

- The cited cofactor annotation has evidence code ECO:0000305; the supplied evidence does not establish direct experimental measurement.
- Reviewer-only protein identity and annotations are used to assess the key, not as inputs to the answerability inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an enzyme-like region with a glycine-rich nucleotide-binding segment (including IIGGGGVGSSI), consistent with a flavin-dependent oxidoreductase family. Transferable sequence and family patterns can favor FAD over heme or tungstopterin, and distinguish a flavin cofactor from NAD(+) as the best offered choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level flavoprotein inference from the sequence provides a meaningful basis for choosing FAD among these alternatives, although the glycine-rich segment alone is not uniquely diagnostic and does not prove cofactor use."
  },
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate FAD as the cofactor, supporting choice C. The cited evidence is a curated annotation rather than direct experimental validation in the supplied excerpts."
  },
  "important_caveats": [
    "The cited cofactor annotation has evidence code ECO:0000305; the supplied evidence does not establish direct experimental measurement.",
    "Reviewer-only protein identity and annotations are used to assess the key, not as inputs to the answerability inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference and the matched-record cofactor annotation both favor FAD; no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate FAD as the cofactor, supporting choice C. The cited evidence is a curated annotation rather than direct experimental validation in the supplied excerpts.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an enzyme-like region with a glycine-rich nucleotide-binding segment (including IIGGGGVGSSI), consistent with a flavin-dependent oxidoreductase family. Transferable sequence and family patterns can favor FAD over heme or tungstopterin, and distinguish a flavin cofactor from NAD(+) as the best offered choice.",
    "missing_item_specific_fact": "",
    "reason": "A family-level flavoprotein inference from the sequence provides a meaningful basis for choosing FAD among these alternatives, although the glycine-rich segment alone is not uniquely diagnostic and does not prove cofactor use."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference and the matched-record cofactor annotation both favor FAD; no other offered option is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor annotation has evidence code ECO:0000305; the supplied evidence does not establish direct experimental measurement.",
    "Reviewer-only protein identity and annotations are used to assess the key, not as inputs to the answerability inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VJ10 explicitly annotates FAD as the cofactor (ECO:0000305, inferred by curator). The protein is named 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (dFOXRED1). The FOXRED1 domain family is well-established as FAD-dependent across multiple organisms (yeast FAD1, human FOXRED1). The annotation is a curatorial inference based on domain family assignment rather than direct experimental FAD-binding measurement on this exact protein, but it is consistent with the established biochemistry of the FOXRED1 family.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a highly glycine-rich motif 'GGGGVGSSI' (~residues 115-123), which is characteristic of the Rossmann-fold glycine-rich loop found in FAD-binding oxidoreductases. More importantly, the overall sequence architecture matches the FOXRED1 (FAD-dependent oxidoreductase domain-containing protein 1) family, a well-characterized domain found in yeast FAD1, human FOXRED1, and orthologs across eukaryotes. This family is universally described as FAD-dependent in the literature. A model recognizing the FOXRED1 domain from its sequence signatures would transfer the FAD-dependence established across all known family members. The mitochondrial context (complex I biogenesis role) further supports a flavin-dependent oxidoreductase. Among the choices: tungstopterin is essentially restricted to archaeal formate dehydrogenases and is implausible for a eukaryotic mitochondrial protein; heme would require specific Cys-His or bis-His coordination motifs absent here; NAD+ shares Rossmann-fold binding but the FOXRED1 domain specifically binds FAD (the larger isoalloxazine ring accommodated by the domain architecture). Family-level inference from FOXRED1 homologs meaningfully distinguishes FAD from NAD+.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The FOXRED1 domain is a well-known protein family with established FAD dependence across yeast, human, and other eukaryotic homologs. The glycine-rich Rossmann motif and domain architecture are recognizable from sequence. This is legitimate family-level pattern transfer, not memorization of this specific fly protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The FOXRED1 family is unambiguously FAD-dependent. Tungstopterin is implausible for a eukaryotic protein. Heme-binding motifs are absent. While NAD+ also uses Rossmann folds, the specific FOXRED1 domain architecture is documented as FAD-specific across all known members, making FAD the clearly superior answer over NAD+.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000305 (inferred by curator), indicating it is based on domain-family assignment rather than direct experimental FAD-binding measurement on this exact Drosophila protein.
- The FOXRED1 family FAD-dependence is well-established in homologs (yeast FAD1, human FOXRED1), providing strong transferable evidence, but direct biochemical confirmation on dFOXRED1 specifically may rely on the family inference.
- Distinguishing FAD from NAD+ purely from the glycine-rich motif alone can be ambiguous; the FOXRED1 family identity is the stronger discriminator.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a highly glycine-rich motif 'GGGGVGSSI' (~residues 115-123), which is characteristic of the Rossmann-fold glycine-rich loop found in FAD-binding oxidoreductases. More importantly, the overall sequence architecture matches the FOXRED1 (FAD-dependent oxidoreductase domain-containing protein 1) family, a well-characterized domain found in yeast FAD1, human FOXRED1, and orthologs across eukaryotes. This family is universally described as FAD-dependent in the literature. A model recognizing the FOXRED1 domain from its sequence signatures would transfer the FAD-dependence established across all known family members. The mitochondrial context (complex I biogenesis role) further supports a flavin-dependent oxidoreductase. Among the choices: tungstopterin is essentially restricted to archaeal formate dehydrogenases and is implausible for a eukaryotic mitochondrial protein; heme would require specific Cys-His or bis-His coordination motifs absent here; NAD+ shares Rossmann-fold binding but the FOXRED1 domain specifically binds FAD (the larger isoalloxazine ring accommodated by the domain architecture). Family-level inference from FOXRED1 homologs meaningfully distinguishes FAD from NAD+.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The FOXRED1 domain is a well-known protein family with established FAD dependence across yeast, human, and other eukaryotic homologs. The glycine-rich Rossmann motif and domain architecture are recognizable from sequence. This is legitimate family-level pattern transfer, not memorization of this specific fly protein's annotation."
  },
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ10 explicitly annotates FAD as the cofactor (ECO:0000305, inferred by curator). The protein is named 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (dFOXRED1). The FOXRED1 domain family is well-established as FAD-dependent across multiple organisms (yeast FAD1, human FOXRED1). The annotation is a curatorial inference based on domain family assignment rather than direct experimental FAD-binding measurement on this exact protein, but it is consistent with the established biochemistry of the FOXRED1 family."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000305 (inferred by curator), indicating it is based on domain-family assignment rather than direct experimental FAD-binding measurement on this exact Drosophila protein.",
    "The FOXRED1 family FAD-dependence is well-established in homologs (yeast FAD1, human FOXRED1), providing strong transferable evidence, but direct biochemical confirmation on dFOXRED1 specifically may rely on the family inference.",
    "Distinguishing FAD from NAD+ purely from the glycine-rich motif alone can be ambiguous; the FOXRED1 family identity is the stronger discriminator."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FOXRED1 family is unambiguously FAD-dependent. Tungstopterin is implausible for a eukaryotic protein. Heme-binding motifs are absent. While NAD+ also uses Rossmann folds, the specific FOXRED1 domain architecture is documented as FAD-specific across all known members, making FAD the clearly superior answer over NAD+."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ10 explicitly annotates FAD as the cofactor (ECO:0000305, inferred by curator). The protein is named 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (dFOXRED1). The FOXRED1 domain family is well-established as FAD-dependent across multiple organisms (yeast FAD1, human FOXRED1). The annotation is a curatorial inference based on domain family assignment rather than direct experimental FAD-binding measurement on this exact protein, but it is consistent with the established biochemistry of the FOXRED1 family.",
    "evidence_ids": ["C5", "C4", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a highly glycine-rich motif 'GGGGVGSSI' (~residues 115-123), which is characteristic of the Rossmann-fold glycine-rich loop found in FAD-binding oxidoreductases. More importantly, the overall sequence architecture matches the FOXRED1 (FAD-dependent oxidoreductase domain-containing protein 1) family, a well-characterized domain found in yeast FAD1, human FOXRED1, and orthologs across eukaryotes. This family is universally described as FAD-dependent in the literature. A model recognizing the FOXRED1 domain from its sequence signatures would transfer the FAD-dependence established across all known family members. The mitochondrial context (complex I biogenesis role) further supports a flavin-dependent oxidoreductase. Among the choices: tungstopterin is essentially restricted to archaeal formate dehydrogenases and is implausible for a eukaryotic mitochondrial protein; heme would require specific Cys-His or bis-His coordination motifs absent here; NAD+ shares Rossmann-fold binding but the FOXRED1 domain specifically binds FAD (the larger isoalloxazine ring accommodated by the domain architecture). Family-level inference from FOXRED1 homologs meaningfully distinguishes FAD from NAD+.",
    "missing_item_specific_fact": "",
    "reason": "The FOXRED1 domain is a well-known protein family with established FAD dependence across yeast, human, and other eukaryotic homologs. The glycine-rich Rossmann motif and domain architecture are recognizable from sequence. This is legitimate family-level pattern transfer, not memorization of this specific fly protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The FOXRED1 family is unambiguously FAD-dependent. Tungstopterin is implausible for a eukaryotic protein. Heme-binding motifs are absent. While NAD+ also uses Rossmann folds, the specific FOXRED1 domain architecture is documented as FAD-specific across all known members, making FAD the clearly superior answer over NAD+."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000305 (inferred by curator), indicating it is based on domain-family assignment rather than direct experimental FAD-binding measurement on this exact Drosophila protein.",
    "The FOXRED1 family FAD-dependence is well-established in homologs (yeast FAD1, human FOXRED1), providing strong transferable evidence, but direct biochemical confirmation on dFOXRED1 specifically may rely on the family inference.",
    "Distinguishing FAD from NAD+ purely from the glycine-rich motif alone can be ambiguous; the FOXRED1 family identity is the stronger discriminator."
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
  "benchmark_sequence_length": 515,
  "benchmark_sequence_sha256": "f295ddc7682b2e3ff4f82ab0bccabeb67219f9e6c0ec6a5255a9bb834282ad29",
  "current_entry_audit": {
    "entryVersion": 179,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 515,
  "current_source_sequence_sha256": "f295ddc7682b2e3ff4f82ab0bccabeb67219f9e6c0ec6a5255a9bb834282ad29",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 178,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJ10",
  "selected_historical_entry_version": 178,
  "selected_historical_record_sha256": "4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096",
  "selected_historical_source_sequence_length": 515,
  "selected_historical_source_sequence_sha256": "f295ddc7682b2e3ff4f82ab0bccabeb67219f9e6c0ec6a5255a9bb834282ad29",
  "selected_historical_version": {
    "accession": "Q9VJ10",
    "database": "Swiss-Prot",
    "entryVersion": 178,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "FXRD1_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJ10\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":179,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0002021\",\"source\":\"FlyBase\"}],\"value\":\"Protein lethal (2) 37Bb\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"value\":\"FAD-dependent oxidoreductase domain-containing protein 1 homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"value\":\"dFOXRED1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Murari A.\",\"Rhooms S.K.\",\"Garcia C.\",\"Liu T.\",\"Li H.\",\"Mishra B.\",\"Deshong C.\",\"Owusu-Ansah E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34386730\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.isci.2021.102869\"}],\"citationType\":\"journal article\",\"firstPage\":\"102869\",\"id\":\"34386730\",\"journal\":\"IScience\",\"lastPage\":\"102869\",\"publicationDate\":\"2021\",\"title\":\"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.\",\"volume\":\"24\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH COMPLEX 1\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:20.331974+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ10.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H1",
  "excerpt": "ID   FXRD1_DROME             Reviewed;         515 AA.\nAC   Q9VJ10;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 178.\nDE   RecName: Full=FAD-dependent oxidoreductase domain-containing protein 1 homolog {ECO:0000303|PubMed:34386730};\nDE            Short=dFOXRED1 {ECO:0000303|PubMed:34386730};\nDE   AltName: Full=Protein lethal (2) 37Bb {ECO:0000312|FlyBase:FBgn0002021};\nGN   Name=l(2)37Bb {ECO:0000312|FlyBase:FBgn0002021};\nGN   Synonyms=Bb {ECO:0000312|FlyBase:FBgn0002021},\nGN   l(2)35B2 {ECO:0000312|FlyBase:FBgn0002021};\nGN   ORFNames=CG10655 {ECO:0000312|FlyBase:FBgn0002021};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.250109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096",
  "url": "https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=FAD-dependent oxidoreductase domain-containing protein 1 homolog {ECO:0000303|PubMed:34386730};\nDE            Short=dFOXRED1 {ECO:0000303|PubMed:34386730};\nDE   AltName: Full=Protein lethal (2) 37Bb {ECO:0000312|FlyBase:FBgn0002021};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.250109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096",
  "url": "https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH COMPLEX 1.\nRX   PubMed=34386730; DOI=10.1016/j.isci.2021.102869;\nRA   Murari A., Rhooms S.K., Garcia C., Liu T., Li H., Mishra B., Deshong C.,\nRA   Owusu-Ansah E.;\nRT   \"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in\nRT   mitochondrial complex I biogenesis.\";\nRL   IScience 24:102869-102869(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.250109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096",
  "url": "https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692; Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:26.250109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096",
  "url": "https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
