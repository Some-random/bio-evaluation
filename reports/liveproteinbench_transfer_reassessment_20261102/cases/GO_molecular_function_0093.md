# GO_molecular_function_0093: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0093.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **A** — endopeptidase inhibitor activity

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
MRLLWGLAWVFSFCASSLQKPRLLLFSPSVVNLGTPLSVGVQLLDAPPGQEVKGSVFLRNPKGGSCSPKKDFKLSSGDDFVLLSLEVPLEDVRSCGLFDLRRAPYIQLVAQSPWLRNTAFKATETQGVNLLYSSRRGHIFVQTDQPIYNPGQRVRYRVFALDQKMRPSTDFLTITVENSHGLRVLKKEIFTSTSILQDTFTIPDISEPGTWKISARFSDGLESNRSTHFEVKKYVLPNFEVKITPWKPYILMVPSNSDEIQLDIQARYIYGKPVQGVAYTRFALMDEQGKRTFLRGLETQAKLVEGRTHISISKDQFQAALDKINIGVRDLEGLRLYAATAVIESPGGEMEEAELTSWRFVSSAFSLDLSRTKRHLVPGAHFLLQALVREISGSEASNVIVKVSPTLVSGSDSQVLNVQQSTNRIGQVSISFPIPPTVTGLRLLVSAGSLYPMIARLTVQSPPSRGTGFLSIEPLDPRSPRVGDTFILNLQAVGIPAPTFSHYYYMIISRGQIMAMSREARRTVTSVSVLVDHQLAPSFYFVAYFYHQGHPVANSLLINIQPRDCEGKLQLKVVGAKEYHNGDMMKLRIQTDSKALVALGAVDTALYAVGGWSHKPLDMSKVFEVINSYNVGCGPGGGDDAPQVFQDAGLAFSDGDRLTQTREDLSCPKEKKSRQKRNVNFLKALSEKLGQYSSPDAKRCCQDGMTKLPMKRTCEQRAARVPQQACREPFLSCCKFAEDLRRNQTRSQAPLARKVRDMVNLIEEDDILVRTSFPENWLWRVEPVDSSKLLTVRLPDSMTTWEIHGVSLSKSKGLCVAKPTRVRVFRKFHLHLRLPISVRRFEQLELRPVLYNYLNDDKNVSVHVTPVEGLCMAGGGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKGTLDSSDSVSKILQIEKEGAIHREEIVYNLDPLNNLGQMLEIPGSSDPNIVPEGDFSTFVKVTASEPLETLGSEEALSPGGVASLLRLPGCAEQTMIYLAPTLTASNYLDRTKQWSKLSPETKDHAVHLIQKGHVRIQQFRKKDGSFGAWLHRDSSTWLTAFVLKILSLAQEQVGNSPEKLQETASWLLAQQLGDGSFHDPCPVIHRAMQGGLVGSNETVALTAFVVIALHHGLNVFREGHAKQLKNRVEASITKANSFLGQKASAGLLGAHAAAITAYALTLTKASEDLRNVAHNSLMAMAEETGENLYWGLVLGSQDKVVLRPADPRSPTEPVPQAPALWIETTAYALLHLLLREGKGKMADKAASWLTHQGNFHGAFRSTQDTVVTLDALSAYWIASHTTEEKALKVTLSSMGRNGLKTHVLHLNNHQVKGLEEELKFSLGSTISVKVEGNSKGTLKILRTYNVLDMKNTTCQDLQIEVKVTDAVEYAWSAYEDYEDDYNMPATDDPSVPLQPVTPLQLFEGRRSRRRREAPKVAEERESRVHYTVCIWRNGKLGLSGMAIADITLLSGFHALRADLEKLTSLSDRYVSHFETDGPHVLLYFDSVPTTRECVGFGASQEVVVGLVQPASAVLYDYYSPDHKCSVFYAAPTKSQLLATLCSGDVCQCAEGKCPRLLRSLERRVEDKDGYRMRFACYYHQVEYGFTVKVLREDGRAAFRFFESKITQVLHFRTDTMASIGQTRNFLSRTSCRLRLEPNKEYLIMGMDGETSDNKGDPQYLLDSNTWIEEMPSEQMCKSTRHRAACFQLKDFLMEFSSRGCQV

[Multiple Choices]
A. endopeptidase inhibitor activity
B. translation elongation factor activity
C. RNA binding
D. GTPase activity
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.

Citations as saved: [C1](#evidence-c1), [C12](#evidence-c12), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.


**Missing item-specific fact**

> The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.


**Reason**

> Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function.


### Important caveats

- The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.
- The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.
- UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.",
    "reason": "Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C12",
      "H9",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation."
  },
  "important_caveats": [
    "The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.",
    "UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.",
    "evidence_ids": ["C1", "C12", "H9", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.",
    "missing_item_specific_fact": "The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.",
    "reason": "Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function."
  },
  "important_caveats": [
    "The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.",
    "UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options.

Citations as saved: [C12](#evidence-c12), [H9](#evidence-h9), [GO4](#evidence-go4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.


**Missing item-specific fact**

> None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.


**Reason**

> A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices.


### Important caveats

- The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.
- If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.
- The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.",
    "reason": "A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C12",
      "H9",
      "GO4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.",
    "If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.",
    "The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options.",
    "evidence_ids": ["C12", "H9", "GO4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.",
    "reason": "A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.",
    "If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.",
    "The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns endopeptidase inhibitor activity, but the evidence code is IEA:InterPro, so this is a computational annotation rather than direct experimental evidence for this activity. The record also describes the protein as a non-enzymatic complement precursor, consistent with the assigned function but not itself a direct assay of inhibition.

Citations as saved: [C12](#evidence-c12), [C5](#evidence-c5), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence has an N-terminal signal peptide and is a very large, multidomain secreted protein with features characteristic of the complement C3/C4 and alpha-2-macroglobulin-related family. Transferable family knowledge associates this group with protease-trapping or inhibitory activity, making A a meaningful fit. The sequence does not suggest a translation elongation factor, an RNA-binding protein, or a canonical GTPase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level sequence pattern and its known protease-inhibitory mechanism provide a credible way to distinguish A among these choices without knowing this exact protein's recorded annotation. The inference is not equivalent to a direct activity assay or proof that inhibition is its sole or primary biological role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, the complement-family inference supports A; the other choices describe activities poorly matched to the sequence and protein-family context.


### Important caveats

- The specific GO annotation supporting the key is computational (IEA:InterPro), not direct experimental evidence for endopeptidase inhibition.
- The sequence and family features support a probabilistic functional inference; they do not establish that this is the protein's only or primary molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence has an N-terminal signal peptide and is a very large, multidomain secreted protein with features characteristic of the complement C3/C4 and alpha-2-macroglobulin-related family. Transferable family knowledge associates this group with protease-trapping or inhibitory activity, making A a meaningful fit. The sequence does not suggest a translation elongation factor, an RNA-binding protein, or a canonical GTPase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence pattern and its known protease-inhibitory mechanism provide a credible way to distinguish A among these choices without knowing this exact protein's recorded annotation. The inference is not equivalent to a direct activity assay or proof that inhibition is its sole or primary biological role."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C12",
      "C5",
      "H9",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns endopeptidase inhibitor activity, but the evidence code is IEA:InterPro, so this is a computational annotation rather than direct experimental evidence for this activity. The record also describes the protein as a non-enzymatic complement precursor, consistent with the assigned function but not itself a direct assay of inhibition."
  },
  "important_caveats": [
    "The specific GO annotation supporting the key is computational (IEA:InterPro), not direct experimental evidence for endopeptidase inhibition.",
    "The sequence and family features support a probabilistic functional inference; they do not establish that this is the protein's only or primary molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the complement-family inference supports A; the other choices describe activities poorly matched to the sequence and protein-family context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns endopeptidase inhibitor activity, but the evidence code is IEA:InterPro, so this is a computational annotation rather than direct experimental evidence for this activity. The record also describes the protein as a non-enzymatic complement precursor, consistent with the assigned function but not itself a direct assay of inhibition.",
    "evidence_ids": ["C12", "C5", "H9", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence has an N-terminal signal peptide and is a very large, multidomain secreted protein with features characteristic of the complement C3/C4 and alpha-2-macroglobulin-related family. Transferable family knowledge associates this group with protease-trapping or inhibitory activity, making A a meaningful fit. The sequence does not suggest a translation elongation factor, an RNA-binding protein, or a canonical GTPase.",
    "missing_item_specific_fact": "",
    "reason": "The family-level sequence pattern and its known protease-inhibitory mechanism provide a credible way to distinguish A among these choices without knowing this exact protein's recorded annotation. The inference is not equivalent to a direct activity assay or proof that inhibition is its sole or primary biological role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, the complement-family inference supports A; the other choices describe activities poorly matched to the sequence and protein-family context."
  },
  "important_caveats": [
    "The specific GO annotation supporting the key is computational (IEA:InterPro), not direct experimental evidence for endopeptidase inhibition.",
    "The sequence and family features support a probabilistic functional inference; they do not establish that this is the protein's only or primary molecular function."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0AAQ4VMX2, Complement C4-A, mouse) lists GO:0004866 (endopeptidase inhibitor activity) as a molecular function annotation. However, the evidence code is IEA:InterPro, meaning it is an automated annotation inferred from domain matching to the alpha-2-macroglobulin family, not experimental data. The protein's experimentally supported primary function (ECO:0000269, PubMed:32769120 and PubMed:8133084) is as a non-enzymatic complement component acting as an opsonin and convertase scaffold. The endopeptidase inhibitor annotation is one of several GO terms and is the weakest in evidence level. The key is technically supported by the database annotation but represents an automated family-level assignment rather than the protein's primary experimentally verified molecular function.

Citations as saved: [C12](#evidence-c12), [H9](#evidence-h9), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply several transferable inferences. First, the sequence is 1734 AA with an N-terminal signal peptide, indicating a large secreted protein—this immediately makes options B (translation elongation factor activity, typically 400-700 AA intracellular GTPases like EF-Tu/eEF1A) and D (GTPase activity, requiring conserved G1-G5 G-domain motifs such as GXXXXGK&#91;S/T&#93;, DXXG, NKXD) implausible; no such motifs are present. Option C (RNA binding) is also implausible for a large secreted protein lacking RRM, KH, or zinc-finger RNA-binding domains. Second, the sequence contains hallmarks of the alpha-2-macroglobulin (A2M) superfamily: the thioester motif region (e.g., GCGPGGGDDAPQ, GCMAGGG), the bait-region architecture, and the overall domain organization shared with C3, C4, C5, and A2M itself. Alpha-2-macroglobulin is a well-known endopeptidase inhibitor, and the A2M superfamily shares protease-binding domain features. By family-level inference, the remaining option A (endopeptidase inhibitor activity) is the only choice with a domain-architecture connection to the sequence. The elimination of B, C, D is straightforward from general biology, and the A2M-family connection provides a positive (if imperfect) link to A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (1) elimination of B, C, D based on general protein biology (size, localization, domain architecture) and (2) recognition of alpha-2-macroglobulin superfamily features in the sequence, which are shared with known protease inhibitors, provides a legitimate transferable reasoning path to select A among the four offered alternatives. This does not require knowing the specific database annotation for this exact C4 entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, B, C, and D are clearly incompatible with a 1734 AA secreted protein lacking GTPase, RNA-binding, or elongation-factor motifs. Only A has any domain-level justification via the A2M superfamily connection. While the 'primary molecular function' of C4 is more accurately complement binding/opsonin activity (not among the options), the question's four alternatives make A the only defensible choice.


### Important caveats

- The GO:0004866 annotation is IEA:InterPro (automated), not experimental. The protein's experimentally verified primary function is as a complement opsonin/convertase scaffold, not a protease inhibitor.
- The alpha-2-macroglobulin family includes both true protease inhibitors (A2M itself) and complement components (C3, C4, C5) whose protease-inhibitor role is vestigial or absent; C4 is primarily a substrate for complement proteases, not an inhibitor.
- The question asks for 'primary molecular function,' which is somewhat misleading since endopeptidase inhibitor activity is an automated annotation rather than the primary function, but it is the only option with any domain-level justification among the four choices.
- The GO term GO:0004866 lists 'alpha-2 macroglobulin' as a RELATED synonym, reinforcing the family-level connection used in the reasoning path.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable inferences. First, the sequence is 1734 AA with an N-terminal signal peptide, indicating a large secreted protein—this immediately makes options B (translation elongation factor activity, typically 400-700 AA intracellular GTPases like EF-Tu/eEF1A) and D (GTPase activity, requiring conserved G1-G5 G-domain motifs such as GXXXXGK[S/T], DXXG, NKXD) implausible; no such motifs are present. Option C (RNA binding) is also implausible for a large secreted protein lacking RRM, KH, or zinc-finger RNA-binding domains. Second, the sequence contains hallmarks of the alpha-2-macroglobulin (A2M) superfamily: the thioester motif region (e.g., GCGPGGGDDAPQ, GCMAGGG), the bait-region architecture, and the overall domain organization shared with C3, C4, C5, and A2M itself. Alpha-2-macroglobulin is a well-known endopeptidase inhibitor, and the A2M superfamily shares protease-binding domain features. By family-level inference, the remaining option A (endopeptidase inhibitor activity) is the only choice with a domain-architecture connection to the sequence. The elimination of B, C, D is straightforward from general biology, and the A2M-family connection provides a positive (if imperfect) link to A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) elimination of B, C, D based on general protein biology (size, localization, domain architecture) and (2) recognition of alpha-2-macroglobulin superfamily features in the sequence, which are shared with known protease inhibitors, provides a legitimate transferable reasoning path to select A among the four offered alternatives. This does not require knowing the specific database annotation for this exact C4 entry."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C12",
      "H9",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAQ4VMX2, Complement C4-A, mouse) lists GO:0004866 (endopeptidase inhibitor activity) as a molecular function annotation. However, the evidence code is IEA:InterPro, meaning it is an automated annotation inferred from domain matching to the alpha-2-macroglobulin family, not experimental data. The protein's experimentally supported primary function (ECO:0000269, PubMed:32769120 and PubMed:8133084) is as a non-enzymatic complement component acting as an opsonin and convertase scaffold. The endopeptidase inhibitor annotation is one of several GO terms and is the weakest in evidence level. The key is technically supported by the database annotation but represents an automated family-level assignment rather than the protein's primary experimentally verified molecular function."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (automated), not experimental. The protein's experimentally verified primary function is as a complement opsonin/convertase scaffold, not a protease inhibitor.",
    "The alpha-2-macroglobulin family includes both true protease inhibitors (A2M itself) and complement components (C3, C4, C5) whose protease-inhibitor role is vestigial or absent; C4 is primarily a substrate for complement proteases, not an inhibitor.",
    "The question asks for 'primary molecular function,' which is somewhat misleading since endopeptidase inhibitor activity is an automated annotation rather than the primary function, but it is the only option with any domain-level justification among the four choices.",
    "The GO term GO:0004866 lists 'alpha-2 macroglobulin' as a RELATED synonym, reinforcing the family-level connection used in the reasoning path."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, B, C, and D are clearly incompatible with a 1734 AA secreted protein lacking GTPase, RNA-binding, or elongation-factor motifs. Only A has any domain-level justification via the A2M superfamily connection. While the 'primary molecular function' of C4 is more accurately complement binding/opsonin activity (not among the options), the question's four alternatives make A the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAQ4VMX2, Complement C4-A, mouse) lists GO:0004866 (endopeptidase inhibitor activity) as a molecular function annotation. However, the evidence code is IEA:InterPro, meaning it is an automated annotation inferred from domain matching to the alpha-2-macroglobulin family, not experimental data. The protein's experimentally supported primary function (ECO:0000269, PubMed:32769120 and PubMed:8133084) is as a non-enzymatic complement component acting as an opsonin and convertase scaffold. The endopeptidase inhibitor annotation is one of several GO terms and is the weakest in evidence level. The key is technically supported by the database annotation but represents an automated family-level assignment rather than the protein's primary experimentally verified molecular function.",
    "evidence_ids": ["C12", "H9", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable inferences. First, the sequence is 1734 AA with an N-terminal signal peptide, indicating a large secreted protein—this immediately makes options B (translation elongation factor activity, typically 400-700 AA intracellular GTPases like EF-Tu/eEF1A) and D (GTPase activity, requiring conserved G1-G5 G-domain motifs such as GXXXXGK[S/T], DXXG, NKXD) implausible; no such motifs are present. Option C (RNA binding) is also implausible for a large secreted protein lacking RRM, KH, or zinc-finger RNA-binding domains. Second, the sequence contains hallmarks of the alpha-2-macroglobulin (A2M) superfamily: the thioester motif region (e.g., GCGPGGGDDAPQ, GCMAGGG), the bait-region architecture, and the overall domain organization shared with C3, C4, C5, and A2M itself. Alpha-2-macroglobulin is a well-known endopeptidase inhibitor, and the A2M superfamily shares protease-binding domain features. By family-level inference, the remaining option A (endopeptidase inhibitor activity) is the only choice with a domain-architecture connection to the sequence. The elimination of B, C, D is straightforward from general biology, and the A2M-family connection provides a positive (if imperfect) link to A.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) elimination of B, C, D based on general protein biology (size, localization, domain architecture) and (2) recognition of alpha-2-macroglobulin superfamily features in the sequence, which are shared with known protease inhibitors, provides a legitimate transferable reasoning path to select A among the four offered alternatives. This does not require knowing the specific database annotation for this exact C4 entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, B, C, and D are clearly incompatible with a 1734 AA secreted protein lacking GTPase, RNA-binding, or elongation-factor motifs. Only A has any domain-level justification via the A2M superfamily connection. While the 'primary molecular function' of C4 is more accurately complement binding/opsonin activity (not among the options), the question's four alternatives make A the only defensible choice."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (automated), not experimental. The protein's experimentally verified primary function is as a complement opsonin/convertase scaffold, not a protease inhibitor.",
    "The alpha-2-macroglobulin family includes both true protease inhibitors (A2M itself) and complement components (C3, C4, C5) whose protease-inhibitor role is vestigial or absent; C4 is primarily a substrate for complement proteases, not an inhibitor.",
    "The question asks for 'primary molecular function,' which is somewhat misleading since endopeptidase inhibitor activity is an automated annotation rather than the primary function, but it is the only option with any domain-level justification among the four choices.",
    "The GO term GO:0004866 lists 'alpha-2 macroglobulin' as a RELATED synonym, reinforcing the family-level connection used in the reasoning path."
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
  "requested_accession": "A0AAQ4VMX2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "566440192a77f7efc8370aceaea038f1454f2abc74fa9b7b1b1236c996c02193",
  "benchmark_sequence_length": 1734,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 8,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-10-02",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "current_source_sequence_sha256": "566440192a77f7efc8370aceaea038f1454f2abc74fa9b7b1b1236c996c02193",
  "current_source_sequence_length": 1734,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 6,
  "selected_historical_version": {
    "accession": "A0AAQ4VMX2",
    "database": "Swiss-Prot",
    "entryVersion": 6,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CO4A_MOUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "selected_historical_source_sequence_sha256": "566440192a77f7efc8370aceaea038f1454f2abc74fa9b7b1b1236c996c02193",
  "selected_historical_source_sequence_length": 1734,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 6,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0AAQ4VMX2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":8,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-10-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"6208559\",\"source\":\"PubMed\"}],\"value\":\"Sex-limited protein\"}}],\"contains\":[{\"recommendedName\":{\"fullName\":{\"value\":\"Complement C4 beta chain\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Complement C4-A alpha chain\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"C4a anaphylatoxin\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Complement C4b-A\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Complement C4 gamma chain\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"value\":\"Complement C4-A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32769120\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"8133084\",\"source\":\"PubMed\"}],\"value\":\"Precursor of non-enzymatic components of the classical, lectin and GZMK complement pathways, which consist in a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"Complement C4b-A\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0L4\",\"source\":\"UniProtKB\"}],\"value\":\"Non-enzymatic component of C3 and C5 convertases (By similarity). Generated following cleavage by complement proteases (C1S, MASP2 or GZMK, depending on the complement pathway), it covalently attaches to the surface of pathogens, where it acts as an opsonin that marks the surface of antigens for removal (By similarity). It then recruits the serine protease complement C2b to form the C3 and C5 convertases, which cleave and activate C3 and C5, respectively, the next components of the complement pathways (By similarity). Complement C4b-A isotype is responsible for effective binding to form amide bonds with immune aggregates or protein antigens, while complement C4b-B isotype catalyzes the transacylation of the thioester carbonyl group to form ester bonds with carbohydrate antigens (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"C4a anaphylatoxin\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C0L4\",\"source\":\"UniProtKB\"}],\"value\":\"Putative humoral mediator released following cleavage by complement proteases (C1S, MASP2 or GZMK, depending on the complement pathway). While it is strongly similar to anaphylatoxins, its role is unclear. Was reported to act as a mediator of local inflammatory process; however these effects were probably due to contamination with C3a and/C5a anaphylatoxins in biological assays\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/uniProtKBCrossReferences/29",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003823\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:antigen binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/uniProtKBCrossReferences/30",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030246\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:carbohydrate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/uniProtKBCrossReferences/31",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0001848\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:complement binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/uniProtKBCrossReferences/32",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0001849\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:complement component C1q complex binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/uniProtKBCrossReferences/33",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004866\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endopeptidase inhibitor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Nonaka M.\",\"Takahashi M.\",\"Natsuume-Sakai S.\",\"Nonaka M.\",\"Tanaka S.\",\"Shimizu A.\",\"Honjo T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"6208559\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.81.21.6822\"}],\"citationType\":\"journal article\",\"firstPage\":\"6822\",\"id\":\"6208559\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"6826\",\"publicationDate\":\"1984\",\"title\":\"Isolation of cDNA clones specifying the fourth component of mouse complement and its isotype, sex-limited protein.\",\"volume\":\"81\"},\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] OF 20-1734\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Van den Berg C.W.\",\"Van Dijk H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"8133084\"},{\"database\":\"DOI\",\"id\":\"10.1016/0022-1759(94)90269-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"251\",\"id\":\"8133084\",\"journal\":\"J. Immunol. Methods\",\"lastPage\":\"256\",\"publicationDate\":\"1994\",\"title\":\"Rapid, activity-guided isolation of sex-limited protein (Slp) from mouse serum by fractionated precipitation and high-performance liquid chromatography.\",\"volume\":\"169\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json",
  "source_sha256": "ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be",
  "retrieved_utc": "2026-11-02T04:26:29.030340+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zarantonello A.\",\"Presumey J.\",\"Simoni L.\",\"Yalcin E.\",\"Fox R.\",\"Hansen A.\",\"Olesen H.G.\",\"Thiel S.\",\"Johnson M.B.\",\"Stevens B.\",\"Laursen N.S.\",\"Carroll M.C.\",\"Andersen G.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32769120\"},{\"database\":\"DOI\",\"id\":\"10.4049/jimmunol.2000528\"}],\"citationType\":\"journal article\",\"firstPage\":\"1678\",\"id\":\"32769120\",\"journal\":\"J. Immunol.\",\"lastPage\":\"1694\",\"publicationDate\":\"2020\",\"title\":\"An ultrahigh-affinity complement C4b-specific nanobody inhibits in vivo assembly of the classical pathway proconvertase.\",\"volume\":\"205\"},\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 1-25",
  "excerpt": "ID   CO4A_MOUSE              Reviewed;        1734 AA.\nAC   A0AAQ4VMX2; B9EIU2; Q6P3Y0; V9GZG9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-OCT-2024, sequence version 1.\nDT   28-JAN-2026, entry version 6.\nDE   RecName: Full=Complement C4-A;\nDE   AltName: Full=Sex-limited protein {ECO:0000303|PubMed:6208559};\nDE   Contains:\nDE     RecName: Full=Complement C4 beta chain;\nDE   Contains:\nDE     RecName: Full=Complement C4-A alpha chain;\nDE   Contains:\nDE     RecName: Full=C4a anaphylatoxin;\nDE   Contains:\nDE     RecName: Full=Complement C4b-A;\nDE   Contains:\nDE     RecName: Full=Complement C4 gamma chain;\nDE   Flags: Precursor;\nGN   Name=C4a {ECO:0000312|MGI:MGI:98320};\nGN   Synonyms=Slp {ECO:0000303|PubMed:6208559};\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 39-46",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA] OF 20-1734.\nRX   PubMed=6208559; DOI=10.1073/pnas.81.21.6822;\nRA   Nonaka M., Takahashi M., Natsuume-Sakai S., Nonaka M., Tanaka S.,\nRA   Shimizu A., Honjo T.;\nRT   \"Isolation of cDNA clones specifying the fourth component of mouse\nRT   complement and its isotype, sex-limited protein.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 81:6822-6826(1984).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 70-77",
  "excerpt": "RN   [6]\nRP   FUNCTION.\nRX   PubMed=8133084; DOI=10.1016/0022-1759(94)90269-0;\nRA   Van den Berg C.W., Van Dijk H.;\nRT   \"Rapid, activity-guided isolation of sex-limited protein (Slp) from mouse\nRT   serum by fractionated precipitation and high-performance liquid\nRT   chromatography.\";\nRL   J. Immunol. Methods 169:251-256(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 78-86",
  "excerpt": "RN   [7]\nRP   FUNCTION, AND ACTIVITY REGULATION.\nRX   PubMed=32769120; DOI=10.4049/jimmunol.2000528;\nRA   Zarantonello A., Presumey J., Simoni L., Yalcin E., Fox R., Hansen A.,\nRA   Olesen H.G., Thiel S., Johnson M.B., Stevens B., Laursen N.S.,\nRA   Carroll M.C., Andersen G.R.;\nRT   \"An ultrahigh-affinity complement C4b-specific nanobody inhibits in vivo\nRT   assembly of the classical pathway proconvertase.\";\nRL   J. Immunol. 205:1678-1694(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 87-91",
  "excerpt": "CC   -!- FUNCTION: Precursor of non-enzymatic components of the classical,\nCC       lectin and GZMK complement pathways, which consist in a cascade of\nCC       proteins that leads to phagocytosis and breakdown of pathogens and\nCC       signaling that strengthens the adaptive immune system.\nCC       {ECO:0000269|PubMed:32769120, ECO:0000269|PubMed:8133084}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 92-104",
  "excerpt": "CC   -!- FUNCTION: [Complement C4b-A]: Non-enzymatic component of C3 and C5\nCC       convertases (By similarity). Generated following cleavage by complement\nCC       proteases (C1S, MASP2 or GZMK, depending on the complement pathway), it\nCC       covalently attaches to the surface of pathogens, where it acts as an\nCC       opsonin that marks the surface of antigens for removal (By similarity).\nCC       It then recruits the serine protease complement C2b to form the C3 and\nCC       C5 convertases, which cleave and activate C3 and C5, respectively, the\nCC       next components of the complement pathways (By similarity). Complement\nCC       C4b-A isotype is responsible for effective binding to form amide bonds\nCC       with immune aggregates or protein antigens, while complement C4b-B\nCC       isotype catalyzes the transacylation of the thioester carbonyl group to\nCC       form ester bonds with carbohydrate antigens (By similarity).\nCC       {ECO:0000250|UniProtKB:P0C0L4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 105-111",
  "excerpt": "CC   -!- FUNCTION: [C4a anaphylatoxin]: Putative humoral mediator released\nCC       following cleavage by complement proteases (C1S, MASP2 or GZMK,\nCC       depending on the complement pathway). While it is strongly similar to\nCC       anaphylatoxins, its role is unclear. Was reported to act as a mediator\nCC       of local inflammatory process; however these effects were probably due\nCC       to contamination with C3a and/C5a anaphylatoxins in biological assays.\nCC       {ECO:0000250|UniProtKB:P0C0L4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 199-199",
  "excerpt": "DR   GO; GO:0003823; F:antigen binding; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6",
  "source_sha256": "b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9",
  "retrieved_utc": "2026-11-02T04:26:31.699377+00:00",
  "source_locator": "lines 200-200",
  "excerpt": "DR   GO; GO:0004866; F:endopeptidase inhibitor activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 6,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 28242-28268",
  "excerpt": "[Term]\nid: GO:0003723\nname: RNA binding\nnamespace: molecular_function\nalt_id: GO:0000498\nalt_id: GO:0044822\ndef: \"Binding to an RNA molecule or a portion thereof.\" [GOC:jl, GOC:mah]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"base pairing with RNA\" NARROW []\nsynonym: \"poly(A) RNA binding\" RELATED []\nsynonym: \"poly(A)-RNA binding\" RELATED []\nsynonym: \"poly-A RNA binding\" RELATED []\nxref: Reactome:R-HSA-203922 \"Exportin-5 recognizes 3' overhang of pre-miRNA\"\nis_a: GO:0003676 ! nucleic acid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003723"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 28414-28424",
  "excerpt": "[Term]\nid: GO:0003746\nname: translation elongation factor activity\nnamespace: molecular_function\nalt_id: GO:0008182\nalt_id: GO:0008183\ndef: \"Functions in chain elongation during polypeptide synthesis at the ribosome.\" [ISBN:0198506732]\nxref: Reactome:R-HSA-192704 \"Synthesis of PB1-F2\"\nxref: Reactome:R-HSA-192841 \"Viral Protein Synthesis\"\nis_a: GO:0180051 ! translation factor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003746"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 31441-31534",
  "excerpt": "[Term]\nid: GO:0003924\nname: GTPase activity\nnamespace: molecular_function\nalt_id: GO:0061745\ndef: \"Catalysis of the reaction: GTP + H2O = GDP + H+ + phosphate.\" [PMID:26832457, PMID:27218782]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nsynonym: \"ARF small monomeric GTPase activity\" NARROW []\nsynonym: \"dynamin GTPase activity\" NARROW []\nsynonym: \"GTPase activity, coupled\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase activity\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, alpha-subunit\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, beta-subunit\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, gamma-subunit\" RELATED []\nsynonym: \"hydrolase activity, acting on acid anhydrides, acting on GTP, involved in cellular and subcellular movement\" BROAD []\nsynonym: \"protein-synthesizing GTPase activity\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, elongation\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, initiation\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, termination\" NARROW []\nsynonym: \"Rab small monomeric GTPase activity\" NARROW []\nsynonym: \"Ran small monomeric GTPase activity\" NARROW []\nsynonym: \"Ras small monomeric GTPase activity\" NARROW []\nsynonym: \"RHEB small monomeric GTPase activity\" NARROW []\nsynonym: \"Rho small monomeric GTPase activity\" NARROW []\nsynonym: \"Sar small monomeric GTPase activity\" NARROW []\nsynonym: \"signal-recognition-particle GTPase activity\" NARROW []\nsynonym: \"small monomeric GTPase activity\" NARROW []\nsynonym: \"tubulin GTPase activity\" NARROW []\nxref: MetaCyc:RXN0-5462\nxref: Reactome:R-HSA-1445143 \"RAB8A,10,13,14 hydrolyze GTP\"\nxref: Reactome:R-HSA-1458485 \"RALA hydrolyzes GTP\"\nxref: Reactome:R-HSA-156923 \"Hydrolysis of eEF1A:GTP\"\nxref: Reactome:R-HSA-164381 \"G alpha (s) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-165055 \"Hydrolysis of Ran:GTP to Ran:GDP\"\nxref: Reactome:R-HSA-167415 \"G-protein alpha subunit is inactivated\"\nxref: Reactome:R-HSA-170666 \"Adenylate cyclase increases the GTPase activity of G alpha-olf\"\nxref: Reactome:R-HSA-170685 \"Adenylaye cyclase increases the GTPase activity of G alpha-olf\"\nxref: Reactome:R-HSA-170686 \"Adenylate cyclase increases the GTPase activity of Gi alpha\"\nxref: Reactome:R-HSA-177501 \"Endocytosis (internalization) of clathrin-coated vesicle\"\nxref: Reactome:R-HSA-203973 \"Vesicle budding\"\nxref: Reactome:R-HSA-2130641 \"Translocation of TGN-lysosome vesicle to lysosome\"\nxref: Reactome:R-HSA-2130725 \"Internalization of MHC II:Ii clathrin coated vesicle\"\nxref: Reactome:R-HSA-2584246 \"GNAT1-GTP hydrolyses its bound GTP to GDP\"\nxref: Reactome:R-HSA-380979 \"RHEB in mTORC1:RHEB:GTP hydrolyses GTP\"\nxref: Reactome:R-HSA-392133 \"G alpha (z) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-392212 \"G alpha (i) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-418574 \"G alpha (12/13) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-418582 \"G alpha (q) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-421835 \"trans-Golgi Network Vesicle Scission\"\nxref: Reactome:R-HSA-428941 \"P2Y purinoceptor 1 activates MAP kinase p38 alpha\"\nxref: Reactome:R-HSA-432707 \"trans-Golgi Network Lysosomal Vesicle Scission\"\nxref: Reactome:R-HSA-5333615 \"80S:Met-tRNAi:mRNA:SECISBP2:Sec-tRNA(Sec):EEFSEC:GTP is hydrolysed to 80S:Met-tRNAi:mRNA:SECISBP2:Sec and EEFSEC:GDP by EEFSEC\"\nxref: Reactome:R-HSA-5389839 \"39S subunit binds 28S subunit:mRNA:fMet-tRNA\"\nxref: Reactome:R-HSA-5389842 \"TUFM hydrolyzes GTP and TUFM:GDP dissociates from 55S ribosome\"\nxref: Reactome:R-HSA-5419273 \"Hydrolysis of GTP and dissociation of 28S and 39S subunits\"\nxref: Reactome:R-HSA-5419279 \"Translocation of peptidyl-tRNA from A-site to P-site (and translocation of 55S ribosome by 3 bases along mRNA)\"\nxref: Reactome:R-HSA-555065 \"Formation of clathrin coated vesicle\"\nxref: Reactome:R-HSA-5623513 \"ASAP1 stimulates GTPase activity of ARF4\"\nxref: Reactome:R-HSA-5638006 \"ARL3 hydrolyzes GTP\"\nxref: Reactome:R-HSA-5658231 \"RAS GAPs stimulate RAS GTPase activity\"\nxref: Reactome:R-HSA-5665809 \"SRGAP2 stimulates RAC1 GTP-ase activity and ends FMNL1-mediated elongation of actin filaments\"\nxref: Reactome:R-HSA-5672017 \"Rheb in the MTORC1 complex hydrolyses GTP\"\nxref: Reactome:R-HSA-5694527 \"Loss of SAR1B GTPase\"\nxref: Reactome:R-HSA-6807877 \"ARFGAPs stimulate ARF GTPase activity\"\nxref: Reactome:R-HSA-6814833 \"TBC1D20 stimulates GTPase activity of RAB1, resulting in hydrolysis of GTP\"\nxref: Reactome:R-HSA-8847534 \"RAB43 hydrolyses GTP\"\nxref: Reactome:R-HSA-8847883 \"CYTH proteins stimulate ARF1 GTPase activity\"\nxref: Reactome:R-HSA-8849082 \"ARHGAP35 stimulates RHOA GTPase activity\"\nxref: Reactome:R-HSA-8854173 \"TBC RabGAPs accelerate GTP hydrolysis by RAB35\"\nxref: Reactome:R-HSA-8854255 \"TBC1D2A accelerates GTP hydrolysis by RAB7\"\nxref: Reactome:R-HSA-8854329 \"TBC1D15 accelerates GTP hydrolysis by RAB7\"\nxref: Reactome:R-HSA-8854604 \"TBC1D16 accelerates GTP hydrolysis by RAB4A\"\nxref: Reactome:R-HSA-8854612 \"TBC1D25 accelerates GTP hydrolysis by RAB33B\"\nxref: Reactome:R-HSA-8868661 \"Dynamin-mediated GTP hydrolysis promotes vesicle scission\"\nxref: Reactome:R-HSA-8981353 \"RASA1 stimulates RAS GTPase activity\"\nxref: Reactome:R-HSA-8982020 \"G alpha (i)i1/i2/i3 in G (i):RGS complex is inactivated\"\nxref: Reactome:R-HSA-8982021 \"G alpha (z) in G alpha (z):RGS complex is inactivated\"\nxref: Reactome:R-HSA-8982025 \"G alpha (q) in G (q):RGS complex is inactivated\"\nxref: Reactome:R-HSA-9018814 \"RHOT1 hydrolyzes GTP\"\nxref: Reactome:R-HSA-9018826 \"RHOT2 hydrolyzes GTP\"\nxref: Reactome:R-HSA-9640195 \"RRAGA,B hydrolyzes GTP\"\nxref: Reactome:R-HSA-9645598 \"RRAGC,D hydrolyzes GTP\"\nxref: Reactome:R-HSA-9649736 \"RAS intrinsic GTPase activity hydrolyzes GTP to GDP\"\nxref: Reactome:R-HSA-983422 \"Disassembly of COPII coated vesicle\"\nxref: Reactome:R-HSA-9947842 \"GBP1 hydrolyzes GTP forming GBP1 oligomers\"\nxref: Reactome:R-HSA-9954919 \"ABCE1:ATP binds PELO:HBS1L-1:GTP:80S ribosome:non-stop mRNA:peptidyl-tRNA with nascent peptide and HBS1L-1:GDP is released\"\nxref: RHEA:19669\nis_a: GO:0017111 ! ribonucleoside triphosphate phosphatase activity\nproperty_value: skos:exactMatch RHEA:19669\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003924"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 51565-51575",
  "excerpt": "[Term]\nid: GO:0004866\nname: endopeptidase inhibitor activity\nnamespace: molecular_function\ndef: \"Binds to and stops, prevents or reduces the activity of an endopeptidase.\" [GOC:jl]\nsynonym: \"alpha-2 macroglobulin\" RELATED []\nsynonym: \"endoproteinase inhibitor\" NARROW []\nsynonym: \"proteinase inhibitor\" NARROW []\nis_a: GO:0030414 ! peptidase inhibitor activity\nis_a: GO:0061135 ! endopeptidase regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004866"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
