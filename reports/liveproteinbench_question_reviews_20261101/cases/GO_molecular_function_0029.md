# GO_molecular_function_0029

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — folic acid transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEDDDFSIKDKKENYETCSTETISSYISINEKCQLIEKDINDDNHENPYMIFNKISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQVVESNRNCSINSSARNVSLFFAFRKLSFAIMSYLSGYLLLLISKKHIFLIGSFLPICVFTSGFFIIEKRNYTKSSIKDQIKCIYSIIKLSYLKNFIIFIFIMMSTPSCGNTLFFYITNELKFSPNLLGKMAMFQSLASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKKVNYFLFIPNTLFFITDTVLIEFIAEFQTMPILVLCSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPNHSQKKNLQHSNSHTQKYYSYPSTDYISSQKSDSSEITKFSADMQIDDITLE

[Multiple Choices]
A. folic acid transmembrane transporter activity
B. beta-glucuronidase activity
C. NAD binding
D. calcium-dependent phospholipid binding
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

> The supplied sequence exactly matches the Plasmodium falciparum Folate transporter 1 record. That record describes folate transport with ECO:0000269 evidence and assigns folic acid transmembrane transporter activity with IDA evidence. This supports choice A; the evidence is annotation linked to a cited study, not a primary-paper assessment here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many hydrophobic segments, consistent with a multipass membrane protein, which favors a transmembrane function over the soluble-enzyme choices. But that topology does not identify folic acid as the transported substrate.


**Missing item-specific fact**

> The protein-specific evidence that this membrane protein transports folate, rather than another substrate or performing another membrane-associated function.


**Reason**

> The exact folate-transporter function depends on protein-specific characterization or annotation absent from the input. Recognizing the sequence or retrieving its database record would supply that fact; generic topology-based inference alone does not establish the folate-specific GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a multipass membrane-protein interpretation, but the choices do not provide a second comparably supported function. The limitation is that the substrate specificity is not inferable from the sequence alone, rather than that multiple listed answers are equally defensible.


### Important caveats

- Reviewer-only annotations and source identity were not supplied to the evaluated model.
- The source record matches the sequence, but the author's exact annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic segments, consistent with a multipass membrane protein, which favors a transmembrane function over the soluble-enzyme choices. But that topology does not identify folic acid as the transported substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this membrane protein transports folate, rather than another substrate or performing another membrane-associated function.",
    "reason": "The exact folate-transporter function depends on protein-specific characterization or annotation absent from the input. Recognizing the sequence or retrieving its database record would supply that fact; generic topology-based inference alone does not establish the folate-specific GO term."
  },
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium falciparum Folate transporter 1 record. That record describes folate transport with ECO:0000269 evidence and assigns folic acid transmembrane transporter activity with IDA evidence. This supports choice A; the evidence is annotation linked to a cited study, not a primary-paper assessment here."
  },
  "important_caveats": [
    "Reviewer-only annotations and source identity were not supplied to the evaluated model.",
    "The source record matches the sequence, but the author's exact annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a multipass membrane-protein interpretation, but the choices do not provide a second comparably supported function. The limitation is that the substrate specificity is not inferable from the sequence alone, rather than that multiple listed answers are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium falciparum Folate transporter 1 record. That record describes folate transport with ECO:0000269 evidence and assigns folic acid transmembrane transporter activity with IDA evidence. This supports choice A; the evidence is annotation linked to a cited study, not a primary-paper assessment here.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many hydrophobic segments, consistent with a multipass membrane protein, which favors a transmembrane function over the soluble-enzyme choices. But that topology does not identify folic acid as the transported substrate.",
    "missing_item_specific_fact": "The protein-specific evidence that this membrane protein transports folate, rather than another substrate or performing another membrane-associated function.",
    "reason": "The exact folate-transporter function depends on protein-specific characterization or annotation absent from the input. Recognizing the sequence or retrieving its database record would supply that fact; generic topology-based inference alone does not establish the folate-specific GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a multipass membrane-protein interpretation, but the choices do not provide a second comparably supported function. The limitation is that the substrate specificity is not inferable from the sequence alone, rather than that multiple listed answers are equally defensible."
  },
  "important_caveats": [
    "Reviewer-only annotations and source identity were not supplied to the evaluated model.",
    "The source record matches the sequence, but the author's exact annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) is annotated with GO:0008517 'folic acid transmembrane transporter activity' with evidence code IDA:GeneDB (Inferred from Direct Assay, PubMed:21998306). The protein is experimentally confirmed to transport folic acid, folinic acid, pteroic acid, dihydropteroic acid, pABA, and pABA monoglutamate across membranes via a proton-coupled mechanism. The sequence matches the benchmark input exactly (505 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'SLIAMLQGVEVLCNLSIIYLLK', 'SLSIVMCFIKIPWSIKLVWAVISD', 'GSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIG', 'SFLPICVFTSGFFIIEKR', 'ASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKK', 'CSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPN') characteristic of a multi-pass integral membrane transporter. Among the four choices, only A describes a transmembrane transporter activity. B (beta-glucuronidase, EC 3.2.1.31) is a soluble hydrolase with a TIM-barrel fold and catalytic Glu/Asp residues absent here. C (NAD binding) is associated with soluble Rossmann-fold enzymes (GxGxxG motif absent). D (calcium-dependent phospholipid binding) corresponds to C2-domain peripheral membrane proteins (~130 aa beta-sandwich), incompatible with a multi-pass integral membrane architecture. The transmembrane topology thus meaningfully eliminates B, C, and D.


**Missing item-specific fact**

> None critical. While identifying the specific substrate as folic acid (rather than another transmembrane transport substrate) would require database knowledge, the question's four options are structured so that only A is a transmembrane transporter function; the other three are soluble-protein functions incompatible with the observed multi-pass membrane architecture.


**Reason**

> A model can observe the multi-pass transmembrane topology from the hydrophobic segments and eliminate the three soluble-protein functions (hydrolase, nucleotide-binding, C2-domain binding) by general biological knowledge of protein architecture-function relationships. The specific substrate identity (folic acid) is not independently derivable from sequence motifs alone, but is not needed to select among these four options because only A is a transmembrane transporter activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct protein classes (transmembrane transporter, soluble hydrolase, soluble nucleotide-binding protein, C2-domain peripheral protein). The multi-pass transmembrane architecture of the sequence uniquely matches option A. No other option is compatible with an integral multi-pass membrane protein lacking catalytic or C2-domain features.


### Important caveats

- The GO annotation is IDA (Inferred from Direct Assay) based on PubMed:21998306, an experimental characterization of PfFT1 transport kinetics in Xenopus oocytes and parasite uptake assays.
- The reviewer-only evidence confirms the protein identity and experimental support, but this information was not available to the evaluated model.
- While the transmembrane architecture strongly eliminates B, C, and D, distinguishing 'folic acid' transport from other transmembrane transport activities would require additional knowledge not derivable from sequence alone. However, this is not needed because no other option describes a transmembrane transporter.
- The sequence match between the benchmark input and UniProt Q8IBB7 is exact (505 aa, SHA256 confirmed across current and archived entries).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'SLIAMLQGVEVLCNLSIIYLLK', 'SLSIVMCFIKIPWSIKLVWAVISD', 'GSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIG', 'SFLPICVFTSGFFIIEKR', 'ASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKK', 'CSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPN') characteristic of a multi-pass integral membrane transporter. Among the four choices, only A describes a transmembrane transporter activity. B (beta-glucuronidase, EC 3.2.1.31) is a soluble hydrolase with a TIM-barrel fold and catalytic Glu/Asp residues absent here. C (NAD binding) is associated with soluble Rossmann-fold enzymes (GxGxxG motif absent). D (calcium-dependent phospholipid binding) corresponds to C2-domain peripheral membrane proteins (~130 aa beta-sandwich), incompatible with a multi-pass integral membrane architecture. The transmembrane topology thus meaningfully eliminates B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While identifying the specific substrate as folic acid (rather than another transmembrane transport substrate) would require database knowledge, the question's four options are structured so that only A is a transmembrane transporter function; the other three are soluble-protein functions incompatible with the observed multi-pass membrane architecture.",
    "reason": "A model can observe the multi-pass transmembrane topology from the hydrophobic segments and eliminate the three soluble-protein functions (hydrolase, nucleotide-binding, C2-domain binding) by general biological knowledge of protein architecture-function relationships. The specific substrate identity (folic acid) is not independently derivable from sequence motifs alone, but is not needed to select among these four options because only A is a transmembrane transporter activity."
  },
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) is annotated with GO:0008517 'folic acid transmembrane transporter activity' with evidence code IDA:GeneDB (Inferred from Direct Assay, PubMed:21998306). The protein is experimentally confirmed to transport folic acid, folinic acid, pteroic acid, dihydropteroic acid, pABA, and pABA monoglutamate across membranes via a proton-coupled mechanism. The sequence matches the benchmark input exactly (505 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation is IDA (Inferred from Direct Assay) based on PubMed:21998306, an experimental characterization of PfFT1 transport kinetics in Xenopus oocytes and parasite uptake assays.",
    "The reviewer-only evidence confirms the protein identity and experimental support, but this information was not available to the evaluated model.",
    "While the transmembrane architecture strongly eliminates B, C, and D, distinguishing 'folic acid' transport from other transmembrane transport activities would require additional knowledge not derivable from sequence alone. However, this is not needed because no other option describes a transmembrane transporter.",
    "The sequence match between the benchmark input and UniProt Q8IBB7 is exact (505 aa, SHA256 confirmed across current and archived entries)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct protein classes (transmembrane transporter, soluble hydrolase, soluble nucleotide-binding protein, C2-domain peripheral protein). The multi-pass transmembrane architecture of the sequence uniquely matches option A. No other option is compatible with an integral multi-pass membrane protein lacking catalytic or C2-domain features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) is annotated with GO:0008517 'folic acid transmembrane transporter activity' with evidence code IDA:GeneDB (Inferred from Direct Assay, PubMed:21998306). The protein is experimentally confirmed to transport folic acid, folinic acid, pteroic acid, dihydropteroic acid, pABA, and pABA monoglutamate across membranes via a proton-coupled mechanism. The sequence matches the benchmark input exactly (505 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 505-aa sequence contains numerous long hydrophobic stretches (e.g., 'SLIAMLQGVEVLCNLSIIYLLK', 'SLSIVMCFIKIPWSIKLVWAVISD', 'GSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIG', 'SFLPICVFTSGFFIIEKR', 'ASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKK', 'CSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPN') characteristic of a multi-pass integral membrane transporter. Among the four choices, only A describes a transmembrane transporter activity. B (beta-glucuronidase, EC 3.2.1.31) is a soluble hydrolase with a TIM-barrel fold and catalytic Glu/Asp residues absent here. C (NAD binding) is associated with soluble Rossmann-fold enzymes (GxGxxG motif absent). D (calcium-dependent phospholipid binding) corresponds to C2-domain peripheral membrane proteins (~130 aa beta-sandwich), incompatible with a multi-pass integral membrane architecture. The transmembrane topology thus meaningfully eliminates B, C, and D.",
    "missing_item_specific_fact": "None critical. While identifying the specific substrate as folic acid (rather than another transmembrane transport substrate) would require database knowledge, the question's four options are structured so that only A is a transmembrane transporter function; the other three are soluble-protein functions incompatible with the observed multi-pass membrane architecture.",
    "reason": "A model can observe the multi-pass transmembrane topology from the hydrophobic segments and eliminate the three soluble-protein functions (hydrolase, nucleotide-binding, C2-domain binding) by general biological knowledge of protein architecture-function relationships. The specific substrate identity (folic acid) is not independently derivable from sequence motifs alone, but is not needed to select among these four options because only A is a transmembrane transporter activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct protein classes (transmembrane transporter, soluble hydrolase, soluble nucleotide-binding protein, C2-domain peripheral protein). The multi-pass transmembrane architecture of the sequence uniquely matches option A. No other option is compatible with an integral multi-pass membrane protein lacking catalytic or C2-domain features."
  },
  "important_caveats": [
    "The GO annotation is IDA (Inferred from Direct Assay) based on PubMed:21998306, an experimental characterization of PfFT1 transport kinetics in Xenopus oocytes and parasite uptake assays.",
    "The reviewer-only evidence confirms the protein identity and experimental support, but this information was not available to the evaluated model.",
    "While the transmembrane architecture strongly eliminates B, C, and D, distinguishing 'folic acid' transport from other transmembrane transport activities would require additional knowledge not derivable from sequence alone. However, this is not needed because no other option describes a transmembrane transporter.",
    "The sequence match between the benchmark input and UniProt Q8IBB7 is exact (505 aa, SHA256 confirmed across current and archived entries)."
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

**Accession:** `Q8IBB7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 98. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
"Q8IBB7"
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"entryVersion":100,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2003-03-01","sequenceVersion":1}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"Folate transporter 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"PfFT1"}]}}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21998306","source":"PubMed"}],"value":"Folate transporter with broad substrate specificity (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid, dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA) and the human folate catabolite pABA monoglutamate (PubMed:21998306)"}]}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"21998306","source":"PubMed"}],"name":"folate(in) + H(+)(in) = folate(out) + H(+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:70159"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:62501"}]}}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.455529+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"21998306","source":"PubMed"}],"id":"GO:0008517","properties":[{"key":"GoTerm","value":"F:folic acid transmembrane transporter activity"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 56-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
CC   -!- FUNCTION: Folate transporter with broad substrate specificity
CC       (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid,
CC       dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA)
CC       and the human folate catabolite pABA monoglutamate (PubMed:21998306).
CC       {ECO:0000269|PubMed:21998306}.
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 61-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=folate(in) + H(+)(in) = folate(out) + H(+)(out);
CC         Xref=Rhea:RHEA:70159, ChEBI:CHEBI:15378, ChEBI:CHEBI:62501;
CC         Evidence={ECO:0000305|PubMed:21998306};
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 98 / 1.  
**Retrieved:** 2026-11-02T04:32:10.640562+00:00.  

```text
DR   GO; GO:0008517; F:folic acid transmembrane transporter activity; IDA:GeneDB.
```

Source SHA-256: `23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
