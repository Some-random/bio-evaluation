# catalytic_activity_0173: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0173.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **A** — 2 a 1,2-diacyl-sn-glycero-3-phospho-(1&#x27;-sn-glycerol) = a cardiolipin + glycerol

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTFNGRFRATLRGINIRNASMTSLSLTGSHAQKQTVLGSTPGALGTIPTVALNGVNPLPRYRHNLLFGTLSFGDRWDRIQRRLAVLGRASTGNVVVPFSDSADAFRRMWESVDSASDSVLWQTYICKDDFVGQKTVKKLEEAHRRGCKTELLYDCGGNITGRRRLVGDLKKSGANVIEHRPMWEHFFPYFLRGMKWELSPGIRNHRKILIVDNKLGFCGGLNIGDEYCGTSEGGNGRFRDTHCVVMGPAVMHMREVYEDTKAPKPWKWSLARWRQIASATMNLRYLEGMNVKHDYLEPTTTFVRQGGGVYLRRQMERAERSTVRMMERMRWKRQRERLNRCLLTLAKNLREGQGLVFKAATGKGDDVATTDAGSKRNNEVSHGQWKLMKRRIDEYRQRAIKNAEESFFRRLRVVNPSMRLLEDTSPVAEAEAYGQAHAAVTQVLSCNPHSRDWSIPYAFWQVSKFVHQRLWVTTPYYMPHRKLMRALQLAARRGVDVRILAGSNRTTDPWFMWYASNYITGMLMASGVRVYEYKGGQVMHAKTVVADSIWTSIGSYNWDMMSNKNMEICVCHLDHNLALTMEKQFLDDMNVSEEVNYEEYQRRSLWLRFSSWFFYTALRIAEKFTFRTFWDPDLSSEID

[Multiple Choices]
A. 2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol
B. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
C. norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)
D. restrictinol + glycine + H(+) = restricticin + H2O
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.


**Missing item-specific fact**

> The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.


**Reason**

> The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity.


### Important caveats

- The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.
- The reviewer-only accession and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.",
    "reason": "The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details."
  },
  "important_caveats": [
    "The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.",
    "The reviewer-only accession and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for Trypanosoma brucei cardiolipin synthetase, whose curated catalytic-activity annotation gives choice A. That annotation cites a 2012 paper, but the supplied excerpts do not independently establish the experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name distinct, specific enzyme reactions; the sequence and prompt provide no biological context or sufficiently distinctive evidence to identify this particular reaction by general reasoning alone.",
    "missing_item_specific_fact": "The sequence-specific identity or functional annotation linking this protein to cardiolipin synthetase and its cardiolipin-forming reaction.",
    "reason": "The reviewer-only annotation supports the key, but that protein-specific identity and reaction are absent from the evaluated input. Recognizing the sequence from a database would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe different reactions, and the sequence-matched curated annotation specifically corresponds to A. The limitation is lack of supplied grounds to distinguish them, not evidence that multiple choices describe the same activity."
  },
  "important_caveats": [
    "The UniProt annotation is curator-assigned and cites a publication; the excerpts do not include primary experimental results for independent assessment.",
    "The reviewer-only accession and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.


**Missing item-specific fact**

> None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.


**Reason**

> A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors.


### Important caveats

- The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.
- The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.
- All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.
- The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.",
    "reason": "A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.",
    "The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.",
    "All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.",
    "The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q584D1 (CLS_TRYB2, 639 AA, Trypanosoma brucei brucei) by SHA-256. The Swiss-Prot reviewed entry annotates it as Cardiolipin synthetase (EC 2.7.8.-) with the exact catalytic reaction '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' (Rhea:RHEA:31451), supported by ECO:0000305 from PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012), a paper that experimentally characterized this enzyme's cardiolipin-synthase function. The historical (entry v102) and current (v104) records both confirm the same annotation and sequence match.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable DRD-like motif ('GDRWDR' within 'TLSFGDRWDRIQRRLAVL'), a hallmark of the CDP-alcohol phosphatidyltransferase superfamily, which catalyzes phospholipid transfer and synthesis reactions. Among the four choices, only A describes a phospholipid condensation reaction (two phosphatidylglycerol molecules → cardiolipin + glycerol). The other three options belong to entirely different enzyme classes: B is a GNAT-fold lysine acetyltransferase reaction, C is a SAM-dependent methyltransferase reaction on an alkaloid substrate, and D is a non-ribosomal peptide-synthetase-style amide bond formation. The DRD motif and the phospholipid-chemistry context of choice A are distinguishable from the other three through general enzymology and membrane-protein biochemistry knowledge.",
    "missing_item_specific_fact": "None that is strictly required. Identifying the DRD motif and associating it with the CDP-alcohol phosphatidyltransferase superfamily is general biochemical knowledge, not a protein-specific database lookup.",
    "reason": "A model familiar with the DRD/DRDxxG motif of CDP-alcohol phosphatidyltransferases can scan the sequence, note the motif, infer a phospholipid-transfer/synthesis function, and eliminate the three non-phospholipid choices (acetyltransferase, methyltransferase, peptide ligase). This is a concrete, general-knowledge reasoning chain rather than a single-protein database recall."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four unrelated enzyme classes (phospholipid synthase, protein acetyltransferase, alkaloid methyltransferase, peptide ligase). The sequence's DRD motif and hydrophobic transmembrane segments clearly point to a membrane phospholipid-transfer enzyme, leaving no viable alternative among the distractors."
  },
  "important_caveats": [
    "The annotation evidence code ECO:0000305 (inferred from direct assay / curator inference from published paper) references a 2012 PNAS study that experimentally demonstrated cardiolipin-synthase activity; the annotation is not purely computational.",
    "The DRD motif in this sequence reads 'GDRWDR' rather than the textbook-perfect 'DRDxxG'; a model must tolerate this variant to make the superfamily assignment.",
    "All UniProt evidence is reviewer-only and was absent from the evaluated model input; the reasoning argument relies on general biochemical knowledge of the DRD motif, not on access to the database entry.",
    "The EC number is listed as 2.7.8.- (unspecified sub-subclass), so the annotation does not pin down a single EC sub-subclass, but the Rhea reaction and PubMed reference do specify the exact transformation."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the UniProt entry annotated as cardiolipin synthetase, and that entry gives the reaction in choice A with a literature citation. This supports the key as a curated database annotation; the excerpts do not independently show the underlying assay results.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two HxKxxxxD-like motifs, a characteristic pattern of the phospholipase D family. Bacterial-type cardiolipin synthases belong to this family and transfer phosphatidyl groups between phosphatidylglycerol molecules, producing cardiolipin and glycerol as in A. This family-level sequence clue distinguishes A from the protein acetylation, methylation, and peptide-forming reactions in the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family inference from the sequence provides a meaningful basis for choosing A among these alternatives. The motifs alone do not uniquely establish the enzyme's substrate or reaction, but the options make the family-level inference discriminating without requiring recall of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based phospholipase D family inference favors A, and no other offered reaction is comparably supported.


### Important caveats

- The cited database annotation supports the expected reaction, but the supplied excerpts do not include primary experimental data.
- The source record is sequence-matched; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two HxKxxxxD-like motifs, a characteristic pattern of the phospholipase D family. Bacterial-type cardiolipin synthases belong to this family and transfer phosphatidyl groups between phosphatidylglycerol molecules, producing cardiolipin and glycerol as in A. This family-level sequence clue distinguishes A from the protein acetylation, methylation, and peptide-forming reactions in the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family inference from the sequence provides a meaningful basis for choosing A among these alternatives. The motifs alone do not uniquely establish the enzyme's substrate or reaction, but the options make the family-level inference discriminating without requiring recall of this exact protein's annotation."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as cardiolipin synthetase, and that entry gives the reaction in choice A with a literature citation. This supports the key as a curated database annotation; the excerpts do not independently show the underlying assay results."
  },
  "important_caveats": [
    "The cited database annotation supports the expected reaction, but the supplied excerpts do not include primary experimental data.",
    "The source record is sequence-matched; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based phospholipase D family inference favors A, and no other offered reaction is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as cardiolipin synthetase, and that entry gives the reaction in choice A with a literature citation. This supports the key as a curated database annotation; the excerpts do not independently show the underlying assay results.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two HxKxxxxD-like motifs, a characteristic pattern of the phospholipase D family. Bacterial-type cardiolipin synthases belong to this family and transfer phosphatidyl groups between phosphatidylglycerol molecules, producing cardiolipin and glycerol as in A. This family-level sequence clue distinguishes A from the protein acetylation, methylation, and peptide-forming reactions in the other options.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family inference from the sequence provides a meaningful basis for choosing A among these alternatives. The motifs alone do not uniquely establish the enzyme's substrate or reaction, but the options make the family-level inference discriminating without requiring recall of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based phospholipase D family inference favors A, and no other offered reaction is comparably supported."
  },
  "important_caveats": [
    "The cited database annotation supports the expected reaction, but the supplied excerpts do not include primary experimental data.",
    "The source record is sequence-matched; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, H4) from UniProt entry Q584D1 (sequence matched, 639 aa) records the catalytic activity as '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' with evidence code ECO:0000305|PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012). The protein is annotated as Cardiolipin synthetase (EC 2.7.8.-) from Trypanosoma brucei brucei. The author's expected answer matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two identifiable phospholipase D (PLD) superfamily HKD motifs: 'HRKILIVDNK' (H-R-K-I-L-I-V-D, first motif) and 'HAKTVVAD' (H-A-K-T-V-V-A-D, second motif). The HxK4D motif pair is the canonical catalytic signature of the PLD superfamily, a well-characterized enzyme class learned from many homologs (e.g., bacterial CDP-diacylglycerol synthase, mammalian PLD1/2, yeast CDS1, bacterial cardiolipin synthases). PLD superfamily members catalyze phosphodiester cleavage/transfer in phospholipid substrates. Among the four choices, only option A (phosphatidylglycerol → cardiolipin + glycerol) involves phospholipid phosphodiester chemistry consistent with PLD superfamily catalysis. Option B (lysine acetyltransferase, GNAT/MYST fold using acetyl-CoA), option C (SAM-dependent methyltransferase), and option D (glycine-dependent amidation/acyltransfer) belong to completely unrelated enzyme superfamilies that lack HKD motifs and do not act on phospholipid phosphodiester bonds. The protein's ~639 aa length and N-terminal hydrophobic/signal-like region (consistent with membrane association for phospholipid substrates) further support a phospholipid-metabolizing enzyme. Thus, recognizing the PLD HKD motifs from general family knowledge meaningfully distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The two HKD motifs are directly observable in the provided sequence and are the defining signature of the PLD superfamily, a well-known enzyme class with many characterized members. This family-level knowledge, transferable from other proteins, eliminates the three non-phospholipid options and points to the phosphatidyltransferase reaction in option A. No target-specific database lookup is required to make this distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four distinct enzyme classes (phospholipid phosphatidyltransferase, protein acetyltransferase, SAM methyltransferase, glycine amidase/acyltransferase). The presence of PLD HKD motifs in the sequence unambiguously points to phospholipid chemistry (option A) and is incompatible with the mechanisms of options B, C, and D.


### Important caveats

- The UniProt annotation cites ECO:0000305 (curator inference from literature) rather than ECO:0000269 (direct experimental assay), though the referenced PNAS 2012 paper reports functional characterization including disruption phenotype. The annotation is well-supported but is curated from a single publication.
- The HKD motifs identified are approximate matches to the canonical HxK4D pattern (e.g., HRKILIVD vs. strict HKxxxxD). PLD superfamily motifs tolerate substitutions, and the identification relies on pattern recognition across the broader family.
- The 'bacterial-type' designation noted in the PNAS title indicates this eukaryotic CLS resembles bacterial homologs rather than the eukaryotic-type CLS (which uses a different fold), reinforcing PLD superfamily membership.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two identifiable phospholipase D (PLD) superfamily HKD motifs: 'HRKILIVDNK' (H-R-K-I-L-I-V-D, first motif) and 'HAKTVVAD' (H-A-K-T-V-V-A-D, second motif). The HxK4D motif pair is the canonical catalytic signature of the PLD superfamily, a well-characterized enzyme class learned from many homologs (e.g., bacterial CDP-diacylglycerol synthase, mammalian PLD1/2, yeast CDS1, bacterial cardiolipin synthases). PLD superfamily members catalyze phosphodiester cleavage/transfer in phospholipid substrates. Among the four choices, only option A (phosphatidylglycerol → cardiolipin + glycerol) involves phospholipid phosphodiester chemistry consistent with PLD superfamily catalysis. Option B (lysine acetyltransferase, GNAT/MYST fold using acetyl-CoA), option C (SAM-dependent methyltransferase), and option D (glycine-dependent amidation/acyltransfer) belong to completely unrelated enzyme superfamilies that lack HKD motifs and do not act on phospholipid phosphodiester bonds. The protein's ~639 aa length and N-terminal hydrophobic/signal-like region (consistent with membrane association for phospholipid substrates) further support a phospholipid-metabolizing enzyme. Thus, recognizing the PLD HKD motifs from general family knowledge meaningfully distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The two HKD motifs are directly observable in the provided sequence and are the defining signature of the PLD superfamily, a well-known enzyme class with many characterized members. This family-level knowledge, transferable from other proteins, eliminates the three non-phospholipid options and points to the phosphatidyltransferase reaction in option A. No target-specific database lookup is required to make this distinction."
  },
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry Q584D1 (sequence matched, 639 aa) records the catalytic activity as '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' with evidence code ECO:0000305|PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012). The protein is annotated as Cardiolipin synthetase (EC 2.7.8.-) from Trypanosoma brucei brucei. The author's expected answer matches the database annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation cites ECO:0000305 (curator inference from literature) rather than ECO:0000269 (direct experimental assay), though the referenced PNAS 2012 paper reports functional characterization including disruption phenotype. The annotation is well-supported but is curated from a single publication.",
    "The HKD motifs identified are approximate matches to the canonical HxK4D pattern (e.g., HRKILIVD vs. strict HKxxxxD). PLD superfamily motifs tolerate substitutions, and the identification relies on pattern recognition across the broader family.",
    "The 'bacterial-type' designation noted in the PNAS title indicates this eukaryotic CLS resembles bacterial homologs rather than the eukaryotic-type CLS (which uses a different fold), reinforcing PLD superfamily membership."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (phospholipid phosphatidyltransferase, protein acetyltransferase, SAM methyltransferase, glycine amidase/acyltransferase). The presence of PLD HKD motifs in the sequence unambiguously points to phospholipid chemistry (option A) and is incompatible with the mechanisms of options B, C, and D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry Q584D1 (sequence matched, 639 aa) records the catalytic activity as '2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol' with evidence code ECO:0000305|PubMed:22451910 (Serricchio & Buetikofer, PNAS 2012). The protein is annotated as Cardiolipin synthetase (EC 2.7.8.-) from Trypanosoma brucei brucei. The author's expected answer matches the database annotation exactly.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two identifiable phospholipase D (PLD) superfamily HKD motifs: 'HRKILIVDNK' (H-R-K-I-L-I-V-D, first motif) and 'HAKTVVAD' (H-A-K-T-V-V-A-D, second motif). The HxK4D motif pair is the canonical catalytic signature of the PLD superfamily, a well-characterized enzyme class learned from many homologs (e.g., bacterial CDP-diacylglycerol synthase, mammalian PLD1/2, yeast CDS1, bacterial cardiolipin synthases). PLD superfamily members catalyze phosphodiester cleavage/transfer in phospholipid substrates. Among the four choices, only option A (phosphatidylglycerol → cardiolipin + glycerol) involves phospholipid phosphodiester chemistry consistent with PLD superfamily catalysis. Option B (lysine acetyltransferase, GNAT/MYST fold using acetyl-CoA), option C (SAM-dependent methyltransferase), and option D (glycine-dependent amidation/acyltransfer) belong to completely unrelated enzyme superfamilies that lack HKD motifs and do not act on phospholipid phosphodiester bonds. The protein's ~639 aa length and N-terminal hydrophobic/signal-like region (consistent with membrane association for phospholipid substrates) further support a phospholipid-metabolizing enzyme. Thus, recognizing the PLD HKD motifs from general family knowledge meaningfully distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The two HKD motifs are directly observable in the provided sequence and are the defining signature of the PLD superfamily, a well-known enzyme class with many characterized members. This family-level knowledge, transferable from other proteins, eliminates the three non-phospholipid options and points to the phosphatidyltransferase reaction in option A. No target-specific database lookup is required to make this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (phospholipid phosphatidyltransferase, protein acetyltransferase, SAM methyltransferase, glycine amidase/acyltransferase). The presence of PLD HKD motifs in the sequence unambiguously points to phospholipid chemistry (option A) and is incompatible with the mechanisms of options B, C, and D."
  },
  "important_caveats": [
    "The UniProt annotation cites ECO:0000305 (curator inference from literature) rather than ECO:0000269 (direct experimental assay), though the referenced PNAS 2012 paper reports functional characterization including disruption phenotype. The annotation is well-supported but is curated from a single publication.",
    "The HKD motifs identified are approximate matches to the canonical HxK4D pattern (e.g., HRKILIVD vs. strict HKxxxxD). PLD superfamily motifs tolerate substitutions, and the identification relies on pattern recognition across the broader family.",
    "The 'bacterial-type' designation noted in the PNAS title indicates this eukaryotic CLS resembles bacterial homologs rather than the eukaryotic-type CLS (which uses a different fold), reinforcing PLD superfamily membership."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q584D1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "benchmark_sequence_length": 639,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 104,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-05-10",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "current_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "current_source_sequence_length": 639,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 102,
  "selected_historical_version": {
    "accession": "Q584D1",
    "database": "Swiss-Prot",
    "entryVersion": 102,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CLS_TRYB2",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "selected_historical_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "selected_historical_source_sequence_length": 639,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 102,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q584D1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":104,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-05-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CL synthase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"name\":\"2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:31451\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17754\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64716\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Serricchio M.\",\"Buetikofer P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22451910\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1121528109\"}],\"citationType\":\"journal article\",\"firstPage\":\"E954\",\"id\":\"22451910\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"E961\",\"publicationDate\":\"2012\",\"title\":\"An essential bacterial-type cardiolipin synthase mediates cardiolipin formation in a eukaryote.\",\"volume\":\"109\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   CLS_TRYB2               Reviewed;         639 AA.\nAC   Q584D1; D6XFJ2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-MAY-2005, sequence version 1.\nDT   28-JAN-2026, entry version 102.\nDE   RecName: Full=Cardiolipin synthetase {ECO:0000305};\nDE            Short=CL synthase {ECO:0000305};\nDE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};\nDE   Flags: Precursor;\nGN   Name=CLS {ECO:0000303|PubMed:22451910};\nGN   ORFNames=Tb04.1H19.1130 {ECO:0000312|EMBL:AAZ10847.1},\nGN   Tb927.4.2560 {ECO:0000312|EMBL:AAX79074.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 102,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Cardiolipin synthetase {ECO:0000305};\nDE            Short=CL synthase {ECO:0000305};\nDE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 102,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "source_locator": "lines 65-72",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=22451910; DOI=10.1073/pnas.1121528109;\nRA   Serricchio M., Buetikofer P.;\nRT   \"An essential bacterial-type cardiolipin synthase mediates cardiolipin\nRT   formation in a eukaryote.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 109:E954-E961(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 102,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "source_locator": "lines 88-92",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a\nCC         cardiolipin + glycerol; Xref=Rhea:RHEA:31451, ChEBI:CHEBI:17754,\nCC         ChEBI:CHEBI:62237, ChEBI:CHEBI:64716;\nCC         Evidence={ECO:0000305|PubMed:22451910};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 102,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
