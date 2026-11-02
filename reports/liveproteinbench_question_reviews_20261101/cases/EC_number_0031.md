# EC_number_0031

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.26.3

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGLQLMTPASSPMGPFFGLPWQQEAIHDNIYTPRKYQVELLEAALDHNTIVCLNSGSGKTFIAVLLSKELSYQIRGDFSKNAKRTVFLVNSEKQVSQQVSAVRTHTDLKVGEYSDLQKTQCWAKEKWYQEFETRQVLVMTCHIFLNVLKSGNVSLSNINLLVFDECHLAIQDHPYREIMKICESCQPCPRILGLTASILNGKCDPRDLEEKIQKLEKILRSNAETATDLVVLDRYASQPCEIVLDCGPYVDRSGLFQRLLNELDEALNFLIDCNISTHSKERDSTIISKQILSDCRAVLLVLGPWCADKVAGMMVRELQKYIKHEQEELHRKFLLFTDTILRKIHALCEEHFSPASLDMKFVTPKVIKLLEILRKYKPYERQQFESVEWYNNRNQDNYVSWSDSEDDDDDEDEEIEEKEKTETSFPSPFTNILCGIIFVERRYTAVVLNRLIKEAGKQDPELAYISSNFITGHGIGKNQPRNKQMEVEFRKQEEVLRKFRAHETNLLIATSIVEEGVDIPKCNLVVRFDLPSEYRSYVQSKGRARAPISNYIMLADSDKIKTFEEDLKTYKAIEKILRNKCSKSIDCGNTESEPVVDDDEIFPPYVLRQDDGSPRVTINTAIGHINRYCARLPSDPFTHLAPKCKTREMSDGPYRSTLYLPINSPLRAPIVGPPMNCARLAERAVALICCKKLHEIGELDDHLMPVGKETVKYEEELDLHDEEETSVPGRPGSTKRRQCYPKAIPECLRNSYPKPGQPCYLYVIGMVLTTPLPDELNFRRRKLYPPEDTTRCFGILTAKPIPQIPHFPVYTRSGEVTISIELKKSGFTLNLEQLELITRLHQYIFSHILRLEKPALEFKPTVADCAYCVLPLNVVNDSGTLDIDFKFVEDIEKSEARTGIPNTQYSAESPFIFKLEDYQDAVIIPRYRNFDQPHRFYVADVYTDLTPLSKFPSPEYETFAEYYKTKYNLDLTNLNQPLLDVDHTSSRLNLLTPRHLNQKGKALPLSSAEKRKAKWESLQNKQILVPELCAIHPVPASLWRKAVCLPSILYRLHCLLTAEELRAQTAIDAGVGVKSLPEDFRYPNLDFGWKRSIDSKTFISSQSSSAVESEGDCRLNTTMVPDSATSSAANHVIYTQTNDQMSVNCTPLCQKSLSDLRGVCFSEDYKAINGVSCNGVTSDSEAESGVCFQKDERIACTQEIPEKSTSFHIQNLPKENQPILNECTLSKKFLDGNVSKPTSDECPSTCTSDMQYESGLSNGYSSKTLGPNPGLILQALTLSNASDGFNLERLEMLGDSFLKHAITTYLFCTYPDAHEGRLSYMRSKKVSNCNLYRLGKKKGSPSRMVVSIFDPPVNWLPPGYIVNQDKSSDKWESNETSGEGVMANGKIDEDFDDDDEEDEDLMWRNPKEETDFDDDFLEYDQEHIKFIDSMLMGSGAFVKKIPLSSFAPPDQNYEWRAPKKPLLESAQFPSEFDDFDYSSWDAMCYLDPSKAVEEDDFVVGFWNPSEENCGTDVGKQSISYDLHTEQCIADKSIADCVEALLGCYLTSCGERAAQLFLCSLGLKVLPQVRRSVTSTNSISASSSYQKTSTRDICTLNSELSSCKGVEYGYLKIPPRCMFEHPDAEKTLDHLISGFENFEKKINYPFKNKAYLLQAFTHASYHYNTITDCYQRLEFLGDAILDYLITKHLYEDPRQHSPGVLTDLRSALVNNTIFASLAVKYDYHKYFKAISPELFHVIDDFVQFQLEKNEMQGMDSELRRSEEDEEKEEDIEVPKAMGDIFESLAGAIYMDSGMSLETVWRVYYPMMHPLIEKFSANVPRSPVRELLEMEPETAKFSPAERTYDGKVRVTVEVVGKGKFKGVGRSYRIAKSAAARRALRSLKANQSQVPNS

[Multiple Choices]
A. 3.1.3.112
B. 3.1.26.3
C. 3.6.1.5
D. 1.5.1.38
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

> The exact 1,891-aa sequence matches the UniProt entry annotated as Dicer-L with EC 3.1.26.3; its catalytic-activity annotation gives endonucleolytic cleavage to a 5′-phosphomonoester. The evidence is annotation-based and transferred from another UniProt entry, not direct experimental confirmation for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has a Dicer-like architecture, including a P-loop helicase region and C-terminal RNase III catalytic-domain features. That supports RNA endonuclease activity and distinguishes option B from the phosphatase, triphosphatase, and dehydrogenase alternatives.


**Missing item-specific fact**

> The precise EC label is not explicitly supplied; its assignment to this sequence is supported by the reviewer-only annotation.


**Reason**

> The sequence provides a meaningful family- and catalytic-function-based argument for an RNA endonuclease, although the exact EC assignment is more specific than direct sequence inspection alone establishes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, only B matches the Dicer-like RNA endonuclease evidence.


### Important caveats

- The UniProt catalytic-activity annotation cites ECO:0000250, indicating evidence transferred by similarity; the supplied evidence does not independently establish experimental validation for this exact protein.
- The reviewer-only accession and database evidence were not present in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has a Dicer-like architecture, including a P-loop helicase region and C-terminal RNase III catalytic-domain features. That supports RNA endonuclease activity and distinguishes option B from the phosphatase, triphosphatase, and dehydrogenase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise EC label is not explicitly supplied; its assignment to this sequence is supported by the reviewer-only annotation.",
    "reason": "The sequence provides a meaningful family- and catalytic-function-based argument for an RNA endonuclease, although the exact EC assignment is more specific than direct sequence inspection alone establishes."
  },
  "case_id": "EC_number_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact 1,891-aa sequence matches the UniProt entry annotated as Dicer-L with EC 3.1.26.3; its catalytic-activity annotation gives endonucleolytic cleavage to a 5′-phosphomonoester. The evidence is annotation-based and transferred from another UniProt entry, not direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites ECO:0000250, indicating evidence transferred by similarity; the supplied evidence does not independently establish experimental validation for this exact protein.",
    "The reviewer-only accession and database evidence were not present in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, only B matches the Dicer-like RNA endonuclease evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 1,891-aa sequence matches the UniProt entry annotated as Dicer-L with EC 3.1.26.3; its catalytic-activity annotation gives endonucleolytic cleavage to a 5′-phosphomonoester. The evidence is annotation-based and transferred from another UniProt entry, not direct experimental confirmation for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has a Dicer-like architecture, including a P-loop helicase region and C-terminal RNase III catalytic-domain features. That supports RNA endonuclease activity and distinguishes option B from the phosphatase, triphosphatase, and dehydrogenase alternatives.",
    "missing_item_specific_fact": "The precise EC label is not explicitly supplied; its assignment to this sequence is supported by the reviewer-only annotation.",
    "reason": "The sequence provides a meaningful family- and catalytic-function-based argument for an RNA endonuclease, although the exact EC assignment is more specific than direct sequence inspection alone establishes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, only B matches the Dicer-like RNA endonuclease evidence."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites ECO:0000250, indicating evidence transferred by similarity; the supplied evidence does not independently establish experimental validation for this exact protein.",
    "The reviewer-only accession and database evidence were not present in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A974H8H3 (DICRL_XENLA, 1891 aa, sequence exactly matched) annotates this protein as Endoribonuclease Dicer-L with EC 3.1.26.3 and catalytic activity 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (inferred by similarity from B3DLA6), which is computational inference rather than direct experimental measurement. However, Dicer function is extensively validated in the literature, and the Swiss-Prot reviewed annotation supports the key. The sequence length (1891 aa) and domain architecture are consistent with full-length Dicer.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Walker A motif 'NSGSGKTFIAVLLSKEL' (GSGKT P-loop) in the N-terminal region, diagnostic of a helicase/ATPase domain. The overall multi-domain architecture spanning ~1900 residues with a helicase domain, PAZ domain, tandem RNase III catalytic domains, and a dsRNA-binding domain is the hallmark of Dicer. RNase III domains catalyze endonucleolytic cleavage of double-stranded RNA producing 5'-phosphomonoesters, placing the activity in EC class 3.1.26 (endoribonucleases producing 5'-phosphomonoesters). Among the four options, only B (3.1.26.3) belongs to this class; A (3.1.3.112) is a phosphomonoester phosphatase, C (3.6.1.5) acts on phosphorus-containing anhydrides, and D (1.5.1.38) is an oxidoreductase. The Walker A motif and multi-domain architecture provide concrete sequence-level grounds to exclude the non-endoribonuclease options.


**Missing item-specific fact**

> None critical. The specific assignment of 3.1.26.3 versus other 3.1.26.x sub-numbers (e.g., 3.1.26.4 for RNase III) would require recognizing Dicer-specific domain architecture, but among the provided options only one falls in the 3.1.26 class, so the reasoning path to B is tractable.


**Reason**

> A biologist familiar with Dicer domain architecture can identify the Walker A helicase motif directly in the sequence, recognize the ~1900-residue multi-domain organization as Dicer-specific, deduce endoribonuclease (RNase III) activity, and select the only endoribonuclease option. The distractors span entirely different EC top-level classes (oxidoreductase, phosphatase, anhydride hydrolase), making them distinguishable by general enzymology knowledge without needing to memorize this particular protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to four different EC top-level classes (3.1.3 phosphatase, 3.1.26 endoribonuclease, 3.6.1 anhydride hydrolase, 1.5.1 oxidoreductase). The sequence's helicase motif and multi-domain architecture clearly point to an endoribonuclease, uniquely selecting B. No other option is defensible for a Dicer-type protein.


### Important caveats

- The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity), meaning the EC assignment is computational transfer, not direct experimental measurement for this Xenopus laevis Dicer-L isoform.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt accession or annotation.
- The specific sub-number 3.1.26.3 (Dicer) versus the broader 3.1.26 class (all endoribonucleases producing 5'-phosphomonoesters) relies on recognizing Dicer-specific architecture; however, since no other 3.1.26.x option is presented, this does not create ambiguity among the given choices.
- The entry was first released in 2026_01 (Swiss-Prot), so it post-dates some benchmark construction dates; the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A motif 'NSGSGKTFIAVLLSKEL' (GSGKT P-loop) in the N-terminal region, diagnostic of a helicase/ATPase domain. The overall multi-domain architecture spanning ~1900 residues with a helicase domain, PAZ domain, tandem RNase III catalytic domains, and a dsRNA-binding domain is the hallmark of Dicer. RNase III domains catalyze endonucleolytic cleavage of double-stranded RNA producing 5'-phosphomonoesters, placing the activity in EC class 3.1.26 (endoribonucleases producing 5'-phosphomonoesters). Among the four options, only B (3.1.26.3) belongs to this class; A (3.1.3.112) is a phosphomonoester phosphatase, C (3.6.1.5) acts on phosphorus-containing anhydrides, and D (1.5.1.38) is an oxidoreductase. The Walker A motif and multi-domain architecture provide concrete sequence-level grounds to exclude the non-endoribonuclease options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific assignment of 3.1.26.3 versus other 3.1.26.x sub-numbers (e.g., 3.1.26.4 for RNase III) would require recognizing Dicer-specific domain architecture, but among the provided options only one falls in the 3.1.26 class, so the reasoning path to B is tractable.",
    "reason": "A biologist familiar with Dicer domain architecture can identify the Walker A helicase motif directly in the sequence, recognize the ~1900-residue multi-domain organization as Dicer-specific, deduce endoribonuclease (RNase III) activity, and select the only endoribonuclease option. The distractors span entirely different EC top-level classes (oxidoreductase, phosphatase, anhydride hydrolase), making them distinguishable by general enzymology knowledge without needing to memorize this particular protein's annotation."
  },
  "case_id": "EC_number_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A974H8H3 (DICRL_XENLA, 1891 aa, sequence exactly matched) annotates this protein as Endoribonuclease Dicer-L with EC 3.1.26.3 and catalytic activity 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (inferred by similarity from B3DLA6), which is computational inference rather than direct experimental measurement. However, Dicer function is extensively validated in the literature, and the Swiss-Prot reviewed annotation supports the key. The sequence length (1891 aa) and domain architecture are consistent with full-length Dicer."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity), meaning the EC assignment is computational transfer, not direct experimental measurement for this Xenopus laevis Dicer-L isoform.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt accession or annotation.",
    "The specific sub-number 3.1.26.3 (Dicer) versus the broader 3.1.26 class (all endoribonucleases producing 5'-phosphomonoesters) relies on recognizing Dicer-specific architecture; however, since no other 3.1.26.x option is presented, this does not create ambiguity among the given choices.",
    "The entry was first released in 2026_01 (Swiss-Prot), so it post-dates some benchmark construction dates; the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four different EC top-level classes (3.1.3 phosphatase, 3.1.26 endoribonuclease, 3.6.1 anhydride hydrolase, 1.5.1 oxidoreductase). The sequence's helicase motif and multi-domain architecture clearly point to an endoribonuclease, uniquely selecting B. No other option is defensible for a Dicer-type protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A974H8H3 (DICRL_XENLA, 1891 aa, sequence exactly matched) annotates this protein as Endoribonuclease Dicer-L with EC 3.1.26.3 and catalytic activity 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (inferred by similarity from B3DLA6), which is computational inference rather than direct experimental measurement. However, Dicer function is extensively validated in the literature, and the Swiss-Prot reviewed annotation supports the key. The sequence length (1891 aa) and domain architecture are consistent with full-length Dicer.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Walker A motif 'NSGSGKTFIAVLLSKEL' (GSGKT P-loop) in the N-terminal region, diagnostic of a helicase/ATPase domain. The overall multi-domain architecture spanning ~1900 residues with a helicase domain, PAZ domain, tandem RNase III catalytic domains, and a dsRNA-binding domain is the hallmark of Dicer. RNase III domains catalyze endonucleolytic cleavage of double-stranded RNA producing 5'-phosphomonoesters, placing the activity in EC class 3.1.26 (endoribonucleases producing 5'-phosphomonoesters). Among the four options, only B (3.1.26.3) belongs to this class; A (3.1.3.112) is a phosphomonoester phosphatase, C (3.6.1.5) acts on phosphorus-containing anhydrides, and D (1.5.1.38) is an oxidoreductase. The Walker A motif and multi-domain architecture provide concrete sequence-level grounds to exclude the non-endoribonuclease options.",
    "missing_item_specific_fact": "None critical. The specific assignment of 3.1.26.3 versus other 3.1.26.x sub-numbers (e.g., 3.1.26.4 for RNase III) would require recognizing Dicer-specific domain architecture, but among the provided options only one falls in the 3.1.26 class, so the reasoning path to B is tractable.",
    "reason": "A biologist familiar with Dicer domain architecture can identify the Walker A helicase motif directly in the sequence, recognize the ~1900-residue multi-domain organization as Dicer-specific, deduce endoribonuclease (RNase III) activity, and select the only endoribonuclease option. The distractors span entirely different EC top-level classes (oxidoreductase, phosphatase, anhydride hydrolase), making them distinguishable by general enzymology knowledge without needing to memorize this particular protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four different EC top-level classes (3.1.3 phosphatase, 3.1.26 endoribonuclease, 3.6.1 anhydride hydrolase, 1.5.1 oxidoreductase). The sequence's helicase motif and multi-domain architecture clearly point to an endoribonuclease, uniquely selecting B. No other option is defensible for a Dicer-type protein."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000250 (inferred by similarity), meaning the EC assignment is computational transfer, not direct experimental measurement for this Xenopus laevis Dicer-L isoform.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) and Swiss-Prot reviewed status, but the evaluated model had no access to the UniProt accession or annotation.",
    "The specific sub-number 3.1.26.3 (Dicer) versus the broader 3.1.26 class (all endoribonucleases producing 5'-phosphomonoesters) relies on recognizing Dicer-specific architecture; however, since no other 3.1.26.x option is presented, this does not create ambiguity among the given choices.",
    "The entry was first released in 2026_01 (Swiss-Prot), so it post-dates some benchmark construction dates; the author's source snapshot is unknown."
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

**Accession:** `A0A974H8H3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:07.960553+00:00.  

```json
"A0A974H8H3"
```

Source SHA-256: `b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:07.960553+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"3.1.26.3"}],"fullName":{"value":"Endoribonuclease Dicer-L"}}}
```

Source SHA-256: `b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:07.960553+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.26.3","evidences":[{"evidenceCode":"ECO:0000250","id":"B3DLA6","source":"UniProtKB"}],"name":"Endonucleolytic cleavage to 5'-phosphomonoester."}}
```

Source SHA-256: `b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:26:10.677603+00:00.  

```text
ID   DICRL_XENLA             Reviewed;        1891 AA.
AC   A0A974H8H3; A0A1L8F9L1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-FEB-2023, sequence version 1.
DT   28-JAN-2026, entry version 15.
DE   RecName: Full=Endoribonuclease Dicer-L;
DE            EC=3.1.26.3;
GN   Name=dicer1.L; Synonyms=dicer1;
OS   Xenopus laevis (African clawed frog).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;
OC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Xenopus.
OX   NCBI_TaxID=8355;
```

Source SHA-256: `41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:26:10.677603+00:00.  

```text
DE   RecName: Full=Endoribonuclease Dicer-L;
DE            EC=3.1.26.3;
```

Source SHA-256: `41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)  
**Locator:** `lines 62-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:26:10.677603+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endonucleolytic cleavage to 5'-phosphomonoester.; EC=3.1.26.3;
CC         Evidence={ECO:0000250|UniProtKB:B3DLA6};
```

Source SHA-256: `41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
