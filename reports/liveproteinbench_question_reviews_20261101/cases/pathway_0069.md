# pathway_0069

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
B. spheroidene biosynthesis. .
C. Capsule biogenesis
D. Amino-acid degradation
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

> The exact sequence matches the Campylobacter jejuni strain 81116 protein annotated as N-acylneuraminate cytidylyltransferase. Its pathway annotation assigns it to capsule biogenesis and cites experimental literature, supporting choice C. The excerpts report the annotation and its evidence citation; they do not independently present the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support predictions about protein family or enzymatic function, but the input gives no organism, pathway context, or other clear evidence that identifies which candidate pathway this specific protein serves.


**Missing item-specific fact**

> The protein's identity and role as an N-acylneuraminate cytidylyltransferase in capsule-polysaccharide precursor biosynthesis.


**Reason**

> Distinguishing capsule biogenesis from the listed alternatives requires a protein-specific functional or pathway annotation not supplied in the question. Recognizing the sequence or relying on an unspecified predictor would not make the distinction reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports C for the matched protein. The sequence-only prompt does not provide enough context to distinguish the choices, but that lack of information does not establish another option as correct.


### Important caveats

- The archived and current UniProt records match the supplied sequence and identify the same strain-specific protein.
- The pathway annotation cites a 2024 publication with an experimental evidence code; the primary paper was not independently reviewed here.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support predictions about protein family or enzymatic function, but the input gives no organism, pathway context, or other clear evidence that identifies which candidate pathway this specific protein serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and role as an N-acylneuraminate cytidylyltransferase in capsule-polysaccharide precursor biosynthesis.",
    "reason": "Distinguishing capsule biogenesis from the listed alternatives requires a protein-specific functional or pathway annotation not supplied in the question. Recognizing the sequence or relying on an unspecified predictor would not make the distinction reasoning-supported."
  },
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Campylobacter jejuni strain 81116 protein annotated as N-acylneuraminate cytidylyltransferase. Its pathway annotation assigns it to capsule biogenesis and cites experimental literature, supporting choice C. The excerpts report the annotation and its evidence citation; they do not independently present the underlying experiments."
  },
  "important_caveats": [
    "The archived and current UniProt records match the supplied sequence and identify the same strain-specific protein.",
    "The pathway annotation cites a 2024 publication with an experimental evidence code; the primary paper was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched protein. The sequence-only prompt does not provide enough context to distinguish the choices, but that lack of information does not establish another option as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Campylobacter jejuni strain 81116 protein annotated as N-acylneuraminate cytidylyltransferase. Its pathway annotation assigns it to capsule biogenesis and cites experimental literature, supporting choice C. The excerpts report the annotation and its evidence citation; they do not independently present the underlying experiments.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support predictions about protein family or enzymatic function, but the input gives no organism, pathway context, or other clear evidence that identifies which candidate pathway this specific protein serves.",
    "missing_item_specific_fact": "The protein's identity and role as an N-acylneuraminate cytidylyltransferase in capsule-polysaccharide precursor biosynthesis.",
    "reason": "Distinguishing capsule biogenesis from the listed alternatives requires a protein-specific functional or pathway annotation not supplied in the question. Recognizing the sequence or relying on an unspecified predictor would not make the distinction reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched protein. The sequence-only prompt does not provide enough context to distinguish the choices, but that lack of information does not establish another option as correct."
  },
  "important_caveats": [
    "The archived and current UniProt records match the supplied sequence and identify the same strain-specific protein.",
    "The pathway annotation cites a 2024 publication with an experimental evidence code; the primary paper was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DY07 (NEUAC_CAMJ8), N-acylneuraminate cytidylyltransferase (EC 2.7.7.43, CMP-Neu5Ac synthase) from Campylobacter jejuni. The UniProt pathway annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). Sequence SHA256 match confirmed across current and historical records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable P-loop/NTP-binding motif (GAGAGKTT ~residues 180-188) suggesting a nucleotidyltransferase, which is consistent with a cytidylyltransferase. However, the nucleotidyltransferase superfamily is enormous and spans dozens of pathways. Identifying this specific enzyme as CMP-N-acetylneuraminate synthase, and then recognizing that in Campylobacter jejuni sialic acid metabolism feeds into capsule polysaccharide biosynthesis (rather than, say, glycolipid or glycoprotein modification pathways), requires item-specific knowledge of this enzyme's substrate specificity and its organism-specific metabolic role.


**Missing item-specific fact**

> The specific identity of this protein as CMP-Neu5Ac synthase (a sialic acid-activating cytidylyltransferase) and the fact that in Campylobacter jejuni, sialic acid (Neu5Ac) is incorporated into the capsular polysaccharide rather than serving other metabolic roles. Neither the substrate specificity nor the organism context is derivable from the bare sequence without database lookup or memorization.


**Reason**

> While the P-loop motif hints at a nucleotidyltransferase, this is far too broad to distinguish capsule biogenesis from amino-acid degradation or other pathways. The critical step—identifying the substrate as N-acetylneuraminate and linking sialic acid metabolism to capsule biosynthesis in Campylobacter—is an item-specific annotation fact not inferable from general biological reasoning on the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct. Option D (amino-acid degradation) is a weak distractor since sialic acid is an amino sugar, but sialic acid metabolism is not amino-acid degradation. Options A and B are clearly unrelated pathways. Given the correct annotation, C is the only defensible answer.


### Important caveats

- The UniProt entry P0DY07 was first publicly released on 2025-06-18, with the key experimental paper (PubMed:38382015) published in 2024. The author's source snapshot date is unknown; if the benchmark was constructed before June 2025, the pathway annotation may not have been in Swiss-Prot at construction time.
- The pathway assignment is supported by in vitro biochemical characterization (Ghosh & Raushel, Biochemistry 2024), not merely computational transfer, lending strong experimental support to the key.
- The organism (Campylobacter jejuni) is not provided to the model, which removes important contextual information for pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P-loop/NTP-binding motif (GAGAGKTT ~residues 180-188) suggesting a nucleotidyltransferase, which is consistent with a cytidylyltransferase. However, the nucleotidyltransferase superfamily is enormous and spans dozens of pathways. Identifying this specific enzyme as CMP-N-acetylneuraminate synthase, and then recognizing that in Campylobacter jejuni sialic acid metabolism feeds into capsule polysaccharide biosynthesis (rather than, say, glycolipid or glycoprotein modification pathways), requires item-specific knowledge of this enzyme's substrate specificity and its organism-specific metabolic role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as CMP-Neu5Ac synthase (a sialic acid-activating cytidylyltransferase) and the fact that in Campylobacter jejuni, sialic acid (Neu5Ac) is incorporated into the capsular polysaccharide rather than serving other metabolic roles. Neither the substrate specificity nor the organism context is derivable from the bare sequence without database lookup or memorization.",
    "reason": "While the P-loop motif hints at a nucleotidyltransferase, this is far too broad to distinguish capsule biogenesis from amino-acid degradation or other pathways. The critical step—identifying the substrate as N-acetylneuraminate and linking sialic acid metabolism to capsule biosynthesis in Campylobacter—is an item-specific annotation fact not inferable from general biological reasoning on the sequence alone."
  },
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DY07 (NEUAC_CAMJ8), N-acylneuraminate cytidylyltransferase (EC 2.7.7.43, CMP-Neu5Ac synthase) from Campylobacter jejuni. The UniProt pathway annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). Sequence SHA256 match confirmed across current and historical records."
  },
  "important_caveats": [
    "The UniProt entry P0DY07 was first publicly released on 2025-06-18, with the key experimental paper (PubMed:38382015) published in 2024. The author's source snapshot date is unknown; if the benchmark was constructed before June 2025, the pathway annotation may not have been in Swiss-Prot at construction time.",
    "The pathway assignment is supported by in vitro biochemical characterization (Ghosh & Raushel, Biochemistry 2024), not merely computational transfer, lending strong experimental support to the key.",
    "The organism (Campylobacter jejuni) is not provided to the model, which removes important contextual information for pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct. Option D (amino-acid degradation) is a weak distractor since sialic acid is an amino sugar, but sialic acid metabolism is not amino-acid degradation. Options A and B are clearly unrelated pathways. Given the correct annotation, C is the only defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DY07 (NEUAC_CAMJ8), N-acylneuraminate cytidylyltransferase (EC 2.7.7.43, CMP-Neu5Ac synthase) from Campylobacter jejuni. The UniProt pathway annotation explicitly states 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). Sequence SHA256 match confirmed across current and historical records.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable P-loop/NTP-binding motif (GAGAGKTT ~residues 180-188) suggesting a nucleotidyltransferase, which is consistent with a cytidylyltransferase. However, the nucleotidyltransferase superfamily is enormous and spans dozens of pathways. Identifying this specific enzyme as CMP-N-acetylneuraminate synthase, and then recognizing that in Campylobacter jejuni sialic acid metabolism feeds into capsule polysaccharide biosynthesis (rather than, say, glycolipid or glycoprotein modification pathways), requires item-specific knowledge of this enzyme's substrate specificity and its organism-specific metabolic role.",
    "missing_item_specific_fact": "The specific identity of this protein as CMP-Neu5Ac synthase (a sialic acid-activating cytidylyltransferase) and the fact that in Campylobacter jejuni, sialic acid (Neu5Ac) is incorporated into the capsular polysaccharide rather than serving other metabolic roles. Neither the substrate specificity nor the organism context is derivable from the bare sequence without database lookup or memorization.",
    "reason": "While the P-loop motif hints at a nucleotidyltransferase, this is far too broad to distinguish capsule biogenesis from amino-acid degradation or other pathways. The critical step—identifying the substrate as N-acetylneuraminate and linking sialic acid metabolism to capsule biosynthesis in Campylobacter—is an item-specific annotation fact not inferable from general biological reasoning on the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct. Option D (amino-acid degradation) is a weak distractor since sialic acid is an amino sugar, but sialic acid metabolism is not amino-acid degradation. Options A and B are clearly unrelated pathways. Given the correct annotation, C is the only defensible answer."
  },
  "important_caveats": [
    "The UniProt entry P0DY07 was first publicly released on 2025-06-18, with the key experimental paper (PubMed:38382015) published in 2024. The author's source snapshot date is unknown; if the benchmark was constructed before June 2025, the pathway annotation may not have been in Swiss-Prot at construction time.",
    "The pathway assignment is supported by in vitro biochemical characterization (Ghosh & Raushel, Biochemistry 2024), not merely computational transfer, lending strong experimental support to the key.",
    "The organism (Campylobacter jejuni) is not provided to the model, which removes important contextual information for pathway assignment."
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

**Accession:** `P0DY07` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
"P0DY07"
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Campylobacterota","Epsilonproteobacteria","Campylobacterales","Campylobacteraceae","Campylobacter"],"scientificName":"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)","taxonId":407148}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-Neu5Ac synthase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.7.7.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"N-acylneuraminate cytidylyltransferase"}}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"Capsule biogenesis; capsule polysaccharide biosynthesis"}]}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"81116 / NCTC 11828"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
ID   NEUAC_CAMJ8             Reviewed;         394 AA.
AC   P0DY07;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};
DE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};
GN   Name=HS6.5 {ECO:0000303|PubMed:38382015};
GN   OrderedLocusNames=C8J_1333 {ECO:0000312|EMBL:ABV52931.1};
OS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC
OS   11828).
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=407148;
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 26-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.
RC   STRAIN=81116 / NCTC 11828;
RX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;
RA   Ghosh M.K., Raushel F.M.;
RT   "Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-
RT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter
RT   jejuni.";
RL   Biochemistry 63:688-698(2024).
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 57-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.
CC       {ECO:0000269|PubMed:38382015}.
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
