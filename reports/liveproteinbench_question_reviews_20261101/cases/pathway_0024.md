# pathway_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. L-fucose degradation. .
B. glycosylphosphatidylinositol-anchor biosynthesis. .
C. Alkaloid biosynthesis
D. terpenoid biosynthesis.
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

> The supplied sequence exactly matches the reviewed UniProt sequence for vomilenine reductase, which is annotated to alkaloid and ajmaline biosynthesis. The annotation cites experimental-evidence codes and relevant publications; this supports choice C for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but the input supplies no organism, substrate, reaction, or other context that identifies its specific pathway among these choices.


**Missing item-specific fact**

> The protein-specific identification as vomilenine reductase and its role in ajmaline alkaloid biosynthesis.


**Reason**

> The reviewer evidence supports the key, but it was not supplied to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be needed to distinguish the pathway; generic sequence-based enzyme inference does not establish this particular pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports alkaloid biosynthesis for the matched sequence; no competing listed pathway is supported by the supplied evidence.


### Important caveats

- The pathway annotation is reviewer-only information, not information available in the original question.
- The source reports experimental evidence for the annotation, but the primary studies were not independently reviewed here.
- The author's exact source snapshot is unknown; the matching historical and current sequence records support applicability to the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input supplies no organism, substrate, reaction, or other context that identifies its specific pathway among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as vomilenine reductase and its role in ajmaline alkaloid biosynthesis.",
    "reason": "The reviewer evidence supports the key, but it was not supplied to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be needed to distinguish the pathway; generic sequence-based enzyme inference does not establish this particular pathway."
  },
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for vomilenine reductase, which is annotated to alkaloid and ajmaline biosynthesis. The annotation cites experimental-evidence codes and relevant publications; this supports choice C for this sequence."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only information, not information available in the original question.",
    "The source reports experimental evidence for the annotation, but the primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the matching historical and current sequence records support applicability to the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports alkaloid biosynthesis for the matched sequence; no competing listed pathway is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for vomilenine reductase, which is annotated to alkaloid and ajmaline biosynthesis. The annotation cites experimental-evidence codes and relevant publications; this supports choice C for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but the input supplies no organism, substrate, reaction, or other context that identifies its specific pathway among these choices.",
    "missing_item_specific_fact": "The protein-specific identification as vomilenine reductase and its role in ajmaline alkaloid biosynthesis.",
    "reason": "The reviewer evidence supports the key, but it was not supplied to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be needed to distinguish the pathway; generic sequence-based enzyme inference does not establish this particular pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports alkaloid biosynthesis for the matched sequence; no competing listed pathway is supported by the supplied evidence."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only information, not information available in the original question.",
    "The source reports experimental evidence for the annotation, but the primary studies were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the matching historical and current sequence records support applicability to the sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ3 (sequence matched exactly, 360 aa) annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with the PATHWAY comment explicitly stating 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. The author key 'C. Alkaloid biosynthesis' aligns directly with this annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold NAD(P)-binding motif (GDLVGCLVGSCRKCDMCSQ) indicating an NAD(P)-dependent oxidoreductase, which weakly disfavors options A (glycosidase-based) and B (phosphatase/transferase-based). The EC 1.5.1.x class (acting on CH-NH group) is more commonly associated with imine reduction in alkaloid pathways than with terpenoid biosynthesis (which predominantly uses P450s, terpene synthases, and CH-OH reductases). However, this is a weak and indirect argument.


**Missing item-specific fact**

> The specific substrate identity (vomilenine, an indole alkaloid intermediate) or the organism context (Rauvolfia serpentina, a genus renowned for monoterpene indole alkaloid production) is required to confidently distinguish alkaloid biosynthesis (C) from terpenoid biosynthesis (D). Neither is derivable from the bare 360-aa sequence. Additionally, the 'CAD2-homolog' annotation (which could mislead toward phenylpropanoid/lignin pathways) is a database-derived fact.


**Reason**

> While the Rossmann fold narrows the enzyme class to oxidoreductases, both alkaloid and terpenoid biosynthesis employ NAD(P)-dependent reductases. The sequence lacks distinctive terpene-synthase motifs (DDxxD, NSE/DTE) and lacks glycosidase/GPI-anchor features, but these negative observations are insufficient to definitively select C over D. Reliable identification requires knowing the specific protein (vomilenine reductase) or the producing organism, which are item-specific database facts absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> An NAD(P)-dependent oxidoreductase with a Rossmann fold could plausibly participate in either alkaloid or terpenoid biosynthesis based on sequence alone. Without the organism name or substrate identity, a knowledgeable model might argue for D (terpenoid biosynthesis also uses reductases, e.g., in carotenoid or gibberellin pathways). The distinction ultimately rests on the specific substrate (vomilenine) which is not encoded in the sequence.


### Important caveats

- The UniProt entry P0DXJ3 was first publicly released 2025-06-18; if the benchmark was constructed before that date, the annotation would not have been available in Swiss-Prot, though the underlying publications (2002, 2024) existed.
- The sequence is annotated as a CAD2-homolog (cinnamyl alcohol dehydrogenase homolog), which could mislead a model toward phenylpropanoid/lignin pathways not listed among the choices.
- The pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' is supported by experimental evidence (ECO:0000269), not merely computational inference.
- The organism Rauvolfia serpentina is not stated in the question; its well-known association with indole alkaloid production would be a strong contextual clue if provided.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif (GDLVGCLVGSCRKCDMCSQ) indicating an NAD(P)-dependent oxidoreductase, which weakly disfavors options A (glycosidase-based) and B (phosphatase/transferase-based). The EC 1.5.1.x class (acting on CH-NH group) is more commonly associated with imine reduction in alkaloid pathways than with terpenoid biosynthesis (which predominantly uses P450s, terpene synthases, and CH-OH reductases). However, this is a weak and indirect argument.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (vomilenine, an indole alkaloid intermediate) or the organism context (Rauvolfia serpentina, a genus renowned for monoterpene indole alkaloid production) is required to confidently distinguish alkaloid biosynthesis (C) from terpenoid biosynthesis (D). Neither is derivable from the bare 360-aa sequence. Additionally, the 'CAD2-homolog' annotation (which could mislead toward phenylpropanoid/lignin pathways) is a database-derived fact.",
    "reason": "While the Rossmann fold narrows the enzyme class to oxidoreductases, both alkaloid and terpenoid biosynthesis employ NAD(P)-dependent reductases. The sequence lacks distinctive terpene-synthase motifs (DDxxD, NSE/DTE) and lacks glycosidase/GPI-anchor features, but these negative observations are insufficient to definitively select C over D. Reliable identification requires knowing the specific protein (vomilenine reductase) or the producing organism, which are item-specific database facts absent from the model input."
  },
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (sequence matched exactly, 360 aa) annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with the PATHWAY comment explicitly stating 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. The author key 'C. Alkaloid biosynthesis' aligns directly with this annotation."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ3 was first publicly released 2025-06-18; if the benchmark was constructed before that date, the annotation would not have been available in Swiss-Prot, though the underlying publications (2002, 2024) existed.",
    "The sequence is annotated as a CAD2-homolog (cinnamyl alcohol dehydrogenase homolog), which could mislead a model toward phenylpropanoid/lignin pathways not listed among the choices.",
    "The pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' is supported by experimental evidence (ECO:0000269), not merely computational inference.",
    "The organism Rauvolfia serpentina is not stated in the question; its well-known association with indole alkaloid production would be a strong contextual clue if provided."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "An NAD(P)-dependent oxidoreductase with a Rossmann fold could plausibly participate in either alkaloid or terpenoid biosynthesis based on sequence alone. Without the organism name or substrate identity, a knowledgeable model might argue for D (terpenoid biosynthesis also uses reductases, e.g., in carotenoid or gibberellin pathways). The distinction ultimately rests on the specific substrate (vomilenine) which is not encoded in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ3 (sequence matched exactly, 360 aa) annotates this protein as Vomilenine reductase (EC 1.5.1.32) from Rauvolfia serpentina, with the PATHWAY comment explicitly stating 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence codes ECO:0000269 from PubMed:11937349 and PubMed:38212296. The author key 'C. Alkaloid biosynthesis' aligns directly with this annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif (GDLVGCLVGSCRKCDMCSQ) indicating an NAD(P)-dependent oxidoreductase, which weakly disfavors options A (glycosidase-based) and B (phosphatase/transferase-based). The EC 1.5.1.x class (acting on CH-NH group) is more commonly associated with imine reduction in alkaloid pathways than with terpenoid biosynthesis (which predominantly uses P450s, terpene synthases, and CH-OH reductases). However, this is a weak and indirect argument.",
    "missing_item_specific_fact": "The specific substrate identity (vomilenine, an indole alkaloid intermediate) or the organism context (Rauvolfia serpentina, a genus renowned for monoterpene indole alkaloid production) is required to confidently distinguish alkaloid biosynthesis (C) from terpenoid biosynthesis (D). Neither is derivable from the bare 360-aa sequence. Additionally, the 'CAD2-homolog' annotation (which could mislead toward phenylpropanoid/lignin pathways) is a database-derived fact.",
    "reason": "While the Rossmann fold narrows the enzyme class to oxidoreductases, both alkaloid and terpenoid biosynthesis employ NAD(P)-dependent reductases. The sequence lacks distinctive terpene-synthase motifs (DDxxD, NSE/DTE) and lacks glycosidase/GPI-anchor features, but these negative observations are insufficient to definitively select C over D. Reliable identification requires knowing the specific protein (vomilenine reductase) or the producing organism, which are item-specific database facts absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "An NAD(P)-dependent oxidoreductase with a Rossmann fold could plausibly participate in either alkaloid or terpenoid biosynthesis based on sequence alone. Without the organism name or substrate identity, a knowledgeable model might argue for D (terpenoid biosynthesis also uses reductases, e.g., in carotenoid or gibberellin pathways). The distinction ultimately rests on the specific substrate (vomilenine) which is not encoded in the sequence."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ3 was first publicly released 2025-06-18; if the benchmark was constructed before that date, the annotation would not have been available in Swiss-Prot, though the underlying publications (2002, 2024) existed.",
    "The sequence is annotated as a CAD2-homolog (cinnamyl alcohol dehydrogenase homolog), which could mislead a model toward phenylpropanoid/lignin pathways not listed among the choices.",
    "The pathway annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' is supported by experimental evidence (ECO:0000269), not merely computational inference.",
    "The organism Rauvolfia serpentina is not stated in the question; its well-known association with indole alkaloid production would be a strong contextual clue if provided."
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

**Accession:** `P0DXJ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
"P0DXJ3"
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"commonName":"Serpentine wood","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Vinceae","Rauvolfiinae","Rauvolfia"],"scientificName":"Rauvolfia serpentina","synonyms":["Ophioxylon serpentinum"],"taxonId":4060}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"CAD2-homolog protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Protein RR6-2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsRR6-2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.32"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"Vomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"38212296","source":"PubMed"}],"value":"RsVR"}]}}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11937349","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WKU61927.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:30.487363+00:00.  

```json
{"citation":{"authors":["von Schumann G.","Gao S.","Stoeckigt J."],"citationCrossReferences":[{"database":"PubMed","id":"11937349"},{"database":"DOI","id":"10.1016/s0968-0896(01)00435-7"}],"citationType":"journal article","firstPage":"1913","id":"11937349","journal":"Bioorg. Med. Chem.","lastPage":"1918","publicationDate":"2002","title":"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","ACTIVITY REGULATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
ID   VOR1_RAUSE              Reviewed;         360 AA.
AC   P0DXJ3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};
DE            Short=RsVR {ECO:0000305|PubMed:38212296};
DE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};
DE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};
DE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};
DE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};
GN   Name=VR {ECO:0000305|PubMed:38212296};
GN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 20-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WKU61927.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND
RP   BIOTECHNOLOGY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY,
RP   ACTIVITY REGULATION, AND TISSUE SPECIFICITY.
RX   PubMed=11937349; DOI=10.1016/s0968-0896(01)00435-7;
RA   von Schumann G., Gao S., Stoeckigt J.;
RT   "Vomilenine reductase--a novel enzyme catalyzing a crucial step in the
RT   biosynthesis of the therapeutically applied antiarrhythmic alkaloid
RT   ajmaline.";
RL   Bioorg. Med. Chem. 10:1913-1918(2002).
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)  
**Locator:** `lines 74-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:34.682731+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
