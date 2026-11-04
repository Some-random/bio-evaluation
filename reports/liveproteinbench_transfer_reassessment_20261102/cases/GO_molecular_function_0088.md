# GO_molecular_function_0088

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0088.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — 2-oxoglutarate-dependent dioxygenase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | uncertain | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVVSKDNNKRRRKETETPPPPPPVPPAGSSLAPPSAVAAIESSPEMPKRTKVQAQRKFAQGQSAPSSSSSIAYSAAAAAAGSGSGPSTSGADSNQPPIEILPNKCPKPQDFLTFLCFRGTRALPAHLDFLNQGKSKDSEASSTGANNNNNARKPNNSRASLAGNKKKRGRPAKGATKKVDVVAPIPDPTEKPSTAEKPASDKNNLIAAEAPKIPSRNPTPVLPGAVRKRAEVVTDGNRRGARGRGAGISHDKTTPAALSKDNKRRSNRASTKESKPVIDDDNSEDLDEQEADDDEDEFFSAHDATSRNGEEVKADSPVKAEPTKRGRPSAAKKAVEPAPEGQTVLKDKAPVKRVRQRESPIFIPSPESSGRMTRQRAFFEPVKVPPHKEEPGAHDPPKDEPKKQPETPPSKTEKEQEPTKQIKEAKEKTNSSIYAKEAKQQLENGDSLHGAVAKGKKSLNVFDFSSDDEQPLAKSIKLKKGAKGASPKKGGAAPIAPAARNRKAAAKKLDKEKEIEKEKQREKEEEIERDKAKEKKDKEKEKEKEKHPVPESKVEEPPSGGKRGKAGKKKAEDAPADEEDLAPPSSKKVATNARGSRKSAKSKASEDSAELEPQRSQRPSRKTKEAAAIYMGIIGHKLQLADDEEDDLSMSSFPDIPNVKEMEKMENEIKRNAAGKLNVPEASTVLSAGKSTRKPSPRPKDSPVTAPVEATRNESPSPPEAEEEKPPPPARRGRPPKQNKVNAGPAHKPRIEGMLVKKGSLAKMSEQQAKPKAKSEHSKVDSDEEEDFLINEELNETKRKLEKSFSDSDDEPLAIKVPAVAVKEKELLPPKMASPPPKLVPVPSPISVPTPAVSVAPSLAVPSILPTSTGTTQLTMLPLTAKATSSLGSMPMFPSIQASYSPLKTMEKKPPVPTSKILNVPATYALPGSASGAVSFQKTSSYLPQASPHYHSGYVRPPPTPTHQFGGGAPSGSKTPSQGSSPLKYQTPPTTYPPPIEAYQCPKINPNFLTPKYERSPLPRSSTSSFPSPSPVKFQPTSGTTATTVGTPSSATKSPLAPPPPSPPVSQVVIQTSSLNLSMSIAATVNAAPMPVASTSAAAAHQTTVATTVTATSTPPPAHSNSAATGGGAGANSDPLKDEIGSILAQATLMPSKEESGKIFGIASVSLAQSSGPDNTKCTLGKCGSIHKPVLGPVVPTEGYFGDQLSSKERRKAKVNMTHEQIQKWLIECSSNPDEIQDDLDDDFDDSLRPQQSTTPPPTRDDKELSASFSSSSKNTRGDLGKSESAWSAKGPSLKATPVLVTPPNRKELHEQADSKDCDALDYDKSSTPVNLTQKITSNESLAVEKKVNDRKGKESAKAAASKAATQPRSTAATPPTPISSTPTPASLTPSKSSPTPPPAVKQKAEKGKRNATAGGGATALASPPAAPTPANPKRTPVYNQKNAKAQQQQAETKPASNPPSGAGTKRESVYAFGKDDESGSKSGNRRRTDPSPVPAPALVPNALSERSPTKKRAAAAAAATAVQLTLSPTENCKIEGKPSKAPTGRGAKKQQQQAPAPPAPPVEASGDSDAEGATFYIPLQGAGVGGSGDGGIQGVAVKLGREGPDGPNQKVVMQATLVTKAQMDTNSKPLPESLNTNELVKTLLHAASNDAASTTTSLKSLPKASTSAAAGAAAAPGASSLVRVNSNSSLFSGSAKSRTAAQTSSTAAAVAKKYKDDTPIKMANNTAFPRHDDPTQMVEAPIFRPTEKEFADPIEFIERITPIAARFGICKIIPPASFKPECRISDEMRFTAYNQYVHKMLHRWGPSAKELSAIKKYLATQSIVMNHPPWIGGMEVDLPRLYHTVQELGGLKEVIEKKKWARVAEEMCIPKLAQDRVTKLDDIYCKYLLPYDTLSPAERQKLFDEVEADWAKREARARRNADRFVNTESVSNEEDDLSSDEDEESEEEIDGVSMECIVKGRSMPLSQFYRIARNTMALWFKSTDPTVNEVEAEFWRHVAVRDSHVCVHSGSIDSSGWGYGFPSPGPKGKGSNYARHPWNLKVLTNNSGSVLRSLGPVMGVTVPTLHVGMLFSACCWYRDPHGLSWIEYLHTGASKLWYGIPDDQSANFRAALTSLIPTHCQNKTIWLPCDTVMVPPHMLTDRGVSLCRIEQKPGEFIVVFPRAYTSSLATGYVVSESVYFATMSWLDLAKDDFRDIHESCEPAMFSLEQLLFALGYDQRVNSEALHQMLPMLNDVCEKESAAREQLRAAGVTSTEKVQAEKGQKAKKQQQPPYKSIESECDLCRANLYISMVRTEDGNIYCLQHALKNLNNGNIQAKQCKLIYAYNVDDIQQLIRQLQEKINHKAAVKKK

[Multiple Choices]
A. metalloendopeptidase activity
B. manganese ion transmembrane transporter activity
C. phosphatase activity
D. 2-oxoglutarate-dependent dioxygenase activity
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

### Expected-answer support: uncertain

> The matched-sequence evidence describes a JmjC-containing protein and reports regulatory and chromatin-related functions, but it does not establish 2-oxoglutarate-dependent dioxygenase activity or rule it out. A JmjC domain alone does not prove catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a JmjC-like region. Transferable knowledge associates JmjC domains with Fe(II)/2-oxoglutarate-dependent dioxygenases, which meaningfully favors D over the offered protease, transporter, and phosphatase choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The domain-family association supplies a concrete basis for choosing among these alternatives. It is probabilistic rather than conclusive: a JmjC-containing protein need not retain dioxygenase activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The JmjC-like region favors D among the choices, although the alternatives do not include the regulatory and chromatin-related functions reported in the evidence.


### Important caveats

- The supplied evidence does not provide a direct assay of dioxygenase activity.
- A JmjC-like domain can be present in a catalytically inactive protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a JmjC-like region. Transferable knowledge associates JmjC domains with Fe(II)/2-oxoglutarate-dependent dioxygenases, which meaningfully favors D over the offered protease, transporter, and phosphatase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The domain-family association supplies a concrete basis for choosing among these alternatives. It is probabilistic rather than conclusive: a JmjC-containing protein need not retain dioxygenase activity."
  },
  "case_id": "GO_molecular_function_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "cannot_determine",
    "reason": "The matched-sequence evidence describes a JmjC-containing protein and reports regulatory and chromatin-related functions, but it does not establish 2-oxoglutarate-dependent dioxygenase activity or rule it out. A JmjC domain alone does not prove catalytic activity."
  },
  "important_caveats": [
    "The supplied evidence does not provide a direct assay of dioxygenase activity.",
    "A JmjC-like domain can be present in a catalytically inactive protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The JmjC-like region favors D among the choices, although the alternatives do not include the regulatory and chromatin-related functions reported in the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0088",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The matched-sequence evidence describes a JmjC-containing protein and reports regulatory and chromatin-related functions, but it does not establish 2-oxoglutarate-dependent dioxygenase activity or rule it out. A JmjC domain alone does not prove catalytic activity.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a JmjC-like region. Transferable knowledge associates JmjC domains with Fe(II)/2-oxoglutarate-dependent dioxygenases, which meaningfully favors D over the offered protease, transporter, and phosphatase choices.",
    "missing_item_specific_fact": "",
    "reason": "The domain-family association supplies a concrete basis for choosing among these alternatives. It is probabilistic rather than conclusive: a JmjC-containing protein need not retain dioxygenase activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The JmjC-like region favors D among the choices, although the alternatives do not include the regulatory and chromatin-related functions reported in the evidence."
  },
  "important_caveats": [
    "The supplied evidence does not provide a direct assay of dioxygenase activity.",
    "A JmjC-like domain can be present in a catalytically inactive protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry for Q9VT00 (Jarid2/Jumonji, AT rich interactive domain protein 2) does NOT annotate GO:0016706 (2-oxoglutarate-dependent dioxygenase activity). The annotated molecular functions are GO:0003677 (DNA binding, IEA:InterPro) and GO:0044877 (protein-containing complex binding, IDA:FlyBase). The FUNCTION comment describes Jarid2 as a 'Regulator of histone methyltransferase complexes' and 'Accessory component of PRC2' — not a catalytic enzyme. Jarid2 is a well-established catalytically inactive member of the JmjC family: it lacks the conserved HxD…H catalytic triad required for iron coordination and 2-oxoglutarate-dependent demethylase/dioxygenase activity. The evidence directly contradicts the assignment of 2-oxoglutarate-dependent dioxygenase activity to this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a recognizable JmjC (Jumonji C) domain, identifiable by its characteristic fold and partial motif remnants (e.g., the HxSGSIDSS…H region and the downstream conserved cysteine/histidine clusters). Family-level knowledge from OTHER JmjC proteins (JMJD1A, JMJD2A, PHF8, TET enzymes, etc.) strongly associates the JmjC domain with 2-oxoglutarate-dependent dioxygenase (histone demethylase) activity. None of the other options match any sequence feature: (A) metalloendopeptidase requires a zinc-binding HExxH or similar motif absent here; (B) manganese transmembrane transporter requires multiple transmembrane helices, which this largely disordered/nuclear protein lacks; (C) phosphatase requires a catalytic motif (e.g., HCX5R for cysteine phosphatases or DXDXT/V for serine phosphatases) not present. Thus the JmjC domain provides a concrete family-level inference that meaningfully distinguishes D from A, B, and C. However, a model with specific knowledge of Jarid2 would recognize that this particular JmjC member is catalytically inactive, creating tension with the family-level prediction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The JmjC domain in the sequence is a transferable family feature that links to 2-oxoglutarate-dependent dioxygenase activity via well-characterized homologs (JMJD, PHF, TET families). This distinguishes D from the three other options, none of which have any supporting sequence motif. The inference is a legitimate family-level generalization, though it leads to an answer that is contradicted for this specific catalytically-inactive protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, the JmjC domain clearly points toward D over A, B, and C. However, the true molecular functions of Jarid2 (DNA binding, protein-containing complex binding) are not offered as options, making the question somewhat artificial. No two offered choices are equally defensible given the sequence features.


### Important caveats

- The expected answer D (2-oxoglutarate-dependent dioxygenase activity) is contradicted by the UniProt annotation and the well-established literature that Jarid2 is a catalytically inactive JmjC protein lacking the HxD…H catalytic triad.
- The correct molecular function annotations (DNA binding, protein-containing complex binding) are not among the offered choices, making the question structurally flawed.
- The JmjC domain is present in the sequence, so family-level reasoning would lead a model to choose D, but this family-level inference is incorrect for this specific protein.
- The UniProt function annotation is partially based on similarity to human Q92833 (Jarid2), but even the human ortholog is catalytically inactive; the annotation correctly describes Jarid2 as a regulator/accessory subunit, not a catalytic dioxygenase.
- The GO:0016706 term definition (from GO3) describes catalysis of a specific redox reaction, which Jarid2 does not perform.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a recognizable JmjC (Jumonji C) domain, identifiable by its characteristic fold and partial motif remnants (e.g., the HxSGSIDSS…H region and the downstream conserved cysteine/histidine clusters). Family-level knowledge from OTHER JmjC proteins (JMJD1A, JMJD2A, PHF8, TET enzymes, etc.) strongly associates the JmjC domain with 2-oxoglutarate-dependent dioxygenase (histone demethylase) activity. None of the other options match any sequence feature: (A) metalloendopeptidase requires a zinc-binding HExxH or similar motif absent here; (B) manganese transmembrane transporter requires multiple transmembrane helices, which this largely disordered/nuclear protein lacks; (C) phosphatase requires a catalytic motif (e.g., HCX5R for cysteine phosphatases or DXDXT/V for serine phosphatases) not present. Thus the JmjC domain provides a concrete family-level inference that meaningfully distinguishes D from A, B, and C. However, a model with specific knowledge of Jarid2 would recognize that this particular JmjC member is catalytically inactive, creating tension with the family-level prediction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The JmjC domain in the sequence is a transferable family feature that links to 2-oxoglutarate-dependent dioxygenase activity via well-characterized homologs (JMJD, PHF, TET families). This distinguishes D from the three other options, none of which have any supporting sequence motif. The inference is a legitimate family-level generalization, though it leads to an answer that is contradicted for this specific catalytically-inactive protein."
  },
  "case_id": "GO_molecular_function_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry for Q9VT00 (Jarid2/Jumonji, AT rich interactive domain protein 2) does NOT annotate GO:0016706 (2-oxoglutarate-dependent dioxygenase activity). The annotated molecular functions are GO:0003677 (DNA binding, IEA:InterPro) and GO:0044877 (protein-containing complex binding, IDA:FlyBase). The FUNCTION comment describes Jarid2 as a 'Regulator of histone methyltransferase complexes' and 'Accessory component of PRC2' — not a catalytic enzyme. Jarid2 is a well-established catalytically inactive member of the JmjC family: it lacks the conserved HxD…H catalytic triad required for iron coordination and 2-oxoglutarate-dependent demethylase/dioxygenase activity. The evidence directly contradicts the assignment of 2-oxoglutarate-dependent dioxygenase activity to this protein."
  },
  "important_caveats": [
    "The expected answer D (2-oxoglutarate-dependent dioxygenase activity) is contradicted by the UniProt annotation and the well-established literature that Jarid2 is a catalytically inactive JmjC protein lacking the HxD…H catalytic triad.",
    "The correct molecular function annotations (DNA binding, protein-containing complex binding) are not among the offered choices, making the question structurally flawed.",
    "The JmjC domain is present in the sequence, so family-level reasoning would lead a model to choose D, but this family-level inference is incorrect for this specific protein.",
    "The UniProt function annotation is partially based on similarity to human Q92833 (Jarid2), but even the human ortholog is catalytically inactive; the annotation correctly describes Jarid2 as a regulator/accessory subunit, not a catalytic dioxygenase.",
    "The GO:0016706 term definition (from GO3) describes catalysis of a specific redox reaction, which Jarid2 does not perform."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, the JmjC domain clearly points toward D over A, B, and C. However, the true molecular functions of Jarid2 (DNA binding, protein-containing complex binding) are not offered as options, making the question somewhat artificial. No two offered choices are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0088",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry for Q9VT00 (Jarid2/Jumonji, AT rich interactive domain protein 2) does NOT annotate GO:0016706 (2-oxoglutarate-dependent dioxygenase activity). The annotated molecular functions are GO:0003677 (DNA binding, IEA:InterPro) and GO:0044877 (protein-containing complex binding, IDA:FlyBase). The FUNCTION comment describes Jarid2 as a 'Regulator of histone methyltransferase complexes' and 'Accessory component of PRC2' — not a catalytic enzyme. Jarid2 is a well-established catalytically inactive member of the JmjC family: it lacks the conserved HxD…H catalytic triad required for iron coordination and 2-oxoglutarate-dependent demethylase/dioxygenase activity. The evidence directly contradicts the assignment of 2-oxoglutarate-dependent dioxygenase activity to this protein.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a recognizable JmjC (Jumonji C) domain, identifiable by its characteristic fold and partial motif remnants (e.g., the HxSGSIDSS…H region and the downstream conserved cysteine/histidine clusters). Family-level knowledge from OTHER JmjC proteins (JMJD1A, JMJD2A, PHF8, TET enzymes, etc.) strongly associates the JmjC domain with 2-oxoglutarate-dependent dioxygenase (histone demethylase) activity. None of the other options match any sequence feature: (A) metalloendopeptidase requires a zinc-binding HExxH or similar motif absent here; (B) manganese transmembrane transporter requires multiple transmembrane helices, which this largely disordered/nuclear protein lacks; (C) phosphatase requires a catalytic motif (e.g., HCX5R for cysteine phosphatases or DXDXT/V for serine phosphatases) not present. Thus the JmjC domain provides a concrete family-level inference that meaningfully distinguishes D from A, B, and C. However, a model with specific knowledge of Jarid2 would recognize that this particular JmjC member is catalytically inactive, creating tension with the family-level prediction.",
    "missing_item_specific_fact": "",
    "reason": "The JmjC domain in the sequence is a transferable family feature that links to 2-oxoglutarate-dependent dioxygenase activity via well-characterized homologs (JMJD, PHF, TET families). This distinguishes D from the three other options, none of which have any supporting sequence motif. The inference is a legitimate family-level generalization, though it leads to an answer that is contradicted for this specific catalytically-inactive protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, the JmjC domain clearly points toward D over A, B, and C. However, the true molecular functions of Jarid2 (DNA binding, protein-containing complex binding) are not offered as options, making the question somewhat artificial. No two offered choices are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The expected answer D (2-oxoglutarate-dependent dioxygenase activity) is contradicted by the UniProt annotation and the well-established literature that Jarid2 is a catalytically inactive JmjC protein lacking the HxD…H catalytic triad.",
    "The correct molecular function annotations (DNA binding, protein-containing complex binding) are not among the offered choices, making the question structurally flawed.",
    "The JmjC domain is present in the sequence, so family-level reasoning would lead a model to choose D, but this family-level inference is incorrect for this specific protein.",
    "The UniProt function annotation is partially based on similarity to human Q92833 (Jarid2), but even the human ortholog is catalytically inactive; the annotation correctly describes Jarid2 as a regulator/accessory subunit, not a catalytic dioxygenase.",
    "The GO:0016706 term definition (from GO3) describes catalysis of a specific redox reaction, which Jarid2 does not perform."
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
  "benchmark_sequence_length": 2351,
  "benchmark_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "current_entry_audit": {
    "entryVersion": 183,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 3
  },
  "current_record_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2351,
  "current_source_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 181,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VT00",
  "selected_historical_entry_version": 181,
  "selected_historical_record_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "selected_historical_source_sequence_length": 2351,
  "selected_historical_source_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "selected_historical_version": {
    "accession": "Q9VT00",
    "database": "Swiss-Prot",
    "entryVersion": 181,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "JARD2_DROME",
    "sequenceVersion": 3
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VT00\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":183,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17970746\",\"source\":\"PubMed\"}],\"value\":\"Protein jumonji\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17970746\",\"source\":\"PubMed\"}],\"value\":\"dJmj\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0036004\",\"source\":\"FlyBase\"}],\"value\":\"Jumonji, AT rich interactive domain protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q92833\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17970746\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22354997\",\"source\":\"PubMed\"}],\"value\":\"Regulator of histone methyltransferase complexes (By similarity). Involved in the establishment or maintenance of higher order chromosome compaction and closed euchromatin structure (PubMed:17970746). Accessory component of the polycomb repressive complex 2 (PRC2) involved in maintenance of transcriptional repression and regulation of transcriptional activation or elongation; functions in a PRC2-dependent and PRC2-independent manner (PubMed:22354997). Reduces levels of H3K27me3 histone modification (PubMed:22354997)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003677\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:DNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/40",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22354997\",\"source\":\"PubMed\"}],\"id\":\"GO:0044877\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:protein-containing complex binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/41",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasai N.\",\"Kato Y.\",\"Kimura G.\",\"Takeuchi T.\",\"Yamaguchi M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17970746\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1742-4658.2007.06135.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"6139\",\"id\":\"17970746\",\"journal\":\"FEBS J.\",\"lastPage\":\"6151\",\"publicationDate\":\"2007\",\"title\":\"The Drosophila jumonji gene encodes a JmjC-containing nuclear protein that is required for metamorphosis.\",\"volume\":\"274\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Herz H.M.\",\"Mohan M.\",\"Garrett A.S.\",\"Miller C.\",\"Casto D.\",\"Zhang Y.\",\"Seidel C.\",\"Haug J.S.\",\"Florens L.\",\"Washburn M.P.\",\"Yamaguchi M.\",\"Shiekhattar R.\",\"Shilatifard A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22354997\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.06503-11\"}],\"citationType\":\"journal article\",\"firstPage\":\"1683\",\"id\":\"22354997\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"1693\",\"publicationDate\":\"2012\",\"title\":\"Polycomb repressive complex 2-dependent and -independent functions of Jarid2 in transcriptional regulation in Drosophila.\",\"volume\":\"32\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE PRC2.2 COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H1",
  "excerpt": "ID   JARD2_DROME             Reviewed;        2351 AA.\nAC   Q9VT00; Q6AWH4; Q8SXP6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 3.\nDT   28-JAN-2026, entry version 181.\nDE   RecName: Full=Jumonji, AT rich interactive domain protein 2 {ECO:0000312|FlyBase:FBgn0036004};\nDE   AltName: Full=Protein jumonji {ECO:0000303|PubMed:17970746};\nDE            Short=dJmj {ECO:0000303|PubMed:17970746};\nGN   Name=Jarid2 {ECO:0000312|FlyBase:FBgn0036004};\nGN   Synonyms=Jmj {ECO:0000303|PubMed:17970746};\nGN   ORFNames=CG3654 {ECO:0000312|FlyBase:FBgn0036004};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H2",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=17970746; DOI=10.1111/j.1742-4658.2007.06135.x;\nRA   Sasai N., Kato Y., Kimura G., Takeuchi T., Yamaguchi M.;\nRT   \"The Drosophila jumonji gene encodes a JmjC-containing nuclear protein that\nRT   is required for metamorphosis.\";\nRL   FEBS J. 274:6139-6151(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H3",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE PRC2.2 COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=22354997; DOI=10.1128/mcb.06503-11;\nRA   Herz H.M., Mohan M., Garrett A.S., Miller C., Casto D., Zhang Y.,\nRA   Seidel C., Haug J.S., Florens L., Washburn M.P., Yamaguchi M.,\nRA   Shiekhattar R., Shilatifard A.;\nRT   \"Polycomb repressive complex 2-dependent and -independent functions of\nRT   Jarid2 in transcriptional regulation in Drosophila.\";\nRL   Mol. Cell. Biol. 32:1683-1693(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Regulator of histone methyltransferase complexes (By\nCC       similarity). Involved in the establishment or maintenance of higher\nCC       order chromosome compaction and closed euchromatin structure\nCC       (PubMed:17970746). Accessory component of the polycomb repressive\nCC       complex 2 (PRC2) involved in maintenance of transcriptional repression\nCC       and regulation of transcriptional activation or elongation; functions\nCC       in a PRC2-dependent and PRC2-independent manner (PubMed:22354997).\nCC       Reduces levels of H3K27me3 histone modification (PubMed:22354997).\nCC       {ECO:0000250|UniProtKB:Q92833, ECO:0000269|PubMed:17970746,\nCC       ECO:0000269|PubMed:22354997}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0003677; F:DNA binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-198",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0044877; F:protein-containing complex binding; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 199-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004222\nname: metalloendopeptidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain by a mechanism in which water acts as a nucleophile, one or two metal ions hold the water molecule in place, and charged amino acid side chains are ligands for the metal ions.\" [GOC:mah, https://www.ebi.ac.uk/merops/about/glossary.shtml#CATTYPE, https://www.ebi.ac.uk/merops/about/glossary.shtml#ENDOPEPTIDASE]\nsynonym: \"metalloendoprotease activity\" NARROW [GOC:mah]\nsynonym: \"metalloendoproteinase activity\" NARROW [GOC:mah]\nxref: EC:3.4.24.-\nxref: EC:3.4.24.11\nxref: EC:3.4.24.14\nxref: EC:3.4.24.17\nxref: EC:3.4.24.18\nxref: EC:3.4.24.19\nxref: EC:3.4.24.21\nxref: EC:3.4.24.22\nxref: EC:3.4.24.23\nxref: EC:3.4.24.24\nxref: EC:3.4.24.3\nxref: EC:3.4.24.34\nxref: EC:3.4.24.35\nxref: EC:3.4.24.37\nxref: EC:3.4.24.55\nxref: EC:3.4.24.56\nxref: EC:3.4.24.57\nxref: EC:3.4.24.59\nxref: EC:3.4.24.61\nxref: EC:3.4.24.65\nxref: EC:3.4.24.69\nxref: EC:3.4.24.7\nxref: EC:3.4.24.70\nxref: EC:3.4.24.71\nxref: EC:3.4.24.72\nxref: MetaCyc:3.4.24.11-RXN\nxref: MetaCyc:3.4.24.14-RXN\nxref: MetaCyc:3.4.24.17-RXN\nxref: MetaCyc:3.4.24.18-RXN\nxref: MetaCyc:3.4.24.19-RXN\nxref: MetaCyc:3.4.24.21-RXN\nxref: MetaCyc:3.4.24.22-RXN\nxref: MetaCyc:3.4.24.23-RXN\nxref: MetaCyc:3.4.24.24-RXN\nxref: MetaCyc:3.4.24.35-RXN\nxref: MetaCyc:3.4.24.37-RXN\nxref: MetaCyc:3.4.24.55-RXN\nxref: MetaCyc:3.4.24.56-RXN\nxref: MetaCyc:3.4.24.57-RXN\nxref: MetaCyc:3.4.24.59-RXN\nxref: MetaCyc:3.4.24.61-RXN\nxref: MetaCyc:3.4.24.64-RXN\nxref: MetaCyc:3.4.24.69-RXN\nxref: MetaCyc:3.4.24.70-RXN\nxref: MetaCyc:3.4.24.71-RXN\nxref: MetaCyc:3.4.24.72-RXN\nxref: Reactome:R-HSA-1168777 \"Metalloprotease cleavage of GHR\"\nxref: Reactome:R-HSA-1251992 \"Cleavage of P-ERBB4jmA isoforms by ADAM17\"\nxref: Reactome:R-HSA-1299476 \"MPP cleaves targeting peptide (presequence) of inner membrane precursors\"\nxref: Reactome:R-HSA-1299478 \"MPP cleaves targeting peptide (presequence) of matrix precursors\"\nxref: Reactome:R-HSA-1454757 \"Gelatin degradation by MMP1, 2, 3, 7, 8, 9, 12, 13\"\nxref: Reactome:R-HSA-1454822 \"Collagen type I degradation by MMP1,2,8,13, PRSS2\"\nxref: Reactome:R-HSA-1458433 \"Collagen type I degradation by MMP14\"\nxref: Reactome:R-HSA-1474196 \"Collagen type II degradation by MMP14\"\nxref: Reactome:R-HSA-1474210 \"Collagen type III degradation by MMP14\"\nxref: Reactome:R-HSA-1474213 \"Collagen type III degradation by MMP1,8,9,13\"\nxref: Reactome:R-HSA-1564112 \"Collagen type VI degradation by MMP2,9,11\"\nxref: Reactome:R-HSA-1564117 \"Collagen type XIV degradation by MMP9,13\"\nxref: Reactome:R-HSA-1564120 \"Collagen type VII degradation by MMP1,2,3\"\nxref: Reactome:R-HSA-1564142 \"Collagen type IV degradation by MMP2,3,4,9,10,12\"\nxref: Reactome:R-HSA-1564143 \"Collagen type X degradation by MMP1,2\"\nxref: Reactome:R-HSA-1564164 \"Collagen type V degradation by MMP2,9,10\"\nxref: Reactome:R-HSA-1564169 \"Collagen type VIII degradation by MMP1\"\nxref: Reactome:R-HSA-1564179 \"Collagen type XI degradation by MMP1,2,3,9\"\nxref: Reactome:R-HSA-1564184 \"Collagen type IX degradation by MMP3,13\"\nxref: Reactome:R-HSA-1592310 \"Aggrecan degradation by ADAMTSs\"\nxref: Reactome:R-HSA-1655851 \"S2P hydrolyzes SREBP1A,1C,2\"\nxref: Reactome:R-HSA-177946 \"Pro-EGF is cleaved to form mature EGF\"\nxref: Reactome:R-HSA-181567 \"botC LC cleaves target cell STX1\"\nxref: Reactome:R-HSA-194793 \"botC LC cleaves target cell SNAP25\"\nxref: Reactome:R-HSA-194796 \"botB LC cleaves target cell VAMP2\"\nxref: Reactome:R-HSA-194800 \"botE LC cleaves target cell SNAP25\"\nxref: Reactome:R-HSA-194808 \"botF LC cleaves target cell VAMP1\"\nxref: Reactome:R-HSA-194809 \"botD LC cleaves target cell VAMP1\"\nxref: Reactome:R-HSA-194818 \"botA LC cleaves target cell SNAP25\"\nxref: Reactome:R-HSA-2002428 \"Removal of fibrillar collagen N-propeptides\"\nxref: Reactome:R-HSA-2002440 \"Removal of fibrillar collagen C-propeptides\"\nxref: Reactome:R-HSA-2022141 \"Prolysyl oxidase activation\"\nxref: Reactome:R-HSA-2168046 \"Collagen type XII degradation by MMP12\"\nxref: Reactome:R-HSA-2168982 \"Collagen type XVI degradation by MMP9\"\nxref: Reactome:R-HSA-2179402 \"Active MMP3 can cleave pro-HBEGF to form active HBEGF\"\nxref: Reactome:R-HSA-2473584 \"Collagen type III degradation by MMP15\"\nxref: Reactome:R-HSA-2473594 \"Collagen type II degradation by MMP15\"\nxref: Reactome:R-HSA-2473596 \"Collagen type I degradation by MMP15\"\nxref: Reactome:R-HSA-2484882 \"Collagen type X degradation by MMP3, 13\"\nxref: Reactome:R-HSA-2485111 \"Collagen type III degradation by MMP10\"\nxref: Reactome:R-HSA-2485148 \"Fibrillin 1, 2,(3) degradation by MMP2, 9, 12 and 13\"\nxref: Reactome:R-HSA-2514790 \"Elastin degradation by MMP14\"\nxref: Reactome:R-HSA-2514831 \"Fibrillin-1 degradation by MMP14\"\nxref: Reactome:R-HSA-2533874 \"Laminin-511 degradation by MMP14\"\nxref: Reactome:R-HSA-2533944 \"Fibronectin degradation by MMP10\"\nxref: Reactome:R-HSA-2533950 \"Fibronectin degradation by MMP14\"\nxref: Reactome:R-HSA-2533965 \"NID1 degradation by MMP14, MMP15\"\nxref: Reactome:R-HSA-2533970 \"NID1 degradation by MMP3, 7\"\nxref: Reactome:R-HSA-2534240 \"HSPG2 (perlecan) degradation by MMP14, MMP15\"\nxref: Reactome:R-HSA-2534248 \"DCN (decorin) degradation by MMP2, MMP3, MMP7\"\nxref: Reactome:R-HSA-2537499 \"Gelatin degradation by MMP19\"\nxref: Reactome:R-HSA-264758 \"BMP1-3:Zn2+ cleaves pro-APOA1 to APOA1\"\nxref: Reactome:R-HSA-3371385 \"TNF- is cleaved by ADAM17 (TACE)\"\nxref: Reactome:R-HSA-3788075 \"Brevican degradation by ADAMTS4, ADAMTS5\"\nxref: Reactome:R-HSA-3791149 \"Brevican degradation by MMP1, 2, 3, 7,8,10,13,19\"\nxref: Reactome:R-HSA-3791155 \"Laminin-322 degradation by MMP14\"\nxref: Reactome:R-HSA-3791295 \"Aggrecan degradation by MMP1,2,3,7,9,12,13\"\nxref: Reactome:R-HSA-3791319 \"NID1 degradation by MMP19\"\nxref: Reactome:R-HSA-381435 \"Matrix metalloproteinase proteolyzes IGF:IGFBP3:ALS\"\nxref: Reactome:R-HSA-381518 \"PAAP-A proteolyzes IGF:IGFBP4\"\nxref: Reactome:R-HSA-381537 \"PAPP-A2 proteolyzes IGF:IGFBP5:ALS\"\nxref: Reactome:R-HSA-3827958 \"E-cadherin degradation by MMP9, KLK7\"\nxref: Reactome:R-HSA-3828025 \"DCN (decorin) degradation by MMP14\"\nxref: Reactome:R-HSA-4086205 \"OPN (osteopontin) degradation by MMP3, MMP7\"\nxref: Reactome:R-HSA-420818 \"MBTPS2 (S2P) cleaves ATF6 (ATF6-alpha)\"\nxref: Reactome:R-HSA-4224014 \"E-cadherin degradation by ADAM10, ADAM15\"\nxref: Reactome:R-HSA-5228578 \"tetX LC cleaves target cell VAMP2\"\nxref: Reactome:R-HSA-5250606 \"botD LC cleaves target cell VAMP2\"\nxref: Reactome:R-HSA-5250892 \"botF LC cleaves target cell VAMP2\"\nxref: Reactome:R-HSA-5250962 \"botG LC cleaves target cell VAMP2\"\nxref: Reactome:R-HSA-5250978 \"botG LC cleaves target cell VAMP1\"\nxref: Reactome:R-HSA-5333671 \"CLCAs self cleave\"\nxref: Reactome:R-HSA-5362793 \"Hh-Np is cleaved by ADAM17 to promote ligand shedding\"\nxref: Reactome:R-HSA-5694082 \"XK:KEL:Zn2+ cleaves EDN3\"\nxref: Reactome:R-HSA-6784620 \"MBTPS1,2 cleaves CREB3L3 to CREB3L3(1-?) and CREB3L3(?-461)\"\nxref: Reactome:R-HSA-8867344 \"OMA1 hydrolyses OPA1\"\nxref: Reactome:R-HSA-8874122 \"MBTPS2 (S2P) cleaves ATF6B (ATF6-beta)\"\nxref: Reactome:R-HSA-8874187 \"MBTPS2 (S2P) cleaves CREB3L2\"\nxref: Reactome:R-HSA-8874192 \"MBTPS2 (S2P) cleaves CREB3\"\nxref: Reactome:R-HSA-8874194 \"MBTPS2 (S2P) cleaves CREB3L1\"\nxref: Reactome:R-HSA-8874195 \"MBTPS2 (S2P) cleaves CREB3L4\"\nxref: Reactome:R-HSA-8874201 \"MBTPS2 (S2P) cleaves CREB3L3\"\nxref: Reactome:R-HSA-8876868 \"ECE1 cleaves EDN1(53-90)\"\nxref: Reactome:R-HSA-8877620 \"ECE2 cleaves EDN1(53-90)\"\nxref: Reactome:R-HSA-8940554 \"MMP2 cleaves OPTC\"\nxref: Reactome:R-HSA-8940561 \"MMP7 cleaves OPTC\"\nxref: Reactome:R-HSA-8940641 \"THOP1 cleaves oligopeptide fragment (8-16aa)\"\nxref: Reactome:R-HSA-8940959 \"Neurolysin degrades neurotensin\"\nxref: Reactome:R-HSA-8942302 \"MMP13 cleaves OPTC\"\nxref: Reactome:R-HSA-8943959 \"MMP2, MMP9 cleave SCUBE3\"\nxref: Reactome:R-HSA-8949649 \"PMPCA:PMPCB cleaves the transit peptide of proSMDT1 (proEMRE)\"\nxref: Reactome:R-HSA-8949659 \"AFG3L2 (m-AAA protease) degrades SMDT1 that is not assembled in MCU\"\nxref: Reactome:R-HSA-8949668 \"YME1L1 proteolyzes unassembled proSMDT1\"\nxref: Reactome:R-HSA-9010034 \"ADAM10:Zn2+:TSPANs cleaves APP(18-770)\"\nxref: Reactome:R-HSA-9624272 \"MMPs cleave HB-EGF\"\nxref: Reactome:R-HSA-9822532 \"ADAMTS13 cleaves VWF multimer\"\nxref: Reactome:R-HSA-9824402 \"ADAMTS13 variant does not cleave VWF multimer\"\nxref: Reactome:R-HSA-9840408 \"OMA1 cleaves DELE1\"\nxref: Reactome:R-HSA-9840532 \"OMA1 self-cleaves\"\nxref: Reactome:R-HSA-9840564 \"OMA1 hydrolyzes YME1L1\"\nxref: Reactome:R-HSA-9844241 \"ADAMTS13 cleaves VWF variant multimer\"\nis_a: GO:0004175 ! endopeptidase activity\nis_a: GO:0008237 ! metallopeptidase activity\nproperty_value: skos:exactMatch EC:3.4.24.-\nproperty_value: skos:narrowMatch EC:3.4.24.11\nproperty_value: skos:narrowMatch EC:3.4.24.14\nproperty_value: skos:narrowMatch EC:3.4.24.17\nproperty_value: skos:narrowMatch EC:3.4.24.18\nproperty_value: skos:narrowMatch EC:3.4.24.19\nproperty_value: skos:narrowMatch EC:3.4.24.21\nproperty_value: skos:narrowMatch EC:3.4.24.22\nproperty_value: skos:narrowMatch EC:3.4.24.23\nproperty_value: skos:narrowMatch EC:3.4.24.24\nproperty_value: skos:narrowMatch EC:3.4.24.3\nproperty_value: skos:narrowMatch EC:3.4.24.34\nproperty_value: skos:narrowMatch EC:3.4.24.35\nproperty_value: skos:narrowMatch EC:3.4.24.37\nproperty_value: skos:narrowMatch EC:3.4.24.55\nproperty_value: skos:narrowMatch EC:3.4.24.56\nproperty_value: skos:narrowMatch EC:3.4.24.57\nproperty_value: skos:narrowMatch EC:3.4.24.59\nproperty_value: skos:narrowMatch EC:3.4.24.61\nproperty_value: skos:narrowMatch EC:3.4.24.65\nproperty_value: skos:narrowMatch EC:3.4.24.69\nproperty_value: skos:narrowMatch EC:3.4.24.7\nproperty_value: skos:narrowMatch EC:3.4.24.70\nproperty_value: skos:narrowMatch EC:3.4.24.71\nproperty_value: skos:narrowMatch EC:3.4.24.72\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.11-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.14-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.17-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.18-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.19-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.21-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.22-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.23-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.24-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.35-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.37-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.55-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.56-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.57-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.59-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.61-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.64-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.69-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.70-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.71-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.24.72-RXN\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004222",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 37953-38155",
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
  "excerpt": "[Term]\nid: GO:0005384\nname: manganese ion transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of manganese (Mn) ions from one side of a membrane to the other.\" [GOC:dgf]\nxref: MetaCyc:RXN0-16\nxref: Reactome:R-HSA-8959798 \"SLC30A10 transports Mn2+ from cytosol to extracellular region\"\nis_a: GO:0046915 ! transition metal ion transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005384",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56277-56285",
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
  "excerpt": "[Term]\nid: GO:0016706\nname: 2-oxoglutarate-dependent dioxygenase activity\nnamespace: molecular_function\nalt_id: GO:0010302\ndef: \"Catalysis of the reaction: A + 2-oxoglutarate + O2 = B + succinate + CO2. This is an oxidation-reduction (redox) reaction in which hydrogen or electrons are transferred from 2-oxoglutarate and one other donor, and one atom of oxygen is incorporated into each donor.\" [GOC:mah]\nsynonym: \"2-oxoglutarate dioxygenase activity\" EXACT []\nsynonym: \"oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor, and incorporation of one atom each of oxygen into both donors\" EXACT []\nxref: EC:1.14.11.-\nxref: Reactome:R-HSA-1234164 \"Cytosolic HIF1AN (FIH1) hydroxylates asparagine residues of Hypoxia-inducible Factor Alpha (HIF1A,HIF2A)\"\nxref: Reactome:R-HSA-6783455 \"TYW5 hydroxylates yW-72 yielding OHyW-72 at nucleotide 37 of tRNA(Phe)\"\nis_a: GO:0016705 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen\nis_a: GO:0051213 ! dioxygenase activity\nproperty_value: skos:exactMatch EC:1.14.11.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016706",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129228-129242",
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
  "excerpt": "[Term]\nid: GO:0016791\nname: phosphatase activity\nnamespace: molecular_function\nalt_id: GO:0003869\nalt_id: GO:0016302\ndef: \"Catalysis of the hydrolysis of a phosphoric monoester, releasing a phosphate.\" [GOC:curators]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_metagenomics\nsubset: goslim_yeast\nsynonym: \"phosphatase\" RELATED []\nsynonym: \"phosphoric monoester hydrolase activity\" EXACT []\nxref: EC:3.1.3.-\nxref: Reactome:R-HSA-4419986 \"Unknown pPPP phosphatase dephosphorylates pPPP to pPNOL\"\nxref: Reactome:R-HSA-9636457 \"SapM dephosphorylates PI3P\"\nxref: Reactome:R-HSA-9837419 \"PANK4 hydrolyzes PPANT to pantetheine\"\nxref: Reactome:R-HSA-9940993 \"PXYLP1 dephosphorylates Xyl moiety\"\nis_a: GO:0042578 ! phosphoric ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.3.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016791",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130219-130240",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
