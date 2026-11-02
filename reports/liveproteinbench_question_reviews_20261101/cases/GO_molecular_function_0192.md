# GO_molecular_function_0192

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — cyclosporin A binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPNPKVFFDMTIGGQPAGRIVMELYADVTPSTAENFRALCTGEKGAGRSGKPLHYKGSSFHRVIPNFMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFGQVVEGMDVVKEIEKVGSSSGRTAKPVVVADCGQLS

[Multiple Choices]
A. unfolded protein binding
B. carbohydrate binding
C. cyclosporin A binding
D. rRNA binding
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

> The exact supplied sequence matches the soybean Cyclophilin 2 entry, which carries a cyclosporin A binding GO annotation. That annotation is IBA (inferred from biological ancestry), not direct experimental evidence for this particular protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The compact sequence is consistent with a cyclophilin-family protein; cyclophilins are associated with cyclosporin A binding. Among the choices, that family-level biological inference favors C over carbohydrate or rRNA binding, or unfolded-protein binding.


**Missing item-specific fact**

> No item-specific fact is strictly necessary for a defensible family-level inference, though direct evidence that this particular protein binds cyclosporin A is not supplied.


**Reason**

> A recognizable protein-family inference from the sequence and the choices provides meaningful grounds for selecting C; this does not depend solely on recalling the exact sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options do not include the annotated peptidyl-prolyl cis-trans isomerase activity, but cyclosporin A binding is the clearly best match among the listed choices.


### Important caveats

- The cyclosporin A binding annotation is IBA, an inference by biological ancestry, rather than direct experimental evidence for this soybean protein.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The compact sequence is consistent with a cyclophilin-family protein; cyclophilins are associated with cyclosporin A binding. Among the choices, that family-level biological inference favors C over carbohydrate or rRNA binding, or unfolded-protein binding.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is strictly necessary for a defensible family-level inference, though direct evidence that this particular protein binds cyclosporin A is not supplied.",
    "reason": "A recognizable protein-family inference from the sequence and the choices provides meaningful grounds for selecting C; this does not depend solely on recalling the exact sequence's database entry."
  },
  "case_id": "GO_molecular_function_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the soybean Cyclophilin 2 entry, which carries a cyclosporin A binding GO annotation. That annotation is IBA (inferred from biological ancestry), not direct experimental evidence for this particular protein."
  },
  "important_caveats": [
    "The cyclosporin A binding annotation is IBA, an inference by biological ancestry, rather than direct experimental evidence for this soybean protein.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options do not include the annotated peptidyl-prolyl cis-trans isomerase activity, but cyclosporin A binding is the clearly best match among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the soybean Cyclophilin 2 entry, which carries a cyclosporin A binding GO annotation. That annotation is IBA (inferred from biological ancestry), not direct experimental evidence for this particular protein.",
    "evidence_ids": ["C1", "C4", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The compact sequence is consistent with a cyclophilin-family protein; cyclophilins are associated with cyclosporin A binding. Among the choices, that family-level biological inference favors C over carbohydrate or rRNA binding, or unfolded-protein binding.",
    "missing_item_specific_fact": "No item-specific fact is strictly necessary for a defensible family-level inference, though direct evidence that this particular protein binds cyclosporin A is not supplied.",
    "reason": "A recognizable protein-family inference from the sequence and the choices provides meaningful grounds for selecting C; this does not depend solely on recalling the exact sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options do not include the annotated peptidyl-prolyl cis-trans isomerase activity, but cyclosporin A binding is the clearly best match among the listed choices."
  },
  "important_caveats": [
    "The cyclosporin A binding annotation is IBA, an inference by biological ancestry, rather than direct experimental evidence for this soybean protein.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A0R0H9T5 (CYP2_SOYBN), annotated as Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 (EC 5.2.1.8). GO:0016018 'cyclosporin A binding' is annotated with evidence IBA:GO_Central, and the GO term itself carries the RELATED synonym 'cyclophilin.' Cyclophilins are, by definition, the cellular receptors for cyclosporin A; this is a well-established, defining property of the family. The annotation evidence codes (IBA, ISS) are computational transfers, but the underlying biological fact (cyclophilins bind cyclosporin A) is textbook-level and corroborated by the protein's alternative name 'Cyclophilin 2.'

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 172-residue sequence contains motifs characteristic of the cyclophilin-type PPIase domain (e.g., the 'FMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFG' region with conserved active-site residues). Recognizing this as a cyclophilin-family PPIase, and knowing that cyclophilins are the cognate receptors for cyclosporin A (the drug was literally named after its cyclophilin target), provides a reasoning path to option C. The distractors are eliminable by general biology: unfolded-protein binding is a chaperone (HSP70/90) function, carbohydrate binding is a lectin/glycosidase function, and rRNA binding is a ribosomal/RNA-binding-protein function—none of which match a small PPIase domain.


**Missing item-specific fact**

> Recognition of the cyclophilin PPIase domain from raw sequence requires familiarity with the family's conserved motifs (e.g., the 'FMCQ' and 'GGDFTAGNGTGG' stretches). A model without exposure to cyclophilin sequences would struggle to assign the family de novo, though the domain is well-studied and its motifs are documented in structural biology literature.


**Reason**

> A defensible reasoning chain exists: (1) identify PPIase/cyclophilin domain motifs in the sequence, (2) recall that cyclophilins bind cyclosporin A as a defining property, (3) eliminate distractors that correspond to unrelated protein classes. This is general biological knowledge applied to recognizable sequence features, not a single database lookup. However, the initial family recognition step depends on pattern familiarity with the cyclophilin domain, making the question moderately difficult but not purely lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options correspond to distinct and non-overlapping molecular function classes (chaperone, lectin, cyclophilin, RNA-binding protein). Once the protein is identified as a cyclophilin PPIase, only option C applies. The GO term GO:0003755 (peptidyl-prolyl cis-trans isomerase activity) is also annotated but is not among the choices, so no ambiguity arises between the listed options.


### Important caveats

- The GO:0016018 annotation carries evidence code IBA:GO_Central (inferred by biological ancestor from a phylogenetic tree), not direct experimental binding data. The primary function annotation (PPIase activity) is ISS:UniProtKB (sequence-similarity transfer). The biological fact that cyclophilins bind cyclosporin A is nonetheless well-established independently of these specific evidence codes.
- The protein was first released in UniProt on 2025-04-09; the benchmark author's exact source snapshot is unknown, though the sequence matches both current and historical (v51) records.
- The GO term 'cyclosporin A binding' (GO:0016018) lists 'cyclophilin' as a RELATED synonym, meaning the term is essentially a family-level descriptor rather than a distinct mechanistic activity separate from PPIase catalysis.
- The sequence recognition step (identifying the cyclophilin PPIase domain) is a well-studied pattern in structural biology but still requires some familiarity with the family; a model encountering this sequence for the first time without any cyclophilin training data would find the family assignment non-trivial.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 172-residue sequence contains motifs characteristic of the cyclophilin-type PPIase domain (e.g., the 'FMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFG' region with conserved active-site residues). Recognizing this as a cyclophilin-family PPIase, and knowing that cyclophilins are the cognate receptors for cyclosporin A (the drug was literally named after its cyclophilin target), provides a reasoning path to option C. The distractors are eliminable by general biology: unfolded-protein binding is a chaperone (HSP70/90) function, carbohydrate binding is a lectin/glycosidase function, and rRNA binding is a ribosomal/RNA-binding-protein function—none of which match a small PPIase domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Recognition of the cyclophilin PPIase domain from raw sequence requires familiarity with the family's conserved motifs (e.g., the 'FMCQ' and 'GGDFTAGNGTGG' stretches). A model without exposure to cyclophilin sequences would struggle to assign the family de novo, though the domain is well-studied and its motifs are documented in structural biology literature.",
    "reason": "A defensible reasoning chain exists: (1) identify PPIase/cyclophilin domain motifs in the sequence, (2) recall that cyclophilins bind cyclosporin A as a defining property, (3) eliminate distractors that correspond to unrelated protein classes. This is general biological knowledge applied to recognizable sequence features, not a single database lookup. However, the initial family recognition step depends on pattern familiarity with the cyclophilin domain, making the question moderately difficult but not purely lookup-dependent."
  },
  "case_id": "GO_molecular_function_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A0R0H9T5 (CYP2_SOYBN), annotated as Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 (EC 5.2.1.8). GO:0016018 'cyclosporin A binding' is annotated with evidence IBA:GO_Central, and the GO term itself carries the RELATED synonym 'cyclophilin.' Cyclophilins are, by definition, the cellular receptors for cyclosporin A; this is a well-established, defining property of the family. The annotation evidence codes (IBA, ISS) are computational transfers, but the underlying biological fact (cyclophilins bind cyclosporin A) is textbook-level and corroborated by the protein's alternative name 'Cyclophilin 2.'"
  },
  "important_caveats": [
    "The GO:0016018 annotation carries evidence code IBA:GO_Central (inferred by biological ancestor from a phylogenetic tree), not direct experimental binding data. The primary function annotation (PPIase activity) is ISS:UniProtKB (sequence-similarity transfer). The biological fact that cyclophilins bind cyclosporin A is nonetheless well-established independently of these specific evidence codes.",
    "The protein was first released in UniProt on 2025-04-09; the benchmark author's exact source snapshot is unknown, though the sequence matches both current and historical (v51) records.",
    "The GO term 'cyclosporin A binding' (GO:0016018) lists 'cyclophilin' as a RELATED synonym, meaning the term is essentially a family-level descriptor rather than a distinct mechanistic activity separate from PPIase catalysis.",
    "The sequence recognition step (identifying the cyclophilin PPIase domain) is a well-studied pattern in structural biology but still requires some familiarity with the family; a model encountering this sequence for the first time without any cyclophilin training data would find the family assignment non-trivial."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to distinct and non-overlapping molecular function classes (chaperone, lectin, cyclophilin, RNA-binding protein). Once the protein is identified as a cyclophilin PPIase, only option C applies. The GO term GO:0003755 (peptidyl-prolyl cis-trans isomerase activity) is also annotated but is not among the choices, so no ambiguity arises between the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A0R0H9T5 (CYP2_SOYBN), annotated as Peptidyl-prolyl cis-trans isomerase 2 / Cyclophilin 2 (EC 5.2.1.8). GO:0016018 'cyclosporin A binding' is annotated with evidence IBA:GO_Central, and the GO term itself carries the RELATED synonym 'cyclophilin.' Cyclophilins are, by definition, the cellular receptors for cyclosporin A; this is a well-established, defining property of the family. The annotation evidence codes (IBA, ISS) are computational transfers, but the underlying biological fact (cyclophilins bind cyclosporin A) is textbook-level and corroborated by the protein's alternative name 'Cyclophilin 2.'",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 172-residue sequence contains motifs characteristic of the cyclophilin-type PPIase domain (e.g., the 'FMCQGGDFTAGNGTGGESIYGAKFADENFVKKHTGPGILSMANAGPGTNGSQFFICTTKTEWLDGKHVVFG' region with conserved active-site residues). Recognizing this as a cyclophilin-family PPIase, and knowing that cyclophilins are the cognate receptors for cyclosporin A (the drug was literally named after its cyclophilin target), provides a reasoning path to option C. The distractors are eliminable by general biology: unfolded-protein binding is a chaperone (HSP70/90) function, carbohydrate binding is a lectin/glycosidase function, and rRNA binding is a ribosomal/RNA-binding-protein function—none of which match a small PPIase domain.",
    "missing_item_specific_fact": "Recognition of the cyclophilin PPIase domain from raw sequence requires familiarity with the family's conserved motifs (e.g., the 'FMCQ' and 'GGDFTAGNGTGG' stretches). A model without exposure to cyclophilin sequences would struggle to assign the family de novo, though the domain is well-studied and its motifs are documented in structural biology literature.",
    "reason": "A defensible reasoning chain exists: (1) identify PPIase/cyclophilin domain motifs in the sequence, (2) recall that cyclophilins bind cyclosporin A as a defining property, (3) eliminate distractors that correspond to unrelated protein classes. This is general biological knowledge applied to recognizable sequence features, not a single database lookup. However, the initial family recognition step depends on pattern familiarity with the cyclophilin domain, making the question moderately difficult but not purely lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to distinct and non-overlapping molecular function classes (chaperone, lectin, cyclophilin, RNA-binding protein). Once the protein is identified as a cyclophilin PPIase, only option C applies. The GO term GO:0003755 (peptidyl-prolyl cis-trans isomerase activity) is also annotated but is not among the choices, so no ambiguity arises between the listed options."
  },
  "important_caveats": [
    "The GO:0016018 annotation carries evidence code IBA:GO_Central (inferred by biological ancestor from a phylogenetic tree), not direct experimental binding data. The primary function annotation (PPIase activity) is ISS:UniProtKB (sequence-similarity transfer). The biological fact that cyclophilins bind cyclosporin A is nonetheless well-established independently of these specific evidence codes.",
    "The protein was first released in UniProt on 2025-04-09; the benchmark author's exact source snapshot is unknown, though the sequence matches both current and historical (v51) records.",
    "The GO term 'cyclosporin A binding' (GO:0016018) lists 'cyclophilin' as a RELATED synonym, meaning the term is essentially a family-level descriptor rather than a distinct mechanistic activity separate from PPIase catalysis.",
    "The sequence recognition step (identifying the cyclophilin PPIase domain) is a well-studied pattern in structural biology but still requires some familiarity with the family; a model encountering this sequence for the first time without any cyclophilin training data would find the family assignment non-trivial."
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

**Accession:** `A0A0R0H9T5` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
"A0A0R0H9T5"
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"Cyclophilin 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"GmCYP2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P62937","source":"UniProtKB"}],"value":"5.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"O49886","source":"UniProtKB"}],"value":"Peptidyl-prolyl cis-trans isomerase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O49886","source":"UniProtKB"}],"value":"PPIase 2"}]}}
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O49886","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"Ref.2","source":"Reference"}],"value":"PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (By similarity). Promotes salt tolerance, probably by maintaining the Na(+)/K(+) ratio and good photosynthetic state (Ref.2). May also be involved in the regulation of abscisic acid (ABA) and Ca(2+) signaling pathways (Ref.2)"}]}
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0R0H9T5.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:20.433774+00:00.  

```json
{"database":"GO","id":"GO:0016018","properties":[{"key":"GoTerm","value":"F:cyclosporin A binding"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `f7f163e0c9917e55f2d65f7bb18771151c70abedc4d5d7bc728cc814cefd22ba`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:22.440712+00:00.  

```text
ID   CYP2_SOYBN              Reviewed;         172 AA.
AC   A0A0R0H9T5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-JAN-2016, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Peptidyl-prolyl cis-trans isomerase 2 {ECO:0000250|UniProtKB:O49886};
DE            Short=PPIase 2 {ECO:0000250|UniProtKB:O49886};
DE            EC=5.2.1.8 {ECO:0000250|UniProtKB:P62937};
DE   AltName: Full=Cyclophilin 2 {ECO:0000303|Ref.2};
DE            Short=GmCYP2 {ECO:0000303|Ref.2};
GN   Name=CYP2 {ECO:0000303|Ref.2};
GN   ORFNames=GLYMA_12G024700 {ECO:0000312|EMBL:KRH24153.1};
OS   Glycine max (Soybean) (Glycine hispida).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;
OC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;
OC   Glycine subgen. Soja.
OX   NCBI_TaxID=3847;
```

Source SHA-256: `8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0R0H9T5?format=txt&versions=51)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:22.440712+00:00.  

```text
DR   GO; GO:0016018; F:cyclosporin A binding; IBA:GO_Central.
```

Source SHA-256: `8a831b41ee7356d273422a7e40a6b035b2f08ac1f009b688f9f6f295b13e7e66`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 122608-122615`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016018
name: cyclosporin A binding
namespace: molecular_function
def: "Binding to cyclosporin A, a cyclic undecapeptide that contains several N-methylated and unusual amino acids." [GOC:mb]
synonym: "cyclophilin" RELATED []
is_a: GO:0005488 ! binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
