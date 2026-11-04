# active_site_0071

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0071.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 186 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGKNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAVNSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPARVFASTADPGTTTADQVYKVGHNLLLAHAAALKVYRDNFQDTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQSLGPRLREFTRDQKKLLIGSYDYVGVNYYTATYVSSARPPNDNKAIFHTDGNFYTTDCKDGVLIGPLAGPAWLNIVPEGIYRCLQEIKAKYNNPVIYITENGVYEVNDTTKTLSEARVDTTRVDYLQDHLSYVLKARQQGVRVQGYFVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKRPQEDDGAFDTPRKRLKK

[Multiple Choices]
A. Position 277 (Nucleophile)
B. Position 206 (For beta-ketoacyl synthase activity)
C. Position 186 (Proton donor)
D. Position 962 (Proton acceptor; for dehydratase activity 1)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates position 186 as the proton donor. This is consistent with the glutamate in the conserved GH1 beta-glucosidase NEP motif. The annotation is transferred by similarity, not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has recognizable GH1 beta-glucosidase catalytic motifs, including the NEP motif with its proton-donor glutamate at position 186. GH1 family knowledge therefore supports C; the nucleophile is associated with a separate conserved motif, not the offered position 277, and position 962 is beyond the 540-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level motif inference meaningfully distinguishes C among these choices; it does not require recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options identify different residue roles and positions, and the conserved GH1 proton-donor motif supports only C.


### Important caveats

- The database active-site annotation is supported by similarity evidence (ECO:0000250), rather than direct experimental confirmation for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has recognizable GH1 beta-glucosidase catalytic motifs, including the NEP motif with its proton-donor glutamate at position 186. GH1 family knowledge therefore supports C; the nucleophile is associated with a separate conserved motif, not the offered position 277, and position 962 is beyond the 540-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level motif inference meaningfully distinguishes C among these choices; it does not require recalling this exact protein's database record."
  },
  "case_id": "active_site_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 186 as the proton donor. This is consistent with the glutamate in the conserved GH1 beta-glucosidase NEP motif. The annotation is transferred by similarity, not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The database active-site annotation is supported by similarity evidence (ECO:0000250), rather than direct experimental confirmation for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options identify different residue roles and positions, and the conserved GH1 proton-donor motif supports only C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 186 as the proton donor. This is consistent with the glutamate in the conserved GH1 beta-glucosidase NEP motif. The annotation is transferred by similarity, not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has recognizable GH1 beta-glucosidase catalytic motifs, including the NEP motif with its proton-donor glutamate at position 186. GH1 family knowledge therefore supports C; the nucleophile is associated with a separate conserved motif, not the offered position 277, and position 962 is beyond the 540-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level motif inference meaningfully distinguishes C among these choices; it does not require recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options identify different residue roles and positions, and the conserved GH1 proton-donor motif supports only C."
  },
  "important_caveats": [
    "The database active-site annotation is supported by similarity evidence (ECO:0000250), rather than direct experimental confirmation for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKN1 annotates position 186 as 'Proton donor' (Active site), matching the expected answer. The evidence code is ECO:0000250 (by similarity from Q7XSK0), so the annotation is computational/transferred rather than directly experimental, but it is present in the database record and consistent with the well-known NEP catalytic motif of glycoside hydrolase family 1. The other choices are contradicted by the annotation: the nucleophile is at position 421 (not 277), position 206 has no relevant annotation, and position 962 exceeds the 540-residue protein length.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the NEP motif at positions 185-187 (N185-E186-P187), which is the hallmark catalytic motif of glycoside hydrolase family 1 (GH1). In GH1 enzymes, the glutamate within the NEP motif acts as the general acid/proton donor. This is a highly conserved, well-characterized family-level feature (analogous to recognizing the Ser-His-Asp triad in serine proteases), making it transferable knowledge. Furthermore, the amino acid identities at the other candidate positions independently eliminate those choices: position 277 is Valine (cannot serve as a nucleophile, which requires Ser, Cys, Glu, Asp, or His); position 206 is Alanine (incompatible with any catalytic role, and the 'beta-ketoacyl synthase' description is irrelevant to a protein showing GH1-like features); position 962 exceeds the 540-residue protein length and is therefore impossible. The combination of NEP-motif recognition and elimination of chemically implausible alternatives provides a concrete, transferable path to Choice C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the NEP motif (positions 185-187) as the GH1 proton-donor signature, a textbook family-level feature learned from many GH1 glycosidases. The wrong choices are eliminated by basic chemical reasoning (Val and Ala cannot be catalytic residues) and by the protein length constraint (position 962 > 540). No fact specific to this exact protein beyond general GH1 family knowledge is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each wrong choice is independently eliminable: D is impossible (position exceeds sequence length), A and B assign catalytic roles to Val and Ala respectively (chemically implausible for nucleophile or beta-ketoacyl synthase catalysis), and B's functional description (beta-ketoacyl synthase) is inconsistent with the GH1-like sequence features. Only C is both chemically plausible and consistent with the NEP motif.


### Important caveats

- The UniProt annotation for position 186 carries evidence code ECO:0000250 (by similarity from Q7XSK0), meaning it is a computational transfer rather than direct experimental validation for this specific protein.
- The reviewer-only evidence confirms the protein is Ipecac alkaloid beta-glucosidase 9 (B6ZKN1) from Carapichea ipecacuanha, but this identification was not available to the evaluated model; the reasoning relies on recognizing the NEP motif from the raw sequence.
- The NEP motif recognition assumes the model can identify the motif without prior knowledge of the protein's identity, which is reasonable given the motif's prominence in GH1 biochemistry but does require the model to scan the sequence for this specific tripeptide pattern.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the NEP motif at positions 185-187 (N185-E186-P187), which is the hallmark catalytic motif of glycoside hydrolase family 1 (GH1). In GH1 enzymes, the glutamate within the NEP motif acts as the general acid/proton donor. This is a highly conserved, well-characterized family-level feature (analogous to recognizing the Ser-His-Asp triad in serine proteases), making it transferable knowledge. Furthermore, the amino acid identities at the other candidate positions independently eliminate those choices: position 277 is Valine (cannot serve as a nucleophile, which requires Ser, Cys, Glu, Asp, or His); position 206 is Alanine (incompatible with any catalytic role, and the 'beta-ketoacyl synthase' description is irrelevant to a protein showing GH1-like features); position 962 exceeds the 540-residue protein length and is therefore impossible. The combination of NEP-motif recognition and elimination of chemically implausible alternatives provides a concrete, transferable path to Choice C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the NEP motif (positions 185-187) as the GH1 proton-donor signature, a textbook family-level feature learned from many GH1 glycosidases. The wrong choices are eliminated by basic chemical reasoning (Val and Ala cannot be catalytic residues) and by the protein length constraint (position 962 > 540). No fact specific to this exact protein beyond general GH1 family knowledge is required."
  },
  "case_id": "active_site_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKN1 annotates position 186 as 'Proton donor' (Active site), matching the expected answer. The evidence code is ECO:0000250 (by similarity from Q7XSK0), so the annotation is computational/transferred rather than directly experimental, but it is present in the database record and consistent with the well-known NEP catalytic motif of glycoside hydrolase family 1. The other choices are contradicted by the annotation: the nucleophile is at position 421 (not 277), position 206 has no relevant annotation, and position 962 exceeds the 540-residue protein length."
  },
  "important_caveats": [
    "The UniProt annotation for position 186 carries evidence code ECO:0000250 (by similarity from Q7XSK0), meaning it is a computational transfer rather than direct experimental validation for this specific protein.",
    "The reviewer-only evidence confirms the protein is Ipecac alkaloid beta-glucosidase 9 (B6ZKN1) from Carapichea ipecacuanha, but this identification was not available to the evaluated model; the reasoning relies on recognizing the NEP motif from the raw sequence.",
    "The NEP motif recognition assumes the model can identify the motif without prior knowledge of the protein's identity, which is reasonable given the motif's prominence in GH1 biochemistry but does require the model to scan the sequence for this specific tripeptide pattern."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each wrong choice is independently eliminable: D is impossible (position exceeds sequence length), A and B assign catalytic roles to Val and Ala respectively (chemically implausible for nucleophile or beta-ketoacyl synthase catalysis), and B's functional description (beta-ketoacyl synthase) is inconsistent with the GH1-like sequence features. Only C is both chemically plausible and consistent with the NEP motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKN1 annotates position 186 as 'Proton donor' (Active site), matching the expected answer. The evidence code is ECO:0000250 (by similarity from Q7XSK0), so the annotation is computational/transferred rather than directly experimental, but it is present in the database record and consistent with the well-known NEP catalytic motif of glycoside hydrolase family 1. The other choices are contradicted by the annotation: the nucleophile is at position 421 (not 277), position 206 has no relevant annotation, and position 962 exceeds the 540-residue protein length.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the NEP motif at positions 185-187 (N185-E186-P187), which is the hallmark catalytic motif of glycoside hydrolase family 1 (GH1). In GH1 enzymes, the glutamate within the NEP motif acts as the general acid/proton donor. This is a highly conserved, well-characterized family-level feature (analogous to recognizing the Ser-His-Asp triad in serine proteases), making it transferable knowledge. Furthermore, the amino acid identities at the other candidate positions independently eliminate those choices: position 277 is Valine (cannot serve as a nucleophile, which requires Ser, Cys, Glu, Asp, or His); position 206 is Alanine (incompatible with any catalytic role, and the 'beta-ketoacyl synthase' description is irrelevant to a protein showing GH1-like features); position 962 exceeds the 540-residue protein length and is therefore impossible. The combination of NEP-motif recognition and elimination of chemically implausible alternatives provides a concrete, transferable path to Choice C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the NEP motif (positions 185-187) as the GH1 proton-donor signature, a textbook family-level feature learned from many GH1 glycosidases. The wrong choices are eliminated by basic chemical reasoning (Val and Ala cannot be catalytic residues) and by the protein length constraint (position 962 > 540). No fact specific to this exact protein beyond general GH1 family knowledge is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each wrong choice is independently eliminable: D is impossible (position exceeds sequence length), A and B assign catalytic roles to Val and Ala respectively (chemically implausible for nucleophile or beta-ketoacyl synthase catalysis), and B's functional description (beta-ketoacyl synthase) is inconsistent with the GH1-like sequence features. Only C is both chemically plausible and consistent with the NEP motif."
  },
  "important_caveats": [
    "The UniProt annotation for position 186 carries evidence code ECO:0000250 (by similarity from Q7XSK0), meaning it is a computational transfer rather than direct experimental validation for this specific protein.",
    "The reviewer-only evidence confirms the protein is Ipecac alkaloid beta-glucosidase 9 (B6ZKN1) from Carapichea ipecacuanha, but this identification was not available to the evaluated model; the reasoning relies on recognizing the NEP motif from the raw sequence.",
    "The NEP motif recognition assumes the model can identify the motif without prior knowledge of the protein's identity, which is reasonable given the motif's prominence in GH1 biochemistry but does require the model to scan the sequence for this specific tripeptide pattern."
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
  "benchmark_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "current_entry_audit": {
    "entryVersion": 46,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 44,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B6ZKN1",
  "selected_historical_entry_version": 44,
  "selected_historical_record_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "selected_historical_version": {
    "accession": "B6ZKN1",
    "database": "Swiss-Prot",
    "entryVersion": 44,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLU9_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B6ZKN1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":46,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecac alkaloid beta-glucosidase 9\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"IpeGLU9\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7XSK0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7XSK0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":421},\"start\":{\"modifier\":\"EXACT\",\"value\":421}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":36},\"start\":{\"modifier\":\"EXACT\",\"value\":36}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":140}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":185}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8L7J2\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":350},\"start\":{\"modifier\":\"EXACT\",\"value\":350}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":421},\"start\":{\"modifier\":\"EXACT\",\"value\":421}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":470},\"start\":{\"modifier\":\"EXACT\",\"value\":470}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1XH05\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:22798\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:22798\",\"name\":\"a beta-D-glucoside\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":486},\"start\":{\"modifier\":\"EXACT\",\"value\":486}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Controls the gate shape and acceptance of substrates\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SPP9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":393},\"start\":{\"modifier\":\"EXACT\",\"value\":393}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Quesada A.L.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18927081\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m806953200\"}],\"citationType\":\"journal article\",\"firstPage\":\"34650\",\"id\":\"18927081\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34659\",\"publicationDate\":\"2008\",\"title\":\"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.\",\"volume\":\"283\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02552.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"},{\"type\":\"TISSUE\",\"value\":\"Shoot\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H1",
  "excerpt": "ID   GLU9_CARIP              Reviewed;         540 AA.\nAC   B6ZKN1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 44.\nDE   RecName: Full=Ipecac alkaloid beta-glucosidase 9 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU9 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};\nGN   Name=GLU9 {ECO:0000303|PubMed:18927081};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAH02552.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   TISSUE=Root, and Shoot;\nRX   PubMed=18927081; DOI=10.1074/jbc.m806953200;\nRA   Nomura T., Quesada A.L., Kutchan T.M.;\nRT   \"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis\nRT   in Psychotria ipecacuanha.\";\nRL   J. Biol. Chem. 283:34650-34659(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        186\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q7XSK0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        421\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q7XSK0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         36\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         140\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         185..186\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         350\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8L7J2\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         421\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         470\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         486\nFT                   /ligand=\"a beta-D-glucoside\"\nFT                   /ligand_id=\"ChEBI:CHEBI:22798\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q1XH05\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H12",
  "excerpt": "FT   SITE            393\nFT                   /note=\"Controls the gate shape and acceptance of\nFT                   substrates\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SPP9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
