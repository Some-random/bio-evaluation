# GO_molecular_function_0130

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — translation regulator activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASDQLRFLGSLEGHKGWVTAIATSQENPDMILTASRDKTIIVWQLTRDEDSYGYPKRILTGHNHFVSDVVISSDGQFALSSSWDHTLRLWDLNTGATTRRFVGHTSDVLSVSFSADNRQIVSGSRDKTIKLWNTLGECKYDIKDECHTEWVSCVRFSPNVSNPVIVSCGWDRVVKVWELSKFKLKTNHYGHTGYINTVSVSPDGSLAASGGKDGITMLWDLNEGKHLYSLEAGDIVNALVFSPNRYWLCAATASCVKIFDLESKSIVDELKPAYTDVQDEGRQPECVSIAWSADGQTLFAGFTDNQLRVWTVTS

[Multiple Choices]
A. aspartic-type endopeptidase activity
B. glycosaminoglycan binding
C. phosphoglycolate phosphatase activity
D. translation regulator activity
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

> The exact-match sequence has a historical UniProt annotation for translation regulator activity, assigned by InterPro (computational evidence). Its record also describes a ribosome-associated protein and reports regulation of gene expression, though those facts do not independently establish the precise molecular-function term experimentally.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The WD-repeat-rich sequence may suggest a protein-interaction scaffold, but that does not meaningfully distinguish translation regulation from other regulatory or binding functions among the options.


**Missing item-specific fact**

> The identity-specific InterPro/GO annotation linking this sequence to translation regulator activity, or equivalent protein-specific functional evidence.


**Reason**

> The sequence and choices alone provide no sufficiently diagnostic feature for the specific regulatory role; recognizing the protein or consulting its annotation supplies the distinguishing fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the best-supported listed choice. The experimental evidence described is broader than translation regulation, but no other option is supported by the supplied reviewer evidence.


### Important caveats

- The GO assignment is computational (IEA:InterPro), not direct experimental evidence for the molecular-function term.
- The sequence matches historical and current UniProt records, but the original author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The WD-repeat-rich sequence may suggest a protein-interaction scaffold, but that does not meaningfully distinguish translation regulation from other regulatory or binding functions among the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity-specific InterPro/GO annotation linking this sequence to translation regulator activity, or equivalent protein-specific functional evidence.",
    "reason": "The sequence and choices alone provide no sufficiently diagnostic feature for the specific regulatory role; recognizing the protein or consulting its annotation supplies the distinguishing fact."
  },
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact-match sequence has a historical UniProt annotation for translation regulator activity, assigned by InterPro (computational evidence). Its record also describes a ribosome-associated protein and reports regulation of gene expression, though those facts do not independently establish the precise molecular-function term experimentally."
  },
  "important_caveats": [
    "The GO assignment is computational (IEA:InterPro), not direct experimental evidence for the molecular-function term.",
    "The sequence matches historical and current UniProt records, but the original author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported listed choice. The experimental evidence described is broader than translation regulation, but no other option is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match sequence has a historical UniProt annotation for translation regulator activity, assigned by InterPro (computational evidence). Its record also describes a ribosome-associated protein and reports regulation of gene expression, though those facts do not independently establish the precise molecular-function term experimentally.",
    "evidence_ids": ["H3", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The WD-repeat-rich sequence may suggest a protein-interaction scaffold, but that does not meaningfully distinguish translation regulation from other regulatory or binding functions among the options.",
    "missing_item_specific_fact": "The identity-specific InterPro/GO annotation linking this sequence to translation regulator activity, or equivalent protein-specific functional evidence.",
    "reason": "The sequence and choices alone provide no sufficiently diagnostic feature for the specific regulatory role; recognizing the protein or consulting its annotation supplies the distinguishing fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported listed choice. The experimental evidence described is broader than translation regulation, but no other option is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The GO assignment is computational (IEA:InterPro), not direct experimental evidence for the molecular-function term.",
    "The sequence matches historical and current UniProt records, but the original author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A223GEB2 (CPC2_FLAVE, Cross-pathway control WD-repeat protein 2 from Flammulina velutipes) carries GO:0045182 (translation regulator activity) as an IEA:InterPro annotation (evidence C7/H5). The protein is annotated as a ribosomal component (C5/H3), and the GO term definition covers functions involved in regulation of polypeptide synthesis at the ribosome. The annotation is computationally inferred (IEA:InterPro) rather than experimentally validated; the experimental evidence (PubMed:32273873) documents developmental gene regulation, not direct translation-regulation assays. Nonetheless, the annotation is present in the database and is consistent with the protein's described role as a ribosomal subunit component.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple tandem WD40 repeats (recurring 'TD…GH…SD…LW…G…H…SD…LS…S' motifs forming a beta-propeller scaffold). WD40 domains are protein-protein interaction scaffolds, not catalytic or glycan-binding modules. This is incompatible with aspartic-type endopeptidase activity (which requires a DTG motif and catalytic Asp dyad), glycosaminoglycan binding (which requires clusters of basic residues in specific binding motifs), and phosphoglycolate phosphatase activity (which requires dedicated catalytic residues). By elimination of these three mechanistically incompatible options, the remaining choice—translation regulator activity, a general regulatory/scaffold function—is the only one consistent with a WD40 repeat protein.


**Missing item-specific fact**

> Positive identification as specifically a 'translation regulator' (rather than, e.g., a signal-transduction or chromatin-remodeling WD40 scaffold) would require knowing this protein is a ribosomal subunit component. However, because the other three options are mechanistically excluded by the WD40 fold, elimination alone suffices to select D among the given choices.


**Reason**

> A model can reason from the WD40 repeat architecture to exclude options A, B, and C on mechanistic grounds (no catalytic Asp dyad, no basic GAG-binding motifs, no phosphatase active-site residues). Option D is the sole remaining compatible choice. The reasoning does not require memorizing this specific protein's UniProt entry, though confirming the 'translation' specificity (as opposed to other regulatory roles) benefits from knowing it is a ribosomal component.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are mechanistically incompatible with a WD40 beta-propeller scaffold. Option D is the only remaining choice. While 'ribosome binding' (GO:0043022) might be a more precise GO term for a structural ribosomal component, it is not among the options, so no ambiguity arises within the given set.


### Important caveats

- The GO:0045182 annotation is IEA:InterPro (computationally inferred from domain match), not experimentally validated. The experimental study (PubMed:32273873) characterizes developmental gene regulation, not direct translation-regulation assays.
- The protein is described as a 'component of the ribosome'; GO:0043022 (ribosome binding) is also annotated. The distinction between 'ribosome binding' and 'translation regulator activity' is subtle and neither term is perfectly precise for a structural ribosomal subunit.
- The positive assignment to 'translation regulator' specifically (rather than another regulatory role common to WD40 proteins) relies on elimination of the other three options rather than direct positive evidence from the sequence alone.
- The sequence is 315 aa and matches the UniProt canonical entry exactly (SHA-256 confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple tandem WD40 repeats (recurring 'TD…GH…SD…LW…G…H…SD…LS…S' motifs forming a beta-propeller scaffold). WD40 domains are protein-protein interaction scaffolds, not catalytic or glycan-binding modules. This is incompatible with aspartic-type endopeptidase activity (which requires a DTG motif and catalytic Asp dyad), glycosaminoglycan binding (which requires clusters of basic residues in specific binding motifs), and phosphoglycolate phosphatase activity (which requires dedicated catalytic residues). By elimination of these three mechanistically incompatible options, the remaining choice—translation regulator activity, a general regulatory/scaffold function—is the only one consistent with a WD40 repeat protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification as specifically a 'translation regulator' (rather than, e.g., a signal-transduction or chromatin-remodeling WD40 scaffold) would require knowing this protein is a ribosomal subunit component. However, because the other three options are mechanistically excluded by the WD40 fold, elimination alone suffices to select D among the given choices.",
    "reason": "A model can reason from the WD40 repeat architecture to exclude options A, B, and C on mechanistic grounds (no catalytic Asp dyad, no basic GAG-binding motifs, no phosphatase active-site residues). Option D is the sole remaining compatible choice. The reasoning does not require memorizing this specific protein's UniProt entry, though confirming the 'translation' specificity (as opposed to other regulatory roles) benefits from knowing it is a ribosomal component."
  },
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A223GEB2 (CPC2_FLAVE, Cross-pathway control WD-repeat protein 2 from Flammulina velutipes) carries GO:0045182 (translation regulator activity) as an IEA:InterPro annotation (evidence C7/H5). The protein is annotated as a ribosomal component (C5/H3), and the GO term definition covers functions involved in regulation of polypeptide synthesis at the ribosome. The annotation is computationally inferred (IEA:InterPro) rather than experimentally validated; the experimental evidence (PubMed:32273873) documents developmental gene regulation, not direct translation-regulation assays. Nonetheless, the annotation is present in the database and is consistent with the protein's described role as a ribosomal subunit component."
  },
  "important_caveats": [
    "The GO:0045182 annotation is IEA:InterPro (computationally inferred from domain match), not experimentally validated. The experimental study (PubMed:32273873) characterizes developmental gene regulation, not direct translation-regulation assays.",
    "The protein is described as a 'component of the ribosome'; GO:0043022 (ribosome binding) is also annotated. The distinction between 'ribosome binding' and 'translation regulator activity' is subtle and neither term is perfectly precise for a structural ribosomal subunit.",
    "The positive assignment to 'translation regulator' specifically (rather than another regulatory role common to WD40 proteins) relies on elimination of the other three options rather than direct positive evidence from the sequence alone.",
    "The sequence is 315 aa and matches the UniProt canonical entry exactly (SHA-256 confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are mechanistically incompatible with a WD40 beta-propeller scaffold. Option D is the only remaining choice. While 'ribosome binding' (GO:0043022) might be a more precise GO term for a structural ribosomal component, it is not among the options, so no ambiguity arises within the given set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A223GEB2 (CPC2_FLAVE, Cross-pathway control WD-repeat protein 2 from Flammulina velutipes) carries GO:0045182 (translation regulator activity) as an IEA:InterPro annotation (evidence C7/H5). The protein is annotated as a ribosomal component (C5/H3), and the GO term definition covers functions involved in regulation of polypeptide synthesis at the ribosome. The annotation is computationally inferred (IEA:InterPro) rather than experimentally validated; the experimental evidence (PubMed:32273873) documents developmental gene regulation, not direct translation-regulation assays. Nonetheless, the annotation is present in the database and is consistent with the protein's described role as a ribosomal subunit component.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple tandem WD40 repeats (recurring 'TD…GH…SD…LW…G…H…SD…LS…S' motifs forming a beta-propeller scaffold). WD40 domains are protein-protein interaction scaffolds, not catalytic or glycan-binding modules. This is incompatible with aspartic-type endopeptidase activity (which requires a DTG motif and catalytic Asp dyad), glycosaminoglycan binding (which requires clusters of basic residues in specific binding motifs), and phosphoglycolate phosphatase activity (which requires dedicated catalytic residues). By elimination of these three mechanistically incompatible options, the remaining choice—translation regulator activity, a general regulatory/scaffold function—is the only one consistent with a WD40 repeat protein.",
    "missing_item_specific_fact": "Positive identification as specifically a 'translation regulator' (rather than, e.g., a signal-transduction or chromatin-remodeling WD40 scaffold) would require knowing this protein is a ribosomal subunit component. However, because the other three options are mechanistically excluded by the WD40 fold, elimination alone suffices to select D among the given choices.",
    "reason": "A model can reason from the WD40 repeat architecture to exclude options A, B, and C on mechanistic grounds (no catalytic Asp dyad, no basic GAG-binding motifs, no phosphatase active-site residues). Option D is the sole remaining compatible choice. The reasoning does not require memorizing this specific protein's UniProt entry, though confirming the 'translation' specificity (as opposed to other regulatory roles) benefits from knowing it is a ribosomal component."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are mechanistically incompatible with a WD40 beta-propeller scaffold. Option D is the only remaining choice. While 'ribosome binding' (GO:0043022) might be a more precise GO term for a structural ribosomal component, it is not among the options, so no ambiguity arises within the given set."
  },
  "important_caveats": [
    "The GO:0045182 annotation is IEA:InterPro (computationally inferred from domain match), not experimentally validated. The experimental study (PubMed:32273873) characterizes developmental gene regulation, not direct translation-regulation assays.",
    "The protein is described as a 'component of the ribosome'; GO:0043022 (ribosome binding) is also annotated. The distinction between 'ribosome binding' and 'translation regulator activity' is subtle and neither term is perfectly precise for a structural ribosomal subunit.",
    "The positive assignment to 'translation regulator' specifically (rather than another regulatory role common to WD40 proteins) relies on elimination of the other three options rather than direct positive evidence from the sequence alone.",
    "The sequence is 315 aa and matches the UniProt canonical entry exactly (SHA-256 confirmed)."
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

**Accession:** `A0A223GEB2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:42.147209+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q01369","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"32273873","source":"PubMed"}],"value":"Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a polypeptide chain. The nascent polypeptides leave the ribosome through a tunnel in the LSU and interact with protein factors that function in enzymatic processing, targeting, and the membrane insertion of nascent chains at the exit of the ribosomal tunnel (By similarity). Plays in important role in the regulation of vegetative growth and fruiting body development (PubMed:32273873). Especially, positively regulates the expression of genes involved in fruiting body development such as FVFD30 and FVFD16, as well as genes encoding for lectins and hydrophobins (PubMed:32273873). Also regulates the expression of genes involved in cAMP signaling pathway (PubMed:32273873)"}]}
```

Source SHA-256: `bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:42.147209+00:00.  

```json
{"database":"GO","id":"GO:0043022","properties":[{"key":"GoTerm","value":"F:ribosome binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:42.147209+00:00.  

```json
{"database":"GO","id":"GO:0045182","properties":[{"key":"GoTerm","value":"F:translation regulator activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)  
**Locator:** `lines 20-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:24:43.872451+00:00.  

```text
CC   -!- FUNCTION: Component of the ribosome, a large ribonucleoprotein complex
CC       responsible for the synthesis of proteins in the cell. The small
CC       ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the
CC       encoded message by selecting cognate aminoacyl-transfer RNA (tRNA)
CC       molecules. The large subunit (LSU) contains the ribosomal catalytic
CC       site termed the peptidyl transferase center (PTC), which catalyzes the
CC       formation of peptide bonds, thereby polymerizing the amino acids
CC       delivered by tRNAs into a polypeptide chain. The nascent polypeptides
CC       leave the ribosome through a tunnel in the LSU and interact with
CC       protein factors that function in enzymatic processing, targeting, and
CC       the membrane insertion of nascent chains at the exit of the ribosomal
CC       tunnel (By similarity). Plays in important role in the regulation of
CC       vegetative growth and fruiting body development (PubMed:32273873).
CC       Especially, positively regulates the expression of genes involved in
CC       fruiting body development such as FVFD30 and FVFD16, as well as genes
CC       encoding for lectins and hydrophobins (PubMed:32273873). Also regulates
CC       the expression of genes involved in cAMP signaling pathway
CC       (PubMed:32273873). {ECO:0000250|UniProtKB:Q01369,
CC       ECO:0000269|PubMed:32273873}.
```

Source SHA-256: `08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)  
**Locator:** `lines 60-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:24:43.872451+00:00.  

```text
DR   GO; GO:0043022; F:ribosome binding; IEA:InterPro.
```

Source SHA-256: `08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)  
**Locator:** `lines 61-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:24:43.872451+00:00.  

```text
DR   GO; GO:0045182; F:translation regulator activity; IEA:InterPro.
```

Source SHA-256: `08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 262674-262689`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045182
name: translation regulator activity
namespace: molecular_function
def: "Any molecular function involved in the regulation of initiation, activation, perpetuation, repression or termination of polypeptide synthesis at the ribosome." [GOC:ai]
subset: goslim_candida
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
