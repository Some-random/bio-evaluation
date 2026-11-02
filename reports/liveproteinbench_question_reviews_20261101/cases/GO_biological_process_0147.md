# GO_biological_process_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — chorismate biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. transsulfuration
B. neuropeptide signaling pathway
C. chorismate biosynthetic process
D. peroxisome organization
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the Plasmodium vivax protein annotated as a bifunctional chorismate synthase/flavin reductase. Its annotated activity converts EPSP to chorismate, directly supporting choice C. The function annotation cites experimental evidence, while the specific GO annotation is computationally assigned.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct processes, but the input supplies only an amino-acid sequence and no organism or functional context. No clear sequence feature in the provided input meaningfully identifies chorismate synthase over the alternatives without protein-specific functional identification.


**Missing item-specific fact**

> The protein's identity or functional annotation as chorismate synthase, including its conversion of EPSP to chorismate, is absent from the model input.


**Reason**

> Selecting C depends on knowing or identifying this particular protein's function. Reviewer-only database evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports chorismate biosynthesis specifically; none of the other listed processes is comparably supported.


### Important caveats

- The sequence match establishes applicability to the cited Plasmodium vivax record, but does not establish which source snapshot the author used.
- The UniProt function annotation cites experimental evidence; the GO:0009423 assignment is computational (IEA), and the cited primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct processes, but the input supplies only an amino-acid sequence and no organism or functional context. No clear sequence feature in the provided input meaningfully identifies chorismate synthase over the alternatives without protein-specific functional identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or functional annotation as chorismate synthase, including its conversion of EPSP to chorismate, is absent from the model input.",
    "reason": "Selecting C depends on knowing or identifying this particular protein's function. Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C8",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as a bifunctional chorismate synthase/flavin reductase. Its annotated activity converts EPSP to chorismate, directly supporting choice C. The function annotation cites experimental evidence, while the specific GO annotation is computationally assigned."
  },
  "important_caveats": [
    "The sequence match establishes applicability to the cited Plasmodium vivax record, but does not establish which source snapshot the author used.",
    "The UniProt function annotation cites experimental evidence; the GO:0009423 assignment is computational (IEA), and the cited primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports chorismate biosynthesis specifically; none of the other listed processes is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as a bifunctional chorismate synthase/flavin reductase. Its annotated activity converts EPSP to chorismate, directly supporting choice C. The function annotation cites experimental evidence, while the specific GO annotation is computationally assigned.",
    "evidence_ids": ["C1", "C3", "C5", "C8", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct processes, but the input supplies only an amino-acid sequence and no organism or functional context. No clear sequence feature in the provided input meaningfully identifies chorismate synthase over the alternatives without protein-specific functional identification.",
    "missing_item_specific_fact": "The protein's identity or functional annotation as chorismate synthase, including its conversion of EPSP to chorismate, is absent from the model input.",
    "reason": "Selecting C depends on knowing or identifying this particular protein's function. Reviewer-only database evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports chorismate biosynthesis specifically; none of the other listed processes is comparably supported."
  },
  "important_caveats": [
    "The sequence match establishes applicability to the cited Plasmodium vivax record, but does not establish which source snapshot the author used.",
    "The UniProt function annotation cites experimental evidence; the GO:0009423 assignment is computational (IEA), and the cited primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProtKB A5K264 (AROC_PLAVS), annotated as chorismate synthase (EC 4.2.3.5) from Plasmodium vivax. Experimental evidence (ECO:0000269, PubMed:31381947) confirms catalytic conversion of EPSP to chorismate. GO:0009423 (chorismate biosynthetic process) is directly annotated. The pathway comment states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The expected answer C is well-supported by both experimental and computational annotations.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved 'GAD' catalytic motif (Gly-Ala-Asp) characteristic of the chorismate synthase family, along with flavin-binding regions consistent with the bifunctional chorismate synthase/flavin reductase architecture. The other options can be excluded by general biological reasoning: (B) neuropeptide signaling requires GPCR or neuropeptide ligand features (7-TM domains, signal peptides for secreted peptides) absent here; (A) transsulfuration requires CBS domains or PLP-dependent lyase architecture (cystathionine beta-synthase/gamma-lyase) not present; (D) peroxisome organization requires PEX proteins or peroxisomal targeting signals (PTS1: -SKL, PTS2) not evident. The presence of the GAD motif combined with flavin-binding architecture and elimination of the other three options provides a concrete biological argument for chorismate biosynthetic process.


**Missing item-specific fact**

> None strictly required, though confident recognition of the GAD motif as a chorismate synthase signature requires familiarity with this enzyme family's conserved catalytic residues.


**Reason**

> A model with general biochemical knowledge can identify the GAD catalytic motif as a chorismate synthase hallmark and eliminate the other three options through absence of their defining structural features (GPCR helices, CBS domains, peroxisomal targeting signals). This constitutes a concrete biological argument from the sequence itself rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct biological processes with different structural requirements. Only chorismate biosynthetic process is consistent with the sequence features (GAD motif, flavin-binding architecture). The other three options require entirely different protein architectures (GPCR, CBS/PLP enzymes, PEX proteins) that are clearly absent.


### Important caveats

- The GAD motif recognition, while a well-documented chorismate synthase signature, requires specific knowledge of this enzyme family; a model without exposure to chorismate synthase sequences might not identify it confidently.
- The GO annotation for chorismate biosynthetic process (GO:0009423) carries IEA evidence (UniProtKB-UniPathway/TreeGrafter), meaning it is computationally inferred by pathway membership rather than direct experimental GO annotation. However, the underlying catalytic function is experimentally verified (ECO:0000269).
- The protein is bifunctional (chorismate synthase + flavin reductase); the primary biological process assignment to chorismate biosynthesis reflects the synthase activity, which is the canonical annotation.
- Plasmodium vivax is an apicomplexan parasite; the shikimate pathway (including chorismate synthase) is present in apicomplexans and is a validated drug target, but this organism-specific context is not provided to the model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved 'GAD' catalytic motif (Gly-Ala-Asp) characteristic of the chorismate synthase family, along with flavin-binding regions consistent with the bifunctional chorismate synthase/flavin reductase architecture. The other options can be excluded by general biological reasoning: (B) neuropeptide signaling requires GPCR or neuropeptide ligand features (7-TM domains, signal peptides for secreted peptides) absent here; (A) transsulfuration requires CBS domains or PLP-dependent lyase architecture (cystathionine beta-synthase/gamma-lyase) not present; (D) peroxisome organization requires PEX proteins or peroxisomal targeting signals (PTS1: -SKL, PTS2) not evident. The presence of the GAD motif combined with flavin-binding architecture and elimination of the other three options provides a concrete biological argument for chorismate biosynthetic process.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required, though confident recognition of the GAD motif as a chorismate synthase signature requires familiarity with this enzyme family's conserved catalytic residues.",
    "reason": "A model with general biochemical knowledge can identify the GAD catalytic motif as a chorismate synthase hallmark and eliminate the other three options through absence of their defining structural features (GPCR helices, CBS domains, peroxisomal targeting signals). This constitutes a concrete biological argument from the sequence itself rather than pure database lookup."
  },
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProtKB A5K264 (AROC_PLAVS), annotated as chorismate synthase (EC 4.2.3.5) from Plasmodium vivax. Experimental evidence (ECO:0000269, PubMed:31381947) confirms catalytic conversion of EPSP to chorismate. GO:0009423 (chorismate biosynthetic process) is directly annotated. The pathway comment states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The expected answer C is well-supported by both experimental and computational annotations."
  },
  "important_caveats": [
    "The GAD motif recognition, while a well-documented chorismate synthase signature, requires specific knowledge of this enzyme family; a model without exposure to chorismate synthase sequences might not identify it confidently.",
    "The GO annotation for chorismate biosynthetic process (GO:0009423) carries IEA evidence (UniProtKB-UniPathway/TreeGrafter), meaning it is computationally inferred by pathway membership rather than direct experimental GO annotation. However, the underlying catalytic function is experimentally verified (ECO:0000269).",
    "The protein is bifunctional (chorismate synthase + flavin reductase); the primary biological process assignment to chorismate biosynthesis reflects the synthase activity, which is the canonical annotation.",
    "Plasmodium vivax is an apicomplexan parasite; the shikimate pathway (including chorismate synthase) is present in apicomplexans and is a validated drug target, but this organism-specific context is not provided to the model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological processes with different structural requirements. Only chorismate biosynthetic process is consistent with the sequence features (GAD motif, flavin-binding architecture). The other three options require entirely different protein architectures (GPCR, CBS/PLP enzymes, PEX proteins) that are clearly absent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProtKB A5K264 (AROC_PLAVS), annotated as chorismate synthase (EC 4.2.3.5) from Plasmodium vivax. Experimental evidence (ECO:0000269, PubMed:31381947) confirms catalytic conversion of EPSP to chorismate. GO:0009423 (chorismate biosynthetic process) is directly annotated. The pathway comment states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The expected answer C is well-supported by both experimental and computational annotations.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H7", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved 'GAD' catalytic motif (Gly-Ala-Asp) characteristic of the chorismate synthase family, along with flavin-binding regions consistent with the bifunctional chorismate synthase/flavin reductase architecture. The other options can be excluded by general biological reasoning: (B) neuropeptide signaling requires GPCR or neuropeptide ligand features (7-TM domains, signal peptides for secreted peptides) absent here; (A) transsulfuration requires CBS domains or PLP-dependent lyase architecture (cystathionine beta-synthase/gamma-lyase) not present; (D) peroxisome organization requires PEX proteins or peroxisomal targeting signals (PTS1: -SKL, PTS2) not evident. The presence of the GAD motif combined with flavin-binding architecture and elimination of the other three options provides a concrete biological argument for chorismate biosynthetic process.",
    "missing_item_specific_fact": "None strictly required, though confident recognition of the GAD motif as a chorismate synthase signature requires familiarity with this enzyme family's conserved catalytic residues.",
    "reason": "A model with general biochemical knowledge can identify the GAD catalytic motif as a chorismate synthase hallmark and eliminate the other three options through absence of their defining structural features (GPCR helices, CBS domains, peroxisomal targeting signals). This constitutes a concrete biological argument from the sequence itself rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct biological processes with different structural requirements. Only chorismate biosynthetic process is consistent with the sequence features (GAD motif, flavin-binding architecture). The other three options require entirely different protein architectures (GPCR, CBS/PLP enzymes, PEX proteins) that are clearly absent."
  },
  "important_caveats": [
    "The GAD motif recognition, while a well-documented chorismate synthase signature, requires specific knowledge of this enzyme family; a model without exposure to chorismate synthase sequences might not identify it confidently.",
    "The GO annotation for chorismate biosynthetic process (GO:0009423) carries IEA evidence (UniProtKB-UniPathway/TreeGrafter), meaning it is computationally inferred by pathway membership rather than direct experimental GO annotation. However, the underlying catalytic function is experimentally verified (ECO:0000269).",
    "The protein is bifunctional (chorismate synthase + flavin reductase); the primary biological process assignment to chorismate biosynthesis reflects the synthase activity, which is the canonical annotation.",
    "Plasmodium vivax is an apicomplexan parasite; the shikimate pathway (including chorismate synthase) is present in apicomplexans and is a validated drug target, but this organism-specific context is not provided to the model."
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

**Accession:** `A5K264` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 64. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
"A5K264"
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"UP000008333","source":"Proteomes"}],"lineage":["Eukaryota","Sar","Alveolata","Apicomplexa","Aconoidasida","Haemosporida","Plasmodiidae","Plasmodium","Plasmodium"],"scientificName":"Plasmodium vivax (strain Salvador I)","taxonId":126793}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"}}}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"Bifunctional chorismate synthase and flavin reductase (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a flavin reductase (FR) able to generate reduced flavin mononucleotide in the presence of NADPH (PubMed:31381947)"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q12640","source":"UniProtKB"}],"value":"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"database":"GO","id":"GO:0009423","properties":[{"key":"GoTerm","value":"P:chorismate biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 35-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- FUNCTION: Bifunctional chorismate synthase and flavin reductase
CC       (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate
CC       3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a
CC       flavin reductase (FR) able to generate reduced flavin mononucleotide in
CC       the presence of NADPH (PubMed:31381947). {ECO:0000269|PubMed:31381947}.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 54-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;
CC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step
CC       7/7. {ECO:0000250|UniProtKB:Q12640}.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 85-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
DR   GO; GO:0009423; P:chorismate biosynthetic process; IEA:TreeGrafter.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 96113-96136`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009423
name: chorismate biosynthetic process
namespace: biological_process
alt_id: GO:0033587
def: "The chemical reactions and pathways resulting in the formation of the unsymmetrical ether derived from phosphoenolpyruvate and 5-phosphoshikimic acid formed as an intermediate in the biosynthesis of aromatic amino acids and many other compounds." [GOC:sm, ISBN:0198547684]
synonym: "chorismate anabolism" EXACT []
synonym: "chorismate biosynthesis" EXACT []
synonym: "chorismate formation" EXACT []
synonym: "chorismate synthesis" EXACT []
synonym: "shikimate anabolism" RELATED []
synonym: "shikimate biosynthesis" RELATED []
synonym: "shikimate biosynthetic process" RELATED []
synonym: "shikimate pathway" EXACT []
synonym: "shikimate synthesis" RELATED []
xref: MetaCyc:ARO-PWY
xref: MetaCyc:PWY-6163
xref: MetaCyc:PWY-6165
is_a: GO:0043650 ! dicarboxylic acid biosynthetic process
is_a: GO:0046417 ! chorismate metabolic process
property_value: skos:narrowMatch MetaCyc:ARO-PWY
property_value: skos:narrowMatch MetaCyc:PWY-6163
property_value: skos:narrowMatch MetaCyc:PWY-6165

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
