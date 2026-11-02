# GO_molecular_function_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — acyltransferase activity, transferring groups other than amino-acyl groups

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSTNAGGIASKQASSMAPNPGKATILALGHAFPQQLVMQDYVVDGFMRNTNCDDPELKEKLTRLCKTTTVKTRYVVMSEEILKSYPELAQEGQPTMKQRLDISNKAVTQMATEASLACVRSWGGALSEITHLVYVSSSEARFPGGDLHLARALGLSPDVRRVMLAFTGCSGGVAGLRVAKGLAESCPGARVLLATSETTIVGFRPPSPDRPYDLVGVALFGDGAGAAVVGADPTPVERPLFELHSALQRFLPDTDKTIDGRLTEEGIKFQLGRELPHIIEANVEAFCQKLMQEHPQAADKLTYGDMFWAVHPGGPAILTKMEGRLGLDGGKLRASRSALRDFGNASSNTIVYVLENMVEETRQRREEAAEEEDCEWGLILAFGPGITFEGILARNLQARARARD

[Multiple Choices]
A. acyltransferase activity, transferring groups other than amino-acyl groups
B. carbohydrate derivative binding
C. thiosulfate-cyanide sulfurtransferase activity
D. nucleoside transmembrane transporter activity
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact-matched sequence is annotated as a plant type III polyketide synthase that condenses fatty acyl-CoA with malonyl-CoA; the specific tetraketide alpha-pyrone synthase activity is a child of option A's acyltransferase term. The function annotation cites experimental evidence.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The roughly 405-residue soluble enzyme sequence, including a conserved cysteine-containing active-site motif characteristic of type III polyketide synthases, supports an acyl-CoA-condensing enzyme rather than a membrane transporter or a rhodanese-like sulfurtransferase. That enzyme family is consistent with option A's acyltransferase activity.


**Missing item-specific fact**

> No item-specific fact is essential to choose among these broad options. Identifying the precise biological product and experimentally characterized substrates would require additional evidence, but is not needed for option A.


**Reason**

> Sequence-family features and the contrast with the transporter and sulfurtransferase choices provide a defensible biological basis for selecting A; this does not require remembering the exact accession or its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is the broad molecular-function category supported by the enzyme's acyl-CoA condensation activity; the other choices describe distinct activities not supported by the sequence.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence, including a historical record, but the author's exact source snapshot is unknown.
- The reviewed function annotation cites experimental studies; the specific GO activity annotation is recorded as IDA. These sources support the key but were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The roughly 405-residue soluble enzyme sequence, including a conserved cysteine-containing active-site motif characteristic of type III polyketide synthases, supports an acyl-CoA-condensing enzyme rather than a membrane transporter or a rhodanese-like sulfurtransferase. That enzyme family is consistent with option A's acyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is essential to choose among these broad options. Identifying the precise biological product and experimentally characterized substrates would require additional evidence, but is not needed for option A.",
    "reason": "Sequence-family features and the contrast with the transporter and sulfurtransferase choices provide a defensible biological basis for selecting A; this does not require remembering the exact accession or its database entry."
  },
  "case_id": "GO_molecular_function_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as a plant type III polyketide synthase that condenses fatty acyl-CoA with malonyl-CoA; the specific tetraketide alpha-pyrone synthase activity is a child of option A's acyltransferase term. The function annotation cites experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence, including a historical record, but the author's exact source snapshot is unknown.",
    "The reviewed function annotation cites experimental studies; the specific GO activity annotation is recorded as IDA. These sources support the key but were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is the broad molecular-function category supported by the enzyme's acyl-CoA condensation activity; the other choices describe distinct activities not supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as a plant type III polyketide synthase that condenses fatty acyl-CoA with malonyl-CoA; the specific tetraketide alpha-pyrone synthase activity is a child of option A's acyltransferase term. The function annotation cites experimental evidence.",
    "evidence_ids": ["C5", "H5", "C6", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The roughly 405-residue soluble enzyme sequence, including a conserved cysteine-containing active-site motif characteristic of type III polyketide synthases, supports an acyl-CoA-condensing enzyme rather than a membrane transporter or a rhodanese-like sulfurtransferase. That enzyme family is consistent with option A's acyltransferase activity.",
    "missing_item_specific_fact": "No item-specific fact is essential to choose among these broad options. Identifying the precise biological product and experimentally characterized substrates would require additional evidence, but is not needed for option A.",
    "reason": "Sequence-family features and the contrast with the transporter and sulfurtransferase choices provide a defensible biological basis for selecting A; this does not require remembering the exact accession or its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is the broad molecular-function category supported by the enzyme's acyl-CoA condensation activity; the other choices describe distinct activities not supported by the sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence, including a historical record, but the author's exact source snapshot is unknown.",
    "The reviewed function annotation cites experimental studies; the specific GO activity annotation is recorded as IDA. These sources support the key but were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein Q8H305 (PKS10_ORYSJ) is experimentally annotated (IDA, PubMed:28783252) with GO:0090439 'tetraketide alpha-pyrone synthase activity' and EC 2.3.1.- (confirmed by ECO:0000269). The GO ontology shows GO:0090439 is_a GO:0016747 'acyltransferase activity, transferring groups other than amino-acyl groups' (evidence GO4). The function comment describes catalysis of fatty acyl-CoA + malonyl-CoA condensation, consistent with acyltransferase activity. Option A is the direct parent term of the experimentally annotated specific function, making it scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO3](#evidence-go3), [GO4](#evidence-go4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of the chalcone synthase / stilbene synthase (type III PKS) superfamily: the GCSGG active-site cysteine motif (~residue 108), the GADPT motif, and the GPG motif, along with the characteristic ~405-residue three-domain architecture. Type III PKS enzymes are EC 2.3.1.- acyltransferases that catalyze condensation of acyl-CoA with malonyl-CoA. This maps directly to GO:0016747. The other options are incompatible: C (rhodanese, EC 2.8.1.1) requires a rhodanese fold absent here; D (transmembrane transporter) requires transmembrane helices absent from this cytosolic enzyme; B (carbohydrate derivative binding) is a binding function, not a catalytic one, and no carbohydrate-binding modules are present.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides identifiable enzyme-family motifs (GCSGG, GADPT, GPG) diagnostic of the CHS/type III PKS superfamily, whose EC classification (2.3.1.-, acyltransferase) is standard biochemistry. Recognizing these motifs and their functional implication is general protein-structure knowledge, not memorization of a specific database entry. The three distractors are clearly incompatible with the sequence features, leaving A as the only defensible choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with the sequence: B is a binding function (not catalytic), C is a rhodanese (wrong fold, wrong EC class), D is a transmembrane transporter (no TM helices, wrong localization). Only A (acyltransferase, EC 2.3.1.-) is consistent with the type III PKS motifs present in the sequence.


### Important caveats

- The specific GO annotation is GO:0090439 (tetraketide alpha-pyrone synthase activity); option A is its direct parent GO:0016747. The question uses the broader parent term rather than the most specific annotated term.
- The EC number is 2.3.1.- (generic acyltransferase), not a fully specified EC, consistent with the broad GO term in option A.
- Recognition of type III PKS motifs (GCSGG, GADPT, GPG) requires domain-specific pattern knowledge; while this is general biochemistry for a protein scientist, it is not derivable from first-principles physics/chemistry alone.
- The reviewer-only evidence confirms the annotation was established by in vitro experiments (PubMed:28783252, 29411094), but this experimental context was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the chalcone synthase / stilbene synthase (type III PKS) superfamily: the GCSGG active-site cysteine motif (~residue 108), the GADPT motif, and the GPG motif, along with the characteristic ~405-residue three-domain architecture. Type III PKS enzymes are EC 2.3.1.- acyltransferases that catalyze condensation of acyl-CoA with malonyl-CoA. This maps directly to GO:0016747. The other options are incompatible: C (rhodanese, EC 2.8.1.1) requires a rhodanese fold absent here; D (transmembrane transporter) requires transmembrane helices absent from this cytosolic enzyme; B (carbohydrate derivative binding) is a binding function, not a catalytic one, and no carbohydrate-binding modules are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable enzyme-family motifs (GCSGG, GADPT, GPG) diagnostic of the CHS/type III PKS superfamily, whose EC classification (2.3.1.-, acyltransferase) is standard biochemistry. Recognizing these motifs and their functional implication is general protein-structure knowledge, not memorization of a specific database entry. The three distractors are clearly incompatible with the sequence features, leaving A as the only defensible choice."
  },
  "case_id": "GO_molecular_function_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO3",
      "GO4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein Q8H305 (PKS10_ORYSJ) is experimentally annotated (IDA, PubMed:28783252) with GO:0090439 'tetraketide alpha-pyrone synthase activity' and EC 2.3.1.- (confirmed by ECO:0000269). The GO ontology shows GO:0090439 is_a GO:0016747 'acyltransferase activity, transferring groups other than amino-acyl groups' (evidence GO4). The function comment describes catalysis of fatty acyl-CoA + malonyl-CoA condensation, consistent with acyltransferase activity. Option A is the direct parent term of the experimentally annotated specific function, making it scientifically supported."
  },
  "important_caveats": [
    "The specific GO annotation is GO:0090439 (tetraketide alpha-pyrone synthase activity); option A is its direct parent GO:0016747. The question uses the broader parent term rather than the most specific annotated term.",
    "The EC number is 2.3.1.- (generic acyltransferase), not a fully specified EC, consistent with the broad GO term in option A.",
    "Recognition of type III PKS motifs (GCSGG, GADPT, GPG) requires domain-specific pattern knowledge; while this is general biochemistry for a protein scientist, it is not derivable from first-principles physics/chemistry alone.",
    "The reviewer-only evidence confirms the annotation was established by in vitro experiments (PubMed:28783252, 29411094), but this experimental context was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence: B is a binding function (not catalytic), C is a rhodanese (wrong fold, wrong EC class), D is a transmembrane transporter (no TM helices, wrong localization). Only A (acyltransferase, EC 2.3.1.-) is consistent with the type III PKS motifs present in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein Q8H305 (PKS10_ORYSJ) is experimentally annotated (IDA, PubMed:28783252) with GO:0090439 'tetraketide alpha-pyrone synthase activity' and EC 2.3.1.- (confirmed by ECO:0000269). The GO ontology shows GO:0090439 is_a GO:0016747 'acyltransferase activity, transferring groups other than amino-acyl groups' (evidence GO4). The function comment describes catalysis of fatty acyl-CoA + malonyl-CoA condensation, consistent with acyltransferase activity. Option A is the direct parent term of the experimentally annotated specific function, making it scientifically supported.",
    "evidence_ids": ["C4", "C5", "C6", "GO3", "GO4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the chalcone synthase / stilbene synthase (type III PKS) superfamily: the GCSGG active-site cysteine motif (~residue 108), the GADPT motif, and the GPG motif, along with the characteristic ~405-residue three-domain architecture. Type III PKS enzymes are EC 2.3.1.- acyltransferases that catalyze condensation of acyl-CoA with malonyl-CoA. This maps directly to GO:0016747. The other options are incompatible: C (rhodanese, EC 2.8.1.1) requires a rhodanese fold absent here; D (transmembrane transporter) requires transmembrane helices absent from this cytosolic enzyme; B (carbohydrate derivative binding) is a binding function, not a catalytic one, and no carbohydrate-binding modules are present.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable enzyme-family motifs (GCSGG, GADPT, GPG) diagnostic of the CHS/type III PKS superfamily, whose EC classification (2.3.1.-, acyltransferase) is standard biochemistry. Recognizing these motifs and their functional implication is general protein-structure knowledge, not memorization of a specific database entry. The three distractors are clearly incompatible with the sequence features, leaving A as the only defensible choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence: B is a binding function (not catalytic), C is a rhodanese (wrong fold, wrong EC class), D is a transmembrane transporter (no TM helices, wrong localization). Only A (acyltransferase, EC 2.3.1.-) is consistent with the type III PKS motifs present in the sequence."
  },
  "important_caveats": [
    "The specific GO annotation is GO:0090439 (tetraketide alpha-pyrone synthase activity); option A is its direct parent GO:0016747. The question uses the broader parent term rather than the most specific annotated term.",
    "The EC number is 2.3.1.- (generic acyltransferase), not a fully specified EC, consistent with the broad GO term in option A.",
    "Recognition of type III PKS motifs (GCSGG, GADPT, GPG) requires domain-specific pattern knowledge; while this is general biochemistry for a protein scientist, it is not derivable from first-principles physics/chemistry alone.",
    "The reviewer-only evidence confirms the annotation was established by in vitro experiments (PubMed:28783252, 29411094), but this experimental context was not available to the evaluated model."
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

**Accession:** `Q8H305` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 131. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28783252","source":"PubMed"}],"value":"Type III polyketide synthase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28783252","source":"PubMed"}],"value":"OsPKS2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28783252","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27878652","source":"PubMed"}],"value":"Type III polyketide synthase 10"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27878652","source":"PubMed"}],"value":"OsPKS10"}]}}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28783252","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29411094","source":"PubMed"}],"value":"Plant type III polyketide synthases (PKSs) that catalyzes the condensation of fatty acyl-CoA with malonyl-CoA to generate triketide and tetraketide alpha-pyrones, the main components of pollen exine and potential sporopollenin precursors (PubMed:28783252). May be involved in the synthesis of sporopollenin precursors in tapetal cells to regulate pollen wall formation (PubMed:29411094). Required for exine and Ubisch body formation in anthers (PubMed:28783252). Does not possess chalcone synthase (CHS) activity in vitro with the substrates 4-coumaroyl-CoA and malonyl-CoA (PubMed:28783252)"}]}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"28783252","source":"PubMed"}],"id":"GO:0090439","properties":[{"key":"GoTerm","value":"F:tetraketide alpha-pyrone synthase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)  
**Locator:** `lines 81-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-02T04:32:02.084503+00:00.  

```text
CC   -!- FUNCTION: Plant type III polyketide synthases (PKSs) that catalyzes the
CC       condensation of fatty acyl-CoA with malonyl-CoA to generate triketide
CC       and tetraketide alpha-pyrones, the main components of pollen exine and
CC       potential sporopollenin precursors (PubMed:28783252). May be involved
CC       in the synthesis of sporopollenin precursors in tapetal cells to
CC       regulate pollen wall formation (PubMed:29411094). Required for exine
CC       and Ubisch body formation in anthers (PubMed:28783252). Does not
CC       possess chalcone synthase (CHS) activity in vitro with the substrates
CC       4-coumaroyl-CoA and malonyl-CoA (PubMed:28783252).
CC       {ECO:0000269|PubMed:28783252, ECO:0000269|PubMed:29411094}.
```

Source SHA-256: `087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)  
**Locator:** `lines 134-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-02T04:32:02.084503+00:00.  

```text
DR   GO; GO:0090439; F:tetraketide alpha-pyrone synthase activity; IDA:UniProtKB.
```

Source SHA-256: `087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 129733-129745`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016747
name: acyltransferase activity, transferring groups other than amino-acyl groups
namespace: molecular_function
def: "Catalysis of the transfer of an acyl group, other than amino-acyl, from one compound (donor) to another (acceptor)." [EC:2.3.1.-]
synonym: "transferase activity, transferring acyl groups other than amino-acyl groups" EXACT []
synonym: "transferase activity, transferring groups other than amino-acyl groups" RELATED [EC:2.3.1.-]
xref: EC:2.3.1.-
xref: Reactome:R-HSA-9859163 "DBT transfers BCAA to CoA"
xref: Reactome:R-HSA-9865115 "DBT loss-of-function mutants don't synthesize BCAA-CoA"
is_a: GO:0016746 ! acyltransferase activity
property_value: skos:exactMatch EC:2.3.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 399100-399108`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0090439
name: tetraketide alpha-pyrone synthase activity
namespace: molecular_function
def: "Catalyzes the reaction: 7-hydroxylauroyl-CoA + 3 malonyl-CoA + 2 H+ = 2-(8-hydroxy-2-oxotridecyl)-6-oxopyran-4-olate + 3 CO2 + 4 coenzyme A." [MetaCyc:RXN-16407, PMID:21193570]
xref: MetaCyc:RXN-16407
is_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups
property_value: skos:exactMatch MetaCyc:RXN-16407

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
