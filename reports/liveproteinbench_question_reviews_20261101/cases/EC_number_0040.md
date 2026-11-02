# EC_number_0040

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.8.1.7

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKFLQIIKHLKLQNKKNALDNFVNCRTYEHISNINKLFLNNFSSTKEHSEHGQVKHENFLNSTLKYEENSQNGSTNNLKNGKYNMYVSEGNVNINEEKYKDNNISSNNTQYNNNSSNSGSLNDEGPLWKEHIDDVVNENKKKKMNRFYLDSQATTMIDPRVLDKMLPYMTYIYGNAHSRNHFFGWESEKAVEDARTNLLNLINGKNNKEIIFTSGATESNNLALIGICTYYNKLNKQKNHIITSQIEHKCILQTCRFLQTKGFEVTYLKPDTNGLVKLDDIKNSIKDNTIMASFIFVNNEIGVIQDIENIGNLCKEKNILFHTDASQAAGKVPIDVQKMNIDLMSMSGHKLYGPKGIGALYIKRKKPNIRLNALIHGGGQERGLRSGTLPTHLIVGFGEAAKVCSLEMNRDEKKVRYFFNYVKDYLTKHLDYIVFNGCQINRYYGNMNISFLFVEGESLLMSLNEIALSSGSACTSSTLEPSYVLRSIGISEDIAHTSIRIGFNRFTTFFEVQQLCINLVKSVERLRSISPLYEMELEKKNPSNDDIPKFIWT

[Multiple Choices]
A. 2.8.1.11
B. 2.8.1.7
C. 3.2.1.20
D. 2.4.1.391
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

> The supplied 553-aa sequence exactly matches the UniProt sequence for Plasmodium falciparum IscS. Its EC 2.8.1.7 annotation is linked to experimental evidence (ECO:0000269, PubMed 34032321), including for the catalytic reaction. This supports choice B, though the cited paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence analysis might suggest a PLP-dependent sulfur-metabolism enzyme, but that broad inference does not establish the precise catalytic reaction needed to select the complete EC number, particularly between related sulfur-transferase options.


**Missing item-specific fact**

> The protein-specific identification as IscS and its experimentally characterized cysteine-desulfurase reaction, corresponding to EC 2.8.1.7.


**Reason**

> The input gives only sequence and choices; it does not supply the functional annotation or reaction measurement that resolves the exact EC assignment. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one EC assignment for the matched protein. The limitation is that the input alone does not provide enough item-specific functional evidence to establish it, not that the choices remain equally defensible given the annotation.


### Important caveats

- The UniProt annotation and sequence match are reviewer-only evidence, not information supplied to the evaluated model.
- The author's exact data-source snapshot is unknown; the historical record available by the stated cutoff also matches the sequence and lists EC 2.8.1.7.
- The experimental evidence code and citation support the annotation, but the underlying publication was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence analysis might suggest a PLP-dependent sulfur-metabolism enzyme, but that broad inference does not establish the precise catalytic reaction needed to select the complete EC number, particularly between related sulfur-transferase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as IscS and its experimentally characterized cysteine-desulfurase reaction, corresponding to EC 2.8.1.7.",
    "reason": "The input gives only sequence and choices; it does not supply the functional annotation or reaction measurement that resolves the exact EC assignment. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied 553-aa sequence exactly matches the UniProt sequence for Plasmodium falciparum IscS. Its EC 2.8.1.7 annotation is linked to experimental evidence (ECO:0000269, PubMed 34032321), including for the catalytic reaction. This supports choice B, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation and sequence match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The author's exact data-source snapshot is unknown; the historical record available by the stated cutoff also matches the sequence and lists EC 2.8.1.7.",
    "The experimental evidence code and citation support the annotation, but the underlying publication was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the matched protein. The limitation is that the input alone does not provide enough item-specific functional evidence to establish it, not that the choices remain equally defensible given the annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 553-aa sequence exactly matches the UniProt sequence for Plasmodium falciparum IscS. Its EC 2.8.1.7 annotation is linked to experimental evidence (ECO:0000269, PubMed 34032321), including for the catalytic reaction. This supports choice B, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence analysis might suggest a PLP-dependent sulfur-metabolism enzyme, but that broad inference does not establish the precise catalytic reaction needed to select the complete EC number, particularly between related sulfur-transferase options.",
    "missing_item_specific_fact": "The protein-specific identification as IscS and its experimentally characterized cysteine-desulfurase reaction, corresponding to EC 2.8.1.7.",
    "reason": "The input gives only sequence and choices; it does not supply the functional annotation or reaction measurement that resolves the exact EC assignment. Recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the matched protein. The limitation is that the input alone does not provide enough item-specific functional evidence to establish it, not that the choices remain equally defensible given the annotation."
  },
  "important_caveats": [
    "The UniProt annotation and sequence match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The author's exact data-source snapshot is unknown; the historical record available by the stated cutoff also matches the sequence and lists EC 2.8.1.7.",
    "The experimental evidence code and citation support the annotation, but the underlying publication was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, exact SHA256 match to the benchmark sequence) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by direct assay evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine → (sulfur carrier)-SH + L-alanine is experimentally characterized. Both current (v129) and historical (v127) entries confirm the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options C (3.2.1.20, α-L-fucosidase) and D (2.4.1.391, glycosyltransferase) can be eliminated by recognizing PLP-dependent enzyme fold features in the sequence (e.g., the 'TSG' motif near the N-terminus, 'GPKG' and 'IHGGG' motifs in the central region, and the overall domain architecture consistent with fold-type I PLP-dependent enzymes). However, options A (2.8.1.11, NifS-type cysteine desulfurase) and B (2.8.1.7, IscS-type cysteine desulfurase) catalyze the same overall reaction type (sulfur transfer from L-cysteine to a sulfur carrier). Distinguishing the IscS subfamily from the NifS subfamily at the EC-number level requires memorized knowledge of specific subfamily sequence signatures (e.g., the exact 'TSGAT' context, C-terminal domain architecture, and overall length) or database lookup. The EC distinction between 2.8.1.7 and 2.8.1.11 is a classification decision based on evolutionary lineage rather than a fundamentally different reaction mechanism.


**Missing item-specific fact**

> The specific subfamily assignment (IscS vs NifS) that determines whether the EC number is 2.8.1.7 or 2.8.1.11. While the 'TSG' motif and 'GPKG/IHGGG' context are suggestive of IscS, reliably distinguishing these two closely related cysteine desulfurase subfamilies from raw sequence without database access requires memorized family-specific signatures.


**Reason**

> The sequence clearly indicates a PLP-dependent sulfurtransferase, eliminating C and D. However, the critical A-vs-B distinction (IscS vs NifS) hinges on recognizing subfamily-specific sequence signatures that are not derivable from general enzyme-class reasoning alone. A model must either recognize the exact protein or memorize the IscS-vs-NifS sequence discriminants.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 2.8.1.7 (IscS-type cysteine desulfurase) and 2.8.1.11 (NifS-type cysteine desulfurase) catalyze the same overall reaction (sulfur transfer from L-cysteine to a sulfur carrier protein). Without memorized subfamily signatures, a knowledgeable biologist could reasonably assign either EC number based on the PLP-dependent sulfurtransferase features visible in the sequence. Options C and D are unambiguously eliminable.


### Important caveats

- The EC distinction between 2.8.1.7 and 2.8.1.11 is a subfamily classification within the same reaction type; it is not a mechanistically distinct reaction.
- The experimental evidence (ECO:0000269) supports the IscS assignment for this Plasmodium falciparum protein, but this was established through targeted biochemical assays in the 2021 Sadik et al. paper, not from sequence alone.
- The benchmark sequence matches Q8IBI5 exactly (SHA256 confirmed), and the historical entry (v127, released Jan 2026) already carried the 2.8.1.7 annotation, so the key was available at benchmark construction time.
- Plasmodium falciparum relies primarily on the ISC pathway for Fe-S cluster biogenesis (confirmed by Gisselberg et al. 2013, PubMed:24086138), which provides biological context favoring IscS over NifS, but this organism-specific pathway knowledge is itself a lookup-dependent fact.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (3.2.1.20, α-L-fucosidase) and D (2.4.1.391, glycosyltransferase) can be eliminated by recognizing PLP-dependent enzyme fold features in the sequence (e.g., the 'TSG' motif near the N-terminus, 'GPKG' and 'IHGGG' motifs in the central region, and the overall domain architecture consistent with fold-type I PLP-dependent enzymes). However, options A (2.8.1.11, NifS-type cysteine desulfurase) and B (2.8.1.7, IscS-type cysteine desulfurase) catalyze the same overall reaction type (sulfur transfer from L-cysteine to a sulfur carrier). Distinguishing the IscS subfamily from the NifS subfamily at the EC-number level requires memorized knowledge of specific subfamily sequence signatures (e.g., the exact 'TSGAT' context, C-terminal domain architecture, and overall length) or database lookup. The EC distinction between 2.8.1.7 and 2.8.1.11 is a classification decision based on evolutionary lineage rather than a fundamentally different reaction mechanism.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific subfamily assignment (IscS vs NifS) that determines whether the EC number is 2.8.1.7 or 2.8.1.11. While the 'TSG' motif and 'GPKG/IHGGG' context are suggestive of IscS, reliably distinguishing these two closely related cysteine desulfurase subfamilies from raw sequence without database access requires memorized family-specific signatures.",
    "reason": "The sequence clearly indicates a PLP-dependent sulfurtransferase, eliminating C and D. However, the critical A-vs-B distinction (IscS vs NifS) hinges on recognizing subfamily-specific sequence signatures that are not derivable from general enzyme-class reasoning alone. A model must either recognize the exact protein or memorize the IscS-vs-NifS sequence discriminants."
  },
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, exact SHA256 match to the benchmark sequence) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by direct assay evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine → (sulfur carrier)-SH + L-alanine is experimentally characterized. Both current (v129) and historical (v127) entries confirm the annotation."
  },
  "important_caveats": [
    "The EC distinction between 2.8.1.7 and 2.8.1.11 is a subfamily classification within the same reaction type; it is not a mechanistically distinct reaction.",
    "The experimental evidence (ECO:0000269) supports the IscS assignment for this Plasmodium falciparum protein, but this was established through targeted biochemical assays in the 2021 Sadik et al. paper, not from sequence alone.",
    "The benchmark sequence matches Q8IBI5 exactly (SHA256 confirmed), and the historical entry (v127, released Jan 2026) already carried the 2.8.1.7 annotation, so the key was available at benchmark construction time.",
    "Plasmodium falciparum relies primarily on the ISC pathway for Fe-S cluster biogenesis (confirmed by Gisselberg et al. 2013, PubMed:24086138), which provides biological context favoring IscS over NifS, but this organism-specific pathway knowledge is itself a lookup-dependent fact."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 2.8.1.7 (IscS-type cysteine desulfurase) and 2.8.1.11 (NifS-type cysteine desulfurase) catalyze the same overall reaction (sulfur transfer from L-cysteine to a sulfur carrier protein). Without memorized subfamily signatures, a knowledgeable biologist could reasonably assign either EC number based on the PLP-dependent sulfurtransferase features visible in the sequence. Options C and D are unambiguously eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, exact SHA256 match to the benchmark sequence) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by direct assay evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021, Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine → (sulfur carrier)-SH + L-alanine is experimentally characterized. Both current (v129) and historical (v127) entries confirm the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options C (3.2.1.20, α-L-fucosidase) and D (2.4.1.391, glycosyltransferase) can be eliminated by recognizing PLP-dependent enzyme fold features in the sequence (e.g., the 'TSG' motif near the N-terminus, 'GPKG' and 'IHGGG' motifs in the central region, and the overall domain architecture consistent with fold-type I PLP-dependent enzymes). However, options A (2.8.1.11, NifS-type cysteine desulfurase) and B (2.8.1.7, IscS-type cysteine desulfurase) catalyze the same overall reaction type (sulfur transfer from L-cysteine to a sulfur carrier). Distinguishing the IscS subfamily from the NifS subfamily at the EC-number level requires memorized knowledge of specific subfamily sequence signatures (e.g., the exact 'TSGAT' context, C-terminal domain architecture, and overall length) or database lookup. The EC distinction between 2.8.1.7 and 2.8.1.11 is a classification decision based on evolutionary lineage rather than a fundamentally different reaction mechanism.",
    "missing_item_specific_fact": "The specific subfamily assignment (IscS vs NifS) that determines whether the EC number is 2.8.1.7 or 2.8.1.11. While the 'TSG' motif and 'GPKG/IHGGG' context are suggestive of IscS, reliably distinguishing these two closely related cysteine desulfurase subfamilies from raw sequence without database access requires memorized family-specific signatures.",
    "reason": "The sequence clearly indicates a PLP-dependent sulfurtransferase, eliminating C and D. However, the critical A-vs-B distinction (IscS vs NifS) hinges on recognizing subfamily-specific sequence signatures that are not derivable from general enzyme-class reasoning alone. A model must either recognize the exact protein or memorize the IscS-vs-NifS sequence discriminants."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 2.8.1.7 (IscS-type cysteine desulfurase) and 2.8.1.11 (NifS-type cysteine desulfurase) catalyze the same overall reaction (sulfur transfer from L-cysteine to a sulfur carrier protein). Without memorized subfamily signatures, a knowledgeable biologist could reasonably assign either EC number based on the PLP-dependent sulfurtransferase features visible in the sequence. Options C and D are unambiguously eliminable."
  },
  "important_caveats": [
    "The EC distinction between 2.8.1.7 and 2.8.1.11 is a subfamily classification within the same reaction type; it is not a mechanistically distinct reaction.",
    "The experimental evidence (ECO:0000269) supports the IscS assignment for this Plasmodium falciparum protein, but this was established through targeted biochemical assays in the 2021 Sadik et al. paper, not from sequence alone.",
    "The benchmark sequence matches Q8IBI5 exactly (SHA256 confirmed), and the historical entry (v127, released Jan 2026) already carried the 2.8.1.7 annotation, so the key was available at benchmark construction time.",
    "Plasmodium falciparum relies primarily on the ISC pathway for Fe-S cluster biogenesis (confirmed by Gisselberg et al. 2013, PubMed:24086138), which provides biological context favoring IscS over NifS, but this organism-specific pathway knowledge is itself a lookup-dependent fact."
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

**Accession:** `Q8IBI5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
"Q8IBI5"
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"2.8.1.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cysteine desulfurase IscS"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscS"}]}}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:43893"}}],"reaction":{"ecNumber":"2.8.1.7","evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"name":"(sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43892"},{"database":"Rhea","id":"RHEA-COMP:14737"},{"database":"Rhea","id":"RHEA-COMP:14739"},{"database":"ChEBI","id":"CHEBI:29917"},{"database":"ChEBI","id":"CHEBI:35235"},{"database":"ChEBI","id":"CHEBI:57972"},{"database":"ChEBI","id":"CHEBI:64428"}]}}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"citation":{"authors":["Sadik M.","Afsar M.","Ramachandran R.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"34032321"},{"database":"DOI","id":"10.1111/mmi.14735"}],"citationType":"journal article","firstPage":"606","id":"34032321","journal":"Mol. Microbiol.","lastPage":"623","publicationDate":"2021","title":"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","INTERACTION WITH ISD11 AND ISCU"]}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
ID   ISCS_PLAF7              Reviewed;         553 AA.
AC   Q8IBI5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2003, sequence version 1.
DT   28-JAN-2026, entry version 127.
DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};
DE            Short=PfIscS {ECO:0000303|PubMed:34032321};
DE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};
GN   Name=IscS {ECO:0000303|PubMed:24086138, ECO:0000303|PubMed:34032321};
GN   Synonyms=NFS1 {ECO:0000305};
GN   ORFNames=PF3D7_0727200 {ECO:0000312|EMBL:CAD51015.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};
DE            Short=PfIscS {ECO:0000303|PubMed:34032321};
DE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 58-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, AND INTERACTION WITH ISD11
RP   AND ISCU.
RX   PubMed=34032321; DOI=10.1111/mmi.14735;
RA   Sadik M., Afsar M., Ramachandran R., Habib S.;
RT   "[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the
RT   Plasmodium falciparum mitochondrion.";
RL   Mol. Microbiol. 116:606-623(2021).
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 70-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-
CC         alanine; Xref=Rhea:RHEA:43892, Rhea:RHEA-COMP:14737, Rhea:RHEA-
CC         COMP:14739, ChEBI:CHEBI:29917, ChEBI:CHEBI:35235, ChEBI:CHEBI:57972,
CC         ChEBI:CHEBI:64428; EC=2.8.1.7;
CC         Evidence={ECO:0000269|PubMed:34032321};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:43893;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
