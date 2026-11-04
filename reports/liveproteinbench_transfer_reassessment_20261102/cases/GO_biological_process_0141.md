# GO_biological_process_0141

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0141.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — antibiotic biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQDPRVAAGYDFQEPVFLVDGVQEMAAGITDPDVLALSCYVWNFRRQMKVARLVKERHPGMLVVAGGPHVPDRPGDFFARHPYVDVLVHGEGETAFRELLIERLADHPDYTRVPGVSVRHGTEAVPGRPAERLPRRIETPSPYLLGVMDGAVATCRQRDLRFYALWETNRGCPYSCAFCDWGSATMSALRLFDAERLQEEIEWFAEHDVEDLFVCDANFGILPRDLEIARALADARAATGAPKLIRVNFAKNSNDRVFEISKTWHDADLLMGTTLSMQSTDLDVLEAIDRKNIGLENYRKLQQRYATENIHTYTELILGLPLESPRSFRDGIGSLLEAGNHEDIRVYEFGILPNAPINTPEKIAGYGLRTVPKRLYVEEPGTPDDEAETVDMVMETNAMSRDEWVDCFGFVQAVQFLHNGCYTRYLSMYLRQRHDIGYTAFYERLQQYFGARPDTVLGSIYLRMRKLYHDYIDIPELPLANLVASQPDMAADLARYGKRRGWTIDNWGWLRIANDFERTYTELRDFVAALGVDDTSDPDLAEVFRFQQDVMLRPDYDPAAGRTTEYTADWPGYFTTGELRRRPVRMRLADQRFGANGRYTPVPGDLKAFARAAIGPSYPVSRIGHYRHRFEAAEVTSPAEPVLTEQR

[Multiple Choices]
A. toll-like receptor TLR6:TLR2 signaling pathway
B. regulation of locomotion
C. cellular response to nicotine
D. antibiotic biosynthetic process
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

> The supplied sequence matches the annotated protein. Its cited function is methylation involved in thienamycin, a carbapenem antibiotic, biosynthesis, and the pathway annotation is antibiotic biosynthesis. The function annotation cites experimental evidence; the GO annotation itself is marked IEA.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a CxxxCxxC cysteine motif characteristic of radical SAM enzymes, a family that catalyzes specialized radical-dependent transformations, including methylations in natural-product biosynthesis. This supports a biosynthetic enzyme interpretation over the offered receptor-signaling, locomotion-regulation, or nicotine-response processes, making antibiotic biosynthesis the meaningful choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The motif and enzyme-family inference provide a transferable basis for selecting D from these choices, without needing the exact protein annotation. They do not independently establish the precise substrate or antibiotic pathway, so the inference is strongest at the level of distinguishing the offered options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed alternatives, antibiotic biosynthesis is the only one consistent with the sequence’s enzyme-family clues; the other choices describe signaling or cellular-response processes.


### Important caveats

- A radical SAM motif alone does not identify the enzyme’s specific substrate or prove antibiotic biosynthesis; that specificity is established by the reviewer-only functional evidence.
- The supplied GO annotation is marked IEA, while the supporting functional annotation cites experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC cysteine motif characteristic of radical SAM enzymes, a family that catalyzes specialized radical-dependent transformations, including methylations in natural-product biosynthesis. This supports a biosynthetic enzyme interpretation over the offered receptor-signaling, locomotion-regulation, or nicotine-response processes, making antibiotic biosynthesis the meaningful choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The motif and enzyme-family inference provide a transferable basis for selecting D from these choices, without needing the exact protein annotation. They do not independently establish the precise substrate or antibiotic pathway, so the inference is strongest at the level of distinguishing the offered options."
  },
  "case_id": "GO_biological_process_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its cited function is methylation involved in thienamycin, a carbapenem antibiotic, biosynthesis, and the pathway annotation is antibiotic biosynthesis. The function annotation cites experimental evidence; the GO annotation itself is marked IEA."
  },
  "important_caveats": [
    "A radical SAM motif alone does not identify the enzyme’s specific substrate or prove antibiotic biosynthesis; that specificity is established by the reviewer-only functional evidence.",
    "The supplied GO annotation is marked IEA, while the supporting functional annotation cites experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, antibiotic biosynthesis is the only one consistent with the sequence’s enzyme-family clues; the other choices describe signaling or cellular-response processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. Its cited function is methylation involved in thienamycin, a carbapenem antibiotic, biosynthesis, and the pathway annotation is antibiotic biosynthesis. The function annotation cites experimental evidence; the GO annotation itself is marked IEA.",
    "evidence_ids": ["C5", "C6", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC cysteine motif characteristic of radical SAM enzymes, a family that catalyzes specialized radical-dependent transformations, including methylations in natural-product biosynthesis. This supports a biosynthetic enzyme interpretation over the offered receptor-signaling, locomotion-regulation, or nicotine-response processes, making antibiotic biosynthesis the meaningful choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The motif and enzyme-family inference provide a transferable basis for selecting D from these choices, without needing the exact protein annotation. They do not independently establish the precise substrate or antibiotic pathway, so the inference is strongest at the level of distinguishing the offered options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, antibiotic biosynthesis is the only one consistent with the sequence’s enzyme-family clues; the other choices describe signaling or cellular-response processes."
  },
  "important_caveats": [
    "A radical SAM motif alone does not identify the enzyme’s specific substrate or prove antibiotic biosynthesis; that specificity is established by the reviewer-only functional evidence.",
    "The supplied GO annotation is marked IEA, while the supporting functional annotation cites experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q83XP3 (ThnK, EC 2.1.1.394) is a methyltransferase involved in the biosynthesis of the beta-lactam carbapenem antibiotic thienamycin in Streptomyces cattleya. The PATHWAY comment explicitly states 'Antibiotic biosynthesis' with experimental evidence (ECO:0000269, PubMed:26240322; ECO:0000305, PubMed:12725858). The GO annotation GO:0017000 (antibiotic biosynthetic process) is present (IEA:UniProtKB-KW). The sequence matches exactly (681 AA, identical SHA256). Option D is well-supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a canonical bacterial Sec-type signal peptide (MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQ — positively charged N-terminus, hydrophobic core, cleavage site), identifying this as a bacterial protein. Options A (TLR6:TLR2 signaling) and C (cellular response to nicotine) are strictly eukaryotic processes (mammalian innate immunity and neuronal nicotinic receptor signaling, respectively), immediately eliminated by the bacterial context. The sequence contains a radical SAM cluster motif (CxxxCxxC visible as 'CPYSCAFCDW' near residue ~280), a well-known feature of enzymes involved in natural product/secondary metabolite biosynthesis across many bacterial species (e.g., thiamine, biotin, polyketide, and non-ribosomal peptide pathways). Bacterial radical SAM enzymes are overwhelmingly associated with biosynthetic pathways for small molecules, not motility regulation (which uses CheA/CheY/flagellar domains). Among the remaining options, D (antibiotic biosynthetic process) is the only one consistent with a bacterial radical SAM enzyme engaged in small-molecule biosynthesis. Option B (regulation of locomotion) would require chemotaxis or flagellar motor components, which are absent.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A and C by recognizing the bacterial signal peptide (eukaryotic processes ruled out), eliminate B by the absence of chemotaxis/motility domains and presence of a radical SAM cluster, and select D by the well-established association of radical SAM enzymes with natural product biosynthesis in bacteria (especially actinobacteria). This is a legitimate family/pattern-level inference from other radical SAM enzymes and bacterial biosynthetic pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span radically different biological contexts (mammalian immune signaling, eukaryotic motility, eukaryotic neuronal response, bacterial secondary metabolism). The bacterial signal peptide and radical SAM motif cleanly separate D from the three eukaryotic or motility-specific alternatives. No option is defensible for this bacterial enzyme.


### Important caveats

- The GO:0017000 annotation is IEA:UniProtKB-KW (inferred from keyword), but the underlying pathway assignment is supported by experimental evidence (PubMed:26240322, PubMed:12725858).
- The protein is ThnK, a cobalamin-dependent radical SAM methyltransferase. Its radical SAM cluster (CxxxCxxC) is a transferable feature shared with many other radical SAM enzymes in natural product biosynthesis.
- The sequence lacks any transmembrane segments, TIR domains, or neuronal receptor features that would support options A or C.
- The reviewer-only evidence confirms the sequence matches Q83XP3 exactly; the model was not given the accession or organism name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a canonical bacterial Sec-type signal peptide (MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQ — positively charged N-terminus, hydrophobic core, cleavage site), identifying this as a bacterial protein. Options A (TLR6:TLR2 signaling) and C (cellular response to nicotine) are strictly eukaryotic processes (mammalian innate immunity and neuronal nicotinic receptor signaling, respectively), immediately eliminated by the bacterial context. The sequence contains a radical SAM cluster motif (CxxxCxxC visible as 'CPYSCAFCDW' near residue ~280), a well-known feature of enzymes involved in natural product/secondary metabolite biosynthesis across many bacterial species (e.g., thiamine, biotin, polyketide, and non-ribosomal peptide pathways). Bacterial radical SAM enzymes are overwhelmingly associated with biosynthetic pathways for small molecules, not motility regulation (which uses CheA/CheY/flagellar domains). Among the remaining options, D (antibiotic biosynthetic process) is the only one consistent with a bacterial radical SAM enzyme engaged in small-molecule biosynthesis. Option B (regulation of locomotion) would require chemotaxis or flagellar motor components, which are absent.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by recognizing the bacterial signal peptide (eukaryotic processes ruled out), eliminate B by the absence of chemotaxis/motility domains and presence of a radical SAM cluster, and select D by the well-established association of radical SAM enzymes with natural product biosynthesis in bacteria (especially actinobacteria). This is a legitimate family/pattern-level inference from other radical SAM enzymes and bacterial biosynthetic pathways."
  },
  "case_id": "GO_biological_process_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q83XP3 (ThnK, EC 2.1.1.394) is a methyltransferase involved in the biosynthesis of the beta-lactam carbapenem antibiotic thienamycin in Streptomyces cattleya. The PATHWAY comment explicitly states 'Antibiotic biosynthesis' with experimental evidence (ECO:0000269, PubMed:26240322; ECO:0000305, PubMed:12725858). The GO annotation GO:0017000 (antibiotic biosynthetic process) is present (IEA:UniProtKB-KW). The sequence matches exactly (681 AA, identical SHA256). Option D is well-supported."
  },
  "important_caveats": [
    "The GO:0017000 annotation is IEA:UniProtKB-KW (inferred from keyword), but the underlying pathway assignment is supported by experimental evidence (PubMed:26240322, PubMed:12725858).",
    "The protein is ThnK, a cobalamin-dependent radical SAM methyltransferase. Its radical SAM cluster (CxxxCxxC) is a transferable feature shared with many other radical SAM enzymes in natural product biosynthesis.",
    "The sequence lacks any transmembrane segments, TIR domains, or neuronal receptor features that would support options A or C.",
    "The reviewer-only evidence confirms the sequence matches Q83XP3 exactly; the model was not given the accession or organism name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span radically different biological contexts (mammalian immune signaling, eukaryotic motility, eukaryotic neuronal response, bacterial secondary metabolism). The bacterial signal peptide and radical SAM motif cleanly separate D from the three eukaryotic or motility-specific alternatives. No option is defensible for this bacterial enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q83XP3 (ThnK, EC 2.1.1.394) is a methyltransferase involved in the biosynthesis of the beta-lactam carbapenem antibiotic thienamycin in Streptomyces cattleya. The PATHWAY comment explicitly states 'Antibiotic biosynthesis' with experimental evidence (ECO:0000269, PubMed:26240322; ECO:0000305, PubMed:12725858). The GO annotation GO:0017000 (antibiotic biosynthetic process) is present (IEA:UniProtKB-KW). The sequence matches exactly (681 AA, identical SHA256). Option D is well-supported.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a canonical bacterial Sec-type signal peptide (MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQ — positively charged N-terminus, hydrophobic core, cleavage site), identifying this as a bacterial protein. Options A (TLR6:TLR2 signaling) and C (cellular response to nicotine) are strictly eukaryotic processes (mammalian innate immunity and neuronal nicotinic receptor signaling, respectively), immediately eliminated by the bacterial context. The sequence contains a radical SAM cluster motif (CxxxCxxC visible as 'CPYSCAFCDW' near residue ~280), a well-known feature of enzymes involved in natural product/secondary metabolite biosynthesis across many bacterial species (e.g., thiamine, biotin, polyketide, and non-ribosomal peptide pathways). Bacterial radical SAM enzymes are overwhelmingly associated with biosynthetic pathways for small molecules, not motility regulation (which uses CheA/CheY/flagellar domains). Among the remaining options, D (antibiotic biosynthetic process) is the only one consistent with a bacterial radical SAM enzyme engaged in small-molecule biosynthesis. Option B (regulation of locomotion) would require chemotaxis or flagellar motor components, which are absent.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by recognizing the bacterial signal peptide (eukaryotic processes ruled out), eliminate B by the absence of chemotaxis/motility domains and presence of a radical SAM cluster, and select D by the well-established association of radical SAM enzymes with natural product biosynthesis in bacteria (especially actinobacteria). This is a legitimate family/pattern-level inference from other radical SAM enzymes and bacterial biosynthetic pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span radically different biological contexts (mammalian immune signaling, eukaryotic motility, eukaryotic neuronal response, bacterial secondary metabolism). The bacterial signal peptide and radical SAM motif cleanly separate D from the three eukaryotic or motility-specific alternatives. No option is defensible for this bacterial enzyme."
  },
  "important_caveats": [
    "The GO:0017000 annotation is IEA:UniProtKB-KW (inferred from keyword), but the underlying pathway assignment is supported by experimental evidence (PubMed:26240322, PubMed:12725858).",
    "The protein is ThnK, a cobalamin-dependent radical SAM methyltransferase. Its radical SAM cluster (CxxxCxxC) is a transferable feature shared with many other radical SAM enzymes in natural product biosynthesis.",
    "The sequence lacks any transmembrane segments, TIR domains, or neuronal receptor features that would support options A or C.",
    "The reviewer-only evidence confirms the sequence matches Q83XP3 exactly; the model was not given the accession or organism name."
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
  "benchmark_sequence_length": 681,
  "benchmark_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 681,
  "current_source_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q83XP3",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "selected_historical_source_sequence_length": 681,
  "selected_historical_source_sequence_sha256": "9af3f057a63063df67b1505a5dd7494c95280d99f3fa45c9786ad221469f52c2",
  "selected_historical_version": {
    "accession": "Q83XP3",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "THNK_STREN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q83XP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Streptomyces cattleya\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptantibioticus\"],\"scientificName\":\"Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NRRL 8057)\",\"taxonId\":1003195}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31774078\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36042702\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.394\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12725858\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31774078\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36042702\",\"source\":\"PubMed\"}],\"value\":\"Methyltransferase involved in the biosynthesis of the beta-lactam carbapenem antibiotic thienamycin (PubMed:12725858, PubMed:26240322). Catalyzes two consecutive S-adenosyl-L-methionine-dependent methylations to build out the C6-ethyl side chain in a stereocontrolled manner (PubMed:26240322, PubMed:31774078, PubMed:36042702). In vitro can use methyl viologen and NADPH as the iron-sulfur cluster reductants (PubMed:26240322)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26240322\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"12725858\",\"source\":\"PubMed\"}],\"value\":\"Antibiotic biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Nunez L.E.\",\"Mendez C.\",\"Brana A.F.\",\"Blanco G.\",\"Salas J.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12725858\"},{\"database\":\"DOI\",\"id\":\"10.1016/s1074-5521(03)00069-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"301\",\"id\":\"12725858\",\"journal\":\"Chem. Biol.\",\"lastPage\":\"311\",\"publicationDate\":\"2003\",\"title\":\"The biosynthetic gene cluster for the beta-lactam carbapenem thienamycin in Streptomyces cattleya.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD18979.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL 8057 / MA-4297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"GENE CLUSTER\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Marous D.R.\",\"Lloyd E.P.\",\"Buller A.R.\",\"Moshos K.A.\",\"Grove T.L.\",\"Blaszczyk A.J.\",\"Booker S.J.\",\"Townsend C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26240322\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1508615112\"}],\"citationType\":\"journal article\",\"firstPage\":\"10354\",\"id\":\"26240322\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"10358\",\"publicationDate\":\"2015\",\"title\":\"Consecutive radical S-adenosylmethionine methylations form the ethyl side chain in thienamycin biosynthesis.\",\"volume\":\"112\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL 8057 / MA-4297\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sinner E.K.\",\"Lichstrahl M.S.\",\"Li R.\",\"Marous D.R.\",\"Townsend C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31774078\"},{\"database\":\"DOI\",\"id\":\"10.1039/c9cc07197k\"}],\"citationType\":\"journal article\",\"firstPage\":\"14934\",\"id\":\"31774078\",\"journal\":\"Chem. Commun. (Camb.)\",\"lastPage\":\"14937\",\"publicationDate\":\"2019\",\"title\":\"Methylations in complex carbapenem biosynthesis are catalyzed by a single cobalamin-dependent radical S-adenosylmethionine enzyme.\",\"volume\":\"55\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Lichstrahl M.S.\",\"Townsend C.A.\",\"Sinner E.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36042702\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2cb00113f\"}],\"citationType\":\"journal article\",\"firstPage\":\"1028\",\"id\":\"36042702\",\"journal\":\"RSC Chem. Biol.\",\"lastPage\":\"1034\",\"publicationDate\":\"2022\",\"title\":\"Stereochemical course of cobalamin-dependent radical SAM methylation by TokK and ThnK.\",\"volume\":\"3\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"REACTION MECHANISM FOR THE FIRST METHYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:53.086451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1",
  "url": "https://rest.uniprot.org/uniprotkb/Q83XP3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   THNK_STREN              Reviewed;         681 AA.\nAC   Q83XP3; F8JND9; G8XDF2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2003, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};\nDE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};\nGN   Name=thnK {ECO:0000303|PubMed:12725858};\nGN   OrderedLocusNames=SCATT_p09050 {ECO:0000312|EMBL:AEW99098.1};\nOS   Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925\nOS   / NBRC 14057 / NRRL 8057) (Streptomyces cattleya).\nOG   Plasmid pSCATT {ECO:0000312|EMBL:AEW99098.1}.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptantibioticus.\nOX   NCBI_TaxID=1003195;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAD18979.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND GENE CLUSTER.\nRC   STRAIN=ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL\nRC   8057 / MA-4297;\nRX   PubMed=12725858; DOI=10.1016/s1074-5521(03)00069-3;\nRA   Nunez L.E., Mendez C., Brana A.F., Blanco G., Salas J.A.;\nRT   \"The biosynthetic gene cluster for the beta-lactam carbapenem thienamycin\nRT   in Streptomyces cattleya.\";\nRL   Chem. Biol. 10:301-311(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, AND PATHWAY.\nRC   STRAIN=ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL\nRC   8057 / MA-4297;\nRX   PubMed=26240322; DOI=10.1073/pnas.1508615112;\nRA   Marous D.R., Lloyd E.P., Buller A.R., Moshos K.A., Grove T.L.,\nRA   Blaszczyk A.J., Booker S.J., Townsend C.A.;\nRT   \"Consecutive radical S-adenosylmethionine methylations form the ethyl side\nRT   chain in thienamycin biosynthesis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 112:10354-10358(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31774078; DOI=10.1039/c9cc07197k;\nRA   Sinner E.K., Lichstrahl M.S., Li R., Marous D.R., Townsend C.A.;\nRT   \"Methylations in complex carbapenem biosynthesis are catalyzed by a single\nRT   cobalamin-dependent radical S-adenosylmethionine enzyme.\";\nRL   Chem. Commun. (Camb.) 55:14934-14937(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "RN   [6]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND REACTION MECHANISM FOR THE FIRST\nRP   METHYLATION.\nRX   PubMed=36042702; DOI=10.1039/d2cb00113f;\nRA   Lichstrahl M.S., Townsend C.A., Sinner E.K.;\nRT   \"Stereochemical course of cobalamin-dependent radical SAM methylation by\nRT   TokK and ThnK.\";\nRL   RSC Chem. Biol. 3:1028-1034(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Methyltransferase involved in the biosynthesis of the beta-\nCC       lactam carbapenem antibiotic thienamycin (PubMed:12725858,\nCC       PubMed:26240322). Catalyzes two consecutive S-adenosyl-L-methionine-\nCC       dependent methylations to build out the C6-ethyl side chain in a\nCC       stereocontrolled manner (PubMed:26240322, PubMed:31774078,\nCC       PubMed:36042702). In vitro can use methyl viologen and NADPH as the\nCC       iron-sulfur cluster reductants (PubMed:26240322).\nCC       {ECO:0000269|PubMed:12725858, ECO:0000269|PubMed:26240322,\nCC       ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H7",
  "excerpt": "CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000269|PubMed:26240322,\nCC       ECO:0000305|PubMed:12725858}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0017000; P:antibiotic biosynthetic process; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0032259; P:methylation; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:56.526994+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-140",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606",
  "url": "https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0017000\nname: antibiotic biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of an antibiotic, a substance produced by or derived from certain fungi, bacteria, and other organisms, that can destroy or inhibit the growth of other microorganisms.\" [GOC:curators]\nsubset: goslim_metagenomics\nsynonym: \"antibiotic anabolism\" EXACT []\nsynonym: \"antibiotic biosynthesis\" EXACT []\nsynonym: \"antibiotic formation\" EXACT []\nsynonym: \"antibiotic synthesis\" EXACT []\nis_a: GO:0009058 ! biosynthetic process\nis_a: GO:0016999 ! antibiotic metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0017000",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 132339-132351",
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
  "excerpt": "[Term]\nid: GO:0038124\nname: toll-like receptor TLR6:TLR2 signaling pathway\nnamespace: biological_process\ndef: \"The series of molecular signals initiated by a ligand binding of a heterodimeric TLR6:TLR2 complex, followed by transmission of the signal by the activated receptor, and ending with the regulation of a downstream cellular process, e.g. transcription.\" [GOC:nhn, GOC:signaling, PMID:17318230]\nsynonym: \"TLR2:TLR6 signaling pathway\" EXACT [GOC:bf]\nsynonym: \"toll-like receptor TLR6:TLR2 signalling pathway\" EXACT [GOC:mah]\nxref: Reactome:R-HSA-168188 \"Toll Like Receptor TLR6:TLR2 Cascade\"\nis_a: GO:0002224 ! toll-like receptor signaling pathway\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0038124",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 229944-229953",
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
  "excerpt": "[Term]\nid: GO:0040012\nname: regulation of locomotion\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of locomotion of a cell or organism.\" [GOC:ems]\nis_a: GO:0050789 ! regulation of biological process\nrelationship: regulates GO:0040011 ! locomotion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0040012",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 233200-233207",
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
  "excerpt": "[Term]\nid: GO:0071316\nname: cellular response to nicotine\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a nicotine stimulus.\" [GOC:mah]\nis_a: GO:0035094 ! response to nicotine\nis_a: GO:0070887 ! cellular response to chemical stimulus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071316",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 375973-375980",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
