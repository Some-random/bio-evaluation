# GO_biological_process_0030

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — mRNA splicing, via spliceosome

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQSQVPSRAGHYNMTALANALPQANYRQAPWNNGSQMRYNPAGASPNVVGQTQSSPQYNGQPGMGSMPNQGYYMPQQQQQQQQMPQYYGGPMSPSQPQPNMSSRPNVPFYGNQVMSNHQAHPSMGYYYAQVPAYALQGHPPHQAPVDSQSNVVRGPPRKPRQSGHAIWIGNLPSQTDLMSLVHHVCREAQGLESLFLISKSNCAFANFRDEASCLTAQQKLHESKFQSVRLVSRLRKNTVEGASGITAPTGPSATTPQQAVAPEVKEIEQIDSTETQSDNADTDTPTAVGTPDAKGPAVVDAAQKDRFFVLKSLTVEDLDLSVRTGIWATQSHNEEALNSAFKNAENVYLVFSANKSGEYFGYARMVSTINEDPAAAIEFAPKAQSVNEVDLPREIPTEPTKFTPKGRIIDDSARGTIFWEIAREDSSEGVTQEEPAPAVAEQDDTTGGLDGNSENKTWGKPFKLEWLSTTRLPFYRCRGLRNPWNSNREVKIARDGTELEPSVGRRLIGLFNRSHNSPGPRGPMMGMGQMMSPSQQQMPMGYPPPYS

[Multiple Choices]
A. defense response to virus
B. AMP catabolic process
C. dTTP biosynthetic process
D. mRNA splicing, via spliceosome
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

> The sequence matches a UniProt entry annotated with mRNA splicing via the spliceosome (D), but that GO annotation is computationally inferred (IEA:TreeGrafter), not direct experimental evidence of splicing. The cited experimental function concerns m6A-containing mRNA binding and stability, which supports an RNA-related role but does not specifically establish spliceosome-mediated splicing. The matching historical annotation supports the key as an annotation-based answer, with that limitation.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an RNA-related protein, making D more plausible than the virus-response, AMP-catabolism, or dTTP-biosynthesis choices. However, that broad inference does not establish the specific process of spliceosome-mediated mRNA splicing.


**Missing item-specific fact**

> A protein-specific functional characterization or annotation linking this sequence to spliceosomal mRNA splicing is needed to distinguish D from other possible RNA-related roles.


**Reason**

> The input provides only the sequence and choices. Selecting the specific GO process depends on item-specific annotation or experimental knowledge not supplied to the model; recognizing the sequence or recalling its database entry would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only choice supported by the matching GO annotation. The experimental function excerpt does not establish D specifically, but it also does not support another listed option.


### Important caveats

- The sequence match is confirmed for the UniProt entry, but the author’s exact source snapshot is unknown.
- The spliceosome GO annotation is computationally inferred; the cited experimental function describes m6A-containing mRNA binding and stability, not direct spliceosome activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an RNA-related protein, making D more plausible than the virus-response, AMP-catabolism, or dTTP-biosynthesis choices. However, that broad inference does not establish the specific process of spliceosome-mediated mRNA splicing.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional characterization or annotation linking this sequence to spliceosomal mRNA splicing is needed to distinguish D from other possible RNA-related roles.",
    "reason": "The input provides only the sequence and choices. Selecting the specific GO process depends on item-specific annotation or experimental knowledge not supplied to the model; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "case_id": "GO_biological_process_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6",
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated with mRNA splicing via the spliceosome (D), but that GO annotation is computationally inferred (IEA:TreeGrafter), not direct experimental evidence of splicing. The cited experimental function concerns m6A-containing mRNA binding and stability, which supports an RNA-related role but does not specifically establish spliceosome-mediated splicing. The matching historical annotation supports the key as an annotation-based answer, with that limitation."
  },
  "important_caveats": [
    "The sequence match is confirmed for the UniProt entry, but the author’s exact source snapshot is unknown.",
    "The spliceosome GO annotation is computationally inferred; the cited experimental function describes m6A-containing mRNA binding and stability, not direct spliceosome activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only choice supported by the matching GO annotation. The experimental function excerpt does not establish D specifically, but it also does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated with mRNA splicing via the spliceosome (D), but that GO annotation is computationally inferred (IEA:TreeGrafter), not direct experimental evidence of splicing. The cited experimental function concerns m6A-containing mRNA binding and stability, which supports an RNA-related role but does not specifically establish spliceosome-mediated splicing. The matching historical annotation supports the key as an annotation-based answer, with that limitation.",
    "evidence_ids": ["H4", "C6", "H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an RNA-related protein, making D more plausible than the virus-response, AMP-catabolism, or dTTP-biosynthesis choices. However, that broad inference does not establish the specific process of spliceosome-mediated mRNA splicing.",
    "missing_item_specific_fact": "A protein-specific functional characterization or annotation linking this sequence to spliceosomal mRNA splicing is needed to distinguish D from other possible RNA-related roles.",
    "reason": "The input provides only the sequence and choices. Selecting the specific GO process depends on item-specific annotation or experimental knowledge not supplied to the model; recognizing the sequence or recalling its database entry would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only choice supported by the matching GO annotation. The experimental function excerpt does not establish D specifically, but it also does not support another listed option."
  },
  "important_caveats": [
    "The sequence match is confirmed for the UniProt entry, but the author’s exact source snapshot is unknown.",
    "The spliceosome GO annotation is computationally inferred; the cited experimental function describes m6A-containing mRNA binding and stability, not direct spliceosome activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9P4XWM4) annotates this protein with GO:0000398 'mRNA splicing, via spliceosome' (C6, H4) and GO:0000381 'regulation of alternative mRNA splicing, via spliceosome' (C7, H5). However, both annotations carry evidence code IEA:TreeGrafter, meaning they are computational inferences by automated similarity transfer, not experimental findings. The experimental evidence (ECO:0000269, PubMed:39159278) describes the protein as an m6A reader that regulates mRNA stability (C5, H3), not as a direct spliceosomal component. The annotation is present in the database, so the key is technically supported by the annotation record, but the supporting evidence is computational rather than experimental.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features of an RNA-binding protein: low-complexity regions rich in Q, P, S, G residues (typical of intrinsically disordered RNA-binding domains) and no catalytic motifs for nucleotide metabolism (no kinase, phosphatase, or nucleotidyl-transferase signatures) and no antiviral effector domains (no OAS, PKR, or interferon-related motifs). Recognizing the YTH domain (a conserved m6A-reading fold) links the protein to mRNA processing/fate pathways. Among the four options, B (AMP catabolic process) and C (dTTP biosynthetic process) are nucleotide metabolism processes incompatible with an RNA-binding protein lacking any enzymatic catalytic machinery for nucleotide interconversion. A (defense response to virus) has no supporting sequence features. D (mRNA splicing, via spliceosome) is the only option in the mRNA-processing space, making it the best match by elimination and by the general association of YTH-domain proteins with mRNA maturation and fate.


**Missing item-specific fact**

> The specific experimental evidence for this protein describes m6A-dependent mRNA stability regulation, not direct spliceosomal splicing. The assignment to 'mRNA splicing, via spliceosome' specifically (rather than 'mRNA stability' or 'mRNA processing') relies on the IEA:TreeGrafter computational annotation, which is not derivable from the sequence alone without recognizing the exact YTHDF1 ortholog and its database annotation.


**Reason**

> The question is answerable by elimination and general biological reasoning: the sequence is clearly an RNA-binding protein (not a nucleotide-metabolism enzyme or antiviral effector), and D is the only mRNA-processing option. However, the precise mapping to 'splicing via spliceosome' rather than 'mRNA stability' depends on the specific database annotation (IEA), which is a computational inference not derivable from the sequence features alone. The reasoning path is supported but somewhat indirect.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with an RNA-binding protein lacking nucleotide-metabolism or antiviral-effector domains. D is the only mRNA-processing option. While the experimental function (m6A-dependent mRNA stability) is not identical to 'mRNA splicing, via spliceosome,' no better option exists among the four choices, so D is uniquely defensible within the given option set.


### Important caveats

- The GO annotation for 'mRNA splicing, via spliceosome' is IEA:TreeGrafter (automated computational transfer), not experimental. The experimental evidence (PubMed:39159278) describes m6A reading and mRNA stability, not direct spliceosomal activity.
- The protein is a YTH-domain m6A reader (YTHDF1 ortholog in Cryphonectria parasitica). While m6A modifications can influence splicing decisions, this protein's experimentally demonstrated role is mRNA stability regulation, not catalysis of spliceosomal splicing.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.
- The benchmark question asks for the 'primary biological process,' and the IEA annotation may not reflect the most accurate or primary process for this protein based on available experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features of an RNA-binding protein: low-complexity regions rich in Q, P, S, G residues (typical of intrinsically disordered RNA-binding domains) and no catalytic motifs for nucleotide metabolism (no kinase, phosphatase, or nucleotidyl-transferase signatures) and no antiviral effector domains (no OAS, PKR, or interferon-related motifs). Recognizing the YTH domain (a conserved m6A-reading fold) links the protein to mRNA processing/fate pathways. Among the four options, B (AMP catabolic process) and C (dTTP biosynthetic process) are nucleotide metabolism processes incompatible with an RNA-binding protein lacking any enzymatic catalytic machinery for nucleotide interconversion. A (defense response to virus) has no supporting sequence features. D (mRNA splicing, via spliceosome) is the only option in the mRNA-processing space, making it the best match by elimination and by the general association of YTH-domain proteins with mRNA maturation and fate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental evidence for this protein describes m6A-dependent mRNA stability regulation, not direct spliceosomal splicing. The assignment to 'mRNA splicing, via spliceosome' specifically (rather than 'mRNA stability' or 'mRNA processing') relies on the IEA:TreeGrafter computational annotation, which is not derivable from the sequence alone without recognizing the exact YTHDF1 ortholog and its database annotation.",
    "reason": "The question is answerable by elimination and general biological reasoning: the sequence is clearly an RNA-binding protein (not a nucleotide-metabolism enzyme or antiviral effector), and D is the only mRNA-processing option. However, the precise mapping to 'splicing via spliceosome' rather than 'mRNA stability' depends on the specific database annotation (IEA), which is a computational inference not derivable from the sequence features alone. The reasoning path is supported but somewhat indirect."
  },
  "case_id": "GO_biological_process_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "H4",
      "H5",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9P4XWM4) annotates this protein with GO:0000398 'mRNA splicing, via spliceosome' (C6, H4) and GO:0000381 'regulation of alternative mRNA splicing, via spliceosome' (C7, H5). However, both annotations carry evidence code IEA:TreeGrafter, meaning they are computational inferences by automated similarity transfer, not experimental findings. The experimental evidence (ECO:0000269, PubMed:39159278) describes the protein as an m6A reader that regulates mRNA stability (C5, H3), not as a direct spliceosomal component. The annotation is present in the database, so the key is technically supported by the annotation record, but the supporting evidence is computational rather than experimental."
  },
  "important_caveats": [
    "The GO annotation for 'mRNA splicing, via spliceosome' is IEA:TreeGrafter (automated computational transfer), not experimental. The experimental evidence (PubMed:39159278) describes m6A reading and mRNA stability, not direct spliceosomal activity.",
    "The protein is a YTH-domain m6A reader (YTHDF1 ortholog in Cryphonectria parasitica). While m6A modifications can influence splicing decisions, this protein's experimentally demonstrated role is mRNA stability regulation, not catalysis of spliceosomal splicing.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.",
    "The benchmark question asks for the 'primary biological process,' and the IEA annotation may not reflect the most accurate or primary process for this protein based on available experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with an RNA-binding protein lacking nucleotide-metabolism or antiviral-effector domains. D is the only mRNA-processing option. While the experimental function (m6A-dependent mRNA stability) is not identical to 'mRNA splicing, via spliceosome,' no better option exists among the four choices, so D is uniquely defensible within the given option set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9P4XWM4) annotates this protein with GO:0000398 'mRNA splicing, via spliceosome' (C6, H4) and GO:0000381 'regulation of alternative mRNA splicing, via spliceosome' (C7, H5). However, both annotations carry evidence code IEA:TreeGrafter, meaning they are computational inferences by automated similarity transfer, not experimental findings. The experimental evidence (ECO:0000269, PubMed:39159278) describes the protein as an m6A reader that regulates mRNA stability (C5, H3), not as a direct spliceosomal component. The annotation is present in the database, so the key is technically supported by the annotation record, but the supporting evidence is computational rather than experimental.",
    "evidence_ids": ["C6", "C7", "H4", "H5", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features of an RNA-binding protein: low-complexity regions rich in Q, P, S, G residues (typical of intrinsically disordered RNA-binding domains) and no catalytic motifs for nucleotide metabolism (no kinase, phosphatase, or nucleotidyl-transferase signatures) and no antiviral effector domains (no OAS, PKR, or interferon-related motifs). Recognizing the YTH domain (a conserved m6A-reading fold) links the protein to mRNA processing/fate pathways. Among the four options, B (AMP catabolic process) and C (dTTP biosynthetic process) are nucleotide metabolism processes incompatible with an RNA-binding protein lacking any enzymatic catalytic machinery for nucleotide interconversion. A (defense response to virus) has no supporting sequence features. D (mRNA splicing, via spliceosome) is the only option in the mRNA-processing space, making it the best match by elimination and by the general association of YTH-domain proteins with mRNA maturation and fate.",
    "missing_item_specific_fact": "The specific experimental evidence for this protein describes m6A-dependent mRNA stability regulation, not direct spliceosomal splicing. The assignment to 'mRNA splicing, via spliceosome' specifically (rather than 'mRNA stability' or 'mRNA processing') relies on the IEA:TreeGrafter computational annotation, which is not derivable from the sequence alone without recognizing the exact YTHDF1 ortholog and its database annotation.",
    "reason": "The question is answerable by elimination and general biological reasoning: the sequence is clearly an RNA-binding protein (not a nucleotide-metabolism enzyme or antiviral effector), and D is the only mRNA-processing option. However, the precise mapping to 'splicing via spliceosome' rather than 'mRNA stability' depends on the specific database annotation (IEA), which is a computational inference not derivable from the sequence features alone. The reasoning path is supported but somewhat indirect."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with an RNA-binding protein lacking nucleotide-metabolism or antiviral-effector domains. D is the only mRNA-processing option. While the experimental function (m6A-dependent mRNA stability) is not identical to 'mRNA splicing, via spliceosome,' no better option exists among the four choices, so D is uniquely defensible within the given option set."
  },
  "important_caveats": [
    "The GO annotation for 'mRNA splicing, via spliceosome' is IEA:TreeGrafter (automated computational transfer), not experimental. The experimental evidence (PubMed:39159278) describes m6A reading and mRNA stability, not direct spliceosomal activity.",
    "The protein is a YTH-domain m6A reader (YTHDF1 ortholog in Cryphonectria parasitica). While m6A modifications can influence splicing decisions, this protein's experimentally demonstrated role is mRNA stability regulation, not catalysis of spliceosomal splicing.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.",
    "The benchmark question asks for the 'primary biological process,' and the IEA annotation may not reflect the most accurate or primary process for this protein based on available experimental data."
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

**Accession:** `A0A9P4XWM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 9. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.400481+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"}],"value":"Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability (PubMed:39159278). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (PubMed:39159278). Directly interacts with the acid phosphatase APHA mRNA to increase its stability (PubMed:39159278)"}]}
```

Source SHA-256: `db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.400481+00:00.  

```json
{"database":"GO","id":"GO:0000398","properties":[{"key":"GoTerm","value":"P:mRNA splicing, via spliceosome"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.400481+00:00.  

```json
{"database":"GO","id":"GO:0000381","properties":[{"key":"GoTerm","value":"P:regulation of alternative mRNA splicing, via spliceosome"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)  
**Locator:** `lines 33-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-02T04:26:18.939090+00:00.  

```text
CC   -!- FUNCTION: Specifically recognizes and binds N6-methyladenosine (m6A)-
CC       containing mRNAs, and regulates their stability (PubMed:39159278). M6A
CC       is a modification present at internal sites of mRNAs and some non-
CC       coding RNAs and plays a role in mRNA stability and processing
CC       (PubMed:39159278). Directly interacts with the acid phosphatase APHA
CC       mRNA to increase its stability (PubMed:39159278).
CC       {ECO:0000269|PubMed:39159278}.
```

Source SHA-256: `c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-02T04:26:18.939090+00:00.  

```text
DR   GO; GO:0000398; P:mRNA splicing, via spliceosome; IEA:TreeGrafter.
```

Source SHA-256: `c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)  
**Locator:** `lines 57-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 1.  
**Retrieved:** 2026-11-02T04:26:18.939090+00:00.  

```text
DR   GO; GO:0000381; P:regulation of alternative mRNA splicing, via spliceosome; IEA:TreeGrafter.
```

Source SHA-256: `c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
