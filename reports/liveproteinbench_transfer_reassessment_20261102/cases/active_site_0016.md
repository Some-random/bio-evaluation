# active_site_0016

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0016.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 159 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. Position 64 (Nucleophile (Probable))
B. Position 159 (Proton donor)
C. Position 153 (catalytic acid/base residue)
D. Position 342 (Charge relay system)
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

> The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence.


### Important caveats

- The supporting database annotation is similarity-based, not direct experimental evidence for this protein.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based, not direct experimental evidence for this protein.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 159 as the proton donor. This annotation is transferred by similarity from another UniProt entry, so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich dinucleotide-binding motif and a downstream Tyr-X3-Lys motif consistent with a short-chain dehydrogenase/reductase. In this enzyme-family pattern, the catalytic Ser is often positioned shortly before the Tyr; here Ser159 lies 15 residues before Tyr174, making option B a credible family-based inference. Ser153 is another nearby serine, but it does not fit that spacing as well.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge gives a meaningful basis for favoring B over the offered alternatives. This is a probabilistic inference, not proof of the precise proton-donor role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence provides a plausible catalytic-motif basis for B; position 342 is beyond the 266-residue sequence."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based, not direct experimental evidence for this protein.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible.


### Important caveats

- The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.
- The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.
- Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.
- The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation."
  },
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.",
    "The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.",
    "Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.",
    "The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation at position 159 lists 'Proton donor' (evidence ECO:0000250, inferred by similarity to P0C0Y5, a characterized mannitol dehydrogenase). The residue at position 159 in the supplied 266-aa sequence is indeed Serine (S), consistent with the SDR-family catalytic tetrad mechanism (Ser-Tyr-Lys) in which the Ser acts as proton donor to the substrate. The annotation is computational/similarity-based rather than directly experimental for this exact protein, but the SDR proton-donor role of the Ser is a well-established family-level mechanism. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold glycine-rich motif 'GASGPRG' (positions 26–32), identifying it as an NAD(P)-dependent dehydrogenase. The 266-aa length and the downstream 'S…YxxxK' pattern (Ser159…Tyr174…Lys178) match the well-characterized SDR (Short-chain Dehydrogenase/Reductase) catalytic tetrad. In SDRs, the Ser of the tetrad is the proton donor/orienting residue, the Tyr is the catalytic acid/base, and the Lys is part of the charge relay that lowers the Tyr pKa. Applying this family-level mechanism: (A) position 64 is Ala—not a nucleophile, and SDRs do not employ nucleophilic catalysis; (C) position 153 is a Ser outside the canonical tetrad, and calling any Ser the 'catalytic acid/base' contradicts SDR mechanism (the Tyr fulfills that role); (D) position 342 exceeds the 266-residue sequence length and is impossible. Only (B) Ser159 as 'Proton donor' is consistent with the SDR tetrad geometry and mechanism.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the Rossmann fold, recognize the SDR family catalytic tetrad (S…YxxxK), and apply the well-established SDR mechanism (Ser = proton donor, Tyr = acid/base, Lys = charge relay) to eliminate A (Ala, no nucleophile in SDRs), C (Ser is not the acid/base in SDRs), and D (position 342 does not exist in a 266-aa protein). This is a concrete family-level inference from transferable SDR biochemistry, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated because position 342 exceeds the sequence length (266 aa). Option A is eliminated because position 64 is Ala, which is not a nucleophile and SDRs do not use nucleophilic catalysis. Option C is inconsistent with SDR mechanism because the catalytic acid/base is the Tyr (position 174), not a Ser. Only B remains defensible."
  },
  "important_caveats": [
    "The UniProt annotation at position 159 is based on similarity (ECO:0000250 to P0C0Y5), not direct experimental mutagenesis or structural determination of this exact protein.",
    "The SDR tetrad mechanism (Ser proton donor, Tyr acid/base, Lys charge relay) is well-established across the family but individual members may show mechanistic variations.",
    "Option D (position 342) is trivially eliminated by sequence length, making it a very easy distractor.",
    "The protein identity (NADP-dependent mannitol dehydrogenase, EC 1.1.1.138, Aureobasidium melanogenum) was not provided in the model input; identification relies on sequence pattern recognition."
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
  "benchmark_sequence_length": 266,
  "benchmark_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 266,
  "current_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223HDI5",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "selected_historical_source_sequence_length": 266,
  "selected_historical_source_sequence_sha256": "9ba750d830f9b17efbb379114b2586beae27b485e183fc99fdd2ab0bad2a96aa",
  "selected_historical_version": {
    "accession": "A0A223HDI5",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMTDH_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223HDI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.138\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"NADP-dependent mannitol dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MtDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0Y5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":107},\"start\":{\"modifier\":\"EXACT\",\"value\":107}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":140}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":174}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":208},\"start\":{\"modifier\":\"EXACT\",\"value\":208}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:44.241345+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   NMTDH_AURME             Reviewed;         266 AA.\nAC   A0A223HDI5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=NADP-dependent mannitol dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MtDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.138 {ECO:0000269|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        159\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        174\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        178\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P0C0Y5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         107\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         140\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         174\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         178\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         208\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.627063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
