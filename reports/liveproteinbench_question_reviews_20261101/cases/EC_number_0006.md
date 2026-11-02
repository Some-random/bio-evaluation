# EC_number_0006

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.3.1.322

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNITILSKETIKPLAPTPHHHKYYKVSLLDQFAPSSYMPFIFFYPNKFADRDAAGILTQLKESLSQILTIYYPLAGRVKDTVYVECNDEGVEFIEAQANGSLSDFLKQPDIAALNNFLPRNGNGLEKGCSISPVAIKATVFECSGIVLGVCIFHKVVDAAAAGEFLQSWAKIGRGSKETVELPNFTSASSLFPPRESLSSKFVRDFDNFFFQGSKSFMRRFVFDATAITTLRTKATSEKVPNPSRVEALMEFVVQHLSTAFKTAKSETPETLMITHPVNLRKRIEPPLPDSTFGNVIWLAFAFYDCDPSETKIKPGDVVERVREAFAALDKESISELETDDAFTSLSELLESVYTNEKIKIYRFTSTCNMGFYDVDFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN

[Multiple Choices]
A. 2.3.1.312
B. 2.3.1.322
C. 2.4.2.12
D. 5.3.99.13
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as akuammiline synthase 2, EC 2.3.1.322. The entry links the catalytic activity and EC assignment to experimental evidence (ECO:0000269) and a cited publication, supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest an acyltransferase, but they do not establish the precise substrate reaction needed to distinguish these EC numbers.


**Missing item-specific fact**

> The protein-specific catalytic activity—acetyl transfer from acetyl-CoA to rhazimol to form akuammiline—or an equivalent functional annotation or experimental result.


**Reason**

> The sequence is provided without organism or functional context. Identifying the exact EC number requires a protein-specific reaction fact absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched entry's supported EC assignment distinguishes B; the supplied evidence does not support another listed option for this sequence.


### Important caveats

- The experimental evidence code and cited publication support the database annotation, but the primary study was not independently reviewed here.
- Reviewer-only annotations establish support for the key; they were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase, but they do not establish the precise substrate reaction needed to distinguish these EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—acetyl transfer from acetyl-CoA to rhazimol to form akuammiline—or an equivalent functional annotation or experimental result.",
    "reason": "The sequence is provided without organism or functional context. Identifying the exact EC number requires a protein-specific reaction fact absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the supplied information."
  },
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as akuammiline synthase 2, EC 2.3.1.322. The entry links the catalytic activity and EC assignment to experimental evidence (ECO:0000269) and a cited publication, supporting choice B."
  },
  "important_caveats": [
    "The experimental evidence code and cited publication support the database annotation, but the primary study was not independently reviewed here.",
    "Reviewer-only annotations establish support for the key; they were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry's supported EC assignment distinguishes B; the supplied evidence does not support another listed option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as akuammiline synthase 2, EC 2.3.1.322. The entry links the catalytic activity and EC assignment to experimental evidence (ECO:0000269) and a cited publication, supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest an acyltransferase, but they do not establish the precise substrate reaction needed to distinguish these EC numbers.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—acetyl transfer from acetyl-CoA to rhazimol to form akuammiline—or an equivalent functional annotation or experimental result.",
    "reason": "The sequence is provided without organism or functional context. Identifying the exact EC number requires a protein-specific reaction fact absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry's supported EC assignment distinguishes B; the supplied evidence does not support another listed option for this sequence."
  },
  "important_caveats": [
    "The experimental evidence code and cited publication support the database annotation, but the primary study was not independently reviewed here.",
    "Reviewer-only annotations establish support for the key; they were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence exactly matches UniProt entry A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2 from Alstonia scholaris). The EC 2.3.1.322 annotation is backed by experimental evidence (ECO:0000269, inferred from direct assay) citing PubMed:36349266 (Wang et al., Chem. Sci. 2022). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) is confirmed by Rhea:RHEA:79623. The entry is in Swiss-Prot (reviewed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the DFGWG motif and HxxxD-type motifs characteristic of the BAHD acyltransferase superfamily, which can reasonably narrow the EC class to 2.3.1.x (acyltransferases), eliminating C (2.4.2.12, glycosyltransferase) and D (5.3.99.13, isomerase). However, distinguishing EC 2.3.1.312 from EC 2.3.1.322 requires knowing the specific substrate (rhazimol vs. another acyl acceptor) and product (akuammiline), which is an experimentally determined substrate-specificity fact not derivable from sequence motifs alone.


**Missing item-specific fact**

> The specific substrate identity (rhazimol) and product (akuammiline) of this particular BAHD acyltransferase, which determines whether the 4th digit is 312 or 322. This was established experimentally in Wang et al. (2022) and cannot be inferred from the amino acid sequence without knowledge of the specific natural-product pathway.


**Reason**

> While sequence motifs (DFGWG, HxxxD) allow a knowledgeable model to identify the protein as a BAHD acyltransferase (EC 2.3.1.x), the final distinction between 2.3.1.312 and 2.3.1.322 hinges on the specific acyl-acceptor substrate, which is an item-specific experimental fact. No general biological reasoning from the sequence alone can resolve which of these two adjacent acyltransferase EC numbers applies.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.3.1.312) and B (2.3.1.322) are BAHD acyltransferases (EC 2.3.1.x). Without external knowledge of the specific substrate, a model identifying the protein as a BAHD acyltransferase cannot definitively choose between these two options. C and D are clearly eliminable by class-level reasoning.


### Important caveats

- The UniProt annotation is supported by direct experimental evidence (ECO:0000269), not merely computational inference.
- The sequence match to A0A9E7LUL3 is exact (SHA-256 verified) across both current and historical (v13) snapshots.
- The identity of the protein as AKS2 was inferred by the reviewer from dataset metadata; this was not provided to the evaluated model.
- EC 2.3.1.312's exact reaction was not independently verified in the reviewer evidence; the key point is that both A and B fall within the same EC 2.3.1.x acyltransferase class, making the 4th-digit distinction substrate-specific.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the DFGWG motif and HxxxD-type motifs characteristic of the BAHD acyltransferase superfamily, which can reasonably narrow the EC class to 2.3.1.x (acyltransferases), eliminating C (2.4.2.12, glycosyltransferase) and D (5.3.99.13, isomerase). However, distinguishing EC 2.3.1.312 from EC 2.3.1.322 requires knowing the specific substrate (rhazimol vs. another acyl acceptor) and product (akuammiline), which is an experimentally determined substrate-specificity fact not derivable from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (rhazimol) and product (akuammiline) of this particular BAHD acyltransferase, which determines whether the 4th digit is 312 or 322. This was established experimentally in Wang et al. (2022) and cannot be inferred from the amino acid sequence without knowledge of the specific natural-product pathway.",
    "reason": "While sequence motifs (DFGWG, HxxxD) allow a knowledgeable model to identify the protein as a BAHD acyltransferase (EC 2.3.1.x), the final distinction between 2.3.1.312 and 2.3.1.322 hinges on the specific acyl-acceptor substrate, which is an item-specific experimental fact. No general biological reasoning from the sequence alone can resolve which of these two adjacent acyltransferase EC numbers applies."
  },
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt entry A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2 from Alstonia scholaris). The EC 2.3.1.322 annotation is backed by experimental evidence (ECO:0000269, inferred from direct assay) citing PubMed:36349266 (Wang et al., Chem. Sci. 2022). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) is confirmed by Rhea:RHEA:79623. The entry is in Swiss-Prot (reviewed)."
  },
  "important_caveats": [
    "The UniProt annotation is supported by direct experimental evidence (ECO:0000269), not merely computational inference.",
    "The sequence match to A0A9E7LUL3 is exact (SHA-256 verified) across both current and historical (v13) snapshots.",
    "The identity of the protein as AKS2 was inferred by the reviewer from dataset metadata; this was not provided to the evaluated model.",
    "EC 2.3.1.312's exact reaction was not independently verified in the reviewer evidence; the key point is that both A and B fall within the same EC 2.3.1.x acyltransferase class, making the 4th-digit distinction substrate-specific."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.3.1.312) and B (2.3.1.322) are BAHD acyltransferases (EC 2.3.1.x). Without external knowledge of the specific substrate, a model identifying the protein as a BAHD acyltransferase cannot definitively choose between these two options. C and D are clearly eliminable by class-level reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt entry A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2 from Alstonia scholaris). The EC 2.3.1.322 annotation is backed by experimental evidence (ECO:0000269, inferred from direct assay) citing PubMed:36349266 (Wang et al., Chem. Sci. 2022). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) is confirmed by Rhea:RHEA:79623. The entry is in Swiss-Prot (reviewed).",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the DFGWG motif and HxxxD-type motifs characteristic of the BAHD acyltransferase superfamily, which can reasonably narrow the EC class to 2.3.1.x (acyltransferases), eliminating C (2.4.2.12, glycosyltransferase) and D (5.3.99.13, isomerase). However, distinguishing EC 2.3.1.312 from EC 2.3.1.322 requires knowing the specific substrate (rhazimol vs. another acyl acceptor) and product (akuammiline), which is an experimentally determined substrate-specificity fact not derivable from sequence motifs alone.",
    "missing_item_specific_fact": "The specific substrate identity (rhazimol) and product (akuammiline) of this particular BAHD acyltransferase, which determines whether the 4th digit is 312 or 322. This was established experimentally in Wang et al. (2022) and cannot be inferred from the amino acid sequence without knowledge of the specific natural-product pathway.",
    "reason": "While sequence motifs (DFGWG, HxxxD) allow a knowledgeable model to identify the protein as a BAHD acyltransferase (EC 2.3.1.x), the final distinction between 2.3.1.312 and 2.3.1.322 hinges on the specific acyl-acceptor substrate, which is an item-specific experimental fact. No general biological reasoning from the sequence alone can resolve which of these two adjacent acyltransferase EC numbers applies."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.3.1.312) and B (2.3.1.322) are BAHD acyltransferases (EC 2.3.1.x). Without external knowledge of the specific substrate, a model identifying the protein as a BAHD acyltransferase cannot definitively choose between these two options. C and D are clearly eliminable by class-level reasoning."
  },
  "important_caveats": [
    "The UniProt annotation is supported by direct experimental evidence (ECO:0000269), not merely computational inference.",
    "The sequence match to A0A9E7LUL3 is exact (SHA-256 verified) across both current and historical (v13) snapshots.",
    "The identity of the protein as AKS2 was inferred by the reviewer from dataset metadata; this was not provided to the evaluated model.",
    "EC 2.3.1.312's exact reaction was not independently verified in the reviewer evidence; the key point is that both A and B fall within the same EC 2.3.1.x acyltransferase class, making the 4th-digit distinction substrate-specific."
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

**Accession:** `A0A9E7LUL3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
"A0A9E7LUL3"
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"2.3.1.322"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Akuammiline synthase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAKS2"}]}}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79624"}}],"reaction":{"ecNumber":"2.3.1.322","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79623"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:141879"},{"database":"ChEBI","id":"CHEBI:230474"}]}}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65388.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
DE   RecName: Full=Akuammiline synthase 2 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS2 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 17-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65388.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);
CC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;
CC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
