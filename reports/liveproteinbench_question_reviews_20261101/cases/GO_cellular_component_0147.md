# GO_cellular_component_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — virus tail, tube

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTVIQDTADVYFKRKSDGKLVFTAEAQTASFSQAISEEKLRGGIGNKPLYILKSEKEINLTVKNAFFDLEWLAMTQGETIQEETKVKVFDREHGLIVDDTNKVTLKGKPVSDVTFYNKKGLTYKIAVSTDGTYTIPTAFAAAKDKLTAVYQIEKVGRRLAIKASKFSERYEVEYRTIAYNPDTEEVYSDIYIQFPNVSPSGEFEMSLENGNALAPEIKFEALADTDTDEMAVVIEASRDENTAAPVEDTTGSTQSSDLGGTTE

[Multiple Choices]
A. virus tail, tube
B. actin cytoskeleton
C. host cell plasma membrane
D. microvillus membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt record named “Tail tube protein,” with a GO annotation to “virus tail, tube.” The GO annotation is IEA:UniProtKB-KW, so this supports the key as a database annotation, not as a demonstrated experimental localization. The archived record also annotates subcellular location as virion.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices contrast a viral structural component with host-cell structures, but the supplied sequence and prompt provide no clear viral identity or specific tail-tube signal that meaningfully establishes which applies.


**Missing item-specific fact**

> That this exact sequence is the tail tube protein of Bacillus phage SPR, along with its associated GO annotation.


**Reason**

> Selecting A depends on the protein-specific identification or annotation; recognizing the sequence from an external record would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation specifically supports A; the other choices describe host-cell structures and are not supported by the supplied sequence.


### Important caveats

- The sequence match is exact in both the current and retrieved historical UniProt records.
- The GO term is annotated with an IEA evidence code; the record’s virion localization annotation is not presented here as experimental evidence.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices contrast a viral structural component with host-cell structures, but the supplied sequence and prompt provide no clear viral identity or specific tail-tube signal that meaningfully establishes which applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact sequence is the tail tube protein of Bacillus phage SPR, along with its associated GO annotation.",
    "reason": "Selecting A depends on the protein-specific identification or annotation; recognizing the sequence from an external record would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record named “Tail tube protein,” with a GO annotation to “virus tail, tube.” The GO annotation is IEA:UniProtKB-KW, so this supports the key as a database annotation, not as a demonstrated experimental localization. The archived record also annotates subcellular location as virion."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and retrieved historical UniProt records.",
    "The GO term is annotated with an IEA evidence code; the record’s virion localization annotation is not presented here as experimental evidence.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifically supports A; the other choices describe host-cell structures and are not supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record named “Tail tube protein,” with a GO annotation to “virus tail, tube.” The GO annotation is IEA:UniProtKB-KW, so this supports the key as a database annotation, not as a demonstrated experimental localization. The archived record also annotates subcellular location as virion.",
    "evidence_ids": ["H1", "H2", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices contrast a viral structural component with host-cell structures, but the supplied sequence and prompt provide no clear viral identity or specific tail-tube signal that meaningfully establishes which applies.",
    "missing_item_specific_fact": "That this exact sequence is the tail tube protein of Bacillus phage SPR, along with its associated GO annotation.",
    "reason": "Selecting A depends on the protein-specific identification or annotation; recognizing the sequence from an external record would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation specifically supports A; the other choices describe host-cell structures and are not supported by the supplied sequence."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and retrieved historical UniProt records.",
    "The GO term is annotated with an IEA evidence code; the record’s virion localization annotation is not presented here as experimental evidence.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (264 AA) matches UniProtKB A0AAE9G628 exactly (SHA256 confirmed). The entry is a reviewed Swiss-Prot record named 'Tail tube protein' from Bacillus phage SPR (C4, H1). The subcellular location is annotated as 'Virion' (C5, H2), and GO:0098026 'virus tail, tube' is directly assigned (C6, H3) with evidence code IEA:UniProtKB-KW. The protein name, organism (bacteriophage), and GO annotation all consistently support option A. The IEA evidence code indicates computational inference from keyword rather than direct experimental localization, but the protein is explicitly named 'Tail tube protein' and belongs to a Caudoviricetes phage, making the annotation highly reliable.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could eliminate options B, C, and D by noting the absence of transmembrane domains or signal peptides (ruling out host cell plasma membrane and microvillus membrane) and the absence of actin-like sequence motifs or actin-binding domains (ruling out actin cytoskeleton). However, this elimination only narrows to 'the remaining viral option' without positively identifying the protein as specifically a tail tube protein versus other viral structural proteins (capsid, tail fiber, baseplate). The sequence lacks distinctive features that would allow a general reasoner to positively identify 'tail tube' architecture.


**Missing item-specific fact**

> The specific identity of this 264-residue sequence as the Bacillus phage SPR tail tube protein (UniProt A0AAE9G628, ORF spr_64). Without database lookup or memorization of this particular phage genome annotation, a model cannot positively assign the protein to the 'virus tail, tube' compartment rather than other possible viral structural roles. The sequence itself does not contain a recognizable 'tail tube' motif distinguishable from other phage structural proteins.


**Reason**

> While elimination of the three eukaryotic/host-cell options is feasible through general biological knowledge (no membrane domains, no actin motifs), the positive identification of 'tail tube' specifically requires knowing this exact protein's annotation. The answer is reachable by elimination only because 'virus tail, tube' is the sole viral option among the four choices; if other viral compartments were offered, elimination would fail. The core identification depends on recognizing this specific sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with the sequence: no transmembrane helices or signal peptide (excludes C and D), and no resemblance to actin or actin-associated proteins (excludes B). Option A is the only remaining choice and is consistent with the protein being a small, soluble viral structural protein. No ambiguity among the given options.


### Important caveats

- The GO annotation evidence code is IEA:UniProtKB-KW (inferred from electronic annotation based on keyword), not direct experimental evidence. However, the protein is explicitly named 'Tail tube protein' in a reviewed Swiss-Prot entry, providing strong support.
- The sequence is from a bacteriophage (Bacillus phage SPR), not a eukaryotic host protein, which is not obvious from sequence features alone without database knowledge.
- The elimination-based reasoning path works only because 'virus tail, tube' is the single viral option among four choices; this is a structural artifact of the question design rather than a feature of the protein sequence itself.
- The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could eliminate options B, C, and D by noting the absence of transmembrane domains or signal peptides (ruling out host cell plasma membrane and microvillus membrane) and the absence of actin-like sequence motifs or actin-binding domains (ruling out actin cytoskeleton). However, this elimination only narrows to 'the remaining viral option' without positively identifying the protein as specifically a tail tube protein versus other viral structural proteins (capsid, tail fiber, baseplate). The sequence lacks distinctive features that would allow a general reasoner to positively identify 'tail tube' architecture.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this 264-residue sequence as the Bacillus phage SPR tail tube protein (UniProt A0AAE9G628, ORF spr_64). Without database lookup or memorization of this particular phage genome annotation, a model cannot positively assign the protein to the 'virus tail, tube' compartment rather than other possible viral structural roles. The sequence itself does not contain a recognizable 'tail tube' motif distinguishable from other phage structural proteins.",
    "reason": "While elimination of the three eukaryotic/host-cell options is feasible through general biological knowledge (no membrane domains, no actin motifs), the positive identification of 'tail tube' specifically requires knowing this exact protein's annotation. The answer is reachable by elimination only because 'virus tail, tube' is the sole viral option among the four choices; if other viral compartments were offered, elimination would fail. The core identification depends on recognizing this specific sequence's database entry."
  },
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence (264 AA) matches UniProtKB A0AAE9G628 exactly (SHA256 confirmed). The entry is a reviewed Swiss-Prot record named 'Tail tube protein' from Bacillus phage SPR (C4, H1). The subcellular location is annotated as 'Virion' (C5, H2), and GO:0098026 'virus tail, tube' is directly assigned (C6, H3) with evidence code IEA:UniProtKB-KW. The protein name, organism (bacteriophage), and GO annotation all consistently support option A. The IEA evidence code indicates computational inference from keyword rather than direct experimental localization, but the protein is explicitly named 'Tail tube protein' and belongs to a Caudoviricetes phage, making the annotation highly reliable."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:UniProtKB-KW (inferred from electronic annotation based on keyword), not direct experimental evidence. However, the protein is explicitly named 'Tail tube protein' in a reviewed Swiss-Prot entry, providing strong support.",
    "The sequence is from a bacteriophage (Bacillus phage SPR), not a eukaryotic host protein, which is not obvious from sequence features alone without database knowledge.",
    "The elimination-based reasoning path works only because 'virus tail, tube' is the single viral option among four choices; this is a structural artifact of the question design rather than a feature of the protein sequence itself.",
    "The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence: no transmembrane helices or signal peptide (excludes C and D), and no resemblance to actin or actin-associated proteins (excludes B). Option A is the only remaining choice and is consistent with the protein being a small, soluble viral structural protein. No ambiguity among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (264 AA) matches UniProtKB A0AAE9G628 exactly (SHA256 confirmed). The entry is a reviewed Swiss-Prot record named 'Tail tube protein' from Bacillus phage SPR (C4, H1). The subcellular location is annotated as 'Virion' (C5, H2), and GO:0098026 'virus tail, tube' is directly assigned (C6, H3) with evidence code IEA:UniProtKB-KW. The protein name, organism (bacteriophage), and GO annotation all consistently support option A. The IEA evidence code indicates computational inference from keyword rather than direct experimental localization, but the protein is explicitly named 'Tail tube protein' and belongs to a Caudoviricetes phage, making the annotation highly reliable.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could eliminate options B, C, and D by noting the absence of transmembrane domains or signal peptides (ruling out host cell plasma membrane and microvillus membrane) and the absence of actin-like sequence motifs or actin-binding domains (ruling out actin cytoskeleton). However, this elimination only narrows to 'the remaining viral option' without positively identifying the protein as specifically a tail tube protein versus other viral structural proteins (capsid, tail fiber, baseplate). The sequence lacks distinctive features that would allow a general reasoner to positively identify 'tail tube' architecture.",
    "missing_item_specific_fact": "The specific identity of this 264-residue sequence as the Bacillus phage SPR tail tube protein (UniProt A0AAE9G628, ORF spr_64). Without database lookup or memorization of this particular phage genome annotation, a model cannot positively assign the protein to the 'virus tail, tube' compartment rather than other possible viral structural roles. The sequence itself does not contain a recognizable 'tail tube' motif distinguishable from other phage structural proteins.",
    "reason": "While elimination of the three eukaryotic/host-cell options is feasible through general biological knowledge (no membrane domains, no actin motifs), the positive identification of 'tail tube' specifically requires knowing this exact protein's annotation. The answer is reachable by elimination only because 'virus tail, tube' is the sole viral option among the four choices; if other viral compartments were offered, elimination would fail. The core identification depends on recognizing this specific sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with the sequence: no transmembrane helices or signal peptide (excludes C and D), and no resemblance to actin or actin-associated proteins (excludes B). Option A is the only remaining choice and is consistent with the protein being a small, soluble viral structural protein. No ambiguity among the given options."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:UniProtKB-KW (inferred from electronic annotation based on keyword), not direct experimental evidence. However, the protein is explicitly named 'Tail tube protein' in a reviewed Swiss-Prot entry, providing strong support.",
    "The sequence is from a bacteriophage (Bacillus phage SPR), not a eukaryotic host protein, which is not obvious from sequence features alone without database knowledge.",
    "The elimination-based reasoning path works only because 'virus tail, tube' is the single viral option among four choices; this is a structural artifact of the question design rather than a feature of the protein sequence itself.",
    "The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
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

**Accession:** `A0AAE9G628` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 7. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:26.141304+00:00.  

```json
"A0AAE9G628"
```

Source SHA-256: `4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:26.141304+00:00.  

```json
{"commonName":"Bacteriophage SPR","lineage":["Viruses","Duplodnaviria","Heunggongvirae","Uroviricota","Caudoviricetes","Caudoviricetes incertae sedis","Spbetavirus"],"scientificName":"Bacillus phage SPR","taxonId":10725}
```

Source SHA-256: `4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:26.141304+00:00.  

```json
{"recommendedName":{"fullName":{"value":"Tail tube protein"}}}
```

Source SHA-256: `4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:26.141304+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0274","value":"Virion"}}]}
```

Source SHA-256: `4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAE9G628.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:26.141304+00:00.  

```json
{"database":"GO","id":"GO:0098026","properties":[{"key":"GoTerm","value":"C:virus tail, tube"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-KW"}]}
```

Source SHA-256: `4475df5f43a35856bdc9052cbc30827ee69fe8a43237be8ce3c790d160dd3264`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:26:28.241173+00:00.  

```text
ID   TUBE_BPSPR              Reviewed;         264 AA.
AC   A0AAE9G628;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2024, sequence version 1.
DT   28-JAN-2026, entry version 7.
DE   RecName: Full=Tail tube protein;
GN   ORFNames=spr_64 {ECO:0000312|EMBL:UNY48585.1};
OS   Bacillus phage SPR (Bacteriophage SPR).
OC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes;
OC   Spbetavirus.
OX   NCBI_TaxID=10725 {ECO:0000312|EMBL:UNY48585.1, ECO:0000312|Proteomes:UP000831086};
OH   NCBI_TaxID=1423; Bacillus subtilis.
```

Source SHA-256: `26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)  
**Locator:** `lines 79-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:26:28.241173+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000305}.
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAE9G628?format=txt&versions=7)  
**Locator:** `lines 114-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:26:28.241173+00:00.  

```text
DR   GO; GO:0098026; C:virus tail, tube; IEA:UniProtKB-KW.
```

Source SHA-256: `26705b5d417d3c322399eae942edabb8ae0ff902980f43d35c91029f8fb74650`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 408367-408377`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098026
name: virus tail, tube
namespace: cellular_component
def: "The internal tube of the tail of some viruses. The virus tail tube is the channel for DNA ejection into the host cytoplasm." [PMID:33188213, VZ:3960]
comment: Applies in particular the Myoviridae bacteriophages. Many bacteriophages with dsDNA genomes, or Caudovirales, have a tail. The viral tail can be short (Podoviridae), long and non-contractile (Siphoviridae) or long and contractile (Myoviridae). The tail is the channel through which the phage genome is injected into the host bacterial cell.
synonym: "bacteriophage tail tube" NARROW [GOC:bm]
xref: VZ:3960 "Viral tail tube protein"
is_a: GO:0044423 ! virion component
relationship: part_of GO:0098015 ! virus tail

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
