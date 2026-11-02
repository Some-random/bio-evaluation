# GO_biological_process_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — microtubule cytoskeleton organization

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLDKLSKHKTMFYERVKEIDQILFSQQQAKQTQLDNLSNNNASGGFFSGFMKMFSPLSTPPNSSSNNNSNTQQAISQETRKLCSVNNNRHEPIYNQYTTNSQVIRSFPAVSSIGQSSTNMYNSVNICDGISSSEKRSPTPPRNRSNSNDKILFGHYDALGSLPQNNMGHYQQPPQQSSQQQQQPLVPKQNSVTALRNTTSATSSTTTANNKKPSLDQIPELKGVDRKLLDHILNEVIETKTTNWDDIAGLKDAKQTLLETVILPSIRPDLFNGLRAPCRGILLFGPPGTGKTMIARACASQCNATFFSISAGSLVSKYHGEGEKLVRCLFAAARYLQPSVIFIDEIDSILSARSSEEHEASRRMKTEFMIQMDGVSNMNGKEDRVLVMGATNIPTELDEAILRRFTKRIYIPLPDHAARASLIKQLSHGQNMSLSETDINKICVATEGFSGSDLTALCKETSMVPLREISMDQLISIDARKIRPIVLKDFQSSLVHVRPSTSQDTIKKLEKWNESYGTFAKGI

[Multiple Choices]
A. transmembrane transport
B. symbiont-mediated suppression of host gene expression
C. microtubule cytoskeleton organization
D. response to xenobiotic stimulus
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence match is annotated as spastin, with an ATP-dependent microtubule-severing function that supports microtubule cytoskeleton organization. The functional annotation is by similarity, not direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble P-loop AAA ATPase, which makes transmembrane transport less plausible; however, that broad feature does not by itself establish the specific microtubule-related process.


**Missing item-specific fact**

> That this sequence is a spastin homolog whose function is microtubule severing.


**Reason**

> Distinguishing C requires identifying the protein family and knowing its specific cellular role, neither of which is supplied explicitly. Merely recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the reviewer-only function annotation, C is the clear best fit among the listed choices.


### Important caveats

- The matched UniProt annotation transfers function by similarity from another protein; it is not direct experimental evidence for this Naegleria protein.
- The sequence match is exact in the cited historical record, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble P-loop AAA ATPase, which makes transmembrane transport less plausible; however, that broad feature does not by itself establish the specific microtubule-related process.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is a spastin homolog whose function is microtubule severing.",
    "reason": "Distinguishing C requires identifying the protein family and knowing its specific cellular role, neither of which is supplied explicitly. Merely recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported."
  },
  "case_id": "GO_biological_process_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as spastin, with an ATP-dependent microtubule-severing function that supports microtubule cytoskeleton organization. The functional annotation is by similarity, not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The matched UniProt annotation transfers function by similarity from another protein; it is not direct experimental evidence for this Naegleria protein.",
    "The sequence match is exact in the cited historical record, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the reviewer-only function annotation, C is the clear best fit among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as spastin, with an ATP-dependent microtubule-severing function that supports microtubule cytoskeleton organization. The functional annotation is by similarity, not direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble P-loop AAA ATPase, which makes transmembrane transport less plausible; however, that broad feature does not by itself establish the specific microtubule-related process.",
    "missing_item_specific_fact": "That this sequence is a spastin homolog whose function is microtubule severing.",
    "reason": "Distinguishing C requires identifying the protein family and knowing its specific cellular role, neither of which is supplied explicitly. Merely recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the reviewer-only function annotation, C is the clear best fit among the listed choices."
  },
  "important_caveats": [
    "The matched UniProt annotation transfers function by similarity from another protein; it is not direct experimental evidence for this Naegleria protein.",
    "The sequence match is exact in the cited historical record, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D2VS83 (Naegleria gruberi Spastin, EC 5.6.1.1) is annotated as an 'ATP-dependent microtubule severing protein' that 'stimulates microtubule minus-end depolymerization and poleward microtubule flux in the mitotic spindle.' GO:0000226 (microtubule cytoskeleton organization) is defined as assembly, arrangement, or disassembly of microtubule-based cytoskeletal structures, which encompasses severing and depolymerization. The sequence contains a recognizable AAA ATPase domain (Walker A 'PPGTGKT', Walker B 'IDEID', sensor regions), consistent with spastin. Note: the annotation carries evidence code ECO:0000250 (similarity to human Q9UBP0), so it is a computational/by-similarity inference rather than direct experimental characterization of this Naegleria ortholog.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical AAA ATPase domain identifiable by the Walker A motif (GPPGTGKT), Walker B motif (IDEID), and sensor-1/sensor-2 arginine residues. Among the four choices: (A) transmembrane transport requires membrane-spanning segments, which are absent from this 523-aa soluble protein; (B) symbiont-mediated suppression of host gene expression applies to viral/symbiont effectors, not a free-living amoeba's own protein; (D) response to xenobiotic stimulus typically involves cytochrome P450s, GSTs, or ABC transporters, none of which match the AAA ATPase architecture. Microtubule-severing AAA ATPases (spastin, katanin, fidgetin) are a well-established subfamily in general cell biology. The combination of AAA ATPase identification plus elimination of the three incompatible options provides a defensible biological argument for C.


**Missing item-specific fact**

> Positive identification of this specific protein as spastin (rather than another AAA ATPase with a different substrate) would require either exact sequence lookup or knowledge of the spastin/katanin AAA ATPase subfamily. However, recognizing microtubule severing as a canonical AAA ATPase function is general biological knowledge, not an item-specific annotation.


**Reason**

> The AAA ATPase domain is sequence-identifiable. Process of elimination of the other three options is grounded in general biology (no TM domains, not a symbiont protein, no xenobiotic-metabolism motifs). The positive link to microtubule organization relies on knowing that microtubule-severing is a recognized AAA ATPase function, which is textbook-level knowledge rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated biologically. Transmembrane transport requires membrane-spanning regions (absent). Symbiont-mediated suppression applies to viral/parasite effectors (incompatible with a free-living amoeba's own protein). Response to xenobiotic stimulus implies xenobiotic-metabolizing or detoxification enzymes (incompatible with AAA ATPase architecture). Microtubule cytoskeleton organization is the only option consistent with a soluble AAA ATPase in a eukaryotic cytoskeletal context.


### Important caveats

- The UniProt function annotation is 'By similarity' (ECO:0000250) to human spastin Q9UBP0; no direct experimental evidence (e.g., in vitro microtubule-severing assay) for the Naegleria ortholog is cited in the supplied evidence.
- The sequence is from Naegleria gruberi, a free-living amoeba; the spastin ortholog annotation is computationally transferred, and the degree of functional conservation with human spastin has not been experimentally verified in the provided evidence.
- The AAA ATPase domain identification is robust from sequence motifs, but the specific assignment to microtubule severing (as opposed to, e.g., protein degradation or membrane trafficking AAA ATPases) depends on recognizing the spastin/katanin subfamily or eliminating alternatives.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt D2VS83, and the historical entry (version 58) was released 28-Jan-2026, within the benchmark construction window.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical AAA ATPase domain identifiable by the Walker A motif (GPPGTGKT), Walker B motif (IDEID), and sensor-1/sensor-2 arginine residues. Among the four choices: (A) transmembrane transport requires membrane-spanning segments, which are absent from this 523-aa soluble protein; (B) symbiont-mediated suppression of host gene expression applies to viral/symbiont effectors, not a free-living amoeba's own protein; (D) response to xenobiotic stimulus typically involves cytochrome P450s, GSTs, or ABC transporters, none of which match the AAA ATPase architecture. Microtubule-severing AAA ATPases (spastin, katanin, fidgetin) are a well-established subfamily in general cell biology. The combination of AAA ATPase identification plus elimination of the three incompatible options provides a defensible biological argument for C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of this specific protein as spastin (rather than another AAA ATPase with a different substrate) would require either exact sequence lookup or knowledge of the spastin/katanin AAA ATPase subfamily. However, recognizing microtubule severing as a canonical AAA ATPase function is general biological knowledge, not an item-specific annotation.",
    "reason": "The AAA ATPase domain is sequence-identifiable. Process of elimination of the other three options is grounded in general biology (no TM domains, not a symbiont protein, no xenobiotic-metabolism motifs). The positive link to microtubule organization relies on knowing that microtubule-severing is a recognized AAA ATPase function, which is textbook-level knowledge rather than a protein-specific database lookup."
  },
  "case_id": "GO_biological_process_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D2VS83 (Naegleria gruberi Spastin, EC 5.6.1.1) is annotated as an 'ATP-dependent microtubule severing protein' that 'stimulates microtubule minus-end depolymerization and poleward microtubule flux in the mitotic spindle.' GO:0000226 (microtubule cytoskeleton organization) is defined as assembly, arrangement, or disassembly of microtubule-based cytoskeletal structures, which encompasses severing and depolymerization. The sequence contains a recognizable AAA ATPase domain (Walker A 'PPGTGKT', Walker B 'IDEID', sensor regions), consistent with spastin. Note: the annotation carries evidence code ECO:0000250 (similarity to human Q9UBP0), so it is a computational/by-similarity inference rather than direct experimental characterization of this Naegleria ortholog."
  },
  "important_caveats": [
    "The UniProt function annotation is 'By similarity' (ECO:0000250) to human spastin Q9UBP0; no direct experimental evidence (e.g., in vitro microtubule-severing assay) for the Naegleria ortholog is cited in the supplied evidence.",
    "The sequence is from Naegleria gruberi, a free-living amoeba; the spastin ortholog annotation is computationally transferred, and the degree of functional conservation with human spastin has not been experimentally verified in the provided evidence.",
    "The AAA ATPase domain identification is robust from sequence motifs, but the specific assignment to microtubule severing (as opposed to, e.g., protein degradation or membrane trafficking AAA ATPases) depends on recognizing the spastin/katanin subfamily or eliminating alternatives.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt D2VS83, and the historical entry (version 58) was released 28-Jan-2026, within the benchmark construction window."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Transmembrane transport requires membrane-spanning regions (absent). Symbiont-mediated suppression applies to viral/parasite effectors (incompatible with a free-living amoeba's own protein). Response to xenobiotic stimulus implies xenobiotic-metabolizing or detoxification enzymes (incompatible with AAA ATPase architecture). Microtubule cytoskeleton organization is the only option consistent with a soluble AAA ATPase in a eukaryotic cytoskeletal context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D2VS83 (Naegleria gruberi Spastin, EC 5.6.1.1) is annotated as an 'ATP-dependent microtubule severing protein' that 'stimulates microtubule minus-end depolymerization and poleward microtubule flux in the mitotic spindle.' GO:0000226 (microtubule cytoskeleton organization) is defined as assembly, arrangement, or disassembly of microtubule-based cytoskeletal structures, which encompasses severing and depolymerization. The sequence contains a recognizable AAA ATPase domain (Walker A 'PPGTGKT', Walker B 'IDEID', sensor regions), consistent with spastin. Note: the annotation carries evidence code ECO:0000250 (similarity to human Q9UBP0), so it is a computational/by-similarity inference rather than direct experimental characterization of this Naegleria ortholog.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical AAA ATPase domain identifiable by the Walker A motif (GPPGTGKT), Walker B motif (IDEID), and sensor-1/sensor-2 arginine residues. Among the four choices: (A) transmembrane transport requires membrane-spanning segments, which are absent from this 523-aa soluble protein; (B) symbiont-mediated suppression of host gene expression applies to viral/symbiont effectors, not a free-living amoeba's own protein; (D) response to xenobiotic stimulus typically involves cytochrome P450s, GSTs, or ABC transporters, none of which match the AAA ATPase architecture. Microtubule-severing AAA ATPases (spastin, katanin, fidgetin) are a well-established subfamily in general cell biology. The combination of AAA ATPase identification plus elimination of the three incompatible options provides a defensible biological argument for C.",
    "missing_item_specific_fact": "Positive identification of this specific protein as spastin (rather than another AAA ATPase with a different substrate) would require either exact sequence lookup or knowledge of the spastin/katanin AAA ATPase subfamily. However, recognizing microtubule severing as a canonical AAA ATPase function is general biological knowledge, not an item-specific annotation.",
    "reason": "The AAA ATPase domain is sequence-identifiable. Process of elimination of the other three options is grounded in general biology (no TM domains, not a symbiont protein, no xenobiotic-metabolism motifs). The positive link to microtubule organization relies on knowing that microtubule-severing is a recognized AAA ATPase function, which is textbook-level knowledge rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Transmembrane transport requires membrane-spanning regions (absent). Symbiont-mediated suppression applies to viral/parasite effectors (incompatible with a free-living amoeba's own protein). Response to xenobiotic stimulus implies xenobiotic-metabolizing or detoxification enzymes (incompatible with AAA ATPase architecture). Microtubule cytoskeleton organization is the only option consistent with a soluble AAA ATPase in a eukaryotic cytoskeletal context."
  },
  "important_caveats": [
    "The UniProt function annotation is 'By similarity' (ECO:0000250) to human spastin Q9UBP0; no direct experimental evidence (e.g., in vitro microtubule-severing assay) for the Naegleria ortholog is cited in the supplied evidence.",
    "The sequence is from Naegleria gruberi, a free-living amoeba; the spastin ortholog annotation is computationally transferred, and the degree of functional conservation with human spastin has not been experimentally verified in the provided evidence.",
    "The AAA ATPase domain identification is robust from sequence motifs, but the specific assignment to microtubule severing (as opposed to, e.g., protein degradation or membrane trafficking AAA ATPases) depends on recognizing the spastin/katanin subfamily or eliminating alternatives.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt D2VS83, and the historical entry (version 58) was released 28-Jan-2026, within the benchmark construction window."
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

**Accession:** `D2VS83` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 58. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:39.406341+00:00.  

```json
"D2VS83"
```

Source SHA-256: `f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:39.406341+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBP0","source":"UniProtKB"}],"value":"5.6.1.1"}],"fullName":{"value":"Spastin"}}}
```

Source SHA-256: `f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:39.406341+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UBP0","source":"UniProtKB"}],"value":"ATP-dependent microtubule severing protein (By similarity). Stimulates microtubule minus-end depolymerization and poleward microtubule flux in the mitotic spindle (By similarity)"}]}
```

Source SHA-256: `f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 2.  
**Retrieved:** 2026-11-02T04:27:44.335585+00:00.  

```text
ID   SPAST_NAEGR             Reviewed;         523 AA.
AC   D2VS83;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 58.
DE   RecName: Full=Spastin;
DE            EC=5.6.1.1 {ECO:0000250|UniProtKB:Q9UBP0};
GN   ORFNames=NAEGRDRAFT_83257;
OS   Naegleria gruberi (Amoeba).
OC   Eukaryota; Discoba; Heterolobosea; Tetramitia; Eutetramitia;
OC   Vahlkampfiidae; Naegleria.
OX   NCBI_TaxID=5762;
```

Source SHA-256: `123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58)  
**Locator:** `lines 24-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 2.  
**Retrieved:** 2026-11-02T04:27:44.335585+00:00.  

```text
CC   -!- FUNCTION: ATP-dependent microtubule severing protein (By similarity).
CC       Stimulates microtubule minus-end depolymerization and poleward
CC       microtubule flux in the mitotic spindle (By similarity).
CC       {ECO:0000250|UniProtKB:Q9UBP0}.
```

Source SHA-256: `123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 2328-2338`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000226
name: microtubule cytoskeleton organization
namespace: biological_process
def: "A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins." [GOC:mah]
subset: goslim_pombe
synonym: "microtubule cytoskeleton organisation" EXACT [GOC:mah]
synonym: "microtubule cytoskeleton organization and biogenesis" RELATED [GOC:mah]
is_a: GO:0007010 ! cytoskeleton organization
is_a: GO:0007017 ! microtubule-based process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
