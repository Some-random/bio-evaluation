# catalytic_activity_0166

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-lysyl-&#91;protein&#93; + acetyl-CoA = N(6)-acetyl-L-lysyl-&#91;protein&#93; + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASENNKRKASEEALSPDSQLQSKKARTDSPEREPKSEGGPLGKPPLRIVPFPEKPAVLEERRGEIEFRVVNNDGSRDSFVVLTGLKCIFQKQLPKMPKDYIARLVYDRSHLSIAIVKHPLEVVGGITYRPFNSRRFAEIVFCAISSDQQVKGYGAHLMSHLKDYVKATSPIMHFLTYADNYAIGYFKKQGFTKEITLDKSIWMGYIKDYEGGTIMQCTMLPKIRYLEIGRMLLKQKEAVHAKIRAFSRSHIIHAPPKEWKNGACKIDPLSIPAIKQSGWSPDMDELARQPRHGPNYNQLLHLLNDMQNHSAAWPFTQPVNRDEVPDYYEVIKEPMDLSTMEEKHEKDMYPTPQDFIKDAMLIFDNCRRYNNENTPYAKSANKLEKFMWQQIRNIPEWSVST

[Multiple Choices]
A. Hydrolyzes single-stranded DNA or mismatched double-stranded DNA and polynucleotides, releasing free uracil.
B. Cs(+)(in) = Cs(+)(out)
C. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
D. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
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

> The exact sequence matches the UniProt entry, whose catalytic-activity annotation gives the reaction in D and cites experimental evidence from PubMed 39601562. This supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support predicting an acetyltransferase-like function, but it does not by itself establish this protein's specific substrate and reaction well enough to distinguish D from the alternatives.


**Missing item-specific fact**

> The protein-specific assignment of this sequence to GcnE and its experimentally annotated acetylation of protein-bound lysine using acetyl-CoA.


**Reason**

> Selecting the precise reaction depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence from a database would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D matches the supported listed reaction. The protein also has an annotated benzoyltransferase activity, but that reaction is not among the choices.


### Important caveats

- The database annotation cites experimental evidence, but the cited primary study was not independently validated in the supplied evidence.
- The reviewer-only sequence match and annotations were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support predicting an acetyltransferase-like function, but it does not by itself establish this protein's specific substrate and reaction well enough to distinguish D from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to GcnE and its experimentally annotated acetylation of protein-bound lysine using acetyl-CoA.",
    "reason": "Selecting the precise reaction depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence from a database would be lookup, not reasoning from the supplied input."
  },
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, whose catalytic-activity annotation gives the reaction in D and cites experimental evidence from PubMed 39601562. This supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary study was not independently validated in the supplied evidence.",
    "The reviewer-only sequence match and annotations were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the supported listed reaction. The protein also has an annotated benzoyltransferase activity, but that reaction is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, whose catalytic-activity annotation gives the reaction in D and cites experimental evidence from PubMed 39601562. This supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support predicting an acetyltransferase-like function, but it does not by itself establish this protein's specific substrate and reaction well enough to distinguish D from the alternatives.",
    "missing_item_specific_fact": "The protein-specific assignment of this sequence to GcnE and its experimentally annotated acetylation of protein-bound lysine using acetyl-CoA.",
    "reason": "Selecting the precise reaction depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence from a database would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the supported listed reaction. The protein also has an annotated benzoyltransferase activity, but that reaction is not among the choices."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary study was not independently validated in the supplied evidence.",
    "The reviewer-only sequence match and annotations were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7U2QYM2 (GCNE_ASPFN, Histone acetyltransferase gcnE, EC 2.3.1.48) from Aspergillus flavus explicitly annotates the catalytic activity as 'L-lysyl-&#91;protein&#93; + acetyl-CoA = N(6)-acetyl-L-lysyl-&#91;protein&#93; + CoA + H(+)' with experimental evidence (ECO:0000269, PubMed:39601562). The sequence matches exactly (SHA256 identical, 402 AA). The recommended name is Histone acetyltransferase gcnE, and the EC number 2.3.1.48 corresponds precisely to the reaction in Choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None readily available from the raw sequence. While the protein belongs to the GNAT (Gcn5-related N-acetyltransferase) family, identifying a GNAT fold from a 402-aa fungal sequence without prior knowledge of this specific protein or access to sequence databases is not achievable through general biological reasoning. The four distractors (uracil DNA glycosylase, Cs+ transporter, alcohol dehydrogenase, histone acetyltransferase) represent entirely different enzyme classes, and nothing in the sequence text alone—such as an easily recognizable active-site motif or substrate-binding signature—allows a general biologist to distinguish acetyltransferase activity from the other options.


**Missing item-specific fact**

> The identity of this protein as GcnE (a Gcn5-related N-acetyltransferase) from Aspergillus flavus, or recognition of the specific GNAT-domain fold architecture in this sequence, which is required to select D over the other three enzyme classes.


**Reason**

> Selecting D requires recognizing this specific protein's identity or its GNAT-domain fold. A trained model might recall the sequence-to-function mapping, but that constitutes memorization of a database entry rather than reasoning from general biological principles. No general argument from amino-acid composition, length, or obvious motifs distinguishes a histone acetyltransferase from a DNA repair enzyme, ion transporter, or alcohol dehydrogenase in this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, D is the only one matching the experimentally validated primary catalytic activity of this protein. The alternative benzoyltransferase activity (benzoyl-CoA + L-lysyl-&#91;protein&#93; = N(6)-benzoyl-L-lysyl-&#91;protein&#93; + CoA + H(+)) is not offered as a choice, so no ambiguity exists among the listed options.


### Important caveats

- The protein also has a documented benzoyltransferase activity (EC 2.3.1.-, PubMed:39601562), but this reaction is not among the choices, so it does not create ambiguity.
- The primary annotation of histone acetyltransferase activity carries evidence code ECO:0000250 (similarity to UniProtKB:Q03330, S. cerevisiae Gcn5) for the name, while the catalytic activity annotation itself is backed by experimental evidence (ECO:0000269, PubMed:39601562).
- The identity origin of the accession (A0A7U2QYM2) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model only saw the raw sequence.
- The entry was first publicly released in April 2025 and the supporting publication appeared in 2025; the author's source snapshot date is unknown, so the annotation may not have existed at the time of question construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None readily available from the raw sequence. While the protein belongs to the GNAT (Gcn5-related N-acetyltransferase) family, identifying a GNAT fold from a 402-aa fungal sequence without prior knowledge of this specific protein or access to sequence databases is not achievable through general biological reasoning. The four distractors (uracil DNA glycosylase, Cs+ transporter, alcohol dehydrogenase, histone acetyltransferase) represent entirely different enzyme classes, and nothing in the sequence text alone—such as an easily recognizable active-site motif or substrate-binding signature—allows a general biologist to distinguish acetyltransferase activity from the other options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this protein as GcnE (a Gcn5-related N-acetyltransferase) from Aspergillus flavus, or recognition of the specific GNAT-domain fold architecture in this sequence, which is required to select D over the other three enzyme classes.",
    "reason": "Selecting D requires recognizing this specific protein's identity or its GNAT-domain fold. A trained model might recall the sequence-to-function mapping, but that constitutes memorization of a database entry rather than reasoning from general biological principles. No general argument from amino-acid composition, length, or obvious motifs distinguishes a histone acetyltransferase from a DNA repair enzyme, ion transporter, or alcohol dehydrogenase in this sequence."
  },
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7U2QYM2 (GCNE_ASPFN, Histone acetyltransferase gcnE, EC 2.3.1.48) from Aspergillus flavus explicitly annotates the catalytic activity as 'L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)' with experimental evidence (ECO:0000269, PubMed:39601562). The sequence matches exactly (SHA256 identical, 402 AA). The recommended name is Histone acetyltransferase gcnE, and the EC number 2.3.1.48 corresponds precisely to the reaction in Choice D."
  },
  "important_caveats": [
    "The protein also has a documented benzoyltransferase activity (EC 2.3.1.-, PubMed:39601562), but this reaction is not among the choices, so it does not create ambiguity.",
    "The primary annotation of histone acetyltransferase activity carries evidence code ECO:0000250 (similarity to UniProtKB:Q03330, S. cerevisiae Gcn5) for the name, while the catalytic activity annotation itself is backed by experimental evidence (ECO:0000269, PubMed:39601562).",
    "The identity origin of the accession (A0A7U2QYM2) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model only saw the raw sequence.",
    "The entry was first publicly released in April 2025 and the supporting publication appeared in 2025; the author's source snapshot date is unknown, so the annotation may not have existed at the time of question construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, D is the only one matching the experimentally validated primary catalytic activity of this protein. The alternative benzoyltransferase activity (benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)) is not offered as a choice, so no ambiguity exists among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7U2QYM2 (GCNE_ASPFN, Histone acetyltransferase gcnE, EC 2.3.1.48) from Aspergillus flavus explicitly annotates the catalytic activity as 'L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)' with experimental evidence (ECO:0000269, PubMed:39601562). The sequence matches exactly (SHA256 identical, 402 AA). The recommended name is Histone acetyltransferase gcnE, and the EC number 2.3.1.48 corresponds precisely to the reaction in Choice D.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None readily available from the raw sequence. While the protein belongs to the GNAT (Gcn5-related N-acetyltransferase) family, identifying a GNAT fold from a 402-aa fungal sequence without prior knowledge of this specific protein or access to sequence databases is not achievable through general biological reasoning. The four distractors (uracil DNA glycosylase, Cs+ transporter, alcohol dehydrogenase, histone acetyltransferase) represent entirely different enzyme classes, and nothing in the sequence text alone—such as an easily recognizable active-site motif or substrate-binding signature—allows a general biologist to distinguish acetyltransferase activity from the other options.",
    "missing_item_specific_fact": "The identity of this protein as GcnE (a Gcn5-related N-acetyltransferase) from Aspergillus flavus, or recognition of the specific GNAT-domain fold architecture in this sequence, which is required to select D over the other three enzyme classes.",
    "reason": "Selecting D requires recognizing this specific protein's identity or its GNAT-domain fold. A trained model might recall the sequence-to-function mapping, but that constitutes memorization of a database entry rather than reasoning from general biological principles. No general argument from amino-acid composition, length, or obvious motifs distinguishes a histone acetyltransferase from a DNA repair enzyme, ion transporter, or alcohol dehydrogenase in this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, D is the only one matching the experimentally validated primary catalytic activity of this protein. The alternative benzoyltransferase activity (benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)) is not offered as a choice, so no ambiguity exists among the listed options."
  },
  "important_caveats": [
    "The protein also has a documented benzoyltransferase activity (EC 2.3.1.-, PubMed:39601562), but this reaction is not among the choices, so it does not create ambiguity.",
    "The primary annotation of histone acetyltransferase activity carries evidence code ECO:0000250 (similarity to UniProtKB:Q03330, S. cerevisiae Gcn5) for the name, while the catalytic activity annotation itself is backed by experimental evidence (ECO:0000269, PubMed:39601562).",
    "The identity origin of the accession (A0A7U2QYM2) was inferred mechanically from dataset metadata and was absent from the evaluated model input; the model only saw the raw sequence.",
    "The entry was first publicly released in April 2025 and the supporting publication appeared in 2025; the author's source snapshot date is unknown, so the annotation may not have existed at the time of question construction."
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

**Accession:** `A0A7U2QYM2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.100326+00:00.  

```json
"A0A7U2QYM2"
```

Source SHA-256: `62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.100326+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39601562","source":"PubMed"}],"value":"Benzoyltransferase gcnE"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"value":"2.3.1.48"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q03330","source":"UniProtKB"}],"value":"Histone acetyltransferase gcnE"}}}
```

Source SHA-256: `62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.100326+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:45949"}}],"reaction":{"ecNumber":"2.3.1.48","evidences":[{"evidenceCode":"ECO:0000269","id":"39601562","source":"PubMed"}],"name":"L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:45948"},{"database":"Rhea","id":"RHEA-COMP:9752"},{"database":"Rhea","id":"RHEA-COMP:10731"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29969"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:61930"}]}}
```

Source SHA-256: `62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2QYM2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.100326+00:00.  

```json
{"citation":{"authors":["Chen X.","Wu L.","Zhang Y.","Wang S.","Wang S."],"citationCrossReferences":[{"database":"PubMed","id":"39601562"},{"database":"DOI","id":"10.1128/mbio.02665-24"}],"citationType":"journal article","firstPage":"e0266524","id":"39601562","journal":"MBio","lastPage":"e0266524","publicationDate":"2025","title":"Importance of benzoyltransferase GcnE and lysine benzoylation of alcohol dehydrogenase AdhB in pathogenesis and aflatoxin production in Aspergillus flavus.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","CATALYTIC ACTIVITY","DOMAIN","ACTIVE SITE","MUTAGENESIS OF GLU-139"]}
```

Source SHA-256: `62832be697e21c858f10966f2857a43e5cbc83ed896c702c9eaf6b22d957a2f7`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:27:33.661793+00:00.  

```text
ID   GCNE_ASPFN              Reviewed;         402 AA.
AC   A0A7U2QYM2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 21.
DE   RecName: Full=Histone acetyltransferase gcnE {ECO:0000250|UniProtKB:Q03330};
DE            EC=2.3.1.48 {ECO:0000269|PubMed:39601562};
DE   AltName: Full=Benzoyltransferase gcnE {ECO:0000303|PubMed:39601562};
DE            EC=2.3.1.- {ECO:0000269|PubMed:39601562};
GN   Name=gcnE {ECO:0000303|PubMed:39601562}; ORFNames=F9C07_11133;
OS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357
OS   / JCM 12722 / SRRC 167).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=332952;
```

Source SHA-256: `36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:27:33.661793+00:00.  

```text
DE   RecName: Full=Histone acetyltransferase gcnE {ECO:0000250|UniProtKB:Q03330};
DE            EC=2.3.1.48 {ECO:0000269|PubMed:39601562};
DE   AltName: Full=Benzoyltransferase gcnE {ECO:0000303|PubMed:39601562};
DE            EC=2.3.1.- {ECO:0000269|PubMed:39601562};
```

Source SHA-256: `36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2QYM2?format=txt&versions=21)  
**Locator:** `lines 43-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:27:33.661793+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein]
CC         + CoA + H(+); Xref=Rhea:RHEA:45948, Rhea:RHEA-COMP:9752, Rhea:RHEA-
CC         COMP:10731, ChEBI:CHEBI:15378, ChEBI:CHEBI:29969, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:61930; EC=2.3.1.48;
CC         Evidence={ECO:0000269|PubMed:39601562};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45949;
CC         Evidence={ECO:0000269|PubMed:39601562};
```

Source SHA-256: `36f550ae7bc08c06f607864032c4242543bb45af90f57f1b6319f8ebe893703c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
