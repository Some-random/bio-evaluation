# catalytic_activity_0001

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
B. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
C. an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)
D. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt sequence annotated as peptidyl-tRNA hydrolase (EC 3.1.1.29), whose catalytic reaction is option C. The general activity annotation is attributed to the computational HAMAP rule; a cited literature-backed annotation also reports hydrolysis of N-acetylglycyl-tRNA to N-acetylglycine and tRNA, consistent with option C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone gives no sufficiently concrete biological argument for identifying this protein specifically as a peptidyl-tRNA hydrolase and selecting its tRNA-deacylation reaction over the other choices. Doing so would require recognizing its protein family or retrieving its functional annotation.


**Missing item-specific fact**

> The absent item-specific fact is that this sequence is a peptidyl-tRNA hydrolase (Pth), with EC 3.1.1.29 activity.


**Reason**

> The options name distinct, specific enzyme reactions; the input provides only an uncontextualized sequence. The reviewer-only annotation supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's annotated peptidyl-tRNA hydrolase activity corresponds to option C; the supplied evidence does not support another listed reaction.


### Important caveats

- The broad peptidyl-tRNA hydrolase annotation is computationally assigned by HAMAP, not itself a direct experimental measurement.
- The sequence match establishes that the annotation applies to the supplied sequence; the cited literature-backed annotation supports a specific N-acetylglycyl-tRNA reaction. The primary papers were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone gives no sufficiently concrete biological argument for identifying this protein specifically as a peptidyl-tRNA hydrolase and selecting its tRNA-deacylation reaction over the other choices. Doing so would require recognizing its protein family or retrieving its functional annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The absent item-specific fact is that this sequence is a peptidyl-tRNA hydrolase (Pth), with EC 3.1.1.29 activity.",
    "reason": "The options name distinct, specific enzyme reactions; the input provides only an uncontextualized sequence. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as peptidyl-tRNA hydrolase (EC 3.1.1.29), whose catalytic reaction is option C. The general activity annotation is attributed to the computational HAMAP rule; a cited literature-backed annotation also reports hydrolysis of N-acetylglycyl-tRNA to N-acetylglycine and tRNA, consistent with option C."
  },
  "important_caveats": [
    "The broad peptidyl-tRNA hydrolase annotation is computationally assigned by HAMAP, not itself a direct experimental measurement.",
    "The sequence match establishes that the annotation applies to the supplied sequence; the cited literature-backed annotation supports a specific N-acetylglycyl-tRNA reaction. The primary papers were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's annotated peptidyl-tRNA hydrolase activity corresponds to option C; the supplied evidence does not support another listed reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as peptidyl-tRNA hydrolase (EC 3.1.1.29), whose catalytic reaction is option C. The general activity annotation is attributed to the computational HAMAP rule; a cited literature-backed annotation also reports hydrolysis of N-acetylglycyl-tRNA to N-acetylglycine and tRNA, consistent with option C.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone gives no sufficiently concrete biological argument for identifying this protein specifically as a peptidyl-tRNA hydrolase and selecting its tRNA-deacylation reaction over the other choices. Doing so would require recognizing its protein family or retrieving its functional annotation.",
    "missing_item_specific_fact": "The absent item-specific fact is that this sequence is a peptidyl-tRNA hydrolase (Pth), with EC 3.1.1.29 activity.",
    "reason": "The options name distinct, specific enzyme reactions; the input provides only an uncontextualized sequence. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's annotated peptidyl-tRNA hydrolase activity corresponds to option C; the supplied evidence does not support another listed reaction."
  },
  "important_caveats": [
    "The broad peptidyl-tRNA hydrolase annotation is computationally assigned by HAMAP, not itself a direct experimental measurement.",
    "The sequence match establishes that the annotation applies to the supplied sequence; the cited literature-backed annotation supports a specific N-acetylglycyl-tRNA reaction. The primary papers were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA-256 match confirmed in both current and historical records). The entry is annotated as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29). The catalytic activity 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' is listed verbatim as the primary reaction (evidence C5/H5, HAMAP-Rule MF_00083, ECO:0000255). Additionally, two experimental papers (PubMed:27264868, PubMed:29777131; ECO:0000305) confirm catalytic hydrolysis of N-acetylglycyl-tRNA(Gly) (evidence C6/H6), providing experimental corroboration of peptidyl-tRNA ester-bond hydrolysis. Choice C matches the annotated reaction exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved 'GHGGH' histidine-rich motif (residues ~113-117: 'GGGHGGHNGLKDIIS'), which is a well-known family signature for peptidyl-tRNA hydrolase (Pth). A knowledgeable model can reason: (1) the GHGGH motif is characteristic of the Pth enzyme family; (2) Pth catalyzes hydrolysis of the ester bond linking the amino acid to the 3'-terminal adenosine of tRNA; (3) this corresponds to the reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)', i.e., choice C. The other options describe lipoxygenase (A), nitroreductase (B), and dihydroxy-acid dehydratase (D) activities, none of which are associated with the GHGGH signature or the overall 194-aa Pth fold.


**Missing item-specific fact**

> None strictly required. The GHGGH motif is a general protein-family signature rather than an item-specific annotation. However, a model without training on protein-family motifs would need to look up the sequence in a database.


**Reason**

> The GHGGH motif is a widely recognized, general protein-family signature for peptidyl-tRNA hydrolase. Identifying this motif and inferring the enzyme class (and hence the hydrolysis of the peptidyl-tRNA ester bond) constitutes a defensible biological inference from the supplied sequence. This goes beyond exact-sequence memorization; it uses a conserved functional motif as a reasoning anchor. The four distractors span entirely different enzyme classes (oxidation, reduction, dehydration), making the motif-based identification sufficiently discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes (lipoxygenase, nitroreductase, peptidyl-tRNA hydrolase, dihydroxy-acid dehydratase). The GHGGH motif and overall sequence architecture point specifically to Pth. No other option is defensible for this sequence.


### Important caveats

- The primary EC annotation (3.1.1.29) is assigned by HAMAP-Rule (ECO:0000255), a computational protein-family rule, not by direct experiment on this exact Salmonella Pth. Experimental evidence (ECO:0000305) confirms activity on N-acetylglycyl-tRNA(Gly) specifically, supporting the general peptidyl-tRNA hydrolase function.
- The GHGGH motif recognition depends on the model having been trained on protein-family signatures; a model lacking this training would effectively need a database lookup.
- The reviewer-only evidence was absent from the evaluated model's input; the model must work solely from the 194-aa sequence and the four choices.
- The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation is relatively recent; the underlying Pth family is well established in E. coli and other bacteria.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved 'GHGGH' histidine-rich motif (residues ~113-117: 'GGGHGGHNGLKDIIS'), which is a well-known family signature for peptidyl-tRNA hydrolase (Pth). A knowledgeable model can reason: (1) the GHGGH motif is characteristic of the Pth enzyme family; (2) Pth catalyzes hydrolysis of the ester bond linking the amino acid to the 3'-terminal adenosine of tRNA; (3) this corresponds to the reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)', i.e., choice C. The other options describe lipoxygenase (A), nitroreductase (B), and dihydroxy-acid dehydratase (D) activities, none of which are associated with the GHGGH signature or the overall 194-aa Pth fold.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The GHGGH motif is a general protein-family signature rather than an item-specific annotation. However, a model without training on protein-family motifs would need to look up the sequence in a database.",
    "reason": "The GHGGH motif is a widely recognized, general protein-family signature for peptidyl-tRNA hydrolase. Identifying this motif and inferring the enzyme class (and hence the hydrolysis of the peptidyl-tRNA ester bond) constitutes a defensible biological inference from the supplied sequence. This goes beyond exact-sequence memorization; it uses a conserved functional motif as a reasoning anchor. The four distractors span entirely different enzyme classes (oxidation, reduction, dehydration), making the motif-based identification sufficiently discriminating."
  },
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H5",
      "H6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA-256 match confirmed in both current and historical records). The entry is annotated as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29). The catalytic activity 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' is listed verbatim as the primary reaction (evidence C5/H5, HAMAP-Rule MF_00083, ECO:0000255). Additionally, two experimental papers (PubMed:27264868, PubMed:29777131; ECO:0000305) confirm catalytic hydrolysis of N-acetylglycyl-tRNA(Gly) (evidence C6/H6), providing experimental corroboration of peptidyl-tRNA ester-bond hydrolysis. Choice C matches the annotated reaction exactly."
  },
  "important_caveats": [
    "The primary EC annotation (3.1.1.29) is assigned by HAMAP-Rule (ECO:0000255), a computational protein-family rule, not by direct experiment on this exact Salmonella Pth. Experimental evidence (ECO:0000305) confirms activity on N-acetylglycyl-tRNA(Gly) specifically, supporting the general peptidyl-tRNA hydrolase function.",
    "The GHGGH motif recognition depends on the model having been trained on protein-family signatures; a model lacking this training would effectively need a database lookup.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work solely from the 194-aa sequence and the four choices.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation is relatively recent; the underlying Pth family is well established in E. coli and other bacteria."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (lipoxygenase, nitroreductase, peptidyl-tRNA hydrolase, dihydroxy-acid dehydratase). The GHGGH motif and overall sequence architecture point specifically to Pth. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA-256 match confirmed in both current and historical records). The entry is annotated as Peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29). The catalytic activity 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)' is listed verbatim as the primary reaction (evidence C5/H5, HAMAP-Rule MF_00083, ECO:0000255). Additionally, two experimental papers (PubMed:27264868, PubMed:29777131; ECO:0000305) confirm catalytic hydrolysis of N-acetylglycyl-tRNA(Gly) (evidence C6/H6), providing experimental corroboration of peptidyl-tRNA ester-bond hydrolysis. Choice C matches the annotated reaction exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H5", "H6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved 'GHGGH' histidine-rich motif (residues ~113-117: 'GGGHGGHNGLKDIIS'), which is a well-known family signature for peptidyl-tRNA hydrolase (Pth). A knowledgeable model can reason: (1) the GHGGH motif is characteristic of the Pth enzyme family; (2) Pth catalyzes hydrolysis of the ester bond linking the amino acid to the 3'-terminal adenosine of tRNA; (3) this corresponds to the reaction 'an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)', i.e., choice C. The other options describe lipoxygenase (A), nitroreductase (B), and dihydroxy-acid dehydratase (D) activities, none of which are associated with the GHGGH signature or the overall 194-aa Pth fold.",
    "missing_item_specific_fact": "None strictly required. The GHGGH motif is a general protein-family signature rather than an item-specific annotation. However, a model without training on protein-family motifs would need to look up the sequence in a database.",
    "reason": "The GHGGH motif is a widely recognized, general protein-family signature for peptidyl-tRNA hydrolase. Identifying this motif and inferring the enzyme class (and hence the hydrolysis of the peptidyl-tRNA ester bond) constitutes a defensible biological inference from the supplied sequence. This goes beyond exact-sequence memorization; it uses a conserved functional motif as a reasoning anchor. The four distractors span entirely different enzyme classes (oxidation, reduction, dehydration), making the motif-based identification sufficiently discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (lipoxygenase, nitroreductase, peptidyl-tRNA hydrolase, dihydroxy-acid dehydratase). The GHGGH motif and overall sequence architecture point specifically to Pth. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The primary EC annotation (3.1.1.29) is assigned by HAMAP-Rule (ECO:0000255), a computational protein-family rule, not by direct experiment on this exact Salmonella Pth. Experimental evidence (ECO:0000305) confirms activity on N-acetylglycyl-tRNA(Gly) specifically, supporting the general peptidyl-tRNA hydrolase function.",
    "The GHGGH motif recognition depends on the model having been trained on protein-family signatures; a model lacking this training would effectively need a database lookup.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work solely from the 194-aa sequence and the four choices.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation is relatively recent; the underlying Pth family is well established in E. coli and other bacteria."
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

**Accession:** `A0A0F6B281` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 42. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
"A0A0F6B281"
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"3.1.1.29"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Peptidyl-tRNA hydrolase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Pth"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.29","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"name":"an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54448"},{"database":"Rhea","id":"RHEA-COMP:10123"},{"database":"Rhea","id":"RHEA-COMP:13883"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:59874"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:138191"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"27264868","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"29777131","source":"PubMed"}],"name":"N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81979"},{"database":"Rhea","id":"RHEA-COMP:9664"},{"database":"Rhea","id":"RHEA-COMP:19766"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:61887"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:232036"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"citation":{"authors":["Cheverton A.M.","Gollan B.","Przydacz M.","Wong C.T.","Mylona A.","Hare S.A.","Helaine S."],"citationCrossReferences":[{"database":"PubMed","id":"27264868"},{"database":"DOI","id":"10.1016/j.molcel.2016.05.002"}],"citationType":"journal article","firstPage":"86","id":"27264868","journal":"Mol. Cell","lastPage":"96","publicationDate":"2016","title":"A Salmonella Toxin Promotes Persister Formation through Acetylation of tRNA.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"citation":{"authors":["Rycroft J.A.","Gollan B.","Grabe G.J.","Hall A.","Cheverton A.M.","Larrouy-Maumus G.","Hare S.A.","Helaine S."],"citationCrossReferences":[{"database":"PubMed","id":"29777131"},{"database":"DOI","id":"10.1038/s41467-018-04472-6"}],"citationType":"journal article","firstPage":"1993","id":"29777131","journal":"Nat. Commun.","lastPage":"1993","publicationDate":"2018","title":"Activity of acetyltransferase toxins involved in Salmonella persister formation during macrophage infection.","volume":"9"},"referenceComments":[{"type":"STRAIN","value":"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
DE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};
DE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};
DE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 23-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
RN   [2]
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;
RX   PubMed=27264868; DOI=10.1016/j.molcel.2016.05.002;
RA   Cheverton A.M., Gollan B., Przydacz M., Wong C.T., Mylona A., Hare S.A.,
RA   Helaine S.;
RT   "A Salmonella Toxin Promotes Persister Formation through Acetylation of
RT   tRNA.";
RL   Mol. Cell 63:86-96(2016).
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
RN   [3]
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023;
RX   PubMed=29777131; DOI=10.1038/s41467-018-04472-6;
RA   Rycroft J.A., Gollan B., Grabe G.J., Hall A., Cheverton A.M.,
RA   Larrouy-Maumus G., Hare S.A., Helaine S.;
RT   "Activity of acetyltransferase toxins involved in Salmonella persister
RT   formation during macrophage infection.";
RL   Nat. Commun. 9:1993-1993(2018).
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 52-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino
CC         acid + a tRNA + H(+); Xref=Rhea:RHEA:54448, Rhea:RHEA-COMP:10123,
CC         Rhea:RHEA-COMP:13883, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:59874, ChEBI:CHEBI:78442, ChEBI:CHEBI:138191;
CC         EC=3.1.1.29; Evidence={ECO:0000255|HAMAP-Rule:MF_00083};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) +
CC         H(+); Xref=Rhea:RHEA:81979, Rhea:RHEA-COMP:9664, Rhea:RHEA-
CC         COMP:19766, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:61887,
CC         ChEBI:CHEBI:78442, ChEBI:CHEBI:232036;
CC         Evidence={ECO:0000305|PubMed:27264868, ECO:0000305|PubMed:29777131};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
