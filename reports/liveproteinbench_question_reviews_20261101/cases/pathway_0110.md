# pathway_0110

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. Capsule biogenesis
B. Lipid metabolism. .
C. Alkaloid biosynthesis. .
D. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
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

> The sequence matches the UniProt entry annotated as Rhazimal reductase 1, with an alkaloid-biosynthesis pathway annotation linked to a publication reporting function and catalytic activity. This supports choice C for this protein, while the annotation and cited experimental evidence are reviewer-only, not information supplied in the question.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad inference of an oxidoreductase, but that does not establish which pathway it serves. The choices require knowing this particular enzyme's biological function.


**Missing item-specific fact**

> The protein-specific identification and functional/pathway annotation as rhazimal reductase 1 in alkaloid biosynthesis.


**Reason**

> No organism, enzyme name, reaction, or pathway context is supplied. General sequence-based reasoning does not meaningfully distinguish alkaloid biosynthesis from the other proposed pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports C for the matched sequence; the input itself does not provide enough context to establish another choice.


### Important caveats

- The matched UniProt entry and its pathway annotation are reviewer-only evidence and cannot be treated as supplied to the evaluated model.
- The entry links its pathway annotation to a publication with function and catalytic-activity evidence, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad inference of an oxidoreductase, but that does not establish which pathway it serves. The choices require knowing this particular enzyme's biological function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional/pathway annotation as rhazimal reductase 1 in alkaloid biosynthesis.",
    "reason": "No organism, enzyme name, reaction, or pathway context is supplied. General sequence-based reasoning does not meaningfully distinguish alkaloid biosynthesis from the other proposed pathways."
  },
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as Rhazimal reductase 1, with an alkaloid-biosynthesis pathway annotation linked to a publication reporting function and catalytic activity. This supports choice C for this protein, while the annotation and cited experimental evidence are reviewer-only, not information supplied in the question."
  },
  "important_caveats": [
    "The matched UniProt entry and its pathway annotation are reviewer-only evidence and cannot be treated as supplied to the evaluated model.",
    "The entry links its pathway annotation to a publication with function and catalytic-activity evidence, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C for the matched sequence; the input itself does not provide enough context to establish another choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated as Rhazimal reductase 1, with an alkaloid-biosynthesis pathway annotation linked to a publication reporting function and catalytic activity. This supports choice C for this protein, while the annotation and cited experimental evidence are reviewer-only, not information supplied in the question.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad inference of an oxidoreductase, but that does not establish which pathway it serves. The choices require knowing this particular enzyme's biological function.",
    "missing_item_specific_fact": "The protein-specific identification and functional/pathway annotation as rhazimal reductase 1 in alkaloid biosynthesis.",
    "reason": "No organism, enzyme name, reaction, or pathway context is supplied. General sequence-based reasoning does not meaningfully distinguish alkaloid biosynthesis from the other proposed pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C for the matched sequence; the input itself does not provide enough context to establish another choice."
  },
  "important_caveats": [
    "The matched UniProt entry and its pathway annotation are reviewer-only evidence and cannot be treated as supplied to the evaluated model.",
    "The entry links its pathway annotation to a publication with function and catalytic-activity evidence, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S518 (Rhazimal reductase 1, AsRHR1, EC 1.1.1.440 from Alstonia scholaris) carries the explicit pathway annotation 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022, on indole alkaloid biosynthesis). The sequence matches exactly (SHA-256 confirmed). The annotation is backed by experimental characterization of catalytic activity and pathway role.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 323-aa sequence contains a possible Rossmann-fold nucleotide-binding motif (e.g., 'VGFGT' near the N-terminus), consistent with a short-chain dehydrogenase/reductase (SDR) or related NAD(P)-dependent oxidoreductase. However, SDR/oxidoreductase motifs are ubiquitous across lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis pathways. Without organism context (Alstonia scholaris, a plant in the Apocynaceae family renowned for monoterpenoid indole alkaloid production) or knowledge that this is Rhazimal reductase 1, the sequence provides no alkaloid-specific catalytic motif that would unambiguously distinguish choice C from choice B (Lipid metabolism).


**Missing item-specific fact**

> The organism identity (Alstonia scholaris, Apocynaceae) and the specific protein identity (Rhazimal reductase 1, EC 1.1.1.440, acting in the indole alkaloid biosynthetic pathway) are absent from the model input. Recognizing the protein or knowing the organism's dominant secondary-metabolism pathway is required to select C over B.


**Reason**

> The question supplies only a raw amino acid sequence and four pathway labels. The sequence is consistent with a generic NAD(P)-dependent oxidoreductase, a superfamily found in lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis alike. No alkaloid-specific active-site motif, substrate-binding signature, or pathway-specific domain is identifiable from the sequence alone. Selecting 'Alkaloid biosynthesis' over 'Lipid metabolism' requires knowing the protein's identity or the organism's metabolic context, which is a lookup/memorization task rather than a reasoning task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Without organism or protein-identity context, an NAD(P)-dependent oxidoreductase of ~323 aa could plausibly be assigned to lipid metabolism (B), as many plant fatty-acid or terpenoid oxidoreductases belong to the same structural superfamily. Choice C is correct per the database annotation, but the sequence alone does not provide a decisive argument to exclude B. Choices A (capsule biogenesis, a bacterial pathway) and D (a very specific histidine-biosynthesis step) are clearly less plausible.


### Important caveats

- The pathway annotation 'Alkaloid biosynthesis' is backed by experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's correctness.
- The organism (Alstonia scholaris) and protein name (Rhazimal reductase 1) are absent from the evaluated model input; they appear only in reviewer-only evidence.
- The entry was first publicly released 2025-06-18; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2023-05-03.
- The trailing periods in choices B, C, and D appear to be formatting artifacts and do not affect meaning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 323-aa sequence contains a possible Rossmann-fold nucleotide-binding motif (e.g., 'VGFGT' near the N-terminus), consistent with a short-chain dehydrogenase/reductase (SDR) or related NAD(P)-dependent oxidoreductase. However, SDR/oxidoreductase motifs are ubiquitous across lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis pathways. Without organism context (Alstonia scholaris, a plant in the Apocynaceae family renowned for monoterpenoid indole alkaloid production) or knowledge that this is Rhazimal reductase 1, the sequence provides no alkaloid-specific catalytic motif that would unambiguously distinguish choice C from choice B (Lipid metabolism).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The organism identity (Alstonia scholaris, Apocynaceae) and the specific protein identity (Rhazimal reductase 1, EC 1.1.1.440, acting in the indole alkaloid biosynthetic pathway) are absent from the model input. Recognizing the protein or knowing the organism's dominant secondary-metabolism pathway is required to select C over B.",
    "reason": "The question supplies only a raw amino acid sequence and four pathway labels. The sequence is consistent with a generic NAD(P)-dependent oxidoreductase, a superfamily found in lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis alike. No alkaloid-specific active-site motif, substrate-binding signature, or pathway-specific domain is identifiable from the sequence alone. Selecting 'Alkaloid biosynthesis' over 'Lipid metabolism' requires knowing the protein's identity or the organism's metabolic context, which is a lookup/memorization task rather than a reasoning task."
  },
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, AsRHR1, EC 1.1.1.440 from Alstonia scholaris) carries the explicit pathway annotation 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022, on indole alkaloid biosynthesis). The sequence matches exactly (SHA-256 confirmed). The annotation is backed by experimental characterization of catalytic activity and pathway role."
  },
  "important_caveats": [
    "The pathway annotation 'Alkaloid biosynthesis' is backed by experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's correctness.",
    "The organism (Alstonia scholaris) and protein name (Rhazimal reductase 1) are absent from the evaluated model input; they appear only in reviewer-only evidence.",
    "The entry was first publicly released 2025-06-18; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2023-05-03.",
    "The trailing periods in choices B, C, and D appear to be formatting artifacts and do not affect meaning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Without organism or protein-identity context, an NAD(P)-dependent oxidoreductase of ~323 aa could plausibly be assigned to lipid metabolism (B), as many plant fatty-acid or terpenoid oxidoreductases belong to the same structural superfamily. Choice C is correct per the database annotation, but the sequence alone does not provide a decisive argument to exclude B. Choices A (capsule biogenesis, a bacterial pathway) and D (a very specific histidine-biosynthesis step) are clearly less plausible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, AsRHR1, EC 1.1.1.440 from Alstonia scholaris) carries the explicit pathway annotation 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 from PubMed:36349266 (Wang et al., Chem. Sci. 2022, on indole alkaloid biosynthesis). The sequence matches exactly (SHA-256 confirmed). The annotation is backed by experimental characterization of catalytic activity and pathway role.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 323-aa sequence contains a possible Rossmann-fold nucleotide-binding motif (e.g., 'VGFGT' near the N-terminus), consistent with a short-chain dehydrogenase/reductase (SDR) or related NAD(P)-dependent oxidoreductase. However, SDR/oxidoreductase motifs are ubiquitous across lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis pathways. Without organism context (Alstonia scholaris, a plant in the Apocynaceae family renowned for monoterpenoid indole alkaloid production) or knowledge that this is Rhazimal reductase 1, the sequence provides no alkaloid-specific catalytic motif that would unambiguously distinguish choice C from choice B (Lipid metabolism).",
    "missing_item_specific_fact": "The organism identity (Alstonia scholaris, Apocynaceae) and the specific protein identity (Rhazimal reductase 1, EC 1.1.1.440, acting in the indole alkaloid biosynthetic pathway) are absent from the model input. Recognizing the protein or knowing the organism's dominant secondary-metabolism pathway is required to select C over B.",
    "reason": "The question supplies only a raw amino acid sequence and four pathway labels. The sequence is consistent with a generic NAD(P)-dependent oxidoreductase, a superfamily found in lipid metabolism, amino acid biosynthesis, and alkaloid biosynthesis alike. No alkaloid-specific active-site motif, substrate-binding signature, or pathway-specific domain is identifiable from the sequence alone. Selecting 'Alkaloid biosynthesis' over 'Lipid metabolism' requires knowing the protein's identity or the organism's metabolic context, which is a lookup/memorization task rather than a reasoning task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Without organism or protein-identity context, an NAD(P)-dependent oxidoreductase of ~323 aa could plausibly be assigned to lipid metabolism (B), as many plant fatty-acid or terpenoid oxidoreductases belong to the same structural superfamily. Choice C is correct per the database annotation, but the sequence alone does not provide a decisive argument to exclude B. Choices A (capsule biogenesis, a bacterial pathway) and D (a very specific histidine-biosynthesis step) are clearly less plausible."
  },
  "important_caveats": [
    "The pathway annotation 'Alkaloid biosynthesis' is backed by experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's correctness.",
    "The organism (Alstonia scholaris) and protein name (Rhazimal reductase 1) are absent from the evaluated model input; they appear only in reviewer-only evidence.",
    "The entry was first publicly released 2025-06-18; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2023-05-03.",
    "The trailing periods in choices B, C, and D appear to be formatting artifacts and do not affect meaning."
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

**Accession:** `A0A9E7S518` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
"A0A9E7S518"
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"commonName":"Dogbane","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Alstonieae","Alstonia"],"scientificName":"Alstonia scholaris","synonyms":["Echites scholaris"],"taxonId":52822}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.1.1.440"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Rhazimal reductase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsRHR1"}]}}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65385.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
ID   RHR1_ALSSC              Reviewed;         323 AA.
AC   A0A9E7S518;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};
DE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};
GN   Name=RHR1 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 16-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65385.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 43-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
