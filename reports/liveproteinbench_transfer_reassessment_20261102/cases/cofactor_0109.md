# cofactor_0109

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0109.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. heme b
B. Zn(2+)
C. NAD(+)
D. Fe(2+)
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

> The matched-sequence UniProt annotation lists Zn(2+) and says the protein binds two zinc ions per subunit. This annotation is transferred from a homolog rather than direct experimental evidence for this exact protein, so it supports the key with that qualification.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous Cys/His-rich region and resembles zinc-dependent plant alcohol-dehydrogenase/reductase family proteins. Transferable family knowledge makes zinc a meaningful choice over heme or Fe; NAD(+) is also a poor fit for the metal-binding pattern, and the related reductases commonly use NAD(P)H rather than NAD(+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and its metal-binding pattern provide a credible family-level basis for choosing Zn(2+) among these options. The exact protein's annotation is useful corroboration, but is not necessary to make that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, Zn(2+) is meaningfully distinguished by the sequence's Cys/His-rich pattern and the relevant enzyme-family regularity.


### Important caveats

- The supplied source annotation attributes the zinc assignment to similarity with a homolog; it does not establish direct experimental confirmation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous Cys/His-rich region and resembles zinc-dependent plant alcohol-dehydrogenase/reductase family proteins. Transferable family knowledge makes zinc a meaningful choice over heme or Fe; NAD(+) is also a poor fit for the metal-binding pattern, and the related reductases commonly use NAD(P)H rather than NAD(+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and its metal-binding pattern provide a credible family-level basis for choosing Zn(2+) among these options. The exact protein's annotation is useful corroboration, but is not necessary to make that distinction."
  },
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation lists Zn(2+) and says the protein binds two zinc ions per subunit. This annotation is transferred from a homolog rather than direct experimental evidence for this exact protein, so it supports the key with that qualification."
  },
  "important_caveats": [
    "The supplied source annotation attributes the zinc assignment to similarity with a homolog; it does not establish direct experimental confirmation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Zn(2+) is meaningfully distinguished by the sequence's Cys/His-rich pattern and the relevant enzyme-family regularity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation lists Zn(2+) and says the protein binds two zinc ions per subunit. This annotation is transferred from a homolog rather than direct experimental evidence for this exact protein, so it supports the key with that qualification.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous Cys/His-rich region and resembles zinc-dependent plant alcohol-dehydrogenase/reductase family proteins. Transferable family knowledge makes zinc a meaningful choice over heme or Fe; NAD(+) is also a poor fit for the metal-binding pattern, and the related reductases commonly use NAD(P)H rather than NAD(+).",
    "missing_item_specific_fact": "",
    "reason": "The sequence and its metal-binding pattern provide a credible family-level basis for choosing Zn(2+) among these options. The exact protein's annotation is useful corroboration, but is not necessary to make that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, Zn(2+) is meaningfully distinguished by the sequence's Cys/His-rich pattern and the relevant enzyme-family regularity."
  },
  "important_caveats": [
    "The supplied source annotation attributes the zinc assignment to similarity with a homolog; it does not establish direct experimental confirmation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H5) lists Zn(2+) as the cofactor with the note 'Binds 2 Zn(2+) ions per subunit,' based on similarity to P06525 (CAD2). The evidence code is ECO:0000250 (similarity transfer), making this a computational inference from a well-characterized homolog rather than direct experimental measurement of this exact protein. However, the protein is a CAD-family enzyme (EC 1.5.1.32, Vomilenine reductase), and the CAD family is well-established as zinc-dependent. The sequence contains recognizable zinc-binding motifs (GCLVGS, CGICHSDLHM) consistent with the MDR/CAD superfamily zinc site. The annotation is supported by family-level evidence, though the specific evidence code is transfer-based rather than direct experimental verification for this protein.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif 'GCLVGSCRKCDMCSQ' and 'CGICHSDLHM' — clusters of cysteine residues in positions characteristic of the zinc-binding site in the medium-chain dehydrogenase/reductase (MDR) superfamily, specifically the Cinnamyl Alcohol Dehydrogenase (CAD) subfamily. The 'GCLVGS' pattern is a well-known zinc-coordination signature shared across hundreds of CAD homologs (e.g., P06525, P12450, and numerous plant CADs). A model familiar with MDR-family zinc-binding motifs can recognize these cysteine clusters and infer Zn(2+) dependence. Additionally, the absence of heme-binding motifs (no Cys-His or His-X-X-X-His cytochrome signatures) rules out heme b; the absence of iron-specific ligand arrangements makes Fe(2+) unlikely. The key distinction between Zn(2+) and NAD+ rests on biochemical terminology: NAD+ is a co-substrate consumed in the redox reaction (EC 1.5.1.x class), while Zn(2+) is the catalytic metal cofactor. The sequence shows NADH-binding Rossmann-like features (GGLG) but the question asks for the 'cofactor,' which in strict usage refers to the metal ion. Family-level knowledge of CAD enzymes as zinc metalloenzymes meaningfully distinguishes B from the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The zinc-binding cysteine motifs (GCLVGS, CGICHSDLHM) are recognizable sequence features shared across the CAD/MDR family. A model with knowledge of other CAD proteins can transfer the zinc-dependence inference. The distinction between Zn(2+) as a catalytic cofactor and NAD+ as a co-substrate is a standard biochemical convention applicable across oxidoreductases. The answer does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> In broader biochemical usage, NAD+ is sometimes loosely called a 'cofactor' for oxidoreductases. The EC 1.5.1.32 classification implies NAD+/NADP+ involvement. However, in strict UniProt and classical enzymology terminology, 'cofactor' refers to the metal ion (Zn2+) while NAD+ is a co-substrate. The question wording 'cofactor required for catalytic activity' could be interpreted either way, but the presence of clear zinc-binding motifs and the standard usage in the field favor B. This is a minor terminological ambiguity rather than a true scientific ambiguity.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (similarity to P06525/CAD2), meaning it is a transferred inference rather than direct experimental measurement of zinc binding in this specific protein.
- The protein is annotated as a 'CAD2-homolog protein,' confirming family membership, but this name is not available to the evaluated model.
- NAD+ is a co-substrate for EC 1.5.1.32 reactions; the strict distinction between 'cofactor' (metal) and 'co-substrate' (NAD+) is the basis for choosing B over C.
- The sequence-match is confirmed (SHA256 match), so the evidence applies to the exact sequence presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif 'GCLVGSCRKCDMCSQ' and 'CGICHSDLHM' — clusters of cysteine residues in positions characteristic of the zinc-binding site in the medium-chain dehydrogenase/reductase (MDR) superfamily, specifically the Cinnamyl Alcohol Dehydrogenase (CAD) subfamily. The 'GCLVGS' pattern is a well-known zinc-coordination signature shared across hundreds of CAD homologs (e.g., P06525, P12450, and numerous plant CADs). A model familiar with MDR-family zinc-binding motifs can recognize these cysteine clusters and infer Zn(2+) dependence. Additionally, the absence of heme-binding motifs (no Cys-His or His-X-X-X-His cytochrome signatures) rules out heme b; the absence of iron-specific ligand arrangements makes Fe(2+) unlikely. The key distinction between Zn(2+) and NAD+ rests on biochemical terminology: NAD+ is a co-substrate consumed in the redox reaction (EC 1.5.1.x class), while Zn(2+) is the catalytic metal cofactor. The sequence shows NADH-binding Rossmann-like features (GGLG) but the question asks for the 'cofactor,' which in strict usage refers to the metal ion. Family-level knowledge of CAD enzymes as zinc metalloenzymes meaningfully distinguishes B from the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding cysteine motifs (GCLVGS, CGICHSDLHM) are recognizable sequence features shared across the CAD/MDR family. A model with knowledge of other CAD proteins can transfer the zinc-dependence inference. The distinction between Zn(2+) as a catalytic cofactor and NAD+ as a co-substrate is a standard biochemical convention applicable across oxidoreductases. The answer does not require memorizing this specific protein's database entry."
  },
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H5) lists Zn(2+) as the cofactor with the note 'Binds 2 Zn(2+) ions per subunit,' based on similarity to P06525 (CAD2). The evidence code is ECO:0000250 (similarity transfer), making this a computational inference from a well-characterized homolog rather than direct experimental measurement of this exact protein. However, the protein is a CAD-family enzyme (EC 1.5.1.32, Vomilenine reductase), and the CAD family is well-established as zinc-dependent. The sequence contains recognizable zinc-binding motifs (GCLVGS, CGICHSDLHM) consistent with the MDR/CAD superfamily zinc site. The annotation is supported by family-level evidence, though the specific evidence code is transfer-based rather than direct experimental verification for this protein."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity to P06525/CAD2), meaning it is a transferred inference rather than direct experimental measurement of zinc binding in this specific protein.",
    "The protein is annotated as a 'CAD2-homolog protein,' confirming family membership, but this name is not available to the evaluated model.",
    "NAD+ is a co-substrate for EC 1.5.1.32 reactions; the strict distinction between 'cofactor' (metal) and 'co-substrate' (NAD+) is the basis for choosing B over C.",
    "The sequence-match is confirmed (SHA256 match), so the evidence applies to the exact sequence presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "In broader biochemical usage, NAD+ is sometimes loosely called a 'cofactor' for oxidoreductases. The EC 1.5.1.32 classification implies NAD+/NADP+ involvement. However, in strict UniProt and classical enzymology terminology, 'cofactor' refers to the metal ion (Zn2+) while NAD+ is a co-substrate. The question wording 'cofactor required for catalytic activity' could be interpreted either way, but the presence of clear zinc-binding motifs and the standard usage in the field favor B. This is a minor terminological ambiguity rather than a true scientific ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H5) lists Zn(2+) as the cofactor with the note 'Binds 2 Zn(2+) ions per subunit,' based on similarity to P06525 (CAD2). The evidence code is ECO:0000250 (similarity transfer), making this a computational inference from a well-characterized homolog rather than direct experimental measurement of this exact protein. However, the protein is a CAD-family enzyme (EC 1.5.1.32, Vomilenine reductase), and the CAD family is well-established as zinc-dependent. The sequence contains recognizable zinc-binding motifs (GCLVGS, CGICHSDLHM) consistent with the MDR/CAD superfamily zinc site. The annotation is supported by family-level evidence, though the specific evidence code is transfer-based rather than direct experimental verification for this protein.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif 'GCLVGSCRKCDMCSQ' and 'CGICHSDLHM' — clusters of cysteine residues in positions characteristic of the zinc-binding site in the medium-chain dehydrogenase/reductase (MDR) superfamily, specifically the Cinnamyl Alcohol Dehydrogenase (CAD) subfamily. The 'GCLVGS' pattern is a well-known zinc-coordination signature shared across hundreds of CAD homologs (e.g., P06525, P12450, and numerous plant CADs). A model familiar with MDR-family zinc-binding motifs can recognize these cysteine clusters and infer Zn(2+) dependence. Additionally, the absence of heme-binding motifs (no Cys-His or His-X-X-X-His cytochrome signatures) rules out heme b; the absence of iron-specific ligand arrangements makes Fe(2+) unlikely. The key distinction between Zn(2+) and NAD+ rests on biochemical terminology: NAD+ is a co-substrate consumed in the redox reaction (EC 1.5.1.x class), while Zn(2+) is the catalytic metal cofactor. The sequence shows NADH-binding Rossmann-like features (GGLG) but the question asks for the 'cofactor,' which in strict usage refers to the metal ion. Family-level knowledge of CAD enzymes as zinc metalloenzymes meaningfully distinguishes B from the other choices.",
    "missing_item_specific_fact": "",
    "reason": "The zinc-binding cysteine motifs (GCLVGS, CGICHSDLHM) are recognizable sequence features shared across the CAD/MDR family. A model with knowledge of other CAD proteins can transfer the zinc-dependence inference. The distinction between Zn(2+) as a catalytic cofactor and NAD+ as a co-substrate is a standard biochemical convention applicable across oxidoreductases. The answer does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "In broader biochemical usage, NAD+ is sometimes loosely called a 'cofactor' for oxidoreductases. The EC 1.5.1.32 classification implies NAD+/NADP+ involvement. However, in strict UniProt and classical enzymology terminology, 'cofactor' refers to the metal ion (Zn2+) while NAD+ is a co-substrate. The question wording 'cofactor required for catalytic activity' could be interpreted either way, but the presence of clear zinc-binding motifs and the standard usage in the field favor B. This is a minor terminological ambiguity rather than a true scientific ambiguity."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity to P06525/CAD2), meaning it is a transferred inference rather than direct experimental measurement of zinc binding in this specific protein.",
    "The protein is annotated as a 'CAD2-homolog protein,' confirming family membership, but this name is not available to the evaluated model.",
    "NAD+ is a co-substrate for EC 1.5.1.32 reactions; the strict distinction between 'cofactor' (metal) and 'co-substrate' (NAD+) is the basis for choosing B over C.",
    "The sequence-match is confirmed (SHA256 match), so the evidence applies to the exact sequence presented."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ3",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "selected_historical_version": {
    "accession": "P0DXJ3",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VOR1_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"CAD2-homolog protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Protein RR6-2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsRR6-2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.32\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 Zn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61927.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"von Schumann G.\",\"Gao S.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11937349\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0968-0896(01)00435-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"1913\",\"id\":\"11937349\",\"journal\":\"Bioorg. Med. Chem.\",\"lastPage\":\"1918\",\"publicationDate\":\"2002\",\"title\":\"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"ACTIVITY REGULATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   VOR1_RAUSE              Reviewed;         360 AA.\nAC   P0DXJ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\nGN   Name=VR {ECO:0000305|PubMed:38212296};\nGN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61927.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY,\nRP   ACTIVITY REGULATION, AND TISSUE SPECIFICITY.\nRX   PubMed=11937349; DOI=10.1016/s0968-0896(01)00435-7;\nRA   von Schumann G., Gao S., Stoeckigt J.;\nRT   \"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the\nRT   biosynthesis of the therapeutically applied antiarrhythmic alkaloid\nRT   ajmaline.\";\nRL   Bioorg. Med. Chem. 10:1913-1918(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:P06525};\nCC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
