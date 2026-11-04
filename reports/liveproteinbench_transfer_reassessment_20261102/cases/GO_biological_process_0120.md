# GO_biological_process_0120

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0120.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — exocytosis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMKLKEMVEAAEAKVESKPPQAAEEKAPDQAAGGAEEDVAAAPAEGGEGAEPLDQAEIEKMLFDESLGAQEYTYEEFLDLIDQPPEERGEAEDERKHWSYPRRWKVVLWNLQIQNYMDDNFSAFMEFEFGGTREECKVHKGTSVLIYATGQDKNYLRTPVIPDVSNAGPVDMHFRKAFEYRGSYLDLEREKLKIKVWEYRNWTLNHLEAVYEEALLNLATGETHVERDLYKFIKGRRSRRCRISFHLYFQELYDFELSFVKWRLVQIMPCLTLQEKIANRGKNKGGYTREATIGFKRHQLADQAKYVFQQRQVKREMQKRDSQRELLPGASRPEMLGGFADKGSARLSHLGFESAMKLPNRGTRSPSGLESNRPEDGNRNMEEIFLQHQATILASDQLEELPASLRPPLSKRRKGEDKKDGNKADGPQVKMTISLMHASSMNKGLGLVSSERPADGIPRWDNLGEIYFRGTLRDLDSTYIQVVVEDTTAPKVMRQIGYGQIPLRGVVDYSCLSTELGTPMWLALQAKMEGWGHELKEWCFGFVEGTVMVAHLPRYRQLGEVSESDSDRVYLILRIKDVDQIVTPDNRPVVDSYVEVSFDGTSRRTRTVRNTLNPVWDDEVTIPLRLPAFRDITESDVTRKGKVWLDVWGTGPGYVDHLGGCSFSLYEIFFNEKHNKRNLTAMQRIDLEANTRQSYETRVFSTSRRLAFIHKADRPSTIQFEAWTCPDILEVSGIDKLPEPERITTTSNFPRALRNTYERLKRMYAEVIEKKGLVNPDTGVGPPRFFDVEFLDQRKETHYAPTMVTRIRPPFGVDSESSVFHYCRCVPFAVKRENLVFTPEFAVQIRSGNAMDHSILMTSLLLGLPAFAFVCVGTLWDKHMHAWVATFHYDDDRACGVVKFWETTTGLVYTLKHRFRDPYTLQRLSADPEFGILKMMNIQRRKRLSILGVSVDADTPDYISRSGEDLVQSEFPTGGAKLPYRSLDIMFNNRNVWLNIQDGNPAKVWFDIWDVEQWYQFSPGLHDVPPCFIVRGFGAKVAEWQFDRAAQEIQGKVLSDITAFRATRNLPTKWNRDDVLDAFLQMGLELLHQAATARDEDFQLARLKLEDWKKAFYSKVPCSYRVRGAPLHFNTYDSKTISDAIIANVDFVESRDRSAFFSLAVMLYNLPGELVSTYVYICVTQKVTERERRRILAQKEKQSREDAQRKARKQRRKAGHEGADNGAEDKQGAEGNEEEHGDAAAAAVAEESVSAEAVQGAEEPKKVVKKGAVPRVKKRSYEQVEGTEVAAIAIERDFFTEAEAPDFKNLMTDVEHAINTHLGLSPGRVRAFQARYAEKRIVFAVGPPMDDATEADAVSSVALMEKLRDILPSMAHEEGRFQEVTGGGATLQWDGPGTNILDRIAQEQATAGEGEQQTSEGIPTRDMQVDGTAVLEEAGEKSDKKKKKKEKKEKKEKKEKKEKKEKKEKKKKKGGETAAEPEEASAVLAPPPVPAPAAAIPSVLLPTDSEDGEKEKPKEKKKEKKEKKKKKDGETDAEPDEASAVLAPPPVPVPAAAIPSILLPADGEDGEEEKPKEKKTEKKKEKHTEKKHKKKSETLPESETTAVVTVTPGEEDETSPLVPVPSSIASSEAPEPPASTRVTPAPEPKAKPGLSMGAALLAVRARSRLQRKHLAQQLSSSSSSEVSASSASSLSPSSSSSSDFAETRAKADALRARLQAAQARLAAARETEVSSSETESSETSEASFLSSDGEWDALWQSQRAAAMERQQRLQKMVSGVKAAYRRLEEENTRLAATRRRDDKLQRQVEAERERAVELLKEATRRAKEEKDLIARQPPPARDWSDTVVLSTPQIFVNSQAACAPFADSGRDEGERDEWYEVSDACSRRAESSNESRTTAGAKLRQQQLDLAGRT

[Multiple Choices]
A. exocytosis
B. fatty acid biosynthetic process
C. aggresome assembly
D. regulation of DNA replication
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

> The sequence-matched historical entry reports regulation of microneme secretion and describes possible regulation of rhoptry and dense-granule secretion. These experimentally supported secretion functions are consistent with exocytosis; the entry also directly annotates exocytosis, though that GO annotation is IEA.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has features consistent with a multi-C2-domain membrane-associated protein. C2 domains commonly support membrane interaction and vesicle-secretion machinery, making exocytosis a credible choice over fatty-acid biosynthesis, aggresome assembly, or DNA-replication regulation. This is a family-level inference, not a definitive functional assignment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about C2-domain proteins and vesicle secretion provides a meaningful basis for preferring A among these alternatives, even though sequence alone does not establish the precise secretion role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other choices are not comparably supported by the sequence features or the inferred vesicle-secretion role.


### Important caveats

- The exocytosis GO annotation in the historical record is IEA; the record separately reports experimental evidence for secretion-related functions.
- The exact family or secretion role cannot be established from sequence inspection alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has features consistent with a multi-C2-domain membrane-associated protein. C2 domains commonly support membrane interaction and vesicle-secretion machinery, making exocytosis a credible choice over fatty-acid biosynthesis, aggresome assembly, or DNA-replication regulation. This is a family-level inference, not a definitive functional assignment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about C2-domain proteins and vesicle secretion provides a meaningful basis for preferring A among these alternatives, even though sequence alone does not establish the precise secretion role."
  },
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical entry reports regulation of microneme secretion and describes possible regulation of rhoptry and dense-granule secretion. These experimentally supported secretion functions are consistent with exocytosis; the entry also directly annotates exocytosis, though that GO annotation is IEA."
  },
  "important_caveats": [
    "The exocytosis GO annotation in the historical record is IEA; the record separately reports experimental evidence for secretion-related functions.",
    "The exact family or secretion role cannot be established from sequence inspection alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other choices are not comparably supported by the sequence features or the inferred vesicle-secretion role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical entry reports regulation of microneme secretion and describes possible regulation of rhoptry and dense-granule secretion. These experimentally supported secretion functions are consistent with exocytosis; the entry also directly annotates exocytosis, though that GO annotation is IEA.",
    "evidence_ids": ["H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has features consistent with a multi-C2-domain membrane-associated protein. C2 domains commonly support membrane interaction and vesicle-secretion machinery, making exocytosis a credible choice over fatty-acid biosynthesis, aggresome assembly, or DNA-replication regulation. This is a family-level inference, not a definitive functional assignment.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about C2-domain proteins and vesicle secretion provides a meaningful basis for preferring A among these alternatives, even though sequence alone does not establish the precise secretion role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other choices are not comparably supported by the sequence features or the inferred vesicle-secretion role."
  },
  "important_caveats": [
    "The exocytosis GO annotation in the historical record is IEA; the record separately reports experimental evidence for secretion-related functions.",
    "The exact family or secretion role cannot be established from sequence inspection alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is TgDOC2 (C2 domain-containing protein) from Toxoplasma gondii. The UniProt FUNCTION comment states it 'Regulates microneme secretion' and is 'Probably involved in regulation of rhoptry and dense granule secretion,' supported by direct assay evidence (ECO:0000269) from two PubMed papers. The key reference (Farrell et al., Science 2012) is titled 'A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.' The GO annotation GO:0006887 (exocytosis) is present, though assigned via IEA:UniProtKB-KW. The underlying experimental evidence directly supports exocytosis as the biological process. Microneme, rhoptry, and dense granule secretion are all vesicle-fusion events fitting the GO exocytosis definition.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple C2 domain motifs (aspartate-rich loops flanked by beta-strand regions with conserved Phe residues), characteristic of the DOC2 (Double C2 domain) protein family. In well-studied mammalian homologs (DOC2A, DOC2B), these proteins function as calcium sensors that promote SNARE-mediated vesicle fusion and neurotransmitter release — a canonical exocytosis role. The C2 domain superfamily broadly associates with calcium-dependent membrane trafficking and exocytosis (synaptotagmin, PKC, Munc13, DOC2), not with fatty acid synthesis (which requires acyltransferase/ketoacyl-synthase domains), aggresome assembly (which requires chaperone/motor domains like HSP70, dynein, HDAC6), or DNA replication regulation (which requires DNA-binding, helicase, or replication-fork-associated motifs). The coiled-coil heptad-repeat regions in the C-terminal half are consistent with protein-protein interaction modules in secretion machinery. Recognizing the C2 domain architecture and the DOC2 family's established exocytosis role in other organisms provides a concrete, transferable inference that meaningfully distinguishes option A from the other three.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify C2 domain features in the sequence and recall that the DOC2 family (and C2 domains generally) are calcium sensors for regulated exocytosis, as demonstrated in mammalian synaptotagmin and DOC2A/B. This family-level knowledge, combined with the absence of any motifs associated with fatty acid synthesis, aggresome assembly, or DNA replication, meaningfully distinguishes exocytosis as the answer without requiring the specific Toxoplasma annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct biological processes (secretion, lipid metabolism, protein-aggregate handling, DNA replication control). The C2/DOC2 domain architecture unambiguously points to exocytosis and is inconsistent with the other three processes. No alternative option is defensible given the domain content.


### Important caveats

- The GO:0006887 exocytosis annotation carries IEA:UniProtKB-KW evidence code (electronic), but the underlying FUNCTION statement is supported by direct assay data (ECO:0000269) from two independent studies.
- The protein is from Toxoplasma gondii (an apicomplexan parasite); its exocytosis involves microneme/rhoptry/dense granule secretion, which are parasite-specific organelle discharge events but still qualify as exocytosis per the GO definition.
- The C2 domain recognition from raw sequence is approximate; definitive domain boundaries require structural or HMM analysis, but the aspartate-rich clusters and overall domain architecture are recognizable.
- The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple C2 domain motifs (aspartate-rich loops flanked by beta-strand regions with conserved Phe residues), characteristic of the DOC2 (Double C2 domain) protein family. In well-studied mammalian homologs (DOC2A, DOC2B), these proteins function as calcium sensors that promote SNARE-mediated vesicle fusion and neurotransmitter release — a canonical exocytosis role. The C2 domain superfamily broadly associates with calcium-dependent membrane trafficking and exocytosis (synaptotagmin, PKC, Munc13, DOC2), not with fatty acid synthesis (which requires acyltransferase/ketoacyl-synthase domains), aggresome assembly (which requires chaperone/motor domains like HSP70, dynein, HDAC6), or DNA replication regulation (which requires DNA-binding, helicase, or replication-fork-associated motifs). The coiled-coil heptad-repeat regions in the C-terminal half are consistent with protein-protein interaction modules in secretion machinery. Recognizing the C2 domain architecture and the DOC2 family's established exocytosis role in other organisms provides a concrete, transferable inference that meaningfully distinguishes option A from the other three.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify C2 domain features in the sequence and recall that the DOC2 family (and C2 domains generally) are calcium sensors for regulated exocytosis, as demonstrated in mammalian synaptotagmin and DOC2A/B. This family-level knowledge, combined with the absence of any motifs associated with fatty acid synthesis, aggresome assembly, or DNA replication, meaningfully distinguishes exocytosis as the answer without requiring the specific Toxoplasma annotation."
  },
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is TgDOC2 (C2 domain-containing protein) from Toxoplasma gondii. The UniProt FUNCTION comment states it 'Regulates microneme secretion' and is 'Probably involved in regulation of rhoptry and dense granule secretion,' supported by direct assay evidence (ECO:0000269) from two PubMed papers. The key reference (Farrell et al., Science 2012) is titled 'A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.' The GO annotation GO:0006887 (exocytosis) is present, though assigned via IEA:UniProtKB-KW. The underlying experimental evidence directly supports exocytosis as the biological process. Microneme, rhoptry, and dense granule secretion are all vesicle-fusion events fitting the GO exocytosis definition."
  },
  "important_caveats": [
    "The GO:0006887 exocytosis annotation carries IEA:UniProtKB-KW evidence code (electronic), but the underlying FUNCTION statement is supported by direct assay data (ECO:0000269) from two independent studies.",
    "The protein is from Toxoplasma gondii (an apicomplexan parasite); its exocytosis involves microneme/rhoptry/dense granule secretion, which are parasite-specific organelle discharge events but still qualify as exocytosis per the GO definition.",
    "The C2 domain recognition from raw sequence is approximate; definitive domain boundaries require structural or HMM analysis, but the aspartate-rich clusters and overall domain architecture are recognizable.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological processes (secretion, lipid metabolism, protein-aggregate handling, DNA replication control). The C2/DOC2 domain architecture unambiguously points to exocytosis and is inconsistent with the other three processes. No alternative option is defensible given the domain content."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is TgDOC2 (C2 domain-containing protein) from Toxoplasma gondii. The UniProt FUNCTION comment states it 'Regulates microneme secretion' and is 'Probably involved in regulation of rhoptry and dense granule secretion,' supported by direct assay evidence (ECO:0000269) from two PubMed papers. The key reference (Farrell et al., Science 2012) is titled 'A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.' The GO annotation GO:0006887 (exocytosis) is present, though assigned via IEA:UniProtKB-KW. The underlying experimental evidence directly supports exocytosis as the biological process. Microneme, rhoptry, and dense granule secretion are all vesicle-fusion events fitting the GO exocytosis definition.",
    "evidence_ids": ["C5", "C6", "C8", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple C2 domain motifs (aspartate-rich loops flanked by beta-strand regions with conserved Phe residues), characteristic of the DOC2 (Double C2 domain) protein family. In well-studied mammalian homologs (DOC2A, DOC2B), these proteins function as calcium sensors that promote SNARE-mediated vesicle fusion and neurotransmitter release — a canonical exocytosis role. The C2 domain superfamily broadly associates with calcium-dependent membrane trafficking and exocytosis (synaptotagmin, PKC, Munc13, DOC2), not with fatty acid synthesis (which requires acyltransferase/ketoacyl-synthase domains), aggresome assembly (which requires chaperone/motor domains like HSP70, dynein, HDAC6), or DNA replication regulation (which requires DNA-binding, helicase, or replication-fork-associated motifs). The coiled-coil heptad-repeat regions in the C-terminal half are consistent with protein-protein interaction modules in secretion machinery. Recognizing the C2 domain architecture and the DOC2 family's established exocytosis role in other organisms provides a concrete, transferable inference that meaningfully distinguishes option A from the other three.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify C2 domain features in the sequence and recall that the DOC2 family (and C2 domains generally) are calcium sensors for regulated exocytosis, as demonstrated in mammalian synaptotagmin and DOC2A/B. This family-level knowledge, combined with the absence of any motifs associated with fatty acid synthesis, aggresome assembly, or DNA replication, meaningfully distinguishes exocytosis as the answer without requiring the specific Toxoplasma annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological processes (secretion, lipid metabolism, protein-aggregate handling, DNA replication control). The C2/DOC2 domain architecture unambiguously points to exocytosis and is inconsistent with the other three processes. No alternative option is defensible given the domain content."
  },
  "important_caveats": [
    "The GO:0006887 exocytosis annotation carries IEA:UniProtKB-KW evidence code (electronic), but the underlying FUNCTION statement is supported by direct assay data (ECO:0000269) from two independent studies.",
    "The protein is from Toxoplasma gondii (an apicomplexan parasite); its exocytosis involves microneme/rhoptry/dense granule secretion, which are parasite-specific organelle discharge events but still qualify as exocytosis per the GO definition.",
    "The C2 domain recognition from raw sequence is approximate; definitive domain boundaries require structural or HMM analysis, but the aspartate-rich clusters and overall domain architecture are recognizable.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge."
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
  "benchmark_sequence_length": 1910,
  "benchmark_sequence_sha256": "52c3fcbc01722e2bc4c9cc5fb0e191cb1c82c226125de77539c5eeb917ffb776",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-04-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1910,
  "current_source_sequence_sha256": "52c3fcbc01722e2bc4c9cc5fb0e191cb1c82c226125de77539c5eeb917ffb776",
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
  "requested_accession": "A0A7J6K9S4",
  "selected_historical_entry_version": 14,
  "selected_historical_record_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "selected_historical_source_sequence_length": 1910,
  "selected_historical_source_sequence_sha256": "52c3fcbc01722e2bc4c9cc5fb0e191cb1c82c226125de77539c5eeb917ffb776",
  "selected_historical_version": {
    "accession": "A0A7J6K9S4",
    "database": "Swiss-Prot",
    "entryVersion": 14,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DOC2_TOXGO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7J6K9S4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-04-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000557509\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"C2 domain-containing protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30564214\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"TgDOC2\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22246776\",\"source\":\"PubMed\"}],\"value\":\"TgDOC2.1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22246776\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"Regulates microneme secretion (PubMed:22246776, PubMed:33803212). Probably involved in regulation of rhoptry and dense granule secretion (PubMed:33803212)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Farrell A.\",\"Thirugnanam S.\",\"Lorestani A.\",\"Dvorin J.D.\",\"Eidell K.P.\",\"Ferguson D.J.\",\"Anderson-White B.R.\",\"Duraisingh M.T.\",\"Marth G.T.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22246776\"},{\"database\":\"DOI\",\"id\":\"10.1126/science.1210829\"}],\"citationType\":\"journal article\",\"firstPage\":\"218\",\"id\":\"22246776\",\"journal\":\"Science\",\"lastPage\":\"221\",\"publicationDate\":\"2012\",\"title\":\"A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.\",\"volume\":\"335\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"MUTAGENESIS OF PHE-124\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang N.Z.\",\"Gao Q.\",\"Wang M.\",\"Hou J.L.\",\"Zhang F.K.\",\"Hu L.Y.\",\"Zhu X.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30564214\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2018.02965\"}],\"citationType\":\"journal article\",\"firstPage\":\"2965\",\"id\":\"30564214\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"2965\",\"publicationDate\":\"2018\",\"title\":\"Protective Efficacy Against Acute and Chronic Toxoplasma gondii Infection Induced by Immunization With the DNA Vaccine TgDOC2C.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"VACCINE CANDIDATE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Drozda A.A.\",\"Falco J.A.\",\"Bechtel T.J.\",\"Weerapana E.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33803212\"},{\"database\":\"DOI\",\"id\":\"10.3390/life11030217\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33803212\",\"journal\":\"Life\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:25:41.523865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H1",
  "excerpt": "ID   DOC2_TOXGO              Reviewed;        1910 AA.\nAC   A0A7J6K9S4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-APR-2021, sequence version 1.\nDT   28-JAN-2026, entry version 14.\nDE   RecName: Full=C2 domain-containing protein {ECO:0000305};\nDE            Short=TgDOC2 {ECO:0000303|PubMed:30564214, ECO:0000303|PubMed:33803212};\nDE            Short=TgDOC2.1 {ECO:0000303|PubMed:22246776};\nGN   ORFNames=TGRH88_030250 {ECO:0000312|EMBL:KAF4643359.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|Proteomes:UP000557509};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND MUTAGENESIS OF PHE-124.\nRX   PubMed=22246776; DOI=10.1126/science.1210829;\nRA   Farrell A., Thirugnanam S., Lorestani A., Dvorin J.D., Eidell K.P.,\nRA   Ferguson D.J., Anderson-White B.R., Duraisingh M.T., Marth G.T.,\nRA   Gubbels M.J.;\nRT   \"A DOC2 protein identified by mutational profiling is essential for\nRT   apicomplexan parasite exocytosis.\";\nRL   Science 335:218-221(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   VACCINE CANDIDATE.\nRX   PubMed=30564214; DOI=10.3389/fmicb.2018.02965;\nRA   Zhang N.Z., Gao Q., Wang M., Hou J.L., Zhang F.K., Hu L.Y., Zhu X.Q.;\nRT   \"Protective Efficacy Against Acute and Chronic Toxoplasma gondii Infection\nRT   Induced by Immunization With the DNA Vaccine TgDOC2C.\";\nRL   Front. Microbiol. 9:2965-2965(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION.\nRC   STRAIN=RH {ECO:0000303|PubMed:33803212};\nRX   PubMed=33803212; DOI=10.3390/life11030217;\nRA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,\nRA   Gubbels M.J.;\nRT   \"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule\nRT   Secretion.\";\nRL   Life 11:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Regulates microneme secretion (PubMed:22246776,\nCC       PubMed:33803212). Probably involved in regulation of rhoptry and dense\nCC       granule secretion (PubMed:33803212). {ECO:0000269|PubMed:22246776,\nCC       ECO:0000269|PubMed:33803212}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)

```json
{
  "entry_version": 14,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0006887; P:exocytosis; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:43.566279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702",
  "url": "https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006275\nname: regulation of DNA replication\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of DNA replication.\" [GOC:curators]\nis_a: GO:0051052 ! regulation of DNA metabolic process\nrelationship: regulates GO:0006260 ! DNA replication\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006275",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 64693-64700",
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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0006887\nname: exocytosis\nnamespace: biological_process\nalt_id: GO:0016194\nalt_id: GO:0016195\ndef: \"A process of secretion by a cell that results in the release of intracellular molecules (e.g. hormones, matrix proteins) contained within a membrane-bounded vesicle. Exocytosis can occur either by full fusion, when the vesicle collapses into the plasma membrane, or by a kiss-and-run mechanism that involves the formation of a transient contact, a pore, between a granule (for example of chromaffin cells) and the plasma membrane. The latter process most of the time leads to only partial secretion of the granule content. Exocytosis begins with steps that prepare vesicles for fusion with the membrane (tethering and docking) and ends when molecules are secreted from the cell.\" [GOC:mah, ISBN:0716731363, PMID:22323285]\nsubset: goslim_yeast\nsynonym: \"nonselective vesicle exocytosis\" RELATED []\nsynonym: \"vesicle exocytosis\" EXACT []\nxref: Wikipedia:Exocytosis\nis_a: GO:0016192 ! vesicle-mediated transport\nis_a: GO:0032940 ! secretion by cell\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006887",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 71255-71268",
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
  "excerpt": "[Term]\nid: GO:0070842\nname: aggresome assembly\nnamespace: biological_process\ndef: \"The aggregation, arrangement and bonding together of a set of components to form an aggresome; requires the microtubule cytoskeleton and dynein.\" [GOC:BHF, GOC:rl, PMID:14675537]\nis_a: GO:0070841 ! inclusion body assembly\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070842",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 371574-371580",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
