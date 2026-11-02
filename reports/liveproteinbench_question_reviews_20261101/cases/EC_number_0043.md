# EC_number_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVKVRFDKEVRDYAKGEKVKDSILKLTETALAQALENFHRRMIVIEGDTLRKAELAGILAGASARVLSGILEELMKKRLRDESEDKIEVLYATDALGEETFGRKRYEAFRKHFDVLAGSNVEVKAVTFKHTRDILGRTYDLLILDMSYDYSPNDLGRIIETVRGGGLIFILAHPFEKWKNMWTGFHKSLVTPPYTIDDVKKRFNRRLIRKFTEHDGIYIITEGGKARKKPKRSKSQARIKARKGVPIPEETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKKRTRIVVTAPELENVQALFRFAKRALERLGFKPYVVEERGLIKELYARKIGLRYYPPADGYKKSADLYILDEAAGIHVPILHKYLNKERVVYSSTIHGYEGAGRGFSVKFLKRAREKREFKELHMDEPIRYAENDPIERWLFDVLLLDAEPVELTEEDFELIEKKEVYLEEPDLDDWFENDREDLRNFVGIYILAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAIQIAKEGGIPKKVIEKMAKGYKPRGNIIPDMMVKHHYLKEFAKLKGYRIVRIATHPDAMDRGLGSKALELLEKEAREKGLDWIGSGFGASEELVRFWVRNGFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKKANDEFRIRLTEWLGDTHRELEPEIARWLFETPFGEAVDYPVHLTEIQKKRLDAFTGKVLTYDTVVDAVKPIVKLYFLDGWMKPYLDERQIRLLIYRVLQAHSWEETAKLIDRTETFTMIEVRDIIRGLWYYYKRLLKA

[Multiple Choices]
A. 2.3.1.319
B. 3.2.1.55
C. 5.3.99.13
D. 2.3.1.193
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

> The supplied sequence exactly matches the UniProt entry annotated as TmcA with EC 2.3.1.193. That EC assignment and the specific tRNA(Met) reaction are supported by a HAMAP computational rule, not direct experimental evidence in the cited annotation. A cited paper supports broader RNA acetylation activity, but the supplied excerpts do not establish the exact tRNA(Met) reaction experimentally.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a structured enzyme, but no supplied context or broadly interpretable sequence feature distinguishes this specific RNA acetyltransferase reaction and EC number from the listed alternatives.


**Missing item-specific fact**

> The protein-specific TmcA functional assignment and the mapping of its catalytic activity to EC 2.3.1.193 are needed; these are absent from the question input.


**Reason**

> Choosing the exact four-part EC number depends on an item-specific functional annotation or equivalent protein-specific knowledge. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports D; the choices represent distinct EC numbers, and the available evidence does not support another listed option for this protein.


### Important caveats

- The sequence match establishes applicability of the database annotation to the supplied sequence, but the EC assignment is computationally annotated via HAMAP.
- The cited publication evidence supports RNA acetylation more broadly; the exact tRNA(Met) reaction in the excerpts is attributed to the computational rule.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a structured enzyme, but no supplied context or broadly interpretable sequence feature distinguishes this specific RNA acetyltransferase reaction and EC number from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific TmcA functional assignment and the mapping of its catalytic activity to EC 2.3.1.193 are needed; these are absent from the question input.",
    "reason": "Choosing the exact four-part EC number depends on an item-specific functional annotation or equivalent protein-specific knowledge. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided information."
  },
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as TmcA with EC 2.3.1.193. That EC assignment and the specific tRNA(Met) reaction are supported by a HAMAP computational rule, not direct experimental evidence in the cited annotation. A cited paper supports broader RNA acetylation activity, but the supplied excerpts do not establish the exact tRNA(Met) reaction experimentally."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the database annotation to the supplied sequence, but the EC assignment is computationally annotated via HAMAP.",
    "The cited publication evidence supports RNA acetylation more broadly; the exact tRNA(Met) reaction in the excerpts is attributed to the computational rule.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports D; the choices represent distinct EC numbers, and the available evidence does not support another listed option for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as TmcA with EC 2.3.1.193. That EC assignment and the specific tRNA(Met) reaction are supported by a HAMAP computational rule, not direct experimental evidence in the cited annotation. A cited paper supports broader RNA acetylation activity, but the supplied excerpts do not establish the exact tRNA(Met) reaction experimentally.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a structured enzyme, but no supplied context or broadly interpretable sequence feature distinguishes this specific RNA acetyltransferase reaction and EC number from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific TmcA functional assignment and the mapping of its catalytic activity to EC 2.3.1.193 are needed; these are absent from the question input.",
    "reason": "Choosing the exact four-part EC number depends on an item-specific functional annotation or equivalent protein-specific knowledge. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports D; the choices represent distinct EC numbers, and the available evidence does not support another listed option for this protein."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the database annotation to the supplied sequence, but the EC assignment is computationally annotated via HAMAP.",
    "The cited publication evidence supports RNA acetylation more broadly; the exact tRNA(Met) reaction in the excerpts is attributed to the computational rule.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt B7R4L8 (Thermococcus sp. AM4, TmcA). UniProt annotates it as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255, computational/curatorial), and the broader catalytic activities (cytidine acetylation in RNA/tRNA/mRNA) are additionally supported by experimental evidence (ECO:0000305|PubMed:32555463, Nature 2020). The primary EC assignment is curatorial but corroborated by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One might broadly infer transferase activity (EC class 2) from sequence features suggestive of acyl-CoA binding, and the archaeal tRNA-modification context could hint at a modification enzyme. However, distinguishing EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase requiring both acetyl-CoA and ATP) from EC 2.3.1.319 (a different specific acyltransferase) within the same 3-digit subclass cannot be achieved through general sequence reasoning. The specific substrate (cytidine(34) in elongator tRNA), the dual cofactor requirement (acetyl-CoA + ATP), and the unique reaction mechanism are protein-specific facts encoded in HAMAP rule MF_01886.


**Missing item-specific fact**

> The identity of this protein as TmcA and its specific catalytic mechanism (ATP-dependent cytidine(34) acetylation in tRNA) as defined by HAMAP rule MF_01886, or equivalently, the experimental characterization from Sas-Chen et al. (Nature 2020, PMID 32555463). Without recognizing the protein or knowing the specific substrate/reaction, the 4-digit EC number cannot be resolved from sequence alone.


**Reason**

> The question requires selecting the exact 4-digit EC number. While the first digit (2, transferase) might be loosely inferred, distinguishing 2.3.1.193 from 2.3.1.319 (both acyltransferases in the same 3-digit class) demands knowledge of the specific substrate and reaction mechanism unique to TmcA. This is an item-specific annotation fact, not a generalizable biological principle derivable from sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase) are in entirely different EC classes and are clearly wrong. Option A (2.3.1.319) is in the same 3-digit class as D but represents a different specific reaction; without item-specific knowledge, a model might confuse A and D, but the annotation unambiguously assigns D.


### Important caveats

- The primary EC annotation (2.3.1.193) is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial method, not direct experimental determination of the specific tRNA(Met) cytidine(34) acetylation reaction for this exact protein.
- Experimental evidence (PubMed 32555463) supports the broader catalytic activity (cytidine acetylation in RNA) but was obtained in a related context; the specific assignment to position 34 of elongator tRNA(Met) in Thermococcus AM4 relies on the HAMAP rule.
- The sequence is 811 aa and matched exactly to the UniProt entry, confirming identity.
- The question tests recall of a specific enzyme's EC number rather than generalizable enzyme-class inference from sequence motifs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One might broadly infer transferase activity (EC class 2) from sequence features suggestive of acyl-CoA binding, and the archaeal tRNA-modification context could hint at a modification enzyme. However, distinguishing EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase requiring both acetyl-CoA and ATP) from EC 2.3.1.319 (a different specific acyltransferase) within the same 3-digit subclass cannot be achieved through general sequence reasoning. The specific substrate (cytidine(34) in elongator tRNA), the dual cofactor requirement (acetyl-CoA + ATP), and the unique reaction mechanism are protein-specific facts encoded in HAMAP rule MF_01886.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this protein as TmcA and its specific catalytic mechanism (ATP-dependent cytidine(34) acetylation in tRNA) as defined by HAMAP rule MF_01886, or equivalently, the experimental characterization from Sas-Chen et al. (Nature 2020, PMID 32555463). Without recognizing the protein or knowing the specific substrate/reaction, the 4-digit EC number cannot be resolved from sequence alone.",
    "reason": "The question requires selecting the exact 4-digit EC number. While the first digit (2, transferase) might be loosely inferred, distinguishing 2.3.1.193 from 2.3.1.319 (both acyltransferases in the same 3-digit class) demands knowledge of the specific substrate and reaction mechanism unique to TmcA. This is an item-specific annotation fact, not a generalizable biological principle derivable from sequence features."
  },
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt B7R4L8 (Thermococcus sp. AM4, TmcA). UniProt annotates it as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255, computational/curatorial), and the broader catalytic activities (cytidine acetylation in RNA/tRNA/mRNA) are additionally supported by experimental evidence (ECO:0000305|PubMed:32555463, Nature 2020). The primary EC assignment is curatorial but corroborated by experimental data."
  },
  "important_caveats": [
    "The primary EC annotation (2.3.1.193) is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial method, not direct experimental determination of the specific tRNA(Met) cytidine(34) acetylation reaction for this exact protein.",
    "Experimental evidence (PubMed 32555463) supports the broader catalytic activity (cytidine acetylation in RNA) but was obtained in a related context; the specific assignment to position 34 of elongator tRNA(Met) in Thermococcus AM4 relies on the HAMAP rule.",
    "The sequence is 811 aa and matched exactly to the UniProt entry, confirming identity.",
    "The question tests recall of a specific enzyme's EC number rather than generalizable enzyme-class inference from sequence motifs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase) are in entirely different EC classes and are clearly wrong. Option A (2.3.1.319) is in the same 3-digit class as D but represents a different specific reaction; without item-specific knowledge, a model might confuse A and D, but the annotation unambiguously assigns D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt B7R4L8 (Thermococcus sp. AM4, TmcA). UniProt annotates it as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) via HAMAP-Rule MF_01886 (ECO:0000255, computational/curatorial), and the broader catalytic activities (cytidine acetylation in RNA/tRNA/mRNA) are additionally supported by experimental evidence (ECO:0000305|PubMed:32555463, Nature 2020). The primary EC assignment is curatorial but corroborated by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C9", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One might broadly infer transferase activity (EC class 2) from sequence features suggestive of acyl-CoA binding, and the archaeal tRNA-modification context could hint at a modification enzyme. However, distinguishing EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase requiring both acetyl-CoA and ATP) from EC 2.3.1.319 (a different specific acyltransferase) within the same 3-digit subclass cannot be achieved through general sequence reasoning. The specific substrate (cytidine(34) in elongator tRNA), the dual cofactor requirement (acetyl-CoA + ATP), and the unique reaction mechanism are protein-specific facts encoded in HAMAP rule MF_01886.",
    "missing_item_specific_fact": "The identity of this protein as TmcA and its specific catalytic mechanism (ATP-dependent cytidine(34) acetylation in tRNA) as defined by HAMAP rule MF_01886, or equivalently, the experimental characterization from Sas-Chen et al. (Nature 2020, PMID 32555463). Without recognizing the protein or knowing the specific substrate/reaction, the 4-digit EC number cannot be resolved from sequence alone.",
    "reason": "The question requires selecting the exact 4-digit EC number. While the first digit (2, transferase) might be loosely inferred, distinguishing 2.3.1.193 from 2.3.1.319 (both acyltransferases in the same 3-digit class) demands knowledge of the specific substrate and reaction mechanism unique to TmcA. This is an item-specific annotation fact, not a generalizable biological principle derivable from sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors B (3.2.1.55, glycosidase) and C (5.3.99.13, isomerase) are in entirely different EC classes and are clearly wrong. Option A (2.3.1.319) is in the same 3-digit class as D but represents a different specific reaction; without item-specific knowledge, a model might confuse A and D, but the annotation unambiguously assigns D."
  },
  "important_caveats": [
    "The primary EC annotation (2.3.1.193) is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial method, not direct experimental determination of the specific tRNA(Met) cytidine(34) acetylation reaction for this exact protein.",
    "Experimental evidence (PubMed 32555463) supports the broader catalytic activity (cytidine acetylation in RNA) but was obtained in a related context; the specific assignment to position 34 of elongator tRNA(Met) in Thermococcus AM4 relies on the HAMAP rule.",
    "The sequence is 811 aa and matched exactly to the UniProt entry, confirming identity.",
    "The question tests recall of a specific enzyme's EC number rather than generalizable enzyme-class inference from sequence motifs."
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

**Accession:** `B7R4L8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 76. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
"B7R4L8"
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA"}}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82211"},{"database":"Rhea","id":"RHEA-COMP:15704"},{"database":"Rhea","id":"RHEA-COMP:19834"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:53876"},{"database":"Rhea","id":"RHEA-COMP:13670"},{"database":"Rhea","id":"RHEA-COMP:13671"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"citation":{"authors":["Sas-Chen A.","Thomas J.M.","Matzov D.","Taoka M.","Nance K.D.","Nir R.","Bryson K.M.","Shachar R.","Liman G.L.S.","Burkhart B.W.","Gamage S.T.","Nobe Y.","Briney C.A.","Levy M.J.","Fuchs R.T.","Robb G.B.","Hartmann J.","Sharma S.","Lin Q.","Florens L.","Washburn M.P.","Isobe T.","Santangelo T.J.","Shalev-Benami M.","Meier J.L.","Schwartz S."],"citationCrossReferences":[{"database":"PubMed","id":"32555463"},{"database":"DOI","id":"10.1038/s41586-020-2418-2"}],"citationType":"journal article","firstPage":"638","id":"32555463","journal":"Nature","lastPage":"643","publicationDate":"2020","title":"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.","volume":"583"},"referenceComments":[{"type":"STRAIN","value":"AM4"}],"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 44-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 61-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 70-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
