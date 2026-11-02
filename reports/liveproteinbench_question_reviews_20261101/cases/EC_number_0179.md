# EC_number_0179

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.14.14.126

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. 1.14.14.187
B. 1.14.14.126
C. 2.7.2.3
D. 5.3.3.21
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

> The supplied sequence exactly matches the UniProt entry annotated as EC 1.14.14.126. The annotation and catalytic-activity entry cite ECO:0000269 experimental evidence, describing beta-amyrin oxidation to oleanolate. The matching historical entry also carries this annotation, though the author’s exact source snapshot is unknown.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450, which makes the two EC 1.14.14.x choices more plausible than the kinase or isomerase choices. But that broad family-level inference does not distinguish the two P450 EC numbers.


**Missing item-specific fact**

> The protein-specific catalytic activity—identified in the reviewer-only evidence as beta-amyrin 28-monooxygenation to oleanolate—is needed to select EC 1.14.14.126 over 1.14.14.187.


**Reason**

> The exact EC assignment depends on substrate and reaction specificity not established by the supplied sequence and choices alone. The matching experimental annotation supports the key, but that reviewer-only information was not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the supplied information, both options are P450 EC numbers, and the sequence-level family inference does not establish which specific catalytic activity applies.


### Important caveats

- The reviewer-only evidence reports a sequence match and an experimental evidence code tied to a publication; the primary paper was not independently reviewed here.
- The actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, which makes the two EC 1.14.14.x choices more plausible than the kinase or isomerase choices. But that broad family-level inference does not distinguish the two P450 EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—identified in the reviewer-only evidence as beta-amyrin 28-monooxygenation to oleanolate—is needed to select EC 1.14.14.126 over 1.14.14.187.",
    "reason": "The exact EC assignment depends on substrate and reaction specificity not established by the supplied sequence and choices alone. The matching experimental annotation supports the key, but that reviewer-only information was not supplied to the model."
  },
  "case_id": "EC_number_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 1.14.14.126. The annotation and catalytic-activity entry cite ECO:0000269 experimental evidence, describing beta-amyrin oxidation to oleanolate. The matching historical entry also carries this annotation, though the author’s exact source snapshot is unknown."
  },
  "important_caveats": [
    "The reviewer-only evidence reports a sequence match and an experimental evidence code tied to a publication; the primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the supplied information, both options are P450 EC numbers, and the sequence-level family inference does not establish which specific catalytic activity applies."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as EC 1.14.14.126. The annotation and catalytic-activity entry cite ECO:0000269 experimental evidence, describing beta-amyrin oxidation to oleanolate. The matching historical entry also carries this annotation, though the author’s exact source snapshot is unknown.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, which makes the two EC 1.14.14.x choices more plausible than the kinase or isomerase choices. But that broad family-level inference does not distinguish the two P450 EC numbers.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—identified in the reviewer-only evidence as beta-amyrin 28-monooxygenation to oleanolate—is needed to select EC 1.14.14.126 over 1.14.14.187.",
    "reason": "The exact EC assignment depends on substrate and reaction specificity not established by the supplied sequence and choices alone. The matching experimental annotation supports the key, but that reviewer-only information was not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the supplied information, both options are P450 EC numbers, and the sequence-level family inference does not establish which specific catalytic activity applies."
  },
  "important_caveats": [
    "The reviewer-only evidence reports a sequence match and an experimental evidence code tied to a publication; the primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt entry A0AAW1NEA3 (sequence SHA256 identical). The UniProt annotation assigns EC 1.14.14.126 (Beta-amyrin 28-monooxygenase CYP716A378) with evidence code ECO:0000269 (experimental) from PubMed:39043959 (Nat. Chem. Biol. 2025). The catalytic activity (beta-amyrin → oleanolate via 3 sequential oxidations) is experimentally characterized. The expected answer B (1.14.14.126) is directly supported by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a canonical P450 heme-binding motif (FGGGPRMCPGKEY) and overall CYP716A architecture, which reliably eliminates options C (transferase, EC 2.7.2.3) and D (isomerase, EC 5.3.3.21). However, both A (1.14.14.187) and B (1.14.14.126) are P450 monooxygenases (EC class 1.14.14). Distinguishing between these two 4-digit codes requires knowing the specific substrate and oxidation position of this particular CYP716A variant, which is an experimentally determined item-specific fact.


**Missing item-specific fact**

> The identity of EC 1.14.14.187 (what specific reaction it denotes) and the experimentally determined substrate specificity of this particular Saponaria officinalis CYP716A378 variant (C-28 oxidation of beta-amyrin vs. whatever 1.14.14.187 describes) cannot be resolved from sequence alone without database lookup or memorization of the specific annotation.


**Reason**

> While general P450 identification from the heme-binding motif is reasoning-supported, the final 4-digit EC assignment between two P450 monooxygenase codes (1.14.14.187 vs 1.14.14.126) depends on knowing which specific triterpenoid oxidation reaction this enzyme variant performs, an experimental characterization from PubMed:39043959 that is not derivable from the sequence without external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly wrong for a P450. Between A and B, only B is supported by experimental evidence for this specific sequence. If EC 1.14.14.187 does not correspond to a reaction this enzyme performs, then B is uniquely correct. No genuine ambiguity exists in the correct answer, though the A-vs-B distinction is difficult from sequence alone.


### Important caveats

- EC 1.14.14.187 may be a very recently assigned or obscure EC number; its exact definition was not verified in the supplied evidence.
- The CYP716A family association with beta-amyrin 28-oxidation in saponin-producing plants provides a weak general heuristic favoring 1.14.14.126, but does not constitute a rigorous sequence-based distinction from 1.14.14.187.
- The UniProt annotation carries experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.
- The identity of the protein (Saponaria officinalis CYP716A378) was inferred by the reviewer from accession metadata absent from the model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGPRMCPGKEY) and overall CYP716A architecture, which reliably eliminates options C (transferase, EC 2.7.2.3) and D (isomerase, EC 5.3.3.21). However, both A (1.14.14.187) and B (1.14.14.126) are P450 monooxygenases (EC class 1.14.14). Distinguishing between these two 4-digit codes requires knowing the specific substrate and oxidation position of this particular CYP716A variant, which is an experimentally determined item-specific fact.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of EC 1.14.14.187 (what specific reaction it denotes) and the experimentally determined substrate specificity of this particular Saponaria officinalis CYP716A378 variant (C-28 oxidation of beta-amyrin vs. whatever 1.14.14.187 describes) cannot be resolved from sequence alone without database lookup or memorization of the specific annotation.",
    "reason": "While general P450 identification from the heme-binding motif is reasoning-supported, the final 4-digit EC assignment between two P450 monooxygenase codes (1.14.14.187 vs 1.14.14.126) depends on knowing which specific triterpenoid oxidation reaction this enzyme variant performs, an experimental characterization from PubMed:39043959 that is not derivable from the sequence without external knowledge."
  },
  "case_id": "EC_number_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0AAW1NEA3 (sequence SHA256 identical). The UniProt annotation assigns EC 1.14.14.126 (Beta-amyrin 28-monooxygenase CYP716A378) with evidence code ECO:0000269 (experimental) from PubMed:39043959 (Nat. Chem. Biol. 2025). The catalytic activity (beta-amyrin → oleanolate via 3 sequential oxidations) is experimentally characterized. The expected answer B (1.14.14.126) is directly supported by experimental evidence."
  },
  "important_caveats": [
    "EC 1.14.14.187 may be a very recently assigned or obscure EC number; its exact definition was not verified in the supplied evidence.",
    "The CYP716A family association with beta-amyrin 28-oxidation in saponin-producing plants provides a weak general heuristic favoring 1.14.14.126, but does not constitute a rigorous sequence-based distinction from 1.14.14.187.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.",
    "The identity of the protein (Saponaria officinalis CYP716A378) was inferred by the reviewer from accession metadata absent from the model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly wrong for a P450. Between A and B, only B is supported by experimental evidence for this specific sequence. If EC 1.14.14.187 does not correspond to a reaction this enzyme performs, then B is uniquely correct. No genuine ambiguity exists in the correct answer, though the A-vs-B distinction is difficult from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0AAW1NEA3 (sequence SHA256 identical). The UniProt annotation assigns EC 1.14.14.126 (Beta-amyrin 28-monooxygenase CYP716A378) with evidence code ECO:0000269 (experimental) from PubMed:39043959 (Nat. Chem. Biol. 2025). The catalytic activity (beta-amyrin → oleanolate via 3 sequential oxidations) is experimentally characterized. The expected answer B (1.14.14.126) is directly supported by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a canonical P450 heme-binding motif (FGGGPRMCPGKEY) and overall CYP716A architecture, which reliably eliminates options C (transferase, EC 2.7.2.3) and D (isomerase, EC 5.3.3.21). However, both A (1.14.14.187) and B (1.14.14.126) are P450 monooxygenases (EC class 1.14.14). Distinguishing between these two 4-digit codes requires knowing the specific substrate and oxidation position of this particular CYP716A variant, which is an experimentally determined item-specific fact.",
    "missing_item_specific_fact": "The identity of EC 1.14.14.187 (what specific reaction it denotes) and the experimentally determined substrate specificity of this particular Saponaria officinalis CYP716A378 variant (C-28 oxidation of beta-amyrin vs. whatever 1.14.14.187 describes) cannot be resolved from sequence alone without database lookup or memorization of the specific annotation.",
    "reason": "While general P450 identification from the heme-binding motif is reasoning-supported, the final 4-digit EC assignment between two P450 monooxygenase codes (1.14.14.187 vs 1.14.14.126) depends on knowing which specific triterpenoid oxidation reaction this enzyme variant performs, an experimental characterization from PubMed:39043959 that is not derivable from the sequence without external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly wrong for a P450. Between A and B, only B is supported by experimental evidence for this specific sequence. If EC 1.14.14.187 does not correspond to a reaction this enzyme performs, then B is uniquely correct. No genuine ambiguity exists in the correct answer, though the A-vs-B distinction is difficult from sequence alone."
  },
  "important_caveats": [
    "EC 1.14.14.187 may be a very recently assigned or obscure EC number; its exact definition was not verified in the supplied evidence.",
    "The CYP716A family association with beta-amyrin 28-oxidation in saponin-producing plants provides a weak general heuristic favoring 1.14.14.126, but does not constitute a rigorous sequence-based distinction from 1.14.14.187.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.",
    "The identity of the protein (Saponaria officinalis CYP716A378) was inferred by the reviewer from accession metadata absent from the model input."
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

**Accession:** `A0AAW1NEA3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cytochrome P450 716A378"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCYP716A378"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.126"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Beta-amyrin 28-monooxygenase CYP716A378"}}}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:43069"}}],"reaction":{"ecNumber":"1.14.14.126","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"name":"beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43068"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:10352"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:82828"}]}}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.776537+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48148.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
DE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};
DE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};
DE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};
DE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.561544+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2
CC         = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4
CC         H(+); Xref=Rhea:RHEA:43068, Rhea:RHEA-COMP:11964, Rhea:RHEA-
CC         COMP:11965, ChEBI:CHEBI:10352, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:82828; EC=1.14.14.126;
CC         Evidence={ECO:0000269|PubMed:39043959};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:43069;
CC         Evidence={ECO:0000269|PubMed:39043959};
```

Source SHA-256: `8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
