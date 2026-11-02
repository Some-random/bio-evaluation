# pathway_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLFQDLSFPAAIGAVFGAVAISVAARCIYDLFFHPLRNFPGPKRAAIWSFYEFYYDVIRDGTYLWEIEKMHQKYGPIVRINSRSLHIHDPEYFNTIYAGSGRKVNKELSAVSGYTFPHSTISTLDHDLHRKRRAIVSPYFSKRAIAEIEPVIHERLNVLISRLAEAKGSIVDLTSAFSAYTADVVTYHFYGTHANYIGSKDFKYGLKDALTVLLNLYNLTRFLPVPANTLKNLPLPILGLINPNFPLVVSAREANKKMVLGYLNKPDEDKKAMKDARSKSVIVSALTDPNVPDAEKTLDRLLDEGETIIFAGIDTTARTLGVALFHLLNNKDVLMKLRKELQAVAKPDGQQWTTTELEAVPYMRGVVQEAIRLAYGLVVRIPRISPHEALRYNGFVIPPGTPVSQSTYLVNNDPSVFPNPQVFDPERWVKAAQDGVSLDKYMVSFSKGSRGCLGINLAYAKLYLGIARVATSLDMELFETTAKAISVYHTRGFAFPKEGDGAVKARVMGLCK

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. Glycolipid biosynthesis
C. Protein modification
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

> The supplied sequence exactly matches UniProt entry Q0CPG7, annotated as cytochrome P450 monooxygenase astB and as functioning in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The pathway annotation cites literature; this supports choice A without establishing that every part of the annotation was independently experimentally verified here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a membrane-associated enzyme or P450-like protein, but they do not identify its particular biosynthetic pathway. General enzyme-family inference is insufficient to distinguish secondary-metabolite biosynthesis from the other pathway labels.


**Missing item-specific fact**

> The protein-specific identification as astB in the aspterric-acid biosynthesis cluster, and its associated pathway annotation, is absent from the supplied input.


**Reason**

> The key is supported by sequence-matched database and literature-linked annotation, but selecting it from the sequence and choices requires that item-specific functional information or prior knowledge of this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not substantiate a specific pathway choice, but the sequence-matched annotation supports A; the evidence does not establish another listed option as an equally defensible answer.


### Important caveats

- The reviewer-only accession and annotations were not supplied to the evaluated model.
- The exact historical author-source snapshot is unknown, although the sequence matches the checked historical and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a membrane-associated enzyme or P450-like protein, but they do not identify its particular biosynthetic pathway. General enzyme-family inference is insufficient to distinguish secondary-metabolite biosynthesis from the other pathway labels.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as astB in the aspterric-acid biosynthesis cluster, and its associated pathway annotation, is absent from the supplied input.",
    "reason": "The key is supported by sequence-matched database and literature-linked annotation, but selecting it from the sequence and choices requires that item-specific functional information or prior knowledge of this protein."
  },
  "case_id": "pathway_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt entry Q0CPG7, annotated as cytochrome P450 monooxygenase astB and as functioning in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The pathway annotation cites literature; this supports choice A without establishing that every part of the annotation was independently experimentally verified here."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The exact historical author-source snapshot is unknown, although the sequence matches the checked historical and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not substantiate a specific pathway choice, but the sequence-matched annotation supports A; the evidence does not establish another listed option as an equally defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt entry Q0CPG7, annotated as cytochrome P450 monooxygenase astB and as functioning in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The pathway annotation cites literature; this supports choice A without establishing that every part of the annotation was independently experimentally verified here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a membrane-associated enzyme or P450-like protein, but they do not identify its particular biosynthetic pathway. General enzyme-family inference is insufficient to distinguish secondary-metabolite biosynthesis from the other pathway labels.",
    "missing_item_specific_fact": "The protein-specific identification as astB in the aspterric-acid biosynthesis cluster, and its associated pathway annotation, is absent from the supplied input.",
    "reason": "The key is supported by sequence-matched database and literature-linked annotation, but selecting it from the sequence and choices requires that item-specific functional information or prior knowledge of this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not substantiate a specific pathway choice, but the sequence-matched annotation supports A; the evidence does not establish another listed option as an equally defensible answer."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The exact historical author-source snapshot is unknown, although the sequence matches the checked historical and current records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (evidence codes ECO:0000269|PubMed:29995859 and ECO:0000269|PubMed:39511739). The protein is named 'Aspterric acid biosynthesis cluster protein B,' and aspterric acid is a natural-product herbicide (a terpenoid secondary metabolite). The sequence matches exactly. Choice A is directly supported by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable cytochrome P450 hallmarks: an N-terminal hydrophobic membrane-anchoring segment, the conserved I-helix region (FGIDTTARTLGVALFHLLNNKD…), and the heme-binding FxxGxxxCxG motif (FSKGSRGCLGINLAYAKLYLGIARVATSLDMELFETTAKAISVYHTRGFAFPKEGDGAVKARVMGLCK with the invariant Cys). Recognizing the protein as a P450 allows elimination of D (threonine biosynthesis from aspartate involves dehydrogenases and kinases, not P450s) and C (P450s catalyze monooxygenation of small molecules, not protein modification). Between A and B, fungal P450s are overwhelmingly associated with secondary metabolite (terpenoid, polyketide, NRPS) biosynthetic gene clusters, whereas glycolipid biosynthesis relies primarily on glycosyltransferases, phosphatases, and acyltransferases rather than P450s. This general biological knowledge provides a meaningful reasoning chain to select A.


**Missing item-specific fact**

> None strictly required. The specific identity of astB and its role in aspterric acid biosynthesis is an item-specific fact, but the general P450-in-secondary-metabolite association in fungi is sufficient to favor A over the other three options without knowing the exact protein.


**Reason**

> A model can (a) identify P450 features from the sequence, (b) eliminate D and C on mechanistic grounds, and (c) use the well-established association of fungal P450s with secondary metabolite gene clusters to prefer A over B. This constitutes a concrete biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D and C are mechanistically incompatible with P450 catalysis. B (glycolipid biosynthesis) is a weak alternative since a few P450s participate in lipid tailoring, but this is rare and not the primary fungal P450 context. The experimental annotation unambiguously places this protein in secondary metabolite/terpenoid biosynthesis, leaving A as the single defensible answer.


### Important caveats

- The model is not told the organism is a fungus; the fungal P450 → secondary metabolite heuristic is a general biological tendency rather than a sequence-enclosed fact. However, P450 involvement in secondary metabolite biosynthesis is well-established across kingdoms.
- The UniProt entry was first publicly released in April 2025; the author's exact source snapshot is unknown, but the sequence and pathway annotation are consistent across archived and current versions.
- The EC number is listed as 1.-.-.- (unassigned subclass), so the exact catalytic reaction is not fully specified in the annotation, though the pathway assignment is experimentally supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 hallmarks: an N-terminal hydrophobic membrane-anchoring segment, the conserved I-helix region (FGIDTTARTLGVALFHLLNNKD…), and the heme-binding FxxGxxxCxG motif (FSKGSRGCLGINLAYAKLYLGIARVATSLDMELFETTAKAISVYHTRGFAFPKEGDGAVKARVMGLCK with the invariant Cys). Recognizing the protein as a P450 allows elimination of D (threonine biosynthesis from aspartate involves dehydrogenases and kinases, not P450s) and C (P450s catalyze monooxygenation of small molecules, not protein modification). Between A and B, fungal P450s are overwhelmingly associated with secondary metabolite (terpenoid, polyketide, NRPS) biosynthetic gene clusters, whereas glycolipid biosynthesis relies primarily on glycosyltransferases, phosphatases, and acyltransferases rather than P450s. This general biological knowledge provides a meaningful reasoning chain to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The specific identity of astB and its role in aspterric acid biosynthesis is an item-specific fact, but the general P450-in-secondary-metabolite association in fungi is sufficient to favor A over the other three options without knowing the exact protein.",
    "reason": "A model can (a) identify P450 features from the sequence, (b) eliminate D and C on mechanistic grounds, and (c) use the well-established association of fungal P450s with secondary metabolite gene clusters to prefer A over B. This constitutes a concrete biological argument rather than pure lookup."
  },
  "case_id": "pathway_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (evidence codes ECO:0000269|PubMed:29995859 and ECO:0000269|PubMed:39511739). The protein is named 'Aspterric acid biosynthesis cluster protein B,' and aspterric acid is a natural-product herbicide (a terpenoid secondary metabolite). The sequence matches exactly. Choice A is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The model is not told the organism is a fungus; the fungal P450 → secondary metabolite heuristic is a general biological tendency rather than a sequence-enclosed fact. However, P450 involvement in secondary metabolite biosynthesis is well-established across kingdoms.",
    "The UniProt entry was first publicly released in April 2025; the author's exact source snapshot is unknown, but the sequence and pathway annotation are consistent across archived and current versions.",
    "The EC number is listed as 1.-.-.- (unassigned subclass), so the exact catalytic reaction is not fully specified in the annotation, though the pathway assignment is experimentally supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D and C are mechanistically incompatible with P450 catalysis. B (glycolipid biosynthesis) is a weak alternative since a few P450s participate in lipid tailoring, but this is rare and not the primary fungal P450 context. The experimental annotation unambiguously places this protein in secondary metabolite/terpenoid biosynthesis, leaving A as the single defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG7 (Cytochrome P450 monooxygenase astB, Aspergillus terreus) is explicitly annotated with PATHWAY: 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (evidence codes ECO:0000269|PubMed:29995859 and ECO:0000269|PubMed:39511739). The protein is named 'Aspterric acid biosynthesis cluster protein B,' and aspterric acid is a natural-product herbicide (a terpenoid secondary metabolite). The sequence matches exactly. Choice A is directly supported by experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 hallmarks: an N-terminal hydrophobic membrane-anchoring segment, the conserved I-helix region (FGIDTTARTLGVALFHLLNNKD…), and the heme-binding FxxGxxxCxG motif (FSKGSRGCLGINLAYAKLYLGIARVATSLDMELFETTAKAISVYHTRGFAFPKEGDGAVKARVMGLCK with the invariant Cys). Recognizing the protein as a P450 allows elimination of D (threonine biosynthesis from aspartate involves dehydrogenases and kinases, not P450s) and C (P450s catalyze monooxygenation of small molecules, not protein modification). Between A and B, fungal P450s are overwhelmingly associated with secondary metabolite (terpenoid, polyketide, NRPS) biosynthetic gene clusters, whereas glycolipid biosynthesis relies primarily on glycosyltransferases, phosphatases, and acyltransferases rather than P450s. This general biological knowledge provides a meaningful reasoning chain to select A.",
    "missing_item_specific_fact": "None strictly required. The specific identity of astB and its role in aspterric acid biosynthesis is an item-specific fact, but the general P450-in-secondary-metabolite association in fungi is sufficient to favor A over the other three options without knowing the exact protein.",
    "reason": "A model can (a) identify P450 features from the sequence, (b) eliminate D and C on mechanistic grounds, and (c) use the well-established association of fungal P450s with secondary metabolite gene clusters to prefer A over B. This constitutes a concrete biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D and C are mechanistically incompatible with P450 catalysis. B (glycolipid biosynthesis) is a weak alternative since a few P450s participate in lipid tailoring, but this is rare and not the primary fungal P450 context. The experimental annotation unambiguously places this protein in secondary metabolite/terpenoid biosynthesis, leaving A as the single defensible answer."
  },
  "important_caveats": [
    "The model is not told the organism is a fungus; the fungal P450 → secondary metabolite heuristic is a general biological tendency rather than a sequence-enclosed fact. However, P450 involvement in secondary metabolite biosynthesis is well-established across kingdoms.",
    "The UniProt entry was first publicly released in April 2025; the author's exact source snapshot is unknown, but the sequence and pathway annotation are consistent across archived and current versions.",
    "The EC number is listed as 1.-.-.- (unassigned subclass), so the exact catalytic reaction is not fully specified in the annotation, though the pathway assignment is experimentally supported."
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

**Accession:** `Q0CPG7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:23.383605+00:00.  

```json
"Q0CPG7"
```

Source SHA-256: `86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:23.383605+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein B"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase astB"}}}
```

Source SHA-256: `86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:23.383605+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:23.383605+00:00.  

```json
{"citation":{"authors":["Yan Y.","Liu Q.","Zang X.","Yuan S.","Bat-Erdene U.","Nguyen C.","Gan J.","Zhou J.","Jacobsen S.E.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"29995859"},{"database":"DOI","id":"10.1038/s41586-018-0319-4"}],"citationType":"journal article","firstPage":"415","id":"29995859","journal":"Nature","lastPage":"418","publicationDate":"2018","title":"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.","volume":"559"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `86ed5fa987c40e9dd0f38132dfb083141c7c6bc7fd318b92a558b8e92e5846fc`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:30:28.173476+00:00.  

```text
ID   ASTB_ASPTN              Reviewed;         512 AA.
AC   Q0CPG7;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-OCT-2006, sequence version 1.
DT   28-JAN-2026, entry version 84.
DE   RecName: Full=Cytochrome P450 monooxygenase astB {ECO:0000303|PubMed:29995859};
DE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein B {ECO:0000303|PubMed:29995859};
GN   Name=astB {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04417;
OS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=341663;
```

Source SHA-256: `af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)  
**Locator:** `lines 27-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:30:28.173476+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;
RA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,
RA   Zhou J., Jacobsen S.E., Tang Y.;
RT   "Resistance-gene-directed discovery of a natural-product herbicide with a
RT   new mode of action.";
RL   Nature 559:415-418(2018).
```

Source SHA-256: `af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG7?format=txt&versions=84)  
**Locator:** `lines 63-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:30:28.173476+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:29995859, ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `af10b808e0591f68545ada812b145c7d6e3f216b49d49121ac583c1305af66ce`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
