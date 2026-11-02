# GO_biological_process_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — regulation of locomotion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAASSMSSLTSSYHTTAMPSSNSVVPPFDARNLEIKTKSIEQTLIPLVTQITTLVNYKESYMASGKPKSERAMRAALKIGSAVEAAIERFVCVGETIADENADIQPEMYDACTEARLAGASMANLSCACNDDPNSVVDKAVLVRASRQLLSSVTRVLLLADRVLVKQVLRAEDKIAFSLSRLESTRSFNDFVKVFAVFGGEMVELAHRSGDRQHDLKSEKRKAQMSIARTSLERLTMLLLTASKTYLRHPDCDSALQCRDGVFYQMKLSLELIAICVCDGILTTEKSRYIQDEPDMPIDIALQLTANAAIKQLTEMLEMIRMTVRVGAGVRERIVSALDALCQLTQDFTDSAYTPHHQREQILDFLEECRFEMTNLIQPDENEQLAASGLEVTVERLNRRLKDLSKQLQIVAMEQISEVLRANEDQVLLSSMKACAVSGDIDGVEKYMHKFREHADHMQEVCRLLHHISITDALHVHTGHVERNMRALAPLTILAGRTLCVHPSSRIARENLEVFCDTWGQAVNDLSRVAKESDVAANGRVAAEKQAYMSLPRPGKHGTTQKPSKPITLDVEDQQKMAKVGLEMKLLTSEVDAEAEKWDEYAENDIVKRAKAMSSMAYNMYLFTRGDGPLKTTHDLFTQAEFFAEQANQMYRTVREFSYEVPGSAEKSDLSAILERIPLHCQQLQVMVKSPTVGKTATFGKVDSVIQETKNLMNEIAKLVTASFVCATKYEIEFRGGSVNGRTGADGERTSRESTVWRRTPSIRRAAPPTSSHLSANNSSSIHI

[Multiple Choices]
A. envenomation resulting in negative regulation of voltage-gated potassium channel activity in another organism
B. regulation of locomotion
C. cytoplasmic translational elongation
D. amino acid activation for nonribosomal peptide biosynthetic process
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

> The exact sequence matches the C. elegans alpha-catulin CTN-1 record, which has a regulation-of-locomotion GO annotation with IMP evidence; the record also describes experimentally supported roles in potassium-channel localization and neuromuscular function. This supports B, though it does not establish that locomotion is the protein’s uniquely primary process.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is not an obvious enzyme matching the translation-elongation or nonribosomal amino-acid-activation choices, and it lacks a clear basis for the venom-mediated process. But these exclusions do not identify regulation of locomotion from sequence alone.


**Missing item-specific fact**

> The protein-specific identity and evidence linking CTN-1 to locomotion and neuromuscular function are not supplied in the question.


**Reason**

> Selecting B requires the item-specific functional annotation or prior knowledge of this protein; recognizing the sequence or invoking a predictor would not constitute a biological argument available from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B is the supported process annotation; the other options describe unrelated processes. The wording “primary” is not uniquely established by the cited evidence, but does not make another listed option comparably defensible.


### Important caveats

- The sequence match and protein identity are established by reviewer-only evidence, not information given to the evaluated model.
- The GO annotation has IMP evidence; database annotation and experimental support do not prove that this is the protein’s sole or uniquely primary biological process.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is not an obvious enzyme matching the translation-elongation or nonribosomal amino-acid-activation choices, and it lacks a clear basis for the venom-mediated process. But these exclusions do not identify regulation of locomotion from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and evidence linking CTN-1 to locomotion and neuromuscular function are not supplied in the question.",
    "reason": "Selecting B requires the item-specific functional annotation or prior knowledge of this protein; recognizing the sequence or invoking a predictor would not constitute a biological argument available from the prompt."
  },
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the C. elegans alpha-catulin CTN-1 record, which has a regulation-of-locomotion GO annotation with IMP evidence; the record also describes experimentally supported roles in potassium-channel localization and neuromuscular function. This supports B, though it does not establish that locomotion is the protein’s uniquely primary process."
  },
  "important_caveats": [
    "The sequence match and protein identity are established by reviewer-only evidence, not information given to the evaluated model.",
    "The GO annotation has IMP evidence; database annotation and experimental support do not prove that this is the protein’s sole or uniquely primary biological process."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the supported process annotation; the other options describe unrelated processes. The wording “primary” is not uniquely established by the cited evidence, but does not make another listed option comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the C. elegans alpha-catulin CTN-1 record, which has a regulation-of-locomotion GO annotation with IMP evidence; the record also describes experimentally supported roles in potassium-channel localization and neuromuscular function. This supports B, though it does not establish that locomotion is the protein’s uniquely primary process.",
    "evidence_ids": ["C1", "C5", "C7", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is not an obvious enzyme matching the translation-elongation or nonribosomal amino-acid-activation choices, and it lacks a clear basis for the venom-mediated process. But these exclusions do not identify regulation of locomotion from sequence alone.",
    "missing_item_specific_fact": "The protein-specific identity and evidence linking CTN-1 to locomotion and neuromuscular function are not supplied in the question.",
    "reason": "Selecting B requires the item-specific functional annotation or prior knowledge of this protein; recognizing the sequence or invoking a predictor would not constitute a biological argument available from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is the supported process annotation; the other options describe unrelated processes. The wording “primary” is not uniquely established by the cited evidence, but does not make another listed option comparably defensible."
  },
  "important_caveats": [
    "The sequence match and protein identity are established by reviewer-only evidence, not information given to the evaluated model.",
    "The GO annotation has IMP evidence; database annotation and experimental support do not prove that this is the protein’s sole or uniquely primary biological process."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G8JYB2 (Alpha-catulin, C. elegans CTN-1) carries GO:0040012 'regulation of locomotion' with IMP:WormBase evidence code (evidence C7/H8), indicating experimental mutant-phenotype support. The FUNCTION comment (C5/H6) confirms the protein is required for slo-1 BK channel clustering at presynaptic terminals and body-wall muscle dense bodies, and for dystrophin complex localization—all neuromuscular processes whose disruption causes locomotion defects in C. elegans. Multiple PubMed references (20700105, 20865173, 22577143, 31308408) provide experimental basis. The sequence matches exactly (784 AA, SHA256 match).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a large (~784 AA) scaffolding/adaptor protein with catenin-like domains (e.g., 'GSAVEAAIERFVCVGETIADEN' region resembling catenin/cadherin-binding motifs). It lacks: (1) any small disulfide-rich toxin fold or secretory signal peptide needed for option A (venom-mediated potassium channel inhibition in another organism); (2) any ribosomal protein motifs, tRNA-binding domains, or elongation-factor features required for option C (cytoplasmic translational elongation); (3) any adenylation (A-domain) or thiolation (PCP) domains required for option D (amino acid activation for NRPS). By elimination, the only remaining option—B, 'regulation of locomotion'—is consistent with a large cytoskeletal/neuromuscular scaffolding protein in a motile organism. The distractors are categorically incompatible with the protein's domain architecture.


**Missing item-specific fact**

> The specific genetic evidence (IMP) linking ctn-1 loss to locomotion defects via BK channel mislocalization is an experimental finding, but it is not strictly needed to select B over the other three options, which are eliminated by domain-architecture reasoning.


**Reason**

> While the precise annotation 'regulation of locomotion' as the primary BP derives from genetic studies, the four answer choices are sufficiently heterogeneous that general protein-architecture reasoning (no toxin fold, no ribosomal features, no NRPS adenylation domain) eliminates A, C, and D, leaving B as the only viable option. This constitutes a concrete biological argument from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are categorically incompatible with the protein's domain architecture and organismal context (C. elegans intracellular scaffolding protein). No other option among the four is defensible for this sequence.


### Important caveats

- The protein also carries IEA:InterPro annotations for 'cell adhesion' (GO:0007155) and 'Rho protein signal transduction' (GO:0007266), which were not offered as options. If these had been included as distractors, the question would be much harder to resolve by reasoning alone.
- The IMP evidence for locomotion regulation is specific to C. elegans genetic studies; the protein's molecular function is scaffolding/localization, and 'regulation of locomotion' is a downstream phenotypic annotation rather than a direct molecular-process description.
- The accession G8JYB2 was first publicly released 2025-04-09; the benchmark's author snapshot is unknown but the historical entry (version 84) matches the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a large (~784 AA) scaffolding/adaptor protein with catenin-like domains (e.g., 'GSAVEAAIERFVCVGETIADEN' region resembling catenin/cadherin-binding motifs). It lacks: (1) any small disulfide-rich toxin fold or secretory signal peptide needed for option A (venom-mediated potassium channel inhibition in another organism); (2) any ribosomal protein motifs, tRNA-binding domains, or elongation-factor features required for option C (cytoplasmic translational elongation); (3) any adenylation (A-domain) or thiolation (PCP) domains required for option D (amino acid activation for NRPS). By elimination, the only remaining option—B, 'regulation of locomotion'—is consistent with a large cytoskeletal/neuromuscular scaffolding protein in a motile organism. The distractors are categorically incompatible with the protein's domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific genetic evidence (IMP) linking ctn-1 loss to locomotion defects via BK channel mislocalization is an experimental finding, but it is not strictly needed to select B over the other three options, which are eliminated by domain-architecture reasoning.",
    "reason": "While the precise annotation 'regulation of locomotion' as the primary BP derives from genetic studies, the four answer choices are sufficiently heterogeneous that general protein-architecture reasoning (no toxin fold, no ribosomal features, no NRPS adenylation domain) eliminates A, C, and D, leaving B as the only viable option. This constitutes a concrete biological argument from the sequence."
  },
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "C10",
      "C11",
      "C12",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G8JYB2 (Alpha-catulin, C. elegans CTN-1) carries GO:0040012 'regulation of locomotion' with IMP:WormBase evidence code (evidence C7/H8), indicating experimental mutant-phenotype support. The FUNCTION comment (C5/H6) confirms the protein is required for slo-1 BK channel clustering at presynaptic terminals and body-wall muscle dense bodies, and for dystrophin complex localization—all neuromuscular processes whose disruption causes locomotion defects in C. elegans. Multiple PubMed references (20700105, 20865173, 22577143, 31308408) provide experimental basis. The sequence matches exactly (784 AA, SHA256 match)."
  },
  "important_caveats": [
    "The protein also carries IEA:InterPro annotations for 'cell adhesion' (GO:0007155) and 'Rho protein signal transduction' (GO:0007266), which were not offered as options. If these had been included as distractors, the question would be much harder to resolve by reasoning alone.",
    "The IMP evidence for locomotion regulation is specific to C. elegans genetic studies; the protein's molecular function is scaffolding/localization, and 'regulation of locomotion' is a downstream phenotypic annotation rather than a direct molecular-process description.",
    "The accession G8JYB2 was first publicly released 2025-04-09; the benchmark's author snapshot is unknown but the historical entry (version 84) matches the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are categorically incompatible with the protein's domain architecture and organismal context (C. elegans intracellular scaffolding protein). No other option among the four is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G8JYB2 (Alpha-catulin, C. elegans CTN-1) carries GO:0040012 'regulation of locomotion' with IMP:WormBase evidence code (evidence C7/H8), indicating experimental mutant-phenotype support. The FUNCTION comment (C5/H6) confirms the protein is required for slo-1 BK channel clustering at presynaptic terminals and body-wall muscle dense bodies, and for dystrophin complex localization—all neuromuscular processes whose disruption causes locomotion defects in C. elegans. Multiple PubMed references (20700105, 20865173, 22577143, 31308408) provide experimental basis. The sequence matches exactly (784 AA, SHA256 match).",
    "evidence_ids": ["C5", "C7", "C9", "C10", "C11", "C12", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a large (~784 AA) scaffolding/adaptor protein with catenin-like domains (e.g., 'GSAVEAAIERFVCVGETIADEN' region resembling catenin/cadherin-binding motifs). It lacks: (1) any small disulfide-rich toxin fold or secretory signal peptide needed for option A (venom-mediated potassium channel inhibition in another organism); (2) any ribosomal protein motifs, tRNA-binding domains, or elongation-factor features required for option C (cytoplasmic translational elongation); (3) any adenylation (A-domain) or thiolation (PCP) domains required for option D (amino acid activation for NRPS). By elimination, the only remaining option—B, 'regulation of locomotion'—is consistent with a large cytoskeletal/neuromuscular scaffolding protein in a motile organism. The distractors are categorically incompatible with the protein's domain architecture.",
    "missing_item_specific_fact": "The specific genetic evidence (IMP) linking ctn-1 loss to locomotion defects via BK channel mislocalization is an experimental finding, but it is not strictly needed to select B over the other three options, which are eliminated by domain-architecture reasoning.",
    "reason": "While the precise annotation 'regulation of locomotion' as the primary BP derives from genetic studies, the four answer choices are sufficiently heterogeneous that general protein-architecture reasoning (no toxin fold, no ribosomal features, no NRPS adenylation domain) eliminates A, C, and D, leaving B as the only viable option. This constitutes a concrete biological argument from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are categorically incompatible with the protein's domain architecture and organismal context (C. elegans intracellular scaffolding protein). No other option among the four is defensible for this sequence."
  },
  "important_caveats": [
    "The protein also carries IEA:InterPro annotations for 'cell adhesion' (GO:0007155) and 'Rho protein signal transduction' (GO:0007266), which were not offered as options. If these had been included as distractors, the question would be much harder to resolve by reasoning alone.",
    "The IMP evidence for locomotion regulation is specific to C. elegans genetic studies; the protein's molecular function is scaffolding/localization, and 'regulation of locomotion' is a downstream phenotypic annotation rather than a direct molecular-process description.",
    "The accession G8JYB2 was first publicly released 2025-04-09; the benchmark's author snapshot is unknown but the historical entry (version 84) matches the sequence."
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

**Accession:** `G8JYB2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
"G8JYB2"
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20700105","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20865173","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"22577143","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31308408","source":"PubMed"}],"value":"Required for slo-1 potassium ion channel clustering at presynaptic terminals and in egg-laying muscles; clustering of slo-1 mediates the intoxicating and sedatory effects of ethanol on worms (PubMed:31308408). Required for slo-1 localization to dense bodies in body wall muscle cells (PubMed:20700105). Maintains the localization of the dystrophin complex near muscle cell dense bodies via its interaction with complex member dyb-1 which is required for slo-1 localization in muscle while slo-1 localization in neurons is independent of the dystrophin complex (PubMed:20865173, PubMed:22577143)"}]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000315","id":"22577143","source":"PubMed"}],"id":"GO:0040012","properties":[{"key":"GoTerm","value":"P:regulation of locomotion"},{"key":"GoEvidenceType","value":"IMP:WormBase"}]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Chen B.","Liu P.","Wang S.J.","Ge Q.","Zhan H.","Mohler W.A.","Wang Z.W."],"citationCrossReferences":[{"database":"PubMed","id":"20700105"},{"database":"DOI","id":"10.1038/emboj.2010.194"}],"citationType":"journal article","firstPage":"3184","id":"20700105","journal":"EMBO J.","lastPage":"3195","publicationDate":"2010","title":"alpha-Catulin CTN-1 is required for BK channel subcellular localization in C. elegans body-wall muscle cells.","volume":"29"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","INTERACTION WITH SLO-1","TISSUE SPECIFICITY","MUTAGENESIS OF 358-ARG--ILE-784"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Abraham L.S.","Oh H.J.","Sancar F.","Richmond J.E.","Kim H."],"citationCrossReferences":[{"database":"PubMed","id":"20865173"},{"database":"DOI","id":"10.1371/journal.pgen.1001077"}],"citationType":"journal article","firstPage":"0","id":"20865173","journal":"PLoS Genet.","lastPage":"0","publicationDate":"2010","title":"An alpha-catulin homologue controls neuromuscular function through localization of the dystrophin complex and BK channels in Caenorhabditis elegans.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","INTERACTION WITH SLO-1","TISSUE SPECIFICITY","MUTAGENESIS OF 144-ARG--ILE-784 AND 521-GLN--ILE-784"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Oh H.J.","Abraham L.S.","van Hengel J.","Stove C.","Proszynski T.J.","Gevaert K.","DiMario J.X.","Sanes J.R.","van Roy F.","Kim H."],"citationCrossReferences":[{"database":"PubMed","id":"22577143"},{"database":"DOI","id":"10.1074/jbc.m112.369496"}],"citationType":"journal article","firstPage":"21717","id":"22577143","journal":"J. Biol. Chem.","lastPage":"21728","publicationDate":"2012","title":"Interaction of alpha-catulin with dystrobrevin contributes to integrity of dystrophin complex in muscle.","volume":"287"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","INTERACTION WITH DYB-1","TISSUE SPECIFICITY","DOMAIN","MUTAGENESIS OF 382-ASN--ILE-416"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Oh K.H.","Kim H."],"citationCrossReferences":[{"database":"PubMed","id":"31308408"},{"database":"DOI","id":"10.1038/s41598-019-46615-9"}],"citationType":"journal article","firstPage":"10224","id":"31308408","journal":"Sci. Rep.","lastPage":"10224","publicationDate":"2019","title":"BK channel clustering is required for normal behavioral alcohol sensitivity in C. elegans.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","MUTAGENESIS OF 144-ARG--ILE-784"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)  
**Locator:** `lines 55-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:28:52.763286+00:00.  

```text
CC   -!- FUNCTION: Required for slo-1 potassium ion channel clustering at
CC       presynaptic terminals and in egg-laying muscles; clustering of slo-1
CC       mediates the intoxicating and sedatory effects of ethanol on worms
CC       (PubMed:31308408). Required for slo-1 localization to dense bodies in
CC       body wall muscle cells (PubMed:20700105). Maintains the localization of
CC       the dystrophin complex near muscle cell dense bodies via its
CC       interaction with complex member dyb-1 which is required for slo-1
CC       localization in muscle while slo-1 localization in neurons is
CC       independent of the dystrophin complex (PubMed:20865173,
CC       PubMed:22577143). {ECO:0000269|PubMed:20700105,
CC       ECO:0000269|PubMed:20865173, ECO:0000269|PubMed:22577143,
CC       ECO:0000269|PubMed:31308408}.
```

Source SHA-256: `bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)  
**Locator:** `lines 118-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:28:52.763286+00:00.  

```text
DR   GO; GO:0040012; P:regulation of locomotion; IMP:WormBase.
```

Source SHA-256: `bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
