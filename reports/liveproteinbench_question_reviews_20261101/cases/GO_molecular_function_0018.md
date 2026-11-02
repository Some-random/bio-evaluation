# GO_molecular_function_0018

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — zinc ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAKSPEVEHPVKAFGWAARDPSGVLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSDDLENYCPGQILTYSAAYTDGTTTYGGYSNLMVSDEHFVICWPENLPMDIGAPLLCAGITTYSPLRYFGLDKPGTHVGVVGLGGLGHVAVKFAKAFGAKVTVISTSESKKQEAIEKLGADAFLVSRDPEQMQGAAGSMDGIIDTVSAVHPVLPLVNLLKSQGKLIMVGAPEKPLELPVFPLLAGRRIIAGSAIGGLKETQEMIDFAAKNNILPDVELVPMDYVNTAMERLLKADVKYRFVIDIGNTLKSA

[Multiple Choices]
A. zinc ion binding
B. cadmium ion transmembrane transporter activity
C. isomerase activity
D. monooxygenase activity
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

> The matched sequence has a zinc-ion-binding GO annotation, but its evidence is computational (IEA:InterPro), not a direct metal-binding experiment. The same protein is reported to catalyze an alcohol-dehydrogenase reaction; that specific activity is not among the choices.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous Cys/His-rich region compatible with metal coordination, while it lacks the extended hydrophobic segment expected of a membrane transporter. These features favor zinc binding over cadmium transmembrane transport; the sequence does not suggest a monooxygenase.


**Missing item-specific fact**

> A direct experimental measurement of zinc binding is not supplied; the annotation supporting it is computational.


**Reason**

> Sequence motifs provide a defensible basis for favoring zinc binding among these options, although they do not establish it experimentally or identify the protein's specific substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only zinc binding is supported among the listed choices. However, the protein's reported alcohol-dehydrogenase activity is absent, so the choices do not include its specific catalytic function.


### Important caveats

- The GO zinc-binding annotation is IEA:InterPro, not experimental evidence.
- The matched protein has experimentally evidenced alcohol-dehydrogenase activity, which is distinct from the zinc-binding annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich region compatible with metal coordination, while it lacks the extended hydrophobic segment expected of a membrane transporter. These features favor zinc binding over cadmium transmembrane transport; the sequence does not suggest a monooxygenase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A direct experimental measurement of zinc binding is not supplied; the annotation supporting it is computational.",
    "reason": "Sequence motifs provide a defensible basis for favoring zinc binding among these options, although they do not establish it experimentally or identify the protein's specific substrate."
  },
  "case_id": "GO_molecular_function_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a zinc-ion-binding GO annotation, but its evidence is computational (IEA:InterPro), not a direct metal-binding experiment. The same protein is reported to catalyze an alcohol-dehydrogenase reaction; that specific activity is not among the choices."
  },
  "important_caveats": [
    "The GO zinc-binding annotation is IEA:InterPro, not experimental evidence.",
    "The matched protein has experimentally evidenced alcohol-dehydrogenase activity, which is distinct from the zinc-binding annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only zinc binding is supported among the listed choices. However, the protein's reported alcohol-dehydrogenase activity is absent, so the choices do not include its specific catalytic function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a zinc-ion-binding GO annotation, but its evidence is computational (IEA:InterPro), not a direct metal-binding experiment. The same protein is reported to catalyze an alcohol-dehydrogenase reaction; that specific activity is not among the choices.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich region compatible with metal coordination, while it lacks the extended hydrophobic segment expected of a membrane transporter. These features favor zinc binding over cadmium transmembrane transport; the sequence does not suggest a monooxygenase.",
    "missing_item_specific_fact": "A direct experimental measurement of zinc binding is not supplied; the annotation supporting it is computational.",
    "reason": "Sequence motifs provide a defensible basis for favoring zinc binding among these options, although they do not establish it experimentally or identify the protein's specific substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only zinc binding is supported among the listed choices. However, the protein's reported alcohol-dehydrogenase activity is absent, so the choices do not include its specific catalytic function."
  },
  "important_caveats": [
    "The GO zinc-binding annotation is IEA:InterPro, not experimental evidence.",
    "The matched protein has experimentally evidenced alcohol-dehydrogenase activity, which is distinct from the zinc-binding annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U4AHM6 (CAD2_RAUSE) carries GO:0008270 'zinc ion binding' as an annotation (evidence IEA:InterPro, C8/H6). The sequence contains Cys-His and Cys-cluster motifs (e.g., 'CICHSDLHM', 'SCRKCDMCS') consistent with zinc coordination in alcohol dehydrogenases. However, the PRIMARY molecular function per experimental evidence (ECO:0000269, PubMed:26715562) is GO:0045551 'cinnamyl-alcohol dehydrogenase activity' (C7/H5), which is NOT among the options. Zinc binding is a cofactor/structural annotation, not the primary catalytic function. The expected answer is supported as an annotation present on this protein, but calling it the 'primary molecular function' is inaccurate; it is the only option with any annotation linkage to this protein.

Citations as saved: [C8](#evidence-c8), [H6](#evidence-h6), [C7](#evidence-c7), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of the alcohol dehydrogenase (ADH) superfamily: a Rossmann-fold NAD(P)-binding region, catalytic Cys-His zinc-coordinating motifs ('CICHSDLHM'), and Cys clusters ('SCRKCDMCS'). General knowledge that ADHs are zinc metalloenzymes supports zinc ion binding. Options B (cadmium transporter) is eliminated by absence of transmembrane helices; C (isomerase) is eliminated by presence of NAD(P)-binding and catalytic motifs indicating oxidoreductase chemistry; D (monooxygenase) is eliminated because monooxygenases require heme or flavin cofactors and incorporate oxygen into substrate, whereas this enzyme transfers hydride to NADP+ (EC 1.1.1.195). By elimination and positive motif evidence, A is the only defensible choice.


**Missing item-specific fact**

> None strictly required. The elimination of B, C, D and the recognition of zinc-binding motifs in the sequence are achievable from general ADH-family biology. The imperfect framing ('primary molecular function' when the true primary function—dehydrogenase activity—is absent from options) adds confusion but does not require a protein-specific lookup to select A over B/C/D.


**Reason**

> A model with general knowledge of the ADH superfamily, zinc metalloenzyme catalysis, and enzyme-class distinctions can eliminate B, C, D and identify A via motif recognition and elimination reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the true primary function (cinnamyl-alcohol dehydrogenase activity) is absent from the options, the remaining three (B, C, D) are clearly incompatible with the sequence's ADH-family architecture. Zinc ion binding (A) is the only option with any annotation linkage and is consistent with the observed Cys/His motifs. No other option is defensible.


### Important caveats

- The GO:0008270 annotation is IEA (Inferred from Electronic Annotation via InterPro), not experimentally verified for this specific protein. The experimental evidence supports dehydrogenase activity, not zinc binding per se.
- The question asks for 'primary molecular function' but the true primary function (cinnamyl-alcohol dehydrogenase activity, GO:0045551, EXP evidence) is not among the choices. This framing is misleading; zinc binding is a secondary cofactor-binding annotation.
- The protein is a dehydrogenase (EC 1.1.1.195, oxidoreductase), not a monooxygenase (EC 1.14). Option D is a common but incorrect conflation of oxidoreductase subclasses.
- The accession and annotation were identified via reviewer-only metadata; the evaluated model had access only to the raw sequence and options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the alcohol dehydrogenase (ADH) superfamily: a Rossmann-fold NAD(P)-binding region, catalytic Cys-His zinc-coordinating motifs ('CICHSDLHM'), and Cys clusters ('SCRKCDMCS'). General knowledge that ADHs are zinc metalloenzymes supports zinc ion binding. Options B (cadmium transporter) is eliminated by absence of transmembrane helices; C (isomerase) is eliminated by presence of NAD(P)-binding and catalytic motifs indicating oxidoreductase chemistry; D (monooxygenase) is eliminated because monooxygenases require heme or flavin cofactors and incorporate oxygen into substrate, whereas this enzyme transfers hydride to NADP+ (EC 1.1.1.195). By elimination and positive motif evidence, A is the only defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, D and the recognition of zinc-binding motifs in the sequence are achievable from general ADH-family biology. The imperfect framing ('primary molecular function' when the true primary function—dehydrogenase activity—is absent from options) adds confusion but does not require a protein-specific lookup to select A over B/C/D.",
    "reason": "A model with general knowledge of the ADH superfamily, zinc metalloenzyme catalysis, and enzyme-class distinctions can eliminate B, C, D and identify A via motif recognition and elimination reasoning."
  },
  "case_id": "GO_molecular_function_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H6",
      "C7",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U4AHM6 (CAD2_RAUSE) carries GO:0008270 'zinc ion binding' as an annotation (evidence IEA:InterPro, C8/H6). The sequence contains Cys-His and Cys-cluster motifs (e.g., 'CICHSDLHM', 'SCRKCDMCS') consistent with zinc coordination in alcohol dehydrogenases. However, the PRIMARY molecular function per experimental evidence (ECO:0000269, PubMed:26715562) is GO:0045551 'cinnamyl-alcohol dehydrogenase activity' (C7/H5), which is NOT among the options. Zinc binding is a cofactor/structural annotation, not the primary catalytic function. The expected answer is supported as an annotation present on this protein, but calling it the 'primary molecular function' is inaccurate; it is the only option with any annotation linkage to this protein."
  },
  "important_caveats": [
    "The GO:0008270 annotation is IEA (Inferred from Electronic Annotation via InterPro), not experimentally verified for this specific protein. The experimental evidence supports dehydrogenase activity, not zinc binding per se.",
    "The question asks for 'primary molecular function' but the true primary function (cinnamyl-alcohol dehydrogenase activity, GO:0045551, EXP evidence) is not among the choices. This framing is misleading; zinc binding is a secondary cofactor-binding annotation.",
    "The protein is a dehydrogenase (EC 1.1.1.195, oxidoreductase), not a monooxygenase (EC 1.14). Option D is a common but incorrect conflation of oxidoreductase subclasses.",
    "The accession and annotation were identified via reviewer-only metadata; the evaluated model had access only to the raw sequence and options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the true primary function (cinnamyl-alcohol dehydrogenase activity) is absent from the options, the remaining three (B, C, D) are clearly incompatible with the sequence's ADH-family architecture. Zinc ion binding (A) is the only option with any annotation linkage and is consistent with the observed Cys/His motifs. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U4AHM6 (CAD2_RAUSE) carries GO:0008270 'zinc ion binding' as an annotation (evidence IEA:InterPro, C8/H6). The sequence contains Cys-His and Cys-cluster motifs (e.g., 'CICHSDLHM', 'SCRKCDMCS') consistent with zinc coordination in alcohol dehydrogenases. However, the PRIMARY molecular function per experimental evidence (ECO:0000269, PubMed:26715562) is GO:0045551 'cinnamyl-alcohol dehydrogenase activity' (C7/H5), which is NOT among the options. Zinc binding is a cofactor/structural annotation, not the primary catalytic function. The expected answer is supported as an annotation present on this protein, but calling it the 'primary molecular function' is inaccurate; it is the only option with any annotation linkage to this protein.",
    "evidence_ids": ["C8", "H6", "C7", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the alcohol dehydrogenase (ADH) superfamily: a Rossmann-fold NAD(P)-binding region, catalytic Cys-His zinc-coordinating motifs ('CICHSDLHM'), and Cys clusters ('SCRKCDMCS'). General knowledge that ADHs are zinc metalloenzymes supports zinc ion binding. Options B (cadmium transporter) is eliminated by absence of transmembrane helices; C (isomerase) is eliminated by presence of NAD(P)-binding and catalytic motifs indicating oxidoreductase chemistry; D (monooxygenase) is eliminated because monooxygenases require heme or flavin cofactors and incorporate oxygen into substrate, whereas this enzyme transfers hydride to NADP+ (EC 1.1.1.195). By elimination and positive motif evidence, A is the only defensible choice.",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, D and the recognition of zinc-binding motifs in the sequence are achievable from general ADH-family biology. The imperfect framing ('primary molecular function' when the true primary function—dehydrogenase activity—is absent from options) adds confusion but does not require a protein-specific lookup to select A over B/C/D.",
    "reason": "A model with general knowledge of the ADH superfamily, zinc metalloenzyme catalysis, and enzyme-class distinctions can eliminate B, C, D and identify A via motif recognition and elimination reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the true primary function (cinnamyl-alcohol dehydrogenase activity) is absent from the options, the remaining three (B, C, D) are clearly incompatible with the sequence's ADH-family architecture. Zinc ion binding (A) is the only option with any annotation linkage and is consistent with the observed Cys/His motifs. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0008270 annotation is IEA (Inferred from Electronic Annotation via InterPro), not experimentally verified for this specific protein. The experimental evidence supports dehydrogenase activity, not zinc binding per se.",
    "The question asks for 'primary molecular function' but the true primary function (cinnamyl-alcohol dehydrogenase activity, GO:0045551, EXP evidence) is not among the choices. This framing is misleading; zinc binding is a secondary cofactor-binding annotation.",
    "The protein is a dehydrogenase (EC 1.1.1.195, oxidoreductase), not a monooxygenase (EC 1.14). Option D is a common but incorrect conflation of oxidoreductase subclasses.",
    "The accession and annotation were identified via reviewer-only metadata; the evaluated model had access only to the raw sequence and options."
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

**Accession:** `A0A0U4AHM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
"A0A0U4AHM6"
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR6"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR6"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"1.1.1.195"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Cinnamyl alcohol dehydrogenase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsCAD2"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"Alcohol dehydrogenase that catalyzes the conversion of (E)-cinnamyl alcohol to (E)-cinnamaldehyde"}]}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10394"}}],"reaction":{"ecNumber":"1.1.1.195","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"name":"(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10392"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16731"},{"database":"ChEBI","id":"CHEBI:33227"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"id":"GO:0045551","properties":[{"key":"GoTerm","value":"F:cinnamyl-alcohol dehydrogenase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"database":"GO","id":"GO:0008270","properties":[{"key":"GoTerm","value":"F:zinc ion binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 27-28`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
CC   -!- FUNCTION: Alcohol dehydrogenase that catalyzes the conversion of (E)-
CC       cinnamyl alcohol to (E)-cinnamaldehyde. {ECO:0000269|PubMed:26715562}.
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 29-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH +
CC         H(+); Xref=Rhea:RHEA:10392, ChEBI:CHEBI:15378, ChEBI:CHEBI:16731,
CC         ChEBI:CHEBI:33227, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.1.1.195; Evidence={ECO:0000269|PubMed:26715562};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:10394;
CC         Evidence={ECO:0000269|PubMed:26715562};
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
DR   GO; GO:0045551; F:cinnamyl-alcohol dehydrogenase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
DR   GO; GO:0008270; F:zinc ion binding; IEA:InterPro.
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence GO2

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
