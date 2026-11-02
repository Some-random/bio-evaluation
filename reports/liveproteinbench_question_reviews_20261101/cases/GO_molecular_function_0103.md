# GO_molecular_function_0103

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — tetraketide alpha-pyrone synthase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADLGFGDARSGNGSRSQCSRGKAMLLALGKGLPEQVLPQEKVVETYLQDTICDDPATRAKLERLCKTTTVRTRYTVMSKELLDEHPELRTEGTPTLTPRLDICNAAVLELGATAARAALGEWGRPAADITHLVYISSSELRLPGGDLFLATRLGLHPNTVRTSLLFLGCSGGAAALRTAKDIAENNPGSRVLVVAAETTVLGFRPPSPDRPYDLVGAALFGDGASAAIIGAGPIAAEESPFLELQFSTQEFLPGTDKVIDGKITEEGINFKLGRDLPEKIENRIEGFCRTLMDRVGIKEFNDVFWAVHPGGPAILNRLEVCLELQPEKLKISRKALMNYGNVSSNTVFYVLEYLRDELKKGMIREEWGLILAFGPGITFEGMLVRGIN

[Multiple Choices]
A. hydrolase activity, acting on glycosyl bonds
B. tetraketide alpha-pyrone synthase activity
C. mechanosensitive monoatomic cation channel activity
D. ATP hydrolysis activity
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

> The supplied sequence exactly matches the archived and current UniProt sequence for the rice protein. Its annotation reports experimentally supported production of triketide and tetraketide alpha-pyrones, and assigns tetraketide alpha-pyrone synthase activity. This supports B, while the exact author source snapshot is unknown.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble type III polyketide synthase, which makes B more plausible than a glycosyl-bond hydrolase, mechanosensitive channel, or ATPase. But that family-level inference does not establish this protein's specific tetraketide alpha-pyrone activity.


**Missing item-specific fact**

> Evidence that this particular protein catalyzes formation of tetraketide alpha-pyrones, such as a protein-specific functional annotation or experimental product assay.


**Reason**

> The sequence and choices provide a useful broad family-level clue, but the keyed GO activity is more specific than that clue establishes. Selecting B as that precise activity depends on a protein-specific fact absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only option consistent with the protein's supported function; the other options describe unrelated activity classes.


### Important caveats

- The reviewed experimental and annotation evidence was not supplied to the evaluated model.
- The author’s exact source snapshot is unknown, although the sequence matches the historical UniProt record available by the stated cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble type III polyketide synthase, which makes B more plausible than a glycosyl-bond hydrolase, mechanosensitive channel, or ATPase. But that family-level inference does not establish this protein's specific tetraketide alpha-pyrone activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Evidence that this particular protein catalyzes formation of tetraketide alpha-pyrones, such as a protein-specific functional annotation or experimental product assay.",
    "reason": "The sequence and choices provide a useful broad family-level clue, but the keyed GO activity is more specific than that clue establishes. Selecting B as that precise activity depends on a protein-specific fact absent from the original input."
  },
  "case_id": "GO_molecular_function_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for the rice protein. Its annotation reports experimentally supported production of triketide and tetraketide alpha-pyrones, and assigns tetraketide alpha-pyrone synthase activity. This supports B, while the exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The reviewed experimental and annotation evidence was not supplied to the evaluated model.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical UniProt record available by the stated cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only option consistent with the protein's supported function; the other options describe unrelated activity classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for the rice protein. Its annotation reports experimentally supported production of triketide and tetraketide alpha-pyrones, and assigns tetraketide alpha-pyrone synthase activity. This supports B, while the exact author source snapshot is unknown.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble type III polyketide synthase, which makes B more plausible than a glycosyl-bond hydrolase, mechanosensitive channel, or ATPase. But that family-level inference does not establish this protein's specific tetraketide alpha-pyrone activity.",
    "missing_item_specific_fact": "Evidence that this particular protein catalyzes formation of tetraketide alpha-pyrones, such as a protein-specific functional annotation or experimental product assay.",
    "reason": "The sequence and choices provide a useful broad family-level clue, but the keyed GO activity is more specific than that clue establishes. Selecting B as that precise activity depends on a protein-specific fact absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only option consistent with the protein's supported function; the other options describe unrelated activity classes."
  },
  "important_caveats": [
    "The reviewed experimental and annotation evidence was not supplied to the evaluated model.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical UniProt record available by the stated cutoff."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt A3C5V6 (PKS21_ORYSJ, Type III polyketide synthase 21 from Oryza sativa). The UniProt entry carries GO:0090439 'tetraketide alpha-pyrone synthase activity' annotated with evidence code IDA:UniProtKB, derived from experimental data (PubMed:23231646, ECO:0000269 direct assay). The FUNCTION comment explicitly states the enzyme 'catalyzes the condensation of fatty acyl-CoA with malonyl-CoA to generate triketide and tetraketide alpha-pyrones.' The GO term definition (GO:0090439) describes the exact reaction catalyzed. The annotation is experimentally supported, not merely computational.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~389 aa) contains hallmarks of the type III polyketide synthase / chalcone synthase superfamily: a GAG motif (…AALFGDGASAAIIGAGPIAAEESPFLELQFSTQEF…), a GCSGGAA-like active-site region, and the overall length and fold architecture typical of plant type III PKS enzymes. None of the distractors match this protein class: (C) mechanosensitive cation channels require multiple transmembrane helices absent here; (D) ATP hydrolysis requires Walker A (GxxxxGK&#91;ST&#93;) and Walker B motifs, which are absent; (A) glycosyl hydrolases require characteristic catalytic motifs (e.g., the GH-family (V/I)-X-W-Y-D-E signature) not present. The only option consistent with a transferase/synthase enzyme of the PKS family is B. A biologist recognizing the PKS fold and catalytic architecture can eliminate A, C, and D and select B without needing to know the exact GO term name.


**Missing item-specific fact**

> The precise product specificity (tetraketide vs. triketide alpha-pyrone) and the exact GO term name 'tetraketide alpha-pyrone synthase activity' are experimentally determined for this specific enzyme (OsPKS21) and cannot be deduced from sequence alone. However, this does not affect answer selection because B is the sole transferase/synthase option among the four choices.


**Reason**

> The four options span four distinct functional classes (glycosidase, PKS synthase, ion channel, ATPase). Sequence-level recognition of the type III PKS family (length, GAG motif, active-site architecture, absence of TM helices, absence of Walker motifs, absence of glycosidase motifs) provides a concrete biological argument to select B and eliminate A, C, D. The reasoning does not require memorizing the UniProt entry for A3C5V6.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to mutually exclusive functional categories (hydrolase, transferase/synthase, ion channel, ATPase). Once the protein is recognized as a type III PKS-family enzyme, only B is consistent. No other option is defensible for a soluble plant PKS with no transmembrane segments, no ATP-binding motifs, and no glycosidase catalytic residues.


### Important caveats

- The specific 'tetraketide alpha-pyrone' product specificity is an experimentally determined property (PubMed:23231646) that cannot be inferred from sequence alone; however, it is irrelevant here because B is the only synthase/transferase option.
- The UniProt entry was first publicly released 2025-04-09; the author's data-construction date and exact source snapshot are unknown, though the sequence version has been stable since 2020-02-26.
- The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.
- A model that fails to recognize the PKS family from the sequence would lack a reasoning path and would be forced to guess among four unrelated options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~389 aa) contains hallmarks of the type III polyketide synthase / chalcone synthase superfamily: a GAG motif (…AALFGDGASAAIIGAGPIAAEESPFLELQFSTQEF…), a GCSGGAA-like active-site region, and the overall length and fold architecture typical of plant type III PKS enzymes. None of the distractors match this protein class: (C) mechanosensitive cation channels require multiple transmembrane helices absent here; (D) ATP hydrolysis requires Walker A (GxxxxGK[ST]) and Walker B motifs, which are absent; (A) glycosyl hydrolases require characteristic catalytic motifs (e.g., the GH-family (V/I)-X-W-Y-D-E signature) not present. The only option consistent with a transferase/synthase enzyme of the PKS family is B. A biologist recognizing the PKS fold and catalytic architecture can eliminate A, C, and D and select B without needing to know the exact GO term name.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise product specificity (tetraketide vs. triketide alpha-pyrone) and the exact GO term name 'tetraketide alpha-pyrone synthase activity' are experimentally determined for this specific enzyme (OsPKS21) and cannot be deduced from sequence alone. However, this does not affect answer selection because B is the sole transferase/synthase option among the four choices.",
    "reason": "The four options span four distinct functional classes (glycosidase, PKS synthase, ion channel, ATPase). Sequence-level recognition of the type III PKS family (length, GAG motif, active-site architecture, absence of TM helices, absence of Walker motifs, absence of glycosidase motifs) provides a concrete biological argument to select B and eliminate A, C, D. The reasoning does not require memorizing the UniProt entry for A3C5V6."
  },
  "case_id": "GO_molecular_function_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A3C5V6 (PKS21_ORYSJ, Type III polyketide synthase 21 from Oryza sativa). The UniProt entry carries GO:0090439 'tetraketide alpha-pyrone synthase activity' annotated with evidence code IDA:UniProtKB, derived from experimental data (PubMed:23231646, ECO:0000269 direct assay). The FUNCTION comment explicitly states the enzyme 'catalyzes the condensation of fatty acyl-CoA with malonyl-CoA to generate triketide and tetraketide alpha-pyrones.' The GO term definition (GO:0090439) describes the exact reaction catalyzed. The annotation is experimentally supported, not merely computational."
  },
  "important_caveats": [
    "The specific 'tetraketide alpha-pyrone' product specificity is an experimentally determined property (PubMed:23231646) that cannot be inferred from sequence alone; however, it is irrelevant here because B is the only synthase/transferase option.",
    "The UniProt entry was first publicly released 2025-04-09; the author's data-construction date and exact source snapshot are unknown, though the sequence version has been stable since 2020-02-26.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.",
    "A model that fails to recognize the PKS family from the sequence would lack a reasoning path and would be forced to guess among four unrelated options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to mutually exclusive functional categories (hydrolase, transferase/synthase, ion channel, ATPase). Once the protein is recognized as a type III PKS-family enzyme, only B is consistent. No other option is defensible for a soluble plant PKS with no transmembrane segments, no ATP-binding motifs, and no glycosidase catalytic residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A3C5V6 (PKS21_ORYSJ, Type III polyketide synthase 21 from Oryza sativa). The UniProt entry carries GO:0090439 'tetraketide alpha-pyrone synthase activity' annotated with evidence code IDA:UniProtKB, derived from experimental data (PubMed:23231646, ECO:0000269 direct assay). The FUNCTION comment explicitly states the enzyme 'catalyzes the condensation of fatty acyl-CoA with malonyl-CoA to generate triketide and tetraketide alpha-pyrones.' The GO term definition (GO:0090439) describes the exact reaction catalyzed. The annotation is experimentally supported, not merely computational.",
    "evidence_ids": ["C5", "C6", "C8", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~389 aa) contains hallmarks of the type III polyketide synthase / chalcone synthase superfamily: a GAG motif (…AALFGDGASAAIIGAGPIAAEESPFLELQFSTQEF…), a GCSGGAA-like active-site region, and the overall length and fold architecture typical of plant type III PKS enzymes. None of the distractors match this protein class: (C) mechanosensitive cation channels require multiple transmembrane helices absent here; (D) ATP hydrolysis requires Walker A (GxxxxGK[ST]) and Walker B motifs, which are absent; (A) glycosyl hydrolases require characteristic catalytic motifs (e.g., the GH-family (V/I)-X-W-Y-D-E signature) not present. The only option consistent with a transferase/synthase enzyme of the PKS family is B. A biologist recognizing the PKS fold and catalytic architecture can eliminate A, C, and D and select B without needing to know the exact GO term name.",
    "missing_item_specific_fact": "The precise product specificity (tetraketide vs. triketide alpha-pyrone) and the exact GO term name 'tetraketide alpha-pyrone synthase activity' are experimentally determined for this specific enzyme (OsPKS21) and cannot be deduced from sequence alone. However, this does not affect answer selection because B is the sole transferase/synthase option among the four choices.",
    "reason": "The four options span four distinct functional classes (glycosidase, PKS synthase, ion channel, ATPase). Sequence-level recognition of the type III PKS family (length, GAG motif, active-site architecture, absence of TM helices, absence of Walker motifs, absence of glycosidase motifs) provides a concrete biological argument to select B and eliminate A, C, D. The reasoning does not require memorizing the UniProt entry for A3C5V6."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to mutually exclusive functional categories (hydrolase, transferase/synthase, ion channel, ATPase). Once the protein is recognized as a type III PKS-family enzyme, only B is consistent. No other option is defensible for a soluble plant PKS with no transmembrane segments, no ATP-binding motifs, and no glycosidase catalytic residues."
  },
  "important_caveats": [
    "The specific 'tetraketide alpha-pyrone' product specificity is an experimentally determined property (PubMed:23231646) that cannot be inferred from sequence alone; however, it is irrelevant here because B is the only synthase/transferase option.",
    "The UniProt entry was first publicly released 2025-04-09; the author's data-construction date and exact source snapshot are unknown, though the sequence version has been stable since 2020-02-26.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.",
    "A model that fails to recognize the PKS family from the sequence would lack a reasoning path and would be forced to guess among four unrelated options."
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

**Accession:** `A3C5V6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3C5V6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:54.541030+00:00.  

```json
"A3C5V6"
```

Source SHA-256: `24e629887190629f6a1e145cce4db690436ccf4a390ec2b8db579019f118d0e1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3C5V6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:54.541030+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23231646","source":"PubMed"}],"value":"Plant type III polyketide synthases (PKSs) that catalyzes the condensation of fatty acyl-CoA with malonyl-CoA to generate triketide and tetraketide alpha-pyrones, the main components of pollen exine and potential sporopollenin precursors"}]}
```

Source SHA-256: `24e629887190629f6a1e145cce4db690436ccf4a390ec2b8db579019f118d0e1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3C5V6.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:54.541030+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"23231646","source":"PubMed"}],"id":"GO:0090439","properties":[{"key":"GoTerm","value":"F:tetraketide alpha-pyrone synthase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `24e629887190629f6a1e145cce4db690436ccf4a390ec2b8db579019f118d0e1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3C5V6.json)  
**Locator:** `/references/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:54.541030+00:00.  

```json
{"citation":{"authors":["Wang Y.","Lin Y.C.","So J.","Du Y.","Lo C."],"citationCrossReferences":[{"database":"PubMed","id":"23231646"},{"database":"DOI","id":"10.1111/ppl.12018"}],"citationType":"journal article","firstPage":"13","id":"23231646","journal":"Physiol. Plantarum","lastPage":"24","publicationDate":"2013","title":"Conserved metabolic steps for sporopollenin precursor formation in tobacco and rice.","volume":"149"},"referenceNumber":9,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `24e629887190629f6a1e145cce4db690436ccf4a390ec2b8db579019f118d0e1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3C5V6?format=txt&versions=25)  
**Locator:** `lines 121-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:26:59.743061+00:00.  

```text
CC   -!- FUNCTION: Plant type III polyketide synthases (PKSs) that catalyzes the
CC       condensation of fatty acyl-CoA with malonyl-CoA to generate triketide
CC       and tetraketide alpha-pyrones, the main components of pollen exine and
CC       potential sporopollenin precursors. {ECO:0000269|PubMed:23231646}.
```

Source SHA-256: `4afc31422b2888d90222ca4f1f0e622064aaa08e0b35c195a6dbb59e15f20f0f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3C5V6?format=txt&versions=25)  
**Locator:** `lines 158-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:26:59.743061+00:00.  

```text
DR   GO; GO:0090439; F:tetraketide alpha-pyrone synthase activity; IDA:UniProtKB.
```

Source SHA-256: `4afc31422b2888d90222ca4f1f0e622064aaa08e0b35c195a6dbb59e15f20f0f`.

### Evidence GO3

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
