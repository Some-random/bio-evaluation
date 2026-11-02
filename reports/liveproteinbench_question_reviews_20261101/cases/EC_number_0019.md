# EC_number_0019

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.26.3

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
A. 3.1.3.112
B. 3.1.26.3
C. 3.4.21.90
D. 1.97.1.13
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

> The exact sequence matches a UniProt entry annotated as Endoribonuclease Dicer-S with EC 3.1.26.3. The catalytic-activity annotation assigns that EC to endonucleolytic cleavage, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support a broad inference that this is a large RNA-processing nuclease, but they do not by themselves establish the exact four-part EC classification among the choices.


**Missing item-specific fact**

> The protein-specific Dicer-S annotation and its EC number, or equivalent evidence identifying its precise catalytic activity.


**Reason**

> Choosing the exact EC number depends on protein-specific functional annotation or recognition of this sequence; that fact is not supplied in the question. General sequence-based inference does not establish the precise EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports B; the supplied evidence does not establish another listed option for this sequence.


### Important caveats

- Reviewer-only evidence identifies the matching protein as Xenopus laevis Dicer-S; that identity and annotation were absent from the evaluated input.
- The catalytic-activity evidence is transferred by similarity, so the annotation supports the key but is not direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support a broad inference that this is a large RNA-processing nuclease, but they do not by themselves establish the exact four-part EC classification among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific Dicer-S annotation and its EC number, or equivalent evidence identifying its precise catalytic activity.",
    "reason": "Choosing the exact EC number depends on protein-specific functional annotation or recognition of this sequence; that fact is not supplied in the question. General sequence-based inference does not establish the precise EC assignment."
  },
  "case_id": "EC_number_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as Endoribonuclease Dicer-S with EC 3.1.26.3. The catalytic-activity annotation assigns that EC to endonucleolytic cleavage, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "Reviewer-only evidence identifies the matching protein as Xenopus laevis Dicer-S; that identity and annotation were absent from the evaluated input.",
    "The catalytic-activity evidence is transferred by similarity, so the annotation supports the key but is not direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports B; the supplied evidence does not establish another listed option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as Endoribonuclease Dicer-S with EC 3.1.26.3. The catalytic-activity annotation assigns that EC to endonucleolytic cleavage, but its evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support a broad inference that this is a large RNA-processing nuclease, but they do not by themselves establish the exact four-part EC classification among the choices.",
    "missing_item_specific_fact": "The protein-specific Dicer-S annotation and its EC number, or equivalent evidence identifying its precise catalytic activity.",
    "reason": "Choosing the exact EC number depends on protein-specific functional annotation or recognition of this sequence; that fact is not supplied in the question. General sequence-based inference does not establish the precise EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports B; the supplied evidence does not establish another listed option for this sequence."
  },
  "important_caveats": [
    "Reviewer-only evidence identifies the matching protein as Xenopus laevis Dicer-S; that identity and annotation were absent from the evaluated input.",
    "The catalytic-activity evidence is transferred by similarity, so the annotation supports the key but is not direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt entry A0A8J1LLF7 (DICRS_XENLA), annotated as Endoribonuclease Dicer-S from Xenopus laevis with EC 3.1.26.3. The sequence is 1881 aa, contains a DECH-box helicase motif, and exhibits the characteristic Dicer domain architecture (helicase, PAZ, RNase III). The annotation evidence code is ECO:0000250 (inferred by similarity from B3DLA6), meaning the EC assignment is a transfer annotation rather than direct experimental measurement, but it is consistent with the well-established identity and function of Dicer proteins as endoribonucleases producing 5'-phosphomonoesters.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable DECH-box motif ('FDECH' visible in the helicase domain region), and the overall ~1881-aa architecture with helicase, PAZ-like, and RNase III-like domains is characteristic of Dicer proteins. Dicer is an endoribonuclease (EC class 3.1.26). Among the four choices, only B (3.1.26.3) belongs to the endoribonuclease class; A is a phosphatase, C is a serine protease (no catalytic triad present), and D is an oxidoreductase (no redox cofactor motifs). A model with general knowledge of Dicer domain architecture and EC classification can eliminate A, C, and D and select B.


**Missing item-specific fact**

> None critical. The precise 4th digit (.3 for Dicer specifically vs. other 3.1.26.x enzymes) could in principle require memorization, but since B is the only endoribonuclease among the choices, identifying the protein as an endoribonuclease suffices.


**Reason**

> The DECH-box helicase motif is a concrete, identifiable sequence feature. Combined with the domain architecture and the elimination of non-ribonuclease EC classes (no phosphatase motifs, no catalytic triad, no redox centers), general biological reasoning meaningfully distinguishes B from A, C, and D without requiring lookup of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span entirely different EC classes (phosphatase, endoribonuclease, serine protease, oxidoreductase). The protein's domain architecture and sequence motifs clearly align with only one class (endoribonuclease), leaving no ambiguity among the options.


### Important caveats

- The UniProt EC annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental evidence. The EC assignment is a computational transfer from a homologous Dicer entry (B3DLA6).
- The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable (version 1 since 2022-05-25).
- The reviewer identified the accession from dataset image-path metadata; this accession was not provided to the evaluated model.
- While the DECH-box motif is identifiable, precise 4-digit EC assignment within the 3.1.26.x family could in principle require additional specificity knowledge; however, the choice set makes this moot since only one option is an endoribonuclease.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable DECH-box motif ('FDECH' visible in the helicase domain region), and the overall ~1881-aa architecture with helicase, PAZ-like, and RNase III-like domains is characteristic of Dicer proteins. Dicer is an endoribonuclease (EC class 3.1.26). Among the four choices, only B (3.1.26.3) belongs to the endoribonuclease class; A is a phosphatase, C is a serine protease (no catalytic triad present), and D is an oxidoreductase (no redox cofactor motifs). A model with general knowledge of Dicer domain architecture and EC classification can eliminate A, C, and D and select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The precise 4th digit (.3 for Dicer specifically vs. other 3.1.26.x enzymes) could in principle require memorization, but since B is the only endoribonuclease among the choices, identifying the protein as an endoribonuclease suffices.",
    "reason": "The DECH-box helicase motif is a concrete, identifiable sequence feature. Combined with the domain architecture and the elimination of non-ribonuclease EC classes (no phosphatase motifs, no catalytic triad, no redox centers), general biological reasoning meaningfully distinguishes B from A, C, and D without requiring lookup of this specific protein's database entry."
  },
  "case_id": "EC_number_0019",
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
    "reason": "The protein sequence matches UniProt entry A0A8J1LLF7 (DICRS_XENLA), annotated as Endoribonuclease Dicer-S from Xenopus laevis with EC 3.1.26.3. The sequence is 1881 aa, contains a DECH-box helicase motif, and exhibits the characteristic Dicer domain architecture (helicase, PAZ, RNase III). The annotation evidence code is ECO:0000250 (inferred by similarity from B3DLA6), meaning the EC assignment is a transfer annotation rather than direct experimental measurement, but it is consistent with the well-established identity and function of Dicer proteins as endoribonucleases producing 5'-phosphomonoesters."
  },
  "important_caveats": [
    "The UniProt EC annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental evidence. The EC assignment is a computational transfer from a homologous Dicer entry (B3DLA6).",
    "The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable (version 1 since 2022-05-25).",
    "The reviewer identified the accession from dataset image-path metadata; this accession was not provided to the evaluated model.",
    "While the DECH-box motif is identifiable, precise 4-digit EC assignment within the 3.1.26.x family could in principle require additional specificity knowledge; however, the choice set makes this moot since only one option is an endoribonuclease."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different EC classes (phosphatase, endoribonuclease, serine protease, oxidoreductase). The protein's domain architecture and sequence motifs clearly align with only one class (endoribonuclease), leaving no ambiguity among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt entry A0A8J1LLF7 (DICRS_XENLA), annotated as Endoribonuclease Dicer-S from Xenopus laevis with EC 3.1.26.3. The sequence is 1881 aa, contains a DECH-box helicase motif, and exhibits the characteristic Dicer domain architecture (helicase, PAZ, RNase III). The annotation evidence code is ECO:0000250 (inferred by similarity from B3DLA6), meaning the EC assignment is a transfer annotation rather than direct experimental measurement, but it is consistent with the well-established identity and function of Dicer proteins as endoribonucleases producing 5'-phosphomonoesters.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable DECH-box motif ('FDECH' visible in the helicase domain region), and the overall ~1881-aa architecture with helicase, PAZ-like, and RNase III-like domains is characteristic of Dicer proteins. Dicer is an endoribonuclease (EC class 3.1.26). Among the four choices, only B (3.1.26.3) belongs to the endoribonuclease class; A is a phosphatase, C is a serine protease (no catalytic triad present), and D is an oxidoreductase (no redox cofactor motifs). A model with general knowledge of Dicer domain architecture and EC classification can eliminate A, C, and D and select B.",
    "missing_item_specific_fact": "None critical. The precise 4th digit (.3 for Dicer specifically vs. other 3.1.26.x enzymes) could in principle require memorization, but since B is the only endoribonuclease among the choices, identifying the protein as an endoribonuclease suffices.",
    "reason": "The DECH-box helicase motif is a concrete, identifiable sequence feature. Combined with the domain architecture and the elimination of non-ribonuclease EC classes (no phosphatase motifs, no catalytic triad, no redox centers), general biological reasoning meaningfully distinguishes B from A, C, and D without requiring lookup of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different EC classes (phosphatase, endoribonuclease, serine protease, oxidoreductase). The protein's domain architecture and sequence motifs clearly align with only one class (endoribonuclease), leaving no ambiguity among the options."
  },
  "important_caveats": [
    "The UniProt EC annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental evidence. The EC assignment is a computational transfer from a homologous Dicer entry (B3DLA6).",
    "The UniProt entry was first publicly released on 2025-06-18; the author's source snapshot date is unknown, but the sequence has been stable (version 1 since 2022-05-25).",
    "The reviewer identified the accession from dataset image-path metadata; this accession was not provided to the evaluated model.",
    "While the DECH-box motif is identifiable, precise 4-digit EC assignment within the 3.1.26.x family could in principle require additional specificity knowledge; however, the choice set makes this moot since only one option is an endoribonuclease."
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

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8J1LLF7?format=txt&versions=19)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:05.098009+00:00.  

```text
ID   DICRS_XENLA             Reviewed;        1881 AA.
AC   A0A8J1LLF7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-MAY-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Endoribonuclease Dicer-S;
DE            EC=3.1.26.3;
GN   Name=dicer1.S; Synonyms=dicer1;
OS   Xenopus laevis (African clawed frog).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;
OC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Xenopus.
OX   NCBI_TaxID=8355;
```

Source SHA-256: `1ee78b98ec19d73b1d687d332eb3f9b6453d7a8816c912104ab16c4b4c2b5ead`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
