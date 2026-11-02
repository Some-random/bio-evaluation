# GO_molecular_function_0162

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — zinc ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKNMSSRLLNMKFMQRASASTPTTPTTPDGTRPSKRLRTEAAPSPETRAFQEAAAAEEAKKNAFIERAAAEAGETKWVLSVSDDKPKTAGQGLRIVEAGYGAIDSGAPIPESDDDQDEEQSAGMAGRRSFGKFNKAVERQHNPDLSSPESEQDSDASSDSDSDDDEDLDEAELLIKAERKEAAAKLRAERKAQRKADEVKSKQMAERRRSRDINLNKVGGISNAAIRNKQANVANMACHVCGQKGHLQKDCPDRKQRRGDKRKSGGAMDY

[Multiple Choices]
A. double-stranded DNA binding
B. zinc ion binding
C. nucleoside diphosphate kinase activity
D. histone deacetylase activity
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

> The exact sequence matches the annotated GAL1 zinc-finger protein, and the matched record assigns zinc ion binding. This support is primarily annotation-based: the zinc-binding GO annotation is computational (IEA), not direct experimental evidence of zinc binding.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The Cys/His-rich segment near the C-terminus is consistent with a metal-coordinating zinc-finger-like motif, supporting zinc ion binding; the sequence does not show an evident catalytic signature for either enzyme option.


**Missing item-specific fact**

> No item-specific fact is essential for favoring zinc binding, though confirming the precise domain and its activity would require annotation or experimental evidence.


**Reason**

> The sequence provides a meaningful motif-based argument for B. DNA binding may also be plausible for a zinc-finger-like protein, but double-stranded DNA binding is not established by sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the strongest choice from the metal-coordinating motif. A is a plausible related function, but the supplied sequence does not specifically establish double-stranded DNA binding.


### Important caveats

- The matched UniProt record describes GAL1 as a transcription factor with an experimentally supported regulatory role, but that does not by itself establish direct zinc binding.
- The zinc ion binding GO annotation is computationally assigned; it should not be presented as direct experimental measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Cys/His-rich segment near the C-terminus is consistent with a metal-coordinating zinc-finger-like motif, supporting zinc ion binding; the sequence does not show an evident catalytic signature for either enzyme option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is essential for favoring zinc binding, though confirming the precise domain and its activity would require annotation or experimental evidence.",
    "reason": "The sequence provides a meaningful motif-based argument for B. DNA binding may also be plausible for a zinc-finger-like protein, but double-stranded DNA binding is not established by sequence alone."
  },
  "case_id": "GO_molecular_function_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated GAL1 zinc-finger protein, and the matched record assigns zinc ion binding. This support is primarily annotation-based: the zinc-binding GO annotation is computational (IEA), not direct experimental evidence of zinc binding."
  },
  "important_caveats": [
    "The matched UniProt record describes GAL1 as a transcription factor with an experimentally supported regulatory role, but that does not by itself establish direct zinc binding.",
    "The zinc ion binding GO annotation is computationally assigned; it should not be presented as direct experimental measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the strongest choice from the metal-coordinating motif. A is a plausible related function, but the supplied sequence does not specifically establish double-stranded DNA binding."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated GAL1 zinc-finger protein, and the matched record assigns zinc ion binding. This support is primarily annotation-based: the zinc-binding GO annotation is computational (IEA), not direct experimental evidence of zinc binding.",
    "evidence_ids": ["C1", "C4", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The Cys/His-rich segment near the C-terminus is consistent with a metal-coordinating zinc-finger-like motif, supporting zinc ion binding; the sequence does not show an evident catalytic signature for either enzyme option.",
    "missing_item_specific_fact": "No item-specific fact is essential for favoring zinc binding, though confirming the precise domain and its activity would require annotation or experimental evidence.",
    "reason": "The sequence provides a meaningful motif-based argument for B. DNA binding may also be plausible for a zinc-finger-like protein, but double-stranded DNA binding is not established by sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the strongest choice from the metal-coordinating motif. A is a plausible related function, but the supplied sequence does not specifically establish double-stranded DNA binding."
  },
  "important_caveats": [
    "The matched UniProt record describes GAL1 as a transcription factor with an experimentally supported regulatory role, but that does not by itself establish direct zinc binding.",
    "The zinc ion binding GO annotation is computationally assigned; it should not be presented as direct experimental measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A385XIL0, GAL1_AURME) explicitly annotates GO:0008270 (zinc ion binding) with IEA evidence (InterPro/UniProtKB-KW). The protein's alternative name is 'Zinc finger protein GAL1.' The C-terminal region contains a Cys/His cluster (MACHVCGQKGHLQKDC) consistent with a zinc-coordinating motif. The annotation is IEA (inferred from electronic annotation), not experimental, but it is consistent with the observable sequence features. The experimental evidence (ECO:0000269, PubMed:32003433) supports the transcription factor role, not zinc binding directly, but the sequence-level zinc finger motif and keyword-based annotation are coherent.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C4](#evidence-c4), [H1](#evidence-h1), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region 'MACHVCGQKGHLQKDC' contains a Cys/His cluster (C-x2-C…H…C pattern) characteristic of a zinc-coordinating motif, which directly maps to zinc ion binding. Options C (nucleoside diphosphate kinase) and D (histone deacetylase) can be confidently excluded: the sequence lacks the NDK active-site His (e.g., the conserved His117/His118 in the NDP kinase fold) and lacks HDAC catalytic motifs (e.g., the conserved His-Asp-His/His-Asp-His-His zinc-dependent HDAC catalytic triad or the NAD+-binding Rossmann fold of sirtuins). Between A and B, the zinc finger motif is the most directly observable and unambiguous molecular feature in the sequence, making zinc ion binding the most sequence-justifiable answer.


**Missing item-specific fact**

> None strictly required. The Cys/His cluster is present in the supplied sequence. However, the motif spacing is not a textbook-perfect C2H2 zinc finger (C-x2-C-x12-H-x3-H), which may reduce confidence in purely sequence-based identification without database corroboration.


**Reason**

> A model with general knowledge of zinc-coordinating motifs can identify the Cys/His cluster and select zinc ion binding. The other three options lack any supporting catalytic or structural motifs in the sequence. The reasoning path from sequence feature to GO term is concrete, though the imperfect motif spacing introduces some uncertainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> The protein is a transcription factor (annotated in UniProt with GO:0003676 nucleic acid binding, IEA:InterPro). Zinc finger transcription factors bind double-stranded DNA, making option A (double-stranded DNA binding, GO:0003690) biologically plausible. However, the specific GO term 'double-stranded DNA binding' is NOT annotated in the UniProt entry; only the broader 'nucleic acid binding' is. The sequence contains a basic/coiled-coil region (EAAAKLRAERKAQRKADEVKSKQMAERRRSR) suggestive of DNA interaction, but this alone does not uniquely specify dsDNA binding. The zinc finger motif is the more directly identifiable sequence feature, giving B a stronger sequence-level justification, but a model reasoning from 'transcription factor → DNA binding' could defensibly select A.


### Important caveats

- The zinc ion binding annotation carries IEA evidence code (inferred from electronic annotation via InterPro/UniProtKB-KW), not experimental evidence. The experimental evidence (ECO:0000269) pertains to the transcription factor function, not zinc coordination specifically.
- The Cys/His cluster in the C-terminal region does not perfectly match the canonical C2H2 zinc finger spacing (C-x2-C-x12-H-x3-H); it more closely resembles a C2HC or atypical variant, which may reduce confidence in purely sequence-based motif recognition.
- The UniProt entry was first released in 2025 (Swiss-Prot integration Feb 2025); the benchmark author's source snapshot date is unknown, and the accession was inferred from dataset metadata rather than provided in the model input.
- Option A (dsDNA binding) is not annotated in the UniProt entry but is biologically consistent with the protein's role as a zinc finger transcription factor, creating mild ambiguity with the expected answer B.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region 'MACHVCGQKGHLQKDC' contains a Cys/His cluster (C-x2-C…H…C pattern) characteristic of a zinc-coordinating motif, which directly maps to zinc ion binding. Options C (nucleoside diphosphate kinase) and D (histone deacetylase) can be confidently excluded: the sequence lacks the NDK active-site His (e.g., the conserved His117/His118 in the NDP kinase fold) and lacks HDAC catalytic motifs (e.g., the conserved His-Asp-His/His-Asp-His-His zinc-dependent HDAC catalytic triad or the NAD+-binding Rossmann fold of sirtuins). Between A and B, the zinc finger motif is the most directly observable and unambiguous molecular feature in the sequence, making zinc ion binding the most sequence-justifiable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The Cys/His cluster is present in the supplied sequence. However, the motif spacing is not a textbook-perfect C2H2 zinc finger (C-x2-C-x12-H-x3-H), which may reduce confidence in purely sequence-based identification without database corroboration.",
    "reason": "A model with general knowledge of zinc-coordinating motifs can identify the Cys/His cluster and select zinc ion binding. The other three options lack any supporting catalytic or structural motifs in the sequence. The reasoning path from sequence feature to GO term is concrete, though the imperfect motif spacing introduces some uncertainty."
  },
  "case_id": "GO_molecular_function_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C4",
      "H1",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A385XIL0, GAL1_AURME) explicitly annotates GO:0008270 (zinc ion binding) with IEA evidence (InterPro/UniProtKB-KW). The protein's alternative name is 'Zinc finger protein GAL1.' The C-terminal region contains a Cys/His cluster (MACHVCGQKGHLQKDC) consistent with a zinc-coordinating motif. The annotation is IEA (inferred from electronic annotation), not experimental, but it is consistent with the observable sequence features. The experimental evidence (ECO:0000269, PubMed:32003433) supports the transcription factor role, not zinc binding directly, but the sequence-level zinc finger motif and keyword-based annotation are coherent."
  },
  "important_caveats": [
    "The zinc ion binding annotation carries IEA evidence code (inferred from electronic annotation via InterPro/UniProtKB-KW), not experimental evidence. The experimental evidence (ECO:0000269) pertains to the transcription factor function, not zinc coordination specifically.",
    "The Cys/His cluster in the C-terminal region does not perfectly match the canonical C2H2 zinc finger spacing (C-x2-C-x12-H-x3-H); it more closely resembles a C2HC or atypical variant, which may reduce confidence in purely sequence-based motif recognition.",
    "The UniProt entry was first released in 2025 (Swiss-Prot integration Feb 2025); the benchmark author's source snapshot date is unknown, and the accession was inferred from dataset metadata rather than provided in the model input.",
    "Option A (dsDNA binding) is not annotated in the UniProt entry but is biologically consistent with the protein's role as a zinc finger transcription factor, creating mild ambiguity with the expected answer B."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "The protein is a transcription factor (annotated in UniProt with GO:0003676 nucleic acid binding, IEA:InterPro). Zinc finger transcription factors bind double-stranded DNA, making option A (double-stranded DNA binding, GO:0003690) biologically plausible. However, the specific GO term 'double-stranded DNA binding' is NOT annotated in the UniProt entry; only the broader 'nucleic acid binding' is. The sequence contains a basic/coiled-coil region (EAAAKLRAERKAQRKADEVKSKQMAERRRSR) suggestive of DNA interaction, but this alone does not uniquely specify dsDNA binding. The zinc finger motif is the more directly identifiable sequence feature, giving B a stronger sequence-level justification, but a model reasoning from 'transcription factor → DNA binding' could defensibly select A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A385XIL0, GAL1_AURME) explicitly annotates GO:0008270 (zinc ion binding) with IEA evidence (InterPro/UniProtKB-KW). The protein's alternative name is 'Zinc finger protein GAL1.' The C-terminal region contains a Cys/His cluster (MACHVCGQKGHLQKDC) consistent with a zinc-coordinating motif. The annotation is IEA (inferred from electronic annotation), not experimental, but it is consistent with the observable sequence features. The experimental evidence (ECO:0000269, PubMed:32003433) supports the transcription factor role, not zinc binding directly, but the sequence-level zinc finger motif and keyword-based annotation are coherent.",
    "evidence_ids": ["C7", "H5", "C4", "H1", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region 'MACHVCGQKGHLQKDC' contains a Cys/His cluster (C-x2-C…H…C pattern) characteristic of a zinc-coordinating motif, which directly maps to zinc ion binding. Options C (nucleoside diphosphate kinase) and D (histone deacetylase) can be confidently excluded: the sequence lacks the NDK active-site His (e.g., the conserved His117/His118 in the NDP kinase fold) and lacks HDAC catalytic motifs (e.g., the conserved His-Asp-His/His-Asp-His-His zinc-dependent HDAC catalytic triad or the NAD+-binding Rossmann fold of sirtuins). Between A and B, the zinc finger motif is the most directly observable and unambiguous molecular feature in the sequence, making zinc ion binding the most sequence-justifiable answer.",
    "missing_item_specific_fact": "None strictly required. The Cys/His cluster is present in the supplied sequence. However, the motif spacing is not a textbook-perfect C2H2 zinc finger (C-x2-C-x12-H-x3-H), which may reduce confidence in purely sequence-based identification without database corroboration.",
    "reason": "A model with general knowledge of zinc-coordinating motifs can identify the Cys/His cluster and select zinc ion binding. The other three options lack any supporting catalytic or structural motifs in the sequence. The reasoning path from sequence feature to GO term is concrete, though the imperfect motif spacing introduces some uncertainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "The protein is a transcription factor (annotated in UniProt with GO:0003676 nucleic acid binding, IEA:InterPro). Zinc finger transcription factors bind double-stranded DNA, making option A (double-stranded DNA binding, GO:0003690) biologically plausible. However, the specific GO term 'double-stranded DNA binding' is NOT annotated in the UniProt entry; only the broader 'nucleic acid binding' is. The sequence contains a basic/coiled-coil region (EAAAKLRAERKAQRKADEVKSKQMAERRRSR) suggestive of DNA interaction, but this alone does not uniquely specify dsDNA binding. The zinc finger motif is the more directly identifiable sequence feature, giving B a stronger sequence-level justification, but a model reasoning from 'transcription factor → DNA binding' could defensibly select A."
  },
  "important_caveats": [
    "The zinc ion binding annotation carries IEA evidence code (inferred from electronic annotation via InterPro/UniProtKB-KW), not experimental evidence. The experimental evidence (ECO:0000269) pertains to the transcription factor function, not zinc coordination specifically.",
    "The Cys/His cluster in the C-terminal region does not perfectly match the canonical C2H2 zinc finger spacing (C-x2-C-x12-H-x3-H); it more closely resembles a C2HC or atypical variant, which may reduce confidence in purely sequence-based motif recognition.",
    "The UniProt entry was first released in 2025 (Swiss-Prot integration Feb 2025); the benchmark author's source snapshot date is unknown, and the accession was inferred from dataset metadata rather than provided in the model input.",
    "Option A (dsDNA binding) is not annotated in the UniProt entry but is biologically consistent with the protein's role as a zinc finger transcription factor, creating mild ambiguity with the expected answer B."
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

**Accession:** `A0A385XIL0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XIL0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.136441+00:00.  

```json
"A0A385XIL0"
```

Source SHA-256: `ca6eee4ffe3fa92f59117a0d03edf21fc41a47539051acda5f65874d795a659a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XIL0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.136441+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Liamocins biosynthesis cluster protein GAL1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Zinc finger protein GAL1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Transcription factor GAL1"}}}
```

Source SHA-256: `ca6eee4ffe3fa92f59117a0d03edf21fc41a47539051acda5f65874d795a659a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XIL0.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.136441+00:00.  

```json
{"database":"GO","id":"GO:0008270","properties":[{"key":"GoTerm","value":"F:zinc ion binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ca6eee4ffe3fa92f59117a0d03edf21fc41a47539051acda5f65874d795a659a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XIL0?format=txt&versions=12)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-01T06:27:28.489076+00:00.  

```text
ID   GAL1_AURME              Reviewed;         272 AA.
AC   A0A385XIL0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-DEC-2018, sequence version 1.
DT   18-JUN-2025, entry version 12.
DE   RecName: Full=Transcription factor GAL1 {ECO:0000303|PubMed:32003433};
DE   AltName: Full=Liamocins biosynthesis cluster protein GAL1 {ECO:0000303|PubMed:32003433};
DE   AltName: Full=Zinc finger protein GAL1 {ECO:0000303|PubMed:32003433};
GN   Name=GAL1 {ECO:0000303|PubMed:32003433};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `fba47c0fa327c6555b960296d04774305f4a11c7edac1370036b1faa20057f55`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XIL0?format=txt&versions=12)  
**Locator:** `lines 87-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-01T06:27:28.489076+00:00.  

```text
DR   GO; GO:0008270; F:zinc ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `fba47c0fa327c6555b960296d04774305f4a11c7edac1370036b1faa20057f55`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 81431-81439`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008270
name: zinc ion binding
namespace: molecular_function
def: "Binding to a zinc ion (Zn)." [GOC:ai]
synonym: "zinc binding" EXACT []
synonym: "Zn binding" EXACT []
is_a: GO:0046914 ! transition metal ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
