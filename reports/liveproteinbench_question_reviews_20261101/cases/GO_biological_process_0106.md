# GO_biological_process_0106

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — symbiont-mediated perturbation of host defenses

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTILAVIFFGILAFAFADYPSIENCTHPPAMANFNQKKFLEGKWYVTKAKHGSNSTVCREYRAKTKGNDQILVGDGYYSFNGGTFYFTVRCKRLPNKEVQKPLQFTCTQKSTDDPSKMFKFQLEVTILDTDYANYAVMYRCVQFPEQLGSHFEDNTLLLHRNPDQLVDENQVERKLNLSFDSFRSREDVVDGCPKLPSKKKNKAS

[Multiple Choices]
A. carbohydrate metabolic process
B. negative regulation of chondrocyte differentiation
C. symbiont-mediated perturbation of host defenses
D. positive regulation of interleukin-8 production
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

> The supplied sequence matches the annotated Triatoma infestans protein triafestin-2. Its experimentally supported inhibition of the host kallikrein-kinin system and intrinsic coagulation pathway supports perturbation of host defenses. The exact GO annotation for option C is computationally assigned by InterPro, rather than itself being experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, which makes a host-interacting role plausible, but does not establish that it perturbs host defenses or distinguish that specific role from other host effects.


**Missing item-specific fact**

> The protein-specific identification as triafestin-2 from Triatoma infestans saliva, and evidence that it suppresses host kallikrein-kinin activation and coagulation.


**Reason**

> Those identifying and functional facts are absent from the sequence-and-choices input. Recognizing a secreted protein is not enough to select the particular GO process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific evidence supports option C; the other options are not supported by the supplied functional evidence.


### Important caveats

- The sequence match and accession identification come from reviewer-only evidence, not the evaluated input.
- The current UniProt record's exact GO annotation for C is IEA:InterPro; the supporting experimental evidence concerns the protein's host kallikrein-kinin and coagulation effects.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, which makes a host-interacting role plausible, but does not establish that it perturbs host defenses or distinguish that specific role from other host effects.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as triafestin-2 from Triatoma infestans saliva, and evidence that it suppresses host kallikrein-kinin activation and coagulation.",
    "reason": "Those identifying and functional facts are absent from the sequence-and-choices input. Recognizing a secreted protein is not enough to select the particular GO process."
  },
  "case_id": "GO_biological_process_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated Triatoma infestans protein triafestin-2. Its experimentally supported inhibition of the host kallikrein-kinin system and intrinsic coagulation pathway supports perturbation of host defenses. The exact GO annotation for option C is computationally assigned by InterPro, rather than itself being experimental evidence."
  },
  "important_caveats": [
    "The sequence match and accession identification come from reviewer-only evidence, not the evaluated input.",
    "The current UniProt record's exact GO annotation for C is IEA:InterPro; the supporting experimental evidence concerns the protein's host kallikrein-kinin and coagulation effects."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports option C; the other options are not supported by the supplied functional evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated Triatoma infestans protein triafestin-2. Its experimentally supported inhibition of the host kallikrein-kinin system and intrinsic coagulation pathway supports perturbation of host defenses. The exact GO annotation for option C is computationally assigned by InterPro, rather than itself being experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H3", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, which makes a host-interacting role plausible, but does not establish that it perturbs host defenses or distinguish that specific role from other host effects.",
    "missing_item_specific_fact": "The protein-specific identification as triafestin-2 from Triatoma infestans saliva, and evidence that it suppresses host kallikrein-kinin activation and coagulation.",
    "reason": "Those identifying and functional facts are absent from the sequence-and-choices input. Recognizing a secreted protein is not enough to select the particular GO process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports option C; the other options are not supported by the supplied functional evidence."
  },
  "important_caveats": [
    "The sequence match and accession identification come from reviewer-only evidence, not the evaluated input.",
    "The current UniProt record's exact GO annotation for C is IEA:InterPro; the supporting experimental evidence concerns the protein's host kallikrein-kinin and coagulation effects."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A7BJ46 (Triafestin-2 from Triatoma infestans) carries GO:0030682 'symbiont-mediated perturbation of host defenses' as an annotation (evidence_id C7, H5). However, this annotation is IEA:InterPro (computational inference from domain), not experimentally verified. The experimental (IDA) annotations are GO:0140184 'venom-mediated suppression of blood coagulation, intrinsic pathway' and GO:0140106 'hematophagy'. The protein's experimentally characterized function (suppressing host kallikrein-kinin system and intrinsic coagulation) is consistent with the broader concept of perturbing host defenses, and the annotation exists in the database. Among the four provided choices, C is the most appropriate, though the 'symbiont' framing is somewhat unusual for a macro-organism parasite and derives from InterPro domain-based inference rather than direct experimental assignment.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a signal peptide (suggesting secretion) and a Kunitz-type serine protease inhibitor domain. One could reason that a secreted protease inhibitor is unlikely to be involved in carbohydrate metabolism (A) or chondrocyte differentiation (B), and its anti-proteolytic nature argues against positive regulation of IL-8 (D). However, the critical 'symbiont-mediated' qualifier in option C requires knowing the organism is a blood-sucking parasite (Triatoma infestans) and that the protein targets host defense pathways (kallikrein-kinin, coagulation). This ecological/organism-specific context is not derivable from the amino acid sequence alone.


**Missing item-specific fact**

> The identity of the source organism (Triatoma infestans, a hematophagous insect) and the specific experimental finding that this salivary protein inhibits host factor XII, prekallikrein, and kallikrein-kinin system activation. Without knowing the protein is from a blood-sucking parasite targeting host coagulation/inflammation pathways, the 'symbiont-mediated perturbation of host defenses' GO term cannot be assigned from sequence features alone.


**Reason**

> While general reasoning about Kunitz domains and secreted protease inhibitors can weakly eliminate A, B, and D, the specific GO term 'symbiont-mediated perturbation of host defenses' requires organism-level ecological knowledge (parasite/host relationship) and knowledge of the specific host defense pathway targeted. The sequence provides no information about the organism being a blood-sucking insect or the protein being a salivary secretion. The correct answer depends on knowing the protein's identity and experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, C is clearly the best fit. A (carbohydrate metabolism) and B (chondrocyte differentiation) are entirely unrelated to a secreted protease inhibitor. D (positive regulation of IL-8) is mechanistically opposite to the protein's anti-inflammatory/anti-coagulation function. C is the only option consistent with a parasite-derived secreted inhibitor of host defense pathways. No genuine ambiguity exists among the provided choices.


### Important caveats

- The GO:0030682 annotation is IEA:InterPro (computational, domain-based), not experimentally verified. The experimental (IDA) annotations are 'venom-mediated suppression of blood coagulation, intrinsic pathway' and 'hematophagy', neither of which appears among the choices.
- The term 'symbiont' in GO ontology typically refers to microorganisms in a host relationship; applying it to a macro-organism parasite (insect) is somewhat unconventional and likely stems from InterPro domain-level annotation transfer.
- The protein sequence alone (206 aa, signal peptide + Kunitz domain) provides limited information for precise GO term assignment without organism context.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between benchmark and UniProt entry A7BJ46.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a signal peptide (suggesting secretion) and a Kunitz-type serine protease inhibitor domain. One could reason that a secreted protease inhibitor is unlikely to be involved in carbohydrate metabolism (A) or chondrocyte differentiation (B), and its anti-proteolytic nature argues against positive regulation of IL-8 (D). However, the critical 'symbiont-mediated' qualifier in option C requires knowing the organism is a blood-sucking parasite (Triatoma infestans) and that the protein targets host defense pathways (kallikrein-kinin, coagulation). This ecological/organism-specific context is not derivable from the amino acid sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the source organism (Triatoma infestans, a hematophagous insect) and the specific experimental finding that this salivary protein inhibits host factor XII, prekallikrein, and kallikrein-kinin system activation. Without knowing the protein is from a blood-sucking parasite targeting host coagulation/inflammation pathways, the 'symbiont-mediated perturbation of host defenses' GO term cannot be assigned from sequence features alone.",
    "reason": "While general reasoning about Kunitz domains and secreted protease inhibitors can weakly eliminate A, B, and D, the specific GO term 'symbiont-mediated perturbation of host defenses' requires organism-level ecological knowledge (parasite/host relationship) and knowledge of the specific host defense pathway targeted. The sequence provides no information about the organism being a blood-sucking insect or the protein being a salivary secretion. The correct answer depends on knowing the protein's identity and experimental characterization."
  },
  "case_id": "GO_biological_process_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "H3",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A7BJ46 (Triafestin-2 from Triatoma infestans) carries GO:0030682 'symbiont-mediated perturbation of host defenses' as an annotation (evidence_id C7, H5). However, this annotation is IEA:InterPro (computational inference from domain), not experimentally verified. The experimental (IDA) annotations are GO:0140184 'venom-mediated suppression of blood coagulation, intrinsic pathway' and GO:0140106 'hematophagy'. The protein's experimentally characterized function (suppressing host kallikrein-kinin system and intrinsic coagulation) is consistent with the broader concept of perturbing host defenses, and the annotation exists in the database. Among the four provided choices, C is the most appropriate, though the 'symbiont' framing is somewhat unusual for a macro-organism parasite and derives from InterPro domain-based inference rather than direct experimental assignment."
  },
  "important_caveats": [
    "The GO:0030682 annotation is IEA:InterPro (computational, domain-based), not experimentally verified. The experimental (IDA) annotations are 'venom-mediated suppression of blood coagulation, intrinsic pathway' and 'hematophagy', neither of which appears among the choices.",
    "The term 'symbiont' in GO ontology typically refers to microorganisms in a host relationship; applying it to a macro-organism parasite (insect) is somewhat unconventional and likely stems from InterPro domain-level annotation transfer.",
    "The protein sequence alone (206 aa, signal peptide + Kunitz domain) provides limited information for precise GO term assignment without organism context.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between benchmark and UniProt entry A7BJ46."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, C is clearly the best fit. A (carbohydrate metabolism) and B (chondrocyte differentiation) are entirely unrelated to a secreted protease inhibitor. D (positive regulation of IL-8) is mechanistically opposite to the protein's anti-inflammatory/anti-coagulation function. C is the only option consistent with a parasite-derived secreted inhibitor of host defense pathways. No genuine ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A7BJ46 (Triafestin-2 from Triatoma infestans) carries GO:0030682 'symbiont-mediated perturbation of host defenses' as an annotation (evidence_id C7, H5). However, this annotation is IEA:InterPro (computational inference from domain), not experimentally verified. The experimental (IDA) annotations are GO:0140184 'venom-mediated suppression of blood coagulation, intrinsic pathway' and GO:0140106 'hematophagy'. The protein's experimentally characterized function (suppressing host kallikrein-kinin system and intrinsic coagulation) is consistent with the broader concept of perturbing host defenses, and the annotation exists in the database. Among the four provided choices, C is the most appropriate, though the 'symbiont' framing is somewhat unusual for a macro-organism parasite and derives from InterPro domain-based inference rather than direct experimental assignment.",
    "evidence_ids": ["C7", "H5", "C5", "H3", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a signal peptide (suggesting secretion) and a Kunitz-type serine protease inhibitor domain. One could reason that a secreted protease inhibitor is unlikely to be involved in carbohydrate metabolism (A) or chondrocyte differentiation (B), and its anti-proteolytic nature argues against positive regulation of IL-8 (D). However, the critical 'symbiont-mediated' qualifier in option C requires knowing the organism is a blood-sucking parasite (Triatoma infestans) and that the protein targets host defense pathways (kallikrein-kinin, coagulation). This ecological/organism-specific context is not derivable from the amino acid sequence alone.",
    "missing_item_specific_fact": "The identity of the source organism (Triatoma infestans, a hematophagous insect) and the specific experimental finding that this salivary protein inhibits host factor XII, prekallikrein, and kallikrein-kinin system activation. Without knowing the protein is from a blood-sucking parasite targeting host coagulation/inflammation pathways, the 'symbiont-mediated perturbation of host defenses' GO term cannot be assigned from sequence features alone.",
    "reason": "While general reasoning about Kunitz domains and secreted protease inhibitors can weakly eliminate A, B, and D, the specific GO term 'symbiont-mediated perturbation of host defenses' requires organism-level ecological knowledge (parasite/host relationship) and knowledge of the specific host defense pathway targeted. The sequence provides no information about the organism being a blood-sucking insect or the protein being a salivary secretion. The correct answer depends on knowing the protein's identity and experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, C is clearly the best fit. A (carbohydrate metabolism) and B (chondrocyte differentiation) are entirely unrelated to a secreted protease inhibitor. D (positive regulation of IL-8) is mechanistically opposite to the protein's anti-inflammatory/anti-coagulation function. C is the only option consistent with a parasite-derived secreted inhibitor of host defense pathways. No genuine ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The GO:0030682 annotation is IEA:InterPro (computational, domain-based), not experimentally verified. The experimental (IDA) annotations are 'venom-mediated suppression of blood coagulation, intrinsic pathway' and 'hematophagy', neither of which appears among the choices.",
    "The term 'symbiont' in GO ontology typically refers to microorganisms in a host relationship; applying it to a macro-organism parasite (insect) is somewhat unconventional and likely stems from InterPro domain-level annotation transfer.",
    "The protein sequence alone (206 aa, signal peptide + Kunitz domain) provides limited information for precise GO term assignment without organism context.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between benchmark and UniProt entry A7BJ46."
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

**Accession:** `A7BJ46` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ46.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.036893+00:00.  

```json
"A7BJ46"
```

Source SHA-256: `f9ac347806d10a9f1acc8ee345e7afb2371a11451b4b570457c931cf4fb49a0d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ46.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.036893+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17645545","source":"PubMed"}],"value":"Triafestin-2"}}}
```

Source SHA-256: `f9ac347806d10a9f1acc8ee345e7afb2371a11451b4b570457c931cf4fb49a0d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ46.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.036893+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17645545","source":"PubMed"}],"value":"Suppresses activation of the host plasma kallikrein-kinin system, leading to inhibition of the intrinsic coagulation pathway (PubMed:17645545). Blocks host coagulation factor XII (F12) and prekallikrein (KLKB1) reciprocal activation without affecting their amidolytic activities (PubMed:17645545). Blocks binding of host F12 and high molecular weight kininogen (KNG1) to negatively charged surfaces (PubMed:17645545). Attenuates generation of bradykinin by interfering with activation of host kallikrein-kinin system (PubMed:17645545)"}]}
```

Source SHA-256: `f9ac347806d10a9f1acc8ee345e7afb2371a11451b4b570457c931cf4fb49a0d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ46.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.036893+00:00.  

```json
{"database":"GO","id":"GO:0030682","properties":[{"key":"GoTerm","value":"P:symbiont-mediated perturbation of host defenses"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `f9ac347806d10a9f1acc8ee345e7afb2371a11451b4b570457c931cf4fb49a0d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7BJ46.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.036893+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17645545","source":"PubMed"}],"id":"GO:0140184","properties":[{"key":"GoTerm","value":"P:venom-mediated suppression of blood coagulation, intrinsic pathway"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `f9ac347806d10a9f1acc8ee345e7afb2371a11451b4b570457c931cf4fb49a0d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ46?format=txt&versions=31)  
**Locator:** `lines 23-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:27:10.922082+00:00.  

```text
CC   -!- FUNCTION: Suppresses activation of the host plasma kallikrein-kinin
CC       system, leading to inhibition of the intrinsic coagulation pathway
CC       (PubMed:17645545). Blocks host coagulation factor XII (F12) and
CC       prekallikrein (KLKB1) reciprocal activation without affecting their
CC       amidolytic activities (PubMed:17645545). Blocks binding of host F12 and
CC       high molecular weight kininogen (KNG1) to negatively charged surfaces
CC       (PubMed:17645545). Attenuates generation of bradykinin by interfering
CC       with activation of host kallikrein-kinin system (PubMed:17645545).
CC       {ECO:0000269|PubMed:17645545}.
```

Source SHA-256: `8f96422bf3858862da59351ba95456e5b72cff9854924439343c78a6f88b7c07`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ46?format=txt&versions=31)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:27:10.922082+00:00.  

```text
DR   GO; GO:0030682; P:symbiont-mediated perturbation of host defenses; IEA:InterPro.
```

Source SHA-256: `8f96422bf3858862da59351ba95456e5b72cff9854924439343c78a6f88b7c07`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7BJ46?format=txt&versions=31)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:27:10.922082+00:00.  

```text
DR   GO; GO:0140184; P:venom-mediated suppression of blood coagulation, intrinsic pathway; IDA:UniProtKB.
```

Source SHA-256: `8f96422bf3858862da59351ba95456e5b72cff9854924439343c78a6f88b7c07`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
