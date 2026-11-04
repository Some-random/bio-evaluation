# pathway_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0064.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPQFSCLLPAFFLLVVFLFLLIKELRRYKSPKTTQKLPPGPPMLPIIGNLHQMASSLPHQNLKKLADKYGPLMHLKLGEISAVAVSSPRLAKEVLQTRGLAFADRPQSVVAKLMLHNCLGVTFSRYGDYWRQLRQIFAMELLSSKSVQSFSTIMEDELFAMVKSIESEAGRPIILADKLISYLYATLSRATLGRVCKGKETLIEVTGETLALSGAQSLEDIFPSVKIFAYLNPLRPKVRKLFNRIDGVLEDIINQQEKKLLSARVDNDQLQPEENDMLSVLLKLRNGKDSKVQVTNNDIKAIIFELFLAGTVGSSTTVEWAMSEMMKNPKVMEKAQHEVREVLKGKKRICQSDIQKLSYLKLVVKETLRLHPPAPLLFPRECRGQCEVDGYTIPAKAMVMVNCWALGRDPEHWIEADKFEPERFKNSSIDFIGNHFEYIPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN

[Multiple Choices]
A. ergot alkaloid biosynthesis. .
B. Alkaloid biosynthesis. .
C. L-homoserine from L-aspartate: step 1/3. .
D. nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence matches the cited UniProt entry, whose pathway annotation is Alkaloid biosynthesis and whose recommended name is Alstonine synthase. The annotation carries experimental evidence codes linked to a publication, supporting choice B; the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region and conserved heme-binding cysteine motif are consistent with a membrane-associated cytochrome P450. That makes a monooxygenase role more plausible than the offered homoserine- or nicotinamide-related alternatives, but P450 family features alone do not identify its substrate or distinguish general alkaloid biosynthesis from the narrower ergot alkaloid pathway.


**Missing item-specific fact**

> The protein's specific substrate or experimentally determined pathway role is needed to distinguish general alkaloid biosynthesis from ergot alkaloid biosynthesis.


**Reason**

> Transferable P450 knowledge narrows the choices but does not meaningfully resolve the two alkaloid-related options. Selecting B over A requires protein-specific functional knowledge not supplied in the sequence or context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports the broad alkaloid-biosynthesis choice for this protein; it does not support the ergot-specific alternative.


### Important caveats

- The sequence match and experimental evidence attribution come from reviewer-only database excerpts, not from the original model input.
- The source annotation supports the key but does not make the pathway identifiable from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region and conserved heme-binding cysteine motif are consistent with a membrane-associated cytochrome P450. That makes a monooxygenase role more plausible than the offered homoserine- or nicotinamide-related alternatives, but P450 family features alone do not identify its substrate or distinguish general alkaloid biosynthesis from the narrower ergot alkaloid pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific substrate or experimentally determined pathway role is needed to distinguish general alkaloid biosynthesis from ergot alkaloid biosynthesis.",
    "reason": "Transferable P450 knowledge narrows the choices but does not meaningfully resolve the two alkaloid-related options. Selecting B over A requires protein-specific functional knowledge not supplied in the sequence or context."
  },
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose pathway annotation is Alkaloid biosynthesis and whose recommended name is Alstonine synthase. The annotation carries experimental evidence codes linked to a publication, supporting choice B; the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and experimental evidence attribution come from reviewer-only database excerpts, not from the original model input.",
    "The source annotation supports the key but does not make the pathway identifiable from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports the broad alkaloid-biosynthesis choice for this protein; it does not support the ergot-specific alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, whose pathway annotation is Alkaloid biosynthesis and whose recommended name is Alstonine synthase. The annotation carries experimental evidence codes linked to a publication, supporting choice B; the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region and conserved heme-binding cysteine motif are consistent with a membrane-associated cytochrome P450. That makes a monooxygenase role more plausible than the offered homoserine- or nicotinamide-related alternatives, but P450 family features alone do not identify its substrate or distinguish general alkaloid biosynthesis from the narrower ergot alkaloid pathway.",
    "missing_item_specific_fact": "The protein's specific substrate or experimentally determined pathway role is needed to distinguish general alkaloid biosynthesis from ergot alkaloid biosynthesis.",
    "reason": "Transferable P450 knowledge narrows the choices but does not meaningfully resolve the two alkaloid-related options. Selecting B over A requires protein-specific functional knowledge not supplied in the sequence or context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports the broad alkaloid-biosynthesis choice for this protein; it does not support the ergot-specific alternative."
  },
  "important_caveats": [
    "The sequence match and experimental evidence attribution come from reviewer-only database excerpts, not from the original model input.",
    "The source annotation supports the key but does not make the pathway identifiable from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7LUJ4) for this sequence (Alstonine synthase from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is a cytochrome P450 (EC 1.14.19.-) involved in indole alkaloid biosynthesis, which falls under the general 'Alkaloid biosynthesis' pathway category in UniProt. Choice B matches this annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRRICPG' (the FxxGxxxCxG signature), along with the conserved P450 I-helix region and overall domain architecture (~500 aa, ER-membrane anchored). This immediately eliminates choices C (aspartate kinase, a small allosteric enzyme) and D (nicotinamide phosphoribosyltransferase, a small transferase) because neither is a P450. Between A and B: ergot alkaloid biosynthesis is a fungal-specific pathway (Claviceps purpurea and relatives) whose P450s are cytosolic or mitochondrial fungal enzymes. The N-terminal region of this sequence shows a cleavable signal peptide (MATPQFSCLLPAFFLLVVFLFLL) followed by a transmembrane anchor segment, the hallmark architecture of plant ER-membrane P450s involved in secondary metabolism. This plant-type membrane targeting is inconsistent with fungal ergot-alkaloid P450s. Therefore, the general 'Alkaloid biosynthesis' pathway (B) is the appropriate category for a plant P450 involved in alkaloid production, while the fungal-specific ergot pathway (A) is excluded.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 heme-binding motif is directly readable from the sequence, and the distinction between plant ER-membrane P450s and fungal cytosolic P450s is well-established general biology. The ergot alkaloid pathway being fungal-specific is transferable knowledge. These features meaningfully separate B from A, C, and D without requiring recall of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While ergot alkaloid biosynthesis is technically a subset of alkaloid biosynthesis, the specific pathway name 'ergot alkaloid biosynthesis' refers to the fungal Claviceps pathway, which is mechanistically and evolutionarily distinct from plant indole alkaloid biosynthesis. The plant-type membrane anchoring and the absence of fungal P450 characteristics clearly exclude A. Choices C and D are non-P450 enzyme steps and are straightforwardly eliminated by the P450 sequence signature.


### Important caveats

- The reviewer-only evidence confirms the UniProt pathway annotation is 'Alkaloid biosynthesis' (general category), not a more specific sub-pathway name. The benchmark uses this general category as the correct answer.
- The sequence's plant-type signal peptide and transmembrane anchor are strong but not absolutely diagnostic of plant origin without organism context; however, combined with the P450 architecture and the offered choices, the inference to B over A is well-supported.
- The firstPublicDate of the UniProt entry is 2025-06-18, and the underlying paper is from 2022; the sequence itself was deposited earlier, so the protein sequence was publicly available before the Swiss-Prot annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRRICPG' (the FxxGxxxCxG signature), along with the conserved P450 I-helix region and overall domain architecture (~500 aa, ER-membrane anchored). This immediately eliminates choices C (aspartate kinase, a small allosteric enzyme) and D (nicotinamide phosphoribosyltransferase, a small transferase) because neither is a P450. Between A and B: ergot alkaloid biosynthesis is a fungal-specific pathway (Claviceps purpurea and relatives) whose P450s are cytosolic or mitochondrial fungal enzymes. The N-terminal region of this sequence shows a cleavable signal peptide (MATPQFSCLLPAFFLLVVFLFLL) followed by a transmembrane anchor segment, the hallmark architecture of plant ER-membrane P450s involved in secondary metabolism. This plant-type membrane targeting is inconsistent with fungal ergot-alkaloid P450s. Therefore, the general 'Alkaloid biosynthesis' pathway (B) is the appropriate category for a plant P450 involved in alkaloid production, while the fungal-specific ergot pathway (A) is excluded.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif is directly readable from the sequence, and the distinction between plant ER-membrane P450s and fungal cytosolic P450s is well-established general biology. The ergot alkaloid pathway being fungal-specific is transferable knowledge. These features meaningfully separate B from A, C, and D without requiring recall of this exact protein's database entry."
  },
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7LUJ4) for this sequence (Alstonine synthase from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is a cytochrome P450 (EC 1.14.19.-) involved in indole alkaloid biosynthesis, which falls under the general 'Alkaloid biosynthesis' pathway category in UniProt. Choice B matches this annotation exactly."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the UniProt pathway annotation is 'Alkaloid biosynthesis' (general category), not a more specific sub-pathway name. The benchmark uses this general category as the correct answer.",
    "The sequence's plant-type signal peptide and transmembrane anchor are strong but not absolutely diagnostic of plant origin without organism context; however, combined with the P450 architecture and the offered choices, the inference to B over A is well-supported.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, and the underlying paper is from 2022; the sequence itself was deposited earlier, so the protein sequence was publicly available before the Swiss-Prot annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While ergot alkaloid biosynthesis is technically a subset of alkaloid biosynthesis, the specific pathway name 'ergot alkaloid biosynthesis' refers to the fungal Claviceps pathway, which is mechanistically and evolutionarily distinct from plant indole alkaloid biosynthesis. The plant-type membrane anchoring and the absence of fungal P450 characteristics clearly exclude A. Choices C and D are non-P450 enzyme steps and are straightforwardly eliminated by the P450 sequence signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7LUJ4) for this sequence (Alstonine synthase from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein is a cytochrome P450 (EC 1.14.19.-) involved in indole alkaloid biosynthesis, which falls under the general 'Alkaloid biosynthesis' pathway category in UniProt. Choice B matches this annotation exactly.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRRICPG' (the FxxGxxxCxG signature), along with the conserved P450 I-helix region and overall domain architecture (~500 aa, ER-membrane anchored). This immediately eliminates choices C (aspartate kinase, a small allosteric enzyme) and D (nicotinamide phosphoribosyltransferase, a small transferase) because neither is a P450. Between A and B: ergot alkaloid biosynthesis is a fungal-specific pathway (Claviceps purpurea and relatives) whose P450s are cytosolic or mitochondrial fungal enzymes. The N-terminal region of this sequence shows a cleavable signal peptide (MATPQFSCLLPAFFLLVVFLFLL) followed by a transmembrane anchor segment, the hallmark architecture of plant ER-membrane P450s involved in secondary metabolism. This plant-type membrane targeting is inconsistent with fungal ergot-alkaloid P450s. Therefore, the general 'Alkaloid biosynthesis' pathway (B) is the appropriate category for a plant P450 involved in alkaloid production, while the fungal-specific ergot pathway (A) is excluded.",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif is directly readable from the sequence, and the distinction between plant ER-membrane P450s and fungal cytosolic P450s is well-established general biology. The ergot alkaloid pathway being fungal-specific is transferable knowledge. These features meaningfully separate B from A, C, and D without requiring recall of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While ergot alkaloid biosynthesis is technically a subset of alkaloid biosynthesis, the specific pathway name 'ergot alkaloid biosynthesis' refers to the fungal Claviceps pathway, which is mechanistically and evolutionarily distinct from plant indole alkaloid biosynthesis. The plant-type membrane anchoring and the absence of fungal P450 characteristics clearly exclude A. Choices C and D are non-P450 enzyme steps and are straightforwardly eliminated by the P450 sequence signature."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the UniProt pathway annotation is 'Alkaloid biosynthesis' (general category), not a more specific sub-pathway name. The benchmark uses this general category as the correct answer.",
    "The sequence's plant-type signal peptide and transmembrane anchor are strong but not absolutely diagnostic of plant origin without organism context; however, combined with the P450 architecture and the offered choices, the inference to B over A is well-supported.",
    "The firstPublicDate of the UniProt entry is 2025-06-18, and the underlying paper is from 2022; the sequence itself was deposited earlier, so the protein sequence was publicly available before the Swiss-Prot annotation."
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
  "benchmark_sequence_length": 514,
  "benchmark_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 514,
  "current_source_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7LUJ4",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "selected_historical_source_sequence_length": 514,
  "selected_historical_source_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "selected_historical_version": {
    "accession": "A0A9E7LUJ4",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AS_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7LUJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 AS\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.14.19.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Alstonine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsAS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65382.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   AS_ALSSC                Reviewed;         514 AA.\nAC   A0A9E7LUJ4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Alstonine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsAS {ECO:0000303|PubMed:36349266};\nDE            EC=1.14.19.- {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Cytochrome P450 AS {ECO:0000303|PubMed:36349266};\nGN   Name=AS {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65382.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
