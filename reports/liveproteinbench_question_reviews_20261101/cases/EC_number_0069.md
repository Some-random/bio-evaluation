# EC_number_0069

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.7.8.43

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. 2.7.8.41
B. 2.7.8.43
C. 2.5.1.15
D. 4.1.1.129
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt record for Mcr-2, which assigns EC 2.7.8.43 and annotates the corresponding lipid A phosphoethanolamine-transfer reaction. The annotation cites a paper on Mcr-2 structure and function; the excerpts support the key, though they do not independently establish the details of the underlying experimental assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The hydrophobic N-terminal region and larger catalytic portion are compatible with a membrane-associated lipid-modifying enzyme, but those broad features do not distinguish the exact EC number, especially between the closely related phosphoethanolamine-transferase choices.


**Missing item-specific fact**

> The protein-specific functional assignment identifying this sequence as Mcr-2 and its precise EC 2.7.8.43 reaction, rather than a related transferase with a different EC number.


**Reason**

> The sequence is supplied, but inferring the precise catalytic classification requires protein-specific functional knowledge or external annotation; general sequence-level reasoning does not establish the exact reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC classifications, and the sequence-matched annotation supports B. The need for an external protein-specific fact does not itself make multiple choices correct.


### Important caveats

- The UniProt EC assignment is a curated annotation citing a functional study, not a primary experimental record independently reviewed here.
- The reviewer-only accession and annotation were not available in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The hydrophobic N-terminal region and larger catalytic portion are compatible with a membrane-associated lipid-modifying enzyme, but those broad features do not distinguish the exact EC number, especially between the closely related phosphoethanolamine-transferase choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying this sequence as Mcr-2 and its precise EC 2.7.8.43 reaction, rather than a related transferase with a different EC number.",
    "reason": "The sequence is supplied, but inferring the precise catalytic classification requires protein-specific functional knowledge or external annotation; general sequence-level reasoning does not establish the exact reaction."
  },
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record for Mcr-2, which assigns EC 2.7.8.43 and annotates the corresponding lipid A phosphoethanolamine-transfer reaction. The annotation cites a paper on Mcr-2 structure and function; the excerpts support the key, though they do not independently establish the details of the underlying experimental assay."
  },
  "important_caveats": [
    "The UniProt EC assignment is a curated annotation citing a functional study, not a primary experimental record independently reviewed here.",
    "The reviewer-only accession and annotation were not available in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the sequence-matched annotation supports B. The need for an external protein-specific fact does not itself make multiple choices correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record for Mcr-2, which assigns EC 2.7.8.43 and annotates the corresponding lipid A phosphoethanolamine-transfer reaction. The annotation cites a paper on Mcr-2 structure and function; the excerpts support the key, though they do not independently establish the details of the underlying experimental assay.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The hydrophobic N-terminal region and larger catalytic portion are compatible with a membrane-associated lipid-modifying enzyme, but those broad features do not distinguish the exact EC number, especially between the closely related phosphoethanolamine-transferase choices.",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying this sequence as Mcr-2 and its precise EC 2.7.8.43 reaction, rather than a related transferase with a different EC number.",
    "reason": "The sequence is supplied, but inferring the precise catalytic classification requires protein-specific functional knowledge or external annotation; general sequence-level reasoning does not establish the exact reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC classifications, and the sequence-matched annotation supports B. The need for an external protein-specific fact does not itself make multiple choices correct."
  },
  "important_caveats": [
    "The UniProt EC assignment is a curated annotation citing a functional study, not a primary experimental record independently reviewed here.",
    "The reviewer-only accession and annotation were not available in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The 538-aa sequence matches UniProt A0A1C3NEV1 (MCR2_ECOLX) exactly. The entry is annotated as 'Phosphatidylethanolamine transferase Mcr-2' with EC 2.7.8.43, supported by evidence code ECO:0000305 linked to PubMed 30194678 (Wang et al. 2018, Sci China Life Sci) and PDB 6A7W crystallographic data with mutagenesis studies. The catalytic reaction (lipid A + phosphoethanolamine → lipid A 4'-phosphoethanolamine + diacylglycerol) is consistent with EC 2.7.8.43.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could potentially reason from the hydrophobic N-terminal transmembrane region and the alkaline-phosphatase-like catalytic fold (Zn-binding residues, HxKxNxD motif) that this is a membrane-bound phosphatidylethanolamine transferase (EC 2.7.8.x), thereby eliminating D (4.1.1.129, a decarboxylase) and C (2.5.1.15, a prenyltransferase). However, the critical distinction between A (2.7.8.41, MCR-1) and B (2.7.8.43, MCR-2) requires knowing which specific MCR variant this sequence encodes. These are closely related orthologs with nearly identical catalytic mechanisms; the separate EC numbers were assigned based on specific structural/functional characterization (PDB 6A7W, site-directed mutagenesis of 11 residues) in the 2018 Wang et al. paper. No general sequence heuristic distinguishes the 4th EC digit between these two entries.


**Missing item-specific fact**

> The specific identity of this protein as MCR-2 (rather than MCR-1 or another MCR variant), and the structural/functional rationale (specific residue differences, substrate preference details) that justifies a distinct EC 4th-digit assignment from MCR-1 (2.7.8.41).


**Reason**

> While the broad transferase class (EC 2.7.8.x) might be inferable from domain architecture, selecting 2.7.8.43 over 2.7.8.41 depends entirely on recognizing this exact sequence as MCR-2 and recalling its database-assigned EC number. The 4th-digit distinction between MCR-1 and MCR-2 is an item-specific annotation derived from a single 2018 structural paper, not from generalizable sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> EC 2.7.8.41 (MCR-1) and EC 2.7.8.43 (MCR-2) are both phosphatidylethanolamine transferases that modify lipid A with nearly identical catalytic chemistry. Without prior knowledge of which MCR variant this sequence represents, a knowledgeable model could reasonably select either A or B based on the general MCR-family fold. The distinction rests on variant-specific characterization not derivable from sequence alone.


### Important caveats

- The UniProt annotation uses ECO:0000305 (curator inference from literature), meaning the EC assignment is based on published experimental work (crystallography, mutagenesis) rather than direct assay of this specific sequence variant in isolation.
- The sequence was first integrated into Swiss-Prot in June 2025 (entry version 40); the historical version 38 was released January 2026. The benchmark construction date relative to these releases is unknown.
- Distractors C (2.5.1.15) and D (4.1.1.129) are in entirely different EC classes and are relatively easy to eliminate for a model with general enzymology knowledge, but this does not resolve the A-vs-B distinction.
- The identity origin note states the UniProt accession was inferred mechanically from dataset image-path metadata, not from the evaluated model's input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could potentially reason from the hydrophobic N-terminal transmembrane region and the alkaline-phosphatase-like catalytic fold (Zn-binding residues, HxKxNxD motif) that this is a membrane-bound phosphatidylethanolamine transferase (EC 2.7.8.x), thereby eliminating D (4.1.1.129, a decarboxylase) and C (2.5.1.15, a prenyltransferase). However, the critical distinction between A (2.7.8.41, MCR-1) and B (2.7.8.43, MCR-2) requires knowing which specific MCR variant this sequence encodes. These are closely related orthologs with nearly identical catalytic mechanisms; the separate EC numbers were assigned based on specific structural/functional characterization (PDB 6A7W, site-directed mutagenesis of 11 residues) in the 2018 Wang et al. paper. No general sequence heuristic distinguishes the 4th EC digit between these two entries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as MCR-2 (rather than MCR-1 or another MCR variant), and the structural/functional rationale (specific residue differences, substrate preference details) that justifies a distinct EC 4th-digit assignment from MCR-1 (2.7.8.41).",
    "reason": "While the broad transferase class (EC 2.7.8.x) might be inferable from domain architecture, selecting 2.7.8.43 over 2.7.8.41 depends entirely on recognizing this exact sequence as MCR-2 and recalling its database-assigned EC number. The 4th-digit distinction between MCR-1 and MCR-2 is an item-specific annotation derived from a single 2018 structural paper, not from generalizable sequence features."
  },
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The 538-aa sequence matches UniProt A0A1C3NEV1 (MCR2_ECOLX) exactly. The entry is annotated as 'Phosphatidylethanolamine transferase Mcr-2' with EC 2.7.8.43, supported by evidence code ECO:0000305 linked to PubMed 30194678 (Wang et al. 2018, Sci China Life Sci) and PDB 6A7W crystallographic data with mutagenesis studies. The catalytic reaction (lipid A + phosphoethanolamine → lipid A 4'-phosphoethanolamine + diacylglycerol) is consistent with EC 2.7.8.43."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (curator inference from literature), meaning the EC assignment is based on published experimental work (crystallography, mutagenesis) rather than direct assay of this specific sequence variant in isolation.",
    "The sequence was first integrated into Swiss-Prot in June 2025 (entry version 40); the historical version 38 was released January 2026. The benchmark construction date relative to these releases is unknown.",
    "Distractors C (2.5.1.15) and D (4.1.1.129) are in entirely different EC classes and are relatively easy to eliminate for a model with general enzymology knowledge, but this does not resolve the A-vs-B distinction.",
    "The identity origin note states the UniProt accession was inferred mechanically from dataset image-path metadata, not from the evaluated model's input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "EC 2.7.8.41 (MCR-1) and EC 2.7.8.43 (MCR-2) are both phosphatidylethanolamine transferases that modify lipid A with nearly identical catalytic chemistry. Without prior knowledge of which MCR variant this sequence represents, a knowledgeable model could reasonably select either A or B based on the general MCR-family fold. The distinction rests on variant-specific characterization not derivable from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The 538-aa sequence matches UniProt A0A1C3NEV1 (MCR2_ECOLX) exactly. The entry is annotated as 'Phosphatidylethanolamine transferase Mcr-2' with EC 2.7.8.43, supported by evidence code ECO:0000305 linked to PubMed 30194678 (Wang et al. 2018, Sci China Life Sci) and PDB 6A7W crystallographic data with mutagenesis studies. The catalytic reaction (lipid A + phosphoethanolamine → lipid A 4'-phosphoethanolamine + diacylglycerol) is consistent with EC 2.7.8.43.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could potentially reason from the hydrophobic N-terminal transmembrane region and the alkaline-phosphatase-like catalytic fold (Zn-binding residues, HxKxNxD motif) that this is a membrane-bound phosphatidylethanolamine transferase (EC 2.7.8.x), thereby eliminating D (4.1.1.129, a decarboxylase) and C (2.5.1.15, a prenyltransferase). However, the critical distinction between A (2.7.8.41, MCR-1) and B (2.7.8.43, MCR-2) requires knowing which specific MCR variant this sequence encodes. These are closely related orthologs with nearly identical catalytic mechanisms; the separate EC numbers were assigned based on specific structural/functional characterization (PDB 6A7W, site-directed mutagenesis of 11 residues) in the 2018 Wang et al. paper. No general sequence heuristic distinguishes the 4th EC digit between these two entries.",
    "missing_item_specific_fact": "The specific identity of this protein as MCR-2 (rather than MCR-1 or another MCR variant), and the structural/functional rationale (specific residue differences, substrate preference details) that justifies a distinct EC 4th-digit assignment from MCR-1 (2.7.8.41).",
    "reason": "While the broad transferase class (EC 2.7.8.x) might be inferable from domain architecture, selecting 2.7.8.43 over 2.7.8.41 depends entirely on recognizing this exact sequence as MCR-2 and recalling its database-assigned EC number. The 4th-digit distinction between MCR-1 and MCR-2 is an item-specific annotation derived from a single 2018 structural paper, not from generalizable sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "EC 2.7.8.41 (MCR-1) and EC 2.7.8.43 (MCR-2) are both phosphatidylethanolamine transferases that modify lipid A with nearly identical catalytic chemistry. Without prior knowledge of which MCR variant this sequence represents, a knowledgeable model could reasonably select either A or B based on the general MCR-family fold. The distinction rests on variant-specific characterization not derivable from sequence alone."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (curator inference from literature), meaning the EC assignment is based on published experimental work (crystallography, mutagenesis) rather than direct assay of this specific sequence variant in isolation.",
    "The sequence was first integrated into Swiss-Prot in June 2025 (entry version 40); the historical version 38 was released January 2026. The benchmark construction date relative to these releases is unknown.",
    "Distractors C (2.5.1.15) and D (4.1.1.129) are in entirely different EC classes and are relatively easy to eliminate for a model with general enzymology knowledge, but this does not resolve the A-vs-B distinction.",
    "The identity origin note states the UniProt accession was inferred mechanically from dataset image-path metadata, not from the evaluated model's input."
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

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
"A0A1C3NEV1"
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"}],"value":"Polymyxin resistance protein MCR-2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"value":"2.7.8.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30194678","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"Ref.1","source":"Reference"}],"value":"Phosphatidylethanolamine transferase Mcr-2"}}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.43","evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"name":"lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46900"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17815"},{"database":"ChEBI","id":"CHEBI:64612"},{"database":"ChEBI","id":"CHEBI:87097"},{"database":"ChEBI","id":"CHEBI:134257"}]}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"citation":{"authors":["Wang X.","Lu Q.","Qi J.","Chai Y.","Wang Y.","Gao G.F."],"citationCrossReferences":[{"database":"PubMed","id":"30194678"},{"database":"DOI","id":"10.1007/s11427-018-9363-4"}],"citationType":"journal article","firstPage":"1432","id":"30194678","journal":"Sci. China Life Sci.","lastPage":"1436","publicationDate":"2018","title":"Structural and functional insights into MCR-2 mediated colistin resistance.","volume":"61"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6A7W","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"WHI04997.1","source":"EMBL"}],"type":"PLASMID","value":"unnamed5"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)","DISULFIDE BONDS","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476"]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
DE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};
DE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};
DE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6A7W}
RP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),
RP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;
RP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;
RP   LYS-331 AND HIS-476.
RC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};
RX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;
RA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;
RT   "Structural and functional insights into MCR-2 mediated colistin
RT   resistance.";
RL   Sci. China Life Sci. 61:1432-1436(2018).
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 72-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-
CC         phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate)
CC         (E. coli) + a 1,2-diacyl-sn-glycerol; Xref=Rhea:RHEA:46900,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17815, ChEBI:CHEBI:64612,
CC         ChEBI:CHEBI:87097, ChEBI:CHEBI:134257; EC=2.7.8.43;
CC         Evidence={ECO:0000305|PubMed:30194678};
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
