# catalytic_activity_0079

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-&#124;-Ser- bond.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q53AM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 100. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
"Q53AM4"
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commonName":"SAV3","lineage":["Viruses","Riboviria","Orthornavirae","Kitrinoviricota","Alsuviricetes","Martellivirales","Togaviridae","Alphavirus"],"scientificName":"Alphavirus salmon subtype 3","synonyms":["Norwegian salmonid alphavirus"],"taxonId":344701}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"p130"}}],"contains":[{"alternativeNames":[{"fullName":{"value":"Coat protein"},"shortNames":[{"value":"C"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"}],"value":"3.4.21.90"}],"fullName":{"value":"Capsid protein"}}},{"alternativeNames":[{"fullName":{"value":"p62"}},{"fullName":{"value":"pE2"}}],"recommendedName":{"fullName":{"value":"Precursor of protein E3/E2"}}},{"recommendedName":{"fullName":{"value":"Assembly protein E3"}}},{"alternativeNames":[{"fullName":{"value":"E2 envelope glycoprotein"}}],"recommendedName":{"fullName":{"value":"Spike glycoprotein E2"}}},{"recommendedName":{"fullName":{"value":"6K protein"}}},{"alternativeNames":[{"fullName":{"value":"E1 envelope glycoprotein"}}],"recommendedName":{"fullName":{"value":"Spike glycoprotein E1"}}}],"recommendedName":{"fullName":{"value":"Structural polyprotein"}}}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.90","evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"}],"name":"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond."}}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 1-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
ID   POLS_SAV3               Reviewed;        1319 AA.
AC   Q53AM4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-MAY-2005, sequence version 1.
DT   28-JAN-2026, entry version 100.
DE   RecName: Full=Structural polyprotein;
DE   AltName: Full=p130;
DE   Contains:
DE     RecName: Full=Capsid protein;
DE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};
DE     AltName: Full=Coat protein;
DE              Short=C;
DE   Contains:
DE     RecName: Full=Precursor of protein E3/E2;
DE     AltName: Full=p62;
DE     AltName: Full=pE2;
DE   Contains:
DE     RecName: Full=Assembly protein E3;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E2;
DE     AltName: Full=E2 envelope glycoprotein;
DE   Contains:
DE     RecName: Full=6K protein;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E1;
DE     AltName: Full=E1 envelope glycoprotein;
OS   Alphavirus salmon subtype 3 (SAV3) (Norwegian salmonid alphavirus).
OC   Viruses; Riboviria; Orthornavirae; Kitrinoviricota; Alsuviricetes;
OC   Martellivirales; Togaviridae; Alphavirus.
OX   NCBI_TaxID=344701;
OH   NCBI_TaxID=8022; Oncorhynchus mykiss (Rainbow trout) (Salmo gairdneri).
OH   NCBI_TaxID=8030; Salmo salar (Atlantic salmon).
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 6-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
DE   RecName: Full=Structural polyprotein;
DE   AltName: Full=p130;
DE   Contains:
DE     RecName: Full=Capsid protein;
DE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};
DE     AltName: Full=Coat protein;
DE              Short=C;
DE   Contains:
DE     RecName: Full=Precursor of protein E3/E2;
DE     AltName: Full=p62;
DE     AltName: Full=pE2;
DE   Contains:
DE     RecName: Full=Assembly protein E3;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E2;
DE     AltName: Full=E2 envelope glycoprotein;
DE   Contains:
DE     RecName: Full=6K protein;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E1;
DE     AltName: Full=E1 envelope glycoprotein;
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 119-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Autocatalytic release of the core protein from the N-terminus
CC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-
CC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
