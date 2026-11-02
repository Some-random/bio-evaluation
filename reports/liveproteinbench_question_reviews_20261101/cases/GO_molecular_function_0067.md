# GO_molecular_function_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — ATP binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDGYAVRAEAMEKRYGEKRALDGFDLAVGEGTVHGLLGPNGAGKTTAVRILSTLVRLDGGRATVAGLDVARQPREVRARIGLTGQYAAVDEVLTGRQNLEMFGRLFHLGGRRARLRATELLEQFDLTDAGDRGVGKYSGGMRRRLDLAASMILAPAVLFLDEPTTGLDPRSRGEVWESVRALVAGGTTVLLTTQYLEEADKLASRITVIDQGRAIADDTPDGLKNLVGGDRIEVVVAERAEIPRVVKVVARVADGEPEADETESRVHAPVTDRVTALTEVARTLQDEGVRVEDIGLRRPSLDDVFLRLTGHRTENTEAKEAA

[Multiple Choices]
A. ATP binding
B. carbohydrate derivative binding
C. RNA polymerase II general transcription initiation factor activity
D. hydrolase activity, acting on ester bonds
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

> The supplied sequence matches the cited UniProt record. That record identifies the protein as an ABC transporter ATP-binding component, with ATP binding annotated computationally and ATP-dependent transporter activity described in the record. The catalytic reaction uses ATP. These support ATP binding, although the GO annotation itself is not a direct ligand-binding assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a characteristic ABC-transporter nucleotide-binding P-loop motif, GPNGAGKTT, including the conserved lysine and threonine associated with ATP binding. This gives a concrete reason to favor ATP binding over transcription-factor or ester-hydrolase activity; it also supports a nucleotide-binding function rather than an unrelated carbohydrate-binding function.


**Missing item-specific fact**

> No item-specific fact is needed to favor ATP binding from the sequence motifs. The precise transporter substrate and the protein-specific annotation or experimental record are not supplied, but they are not needed to distinguish the listed best, specific function.


**Reason**

> The sequence provides recognizable ABC ATPase-family evidence that meaningfully distinguishes option A. This is a defensible family-level inference, not merely recognition of an exact sequence or reliance on a predictor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> ATP binding is more specific and is the best choice, but the supplied ontology evidence places ATP binding under carbohydrate derivative binding, so option B is a broader parent term that can also apply in GO annotation semantics.


### Important caveats

- The matched UniProt record and its annotations are reviewer-only evidence, not information supplied to the evaluated model.
- The ATP-binding GO annotation is computationally inferred; the record's ATP-dependent transport reaction is supported by a cited publication, but the excerpts do not establish a direct ATP-binding assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a characteristic ABC-transporter nucleotide-binding P-loop motif, GPNGAGKTT, including the conserved lysine and threonine associated with ATP binding. This gives a concrete reason to favor ATP binding over transcription-factor or ester-hydrolase activity; it also supports a nucleotide-binding function rather than an unrelated carbohydrate-binding function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is needed to favor ATP binding from the sequence motifs. The precise transporter substrate and the protein-specific annotation or experimental record are not supplied, but they are not needed to distinguish the listed best, specific function.",
    "reason": "The sequence provides recognizable ABC ATPase-family evidence that meaningfully distinguishes option A. This is a defensible family-level inference, not merely recognition of an exact sequence or reliance on a predictor."
  },
  "case_id": "GO_molecular_function_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the cited UniProt record. That record identifies the protein as an ABC transporter ATP-binding component, with ATP binding annotated computationally and ATP-dependent transporter activity described in the record. The catalytic reaction uses ATP. These support ATP binding, although the GO annotation itself is not a direct ligand-binding assay."
  },
  "important_caveats": [
    "The matched UniProt record and its annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The ATP-binding GO annotation is computationally inferred; the record's ATP-dependent transport reaction is supported by a cited publication, but the excerpts do not establish a direct ATP-binding assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "ATP binding is more specific and is the best choice, but the supplied ontology evidence places ATP binding under carbohydrate derivative binding, so option B is a broader parent term that can also apply in GO annotation semantics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the cited UniProt record. That record identifies the protein as an ABC transporter ATP-binding component, with ATP binding annotated computationally and ATP-dependent transporter activity described in the record. The catalytic reaction uses ATP. These support ATP binding, although the GO annotation itself is not a direct ligand-binding assay.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C8", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a characteristic ABC-transporter nucleotide-binding P-loop motif, GPNGAGKTT, including the conserved lysine and threonine associated with ATP binding. This gives a concrete reason to favor ATP binding over transcription-factor or ester-hydrolase activity; it also supports a nucleotide-binding function rather than an unrelated carbohydrate-binding function.",
    "missing_item_specific_fact": "No item-specific fact is needed to favor ATP binding from the sequence motifs. The precise transporter substrate and the protein-specific annotation or experimental record are not supplied, but they are not needed to distinguish the listed best, specific function.",
    "reason": "The sequence provides recognizable ABC ATPase-family evidence that meaningfully distinguishes option A. This is a defensible family-level inference, not merely recognition of an exact sequence or reliance on a predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "ATP binding is more specific and is the best choice, but the supplied ontology evidence places ATP binding under carbohydrate derivative binding, so option B is a broader parent term that can also apply in GO annotation semantics."
  },
  "important_caveats": [
    "The matched UniProt record and its annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The ATP-binding GO annotation is computationally inferred; the record's ATP-dependent transport reaction is supported by a cited publication, but the excerpts do not establish a direct ATP-binding assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (P0DXU5, DrrA2) is an ABC transporter nucleotide-binding domain (NBD) component. UniProt directly annotates GO:0005524 'ATP binding' (C8/H6, IEA:InterPro), the protein name explicitly includes 'ATP-binding' (C4/H1), and the catalytic reaction (C6/H4) consumes ATP. The experimental evidence (PubMed:39375957, ECO:0000269) confirms its role in daunorubicin efflux via ABC transport, which inherently requires ATP binding. The IEA evidence code for the GO annotation is computational, but the protein's identity as an ABC transporter NBD is experimentally established, and ATP binding is a defining property of this protein family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A motif 'GPNGAGKTT' (residues ~38-46), matching the GxxxxGK&#91;ST&#93; consensus diagnostic of nucleotide-binding P-loops. Additional ABC transporter signature features are present (e.g., 'DEPT' motif in 'FLDEPTTGLDPR'). Together these identify the protein as an ABC transporter NBD, whose defining molecular function is ATP binding. Option C (RNA Pol II transcription factor) is excluded because the protein is bacterial (no RNA Pol II machinery). Option D (ester-bond hydrolase, EC 3.1) is excluded because ATP hydrolysis acts on phosphoanhydride bonds (EC 3.6), not ester bonds. Option B (carbohydrate derivative binding) is a very broad parent term; standard GO annotation practice and the 'best describes' phrasing favor the most specific applicable term.


**Missing item-specific fact**

> None strictly required. The Walker A motif and ABC signature motifs are identifiable from the raw sequence by a knowledgeable reader without database lookup.


**Reason**

> A model with general biochemistry knowledge can recognize the Walker A P-loop motif from the sequence, infer nucleotide binding, identify additional ABC transporter hallmarks to narrow to ATP binding specifically, and eliminate C (bacterial protein, no eukaryotic transcription machinery) and D (wrong bond chemistry). The A-vs-B distinction is resolved by the GO specificity principle and the 'best describes' wording.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although GO:0005524 (ATP binding) is a descendant of GO:0097367 (carbohydrate derivative binding) in the GO DAG, making B technically true by inheritance, standard GO annotation convention and the question's 'best describes its primary molecular function' phrasing unambiguously favor the most specific term (A). Options C and D are clearly incorrect. No genuine ambiguity remains for a well-informed respondent.


### Important caveats

- The GO:0005524 annotation carries IEA:InterPro evidence (computational inference from domain match), not direct experimental ATP-binding measurement. However, the protein's ABC transporter identity is experimentally supported (ECO:0000269, PubMed:39375957), and ATP binding is a defining mechanistic requirement of ABC transporters.
- GO:0005524 is an is_a descendant of GO:0097367 (carbohydrate derivative binding), so option B is technically satisfied by the same annotation. The question relies on the convention of selecting the most specific GO term, which is standard practice but not explicitly stated in the stem.
- The protein was first public in Feb 2025; the benchmark author snapshot date is unknown, so the annotation context at question-construction time may have differed slightly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif 'GPNGAGKTT' (residues ~38-46), matching the GxxxxGK[ST] consensus diagnostic of nucleotide-binding P-loops. Additional ABC transporter signature features are present (e.g., 'DEPT' motif in 'FLDEPTTGLDPR'). Together these identify the protein as an ABC transporter NBD, whose defining molecular function is ATP binding. Option C (RNA Pol II transcription factor) is excluded because the protein is bacterial (no RNA Pol II machinery). Option D (ester-bond hydrolase, EC 3.1) is excluded because ATP hydrolysis acts on phosphoanhydride bonds (EC 3.6), not ester bonds. Option B (carbohydrate derivative binding) is a very broad parent term; standard GO annotation practice and the 'best describes' phrasing favor the most specific applicable term.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The Walker A motif and ABC signature motifs are identifiable from the raw sequence by a knowledgeable reader without database lookup.",
    "reason": "A model with general biochemistry knowledge can recognize the Walker A P-loop motif from the sequence, infer nucleotide binding, identify additional ABC transporter hallmarks to narrow to ATP binding specifically, and eliminate C (bacterial protein, no eukaryotic transcription machinery) and D (wrong bond chemistry). The A-vs-B distinction is resolved by the GO specificity principle and the 'best describes' wording."
  },
  "case_id": "GO_molecular_function_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "H1",
      "H3",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The protein (P0DXU5, DrrA2) is an ABC transporter nucleotide-binding domain (NBD) component. UniProt directly annotates GO:0005524 'ATP binding' (C8/H6, IEA:InterPro), the protein name explicitly includes 'ATP-binding' (C4/H1), and the catalytic reaction (C6/H4) consumes ATP. The experimental evidence (PubMed:39375957, ECO:0000269) confirms its role in daunorubicin efflux via ABC transport, which inherently requires ATP binding. The IEA evidence code for the GO annotation is computational, but the protein's identity as an ABC transporter NBD is experimentally established, and ATP binding is a defining property of this protein family."
  },
  "important_caveats": [
    "The GO:0005524 annotation carries IEA:InterPro evidence (computational inference from domain match), not direct experimental ATP-binding measurement. However, the protein's ABC transporter identity is experimentally supported (ECO:0000269, PubMed:39375957), and ATP binding is a defining mechanistic requirement of ABC transporters.",
    "GO:0005524 is an is_a descendant of GO:0097367 (carbohydrate derivative binding), so option B is technically satisfied by the same annotation. The question relies on the convention of selecting the most specific GO term, which is standard practice but not explicitly stated in the stem.",
    "The protein was first public in Feb 2025; the benchmark author snapshot date is unknown, so the annotation context at question-construction time may have differed slightly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0005524 (ATP binding) is a descendant of GO:0097367 (carbohydrate derivative binding) in the GO DAG, making B technically true by inheritance, standard GO annotation convention and the question's 'best describes its primary molecular function' phrasing unambiguously favor the most specific term (A). Options C and D are clearly incorrect. No genuine ambiguity remains for a well-informed respondent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (P0DXU5, DrrA2) is an ABC transporter nucleotide-binding domain (NBD) component. UniProt directly annotates GO:0005524 'ATP binding' (C8/H6, IEA:InterPro), the protein name explicitly includes 'ATP-binding' (C4/H1), and the catalytic reaction (C6/H4) consumes ATP. The experimental evidence (PubMed:39375957, ECO:0000269) confirms its role in daunorubicin efflux via ABC transport, which inherently requires ATP binding. The IEA evidence code for the GO annotation is computational, but the protein's identity as an ABC transporter NBD is experimentally established, and ATP binding is a defining property of this protein family.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "H1", "H3", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif 'GPNGAGKTT' (residues ~38-46), matching the GxxxxGK[ST] consensus diagnostic of nucleotide-binding P-loops. Additional ABC transporter signature features are present (e.g., 'DEPT' motif in 'FLDEPTTGLDPR'). Together these identify the protein as an ABC transporter NBD, whose defining molecular function is ATP binding. Option C (RNA Pol II transcription factor) is excluded because the protein is bacterial (no RNA Pol II machinery). Option D (ester-bond hydrolase, EC 3.1) is excluded because ATP hydrolysis acts on phosphoanhydride bonds (EC 3.6), not ester bonds. Option B (carbohydrate derivative binding) is a very broad parent term; standard GO annotation practice and the 'best describes' phrasing favor the most specific applicable term.",
    "missing_item_specific_fact": "None strictly required. The Walker A motif and ABC signature motifs are identifiable from the raw sequence by a knowledgeable reader without database lookup.",
    "reason": "A model with general biochemistry knowledge can recognize the Walker A P-loop motif from the sequence, infer nucleotide binding, identify additional ABC transporter hallmarks to narrow to ATP binding specifically, and eliminate C (bacterial protein, no eukaryotic transcription machinery) and D (wrong bond chemistry). The A-vs-B distinction is resolved by the GO specificity principle and the 'best describes' wording."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0005524 (ATP binding) is a descendant of GO:0097367 (carbohydrate derivative binding) in the GO DAG, making B technically true by inheritance, standard GO annotation convention and the question's 'best describes its primary molecular function' phrasing unambiguously favor the most specific term (A). Options C and D are clearly incorrect. No genuine ambiguity remains for a well-informed respondent."
  },
  "important_caveats": [
    "The GO:0005524 annotation carries IEA:InterPro evidence (computational inference from domain match), not direct experimental ATP-binding measurement. However, the protein's ABC transporter identity is experimentally supported (ECO:0000269, PubMed:39375957), and ATP binding is a defining mechanistic requirement of ABC transporters.",
    "GO:0005524 is an is_a descendant of GO:0097367 (carbohydrate derivative binding), so option B is technically satisfied by the same annotation. The question relies on the convention of selecting the most specific GO term, which is standard practice but not explicitly stated in the stem.",
    "The protein was first public in Feb 2025; the benchmark author snapshot date is unknown, so the annotation context at question-construction time may have differed slightly."
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

**Accession:** `P0DXU5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
"P0DXU5"
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ATP-binding protein DrrA2"}}}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39375957","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux (PubMed:39375957). Responsible for energy coupling to the transport system (Probable). Confers self-resistance to daunorubicin, an antibiotic produced by S.coeruleorubidus (PubMed:39375957)"}]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33148"}}],"reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"name":"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33147"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:64677"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"database":"GO","id":"GO:0005524","properties":[{"key":"GoTerm","value":"F:ATP binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"database":"GO","id":"GO:0016887","properties":[{"key":"GoTerm","value":"F:ATP hydrolysis activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
ID   DRRA2_STRC4             Reviewed;         322 AA.
AC   P0DXU5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
GN   Name=drrA2 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_15995 {ECO:0000312|EMBL:WOT35541.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 26-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
CC   -!- FUNCTION: Part of the ABC transporter complex DrrA2B2 involved in
CC       daunorubicin efflux (PubMed:39375957). Responsible for energy coupling
CC       to the transport system (Probable). Confers self-resistance to
CC       daunorubicin, an antibiotic produced by S.coeruleorubidus
CC       (PubMed:39375957). {ECO:0000269|PubMed:39375957, ECO:0000305}.
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 31-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;
CC         Evidence={ECO:0000305|PubMed:39375957};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;
CC         Evidence={ECO:0000305|PubMed:39375957};
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
DR   GO; GO:0016887; F:ATP hydrolysis activity; IEA:InterPro.
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
