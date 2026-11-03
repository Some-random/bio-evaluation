# GO_molecular_function_0114: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0114.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — serine-type endopeptidase activity

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
MFPMQFTNSAYRQMEPMFAPGPRGQVQPYRPRTKRRQEPQVGNAAIAALANQMSALQLQVAGLAGQARVDRRGPRRVQKSKQKKKNPSNGEKPKEKKKKQKQQEKKGSGGVIKKPRNRPGKEVRISVKRARQSTFPVYHDGAISGYAVLIGSRVFKPAHVKGKIDHPELADIKFQVAEDMDLEAAAYPKSMRDQAAEPATMMDGVYNWEYGTIRVEDNVVIDASGRGKPGDSGRAITDNSGKVVGIVLGGGPDGRRTRLSVIGFDKKMKAREIAYSEAIPWTRAPALLLLPMVIACTYNSNTFDCSKPSCQDCCITAEPKKAMAMLKDNLNDPNYWDLLIAVTTCNSARKKRAVSTSPAAVYDTQILAAHAAASPYRAYCPDCDGTACISPIAIDEVVSSGSDHVLRIRVGSQSGVTAKGGAAGETSLRYLGRDGKVHAADNTRLVVRTTAKCDVLQATGHYILASCPEGQSITVAATLDGTRHQCTTVFEHQVTEKFTRERSKGHHLSDLTKKCTRFSTTPKKSAPYLVDVYDALPISVEISTVVTCNDNQCTVKVPPGTTVKFDKKCKSAAQATVTFTSDSQTFTCEEPVLTAASITQGKPHLRSSMLPSGGKEVKARIPFPFPPETATCRVSVAPLPSITYEESDVLLAGTAKYPVLLTTRNLGFHSNATSEWIQGKYLRRIPVTPQGIELTWGNNAPLHFWSSVRYASGDADAYPWELLVHHTKHHPEYAWAFVGVACGLLVIAVCMFACACNRVRYSLVANTFNPNPPPLTALTAALCCIPGARADQPYLDIIAYLWTNSKVAFGLQCAAPVACVLIVTYALRHCRLCCKSFLGVRGWSALLVILAYVQSCKSYEHTVVVPMDPRAPSYEAVINRNGYDPLKLTIAVNFTVISPTTALEYWTCASVPIVEPPHVGCCTSVSCPSDLSTLHAFTGKAVSDVHCDVHTNVYPLLWGAAHCFCSTENTQVSAVAATVSEFCAQDSERAEAFSVHSSSVTAEVLVTLGEVVTAVHVYVDGVTSARGTDLKIVAGPITTDYSPFDRKVVRIGEEVYNYDWPPYGAGRPGTFGDIQARSTNYVKPNDLYGDIGIEVLQPTNDHVHVAYTYTTSGLLRWLQDAPKPLSVTAPHGCKISANPLLALDCGVGAVPMSINIPDAKFTRKLKDPKPSALKCVVDSCEYGVDYGGAATITYEGHEAGKCGIHSLTPGVPLRTSVVEVVAGANTVKTTFSSPTPEVTLEVEICSAMVTCASECTPPKEHVVATRPRHGSDTGGYISGPAMRWAGGIVGTLAVLFLILAVTYCVVKKCRSKRIRIVKS

[Multiple Choices]
A. DNA nuclease activity
B. G protein-coupled receptor activity
C. peptidase activity
D. serine-type endopeptidase activity
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

> The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.


**Missing item-specific fact**

> The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.


**Reason**

> The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected.


### Important caveats

- The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.
- The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.",
    "reason": "The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C10",
      "C13",
      "H8",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.",
    "The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C5", "C10", "C13", "H8", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.",
    "missing_item_specific_fact": "The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.",
    "reason": "The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected."
  },
  "important_caveats": [
    "The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.",
    "The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites.

Citations as saved: [C10](#evidence-c10), [C13](#evidence-c13), [C5](#evidence-c5), [H8](#evidence-h8), [H11](#evidence-h11), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.


**Missing item-specific fact**

> None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.


**Reason**

> A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer.


### Important caveats

- The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.
- The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.
- The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.
- The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.",
    "reason": "A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C10",
      "C13",
      "C5",
      "H8",
      "H11",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites."
  },
  "important_caveats": [
    "The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.",
    "The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.",
    "The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.",
    "The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites.",
    "evidence_ids": ["C10", "C13", "C5", "H8", "H11", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.",
    "missing_item_specific_fact": "None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.",
    "reason": "A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer."
  },
  "important_caveats": [
    "The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.",
    "The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.",
    "The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.",
    "The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as having serine-type endopeptidase activity, and its capsid component is described as autocatalytically cleaving from the structural polyprotein. The catalytic activity is assigned by similarity to related proteins, while the GO annotation is computational (InterPro); this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has a strongly basic N-terminal region followed by a folded enzyme-like region and then extensive membrane-spanning viral glycoprotein segments, consistent with a viral structural polyprotein. Transferable knowledge of alphavirus-like structural polyproteins predicts an N-terminal capsid component that autocleaves by serine-type endopeptidase activity. That meaningfully favors D over DNA nuclease or GPCR activity; C is the broader peptidase category.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence architecture and the conserved role of capsid proteases provides a credible basis for selecting D without relying on the exact protein's database record. The precise annotation is not directly established from the sequence alone, but the offered choices make the predicted protease class discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Peptidase activity (C) is a broad category that includes serine-type endopeptidase activity, but D is the more specific and informative choice among the options.


### Important caveats

- The supplied source evidence supports the activity by similarity to related proteins; it does not establish direct experimental confirmation for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has a strongly basic N-terminal region followed by a folded enzyme-like region and then extensive membrane-spanning viral glycoprotein segments, consistent with a viral structural polyprotein. Transferable knowledge of alphavirus-like structural polyproteins predicts an N-terminal capsid component that autocleaves by serine-type endopeptidase activity. That meaningfully favors D over DNA nuclease or GPCR activity; C is the broader peptidase category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence architecture and the conserved role of capsid proteases provides a credible basis for selecting D without relying on the exact protein's database record. The precise annotation is not directly established from the sequence alone, but the offered choices make the predicted protease class discriminating."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C10",
      "C13",
      "H8",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as having serine-type endopeptidase activity, and its capsid component is described as autocatalytically cleaving from the structural polyprotein. The catalytic activity is assigned by similarity to related proteins, while the GO annotation is computational (InterPro); this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied source evidence supports the activity by similarity to related proteins; it does not establish direct experimental confirmation for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Peptidase activity (C) is a broad category that includes serine-type endopeptidase activity, but D is the more specific and informative choice among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as having serine-type endopeptidase activity, and its capsid component is described as autocatalytically cleaving from the structural polyprotein. The catalytic activity is assigned by similarity to related proteins, while the GO annotation is computational (InterPro); this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "C10", "C13", "H8", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has a strongly basic N-terminal region followed by a folded enzyme-like region and then extensive membrane-spanning viral glycoprotein segments, consistent with a viral structural polyprotein. Transferable knowledge of alphavirus-like structural polyproteins predicts an N-terminal capsid component that autocleaves by serine-type endopeptidase activity. That meaningfully favors D over DNA nuclease or GPCR activity; C is the broader peptidase category.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence architecture and the conserved role of capsid proteases provides a credible basis for selecting D without relying on the exact protein's database record. The precise annotation is not directly established from the sequence alone, but the offered choices make the predicted protease class discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Peptidase activity (C) is a broad category that includes serine-type endopeptidase activity, but D is the more specific and informative choice among the options."
  },
  "important_caveats": [
    "The supplied source evidence supports the activity by similarity to related proteins; it does not establish direct experimental confirmation for this exact sequence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 annotates the capsid protein component with EC 3.4.21.90 and GO:0004252 (serine-type endopeptidase activity). The catalytic activity is described as autocatalytic release of the core protein via hydrolysis of a -Trp-|-Ser- bond. The GO annotation is via IEA:InterPro, and the EC assignment is by similarity (ECO:0000250) to related alphaviruses (P03315, P03316, P27284). While this is computational/transferred annotation rather than direct experimental evidence for this exact protein, the annotation is consistent with well-established alphavirus biology. The expected answer D is supported by the database record.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of an alphavirus (Togaviridae) structural polyprotein: an N-terminal highly basic RNA-binding/capsid region, followed by transmembrane segments characteristic of E1/E2 spike glycoproteins, a 6K viroporin segment, and the overall ~1300-residue polyprotein architecture. A model trained on protein families would recognize this as an alphavirus structural polyprotein. Family-level knowledge establishes that the alphavirus capsid domain (e.g., in Semliki Forest virus, Sindbis virus, Ross River virus) is a well-characterized autocatalytic serine protease classified as EC 3.4.21.90. The '21' in the EC number specifically denotes serine-type endopeptidase. This distinguishes option D (serine-type endopeptidase) from option C (general peptidase activity): the alphavirus capsid protease is not merely a generic peptidase but specifically uses a serine nucleophile in a catalytic dyad. Options A (DNA nuclease) and B (GPCR activity) are excluded by the protein's architecture (no nuclease motifs, no seven-transmembrane GPCR topology). The family-level identification of alphavirus capsid as a serine protease provides a concrete, transferable basis for selecting D over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the alphavirus structural polyprotein family from sequence features (basic N-terminal capsid region, transmembrane domains, polyprotein length) combined with well-established family knowledge that alphavirus capsid proteases are serine-type endopeptidases (EC 3.4.21.90) provides a concrete transferable inference that distinguishes D from C, A, and B. The distinction between 'peptidase' (C) and 'serine-type endopeptidase' (D) is resolved by the specific EC classification of the alphavirus capsid protease family, which is standard virology knowledge learned from multiple related alphavirus proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Option C (peptidase activity, GO:0008233) is a parent term of option D (serine-type endopeptidase activity, GO:0004252) in the GO hierarchy. A serine-type endopeptidase IS a peptidase, so C is technically also true. However, standard GO annotation practice assigns the most specific applicable term, and the EC 3.4.21.90 classification specifically identifies the mechanism as serine-type. The question asks for 'primary molecular function,' which conventionally calls for the most specific annotation. This is a common hierarchy issue in GO-based MCQs and does not render the question defective, but C is not strictly false.


### Important caveats

- The serine-type endopeptidase annotation applies specifically to the capsid protein domain within the polyprotein, not to the entire 1319-residue polyprotein. The polyprotein also has structural molecule activity, RNA binding, channel activity, and fusion activity annotations.
- The annotation evidence is ECO:0000250 (by similarity) to related alphaviruses and IEA:InterPro, not direct experimental characterization of this exact SAV3 protein.
- The alphavirus capsid protease uses a catalytic dyad (Ser-His) rather than the classical Ser-His-Asp triad, but is still classified as a serine-type endopeptidase under EC 3.4.21.
- The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of an alphavirus (Togaviridae) structural polyprotein: an N-terminal highly basic RNA-binding/capsid region, followed by transmembrane segments characteristic of E1/E2 spike glycoproteins, a 6K viroporin segment, and the overall ~1300-residue polyprotein architecture. A model trained on protein families would recognize this as an alphavirus structural polyprotein. Family-level knowledge establishes that the alphavirus capsid domain (e.g., in Semliki Forest virus, Sindbis virus, Ross River virus) is a well-characterized autocatalytic serine protease classified as EC 3.4.21.90. The '21' in the EC number specifically denotes serine-type endopeptidase. This distinguishes option D (serine-type endopeptidase) from option C (general peptidase activity): the alphavirus capsid protease is not merely a generic peptidase but specifically uses a serine nucleophile in a catalytic dyad. Options A (DNA nuclease) and B (GPCR activity) are excluded by the protein's architecture (no nuclease motifs, no seven-transmembrane GPCR topology). The family-level identification of alphavirus capsid as a serine protease provides a concrete, transferable basis for selecting D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the alphavirus structural polyprotein family from sequence features (basic N-terminal capsid region, transmembrane domains, polyprotein length) combined with well-established family knowledge that alphavirus capsid proteases are serine-type endopeptidases (EC 3.4.21.90) provides a concrete transferable inference that distinguishes D from C, A, and B. The distinction between 'peptidase' (C) and 'serine-type endopeptidase' (D) is resolved by the specific EC classification of the alphavirus capsid protease family, which is standard virology knowledge learned from multiple related alphavirus proteins."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C10",
      "C13",
      "H8",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 annotates the capsid protein component with EC 3.4.21.90 and GO:0004252 (serine-type endopeptidase activity). The catalytic activity is described as autocatalytic release of the core protein via hydrolysis of a -Trp-|-Ser- bond. The GO annotation is via IEA:InterPro, and the EC assignment is by similarity (ECO:0000250) to related alphaviruses (P03315, P03316, P27284). While this is computational/transferred annotation rather than direct experimental evidence for this exact protein, the annotation is consistent with well-established alphavirus biology. The expected answer D is supported by the database record."
  },
  "important_caveats": [
    "The serine-type endopeptidase annotation applies specifically to the capsid protein domain within the polyprotein, not to the entire 1319-residue polyprotein. The polyprotein also has structural molecule activity, RNA binding, channel activity, and fusion activity annotations.",
    "The annotation evidence is ECO:0000250 (by similarity) to related alphaviruses and IEA:InterPro, not direct experimental characterization of this exact SAV3 protein.",
    "The alphavirus capsid protease uses a catalytic dyad (Ser-His) rather than the classical Ser-His-Asp triad, but is still classified as a serine-type endopeptidase under EC 3.4.21.",
    "The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Option C (peptidase activity, GO:0008233) is a parent term of option D (serine-type endopeptidase activity, GO:0004252) in the GO hierarchy. A serine-type endopeptidase IS a peptidase, so C is technically also true. However, standard GO annotation practice assigns the most specific applicable term, and the EC 3.4.21.90 classification specifically identifies the mechanism as serine-type. The question asks for 'primary molecular function,' which conventionally calls for the most specific annotation. This is a common hierarchy issue in GO-based MCQs and does not render the question defective, but C is not strictly false."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 annotates the capsid protein component with EC 3.4.21.90 and GO:0004252 (serine-type endopeptidase activity). The catalytic activity is described as autocatalytic release of the core protein via hydrolysis of a -Trp-|-Ser- bond. The GO annotation is via IEA:InterPro, and the EC assignment is by similarity (ECO:0000250) to related alphaviruses (P03315, P03316, P27284). While this is computational/transferred annotation rather than direct experimental evidence for this exact protein, the annotation is consistent with well-established alphavirus biology. The expected answer D is supported by the database record.",
    "evidence_ids": ["C4", "C5", "C10", "C13", "H8", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of an alphavirus (Togaviridae) structural polyprotein: an N-terminal highly basic RNA-binding/capsid region, followed by transmembrane segments characteristic of E1/E2 spike glycoproteins, a 6K viroporin segment, and the overall ~1300-residue polyprotein architecture. A model trained on protein families would recognize this as an alphavirus structural polyprotein. Family-level knowledge establishes that the alphavirus capsid domain (e.g., in Semliki Forest virus, Sindbis virus, Ross River virus) is a well-characterized autocatalytic serine protease classified as EC 3.4.21.90. The '21' in the EC number specifically denotes serine-type endopeptidase. This distinguishes option D (serine-type endopeptidase) from option C (general peptidase activity): the alphavirus capsid protease is not merely a generic peptidase but specifically uses a serine nucleophile in a catalytic dyad. Options A (DNA nuclease) and B (GPCR activity) are excluded by the protein's architecture (no nuclease motifs, no seven-transmembrane GPCR topology). The family-level identification of alphavirus capsid as a serine protease provides a concrete, transferable basis for selecting D over C.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the alphavirus structural polyprotein family from sequence features (basic N-terminal capsid region, transmembrane domains, polyprotein length) combined with well-established family knowledge that alphavirus capsid proteases are serine-type endopeptidases (EC 3.4.21.90) provides a concrete transferable inference that distinguishes D from C, A, and B. The distinction between 'peptidase' (C) and 'serine-type endopeptidase' (D) is resolved by the specific EC classification of the alphavirus capsid protease family, which is standard virology knowledge learned from multiple related alphavirus proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Option C (peptidase activity, GO:0008233) is a parent term of option D (serine-type endopeptidase activity, GO:0004252) in the GO hierarchy. A serine-type endopeptidase IS a peptidase, so C is technically also true. However, standard GO annotation practice assigns the most specific applicable term, and the EC 3.4.21.90 classification specifically identifies the mechanism as serine-type. The question asks for 'primary molecular function,' which conventionally calls for the most specific annotation. This is a common hierarchy issue in GO-based MCQs and does not render the question defective, but C is not strictly false."
  },
  "important_caveats": [
    "The serine-type endopeptidase annotation applies specifically to the capsid protein domain within the polyprotein, not to the entire 1319-residue polyprotein. The polyprotein also has structural molecule activity, RNA binding, channel activity, and fusion activity annotations.",
    "The annotation evidence is ECO:0000250 (by similarity) to related alphaviruses and IEA:InterPro, not direct experimental characterization of this exact SAV3 protein.",
    "The alphavirus capsid protease uses a catalytic dyad (Ser-His) rather than the classical Ser-His-Asp triad, but is still classified as a serine-type endopeptidase under EC 3.4.21.",
    "The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `ontology_parent_relation_traced_with_evidence_qualification`.

> The supplied ontology paths link serine-type endopeptidase GO:0004252 through endopeptidase GO:0004175 to peptidase GO:0008233. C10/H8 assign protease activity by similarity and C13/H11 use IEA:InterPro.

**Remaining uncertainty:** The nested term relationship is traceable. The protein activity and exact specificity remain qualified by similarity/computational evidence; wording interpretation is not resolved by citation presence.

Evidence checked: [C1](#evidence-c1), [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q53AM4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "benchmark_sequence_length": 1319,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 102,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-05-24",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "current_source_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "current_source_sequence_length": 1319,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 100,
  "selected_historical_version": {
    "accession": "Q53AM4",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "POLS_SAV3",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "selected_historical_source_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "selected_historical_source_sequence_length": 1319,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q53AM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":102,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-05-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"SAV3\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Kitrinoviricota\",\"Alsuviricetes\",\"Martellivirales\",\"Togaviridae\",\"Alphavirus\"],\"scientificName\":\"Alphavirus salmon subtype 3\",\"synonyms\":[\"Norwegian salmonid alphavirus\"],\"taxonId\":344701}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"p130\"}}],\"contains\":[{\"alternativeNames\":[{\"fullName\":{\"value\":\"Coat protein\"},\"shortNames\":[{\"value\":\"C\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.21.90\"}],\"fullName\":{\"value\":\"Capsid protein\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"p62\"}},{\"fullName\":{\"value\":\"pE2\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Precursor of protein E3/E2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Assembly protein E3\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"E2 envelope glycoprotein\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Spike glycoprotein E2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"6K protein\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"E1 envelope glycoprotein\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Spike glycoprotein E1\"}}}],\"recommendedName\":{\"fullName\":{\"value\":\"Structural polyprotein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"Capsid protein\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03316\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27284\",\"source\":\"UniProtKB\"}],\"value\":\"Forms an icosahedral capsid with a T=4 symmetry composed of 240 copies of the capsid protein surrounded by a lipid membrane through which penetrate 80 spikes composed of trimers of E1-E2 heterodimers (By similarity). The capsid protein binds to the viral RNA genome at a site adjacent to a ribosome binding site for viral genome translation following genome release (By similarity). Possesses a protease activity that results in its autocatalytic cleavage from the nascent structural protein (By similarity). Following its self-cleavage, the capsid protein transiently associates with ribosomes, and within several minutes the protein binds to viral RNA and rapidly assembles into icosahedric core particles (By similarity). The resulting nucleocapsid eventually associates with the cytoplasmic domain of the spike glycoprotein E2 at the cell membrane, leading to budding and formation of mature virions (By similarity). In case of infection, new virions attach to target cells and after clathrin-mediated endocytosis their membrane fuses with the host endosomal membrane (By similarity). This leads to the release of the nucleocapsid into the cytoplasm, followed by an uncoating event necessary for the genomic RNA to become accessible (By similarity). The uncoating might be triggered by the interaction of capsid proteins with ribosomes (By similarity). Binding of ribosomes would release the genomic RNA since the same region is genomic RNA-binding and ribosome-binding (By similarity). Specifically inhibits interleukin-1 receptor-associated kinase 1/IRAK1-dependent signaling during viral entry, representing a means by which the alphaviruses may evade innate immune detection and activation prior to viral gene expression (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"Assembly protein E3\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"value\":\"Provides the signal sequence for the translocation of the precursor of protein E3/E2 to the host endoplasmic reticulum. Furin-cleaved E3 remains associated with spike glycoprotein E1 and mediates pH protection of the latter during the transport via the secretory pathway. After virion release from the host cell, the assembly protein E3 is gradually released in the extracellular space\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"Spike glycoprotein E2\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03316\",\"source\":\"UniProtKB\"}],\"value\":\"Plays a role in viral attachment to target host cell, by binding to the cell receptor. Synthesized as a p62 precursor which is processed by furin at the cell membrane just before virion budding, giving rise to E2-E1 heterodimer. The p62-E1 heterodimer is stable, whereas E2-E1 is unstable and dissociate at low pH. p62 is processed at the last step, presumably to avoid E1 fusion activation before its final export to cell surface. E2 C-terminus contains a transitory transmembrane that would be disrupted by palmitoylation, resulting in reorientation of the C-terminal tail from lumenal to cytoplasmic side. This step is critical since E2 C-terminus is involved in budding by interacting with capsid proteins. This release of E2 C-terminus in cytoplasm occurs lately in protein export, and precludes premature assembly of particles at the endoplasmic reticulum membrane\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"6K protein\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03316\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"25009976\",\"source\":\"PubMed\"}],\"value\":\"Acts as a viroporin that participates in virus glycoprotein processing and transport to the plasma membrane, cell permeabilization and budding of viral particles (Probable). Disrupts the calcium homeostasis of the cell, probably at the endoplasmic reticulum level (By similarity). This leads to cytoplasmic calcium elevation (By similarity). Because of its lipophilic properties, the 6K protein is postulated to influence the selection of lipids that interact with the transmembrane domains of the glycoproteins, which, in turn, affects the deformability of the bilayer required for the extreme curvature that occurs as budding proceeds. Present in low amount in virions, about 3% compared to viral glycoproteins (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"molecule\":\"Spike glycoprotein E1\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"value\":\"Class II viral fusion protein. Fusion activity is inactive as long as E1 is bound to E2 in mature virion. After virus attachment to target cell and endocytosis, acidification of the endosome induce dissociation of E1/E2 heterodimer and concomitant trimerization of the E1 subunits. This E1 trimer is fusion active, and promotes release of viral nucleocapsid in cytoplasm after endosome and viral membrane fusion. Efficient fusion requires the presence of cholesterol and sphingolipid in the target membrane\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.21.90\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"name\":\"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0015267\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:channel activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003723\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:RNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004252\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:serine-type endopeptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005198\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:structural molecule activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo T.C.\",\"Johansson D.X.\",\"Haugland O.\",\"Liljestroem P.\",\"Evensen O.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25009976\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0100184\"}],\"citationType\":\"journal article\",\"firstPage\":\"e100184\",\"id\":\"25009976\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e100184\",\"publicationDate\":\"2014\",\"title\":\"A 6K-deletion variant of salmonid alphavirus is non-viable but can be rescued through RNA recombination.\",\"volume\":\"9\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION (6K PROTEIN)\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 1-32",
  "excerpt": "ID   POLS_SAV3               Reviewed;        1319 AA.\nAC   Q53AM4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-MAY-2005, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Structural polyprotein;\nDE   AltName: Full=p130;\nDE   Contains:\nDE     RecName: Full=Capsid protein;\nDE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};\nDE     AltName: Full=Coat protein;\nDE              Short=C;\nDE   Contains:\nDE     RecName: Full=Precursor of protein E3/E2;\nDE     AltName: Full=p62;\nDE     AltName: Full=pE2;\nDE   Contains:\nDE     RecName: Full=Assembly protein E3;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E2;\nDE     AltName: Full=E2 envelope glycoprotein;\nDE   Contains:\nDE     RecName: Full=6K protein;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E1;\nDE     AltName: Full=E1 envelope glycoprotein;\nOS   Alphavirus salmon subtype 3 (SAV3) (Norwegian salmonid alphavirus).\nOC   Viruses; Riboviria; Orthornavirae; Kitrinoviricota; Alsuviricetes;\nOC   Martellivirales; Togaviridae; Alphavirus.\nOX   NCBI_TaxID=344701;\nOH   NCBI_TaxID=8022; Oncorhynchus mykiss (Rainbow trout) (Salmo gairdneri).\nOH   NCBI_TaxID=8030; Salmo salar (Atlantic salmon).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 41-47",
  "excerpt": "RN   [2]\nRP   FUNCTION (6K PROTEIN).\nRX   PubMed=25009976; DOI=10.1371/journal.pone.0100184;\nRA   Guo T.C., Johansson D.X., Haugland O., Liljestroem P., Evensen O.;\nRT   \"A 6K-deletion variant of salmonid alphavirus is non-viable but can be\nRT   rescued through RNA recombination.\";\nRL   PLoS ONE 9:e100184-e100184(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 48-75",
  "excerpt": "CC   -!- FUNCTION: [Capsid protein]: Forms an icosahedral capsid with a T=4\nCC       symmetry composed of 240 copies of the capsid protein surrounded by a\nCC       lipid membrane through which penetrate 80 spikes composed of trimers of\nCC       E1-E2 heterodimers (By similarity). The capsid protein binds to the\nCC       viral RNA genome at a site adjacent to a ribosome binding site for\nCC       viral genome translation following genome release (By similarity).\nCC       Possesses a protease activity that results in its autocatalytic\nCC       cleavage from the nascent structural protein (By similarity). Following\nCC       its self-cleavage, the capsid protein transiently associates with\nCC       ribosomes, and within several minutes the protein binds to viral RNA\nCC       and rapidly assembles into icosahedric core particles (By similarity).\nCC       The resulting nucleocapsid eventually associates with the cytoplasmic\nCC       domain of the spike glycoprotein E2 at the cell membrane, leading to\nCC       budding and formation of mature virions (By similarity). In case of\nCC       infection, new virions attach to target cells and after clathrin-\nCC       mediated endocytosis their membrane fuses with the host endosomal\nCC       membrane (By similarity). This leads to the release of the nucleocapsid\nCC       into the cytoplasm, followed by an uncoating event necessary for the\nCC       genomic RNA to become accessible (By similarity). The uncoating might\nCC       be triggered by the interaction of capsid proteins with ribosomes (By\nCC       similarity). Binding of ribosomes would release the genomic RNA since\nCC       the same region is genomic RNA-binding and ribosome-binding (By\nCC       similarity). Specifically inhibits interleukin-1 receptor-associated\nCC       kinase 1/IRAK1-dependent signaling during viral entry, representing a\nCC       means by which the alphaviruses may evade innate immune detection and\nCC       activation prior to viral gene expression (By similarity).\nCC       {ECO:0000250|UniProtKB:P03315, ECO:0000250|UniProtKB:P03316,\nCC       ECO:0000250|UniProtKB:P27284}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 76-82",
  "excerpt": "CC   -!- FUNCTION: [Assembly protein E3]: Provides the signal sequence for the\nCC       translocation of the precursor of protein E3/E2 to the host endoplasmic\nCC       reticulum. Furin-cleaved E3 remains associated with spike glycoprotein\nCC       E1 and mediates pH protection of the latter during the transport via\nCC       the secretory pathway. After virion release from the host cell, the\nCC       assembly protein E3 is gradually released in the extracellular space.\nCC       {ECO:0000250|UniProtKB:P03315}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 83-96",
  "excerpt": "CC   -!- FUNCTION: [Spike glycoprotein E2]: Plays a role in viral attachment to\nCC       target host cell, by binding to the cell receptor. Synthesized as a p62\nCC       precursor which is processed by furin at the cell membrane just before\nCC       virion budding, giving rise to E2-E1 heterodimer. The p62-E1\nCC       heterodimer is stable, whereas E2-E1 is unstable and dissociate at low\nCC       pH. p62 is processed at the last step, presumably to avoid E1 fusion\nCC       activation before its final export to cell surface. E2 C-terminus\nCC       contains a transitory transmembrane that would be disrupted by\nCC       palmitoylation, resulting in reorientation of the C-terminal tail from\nCC       lumenal to cytoplasmic side. This step is critical since E2 C-terminus\nCC       is involved in budding by interacting with capsid proteins. This\nCC       release of E2 C-terminus in cytoplasm occurs lately in protein export,\nCC       and precludes premature assembly of particles at the endoplasmic\nCC       reticulum membrane. {ECO:0000250|UniProtKB:P03316}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 97-109",
  "excerpt": "CC   -!- FUNCTION: [6K protein]: Acts as a viroporin that participates in virus\nCC       glycoprotein processing and transport to the plasma membrane, cell\nCC       permeabilization and budding of viral particles (Probable). Disrupts\nCC       the calcium homeostasis of the cell, probably at the endoplasmic\nCC       reticulum level (By similarity). This leads to cytoplasmic calcium\nCC       elevation (By similarity). Because of its lipophilic properties, the 6K\nCC       protein is postulated to influence the selection of lipids that\nCC       interact with the transmembrane domains of the glycoproteins, which, in\nCC       turn, affects the deformability of the bilayer required for the extreme\nCC       curvature that occurs as budding proceeds. Present in low amount in\nCC       virions, about 3% compared to viral glycoproteins (By similarity).\nCC       {ECO:0000250|UniProtKB:P03315, ECO:0000250|UniProtKB:P03316,\nCC       ECO:0000305|PubMed:25009976}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 110-118",
  "excerpt": "CC   -!- FUNCTION: [Spike glycoprotein E1]: Class II viral fusion protein.\nCC       Fusion activity is inactive as long as E1 is bound to E2 in mature\nCC       virion. After virus attachment to target cell and endocytosis,\nCC       acidification of the endosome induce dissociation of E1/E2 heterodimer\nCC       and concomitant trimerization of the E1 subunits. This E1 trimer is\nCC       fusion active, and promotes release of viral nucleocapsid in cytoplasm\nCC       after endosome and viral membrane fusion. Efficient fusion requires the\nCC       presence of cholesterol and sphingolipid in the target membrane.\nCC       {ECO:0000250|UniProtKB:P03315}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 119-122",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Autocatalytic release of the core protein from the N-terminus\nCC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-\nCC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 221-221",
  "excerpt": "DR   GO; GO:0015267; F:channel activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 222-222",
  "excerpt": "DR   GO; GO:0003723; F:RNA binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 223-223",
  "excerpt": "DR   GO; GO:0004252; F:serine-type endopeptidase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "source_locator": "lines 224-224",
  "excerpt": "DR   GO; GO:0005198; F:structural molecule activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
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
  "source_locator": "lines 36973-37083",
  "excerpt": "[Term]\nid: GO:0004175\nname: endopeptidase activity\nnamespace: molecular_function\nalt_id: GO:0016809\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain.\" [http://merops.sanger.ac.uk/about/glossary.htm#ENDOPEPTIDASE]\nsynonym: \"elastase activity\" RELATED [GOC:krc]\nsynonym: \"endoprotease activity\" NARROW []\nsynonym: \"proteasome endopeptidase activity\" NARROW []\nsynonym: \"proteinase\" NARROW []\nxref: EC:3.4.99.-\nxref: Reactome:R-HSA-1168640 \"Ubiquitinated IkB is degraded\"\nxref: Reactome:R-HSA-1234159 \"Proteasome proteolyzes ub-HIF-alpha\"\nxref: Reactome:R-HSA-1236935 \"Proteasomal cleavage of substrate (26S proteasome catalyst)\"\nxref: Reactome:R-HSA-1236970 \"Proteasomal clevage of exogenous antigen (26S proteasome catalyst)\"\nxref: Reactome:R-HSA-1251997 \"Cleavage of ERBB4m80 by gamma-scretase complex\"\nxref: Reactome:R-HSA-1433374 \"Processing of SCF isoform 1\"\nxref: Reactome:R-HSA-1504193 \"Ubiquitinated DVL is degraded by the proteasome\"\nxref: Reactome:R-HSA-174058 \"Degradation of multiubiquitinated Cdh1\"\nxref: Reactome:R-HSA-174105 \"Degradation of multiubiquitinated cell cycle proteins\"\nxref: Reactome:R-HSA-174202 \"Degradation of multiubiquitinated Securin\"\nxref: Reactome:R-HSA-174203 \"SCF-mediated degradation of Emi1\"\nxref: Reactome:R-HSA-174255 \"Degradation multiubiquitinated Cyclin A\"\nxref: Reactome:R-HSA-180573 \"Degradation of ubiquitinated CD4\"\nxref: Reactome:R-HSA-180603 \"Proteosome-mediated degradation of APOBEC3G\"\nxref: Reactome:R-HSA-187574 \"Degradation of ubiquitinated p27/p21 by the 26S proteasome\"\nxref: Reactome:R-HSA-188191 \"APC/C:Cdh1-mediated degradation of Skp2\"\nxref: Reactome:R-HSA-193682 \"gamma-secretase cleaves the p75NTR transmembrane domain\"\nxref: Reactome:R-HSA-209061 \"Ubiquitinated and phosphorylated IKBA binds to and is degraded by the proteasome complex\"\nxref: Reactome:R-HSA-211715 \"Proteasome mediated degradation of PAK-2p34\"\nxref: Reactome:R-HSA-2130282 \"Degradation of ubiquitinated beta catenin by the proteasome\"\nxref: Reactome:R-HSA-2213200 \"Release of endostatin-like peptides\"\nxref: Reactome:R-HSA-264458 \"Proteasome mediated degradation of COP1\"\nxref: Reactome:R-HSA-353125 \"26S proteosome degrades ODC holoenzyme complex\"\nxref: Reactome:R-HSA-3640874 \"Ub-RibC-AXIN is degraded by the proteasome\"\nxref: Reactome:R-HSA-3928656 \"gamma-secretase cleaves EPHB2\"\nxref: Reactome:R-HSA-450466 \"AUF1:mRNA complex is degraded\"\nxref: Reactome:R-HSA-4608855 \"PRICKLE1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-4641256 \"Ubiquitinated AXIN is degraded by the proteasome\"\nxref: Reactome:R-HSA-4641260 \"Ubiquitinated DVL1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5358340 \"Autoproteolytic cleavage of Hh precursors\"\nxref: Reactome:R-HSA-5358460 \"HPE SHH variants don't undergo autoproteolytic cleavage\"\nxref: Reactome:R-HSA-5362448 \"Hh C-terminal fragments are degraded by the proteasome\"\nxref: Reactome:R-HSA-5387392 \"processing defective Hh variants are degraded by the proteasome\"\nxref: Reactome:R-HSA-5607724 \"26S proteasome processes K48PolyUb-K21,22-p-S32,36-IkBA:NF-kB complex to form NF-kB complex\"\nxref: Reactome:R-HSA-5607731 \"26S proteasome processes p-7S-p100:RELB to form p52:RELB\"\nxref: Reactome:R-HSA-5610754 \"GLI3 is partially degraded by the proteasome to yield the GLI3 repressor\"\nxref: Reactome:R-HSA-5610757 \"GLI2 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5610758 \"GLI1 is degraded by the proteasome after ubiquitination by beta-TrCP\"\nxref: Reactome:R-HSA-5610760 \"GLI1 is degraded by the proteasome after ubiquitination by ITCH\"\nxref: Reactome:R-HSA-5635854 \"GLI2,3 are degraded by the proteasome\"\nxref: Reactome:R-HSA-5635868 \"ub-GLI is degraded by the proteasome\"\nxref: Reactome:R-HSA-5658430 \"NF1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-5668481 \"Protesomal degradation of K48polyUb-TRAF3\"\nxref: Reactome:R-HSA-5668520 \"26Sproteasome degrades K48polyUb-NIK\"\nxref: Reactome:R-HSA-5687112 \"MAPK6 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-5693081 \"FURIN cleaves 7K-BACE1 to 7K-BACE1(46-501)\"\nxref: Reactome:R-HSA-6784628 \"PCSK6,FURIN mediate dissociation of 2 x LPL from GPIHBP1:HSPG:LPL dimer\"\nxref: Reactome:R-HSA-6784676 \"PCSK5 mediates dissociation of 2 x LPL from GPIHBP1:HSPG:LPL dimer\"\nxref: Reactome:R-HSA-68825 \"Ubiquitinated geminin is degraded by the proteasome\"\nxref: Reactome:R-HSA-68948 \"Ubiquitinated Orc1 is degraded by the proteasome\"\nxref: Reactome:R-HSA-69016 \"Ubiquitinated Cdc6 is degraded by the proteasome\"\nxref: Reactome:R-HSA-69600 \"Proteolytic degradation of ubiquitinated-Cdc25A\"\nxref: Reactome:R-HSA-74730 \"Insulin degradation\"\nxref: Reactome:R-HSA-75825 \"Proteasome mediated degradation of Cyclin D1\"\nxref: Reactome:R-HSA-8849797 \"Membrane proteases cleave Profilaggrin producing Filaggrin\"\nxref: Reactome:R-HSA-8850992 \"Proteasome degrades polyubiquitinated PTEN\"\nxref: Reactome:R-HSA-8852354 \"GTSE1 facilitates proteasome-mediated degradation of TP53\"\nxref: Reactome:R-HSA-8854044 \"Proteasome degrades AURKA ubiquitinated by SCF-FBXL7\"\nxref: Reactome:R-HSA-8854071 \"Proteasome-mediated degradation of PolyUb-FBXL7\"\nxref: Reactome:R-HSA-8866553 \"misfolded CFTR is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-8866858 \"CFTR F508del is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-8932355 \"26S proteasome degrades Ub-NFE2L2\"\nxref: Reactome:R-HSA-8934819 \"Cytoplasmic proteases cleave Profilaggrin producing Filaggrin\"\nxref: Reactome:R-HSA-8939801 \"26S proteasome degrades PolyUb-RUNX2\"\nxref: Reactome:R-HSA-8952408 \"Polyubiquitinated RUNX3 is degraded by the proteasome\"\nxref: Reactome:R-HSA-8957265 \"26S proteasome degrades TP73 polyubiquitinated by ITCH\"\nxref: Reactome:R-HSA-9008110 \"Proteasome degrades polyubiquitinated RUNX2\"\nxref: Reactome:R-HSA-9009362 \"Proteasome degrades PolyUb-RUNX2\"\nxref: Reactome:R-HSA-9010096 \"Gamma-secretase cleaves APP(672-770) to APP(672-711) and APP(672-713)\"\nxref: Reactome:R-HSA-9011313 \"Proteasome degrades ubiquitinated ROBO3.1\"\nxref: Reactome:R-HSA-9604642 \"Proteasome degrades ubiquitinated NICD4\"\nxref: Reactome:R-HSA-9614271 \"Autocleavage of ADGRG6\"\nxref: Reactome:R-HSA-9755303 \"26S proteasome degrades HIFalpha\"\nxref: Reactome:R-HSA-9755306 \"ub UBXN7 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-9760521 \"Unknown peptidase cleaves pro-STa\"\nxref: Reactome:R-HSA-9762096 \"Ub,pS335,S338,T NFE2L2 is degraded\"\nxref: Reactome:R-HSA-9766223 \"Proteasome-dependent degradation of ubiquitinated CDH1\"\nxref: Reactome:R-HSA-983150 \"Proteasomal cleavage of substrate\"\nxref: Reactome:R-HSA-983158 \"Trimming of peptides in ER\"\nxref: Reactome:R-HSA-9839376 \"TGFBR3(784-851) degradation\"\nxref: Reactome:R-HSA-9906017 \"Unknown peptidase cleaves UQCRFS1 subunit\"\nxref: Reactome:R-HSA-9908101 \"Maturation of the canonical 20S core particle\"\nxref: Reactome:R-HSA-9908105 \"Maturation of the 20S immunoproteasome core particle\"\nxref: Reactome:R-HSA-9908108 \"Maturation of the 20S thymoproteasome core particle\"\nxref: Reactome:R-HSA-9908780 \"Maturation of the preholospermatoproteasome\"\nxref: Reactome:R-HSA-9912636 \"Proteasomal cleavage of intracellular substrate (PA28-alpha-beta-20S proteasome catalyst)\"\nxref: Reactome:R-HSA-9912655 \"Proteasomal cleavage of intracellular substrate (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9912747 \"Proteasomal clevage of exogenous antigen (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9912751 \"Proteasomal cleavage of partially digested antigen (immunoproteasome catalyst)\"\nxref: Reactome:R-HSA-9929352 \"Ubiquitinated CD274 is degraded by the 26S proteasome\"\nxref: Reactome:R-HSA-9929486 \"SPOP-mediated degradation of CD274 by 26S Proteosome\"\nxref: Reactome:R-HSA-9931314 \"Proteasomal degradation of polyUb-p-S195-CD274\"\nxref: Reactome:R-HSA-9934884 \"Proteolysis of K48polyUb,p-S-CRY1,2\"\nxref: Reactome:R-HSA-9934887 \"Proteolysis of K48polyUb-K107,p-S-CRY1,K48polyUb-K126,p-S-CRY2\"\nxref: Reactome:R-HSA-9934893 \"Proteolysis of K48polyUb-K,p-S-PER1,2,3\"\nxref: Reactome:R-HSA-9949676 \"The proteasome degrades the alanine-tailed K48-polyUb nascent peptide bound to LTN1:NEMF:TCF25:VCP hexamer\"\nxref: Reactome:R-HSA-9954728 \"The proteasome degrades the K48-polyubiquitinated alanine-tailed nascent peptide\"\nis_a: GO:0008233 ! peptidase activity\nproperty_value: skos:narrowMatch EC:3.4.99.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004175"
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
  "source_locator": "lines 38518-38819",
  "excerpt": "[Term]\nid: GO:0004252\nname: serine-type endopeptidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain by a catalytic mechanism that involves a catalytic triad consisting of a serine nucleophile that is activated by a proton relay involving an acidic residue (e.g. aspartate or glutamate) and a basic residue (usually histidine).\" [GOC:mah, https://www.ebi.ac.uk/merops/about/glossary.shtml#CATTYPE]\nsubset: goslim_chembl\nsynonym: \"blood coagulation factor activity\" RELATED []\nsynonym: \"serine elastase activity\" RELATED [GOC:krc]\nxref: EC:3.4.21.-\nxref: EC:3.4.21.1\nxref: EC:3.4.21.10\nxref: EC:3.4.21.102\nxref: EC:3.4.21.20\nxref: EC:3.4.21.21\nxref: EC:3.4.21.22\nxref: EC:3.4.21.26\nxref: EC:3.4.21.27\nxref: EC:3.4.21.34\nxref: EC:3.4.21.35\nxref: EC:3.4.21.36\nxref: EC:3.4.21.38\nxref: EC:3.4.21.39\nxref: EC:3.4.21.4\nxref: EC:3.4.21.41\nxref: EC:3.4.21.42\nxref: EC:3.4.21.43\nxref: EC:3.4.21.45\nxref: EC:3.4.21.46\nxref: EC:3.4.21.47\nxref: EC:3.4.21.48\nxref: EC:3.4.21.5\nxref: EC:3.4.21.53\nxref: EC:3.4.21.54\nxref: EC:3.4.21.59\nxref: EC:3.4.21.6\nxref: EC:3.4.21.61\nxref: EC:3.4.21.62\nxref: EC:3.4.21.68\nxref: EC:3.4.21.69\nxref: EC:3.4.21.7\nxref: EC:3.4.21.71\nxref: EC:3.4.21.73\nxref: EC:3.4.21.75\nxref: EC:3.4.21.78\nxref: EC:3.4.21.79\nxref: EC:3.4.21.83\nxref: EC:3.4.21.88\nxref: EC:3.4.21.9\nxref: EC:3.4.21.92\nxref: EC:3.4.21.93\nxref: EC:3.4.21.94\nxref: Reactome:R-HSA-114697 \"Activated thrombin (factor IIa) cleaves PAR3,4, activating them\"\nxref: Reactome:R-HSA-1181152 \"Cleavage of NODAL proprotein\"\nxref: Reactome:R-HSA-139893 \"Granzyme-B activates BID by cleavage\"\nxref: Reactome:R-HSA-140599 \"factor XIII -> factor XIII cleaved tetramer + 2 factor XIII A activation peptides\"\nxref: Reactome:R-HSA-140664 \"prothrombin -> activated thrombin (factor IIa) + thrombin activation peptide (prothrombinase catalyst)\"\nxref: Reactome:R-HSA-140696 \"factor V -> factor Va + factor V activation peptide (thrombin catalyst)\"\nxref: Reactome:R-HSA-140700 \"prothrombin -> activated thrombin (factor IIa) + thrombin activation peptide (Xa catalyst)\"\nxref: Reactome:R-HSA-140736 \"factor X -> factor Xa + factor X activation peptide (TF:F7a catalyst)\"\nxref: Reactome:R-HSA-140769 \"factor VII -> factor VIIa\"\nxref: Reactome:R-HSA-140777 \"factor X -> factor Xa + factor X activation peptide (TF:F7 catalyst)\"\nxref: Reactome:R-HSA-140823 \"factor IX -> factor IXa + factor IX activation peptide (TF:F7a catalyst)\"\nxref: Reactome:R-HSA-140840 \"fibrinogen -> fibrin monomer + 2 fibrinopeptide A + 2 fibrinopeptide B\"\nxref: Reactome:R-HSA-140870 \"thrombin:antithrombin III:heparin -> thrombin:cleaved antithrombin III:heparin\"\nxref: Reactome:R-HSA-141026 \"Activated protein C cleaves factor Va to factor Vi intermediate form\"\nxref: Reactome:R-HSA-141040 \"Activated thrombin:thrombomodulin cleaves PROCR:Protein C to PROCR:Activated protein C\"\nxref: Reactome:R-HSA-1454843 \"E-cadherin degradation by MMP3, MMP7 and plasmin\"\nxref: Reactome:R-HSA-1474197 \"Collagen type II degradation by MMP1,3,8,13,PRSS2\"\nxref: Reactome:R-HSA-1566962 \"Elastin degradation by elastin-degrading extracellular proteinases\"\nxref: Reactome:R-HSA-1566979 \"Laminin-332 degradation by laminin-322 degrading extracellular proteinases\"\nxref: Reactome:R-HSA-1566981 \"Fibronectin degradation by MMP1, 3, 7, 12, 13, 19, CTSS\"\nxref: Reactome:R-HSA-158137 \"factor VIII:von Willibrand factor multimer -> factor VIIIa + factor VIIIa B A3 acidic polypeptide + von Willibrand factor multimer\"\nxref: Reactome:R-HSA-158164 \"factor X -> factor Xa + factor X activation peptide (VIIIa:IXa catalyst)\"\nxref: Reactome:R-HSA-158300 \"factor XI:platelet glycoprotein (GP) Ib:IX:V complex -> factor XIa:platelet glycoprotein (GP) Ib:IX:V complex (XIIa catalyst)\"\nxref: Reactome:R-HSA-158311 \"kallikrein:kininogen:C1q binding protein tetramer -> kallikrein + activated kininogen:C1q binding protein tetramer + bradykinin\"\nxref: Reactome:R-HSA-158313 \"factor XII -> factor XIIa\"\nxref: Reactome:R-HSA-158333 \"factor IX -> factor IXa + factor IX activation peptide (factor XIa catalyst)\"\nxref: Reactome:R-HSA-158419 \"factor XI:platelet glycoprotein (GP) Ib:IX:V complex -> factor XIa:platelet glycoprotein (GP) Ib:IX:V complex (thrombin catalyst)\"\nxref: Reactome:R-HSA-158744 \"crosslinked fibrin multimer:tissue plasminogen activator (two-chain):plasminogen -> crosslinked fibrin multimer:tissue plasminogen activator (two-chain) + plasmin\"\nxref: Reactome:R-HSA-158747 \"crosslinked fibrin multimer:tissue plasminogen activator (one-chain) -> crosslinked fibrin multimer:tissue plasminogen activator (two-chain)\"\nxref: Reactome:R-HSA-158750 \"crosslinked fibrin multimer:tissue plasminogen activator (one-chain):plasminogen -> crosslinked fibrin multimer:tissue plasminogen activator (one-chain) + plasmin\"\nxref: Reactome:R-HSA-158766 \"fibrin multimer, crosslinked -> fibrin digestion products (plasmin)\"\nxref: Reactome:R-HSA-158925 \"plasminogen:histidine-rich glycoprotein -> plasmin + histidine-rich glycoprotein (uPA [two-chain] catalyst)\"\nxref: Reactome:R-HSA-158942 \"urokinase plasminogen activator (one-chain):uPAR -> urokinase plasminogen activator (two-chain):uPAR\"\nxref: Reactome:R-HSA-158982 \"plasminogen:histidine-rich glycoprotein -> plasmin + histidine-rich glycoprotein (uPA [one-chain] catalyst)\"\nxref: Reactome:R-HSA-1592270 \"NID1 degradation by MMP1, 9, 12, ELANE\"\nxref: Reactome:R-HSA-1592278 \"Autocatalytic activation of proMMP2\"\nxref: Reactome:R-HSA-1592297 \"Full activation of MMP1\"\nxref: Reactome:R-HSA-1592314 \"HSPG2 (perlecan) degradation by MMP3, plasmin, (MMP12)\"\nxref: Reactome:R-HSA-1592316 \"Initial activation of proMMP1\"\nxref: Reactome:R-HSA-1592362 \"Activation of proMMP7 by MMP3\"\nxref: Reactome:R-HSA-1592371 \"Initial activation of proMMP3\"\nxref: Reactome:R-HSA-1592398 \"Activation of proMMP8\"\nxref: Reactome:R-HSA-1592436 \"Initial activation of proMMP9 by MMPs\"\nxref: Reactome:R-HSA-159728 \"Furin cleaves pro-prothrombin to prothrombin\"\nxref: Reactome:R-HSA-159733 \"Furin cleaves pro-factor X to factor X\"\nxref: Reactome:R-HSA-159771 \"Furin cleaves pro-protein C to protein C\"\nxref: Reactome:R-HSA-159773 \"Furin cleaves pro-protein S to protein S\"\nxref: Reactome:R-HSA-159796 \"Furin cleaves pro-factor IX to factor IX\"\nxref: Reactome:R-HSA-159868 \"Furin cleaves pro-factor VII to factor VII\"\nxref: Reactome:R-HSA-1602458 \"Activation of proMMP10\"\nxref: Reactome:R-HSA-1602466 \"Activation of MT-MMPs by FURIN\"\nxref: Reactome:R-HSA-1602473 \"Autocatalytic activation of MMP1\"\nxref: Reactome:R-HSA-1602484 \"Activation of proMMP11 by FURIN\"\nxref: Reactome:R-HSA-1602488 \"Initial activation of proMMP13 by plasmin and trypsin\"\nxref: Reactome:R-HSA-1604359 \"Initial activation of proMMP2 by MMP1, 7\"\nxref: Reactome:R-HSA-1604360 \"Initial activation of proMMP2 by MMP14\"\nxref: Reactome:R-HSA-1604368 \"Autocatalytic activation of bound proMMP2\"\nxref: Reactome:R-HSA-1604690 \"Activation of MMP9 intermediate form by MMPs\"\nxref: Reactome:R-HSA-1604712 \"Initial activation of proMMP7 by trypsin\"\nxref: Reactome:R-HSA-1604722 \"Activation of proMMP9 by proteases\"\nxref: Reactome:R-HSA-1604731 \"Autocatalytic activation of MMP3\"\nxref: Reactome:R-HSA-1604732 \"Autocatalytic activation of proMMP13\"\nxref: Reactome:R-HSA-1604741 \"Initial activation of proMMP13 by MMP14 (MT1-MMP)\"\nxref: Reactome:R-HSA-1604752 \"Initial activation of proMMP13 by MMP3\"\nxref: Reactome:R-HSA-1604763 \"Autocatalytic activation of MMP7\"\nxref: Reactome:R-HSA-163798 \"Furin cleaves pro-protein Z to protein Z\"\nxref: Reactome:R-HSA-163843 \"Furin cleaves pro-GAS6 to GAS6\"\nxref: Reactome:R-HSA-1655842 \"S1P hydrolyzes SREBP1A,1C,2\"\nxref: Reactome:R-HSA-166753 \"Conversion of C4 into C4a and C4b\"\nxref: Reactome:R-HSA-166792 \"Conversion of C2 into C2a and C2b\"\nxref: Reactome:R-HSA-166817 \"Cleavage of C3 by C3 convertases\"\nxref: Reactome:R-HSA-170844 \"Latent TGF-beta-1 is cleaved by FURIN\"\nxref: Reactome:R-HSA-171288 \"Cleavage of the viral Env gp160 precursor polyprotein\"\nxref: Reactome:R-HSA-173626 \"Activation of C1r\"\nxref: Reactome:R-HSA-173631 \"Activation of C1s\"\nxref: Reactome:R-HSA-173680 \"Activation of C5\"\nxref: Reactome:R-HSA-173745 \"Factor D cleaves C3(H2O)-bound Factor B\"\nxref: Reactome:R-HSA-174551 \"Formation of alternative pathway C5 convertase\"\nxref: Reactome:R-HSA-1799329 \"Signal peptidase hydrolyzes signal peptide from ribosome-associated nascent protein\"\nxref: Reactome:R-HSA-183122 \"Factor D cleaves C3b-bound Factor B\"\nxref: Reactome:R-HSA-183130 \"C3(H2O):Factor Bb cleaves C3 to C3b and C3a\"\nxref: Reactome:R-HSA-186785 \"PDGF-AA clevage by Furin\"\nxref: Reactome:R-HSA-187020 \"Part of pro-beta-NGF is processed to mature beta-NGF\"\nxref: Reactome:R-HSA-1912369 \"NOTCH precursor cleaved to form mature NOTCH\"\nxref: Reactome:R-HSA-1912372 \"Fringe-modified Pre-NOTCH is cleaved by FURIN\"\nxref: Reactome:R-HSA-2022411 \"Cathepsin G hydrolyzes AGT(25-34) (Angiotensin-(1-10)) to AGT(25-32) (Angiotensin-(1-8))\"\nxref: Reactome:R-HSA-2129357 \"Fibrillin C-terminal processing\"\nxref: Reactome:R-HSA-2168923 \"Collagen type XVIII endostatin release\"\nxref: Reactome:R-HSA-2168960 \"Collagen type XVII ectodomain shedding\"\nxref: Reactome:R-HSA-2172405 \"Collagen type XXIII ectodomain shedding\"\nxref: Reactome:R-HSA-2214330 \"Cleavage of collagen VII NC2 region by BMP1\"\nxref: Reactome:R-HSA-2471621 \"Endostatin degradation by cathepsins\"\nxref: Reactome:R-HSA-2471842 \"Collagen type XXV ectomain shedding\"\nxref: Reactome:R-HSA-2482180 \"Collagen type VIII degradation by ELANE\"\nxref: Reactome:R-HSA-2514772 \"Fibrillin-1 degradation by MMP3, CTSK, CTSL2\"\nxref: Reactome:R-HSA-2514823 \"Fibrillin-1 degradation by ELANE\"\nxref: Reactome:R-HSA-2534160 \"HSPG2 (perlecan) degradation by MMP13, CTSS\"\nxref: Reactome:R-HSA-2534206 \"E-cadherin degradation by PS1:NCSTN (Gamma-secretase)\"\nxref: Reactome:R-HSA-2534260 \"E-cadherin degradation by caspase-3 and calpain-1\"\nxref: Reactome:R-HSA-265301 \"Corticotropin cleavage from POMC\"\nxref: Reactome:R-HSA-3244626 \"DENV protease NS2B3 cleaves STING\"\nxref: Reactome:R-HSA-3266557 \"Factor I cleaves iC3b\"\nxref: Reactome:R-HSA-3785684 \"Fibronectin degradation by CTSG\"\nxref: Reactome:R-HSA-3788061 \"Fibronectin degradation by ADAM8\"\nxref: Reactome:R-HSA-381135 \"MBTPS1 (S1P) cleaves ATF6 (ATF6-alpha)\"\nxref: Reactome:R-HSA-381446 \"Thrombin proteolyzes IGF:IGFBP3:ALS\"\nxref: Reactome:R-HSA-381461 \"Plasmin proteolyzes IGF:IGFBP-3:ALS\"\nxref: Reactome:R-HSA-381466 \"Prostate-specific Antigen proteolyzes IGF:IGFBP3:ALS\"\nxref: Reactome:R-HSA-3814820 \"HSPG2 (perlecan) is cleaved by BMP1, TLL1, TLL2, Cathepsin L1\"\nxref: Reactome:R-HSA-381500 \"Cathepsin G proteolyzes IGF:IGFBP3:ALS\"\nxref: Reactome:R-HSA-381798 \"PCSK1 hydrolyzes Proglucagon to Glucagon-like Peptide-1\"\nxref: Reactome:R-HSA-382061 \"Extracellular processing of novel PDGFs\"\nxref: Reactome:R-HSA-3928657 \"MMP2,9 cleave EPHB\"\nxref: Reactome:R-HSA-400459 \"Signal peptidase hydrolyzes preproGLP-1 to proGLP-1\"\nxref: Reactome:R-HSA-400492 \"PCSK1 hydrolyzes proGIP to GIP\"\nxref: Reactome:R-HSA-400496 \"Signal peptidase hydrolyzes preproGIP to proGIP\"\nxref: Reactome:R-HSA-422021 \"PCSK1 hydrolyzes acyl Proghrelin to acyl Ghrelin\"\nxref: Reactome:R-HSA-422051 \"Cleavage of the signal peptide of Preproghrelin\"\nxref: Reactome:R-HSA-5210912 \"Furin cleaves ANTXR2-bound pagA to yield pagA(197-794)\"\nxref: Reactome:R-HSA-5210935 \"Furin cleaves ANTXR1-bound pagA to yield pagA(197-794)\"\nxref: Reactome:R-HSA-5578783 \"CORIN(802-1042) hydrolyses NPPA to form NPPA(124-151)\"\nxref: Reactome:R-HSA-5591040 \"Activated protein C cleaves Factor Va intermediate form for Factor Va\"\nxref: Reactome:R-HSA-5607002 \"Activated protein C cleaves factor VIIIa\"\nxref: Reactome:R-HSA-5691512 \"APEH hydrolyses NAc-Ser-protein\"\nxref: Reactome:R-HSA-6800198 \"HPN heterodimer cleaves pro-MST1 to form MST1 dimer\"\nxref: Reactome:R-HSA-6800200 \"HPN heterodimer cleaves pro-HGF to form HGF dimer\"\nxref: Reactome:R-HSA-6800299 \"HGFAC cleaves pro-HGF to form HGF dimer\"\nxref: Reactome:R-HSA-6801687 \"PRTN3 cleaves CAMP(31-170) to generate CAMP(134-170)\"\nxref: Reactome:R-HSA-6807224 \"Furin cleaves pro-BGLAP to BGLAP\"\nxref: Reactome:R-HSA-8849826 \"ST14 hydrolyzes and activates KLK5\"\nxref: Reactome:R-HSA-8849857 \"KLK5 cleaves and activates CELA2\"\nxref: Reactome:R-HSA-8850831 \"KLK5 cleaves and activates KLK8\"\nxref: Reactome:R-HSA-8852716 \"Thrombin, ELANE cleave C5\"\nxref: Reactome:R-HSA-8855825 \"HTRA1 hydrolyzes ACAN (Aggrecan)\"\nxref: Reactome:R-HSA-8865275 \"PDGF-BB clevage by Furin\"\nxref: Reactome:R-HSA-8865276 \"PDGF-AB clevage by Furin\"\nxref: Reactome:R-HSA-8874145 \"MBTPS1 (S1P) cleaves ATF6B (ATF6-beta)\"\nxref: Reactome:R-HSA-8874186 \"MBTPS1 (S1P) cleaves CREB3L4\"\nxref: Reactome:R-HSA-8874204 \"MBTPS1 (S1P) cleaves CREB3\"\nxref: Reactome:R-HSA-8874205 \"MBTPS1 (S1P) cleaves CREB3L2\"\nxref: Reactome:R-HSA-8874206 \"MBTPS1 (S1P) cleaves CREB3L3\"\nxref: Reactome:R-HSA-8874212 \"MBTPS1 (S1P) cleaves CREB3L1\"\nxref: Reactome:R-HSA-9023178 \"PCSK2 cleaves Insulin(57-110) to yield Insulin(90-110) and C-peptide (Insulin(57-89))\"\nxref: Reactome:R-HSA-9023196 \"PCSK1 cleaves proinsulin to yield Insulin(25-56) and Insulin(57-110)\"\nxref: Reactome:R-HSA-9023626 \"DPP4(39-766) hydrolyzes Glucose-dependent Insulinotropic Polypeptide (GIP)\"\nxref: Reactome:R-HSA-9023627 \"DPP4(1-766) hydrolyzes Glucose-dependent Insulinotropic Polypeptide (GIP)\"\nxref: Reactome:R-HSA-9023632 \"DPP4(39-766) hydrolyzes Glucagon-like Peptide-1 (GLP-1)\"\nxref: Reactome:R-HSA-9023633 \"DPP4(1-766) hydrolyzes Glucagon-like Peptide-1 (GLP-1)\"\nxref: Reactome:R-HSA-9033490 \"TYSND1 cleaves PHYH\"\nxref: Reactome:R-HSA-9033506 \"TYSND1 cleaves AGPS\"\nxref: Reactome:R-HSA-9033515 \"TYSND1 cleaves ACOX1\"\nxref: Reactome:R-HSA-9033520 \"TYSND1 cleaves TYSND1\"\nxref: Reactome:R-HSA-9033524 \"TYSND1 cleaves SCP2\"\nxref: Reactome:R-HSA-9033529 \"TYSND1 cleaves ACAA1\"\nxref: Reactome:R-HSA-9033530 \"TYSND1 cleaves HSD17B4\"\nxref: Reactome:R-HSA-9653249 \"Cleavage of factor XII variant by activated thrombin\"\nxref: Reactome:R-HSA-9655046 \"Cleavage of FXII variant by KLKB1\"\nxref: Reactome:R-HSA-9662786 \"FURIN cleaves ADAM17\"\nxref: Reactome:R-HSA-9666383 \"F8 variant is not cleaved by thrombin\"\nxref: Reactome:R-HSA-9668253 \"Hyperactivation of factor X by FVIIIa:FIXa R384L\"\nxref: Reactome:R-HSA-9668365 \"FVIIIa variant:FIXa does not convert FX to the active FXa\"\nxref: Reactome:R-HSA-9670874 \"FIXa variant:FVIIIa does not convert FX to the active FXa\"\nxref: Reactome:R-HSA-9673223 \"FIX(29-461) variant is not activated (factor XIa catalyst)\"\nxref: Reactome:R-HSA-9686710 \"Cleavage of S protein into S1:S2\"\nxref: Reactome:R-HSA-9686731 \"TMPRSS2 Mediated SARS-CoV-1 Spike Protein Cleavage and Endocytosis\"\nxref: Reactome:R-HSA-9694287 \"Cleavage of S protein into S1:S2\"\nxref: Reactome:R-HSA-9694661 \"TMPRSS2 Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis\"\nxref: Reactome:R-HSA-9698988 \"Direct Host Cell Membrane Membrane Fusion and Release of SARS-CoV-2 Nucleocapsid\"\nxref: Reactome:R-HSA-9699007 \"FURIN Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis\"\nxref: Reactome:R-HSA-9708859 \"Activated thrombin (factor IIa) cleaves F2R (PAR1), activating it\"\nxref: Reactome:R-HSA-9710106 \"ELANE cleaves GSDMD\"\nxref: Reactome:R-HSA-9710263 \"GZMB cleaves GSDME\"\nxref: Reactome:R-HSA-976743 \"Factor I inactivates plasma Factor H-bound C3b\"\nxref: Reactome:R-HSA-9769949 \"FURIN Mediated SARS-CoV-2 Spike Protein Cleavage\"\nxref: Reactome:R-HSA-9770187 \"S2 Cleavage by TMPRSS2 Exposes S2' Initiating Cell-Cell Fusion\"\nxref: Reactome:R-HSA-977371 \"Factor I inactivates Factor H-boundC3b\"\nxref: Reactome:R-HSA-977615 \"Factor I inactivates MCP/CR1-bound C4b/C3b\"\nxref: Reactome:R-HSA-9816275 \"CDH1 is proteolytically cleaved in Golgi\"\nxref: Reactome:R-HSA-9829030 \"Nascent F signal peptide is cleaved at ER membrane\"\nxref: Reactome:R-HSA-9829200 \"F0 is cleaved, releasing F1, F2, F(110-136)\"\nxref: Reactome:R-HSA-9830805 \"Nascent sG localizes to ER lumen, gets glycosylated\"\nxref: Reactome:R-HSA-9830882 \"Nascent G signal peptide is cleaved at ER membrane\"\nxref: Reactome:R-HSA-9839367 \"TGFBR3_mem cleavage by MMPs\"\nxref: Reactome:R-HSA-9911236 \"ELANE cleaves NOTCH2NLA\"\nxref: Reactome:R-HSA-9911383 \"LepB cleaves prepro-STa\"\nxref: Reactome:R-HSA-9912368 \"LepB cleaves pre-EltA\"\nxref: Reactome:R-HSA-9912371 \"LepB cleaves pre-EltB\"\nxref: Reactome:R-HSA-9913329 \"Autoproteolysis of DAG1 to alpha and beta chains\"\nxref: Reactome:R-HSA-9918772 \"Dengue polyprotein cis-auto-cleaves\"\nxref: Reactome:R-HSA-9918780 \"Unknown peptidase cleaves NS1-NS2A\"\nxref: Reactome:R-HSA-9918787 \"NS2B3 cleaves C-prM-E-NS1-NS2A\"\nxref: Reactome:R-HSA-9918795 \"Signalase cleaves prM-E-NS1-NS2A\"\nxref: Reactome:R-HSA-9918813 \"NS2B3 cleaves NS4AB\"\nxref: Reactome:R-HSA-9918817 \"NS2B3 cleaves polyprotein\"\nxref: Reactome:R-HSA-9918823 \"NS345:NS2B cleaves NS345\"\nxref: Reactome:R-HSA-9918871 \"Signalase cleaves prepro-NS4B\"\nxref: Reactome:R-HSA-9918876 \"NS2B3 cleaves prepro-C at the C-prM junction\"\nxref: Reactome:R-HSA-9919050 \"Furin cleaves prM:E\"\nxref: Reactome:R-HSA-9921595 \"NS2B3 cleaves FAM134B\"\nxref: Reactome:R-HSA-9921689 \"NS3 cleaves GrpEL1\"\nxref: Reactome:R-HSA-9926936 \"EspC(54-1018) cleaves hemoglobin\"\nxref: Reactome:R-HSA-9926963 \"Hbp cis-autocleaves\"\nxref: Reactome:R-HSA-9927009 \"Hbp(53-1100) cleaves hemoglobin\"\nxref: Reactome:R-HSA-9932162 \"Removal of CDH1 signal peptide\"\nxref: Reactome:R-HSA-9947496 \"ACOT2 cleaves NS345\"\nis_a: GO:0004175 ! endopeptidase activity\nis_a: GO:0008236 ! serine-type peptidase activity\nproperty_value: skos:exactMatch EC:3.4.21.-\nproperty_value: skos:narrowMatch EC:3.4.21.1\nproperty_value: skos:narrowMatch EC:3.4.21.10\nproperty_value: skos:narrowMatch EC:3.4.21.102\nproperty_value: skos:narrowMatch EC:3.4.21.20\nproperty_value: skos:narrowMatch EC:3.4.21.21\nproperty_value: skos:narrowMatch EC:3.4.21.22\nproperty_value: skos:narrowMatch EC:3.4.21.26\nproperty_value: skos:narrowMatch EC:3.4.21.27\nproperty_value: skos:narrowMatch EC:3.4.21.34\nproperty_value: skos:narrowMatch EC:3.4.21.35\nproperty_value: skos:narrowMatch EC:3.4.21.36\nproperty_value: skos:narrowMatch EC:3.4.21.38\nproperty_value: skos:narrowMatch EC:3.4.21.39\nproperty_value: skos:narrowMatch EC:3.4.21.4\nproperty_value: skos:narrowMatch EC:3.4.21.41\nproperty_value: skos:narrowMatch EC:3.4.21.42\nproperty_value: skos:narrowMatch EC:3.4.21.43\nproperty_value: skos:narrowMatch EC:3.4.21.45\nproperty_value: skos:narrowMatch EC:3.4.21.46\nproperty_value: skos:narrowMatch EC:3.4.21.47\nproperty_value: skos:narrowMatch EC:3.4.21.48\nproperty_value: skos:narrowMatch EC:3.4.21.5\nproperty_value: skos:narrowMatch EC:3.4.21.53\nproperty_value: skos:narrowMatch EC:3.4.21.54\nproperty_value: skos:narrowMatch EC:3.4.21.59\nproperty_value: skos:narrowMatch EC:3.4.21.6\nproperty_value: skos:narrowMatch EC:3.4.21.61\nproperty_value: skos:narrowMatch EC:3.4.21.62\nproperty_value: skos:narrowMatch EC:3.4.21.68\nproperty_value: skos:narrowMatch EC:3.4.21.69\nproperty_value: skos:narrowMatch EC:3.4.21.7\nproperty_value: skos:narrowMatch EC:3.4.21.71\nproperty_value: skos:narrowMatch EC:3.4.21.73\nproperty_value: skos:narrowMatch EC:3.4.21.75\nproperty_value: skos:narrowMatch EC:3.4.21.78\nproperty_value: skos:narrowMatch EC:3.4.21.79\nproperty_value: skos:narrowMatch EC:3.4.21.83\nproperty_value: skos:narrowMatch EC:3.4.21.88\nproperty_value: skos:narrowMatch EC:3.4.21.9\nproperty_value: skos:narrowMatch EC:3.4.21.92\nproperty_value: skos:narrowMatch EC:3.4.21.93\nproperty_value: skos:narrowMatch EC:3.4.21.94\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004252"
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
  "source_locator": "lines 44157-44170",
  "excerpt": "[Term]\nid: GO:0004536\nname: DNA nuclease activity\nnamespace: molecular_function\nalt_id: GO:0004537\ndef: \"Catalysis of the cleavage of ester linkages within deoxyribonucleic acid.\" [GOC:mah, ISBN:0198547684]\nsynonym: \"caspase-activated deoxyribonuclease activity\" NARROW []\nsynonym: \"deoxyribonuclease activity\" EXACT []\nxref: Reactome:R-HSA-211247 \"Cleavage of DNA by DFF40\"\nxref: Reactome:R-HSA-5685994 \"Long-range resection of DNA DSBs by EXO1 or DNA2\"\nxref: Reactome:R-HSA-6785986 \"DNA nucleases unhook the interstrand crosslink (ICL)\"\nis_a: GO:0004518 ! nuclease activity\nis_a: GO:0140097 ! catalytic activity, acting on DNA\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004536"
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
  "source_locator": "lines 52078-52112",
  "excerpt": "[Term]\nid: GO:0004930\nname: G protein-coupled receptor activity\nnamespace: molecular_function\nalt_id: GO:0001622\nalt_id: GO:0001623\nalt_id: GO:0001624\nalt_id: GO:0001625\nalt_id: GO:0016526\ndef: \"Combining with an extracellular signal and transmitting the signal across the membrane by activating an associated G-protein; promotes the exchange of GDP for GTP on the alpha subunit of a heterotrimeric G-protein complex.\" [GOC:bf, Wikipedia:GPCR]\nsubset: goslim_chembl\nsynonym: \"EBV-induced receptor\" NARROW []\nsynonym: \"Epstein-Barr Virus-induced receptor activity\" NARROW []\nsynonym: \"G protein coupled receptor activity\" EXACT []\nsynonym: \"G protein linked receptor activity\" EXACT []\nsynonym: \"G-protein coupled receptor activity\" EXACT []\nsynonym: \"G-protein coupled receptor activity, unknown ligand\" NARROW []\nsynonym: \"G-protein linked receptor activity\" EXACT []\nsynonym: \"GPCR activity\" EXACT []\nsynonym: \"ligand-dependent GPCR activity\" EXACT []\nsynonym: \"Mas proto-oncogene receptor activity\" NARROW []\nsynonym: \"orphan G protein coupled receptor activity\" NARROW []\nsynonym: \"orphan G-protein coupled receptor activity\" NARROW []\nsynonym: \"orphan GPCR activity\" NARROW []\nsynonym: \"RDC1 receptor activity\" NARROW []\nsynonym: \"receptor activity, G-protein coupled\" EXACT [GOC:bf]\nsynonym: \"SREB receptor\" NARROW []\nsynonym: \"super conserved receptor expressed in brain receptor activity\" NARROW []\nxref: Reactome:R-HSA-114552 \"Thrombin-activated PARs activate G12/13\"\nxref: Reactome:R-HSA-114558 \"Thrombin-activated PARs activate Gq\"\nxref: Reactome:R-HSA-167408 \"The high affinity receptor complex binds to G-protein\"\nxref: Reactome:R-HSA-381706 \"GLP1R:GLP1 activates G(s)\"\nxref: Wikipedia:GPCR\nis_a: GO:0004888 ! transmembrane signaling receptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004930"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 80903-80940",
  "excerpt": "[Term]\nid: GO:0008233\nname: peptidase activity\nnamespace: molecular_function\nalt_id: GO:0070010\nalt_id: GO:0070011\ndef: \"Catalysis of the hydrolysis of a peptide bond. A peptide bond is a covalent bond formed when the carbon atom from the carboxyl group of one amino acid shares electrons with the nitrogen atom from the amino group of a second amino acid.\" [EC:3.4.-.-, GOC:jl]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_yeast\nsynonym: \"hydrolase, acting on peptide bonds\" EXACT []\nsynonym: \"peptidase activity, acting on D-amino acid peptides\" NARROW []\nsynonym: \"peptidase activity, acting on L-amino acid peptides\" NARROW []\nsynonym: \"peptide hydrolase activity\" EXACT []\nsynonym: \"protease activity\" EXACT []\nsynonym: \"proteinase activity\" NARROW []\nxref: EC:3.4.-.-\nxref: Reactome:R-HSA-205112 \"gamma-secretase cleaves p75NTR, releasing NRIF and TRAF6\"\nxref: Reactome:R-HSA-3000243 \"Unknown lysosomal protease degrades CBLIF:RCbl to release Cbl\"\nxref: Reactome:R-HSA-3000263 \"TCN2:RCbl is degraded to release RCbl\"\nxref: Reactome:R-HSA-3065958 \"An unknown protease degrades ACACA\"\nxref: Reactome:R-HSA-3065959 \"An unknown protease degrades hCBXs\"\nxref: Reactome:R-HSA-3139027 \"Maturation of HIV Virion\"\nxref: Reactome:R-HSA-376149 \"Proteolytic processing of SLIT\"\nxref: Reactome:R-HSA-4167501 \"An unknown protease degrades ACACB\"\nxref: Reactome:R-HSA-448678 \"CTSG cleaves CASP1(1-404)\"\nxref: Reactome:R-HSA-5655483 \"USP1 autocleavage\"\nxref: Reactome:R-HSA-5684864 \"NAPSA, CTSH, PGA3-5 cleave pro-SFTPB\"\nxref: Reactome:R-HSA-5685902 \"NAPSA, CTSH, PGA3-5 cleave pro-SFTPC\"\nxref: Reactome:R-HSA-6803060 \"DCD(63-110) is processed to DCD(63-109)\"\nxref: Reactome:R-HSA-9935547 \"Lysosomal degradation of ubiqutinated CDH1\"\nis_a: GO:0016787 ! hydrolase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:exactMatch EC:3.4.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008233"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
