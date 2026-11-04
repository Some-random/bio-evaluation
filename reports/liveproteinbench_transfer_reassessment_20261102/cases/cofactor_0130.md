# cofactor_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0130.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — &#91;2Fe-2S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. [4Fe-4S] cluster
B. FAD
C. [2Fe-2S] cluster
D. Mg(2+)
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

> The sequence-matched records identify a &#91;2Fe-2S&#93; cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing &#91;2Fe-2S&#93; over FAD or Mg(2+) alone; the family association also argues against &#91;4Fe-4S&#93; as the cluster choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The sequence-matched evidence lists both a &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two.


### Important caveats

- The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.
- The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing [2Fe-2S] over FAD or Mg(2+) alone; the family association also argues against [4Fe-4S] as the cluster choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched records identify a [2Fe-2S] cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive."
  },
  "important_caveats": [
    "The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.",
    "The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The sequence-matched evidence lists both a [2Fe-2S] cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched records identify a [2Fe-2S] cluster as a cofactor, with experimental evidence cited, so choice C is supported. The same records also list Mg(2+), making C non-exclusive.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s Cys-rich region and enzyme-like architecture are consistent with an IlvD/dihydroxy-acid-dehydratase family protein. Transferable knowledge of this family’s iron-sulfur cofactor gives a meaningful basis for choosing [2Fe-2S] over FAD or Mg(2+) alone; the family association also argues against [4Fe-4S] as the cluster choice.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition can support choice C without access to this protein’s exact database record. However, that does not make C the only defensible answer: Mg(2+) is also listed as a cofactor for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The sequence-matched evidence lists both a [2Fe-2S] cluster and Mg(2+) as cofactors. The singular wording and choices do not distinguish between these two."
  },
  "important_caveats": [
    "The reviewer-only evidence supports both cofactors, but the original input did not provide the protein’s name or database annotation.",
    "The family-based sequence inference supports the iron-sulfur choice; it does not independently establish the exact cofactor requirements or conditions for this specific protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q0CPG9) explicitly annotates a &#91;2Fe-2S&#93; cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 &#91;2Fe-2S&#93; cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the &#91;2Fe-2S&#93; cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the &#91;2Fe-2S&#93; cluster is the primary, mechanistically essential cofactor for DHAD catalysis.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with &#91;2Fe-2S&#93; coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of &#91;2Fe-2S&#93; tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of &#91;4Fe-4S&#93; radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the &#91;2Fe-2S&#93; cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between &#91;2Fe-2S&#93; and &#91;4Fe-4S&#93; follows from the cysteine spacing pattern and the DHAD family identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the DHAD family architecture and the characteristic &#91;2Fe-2S&#93; cysteine ligation pattern in the N-terminal region can distinguish option C from A (&#91;4Fe-4S&#93; has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's &#91;2Fe-2S&#93; dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt entry annotates both &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, &#91;2Fe-2S&#93; is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, &#91;2Fe-2S&#93; is considered THE cofactor of DHAD. The ambiguity is mild because the &#91;2Fe-2S&#93; cluster is the defining cofactor that distinguishes DHAD from most other enzymes.


### Important caveats

- The UniProt entry lists both &#91;2Fe-2S&#93; cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors &#91;2Fe-2S&#93; as the defining cofactor but creates mild ambiguity with Mg(2+).
- The &#91;2Fe-2S&#93; annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).
- The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.
- The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with [2Fe-2S] coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of [2Fe-2S] tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of [4Fe-4S] radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the [2Fe-2S] cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between [2Fe-2S] and [4Fe-4S] follows from the cysteine spacing pattern and the DHAD family identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the DHAD family architecture and the characteristic [2Fe-2S] cysteine ligation pattern in the N-terminal region can distinguish option C from A ([4Fe-4S] has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's [2Fe-2S] dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs."
  },
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the [2Fe-2S] cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the [2Fe-2S] cluster is the primary, mechanistically essential cofactor for DHAD catalysis."
  },
  "important_caveats": [
    "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors [2Fe-2S] as the defining cofactor but creates mild ambiguity with Mg(2+).",
    "The [2Fe-2S] annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.",
    "The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt entry annotates both [2Fe-2S] cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, [2Fe-2S] is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, [2Fe-2S] is considered THE cofactor of DHAD. The ambiguity is mild because the [2Fe-2S] cluster is the defining cofactor that distinguishes DHAD from most other enzymes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) explicitly annotates a [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269|PubMed:29995859), stating 'Binds 1 [2Fe-2S] cluster per subunit' (evidence C5, H4). The protein is identified as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9), a well-characterized enzyme family whose defining catalytic cofactor is the [2Fe-2S] cluster. Note that Mg(2+) is also annotated as a cofactor (C6, H5), but the [2Fe-2S] cluster is the primary, mechanistically essential cofactor for DHAD catalysis.",
    "evidence_ids": ["C5", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region of the sequence contains multiple cysteine residues at positions consistent with [2Fe-2S] coordination in the DHAD family: C in 'NPCNMHLHDLS' (~pos 75), C in 'GCDKNMPG' (~pos 143), C in 'GRGACGGMYTANT' (~pos 215), and C in 'GSSSCPADDPKK' (~pos 240). The spacing pattern (~68-72-25 residues) is characteristic of [2Fe-2S] tetrahedral cysteine ligation in DHAD, distinct from the CxxC...CxxC motifs typical of [4Fe-4S] radical SAM enzymes. The overall ~600-residue architecture with an N-terminal cluster-binding domain and a C-terminal catalytic domain matches the DHAD fold. DHAD (EC 4.2.1.9) is a well-known enzyme family whose hallmark is the [2Fe-2S] cluster required for radical-based dehydration catalysis. FAD would require a Rossmann fold (GxGxxG motif) which is absent. Mg(2+) alone cannot explain the cysteine-rich N-terminal region. The distinction between [2Fe-2S] and [4Fe-4S] follows from the cysteine spacing pattern and the DHAD family identity.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the DHAD family architecture and the characteristic [2Fe-2S] cysteine ligation pattern in the N-terminal region can distinguish option C from A ([4Fe-4S] has different Cys spacing), B (FAD requires Rossmann fold), and D (Mg2+ alone doesn't explain the Cys cluster). The DHAD family's [2Fe-2S] dependence is a well-established, transferable biochemical fact learned from E. coli IlvD and other homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt entry annotates both [2Fe-2S] cluster and Mg(2+) as cofactors for this protein (C5 and C6). The question asks for 'the specific cofactor' (singular), but both are experimentally verified cofactors. However, [2Fe-2S] is the more distinctive and mechanistically essential cofactor that defines DHAD's catalytic mechanism, while Mg2+ plays a more auxiliary structural/electrostatic role. In standard biochemistry pedagogy, [2Fe-2S] is considered THE cofactor of DHAD. The ambiguity is mild because the [2Fe-2S] cluster is the defining cofactor that distinguishes DHAD from most other enzymes."
  },
  "important_caveats": [
    "The UniProt entry lists both [2Fe-2S] cluster and Mg(2+) as cofactors; the question's singular phrasing ('the specific cofactor') slightly favors [2Fe-2S] as the defining cofactor but creates mild ambiguity with Mg(2+).",
    "The [2Fe-2S] annotation carries experimental evidence (ECO:0000269, PubMed:29995859) plus a similarity-based note referencing E. coli DHAD (P39522, ECO:0000250).",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, though the sequence itself dates to 2006.",
    "The protein is a mitochondrial precursor (Flags: Precursor), which is consistent with DHAD localization in fungi."
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
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P39522\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 [2Fe-2S] cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       Note=Binds 1 [2Fe-2S] cluster per subunit.\nCC       {ECO:0000250|UniProtKB:P39522};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
