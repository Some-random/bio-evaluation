# GO_molecular_function_0048

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — chorismate synthase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. ATP hydrolysis activity
B. heme oxygenase (decyclizing) activity
C. chorismate synthase activity
D. single-stranded DNA binding
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

> The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.


**Missing item-specific fact**

> That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.


**Reason**

> Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity.


### Important caveats

- The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.
- The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.",
    "reason": "Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices."
  },
  "important_caveats": [
    "The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.",
    "The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.",
    "missing_item_specific_fact": "That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.",
    "reason": "Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity."
  },
  "important_caveats": [
    "The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.",
    "The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C11](#evidence-c11), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could attempt elimination: (A) no Walker A (GxxxxGK&#91;S/T&#93;) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.


**Missing item-specific fact**

> Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.


**Reason**

> While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence.


### Important caveats

- The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.
- The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.
- The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.
- The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could attempt elimination: (A) no Walker A (GxxxxGK[S/T]) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.",
    "reason": "While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C11",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa)."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.",
    "The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.",
    "The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C11", "H1", "H3", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could attempt elimination: (A) no Walker A (GxxxxGK[S/T]) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.",
    "missing_item_specific_fact": "Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.",
    "reason": "While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.",
    "The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.",
    "The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21021"}}],"reaction":{"ecNumber":"4.2.3.5","evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"name":"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21020"},{"database":"ChEBI","id":"CHEBI:29748"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57701"}]}}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"database":"GO","id":"GO:0004107","properties":[{"key":"GoTerm","value":"F:chorismate synthase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"citation":{"authors":["Khera H.K.","Singh S.K.","Singh S."],"citationCrossReferences":[{"database":"PubMed","id":"31381947"},{"database":"DOI","id":"10.1016/j.molbiopara.2019.111202"}],"citationType":"journal article","firstPage":"111202","id":"31381947","journal":"Mol. Biochem. Parasitol.","lastPage":"111202","publicationDate":"2019","title":"Chorismate synthase from malaria parasites is bifunctional enzyme.","volume":"233"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
ID   AROC_PLAVS              Reviewed;         547 AA.
AC   A5K264;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-FEB-2011, sequence version 1.
DT   28-JAN-2026, entry version 64.
DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:31381947};
DE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};
DE            EC=4.2.3.5 {ECO:0000269|PubMed:31381947};
GN   Name=CS {ECO:0000305}; ORFNames=PVX_114265 {ECO:0000312|EMBL:EDL46514.1};
OS   Plasmodium vivax (strain Salvador I).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).
OX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

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
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +
CC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;
CC         Evidence={ECO:0000269|PubMed:31381947};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
DR   GO; GO:0004107; F:chorismate synthase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 35553-35568`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004107
name: chorismate synthase activity
namespace: molecular_function
def: "Catalysis of the reaction: 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate." [EC:4.2.3.5, RHEA:21020]
synonym: "5-enolpyruvylshikimate-3-phosphate phospholyase activity" RELATED [EC:4.2.3.5]
synonym: "5-O-(1-carboxyvinyl)-3-phosphoshikimate phosphate-lyase (chorismate-forming)" RELATED [EC:4.2.3.5]
synonym: "5-O-(1-carboxyvinyl)-3-phosphoshikimate phosphate-lyase activity" RELATED [EC:4.2.3.5]
xref: EC:4.2.3.5
xref: KEGG_REACTION:R01714
xref: MetaCyc:CHORISMATE-SYNTHASE-RXN
xref: RHEA:21020
is_a: GO:0016838 ! carbon-oxygen lyase activity, acting on phosphates
property_value: skos:exactMatch EC:4.2.3.5
property_value: skos:exactMatch RHEA:21020

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
