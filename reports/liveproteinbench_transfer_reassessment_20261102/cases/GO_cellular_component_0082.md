# GO_cellular_component_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0082.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — endosome membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAKAIQYNIKVDLHEVKDLSFREAAGEKEIVPNPYIEVTVNGVTKTTIQKTQVVSATFNTSFNFTAYLTPDEFARSYVEVAVLHKYMLIGGVGLQSAVIGKYVFSFAYVYTKSQHWIYRQWVTLRNLDQPQDETGLLLITVGVFGPGDAMPVVDETVCVVNEGERTSTDVNVKLTHYSLSVNIFKGQDIPSVAGQFSTVLEPYVKVKHGGAELQTRPLPDSNPDWLASISIPACVPCFDGNVLVELWNGQDSSTAAGTLMGTVVLDYFQLIKNDLPPRWFNFYWRPPAEGLLGAVTDMMASAELREPIAYGGRILLSASAAKVQTPLPLGVRSARPIPDPATQECVWWLDLYEMTSATGYTSELRIEIAFGPHVIKTASLEANALGTYVIGDNLGRLPEMKIFAPVDEVQVWDVMMYVCSPPATTVAAGIADISNWFSGWGGSPTATQNTPEPAETPWTRLAWVRIPYDSRQFQNGKPQWYSLRSLDGSGTDMFSVLLGMEMFPTKAGKQRAPRLEYKLARFYFRALIYEGLHLPAVGYDVFPDPYIQVELASKTLRTSTIRQTLNPSYYEAYEIEIRLPENISLAPDINVEVISESNSLLSSDVVLGSVQYPIQKVPKEWTKAPVWLQLHSKAYPRCKARVLVAFELVPAEKAEDDTYPFYDDIRPSTKEGNIRLFLVGVRLFKPITQPFVTVCFGRDVENTAEPLWSQESSAPRTGEGGNWNFLEEFTVSVSLPKRMQHHSFLEVKIQDRTQGIGGESNVDVGMAYITLNPLLPWLDSRERAESLETFRLQMLEEVLIEDAENARRSADGGLAARTGGGSFDEDATKKKEMLAAERSRKMAIPYNDPDMANLKIEEVDDYVSFKVAPRPQASRLSREGTSRDERGKAPGKSLSGMPGPVARASPGAGEETEKKGDPVAEKKEGGAQAAPPVAPSAHQREALAASPEEETYGFTPEQLNFVLADLEEDDAEEMTRDEVPYELEADFTVDDLPYLRTPIFRPTDAGVPETVGYLKYVCRVFQSTDEDEGAEMDAVCKSLIETYNSTRDLVVRAYVLAARGLVPPSGASDIQTYVWIQDSENAATLPGGLSYNIRDTGYTKKQGFKPEFNRCYTLACSLPENSIVQIAVMNMGRLTDECIGRTYLDVEDRFFNKKVEQMVIEESTPIELRTLKNEGSTVSHGSLRGFFEIMRADYAQLHPPYTLASAEPDEYQLRVVIWRVKAVPLDDNSSISLFVRTIYQLEDSSEIVKDTDTHYNSTDGTAVYNWRMVFDVLIPAQIPVLKLQIWNYALLSSTEPIGEANFDLTADFFRARKRQQHYRVPRMWVRCSHPAHKGKLRGTIEIEASILPREEAEYTPVGNGRDEPNRDPFLPAVTTNRTYIDWQQIGETVGAASSAIMSGLKWTGVWMTVAGIIALVIFVMFLLK

[Multiple Choices]
A. mitochondrial inner membrane
B. external side of plasma membrane
C. host cell
D. endosome membrane
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

> The sequence-matched UniProt record reports localization to the trans-Golgi–endosome network and specifically annotates the endosome membrane. The annotation is supported by experimental evidence, so D is supported, though the protein also has other reported locations.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long protein sequence and C-terminal hydrophobic segment are compatible with a membrane-associated protein, and its domain architecture may suggest a ferlin involved in membrane trafficking. Those transferable clues do not meaningfully distinguish an endosome membrane from the offered plasma-membrane-side location; they do not establish this protein’s primary compartment.


**Missing item-specific fact**

> The experimentally determined localization of this particular protein to the trans-Golgi–endosome network, including the endosome membrane.


**Reason**

> Family-level and sequence-based clues support membrane association and trafficking, but choosing D over the plausible membrane alternative B depends on localization information specific to this protein that is absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D among the offered choices. Although the protein has additional reported locations, the evidence does not establish another offered option as equally defensible.


### Important caveats

- The reported localization is dynamic and includes the trans-Golgi–endosome network and cytoplasm; the question’s single primary-location framing simplifies that biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long protein sequence and C-terminal hydrophobic segment are compatible with a membrane-associated protein, and its domain architecture may suggest a ferlin involved in membrane trafficking. Those transferable clues do not meaningfully distinguish an endosome membrane from the offered plasma-membrane-side location; they do not establish this protein’s primary compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined localization of this particular protein to the trans-Golgi–endosome network, including the endosome membrane.",
    "reason": "Family-level and sequence-based clues support membrane association and trafficking, but choosing D over the plausible membrane alternative B depends on localization information specific to this protein that is absent from the input."
  },
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports localization to the trans-Golgi–endosome network and specifically annotates the endosome membrane. The annotation is supported by experimental evidence, so D is supported, though the protein also has other reported locations."
  },
  "important_caveats": [
    "The reported localization is dynamic and includes the trans-Golgi–endosome network and cytoplasm; the question’s single primary-location framing simplifies that biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D among the offered choices. Although the protein has additional reported locations, the evidence does not establish another offered option as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports localization to the trans-Golgi–endosome network and specifically annotates the endosome membrane. The annotation is supported by experimental evidence, so D is supported, though the protein also has other reported locations.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long protein sequence and C-terminal hydrophobic segment are compatible with a membrane-associated protein, and its domain architecture may suggest a ferlin involved in membrane trafficking. Those transferable clues do not meaningfully distinguish an endosome membrane from the offered plasma-membrane-side location; they do not establish this protein’s primary compartment.",
    "missing_item_specific_fact": "The experimentally determined localization of this particular protein to the trans-Golgi–endosome network, including the endosome membrane.",
    "reason": "Family-level and sequence-based clues support membrane association and trafficking, but choosing D over the plausible membrane alternative B depends on localization information specific to this protein that is absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D among the offered choices. Although the protein has additional reported locations, the evidence does not establish another offered option as equally defensible."
  },
  "important_caveats": [
    "The reported localization is dynamic and includes the trans-Golgi–endosome network and cytoplasm; the question’s single primary-location framing simplifies that biology."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7J6JXB6, FER1_TOXGO) annotates this protein with GO:0010008 (endosome membrane) using IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment confirms localization to the trans-Golgi-endosome network in intracellular parasites, with the protein described as a single-pass membrane protein. While the protein also localizes to the trans-Golgi network membrane (IMP evidence) and cytoplasm, among the four offered choices, endosome membrane is the only one with direct experimental support. The answer D is consistent with the primary experimental annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable sequence features allow a knowledgeable model to narrow the choices: (1) The C-terminal hydrophobic stretch 'WTGVWMTVAGIIALVIFVMFLLK' is a clear single-pass transmembrane domain, confirming a membrane protein. (2) The protein is very large (~1425 AA) with multiple repeated domain-like modules containing conserved aspartate clusters, consistent with C2 calcium-binding domains characteristic of the ferlin family, which are well-known mediators of vesicle trafficking and membrane fusion in secretory/endosomal pathways. (3) No N-terminal mitochondrial targeting presequence is present, arguing against mitochondrial inner membrane (A). (4) The protein's unusual amino acid composition (high lysine/arginine, low GC-biased residues) is characteristic of an AT-rich apicomplexan parasite genome, indicating it is a parasite's own protein rather than a host cell component, arguing against C. (5) The multi-domain architecture with a single-pass TM topology and C2-like trafficking domains is inconsistent with a simple external-side plasma membrane protein (B); ferlins are intracellular membrane-trafficking proteins. Together, these features point toward an endosomal/secretory membrane compartment (D) over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The C-terminal TM domain, multi-domain architecture with C2-like motifs, absence of mitochondrial targeting, and parasite-specific sequence composition provide a transferable reasoning path from ferlin family biology and general cell biology to distinguish D from A, B, and C. While recognizing ferlin features in a divergent apicomplexan sequence is non-trivial, the combination of the clear TM domain, large multi-domain architecture, and elimination of the other three options via standard biological reasoning makes D the most defensible choice without requiring exact database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, A (mitochondrial inner membrane) is excluded by absence of targeting sequence; B (external side of plasma membrane) is inconsistent with the multi-domain intracellular trafficking architecture; C (host cell) is excluded because this is clearly a parasite-encoded protein, not a host component. D (endosome membrane) is the only option consistent with the ferlin-like trafficking role and single-pass membrane topology. The trans-Golgi network membrane, which is also annotated, is not among the choices, so no ambiguity arises between the offered alternatives.


### Important caveats

- The protein has dynamic localization: trans-Golgi-endosome network in intracellular parasites and cytoplasm in extracellular parasites. The 'primary' compartment is context-dependent, but among the four offered choices, endosome membrane is the best match.
- The trans-Golgi network membrane (GO:0032588, IMP evidence) is also annotated but is not offered as a choice, so it does not create ambiguity among the given options.
- Recognition of ferlin C2 domains in a divergent apicomplexan sequence is challenging; the reasoning relies on overall architecture and elimination of alternatives rather than precise domain identification.
- The 'host cell' option (C) could be superficially tempting for an intracellular parasite, but GO cellular component annotations for parasite proteins refer to the parasite's own compartments, not the host cell.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable sequence features allow a knowledgeable model to narrow the choices: (1) The C-terminal hydrophobic stretch 'WTGVWMTVAGIIALVIFVMFLLK' is a clear single-pass transmembrane domain, confirming a membrane protein. (2) The protein is very large (~1425 AA) with multiple repeated domain-like modules containing conserved aspartate clusters, consistent with C2 calcium-binding domains characteristic of the ferlin family, which are well-known mediators of vesicle trafficking and membrane fusion in secretory/endosomal pathways. (3) No N-terminal mitochondrial targeting presequence is present, arguing against mitochondrial inner membrane (A). (4) The protein's unusual amino acid composition (high lysine/arginine, low GC-biased residues) is characteristic of an AT-rich apicomplexan parasite genome, indicating it is a parasite's own protein rather than a host cell component, arguing against C. (5) The multi-domain architecture with a single-pass TM topology and C2-like trafficking domains is inconsistent with a simple external-side plasma membrane protein (B); ferlins are intracellular membrane-trafficking proteins. Together, these features point toward an endosomal/secretory membrane compartment (D) over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal TM domain, multi-domain architecture with C2-like motifs, absence of mitochondrial targeting, and parasite-specific sequence composition provide a transferable reasoning path from ferlin family biology and general cell biology to distinguish D from A, B, and C. While recognizing ferlin features in a divergent apicomplexan sequence is non-trivial, the combination of the clear TM domain, large multi-domain architecture, and elimination of the other three options via standard biological reasoning makes D the most defensible choice without requiring exact database lookup."
  },
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7J6JXB6, FER1_TOXGO) annotates this protein with GO:0010008 (endosome membrane) using IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment confirms localization to the trans-Golgi-endosome network in intracellular parasites, with the protein described as a single-pass membrane protein. While the protein also localizes to the trans-Golgi network membrane (IMP evidence) and cytoplasm, among the four offered choices, endosome membrane is the only one with direct experimental support. The answer D is consistent with the primary experimental annotation."
  },
  "important_caveats": [
    "The protein has dynamic localization: trans-Golgi-endosome network in intracellular parasites and cytoplasm in extracellular parasites. The 'primary' compartment is context-dependent, but among the four offered choices, endosome membrane is the best match.",
    "The trans-Golgi network membrane (GO:0032588, IMP evidence) is also annotated but is not offered as a choice, so it does not create ambiguity among the given options.",
    "Recognition of ferlin C2 domains in a divergent apicomplexan sequence is challenging; the reasoning relies on overall architecture and elimination of alternatives rather than precise domain identification.",
    "The 'host cell' option (C) could be superficially tempting for an intracellular parasite, but GO cellular component annotations for parasite proteins refer to the parasite's own compartments, not the host cell."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, A (mitochondrial inner membrane) is excluded by absence of targeting sequence; B (external side of plasma membrane) is inconsistent with the multi-domain intracellular trafficking architecture; C (host cell) is excluded because this is clearly a parasite-encoded protein, not a host component. D (endosome membrane) is the only option consistent with the ferlin-like trafficking role and single-pass membrane topology. The trans-Golgi network membrane, which is also annotated, is not among the choices, so no ambiguity arises between the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7J6JXB6, FER1_TOXGO) annotates this protein with GO:0010008 (endosome membrane) using IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment confirms localization to the trans-Golgi-endosome network in intracellular parasites, with the protein described as a single-pass membrane protein. While the protein also localizes to the trans-Golgi network membrane (IMP evidence) and cytoplasm, among the four offered choices, endosome membrane is the only one with direct experimental support. The answer D is consistent with the primary experimental annotation.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable sequence features allow a knowledgeable model to narrow the choices: (1) The C-terminal hydrophobic stretch 'WTGVWMTVAGIIALVIFVMFLLK' is a clear single-pass transmembrane domain, confirming a membrane protein. (2) The protein is very large (~1425 AA) with multiple repeated domain-like modules containing conserved aspartate clusters, consistent with C2 calcium-binding domains characteristic of the ferlin family, which are well-known mediators of vesicle trafficking and membrane fusion in secretory/endosomal pathways. (3) No N-terminal mitochondrial targeting presequence is present, arguing against mitochondrial inner membrane (A). (4) The protein's unusual amino acid composition (high lysine/arginine, low GC-biased residues) is characteristic of an AT-rich apicomplexan parasite genome, indicating it is a parasite's own protein rather than a host cell component, arguing against C. (5) The multi-domain architecture with a single-pass TM topology and C2-like trafficking domains is inconsistent with a simple external-side plasma membrane protein (B); ferlins are intracellular membrane-trafficking proteins. Together, these features point toward an endosomal/secretory membrane compartment (D) over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal TM domain, multi-domain architecture with C2-like motifs, absence of mitochondrial targeting, and parasite-specific sequence composition provide a transferable reasoning path from ferlin family biology and general cell biology to distinguish D from A, B, and C. While recognizing ferlin features in a divergent apicomplexan sequence is non-trivial, the combination of the clear TM domain, large multi-domain architecture, and elimination of the other three options via standard biological reasoning makes D the most defensible choice without requiring exact database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, A (mitochondrial inner membrane) is excluded by absence of targeting sequence; B (external side of plasma membrane) is inconsistent with the multi-domain intracellular trafficking architecture; C (host cell) is excluded because this is clearly a parasite-encoded protein, not a host component. D (endosome membrane) is the only option consistent with the ferlin-like trafficking role and single-pass membrane topology. The trans-Golgi network membrane, which is also annotated, is not among the choices, so no ambiguity arises between the offered alternatives."
  },
  "important_caveats": [
    "The protein has dynamic localization: trans-Golgi-endosome network in intracellular parasites and cytoplasm in extracellular parasites. The 'primary' compartment is context-dependent, but among the four offered choices, endosome membrane is the best match.",
    "The trans-Golgi network membrane (GO:0032588, IMP evidence) is also annotated but is not offered as a choice, so it does not create ambiguity among the given options.",
    "Recognition of ferlin C2 domains in a divergent apicomplexan sequence is challenging; the reasoning relies on overall architecture and elimination of alternatives rather than precise domain identification.",
    "The 'host cell' option (C) could be superficially tempting for an intracellular parasite, but GO cellular component annotations for parasite proteins refer to the parasite's own compartments, not the host cell."
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
  "benchmark_sequence_length": 1425,
  "benchmark_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2021-04-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1425,
  "current_source_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 14,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7J6JXB6",
  "selected_historical_entry_version": 14,
  "selected_historical_record_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "selected_historical_source_sequence_length": 1425,
  "selected_historical_source_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "selected_historical_version": {
    "accession": "A0A7J6JXB6",
    "database": "Swiss-Prot",
    "entryVersion": 14,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FER1_TOXGO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7J6JXB6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2021-04-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000557509\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"value\":\"Ferlin 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"value\":\"FER1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"TgFER1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"value\":\"In intracellular parasites localizes to the trans-Golgi-endosome network; upon egress disperses into the cytoplasm (PubMed:39294204). In extracellular parasites, localizes throughout the cytoplasm (PubMed:39294204)\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"id\":\"SL-0267\",\"value\":\"Golgi apparatus, trans-Golgi network membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9904\",\"value\":\"Single-pass membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"id\":\"SL-0100\",\"value\":\"Endosome membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9904\",\"value\":\"Single-pass membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"id\":\"GO:0010008\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endosome membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"id\":\"GO:0032588\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:trans-Golgi network membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Drozda A.A.\",\"Falco J.A.\",\"Bechtel T.J.\",\"Weerapana E.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33803212\"},{\"database\":\"DOI\",\"id\":\"10.3390/life11030217\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33803212\",\"journal\":\"Life\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Ribeiro E Silva A.\",\"Drozda A.A.\",\"Coppens I.\",\"Coleman B.I.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39294204\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-024-72628-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"21819\",\"id\":\"39294204\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"21819\",\"publicationDate\":\"2024\",\"title\":\"Toxoplasma FER1 is a versatile and dynamic mediator of differential microneme trafficking and microneme exocytosis.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"PUTATIVE CA(2+)-BINDING RESIDUES\",\"MUTAGENESIS OF ASP-541; ASP-545 AND ASP-605\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H1",
  "excerpt": "ID   FER1_TOXGO              Reviewed;        1425 AA.\nAC   A0A7J6JXB6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-APR-2021, sequence version 1.\nDT   28-JAN-2026, entry version 14.\nDE   RecName: Full=Ferlin 1 {ECO:0000303|PubMed:33803212, ECO:0000303|PubMed:39294204};\nDE            Short=FER1 {ECO:0000303|PubMed:33803212, ECO:0000303|PubMed:39294204};\nDE            Short=TgFER1 {ECO:0000303|PubMed:33803212};\nGN   ORFNames=TGRH88_049110 {ECO:0000312|EMBL:KAF4639140.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|Proteomes:UP000557509};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION.\nRC   STRAIN=RH {ECO:0000303|PubMed:33803212};\nRX   PubMed=33803212; DOI=10.3390/life11030217;\nRA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,\nRA   Gubbels M.J.;\nRT   \"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule\nRT   Secretion.\";\nRL   Life 11:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PUTATIVE\nRP   CA(2+)-BINDING RESIDUES, AND MUTAGENESIS OF ASP-541; ASP-545 AND ASP-605.\nRC   STRAIN=RH {ECO:0000303|PubMed:39294204};\nRX   PubMed=39294204; DOI=10.1038/s41598-024-72628-0;\nRA   Tagoe D.N.A., Ribeiro E Silva A., Drozda A.A., Coppens I., Coleman B.I.,\nRA   Gubbels M.J.;\nRT   \"Toxoplasma FER1 is a versatile and dynamic mediator of differential\nRT   microneme trafficking and microneme exocytosis.\";\nRL   Sci. Rep. 14:21819-21819(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Golgi apparatus, trans-Golgi network membrane\nCC       {ECO:0000269|PubMed:39294204}; Single-pass membrane protein\nCC       {ECO:0000255}. Endosome membrane {ECO:0000269|PubMed:39294204}; Single-\nCC       pass membrane protein {ECO:0000255}. Cytoplasm\nCC       {ECO:0000269|PubMed:39294204}. Note=In intracellular parasites\nCC       localizes to the trans-Golgi-endosome network; upon egress disperses\nCC       into the cytoplasm (PubMed:39294204). In extracellular parasites,\nCC       localizes throughout the cytoplasm (PubMed:39294204).\nCC       {ECO:0000269|PubMed:39294204}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0010008; C:endosome membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0032588; C:trans-Golgi network membrane; IMP:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14"
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
  "excerpt": "[Term]\nid: GO:0009897\nname: external side of plasma membrane\nnamespace: cellular_component\ndef: \"The leaflet of the plasma membrane that faces the extracellular side of the cell, including any protein embedded in, attached to, or peripherally associated with it.\" [GOC:dos, GOC:tb]\nsynonym: \"external leaflet of plasma membrane\" EXACT [GOC:ab]\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"outer surface of cytoplasmic membrane\" EXACT []\nis_a: GO:0098552 ! side of membrane\nrelationship: part_of GO:0005886 ! plasma membrane\nrelationship: part_of GO:0009986 ! cell surface\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009897",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 100773-100784",
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
  "excerpt": "[Term]\nid: GO:0010008\nname: endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an endosome.\" [GOC:mah]\nsynonym: \"endosomal membrane\" EXACT [NIF_Subcellular:sao978443756]\nxref: NIF_Subcellular:sao978443756\nis_a: GO:0030659 ! cytoplasmic vesicle membrane\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005768 ! endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101976-101986",
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
