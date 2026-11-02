# pathway_0179

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSHSSHYSPVDSGMVPSSSSTEDHLSPTLSASIVLPAQLNPFAKAYDIPPSSIVQLGWALLLRCHLAIPSPCWSTIDDKTMPRGSDTHALQWESLHLEEGRSISWILQRWEDPSVHWYLSSDQLPGSKSPTLTTMLFLVKEYGLFDPVTPIDPGMGTIIYFYPSDEQPRLHISWNPDVVSSGHAFHLTRSLEHALQTIFLAPSVDIRDVNLFGIWDHQQLLQWNSYCPDPVDRLVQEMFQDVVAATPEASAVAAWDGELNYRELDRLSSRLAGVLQSDFGVVSETIVALCFEKSVWAIVAMLAVVKAGGAFLHIDPQHPPARHQAMIKSTASKLFLCSEQTRDTVVRSVPDCPSLVIHREMFAAQPDHAQQDTVISSGNLGPTNAAYVVCTSGSTGTPKAIVVEHVSLCSSVTAQAKAMDITAGSRVLQYAAYTFDVSIGDIFAALTHGACICIPSNWERAHDLSGAINRLGVNQACLTSTVASLLTPVEVPKLKKLTLGGEPATQQCINMWVDKVALKNIYGPAECTVWCIIQPDVSSGIAVSNIGHAIGARAWIVHPENHDRLMPIGAVGELLIEGPLVARGYLNDPVRTNAVFLAQPPIWLASFGPPPPRSRFYKTGDLARYGPGGALLFEGRKDTQVKLRGQRIELGEVEYRLHQALSDLSPSAAVELVHPKESTAPLLCAFITWDEGIDLDLQPAKPPLSACLTPNARKRFNHTVSLLQTEMERTLPAYMIPGLCIPVHKLPLTTSGKLDRKALRYFCTQHSLAFLSTFENNNVNSPTDGATDSFAAPLETVSPAESTLAQLWAQVLGRKTDSIGRKDNFLSLGGDSLAAMRLVNRAARDAQLTLTVADVFKCPVLADQASLVRPLVQTRNLVPFELMAPGDLQIEDLVAYVAEKCGVLHDQVEDIYPCTPLQDEMMRDSLSGDRTQMGQEVILLAEDLDIPRYLSACARVFQRFPILRTRFVQHSDRLIQVVIRENLGWQRPESLTEYVEADAKEAPALNKPLTRWALTSDSTHCILTMHHSIFDGISLGHILGAIYAVYQSIPLPPDSVSFAAFLAQINEHTSGLSDDSKQFWRSYLRPSPGSGDLPLPIVDSTYRPCANRGTQRLVTFQSGVVPALQQHGLTEATLIRGAWACTLAQLQTSSSTPSDVVFGTILTGRNLHLPGVDALVAPTLTHAPIRIRMSAASNEKPASFLARVQADATAMIPFEHDGMDRIRAIDAQVRAVCDQMQTLLVIQPIPEGLTSASTSPFPGPILSGPRVEAREMRHFHWYGLLVECTLLPTNGFFVRMCYDDKLFSSEDVERLLDDYSQALHELGGGLTEGEEVHLPTERKLDTLTLPGLVAPSGAEDMV

[Multiple Choices]
A. Cell wall degradation
B. ubiquinone biosynthesis. .
C. Antifungal biosynthesis. .
D. Pigment biosynthesis. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as nonribosomal peptide synthetase rstn8, with the pathway listed as antifungal biosynthesis. The pathway annotation cites PubMed 33857369 with ECO:0000269 evidence; this supports the key, though the cited study was not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which supports a role in natural-product biosynthesis. That alone does not establish that its product is antifungal rather than associated with another biosynthetic pathway.


**Missing item-specific fact**

> The protein-specific identification as Rstn8 and its association with restricticin/antifungal biosynthesis, which is supplied by the database annotation and cited study, not by the question.


**Reason**

> The sequence may suggest a biosynthetic enzyme, but distinguishing antifungal biosynthesis from other natural-product options requires item-specific pathway information. Recognizing the sequence through an external database would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not uniquely distinguish the listed pathways, but the reviewer evidence supports C and does not establish another listed choice as an equally defensible answer.


### Important caveats

- The UniProt record and historical record match the supplied sequence; the source snapshot used by the author is unknown.
- The cited evidence supports a curated pathway annotation, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which supports a role in natural-product biosynthesis. That alone does not establish that its product is antifungal rather than associated with another biosynthetic pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Rstn8 and its association with restricticin/antifungal biosynthesis, which is supplied by the database annotation and cited study, not by the question.",
    "reason": "The sequence may suggest a biosynthetic enzyme, but distinguishing antifungal biosynthesis from other natural-product options requires item-specific pathway information. Recognizing the sequence through an external database would be lookup, not reasoning from the supplied input."
  },
  "case_id": "pathway_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as nonribosomal peptide synthetase rstn8, with the pathway listed as antifungal biosynthesis. The pathway annotation cites PubMed 33857369 with ECO:0000269 evidence; this supports the key, though the cited study was not independently assessed here."
  },
  "important_caveats": [
    "The UniProt record and historical record match the supplied sequence; the source snapshot used by the author is unknown.",
    "The cited evidence supports a curated pathway annotation, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not uniquely distinguish the listed pathways, but the reviewer evidence supports C and does not establish another listed choice as an equally defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as nonribosomal peptide synthetase rstn8, with the pathway listed as antifungal biosynthesis. The pathway annotation cites PubMed 33857369 with ECO:0000269 evidence; this supports the key, though the cited study was not independently assessed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is consistent with a multidomain nonribosomal peptide synthetase, which supports a role in natural-product biosynthesis. That alone does not establish that its product is antifungal rather than associated with another biosynthetic pathway.",
    "missing_item_specific_fact": "The protein-specific identification as Rstn8 and its association with restricticin/antifungal biosynthesis, which is supplied by the database annotation and cited study, not by the question.",
    "reason": "The sequence may suggest a biosynthetic enzyme, but distinguishing antifungal biosynthesis from other natural-product options requires item-specific pathway information. Recognizing the sequence through an external database would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not uniquely distinguish the listed pathways, but the reviewer evidence supports C and does not establish another listed choice as an equally defensible answer."
  },
  "important_caveats": [
    "The UniProt record and historical record match the supplied sequence; the source snapshot used by the author is unknown.",
    "The cited evidence supports a curated pathway annotation, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0L1JF11 explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:33857369. The protein is a nonribosomal peptide synthetase (rstn8) in the restricticin biosynthesis gene cluster of Aspergillus nomiae, and restricticin is a natural product CYP51 inhibitor with antifungal activity. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reasonably infer from the long multi-modular architecture (~1358 aa) with recognizable adenylation and condensation domain motifs that this is a nonribosomal peptide synthetase (NRPS), which effectively eliminates option A (cell wall degradation, typically glycosyl hydrolases) and option B (ubiquinone biosynthesis, typically prenyltransferases and oxidoreductases). However, NRPS enzymes produce both antifungal compounds and pigments, so the sequence alone does not distinguish option C from option D.


**Missing item-specific fact**

> Knowing that this specific NRPS (rstn8) produces restricticin, a CYP51 inhibitor with antifungal activity, rather than a pigment compound, requires knowledge of the specific biosynthetic gene cluster context and the biological activity of the final product—information not derivable from the amino acid sequence alone.


**Reason**

> While NRPS identification eliminates A and B through general domain-architecture reasoning, the distinction between 'antifungal biosynthesis' (C) and 'pigment biosynthesis' (D) depends on knowing the specific compound produced and its biological activity, which is an item-specific fact absent from the sequence input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both antifungal biosynthesis and pigment biosynthesis are common NRPS-derived pathways in fungi. Without the gene cluster context or knowledge of the specific product (restricticin), a model identifying the protein as an NRPS could plausibly select either C or D. The UniProt annotation resolves this to C, but the sequence alone does not.


### Important caveats

- The UniProt pathway annotation carries experimental evidence (ECO:0000269) from a 2021 JACS paper characterizing the restricticin BGC, so the key is well-supported by primary literature.
- The protein was first publicly annotated in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may have come from a different source or been inferred computationally.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence reasoning and general biological knowledge.
- The 'Antifungal biosynthesis' pathway label is a UniProt-specific categorization; in broader biochemical taxonomy this might fall under 'secondary metabolite biosynthesis' or 'natural product biosynthesis.'

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reasonably infer from the long multi-modular architecture (~1358 aa) with recognizable adenylation and condensation domain motifs that this is a nonribosomal peptide synthetase (NRPS), which effectively eliminates option A (cell wall degradation, typically glycosyl hydrolases) and option B (ubiquinone biosynthesis, typically prenyltransferases and oxidoreductases). However, NRPS enzymes produce both antifungal compounds and pigments, so the sequence alone does not distinguish option C from option D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowing that this specific NRPS (rstn8) produces restricticin, a CYP51 inhibitor with antifungal activity, rather than a pigment compound, requires knowledge of the specific biosynthetic gene cluster context and the biological activity of the final product—information not derivable from the amino acid sequence alone.",
    "reason": "While NRPS identification eliminates A and B through general domain-architecture reasoning, the distinction between 'antifungal biosynthesis' (C) and 'pigment biosynthesis' (D) depends on knowing the specific compound produced and its biological activity, which is an item-specific fact absent from the sequence input."
  },
  "case_id": "pathway_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0L1JF11 explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:33857369. The protein is a nonribosomal peptide synthetase (rstn8) in the restricticin biosynthesis gene cluster of Aspergillus nomiae, and restricticin is a natural product CYP51 inhibitor with antifungal activity. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from a 2021 JACS paper characterizing the restricticin BGC, so the key is well-supported by primary literature.",
    "The protein was first publicly annotated in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may have come from a different source or been inferred computationally.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence reasoning and general biological knowledge.",
    "The 'Antifungal biosynthesis' pathway label is a UniProt-specific categorization; in broader biochemical taxonomy this might fall under 'secondary metabolite biosynthesis' or 'natural product biosynthesis.'"
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both antifungal biosynthesis and pigment biosynthesis are common NRPS-derived pathways in fungi. Without the gene cluster context or knowledge of the specific product (restricticin), a model identifying the protein as an NRPS could plausibly select either C or D. The UniProt annotation resolves this to C, but the sequence alone does not."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0L1JF11 explicitly annotates the pathway as 'Antifungal biosynthesis' with evidence code ECO:0000269 (experimental evidence) from PubMed:33857369. The protein is a nonribosomal peptide synthetase (rstn8) in the restricticin biosynthesis gene cluster of Aspergillus nomiae, and restricticin is a natural product CYP51 inhibitor with antifungal activity. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reasonably infer from the long multi-modular architecture (~1358 aa) with recognizable adenylation and condensation domain motifs that this is a nonribosomal peptide synthetase (NRPS), which effectively eliminates option A (cell wall degradation, typically glycosyl hydrolases) and option B (ubiquinone biosynthesis, typically prenyltransferases and oxidoreductases). However, NRPS enzymes produce both antifungal compounds and pigments, so the sequence alone does not distinguish option C from option D.",
    "missing_item_specific_fact": "Knowing that this specific NRPS (rstn8) produces restricticin, a CYP51 inhibitor with antifungal activity, rather than a pigment compound, requires knowledge of the specific biosynthetic gene cluster context and the biological activity of the final product—information not derivable from the amino acid sequence alone.",
    "reason": "While NRPS identification eliminates A and B through general domain-architecture reasoning, the distinction between 'antifungal biosynthesis' (C) and 'pigment biosynthesis' (D) depends on knowing the specific compound produced and its biological activity, which is an item-specific fact absent from the sequence input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both antifungal biosynthesis and pigment biosynthesis are common NRPS-derived pathways in fungi. Without the gene cluster context or knowledge of the specific product (restricticin), a model identifying the protein as an NRPS could plausibly select either C or D. The UniProt annotation resolves this to C, but the sequence alone does not."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from a 2021 JACS paper characterizing the restricticin BGC, so the key is well-supported by primary literature.",
    "The protein was first publicly annotated in UniProt on 2025-02-05; if the benchmark was constructed before that date, the annotation may have come from a different source or been inferred computationally.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence reasoning and general biological knowledge.",
    "The 'Antifungal biosynthesis' pathway label is a UniProt-specific categorization; in broader biochemical taxonomy this might fall under 'secondary metabolite biosynthesis' or 'natural product biosynthesis.'"
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

**Accession:** `A0A0L1JF11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 8"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase rstn8"}}}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY"]}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
RN   [2]
RP   FUNCTION, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
