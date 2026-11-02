# GO_cellular_component_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — endomembrane system

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHNTCTLQITRALLSRLHILFHSALVASVFYYRFSNFSSGPAWALMTFAELTLAFIWALTQAFRWRPVVRAVFGPEEIDPAQLPGLDVFICTADPRKEPVMEVMNSVVSALALDYPAEKLAVYLSDDGGSPLTREVIREAAVFGKYWVGFCGKYNVKTRCPEAYFSSFCDGERVDHNQDYLNDELSVKSKFEAFKKYVQKASEDATKCIVVNDRPSCVEIIHDSKQNGEGEVKMPLLVYVAREKRPGFNHHAKAGAINTLLRVSGLLSNSPFFLVLDCDMYCNDPTSARQAMCFHLDPKLAPSLAFVQYPQIFYNTSKNDIYDGQARAAFKTKYQGMDGLRGPVMSGTGYFLKRKALYGKPHDQDELLREQPTKAFGSSKIFIASLGENTCVALKGLSKDELLQETQKLAACTYESNTLWGSEVGYSYDCLLESTYCGYLLHCKGWISVYLYPKKPCFLGCATVDMNDAMLQIMKWTSGLIGVGISKFSPFTYAMSRISIMQSLCYAYFAFSGLFAVFFLIYGVVLPYSLLQGVPLFPKAGDPWLLAFAGVFISSLLQHLYEVLSSGETVKAWWNEQRIWIIKSITACLFGLLDAMLNKIGVLKASFRLTNKAVDKQKLDKYEKGRFDFQGAQMFMVPLMILVVFNLVSFFGGLRRTVIHKNYEDMFAQLFLSLFILALSYPIMEEIVRKARKGRS

[Multiple Choices]
A. host cytoskeleton
B. endomembrane system
C. chromatin
D. trans-Golgi network membrane
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

> The sequence-matched UniProt record annotates the protein to the Golgi apparatus membrane; Golgi is part of the endomembrane system, supporting B. The location annotation is curator-assigned, while the GO Golgi-membrane annotation is IEA rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The multiple hydrophobic regions support an integral membrane protein and make chromatin or cytoskeleton less plausible, but do not establish its specific membrane compartment.


**Missing item-specific fact**

> The protein-specific Golgi localization (and, to choose D over the broader B, evidence for trans-Golgi network localization) is not supplied in the question.


**Reason**

> Sequence architecture alone does not meaningfully distinguish endomembrane system from a particular Golgi subcompartment. Identifying the likely location depends on protein-specific annotation or evidence absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The choices differ in specificity: trans-Golgi network membrane is within the endomembrane system. If the protein were localized there, both descriptions could apply; the supplied sequence does not resolve that distinction.


### Important caveats

- The reviewer-only records match the supplied sequence, including a historical record available by the stated cutoff, but the author's exact source snapshot is unknown.
- The cited location annotation supports Golgi membrane broadly and does not establish trans-Golgi network membrane specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The multiple hydrophobic regions support an integral membrane protein and make chromatin or cytoskeleton less plausible, but do not establish its specific membrane compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific Golgi localization (and, to choose D over the broader B, evidence for trans-Golgi network localization) is not supplied in the question.",
    "reason": "Sequence architecture alone does not meaningfully distinguish endomembrane system from a particular Golgi subcompartment. Identifying the likely location depends on protein-specific annotation or evidence absent from the input."
  },
  "case_id": "GO_cellular_component_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the Golgi apparatus membrane; Golgi is part of the endomembrane system, supporting B. The location annotation is curator-assigned, while the GO Golgi-membrane annotation is IEA rather than direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, including a historical record available by the stated cutoff, but the author's exact source snapshot is unknown.",
    "The cited location annotation supports Golgi membrane broadly and does not establish trans-Golgi network membrane specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The choices differ in specificity: trans-Golgi network membrane is within the endomembrane system. If the protein were localized there, both descriptions could apply; the supplied sequence does not resolve that distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the Golgi apparatus membrane; Golgi is part of the endomembrane system, supporting B. The location annotation is curator-assigned, while the GO Golgi-membrane annotation is IEA rather than direct experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The multiple hydrophobic regions support an integral membrane protein and make chromatin or cytoskeleton less plausible, but do not establish its specific membrane compartment.",
    "missing_item_specific_fact": "The protein-specific Golgi localization (and, to choose D over the broader B, evidence for trans-Golgi network localization) is not supplied in the question.",
    "reason": "Sequence architecture alone does not meaningfully distinguish endomembrane system from a particular Golgi subcompartment. Identifying the likely location depends on protein-specific annotation or evidence absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The choices differ in specificity: trans-Golgi network membrane is within the endomembrane system. If the protein were localized there, both descriptions could apply; the supplied sequence does not resolve that distinction."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, including a historical record available by the stated cutoff, but the author's exact source snapshot is unknown.",
    "The cited location annotation supports Golgi membrane broadly and does not establish trans-Golgi network membrane specifically."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates this protein (A0AAW1HA02, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) as 'Golgi apparatus membrane; Multi-pass membrane protein' (ECO:0000305, curator inference). The GO ontology explicitly states GO:0005794 (Golgi apparatus) is part_of GO:0012505 (endomembrane system), and GO:0000139 (Golgi membrane) is part_of GO:0005794. Thus the annotated Golgi membrane location is a valid member of the endomembrane system. The annotation does not specify trans-Golgi network (GO:0032588), so option D is not supported. Options A (host cytoskeleton) and C (chromatin) are clearly inconsistent with a multi-pass membrane glycosyltransferase. The evidence code is IEA/curator-inferred rather than direct experimental, but the annotation is valid.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1), [GO3](#evidence-go3), [GO4](#evidence-go4), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic transmembrane segments (visible in the N-terminal region and throughout) indicating a multi-pass membrane protein, which eliminates A (host cytoskeleton) and C (chromatin). The central region contains a DxDxDGQRR-like motif characteristic of the Cellulose Synthase-Like (CSL) glycosyltransferase family, a well-known group of Golgi-localized membrane proteins involved in polysaccharide biosynthesis. CSL proteins function at the Golgi apparatus, not at the trans-Golgi network, which is primarily a sorting/trafficking compartment. Recognizing the CSL domain and its established Golgi localization supports selecting the endomembrane system (B) over the overly specific trans-Golgi network membrane (D). The general principle that a broad category is preferred over an overly specific sub-compartment absent specific targeting evidence also favors B over D.


**Missing item-specific fact**

> None critically missing. Distinguishing B from D relies on knowing that CSL/glycosyltransferase family proteins function at the Golgi for polysaccharide synthesis rather than at the trans-Golgi network for sorting—a matter of general domain biology rather than a protein-specific experimental measurement.


**Reason**

> The sequence provides recognizable CSL-domain features and multiple TM segments. General knowledge that CSL glycosyltransferases are Golgi-resident membrane proteins, combined with the principle that the trans-Golgi network is a sorting compartment not a biosynthetic one, allows a reasoned elimination of D in favor of B. This is a concrete biological argument from the sequence and domain context, not pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (host cytoskeleton) and C (chromatin) are clearly incompatible with a multi-pass membrane glycosyltransferase. Option D (trans-Golgi network membrane) is a specific sub-compartment of the endomembrane system, but CSL proteins are not characterized as TGN-localized; they function at the Golgi for polysaccharide assembly. The broader 'endomembrane system' (B) correctly encompasses the Golgi without overcommitting to the trans-Golgi network. No genuine ambiguity remains among the four choices.


### Important caveats

- The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator) and the GO term is IEA:UniProtKB-SubCell; no direct experimental localization (e.g., GFP tagging) is cited in the supplied evidence.
- The protein was first released in Swiss-Prot on 2025-06-18; the author's exact source snapshot is unknown, though the sequence matches both current and historical (entry v5) records.
- The GO annotation 'Golgi apparatus membrane' is more specific than the answer 'endomembrane system'; the benchmark question chose the broader parent term as the correct option, which is valid but less precise than the underlying annotation.
- Recognition of the CSL domain from raw sequence alone requires familiarity with the DxDxDGQRR motif region; a model lacking this knowledge might struggle to distinguish B from D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic transmembrane segments (visible in the N-terminal region and throughout) indicating a multi-pass membrane protein, which eliminates A (host cytoskeleton) and C (chromatin). The central region contains a DxDxDGQRR-like motif characteristic of the Cellulose Synthase-Like (CSL) glycosyltransferase family, a well-known group of Golgi-localized membrane proteins involved in polysaccharide biosynthesis. CSL proteins function at the Golgi apparatus, not at the trans-Golgi network, which is primarily a sorting/trafficking compartment. Recognizing the CSL domain and its established Golgi localization supports selecting the endomembrane system (B) over the overly specific trans-Golgi network membrane (D). The general principle that a broad category is preferred over an overly specific sub-compartment absent specific targeting evidence also favors B over D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically missing. Distinguishing B from D relies on knowing that CSL/glycosyltransferase family proteins function at the Golgi for polysaccharide synthesis rather than at the trans-Golgi network for sorting—a matter of general domain biology rather than a protein-specific experimental measurement.",
    "reason": "The sequence provides recognizable CSL-domain features and multiple TM segments. General knowledge that CSL glycosyltransferases are Golgi-resident membrane proteins, combined with the principle that the trans-Golgi network is a sorting compartment not a biosynthetic one, allows a reasoned elimination of D in favor of B. This is a concrete biological argument from the sequence and domain context, not pure lookup."
  },
  "case_id": "GO_cellular_component_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1",
      "GO3",
      "GO4",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates this protein (A0AAW1HA02, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) as 'Golgi apparatus membrane; Multi-pass membrane protein' (ECO:0000305, curator inference). The GO ontology explicitly states GO:0005794 (Golgi apparatus) is part_of GO:0012505 (endomembrane system), and GO:0000139 (Golgi membrane) is part_of GO:0005794. Thus the annotated Golgi membrane location is a valid member of the endomembrane system. The annotation does not specify trans-Golgi network (GO:0032588), so option D is not supported. Options A (host cytoskeleton) and C (chromatin) are clearly inconsistent with a multi-pass membrane glycosyltransferase. The evidence code is IEA/curator-inferred rather than direct experimental, but the annotation is valid."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator) and the GO term is IEA:UniProtKB-SubCell; no direct experimental localization (e.g., GFP tagging) is cited in the supplied evidence.",
    "The protein was first released in Swiss-Prot on 2025-06-18; the author's exact source snapshot is unknown, though the sequence matches both current and historical (entry v5) records.",
    "The GO annotation 'Golgi apparatus membrane' is more specific than the answer 'endomembrane system'; the benchmark question chose the broader parent term as the correct option, which is valid but less precise than the underlying annotation.",
    "Recognition of the CSL domain from raw sequence alone requires familiarity with the DxDxDGQRR motif region; a model lacking this knowledge might struggle to distinguish B from D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (host cytoskeleton) and C (chromatin) are clearly incompatible with a multi-pass membrane glycosyltransferase. Option D (trans-Golgi network membrane) is a specific sub-compartment of the endomembrane system, but CSL proteins are not characterized as TGN-localized; they function at the Golgi for polysaccharide assembly. The broader 'endomembrane system' (B) correctly encompasses the Golgi without overcommitting to the trans-Golgi network. No genuine ambiguity remains among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates this protein (A0AAW1HA02, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) as 'Golgi apparatus membrane; Multi-pass membrane protein' (ECO:0000305, curator inference). The GO ontology explicitly states GO:0005794 (Golgi apparatus) is part_of GO:0012505 (endomembrane system), and GO:0000139 (Golgi membrane) is part_of GO:0005794. Thus the annotated Golgi membrane location is a valid member of the endomembrane system. The annotation does not specify trans-Golgi network (GO:0032588), so option D is not supported. Options A (host cytoskeleton) and C (chromatin) are clearly inconsistent with a multi-pass membrane glycosyltransferase. The evidence code is IEA/curator-inferred rather than direct experimental, but the annotation is valid.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1", "GO3", "GO4", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic transmembrane segments (visible in the N-terminal region and throughout) indicating a multi-pass membrane protein, which eliminates A (host cytoskeleton) and C (chromatin). The central region contains a DxDxDGQRR-like motif characteristic of the Cellulose Synthase-Like (CSL) glycosyltransferase family, a well-known group of Golgi-localized membrane proteins involved in polysaccharide biosynthesis. CSL proteins function at the Golgi apparatus, not at the trans-Golgi network, which is primarily a sorting/trafficking compartment. Recognizing the CSL domain and its established Golgi localization supports selecting the endomembrane system (B) over the overly specific trans-Golgi network membrane (D). The general principle that a broad category is preferred over an overly specific sub-compartment absent specific targeting evidence also favors B over D.",
    "missing_item_specific_fact": "None critically missing. Distinguishing B from D relies on knowing that CSL/glycosyltransferase family proteins function at the Golgi for polysaccharide synthesis rather than at the trans-Golgi network for sorting—a matter of general domain biology rather than a protein-specific experimental measurement.",
    "reason": "The sequence provides recognizable CSL-domain features and multiple TM segments. General knowledge that CSL glycosyltransferases are Golgi-resident membrane proteins, combined with the principle that the trans-Golgi network is a sorting compartment not a biosynthetic one, allows a reasoned elimination of D in favor of B. This is a concrete biological argument from the sequence and domain context, not pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (host cytoskeleton) and C (chromatin) are clearly incompatible with a multi-pass membrane glycosyltransferase. Option D (trans-Golgi network membrane) is a specific sub-compartment of the endomembrane system, but CSL proteins are not characterized as TGN-localized; they function at the Golgi for polysaccharide assembly. The broader 'endomembrane system' (B) correctly encompasses the Golgi without overcommitting to the trans-Golgi network. No genuine ambiguity remains among the four choices."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator) and the GO term is IEA:UniProtKB-SubCell; no direct experimental localization (e.g., GFP tagging) is cited in the supplied evidence.",
    "The protein was first released in Swiss-Prot on 2025-06-18; the author's exact source snapshot is unknown, though the sequence matches both current and historical (entry v5) records.",
    "The GO annotation 'Golgi apparatus membrane' is more specific than the answer 'endomembrane system'; the benchmark question chose the broader parent term as the correct option, which is valid but less precise than the underlying annotation.",
    "Recognition of the CSL domain from raw sequence alone requires familiarity with the DxDxDGQRR motif region; a model lacking this knowledge might struggle to distinguish B from D."
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

**Accession:** `A0AAW1HA02` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0134","value":"Golgi apparatus membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"database":"GO","id":"GO:0000139","properties":[{"key":"GoTerm","value":"C:Golgi membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Golgi apparatus membrane {ECO:0000305}; Multi-
CC       pass membrane protein {ECO:0000255}.
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
DR   GO; GO:0000139; C:Golgi membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 1366-1374`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000139
name: Golgi membrane
namespace: cellular_component
def: "The lipid bilayer surrounding any of the compartments of the Golgi apparatus." [GOC:mah]
synonym: "Golgi apparatus membrane" EXACT []
is_a: GO:0098588 ! bounding membrane of organelle
relationship: part_of GO:0005794 ! Golgi apparatus

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59587-59612`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005794
name: Golgi apparatus
namespace: cellular_component
def: "A membrane-bound cytoplasmic organelle of the endomembrane system that further processes the core oligosaccharides (e.g. N-glycans) added to proteins in the endoplasmic reticulum and packages them into membrane-bound vesicles. The Golgi apparatus operates at the intersection of the secretory, lysosomal, and endocytic pathways." [ISBN:0198506732, PMID:9695800]
comment: Note that the Golgi apparatus can be located in various places in the cytoplasm. In plants and lower animal cells, the Golgi apparatus exists as many copies of discrete stacks dispersed throughout the cytoplasm, while the Golgi apparatus of interphase mammalian cells is a juxtanuclear, often pericentriolar reticulum, where the discrete Golgi stacks are stitched together to form a compact and interconnected ribbon, sometimes called the Golgi ribbon.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "Golgi" BROAD []
synonym: "Golgi complex" EXACT []
synonym: "Golgi ribbon" NARROW []
xref: NIF_Subcellular:sao451912436
xref: Wikipedia:Golgi_apparatus
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm
relationship: part_of GO:0012505 ! endomembrane system

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 111059-111069`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0012505
name: endomembrane system
namespace: cellular_component
def: "A collection of membranous structures involved in transport within the cell. The main components of the endomembrane system are endoplasmic reticulum, Golgi bodies, vesicles, cell membrane and nuclear envelope. Members of the endomembrane system pass materials through each other or though the use of vesicles." [GOC:lh]
subset: goslim_candida
subset: goslim_flybase_ribbon
subset: goslim_yeast
xref: Wikipedia:Endomembrane_system
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 187565-187574`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0032588
name: trans-Golgi network membrane
namespace: cellular_component
def: "The lipid bilayer surrounding any of the compartments that make up the trans-Golgi network." [GOC:mah]
synonym: "Golgi trans face membrane" RELATED []
synonym: "trans Golgi network membrane" EXACT []
is_a: GO:0031090 ! organelle membrane
relationship: part_of GO:0005802 ! trans-Golgi network

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
