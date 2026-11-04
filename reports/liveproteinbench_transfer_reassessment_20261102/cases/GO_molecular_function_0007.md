# GO_molecular_function_0007

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0007.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — metal ion binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. glycosyltransferase activity
B. CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity
C. mechanosensitive monoatomic cation channel activity
D. metal ion binding
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

### Expected-answer support: supported

> The sequence-matched record annotates zinc ion binding with IDA evidence, and zinc ion binding is a subtype of metal ion binding. The record also identifies the protein as a zinc metallopeptidase. Thus D is supported, though the protein also has catalytic activities not offered among the choices.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [GO1](#evidence-go1), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-like region followed by a globular, histidine- and acidic-residue-containing enzyme-like region, rather than the multiple transmembrane segments expected for a mechanosensitive channel. Transferable knowledge of secreted or envelope-associated metalloproteases makes metal binding a credible fit; the two highly specific phosphatidyltransferase and glycosyltransferase options are less consistent with that pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the broad contrast among the options support D probabilistically through transferable knowledge about enzyme and metalloprotease patterns. Sequence motifs alone do not prove metal binding or establish it as the protein's primary function, but the alternatives make a meaningful distinction possible without recalling this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, metal ion binding is the only defensible match; the protein's more specific catalytic activities are not listed.


### Important caveats

- The reviewer-only sequence-matched annotation supports the key but was not available to the evaluated model.
- Metal binding is supported as a molecular function, but it need not be the protein's sole or primary activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-like region followed by a globular, histidine- and acidic-residue-containing enzyme-like region, rather than the multiple transmembrane segments expected for a mechanosensitive channel. Transferable knowledge of secreted or envelope-associated metalloproteases makes metal binding a credible fit; the two highly specific phosphatidyltransferase and glycosyltransferase options are less consistent with that pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the broad contrast among the options support D probabilistically through transferable knowledge about enzyme and metalloprotease patterns. Sequence motifs alone do not prove metal binding or establish it as the protein's primary function, but the alternatives make a meaningful distinction possible without recalling this exact protein's annotation."
  },
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "GO1",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates zinc ion binding with IDA evidence, and zinc ion binding is a subtype of metal ion binding. The record also identifies the protein as a zinc metallopeptidase. Thus D is supported, though the protein also has catalytic activities not offered among the choices."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports the key but was not available to the evaluated model.",
    "Metal binding is supported as a molecular function, but it need not be the protein's sole or primary activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, metal ion binding is the only defensible match; the protein's more specific catalytic activities are not listed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates zinc ion binding with IDA evidence, and zinc ion binding is a subtype of metal ion binding. The record also identifies the protein as a zinc metallopeptidase. Thus D is supported, though the protein also has catalytic activities not offered among the choices.",
    "evidence_ids": ["C4", "C8", "GO1", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-like region followed by a globular, histidine- and acidic-residue-containing enzyme-like region, rather than the multiple transmembrane segments expected for a mechanosensitive channel. Transferable knowledge of secreted or envelope-associated metalloproteases makes metal binding a credible fit; the two highly specific phosphatidyltransferase and glycosyltransferase options are less consistent with that pattern.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the broad contrast among the options support D probabilistically through transferable knowledge about enzyme and metalloprotease patterns. Sequence motifs alone do not prove metal binding or establish it as the protein's primary function, but the alternatives make a meaningful distinction possible without recalling this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, metal ion binding is the only defensible match; the protein's more specific catalytic activities are not listed."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports the key but was not available to the evaluated model.",
    "Metal binding is supported as a molecular function, but it need not be the protein's sole or primary activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (E0N688) annotates GO:0046872 (metal ion binding) via IEA:UniProtKB-KW, and the more specific GO:0008270 (zinc ion binding) with IDA evidence (experimental, from PDB 3SLU crystal structure in complex with nickel). GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the parent term applies. The protein is a zinc-dependent metalloprotease, confirming metal ion binding. While the primary catalytic function is peptidase activity (not offered), D is the only correct option among the four choices.

Citations as saved: [C8](#evidence-c8), [H4](#evidence-h4), [GO1](#evidence-go1), [GO4](#evidence-go4), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use several transferable features: (1) The N-terminal hydrophobic stretch (MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTER) is a classic signal peptide indicating a secreted/outer membrane protein, not an inner-membrane phosphatidyltransferase (B) or a multi-TM mechanosensitive channel (C). (2) Mechanosensitive channels (e.g., MscS, MscL, Piezo) require multiple transmembrane helices with specific topologies; this sequence shows only one clear hydrophobic segment (the signal peptide), ruling out C. (3) Glycosyltransferases typically contain conserved motifs (e.g., DXD, HxH, or specific β-strand arrangements); the sequence lacks these, making A unlikely. (4) CDP-diacylglycerol phosphatidyltransferases are inner-membrane enzymes with specific conserved motifs and topology; the signal-peptide architecture is inconsistent, ruling out B. (5) Positive evidence for metal binding: the sequence contains multiple histidine clusters (HPILHTWRLHTG, RSTGPHLHYEARINGQ, HANGVETLYAHLSAFSQAQ) that are hallmark metal-coordination motifs in metalloproteases. Combined with the secreted-protein architecture (signal peptide + globular domain), this is consistent with a periplasmic/outer membrane metalloprotease that binds zinc. Thus D is distinguishable by elimination and positive motif recognition.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A, B, and C relies on well-known structural/sequence signatures of those protein families (multi-TM topology for channels, specific catalytic motifs for transferases, inner-membrane topology for phosphatidyltransferases). The positive identification of D is supported by histidine-rich clusters (common in zinc-binding sites of metalloproteases) and the secreted-protein architecture. This constitutes a credible transferable inference from general protein-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe highly specific enzymatic or channel activities with distinctive structural requirements that are clearly incompatible with the sequence features (single signal peptide, no multi-TM helices, no transferase motifs). Only D (metal ion binding) is compatible with the observed histidine clusters and secreted-protein architecture. No ambiguity among the offered choices.


### Important caveats

- The question asks for 'primary molecular function,' but the true primary function is peptidase (metalloendopeptidase/carboxypeptidase) activity, which is not offered. Metal ion binding is a component of the catalytic mechanism rather than the primary catalytic activity. However, among the four choices, D is the only applicable one.
- GO:0046872 (metal ion binding) is annotated via IEA (automatic keyword assignment), while the experimental evidence (IDA) supports the more specific GO:0008270 (zinc ion binding). The broad term is technically correct but less informative than the specific annotation.
- The histidine-rich regions are suggestive but not definitive proof of metal coordination without structural data; however, combined with the overall architecture, they provide reasonable inferential support for D over the other three options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features: (1) The N-terminal hydrophobic stretch (MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTER) is a classic signal peptide indicating a secreted/outer membrane protein, not an inner-membrane phosphatidyltransferase (B) or a multi-TM mechanosensitive channel (C). (2) Mechanosensitive channels (e.g., MscS, MscL, Piezo) require multiple transmembrane helices with specific topologies; this sequence shows only one clear hydrophobic segment (the signal peptide), ruling out C. (3) Glycosyltransferases typically contain conserved motifs (e.g., DXD, HxH, or specific β-strand arrangements); the sequence lacks these, making A unlikely. (4) CDP-diacylglycerol phosphatidyltransferases are inner-membrane enzymes with specific conserved motifs and topology; the signal-peptide architecture is inconsistent, ruling out B. (5) Positive evidence for metal binding: the sequence contains multiple histidine clusters (HPILHTWRLHTG, RSTGPHLHYEARINGQ, HANGVETLYAHLSAFSQAQ) that are hallmark metal-coordination motifs in metalloproteases. Combined with the secreted-protein architecture (signal peptide + globular domain), this is consistent with a periplasmic/outer membrane metalloprotease that binds zinc. Thus D is distinguishable by elimination and positive motif recognition.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A, B, and C relies on well-known structural/sequence signatures of those protein families (multi-TM topology for channels, specific catalytic motifs for transferases, inner-membrane topology for phosphatidyltransferases). The positive identification of D is supported by histidine-rich clusters (common in zinc-binding sites of metalloproteases) and the secreted-protein architecture. This constitutes a credible transferable inference from general protein-family knowledge."
  },
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H4",
      "GO1",
      "GO4",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (E0N688) annotates GO:0046872 (metal ion binding) via IEA:UniProtKB-KW, and the more specific GO:0008270 (zinc ion binding) with IDA evidence (experimental, from PDB 3SLU crystal structure in complex with nickel). GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the parent term applies. The protein is a zinc-dependent metalloprotease, confirming metal ion binding. While the primary catalytic function is peptidase activity (not offered), D is the only correct option among the four choices."
  },
  "important_caveats": [
    "The question asks for 'primary molecular function,' but the true primary function is peptidase (metalloendopeptidase/carboxypeptidase) activity, which is not offered. Metal ion binding is a component of the catalytic mechanism rather than the primary catalytic activity. However, among the four choices, D is the only applicable one.",
    "GO:0046872 (metal ion binding) is annotated via IEA (automatic keyword assignment), while the experimental evidence (IDA) supports the more specific GO:0008270 (zinc ion binding). The broad term is technically correct but less informative than the specific annotation.",
    "The histidine-rich regions are suggestive but not definitive proof of metal coordination without structural data; however, combined with the overall architecture, they provide reasonable inferential support for D over the other three options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe highly specific enzymatic or channel activities with distinctive structural requirements that are clearly incompatible with the sequence features (single signal peptide, no multi-TM helices, no transferase motifs). Only D (metal ion binding) is compatible with the observed histidine clusters and secreted-protein architecture. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (E0N688) annotates GO:0046872 (metal ion binding) via IEA:UniProtKB-KW, and the more specific GO:0008270 (zinc ion binding) with IDA evidence (experimental, from PDB 3SLU crystal structure in complex with nickel). GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the parent term applies. The protein is a zinc-dependent metalloprotease, confirming metal ion binding. While the primary catalytic function is peptidase activity (not offered), D is the only correct option among the four choices.",
    "evidence_ids": ["C8", "H4", "GO1", "GO4", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use several transferable features: (1) The N-terminal hydrophobic stretch (MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTER) is a classic signal peptide indicating a secreted/outer membrane protein, not an inner-membrane phosphatidyltransferase (B) or a multi-TM mechanosensitive channel (C). (2) Mechanosensitive channels (e.g., MscS, MscL, Piezo) require multiple transmembrane helices with specific topologies; this sequence shows only one clear hydrophobic segment (the signal peptide), ruling out C. (3) Glycosyltransferases typically contain conserved motifs (e.g., DXD, HxH, or specific β-strand arrangements); the sequence lacks these, making A unlikely. (4) CDP-diacylglycerol phosphatidyltransferases are inner-membrane enzymes with specific conserved motifs and topology; the signal-peptide architecture is inconsistent, ruling out B. (5) Positive evidence for metal binding: the sequence contains multiple histidine clusters (HPILHTWRLHTG, RSTGPHLHYEARINGQ, HANGVETLYAHLSAFSQAQ) that are hallmark metal-coordination motifs in metalloproteases. Combined with the secreted-protein architecture (signal peptide + globular domain), this is consistent with a periplasmic/outer membrane metalloprotease that binds zinc. Thus D is distinguishable by elimination and positive motif recognition.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A, B, and C relies on well-known structural/sequence signatures of those protein families (multi-TM topology for channels, specific catalytic motifs for transferases, inner-membrane topology for phosphatidyltransferases). The positive identification of D is supported by histidine-rich clusters (common in zinc-binding sites of metalloproteases) and the secreted-protein architecture. This constitutes a credible transferable inference from general protein-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe highly specific enzymatic or channel activities with distinctive structural requirements that are clearly incompatible with the sequence features (single signal peptide, no multi-TM helices, no transferase motifs). Only D (metal ion binding) is compatible with the observed histidine clusters and secreted-protein architecture. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The question asks for 'primary molecular function,' but the true primary function is peptidase (metalloendopeptidase/carboxypeptidase) activity, which is not offered. Metal ion binding is a component of the catalytic mechanism rather than the primary catalytic activity. However, among the four choices, D is the only applicable one.",
    "GO:0046872 (metal ion binding) is annotated via IEA (automatic keyword assignment), while the experimental evidence (IDA) supports the more specific GO:0008270 (zinc ion binding). The broad term is technically correct but less informative than the specific annotation.",
    "The histidine-rich regions are suggestive but not definitive proof of metal coordination without structural data; however, combined with the overall architecture, they provide reasonable inferential support for D over the other three options."
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
  "benchmark_sequence_length": 430,
  "benchmark_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 430,
  "current_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E0N688",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "selected_historical_source_sequence_length": 430,
  "selected_historical_source_sequence_sha256": "3e75444ef73a59ea32e1df8dd911f094a963233fecca96f1fb511d7b05e30d56",
  "selected_historical_version": {
    "accession": "E0N688",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MPG_NEIM3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E0N688\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Neisseriales\",\"Neisseriaceae\",\"Neisseria\"],\"scientificName\":\"Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091)\",\"taxonId\":862513}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"Metalloprotease active against peptidoglycan\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Outer membrane protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"OMP\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metallopeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Zinc metalloprotease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"value\":\"Zinc-dependent metallopeptidase\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.17.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DD-carboxypeptidase/endopeptidase Mpg\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5F676\",\"source\":\"UniProtKB\"}],\"value\":\"Has both endopeptidase and DD-carboxypeptidase activities. Degrades cell wall peptidoglycan (PG) to allow consummate expression of pili\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004181\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:metallocarboxypeptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004222\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:metalloendopeptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"id\":\"GO:0008270\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:zinc ion binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Yang X.\",\"Yang C.\",\"Wu Z.\",\"Xu H.\",\"Shen Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22046377\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0026845\"}],\"citationType\":\"journal article\",\"firstPage\":\"e26845\",\"id\":\"22046377\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e26845\",\"publicationDate\":\"2011\",\"title\":\"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3SLU\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22046377\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 13091 / M2091\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL\",\"COFACTOR\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"PTM\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:57.637304+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a",
  "url": "https://rest.uniprot.org/uniprotkb/E0N688.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   MPG_NEIM3               Reviewed;         430 AA.\nAC   E0N688;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};\nDE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};\nDE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};\nDE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};\nDE            Short=OMP {ECO:0000303|PubMed:22046377};\nDE   AltName: Full=Zinc metallopeptidase {ECO:0000305};\nDE   AltName: Full=Zinc metalloprotease {ECO:0000305};\nDE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};\nDE   Flags: Precursor;\nGN   ORFNames=HMPREF0602_0018 {ECO:0000312|EMBL:EFM05396.1};\nOS   Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;\nOC   Neisseriaceae; Neisseria.\nOX   NCBI_TaxID=862513;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:3SLU}\nRP   X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL,\nRP   COFACTOR, SUBUNIT, SUBCELLULAR LOCATION, AND PTM.\nRC   STRAIN=ATCC 13091 / M2091 {ECO:0000303|PubMed:22046377};\nRX   PubMed=22046377; DOI=10.1371/journal.pone.0026845;\nRA   Wang X., Yang X., Yang C., Wu Z., Xu H., Shen Y.;\nRT   \"Crystal structure of outer membrane protein NMB0315 from Neisseria\nRT   meningitidis.\";\nRL   PLoS ONE 6:e26845-e26845(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Has both endopeptidase and DD-carboxypeptidase activities.\nCC       Degrades cell wall peptidoglycan (PG) to allow consummate expression of\nCC       pili. {ECO:0000250|UniProtKB:Q5F676}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004222; F:metalloendopeptidase activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:01.531640+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1",
  "url": "https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008270\nname: zinc ion binding\nnamespace: molecular_function\ndef: \"Binding to a zinc ion (Zn).\" [GOC:ai]\nsynonym: \"zinc binding\" EXACT []\nsynonym: \"Zn binding\" EXACT []\nis_a: GO:0046914 ! transition metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008270",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81431-81439",
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
  "excerpt": "[Term]\nid: GO:0008444\nname: CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: sn-glycerol 3-phosphate + CDP-diacylglycerol = 3-(3-sn-phosphatidyl)-sn-glycerol 1-phosphate + CMP + H+.\" [EC:2.7.8.5, RHEA:12593]\nsynonym: \"3-phosphatidyl-1'-glycerol-3'-phosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDP-diacylglycerol:sn-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol-sn-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol:glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol:sn-glycero-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"cytidine 5'-diphospho-1,2-diacyl-sn-glycerol (CDPdiglyceride):sn-glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerol 3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerol phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerophosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"PGP synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerol phosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerol phosphate synthetase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerolphosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerophosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerophosphate synthetase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"sn-glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nxref: EC:2.7.8.5\nxref: KEGG_REACTION:R01801\nxref: MetaCyc:PHOSPHAGLYPSYN-RXN\nxref: Reactome:R-HSA-1482939 \"CDP-DAG is converted to PGP by PGS1\"\nxref: RHEA:12593\nis_a: GO:0017169 ! CDP-alcohol phosphatidyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.8.5\nproperty_value: skos:exactMatch RHEA:12593\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008444",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 83359-83389",
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
  "excerpt": "[Term]\nid: GO:0016757\nname: glycosyltransferase activity\nnamespace: molecular_function\nalt_id: GO:0016932\ndef: \"Catalysis of the transfer of a glycosyl group from one compound (donor) to another (acceptor).\" [GOC:jl, ISBN:0198506732]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"transferase activity, transferring glycosyl groups\" EXACT []\nsynonym: \"transferase activity, transferring other glycosyl groups\" NARROW []\nsynonym: \"transglycosidase activity\" EXACT []\nsynonym: \"transglycosylase activity\" EXACT []\nxref: EC:2.4.-.-\nxref: Reactome:R-HSA-5173005 \"B3GALTL transfers glucose to O-fucosyl-proteins\"\nxref: Reactome:R-HSA-6785565 \"Defective B3GALTL does not transfer glucose to O-fucosyl-proteins\"\nis_a: GO:0016740 ! transferase activity\nproperty_value: skos:exactMatch EC:2.4.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016757",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129828-129846",
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
  "excerpt": "[Term]\nid: GO:0046872\nname: metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a metal ion.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsynonym: \"heavy metal binding\" NARROW []\nsynonym: \"metal binding\" EXACT []\nis_a: GO:0043169 ! cation binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046872",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281280-281292",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0046914\nname: transition metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a transition metal ions; a transition metal is an element whose atom has an incomplete d-subshell of extranuclear electrons, or which gives rise to a cation or cations with an incomplete d-subshell. Transition metals often have more than one valency state. Biologically relevant transition metals include vanadium, manganese, iron, copper, cobalt, nickel, molybdenum and silver.\" [ISBN:0198506732]\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046914",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281764-281770",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0140135\nname: mechanosensitive monoatomic cation channel activity\nnamespace: molecular_function\ndef: \"Enables the transmembrane transfer of a monoatomic cation by a channel that opens in response to a mechanical stress.\" [GOC:ha, PMID:22343900]\nsynonym: \"mechanically-gated cation channel activity\" EXACT []\nsynonym: \"mechanosensitive cation channel activity\" BROAD []\nxref: Reactome:R-HSA-9659380 \"Mechanoelectrical transduction (MET) channel transports cations from the extracellular region into the cytosol of stereocilia of inner hair cell\"\nxref: Reactome:R-HSA-9663363 \"Mechanoelectrical transduction (MET) channel transports cations into the cytosol of stereocilia of cochlear outer hair cell\"\nxref: Reactome:R-HSA-9855089 \"PIEZO1 trimer passively transports cations across the plasma membrane according to their electrochemical gradients\"\nis_a: GO:0005261 ! monoatomic cation channel activity\nis_a: GO:0008381 ! mechanosensitive monoatomic ion channel activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140135",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 437568-437580",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
