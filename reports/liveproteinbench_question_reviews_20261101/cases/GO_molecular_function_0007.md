# GO_molecular_function_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — metal ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. glycosyltransferase activity
B. CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity
C. mechanosensitive monoatomic cation channel activity
D. metal ion binding
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

> The supplied sequence matches the protein entry, which is annotated as zinc ion binding with experimental evidence; zinc binding supports the broader option D, metal ion binding. The historical entry also carried a metal ion binding annotation, though that annotation was computationally assigned.

Citations as saved: [C8](#evidence-c8), [H4](#evidence-h4), [C1](#evidence-c1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices alone do not provide a clear, specific basis for identifying metal binding over the alternatives. A general sequence-based inference would not establish this protein's metal-binding function.


**Missing item-specific fact**

> That this particular protein is a zinc-dependent metalloprotease and binds a metal ion.


**Reason**

> Selecting D depends on protein-specific functional knowledge or annotation not supplied in the question. Recognizing the exact sequence or relying on an unspecified predictor would be lookup or memorization, not reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, metal ion binding is supported. The protein's catalytic peptidase activity is not offered, so D is the supported listed option, although it describes metal binding rather than the protein's catalytic activity.


### Important caveats

- The historical metal-ion-binding annotation is computationally assigned; the current zinc-ion-binding annotation is supported by experimental evidence.
- The exact author source snapshot is unknown, but the matched historical entry already includes the broader metal-ion-binding annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices alone do not provide a clear, specific basis for identifying metal binding over the alternatives. A general sequence-based inference would not establish this protein's metal-binding function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein is a zinc-dependent metalloprotease and binds a metal ion.",
    "reason": "Selecting D depends on protein-specific functional knowledge or annotation not supplied in the question. Recognizing the exact sequence or relying on an unspecified predictor would be lookup or memorization, not reasoning from the provided evidence."
  },
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the protein entry, which is annotated as zinc ion binding with experimental evidence; zinc binding supports the broader option D, metal ion binding. The historical entry also carried a metal ion binding annotation, though that annotation was computationally assigned."
  },
  "important_caveats": [
    "The historical metal-ion-binding annotation is computationally assigned; the current zinc-ion-binding annotation is supported by experimental evidence.",
    "The exact author source snapshot is unknown, but the matched historical entry already includes the broader metal-ion-binding annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported. The protein's catalytic peptidase activity is not offered, so D is the supported listed option, although it describes metal binding rather than the protein's catalytic activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the protein entry, which is annotated as zinc ion binding with experimental evidence; zinc binding supports the broader option D, metal ion binding. The historical entry also carried a metal ion binding annotation, though that annotation was computationally assigned.",
    "evidence_ids": ["C8", "H4", "C1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices alone do not provide a clear, specific basis for identifying metal binding over the alternatives. A general sequence-based inference would not establish this protein's metal-binding function.",
    "missing_item_specific_fact": "That this particular protein is a zinc-dependent metalloprotease and binds a metal ion.",
    "reason": "Selecting D depends on protein-specific functional knowledge or annotation not supplied in the question. Recognizing the exact sequence or relying on an unspecified predictor would be lookup or memorization, not reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, metal ion binding is supported. The protein's catalytic peptidase activity is not offered, so D is the supported listed option, although it describes metal binding rather than the protein's catalytic activity."
  },
  "important_caveats": [
    "The historical metal-ion-binding annotation is computationally assigned; the current zinc-ion-binding annotation is supported by experimental evidence.",
    "The exact author source snapshot is unknown, but the matched historical entry already includes the broader metal-ion-binding annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein E0N688 (MPG_NEIM3) is annotated with GO:0046872 (metal ion binding) in UniProt. More specifically, GO:0008270 (zinc ion binding) is annotated with IDA (Inferred from Direct Assay) evidence from the crystal structure PDB 3SLU solved in complex with nickel, confirming experimental demonstration of metal coordination. The protein is a zinc metalloprotease (DD-carboxypeptidase/endopeptidase Mpg) that requires zinc as a catalytic cofactor. GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the broader term applies. While the primary catalytic function is metalloendopeptidase activity (GO:0004222), metal ion binding is a valid and experimentally supported molecular function annotation for this protein.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4), [GO5](#evidence-go5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple H-x-H motifs (e.g., 'HPILHTWRLHTG', 'IRHANGVETLYAHLS', 'RSTGPHLHYEARING') characteristic of zinc-binding sites in metalloproteases. The N-terminal hydrophobic signal peptide and overall architecture are consistent with a bacterial outer membrane/periplasmic protein. A zinc metalloprotease by definition binds a metal ion cofactor. The three distractors are clearly incompatible: glycosyltransferases require DXD/NDxD motifs and a GT fold; CDP-diacylglycerol phosphatidyltransferases are integral membrane enzymes with distinct topology; mechanosensitive cation channels require multiple transmembrane helices with a pore-forming architecture absent here. Elimination plus identification of metal-binding motifs supports D.


**Missing item-specific fact**

> None strictly required. The H-x-H motifs and the absence of features diagnostic of the other three options provide sufficient grounds. However, confirming this is specifically a peptidase (rather than another metal-binding protein) would require recognizing the full metalloprotease fold, which adds some difficulty but does not change the answer among the given choices.


**Reason**

> The sequence provides identifiable metal-binding motifs (H-x-H patterns) and lacks features of the three distractor functions. General knowledge of metalloprotease sequence signatures and the structural requirements of glycosyltransferases, phosphatidyltransferases, and mechanosensitive channels allow a model to eliminate A, B, and C and select D through reasoning rather than memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only D (metal ion binding) is compatible with a zinc metalloprotease. The other three options describe functions with entirely different sequence/structural requirements that are absent from this protein. No ambiguity among the given options.


### Important caveats

- The question asks for 'primary molecular function,' but the true primary function is metalloendopeptidase/metallocarboxypeptidase activity (GO:0004222/GO:0004181), not metal ion binding per se. Metal ion binding is a secondary/auxiliary annotation. However, since peptidase activity is not among the choices, D remains the only correct option.
- The GO:0046872 annotation carries evidence code IEA:UniProtKB-KW (automatic keyword-based), while the more specific zinc ion binding (GO:0008270) has IDA evidence from crystallography. The broader term is thus computationally assigned but supported by the narrower experimental annotation.
- The crystal structure (3SLU) was solved in complex with nickel (a crystallization artifact), not zinc. The zinc-binding assignment is inferred from sequence motifs and the metalloprotease family classification rather than direct observation of zinc in the crystal.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPILHTWRLHTG', 'IRHANGVETLYAHLS', 'RSTGPHLHYEARING') characteristic of zinc-binding sites in metalloproteases. The N-terminal hydrophobic signal peptide and overall architecture are consistent with a bacterial outer membrane/periplasmic protein. A zinc metalloprotease by definition binds a metal ion cofactor. The three distractors are clearly incompatible: glycosyltransferases require DXD/NDxD motifs and a GT fold; CDP-diacylglycerol phosphatidyltransferases are integral membrane enzymes with distinct topology; mechanosensitive cation channels require multiple transmembrane helices with a pore-forming architecture absent here. Elimination plus identification of metal-binding motifs supports D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The H-x-H motifs and the absence of features diagnostic of the other three options provide sufficient grounds. However, confirming this is specifically a peptidase (rather than another metal-binding protein) would require recognizing the full metalloprotease fold, which adds some difficulty but does not change the answer among the given choices.",
    "reason": "The sequence provides identifiable metal-binding motifs (H-x-H patterns) and lacks features of the three distractor functions. General knowledge of metalloprotease sequence signatures and the structural requirements of glycosyltransferases, phosphatidyltransferases, and mechanosensitive channels allow a model to eliminate A, B, and C and select D through reasoning rather than memorizing this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "C9",
      "H4",
      "H5",
      "GO4",
      "GO5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein E0N688 (MPG_NEIM3) is annotated with GO:0046872 (metal ion binding) in UniProt. More specifically, GO:0008270 (zinc ion binding) is annotated with IDA (Inferred from Direct Assay) evidence from the crystal structure PDB 3SLU solved in complex with nickel, confirming experimental demonstration of metal coordination. The protein is a zinc metalloprotease (DD-carboxypeptidase/endopeptidase Mpg) that requires zinc as a catalytic cofactor. GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the broader term applies. While the primary catalytic function is metalloendopeptidase activity (GO:0004222), metal ion binding is a valid and experimentally supported molecular function annotation for this protein."
  },
  "important_caveats": [
    "The question asks for 'primary molecular function,' but the true primary function is metalloendopeptidase/metallocarboxypeptidase activity (GO:0004222/GO:0004181), not metal ion binding per se. Metal ion binding is a secondary/auxiliary annotation. However, since peptidase activity is not among the choices, D remains the only correct option.",
    "The GO:0046872 annotation carries evidence code IEA:UniProtKB-KW (automatic keyword-based), while the more specific zinc ion binding (GO:0008270) has IDA evidence from crystallography. The broader term is thus computationally assigned but supported by the narrower experimental annotation.",
    "The crystal structure (3SLU) was solved in complex with nickel (a crystallization artifact), not zinc. The zinc-binding assignment is inferred from sequence motifs and the metalloprotease family classification rather than direct observation of zinc in the crystal."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D (metal ion binding) is compatible with a zinc metalloprotease. The other three options describe functions with entirely different sequence/structural requirements that are absent from this protein. No ambiguity among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein E0N688 (MPG_NEIM3) is annotated with GO:0046872 (metal ion binding) in UniProt. More specifically, GO:0008270 (zinc ion binding) is annotated with IDA (Inferred from Direct Assay) evidence from the crystal structure PDB 3SLU solved in complex with nickel, confirming experimental demonstration of metal coordination. The protein is a zinc metalloprotease (DD-carboxypeptidase/endopeptidase Mpg) that requires zinc as a catalytic cofactor. GO:0008270 is_a GO:0046914 (transition metal ion binding) is_a GO:0046872 (metal ion binding), so the broader term applies. While the primary catalytic function is metalloendopeptidase activity (GO:0004222), metal ion binding is a valid and experimentally supported molecular function annotation for this protein.",
    "evidence_ids": ["C4", "C8", "C9", "H4", "H5", "GO4", "GO5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPILHTWRLHTG', 'IRHANGVETLYAHLS', 'RSTGPHLHYEARING') characteristic of zinc-binding sites in metalloproteases. The N-terminal hydrophobic signal peptide and overall architecture are consistent with a bacterial outer membrane/periplasmic protein. A zinc metalloprotease by definition binds a metal ion cofactor. The three distractors are clearly incompatible: glycosyltransferases require DXD/NDxD motifs and a GT fold; CDP-diacylglycerol phosphatidyltransferases are integral membrane enzymes with distinct topology; mechanosensitive cation channels require multiple transmembrane helices with a pore-forming architecture absent here. Elimination plus identification of metal-binding motifs supports D.",
    "missing_item_specific_fact": "None strictly required. The H-x-H motifs and the absence of features diagnostic of the other three options provide sufficient grounds. However, confirming this is specifically a peptidase (rather than another metal-binding protein) would require recognizing the full metalloprotease fold, which adds some difficulty but does not change the answer among the given choices.",
    "reason": "The sequence provides identifiable metal-binding motifs (H-x-H patterns) and lacks features of the three distractor functions. General knowledge of metalloprotease sequence signatures and the structural requirements of glycosyltransferases, phosphatidyltransferases, and mechanosensitive channels allow a model to eliminate A, B, and C and select D through reasoning rather than memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D (metal ion binding) is compatible with a zinc metalloprotease. The other three options describe functions with entirely different sequence/structural requirements that are absent from this protein. No ambiguity among the given options."
  },
  "important_caveats": [
    "The question asks for 'primary molecular function,' but the true primary function is metalloendopeptidase/metallocarboxypeptidase activity (GO:0004222/GO:0004181), not metal ion binding per se. Metal ion binding is a secondary/auxiliary annotation. However, since peptidase activity is not among the choices, D remains the only correct option.",
    "The GO:0046872 annotation carries evidence code IEA:UniProtKB-KW (automatic keyword-based), while the more specific zinc ion binding (GO:0008270) has IDA evidence from crystallography. The broader term is thus computationally assigned but supported by the narrower experimental annotation.",
    "The crystal structure (3SLU) was solved in complex with nickel (a crystallization artifact), not zinc. The zinc-binding assignment is inferred from sequence motifs and the metalloprotease family classification rather than direct observation of zinc in the crystal."
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

**Accession:** `E0N688` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
"E0N688"
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"Metalloprotease active against peptidoglycan"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Outer membrane protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"OMP"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metallopeptidase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metalloprotease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Zinc-dependent metallopeptidase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.17.-"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DD-carboxypeptidase/endopeptidase Mpg"}}}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22046377","source":"PubMed"}],"id":"GO:0008270","properties":[{"key":"GoTerm","value":"F:zinc ion binding"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"citation":{"authors":["Wang X.","Yang X.","Yang C.","Wu Z.","Xu H.","Shen Y."],"citationCrossReferences":[{"database":"PubMed","id":"22046377"},{"database":"DOI","id":"10.1371/journal.pone.0026845"}],"citationType":"journal article","firstPage":"e26845","id":"22046377","journal":"PLoS ONE","lastPage":"e26845","publicationDate":"2011","title":"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3SLU","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"type":"STRAIN","value":"ATCC 13091 / M2091"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL","COFACTOR","SUBUNIT","SUBCELLULAR LOCATION","PTM"]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
DR   GO; GO:0004222; F:metalloendopeptidase activity; IEA:TreeGrafter.
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 81431-81439`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008270
name: zinc ion binding
namespace: molecular_function
def: "Binding to a zinc ion (Zn)." [GOC:ai]
synonym: "zinc binding" EXACT []
synonym: "Zn binding" EXACT []
is_a: GO:0046914 ! transition metal ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 281280-281292`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046872
name: metal ion binding
namespace: molecular_function
def: "Binding to a metal ion." [GOC:ai]
subset: goslim_agr
subset: goslim_drosophila
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
synonym: "heavy metal binding" NARROW []
synonym: "metal binding" EXACT []
is_a: GO:0043169 ! cation binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 281764-281770`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046914
name: transition metal ion binding
namespace: molecular_function
def: "Binding to a transition metal ions; a transition metal is an element whose atom has an incomplete d-subshell of extranuclear electrons, or which gives rise to a cation or cations with an incomplete d-subshell. Transition metals often have more than one valency state. Biologically relevant transition metals include vanadium, manganese, iron, copper, cobalt, nickel, molybdenum and silver." [ISBN:0198506732]
is_a: GO:0046872 ! metal ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
