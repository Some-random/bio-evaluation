# GO_molecular_function_0061

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — folic acid transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. glutaminase activity
B. mannitol-1-phosphate 5-dehydrogenase activity
C. aspartic-type endopeptidase activity
D. folic acid transmembrane transporter activity
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

> The sequence exactly matches the reviewed Plasmodium falciparum folate transporter 2 entry. That entry attributes folate transport to experimental evidence and includes the matching GO term for folic acid transmembrane transporter activity. This supports D, while recognizing the database evidence is attributed to a cited study rather than independently assessed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has numerous long hydrophobic stretches consistent with a multi-pass membrane protein. Of the options, D is the transporter activity; the other choices are enzyme activities, making the membrane-protein topology a meaningful discriminator among these choices.


**Missing item-specific fact**

> The sequence topology alone does not establish folate as the transported substrate; that specificity is protein-specific. However, the choices contrast a transporter with three enzyme activities, so the topology provides grounds to select D without knowing the protein's database identity.


**Reason**

> The supplied sequence provides a concrete, biologically relevant topology signal that distinguishes the sole transmembrane-transporter option from the enzyme options. It does not independently prove the substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the multi-pass membrane-protein topology supports the transporter option rather than the enzyme activities.


### Important caveats

- The substrate-specific folate function is supported by reviewer-only annotation evidence, which was not supplied to the evaluated model.
- Hydrophobic topology supports a membrane protein but is not, on its own, proof of folate transport.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has numerous long hydrophobic stretches consistent with a multi-pass membrane protein. Of the options, D is the transporter activity; the other choices are enzyme activities, making the membrane-protein topology a meaningful discriminator among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence topology alone does not establish folate as the transported substrate; that specificity is protein-specific. However, the choices contrast a transporter with three enzyme activities, so the topology provides grounds to select D without knowing the protein's database identity.",
    "reason": "The supplied sequence provides a concrete, biologically relevant topology signal that distinguishes the sole transmembrane-transporter option from the enzyme options. It does not independently prove the substrate specificity."
  },
  "case_id": "GO_molecular_function_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the reviewed Plasmodium falciparum folate transporter 2 entry. That entry attributes folate transport to experimental evidence and includes the matching GO term for folic acid transmembrane transporter activity. This supports D, while recognizing the database evidence is attributed to a cited study rather than independently assessed here."
  },
  "important_caveats": [
    "The substrate-specific folate function is supported by reviewer-only annotation evidence, which was not supplied to the evaluated model.",
    "Hydrophobic topology supports a membrane protein but is not, on its own, proof of folate transport."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the multi-pass membrane-protein topology supports the transporter option rather than the enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the reviewed Plasmodium falciparum folate transporter 2 entry. That entry attributes folate transport to experimental evidence and includes the matching GO term for folic acid transmembrane transporter activity. This supports D, while recognizing the database evidence is attributed to a cited study rather than independently assessed here.",
    "evidence_ids": ["C1", "C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has numerous long hydrophobic stretches consistent with a multi-pass membrane protein. Of the options, D is the transporter activity; the other choices are enzyme activities, making the membrane-protein topology a meaningful discriminator among these choices.",
    "missing_item_specific_fact": "The sequence topology alone does not establish folate as the transported substrate; that specificity is protein-specific. However, the choices contrast a transporter with three enzyme activities, so the topology provides grounds to select D without knowing the protein's database identity.",
    "reason": "The supplied sequence provides a concrete, biologically relevant topology signal that distinguishes the sole transmembrane-transporter option from the enzyme options. It does not independently prove the substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the multi-pass membrane-protein topology supports the transporter option rather than the enzyme activities."
  },
  "important_caveats": [
    "The substrate-specific folate function is supported by reviewer-only annotation evidence, which was not supplied to the evaluated model.",
    "Hydrophobic topology supports a membrane protein but is not, on its own, proof of folate transport."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (455 AA, SHA256 match) corresponds to UniProt Q8IIK1 (PfFT2, Folate transporter 2) from Plasmodium falciparum 3D7. UniProt annotates GO:0008517 (folic acid transmembrane transporter activity) with evidence code IDA (Inferred from Direct Assay, PubMed:21998306). The FUNCTION comment explicitly states it is a folate transporter with broad substrate specificity, and two CATALYTIC ACTIVITY entries describe proton-coupled folate transport. The GO term text matches option D exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits approximately 12+ hydrophobic stretches of 20+ residues consistent with a polytopic transmembrane protein (MFS-like fold). Options A (glutaminase, a soluble hydrolase), B (mannitol-1-phosphate 5-dehydrogenase, a soluble oxidoreductase), and C (aspartic-type endopeptidase, typically 1–2 TM domains at most, with characteristic D-x-T/G catalytic motifs absent here) are all inconsistent with a 12-TM polytopic architecture. Option D, folic acid transmembrane transporter activity, is the only option requiring a multi-pass membrane topology, which is directly evident from the hydrophobic segment pattern in the sequence.


**Missing item-specific fact**

> None critical. The specific substrate identity (folate vs. another MFS substrate) is not derivable from sequence alone, but the question only requires distinguishing a transporter from three non-transporter enzymes, which the topology argument resolves.


**Reason**

> A model with general knowledge of protein topology can observe the polytopic membrane architecture from the sequence and eliminate three soluble/low-TM enzyme classes, arriving at the single transporter option. This is a concrete structural-biology argument, not mere memorization of the UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe soluble enzymes (hydrolase, oxidoreductase, peptidase) with fundamentally different topologies from the observed polytopic membrane protein. Option C (aspartic protease) could theoretically be membrane-associated (e.g., presenilin), but the sequence lacks the conserved D-x-T/G catalytic motifs and the topology (7 TM for presenilin vs. ~12 TM here) does not match. D is the only option consistent with the observed architecture.


### Important caveats

- The GO annotation carries IDA evidence (direct experimental assay, PubMed:21998306), making the key experimentally grounded rather than purely computational.
- The sequence-to-accession identification (Q8IIK1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.
- The specific folate-substrate identification relies on the experimental paper; a purely sequence-based model could only conclude 'polytopic membrane transporter' without specifying folate. However, since D is the sole transporter option, the elimination logic suffices for the multiple-choice format.
- The entry was first publicly released 2025-02-05 (Swiss-Prot); the historical entry version 107 (2026-01-28) already contained the folate transporter annotation, so the key was available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits approximately 12+ hydrophobic stretches of 20+ residues consistent with a polytopic transmembrane protein (MFS-like fold). Options A (glutaminase, a soluble hydrolase), B (mannitol-1-phosphate 5-dehydrogenase, a soluble oxidoreductase), and C (aspartic-type endopeptidase, typically 1–2 TM domains at most, with characteristic D-x-T/G catalytic motifs absent here) are all inconsistent with a 12-TM polytopic architecture. Option D, folic acid transmembrane transporter activity, is the only option requiring a multi-pass membrane topology, which is directly evident from the hydrophobic segment pattern in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific substrate identity (folate vs. another MFS substrate) is not derivable from sequence alone, but the question only requires distinguishing a transporter from three non-transporter enzymes, which the topology argument resolves.",
    "reason": "A model with general knowledge of protein topology can observe the polytopic membrane architecture from the sequence and eliminate three soluble/low-TM enzyme classes, arriving at the single transporter option. This is a concrete structural-biology argument, not mere memorization of the UniProt entry."
  },
  "case_id": "GO_molecular_function_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence (455 AA, SHA256 match) corresponds to UniProt Q8IIK1 (PfFT2, Folate transporter 2) from Plasmodium falciparum 3D7. UniProt annotates GO:0008517 (folic acid transmembrane transporter activity) with evidence code IDA (Inferred from Direct Assay, PubMed:21998306). The FUNCTION comment explicitly states it is a folate transporter with broad substrate specificity, and two CATALYTIC ACTIVITY entries describe proton-coupled folate transport. The GO term text matches option D exactly."
  },
  "important_caveats": [
    "The GO annotation carries IDA evidence (direct experimental assay, PubMed:21998306), making the key experimentally grounded rather than purely computational.",
    "The sequence-to-accession identification (Q8IIK1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "The specific folate-substrate identification relies on the experimental paper; a purely sequence-based model could only conclude 'polytopic membrane transporter' without specifying folate. However, since D is the sole transporter option, the elimination logic suffices for the multiple-choice format.",
    "The entry was first publicly released 2025-02-05 (Swiss-Prot); the historical entry version 107 (2026-01-28) already contained the folate transporter annotation, so the key was available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe soluble enzymes (hydrolase, oxidoreductase, peptidase) with fundamentally different topologies from the observed polytopic membrane protein. Option C (aspartic protease) could theoretically be membrane-associated (e.g., presenilin), but the sequence lacks the conserved D-x-T/G catalytic motifs and the topology (7 TM for presenilin vs. ~12 TM here) does not match. D is the only option consistent with the observed architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (455 AA, SHA256 match) corresponds to UniProt Q8IIK1 (PfFT2, Folate transporter 2) from Plasmodium falciparum 3D7. UniProt annotates GO:0008517 (folic acid transmembrane transporter activity) with evidence code IDA (Inferred from Direct Assay, PubMed:21998306). The FUNCTION comment explicitly states it is a folate transporter with broad substrate specificity, and two CATALYTIC ACTIVITY entries describe proton-coupled folate transport. The GO term text matches option D exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits approximately 12+ hydrophobic stretches of 20+ residues consistent with a polytopic transmembrane protein (MFS-like fold). Options A (glutaminase, a soluble hydrolase), B (mannitol-1-phosphate 5-dehydrogenase, a soluble oxidoreductase), and C (aspartic-type endopeptidase, typically 1–2 TM domains at most, with characteristic D-x-T/G catalytic motifs absent here) are all inconsistent with a 12-TM polytopic architecture. Option D, folic acid transmembrane transporter activity, is the only option requiring a multi-pass membrane topology, which is directly evident from the hydrophobic segment pattern in the sequence.",
    "missing_item_specific_fact": "None critical. The specific substrate identity (folate vs. another MFS substrate) is not derivable from sequence alone, but the question only requires distinguishing a transporter from three non-transporter enzymes, which the topology argument resolves.",
    "reason": "A model with general knowledge of protein topology can observe the polytopic membrane architecture from the sequence and eliminate three soluble/low-TM enzyme classes, arriving at the single transporter option. This is a concrete structural-biology argument, not mere memorization of the UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe soluble enzymes (hydrolase, oxidoreductase, peptidase) with fundamentally different topologies from the observed polytopic membrane protein. Option C (aspartic protease) could theoretically be membrane-associated (e.g., presenilin), but the sequence lacks the conserved D-x-T/G catalytic motifs and the topology (7 TM for presenilin vs. ~12 TM here) does not match. D is the only option consistent with the observed architecture."
  },
  "important_caveats": [
    "The GO annotation carries IDA evidence (direct experimental assay, PubMed:21998306), making the key experimentally grounded rather than purely computational.",
    "The sequence-to-accession identification (Q8IIK1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.",
    "The specific folate-substrate identification relies on the experimental paper; a purely sequence-based model could only conclude 'polytopic membrane transporter' without specifying folate. However, since D is the sole transporter option, the elimination logic suffices for the multiple-choice format.",
    "The entry was first publicly released 2025-02-05 (Swiss-Prot); the historical entry version 107 (2026-01-28) already contained the folate transporter annotation, so the key was available at benchmark construction time."
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

**Accession:** `Q8IIK1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
"Q8IIK1"
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"Folate transporter 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21998306","source":"PubMed"}],"value":"PfFT2"}]}}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21998306","source":"PubMed"}],"value":"Folate transporter with broad substrate specificity (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid, dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA) and the human folate catabolite pABA monoglutamate (PubMed:21998306). Can transport 5-methyltetrahydrofolate with low efficiency (PubMed:21998306)"}]}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"21998306","source":"PubMed"}],"name":"folate(in) + H(+)(in) = folate(out) + H(+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:70159"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:62501"}]}}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"21998306","source":"PubMed"}],"name":"(6S)-5-methyl-5,6,7,8-tetrahydrofolate(in) + H(+)(in) = (6S)-5-methyl-5,6,7,8-tetrahydrofolate(out) + H(+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:70167"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:18608"}]}}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"21998306","source":"PubMed"}],"id":"GO:0008517","properties":[{"key":"GoTerm","value":"F:folic acid transmembrane transporter activity"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 36-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
CC   -!- FUNCTION: Folate transporter with broad substrate specificity
CC       (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid,
CC       dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA)
CC       and the human folate catabolite pABA monoglutamate (PubMed:21998306).
CC       Can transport 5-methyltetrahydrofolate with low efficiency
CC       (PubMed:21998306). {ECO:0000269|PubMed:21998306}.
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 42-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=folate(in) + H(+)(in) = folate(out) + H(+)(out);
CC         Xref=Rhea:RHEA:70159, ChEBI:CHEBI:15378, ChEBI:CHEBI:62501;
CC         Evidence={ECO:0000305|PubMed:21998306};
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 46-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(6S)-5-methyl-5,6,7,8-tetrahydrofolate(in) + H(+)(in) = (6S)-
CC         5-methyl-5,6,7,8-tetrahydrofolate(out) + H(+)(out);
CC         Xref=Rhea:RHEA:70167, ChEBI:CHEBI:15378, ChEBI:CHEBI:18608;
CC         Evidence={ECO:0000305|PubMed:21998306};
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
DR   GO; GO:0008517; F:folic acid transmembrane transporter activity; IDA:GeneDB.
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 84461-84477`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008517
name: folic acid transmembrane transporter activity
namespace: molecular_function
def: "Enables the transfer of folic acid (pteroylglutamic acid) from one side of a membrane to the other. Folic acid is widely distributed as a member of the vitamin B complex and is essential for the synthesis of purine and pyrimidines." [GOC:ai]
synonym: "folate transmembrane transporter activity" EXACT []
synonym: "folate transporter activity" EXACT []
synonym: "folic acid transporter activity" RELATED []
synonym: "vitamin B9 transporter activity" EXACT []
synonym: "vitamin M transporter activity" EXACT []
xref: Reactome:R-HSA-200652 "SLC19A1 transports 5-methyl-THF from extracellular region to cytosol"
xref: Reactome:R-HSA-200680 "SLC25A32 transports THF from cytosol to mitochondrial matrix"
xref: Reactome:R-HSA-200720 "SLC25A32 transports THF from mitochondrial matrix to cytosol"
is_a: GO:0005310 ! dicarboxylic acid transmembrane transporter activity
is_a: GO:0072349 ! modified amino acid transmembrane transporter activity
is_a: GO:0090482 ! vitamin transmembrane transporter activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
