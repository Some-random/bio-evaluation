# GO_molecular_function_0185

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — pyridoxal phosphate binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. enoyl-[acyl-carrier-protein] reductase (NADPH) activity
B. flavin adenine dinucleotide binding
C. pyridoxal phosphate binding
D. cardiolipin synthase (CMP-forming)
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

> The sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 record, which carries a pyridoxal phosphate-binding GO annotation. Its experimentally supported catalytic function is consistent with a PLP-dependent enzyme. The binding annotation is computational (IEA:InterPro), not direct experimental evidence of binding.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once identified as cystathionine gamma-synthase, PLP binding is biologically consistent with its catalytic class; however, that family identity is not established by an explicit context or an unmistakable motif in the supplied prompt.


**Missing item-specific fact**

> The sequence-to-family assignment as cystathionine gamma-synthase and its PLP-cofactor annotation, which require protein-specific homology/domain knowledge or an external annotation.


**Reason**

> The sequence alone does not offer a clear general biological argument to distinguish PLP binding from the listed alternatives without first recognizing the specific enzyme family. Remembering or retrieving the matching database annotation is therefore needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched record supports pyridoxal phosphate binding; the other choices are not supported for this protein by the supplied reviewer evidence.


### Important caveats

- The sequence match and protein-specific annotations are reviewer-only evidence, not information supplied to the evaluated model.
- The GO annotation uses IEA:InterPro evidence; the cited experimental evidence concerns catalytic function, not a direct binding assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once identified as cystathionine gamma-synthase, PLP binding is biologically consistent with its catalytic class; however, that family identity is not established by an explicit context or an unmistakable motif in the supplied prompt.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-to-family assignment as cystathionine gamma-synthase and its PLP-cofactor annotation, which require protein-specific homology/domain knowledge or an external annotation.",
    "reason": "The sequence alone does not offer a clear general biological argument to distinguish PLP binding from the listed alternatives without first recognizing the specific enzyme family. Remembering or retrieving the matching database annotation is therefore needed."
  },
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 record, which carries a pyridoxal phosphate-binding GO annotation. Its experimentally supported catalytic function is consistent with a PLP-dependent enzyme. The binding annotation is computational (IEA:InterPro), not direct experimental evidence of binding."
  },
  "important_caveats": [
    "The sequence match and protein-specific annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The GO annotation uses IEA:InterPro evidence; the cited experimental evidence concerns catalytic function, not a direct binding assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched record supports pyridoxal phosphate binding; the other choices are not supported for this protein by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 record, which carries a pyridoxal phosphate-binding GO annotation. Its experimentally supported catalytic function is consistent with a PLP-dependent enzyme. The binding annotation is computational (IEA:InterPro), not direct experimental evidence of binding.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once identified as cystathionine gamma-synthase, PLP binding is biologically consistent with its catalytic class; however, that family identity is not established by an explicit context or an unmistakable motif in the supplied prompt.",
    "missing_item_specific_fact": "The sequence-to-family assignment as cystathionine gamma-synthase and its PLP-cofactor annotation, which require protein-specific homology/domain knowledge or an external annotation.",
    "reason": "The sequence alone does not offer a clear general biological argument to distinguish PLP binding from the listed alternatives without first recognizing the specific enzyme family. Remembering or retrieving the matching database annotation is therefore needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched record supports pyridoxal phosphate binding; the other choices are not supported for this protein by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match and protein-specific annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The GO annotation uses IEA:InterPro evidence; the cited experimental evidence concerns catalytic function, not a direct binding assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q9ZPL5) is cystathionine gamma-synthase 1 from Nicotiana tabacum (EC 2.5.1.160), a well-characterized fold-type II PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) to this entry (evidence C9/H7, IEA:InterPro). The PLP-dependence of cystathionine gamma-synthase is established in the primary literature (PMID 10595588 crystal structure). Among the four options, only C correctly applies to this protein; A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase) are all incorrect for this sequence. The GO annotation evidence is computational (IEA:InterPro) rather than direct experimental, but the PLP cofactor requirement is biochemically well-established for this enzyme class.

Citations as saved: [C9](#evidence-c9), [H7](#evidence-h7), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 540-aa sequence contains recognizable fold-type II PLP enzyme domain features (Cys_Met_Meta_PP / PF01053 architecture), including conserved motifs around a catalytic lysine (e.g., the 'GRGIVTDAITTPVVNTSAYFFNKT' region). A biologist familiar with PLP enzyme families could identify these domain signatures. The distractors are clearly distinguishable: enoyl-ACP reductases are ~250-300 aa Rossmann-fold enzymes (too short for this 540-aa protein), FAD-binding flavoproteins require distinct GxGxxG-type motifs absent here, and cardiolipin synthase is a structurally unrelated transferase. The sequence length, domain architecture, and absence of FAD/NADPH-binding Rossmann motifs collectively support PLP dependence over the alternatives.


**Missing item-specific fact**

> Precise identification of the Cys_Met_Meta_PP domain signature requires familiarity with Pfam/InterPro motif patterns, which borders on pattern memorization rather than first-principles deduction.


**Reason**

> While recognizing the exact Pfam domain signature has a memorization component, the overall reasoning path—eliminating A by size/structure, eliminating B by absence of flavoprotein motifs, eliminating D by unrelated enzyme class, and positively identifying PLP-type fold features—is a defensible biological argument from the sequence itself.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for 'primary molecular function' and the true primary function is cystathionine gamma-synthase catalytic activity (GO:0003962) rather than merely PLP cofactor binding, this term is not among the options. Among the four provided choices, only C is a valid annotation for this protein; the other three are entirely incorrect. No ambiguity in selecting the best available answer.


### Important caveats

- The GO:0030170 annotation is IEA:InterPro (computational inference from domain matching), not direct experimental evidence of PLP binding for this specific protein, though PLP dependence of cystathionine gamma-synthase is well-established in the fold-type II enzyme family.
- The 'primary molecular function' phrasing slightly misaligns with the expected answer: PLP binding is a cofactor requirement, not the primary catalytic activity. However, since the catalytic activity term is absent from the options, C remains the only correct choice.
- Sequence match to UniProt Q9ZPL5 is confirmed (SHA-256 match, 540 aa). The identity was inferred by the reviewer from dataset metadata, not from the evaluated model's input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 540-aa sequence contains recognizable fold-type II PLP enzyme domain features (Cys_Met_Meta_PP / PF01053 architecture), including conserved motifs around a catalytic lysine (e.g., the 'GRGIVTDAITTPVVNTSAYFFNKT' region). A biologist familiar with PLP enzyme families could identify these domain signatures. The distractors are clearly distinguishable: enoyl-ACP reductases are ~250-300 aa Rossmann-fold enzymes (too short for this 540-aa protein), FAD-binding flavoproteins require distinct GxGxxG-type motifs absent here, and cardiolipin synthase is a structurally unrelated transferase. The sequence length, domain architecture, and absence of FAD/NADPH-binding Rossmann motifs collectively support PLP dependence over the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the Cys_Met_Meta_PP domain signature requires familiarity with Pfam/InterPro motif patterns, which borders on pattern memorization rather than first-principles deduction.",
    "reason": "While recognizing the exact Pfam domain signature has a memorization component, the overall reasoning path—eliminating A by size/structure, eliminating B by absence of flavoprotein motifs, eliminating D by unrelated enzyme class, and positively identifying PLP-type fold features—is a defensible biological argument from the sequence itself."
  },
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "H7",
      "C4",
      "C5",
      "C6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein (Q9ZPL5) is cystathionine gamma-synthase 1 from Nicotiana tabacum (EC 2.5.1.160), a well-characterized fold-type II PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) to this entry (evidence C9/H7, IEA:InterPro). The PLP-dependence of cystathionine gamma-synthase is established in the primary literature (PMID 10595588 crystal structure). Among the four options, only C correctly applies to this protein; A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase) are all incorrect for this sequence. The GO annotation evidence is computational (IEA:InterPro) rather than direct experimental, but the PLP cofactor requirement is biochemically well-established for this enzyme class."
  },
  "important_caveats": [
    "The GO:0030170 annotation is IEA:InterPro (computational inference from domain matching), not direct experimental evidence of PLP binding for this specific protein, though PLP dependence of cystathionine gamma-synthase is well-established in the fold-type II enzyme family.",
    "The 'primary molecular function' phrasing slightly misaligns with the expected answer: PLP binding is a cofactor requirement, not the primary catalytic activity. However, since the catalytic activity term is absent from the options, C remains the only correct choice.",
    "Sequence match to UniProt Q9ZPL5 is confirmed (SHA-256 match, 540 aa). The identity was inferred by the reviewer from dataset metadata, not from the evaluated model's input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function is cystathionine gamma-synthase catalytic activity (GO:0003962) rather than merely PLP cofactor binding, this term is not among the options. Among the four provided choices, only C is a valid annotation for this protein; the other three are entirely incorrect. No ambiguity in selecting the best available answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q9ZPL5) is cystathionine gamma-synthase 1 from Nicotiana tabacum (EC 2.5.1.160), a well-characterized fold-type II PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) to this entry (evidence C9/H7, IEA:InterPro). The PLP-dependence of cystathionine gamma-synthase is established in the primary literature (PMID 10595588 crystal structure). Among the four options, only C correctly applies to this protein; A (enoyl-ACP reductase), B (FAD binding), and D (cardiolipin synthase) are all incorrect for this sequence. The GO annotation evidence is computational (IEA:InterPro) rather than direct experimental, but the PLP cofactor requirement is biochemically well-established for this enzyme class.",
    "evidence_ids": ["C9", "H7", "C4", "C5", "C6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 540-aa sequence contains recognizable fold-type II PLP enzyme domain features (Cys_Met_Meta_PP / PF01053 architecture), including conserved motifs around a catalytic lysine (e.g., the 'GRGIVTDAITTPVVNTSAYFFNKT' region). A biologist familiar with PLP enzyme families could identify these domain signatures. The distractors are clearly distinguishable: enoyl-ACP reductases are ~250-300 aa Rossmann-fold enzymes (too short for this 540-aa protein), FAD-binding flavoproteins require distinct GxGxxG-type motifs absent here, and cardiolipin synthase is a structurally unrelated transferase. The sequence length, domain architecture, and absence of FAD/NADPH-binding Rossmann motifs collectively support PLP dependence over the alternatives.",
    "missing_item_specific_fact": "Precise identification of the Cys_Met_Meta_PP domain signature requires familiarity with Pfam/InterPro motif patterns, which borders on pattern memorization rather than first-principles deduction.",
    "reason": "While recognizing the exact Pfam domain signature has a memorization component, the overall reasoning path—eliminating A by size/structure, eliminating B by absence of flavoprotein motifs, eliminating D by unrelated enzyme class, and positively identifying PLP-type fold features—is a defensible biological argument from the sequence itself."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function is cystathionine gamma-synthase catalytic activity (GO:0003962) rather than merely PLP cofactor binding, this term is not among the options. Among the four provided choices, only C is a valid annotation for this protein; the other three are entirely incorrect. No ambiguity in selecting the best available answer."
  },
  "important_caveats": [
    "The GO:0030170 annotation is IEA:InterPro (computational inference from domain matching), not direct experimental evidence of PLP binding for this specific protein, though PLP dependence of cystathionine gamma-synthase is well-established in the fold-type II enzyme family.",
    "The 'primary molecular function' phrasing slightly misaligns with the expected answer: PLP binding is a cofactor requirement, not the primary catalytic activity. However, since the catalytic activity term is absent from the options, C remains the only correct choice.",
    "Sequence match to UniProt Q9ZPL5 is confirmed (SHA-256 match, 540 aa). The identity was inferred by the reviewer from dataset metadata, not from the evaluated model's input."
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

**Accession:** `Q9ZPL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 110. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
"Q9ZPL5"
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"value":"2.5.1.160"}],"fullName":{"value":"Cystathionine gamma-synthase 1, chloroplastic"}}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"value":"Catalyzes the first committed step of methionine (Met) biosynthesis. Catalyzes the formation of L-cystathionine from homoserine esters and L-cysteine, via a gamma-replacement reaction"}]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.5.1.160","evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"name":"O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80891"},{"database":"ChEBI","id":"CHEBI:35235"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:58161"}]}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/uniProtKBCrossReferences/25`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"database":"GO","id":"GO:0030170","properties":[{"key":"GoTerm","value":"F:pyridoxal phosphate binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 54-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the first committed step of methionine (Met)
CC       biosynthesis. Catalyzes the formation of L-cystathionine from
CC       homoserine esters and L-cysteine, via a gamma-replacement reaction.
CC       {ECO:0000269|PubMed:10595588}.
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 114-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
DR   GO; GO:0030170; F:pyridoxal phosphate binding; IEA:InterPro.
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 163502-163510`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0030170
name: pyridoxal phosphate binding
namespace: molecular_function
def: "Binding to pyridoxal 5' phosphate, 3-hydroxy-5-(hydroxymethyl)-2-methyl4-pyridine carboxaldehyde 5' phosphate, the biologically active form of vitamin B6." [GOC:mah, ISBN:0198506732]
subset: goslim_metagenomics
is_a: GO:0043168 ! anion binding
is_a: GO:0070279 ! vitamin B6 binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
