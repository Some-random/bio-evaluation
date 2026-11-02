# GO_molecular_function_0074

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — UDP-glucosyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSPLKLYFLPYISPGHMIPLSEMARLFANQGHHVTIITTTSNATLLQKYTTATLSLHLIPLPTKEAGLPDGLENFISVNDLETAGKLYYALSLLQPVIEEFITSNPPDCIVSDMFYPWTADLASQLQVPRMVFHAACIFAMCMKESMRGPDAPHLKVSSDYELFEVKGLPDPVFMTRAQLPDYVRTPNGYTQLMEMWREAEKKSYGVMVNNFYELDPAYTEHYSKIMGHKVWNIGPAAQILHRGSGDKIERVHKAVVGENQCLSWLDTKEPNSVFYVCFGSAIRFPDDQLYEIASALESSGAQFIWAVLGKDSDNSDSNSDSEWLPAGFEEKMKETGRGMIIRGWAPQVLILDHPSVGGFMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN

[Multiple Choices]
A. histone reader activity
B. beta-amyrin 28-monooxygenase activity
C. UDP-glucosyltransferase activity
D. kinase activity
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

### Expected-answer support: contradicted

> The sequence-matched entry has an exact GO annotation to UDP-glucosyltransferase activity, but that annotation is computational (TreeGrafter). The cited experimental catalytic reaction instead transfers xylose from UDP-xylose, whereas the GO term for option C specifies transfer of glucose from UDP-glucose. Thus the experimental evidence does not support the option's specific activity and points to a different sugar-transfer reaction.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble plant glycosyltransferase, which broadly favors C over a histone reader, a beta-amyrin monooxygenase, or a kinase. That broad inference does not establish transfer of glucose rather than another sugar.


**Missing item-specific fact**

> The substrate specificity established for this particular enzyme: its cited reaction uses UDP-xylose, not UDP-glucose.


**Reason**

> The sequence can suggest a glycosyltransferase class, but distinguishing the specific UDP-glucosyltransferase activity in option C requires protein-specific substrate evidence or an annotation not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative option is supported by the supplied sequence-specific experimental evidence. The closest broad class is glycosyltransferase, but the experimentally described sugar-transfer reaction is not precisely represented among the choices.


### Important caveats

- The sequence match is exact, and the experimental annotation is reported with IDA evidence, but the cited reaction does not establish that the enzyme cannot also use UDP-glucose.
- The exact UDP-glucosyltransferase GO annotation is present in the database, but its evidence is computational rather than experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant glycosyltransferase, which broadly favors C over a histone reader, a beta-amyrin monooxygenase, or a kinase. That broad inference does not establish transfer of glucose rather than another sugar.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity established for this particular enzyme: its cited reaction uses UDP-xylose, not UDP-glucose.",
    "reason": "The sequence can suggest a glycosyltransferase class, but distinguishing the specific UDP-glucosyltransferase activity in option C requires protein-specific substrate evidence or an annotation not supplied in the original input."
  },
  "case_id": "GO_molecular_function_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched entry has an exact GO annotation to UDP-glucosyltransferase activity, but that annotation is computational (TreeGrafter). The cited experimental catalytic reaction instead transfers xylose from UDP-xylose, whereas the GO term for option C specifies transfer of glucose from UDP-glucose. Thus the experimental evidence does not support the option's specific activity and points to a different sugar-transfer reaction."
  },
  "important_caveats": [
    "The sequence match is exact, and the experimental annotation is reported with IDA evidence, but the cited reaction does not establish that the enzyme cannot also use UDP-glucose.",
    "The exact UDP-glucosyltransferase GO annotation is present in the database, but its evidence is computational rather than experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative option is supported by the supplied sequence-specific experimental evidence. The closest broad class is glycosyltransferase, but the experimentally described sugar-transfer reaction is not precisely represented among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0074",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched entry has an exact GO annotation to UDP-glucosyltransferase activity, but that annotation is computational (TreeGrafter). The cited experimental catalytic reaction instead transfers xylose from UDP-xylose, whereas the GO term for option C specifies transfer of glucose from UDP-glucose. Thus the experimental evidence does not support the option's specific activity and points to a different sugar-transfer reaction.",
    "evidence_ids": ["C6", "C7", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant glycosyltransferase, which broadly favors C over a histone reader, a beta-amyrin monooxygenase, or a kinase. That broad inference does not establish transfer of glucose rather than another sugar.",
    "missing_item_specific_fact": "The substrate specificity established for this particular enzyme: its cited reaction uses UDP-xylose, not UDP-glucose.",
    "reason": "The sequence can suggest a glycosyltransferase class, but distinguishing the specific UDP-glucosyltransferase activity in option C requires protein-specific substrate evidence or an annotation not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative option is supported by the supplied sequence-specific experimental evidence. The closest broad class is glycosyltransferase, but the experimentally described sugar-transfer reaction is not precisely represented among the choices."
  },
  "important_caveats": [
    "The sequence match is exact, and the experimental annotation is reported with IDA evidence, but the cited reaction does not establish that the enzyme cannot also use UDP-glucose.",
    "The exact UDP-glucosyltransferase GO annotation is present in the database, but its evidence is computational rather than experimental."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1J9R8 (sequence matched) is named 'UDP-glucosyl transferase 73CC6' (EC 2.4.1.-) and carries GO:0035251 (UDP-glucosyltransferase activity, IEA:TreeGrafter) and GO:0008194 (UDP-glycosyltransferase activity, IDA:UniProtKB, experimental). The demonstrated catalytic activity (C6) shows transfer of a sugar from a UDP-sugar donor, confirming the protein is a UDP-dependent glycosyltransferase. The specific GO:0035251 term (glucosyltransferase) is computationally inferred (IEA), while the experimentally verified activity uses UDP-xylose (a glycosyltransferase, GO:0008194). Nevertheless, among the four options, C is the only one consistent with the protein's family (UGT73) and demonstrated enzymatic class. The protein is definitively not a histone reader, monooxygenase, or kinase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable PSPG (plant secondary product glycosyltransferase) motif: the region 'HCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGG' is the canonical plant UGT signature. This motif is a textbook diagnostic feature of the UDP-glycosyltransferase (UGT) superfamily in plants. Conversely, the sequence lacks: (1) kinase catalytic motifs (e.g., VAIK, HRD, DFG catalytic loop), ruling out D; (2) cytochrome P450 heme-binding motif (FxxGxRxCxG) or FAD/NADPH-binding motifs, ruling out B; (3) bromodomain, chromodomain, PHD finger, or Tudor domain signatures, ruling out A. A model with general knowledge of protein domain architecture can identify the PSPG motif and exclude the other three enzyme classes.


**Missing item-specific fact**

> None critical. The PSPG motif is a well-established, general-knowledge sequence signature in plant biochemistry sufficient to assign the protein to the UGT family and thus to UDP-glycosyltransferase activity.


**Reason**

> The PSPG motif is a widely taught, identifiable sequence feature that directly maps to UDP-glycosyltransferase function. The absence of motifs diagnostic of kinases, P450 monooxygenases, and histone readers provides additional negative evidence. This constitutes a concrete biological argument from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C is consistent with the sequence. The PSPG motif unambiguously places the protein in the UGT family. Options A, B, and D lack any supporting sequence features and are incompatible with the identified motif. The minor distinction between 'glucosyltransferase' (GO:0035251, computationally inferred) and 'glycosyltransferase' (GO:0008194, experimentally supported) does not create ambiguity among the given choices, as no 'UDP-glycosyltransferase activity' option is offered.


### Important caveats

- The GO:0035251 annotation (UDP-glucosyltransferase activity) is IEA:TreeGrafter (computational inference), not experimentally verified. The experimentally demonstrated activity (ECO:0000269, PubMed:39043959) is specifically a UDP-xylosyltransferase reaction, which strictly falls under the broader GO:0008194 (UDP-glycosyltransferase activity). However, the protein belongs to the UGT73 family and the option C is the best available match.
- The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available at authoring time, though the sequence itself (and its UGT-family identity via PSPG motif) would have been inferable.
- The protein name 'UDP-glucosyl transferase 73CC6' reflects family nomenclature (UGT73) rather than strict substrate specificity, which is experimentally UDP-xylose in this case.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable PSPG (plant secondary product glycosyltransferase) motif: the region 'HCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGG' is the canonical plant UGT signature. This motif is a textbook diagnostic feature of the UDP-glycosyltransferase (UGT) superfamily in plants. Conversely, the sequence lacks: (1) kinase catalytic motifs (e.g., VAIK, HRD, DFG catalytic loop), ruling out D; (2) cytochrome P450 heme-binding motif (FxxGxRxCxG) or FAD/NADPH-binding motifs, ruling out B; (3) bromodomain, chromodomain, PHD finger, or Tudor domain signatures, ruling out A. A model with general knowledge of protein domain architecture can identify the PSPG motif and exclude the other three enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PSPG motif is a well-established, general-knowledge sequence signature in plant biochemistry sufficient to assign the protein to the UGT family and thus to UDP-glycosyltransferase activity.",
    "reason": "The PSPG motif is a widely taught, identifiable sequence feature that directly maps to UDP-glycosyltransferase function. The absence of motifs diagnostic of kinases, P450 monooxygenases, and histone readers provides additional negative evidence. This constitutes a concrete biological argument from the supplied sequence."
  },
  "case_id": "GO_molecular_function_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J9R8 (sequence matched) is named 'UDP-glucosyl transferase 73CC6' (EC 2.4.1.-) and carries GO:0035251 (UDP-glucosyltransferase activity, IEA:TreeGrafter) and GO:0008194 (UDP-glycosyltransferase activity, IDA:UniProtKB, experimental). The demonstrated catalytic activity (C6) shows transfer of a sugar from a UDP-sugar donor, confirming the protein is a UDP-dependent glycosyltransferase. The specific GO:0035251 term (glucosyltransferase) is computationally inferred (IEA), while the experimentally verified activity uses UDP-xylose (a glycosyltransferase, GO:0008194). Nevertheless, among the four options, C is the only one consistent with the protein's family (UGT73) and demonstrated enzymatic class. The protein is definitively not a histone reader, monooxygenase, or kinase."
  },
  "important_caveats": [
    "The GO:0035251 annotation (UDP-glucosyltransferase activity) is IEA:TreeGrafter (computational inference), not experimentally verified. The experimentally demonstrated activity (ECO:0000269, PubMed:39043959) is specifically a UDP-xylosyltransferase reaction, which strictly falls under the broader GO:0008194 (UDP-glycosyltransferase activity). However, the protein belongs to the UGT73 family and the option C is the best available match.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available at authoring time, though the sequence itself (and its UGT-family identity via PSPG motif) would have been inferable.",
    "The protein name 'UDP-glucosyl transferase 73CC6' reflects family nomenclature (UGT73) rather than strict substrate specificity, which is experimentally UDP-xylose in this case."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the sequence. The PSPG motif unambiguously places the protein in the UGT family. Options A, B, and D lack any supporting sequence features and are incompatible with the identified motif. The minor distinction between 'glucosyltransferase' (GO:0035251, computationally inferred) and 'glycosyltransferase' (GO:0008194, experimentally supported) does not create ambiguity among the given choices, as no 'UDP-glycosyltransferase activity' option is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J9R8 (sequence matched) is named 'UDP-glucosyl transferase 73CC6' (EC 2.4.1.-) and carries GO:0035251 (UDP-glucosyltransferase activity, IEA:TreeGrafter) and GO:0008194 (UDP-glycosyltransferase activity, IDA:UniProtKB, experimental). The demonstrated catalytic activity (C6) shows transfer of a sugar from a UDP-sugar donor, confirming the protein is a UDP-dependent glycosyltransferase. The specific GO:0035251 term (glucosyltransferase) is computationally inferred (IEA), while the experimentally verified activity uses UDP-xylose (a glycosyltransferase, GO:0008194). Nevertheless, among the four options, C is the only one consistent with the protein's family (UGT73) and demonstrated enzymatic class. The protein is definitively not a histone reader, monooxygenase, or kinase.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable PSPG (plant secondary product glycosyltransferase) motif: the region 'HCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGG' is the canonical plant UGT signature. This motif is a textbook diagnostic feature of the UDP-glycosyltransferase (UGT) superfamily in plants. Conversely, the sequence lacks: (1) kinase catalytic motifs (e.g., VAIK, HRD, DFG catalytic loop), ruling out D; (2) cytochrome P450 heme-binding motif (FxxGxRxCxG) or FAD/NADPH-binding motifs, ruling out B; (3) bromodomain, chromodomain, PHD finger, or Tudor domain signatures, ruling out A. A model with general knowledge of protein domain architecture can identify the PSPG motif and exclude the other three enzyme classes.",
    "missing_item_specific_fact": "None critical. The PSPG motif is a well-established, general-knowledge sequence signature in plant biochemistry sufficient to assign the protein to the UGT family and thus to UDP-glycosyltransferase activity.",
    "reason": "The PSPG motif is a widely taught, identifiable sequence feature that directly maps to UDP-glycosyltransferase function. The absence of motifs diagnostic of kinases, P450 monooxygenases, and histone readers provides additional negative evidence. This constitutes a concrete biological argument from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the sequence. The PSPG motif unambiguously places the protein in the UGT family. Options A, B, and D lack any supporting sequence features and are incompatible with the identified motif. The minor distinction between 'glucosyltransferase' (GO:0035251, computationally inferred) and 'glycosyltransferase' (GO:0008194, experimentally supported) does not create ambiguity among the given choices, as no 'UDP-glycosyltransferase activity' option is offered."
  },
  "important_caveats": [
    "The GO:0035251 annotation (UDP-glucosyltransferase activity) is IEA:TreeGrafter (computational inference), not experimentally verified. The experimentally demonstrated activity (ECO:0000269, PubMed:39043959) is specifically a UDP-xylosyltransferase reaction, which strictly falls under the broader GO:0008194 (UDP-glycosyltransferase activity). However, the protein belongs to the UGT73 family and the option C is the best available match.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation may not have been available at authoring time, though the sequence itself (and its UGT-family identity via PSPG motif) would have been inferable.",
    "The protein name 'UDP-glucosyl transferase 73CC6' reflects family nomenclature (UGT73) rather than strict substrate specificity, which is experimentally UDP-xylose in this case."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_donor_difference_traced`.

> C6 gives a UDP-xylose donor reaction; GO2 specifically defines UDP-glucosyltransferase using UDP-glucose; C7 assigns the latter computationally.

**Remaining uncertainty:** The reaction/definition mismatch is literal. The excerpt does not test whether UDP-glucose is an additional usable donor.

Evidence checked: [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0AAW1J9R8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"UDP-glucosyl transferase 73CC6"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoUGT73CC6"}]}}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that mediates the conversion of QA-di to QA-tri via the branching of the C-3 sugar chain with a D-xylose (PubMed:39043959)"}]}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:85040"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"name":"3-O-[beta-D-galactosyl-(1->2)-beta-D-glucuronosyl]-quillate + UDP-alpha-D-xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillate + UDP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:85039"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57632"},{"database":"ChEBI","id":"CHEBI:58223"},{"database":"ChEBI","id":"CHEBI:234160"},{"database":"ChEBI","id":"CHEBI:234161"}]}}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"database":"GO","id":"GO:0035251","properties":[{"key":"GoTerm","value":"F:UDP-glucosyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.561717+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0008194","properties":[{"key":"GoTerm","value":"F:UDP-glycosyltransferase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
ID   GT736_SAPOF             Reviewed;         487 AA.
AC   A0AAW1J9R8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=UDP-glucosyl transferase 73CC6 {ECO:0000303|PubMed:39043959};
DE            Short=SoUGT73CC6 {ECO:0000303|PubMed:39043959};
DE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};
GN   Name=UGT73CC6 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11041839m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_08G118300 {ECO:0000312|EMBL:KAK9698621.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). A glycosyltransferase
CC       that mediates the conversion of QA-di to QA-tri via the branching of
CC       the C-3 sugar chain with a D-xylose (PubMed:39043959).
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 41-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-O-[beta-D-galactosyl-(1->2)-beta-D-glucuronosyl]-quillate +
CC         UDP-alpha-D-xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-
CC         D-GlcA}-quillate + UDP + H(+); Xref=Rhea:RHEA:85039,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57632, ChEBI:CHEBI:58223,
CC         ChEBI:CHEBI:234160, ChEBI:CHEBI:234161;
CC         Evidence={ECO:0000269|PubMed:39043959};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:85040;
CC         Evidence={ECO:0000269|PubMed:39043959};
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
DR   GO; GO:0035251; F:UDP-glucosyltransferase activity; IEA:TreeGrafter.
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-01T06:27:40.480726+00:00.  

```text
DR   GO; GO:0008194; F:UDP-glycosyltransferase activity; IDA:UniProtKB.
```

Source SHA-256: `9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 216295-216303`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0035251
name: UDP-glucosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a glucosyl group from UDP-glucose to an acceptor molecule." [PMID:19858195]
xref: Reactome:R-HSA-1912353 "Glucosylation of Pre-NOTCH by POGLUT1"
is_a: GO:0008194 ! UDP-glycosyltransferase activity
is_a: GO:0046527 ! glucosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
