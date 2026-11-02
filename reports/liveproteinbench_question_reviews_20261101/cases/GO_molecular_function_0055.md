# GO_molecular_function_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. RNA-directed RNA polymerase activity
B. MAP kinase activity
C. trichodiene synthase activity
D. endo-1,4-beta-xylanase activity
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

> The supplied sequence exactly matches the annotated protein. Its entry reports endo-1,4-beta-xylanase activity, including a catalytic reaction supported by experimental evidence; the GO annotation is also experimentally supported.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C7](#evidence-c7), [H18](#evidence-h18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 223-residue sequence has an N-terminal hydrophobic signal-peptide-like region, consistent with a secreted fungal enzyme. Its size and sequence are unlike the typically much larger RNA-directed RNA polymerases and trichodiene synthases; it also lacks the characteristic kinase-domain context expected for a MAP kinase. Among these choices, a secreted xylan-degrading enzyme is a defensible fit.


**Missing item-specific fact**

> The exact substrate specificity—xylan hydrolysis—is not established uniquely by these general sequence features; confirming it would benefit from sequence-family identification or protein-specific annotation.


**Reason**

> The sequence and choices provide meaningful grounds to favor D over the other options, though the precise enzymatic activity is not proven by the broad secretion and size clues alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably consistent with a short, likely secreted fungal protein.


### Important caveats

- Reviewer-only evidence confirms the key but was not available to the evaluated model.
- The sequence evidence supports a plausible choice among these distractors; it does not by itself demonstrate xylanase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 223-residue sequence has an N-terminal hydrophobic signal-peptide-like region, consistent with a secreted fungal enzyme. Its size and sequence are unlike the typically much larger RNA-directed RNA polymerases and trichodiene synthases; it also lacks the characteristic kinase-domain context expected for a MAP kinase. Among these choices, a secreted xylan-degrading enzyme is a defensible fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity—xylan hydrolysis—is not established uniquely by these general sequence features; confirming it would benefit from sequence-family identification or protein-specific annotation.",
    "reason": "The sequence and choices provide meaningful grounds to favor D over the other options, though the precise enzymatic activity is not proven by the broad secretion and size clues alone."
  },
  "case_id": "GO_molecular_function_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C7",
      "H18"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its entry reports endo-1,4-beta-xylanase activity, including a catalytic reaction supported by experimental evidence; the GO annotation is also experimentally supported."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence evidence supports a plausible choice among these distractors; it does not by itself demonstrate xylanase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably consistent with a short, likely secreted fungal protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its entry reports endo-1,4-beta-xylanase activity, including a catalytic reaction supported by experimental evidence; the GO annotation is also experimentally supported.",
    "evidence_ids": ["C1", "C6", "C7", "H18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 223-residue sequence has an N-terminal hydrophobic signal-peptide-like region, consistent with a secreted fungal enzyme. Its size and sequence are unlike the typically much larger RNA-directed RNA polymerases and trichodiene synthases; it also lacks the characteristic kinase-domain context expected for a MAP kinase. Among these choices, a secreted xylan-degrading enzyme is a defensible fit.",
    "missing_item_specific_fact": "The exact substrate specificity—xylan hydrolysis—is not established uniquely by these general sequence features; confirming it would benefit from sequence-family identification or protein-specific annotation.",
    "reason": "The sequence and choices provide meaningful grounds to favor D over the other options, though the precise enzymatic activity is not proven by the broad secretion and size clues alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably consistent with a short, likely secreted fungal protein."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence evidence supports a plausible choice among these distractors; it does not by itself demonstrate xylanase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9UVF9 (EIX_HYPRU), an ethylene-inducing xylanase from Trichoderma viride. UniProt explicitly annotates GO:0031176 (endo-1,4-beta-xylanase activity) with experimental evidence (ECO:0000269, PubMed:16668223). The catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' (EC 3.2.1.8) is backed by experimental product characterization. Multiple independent experimental papers confirm the xylanase function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C12](#evidence-c12), [H17](#evidence-h17), [H18](#evidence-h18), [H19](#evidence-h19).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 223-aa protein can be distinguished from the other options through size and motif analysis: (1) RNA-directed RNA polymerases are typically >500 aa with conserved GDD motifs—this protein is far too small, eliminating A. (2) MAP kinases are ~350-400 aa protein kinases with conserved VAIK, HRD, and DFG motifs—absent here, eliminating B. (3) Trichodiene synthases are sesquiterpene cyclases (~370 aa in maize) with the DDxxD catalytic motif—absent here and the protein is too small, eliminating C. (4) The protein is a small (~223 aa), secreted (N-terminal signal peptide), aromatic-residue-rich fungal protein, consistent with the size and character of GH11 endo-1,4-beta-xylanases (typically 180-220 aa mature, beta-jellyroll fold, secreted by fungi).


**Missing item-specific fact**

> None critical. The positive identification of D relies partly on elimination and partly on consistency with GH11 xylanase characteristics (size, secretion, aromatic content, fungal origin). A model would need general knowledge that GH11 xylanases are ~200 aa secreted fungal enzymes, but this is standard enzymology knowledge.


**Reason**

> Three of four options can be excluded by general biological reasoning (size thresholds for RdRP and MAPK, absence of kinase motifs, absence of DDxxD terpene cyclase motif). The remaining option D is positively consistent with the protein's size, secretion signal, aromatic-rich composition, and fungal origin—all observable from the sequence. This constitutes a meaningful biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C can each be excluded by size and motif analysis. Option D is the only one consistent with a ~223 aa secreted fungal protein lacking kinase, polymerase, or terpene cyclase motifs. No other option is defensible.


### Important caveats

- The positive identification of D as a xylanase (rather than, say, another small secreted fungal protein) is partly by elimination and partly by consistency with GH11 xylanase properties. A model without specific knowledge of GH11 xylanase size/fold characteristics might struggle to positively confirm D, though the elimination of A, B, C is robust.
- The UniProt EC annotation uses PROSITE-ProRule (computational, ECO:0000255), but the catalytic activity itself is experimentally verified (ECO:0000269, PubMed:16668223).
- The sequence is the precursor (223 aa including signal peptide); the mature xylanase is ~190 aa, which is squarely within the GH11 xylanase size range.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 223-aa protein can be distinguished from the other options through size and motif analysis: (1) RNA-directed RNA polymerases are typically >500 aa with conserved GDD motifs—this protein is far too small, eliminating A. (2) MAP kinases are ~350-400 aa protein kinases with conserved VAIK, HRD, and DFG motifs—absent here, eliminating B. (3) Trichodiene synthases are sesquiterpene cyclases (~370 aa in maize) with the DDxxD catalytic motif—absent here and the protein is too small, eliminating C. (4) The protein is a small (~223 aa), secreted (N-terminal signal peptide), aromatic-residue-rich fungal protein, consistent with the size and character of GH11 endo-1,4-beta-xylanases (typically 180-220 aa mature, beta-jellyroll fold, secreted by fungi).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The positive identification of D relies partly on elimination and partly on consistency with GH11 xylanase characteristics (size, secretion, aromatic content, fungal origin). A model would need general knowledge that GH11 xylanases are ~200 aa secreted fungal enzymes, but this is standard enzymology knowledge.",
    "reason": "Three of four options can be excluded by general biological reasoning (size thresholds for RdRP and MAPK, absence of kinase motifs, absence of DDxxD terpene cyclase motif). The remaining option D is positively consistent with the protein's size, secretion signal, aromatic-rich composition, and fungal origin—all observable from the sequence. This constitutes a meaningful biological argument rather than pure lookup."
  },
  "case_id": "GO_molecular_function_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C12",
      "H17",
      "H18",
      "H19"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9UVF9 (EIX_HYPRU), an ethylene-inducing xylanase from Trichoderma viride. UniProt explicitly annotates GO:0031176 (endo-1,4-beta-xylanase activity) with experimental evidence (ECO:0000269, PubMed:16668223). The catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' (EC 3.2.1.8) is backed by experimental product characterization. Multiple independent experimental papers confirm the xylanase function."
  },
  "important_caveats": [
    "The positive identification of D as a xylanase (rather than, say, another small secreted fungal protein) is partly by elimination and partly by consistency with GH11 xylanase properties. A model without specific knowledge of GH11 xylanase size/fold characteristics might struggle to positively confirm D, though the elimination of A, B, C is robust.",
    "The UniProt EC annotation uses PROSITE-ProRule (computational, ECO:0000255), but the catalytic activity itself is experimentally verified (ECO:0000269, PubMed:16668223).",
    "The sequence is the precursor (223 aa including signal peptide); the mature xylanase is ~190 aa, which is squarely within the GH11 xylanase size range."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C can each be excluded by size and motif analysis. Option D is the only one consistent with a ~223 aa secreted fungal protein lacking kinase, polymerase, or terpene cyclase motifs. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9UVF9 (EIX_HYPRU), an ethylene-inducing xylanase from Trichoderma viride. UniProt explicitly annotates GO:0031176 (endo-1,4-beta-xylanase activity) with experimental evidence (ECO:0000269, PubMed:16668223). The catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' (EC 3.2.1.8) is backed by experimental product characterization. Multiple independent experimental papers confirm the xylanase function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C12", "H17", "H18", "H19"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 223-aa protein can be distinguished from the other options through size and motif analysis: (1) RNA-directed RNA polymerases are typically >500 aa with conserved GDD motifs—this protein is far too small, eliminating A. (2) MAP kinases are ~350-400 aa protein kinases with conserved VAIK, HRD, and DFG motifs—absent here, eliminating B. (3) Trichodiene synthases are sesquiterpene cyclases (~370 aa in maize) with the DDxxD catalytic motif—absent here and the protein is too small, eliminating C. (4) The protein is a small (~223 aa), secreted (N-terminal signal peptide), aromatic-residue-rich fungal protein, consistent with the size and character of GH11 endo-1,4-beta-xylanases (typically 180-220 aa mature, beta-jellyroll fold, secreted by fungi).",
    "missing_item_specific_fact": "None critical. The positive identification of D relies partly on elimination and partly on consistency with GH11 xylanase characteristics (size, secretion, aromatic content, fungal origin). A model would need general knowledge that GH11 xylanases are ~200 aa secreted fungal enzymes, but this is standard enzymology knowledge.",
    "reason": "Three of four options can be excluded by general biological reasoning (size thresholds for RdRP and MAPK, absence of kinase motifs, absence of DDxxD terpene cyclase motif). The remaining option D is positively consistent with the protein's size, secretion signal, aromatic-rich composition, and fungal origin—all observable from the sequence. This constitutes a meaningful biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C can each be excluded by size and motif analysis. Option D is the only one consistent with a ~223 aa secreted fungal protein lacking kinase, polymerase, or terpene cyclase motifs. No other option is defensible."
  },
  "important_caveats": [
    "The positive identification of D as a xylanase (rather than, say, another small secreted fungal protein) is partly by elimination and partly by consistency with GH11 xylanase properties. A model without specific knowledge of GH11 xylanase size/fold characteristics might struggle to positively confirm D, though the elimination of A, B, C is robust.",
    "The UniProt EC annotation uses PROSITE-ProRule (computational, ECO:0000255), but the catalytic activity itself is experimentally verified (ECO:0000269, PubMed:16668223).",
    "The sequence is the precursor (223 aa including signal peptide); the mature xylanase is ~190 aa, which is squarely within the GH11 xylanase size range."
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

**Accession:** `Q9UVF9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 91. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
"Q9UVF9"
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"Ethylene biosynthesis-inducing factor"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"EIF"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12231760","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15155877","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16653055","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16653240","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16666504","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16667541","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16667926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"16668506","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19392695","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20357140","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24351686","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35017559","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"7824643","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (PubMed:16668223). Acts as an elicitor of plant defense responses in hosts such as tobacco (Nicotiana tabacum) or tomato (Solanum lycopersicum) (PubMed:12231760, PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:7824643). Induces the production of ethylene and leads alterations in membrane function with rapid efflux of potassium, uptake of calcium, alkalization of the medium, increased leakage of cellular components and necrosis in plant hosts (PubMed:12231760, PubMed:16653055, PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:20357140, PubMed:24351686). EIX is translocated through the xylem of the host plant to the leaf mesophyll, leading to host response to pathogen-derived extracellular proteins in tissues distant from the invading pathogen (PubMed:16653240, PubMed:16668506). Greatly enhances the expression of two calcineurin B-like proteins-interacting protein kinases (CIPKs) family members, OsCIPK14 and OsCIPK15, in rice cultured cells (PubMed:20357140). In tomato, triggers the defense response via binding to and subsequent internalization of the LeEix2 receptor (PubMed:15155877, PubMed:19392695, PubMed:35017559)"}]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"}],"id":"GO:0031176","properties":[{"key":"GoTerm","value":"F:endo-1,4-beta-xylanase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Dean J.F.","Gross K.C.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16668223"},{"database":"DOI","id":"10.1104/pp.96.2.571"}],"citationType":"journal article","firstPage":"571","id":"16668223","journal":"Plant Physiol.","lastPage":"576","publicationDate":"1991","title":"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.","volume":"96"},"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 128-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (PubMed:16668223). Acts as an elicitor of plant defense
CC       responses in hosts such as tobacco (Nicotiana tabacum) or tomato
CC       (Solanum lycopersicum) (PubMed:12231760, PubMed:16666504,
CC       PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:7824643).
CC       Induces the production of ethylene and leads alterations in membrane
CC       function with rapid efflux of potassium, uptake of calcium,
CC       alkalization of the medium, increased leakage of cellular components
CC       and necrosis in plant hosts (PubMed:12231760, PubMed:16653055,
CC       PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506,
CC       PubMed:20357140, PubMed:24351686). EIX is translocated through the
CC       xylem of the host plant to the leaf mesophyll, leading to host response
CC       to pathogen-derived extracellular proteins in tissues distant from the
CC       invading pathogen (PubMed:16653240, PubMed:16668506). Greatly enhances
CC       the expression of two calcineurin B-like proteins-interacting protein
CC       kinases (CIPKs) family members, OsCIPK14 and OsCIPK15, in rice cultured
CC       cells (PubMed:20357140). In tomato, triggers the defense response via
CC       binding to and subsequent internalization of the LeEix2 receptor
CC       (PubMed:15155877, PubMed:19392695, PubMed:35017559).
CC       {ECO:0000269|PubMed:12231760, ECO:0000269|PubMed:15155877,
CC       ECO:0000269|PubMed:16653055, ECO:0000269|PubMed:16653240,
CC       ECO:0000269|PubMed:16666504, ECO:0000269|PubMed:16667541,
CC       ECO:0000269|PubMed:16667926, ECO:0000269|PubMed:16668223,
CC       ECO:0000269|PubMed:16668506, ECO:0000269|PubMed:19392695,
CC       ECO:0000269|PubMed:20357140, ECO:0000269|PubMed:24351686,
CC       ECO:0000269|PubMed:35017559, ECO:0000269|PubMed:7824643}.
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 156-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:16668223};
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 195-195`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
