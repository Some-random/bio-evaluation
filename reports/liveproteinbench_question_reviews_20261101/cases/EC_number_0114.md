# EC_number_0114

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.183

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. 3.2.1.183
B. 3.2.1.8
C. 3.6.1.5
D. 4.2.1.9
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

> The supplied sequence exactly matches the reviewed UniProt sequence, whose archived record assigns EC 3.2.1.183 and cites experimental evidence from PubMed 38382015 for the catalytic activity. This supports choice A, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices distinguish specific catalytic activities, including two glycoside-hydrolase EC numbers; the sequence alone provides no clear, general argument establishing this protein's particular substrate and reaction.


**Missing item-specific fact**

> The protein's experimentally characterized catalytic activity or a reliable protein-specific functional annotation identifying EC 3.2.1.183.


**Reason**

> The key is supported by reviewer-only, sequence-matched annotation and cited experimental evidence, but that information was absent from the question. Exact EC assignment depends on protein-specific function, not merely recognizing broad sequence or enzyme-class tendencies.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited activity supports A; the other options specify different EC activities. The issue is missing evidence in the prompt, rather than evidence that multiple options are correct.


### Important caveats

- The exact author data-source snapshot is unknown.
- The UniProt annotation and sequence match are reviewer-only evidence and were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices distinguish specific catalytic activities, including two glycoside-hydrolase EC numbers; the sequence alone provides no clear, general argument establishing this protein's particular substrate and reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized catalytic activity or a reliable protein-specific functional annotation identifying EC 3.2.1.183.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation and cited experimental evidence, but that information was absent from the question. Exact EC assignment depends on protein-specific function, not merely recognizing broad sequence or enzyme-class tendencies."
  },
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence, whose archived record assigns EC 3.2.1.183 and cites experimental evidence from PubMed 38382015 for the catalytic activity. This supports choice A, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The exact author data-source snapshot is unknown.",
    "The UniProt annotation and sequence match are reviewer-only evidence and were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited activity supports A; the other options specify different EC activities. The issue is missing evidence in the prompt, rather than evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence, whose archived record assigns EC 3.2.1.183 and cites experimental evidence from PubMed 38382015 for the catalytic activity. This supports choice A, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices distinguish specific catalytic activities, including two glycoside-hydrolase EC numbers; the sequence alone provides no clear, general argument establishing this protein's particular substrate and reaction.",
    "missing_item_specific_fact": "The protein's experimentally characterized catalytic activity or a reliable protein-specific functional annotation identifying EC 3.2.1.183.",
    "reason": "The key is supported by reviewer-only, sequence-matched annotation and cited experimental evidence, but that information was absent from the question. Exact EC assignment depends on protein-specific function, not merely recognizing broad sequence or enzyme-class tendencies."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited activity supports A; the other options specify different EC activities. The issue is missing evidence in the prompt, rather than evidence that multiple options are correct."
  },
  "important_caveats": [
    "The exact author data-source snapshot is unknown.",
    "The UniProt annotation and sequence match are reviewer-only evidence and were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated with EC 3.2.1.183 (UDP-N-acetylglucosamine 2-epimerase, hydrolyzing variant) with evidence code ECO:0000269 (experimental) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic reaction is UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+). The benchmark sequence matches the UniProt entry exactly (SHA256 confirmed, 373 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable GNE-family (UDP-GlcNAc 2-epimerase/N-acetylmannosamine kinase) motifs including 'NNDLGFELIL', 'GDRIEPL', and 'GSPDLELL' nucleotide-binding patterns, indicating a UDP-sugar–related glycosidase/hydrolase (EC 3.2.1.x). This eliminates 3.6.1.5 (ADP-ribosyl cyclase, EC class 3.6) and 4.2.1.9 (enolase, EC class 4.2). Between the two EC 3.2.1.x options, the nucleotide-sugar-binding motifs (GDRIEPL, GSPDLELL) are inconsistent with α-glucosidase (3.2.1.8), which hydrolyzes simple α-glucosides without nucleotide-sugar cofactors. This leaves 3.2.1.183 as the only UDP-GlcNAc–related glycosidase among the choices.


**Missing item-specific fact**

> The precise EC number 3.2.1.183 was experimentally characterized only in 2024 and is extremely niche; distinguishing it from the classical GNE-type epimerase (EC 3.2.1.159) purely from sequence is essentially impossible. However, since 3.2.1.159 is not among the options, the elimination logic still converges on A.


**Reason**

> A knowledgeable model can identify GNE-family fold motifs to infer UDP-GlcNAc glycosidase activity, eliminate the clearly unrelated EC classes (3.6 and 4.2), and use nucleotide-sugar-binding features to rule out α-glucosidase (3.2.1.8). The final step to 3.2.1.183 is aided by it being the sole UDP-GlcNAc-related option, though the precise EC number itself is too recent and niche for general memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (α-glucosidase), C (ADP-ribosyl cyclase), and D (enolase) are clearly inconsistent with the GNE-like sequence architecture and nucleotide-sugar-binding motifs. Only option A is compatible with the inferred UDP-GlcNAc glycosidase function.


### Important caveats

- EC 3.2.1.183 was experimentally characterized in 2024 (PubMed:38382015) and is extremely niche; most trained models would not have memorized this EC number.
- The sequence resembles GNE-family enzymes, which could also suggest EC 3.2.1.159 (classical UDP-GlcNAc 2-epimerase), but that EC number is not among the options.
- The reasoning path relies on recognizing GNE-family motifs and knowing that α-glucosidase does not use nucleotide sugars, which is general but non-trivial biochemical knowledge.
- The UniProt annotation is based on experimental evidence (ECO:0000269), not purely computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GNE-family (UDP-GlcNAc 2-epimerase/N-acetylmannosamine kinase) motifs including 'NNDLGFELIL', 'GDRIEPL', and 'GSPDLELL' nucleotide-binding patterns, indicating a UDP-sugar–related glycosidase/hydrolase (EC 3.2.1.x). This eliminates 3.6.1.5 (ADP-ribosyl cyclase, EC class 3.6) and 4.2.1.9 (enolase, EC class 4.2). Between the two EC 3.2.1.x options, the nucleotide-sugar-binding motifs (GDRIEPL, GSPDLELL) are inconsistent with α-glucosidase (3.2.1.8), which hydrolyzes simple α-glucosides without nucleotide-sugar cofactors. This leaves 3.2.1.183 as the only UDP-GlcNAc–related glycosidase among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise EC number 3.2.1.183 was experimentally characterized only in 2024 and is extremely niche; distinguishing it from the classical GNE-type epimerase (EC 3.2.1.159) purely from sequence is essentially impossible. However, since 3.2.1.159 is not among the options, the elimination logic still converges on A.",
    "reason": "A knowledgeable model can identify GNE-family fold motifs to infer UDP-GlcNAc glycosidase activity, eliminate the clearly unrelated EC classes (3.6 and 4.2), and use nucleotide-sugar-binding features to rule out α-glucosidase (3.2.1.8). The final step to 3.2.1.183 is aided by it being the sole UDP-GlcNAc-related option, though the precise EC number itself is too recent and niche for general memorization."
  },
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated with EC 3.2.1.183 (UDP-N-acetylglucosamine 2-epimerase, hydrolyzing variant) with evidence code ECO:0000269 (experimental) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic reaction is UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+). The benchmark sequence matches the UniProt entry exactly (SHA256 confirmed, 373 aa)."
  },
  "important_caveats": [
    "EC 3.2.1.183 was experimentally characterized in 2024 (PubMed:38382015) and is extremely niche; most trained models would not have memorized this EC number.",
    "The sequence resembles GNE-family enzymes, which could also suggest EC 3.2.1.159 (classical UDP-GlcNAc 2-epimerase), but that EC number is not among the options.",
    "The reasoning path relies on recognizing GNE-family motifs and knowing that α-glucosidase does not use nucleotide sugars, which is general but non-trivial biochemical knowledge.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269), not purely computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (α-glucosidase), C (ADP-ribosyl cyclase), and D (enolase) are clearly inconsistent with the GNE-like sequence architecture and nucleotide-sugar-binding motifs. Only option A is compatible with the inferred UDP-GlcNAc glycosidase function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated with EC 3.2.1.183 (UDP-N-acetylglucosamine 2-epimerase, hydrolyzing variant) with evidence code ECO:0000269 (experimental) from PubMed:38382015 (Ghosh & Raushel, Biochemistry 2024). The catalytic reaction is UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+). The benchmark sequence matches the UniProt entry exactly (SHA256 confirmed, 373 aa).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable GNE-family (UDP-GlcNAc 2-epimerase/N-acetylmannosamine kinase) motifs including 'NNDLGFELIL', 'GDRIEPL', and 'GSPDLELL' nucleotide-binding patterns, indicating a UDP-sugar–related glycosidase/hydrolase (EC 3.2.1.x). This eliminates 3.6.1.5 (ADP-ribosyl cyclase, EC class 3.6) and 4.2.1.9 (enolase, EC class 4.2). Between the two EC 3.2.1.x options, the nucleotide-sugar-binding motifs (GDRIEPL, GSPDLELL) are inconsistent with α-glucosidase (3.2.1.8), which hydrolyzes simple α-glucosides without nucleotide-sugar cofactors. This leaves 3.2.1.183 as the only UDP-GlcNAc–related glycosidase among the choices.",
    "missing_item_specific_fact": "The precise EC number 3.2.1.183 was experimentally characterized only in 2024 and is extremely niche; distinguishing it from the classical GNE-type epimerase (EC 3.2.1.159) purely from sequence is essentially impossible. However, since 3.2.1.159 is not among the options, the elimination logic still converges on A.",
    "reason": "A knowledgeable model can identify GNE-family fold motifs to infer UDP-GlcNAc glycosidase activity, eliminate the clearly unrelated EC classes (3.6 and 4.2), and use nucleotide-sugar-binding features to rule out α-glucosidase (3.2.1.8). The final step to 3.2.1.183 is aided by it being the sole UDP-GlcNAc-related option, though the precise EC number itself is too recent and niche for general memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (α-glucosidase), C (ADP-ribosyl cyclase), and D (enolase) are clearly inconsistent with the GNE-like sequence architecture and nucleotide-sugar-binding motifs. Only option A is compatible with the inferred UDP-GlcNAc glycosidase function."
  },
  "important_caveats": [
    "EC 3.2.1.183 was experimentally characterized in 2024 (PubMed:38382015) and is extremely niche; most trained models would not have memorized this EC number.",
    "The sequence resembles GNE-family enzymes, which could also suggest EC 3.2.1.159 (classical UDP-GlcNAc 2-epimerase), but that EC number is not among the options.",
    "The reasoning path relies on recognizing GNE-family motifs and knowing that α-glucosidase does not use nucleotide sugars, which is general but non-trivial biochemical knowledge.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269), not purely computational inference."
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

**Accession:** `P0DY05` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
"P0DY05"
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Hydrolyzing UDP-GlcNAc 2-epimerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"3.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetylglucosamine 2-epimerase"}}}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:30684"}}],"reaction":{"ecNumber":"3.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:30683"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17122"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:58223"}]}}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:02.588931+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=81116 / NCTC 11828;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)  
**Locator:** `lines 40-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:30:04.730217+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-
CC         mannosamine + UDP + H(+); Xref=Rhea:RHEA:30683, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17122, ChEBI:CHEBI:57705,
CC         ChEBI:CHEBI:58223; EC=3.2.1.183;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30684;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
