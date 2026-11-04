# GO_molecular_function_0134

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0134.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNQFNKVCVIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVVNDGYLKATTLPEEADAFIIAVPTPFKGDNHEPNLDYIEMASKAIAKVLKKGNLVILESTSPVGTTEQMAKWLAEERSDLSFPHQCGEVSDIKIAHCPERVLPGQVIRELVENDRIIGGMTQKCAEYAIRLYKIFVQGECIMTNARTAEMTKLTENSFRDLNIAFANELSILCDKLDINVWELIKLANRHPRVNILQPGCGVGGHCIAVDPWFIVYQNPNEAKIIKTAREVNDNKPNFVVQKIKKKIKDILGPKIACLGLAFKPDIDDLRESPALDIVIKLASENASQILVVEPNIKQLPLKLQNKRNIKLVCLSQALDEADVVAVLVRHKEFIEVQSDKVVSFC

[Multiple Choices]
A. calcium ion binding
B. oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
C. adenylyltransferase activity
D. double-stranded DNA binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched record reports an experimentally supported NAD(+)-dependent oxidation of UDP-ManNAc to UDP-ManNAcA and assigns EC 1.1.1.336 (C4, C6, C9). That reaction oxidizes an alcohol-bearing carbon, whereas option B specifies oxidation of a CH-CH group; the supplied GO definition associates B with EC 1.3.1.- (GO3). The record does contain an InterPro-inferred annotation for B (C8), but that computational annotation conflicts with the more specific reported reaction and enzyme classification.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich dinucleotide-binding-like motif (around VIGLGYIGL), consistent with an NAD-dependent enzyme. Transferable knowledge of dehydrogenases makes a redox activity much more plausible than calcium binding, adenylyl transfer, or double-stranded DNA binding, so B is the identifiable closest choice among those offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Sequence-based recognition of a likely dinucleotide-dependent dehydrogenase provides a meaningful basis to select the only redox option over the other alternatives. This supports B only as the closest offered choice; the sequence argument does not establish B's specific CH-CH donor-group claim, which is inconsistent with the reported reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A, C, and D are not comparably supported by the sequence-based dehydrogenase inference. The issue is that the closest option, B, specifies the wrong donor-group class, not that another listed choice is equally defensible.


### Important caveats

- The reviewer evidence includes an InterPro-based annotation matching B, but its computational evidence type should be distinguished from the experimental reaction and EC classification.
- The source evidence is sequence-matched; the actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding-like motif (around VIGLGYIGL), consistent with an NAD-dependent enzyme. Transferable knowledge of dehydrogenases makes a redox activity much more plausible than calcium binding, adenylyl transfer, or double-stranded DNA binding, so B is the identifiable closest choice among those offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Sequence-based recognition of a likely dinucleotide-dependent dehydrogenase provides a meaningful basis to select the only redox option over the other alternatives. This supports B only as the closest offered choice; the sequence argument does not establish B's specific CH-CH donor-group claim, which is inconsistent with the reported reaction."
  },
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C8",
      "C9",
      "GO3"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports an experimentally supported NAD(+)-dependent oxidation of UDP-ManNAc to UDP-ManNAcA and assigns EC 1.1.1.336 (C4, C6, C9). That reaction oxidizes an alcohol-bearing carbon, whereas option B specifies oxidation of a CH-CH group; the supplied GO definition associates B with EC 1.3.1.- (GO3). The record does contain an InterPro-inferred annotation for B (C8), but that computational annotation conflicts with the more specific reported reaction and enzyme classification."
  },
  "important_caveats": [
    "The reviewer evidence includes an InterPro-based annotation matching B, but its computational evidence type should be distinguished from the experimental reaction and EC classification.",
    "The source evidence is sequence-matched; the actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A, C, and D are not comparably supported by the sequence-based dehydrogenase inference. The issue is that the closest option, B, specifies the wrong donor-group class, not that another listed choice is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports an experimentally supported NAD(+)-dependent oxidation of UDP-ManNAc to UDP-ManNAcA and assigns EC 1.1.1.336 (C4, C6, C9). That reaction oxidizes an alcohol-bearing carbon, whereas option B specifies oxidation of a CH-CH group; the supplied GO definition associates B with EC 1.3.1.- (GO3). The record does contain an InterPro-inferred annotation for B (C8), but that computational annotation conflicts with the more specific reported reaction and enzyme classification.",
    "evidence_ids": ["C4", "C6", "C8", "C9", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich dinucleotide-binding-like motif (around VIGLGYIGL), consistent with an NAD-dependent enzyme. Transferable knowledge of dehydrogenases makes a redox activity much more plausible than calcium binding, adenylyl transfer, or double-stranded DNA binding, so B is the identifiable closest choice among those offered.",
    "missing_item_specific_fact": "",
    "reason": "Sequence-based recognition of a likely dinucleotide-dependent dehydrogenase provides a meaningful basis to select the only redox option over the other alternatives. This supports B only as the closest offered choice; the sequence argument does not establish B's specific CH-CH donor-group claim, which is inconsistent with the reported reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A, C, and D are not comparably supported by the sequence-based dehydrogenase inference. The issue is that the closest option, B, specifies the wrong donor-group class, not that another listed choice is equally defensible."
  },
  "important_caveats": [
    "The reviewer evidence includes an InterPro-based annotation matching B, but its computational evidence type should be distinguished from the experimental reaction and EC classification.",
    "The source evidence is sequence-matched; the actual author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0U3AB61) confirms this protein is UDP-N-acetyl-D-mannosamine dehydrogenase (EC 1.1.1.336), an NAD(+)-dependent oxidoreductase, with experimental evidence (ECO:0000269, PubMed:38382015). GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) is annotated via IEA:InterPro. Technically, EC 1.1.1.336 acts on a CH-OH group (EC 1.1), not a CH-CH group (EC 1.3), so the precise GO sub-classification has a minor mismatch; the more exact term would be GO:0016616 (CH-OH group). Nevertheless, the broad classification as an NAD-dependent oxidoreductase is experimentally confirmed, and GO:0016628 is the term actually carried in the entry. Among the four offered choices, B is unambiguously the best fit.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple Rossmann-fold nucleotide-binding motifs: 'GLGYIGLP' (G-L-G-Y-I-G-L-P, approximating GxGxxG at the N-terminus), 'VIGVDINQ', and 'GCGVGGHC' (GxGxxG-like). The Rossmann fold is the canonical NAD/NADP-binding architecture found in hundreds of characterized dehydrogenases (e.g., lactate dehydrogenase, alcohol dehydrogenase, UDP-glucose 6-dehydrogenase family). Recognizing this motif pattern is standard transferable knowledge from the dehydrogenase superfamily. Additionally, the sequence lacks EF-hand calcium-binding motifs (DxDxDGxD) ruling out A, lacks nucleotidyltransferase fold motifs ruling out C, and lacks DNA-binding domains (helix-turn-helix, zinc fingers, winged-helix) ruling out D. The combination of Rossmann motifs and absence of alternative functional signatures points strongly to NAD-dependent oxidoreductase activity, distinguishing B from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify Rossmann-fold GxGxxG-like motifs in the sequence, recognize them as hallmarks of NAD-binding dehydrogenases (a pattern learned from many other dehydrogenases), and eliminate the other options by absence of their characteristic motifs. This is legitimate family-level and structural-motif transfer, not lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with the sequence features (no EF-hands, no nucleotidyltransferase fold, no DNA-binding domain). Option B is the only plausible choice. The minor technical distinction between CH-CH (GO:0016628) and CH-OH (GO:0016616) sub-classification does not create ambiguity among the four offered choices, since no alternative oxidoreductase term is presented.


### Important caveats

- GO:0016628 is technically for EC 1.3.1.- (CH-CH group), while the protein's EC 1.1.1.336 acts on a CH-OH group. The UniProt IEA:InterPro annotation may reflect a broad InterPro-to-GO mapping rather than a precise EC-to-GO match. The more exact GO term would be GO:0016616.
- The GO:0016628 annotation is IEA (inferred from electronic annotation via InterPro), not directly experimental. The experimental evidence (PubMed:38382015) supports the protein as an NAD-dependent dehydrogenase but maps to GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity) rather than GO:0016628.
- The reviewer-only evidence reveals the protein identity (Campylobacter jejuni, UAMDH_CAMJU), but this identity was not available to the evaluated model. The reasoning argument relies only on sequence motifs and transferable dehydrogenase-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple Rossmann-fold nucleotide-binding motifs: 'GLGYIGLP' (G-L-G-Y-I-G-L-P, approximating GxGxxG at the N-terminus), 'VIGVDINQ', and 'GCGVGGHC' (GxGxxG-like). The Rossmann fold is the canonical NAD/NADP-binding architecture found in hundreds of characterized dehydrogenases (e.g., lactate dehydrogenase, alcohol dehydrogenase, UDP-glucose 6-dehydrogenase family). Recognizing this motif pattern is standard transferable knowledge from the dehydrogenase superfamily. Additionally, the sequence lacks EF-hand calcium-binding motifs (DxDxDGxD) ruling out A, lacks nucleotidyltransferase fold motifs ruling out C, and lacks DNA-binding domains (helix-turn-helix, zinc fingers, winged-helix) ruling out D. The combination of Rossmann motifs and absence of alternative functional signatures points strongly to NAD-dependent oxidoreductase activity, distinguishing B from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify Rossmann-fold GxGxxG-like motifs in the sequence, recognize them as hallmarks of NAD-binding dehydrogenases (a pattern learned from many other dehydrogenases), and eliminate the other options by absence of their characteristic motifs. This is legitimate family-level and structural-motif transfer, not lookup of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0U3AB61) confirms this protein is UDP-N-acetyl-D-mannosamine dehydrogenase (EC 1.1.1.336), an NAD(+)-dependent oxidoreductase, with experimental evidence (ECO:0000269, PubMed:38382015). GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) is annotated via IEA:InterPro. Technically, EC 1.1.1.336 acts on a CH-OH group (EC 1.1), not a CH-CH group (EC 1.3), so the precise GO sub-classification has a minor mismatch; the more exact term would be GO:0016616 (CH-OH group). Nevertheless, the broad classification as an NAD-dependent oxidoreductase is experimentally confirmed, and GO:0016628 is the term actually carried in the entry. Among the four offered choices, B is unambiguously the best fit."
  },
  "important_caveats": [
    "GO:0016628 is technically for EC 1.3.1.- (CH-CH group), while the protein's EC 1.1.1.336 acts on a CH-OH group. The UniProt IEA:InterPro annotation may reflect a broad InterPro-to-GO mapping rather than a precise EC-to-GO match. The more exact GO term would be GO:0016616.",
    "The GO:0016628 annotation is IEA (inferred from electronic annotation via InterPro), not directly experimental. The experimental evidence (PubMed:38382015) supports the protein as an NAD-dependent dehydrogenase but maps to GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity) rather than GO:0016628.",
    "The reviewer-only evidence reveals the protein identity (Campylobacter jejuni, UAMDH_CAMJU), but this identity was not available to the evaluated model. The reasoning argument relies only on sequence motifs and transferable dehydrogenase-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (no EF-hands, no nucleotidyltransferase fold, no DNA-binding domain). Option B is the only plausible choice. The minor technical distinction between CH-CH (GO:0016628) and CH-OH (GO:0016616) sub-classification does not create ambiguity among the four offered choices, since no alternative oxidoreductase term is presented."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0U3AB61) confirms this protein is UDP-N-acetyl-D-mannosamine dehydrogenase (EC 1.1.1.336), an NAD(+)-dependent oxidoreductase, with experimental evidence (ECO:0000269, PubMed:38382015). GO:0016628 (oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor) is annotated via IEA:InterPro. Technically, EC 1.1.1.336 acts on a CH-OH group (EC 1.1), not a CH-CH group (EC 1.3), so the precise GO sub-classification has a minor mismatch; the more exact term would be GO:0016616 (CH-OH group). Nevertheless, the broad classification as an NAD-dependent oxidoreductase is experimentally confirmed, and GO:0016628 is the term actually carried in the entry. Among the four offered choices, B is unambiguously the best fit.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple Rossmann-fold nucleotide-binding motifs: 'GLGYIGLP' (G-L-G-Y-I-G-L-P, approximating GxGxxG at the N-terminus), 'VIGVDINQ', and 'GCGVGGHC' (GxGxxG-like). The Rossmann fold is the canonical NAD/NADP-binding architecture found in hundreds of characterized dehydrogenases (e.g., lactate dehydrogenase, alcohol dehydrogenase, UDP-glucose 6-dehydrogenase family). Recognizing this motif pattern is standard transferable knowledge from the dehydrogenase superfamily. Additionally, the sequence lacks EF-hand calcium-binding motifs (DxDxDGxD) ruling out A, lacks nucleotidyltransferase fold motifs ruling out C, and lacks DNA-binding domains (helix-turn-helix, zinc fingers, winged-helix) ruling out D. The combination of Rossmann motifs and absence of alternative functional signatures points strongly to NAD-dependent oxidoreductase activity, distinguishing B from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify Rossmann-fold GxGxxG-like motifs in the sequence, recognize them as hallmarks of NAD-binding dehydrogenases (a pattern learned from many other dehydrogenases), and eliminate the other options by absence of their characteristic motifs. This is legitimate family-level and structural-motif transfer, not lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with the sequence features (no EF-hands, no nucleotidyltransferase fold, no DNA-binding domain). Option B is the only plausible choice. The minor technical distinction between CH-CH (GO:0016628) and CH-OH (GO:0016616) sub-classification does not create ambiguity among the four offered choices, since no alternative oxidoreductase term is presented."
  },
  "important_caveats": [
    "GO:0016628 is technically for EC 1.3.1.- (CH-CH group), while the protein's EC 1.1.1.336 acts on a CH-OH group. The UniProt IEA:InterPro annotation may reflect a broad InterPro-to-GO mapping rather than a precise EC-to-GO match. The more exact GO term would be GO:0016616.",
    "The GO:0016628 annotation is IEA (inferred from electronic annotation via InterPro), not directly experimental. The experimental evidence (PubMed:38382015) supports the protein as an NAD-dependent dehydrogenase but maps to GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity) rather than GO:0016628.",
    "The reviewer-only evidence reveals the protein identity (Campylobacter jejuni, UAMDH_CAMJU), but this identity was not available to the evaluated model. The reasoning argument relies only on sequence motifs and transferable dehydrogenase-family knowledge."
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
  "benchmark_sequence_length": 407,
  "benchmark_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_entry_audit": {
    "entryVersion": 22,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 407,
  "current_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3AB61",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "selected_historical_source_sequence_length": 407,
  "selected_historical_source_sequence_sha256": "973aa0d220221e72d65582aa5a4553875ac176a4c5c02b0b6f18a17eed4370f3",
  "selected_historical_version": {
    "accession": "A0A0U3AB61",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAMDH_CAMJU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3AB61\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":22,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni\",\"taxonId\":197}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"UDP-ManNAc 6-dehydrogenase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.336\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-mannosamine dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Dehydrogenase involved in the biosynthesis of capsular polysaccharides (PubMed:38382015). Catalyzes the NAD(+)-dependent oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc) to UDP-N-acetyl-D-mannosaminuronic acid (UDP-ManNAcA) (PubMed:38382015)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:25781\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.336\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:25780\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:68623\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70731\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051287\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:NAD binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016628\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"id\":\"GO:0089714\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:UDP-N-acetyl-D-mannosamine dehydrogenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HS:11\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:40.671066+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   UAMDH_CAMJU             Reviewed;         407 AA.\nAC   A0A0U3AB61;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=UDP-N-acetyl-D-mannosamine dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.336 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=UDP-ManNAc 6-dehydrogenase {ECO:0000303|PubMed:38382015};\nGN   Name=HS11.16 {ECO:0000303|PubMed:38382015};\nOS   Campylobacter jejuni.\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=197;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=HS:11;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dehydrogenase involved in the biosynthesis of capsular\nCC       polysaccharides (PubMed:38382015). Catalyzes the NAD(+)-dependent\nCC       oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc) to UDP-N-acetyl-D-\nCC       mannosaminuronic acid (UDP-ManNAcA) (PubMed:38382015).\nCC       {ECO:0000269|PubMed:38382015}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-\nCC         acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:25780, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:68623,\nCC         ChEBI:CHEBI:70731; EC=1.1.1.336;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25781;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0051287; F:NAD binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016628; F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0089714; F:UDP-N-acetyl-D-mannosamine dehydrogenase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:21.162556+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a",
  "url": "https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003690\nname: double-stranded DNA binding\nnamespace: molecular_function\ndef: \"Binding to double-stranded DNA.\" [GOC:elh, GOC:vw]\nsynonym: \"dsDNA binding\" EXACT [GOC:elh]\nis_a: GO:0003677 ! DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003690",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 27939-27946",
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
  "excerpt": "[Term]\nid: GO:0005509\nname: calcium ion binding\nnamespace: molecular_function\ndef: \"Binding to a calcium ion (Ca2+).\" [GOC:ai]\nsynonym: \"calcium ion storage activity\" RELATED []\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005509",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56927-56934",
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
  "excerpt": "[Term]\nid: GO:0016628\nname: oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor\nnamespace: molecular_function\ndef: \"Catalysis of an oxidation-reduction (redox) reaction in which a CH-CH group acts as a hydrogen or electron donor and reduces NAD or NADP.\" [EC:1.3.1.-]\nxref: EC:1.3.1.-\nxref: Reactome:R-HSA-4755572 \"Defective SRD5A3 does not reduce pPNOL to DCHOL\"\nxref: Reactome:R-HSA-9661726 \"An unknown reductase reduces D-UBGN to STBN\"\nxref: Reactome:R-HSA-9661745 \"An unknown BILR reduces BIL to D-UBGN\"\nis_a: GO:0016627 ! oxidoreductase activity, acting on the CH-CH group of donors\nproperty_value: skos:exactMatch EC:1.3.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016628",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 128398-128409",
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
  "excerpt": "[Term]\nid: GO:0070566\nname: adenylyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of an adenylyl group to an acceptor.\" [GOC:mah]\nxref: Reactome:R-HSA-9935837 \"The TRAMP:RNA exosome oligoadenylates pre-rRNA 5' external transcribed spacer (5'ETS) fragment\"\nis_a: GO:0016779 ! nucleotidyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070566",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 368928-368935",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
