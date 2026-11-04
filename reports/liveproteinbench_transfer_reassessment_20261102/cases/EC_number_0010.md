# EC_number_0010

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0010.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.6.1.5

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALVRFATIITVLCHLAIQDGAAKSFPHGEKAPFPLTLIHINDLHARFDETNQKSSTCTNSKECIAGIARVYHTIKQLKSEYKTKNPLYLNAGDNFQGTLWYNLLRWNVTAYFIKELPPDAMTLGNHEFDHSPKGLAPYLAELEKMKIPTVVANLEKNGEPALKDSKIARSIVLKVGNRKVGVIGALYDKTHLVAQTGMVTLTNSIEAVRKEAQELKKKNVNIIVVLSHCGLDGDKQLAEEAGDLIDVIVGAHSHSLLLNKDAKVPYDTKYDTIEGDYPLVVKKSNNHTVLITQARSFGKYVGRLTVNFDCEGEVQSWEGYPIYMNNSVKQDEEVLRELEPWRAEVKRLGTQVIGTTEVFLDRESCRWCECTLGDLIADAYADQYTNSTVQPVAFVQAGNFRNPIEKGDITNGLAIEAAPYGSSVDMIKLSGADLWSAIDHSFTLDDEFRYNTAQVSGMAVVADLSKKPYERVQSIDIVGANGAKTALKKDQIYYVVVPSYLADGKDGFAMLKKGTNRVTGPLDSDVLIEYVRKRQTIAKTMFQEKRVVIENHTNGTCSWDLDSQRYKPK

[Multiple Choices]
A. 3.6.1.5
B. 3.4.21.62
C. 2.3.1.193
D. 1.5.1.32
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

> The matched sequence's UniProt annotation assigns EC 3.6.1.5, and the catalytic-activity record gives the corresponding nucleotide-triphosphate hydrolysis reaction with experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a large enzyme domain with conserved polar and histidine-rich regions, consistent with a secreted nucleotide phosphohydrolase/apyrase. That family-level inference supports a phosphohydrolase choice (3.6.1.5) over the offered protease, acyltransferase, and oxidoreductase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of secreted apyrase-like enzymes provide a meaningful basis to distinguish the offered EC classes. This is a family-level inference, not proof of the exact substrate specificity or EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only A is a phosphohydrolase EC number; the other options describe substantially different catalytic classes.


### Important caveats

- The source supports the key with an experimentally evidenced annotation, but the sequence-based inference alone is not equivalent to a direct assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a large enzyme domain with conserved polar and histidine-rich regions, consistent with a secreted nucleotide phosphohydrolase/apyrase. That family-level inference supports a phosphohydrolase choice (3.6.1.5) over the offered protease, acyltransferase, and oxidoreductase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of secreted apyrase-like enzymes provide a meaningful basis to distinguish the offered EC classes. This is a family-level inference, not proof of the exact substrate specificity or EC assignment."
  },
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns EC 3.6.1.5, and the catalytic-activity record gives the corresponding nucleotide-triphosphate hydrolysis reaction with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The source supports the key with an experimentally evidenced annotation, but the sequence-based inference alone is not equivalent to a direct assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is a phosphohydrolase EC number; the other options describe substantially different catalytic classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns EC 3.6.1.5, and the catalytic-activity record gives the corresponding nucleotide-triphosphate hydrolysis reaction with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a large enzyme domain with conserved polar and histidine-rich regions, consistent with a secreted nucleotide phosphohydrolase/apyrase. That family-level inference supports a phosphohydrolase choice (3.6.1.5) over the offered protease, acyltransferase, and oxidoreductase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of secreted apyrase-like enzymes provide a meaningful basis to distinguish the offered EC classes. This is a family-level inference, not proof of the exact substrate specificity or EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is a phosphohydrolase EC number; the other options describe substantially different catalytic classes."
  },
  "important_caveats": [
    "The source supports the key with an experimentally evidenced annotation, but the sequence-based inference alone is not equivalent to a direct assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) carries EC 3.6.1.5 with evidence code ECO:0000269 (experimental evidence from PubMed:39294191, a 2024 Nat. Commun. paper reporting catalytic activity). The catalytic reaction is explicitly stated: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence matches the UniProt canonical sequence (570 AA, SHA-256 confirmed). The EC assignment is backed by experimental data, not merely computational annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a hydrophobic signal peptide (MALVRFATIITVLCHLAIQDGAAKSF...), indicating a secreted or membrane-anchored protein, consistent with an ecto-nucleotidase. Among the four choices, three belong to entirely different EC classes whose hallmark catalytic motifs are absent from the sequence: (B) 3.4.21.62 is a serine endopeptidase requiring the GDSGGP catalytic triad motif, which is not present; (C) 2.3.1.193 is an acyltransferase requiring transferase-specific motifs (e.g., HXXXD or similar), absent here; (D) 1.5.1.32 is an oxidoreductase acting on CH-NH donors, typically requiring FAD/NAD(P)-binding Rossmann-fold motifs (e.g., GxGxxG), which are not evident. The remaining option (A) 3.6.1.5 (ATP diphosphohydrolase / apyrase, a member of the NTPDase family) is consistent with the observed features: secreted protein architecture, ~570 AA length typical of NTPDase family members, multiple conserved cysteine residues (e.g., the SCRWC/CECTL pair near position ~370) matching the conserved disulfide-bond pattern of NTPDases, and the overall domain topology. NTPDase family proteins are well-characterized across many organisms (human CD39/NTPDase1, rat NTPDase2, Drosophila, and other mosquito species), and their conserved sequence motifs (NTPDase1–5 regions) are documented in the literature. A knowledgeable model could recognize the absence of protease, transferase, and oxidoreductase signatures while noting the secreted-protein architecture and cysteine pattern consistent with the NTPDase/apyrase family, thereby meaningfully favoring choice A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of choices B, C, and D rests on the well-established requirement of specific catalytic motifs (GDSGGP for serine proteases, Rossmann-fold for FAD/NAD oxidoreductases, acyltransferase motifs) that are absent from the sequence. The positive assignment to the NTPDase/apyrase family (EC 3.6.1.5) is supported by the secreted-protein architecture, length, conserved cysteine pattern, and general family-level sequence features known from other NTPDases across species. This constitutes a legitimate transferable inference from family-level knowledge rather than a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (hydrolase on anhydrides vs. hydrolase on peptide bonds vs. transferase vs. oxidoreductase). The absence of catalytic motifs for B, C, and D and the presence of NTPDase-consistent features for A provide a clear discrimination. No two options are simultaneously defensible.


### Important caveats

- The positive identification of NTPDase conserved motifs (NTPDase1–5 regions) from the raw sequence is somewhat challenging without a motif database; the argument relies more heavily on the elimination of the other three classes and the general secreted-protein/cysteine-pattern consistency.
- EC 3.6.1.5 (apyrase/ATP diphosphohydrolase) and EC 3.6.1.3 (NTPDase) are closely related; the specific assignment to 3.6.1.5 vs. 3.6.1.3 would require knowledge of the substrate specificity (ATP→AMP vs. broader nucleoside triphosphate hydrolysis), which is not trivially derivable from sequence alone. However, among the four offered choices, only 3.6.1.5 falls in the correct EC class.
- The experimental evidence (PubMed:39294191, 2024) confirming EC 3.6.1.5 was published after the original 2000 sequence characterization; the author's source snapshot date is unknown, but the sequence itself is unchanged since 2007.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a hydrophobic signal peptide (MALVRFATIITVLCHLAIQDGAAKSF...), indicating a secreted or membrane-anchored protein, consistent with an ecto-nucleotidase. Among the four choices, three belong to entirely different EC classes whose hallmark catalytic motifs are absent from the sequence: (B) 3.4.21.62 is a serine endopeptidase requiring the GDSGGP catalytic triad motif, which is not present; (C) 2.3.1.193 is an acyltransferase requiring transferase-specific motifs (e.g., HXXXD or similar), absent here; (D) 1.5.1.32 is an oxidoreductase acting on CH-NH donors, typically requiring FAD/NAD(P)-binding Rossmann-fold motifs (e.g., GxGxxG), which are not evident. The remaining option (A) 3.6.1.5 (ATP diphosphohydrolase / apyrase, a member of the NTPDase family) is consistent with the observed features: secreted protein architecture, ~570 AA length typical of NTPDase family members, multiple conserved cysteine residues (e.g., the SCRWC/CECTL pair near position ~370) matching the conserved disulfide-bond pattern of NTPDases, and the overall domain topology. NTPDase family proteins are well-characterized across many organisms (human CD39/NTPDase1, rat NTPDase2, Drosophila, and other mosquito species), and their conserved sequence motifs (NTPDase1–5 regions) are documented in the literature. A knowledgeable model could recognize the absence of protease, transferase, and oxidoreductase signatures while noting the secreted-protein architecture and cysteine pattern consistent with the NTPDase/apyrase family, thereby meaningfully favoring choice A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of choices B, C, and D rests on the well-established requirement of specific catalytic motifs (GDSGGP for serine proteases, Rossmann-fold for FAD/NAD oxidoreductases, acyltransferase motifs) that are absent from the sequence. The positive assignment to the NTPDase/apyrase family (EC 3.6.1.5) is supported by the secreted-protein architecture, length, conserved cysteine pattern, and general family-level sequence features known from other NTPDases across species. This constitutes a legitimate transferable inference from family-level knowledge rather than a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) carries EC 3.6.1.5 with evidence code ECO:0000269 (experimental evidence from PubMed:39294191, a 2024 Nat. Commun. paper reporting catalytic activity). The catalytic reaction is explicitly stated: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence matches the UniProt canonical sequence (570 AA, SHA-256 confirmed). The EC assignment is backed by experimental data, not merely computational annotation."
  },
  "important_caveats": [
    "The positive identification of NTPDase conserved motifs (NTPDase1–5 regions) from the raw sequence is somewhat challenging without a motif database; the argument relies more heavily on the elimination of the other three classes and the general secreted-protein/cysteine-pattern consistency.",
    "EC 3.6.1.5 (apyrase/ATP diphosphohydrolase) and EC 3.6.1.3 (NTPDase) are closely related; the specific assignment to 3.6.1.5 vs. 3.6.1.3 would require knowledge of the substrate specificity (ATP→AMP vs. broader nucleoside triphosphate hydrolysis), which is not trivially derivable from sequence alone. However, among the four offered choices, only 3.6.1.5 falls in the correct EC class.",
    "The experimental evidence (PubMed:39294191, 2024) confirming EC 3.6.1.5 was published after the original 2000 sequence characterization; the author's source snapshot date is unknown, but the sequence itself is unchanged since 2007."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase on anhydrides vs. hydrolase on peptide bonds vs. transferase vs. oxidoreductase). The absence of catalytic motifs for B, C, and D and the presence of NTPDase-consistent features for A provide a clear discrimination. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase) carries EC 3.6.1.5 with evidence code ECO:0000269 (experimental evidence from PubMed:39294191, a 2024 Nat. Commun. paper reporting catalytic activity). The catalytic reaction is explicitly stated: a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+). The benchmark sequence matches the UniProt canonical sequence (570 AA, SHA-256 confirmed). The EC assignment is backed by experimental data, not merely computational annotation.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a hydrophobic signal peptide (MALVRFATIITVLCHLAIQDGAAKSF...), indicating a secreted or membrane-anchored protein, consistent with an ecto-nucleotidase. Among the four choices, three belong to entirely different EC classes whose hallmark catalytic motifs are absent from the sequence: (B) 3.4.21.62 is a serine endopeptidase requiring the GDSGGP catalytic triad motif, which is not present; (C) 2.3.1.193 is an acyltransferase requiring transferase-specific motifs (e.g., HXXXD or similar), absent here; (D) 1.5.1.32 is an oxidoreductase acting on CH-NH donors, typically requiring FAD/NAD(P)-binding Rossmann-fold motifs (e.g., GxGxxG), which are not evident. The remaining option (A) 3.6.1.5 (ATP diphosphohydrolase / apyrase, a member of the NTPDase family) is consistent with the observed features: secreted protein architecture, ~570 AA length typical of NTPDase family members, multiple conserved cysteine residues (e.g., the SCRWC/CECTL pair near position ~370) matching the conserved disulfide-bond pattern of NTPDases, and the overall domain topology. NTPDase family proteins are well-characterized across many organisms (human CD39/NTPDase1, rat NTPDase2, Drosophila, and other mosquito species), and their conserved sequence motifs (NTPDase1–5 regions) are documented in the literature. A knowledgeable model could recognize the absence of protease, transferase, and oxidoreductase signatures while noting the secreted-protein architecture and cysteine pattern consistent with the NTPDase/apyrase family, thereby meaningfully favoring choice A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of choices B, C, and D rests on the well-established requirement of specific catalytic motifs (GDSGGP for serine proteases, Rossmann-fold for FAD/NAD oxidoreductases, acyltransferase motifs) that are absent from the sequence. The positive assignment to the NTPDase/apyrase family (EC 3.6.1.5) is supported by the secreted-protein architecture, length, conserved cysteine pattern, and general family-level sequence features known from other NTPDases across species. This constitutes a legitimate transferable inference from family-level knowledge rather than a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (hydrolase on anhydrides vs. hydrolase on peptide bonds vs. transferase vs. oxidoreductase). The absence of catalytic motifs for B, C, and D and the presence of NTPDase-consistent features for A provide a clear discrimination. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The positive identification of NTPDase conserved motifs (NTPDase1–5 regions) from the raw sequence is somewhat challenging without a motif database; the argument relies more heavily on the elimination of the other three classes and the general secreted-protein/cysteine-pattern consistency.",
    "EC 3.6.1.5 (apyrase/ATP diphosphohydrolase) and EC 3.6.1.3 (NTPDase) are closely related; the specific assignment to 3.6.1.5 vs. 3.6.1.3 would require knowledge of the substrate specificity (ATP→AMP vs. broader nucleoside triphosphate hydrolysis), which is not trivially derivable from sequence alone. However, among the four offered choices, only 3.6.1.5 falls in the correct EC class.",
    "The experimental evidence (PubMed:39294191, 2024) confirming EC 3.6.1.5 was published after the original 2000 sequence characterization; the author's source snapshot date is unknown, but the sequence itself is unchanged since 2007."
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
  "benchmark_sequence_length": 570,
  "benchmark_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "current_entry_audit": {
    "entryVersion": 122,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 570,
  "current_source_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 120,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5TVM9",
  "selected_historical_entry_version": 120,
  "selected_historical_record_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "selected_historical_source_sequence_length": 570,
  "selected_historical_source_sequence_sha256": "3683149afc9d326cb4fb66628aaf088737022753f738d7c8dc443028715694e1",
  "selected_historical_version": {
    "accession": "Q5TVM9",
    "database": "Swiss-Prot",
    "entryVersion": 120,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "APY_ANOGA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5TVM9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":122,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"African malaria mosquito\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000007062\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Anophelinae\",\"Anopheles\"],\"scientificName\":\"Anopheles gambiae\",\"taxonId\":7165}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"5' nucleotidase ecto\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"Ag5'NTE\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10801886\",\"source\":\"PubMed\"}],\"value\":\"Apyrase-like 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10801886\",\"source\":\"PubMed\"}],\"value\":\"AgApyL1\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"3.6.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"Apyrase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"value\":\"AgApy\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.6.1.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294191\",\"source\":\"PubMed\"}],\"name\":\"a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:36795\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58043\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61557\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lombardo F.\",\"Di Cristina M.\",\"Spanos L.\",\"Louis C.\",\"Coluzzi M.\",\"Arca B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10801886\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m909547199\"}],\"citationType\":\"journal article\",\"firstPage\":\"23861\",\"id\":\"10801886\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"23868\",\"publicationDate\":\"2000\",\"title\":\"Promoter sequences of the putative Anopheles gambiae apyrase confer salivary gland expression in Drosophila melanogaster.\",\"volume\":\"275\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"Gasua\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB40347.1\",\"source\":\"EMBL\"}],\"type\":\"TISSUE\",\"value\":\"Thorax\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY BLOOD FEEDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Pala Z.R.\",\"Alves E Silva T.L.\",\"Minai M.\",\"Crews B.\",\"Patino-Martinez E.\",\"Carmona-Rivera C.\",\"Valenzuela Leon P.C.\",\"Martin-Martin I.\",\"Flores-Garcia Y.\",\"Cachau R.E.\",\"Muslinkina L.\",\"Gittis A.G.\",\"Srivastava N.\",\"Garboczi D.N.\",\"Alves D.A.\",\"Kaplan M.J.\",\"Fischer E.\",\"Calvo E.\",\"Vega-Rodriguez J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39294191\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-52502-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"8194\",\"id\":\"39294191\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"8194\",\"publicationDate\":\"2024\",\"title\":\"Mosquito salivary apyrase regulates blood meal hemostasis and facilitates malaria parasite transmission.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"FUNCTION\",\"FUNCTION (MICROBIAL INFECTION)\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"INTERACTION WITH HUMAN PLAT\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:23.238423+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0",
  "url": "https://rest.uniprot.org/uniprotkb/Q5TVM9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H1",
  "excerpt": "ID   APY_ANOGA               Reviewed;         570 AA.\nAC   Q5TVM9; Q9UB34;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 120.\nDE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};\nDE            Short=AgApy {ECO:0000303|PubMed:39294191};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};\nDE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};\nDE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};\nDE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};\nDE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};\nDE   Flags: Precursor;\nGN   ORFNames=AgaP_AGAP011026 {ECO:0000312|EMBL:EAA05427.2};\nOS   Anopheles gambiae (African malaria mosquito).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Anophelinae; Anopheles.\nOX   NCBI_TaxID=7165 {ECO:0000312|Proteomes:UP000007062};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};\nDE            Short=AgApy {ECO:0000303|PubMed:39294191};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};\nDE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};\nDE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};\nDE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};\nDE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB40347.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], DEVELOPMENTAL STAGE, AND INDUCTION BY BLOOD\nRP   FEEDING.\nRC   STRAIN=Gasua {ECO:0000312|EMBL:CAB40347.1};\nRC   TISSUE=Thorax {ECO:0000312|EMBL:CAB40347.1};\nRX   PubMed=10801886; DOI=10.1074/jbc.m909547199;\nRA   Lombardo F., Di Cristina M., Spanos L., Louis C., Coluzzi M., Arca B.;\nRT   \"Promoter sequences of the putative Anopheles gambiae apyrase confer\nRT   salivary gland expression in Drosophila melanogaster.\";\nRL   J. Biol. Chem. 275:23861-23868(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   IDENTIFICATION BY MASS SPECTROMETRY, FUNCTION, FUNCTION (MICROBIAL\nRP   INFECTION), CATALYTIC ACTIVITY, COFACTOR, INTERACTION WITH HUMAN PLAT,\nRP   SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=39294191; DOI=10.1038/s41467-024-52502-3;\nRA   Pala Z.R., Alves E Silva T.L., Minai M., Crews B., Patino-Martinez E.,\nRA   Carmona-Rivera C., Valenzuela Leon P.C., Martin-Martin I.,\nRA   Flores-Garcia Y., Cachau R.E., Muslinkina L., Gittis A.G., Srivastava N.,\nRA   Garboczi D.N., Alves D.A., Kaplan M.J., Fischer E., Calvo E.,\nRA   Vega-Rodriguez J.;\nRT   \"Mosquito salivary apyrase regulates blood meal hemostasis and facilitates\nRT   malaria parasite transmission.\";\nRL   Nat. Commun. 15:8194-8194(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)

```json
{
  "entry_version": 120,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside\nCC         5'-phosphate + 2 phosphate + 2 H(+); Xref=Rhea:RHEA:36795,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:58043, ChEBI:CHEBI:61557; EC=3.6.1.5;\nCC         Evidence={ECO:0000269|PubMed:39294191};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.028811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945",
  "url": "https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
