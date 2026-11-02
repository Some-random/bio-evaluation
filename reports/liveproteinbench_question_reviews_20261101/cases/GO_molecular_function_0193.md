# GO_molecular_function_0193

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — ferrous iron binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLVRNSSRLLRSQLKRVQSVPVALYHENVVEHYENPRNVGSLDKKDVTVGTGLVGAPACGDVMKLQIKVDENGKIVDAKFKTFGCGSAIASSSLATEWVKGKSIDEAGKLKNTDIAKELRLPPVKLHCSMLAEDAIKAALADYKVKQQKKVAN

[Multiple Choices]
A. ferrous iron binding
B. methionine gamma-lyase activity
C. snRNA methyltransferase activity
D. 3-keto-5-aminohexanoate cleavage activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Drosophila IscU entry, which carries a ferrous iron binding GO annotation with IDA:FlyBase evidence. The entry also describes experimental support for its iron-sulfur cluster assembly function. The annotation supports choice A, although IscU's broader role is as an Fe-S cluster scaffold.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The cysteine-containing sequence is compatible with a metal/iron-sulfur-associated protein, but that clue does not establish this protein's specific ferrous-iron-binding activity.


**Missing item-specific fact**

> The sequence-to-protein identity and its experimentally supported ferrous iron binding annotation are absent from the prompt.


**Reason**

> Choosing A over the other listed functions requires identifying the particular protein or having protein-specific functional evidence; broad sequence-based metal-binding clues do not establish the precise GO activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports ferrous iron binding, and none of the other options is supported for this matched protein.


### Important caveats

- The UniProt identity and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The annotation supports ferrous iron binding, but the entry characterizes IscU more broadly as an Fe-S cluster assembly scaffold.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The cysteine-containing sequence is compatible with a metal/iron-sulfur-associated protein, but that clue does not establish this protein's specific ferrous-iron-binding activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-to-protein identity and its experimentally supported ferrous iron binding annotation are absent from the prompt.",
    "reason": "Choosing A over the other listed functions requires identifying the particular protein or having protein-specific functional evidence; broad sequence-based metal-binding clues do not establish the precise GO activity."
  },
  "case_id": "GO_molecular_function_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila IscU entry, which carries a ferrous iron binding GO annotation with IDA:FlyBase evidence. The entry also describes experimental support for its iron-sulfur cluster assembly function. The annotation supports choice A, although IscU's broader role is as an Fe-S cluster scaffold."
  },
  "important_caveats": [
    "The UniProt identity and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation supports ferrous iron binding, but the entry characterizes IscU more broadly as an Fe-S cluster assembly scaffold."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports ferrous iron binding, and none of the other options is supported for this matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila IscU entry, which carries a ferrous iron binding GO annotation with IDA:FlyBase evidence. The entry also describes experimental support for its iron-sulfur cluster assembly function. The annotation supports choice A, although IscU's broader role is as an Fe-S cluster scaffold.",
    "evidence_ids": ["C1", "C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The cysteine-containing sequence is compatible with a metal/iron-sulfur-associated protein, but that clue does not establish this protein's specific ferrous-iron-binding activity.",
    "missing_item_specific_fact": "The sequence-to-protein identity and its experimentally supported ferrous iron binding annotation are absent from the prompt.",
    "reason": "Choosing A over the other listed functions requires identifying the particular protein or having protein-specific functional evidence; broad sequence-based metal-binding clues do not establish the precise GO activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports ferrous iron binding, and none of the other options is supported for this matched protein."
  },
  "important_caveats": [
    "The UniProt identity and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation supports ferrous iron binding, but the entry characterizes IscU more broadly as an Fe-S cluster assembly scaffold."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9VHK6 (ISCU_DROME) carries GO:0008198 'ferrous iron binding' with evidence code IDA:FlyBase (Inferred from Direct Assay, PubMed:27738674), meaning the binding was experimentally demonstrated. The protein is annotated as an iron-sulfur cluster assembly scaffold (IscU), whose mechanism involves coordination of ferrous iron during de novo Fe-S cluster synthesis. The IDA evidence code provides experimental support for this specific GO term.

Citations as saved: [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [H4](#evidence-h4), [C9](#evidence-c9), [H2](#evidence-h2), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 154-aa sequence lacks PLP-binding motifs (ruling out methionine gamma-lyase, B), lacks the canonical Rossmann-fold methyltransferase catalytic residues and is too small for a typical snRNA methyltransferase (ruling out C), and lacks CoA-binding/acyltransferase motifs (ruling out D). The protein is a small scaffold-type protein containing cysteine residues (e.g., C72, C74, C106, C109) suggestive of metal coordination, and it is the only non-catalytic binding option among the four choices. General knowledge that scaffold proteins in Fe-S cluster biogenesis coordinate ferrous iron provides a defensible reasoning path to select A.


**Missing item-specific fact**

> The specific distinction between 'ferrous iron binding' and other iron-related GO terms (e.g., '2 iron, 2 sulfur cluster binding' or 'iron-sulfur cluster chaperone activity') annotated to IscU requires knowledge of the experimental characterization (PubMed:27738674). However, those alternative iron-related terms are not among the four choices, so the reasoning path is not blocked.


**Reason**

> The four choices span fundamentally different functional categories (one metal-binding, three unrelated catalytic activities). Eliminating B, C, and D through absence of characteristic enzyme motifs and identifying A as the only metal-binding option consistent with a small cysteine-containing scaffold protein constitutes a meaningful biological reasoning pathway. The positive confirmation of 'ferrous' (vs. ferric) specificity and the exclusion of other iron-related GO terms not listed as options adds a minor lookup component but does not prevent reasoning from distinguishing A from B/C/D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are functionally and structurally distinct (one binding activity, three unrelated enzyme catalytic activities). No two options describe overlapping or closely related functions. The only theoretical ambiguity would be between 'ferrous iron binding' and other iron-related GO terms, but those alternatives are not presented as choices.


### Important caveats

- The IDA evidence for GO:0008198 comes from in vitro characterization (PubMed:27738674, Dzul et al. 2017, Metallomics), demonstrating ferrous iron binding in the context of Fe-S cluster assembly.
- The protein also carries GO:0051537 (2 iron, 2 sulfur cluster binding, IBA) and GO:0140132 (iron-sulfur cluster chaperone activity, ISS), but these are not among the answer choices.
- The sequence contains a 'VGTGLVGAPACGDVMKLQ' region superficially resembling a P-loop/NAD-binding motif, which could mislead a model toward nucleotide-binding or methyltransferase functions; however, the overall context (small size, cysteine content, lack of catalytic residues) argues against those interpretations.
- The accession Q9VHK6 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 154-aa sequence lacks PLP-binding motifs (ruling out methionine gamma-lyase, B), lacks the canonical Rossmann-fold methyltransferase catalytic residues and is too small for a typical snRNA methyltransferase (ruling out C), and lacks CoA-binding/acyltransferase motifs (ruling out D). The protein is a small scaffold-type protein containing cysteine residues (e.g., C72, C74, C106, C109) suggestive of metal coordination, and it is the only non-catalytic binding option among the four choices. General knowledge that scaffold proteins in Fe-S cluster biogenesis coordinate ferrous iron provides a defensible reasoning path to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific distinction between 'ferrous iron binding' and other iron-related GO terms (e.g., '2 iron, 2 sulfur cluster binding' or 'iron-sulfur cluster chaperone activity') annotated to IscU requires knowledge of the experimental characterization (PubMed:27738674). However, those alternative iron-related terms are not among the four choices, so the reasoning path is not blocked.",
    "reason": "The four choices span fundamentally different functional categories (one metal-binding, three unrelated catalytic activities). Eliminating B, C, and D through absence of characteristic enzyme motifs and identifying A as the only metal-binding option consistent with a small cysteine-containing scaffold protein constitutes a meaningful biological reasoning pathway. The positive confirmation of 'ferrous' (vs. ferric) specificity and the exclusion of other iron-related GO terms not listed as options adds a minor lookup component but does not prevent reasoning from distinguishing A from B/C/D."
  },
  "case_id": "GO_molecular_function_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H6",
      "C5",
      "H4",
      "C9",
      "H2",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9VHK6 (ISCU_DROME) carries GO:0008198 'ferrous iron binding' with evidence code IDA:FlyBase (Inferred from Direct Assay, PubMed:27738674), meaning the binding was experimentally demonstrated. The protein is annotated as an iron-sulfur cluster assembly scaffold (IscU), whose mechanism involves coordination of ferrous iron during de novo Fe-S cluster synthesis. The IDA evidence code provides experimental support for this specific GO term."
  },
  "important_caveats": [
    "The IDA evidence for GO:0008198 comes from in vitro characterization (PubMed:27738674, Dzul et al. 2017, Metallomics), demonstrating ferrous iron binding in the context of Fe-S cluster assembly.",
    "The protein also carries GO:0051537 (2 iron, 2 sulfur cluster binding, IBA) and GO:0140132 (iron-sulfur cluster chaperone activity, ISS), but these are not among the answer choices.",
    "The sequence contains a 'VGTGLVGAPACGDVMKLQ' region superficially resembling a P-loop/NAD-binding motif, which could mislead a model toward nucleotide-binding or methyltransferase functions; however, the overall context (small size, cysteine content, lack of catalytic residues) argues against those interpretations.",
    "The accession Q9VHK6 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are functionally and structurally distinct (one binding activity, three unrelated enzyme catalytic activities). No two options describe overlapping or closely related functions. The only theoretical ambiguity would be between 'ferrous iron binding' and other iron-related GO terms, but those alternatives are not presented as choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9VHK6 (ISCU_DROME) carries GO:0008198 'ferrous iron binding' with evidence code IDA:FlyBase (Inferred from Direct Assay, PubMed:27738674), meaning the binding was experimentally demonstrated. The protein is annotated as an iron-sulfur cluster assembly scaffold (IscU), whose mechanism involves coordination of ferrous iron during de novo Fe-S cluster synthesis. The IDA evidence code provides experimental support for this specific GO term.",
    "evidence_ids": ["C7", "H6", "C5", "H4", "C9", "H2", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 154-aa sequence lacks PLP-binding motifs (ruling out methionine gamma-lyase, B), lacks the canonical Rossmann-fold methyltransferase catalytic residues and is too small for a typical snRNA methyltransferase (ruling out C), and lacks CoA-binding/acyltransferase motifs (ruling out D). The protein is a small scaffold-type protein containing cysteine residues (e.g., C72, C74, C106, C109) suggestive of metal coordination, and it is the only non-catalytic binding option among the four choices. General knowledge that scaffold proteins in Fe-S cluster biogenesis coordinate ferrous iron provides a defensible reasoning path to select A.",
    "missing_item_specific_fact": "The specific distinction between 'ferrous iron binding' and other iron-related GO terms (e.g., '2 iron, 2 sulfur cluster binding' or 'iron-sulfur cluster chaperone activity') annotated to IscU requires knowledge of the experimental characterization (PubMed:27738674). However, those alternative iron-related terms are not among the four choices, so the reasoning path is not blocked.",
    "reason": "The four choices span fundamentally different functional categories (one metal-binding, three unrelated catalytic activities). Eliminating B, C, and D through absence of characteristic enzyme motifs and identifying A as the only metal-binding option consistent with a small cysteine-containing scaffold protein constitutes a meaningful biological reasoning pathway. The positive confirmation of 'ferrous' (vs. ferric) specificity and the exclusion of other iron-related GO terms not listed as options adds a minor lookup component but does not prevent reasoning from distinguishing A from B/C/D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are functionally and structurally distinct (one binding activity, three unrelated enzyme catalytic activities). No two options describe overlapping or closely related functions. The only theoretical ambiguity would be between 'ferrous iron binding' and other iron-related GO terms, but those alternatives are not presented as choices."
  },
  "important_caveats": [
    "The IDA evidence for GO:0008198 comes from in vitro characterization (PubMed:27738674, Dzul et al. 2017, Metallomics), demonstrating ferrous iron binding in the context of Fe-S cluster assembly.",
    "The protein also carries GO:0051537 (2 iron, 2 sulfur cluster binding, IBA) and GO:0140132 (iron-sulfur cluster chaperone activity, ISS), but these are not among the answer choices.",
    "The sequence contains a 'VGTGLVGAPACGDVMKLQ' region superficially resembling a P-loop/NAD-binding motif, which could mislead a model toward nucleotide-binding or methyltransferase functions; however, the overall context (small size, cysteine content, lack of catalytic residues) argues against those interpretations.",
    "The accession Q9VHK6 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
"Q9VHK6"
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
**Locator:** `/uniProtKBCrossReferences/35`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"27738674","source":"PubMed"}],"id":"GO:0008198","properties":[{"key":"GoTerm","value":"F:ferrous iron binding"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"citation":{"authors":["Dzul S.P.","Rocha A.G.","Rawat S.","Kandegedara A.","Kusowski A.","Pain J.","Murari A.","Pain D.","Dancis A.","Stemmler T.L."],"citationCrossReferences":[{"database":"PubMed","id":"27738674"},{"database":"DOI","id":"10.1039/c6mt00163g"}],"citationType":"journal article","firstPage":"48","id":"27738674","journal":"Metallomics","lastPage":"60","publicationDate":"2017","title":"In vitro characterization of a novel Isu homologue from Drosophila melanogaster for de novo FeS-cluster formation.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","COFACTOR","PATHWAY"]}
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
**Locator:** `lines 163-163`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
DR   GO; GO:0008198; F:ferrous iron binding; IDA:FlyBase.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80595-80602`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008198
name: ferrous iron binding
namespace: molecular_function
def: "Binding to a ferrous iron ion, Fe(II)." [GOC:ai]
xref: Reactome:R-HSA-1362416 "Frataxin binds iron"
is_a: GO:0005506 ! iron ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 193. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
