# GO_cellular_component_0142

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0142.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — mitochondrial inner membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQPPTRAPFFPFSLLRGRKARETCTCRSVASTEGPNTFGPRARPGCHAHQVAPSKESFHSSAFQLVSASRLSPLMSSCFVSFLRYPSFRPSAPFSAPPSSSTVPISTPSDFSHSAPASWRCVPTAPSALHAPFSFTTQAAHLSSCVFDGCSRLPCSEPGSPQTLQRALATTSATAFLRTACMSHRLRRRPDAWTSGCSGQTDNATASPCVRPLLRPPVDTASRAAANDKDAPQPTCFWRNARTSRAVHRNQTDMNFSSFSCSLRPCRHTLAKAAGHHAPLSRHSLQSLPESRIRGGTVSRGDSPGSLTLSPRNMSSDAMPVHPLYFPSAVPFSTTSGSNSSTFSCPSPSSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSPFLLSRSHSVDCRACPVSRAPPNPTSLQLLFSLFPFLWPTALKDRLRVLGSVACLVTAKVLTIQAPLLLANLVDAFQVLPHNSPLSPSGASPSSGDTSLLASSGETSSSLSPSAAPAEGAREAGKSGESAGRERRDEGSTVRLSPLAEGPASPATEERTAAGKAGTSVGGRDAGAVHALDTEHLRNTAQIVSVPLGVVCGFPVARIAATGFNELRSTLFTRVSQNASCDFSCHAFLHLHALALFHDKRAGELSVLISRGMKSVTALLNVLLFQMVPTALEFALVLYLLGSKVGGPVACITSLTMAVYVAFTAAVTARRTKIRKEMIAAEQQSVGLLVDSLANAEAVRFFTAEKGELSRFEAVQRRYAEKHVSVNQSLAFLNFGQQLIFNVGVLGSLAYTASQVAAGLLPVGHIVLVSSLLLQLAVPLNFVGTIYRETSLNLADLEKLYELMNHHPPIVNPPDARPFVLKGGAVAFENVRFAYPPSPLRPGSLPSKTGDDEKPEASRMLLDDVSFSVDAGKKVAIVGPSGVGKSTLIKLLFRMFDPASGTVRIDDQDVKELDLHSFRRQIGVVPQDMVLFNDTIEFNIKYGCPSATDEEMRAAAKQAEIDDVIMRMPQGYSTVVGERGLKLSGGERQRIGIARCLLRNPAIAVFDEATSALDSHTEQKILKAFRAMARGRTTLVIAHRLSTISDADKIIYLKEGKIAEMGTHAELLEKERGLYRALWESQQHQEQEEAVSTPDLTLS

[Multiple Choices]
A. chloroplast
B. endoplasmic reticulum
C. host cell
D. mitochondrial inner membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched record assigns the protein to the mitochondrial membrane, with experimental evidence cited, and specifically annotates the mitochondrial inner membrane by computational inference (TreeGrafter). The exact inner-membrane placement is therefore supported, though the GO annotation is not itself direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic transmembrane segments and a recognizable ABC-transporter nucleotide-binding domain, including a Walker A-like motif. Transferable knowledge of ATM1/ABCB7-like transporter architecture associates this family with mitochondrial membranes, making D a meaningful choice over ER, chloroplast, or host cell.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level and sequence-based clues provide a credible distinction among the offered compartments without requiring the exact protein's database annotation. The precise inner-membrane assignment is less certain from sequence alone than the broader mitochondrial localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family and membrane-protein features favor the mitochondrial inner membrane among the offered alternatives; no other option is comparably supported.


### Important caveats

- The supplied sequence does not by itself establish mitochondrial inner-membrane localization with certainty.
- The specific GO inner-membrane annotation is computational; the cited experimental evidence supports mitochondrial membrane localization more broadly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic transmembrane segments and a recognizable ABC-transporter nucleotide-binding domain, including a Walker A-like motif. Transferable knowledge of ATM1/ABCB7-like transporter architecture associates this family with mitochondrial membranes, making D a meaningful choice over ER, chloroplast, or host cell.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-based clues provide a credible distinction among the offered compartments without requiring the exact protein's database annotation. The precise inner-membrane assignment is less certain from sequence alone than the broader mitochondrial localization."
  },
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record assigns the protein to the mitochondrial membrane, with experimental evidence cited, and specifically annotates the mitochondrial inner membrane by computational inference (TreeGrafter). The exact inner-membrane placement is therefore supported, though the GO annotation is not itself direct experimental evidence."
  },
  "important_caveats": [
    "The supplied sequence does not by itself establish mitochondrial inner-membrane localization with certainty.",
    "The specific GO inner-membrane annotation is computational; the cited experimental evidence supports mitochondrial membrane localization more broadly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family and membrane-protein features favor the mitochondrial inner membrane among the offered alternatives; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record assigns the protein to the mitochondrial membrane, with experimental evidence cited, and specifically annotates the mitochondrial inner membrane by computational inference (TreeGrafter). The exact inner-membrane placement is therefore supported, though the GO annotation is not itself direct experimental evidence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic transmembrane segments and a recognizable ABC-transporter nucleotide-binding domain, including a Walker A-like motif. Transferable knowledge of ATM1/ABCB7-like transporter architecture associates this family with mitochondrial membranes, making D a meaningful choice over ER, chloroplast, or host cell.",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-based clues provide a credible distinction among the offered compartments without requiring the exact protein's database annotation. The precise inner-membrane assignment is less certain from sequence alone than the broader mitochondrial localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family and membrane-protein features favor the mitochondrial inner membrane among the offered alternatives; no other option is comparably supported."
  },
  "important_caveats": [
    "The supplied sequence does not by itself establish mitochondrial inner-membrane localization with certainty.",
    "The specific GO inner-membrane annotation is computational; the cited experimental evidence supports mitochondrial membrane localization more broadly."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (S8EXU2) annotates this protein as 'Mitochondrion membrane, Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:39207139), and GO:0005743 'mitochondrial inner membrane' is listed (IEA:TreeGrafter). The protein is identified as ABC transporter ATM1 / ABCB7-like. While the direct experimental evidence for this specific protein states 'mitochondrion membrane' without specifying inner vs. outer, the GO annotation specifies inner membrane, and the ATM1/ABCB7 family is well-characterized as an inner membrane transporter in yeast and human. The answer D is consistent with both the annotation and family-level knowledge.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains unmistakable ABC transporter NBD motifs: Walker A 'GPSGVGKSTLIK' (GxxGxGKST) and ABC signature 'FDEATSALDSHTEQ'. The overall architecture is a half-transporter (one multi-pass TMD + one NBD), which is the defining structural feature of the ABCB7/ATM1 subfamily. From well-established family knowledge across yeast, human, and other eukaryotes, ABCB7/ATM1 half-transporters localize to the mitochondrial inner membrane and function in Fe-S cluster export. The other options are distinguishable: chloroplast (A) would require a plastid transit peptide and different transporter architecture; ER (B) ABC transporters (TAP, MRP) are full transporters with two NBDs and different TMD topology; host cell (C) would require secretion/host-targeting signals absent here. The half-transporter architecture combined with ABCB7-family sequence motifs provides a credible, transferable inference chain to mitochondrial inner membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the ABC transporter motifs directly from the sequence, recognize the half-transporter architecture (single TMD + single NBD), and apply well-established family-level knowledge that ABCB7/ATM1-type half-transporters reside in the mitochondrial inner membrane. The other three options are excluded by architectural and targeting-sequence considerations. This constitutes legitimate transfer from other proteins (yeast ATM1, human ABCB7) rather than memorization of this exact Toxoplasma entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The half-transporter architecture with ABCB7/ATM1-family motifs strongly points to mitochondrial inner membrane. Chloroplast, ER, and host cell are not supported by the sequence features. While the UniProt experimental annotation says 'mitochondrion membrane' without specifying 'inner,' the GO annotation and family knowledge resolve this to inner membrane, and no other option is defensible.


### Important caveats

- The direct experimental evidence (ECO:0000269) for this specific protein states 'Mitochondrion membrane' without specifying inner vs. outer; the 'inner' specification comes from IEA:TreeGrafter GO annotation and family-level inference.
- The organism (Toxoplasma gondii) is not stated in the original input; the model must rely on sequence features and family knowledge rather than organism-specific targeting conventions.
- The N-terminal ~280-residue region is heavily phosphorylated (many Ser/Thr) and lacks a classic amphipathic mitochondrial targeting sequence, which might initially confuse a model; however, the ABCB7/ATM1 family architecture and motifs are the decisive features.
- The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning must proceed from sequence features and general family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains unmistakable ABC transporter NBD motifs: Walker A 'GPSGVGKSTLIK' (GxxGxGKST) and ABC signature 'FDEATSALDSHTEQ'. The overall architecture is a half-transporter (one multi-pass TMD + one NBD), which is the defining structural feature of the ABCB7/ATM1 subfamily. From well-established family knowledge across yeast, human, and other eukaryotes, ABCB7/ATM1 half-transporters localize to the mitochondrial inner membrane and function in Fe-S cluster export. The other options are distinguishable: chloroplast (A) would require a plastid transit peptide and different transporter architecture; ER (B) ABC transporters (TAP, MRP) are full transporters with two NBDs and different TMD topology; host cell (C) would require secretion/host-targeting signals absent here. The half-transporter architecture combined with ABCB7-family sequence motifs provides a credible, transferable inference chain to mitochondrial inner membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the ABC transporter motifs directly from the sequence, recognize the half-transporter architecture (single TMD + single NBD), and apply well-established family-level knowledge that ABCB7/ATM1-type half-transporters reside in the mitochondrial inner membrane. The other three options are excluded by architectural and targeting-sequence considerations. This constitutes legitimate transfer from other proteins (yeast ATM1, human ABCB7) rather than memorization of this exact Toxoplasma entry."
  },
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (S8EXU2) annotates this protein as 'Mitochondrion membrane, Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:39207139), and GO:0005743 'mitochondrial inner membrane' is listed (IEA:TreeGrafter). The protein is identified as ABC transporter ATM1 / ABCB7-like. While the direct experimental evidence for this specific protein states 'mitochondrion membrane' without specifying inner vs. outer, the GO annotation specifies inner membrane, and the ATM1/ABCB7 family is well-characterized as an inner membrane transporter in yeast and human. The answer D is consistent with both the annotation and family-level knowledge."
  },
  "important_caveats": [
    "The direct experimental evidence (ECO:0000269) for this specific protein states 'Mitochondrion membrane' without specifying inner vs. outer; the 'inner' specification comes from IEA:TreeGrafter GO annotation and family-level inference.",
    "The organism (Toxoplasma gondii) is not stated in the original input; the model must rely on sequence features and family knowledge rather than organism-specific targeting conventions.",
    "The N-terminal ~280-residue region is heavily phosphorylated (many Ser/Thr) and lacks a classic amphipathic mitochondrial targeting sequence, which might initially confuse a model; however, the ABCB7/ATM1 family architecture and motifs are the decisive features.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning must proceed from sequence features and general family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The half-transporter architecture with ABCB7/ATM1-family motifs strongly points to mitochondrial inner membrane. Chloroplast, ER, and host cell are not supported by the sequence features. While the UniProt experimental annotation says 'mitochondrion membrane' without specifying 'inner,' the GO annotation and family knowledge resolve this to inner membrane, and no other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (S8EXU2) annotates this protein as 'Mitochondrion membrane, Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:39207139), and GO:0005743 'mitochondrial inner membrane' is listed (IEA:TreeGrafter). The protein is identified as ABC transporter ATM1 / ABCB7-like. While the direct experimental evidence for this specific protein states 'mitochondrion membrane' without specifying inner vs. outer, the GO annotation specifies inner membrane, and the ATM1/ABCB7 family is well-characterized as an inner membrane transporter in yeast and human. The answer D is consistent with both the annotation and family-level knowledge.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains unmistakable ABC transporter NBD motifs: Walker A 'GPSGVGKSTLIK' (GxxGxGKST) and ABC signature 'FDEATSALDSHTEQ'. The overall architecture is a half-transporter (one multi-pass TMD + one NBD), which is the defining structural feature of the ABCB7/ATM1 subfamily. From well-established family knowledge across yeast, human, and other eukaryotes, ABCB7/ATM1 half-transporters localize to the mitochondrial inner membrane and function in Fe-S cluster export. The other options are distinguishable: chloroplast (A) would require a plastid transit peptide and different transporter architecture; ER (B) ABC transporters (TAP, MRP) are full transporters with two NBDs and different TMD topology; host cell (C) would require secretion/host-targeting signals absent here. The half-transporter architecture combined with ABCB7-family sequence motifs provides a credible, transferable inference chain to mitochondrial inner membrane.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the ABC transporter motifs directly from the sequence, recognize the half-transporter architecture (single TMD + single NBD), and apply well-established family-level knowledge that ABCB7/ATM1-type half-transporters reside in the mitochondrial inner membrane. The other three options are excluded by architectural and targeting-sequence considerations. This constitutes legitimate transfer from other proteins (yeast ATM1, human ABCB7) rather than memorization of this exact Toxoplasma entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The half-transporter architecture with ABCB7/ATM1-family motifs strongly points to mitochondrial inner membrane. Chloroplast, ER, and host cell are not supported by the sequence features. While the UniProt experimental annotation says 'mitochondrion membrane' without specifying 'inner,' the GO annotation and family knowledge resolve this to inner membrane, and no other option is defensible."
  },
  "important_caveats": [
    "The direct experimental evidence (ECO:0000269) for this specific protein states 'Mitochondrion membrane' without specifying inner vs. outer; the 'inner' specification comes from IEA:TreeGrafter GO annotation and family-level inference.",
    "The organism (Toxoplasma gondii) is not stated in the original input; the model must rely on sequence features and family knowledge rather than organism-specific targeting conventions.",
    "The N-terminal ~280-residue region is heavily phosphorylated (many Ser/Thr) and lacks a classic amphipathic mitochondrial targeting sequence, which might initially confuse a model; however, the ABCB7/ATM1 family architecture and motifs are the decisive features.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning must proceed from sequence features and general family knowledge."
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
  "benchmark_sequence_length": 1130,
  "benchmark_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "current_entry_audit": {
    "entryVersion": 60,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1130,
  "current_source_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "S8EXU2",
  "selected_historical_entry_version": 59,
  "selected_historical_record_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "selected_historical_source_sequence_length": 1130,
  "selected_historical_source_sequence_sha256": "daba902a243edc1bc02b2eb767e57c10754863d7c3580600dfa56175853247ac",
  "selected_historical_version": {
    "accession": "S8EXU2",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ATM1_TOXGM",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"S8EXU2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":60,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"ABCB7-like\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"ABCB7L\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39207139\",\"source\":\"PubMed\"}],\"value\":\"TgABCB7L\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IDH9\",\"source\":\"UniProtKB\"}],\"value\":\"7.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ABC transporter ATM1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"TgATM1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39207139\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"id\":\"SL-0171\",\"value\":\"Mitochondrion membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005743\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial inner membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Maclean A.E.\",\"Sloan M.A.\",\"Renaud E.A.\",\"Argyle B.E.\",\"Lewis W.H.\",\"Ovciarikova J.\",\"Demolombe V.\",\"Waller R.F.\",\"Besteiro S.\",\"Sheiner L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39207139\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00872-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0087224\",\"id\":\"39207139\",\"journal\":\"MBio\",\"lastPage\":\"e0087224\",\"publicationDate\":\"2024\",\"title\":\"The Toxoplasma gondii mitochondrial transporter ABCB7L is essential for the biogenesis of cytosolic and nuclear iron-sulfur cluster proteins and cytosolic translation.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Shrivastava D.\",\"Abboud E.\",\"Ramchandra J.P.\",\"Jha A.\",\"Marq J.B.\",\"Chaurasia A.\",\"Mitra K.\",\"Sadik M.\",\"Siddiqi M.I.\",\"Soldati-Favre D.\",\"Kloehn J.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39348385\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012593\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012593\",\"id\":\"39348385\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012593\",\"publicationDate\":\"2024\",\"title\":\"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.\",\"volume\":\"20\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:58.976860+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9",
  "url": "https://rest.uniprot.org/uniprotkb/S8EXU2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H1",
  "excerpt": "ID   ATM1_TOXGM              Reviewed;        1130 AA.\nAC   S8EXU2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2013, sequence version 1.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=ABC transporter ATM1 {ECO:0000305};\nDE            Short=TgATM1 {ECO:0000303|PubMed:39348385};\nDE            EC=7.-.-.- {ECO:0000250|UniProtKB:Q8IDH9};\nDE   AltName: Full=ABCB7-like {ECO:0000303|PubMed:39207139};\nDE            Short=ABCB7L {ECO:0000303|PubMed:39207139};\nDE            Short=TgABCB7L {ECO:0000303|PubMed:39207139};\nDE   Flags: Precursor;\nGN   ORFNames=TGME49_269000 {ECO:0000312|EMBL:EPT28291.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39207139; DOI=10.1128/mbio.00872-24;\nRA   Maclean A.E., Sloan M.A., Renaud E.A., Argyle B.E., Lewis W.H.,\nRA   Ovciarikova J., Demolombe V., Waller R.F., Besteiro S., Sheiner L.;\nRT   \"The Toxoplasma gondii mitochondrial transporter ABCB7L is essential for\nRT   the biogenesis of cytosolic and nuclear iron-sulfur cluster proteins and\nRT   cytosolic translation.\";\nRL   MBio 15:e0087224-e0087224(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39348385; DOI=10.1371/journal.ppat.1012593;\nRA   Shrivastava D., Abboud E., Ramchandra J.P., Jha A., Marq J.B.,\nRA   Chaurasia A., Mitra K., Sadik M., Siddiqi M.I., Soldati-Favre D.,\nRA   Kloehn J., Habib S.;\nRT   \"ATM1, an essential conserved transporter in Apicomplexa, bridges\nRT   mitochondrial and cytosolic [Fe-S] biogenesis.\";\nRL   PLoS Pathog. 20:e1012593-e1012593(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane\nCC       {ECO:0000269|PubMed:39207139, ECO:0000305|PubMed:39348385}; Multi-pass\nCC       membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)

```json
{
  "entry_version": 59,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005743; C:mitochondrial inner membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.453043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933",
  "url": "https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005743\nname: mitochondrial inner membrane\nnamespace: cellular_component\ndef: \"The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae.\" [GOC:ai]\nsynonym: \"inner mitochondrial membrane\" EXACT []\nsynonym: \"inner mitochondrion membrane\" EXACT []\nsynonym: \"mitochondrion inner membrane\" EXACT []\nxref: NIF_Subcellular:sao1371347282\nxref: Wikipedia:Inner_mitochondrial_membrane\nis_a: GO:0019866 ! organelle inner membrane\nis_a: GO:0031966 ! mitochondrial membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005743",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59031-59043",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59450-59472",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0009507\nname: chloroplast\nnamespace: cellular_component\ndef: \"A chlorophyll-containing plastid with thylakoids organized into grana and frets, or stroma thylakoids, and embedded in a stroma.\" [ISBN:0471245208]\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nxref: Wikipedia:Chloroplast\nis_a: GO:0009536 ! plastid\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009507",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 97029-97038",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0043657\nname: host cell\nnamespace: cellular_component\ndef: \"A cell within a host organism. Includes the host plasma membrane and any external encapsulating structures such as the host cell wall and cell envelope.\" [GOC:jl]\nis_a: GO:0018995 ! host cellular component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043657",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 249498-249504",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
