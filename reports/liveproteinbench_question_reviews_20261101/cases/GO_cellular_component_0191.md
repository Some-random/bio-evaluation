# GO_cellular_component_0191

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — Dbf4-dependent protein kinase complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADRVMCQELATPGSHYRRPKTGVPSTNVVYANGGGSWRAAPRQTQRLPRQTVQQYATGTPATGSAGRHSGRAFATAGATEEQTVEFNGAAVMGLPATPRTTKQARNKSEEAINDLLTRIPDIGKLFDVHSRIGNGTFSTVLLGTLRRESHLPDSLRRKFAIKHHIPTSHPDRIMKELQCMTKMGGKENVVGIHCCMRYDASAAFVMPFMAHDRFQDFYTRMDVPEIRQYMRNLLVALRHVHKFDVIHRDVKPSNFLYNRRRREFLLVDFGLAQHVNPPAARSSGSAAAIAAANNKNNNNNNNNNSKRPRERESKGDVQQIALDAGLGGAVKRMRLHEESNKMPLKPVNDIAPSDAPEQSVDGSNHVQPQLVQQEQQQLQPQQQQQQQQQQQQSQQQQQPQQQSQQQHPQRQPQLAQMDQTASTPSGSKYNTNRNVSAAAANNAKCVCFANPSVCLNCLMKKEVHASRAGTPGYRPPEVLLKYPDQTTAVDVWAAGVIFLSIMSTVYPFFKAPNDFIALAEIVTIFGDQAIRKTALALDRMITLSQRSRPLNLRKLCLRFRYRSVFSDAKLLKSYESVDGSCEVCRNCDQYFFNCLCEDSDYLTEPLDAYECFPPSAYDLLDRLLEINPHKRITAEEALKHPFFTAAEEAEQTEQDQLANGTPRKMRRQRYQSHRTVAASQEQVKQQVALDLQQAAINKL

[Multiple Choices]
A. cAMP-dependent protein kinase complex
B. RNA polymerase II transcription regulator complex
C. Dbf4-dependent protein kinase complex
D. IRE1-TRAF2-ASK1 complex
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

> The sequence matches the Drosophila Cdc7 record, which has a GO annotation to the Dbf4-dependent protein kinase complex with IDA:FlyBase evidence. This supports choice C as a curated experimental annotation, rather than merely a sequence-based prediction.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [H3](#evidence-h3), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a protein kinase, but that general feature does not distinguish membership in the Dbf4-dependent kinase complex from the other listed complexes.


**Missing item-specific fact**

> The sequence's identity as Cdc7 and its association with the Dbf4-dependent kinase complex, established by protein-specific annotation or experimental evidence, are not supplied in the question.


**Reason**

> Identifying the correct complex requires a protein-specific association not reliably inferable from the provided sequence and choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports choice C among the options. The limitation is that this distinction depends on external protein-specific information, not that multiple options are equally supported.


### Important caveats

- The supporting complex annotation is a curated database record with IDA:FlyBase evidence; the supplied excerpts do not independently detail the underlying experiment.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a protein kinase, but that general feature does not distinguish membership in the Dbf4-dependent kinase complex from the other listed complexes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as Cdc7 and its association with the Dbf4-dependent kinase complex, established by protein-specific annotation or experimental evidence, are not supplied in the question.",
    "reason": "Identifying the correct complex requires a protein-specific association not reliably inferable from the provided sequence and choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization."
  },
  "case_id": "GO_cellular_component_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "H3",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Cdc7 record, which has a GO annotation to the Dbf4-dependent protein kinase complex with IDA:FlyBase evidence. This supports choice C as a curated experimental annotation, rather than merely a sequence-based prediction."
  },
  "important_caveats": [
    "The supporting complex annotation is a curated database record with IDA:FlyBase evidence; the supplied excerpts do not independently detail the underlying experiment.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice C among the options. The limitation is that this distinction depends on external protein-specific information, not that multiple options are equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Cdc7 record, which has a GO annotation to the Dbf4-dependent protein kinase complex with IDA:FlyBase evidence. This supports choice C as a curated experimental annotation, rather than merely a sequence-based prediction.",
    "evidence_ids": ["C1", "C6", "H3", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a protein kinase, but that general feature does not distinguish membership in the Dbf4-dependent kinase complex from the other listed complexes.",
    "missing_item_specific_fact": "The sequence's identity as Cdc7 and its association with the Dbf4-dependent kinase complex, established by protein-specific annotation or experimental evidence, are not supplied in the question.",
    "reason": "Identifying the correct complex requires a protein-specific association not reliably inferable from the provided sequence and choices alone; recognizing the sequence or retrieving its annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice C among the options. The limitation is that this distinction depends on external protein-specific information, not that multiple options are equally supported."
  },
  "important_caveats": [
    "The supporting complex annotation is a curated database record with IDA:FlyBase evidence; the supplied excerpts do not independently detail the underlying experiment.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9W3Y1 (CDC7_DROME) carries GO:0031431 (Dbf4-dependent protein kinase complex) with evidence code IDA:FlyBase, referencing PubMed:25451925 which explicitly reports 'IDENTIFICATION IN DDK COMPLEX.' The GO term definition (GO2) confirms DDK comprises Cdc7 (catalytic) and Dbf4 (regulatory) subunits. The sequence match is exact (700 aa, SHA256 matched) in both current and historical (v200) records. This is an experimentally derived (IDA) annotation, not computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a Ser/Thr protein kinase (HRD and DFG motifs present), which eliminates options B (transcription regulator complex) and D (ER membrane IRE1-TRAF2-ASK1 complex). The 700-aa length with additional domains (zinc-finger-like motifs, poly-Q stretch) is inconsistent with the ~350-aa PKA catalytic subunit and lacks the PKA N-terminal myristoylation consensus (MGxxxxSxxxx), partially disfavoring option A. However, the final step—assigning this specific kinase to the 'Dbf4-dependent protein kinase complex'—requires knowing that Cdc7 is the catalytic subunit of DDK, which is a protein-specific complex annotation fact.


**Missing item-specific fact**

> The identification of this particular sequence as Cdc7 and the knowledge that Cdc7 is the catalytic subunit of the Dbf4-dependent protein kinase (DDK) complex. While kinase-family recognition from sequence motifs is possible in principle, the precise assignment to DDK (rather than another Ser/Thr kinase complex) depends on recognizing Cdc7's specific subfamily signature or recalling the Cdc7-Dbf4 complex composition.


**Reason**

> Eliminating B and D is reasoning-supported by the kinase domain. Eliminating A (PKA) has partial sequence-based support (size, domain architecture, absence of myristoylation site). However, the positive identification as Cdc7/DDK requires either recognizing the specific CAMK-group kinase subfamily signature of Cdc7 or recalling the specific protein-complex annotation, making the final choice lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, only C (Dbf4-dependent protein kinase complex) matches the experimentally verified complex membership of this protein. Options B and D are eliminated by the kinase domain; option A is disfavored by size and domain architecture. No ambiguity exists among the provided choices.


### Important caveats

- The protein also carries GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IBA) annotations, but these broad compartments are not among the answer choices.
- The GO:0005737 (cytoplasm) annotation uses IBA (Inferred by Biological Aspect from GO_Central), a computational/transferred evidence code, while the DDK complex annotation uses IDA (Inferred by Direct Assay), a stronger experimental evidence code.
- The sequence is from Drosophila melanogaster (fruit fly Cdc7), and the DDK complex annotation is supported by FlyBase experimental data (PubMed:25451925).
- The GO term definition (GO2) states DDK 'comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins,' confirming cross-species applicability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a Ser/Thr protein kinase (HRD and DFG motifs present), which eliminates options B (transcription regulator complex) and D (ER membrane IRE1-TRAF2-ASK1 complex). The 700-aa length with additional domains (zinc-finger-like motifs, poly-Q stretch) is inconsistent with the ~350-aa PKA catalytic subunit and lacks the PKA N-terminal myristoylation consensus (MGxxxxSxxxx), partially disfavoring option A. However, the final step—assigning this specific kinase to the 'Dbf4-dependent protein kinase complex'—requires knowing that Cdc7 is the catalytic subunit of DDK, which is a protein-specific complex annotation fact.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identification of this particular sequence as Cdc7 and the knowledge that Cdc7 is the catalytic subunit of the Dbf4-dependent protein kinase (DDK) complex. While kinase-family recognition from sequence motifs is possible in principle, the precise assignment to DDK (rather than another Ser/Thr kinase complex) depends on recognizing Cdc7's specific subfamily signature or recalling the Cdc7-Dbf4 complex composition.",
    "reason": "Eliminating B and D is reasoning-supported by the kinase domain. Eliminating A (PKA) has partial sequence-based support (size, domain architecture, absence of myristoylation site). However, the positive identification as Cdc7/DDK requires either recognizing the specific CAMK-group kinase subfamily signature of Cdc7 or recalling the specific protein-complex annotation, making the final choice lookup-dependent."
  },
  "case_id": "GO_cellular_component_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "C8",
      "H2",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9W3Y1 (CDC7_DROME) carries GO:0031431 (Dbf4-dependent protein kinase complex) with evidence code IDA:FlyBase, referencing PubMed:25451925 which explicitly reports 'IDENTIFICATION IN DDK COMPLEX.' The GO term definition (GO2) confirms DDK comprises Cdc7 (catalytic) and Dbf4 (regulatory) subunits. The sequence match is exact (700 aa, SHA256 matched) in both current and historical (v200) records. This is an experimentally derived (IDA) annotation, not computational inference."
  },
  "important_caveats": [
    "The protein also carries GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IBA) annotations, but these broad compartments are not among the answer choices.",
    "The GO:0005737 (cytoplasm) annotation uses IBA (Inferred by Biological Aspect from GO_Central), a computational/transferred evidence code, while the DDK complex annotation uses IDA (Inferred by Direct Assay), a stronger experimental evidence code.",
    "The sequence is from Drosophila melanogaster (fruit fly Cdc7), and the DDK complex annotation is supported by FlyBase experimental data (PubMed:25451925).",
    "The GO term definition (GO2) states DDK 'comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins,' confirming cross-species applicability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, only C (Dbf4-dependent protein kinase complex) matches the experimentally verified complex membership of this protein. Options B and D are eliminated by the kinase domain; option A is disfavored by size and domain architecture. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9W3Y1 (CDC7_DROME) carries GO:0031431 (Dbf4-dependent protein kinase complex) with evidence code IDA:FlyBase, referencing PubMed:25451925 which explicitly reports 'IDENTIFICATION IN DDK COMPLEX.' The GO term definition (GO2) confirms DDK comprises Cdc7 (catalytic) and Dbf4 (regulatory) subunits. The sequence match is exact (700 aa, SHA256 matched) in both current and historical (v200) records. This is an experimentally derived (IDA) annotation, not computational inference.",
    "evidence_ids": ["C1", "C4", "C6", "C8", "H2", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a Ser/Thr protein kinase (HRD and DFG motifs present), which eliminates options B (transcription regulator complex) and D (ER membrane IRE1-TRAF2-ASK1 complex). The 700-aa length with additional domains (zinc-finger-like motifs, poly-Q stretch) is inconsistent with the ~350-aa PKA catalytic subunit and lacks the PKA N-terminal myristoylation consensus (MGxxxxSxxxx), partially disfavoring option A. However, the final step—assigning this specific kinase to the 'Dbf4-dependent protein kinase complex'—requires knowing that Cdc7 is the catalytic subunit of DDK, which is a protein-specific complex annotation fact.",
    "missing_item_specific_fact": "The identification of this particular sequence as Cdc7 and the knowledge that Cdc7 is the catalytic subunit of the Dbf4-dependent protein kinase (DDK) complex. While kinase-family recognition from sequence motifs is possible in principle, the precise assignment to DDK (rather than another Ser/Thr kinase complex) depends on recognizing Cdc7's specific subfamily signature or recalling the Cdc7-Dbf4 complex composition.",
    "reason": "Eliminating B and D is reasoning-supported by the kinase domain. Eliminating A (PKA) has partial sequence-based support (size, domain architecture, absence of myristoylation site). However, the positive identification as Cdc7/DDK requires either recognizing the specific CAMK-group kinase subfamily signature of Cdc7 or recalling the specific protein-complex annotation, making the final choice lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, only C (Dbf4-dependent protein kinase complex) matches the experimentally verified complex membership of this protein. Options B and D are eliminated by the kinase domain; option A is disfavored by size and domain architecture. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The protein also carries GO:0005634 (nucleus, IDA) and GO:0005737 (cytoplasm, IBA) annotations, but these broad compartments are not among the answer choices.",
    "The GO:0005737 (cytoplasm) annotation uses IBA (Inferred by Biological Aspect from GO_Central), a computational/transferred evidence code, while the DDK complex annotation uses IDA (Inferred by Direct Assay), a stronger experimental evidence code.",
    "The sequence is from Drosophila melanogaster (fruit fly Cdc7), and the DDK complex annotation is supported by FlyBase experimental data (PubMed:25451925).",
    "The GO term definition (GO2) states DDK 'comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins,' confirming cross-species applicability."
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

**Accession:** `Q9W3Y1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 200. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
"Q9W3Y1"
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cell division cycle 7"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25451925","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0028360","source":"FlyBase"}],"value":"non-specific serine/threonine protein kinase Cdc7"}}}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"25451925","source":"PubMed"}],"id":"GO:0031431","properties":[{"key":"GoTerm","value":"C:Dbf4-dependent protein kinase complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"citation":{"authors":["Stephenson R.","Hosler M.R.","Gavande N.S.","Ghosh A.K.","Weake V.M."],"citationCrossReferences":[{"database":"PubMed","id":"25451925"},{"database":"DOI","id":"10.1074/jbc.m114.597948"}],"citationType":"journal article","firstPage":"1332","id":"25451925","journal":"J. Biol. Chem.","lastPage":"1347","publicationDate":"2015","title":"Characterization of a Drosophila ortholog of the Cdc7 kinase: a role for Cdc7 in endoreplication independent of Chiffon.","volume":"290"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","IDENTIFICATION IN DDK COMPLEX","INTERACTION WITH CHIF","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-269"]}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 77-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, IDENTIFICATION IN DDK
RP   COMPLEX, INTERACTION WITH CHIF, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF
RP   ASP-269.
RX   PubMed=25451925; DOI=10.1074/jbc.m114.597948;
RA   Stephenson R., Hosler M.R., Gavande N.S., Ghosh A.K., Weake V.M.;
RT   "Characterization of a Drosophila ortholog of the Cdc7 kinase: a role for
RT   Cdc7 in endoreplication independent of Chiffon.";
RL   J. Biol. Chem. 290:1332-1347(2015).
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 174-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
DR   GO; GO:0031431; C:Dbf4-dependent protein kinase complex; IDA:FlyBase.
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence GO2

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
