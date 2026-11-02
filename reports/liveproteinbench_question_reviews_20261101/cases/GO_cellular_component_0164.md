# GO_cellular_component_0164

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDKKEVQHHRSQQAMTKSLYAIGMGLLGKSATNMDCANTNLESAGKSSSTNYNRNRFYNERFVPMASGTMPSVSGTNHHSRHQQLLLQQAPKCTADLNEKLVKINRQNANKELSTIQAKDMQSVDKNEEALKELQESIPEINKIFDVHCRIGSGTFSTVLLGTLQRERGLVETQRRRFAIKHHNPTNHPERILRELECMYRIGGVENVIGINCCIRYNDNVAFIMPYMTHDRFHDIYRSLNFPEIRDYLRNLLIALRHVHKFNVIHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGSVVQSSDLSSREVFSILRDLENGRSVTLTDGNSAQAEAEDYMARRRMRALGGGGSVERAVTGPPSIQKLREQAGGHLTKKDVANQRADTMRLLNRLRLVSPNADPNNYVVSTNTSKKEMHASRAGTPGYRPPEVLLRYPKQSTAVDVWAAGVIMLSLLSGLHPFFKAPHDCGALAEIINLFGDMPVRKTAFLLDRLILLAQKVNTLDLRRVCMRFRHADFFLAPEIQRKYQRPDGTTEMCRSCEQPTFNCLCSNSGHNLERYDGLDIFPAVAYDLLSRLLEVNPQKRITAEEALKHPFFSDQHRITPGIPLHQQQLIMHQQQHIMQHQQHLQRSRETLPSSAARTLKAFVCYPMEITSTASQAAGNI

[Multiple Choices]
A. SAGA complex
B. nuclear inclusion body
C. nucleus
D. other organism cell membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the Drosophila CDC7B entry, which annotates the protein to the nucleus (IBA) and to the Dbf4-dependent protein kinase complex (IDA); that complex is a nuclear complex. This supports nucleus, though the nucleus annotation itself is computationally inferred rather than direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C7](#evidence-c7), [H3](#evidence-h3), [C6](#evidence-c6), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a protein-kinase domain, but that alone does not establish its cellular location or distinguish nucleus from other possible locations.


**Missing item-specific fact**

> The protein-specific identity and localization/function of Drosophila CDC7B, including its association with the nuclear Dbf4-dependent kinase complex, are not supplied in the question.


**Reason**

> Choosing nucleus requires protein-specific knowledge or external annotation; recognizing the sequence as CDC7B would be identification or memorization, not a localization argument available from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports nucleus. It also annotates cytoplasm, which is not an option; it provides no comparable support for SAGA complex, nuclear inclusion body, or another organism's cell membrane.


### Important caveats

- The sequence match is exact, but the accession was inferred from reviewer-only metadata and was not provided to the evaluated model.
- The nuclear GO annotation is IBA, a computationally inferred annotation; the IDA evidence is for the kinase complex, not necessarily a direct localization measurement.
- The source snapshot used by the original author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase domain, but that alone does not establish its cellular location or distinguish nucleus from other possible locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and localization/function of Drosophila CDC7B, including its association with the nuclear Dbf4-dependent kinase complex, are not supplied in the question.",
    "reason": "Choosing nucleus requires protein-specific knowledge or external annotation; recognizing the sequence as CDC7B would be identification or memorization, not a localization argument available from the input."
  },
  "case_id": "GO_cellular_component_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C7",
      "H3",
      "C6",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila CDC7B entry, which annotates the protein to the nucleus (IBA) and to the Dbf4-dependent protein kinase complex (IDA); that complex is a nuclear complex. This supports nucleus, though the nucleus annotation itself is computationally inferred rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The nuclear GO annotation is IBA, a computationally inferred annotation; the IDA evidence is for the kinase complex, not necessarily a direct localization measurement.",
    "The source snapshot used by the original author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports nucleus. It also annotates cytoplasm, which is not an option; it provides no comparable support for SAGA complex, nuclear inclusion body, or another organism's cell membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila CDC7B entry, which annotates the protein to the nucleus (IBA) and to the Dbf4-dependent protein kinase complex (IDA); that complex is a nuclear complex. This supports nucleus, though the nucleus annotation itself is computationally inferred rather than direct experimental localization evidence.",
    "evidence_ids": ["C1", "C7", "H3", "C6", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a protein-kinase domain, but that alone does not establish its cellular location or distinguish nucleus from other possible locations.",
    "missing_item_specific_fact": "The protein-specific identity and localization/function of Drosophila CDC7B, including its association with the nuclear Dbf4-dependent kinase complex, are not supplied in the question.",
    "reason": "Choosing nucleus requires protein-specific knowledge or external annotation; recognizing the sequence as CDC7B would be identification or memorization, not a localization argument available from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports nucleus. It also annotates cytoplasm, which is not an option; it provides no comparable support for SAGA complex, nuclear inclusion body, or another organism's cell membrane."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The nuclear GO annotation is IBA, a computationally inferred annotation; the IDA evidence is for the kinase complex, not necessarily a direct localization measurement.",
    "The source snapshot used by the original author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `expected_answer_check:invalid_evidence_ids`.

### Expected-answer support: supported

> UniProt Q9VJ90 (CDC7B_DROME) is annotated to GO:0005634 (nucleus) via IBA:GO_Central (C7/H3) and to GO:0031431 (Dbf4-dependent protein kinase complex) via IDA:FlyBase from PubMed 25451925 (C6/H2). The ontology hierarchy places GO:0031431 is_a GO:0140513 (nuclear protein-containing complex) part_of GO:0005634 (nucleus), confirming the nuclear localization. Cdc7 kinase functions in the nucleus during DNA replication/endoreplication, consistent with the annotation.

Citations as saved: [C7](#evidence-c7), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2), [GO3](#evidence-go3), [GO6](#evidence-go6), `ontology_annotation_term_paths` (not an assigned excerpt ID).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable serine/threonine kinase domain (HRD...DFG...APE motifs) with no signal peptide, no transmembrane helices, and no mitochondrial targeting sequence. This eliminates option D (other organism cell membrane) as there is no membrane-anchoring feature. Option A (SAGA complex) is a histone acetyltransferase complex; a kinase domain is not a HAT domain, making membership unlikely without evidence of specific interaction partners. Option B (nuclear inclusion body) describes sequestered aggregated proteins, not an active kinase. A cell-cycle kinase lacking organelle-targeting signals defaults to the nucleus, where DNA replication and endoreplication occur. The general biological principle that a soluble kinase involved in cell-cycle regulation resides in the nucleus provides meaningful grounds to select C over the specific-complex and aggregation alternatives.


**Missing item-specific fact**

> Precise identification of this kinase as Cdc7/Ddk (rather than any other kinase) would require database lookup, but the general reasoning from kinase domain + absence of targeting signals + cell-cycle context is sufficient to favor 'nucleus' over the other three options without protein-specific memorization.


**Reason**

> The sequence provides a clear kinase domain and the absence of membrane/mitochondrial targeting signals. Biological reasoning (kinase ≠ HAT complex component; kinase ≠ aggregation-prone protein; cell-cycle kinase → nucleus) meaningfully distinguishes C from A, B, and D without requiring exact protein identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (nucleus) is the most general and defensible answer. While the Dbf4-dependent protein kinase complex annotation is more specific, it is not offered as a choice. SAGA complex (A) is a different nuclear complex with no sequence basis for membership. Nuclear inclusion body (B) and other organism cell membrane (D) are clearly incompatible with a soluble kinase. No ambiguity among the offered choices.


### Important caveats

- The direct nucleus annotation uses IBA (inferred by biological aspect) rather than experimental evidence; the stronger IDA evidence is for the Dbf4-dependent protein kinase complex annotation.
- The reviewer-only UniProt accession (Q9VJ90) was inferred from dataset metadata and was not available to the evaluated model; the model must reason from sequence alone.
- The kinase domain is identifiable but distinguishing Cdc7 from other kinases by sequence alone is difficult; however, the question only requires compartment prediction, not kinase-family assignment.
- The ontology snapshot used by the benchmark authors is unknown; current GO structure supports the answer but historical annotations may differ slightly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable serine/threonine kinase domain (HRD...DFG...APE motifs) with no signal peptide, no transmembrane helices, and no mitochondrial targeting sequence. This eliminates option D (other organism cell membrane) as there is no membrane-anchoring feature. Option A (SAGA complex) is a histone acetyltransferase complex; a kinase domain is not a HAT domain, making membership unlikely without evidence of specific interaction partners. Option B (nuclear inclusion body) describes sequestered aggregated proteins, not an active kinase. A cell-cycle kinase lacking organelle-targeting signals defaults to the nucleus, where DNA replication and endoreplication occur. The general biological principle that a soluble kinase involved in cell-cycle regulation resides in the nucleus provides meaningful grounds to select C over the specific-complex and aggregation alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this kinase as Cdc7/Ddk (rather than any other kinase) would require database lookup, but the general reasoning from kinase domain + absence of targeting signals + cell-cycle context is sufficient to favor 'nucleus' over the other three options without protein-specific memorization.",
    "reason": "The sequence provides a clear kinase domain and the absence of membrane/mitochondrial targeting signals. Biological reasoning (kinase ≠ HAT complex component; kinase ≠ aggregation-prone protein; cell-cycle kinase → nucleus) meaningfully distinguishes C from A, B, and D without requiring exact protein identification."
  },
  "case_id": "GO_cellular_component_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C6",
      "H3",
      "H2",
      "GO3",
      "GO6",
      "ontology_annotation_term_paths"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9VJ90 (CDC7B_DROME) is annotated to GO:0005634 (nucleus) via IBA:GO_Central (C7/H3) and to GO:0031431 (Dbf4-dependent protein kinase complex) via IDA:FlyBase from PubMed 25451925 (C6/H2). The ontology hierarchy places GO:0031431 is_a GO:0140513 (nuclear protein-containing complex) part_of GO:0005634 (nucleus), confirming the nuclear localization. Cdc7 kinase functions in the nucleus during DNA replication/endoreplication, consistent with the annotation."
  },
  "important_caveats": [
    "The direct nucleus annotation uses IBA (inferred by biological aspect) rather than experimental evidence; the stronger IDA evidence is for the Dbf4-dependent protein kinase complex annotation.",
    "The reviewer-only UniProt accession (Q9VJ90) was inferred from dataset metadata and was not available to the evaluated model; the model must reason from sequence alone.",
    "The kinase domain is identifiable but distinguishing Cdc7 from other kinases by sequence alone is difficult; however, the question only requires compartment prediction, not kinase-family assignment.",
    "The ontology snapshot used by the benchmark authors is unknown; current GO structure supports the answer but historical annotations may differ slightly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleus) is the most general and defensible answer. While the Dbf4-dependent protein kinase complex annotation is more specific, it is not offered as a choice. SAGA complex (A) is a different nuclear complex with no sequence basis for membership. Nuclear inclusion body (B) and other organism cell membrane (D) are clearly incompatible with a soluble kinase. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9VJ90 (CDC7B_DROME) is annotated to GO:0005634 (nucleus) via IBA:GO_Central (C7/H3) and to GO:0031431 (Dbf4-dependent protein kinase complex) via IDA:FlyBase from PubMed 25451925 (C6/H2). The ontology hierarchy places GO:0031431 is_a GO:0140513 (nuclear protein-containing complex) part_of GO:0005634 (nucleus), confirming the nuclear localization. Cdc7 kinase functions in the nucleus during DNA replication/endoreplication, consistent with the annotation.",
    "evidence_ids": ["C7", "C6", "H3", "H2", "GO3", "GO6", "ontology_annotation_term_paths"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable serine/threonine kinase domain (HRD...DFG...APE motifs) with no signal peptide, no transmembrane helices, and no mitochondrial targeting sequence. This eliminates option D (other organism cell membrane) as there is no membrane-anchoring feature. Option A (SAGA complex) is a histone acetyltransferase complex; a kinase domain is not a HAT domain, making membership unlikely without evidence of specific interaction partners. Option B (nuclear inclusion body) describes sequestered aggregated proteins, not an active kinase. A cell-cycle kinase lacking organelle-targeting signals defaults to the nucleus, where DNA replication and endoreplication occur. The general biological principle that a soluble kinase involved in cell-cycle regulation resides in the nucleus provides meaningful grounds to select C over the specific-complex and aggregation alternatives.",
    "missing_item_specific_fact": "Precise identification of this kinase as Cdc7/Ddk (rather than any other kinase) would require database lookup, but the general reasoning from kinase domain + absence of targeting signals + cell-cycle context is sufficient to favor 'nucleus' over the other three options without protein-specific memorization.",
    "reason": "The sequence provides a clear kinase domain and the absence of membrane/mitochondrial targeting signals. Biological reasoning (kinase ≠ HAT complex component; kinase ≠ aggregation-prone protein; cell-cycle kinase → nucleus) meaningfully distinguishes C from A, B, and D without requiring exact protein identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleus) is the most general and defensible answer. While the Dbf4-dependent protein kinase complex annotation is more specific, it is not offered as a choice. SAGA complex (A) is a different nuclear complex with no sequence basis for membership. Nuclear inclusion body (B) and other organism cell membrane (D) are clearly incompatible with a soluble kinase. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The direct nucleus annotation uses IBA (inferred by biological aspect) rather than experimental evidence; the stronger IDA evidence is for the Dbf4-dependent protein kinase complex annotation.",
    "The reviewer-only UniProt accession (Q9VJ90) was inferred from dataset metadata and was not available to the evaluated model; the model must reason from sequence alone.",
    "The kinase domain is identifiable but distinguishing Cdc7 from other kinases by sequence alone is difficult; however, the question only requires compartment prediction, not kinase-family assignment.",
    "The ontology snapshot used by the benchmark authors is unknown; current GO structure supports the answer but historical annotations may differ slightly."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9VJ90` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 211. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
"Q9VJ90"
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"25451925","source":"PubMed"}],"id":"GO:0031431","properties":[{"key":"GoTerm","value":"C:Dbf4-dependent protein kinase complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/uniProtKBCrossReferences/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 142-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
DR   GO; GO:0031431; C:Dbf4-dependent protein kinase complex; IDA:FlyBase.
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 143-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IBA:GO_Central.
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 176442-176452`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031431
name: Dbf4-dependent protein kinase complex
namespace: cellular_component
def: "A heterodimeric protein complex required for the activation of DNA replication origins; comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins." [PMID:12045100]
synonym: "Cdc7-Dbf4 complex" NARROW []
synonym: "DDK" EXACT []
synonym: "Hsk1-Dfp1 kinase complex" NARROW []
is_a: GO:0140513 ! nuclear protein-containing complex
is_a: GO:1902554 ! serine/threonine protein kinase complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 441123-441132`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140513
name: nuclear protein-containing complex
namespace: cellular_component
def: "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together in the nucleus." [GOC:pg]
subset: gocheck_do_not_annotate
synonym: "nuclear complex" EXACT []
is_a: GO:0032991 ! protein-containing complex
relationship: part_of GO:0005634 ! nucleus

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
