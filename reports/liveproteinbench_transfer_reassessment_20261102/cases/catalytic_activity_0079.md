# catalytic_activity_0079: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0079.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **B** — Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-&#124;-Ser- bond.

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
A. glycyl-tRNA(Gly) + acetyl-CoA = N-acetylglycyl-tRNA(Gly) + CoA + H(+)
B. Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.
C. N-acetyl-D-glutamate = N-acetyl-L-glutamate
D. norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)
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

> The sequence exactly matches a UniProt entry annotated as an alphavirus structural polyprotein with the catalytic activity in choice B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), so it supports the key but does not establish direct experimental verification for this sequence.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and its hydrophobic regions are compatible with a viral structural polyprotein, making B more plausible than the listed reactions for small soluble enzymes. That architecture alone does not establish the specific autocatalytic cleavage or the Trp-Ser bond.


**Missing item-specific fact**

> That this particular sequence is an alphavirus structural polyprotein whose capsid protein is released by autocatalytic hydrolysis at a Trp-Ser bond.


**Reason**

> Choosing B's specific reaction requires a protein-specific functional annotation or equivalent external knowledge; generic sequence architecture does not determine that cleavage chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions are distinct, and the sequence-matched annotation supports B; no other option is comparably supported by the supplied sequence.


### Important caveats

- The sequence match applies to the current and retrieved historical UniProt records, but the author's exact source snapshot is unknown.
- The catalytic-activity evidence is transferred from another UniProt entry rather than shown here as direct experimental evidence for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence and its hydrophobic regions are compatible with a viral structural polyprotein, making B more plausible than the listed reactions for small soluble enzymes. That architecture alone does not establish the specific autocatalytic cleavage or the Trp-Ser bond.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular sequence is an alphavirus structural polyprotein whose capsid protein is released by autocatalytic hydrolysis at a Trp-Ser bond.",
    "reason": "Choosing B's specific reaction requires a protein-specific functional annotation or equivalent external knowledge; generic sequence architecture does not determine that cleavage chemistry."
  },
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry annotated as an alphavirus structural polyprotein with the catalytic activity in choice B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), so it supports the key but does not establish direct experimental verification for this sequence."
  },
  "important_caveats": [
    "The sequence match applies to the current and retrieved historical UniProt records, but the author's exact source snapshot is unknown.",
    "The catalytic-activity evidence is transferred from another UniProt entry rather than shown here as direct experimental evidence for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are distinct, and the sequence-matched annotation supports B; no other option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry annotated as an alphavirus structural polyprotein with the catalytic activity in choice B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), so it supports the key but does not establish direct experimental verification for this sequence.",
    "evidence_ids": ["C3", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence and its hydrophobic regions are compatible with a viral structural polyprotein, making B more plausible than the listed reactions for small soluble enzymes. That architecture alone does not establish the specific autocatalytic cleavage or the Trp-Ser bond.",
    "missing_item_specific_fact": "That this particular sequence is an alphavirus structural polyprotein whose capsid protein is released by autocatalytic hydrolysis at a Trp-Ser bond.",
    "reason": "Choosing B's specific reaction requires a protein-specific functional annotation or equivalent external knowledge; generic sequence architecture does not determine that cleavage chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are distinct, and the sequence-matched annotation supports B; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The sequence match applies to the current and retrieved historical UniProt records, but the author's exact source snapshot is unknown.",
    "The catalytic-activity evidence is transferred from another UniProt entry rather than shown here as direct experimental evidence for this sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein, 1319 AA, sequence SHA256 matched) annotates EC 3.4.21.90 with the exact catalytic activity text in choice B. The evidence code is ECO:0000250 (similarity/transferred from P03315, Semliki Forest virus polyprotein), so this is a computational/similarity annotation rather than direct experimental evidence for this specific SAV3 protein. Nevertheless, the sequence contains a recognizable chymotrypsin-like serine protease domain (GDSG motif, catalytic His in 'YHDGAISGY', GIVLGGGPDGRR pattern) within the N-terminal capsid region, and the overall architecture (polyprotein with multiple transmembrane domains for E1/E2/E3/6K) is consistent with alphavirus structural polyproteins that undergo autoproteolytic processing at a Trp-Ser bond. The annotation is scientifically consistent with the sequence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unambiguous chymotrypsin-like serine protease catalytic domain in the N-terminal region (catalytic His in 'YHDGAISGY', nucleophile Ser in 'GDSG', oxyanion-stabilizing GIVLGGGPDGRR motif). The protein is 1319 AA with multiple hydrophobic transmembrane segments consistent with a multi-domain polyprotein. Among the four choices, only B describes a protease (hydrolysis) reaction; A is an acetyltransferase, C is a racemase, and D is a methyltransferase—none of which are compatible with a sequence containing a serine protease domain embedded in a polyprotein architecture. The presence of a 'W|S' junction (e.g., 'FWSSVRY') further supports the Trp-Ser cleavage specificity. A model with general enzymology knowledge can eliminate A, C, and D by recognizing the absence of transferase/racemase/methyltransferase motifs and the clear presence of a protease domain.


**Missing item-specific fact**

> None critical. The specific identification as 'togavirus' and the exact phrasing 'autocatalytic release of the core protein from the N-terminus' adds specificity, but the protease-vs-non-protease distinction that separates B from A/C/D is directly inferable from sequence motifs.


**Reason**

> The serine protease catalytic triad and polyprotein architecture are identifiable from the amino acid sequence. The three distractors (acetyltransferase, racemase, methyltransferase) are categorically incompatible with a sequence bearing a serine protease domain, making B the only viable choice through general enzymological reasoning without needing to memorize the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four different EC classes (transferase, hydrolase/protease, racemase, methyltransferase). The sequence clearly encodes a protease domain, making B uniquely defensible. No other option is compatible with the observed catalytic motifs.


### Important caveats

- The UniProt annotation for EC 3.4.21.90 on Q53AM4 carries evidence code ECO:0000250 (similarity to P03315), meaning the catalytic activity assignment is transferred by homology from Semliki Forest virus rather than experimentally verified on this specific SAV3 protein.
- The exact Trp-Ser cleavage specificity is inferred from the conserved alphavirus capsid protease mechanism; direct experimental validation on SAV3 was not confirmed in the supplied evidence.
- The reviewer-only accession (Q53AM4) was inferred from dataset metadata and was not available to the evaluated model; however, the sequence-based reasoning path is self-contained.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unambiguous chymotrypsin-like serine protease catalytic domain in the N-terminal region (catalytic His in 'YHDGAISGY', nucleophile Ser in 'GDSG', oxyanion-stabilizing GIVLGGGPDGRR motif). The protein is 1319 AA with multiple hydrophobic transmembrane segments consistent with a multi-domain polyprotein. Among the four choices, only B describes a protease (hydrolysis) reaction; A is an acetyltransferase, C is a racemase, and D is a methyltransferase—none of which are compatible with a sequence containing a serine protease domain embedded in a polyprotein architecture. The presence of a 'W|S' junction (e.g., 'FWSSVRY') further supports the Trp-Ser cleavage specificity. A model with general enzymology knowledge can eliminate A, C, and D by recognizing the absence of transferase/racemase/methyltransferase motifs and the clear presence of a protease domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific identification as 'togavirus' and the exact phrasing 'autocatalytic release of the core protein from the N-terminus' adds specificity, but the protease-vs-non-protease distinction that separates B from A/C/D is directly inferable from sequence motifs.",
    "reason": "The serine protease catalytic triad and polyprotein architecture are identifiable from the amino acid sequence. The three distractors (acetyltransferase, racemase, methyltransferase) are categorically incompatible with a sequence bearing a serine protease domain, making B the only viable choice through general enzymological reasoning without needing to memorize the specific UniProt entry."
  },
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein, 1319 AA, sequence SHA256 matched) annotates EC 3.4.21.90 with the exact catalytic activity text in choice B. The evidence code is ECO:0000250 (similarity/transferred from P03315, Semliki Forest virus polyprotein), so this is a computational/similarity annotation rather than direct experimental evidence for this specific SAV3 protein. Nevertheless, the sequence contains a recognizable chymotrypsin-like serine protease domain (GDSG motif, catalytic His in 'YHDGAISGY', GIVLGGGPDGRR pattern) within the N-terminal capsid region, and the overall architecture (polyprotein with multiple transmembrane domains for E1/E2/E3/6K) is consistent with alphavirus structural polyproteins that undergo autoproteolytic processing at a Trp-Ser bond. The annotation is scientifically consistent with the sequence."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.90 on Q53AM4 carries evidence code ECO:0000250 (similarity to P03315), meaning the catalytic activity assignment is transferred by homology from Semliki Forest virus rather than experimentally verified on this specific SAV3 protein.",
    "The exact Trp-Ser cleavage specificity is inferred from the conserved alphavirus capsid protease mechanism; direct experimental validation on SAV3 was not confirmed in the supplied evidence.",
    "The reviewer-only accession (Q53AM4) was inferred from dataset metadata and was not available to the evaluated model; however, the sequence-based reasoning path is self-contained."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four different EC classes (transferase, hydrolase/protease, racemase, methyltransferase). The sequence clearly encodes a protease domain, making B uniquely defensible. No other option is compatible with the observed catalytic motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein, 1319 AA, sequence SHA256 matched) annotates EC 3.4.21.90 with the exact catalytic activity text in choice B. The evidence code is ECO:0000250 (similarity/transferred from P03315, Semliki Forest virus polyprotein), so this is a computational/similarity annotation rather than direct experimental evidence for this specific SAV3 protein. Nevertheless, the sequence contains a recognizable chymotrypsin-like serine protease domain (GDSG motif, catalytic His in 'YHDGAISGY', GIVLGGGPDGRR pattern) within the N-terminal capsid region, and the overall architecture (polyprotein with multiple transmembrane domains for E1/E2/E3/6K) is consistent with alphavirus structural polyproteins that undergo autoproteolytic processing at a Trp-Ser bond. The annotation is scientifically consistent with the sequence.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unambiguous chymotrypsin-like serine protease catalytic domain in the N-terminal region (catalytic His in 'YHDGAISGY', nucleophile Ser in 'GDSG', oxyanion-stabilizing GIVLGGGPDGRR motif). The protein is 1319 AA with multiple hydrophobic transmembrane segments consistent with a multi-domain polyprotein. Among the four choices, only B describes a protease (hydrolysis) reaction; A is an acetyltransferase, C is a racemase, and D is a methyltransferase—none of which are compatible with a sequence containing a serine protease domain embedded in a polyprotein architecture. The presence of a 'W|S' junction (e.g., 'FWSSVRY') further supports the Trp-Ser cleavage specificity. A model with general enzymology knowledge can eliminate A, C, and D by recognizing the absence of transferase/racemase/methyltransferase motifs and the clear presence of a protease domain.",
    "missing_item_specific_fact": "None critical. The specific identification as 'togavirus' and the exact phrasing 'autocatalytic release of the core protein from the N-terminus' adds specificity, but the protease-vs-non-protease distinction that separates B from A/C/D is directly inferable from sequence motifs.",
    "reason": "The serine protease catalytic triad and polyprotein architecture are identifiable from the amino acid sequence. The three distractors (acetyltransferase, racemase, methyltransferase) are categorically incompatible with a sequence bearing a serine protease domain, making B the only viable choice through general enzymological reasoning without needing to memorize the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four different EC classes (transferase, hydrolase/protease, racemase, methyltransferase). The sequence clearly encodes a protease domain, making B uniquely defensible. No other option is compatible with the observed catalytic motifs."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.90 on Q53AM4 carries evidence code ECO:0000250 (similarity to P03315), meaning the catalytic activity assignment is transferred by homology from Semliki Forest virus rather than experimentally verified on this specific SAV3 protein.",
    "The exact Trp-Ser cleavage specificity is inferred from the conserved alphavirus capsid protease mechanism; direct experimental validation on SAV3 was not confirmed in the supplied evidence.",
    "The reviewer-only accession (Q53AM4) was inferred from dataset metadata and was not available to the evaluated model; however, the sequence-based reasoning path is self-contained."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns this structural polyprotein the stated togavirus core-protein release reaction. The annotation cites evidence transferred from another UniProt entry (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long polyprotein with a basic N-terminal region followed by a protease-like region and multiple hydrophobic segments characteristic of a viral structural polyprotein. Transferable knowledge of togavirus structural polyproteins links the N-terminal capsid/core protein to autocatalytic cleavage; that distinguishes B from the unrelated tRNA acetylation, amino-acid racemization, and alkaloid methylation reactions in A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the viral polyprotein architecture and its N-terminal capsid-protease role provides a meaningful family-level inference for B without needing the exact protein's database record. The inference is strong but does not independently establish the precise cleavage reaction experimentally for this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions are distinct, and only B is consistent with the viral structural-polyprotein inference.


### Important caveats

- The supplied reviewer evidence identifies the reaction annotation as transferred from another protein; it does not establish direct experimental verification for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long polyprotein with a basic N-terminal region followed by a protease-like region and multiple hydrophobic segments characteristic of a viral structural polyprotein. Transferable knowledge of togavirus structural polyproteins links the N-terminal capsid/core protein to autocatalytic cleavage; that distinguishes B from the unrelated tRNA acetylation, amino-acid racemization, and alkaloid methylation reactions in A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the viral polyprotein architecture and its N-terminal capsid-protease role provides a meaningful family-level inference for B without needing the exact protein's database record. The inference is strong but does not independently establish the precise cleavage reaction experimentally for this sequence."
  },
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this structural polyprotein the stated togavirus core-protein release reaction. The annotation cites evidence transferred from another UniProt entry (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied reviewer evidence identifies the reaction annotation as transferred from another protein; it does not establish direct experimental verification for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions are distinct, and only B is consistent with the viral structural-polyprotein inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this structural polyprotein the stated togavirus core-protein release reaction. The annotation cites evidence transferred from another UniProt entry (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long polyprotein with a basic N-terminal region followed by a protease-like region and multiple hydrophobic segments characteristic of a viral structural polyprotein. Transferable knowledge of togavirus structural polyproteins links the N-terminal capsid/core protein to autocatalytic cleavage; that distinguishes B from the unrelated tRNA acetylation, amino-acid racemization, and alkaloid methylation reactions in A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the viral polyprotein architecture and its N-terminal capsid-protease role provides a meaningful family-level inference for B without needing the exact protein's database record. The inference is strong but does not independently establish the precise cleavage reaction experimentally for this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions are distinct, and only B is consistent with the viral structural-polyprotein inference."
  },
  "important_caveats": [
    "The supplied reviewer evidence identifies the reaction annotation as transferred from another protein; it does not establish direct experimental verification for this exact sequence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3, a Togaviridae/Alphavirus) explicitly annotates the catalytic activity as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond' (EC 3.4.21.90). The benchmark sequence matches the UniProt sequence (SHA256 confirmed). The annotation carries evidence code ECO:0000250 (similarity transfer from P03315, another alphavirus capsid protein), so it is a well-supported family-level annotation rather than direct experimental validation of this specific SAV3 protein, but the transfer within Alphavirus is highly appropriate.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1319-aa sequence exhibits a multi-domain architecture with N-terminal basic/cationic region, a papain-like protease domain (recognizable by the His in the 'GAAHC' context, adjacent Cys residues, and the overall fold pattern shared with papain-family cysteine proteases), followed by multiple transmembrane hydrophobic segments and glycoprotein-like domains. This architecture is diagnostic of a togavirus/alphavirus structural polyprotein. A model familiar with alphavirus capsid proteases (Semliki Forest Virus, Sindbis, Ross River virus) knows that (1) the N-terminal capsid domain contains an autocatalytic papain-like protease, (2) it cleaves the polyprotein at a conserved Trp-|-Ser junction to release the core protein, and (3) the large size with multiple TM domains and signal peptides is incompatible with small-molecule enzymes. The sequence itself contains a Trp-Ser junction (e.g., 'HFWSS' in the region 'IELTWGNNAPLHFWSSVRYAS'). The other options are clearly incompatible: A (tRNA acetyltransferase) requires a GNAT fold absent here; C (amino acid racemase) is a tiny enzyme incompatible with 1319 aa and TM domains; D (alkaloid O-methyltransferase) requires a Rossmann-like SAM-binding fold absent here. Family-level knowledge of alphavirus capsid proteases provides a concrete, transferable inference path to option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the papain-like protease domain, recognize the togavirus structural polyprotein architecture (large size, multiple TM segments, signal peptides, glycoprotein domains), and apply family-level knowledge from well-studied alphaviruses (SFV, Sindbis) that the capsid protease autocatalytically cleaves at Trp-Ser. The other three options involve completely different enzyme classes incompatible with the observed sequence architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes (tRNA-modifying acetyltransferase, amino acid racemase, alkaloid methyltransferase, viral autocatalytic protease). The sequence architecture unambiguously points to a viral polyprotein with a protease domain, making B the only viable choice.


### Important caveats

- The UniProt annotation for Q53AM4 uses ECO:0000250 (similarity transfer from P03315, likely Semliki Forest Virus capsid protein). Direct experimental validation of the Trp-Ser specificity specifically in SAV3 is not documented in the provided evidence, but the transfer within Alphavirus is well-justified.
- The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model.
- The Trp-Ser junction ('HFWSS') is visible in the sequence but identifying it as the specific autocatalytic cleavage site requires family knowledge rather than de novo sequence analysis alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1319-aa sequence exhibits a multi-domain architecture with N-terminal basic/cationic region, a papain-like protease domain (recognizable by the His in the 'GAAHC' context, adjacent Cys residues, and the overall fold pattern shared with papain-family cysteine proteases), followed by multiple transmembrane hydrophobic segments and glycoprotein-like domains. This architecture is diagnostic of a togavirus/alphavirus structural polyprotein. A model familiar with alphavirus capsid proteases (Semliki Forest Virus, Sindbis, Ross River virus) knows that (1) the N-terminal capsid domain contains an autocatalytic papain-like protease, (2) it cleaves the polyprotein at a conserved Trp-|-Ser junction to release the core protein, and (3) the large size with multiple TM domains and signal peptides is incompatible with small-molecule enzymes. The sequence itself contains a Trp-Ser junction (e.g., 'HFWSS' in the region 'IELTWGNNAPLHFWSSVRYAS'). The other options are clearly incompatible: A (tRNA acetyltransferase) requires a GNAT fold absent here; C (amino acid racemase) is a tiny enzyme incompatible with 1319 aa and TM domains; D (alkaloid O-methyltransferase) requires a Rossmann-like SAM-binding fold absent here. Family-level knowledge of alphavirus capsid proteases provides a concrete, transferable inference path to option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the papain-like protease domain, recognize the togavirus structural polyprotein architecture (large size, multiple TM segments, signal peptides, glycoprotein domains), and apply family-level knowledge from well-studied alphaviruses (SFV, Sindbis) that the capsid protease autocatalytically cleaves at Trp-Ser. The other three options involve completely different enzyme classes incompatible with the observed sequence architecture."
  },
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3, a Togaviridae/Alphavirus) explicitly annotates the catalytic activity as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond' (EC 3.4.21.90). The benchmark sequence matches the UniProt sequence (SHA256 confirmed). The annotation carries evidence code ECO:0000250 (similarity transfer from P03315, another alphavirus capsid protein), so it is a well-supported family-level annotation rather than direct experimental validation of this specific SAV3 protein, but the transfer within Alphavirus is highly appropriate."
  },
  "important_caveats": [
    "The UniProt annotation for Q53AM4 uses ECO:0000250 (similarity transfer from P03315, likely Semliki Forest Virus capsid protein). Direct experimental validation of the Trp-Ser specificity specifically in SAV3 is not documented in the provided evidence, but the transfer within Alphavirus is well-justified.",
    "The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model.",
    "The Trp-Ser junction ('HFWSS') is visible in the sequence but identifying it as the specific autocatalytic cleavage site requires family knowledge rather than de novo sequence analysis alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (tRNA-modifying acetyltransferase, amino acid racemase, alkaloid methyltransferase, viral autocatalytic protease). The sequence architecture unambiguously points to a viral polyprotein with a protease domain, making B the only viable choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3, a Togaviridae/Alphavirus) explicitly annotates the catalytic activity as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond' (EC 3.4.21.90). The benchmark sequence matches the UniProt sequence (SHA256 confirmed). The annotation carries evidence code ECO:0000250 (similarity transfer from P03315, another alphavirus capsid protein), so it is a well-supported family-level annotation rather than direct experimental validation of this specific SAV3 protein, but the transfer within Alphavirus is highly appropriate.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1319-aa sequence exhibits a multi-domain architecture with N-terminal basic/cationic region, a papain-like protease domain (recognizable by the His in the 'GAAHC' context, adjacent Cys residues, and the overall fold pattern shared with papain-family cysteine proteases), followed by multiple transmembrane hydrophobic segments and glycoprotein-like domains. This architecture is diagnostic of a togavirus/alphavirus structural polyprotein. A model familiar with alphavirus capsid proteases (Semliki Forest Virus, Sindbis, Ross River virus) knows that (1) the N-terminal capsid domain contains an autocatalytic papain-like protease, (2) it cleaves the polyprotein at a conserved Trp-|-Ser junction to release the core protein, and (3) the large size with multiple TM domains and signal peptides is incompatible with small-molecule enzymes. The sequence itself contains a Trp-Ser junction (e.g., 'HFWSS' in the region 'IELTWGNNAPLHFWSSVRYAS'). The other options are clearly incompatible: A (tRNA acetyltransferase) requires a GNAT fold absent here; C (amino acid racemase) is a tiny enzyme incompatible with 1319 aa and TM domains; D (alkaloid O-methyltransferase) requires a Rossmann-like SAM-binding fold absent here. Family-level knowledge of alphavirus capsid proteases provides a concrete, transferable inference path to option B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the papain-like protease domain, recognize the togavirus structural polyprotein architecture (large size, multiple TM segments, signal peptides, glycoprotein domains), and apply family-level knowledge from well-studied alphaviruses (SFV, Sindbis) that the capsid protease autocatalytically cleaves at Trp-Ser. The other three options involve completely different enzyme classes incompatible with the observed sequence architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (tRNA-modifying acetyltransferase, amino acid racemase, alkaloid methyltransferase, viral autocatalytic protease). The sequence architecture unambiguously points to a viral polyprotein with a protease domain, making B the only viable choice."
  },
  "important_caveats": [
    "The UniProt annotation for Q53AM4 uses ECO:0000250 (similarity transfer from P03315, likely Semliki Forest Virus capsid protein). Direct experimental validation of the Trp-Ser specificity specifically in SAV3 is not documented in the provided evidence, but the transfer within Alphavirus is well-justified.",
    "The reviewer-only evidence confirms the sequence matches Q53AM4 exactly, but this accession identification was not available to the evaluated model.",
    "The Trp-Ser junction ('HFWSS') is visible in the sequence but identifying it as the specific autocatalytic cleavage site requires family knowledge rather than de novo sequence analysis alone."
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
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.21.90\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"name\":\"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.\"}}",
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
  "source_locator": "lines 6-26",
  "excerpt": "DE   RecName: Full=Structural polyprotein;\nDE   AltName: Full=p130;\nDE   Contains:\nDE     RecName: Full=Capsid protein;\nDE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};\nDE     AltName: Full=Coat protein;\nDE              Short=C;\nDE   Contains:\nDE     RecName: Full=Precursor of protein E3/E2;\nDE     AltName: Full=p62;\nDE     AltName: Full=pE2;\nDE   Contains:\nDE     RecName: Full=Assembly protein E3;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E2;\nDE     AltName: Full=E2 envelope glycoprotein;\nDE   Contains:\nDE     RecName: Full=6K protein;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E1;\nDE     AltName: Full=E1 envelope glycoprotein;\n",
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
  "source_locator": "lines 119-122",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Autocatalytic release of the core protein from the N-terminus\nCC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-\nCC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
