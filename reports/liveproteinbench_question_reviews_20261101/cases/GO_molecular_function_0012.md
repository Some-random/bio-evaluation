# GO_molecular_function_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — ADP-ribosylarginine hydrolase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSFLYMLSQRPKLACLCGKSIIIWPGKRTNLPENAFTQRMLQECGQMAKPDASVDLDNFKAISEQSPAEFGIDSCRVKAQPEDRSDRIREQIASAYPVIHERTLLLFISFLEHKLTFGSEQEKAIYKDMTVVDLVQRLLAKRCVWFFGANDYYRTMQGNIGNEGFEAVGTPAEKEPLTLTSVLSYDEIKLSALLYVSCHSEFINNGSRVNGGEVLQNKDTIEREGVVIGLIGARFERPDVMEYQDIMITKTQNTEANGYGFDLEQISSETVTPASDLRRIWREFYEEPRDFIYADTPYDTTRFEEVSQGIFDHQVMRKRYAISFDTLLLEAQDRAFKAGKPAYIHVVGIGLGVWKAARQQERTFLESFEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV

[Multiple Choices]
A. RNA polymerase II core promoter sequence-specific DNA binding
B. ADP-ribosylarginine hydrolase activity
C. peptidase inhibitor activity
D. zinc ion binding
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

> The supplied sequence exactly matches the 508-aa Drosophila melanogaster protein annotated as an ADP-ribosylarginine hydrolase. Its catalytic activity and corresponding GO molecular-function term are supported by experimental evidence cited in the record, including an IDA annotation. The matching historical record also supports the key, although the author's exact source snapshot is unknown.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a folded soluble enzyme, and the choices make DNA binding and peptidase inhibition less immediately plausible. But those broad features do not identify this enzyme's specific ADP-ribosylarginine-hydrolysis activity or reliably distinguish it from the remaining molecular-function options.


**Missing item-specific fact**

> The protein-specific identification as Drosophila CG3568/ADP-ribosylarginine hydrolase, or equivalent family/domain evidence connecting this sequence to that precise catalytic activity.


**Reason**

> The input supplies only an amino-acid sequence and choices. Selecting B requires recognizing or retrieving a protein-specific functional assignment; generic sequence reasoning alone does not establish the precise substrate and reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports B for the sequence-matched protein, and no other listed choice is comparably supported.


### Important caveats

- Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.
- The current and retrieved historical UniProt records match the supplied sequence; the author's exact source snapshot remains unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a folded soluble enzyme, and the choices make DNA binding and peptidase inhibition less immediately plausible. But those broad features do not identify this enzyme's specific ADP-ribosylarginine-hydrolysis activity or reliably distinguish it from the remaining molecular-function options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Drosophila CG3568/ADP-ribosylarginine hydrolase, or equivalent family/domain evidence connecting this sequence to that precise catalytic activity.",
    "reason": "The input supplies only an amino-acid sequence and choices. Selecting B requires recognizing or retrieving a protein-specific functional assignment; generic sequence reasoning alone does not establish the precise substrate and reaction."
  },
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 508-aa Drosophila melanogaster protein annotated as an ADP-ribosylarginine hydrolase. Its catalytic activity and corresponding GO molecular-function term are supported by experimental evidence cited in the record, including an IDA annotation. The matching historical record also supports the key, although the author's exact source snapshot is unknown."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.",
    "The current and retrieved historical UniProt records match the supplied sequence; the author's exact source snapshot remains unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B for the sequence-matched protein, and no other listed choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 508-aa Drosophila melanogaster protein annotated as an ADP-ribosylarginine hydrolase. Its catalytic activity and corresponding GO molecular-function term are supported by experimental evidence cited in the record, including an IDA annotation. The matching historical record also supports the key, although the author's exact source snapshot is unknown.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a folded soluble enzyme, and the choices make DNA binding and peptidase inhibition less immediately plausible. But those broad features do not identify this enzyme's specific ADP-ribosylarginine-hydrolysis activity or reliably distinguish it from the remaining molecular-function options.",
    "missing_item_specific_fact": "The protein-specific identification as Drosophila CG3568/ADP-ribosylarginine hydrolase, or equivalent family/domain evidence connecting this sequence to that precise catalytic activity.",
    "reason": "The input supplies only an amino-acid sequence and choices. Selecting B requires recognizing or retrieving a protein-specific functional assignment; generic sequence reasoning alone does not establish the precise substrate and reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B for the sequence-matched protein, and no other listed choice is comparably supported."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.",
    "The current and retrieved historical UniProt records match the supplied sequence; the author's exact source snapshot remains unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA, sequence version 2). The UniProt entry is named 'ADP-ribosylarginine hydrolase CG3568' with EC 3.2.2.19, annotated with experimental evidence (ECO:0000269, PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). GO:0003875 'ADP-ribosylarginine-&#91;protein&#93; hydrolase activity' is annotated with IDA:FlyBase. The option text 'ADP-ribosylarginine hydrolase activity' is an EXACT synonym of GO:0003875. The function comment explicitly states the protein removes mono-ADP-ribosyl modifications from protein arginine residues.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal motif 'CGKSIIIWPG' and the overall fold architecture (β-sheet-rich macrodomain with conserved 'WFFG', 'GIG', and 'DTPYD' regions) are hallmark signatures of the macrodomain superfamily, which is well-established in biochemistry as the structural module responsible for ADP-ribosylation metabolism (reading or hydrolyzing ADP-ribosyl modifications). Among the four options, only B (ADP-ribosylarginine hydrolase activity) pertains to ADP-ribosylation chemistry. Option A (RNA pol II core promoter DNA binding) requires recognizable DNA-binding domains (zinc fingers, homeodomains, TBP-like motifs) absent here. Option C (peptidase inhibitor activity) requires protease-inhibitor motifs (Kunitz, Bowman-Birk, serpin RCL) absent here. Option D (zinc ion binding) requires canonical Zn-coordinating motifs (Cys2His2, Cys4, Cys6) which are not present in a defined geometry; scattered cysteines alone do not constitute a zinc-binding site. Thus, recognizing the macrodomain fold and its established link to ADP-ribosyl metabolism provides a concrete pathway to select B and eliminate A, C, and D.


**Missing item-specific fact**

> The precise 'arginine' specificity (vs. serine or glutamate ADP-ribosyl targets) was experimentally confirmed only in 2024 (PubMed:38503748, PDB 8DMU). However, this fine distinction is not needed to answer the question because B is the sole ADP-ribosyl-related option; the macrodomain-to-ADP-ribosylation connection suffices to eliminate the other three choices.


**Reason**

> The macrodomain fold recognition (CGKS...WPG signature, catalytic GIG region) is within the scope of structural biology and ADP-ribosylation biochemistry knowledge. This fold is specifically associated with ADP-ribosyl metabolism, which uniquely maps to option B among the four choices. The other options are structurally incompatible with the sequence features present.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly incompatible with the macrodomain architecture. Option D (zinc ion binding) lacks a defined Zn-coordinating motif in the sequence and is not the primary molecular function of a macrodomain enzyme. Only B aligns with the structural and functional characteristics of the protein.


### Important caveats

- The specific arginine-targeting specificity of this Drosophila protein was experimentally established only in 2024 (PubMed:38503748); prior to that, it may have been annotated more broadly as a macrodomain protein. However, the question's answer choices make the ADP-ribosyl connection sufficient without requiring arginine-specific knowledge.
- The macrodomain fold recognition (CGKS...WPG motif) is specialized structural biology knowledge; a model without familiarity with macrodomain signatures may struggle, though this is within the expected knowledge domain for a protein-function prediction task.
- The GO annotation evidence code is IDA (Inferred from Direct Assay, FlyBase), indicating experimental rather than purely computational assignment.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9W4J9 sequence version 2.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal motif 'CGKSIIIWPG' and the overall fold architecture (β-sheet-rich macrodomain with conserved 'WFFG', 'GIG', and 'DTPYD' regions) are hallmark signatures of the macrodomain superfamily, which is well-established in biochemistry as the structural module responsible for ADP-ribosylation metabolism (reading or hydrolyzing ADP-ribosyl modifications). Among the four options, only B (ADP-ribosylarginine hydrolase activity) pertains to ADP-ribosylation chemistry. Option A (RNA pol II core promoter DNA binding) requires recognizable DNA-binding domains (zinc fingers, homeodomains, TBP-like motifs) absent here. Option C (peptidase inhibitor activity) requires protease-inhibitor motifs (Kunitz, Bowman-Birk, serpin RCL) absent here. Option D (zinc ion binding) requires canonical Zn-coordinating motifs (Cys2His2, Cys4, Cys6) which are not present in a defined geometry; scattered cysteines alone do not constitute a zinc-binding site. Thus, recognizing the macrodomain fold and its established link to ADP-ribosyl metabolism provides a concrete pathway to select B and eliminate A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise 'arginine' specificity (vs. serine or glutamate ADP-ribosyl targets) was experimentally confirmed only in 2024 (PubMed:38503748, PDB 8DMU). However, this fine distinction is not needed to answer the question because B is the sole ADP-ribosyl-related option; the macrodomain-to-ADP-ribosylation connection suffices to eliminate the other three choices.",
    "reason": "The macrodomain fold recognition (CGKS...WPG signature, catalytic GIG region) is within the scope of structural biology and ADP-ribosylation biochemistry knowledge. This fold is specifically associated with ADP-ribosyl metabolism, which uniquely maps to option B among the four choices. The other options are structurally incompatible with the sequence features present."
  },
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA, sequence version 2). The UniProt entry is named 'ADP-ribosylarginine hydrolase CG3568' with EC 3.2.2.19, annotated with experimental evidence (ECO:0000269, PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). GO:0003875 'ADP-ribosylarginine-[protein] hydrolase activity' is annotated with IDA:FlyBase. The option text 'ADP-ribosylarginine hydrolase activity' is an EXACT synonym of GO:0003875. The function comment explicitly states the protein removes mono-ADP-ribosyl modifications from protein arginine residues."
  },
  "important_caveats": [
    "The specific arginine-targeting specificity of this Drosophila protein was experimentally established only in 2024 (PubMed:38503748); prior to that, it may have been annotated more broadly as a macrodomain protein. However, the question's answer choices make the ADP-ribosyl connection sufficient without requiring arginine-specific knowledge.",
    "The macrodomain fold recognition (CGKS...WPG motif) is specialized structural biology knowledge; a model without familiarity with macrodomain signatures may struggle, though this is within the expected knowledge domain for a protein-function prediction task.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay, FlyBase), indicating experimental rather than purely computational assignment.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9W4J9 sequence version 2."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with the macrodomain architecture. Option D (zinc ion binding) lacks a defined Zn-coordinating motif in the sequence and is not the primary molecular function of a macrodomain enzyme. Only B aligns with the structural and functional characteristics of the protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA, sequence version 2). The UniProt entry is named 'ADP-ribosylarginine hydrolase CG3568' with EC 3.2.2.19, annotated with experimental evidence (ECO:0000269, PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). GO:0003875 'ADP-ribosylarginine-[protein] hydrolase activity' is annotated with IDA:FlyBase. The option text 'ADP-ribosylarginine hydrolase activity' is an EXACT synonym of GO:0003875. The function comment explicitly states the protein removes mono-ADP-ribosyl modifications from protein arginine residues.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "C9", "H1", "H3", "H4", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal motif 'CGKSIIIWPG' and the overall fold architecture (β-sheet-rich macrodomain with conserved 'WFFG', 'GIG', and 'DTPYD' regions) are hallmark signatures of the macrodomain superfamily, which is well-established in biochemistry as the structural module responsible for ADP-ribosylation metabolism (reading or hydrolyzing ADP-ribosyl modifications). Among the four options, only B (ADP-ribosylarginine hydrolase activity) pertains to ADP-ribosylation chemistry. Option A (RNA pol II core promoter DNA binding) requires recognizable DNA-binding domains (zinc fingers, homeodomains, TBP-like motifs) absent here. Option C (peptidase inhibitor activity) requires protease-inhibitor motifs (Kunitz, Bowman-Birk, serpin RCL) absent here. Option D (zinc ion binding) requires canonical Zn-coordinating motifs (Cys2His2, Cys4, Cys6) which are not present in a defined geometry; scattered cysteines alone do not constitute a zinc-binding site. Thus, recognizing the macrodomain fold and its established link to ADP-ribosyl metabolism provides a concrete pathway to select B and eliminate A, C, and D.",
    "missing_item_specific_fact": "The precise 'arginine' specificity (vs. serine or glutamate ADP-ribosyl targets) was experimentally confirmed only in 2024 (PubMed:38503748, PDB 8DMU). However, this fine distinction is not needed to answer the question because B is the sole ADP-ribosyl-related option; the macrodomain-to-ADP-ribosylation connection suffices to eliminate the other three choices.",
    "reason": "The macrodomain fold recognition (CGKS...WPG signature, catalytic GIG region) is within the scope of structural biology and ADP-ribosylation biochemistry knowledge. This fold is specifically associated with ADP-ribosyl metabolism, which uniquely maps to option B among the four choices. The other options are structurally incompatible with the sequence features present."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with the macrodomain architecture. Option D (zinc ion binding) lacks a defined Zn-coordinating motif in the sequence and is not the primary molecular function of a macrodomain enzyme. Only B aligns with the structural and functional characteristics of the protein."
  },
  "important_caveats": [
    "The specific arginine-targeting specificity of this Drosophila protein was experimentally established only in 2024 (PubMed:38503748); prior to that, it may have been annotated more broadly as a macrodomain protein. However, the question's answer choices make the ADP-ribosyl connection sufficient without requiring arginine-specific knowledge.",
    "The macrodomain fold recognition (CGKS...WPG motif) is specialized structural biology knowledge; a model without familiarity with macrodomain signatures may struggle, though this is within the expected knowledge domain for a protein-function prediction task.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay, FlyBase), indicating experimental rather than purely computational assignment.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9W4J9 sequence version 2."
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

**Accession:** `Q9W4J9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 153. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
"Q9W4J9"
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG3568"}}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"Protein ADP-ribosyl hydrolase that specifically removes mono-ADP-ribosyl modifications from protein arginine residues"}]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20784"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:32682"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:60267"}]}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38503748","source":"PubMed"}],"id":"GO:0003875","properties":[{"key":"GoTerm","value":"F:ADP-ribosylarginine-[protein] hydrolase activity"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Fu J.","Rack J.G.M.","Li C.","Voorneveld J.","Filippov D.V.","Ahel I.","Luo Z.Q.","Das C."],"citationCrossReferences":[{"database":"PubMed","id":"38503748"},{"database":"DOI","id":"10.1038/s41467-024-46649-2"}],"citationType":"journal article","firstPage":"2452","id":"38503748","journal":"Nat. Commun.","lastPage":"2452","publicationDate":"2024","title":"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DMU","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 25-508","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
ID   ADPR2_DROME             Reviewed;         508 AA.
AC   Q9W4J9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 2.
DT   28-JAN-2026, entry version 153.
DE   RecName: Full=ADP-ribosylarginine hydrolase CG3568 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
GN   ORFNames=CG3568 {ECO:0000312|FlyBase:FBgn0029710};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- FUNCTION: Protein ADP-ribosyl hydrolase that specifically removes mono-
CC       ADP-ribosyl modifications from protein arginine residues.
CC       {ECO:0000269|PubMed:38503748}.
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 95-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-
CC         arginine; Xref=Rhea:RHEA:20784, ChEBI:CHEBI:15377, ChEBI:CHEBI:32682,
CC         ChEBI:CHEBI:57967, ChEBI:CHEBI:60267; EC=3.2.2.19;
CC         Evidence={ECO:0000269|PubMed:38503748};
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
DR   GO; GO:0003875; F:ADP-ribosylarginine hydrolase activity; IDA:FlyBase.
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 30576-30606`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003875
name: ADP-ribosylarginine-[protein] hydrolase activity
namespace: molecular_function
def: "Catalysis of the reactions: H2O + N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] = ADP-D-ribose + L-arginyl-[protein], and H2O + N(omega)-(ADP-D-ribosyl)-L-arginine = ADP-D-ribose + L-arginine." [EC:3.2.2.19]
synonym: "ADP-ribose-L-arginine cleavage enzyme activity" RELATED [EC:3.2.2.19]
synonym: "ADP-ribose-L-arginine cleaving enzyme activity" RELATED [EC:3.2.2.19]
synonym: "ADP-ribosylarginine hydrolase activity" EXACT []
synonym: "ADPribosylarginine hydrolase activity" EXACT []
synonym: "N(omega)-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity" RELATED [EC:3.2.2.19]
synonym: "nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity" RELATED [EC:3.2.2.19]
synonym: "omega-protein-N-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity" RELATED [EC:3.2.2.19]
synonym: "protein ADP-ribosylarginine hydrolase activity" RELATED [EC:3.2.2.19]
synonym: "protein-nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity" RELATED [EC:3.2.2.19]
xref: EC:3.2.2.19
xref: MetaCyc:3.2.2.24-RXN
xref: MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN
xref: MetaCyc:RXN-8732
xref: RHEA:14493
xref: RHEA:14885
xref: RHEA:20784
is_a: GO:0016799 ! hydrolase activity, hydrolyzing N-glycosyl compounds
is_a: GO:0140096 ! catalytic activity, acting on a protein
property_value: skos:exactMatch EC:3.2.2.19
property_value: skos:narrowMatch MetaCyc:3.2.2.24-RXN
property_value: skos:narrowMatch MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN
property_value: skos:narrowMatch MetaCyc:RXN-8732
property_value: skos:narrowMatch RHEA:14493
property_value: skos:narrowMatch RHEA:14885
property_value: skos:narrowMatch RHEA:20784

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
