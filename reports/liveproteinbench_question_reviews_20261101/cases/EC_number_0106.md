# EC_number_0106

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVNKEQFYDQIRKALEDGNTRYYRNLIYIERDDYFDHVKEIISLFLNFKSNPSVAYGFVPWASGSKERMRTIKEYFSKFDDIDYANAEYYLGNTYDLVILDTVDNFQPINIGRLVDLARGGGLIIIYTNNLIKDKTFRTSIMRNGLILDEYEKRFKRKLYEHEGIFIIDVNEYIPKPFSGNTMPKAEKKVPRNPLMPKEIHELSLSEDQNRVIESFTYLLSGGQRALVLTAARGRGKSAATGLSIAGLIEKLRERKEKSIRIIVTAPSIASASQVMSFAKLGLEALGEELSVKVSDTGHIKSLRGDYFKLEYVPPDAAIEDEGELLIIDEAAALGINYIDLALRAWKKVALVTTVHGYEGSNKAFLRYLRRLIESKRIRVKWVNMEQPLRYAKGDPIEKWLYDALLLDAEPSEPQYLNDTMIYEDVDKSELANDDNRLRAIYGIMVTAHYKNNPDDLMIMLDGIHHKIKAIRIGENSYIAACQIAEEGELSDNMVDIALKGGTFDGDLIPDRIIKHVRIKDFAKLRGWRIVRIAVAPELQDKGFGSELLKMIYEEARDKGVDWVGSSFMSDQKVLNFWIKNGFIPVHISPKKNEKLGDYPVVVIRPISDIATKIVKISAYMLKEKLLNTLHDVYFNMNPEVVRLMLTSTKIVSKTINVSPIILDKTISFLQGVSPYESSADGIHMLTLKYFWDGERDWSLTQDEELVLIAKVLQGKPWSYVSTVLSSNRTHIYELIYSAISKLMKKYYNLTADSKVGLTLKDVMNSQQYD

[Multiple Choices]
A. 2.3.1.319
B. 2.3.1.193
C. 4.3.1.24
D. 3.1.26.3
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

> The supplied sequence exactly matches the UniProt entry for Saccharolobus solfataricus TmcA2, annotated with EC 2.3.1.193. The entry specifies the corresponding tRNA cytidine acetylation reaction and cites both a HAMAP rule and a PubMed reference. The annotation was also present in the historical entry checked, although the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide an evident, general biological argument that distinguishes this particular EC number from the other specific enzyme classifications. Identifying a transferase-like protein would not establish the precise substrate and reaction.


**Missing item-specific fact**

> The protein's specific identity and catalytic activity as TmcA2, including its cytidine acetylation reaction, are not given in the question and are needed to assign EC 2.3.1.193.


**Reason**

> Distinguishing the choices requires protein-specific functional annotation or characterization absent from the input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports B; the evidence supplied for review does not support another listed choice.


### Important caveats

- The database annotation cites both a computational HAMAP rule and a PubMed source; the primary publication was not independently assessed.
- Reviewer-only accession and annotation evidence establish support for the key but were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide an evident, general biological argument that distinguishes this particular EC number from the other specific enzyme classifications. Identifying a transferase-like protein would not establish the precise substrate and reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific identity and catalytic activity as TmcA2, including its cytidine acetylation reaction, are not given in the question and are needed to assign EC 2.3.1.193.",
    "reason": "Distinguishing the choices requires protein-specific functional annotation or characterization absent from the input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided evidence."
  },
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for Saccharolobus solfataricus TmcA2, annotated with EC 2.3.1.193. The entry specifies the corresponding tRNA cytidine acetylation reaction and cites both a HAMAP rule and a PubMed reference. The annotation was also present in the historical entry checked, although the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites both a computational HAMAP rule and a PubMed source; the primary publication was not independently assessed.",
    "Reviewer-only accession and annotation evidence establish support for the key but were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the evidence supplied for review does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for Saccharolobus solfataricus TmcA2, annotated with EC 2.3.1.193. The entry specifies the corresponding tRNA cytidine acetylation reaction and cites both a HAMAP rule and a PubMed reference. The annotation was also present in the historical entry checked, although the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide an evident, general biological argument that distinguishes this particular EC number from the other specific enzyme classifications. Identifying a transferase-like protein would not establish the precise substrate and reaction.",
    "missing_item_specific_fact": "The protein's specific identity and catalytic activity as TmcA2, including its cytidine acetylation reaction, are not given in the question and are needed to assign EC 2.3.1.193.",
    "reason": "Distinguishing the choices requires protein-specific functional annotation or characterization absent from the input; recognizing the sequence from an external database would be lookup or memorization, not reasoning from the provided evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the evidence supplied for review does not support another listed choice."
  },
  "important_caveats": [
    "The database annotation cites both a computational HAMAP rule and a PubMed source; the primary publication was not independently assessed.",
    "Reviewer-only accession and annotation evidence establish support for the key but were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q97U12 (sequence exactly matched, 770 AA, SHA256 confirmed) assigns EC 2.3.1.193 to this protein, named 'tRNA(Met) cytidine acetyltransferase TmcA 2'. The EC annotation is supported by both computational evidence (HAMAP-Rule MF_01886, ECO:0000255) and literature-based curator inference (PubMed 32555463, Sas-Chen et al. Nature 2020, ECO:0000305). Multiple catalytic activity entries (C5–C8) describe acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP, consistent with EC 2.3.1.193. The historical archived entry (version 122) confirms the same annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options C (EC 4.3.1.24, a lyase) and D (EC 3.1.26.3, a ribonuclease/hydrolase) belong to entirely different EC top-level classes (4 = lyases, 3 = hydrolases) than the correct answer (2 = transferases). A knowledgeable model might attempt to rule these out by searching for transferase-like catalytic motifs (e.g., GNAT-fold or acetyl-CoA-binding signatures) and the absence of canonical lyase or RNase catalytic residues. However, options A (EC 2.3.1.319) and B (EC 2.3.1.193) are both acyltransferases within the same EC subclass 2.3.1. Distinguishing between these two requires knowing the exact substrate specificity and reaction mechanism of this particular protein — namely, that it acetylates cytidine(34) in elongator tRNA(Met) rather than whatever substrate EC 2.3.1.319 describes. No general sequence heuristic (motif scanning, length, composition) reliably separates two specific EC numbers in the same subclass.


**Missing item-specific fact**

> The specific substrate and reaction catalyzed by this 770-residue archaeal protein (tRNA(Met) cytidine acetyltransferase vs. the reaction assigned to EC 2.3.1.319). This is an item-specific annotation fact (HAMAP rule MF_01886 / PubMed 32555463) that cannot be derived from the raw sequence by general biological reasoning.


**Reason**

> While C and D can potentially be eliminated by recognizing that the sequence lacks canonical lyase or RNase catalytic motifs, the critical discrimination between A (2.3.1.319) and B (2.3.1.193) depends on knowing the exact enzymatic reaction this protein catalyzes. Both are EC 2.3.1.x acyltransferases. No generalizable sequence feature distinguishes them without memorizing the database entry or performing a BLAST/HAMAP lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> EC 2.3.1.319 and EC 2.3.1.193 are both acyltransferases in the same EC subclass. Without the specific annotation or a structural/functional assay, a model cannot reliably distinguish which of these two EC numbers applies to this sequence. Options C and D are more clearly eliminable as they belong to different top-level EC classes.


### Important caveats

- The EC annotation carries evidence code ECO:0000255 (HAMAP-Rule, computational) alongside ECO:0000305 (inferred by curator from PubMed 32555463). The HAMAP component is a computational similarity-based assignment, not direct experimental proof, though the PubMed reference provides experimental context.
- The sequence match is exact (770 AA, SHA256 confirmed) between the benchmark input and UniProt Q97U12, so the annotation applies to the supplied sequence.
- EC 2.3.1.319 is a very specific and relatively recent EC number; its exact reaction definition was not independently verified in this review.
- The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 770-aa sequence and four EC-number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (EC 4.3.1.24, a lyase) and D (EC 3.1.26.3, a ribonuclease/hydrolase) belong to entirely different EC top-level classes (4 = lyases, 3 = hydrolases) than the correct answer (2 = transferases). A knowledgeable model might attempt to rule these out by searching for transferase-like catalytic motifs (e.g., GNAT-fold or acetyl-CoA-binding signatures) and the absence of canonical lyase or RNase catalytic residues. However, options A (EC 2.3.1.319) and B (EC 2.3.1.193) are both acyltransferases within the same EC subclass 2.3.1. Distinguishing between these two requires knowing the exact substrate specificity and reaction mechanism of this particular protein — namely, that it acetylates cytidine(34) in elongator tRNA(Met) rather than whatever substrate EC 2.3.1.319 describes. No general sequence heuristic (motif scanning, length, composition) reliably separates two specific EC numbers in the same subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate and reaction catalyzed by this 770-residue archaeal protein (tRNA(Met) cytidine acetyltransferase vs. the reaction assigned to EC 2.3.1.319). This is an item-specific annotation fact (HAMAP rule MF_01886 / PubMed 32555463) that cannot be derived from the raw sequence by general biological reasoning.",
    "reason": "While C and D can potentially be eliminated by recognizing that the sequence lacks canonical lyase or RNase catalytic motifs, the critical discrimination between A (2.3.1.319) and B (2.3.1.193) depends on knowing the exact enzymatic reaction this protein catalyzes. Both are EC 2.3.1.x acyltransferases. No generalizable sequence feature distinguishes them without memorizing the database entry or performing a BLAST/HAMAP lookup."
  },
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q97U12 (sequence exactly matched, 770 AA, SHA256 confirmed) assigns EC 2.3.1.193 to this protein, named 'tRNA(Met) cytidine acetyltransferase TmcA 2'. The EC annotation is supported by both computational evidence (HAMAP-Rule MF_01886, ECO:0000255) and literature-based curator inference (PubMed 32555463, Sas-Chen et al. Nature 2020, ECO:0000305). Multiple catalytic activity entries (C5–C8) describe acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP, consistent with EC 2.3.1.193. The historical archived entry (version 122) confirms the same annotation."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000255 (HAMAP-Rule, computational) alongside ECO:0000305 (inferred by curator from PubMed 32555463). The HAMAP component is a computational similarity-based assignment, not direct experimental proof, though the PubMed reference provides experimental context.",
    "The sequence match is exact (770 AA, SHA256 confirmed) between the benchmark input and UniProt Q97U12, so the annotation applies to the supplied sequence.",
    "EC 2.3.1.319 is a very specific and relatively recent EC number; its exact reaction definition was not independently verified in this review.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 770-aa sequence and four EC-number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "EC 2.3.1.319 and EC 2.3.1.193 are both acyltransferases in the same EC subclass. Without the specific annotation or a structural/functional assay, a model cannot reliably distinguish which of these two EC numbers applies to this sequence. Options C and D are more clearly eliminable as they belong to different top-level EC classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q97U12 (sequence exactly matched, 770 AA, SHA256 confirmed) assigns EC 2.3.1.193 to this protein, named 'tRNA(Met) cytidine acetyltransferase TmcA 2'. The EC annotation is supported by both computational evidence (HAMAP-Rule MF_01886, ECO:0000255) and literature-based curator inference (PubMed 32555463, Sas-Chen et al. Nature 2020, ECO:0000305). Multiple catalytic activity entries (C5–C8) describe acetylation of cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP, consistent with EC 2.3.1.193. The historical archived entry (version 122) confirms the same annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "H1", "H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options C (EC 4.3.1.24, a lyase) and D (EC 3.1.26.3, a ribonuclease/hydrolase) belong to entirely different EC top-level classes (4 = lyases, 3 = hydrolases) than the correct answer (2 = transferases). A knowledgeable model might attempt to rule these out by searching for transferase-like catalytic motifs (e.g., GNAT-fold or acetyl-CoA-binding signatures) and the absence of canonical lyase or RNase catalytic residues. However, options A (EC 2.3.1.319) and B (EC 2.3.1.193) are both acyltransferases within the same EC subclass 2.3.1. Distinguishing between these two requires knowing the exact substrate specificity and reaction mechanism of this particular protein — namely, that it acetylates cytidine(34) in elongator tRNA(Met) rather than whatever substrate EC 2.3.1.319 describes. No general sequence heuristic (motif scanning, length, composition) reliably separates two specific EC numbers in the same subclass.",
    "missing_item_specific_fact": "The specific substrate and reaction catalyzed by this 770-residue archaeal protein (tRNA(Met) cytidine acetyltransferase vs. the reaction assigned to EC 2.3.1.319). This is an item-specific annotation fact (HAMAP rule MF_01886 / PubMed 32555463) that cannot be derived from the raw sequence by general biological reasoning.",
    "reason": "While C and D can potentially be eliminated by recognizing that the sequence lacks canonical lyase or RNase catalytic motifs, the critical discrimination between A (2.3.1.319) and B (2.3.1.193) depends on knowing the exact enzymatic reaction this protein catalyzes. Both are EC 2.3.1.x acyltransferases. No generalizable sequence feature distinguishes them without memorizing the database entry or performing a BLAST/HAMAP lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "EC 2.3.1.319 and EC 2.3.1.193 are both acyltransferases in the same EC subclass. Without the specific annotation or a structural/functional assay, a model cannot reliably distinguish which of these two EC numbers applies to this sequence. Options C and D are more clearly eliminable as they belong to different top-level EC classes."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000255 (HAMAP-Rule, computational) alongside ECO:0000305 (inferred by curator from PubMed 32555463). The HAMAP component is a computational similarity-based assignment, not direct experimental proof, though the PubMed reference provides experimental context.",
    "The sequence match is exact (770 AA, SHA256 confirmed) between the benchmark input and UniProt Q97U12, so the annotation applies to the supplied sequence.",
    "EC 2.3.1.319 is a very specific and relatively recent EC number; its exact reaction definition was not independently verified in this review.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 770-aa sequence and four EC-number choices."
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

**Accession:** `Q97U12` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
"Q97U12"
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"commonName":"Sulfolobus solfataricus","lineage":["Archaea","Thermoproteota","Thermoprotei","Sulfolobales","Sulfolobaceae","Saccharolobus"],"scientificName":"Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)","taxonId":273057}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA 2"}}}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82211"},{"database":"Rhea","id":"RHEA-COMP:15704"},{"database":"Rhea","id":"RHEA-COMP:19834"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:53876"},{"database":"Rhea","id":"RHEA-COMP:13670"},{"database":"Rhea","id":"RHEA-COMP:13671"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58480"},{"database":"Rhea","id":"RHEA-COMP:15145"},{"database":"Rhea","id":"RHEA-COMP:15146"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:36.729149+00:00.  

```json
{"citation":{"authors":["Sas-Chen A.","Thomas J.M.","Matzov D.","Taoka M.","Nance K.D.","Nir R.","Bryson K.M.","Shachar R.","Liman G.L.S.","Burkhart B.W.","Gamage S.T.","Nobe Y.","Briney C.A.","Levy M.J.","Fuchs R.T.","Robb G.B.","Hartmann J.","Sharma S.","Lin Q.","Florens L.","Washburn M.P.","Isobe T.","Santangelo T.J.","Shalev-Benami M.","Meier J.L.","Schwartz S."],"citationCrossReferences":[{"database":"PubMed","id":"32555463"},{"database":"DOI","id":"10.1038/s41586-020-2418-2"}],"citationType":"journal article","firstPage":"638","id":"32555463","journal":"Nature","lastPage":"643","publicationDate":"2020","title":"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.","volume":"583"},"referenceComments":[{"type":"STRAIN","value":"ATCC 35092 / DSM 1617 / JCM 11322 / P2"}],"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
ID   TMCA2_SACS2             Reviewed;         770 AA.
AC   Q97U12;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2001, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA 2 {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000305|PubMed:32555463};
GN   Name=tmcA2 {ECO:0000255|HAMAP-Rule:MF_01886};
GN   OrderedLocusNames=SSO3214 {ECO:0000312|EMBL:AAK43310.1};
OS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)
OS   (Sulfolobus solfataricus).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Saccharolobus.
OX   NCBI_TaxID=273057;
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA 2 {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000305|PubMed:32555463};
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 27-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
RN   [2]
RP   FUNCTION.
RC   STRAIN=ATCC 35092 / DSM 1617 / JCM 11322 / P2;
RX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;
RA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,
RA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,
RA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,
RA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,
RA   Shalev-Benami M., Meier J.L., Schwartz S.;
RT   "Dynamic RNA acetylation revealed by quantitative cross-evolutionary
RT   mapping.";
RL   Nature 583:638-643(2020).
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 59-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 68-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000305|PubMed:32555463};
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 76-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000305|PubMed:32555463};
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)  
**Locator:** `lines 84-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:32:38.813381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000305|PubMed:32555463};
```

Source SHA-256: `44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
