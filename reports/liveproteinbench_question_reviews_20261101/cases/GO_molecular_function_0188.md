# GO_molecular_function_0188

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — S-adenosylmethionine-dependent methyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. RNA polymerase II transcription regulatory region sequence-specific DNA binding
B. quercetin 3-O-glucosyltransferase activity
C. protein serine/threonine phosphatase activity
D. S-adenosylmethionine-dependent methyltransferase activity
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

> The supplied sequence exactly matches the UniProt entry for norajmaline N-methyltransferase. That entry reports experimentally supported transfer of a methyl group from S-adenosyl-L-methionine in the enzyme's catalytic reaction, supporting choice D. The GO annotation is also D, though it is computationally assigned by InterPro.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich region, DIGCGVGGTCV, consistent with a SAM-binding motif in SAM-dependent methyltransferases. That gives a defensible sequence-based reason to favor D over DNA binding, protein phosphatase, or glucosyltransferase activity.


**Missing item-specific fact**

> The specific substrate and experimentally verified activity of this particular protein are not given in the question; those facts would be needed to identify it specifically as norajmaline N-methyltransferase, but not to favor the broad SAM-dependent methyltransferase option.


**Reason**

> A recognizable sequence motif provides a biological basis for distinguishing the broad enzyme class among these choices. This is predictive evidence, not experimental proof from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct functions, and the sequence motif supports the SAM-dependent methyltransferase class; no other listed option is comparably supported.


### Important caveats

- The sequence motif is suggestive rather than conclusive on its own.
- The sequence-matched database record and experimental evidence are reviewer-only and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich region, DIGCGVGGTCV, consistent with a SAM-binding motif in SAM-dependent methyltransferases. That gives a defensible sequence-based reason to favor D over DNA binding, protein phosphatase, or glucosyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate and experimentally verified activity of this particular protein are not given in the question; those facts would be needed to identify it specifically as norajmaline N-methyltransferase, but not to favor the broad SAM-dependent methyltransferase option.",
    "reason": "A recognizable sequence motif provides a biological basis for distinguishing the broad enzyme class among these choices. This is predictive evidence, not experimental proof from the supplied input."
  },
  "case_id": "GO_molecular_function_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8",
      "H4",
      "H5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for norajmaline N-methyltransferase. That entry reports experimentally supported transfer of a methyl group from S-adenosyl-L-methionine in the enzyme's catalytic reaction, supporting choice D. The GO annotation is also D, though it is computationally assigned by InterPro."
  },
  "important_caveats": [
    "The sequence motif is suggestive rather than conclusive on its own.",
    "The sequence-matched database record and experimental evidence are reviewer-only and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct functions, and the sequence motif supports the SAM-dependent methyltransferase class; no other listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for norajmaline N-methyltransferase. That entry reports experimentally supported transfer of a methyl group from S-adenosyl-L-methionine in the enzyme's catalytic reaction, supporting choice D. The GO annotation is also D, though it is computationally assigned by InterPro.",
    "evidence_ids": ["C1", "C5", "C6", "C8", "H4", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich region, DIGCGVGGTCV, consistent with a SAM-binding motif in SAM-dependent methyltransferases. That gives a defensible sequence-based reason to favor D over DNA binding, protein phosphatase, or glucosyltransferase activity.",
    "missing_item_specific_fact": "The specific substrate and experimentally verified activity of this particular protein are not given in the question; those facts would be needed to identify it specifically as norajmaline N-methyltransferase, but not to favor the broad SAM-dependent methyltransferase option.",
    "reason": "A recognizable sequence motif provides a biological basis for distinguishing the broad enzyme class among these choices. This is predictive evidence, not experimental proof from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct functions, and the sequence motif supports the SAM-dependent methyltransferase class; no other listed option is comparably supported."
  },
  "important_caveats": [
    "The sequence motif is suggestive rather than conclusive on its own.",
    "The sequence-matched database record and experimental evidence are reviewer-only and were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A075D6M1 (Norajmaline N-methyltransferase, RsNNMT, EC 2.1.1.392) exactly (sha256 confirmed, 292 aa). The protein's catalytic reaction is norajmaline + S-adenosyl-L-methionine → ajmaline + S-adenosyl-L-homocysteine + H+, experimentally validated (ECO:0000269, PubMed:27122470 and 38212296). GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is directly annotated to this entry. The expected answer D is fully supported by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the glycine-rich motif 'DIGCGVGG' (~residues 95–102), which is a recognizable variant of the canonical SAM-binding motif (e.g., VLDVGCGVGG) found in the Rossmann-fold β-sheet of S-adenosylmethionine-dependent methyltransferases. Conversely, the sequence lacks the catalytic motifs of PPP-family phosphatases (GDxVHG) or PPM-family phosphatases (HxHGxDxH) needed for option C; lacks the PSPG motif (HGGPWWP) characteristic of plant UDP-glucosyltransferases needed for option B; and lacks zinc-finger (C-x2-4-C-x12-H-x3-5-H) or helix-turn-helix DNA-binding motifs expected for option A. The combination of a positive SAM-binding motif signal and the absence of motifs diagnostic of the other three enzyme classes provides a concrete, general-biology reasoning path to select D.


**Missing item-specific fact**

> None strictly required. The SAM-binding glycine-rich motif and the absence of competing catalytic/binding motifs are visible in the supplied sequence and interpretable with general enzymology knowledge.


**Reason**

> A model with knowledge of Rossmann-fold methyltransferase motifs can identify 'GCGVGG' as a SAM-contacting glycine-rich loop and, combined with the absence of phosphatase, glycosyltransferase, or DNA-binding signatures, reason toward option D without needing to look up this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different enzyme classes (DNA-binding transcription factor, glycosyltransferase, phosphatase, methyltransferase). The SAM-binding motif and the absence of competing diagnostic motifs cleanly favor D. No other option is defensible given the sequence features.


### Important caveats

- The GO:0008757 annotation carries evidence code IEA:InterPro (computational/curator-inferred from domain match), but the underlying enzyme activity (N-methylation using SAM) is experimentally confirmed (ECO:0000269) in two independent publications.
- The protein is described as derived from a gamma-tocopherol C-methyltransferase gene family; its SAM-binding motif is somewhat degenerate relative to the most canonical 'VLDVGCGVGG' pattern, so motif recognition requires tolerance for variation.
- The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning assessment is based solely on what is extractable from the raw sequence and general biological knowledge.
- The historical entry (version 36, released 2026-01-28) matches the current entry (version 38) in sequence and core annotations; no discrepancy in function assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the glycine-rich motif 'DIGCGVGG' (~residues 95–102), which is a recognizable variant of the canonical SAM-binding motif (e.g., VLDVGCGVGG) found in the Rossmann-fold β-sheet of S-adenosylmethionine-dependent methyltransferases. Conversely, the sequence lacks the catalytic motifs of PPP-family phosphatases (GDxVHG) or PPM-family phosphatases (HxHGxDxH) needed for option C; lacks the PSPG motif (HGGPWWP) characteristic of plant UDP-glucosyltransferases needed for option B; and lacks zinc-finger (C-x2-4-C-x12-H-x3-5-H) or helix-turn-helix DNA-binding motifs expected for option A. The combination of a positive SAM-binding motif signal and the absence of motifs diagnostic of the other three enzyme classes provides a concrete, general-biology reasoning path to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The SAM-binding glycine-rich motif and the absence of competing catalytic/binding motifs are visible in the supplied sequence and interpretable with general enzymology knowledge.",
    "reason": "A model with knowledge of Rossmann-fold methyltransferase motifs can identify 'GCGVGG' as a SAM-contacting glycine-rich loop and, combined with the absence of phosphatase, glycosyltransferase, or DNA-binding signatures, reason toward option D without needing to look up this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H1",
      "H4",
      "H5",
      "H6",
      "H7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A075D6M1 (Norajmaline N-methyltransferase, RsNNMT, EC 2.1.1.392) exactly (sha256 confirmed, 292 aa). The protein's catalytic reaction is norajmaline + S-adenosyl-L-methionine → ajmaline + S-adenosyl-L-homocysteine + H+, experimentally validated (ECO:0000269, PubMed:27122470 and 38212296). GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is directly annotated to this entry. The expected answer D is fully supported by experimental evidence."
  },
  "important_caveats": [
    "The GO:0008757 annotation carries evidence code IEA:InterPro (computational/curator-inferred from domain match), but the underlying enzyme activity (N-methylation using SAM) is experimentally confirmed (ECO:0000269) in two independent publications.",
    "The protein is described as derived from a gamma-tocopherol C-methyltransferase gene family; its SAM-binding motif is somewhat degenerate relative to the most canonical 'VLDVGCGVGG' pattern, so motif recognition requires tolerance for variation.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning assessment is based solely on what is extractable from the raw sequence and general biological knowledge.",
    "The historical entry (version 36, released 2026-01-28) matches the current entry (version 38) in sequence and core annotations; no discrepancy in function assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different enzyme classes (DNA-binding transcription factor, glycosyltransferase, phosphatase, methyltransferase). The SAM-binding motif and the absence of competing diagnostic motifs cleanly favor D. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A075D6M1 (Norajmaline N-methyltransferase, RsNNMT, EC 2.1.1.392) exactly (sha256 confirmed, 292 aa). The protein's catalytic reaction is norajmaline + S-adenosyl-L-methionine → ajmaline + S-adenosyl-L-homocysteine + H+, experimentally validated (ECO:0000269, PubMed:27122470 and 38212296). GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is directly annotated to this entry. The expected answer D is fully supported by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "H1", "H4", "H5", "H6", "H7", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the glycine-rich motif 'DIGCGVGG' (~residues 95–102), which is a recognizable variant of the canonical SAM-binding motif (e.g., VLDVGCGVGG) found in the Rossmann-fold β-sheet of S-adenosylmethionine-dependent methyltransferases. Conversely, the sequence lacks the catalytic motifs of PPP-family phosphatases (GDxVHG) or PPM-family phosphatases (HxHGxDxH) needed for option C; lacks the PSPG motif (HGGPWWP) characteristic of plant UDP-glucosyltransferases needed for option B; and lacks zinc-finger (C-x2-4-C-x12-H-x3-5-H) or helix-turn-helix DNA-binding motifs expected for option A. The combination of a positive SAM-binding motif signal and the absence of motifs diagnostic of the other three enzyme classes provides a concrete, general-biology reasoning path to select D.",
    "missing_item_specific_fact": "None strictly required. The SAM-binding glycine-rich motif and the absence of competing catalytic/binding motifs are visible in the supplied sequence and interpretable with general enzymology knowledge.",
    "reason": "A model with knowledge of Rossmann-fold methyltransferase motifs can identify 'GCGVGG' as a SAM-contacting glycine-rich loop and, combined with the absence of phosphatase, glycosyltransferase, or DNA-binding signatures, reason toward option D without needing to look up this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different enzyme classes (DNA-binding transcription factor, glycosyltransferase, phosphatase, methyltransferase). The SAM-binding motif and the absence of competing diagnostic motifs cleanly favor D. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:0008757 annotation carries evidence code IEA:InterPro (computational/curator-inferred from domain match), but the underlying enzyme activity (N-methylation using SAM) is experimentally confirmed (ECO:0000269) in two independent publications.",
    "The protein is described as derived from a gamma-tocopherol C-methyltransferase gene family; its SAM-binding motif is somewhat degenerate relative to the most canonical 'VLDVGCGVGG' pattern, so motif recognition requires tolerance for variation.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning assessment is based solely on what is extractable from the raw sequence and general biological knowledge.",
    "The historical entry (version 36, released 2026-01-28) matches the current entry (version 38) in sequence and core annotations; no discrepancy in function assignment."
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

**Accession:** `A0A075D6M1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
"A0A075D6M1"
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02781.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase NNMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"2.1.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Norajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsNNMT"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"N-methyltransferase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:27122470, PubMed:38212296). Catalyzes the indole N-methylation of norajmaline to produce ajmaline (PubMed:27122470, PubMed:38212296). Also able, with a lower efficiency, to mediate the conversion of 4-methylnorajmaline to 4-methylajmaline (PubMed:27122470)"}]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79600"}}],"reaction":{"ecNumber":"2.1.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79599"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58567"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:77618"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79604"}}],"reaction":{"ecNumber":"2.1.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79603"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230509"},{"database":"ChEBI","id":"CHEBI:230510"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"database":"GO","id":"GO:0008168","properties":[{"key":"GoTerm","value":"F:methyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
ID   NNMT_RAUSE              Reviewed;         292 AA.
AC   A0A075D6M1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 36.
DE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};
GN   Name=NNMT {ECO:0000303|PubMed:38212296};
GN   Synonyms=Rs9447 {ECO:0000312|EMBL:AHH02781.1};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- FUNCTION: N-methyltransferase involved in the biosynthesis of ajmaline-
CC       type monoterpenoid indole alkaloids (MIAs) natural products, important
CC       plant-derived pharmaceuticals used in the therapy of heart disorders
CC       (PubMed:27122470, PubMed:38212296). Catalyzes the indole N-methylation
CC       of norajmaline to produce ajmaline (PubMed:27122470, PubMed:38212296).
CC       Also able, with a lower efficiency, to mediate the conversion of 4-
CC       methylnorajmaline to 4-methylajmaline (PubMed:27122470).
CC       {ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-
CC         L-homocysteine + H(+); Xref=Rhea:RHEA:79599, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:58567, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:77618; EC=2.1.1.392;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79600;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 59-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylnorajmaline + S-adenosyl-L-methionine = 4-
CC         methylajmaline + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:79603, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509, ChEBI:CHEBI:230510;
CC         EC=2.1.1.392; Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79604;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
DR   GO; GO:0008757; F:S-adenosylmethionine-dependent methyltransferase activity; IEA:InterPro.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 87421-87429`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008757
name: S-adenosylmethionine-dependent methyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a methyl group from S-adenosyl-L-methionine to a substrate." [GOC:mah]
synonym: "S-adenosyl methionine-dependent methyltransferase activity" EXACT []
synonym: "SAM-dependent methyltransferase activity" EXACT []
is_a: GO:0008168 ! methyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
