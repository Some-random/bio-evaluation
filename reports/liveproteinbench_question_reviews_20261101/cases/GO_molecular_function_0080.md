# GO_molecular_function_0080

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — methyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNGREHRRGDEAARREARSILFQNQDRSIVLIDVPTSIEEAQASPEEVGCDAGPLRKRRRLISSEPPHLPFKTPEPKAGSGGLTESVSDLMIAAAATEALRVLQESYAGPFCLPRVTRPNPLKSAFVPKGSFFLHGTVSSERDRFAAEAPVFDLIVLDPPWPNRSARRKQRNYRVADSLGSIRETLSLIPIAAHLAPDGLLAVWITNKAGVVELLTGPRGLFAQWGLEQVDEWTWLKITTSGEPIVDVGSTWRKPWERILIARRRGSSRKPACRGRVLVSVPDLHSRKPNLRGLFEDVLVPSNKGLEIFARNLTAGWWSWGDEVLKFQQPEYWVES

[Multiple Choices]
A. methyltransferase activity
B. spheroidene monooxygenase activity
C. iron ion binding
D. alpha-1,2-mannosyltransferase activity
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

> The sequence exactly matches a UniProt entry for an N6-methyladenosine RNA methyltransferase. Its annotated catalytic reaction transfers a methyl group to adenosine in mRNA, making the broader option A scientifically appropriate. The current record includes experimental-evidence-coded function, reaction, and GO annotations; the historical record also names the enzyme and cites experimental studies, though its GO line uses an IEA code.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a DPPW motif in a soluble enzyme-sized protein. This is a characteristic catalytic motif of the MT-A70 family of N6-adenosine RNA methyltransferases, supporting methyltransferase activity over the listed oxygenase and mannosyltransferase alternatives; the sequence has no obvious transmembrane segments suggesting a membrane-bound glycan-processing enzyme.


**Missing item-specific fact**

> Identifying the exact mRNA N6-methyladenosine substrate and biological role would require protein-specific annotation or experimental evidence, but that specificity is not required for the broad methyltransferase choice.


**Reason**

> The sequence motif provides a concrete family-level clue relevant to choice A rather than relying only on recognition of the exact protein or an external database lookup. It supports the broad activity, although it does not establish all protein-specific details.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimentally annotated methyl-transfer reaction fits option A. The other options describe distinct catalytic activities or iron binding, and the supplied evidence does not support them as this protein's primary molecular function.


### Important caveats

- The sequence-to-entry match and experimental annotations are reviewer-only evidence, not information supplied to the evaluated model.
- The evidence supports broad methyltransferase activity; the exact RNA substrate specificity is more specific than option A.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a soluble enzyme-sized protein. This is a characteristic catalytic motif of the MT-A70 family of N6-adenosine RNA methyltransferases, supporting methyltransferase activity over the listed oxygenase and mannosyltransferase alternatives; the sequence has no obvious transmembrane segments suggesting a membrane-bound glycan-processing enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying the exact mRNA N6-methyladenosine substrate and biological role would require protein-specific annotation or experimental evidence, but that specificity is not required for the broad methyltransferase choice.",
    "reason": "The sequence motif provides a concrete family-level clue relevant to choice A rather than relying only on recognition of the exact protein or an external database lookup. It supports the broad activity, although it does not establish all protein-specific details."
  },
  "case_id": "GO_molecular_function_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry for an N6-methyladenosine RNA methyltransferase. Its annotated catalytic reaction transfers a methyl group to adenosine in mRNA, making the broader option A scientifically appropriate. The current record includes experimental-evidence-coded function, reaction, and GO annotations; the historical record also names the enzyme and cites experimental studies, though its GO line uses an IEA code."
  },
  "important_caveats": [
    "The sequence-to-entry match and experimental annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The evidence supports broad methyltransferase activity; the exact RNA substrate specificity is more specific than option A."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally annotated methyl-transfer reaction fits option A. The other options describe distinct catalytic activities or iron binding, and the supplied evidence does not support them as this protein's primary molecular function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry for an N6-methyladenosine RNA methyltransferase. Its annotated catalytic reaction transfers a methyl group to adenosine in mRNA, making the broader option A scientifically appropriate. The current record includes experimental-evidence-coded function, reaction, and GO annotations; the historical record also names the enzyme and cites experimental studies, though its GO line uses an IEA code.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a DPPW motif in a soluble enzyme-sized protein. This is a characteristic catalytic motif of the MT-A70 family of N6-adenosine RNA methyltransferases, supporting methyltransferase activity over the listed oxygenase and mannosyltransferase alternatives; the sequence has no obvious transmembrane segments suggesting a membrane-bound glycan-processing enzyme.",
    "missing_item_specific_fact": "Identifying the exact mRNA N6-methyladenosine substrate and biological role would require protein-specific annotation or experimental evidence, but that specificity is not required for the broad methyltransferase choice.",
    "reason": "The sequence motif provides a concrete family-level clue relevant to choice A rather than relying only on recognition of the exact protein or an external database lookup. It supports the broad activity, although it does not establish all protein-specific details."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally annotated methyl-transfer reaction fits option A. The other options describe distinct catalytic activities or iron binding, and the supplied evidence does not support them as this protein's primary molecular function."
  },
  "important_caveats": [
    "The sequence-to-entry match and experimental annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The evidence supports broad methyltransferase activity; the exact RNA substrate specificity is more specific than option A."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A9P5CQV5 (MTA1_CRYP1), experimentally annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with GO:0001734 (mRNA m(6)A methyltransferase activity) supported by ECO:0000269 (experimental evidence from PubMed:39159278 and PubMed:39611846). GO:0001734 is_a GO:0008174 (mRNA methyltransferase activity) is_a GO:0008173 (RNA methyltransferase activity) is_a GO:0008168 (methyltransferase activity), so option A is a valid ancestor term. The catalytic reaction (adenosine + SAM → N6-methyladenosine + SAH + H+) is a methyltransferase reaction. The other options (spheroidene monooxygenase, iron ion binding, alpha-1,2-mannosyltransferase) are not annotated for this entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO4](#evidence-go4), [GO5](#evidence-go5), [GO6](#evidence-go6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (spheroidene monooxygenase, GO:0043823) and D (alpha-1,2-mannosyltransferase, GO:0000026) can be eliminated by general biological knowledge: spheroidene monooxygenase is a carotenoid-modifying P450-type enzyme found in photosynthetic bacteria (Rhodobacter), not a plausible function for a fungal protein lacking heme-binding Cys-rich motifs; alpha-1,2-mannosyltransferase is an ER membrane glycosyltransferase involved in N-glycan biosynthesis with distinct transmembrane and catalytic motifs absent here. Between A and C, the 336-aa compact soluble protein lacks dedicated multi-residue iron-coordination motifs (no HxH, CxxC, or DxE clusters typical of iron-binding sites) and its size/composition is more consistent with a small catalytic enzyme than a dedicated metal-binding protein. Methyltransferase activity is the most abundant catalytic class among small soluble enzymes, making A the best-supported choice among the four options.


**Missing item-specific fact**

> Positive identification as an m6A methyltransferase specifically (rather than another methyltransferase subclass) requires recognizing the METTL3-like Rossmann-fold architecture, which is not trivially obvious from this fungal homolog sequence. However, the question asks only for 'methyltransferase activity' (the broad parent term), which is achievable through elimination of clearly incompatible options.


**Reason**

> The question provides four options spanning very different enzyme classes. General biological knowledge about organism context (fungal vs. bacterial carotenoid enzymes), subcellular localization (ER membrane glycosyltransferases), and protein architecture (absence of heme or glycosyltransferase motifs) meaningfully eliminates B and D. The remaining choice between A and C is supported by the protein's enzymatic character and the statistical prevalence of methyltransferases among small soluble proteins. While positive motif-level confirmation of methyltransferase identity would require fold recognition, the elimination-based reasoning is sufficient to distinguish the correct answer from the distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with the protein's identity and context. Option A (methyltransferase activity) is the broad parent term encompassing the experimentally verified m6A methyltransferase function. No other option is defensible.


### Important caveats

- The expected answer 'methyltransferase activity' (GO:0008168) is a broad parent term; the protein's most specific annotation is GO:0001734 (mRNA m(6)A methyltransferase activity). The question tests recognition at the parent-term level, which is valid but less specific.
- The sequence lacks the most textbook-obvious SAM-binding motifs (e.g., VLDVG), making positive motif-level identification of methyltransferase activity non-trivial from sequence alone; the reasoning relies more on elimination of incompatible options.
- The UniProt entry was first public in April 2025; the benchmark author's source snapshot is unknown. The historical entry (version 12, released Jan 2026) already contains the experimental annotations, so timing is unlikely to be an issue.
- Iron ion binding (option C) is a very generic term; many enzymes incidentally bind metals. Its elimination relies on the absence of dedicated multi-residue coordination sites, which is a reasonable but not absolute argument from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (spheroidene monooxygenase, GO:0043823) and D (alpha-1,2-mannosyltransferase, GO:0000026) can be eliminated by general biological knowledge: spheroidene monooxygenase is a carotenoid-modifying P450-type enzyme found in photosynthetic bacteria (Rhodobacter), not a plausible function for a fungal protein lacking heme-binding Cys-rich motifs; alpha-1,2-mannosyltransferase is an ER membrane glycosyltransferase involved in N-glycan biosynthesis with distinct transmembrane and catalytic motifs absent here. Between A and C, the 336-aa compact soluble protein lacks dedicated multi-residue iron-coordination motifs (no HxH, CxxC, or DxE clusters typical of iron-binding sites) and its size/composition is more consistent with a small catalytic enzyme than a dedicated metal-binding protein. Methyltransferase activity is the most abundant catalytic class among small soluble enzymes, making A the best-supported choice among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification as an m6A methyltransferase specifically (rather than another methyltransferase subclass) requires recognizing the METTL3-like Rossmann-fold architecture, which is not trivially obvious from this fungal homolog sequence. However, the question asks only for 'methyltransferase activity' (the broad parent term), which is achievable through elimination of clearly incompatible options.",
    "reason": "The question provides four options spanning very different enzyme classes. General biological knowledge about organism context (fungal vs. bacterial carotenoid enzymes), subcellular localization (ER membrane glycosyltransferases), and protein architecture (absence of heme or glycosyltransferase motifs) meaningfully eliminates B and D. The remaining choice between A and C is supported by the protein's enzymatic character and the statistical prevalence of methyltransferases among small soluble proteins. While positive motif-level confirmation of methyltransferase identity would require fold recognition, the elimination-based reasoning is sufficient to distinguish the correct answer from the distractors."
  },
  "case_id": "GO_molecular_function_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO4",
      "GO5",
      "GO6",
      "H1",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P5CQV5 (MTA1_CRYP1), experimentally annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with GO:0001734 (mRNA m(6)A methyltransferase activity) supported by ECO:0000269 (experimental evidence from PubMed:39159278 and PubMed:39611846). GO:0001734 is_a GO:0008174 (mRNA methyltransferase activity) is_a GO:0008173 (RNA methyltransferase activity) is_a GO:0008168 (methyltransferase activity), so option A is a valid ancestor term. The catalytic reaction (adenosine + SAM → N6-methyladenosine + SAH + H+) is a methyltransferase reaction. The other options (spheroidene monooxygenase, iron ion binding, alpha-1,2-mannosyltransferase) are not annotated for this entry."
  },
  "important_caveats": [
    "The expected answer 'methyltransferase activity' (GO:0008168) is a broad parent term; the protein's most specific annotation is GO:0001734 (mRNA m(6)A methyltransferase activity). The question tests recognition at the parent-term level, which is valid but less specific.",
    "The sequence lacks the most textbook-obvious SAM-binding motifs (e.g., VLDVG), making positive motif-level identification of methyltransferase activity non-trivial from sequence alone; the reasoning relies more on elimination of incompatible options.",
    "The UniProt entry was first public in April 2025; the benchmark author's source snapshot is unknown. The historical entry (version 12, released Jan 2026) already contains the experimental annotations, so timing is unlikely to be an issue.",
    "Iron ion binding (option C) is a very generic term; many enzymes incidentally bind metals. Its elimination relies on the absence of dedicated multi-residue coordination sites, which is a reasonable but not absolute argument from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the protein's identity and context. Option A (methyltransferase activity) is the broad parent term encompassing the experimentally verified m6A methyltransferase function. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9P5CQV5 (MTA1_CRYP1), experimentally annotated as N6-methyladenosine RNA methyltransferase (EC 2.1.1.348) with GO:0001734 (mRNA m(6)A methyltransferase activity) supported by ECO:0000269 (experimental evidence from PubMed:39159278 and PubMed:39611846). GO:0001734 is_a GO:0008174 (mRNA methyltransferase activity) is_a GO:0008173 (RNA methyltransferase activity) is_a GO:0008168 (methyltransferase activity), so option A is a valid ancestor term. The catalytic reaction (adenosine + SAM → N6-methyladenosine + SAH + H+) is a methyltransferase reaction. The other options (spheroidene monooxygenase, iron ion binding, alpha-1,2-mannosyltransferase) are not annotated for this entry.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "GO1", "GO2", "GO4", "GO5", "GO6", "H1", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (spheroidene monooxygenase, GO:0043823) and D (alpha-1,2-mannosyltransferase, GO:0000026) can be eliminated by general biological knowledge: spheroidene monooxygenase is a carotenoid-modifying P450-type enzyme found in photosynthetic bacteria (Rhodobacter), not a plausible function for a fungal protein lacking heme-binding Cys-rich motifs; alpha-1,2-mannosyltransferase is an ER membrane glycosyltransferase involved in N-glycan biosynthesis with distinct transmembrane and catalytic motifs absent here. Between A and C, the 336-aa compact soluble protein lacks dedicated multi-residue iron-coordination motifs (no HxH, CxxC, or DxE clusters typical of iron-binding sites) and its size/composition is more consistent with a small catalytic enzyme than a dedicated metal-binding protein. Methyltransferase activity is the most abundant catalytic class among small soluble enzymes, making A the best-supported choice among the four options.",
    "missing_item_specific_fact": "Positive identification as an m6A methyltransferase specifically (rather than another methyltransferase subclass) requires recognizing the METTL3-like Rossmann-fold architecture, which is not trivially obvious from this fungal homolog sequence. However, the question asks only for 'methyltransferase activity' (the broad parent term), which is achievable through elimination of clearly incompatible options.",
    "reason": "The question provides four options spanning very different enzyme classes. General biological knowledge about organism context (fungal vs. bacterial carotenoid enzymes), subcellular localization (ER membrane glycosyltransferases), and protein architecture (absence of heme or glycosyltransferase motifs) meaningfully eliminates B and D. The remaining choice between A and C is supported by the protein's enzymatic character and the statistical prevalence of methyltransferases among small soluble proteins. While positive motif-level confirmation of methyltransferase identity would require fold recognition, the elimination-based reasoning is sufficient to distinguish the correct answer from the distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the protein's identity and context. Option A (methyltransferase activity) is the broad parent term encompassing the experimentally verified m6A methyltransferase function. No other option is defensible."
  },
  "important_caveats": [
    "The expected answer 'methyltransferase activity' (GO:0008168) is a broad parent term; the protein's most specific annotation is GO:0001734 (mRNA m(6)A methyltransferase activity). The question tests recognition at the parent-term level, which is valid but less specific.",
    "The sequence lacks the most textbook-obvious SAM-binding motifs (e.g., VLDVG), making positive motif-level identification of methyltransferase activity non-trivial from sequence alone; the reasoning relies more on elimination of incompatible options.",
    "The UniProt entry was first public in April 2025; the benchmark author's source snapshot is unknown. The historical entry (version 12, released Jan 2026) already contains the experimental annotations, so timing is unlikely to be an issue.",
    "Iron ion binding (option C) is a very generic term; many enzymes incidentally bind metals. Its elimination relies on the absence of dedicated multi-residue coordination sites, which is a reasonable but not absolute argument from sequence alone."
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

**Accession:** `A0A9P5CQV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
"A0A9P5CQV5"
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"M6A writer MTA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"}],"value":"2.1.1.348"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase MTA1"}}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase that plays a crucial role in fungal phenotypic traits, virulence, and stress tolerance (PubMed:39159278, PubMed:39611846). Mediates the methylation of mRNAs to produce N6-methyladenosine (m6A)-containing mRNAs (PubMed:39159278, PubMed:39611846). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (PubMed:39159278, PubMed:39611846). Mediates specifically acid phosphatase APHA mRNA stability through a YTHDF1-dependent m6A modification of the A1306, A1341, and A1666 key methylation modification sites (PubMed:39159278). Also mediates the stability of the transcription factor ZAP1 mRNA via modification of residue A1935 localized in the 3'UTR (PubMed:39611846)"}]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:55585"}}],"reaction":{"ecNumber":"2.1.1.348","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"name":"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:55584"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"id":"GO:0001734","properties":[{"key":"GoTerm","value":"F:mRNA m(6)A methyltransferase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
ID   MTA1_CRYP1              Reviewed;         336 AA.
AC   A0A9P5CQV5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-SEP-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};
DE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};
GN   Name=MTA1 {ECO:0000303|PubMed:39159278}; ORFNames=M406DRAFT_288717;
OS   Cryphonectria parasitica (strain ATCC 38755 / EP155).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;
OC   Cryphonectria-Endothia species complex; Cryphonectria.
OX   NCBI_TaxID=660469;
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 49-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
CC   -!- FUNCTION: N6-methyladenosine RNA methyltransferase that plays a crucial
CC       role in fungal phenotypic traits, virulence, and stress tolerance
CC       (PubMed:39159278, PubMed:39611846). Mediates the methylation of mRNAs
CC       to produce N6-methyladenosine (m6A)-containing mRNAs (PubMed:39159278,
CC       PubMed:39611846). M6A is a modification present at internal sites of
CC       mRNAs and some non-coding RNAs and plays a role in mRNA stability and
CC       processing (PubMed:39159278, PubMed:39611846). Mediates specifically
CC       acid phosphatase APHA mRNA stability through a YTHDF1-dependent m6A
CC       modification of the A1306, A1341, and A1666 key methylation
CC       modification sites (PubMed:39159278). Also mediates the stability of
CC       the transcription factor ZAP1 mRNA via modification of residue A1935
CC       localized in the 3'UTR (PubMed:39611846). {ECO:0000269|PubMed:39159278,
CC       ECO:0000269|PubMed:39611846}.
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 62-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-
CC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
DR   GO; GO:0001734; F:mRNA m(6)A methyltransferase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 282-294`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000026
name: alpha-1,2-mannosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->2) linkage." [GOC:mcc, PMID:10521541]
xref: Reactome:R-HSA-446187 "ALG11 transfers the fourth and fifth Man to the N-glycan precursor"
xref: Reactome:R-HSA-446215 "ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)6 (PP-Dol)1"
xref: Reactome:R-HSA-446216 "ALG9 transfers Man to N-glycan precursor (GlcNAc)2 (Man)8 (PP-Dol)1"
xref: Reactome:R-HSA-4551297 "Defective ALG11 does not transfer Man to the N-glycan precursor"
xref: Reactome:R-HSA-4720478 "Defective ALG9 does not add the seventh mannose to the N-glycan precursor"
xref: Reactome:R-HSA-9035514 "Defective ALG9 does not add the last mannose to the N-glycan precursor"
is_a: GO:0000030 ! mannosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 11223-11236`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0001734
name: mRNA m(6)A methyltransferase activity
namespace: molecular_function
def: "Catalysis of the reaction: an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + H+ + S-adenosyl-L-homocysteine. This activity is the methylation of adenines in mRNA with the consensus sequence RRACH, where R is a purine, and H is C, A, or U." [EC:2.1.1.348, GOC:hjd]
synonym: "mRNA (N6-adenosine)-methyltransferase activity" EXACT []
xref: EC:2.1.1.348
xref: MetaCyc:RXN-19346
xref: Reactome:R-HSA-72095 "Internal Methylation of mRNA"
xref: RHEA:55584
is_a: GO:0008174 ! mRNA methyltransferase activity
property_value: skos:exactMatch EC:2.1.1.348
property_value: skos:exactMatch RHEA:55584

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80267-80287`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008168
name: methyltransferase activity
namespace: molecular_function
alt_id: GO:0004480
def: "Catalysis of the transfer of a methyl group to an acceptor molecule." [ISBN:0198506732]
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_yeast
synonym: "methylase" BROAD []
xref: EC:2.1.1.-
xref: Reactome:R-HSA-212269 "DNMT1,3A,3B:PRC2 methylates cytosine and histone H3"
xref: Reactome:R-HSA-379387 "COMT transfers Met to DA to form 3MT"
xref: Reactome:R-HSA-379464 "COMT transfers Met to DOPAC to form HVA"
xref: Reactome:R-HSA-5333608 "GSSebGalNac is reduced and methylated to MeSebGalNac"
xref: Reactome:R-HSA-6800149 "N6AMT1:TRMT112 transfers CH3 group from AdoMet to MMAIII"
xref: Reactome:R-HSA-71286 "guanidinoacetate + S-adenosylmethionine => creatine + S-adenosylhomocysteine"
xref: Reactome:R-HSA-9710490 "The GSDME gene promoter is hypermethylated"
is_a: GO:0016741 ! transferase activity, transferring one-carbon groups
property_value: skos:exactMatch EC:2.1.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80322-80330`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008173
name: RNA methyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a methyl group from a donor to a nucleoside residue in an RNA molecule." [GOC:mah]
xref: Reactome:R-HSA-191784 "snRNA Cap hypermethylation"
is_a: GO:0008168 ! methyltransferase activity
is_a: GO:0140098 ! catalytic activity, acting on RNA

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80331-80338`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008174
name: mRNA methyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a methyl group from S-adenosyl-L-methionine to a nucleoside residue in an mRNA molecule." [GOC:mah]
is_a: GO:0008173 ! RNA methyltransferase activity
is_a: GO:0008757 ! S-adenosylmethionine-dependent methyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
