# pathway_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Protein biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPYQMGEAMPDLVPVLAGAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTAETIADPEARSVANRAIVTLRRIGKVPVESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLSDKRLLATPEEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEEFVKHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAVLGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAELAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGHLEASGHNWVEGQGSGERIDKKAGDDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. L-isoleucine biosynthesis
B. Protein biosynthesis
C. terpenoid biosynthesis.
D. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
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

> The supplied sequence exactly matches the 1,055-aa UniProt entry annotated as elongation factor 3, whose pathway is protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity, so it supports B without being direct experimental proof of pathway involvement for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains ATPase-like motifs, but those do not by themselves identify a specific pathway or distinguish translation from other ATP-dependent functions. The choices do not supply additional biological context that identifies the protein as a translation factor.


**Missing item-specific fact**

> The protein-specific identity and function as eukaryotic elongation factor 3, including its role in polypeptide-chain elongation.


**Reason**

> Selecting B requires recognizing or looking up this protein's specific function. General sequence reasoning alone does not establish the pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the protein's annotated elongation-factor function, protein biosynthesis is the clearly fitting choice among the listed options.


### Important caveats

- The pathway annotation is supported by an evidence code indicating transfer from a homolog, rather than direct experimental pathway evidence for this exact sequence.
- The sequence match establishes applicability to the benchmark protein; the exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains ATPase-like motifs, but those do not by themselves identify a specific pathway or distinguish translation from other ATP-dependent functions. The choices do not supply additional biological context that identifies the protein as a translation factor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and function as eukaryotic elongation factor 3, including its role in polypeptide-chain elongation.",
    "reason": "Selecting B requires recognizing or looking up this protein's specific function. General sequence reasoning alone does not establish the pathway."
  },
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1,055-aa UniProt entry annotated as elongation factor 3, whose pathway is protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity, so it supports B without being direct experimental proof of pathway involvement for this exact protein."
  },
  "important_caveats": [
    "The pathway annotation is supported by an evidence code indicating transfer from a homolog, rather than direct experimental pathway evidence for this exact sequence.",
    "The sequence match establishes applicability to the benchmark protein; the exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein's annotated elongation-factor function, protein biosynthesis is the clearly fitting choice among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1,055-aa UniProt entry annotated as elongation factor 3, whose pathway is protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity, so it supports B without being direct experimental proof of pathway involvement for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains ATPase-like motifs, but those do not by themselves identify a specific pathway or distinguish translation from other ATP-dependent functions. The choices do not supply additional biological context that identifies the protein as a translation factor.",
    "missing_item_specific_fact": "The protein-specific identity and function as eukaryotic elongation factor 3, including its role in polypeptide-chain elongation.",
    "reason": "Selecting B requires recognizing or looking up this protein's specific function. General sequence reasoning alone does not establish the pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein's annotated elongation-factor function, protein biosynthesis is the clearly fitting choice among the listed options."
  },
  "important_caveats": [
    "The pathway annotation is supported by an evidence code indicating transfer from a homolog, rather than direct experimental pathway evidence for this exact sequence.",
    "The sequence match establishes applicability to the benchmark protein; the exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5KIM6 (EF3_CRYD1) explicitly annotates the pathway as 'Protein biosynthesis; polypeptide chain elongation' (C5, H3). The protein is Elongation Factor 3 (eEF3), a fungal-specific translation elongation factor with EC 3.6.4.-, experimentally characterized for function, catalytic activity, and ribosome association (C6, H2). The sequence matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer 'Protein biosynthesis' directly corresponds to the annotated pathway.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains three Walker A / P-loop motifs (GRNGSGKSTLMNAIINN, GPNGSGKSTLVKLLTGET, GSGGQKVKVVLGAAT), characteristic of AAA+ ATPase domains, and is very large (~1055 aa), indicating a multi-domain NTPase. Among the four choices, protein biosynthesis (translation) is the only pathway whose key components (elongation factors EF1, EF2, EF3) are large multi-domain ATPases/GTPases. The other options—L-isoleucine biosynthesis, terpenoid biosynthesis, and chorismate biosynthesis (shikimate pathway)—involve relatively small, single-domain biosynthetic enzymes (e.g., acetohydroxyacid synthase, terpene cyclases, DAHP synthase) that lack AAA+ P-loop architectures. A model with general knowledge of enzyme domain families can reasonably infer that a ~1000-aa protein with multiple Walker A motifs belongs to translation rather than small-molecule biosynthesis.


**Missing item-specific fact**

> None strictly required. Recognizing the protein as specifically EF3 (a fungal-specific elongation factor) would require database lookup, but the domain architecture (multiple AAA+ P-loops, large size) provides sufficient biological grounds to select 'Protein biosynthesis' over the three small-enzyme biosynthetic pathway options.


**Reason**

> The multiple Walker A motifs and large multi-domain architecture are generalizable sequence features that distinguish translation factors from the small, specific enzymes of amino acid or terpenoid biosynthesis pathways. This constitutes a concrete biological argument from the sequence itself, not mere memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different pathway categories. The AAA+ ATPase architecture of the sequence is inconsistent with the enzyme types in options A, C, and D. Only option B (protein biosynthesis) involves large multi-domain NTPases as pathway components. The distractors are well-separated from the correct answer.


### Important caveats

- The pathway annotation in UniProt carries evidence code ECO:0000250 (similarity to O93796), meaning the pathway assignment for Q5KIM6 is transferred by similarity rather than independently demonstrated for this exact protein. However, the protein's function as an elongation factor is supported by experimental evidence (PubMed 11244063, ECO:0000305).
- The reviewer-only UniProt accession and metadata were not available to the evaluated model; the model must rely on sequence features and general biological knowledge.
- EF3 is unique to fungi; a model unaware of fungal-specific elongation factors might still reason from domain architecture, but the fungal context (Cryptococcus) is not provided in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains three Walker A / P-loop motifs (GRNGSGKSTLMNAIINN, GPNGSGKSTLVKLLTGET, GSGGQKVKVVLGAAT), characteristic of AAA+ ATPase domains, and is very large (~1055 aa), indicating a multi-domain NTPase. Among the four choices, protein biosynthesis (translation) is the only pathway whose key components (elongation factors EF1, EF2, EF3) are large multi-domain ATPases/GTPases. The other options—L-isoleucine biosynthesis, terpenoid biosynthesis, and chorismate biosynthesis (shikimate pathway)—involve relatively small, single-domain biosynthetic enzymes (e.g., acetohydroxyacid synthase, terpene cyclases, DAHP synthase) that lack AAA+ P-loop architectures. A model with general knowledge of enzyme domain families can reasonably infer that a ~1000-aa protein with multiple Walker A motifs belongs to translation rather than small-molecule biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the protein as specifically EF3 (a fungal-specific elongation factor) would require database lookup, but the domain architecture (multiple AAA+ P-loops, large size) provides sufficient biological grounds to select 'Protein biosynthesis' over the three small-enzyme biosynthetic pathway options.",
    "reason": "The multiple Walker A motifs and large multi-domain architecture are generalizable sequence features that distinguish translation factors from the small, specific enzymes of amino acid or terpenoid biosynthesis pathways. This constitutes a concrete biological argument from the sequence itself, not mere memorization of a database entry."
  },
  "case_id": "pathway_0131",
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
    "reason": "UniProt entry Q5KIM6 (EF3_CRYD1) explicitly annotates the pathway as 'Protein biosynthesis; polypeptide chain elongation' (C5, H3). The protein is Elongation Factor 3 (eEF3), a fungal-specific translation elongation factor with EC 3.6.4.-, experimentally characterized for function, catalytic activity, and ribosome association (C6, H2). The sequence matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer 'Protein biosynthesis' directly corresponds to the annotated pathway."
  },
  "important_caveats": [
    "The pathway annotation in UniProt carries evidence code ECO:0000250 (similarity to O93796), meaning the pathway assignment for Q5KIM6 is transferred by similarity rather than independently demonstrated for this exact protein. However, the protein's function as an elongation factor is supported by experimental evidence (PubMed 11244063, ECO:0000305).",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the model must rely on sequence features and general biological knowledge.",
    "EF3 is unique to fungi; a model unaware of fungal-specific elongation factors might still reason from domain architecture, but the fungal context (Cryptococcus) is not provided in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different pathway categories. The AAA+ ATPase architecture of the sequence is inconsistent with the enzyme types in options A, C, and D. Only option B (protein biosynthesis) involves large multi-domain NTPases as pathway components. The distractors are well-separated from the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5KIM6 (EF3_CRYD1) explicitly annotates the pathway as 'Protein biosynthesis; polypeptide chain elongation' (C5, H3). The protein is Elongation Factor 3 (eEF3), a fungal-specific translation elongation factor with EC 3.6.4.-, experimentally characterized for function, catalytic activity, and ribosome association (C6, H2). The sequence matches the UniProt entry exactly (SHA-256 match confirmed). The expected answer 'Protein biosynthesis' directly corresponds to the annotated pathway.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains three Walker A / P-loop motifs (GRNGSGKSTLMNAIINN, GPNGSGKSTLVKLLTGET, GSGGQKVKVVLGAAT), characteristic of AAA+ ATPase domains, and is very large (~1055 aa), indicating a multi-domain NTPase. Among the four choices, protein biosynthesis (translation) is the only pathway whose key components (elongation factors EF1, EF2, EF3) are large multi-domain ATPases/GTPases. The other options—L-isoleucine biosynthesis, terpenoid biosynthesis, and chorismate biosynthesis (shikimate pathway)—involve relatively small, single-domain biosynthetic enzymes (e.g., acetohydroxyacid synthase, terpene cyclases, DAHP synthase) that lack AAA+ P-loop architectures. A model with general knowledge of enzyme domain families can reasonably infer that a ~1000-aa protein with multiple Walker A motifs belongs to translation rather than small-molecule biosynthesis.",
    "missing_item_specific_fact": "None strictly required. Recognizing the protein as specifically EF3 (a fungal-specific elongation factor) would require database lookup, but the domain architecture (multiple AAA+ P-loops, large size) provides sufficient biological grounds to select 'Protein biosynthesis' over the three small-enzyme biosynthetic pathway options.",
    "reason": "The multiple Walker A motifs and large multi-domain architecture are generalizable sequence features that distinguish translation factors from the small, specific enzymes of amino acid or terpenoid biosynthesis pathways. This constitutes a concrete biological argument from the sequence itself, not mere memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different pathway categories. The AAA+ ATPase architecture of the sequence is inconsistent with the enzyme types in options A, C, and D. Only option B (protein biosynthesis) involves large multi-domain NTPases as pathway components. The distractors are well-separated from the correct answer."
  },
  "important_caveats": [
    "The pathway annotation in UniProt carries evidence code ECO:0000250 (similarity to O93796), meaning the pathway assignment for Q5KIM6 is transferred by similarity rather than independently demonstrated for this exact protein. However, the protein's function as an elongation factor is supported by experimental evidence (PubMed 11244063, ECO:0000305).",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the model must rely on sequence features and general biological knowledge.",
    "EF3 is unique to fungi; a model unaware of fungal-specific elongation factors might still reason from domain architecture, but the fungal context (Cryptococcus) is not provided in the question."
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

**Accession:** `Q5KIM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 144. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
"Q5KIM6"
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11244063","source":"PubMed"}],"value":"CnEF3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11244063","source":"PubMed"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O93796","source":"UniProtKB"}],"value":"Protein biosynthesis; polypeptide chain elongation"}]}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"citation":{"authors":["Blakely G.","Hekman J.","Chakraburtty K.","Williamson P.R."],"citationCrossReferences":[{"database":"PubMed","id":"11244063"},{"database":"DOI","id":"10.1128/jb.183.7.2241-2248.2001"}],"citationType":"journal article","firstPage":"2241","id":"11244063","journal":"J. Bacteriol.","lastPage":"2248","publicationDate":"2001","title":"Evolutionary divergence of an elongation factor 3 from Cryptococcus neoformans.","volume":"183"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11244063","source":"PubMed"}],"type":"STRAIN","value":"B-3501A"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ASSOCIATION WITH RIBOSOMES"]}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
ID   EF3_CRYD1               Reviewed;        1055 AA.
AC   Q5KIM6; Q55TQ9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 144.
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000269|PubMed:11244063};
DE   AltName: Full=CnEF3 {ECO:0000303|PubMed:11244063};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
GN   Name=TEF3 {ECO:0000305};
GN   OrderedLocusNames=CND02420 {ECO:0000312|EMBL:AAW42954.1};
OS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus
OS   neoformans var. neoformans serotype D).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   ASSOCIATION WITH RIBOSOMES.
RC   STRAIN=B-3501A {ECO:0000303|PubMed:11244063};
RX   PubMed=11244063; DOI=10.1128/jb.183.7.2241-2248.2001;
RA   Blakely G., Hekman J., Chakraburtty K., Williamson P.R.;
RT   "Evolutionary divergence of an elongation factor 3 from Cryptococcus
RT   neoformans.";
RL   J. Bacteriol. 183:2241-2248(2001).
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.
CC       {ECO:0000250|UniProtKB:O93796}.
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
