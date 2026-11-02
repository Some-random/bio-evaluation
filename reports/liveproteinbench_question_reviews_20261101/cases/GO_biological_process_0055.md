# GO_biological_process_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — microtubule cytoskeleton organization

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MERSGGNGAGARAGAPSEGAAKGSSLLSAKSTEGATGRFSQSTPRPTGMDGFLKSDERQRLAKERREEREKCLAAREQQILEKQKRAKLQYEKQIEERWRKLEEQRQREDQKRAAVEEKRKQKLREEEERLEAMMRRSLERTQQLELKKKCSWAGSAASGPGGRDGESENTPPLPLTLAASIPPSDTGTATAAAESTNACDKLSTSTMNLPKQTEPPMSKHLSSSIVAISYSPDRALRSPLKSSYKSSPTRTTEKKKNTLLSGVGDAGKGAMTGGEPSQMEKVKKGRGATSVSSGGLGSPLRRCEPPENISKRSSSPVKSKVTAKTYPQSPKTVKPTYIGSPVKYYFPPTPSEETLKKKAEKEKSNKEKEGATGRQTTVLPREETLEKPMADKDATEKYVADKHATEKHSATGGKAEHSAGKSTAGTTDAGEAAKILAEKRRQARLQKEQEEQERLEKEEQERLEKEELKRKAEEERLRIEKQEEEKKQQEEEEKRKAEEKAKEKAEEELLSKEEQEKEKQEKEKKEKAMIEKQIQAEKEAAEAKAQDAAKQMRLEREQIMLQIEQERLERKKRIDEIMKRTRKSDASLEVKKEDPKVEIQPLPDVENKIKPVVPNKIEINVLNTCQKVNVSERAAPETFPQDIFSNGLKPVGGPVHPDVLDGKSNSLDDSTEEVQSMDVSPVSKEELISIPEFSPVSEMIPGMSLDQNGTGNARALQDILDFTGPPAFPKKSSENLSLDDCNKNLIEGFNSPGQETTLNTFC

[Multiple Choices]
A. venom-mediated fibrinolysis
B. positive regulation of transcription elongation by RNA polymerase II
C. amino acid activation for nonribosomal peptide biosynthetic process
D. microtubule cytoskeleton organization
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

> The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.


**Missing item-specific fact**

> The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.


**Reason**

> That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported.


### Important caveats

- The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.
- The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.",
    "reason": "That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process."
  },
  "important_caveats": [
    "The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process.",
    "evidence_ids": ["C1", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.",
    "reason": "That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported."
  },
  "important_caveats": [
    "The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H3](#evidence-h3), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.


**Missing item-specific fact**

> Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.


**Reason**

> The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity.


### Important caveats

- The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.
- The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.
- The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.",
    "reason": "The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "H3",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim."
  },
  "important_caveats": [
    "The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.",
    "The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.",
    "The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim.",
    "evidence_ids": ["C5", "C7", "C9", "H3", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.",
    "missing_item_specific_fact": "Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.",
    "reason": "The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity."
  },
  "important_caveats": [
    "The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.",
    "The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.",
    "The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology."
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

**Accession:** `D4A4L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 89. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:48.272925+00:00.  

```json
"D4A4L4"
```

Source SHA-256: `0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:48.272925+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A2AG50","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30784582","source":"PubMed"}],"value":"Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth (By similarity). Acts as a critical cofactor for kinesin transport; in the proximal axon regulates kinesin-1 family members, KIF5A, KIF5B and KIF5C recruitment to microtubules and contributes to kinesin-1-mediated transport in the axons (PubMed:30784582)"}]}
```

Source SHA-256: `0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)  
**Locator:** `/uniProtKBCrossReferences/40`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:48.272925+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000315","id":"35470240","source":"PubMed"}],"id":"GO:0000226","properties":[{"key":"GoTerm","value":"P:microtubule cytoskeleton organization"},{"key":"GoEvidenceType","value":"IMP:UniProtKB"}]}
```

Source SHA-256: `0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:48.272925+00:00.  

```json
{"citation":{"authors":["Kikuchi K.","Sakamoto Y.","Uezu A.","Yamamoto H.","Ishiguro K.I.","Shimamura K.","Saito T.","Hisanaga S.I.","Nakanishi H."],"citationCrossReferences":[{"database":"PubMed","id":"35470240"},{"database":"DOI","id":"10.26508/lsa.202201390"}],"citationType":"journal article","firstPage":"0","id":"35470240","journal":"Life. Sci Alliance","lastPage":"0","publicationDate":"2022","title":"Map7D2 and Map7D1 facilitate microtubule stabilization through distinct mechanisms in neuronal cells.","volume":"5"},"referenceNumber":5,"referencePositions":["TISSUE SPECIFICITY","SUBCELLULAR LOCATION","INTERACTION WITH MICROTUBULES","SUBUNIT"]}
```

Source SHA-256: `0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)  
**Locator:** `lines 93-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 4.  
**Retrieved:** 2026-11-02T04:27:53.462029+00:00.  

```text
CC   -!- FUNCTION: Microtubule-stabilizing protein involved in the control of
CC       cell motility and neurite outgrowth (By similarity). Acts as a critical
CC       cofactor for kinesin transport; in the proximal axon regulates kinesin-
CC       1 family members, KIF5A, KIF5B and KIF5C recruitment to microtubules
CC       and contributes to kinesin-1-mediated transport in the axons
CC       (PubMed:30784582). {ECO:0000250|UniProtKB:A2AG50,
CC       ECO:0000269|PubMed:30784582}.
```

Source SHA-256: `86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)  
**Locator:** `lines 152-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 4.  
**Retrieved:** 2026-11-02T04:27:53.462029+00:00.  

```text
DR   GO; GO:0000226; P:microtubule cytoskeleton organization; IMP:UniProtKB.
```

Source SHA-256: `86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 2328-2338`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000226
name: microtubule cytoskeleton organization
namespace: biological_process
def: "A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins." [GOC:mah]
subset: goslim_pombe
synonym: "microtubule cytoskeleton organisation" EXACT [GOC:mah]
synonym: "microtubule cytoskeleton organization and biogenesis" RELATED [GOC:mah]
is_a: GO:0007010 ! cytoskeleton organization
is_a: GO:0007017 ! microtubule-based process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
