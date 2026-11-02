# GO_biological_process_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — &#91;2Fe-2S&#93; cluster assembly

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLVRNSSRLLRSQLKRVQSVPVALYHENVVEHYENPRNVGSLDKKDVTVGTGLVGAPACGDVMKLQIKVDENGKIVDAKFKTFGCGSAIASSSLATEWVKGKSIDEAGKLKNTDIAKELRLPPVKLHCSMLAEDAIKAALADYKVKQQKKVAN

[Multiple Choices]
A. [2Fe-2S] cluster assembly
B. cobalt ion transport
C. regulation of oligodendrocyte progenitor proliferation
D. tetrahydrofolate interconversion
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as an iron-sulfur cluster assembly scaffold, with a GO annotation specifically for &#91;2Fe-2S&#93; cluster assembly carrying IDA:FlyBase evidence. The cited functional annotations also describe experimental evidence for de novo Fe-S cluster formation.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence has the size and conserved cysteine-containing pattern characteristic of an IscU-like Fe-S cluster scaffold. That family-level inference points to iron-sulfur cluster assembly, unlike the transport, oligodendrocyte regulation, or folate-process choices.


**Missing item-specific fact**

> No particular database accession or experimental measurement is necessary to make this family-level distinction, though the exact GO annotation and experimental support are external facts.


**Reason**

> A recognizable protein-family signature and its general biochemical role provide meaningful grounds for selecting A; this is more than merely recalling the exact sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct processes, and the sequence's inferred IscU-like role supports A. Its broader role in assembly of both &#91;2Fe-2S&#93; and &#91;4Fe-4S&#93; clusters does not make another listed option defensible.


### Important caveats

- The sequence-family inference is not itself experimental evidence; reviewer-only annotations supply sequence-matched functional support.
- The source also describes a broader role in Fe-S cluster maturation, including &#91;4Fe-4S&#93; proteins, rather than an exclusive role in &#91;2Fe-2S&#93; assembly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence has the size and conserved cysteine-containing pattern characteristic of an IscU-like Fe-S cluster scaffold. That family-level inference points to iron-sulfur cluster assembly, unlike the transport, oligodendrocyte regulation, or folate-process choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No particular database accession or experimental measurement is necessary to make this family-level distinction, though the exact GO annotation and experimental support are external facts.",
    "reason": "A recognizable protein-family signature and its general biochemical role provide meaningful grounds for selecting A; this is more than merely recalling the exact sequence's database entry."
  },
  "case_id": "GO_biological_process_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an iron-sulfur cluster assembly scaffold, with a GO annotation specifically for [2Fe-2S] cluster assembly carrying IDA:FlyBase evidence. The cited functional annotations also describe experimental evidence for de novo Fe-S cluster formation."
  },
  "important_caveats": [
    "The sequence-family inference is not itself experimental evidence; reviewer-only annotations supply sequence-matched functional support.",
    "The source also describes a broader role in Fe-S cluster maturation, including [4Fe-4S] proteins, rather than an exclusive role in [2Fe-2S] assembly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct processes, and the sequence's inferred IscU-like role supports A. Its broader role in assembly of both [2Fe-2S] and [4Fe-4S] clusters does not make another listed option defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an iron-sulfur cluster assembly scaffold, with a GO annotation specifically for [2Fe-2S] cluster assembly carrying IDA:FlyBase evidence. The cited functional annotations also describe experimental evidence for de novo Fe-S cluster formation.",
    "evidence_ids": ["C5", "C7", "H4", "H6", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence has the size and conserved cysteine-containing pattern characteristic of an IscU-like Fe-S cluster scaffold. That family-level inference points to iron-sulfur cluster assembly, unlike the transport, oligodendrocyte regulation, or folate-process choices.",
    "missing_item_specific_fact": "No particular database accession or experimental measurement is necessary to make this family-level distinction, though the exact GO annotation and experimental support are external facts.",
    "reason": "A recognizable protein-family signature and its general biochemical role provide meaningful grounds for selecting A; this is more than merely recalling the exact sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct processes, and the sequence's inferred IscU-like role supports A. Its broader role in assembly of both [2Fe-2S] and [4Fe-4S] clusters does not make another listed option defensible."
  },
  "important_caveats": [
    "The sequence-family inference is not itself experimental evidence; reviewer-only annotations supply sequence-matched functional support.",
    "The source also describes a broader role in Fe-S cluster maturation, including [4Fe-4S] proteins, rather than an exclusive role in [2Fe-2S] assembly."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Drosophila melanogaster IscU (Q9VHK6), a scaffold protein for de novo Fe-S cluster synthesis. UniProt carries GO:0044571 (&#91;2Fe-2S&#93; cluster assembly) with IDA:FlyBase evidence backed by PubMed:27738674 (in vitro FeS-cluster formation characterization) and PubMed:29491838 (ISC assembly complex component). The GO term definition matches the option text exactly. Experimental evidence (direct assay) supports the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10), [C11](#evidence-c11), [GO3](#evidence-go3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 154-residue sequence lacks transmembrane helices (ruling out cobalt ion transport, B), lacks NADPH-binding or folate-metabolism catalytic domains (ruling out tetrahydrofolate interconversion, D), and is a small soluble protein incompatible with a vertebrate neurodevelopmental regulatory role (ruling out oligodendrocyte progenitor regulation, C). The N-terminal region (MSLVRNSSRLLRSQLKR) is consistent with a mitochondrial targeting signal, and the multiple cysteine residues (e.g., in GAPACGDVMKLQ, TFGCGSA, LHCSMLAEDAIK) are characteristic of Fe-S cluster scaffold proteins. Among the four options, only &#91;2Fe-2S&#93; cluster assembly (A) is compatible with a small, cysteine-rich, mitochondrially-targeted soluble protein.


**Missing item-specific fact**

> The specific designation &#91;2Fe-2S&#93; (rather than general iron-sulfur cluster assembly or &#91;4Fe-4S&#93;) is supported by IDA experimental evidence; from sequence alone, IscU handles both cluster types. However, among the given options, A is the only Fe-S-related choice, so the distinction is not required to select correctly.


**Reason**

> Elimination of B, C, and D relies on general structural/functional knowledge (absence of TM domains, absence of folate-enzyme motifs, organismal context). Positive identification of A is supported by mitochondrial targeting signal features and cysteine-rich scaffold-like architecture, making this a defensible reasoning path rather than pure memorization of the IscU entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with the sequence features (no TM domains, no folate-enzyme domains, vertebrate-specific regulatory process). Only A is compatible with a small cysteine-rich mitochondrial protein. The specific &#91;2Fe-2S&#93; vs &#91;4Fe-4S&#93; distinction is not relevant here since no &#91;4Fe-4S&#93; option is offered.


### Important caveats

- The organism (Drosophila melanogaster) is not stated in the question; elimination of option C partially relies on inferring the organism from sequence features or general knowledge.
- The GO annotation GO:0044571 is supported by IDA (direct assay) evidence, making it experimentally grounded rather than purely computational.
- The protein IscU actually assembles both &#91;2Fe-2S&#93; and &#91;4Fe-4S&#93; clusters; the &#91;2Fe-2S&#93; specificity in the GO term reflects the particular experimental assay used.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9VHK6.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 154-residue sequence lacks transmembrane helices (ruling out cobalt ion transport, B), lacks NADPH-binding or folate-metabolism catalytic domains (ruling out tetrahydrofolate interconversion, D), and is a small soluble protein incompatible with a vertebrate neurodevelopmental regulatory role (ruling out oligodendrocyte progenitor regulation, C). The N-terminal region (MSLVRNSSRLLRSQLKR) is consistent with a mitochondrial targeting signal, and the multiple cysteine residues (e.g., in GAPACGDVMKLQ, TFGCGSA, LHCSMLAEDAIK) are characteristic of Fe-S cluster scaffold proteins. Among the four options, only [2Fe-2S] cluster assembly (A) is compatible with a small, cysteine-rich, mitochondrially-targeted soluble protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific designation [2Fe-2S] (rather than general iron-sulfur cluster assembly or [4Fe-4S]) is supported by IDA experimental evidence; from sequence alone, IscU handles both cluster types. However, among the given options, A is the only Fe-S-related choice, so the distinction is not required to select correctly.",
    "reason": "Elimination of B, C, and D relies on general structural/functional knowledge (absence of TM domains, absence of folate-enzyme motifs, organismal context). Positive identification of A is supported by mitochondrial targeting signal features and cysteine-rich scaffold-like architecture, making this a defensible reasoning path rather than pure memorization of the IscU entry."
  },
  "case_id": "GO_biological_process_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C10",
      "C11",
      "GO3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster IscU (Q9VHK6), a scaffold protein for de novo Fe-S cluster synthesis. UniProt carries GO:0044571 ([2Fe-2S] cluster assembly) with IDA:FlyBase evidence backed by PubMed:27738674 (in vitro FeS-cluster formation characterization) and PubMed:29491838 (ISC assembly complex component). The GO term definition matches the option text exactly. Experimental evidence (direct assay) supports the annotation."
  },
  "important_caveats": [
    "The organism (Drosophila melanogaster) is not stated in the question; elimination of option C partially relies on inferring the organism from sequence features or general knowledge.",
    "The GO annotation GO:0044571 is supported by IDA (direct assay) evidence, making it experimentally grounded rather than purely computational.",
    "The protein IscU actually assembles both [2Fe-2S] and [4Fe-4S] clusters; the [2Fe-2S] specificity in the GO term reflects the particular experimental assay used.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9VHK6."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence features (no TM domains, no folate-enzyme domains, vertebrate-specific regulatory process). Only A is compatible with a small cysteine-rich mitochondrial protein. The specific [2Fe-2S] vs [4Fe-4S] distinction is not relevant here since no [4Fe-4S] option is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster IscU (Q9VHK6), a scaffold protein for de novo Fe-S cluster synthesis. UniProt carries GO:0044571 ([2Fe-2S] cluster assembly) with IDA:FlyBase evidence backed by PubMed:27738674 (in vitro FeS-cluster formation characterization) and PubMed:29491838 (ISC assembly complex component). The GO term definition matches the option text exactly. Experimental evidence (direct assay) supports the annotation.",
    "evidence_ids": ["C4", "C5", "C7", "C10", "C11", "GO3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 154-residue sequence lacks transmembrane helices (ruling out cobalt ion transport, B), lacks NADPH-binding or folate-metabolism catalytic domains (ruling out tetrahydrofolate interconversion, D), and is a small soluble protein incompatible with a vertebrate neurodevelopmental regulatory role (ruling out oligodendrocyte progenitor regulation, C). The N-terminal region (MSLVRNSSRLLRSQLKR) is consistent with a mitochondrial targeting signal, and the multiple cysteine residues (e.g., in GAPACGDVMKLQ, TFGCGSA, LHCSMLAEDAIK) are characteristic of Fe-S cluster scaffold proteins. Among the four options, only [2Fe-2S] cluster assembly (A) is compatible with a small, cysteine-rich, mitochondrially-targeted soluble protein.",
    "missing_item_specific_fact": "The specific designation [2Fe-2S] (rather than general iron-sulfur cluster assembly or [4Fe-4S]) is supported by IDA experimental evidence; from sequence alone, IscU handles both cluster types. However, among the given options, A is the only Fe-S-related choice, so the distinction is not required to select correctly.",
    "reason": "Elimination of B, C, and D relies on general structural/functional knowledge (absence of TM domains, absence of folate-enzyme motifs, organismal context). Positive identification of A is supported by mitochondrial targeting signal features and cysteine-rich scaffold-like architecture, making this a defensible reasoning path rather than pure memorization of the IscU entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence features (no TM domains, no folate-enzyme domains, vertebrate-specific regulatory process). Only A is compatible with a small cysteine-rich mitochondrial protein. The specific [2Fe-2S] vs [4Fe-4S] distinction is not relevant here since no [4Fe-4S] option is offered."
  },
  "important_caveats": [
    "The organism (Drosophila melanogaster) is not stated in the question; elimination of option C partially relies on inferring the organism from sequence features or general knowledge.",
    "The GO annotation GO:0044571 is supported by IDA (direct assay) evidence, making it experimentally grounded rather than purely computational.",
    "The protein IscU actually assembles both [2Fe-2S] and [4Fe-4S] clusters; the [2Fe-2S] specificity in the GO term reflects the particular experimental assay used.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q9VHK6."
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

**Accession:** `Q9VHK6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 196. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0037637","source":"FlyBase"}],"value":"Iron-sulfur cluster assembly enzyme IscU"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27738674","source":"PubMed"}],"value":"fIscU"}]}}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27738674","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29491838","source":"PubMed"}],"value":"Scaffold protein for the de novo synthesis of iron-sulfur (Fe-S) clusters within mitochondria, which is required for maturation of both mitochondrial and cytoplasmic [2Fe-2S] and [4Fe-4S] proteins (PubMed:27738674). Component of the mitochondrial core iron-sulfur cluster (ISC) assembly complex; regulates its activity (PubMed:29491838)"}]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"27738674","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"29491838","source":"PubMed"}],"id":"GO:0044571","properties":[{"key":"GoTerm","value":"P:[2Fe-2S] cluster assembly"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"citation":{"authors":["Dzul S.P.","Rocha A.G.","Rawat S.","Kandegedara A.","Kusowski A.","Pain J.","Murari A.","Pain D.","Dancis A.","Stemmler T.L."],"citationCrossReferences":[{"database":"PubMed","id":"27738674"},{"database":"DOI","id":"10.1039/c6mt00163g"}],"citationType":"journal article","firstPage":"48","id":"27738674","journal":"Metallomics","lastPage":"60","publicationDate":"2017","title":"In vitro characterization of a novel Isu homologue from Drosophila melanogaster for de novo FeS-cluster formation.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","COFACTOR","PATHWAY"]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"citation":{"authors":["Marelja Z.","Leimkuehler S.","Missirlis F."],"citationCrossReferences":[{"database":"PubMed","id":"29491838"},{"database":"DOI","id":"10.3389/fphys.2018.00050"}],"citationType":"journal article","firstPage":"50","id":"29491838","journal":"Front. Physiol.","lastPage":"50","publicationDate":"2018","title":"Iron Sulfur and Molybdenum Cofactor Enzymes Regulate the Drosophila Life Cycle by Controlling Cell Metabolism.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":6,"referencePositions":["FUNCTION","INTERACTION WITH NFS1; BCN92 AND FH"]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 85-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, COFACTOR, AND PATHWAY.
RX   PubMed=27738674; DOI=10.1039/c6mt00163g;
RA   Dzul S.P., Rocha A.G., Rawat S., Kandegedara A., Kusowski A., Pain J.,
RA   Murari A., Pain D., Dancis A., Stemmler T.L.;
RT   "In vitro characterization of a novel Isu homologue from Drosophila
RT   melanogaster for de novo FeS-cluster formation.";
RL   Metallomics 9:48-60(2017).
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 100-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
CC   -!- FUNCTION: Scaffold protein for the de novo synthesis of iron-sulfur
CC       (Fe-S) clusters within mitochondria, which is required for maturation
CC       of both mitochondrial and cytoplasmic [2Fe-2S] and [4Fe-4S] proteins
CC       (PubMed:27738674). Component of the mitochondrial core iron-sulfur
CC       cluster (ISC) assembly complex; regulates its activity
CC       (PubMed:29491838). {ECO:0000269|PubMed:27738674,
CC       ECO:0000269|PubMed:29491838}.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 165-165`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
DR   GO; GO:0044571; P:[2Fe-2S] cluster assembly; IDA:FlyBase.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 258499-258507`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044571
name: [2Fe-2S] cluster assembly
namespace: biological_process
def: "The incorporation of two iron atoms and two sulfur atoms into an iron-sulfur cluster." [GOC:jl, GOC:mengo_curators, GOC:pde, GOC:tt, GOC:vw, PMID:15952888]
synonym: "2Fe-2S cluster assembly" EXACT []
synonym: "[2Fe-2S] cluster biosynthetic process" RELATED []
is_a: GO:0016226 ! iron-sulfur cluster assembly

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
