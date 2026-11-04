# GO_biological_process_0005

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0005.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — NAD biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHYLDNLLLNTDSYKASHWLQYPPGTDASFFYVESRGGVYDQTAFFGLQSILKEAINRPVTHADIDDAKALLAAHGEPFNEAGWRDIVDRLGGQLPIRIRAVPEGCVVPTHNVLMTIESTDAKAFWVPSYLETLLLRVWYPVTVATVSWQVKQIVRDFLQRTSDDPEGQLPFKLHDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHTPVAGYSIPAAEHSTITSWGREREVDAYRNMLTQFARPGAIVAVVSDSYDIYRAIREHWGTTLREEIIASGATVVIRPDSGDPVDVVEQCLLLLDEAFGHQVNGKGYKVLNHVRVIQGDGINPQSLRAILERITAAGYAADNVAFGMGGALLQKVDRDTQKFALKCSAVRVDGAWIDVYKDPITDQGKQSKRGRLTLLRDRATGQYRSALLDEVATHAGDSDDALVTVWENGQMLREWTLEQVRAHADAARL

[Multiple Choices]
A. regulation of fat cell differentiation
B. NAD biosynthetic process
C. heme biosynthetic process
D. fatty acid biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record identifies the protein as nicotinamide phosphoribosyltransferase and reports, with ECO:0000269 evidence, that it produces nicotinamide mononucleotide, an intermediate in NAD biosynthesis. The pathway annotation also assigns NAD+ biosynthesis. This supports choice B; the GO annotation itself is computational, while the cited functional annotation is marked as experimentally evidenced.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 468-aa sequence is consistent with the bacterial NAMPT/PncB nicotinamide phosphoribosyltransferase family. Transferable knowledge of that enzyme family connects its reaction—using nicotinamide and PRPP to form NMN—to NAD biosynthesis, distinguishing B from heme or fatty-acid biosynthesis; regulation of fat-cell differentiation is also a poor fit for a bacterial enzyme sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and knowledge of the conserved reaction provide a meaningful basis for choosing NAD biosynthesis without needing the exact protein's database annotation. This is a probabilistic sequence-based inference, not a guarantee from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct processes, and the NAMPT-family reaction points specifically to NAD biosynthesis.


### Important caveats

- The family identification from sequence is an inference; the supplied reviewer-only source evidence is not part of the original input.
- The source record's functional annotation cites experimental evidence, whereas its GO annotation is marked IEA.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 468-aa sequence is consistent with the bacterial NAMPT/PncB nicotinamide phosphoribosyltransferase family. Transferable knowledge of that enzyme family connects its reaction—using nicotinamide and PRPP to form NMN—to NAD biosynthesis, distinguishing B from heme or fatty-acid biosynthesis; regulation of fat-cell differentiation is also a poor fit for a bacterial enzyme sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of the conserved reaction provide a meaningful basis for choosing NAD biosynthesis without needing the exact protein's database annotation. This is a probabilistic sequence-based inference, not a guarantee from the sequence alone."
  },
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as nicotinamide phosphoribosyltransferase and reports, with ECO:0000269 evidence, that it produces nicotinamide mononucleotide, an intermediate in NAD biosynthesis. The pathway annotation also assigns NAD+ biosynthesis. This supports choice B; the GO annotation itself is computational, while the cited functional annotation is marked as experimentally evidenced."
  },
  "important_caveats": [
    "The family identification from sequence is an inference; the supplied reviewer-only source evidence is not part of the original input.",
    "The source record's functional annotation cites experimental evidence, whereas its GO annotation is marked IEA."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct processes, and the NAMPT-family reaction points specifically to NAD biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as nicotinamide phosphoribosyltransferase and reports, with ECO:0000269 evidence, that it produces nicotinamide mononucleotide, an intermediate in NAD biosynthesis. The pathway annotation also assigns NAD+ biosynthesis. This supports choice B; the GO annotation itself is computational, while the cited functional annotation is marked as experimentally evidenced.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 468-aa sequence is consistent with the bacterial NAMPT/PncB nicotinamide phosphoribosyltransferase family. Transferable knowledge of that enzyme family connects its reaction—using nicotinamide and PRPP to form NMN—to NAD biosynthesis, distinguishing B from heme or fatty-acid biosynthesis; regulation of fat-cell differentiation is also a poor fit for a bacterial enzyme sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of the conserved reaction provide a meaningful basis for choosing NAD biosynthesis without needing the exact protein's database annotation. This is a probabilistic sequence-based inference, not a guarantee from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct processes, and the NAMPT-family reaction points specifically to NAD biosynthesis."
  },
  "important_caveats": [
    "The family identification from sequence is an inference; the supplied reviewer-only source evidence is not part of the original input.",
    "The source record's functional annotation cites experimental evidence, whereas its GO annotation is marked IEA."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this exact sequence (A0A0H2X5R2, 468 aa, sequence matched) identifies the protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12). The function comment states it 'Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD' via the NAM salvage pathway. The pathway comment places it in 'NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1.' The GO annotation GO:0009435 (NAD+ biosynthetic process) is present. These annotations are backed by experimental evidence (PubMed:38429435, multiple PDB structures). Option B text 'NAD biosynthetic process' matches the GO term synonyms exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can build a multi-step elimination argument. (1) Option A (regulation of fat cell differentiation) is a eukaryotic-specific process involving adipocyte biology; the sequence shows no eukaryotic hallmarks (no signal peptide, no transmembrane segments, no eukaryotic-specific motifs) and its composition is consistent with a bacterial enzyme, making A implausible. (2) Options C (heme biosynthetic process) and D (fatty acid biosynthetic process) require enzymes with entirely different structural classes: heme biosynthesis uses porphyrin-pathway enzymes (glutamyl-tRNA reductase, porphobilinogen synthase, ferrochelatase, etc.) and fatty acid biosynthesis uses thiolase-fold synthases, reductases, and ACP-related enzymes. None of these enzyme families share the phosphoribosyltransferase (PRTase) architecture visible in this sequence. (3) The sequence contains features consistent with the PRTase superfamily: a ~468-aa length typical of NAMPT-class PRTases, conserved 'GG' motifs, a catalytic 'SDSYDIY'-type motif in the active-site loop region, and a domain architecture (N-terminal helical region followed by a PRTase core) that matches the PRTase fold seen in well-studied members like HGPRT and QPRT. PRTases transfer phosphoribosyl groups to nitrogenous bases and are found exclusively in nucleotide/cofactor salvage and biosynthesis pathways. Among the four options, only B (NAD biosynthetic process) corresponds to a PRTase-catalyzed reaction (NAM + PRPP → NMN, the first committed step of the NAM salvage pathway to NAD+). Thus, recognizing the PRTase family architecture and knowing that PRTases participate in nucleotide/cofactor biosynthesis (not heme or fatty acid pathways) meaningfully distinguishes B from C and D, while the bacterial character eliminates A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A is straightforward from general biology (eukaryotic-specific process vs. bacterial enzyme). The elimination of C and D relies on knowing that heme and fatty acid biosynthetic enzymes belong to entirely different structural/functional classes (porphyrin-pathway enzymes, thiolase-fold synthases) with no resemblance to PRTase architecture. The positive identification of B rests on recognizing PRTase-family features in the sequence and knowing that PRTases catalyze phosphoribosyl transfer reactions in nucleotide/cofactor biosynthesis. This is a transferable family-level inference from the PRTase superfamily (learned from HGPRT, APRT, QPRT, UPP, etc.), not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span biologically distinct processes: a eukaryotic developmental process (A), a PRTase-catalyzed cofactor pathway (B), a porphyrin/iron pathway (C), and a fatty acid synthase pathway (D). The PRTase architecture and bacterial origin of the sequence cleanly separate B from the other three. No option is defensible alongside B given the sequence features and general biology.


### Important caveats

- The GO annotation in UniProt carries evidence code IEA (inferred from electronic annotation via UniPathway/InterPro) for GO:0009435, but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:38429435) and PDB structures.
- Recognizing the PRTase fold from sequence alone requires moderate expertise in protein family architecture; the sequence conservation within the PRTase superfamily is moderate rather than high, so a model without strong exposure to PRTase family sequences might find the positive identification of B less certain, though the elimination of A, C, and D remains robust.
- The protein is from Xanthomonas campestris, a bacterium; the organism identity is not provided in the original input but can be inferred from sequence composition and absence of eukaryotic features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can build a multi-step elimination argument. (1) Option A (regulation of fat cell differentiation) is a eukaryotic-specific process involving adipocyte biology; the sequence shows no eukaryotic hallmarks (no signal peptide, no transmembrane segments, no eukaryotic-specific motifs) and its composition is consistent with a bacterial enzyme, making A implausible. (2) Options C (heme biosynthetic process) and D (fatty acid biosynthetic process) require enzymes with entirely different structural classes: heme biosynthesis uses porphyrin-pathway enzymes (glutamyl-tRNA reductase, porphobilinogen synthase, ferrochelatase, etc.) and fatty acid biosynthesis uses thiolase-fold synthases, reductases, and ACP-related enzymes. None of these enzyme families share the phosphoribosyltransferase (PRTase) architecture visible in this sequence. (3) The sequence contains features consistent with the PRTase superfamily: a ~468-aa length typical of NAMPT-class PRTases, conserved 'GG' motifs, a catalytic 'SDSYDIY'-type motif in the active-site loop region, and a domain architecture (N-terminal helical region followed by a PRTase core) that matches the PRTase fold seen in well-studied members like HGPRT and QPRT. PRTases transfer phosphoribosyl groups to nitrogenous bases and are found exclusively in nucleotide/cofactor salvage and biosynthesis pathways. Among the four options, only B (NAD biosynthetic process) corresponds to a PRTase-catalyzed reaction (NAM + PRPP → NMN, the first committed step of the NAM salvage pathway to NAD+). Thus, recognizing the PRTase family architecture and knowing that PRTases participate in nucleotide/cofactor biosynthesis (not heme or fatty acid pathways) meaningfully distinguishes B from C and D, while the bacterial character eliminates A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A is straightforward from general biology (eukaryotic-specific process vs. bacterial enzyme). The elimination of C and D relies on knowing that heme and fatty acid biosynthetic enzymes belong to entirely different structural/functional classes (porphyrin-pathway enzymes, thiolase-fold synthases) with no resemblance to PRTase architecture. The positive identification of B rests on recognizing PRTase-family features in the sequence and knowing that PRTases catalyze phosphoribosyl transfer reactions in nucleotide/cofactor biosynthesis. This is a transferable family-level inference from the PRTase superfamily (learned from HGPRT, APRT, QPRT, UPP, etc.), not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A0H2X5R2, 468 aa, sequence matched) identifies the protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12). The function comment states it 'Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD' via the NAM salvage pathway. The pathway comment places it in 'NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1.' The GO annotation GO:0009435 (NAD+ biosynthetic process) is present. These annotations are backed by experimental evidence (PubMed:38429435, multiple PDB structures). Option B text 'NAD biosynthetic process' matches the GO term synonyms exactly."
  },
  "important_caveats": [
    "The GO annotation in UniProt carries evidence code IEA (inferred from electronic annotation via UniPathway/InterPro) for GO:0009435, but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:38429435) and PDB structures.",
    "Recognizing the PRTase fold from sequence alone requires moderate expertise in protein family architecture; the sequence conservation within the PRTase superfamily is moderate rather than high, so a model without strong exposure to PRTase family sequences might find the positive identification of B less certain, though the elimination of A, C, and D remains robust.",
    "The protein is from Xanthomonas campestris, a bacterium; the organism identity is not provided in the original input but can be inferred from sequence composition and absence of eukaryotic features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span biologically distinct processes: a eukaryotic developmental process (A), a PRTase-catalyzed cofactor pathway (B), a porphyrin/iron pathway (C), and a fatty acid synthase pathway (D). The PRTase architecture and bacterial origin of the sequence cleanly separate B from the other three. No option is defensible alongside B given the sequence features and general biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A0H2X5R2, 468 aa, sequence matched) identifies the protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12). The function comment states it 'Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD' via the NAM salvage pathway. The pathway comment places it in 'NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1.' The GO annotation GO:0009435 (NAD+ biosynthetic process) is present. These annotations are backed by experimental evidence (PubMed:38429435, multiple PDB structures). Option B text 'NAD biosynthetic process' matches the GO term synonyms exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can build a multi-step elimination argument. (1) Option A (regulation of fat cell differentiation) is a eukaryotic-specific process involving adipocyte biology; the sequence shows no eukaryotic hallmarks (no signal peptide, no transmembrane segments, no eukaryotic-specific motifs) and its composition is consistent with a bacterial enzyme, making A implausible. (2) Options C (heme biosynthetic process) and D (fatty acid biosynthetic process) require enzymes with entirely different structural classes: heme biosynthesis uses porphyrin-pathway enzymes (glutamyl-tRNA reductase, porphobilinogen synthase, ferrochelatase, etc.) and fatty acid biosynthesis uses thiolase-fold synthases, reductases, and ACP-related enzymes. None of these enzyme families share the phosphoribosyltransferase (PRTase) architecture visible in this sequence. (3) The sequence contains features consistent with the PRTase superfamily: a ~468-aa length typical of NAMPT-class PRTases, conserved 'GG' motifs, a catalytic 'SDSYDIY'-type motif in the active-site loop region, and a domain architecture (N-terminal helical region followed by a PRTase core) that matches the PRTase fold seen in well-studied members like HGPRT and QPRT. PRTases transfer phosphoribosyl groups to nitrogenous bases and are found exclusively in nucleotide/cofactor salvage and biosynthesis pathways. Among the four options, only B (NAD biosynthetic process) corresponds to a PRTase-catalyzed reaction (NAM + PRPP → NMN, the first committed step of the NAM salvage pathway to NAD+). Thus, recognizing the PRTase family architecture and knowing that PRTases participate in nucleotide/cofactor biosynthesis (not heme or fatty acid pathways) meaningfully distinguishes B from C and D, while the bacterial character eliminates A.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A is straightforward from general biology (eukaryotic-specific process vs. bacterial enzyme). The elimination of C and D relies on knowing that heme and fatty acid biosynthetic enzymes belong to entirely different structural/functional classes (porphyrin-pathway enzymes, thiolase-fold synthases) with no resemblance to PRTase architecture. The positive identification of B rests on recognizing PRTase-family features in the sequence and knowing that PRTases catalyze phosphoribosyl transfer reactions in nucleotide/cofactor biosynthesis. This is a transferable family-level inference from the PRTase superfamily (learned from HGPRT, APRT, QPRT, UPP, etc.), not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span biologically distinct processes: a eukaryotic developmental process (A), a PRTase-catalyzed cofactor pathway (B), a porphyrin/iron pathway (C), and a fatty acid synthase pathway (D). The PRTase architecture and bacterial origin of the sequence cleanly separate B from the other three. No option is defensible alongside B given the sequence features and general biology."
  },
  "important_caveats": [
    "The GO annotation in UniProt carries evidence code IEA (inferred from electronic annotation via UniPathway/InterPro) for GO:0009435, but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:38429435) and PDB structures.",
    "Recognizing the PRTase fold from sequence alone requires moderate expertise in protein family architecture; the sequence conservation within the PRTase superfamily is moderate rather than high, so a model without strong exposure to PRTase family sequences might find the positive identification of B less certain, though the elimination of A, C, and D remains robust.",
    "The protein is from Xanthomonas campestris, a bacterium; the organism identity is not provided in the original input but can be inferred from sequence composition and absence of eukaryotic features."
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
  "benchmark_sequence_length": 468,
  "benchmark_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 468,
  "current_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0H2X5R2",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "selected_historical_source_sequence_length": 468,
  "selected_historical_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "selected_historical_version": {
    "accession": "A0A0H2X5R2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NAMPT_XANC8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0H2X5R2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Nicotinamide phosphoribosyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAM phosphoribosyltransferase\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAMPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD (PubMed:38429435). Plays an important role in the biosynthesis of NAD via the nicotinamide (NAM) salvage pathway (PubMed:38429435). Is also capable of hydrolyzing ATP and shows ATP-dependent autophosphorylation activity (PubMed:38429435)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009435\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:NAD+ biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQO\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQP\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQQ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQR\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8IGZ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE MUTANT PHE-175/PHE-224/PHE-291/PHE-332\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\",\"DOMAIN\",\"PHOSPHORYLATION AT HIS-229\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332; ASP-335 AND ARG-373\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   NAMPT_XANC8             Reviewed;         468 AA.\nAC   A0A0H2X5R2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Nicotinamide phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAM phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAMPT {ECO:0000303|PubMed:38429435};\nDE            EC=2.4.2.12 {ECO:0000269|PubMed:38429435};\nGN   OrderedLocusNames=XC_0719 {ECO:0000312|EMBL:AAY47797.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7YQO, ECO:0007744|PDB:7YQP, ECO:0007744|PDB:7YQQ, ECO:0007744|PDB:7YQR, ECO:0007744|PDB:8IGZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES\nRP   WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE\nRP   MUTANT PHE-175/PHE-224/PHE-291/PHE-332, FUNCTION, CATALYTIC ACTIVITY,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT,\nRP   DOMAIN, PHOSPHORYLATION AT HIS-229, DISRUPTION PHENOTYPE, AND MUTAGENESIS\nRP   OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332;\nRP   ASP-335 AND ARG-373.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the condensation of nicotinamide with 5-\nCC       phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an\nCC       intermediate in the biosynthesis of NAD (PubMed:38429435). Plays an\nCC       important role in the biosynthesis of NAD via the nicotinamide (NAM)\nCC       salvage pathway (PubMed:38429435). Is also capable of hydrolyzing ATP\nCC       and shows ATP-dependent autophosphorylation activity (PubMed:38429435).\nCC       {ECO:0000269|PubMed:38429435}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-\nCC       ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and\nCC       nicotinamide: step 1/1. {ECO:0000269|PubMed:38429435}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0009435; P:NAD+ biosynthetic process; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006633\nname: fatty acid biosynthetic process\nnamespace: biological_process\nalt_id: GO:0000037\ndef: \"The chemical reactions and pathways resulting in the formation of a fatty acid, any of the aliphatic monocarboxylic acids that can be liberated by hydrolysis from naturally occurring fats and oils. Fatty acids are predominantly straight-chain acids of 4 to 24 carbon atoms, which may be saturated or unsaturated; branched fatty acids and hydroxy fatty acids also occur, and very long chain acids of over 30 carbons are found in waxes.\" [GOC:mah, ISBN:0198506732]\nsynonym: \"fatty acid anabolism\" EXACT []\nsynonym: \"fatty acid biosynthesis\" EXACT []\nsynonym: \"fatty acid formation\" EXACT []\nsynonym: \"fatty acid synthesis\" EXACT []\nxref: MetaCyc:FASYN-INITIAL-PWY\nxref: MetaCyc:PWY-4381\nxref: MetaCyc:PWY-5156\nxref: Wikipedia:Fatty_acid_synthesis\nis_a: GO:0006631 ! fatty acid metabolic process\nis_a: GO:0008610 ! lipid biosynthetic process\nis_a: GO:0072330 ! monocarboxylic acid biosynthetic process\nproperty_value: skos:narrowMatch MetaCyc:FASYN-INITIAL-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-4381\nproperty_value: skos:narrowMatch MetaCyc:PWY-5156\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006633",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 68539-68559",
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
  "excerpt": "[Term]\nid: GO:0006783\nname: heme biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of heme, any compound of iron complexed in a porphyrin (tetrapyrrole) ring, from less complex precursors.\" [GOC:jl, PMID:11788607]\nsynonym: \"haem biosynthesis\" EXACT []\nsynonym: \"haem biosynthetic process\" EXACT []\nsynonym: \"heme anabolism\" EXACT []\nsynonym: \"heme biosynthesis\" EXACT []\nsynonym: \"heme formation\" EXACT []\nsynonym: \"heme synthesis\" EXACT []\nxref: Reactome:R-HSA-189451 \"Heme biosynthesis\"\nis_a: GO:0006779 ! porphyrin-containing compound biosynthetic process\nis_a: GO:0042168 ! heme metabolic process\nis_a: GO:0046148 ! pigment biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 70266-70281",
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
  "excerpt": "[Term]\nid: GO:0009435\nname: NAD+ biosynthetic process\nnamespace: biological_process\nalt_id: GO:0006736\ndef: \"The chemical reactions and pathways resulting in the formation of nicotinamide adenine dinucleotide (NAD+), a coenzyme that interconverts with its reduced form, NADH, in many redox and catabolic reactions. NAD+ is derived from various sources including vitamin B3.\" [PMID:28648096]\nsynonym: \"NAD (oxidized) biosynthesis\" EXACT []\nsynonym: \"NAD (oxidized) biosynthetic process\" EXACT []\nsynonym: \"NAD (reduced) biosynthesis\" EXACT []\nsynonym: \"NAD (reduced) biosynthetic process\" EXACT []\nsynonym: \"NAD anabolism\" EXACT []\nsynonym: \"NAD biosynthesis\" EXACT []\nsynonym: \"NAD biosynthetic process\" EXACT []\nsynonym: \"NAD formation\" EXACT []\nsynonym: \"NAD synthesis\" EXACT []\nsynonym: \"NADH biosynthesis\" EXACT []\nsynonym: \"NADH biosynthetic process\" EXACT []\nsynonym: \"nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nsynonym: \"oxidized NAD biosynthesis\" EXACT []\nsynonym: \"oxidized NAD biosynthetic process\" EXACT []\nsynonym: \"oxidized nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"oxidized nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nsynonym: \"reduced NAD biosynthesis\" EXACT []\nsynonym: \"reduced NAD biosynthetic process\" EXACT []\nsynonym: \"reduced nicotinamide adenine dinucleotide biosynthesis\" EXACT []\nsynonym: \"reduced nicotinamide adenine dinucleotide biosynthetic process\" EXACT []\nis_a: GO:0006164 ! purine nucleotide biosynthetic process\nis_a: GO:0019359 ! nicotinamide nucleotide biosynthetic process\nis_a: GO:0019674 ! NAD+ metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 96227-96257",
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
  "excerpt": "[Term]\nid: GO:0045598\nname: regulation of fat cell differentiation\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of adipocyte differentiation.\" [GOC:curators]\nsynonym: \"regulation of adipocyte cell differentiation\" EXACT []\nsynonym: \"regulation of adipocyte differentiation\" EXACT []\nis_a: GO:0045595 ! regulation of cell differentiation\nrelationship: regulates GO:0045444 ! fat cell differentiation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045598",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 266208-266217",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
