# pathway_0096

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLTENVMKPQIQRFTRDHDPKVLWQVVEEDGAVIIEGFLPHEVIQKFDCELDVRSKATKGGEMNQEFYQMPVPTTTKWMNDLTATCPTFRHEILNNDILHSLCNVAFEPHGDYWLLNGMAMEMMPGNPTQQIHNDHGTHPILQYLRPDAPAPVFSIITAVTEFTESNGATRVILGSHRWPQGQKAKDDQAVRAALQPGDALVMHRSTKHGGAAHDADNQDHRRLLLTCMGTCQLAPYETNVTVPRPIVESMTPLAQKMIGWRSTRPVISNVTGLNTVRMKHLENQIELKSNVPLNVGGC

[Multiple Choices]
A. L-histidine biosynthesis
B. Alkaloid biosynthesis. .
C. spheroidene biosynthesis. .
D. L-threonine from L-aspartate: step 2/5. .
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

> The exact sequence matches the UniProt entry annotated as OkaE, an okaramine-biosynthesis protein, with an alkaloid-biosynthesis pathway annotation citing experimental evidence. The cited primary studies are not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but it does not provide a defensible way to identify its specific role in okaramine biosynthesis rather than the listed alternatives.


**Missing item-specific fact**

> That this protein is OkaE, a protein involved in okaramine alkaloid biosynthesis.


**Reason**

> Distinguishing the pathway requires protein-specific functional knowledge or an annotation absent from the input; recognizing the sequence from an external database would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence directly supports alkaloid biosynthesis. Its broader terpenoid annotation does not establish the specific spheroidene pathway offered as a distractor.


### Important caveats

- The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.
- The pathway annotation cites experimental evidence, but the underlying papers were not independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but it does not provide a defensible way to identify its specific role in okaramine biosynthesis rather than the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this protein is OkaE, a protein involved in okaramine alkaloid biosynthesis.",
    "reason": "Distinguishing the pathway requires protein-specific functional knowledge or an annotation absent from the input; recognizing the sequence from an external database would be lookup or memorization."
  },
  "case_id": "pathway_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as OkaE, an okaramine-biosynthesis protein, with an alkaloid-biosynthesis pathway annotation citing experimental evidence. The cited primary studies are not independently assessed here."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the underlying papers were not independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence directly supports alkaloid biosynthesis. Its broader terpenoid annotation does not establish the specific spheroidene pathway offered as a distractor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as OkaE, an okaramine-biosynthesis protein, with an alkaloid-biosynthesis pathway annotation citing experimental evidence. The cited primary studies are not independently assessed here.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but it does not provide a defensible way to identify its specific role in okaramine biosynthesis rather than the listed alternatives.",
    "missing_item_specific_fact": "That this protein is OkaE, a protein involved in okaramine alkaloid biosynthesis.",
    "reason": "Distinguishing the pathway requires protein-specific functional knowledge or an annotation absent from the input; recognizing the sequence from an external database would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence directly supports alkaloid biosynthesis. Its broader terpenoid annotation does not establish the specific spheroidene pathway offered as a distractor."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The pathway annotation cites experimental evidence, but the underlying papers were not independently validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A2Z5U507 (OKAE_PENOH), an iron/alpha-ketoglutarate-dependent dioxygenase (EC 1.14.20.-) from Penicillium ochrochloron, part of the okaramine biosynthetic gene cluster. Okaramines are complex indole alkaloids. The UniProt PATHWAY annotation 'Alkaloid biosynthesis' is supported by experimental evidence (ECO:0000269) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed.) and PubMed:29384650 (Kato et al., 2018, ACS Chem. Biol.), both of which functionally characterize okaE in the okaramine (indole alkaloid) biosynthetic pathway.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is ~300 AA and consistent with an Fe(II)/2OG dioxygenase fold (HxD...H facial triad motifs are present). General biological knowledge allows elimination of three distractors: (A) L-histidine biosynthesis uses well-defined enzymes (ATP phosphoribosyltransferase, PR-ATP synthase, imidazoleglycerol-phosphate dehydratase, etc.) and does not involve Fe(II)/2OG dioxygenases as pathway enzymes; (C) spheroidene biosynthesis is a bacterial carotenoid pathway (crtP/crtI-type enzymes) and is implausible for a fungal protein; (D) L-threonine from L-aspartate step 2/5 is homoserine dehydrogenase, an NAD(P)-dependent oxidoreductase of a completely different enzyme class. This leaves (B) alkaloid biosynthesis as the only plausible option, consistent with the strong association of fungal Fe(II)/2OG dioxygenases with indole/terpenoid alkaloid tailoring reactions in Aspergillaceae.


**Missing item-specific fact**

> None strictly required. The positive identification of 'alkaloid' rather than a more generic 'secondary metabolite' label benefits from knowing that Penicillium Fe(II)/2OG dioxygenases are disproportionately involved in alkaloid (especially indole alkaloid) biosynthesis, but the elimination of the other three options is sufficient.


**Reason**

> A model with general knowledge of enzyme superfamilies, pathway biochemistry, and fungal secondary metabolism can eliminate A, C, and D and arrive at B without needing to recognize the exact sequence as okaE. The reasoning relies on enzyme-class/pathway incompatibility arguments rather than database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry also lists 'Secondary metabolite biosynthesis; terpenoid biosynthesis' as a secondary pathway annotation, but terpenoid biosynthesis is not among the choices. Among the four provided options, only B is consistent with a fungal Fe(II)/2OG dioxygenase involved in secondary metabolism. No other option is defensible.


### Important caveats

- The UniProt entry carries a secondary pathway annotation ('terpenoid biosynthesis') without an experimental evidence code in the excerpt; the primary experimental pathway is 'Alkaloid biosynthesis.' This does not create ambiguity among the given options since terpenoid biosynthesis is not offered.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-level reasoning and general knowledge.
- The Fe(II)/2OG dioxygenase superfamily is very large and shared across many pathways; the positive assignment to 'alkaloid biosynthesis' specifically rests partly on the statistical prevalence of this enzyme class in fungal alkaloid tailoring, which is general knowledge but not a sequence-intrinsic property.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is ~300 AA and consistent with an Fe(II)/2OG dioxygenase fold (HxD...H facial triad motifs are present). General biological knowledge allows elimination of three distractors: (A) L-histidine biosynthesis uses well-defined enzymes (ATP phosphoribosyltransferase, PR-ATP synthase, imidazoleglycerol-phosphate dehydratase, etc.) and does not involve Fe(II)/2OG dioxygenases as pathway enzymes; (C) spheroidene biosynthesis is a bacterial carotenoid pathway (crtP/crtI-type enzymes) and is implausible for a fungal protein; (D) L-threonine from L-aspartate step 2/5 is homoserine dehydrogenase, an NAD(P)-dependent oxidoreductase of a completely different enzyme class. This leaves (B) alkaloid biosynthesis as the only plausible option, consistent with the strong association of fungal Fe(II)/2OG dioxygenases with indole/terpenoid alkaloid tailoring reactions in Aspergillaceae.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The positive identification of 'alkaloid' rather than a more generic 'secondary metabolite' label benefits from knowing that Penicillium Fe(II)/2OG dioxygenases are disproportionately involved in alkaloid (especially indole alkaloid) biosynthesis, but the elimination of the other three options is sufficient.",
    "reason": "A model with general knowledge of enzyme superfamilies, pathway biochemistry, and fungal secondary metabolism can eliminate A, C, and D and arrive at B without needing to recognize the exact sequence as okaE. The reasoning relies on enzyme-class/pathway incompatibility arguments rather than database lookup."
  },
  "case_id": "pathway_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2Z5U507 (OKAE_PENOH), an iron/alpha-ketoglutarate-dependent dioxygenase (EC 1.14.20.-) from Penicillium ochrochloron, part of the okaramine biosynthetic gene cluster. Okaramines are complex indole alkaloids. The UniProt PATHWAY annotation 'Alkaloid biosynthesis' is supported by experimental evidence (ECO:0000269) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed.) and PubMed:29384650 (Kato et al., 2018, ACS Chem. Biol.), both of which functionally characterize okaE in the okaramine (indole alkaloid) biosynthetic pathway."
  },
  "important_caveats": [
    "The UniProt entry carries a secondary pathway annotation ('terpenoid biosynthesis') without an experimental evidence code in the excerpt; the primary experimental pathway is 'Alkaloid biosynthesis.' This does not create ambiguity among the given options since terpenoid biosynthesis is not offered.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-level reasoning and general knowledge.",
    "The Fe(II)/2OG dioxygenase superfamily is very large and shared across many pathways; the positive assignment to 'alkaloid biosynthesis' specifically rests partly on the statistical prevalence of this enzyme class in fungal alkaloid tailoring, which is general knowledge but not a sequence-intrinsic property."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists 'Secondary metabolite biosynthesis; terpenoid biosynthesis' as a secondary pathway annotation, but terpenoid biosynthesis is not among the choices. Among the four provided options, only B is consistent with a fungal Fe(II)/2OG dioxygenase involved in secondary metabolism. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2Z5U507 (OKAE_PENOH), an iron/alpha-ketoglutarate-dependent dioxygenase (EC 1.14.20.-) from Penicillium ochrochloron, part of the okaramine biosynthetic gene cluster. Okaramines are complex indole alkaloids. The UniProt PATHWAY annotation 'Alkaloid biosynthesis' is supported by experimental evidence (ECO:0000269) from PubMed:28631282 (Lai et al., 2017, Angew. Chem. Int. Ed.) and PubMed:29384650 (Kato et al., 2018, ACS Chem. Biol.), both of which functionally characterize okaE in the okaramine (indole alkaloid) biosynthetic pathway.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is ~300 AA and consistent with an Fe(II)/2OG dioxygenase fold (HxD...H facial triad motifs are present). General biological knowledge allows elimination of three distractors: (A) L-histidine biosynthesis uses well-defined enzymes (ATP phosphoribosyltransferase, PR-ATP synthase, imidazoleglycerol-phosphate dehydratase, etc.) and does not involve Fe(II)/2OG dioxygenases as pathway enzymes; (C) spheroidene biosynthesis is a bacterial carotenoid pathway (crtP/crtI-type enzymes) and is implausible for a fungal protein; (D) L-threonine from L-aspartate step 2/5 is homoserine dehydrogenase, an NAD(P)-dependent oxidoreductase of a completely different enzyme class. This leaves (B) alkaloid biosynthesis as the only plausible option, consistent with the strong association of fungal Fe(II)/2OG dioxygenases with indole/terpenoid alkaloid tailoring reactions in Aspergillaceae.",
    "missing_item_specific_fact": "None strictly required. The positive identification of 'alkaloid' rather than a more generic 'secondary metabolite' label benefits from knowing that Penicillium Fe(II)/2OG dioxygenases are disproportionately involved in alkaloid (especially indole alkaloid) biosynthesis, but the elimination of the other three options is sufficient.",
    "reason": "A model with general knowledge of enzyme superfamilies, pathway biochemistry, and fungal secondary metabolism can eliminate A, C, and D and arrive at B without needing to recognize the exact sequence as okaE. The reasoning relies on enzyme-class/pathway incompatibility arguments rather than database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists 'Secondary metabolite biosynthesis; terpenoid biosynthesis' as a secondary pathway annotation, but terpenoid biosynthesis is not among the choices. Among the four provided options, only B is consistent with a fungal Fe(II)/2OG dioxygenase involved in secondary metabolism. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt entry carries a secondary pathway annotation ('terpenoid biosynthesis') without an experimental evidence code in the excerpt; the primary experimental pathway is 'Alkaloid biosynthesis.' This does not create ambiguity among the given options since terpenoid biosynthesis is not offered.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence-level reasoning and general knowledge.",
    "The Fe(II)/2OG dioxygenase superfamily is very large and shared across many pathways; the positive assignment to 'alkaloid biosynthesis' specifically rests partly on the statistical prevalence of this enzyme class in fungal alkaloid tailoring, which is general knowledge but not a sequence-intrinsic property."
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

**Accession:** `A0A2Z5U507` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Okaramines biosynthesis cluster protein E"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"}],"value":"1.14.20.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28631282","source":"PubMed"}],"value":"Iron/alpha-ketoglutarate-dependent dioxygenase okaE"}}}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28631282","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29384650","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"citation":{"authors":["Kato N.","Furutani S.","Otaka J.","Noguchi A.","Kinugasa K.","Kai K.","Hayashi H.","Ihara M.","Takahashi S.","Matsuda K.","Osada H."],"citationCrossReferences":[{"database":"PubMed","id":"29384650"},{"database":"DOI","id":"10.1021/acschembio.7b00878"}],"citationType":"journal article","firstPage":"561","id":"29384650","journal":"ACS Chem. Biol.","lastPage":"566","publicationDate":"2018","title":"Biosynthesis and Structure-Activity Relationship Studies of Okaramines That Target Insect Glutamate-Gated Chloride Channels.","volume":"13"},"referenceComments":[{"type":"STRAIN","value":"ATCC 90288 / AK-40"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","DISRUPTION PHENOTYPE","PATHWAY"]}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U507.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:53.902384+00:00.  

```json
{"citation":{"authors":["Lai C.Y.","Lo I.W.","Hewage R.T.","Chen Y.C.","Chen C.T.","Lee C.F.","Lin S.","Tang M.C.","Lin H.C."],"citationCrossReferences":[{"database":"PubMed","id":"28631282"},{"database":"DOI","id":"10.1002/anie.201705501"}],"citationType":"journal article","firstPage":"9478","id":"28631282","journal":"Angew. Chem. Int. Ed.","lastPage":"9482","publicationDate":"2017","title":"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.","volume":"56"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `9990e6a6f579d0a5380e26f04d728094e4f4bad34f420af474667124b07036bb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
ID   OKAE_PENOH              Reviewed;         300 AA.
AC   A0A2Z5U507;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-OCT-2018, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=Iron/alpha-ketoglutarate-dependent dioxygenase okaE {ECO:0000303|PubMed:28631282};
DE            EC=1.14.20.- {ECO:0000269|PubMed:28631282};
DE   AltName: Full=Okaramines biosynthesis cluster protein E {ECO:0000303|PubMed:28631282};
GN   Name=okaE {ECO:0000303|PubMed:28631282};
OS   Penicillium ochrochloron.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=69780;
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 14-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, DISRUPTION PHENOTYPE, AND
RP   PATHWAY.
RC   STRAIN=ATCC 90288 / AK-40;
RX   PubMed=29384650; DOI=10.1021/acschembio.7b00878;
RA   Kato N., Furutani S., Otaka J., Noguchi A., Kinugasa K., Kai K.,
RA   Hayashi H., Ihara M., Takahashi S., Matsuda K., Osada H.;
RT   "Biosynthesis and Structure-Activity Relationship Studies of Okaramines
RT   That Target Insect Glutamate-Gated Chloride Channels.";
RL   ACS Chem. Biol. 13:561-566(2018).
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=28631282; DOI=10.1002/anie.201705501;
RA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,
RA   Tang M.C., Lin H.C.;
RT   "Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise
RT   Pathway of Okaramines.";
RL   Angew. Chem. Int. Ed. 56:9478-9482(2017).
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U507?format=txt&versions=21)  
**Locator:** `lines 87-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-02T04:24:56.491248+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:28631282,
CC       ECO:0000269|PubMed:29384650}.
```

Source SHA-256: `64ddb23c63ce009b89733028cc2d13c659d4412b3c22f48c98c262654f9060ab`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
