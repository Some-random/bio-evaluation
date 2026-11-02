# catalytic_activity_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — Endonucleolytic cleavage to 5&#x27;-phosphomonoester.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGLQLMTPASSPMGPFFGLPWQQEAIHDNIYTPRKYQVELLEAALDHNIIVCLNSGSGKTFIAVLLSKELSYQIRGDFSKNAKRTVFLVNSEKQVSQQVSAVRTHTDLKVGEYSDLQKTQCWAKEKWYQEFQTHQVLVMTCHIFLNVLKTGNVSLSNINLLVFDECHLAIQDHPYRDIMKICESCQTCPRILGLTASILNGKCDPHDLEEKIQNLEEILRSNAETATDLVVLDRYASQPCEIVLDCGPYVDRSGLYQRLLNELDEALNFLTDCNISTHSKERDSTIISKQILSDCWAVLLVLGPWCADKVAGMMVRELQKYIKHEQEELHRKFLLFTDTILRKIHALCEEHFSPASLDMKFVTPKVIKLLEILRKYKPYERQQFESVEWYNNRNQDNYVSWSDSEDDDDDEDEEIEEKEKTETSFPSPFTNILCGIIFVERRYTAVVLNRLIKEAGKQDPELAYISSNFITGHGIGKNQPRNKQMEVEFRKQEEVLRKFRAHETNLLIATSIVEEGVDIPKCNLVVRFDLPSEYRSYVQSKGRARAPISNYIMLADSDKIKAFEEDLKTYKAIEKILRNKCSKSMDCGNTESEPIVDDDEIFPPYVLRQDDGSPRVTINTAIGHINRYCARLPSDPFTHLAPKCRTRELPDGPYRSTLYLPINSPLRAPIVGPPMNCARLAERAVALICCKKLHEIGELDDHLMPVGKETVKYEEELDLHDEEETSVPGRPGSTKRRQCYPKAIPECLRNSYPKPGQPCYLYVIGMVLTTPLPDELNFRRRKLYPPEDTTRCFGILTAKPIPQIPHFPVYTRSGEVTISIELKKSGFSLNLEQLELITRLHRYIFSHILRLEKPALEFKPTVADCAYCVLPLNVVNDSGTLDIDFKFVEDIEKSEARTGIPNTQYSAEGPFIFKLEDYQDAVIIPRYRNFDQPHRFYVADVYTDLTPLSKFPSPEYETFAEYYKTKYNLDLTNLNQPLLDVDHTSSRLNLLTPRHLNQKGKALPLSSAEKRKAKWESLQNKQILVPELCAIHPVPASLWRKAVCLPSILYRLHCLLTAEELRAQTAIDAGVGVKSLPEDFRYPNLDFGWKRSIDGKTFISNQSFSAMERESDCRLDITTVPDSATSSAAHHVMYTQMNDQMSVNCTPPCPKSLSDLQGVCFSDDCKAINGITCNGLTNGNWEAESGVCFQKDELIACKQEIPEKSTSFHVQNLPNDNQPILNECTLSKKFLDGNVGKPISDECPSTCTSDINYESGLSSGYSSKTLGPNPGLILQALTLSNASDGFNLERLEMLGDSFLKHAITTYLFCTYPDSHEGRLSYMRSKKVSNCNLYRLGKKKGSPSRMVVSIFDPPVNWLPPGYIVNQDKNCDKWESNETSGESVMANGKIDEDFEDEEDEDLMWRNPKEETDFDDDFLEYDQEHIKFIDNMLMGSGAFVKKIQLSAFAPPDQNYEWRPPKKPPLESAPFRSEFDDFDYSSWDAMCYLDPSKAVEEDDFVVGFWNPSEENGGADAGKQSISYDLHTEQCIADKSIADCVEALLGCYLTSCGERAAQLFLCSLGLKVLPEVRKPVTNTSTRGNYSLDGRTNSELSCKGIEYGYLKIPPRCMFEHPEAEKTLDHLISGFENFEKKINYQFKNKAYLLQAFTHASYHYNTITDCYQRLEFLGDAILDYLITKHLYEDPRQHSPGVLTDLRSALVNNTIFASLAVKYDYHKYFKAISPELFHVIDDFVQFQLEKNEMQGMDSELRRSEEDEEKEEDIEVPKAMGDIFESLAGAIYMDSGMSLETVWRVYYPMMQPLIEKFSANVPRSPVRELLEMEPETAKFSPAERTYDGKVRVMVEVVGKGKFKGVGRSYRIAKSAAARRALRSLKANQSQVPNS

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. a beta-lactam + H2O = a substituted beta-amino acid
C. (9S)-hydroperoxy-(10E,12Z,15Z)-octadecatrienoate = colnelenate + H2O
D. Endonucleolytic cleavage to 5'-phosphomonoester.
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

> The supplied sequence exactly matches a Xenopus laevis Dicer-S entry annotated with EC 3.1.26.3 and the reaction in choice D. The annotation is supported by similarity evidence, not by direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Recognizing Dicer-like domain architecture could suggest an RNase III endonuclease, but the raw sequence does not directly state the protein identity or its annotated reaction.


**Missing item-specific fact**

> The protein-specific identification as Dicer-S and its assigned catalytic activity (EC 3.1.26.3) are needed to select the reaction confidently.


**Reason**

> The sequence may support computational identification of Dicer, but selecting D depends on that protein-specific identification and activity rather than a clearly discriminating argument available from the prompt alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the Dicer-S identification, choice D is the matching reaction; the other options describe different enzyme activities.


### Important caveats

- The matched UniProt catalytic-activity annotation cites similarity evidence (ECO:0000250), rather than direct experimental evidence in the excerpts.
- The historical record also matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Recognizing Dicer-like domain architecture could suggest an RNase III endonuclease, but the raw sequence does not directly state the protein identity or its annotated reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Dicer-S and its assigned catalytic activity (EC 3.1.26.3) are needed to select the reaction confidently.",
    "reason": "The sequence may support computational identification of Dicer, but selecting D depends on that protein-specific identification and activity rather than a clearly discriminating argument available from the prompt alone."
  },
  "case_id": "catalytic_activity_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a Xenopus laevis Dicer-S entry annotated with EC 3.1.26.3 and the reaction in choice D. The annotation is supported by similarity evidence, not by direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The matched UniProt catalytic-activity annotation cites similarity evidence (ECO:0000250), rather than direct experimental evidence in the excerpts.",
    "The historical record also matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the Dicer-S identification, choice D is the matching reaction; the other options describe different enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a Xenopus laevis Dicer-S entry annotated with EC 3.1.26.3 and the reaction in choice D. The annotation is supported by similarity evidence, not by direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Recognizing Dicer-like domain architecture could suggest an RNase III endonuclease, but the raw sequence does not directly state the protein identity or its annotated reaction.",
    "missing_item_specific_fact": "The protein-specific identification as Dicer-S and its assigned catalytic activity (EC 3.1.26.3) are needed to select the reaction confidently.",
    "reason": "The sequence may support computational identification of Dicer, but selecting D depends on that protein-specific identification and activity rather than a clearly discriminating argument available from the prompt alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the Dicer-S identification, choice D is the matching reaction; the other options describe different enzyme activities."
  },
  "important_caveats": [
    "The matched UniProt catalytic-activity annotation cites similarity evidence (ECO:0000250), rather than direct experimental evidence in the excerpts.",
    "The historical record also matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A8J1LLF7 (DICRS_XENLA, Endoribonuclease Dicer-S, EC 3.1.26.3) from Xenopus laevis. The catalytic activity annotation explicitly states 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (similarity to B3DLA6), meaning the annotation is transferred by homology rather than directly experimentally validated for this specific protein, but the annotation is present and the sequence is an exact match.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 1881 amino acids long. Beta-lactamases (option B) are typically 300–400 aa; lipoxygenases (option C) are ~700–800 aa; lipid A phosphoethanolamine transferases (option A) are small membrane-associated proteins (<500 aa). All three are decisively ruled out by the large size. The sequence contains multiple 'DEDD' acidic stretches (e.g., 'DEDDDDDEDEEIEEK' and 'DEDEDLMWRNPKEETDFDDDFLEYDQE') characteristic of the RNase III catalytic tetrad. RNase III superfamily enzymes (including Dicer) are large multi-domain endoribonucleases (~1500–2000 aa) that cleave dsRNA to yield 5'-phosphomonoester and 3'-hydroxyl products. This combination of size elimination and DEDD-motif recognition provides a concrete biological argument for option D.


**Missing item-specific fact**

> None critical. The exact UniProt annotation wording is not required; the size-based elimination and RNase III DEDD-motif recognition are sufficient to identify the enzyme class and its characteristic 5'-phosphomonoester product.


**Reason**

> A knowledgeable model can eliminate A, B, and C by protein size (all are much smaller than 1881 aa) and identify the DEDD catalytic motifs diagnostic of the RNase III superfamily, whose well-known mechanism produces 5'-phosphomonoester ends. This constitutes a concrete, multi-step biological argument from the sequence itself.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent radically different enzyme classes (transferase, hydrolase of beta-lactam, oxygenase, endonuclease) with well-separated size ranges and substrate types. The 1881-aa length and DEDD motifs unambiguously point to the RNase III family, leaving no competing defensible option.


### Important caveats

- The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity to B3DLA6), indicating the annotation is transferred by homology rather than directly experimentally confirmed for this Xenopus Dicer-S entry.
- The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biochemical knowledge.
- The DEDD motifs in the sequence are embedded in longer acidic stretches and are not trivially obvious without prior knowledge of RNase III catalytic-site architecture, but they are identifiable by a well-trained biochemist.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 1881 amino acids long. Beta-lactamases (option B) are typically 300–400 aa; lipoxygenases (option C) are ~700–800 aa; lipid A phosphoethanolamine transferases (option A) are small membrane-associated proteins (<500 aa). All three are decisively ruled out by the large size. The sequence contains multiple 'DEDD' acidic stretches (e.g., 'DEDDDDDEDEEIEEK' and 'DEDEDLMWRNPKEETDFDDDFLEYDQE') characteristic of the RNase III catalytic tetrad. RNase III superfamily enzymes (including Dicer) are large multi-domain endoribonucleases (~1500–2000 aa) that cleave dsRNA to yield 5'-phosphomonoester and 3'-hydroxyl products. This combination of size elimination and DEDD-motif recognition provides a concrete biological argument for option D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact UniProt annotation wording is not required; the size-based elimination and RNase III DEDD-motif recognition are sufficient to identify the enzyme class and its characteristic 5'-phosphomonoester product.",
    "reason": "A knowledgeable model can eliminate A, B, and C by protein size (all are much smaller than 1881 aa) and identify the DEDD catalytic motifs diagnostic of the RNase III superfamily, whose well-known mechanism produces 5'-phosphomonoester ends. This constitutes a concrete, multi-step biological argument from the sequence itself."
  },
  "case_id": "catalytic_activity_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8J1LLF7 (DICRS_XENLA, Endoribonuclease Dicer-S, EC 3.1.26.3) from Xenopus laevis. The catalytic activity annotation explicitly states 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (similarity to B3DLA6), meaning the annotation is transferred by homology rather than directly experimentally validated for this specific protein, but the annotation is present and the sequence is an exact match."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity to B3DLA6), indicating the annotation is transferred by homology rather than directly experimentally confirmed for this Xenopus Dicer-S entry.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biochemical knowledge.",
    "The DEDD motifs in the sequence are embedded in longer acidic stretches and are not trivially obvious without prior knowledge of RNase III catalytic-site architecture, but they are identifiable by a well-trained biochemist."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent radically different enzyme classes (transferase, hydrolase of beta-lactam, oxygenase, endonuclease) with well-separated size ranges and substrate types. The 1881-aa length and DEDD motifs unambiguously point to the RNase III family, leaving no competing defensible option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A8J1LLF7 (DICRS_XENLA, Endoribonuclease Dicer-S, EC 3.1.26.3) from Xenopus laevis. The catalytic activity annotation explicitly states 'Endonucleolytic cleavage to 5'-phosphomonoester.' The evidence code is ECO:0000250 (similarity to B3DLA6), meaning the annotation is transferred by homology rather than directly experimentally validated for this specific protein, but the annotation is present and the sequence is an exact match.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 1881 amino acids long. Beta-lactamases (option B) are typically 300–400 aa; lipoxygenases (option C) are ~700–800 aa; lipid A phosphoethanolamine transferases (option A) are small membrane-associated proteins (<500 aa). All three are decisively ruled out by the large size. The sequence contains multiple 'DEDD' acidic stretches (e.g., 'DEDDDDDEDEEIEEK' and 'DEDEDLMWRNPKEETDFDDDFLEYDQE') characteristic of the RNase III catalytic tetrad. RNase III superfamily enzymes (including Dicer) are large multi-domain endoribonucleases (~1500–2000 aa) that cleave dsRNA to yield 5'-phosphomonoester and 3'-hydroxyl products. This combination of size elimination and DEDD-motif recognition provides a concrete biological argument for option D.",
    "missing_item_specific_fact": "None critical. The exact UniProt annotation wording is not required; the size-based elimination and RNase III DEDD-motif recognition are sufficient to identify the enzyme class and its characteristic 5'-phosphomonoester product.",
    "reason": "A knowledgeable model can eliminate A, B, and C by protein size (all are much smaller than 1881 aa) and identify the DEDD catalytic motifs diagnostic of the RNase III superfamily, whose well-known mechanism produces 5'-phosphomonoester ends. This constitutes a concrete, multi-step biological argument from the sequence itself."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent radically different enzyme classes (transferase, hydrolase of beta-lactam, oxygenase, endonuclease) with well-separated size ranges and substrate types. The 1881-aa length and DEDD motifs unambiguously point to the RNase III family, leaving no competing defensible option."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity to B3DLA6), indicating the annotation is transferred by homology rather than directly experimentally confirmed for this Xenopus Dicer-S entry.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biochemical knowledge.",
    "The DEDD motifs in the sequence are embedded in longer acidic stretches and are not trivially obvious without prior knowledge of RNase III catalytic-site architecture, but they are identifiable by a well-trained biochemist."
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

**Accession:** `A0A8J1LLF7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
"A0A8J1LLF7"
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"3.1.26.3"}],"fullName":{"value":"Endoribonuclease Dicer-S"}}}
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.26.3","evidences":[{"evidenceCode":"ECO:0000250","id":"B3DLA6","source":"UniProtKB"}],"name":"Endonucleolytic cleavage to 5'-phosphomonoester."}}
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8J1LLF7?format=txt&versions=19)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:05.098009+00:00.  

```text
DE   RecName: Full=Endoribonuclease Dicer-S;
DE            EC=3.1.26.3;
```

Source SHA-256: `1ee78b98ec19d73b1d687d332eb3f9b6453d7a8816c912104ab16c4b4c2b5ead`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8J1LLF7?format=txt&versions=19)  
**Locator:** `lines 52-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:05.098009+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endonucleolytic cleavage to 5'-phosphomonoester.; EC=3.1.26.3;
CC         Evidence={ECO:0000250|UniProtKB:B3DLA6};
```

Source SHA-256: `1ee78b98ec19d73b1d687d332eb3f9b6453d7a8816c912104ab16c4b4c2b5ead`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
