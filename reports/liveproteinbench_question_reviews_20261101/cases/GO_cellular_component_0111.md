# GO_cellular_component_0111

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cytoplasm

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
A. replisome
B. RISC-loading complex
C. cytoplasm
D. T=4 icosahedral viral capsid
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

> The exact sequence match has a cytoplasm GO annotation (IBA), as well as annotations for the mitochondrial matrix (ISS) and mitochondrial &#91;2Fe-2S&#93; assembly complex (IDA). Under the supplied GO relationships, the mitochondrial annotations are compatible with the broader cytoplasm term. The evidence supports C, though it does not make cytoplasm the most specific location.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is enriched in basic and hydrophobic residues and lacks acidic residues across the likely targeting segment, consistent with a mitochondrial targeting peptide. That favors a mitochondrial protein over a replisome component, RISC-loading component, or viral capsid protein. Of the choices, cytoplasm is the broad GO location compatible with mitochondria.


**Missing item-specific fact**

> The protein-specific mitochondrial localization and its curated GO annotations would be needed to establish the more precise location, but are not required to distinguish the offered choices under the broad GO interpretation of cytoplasm.


**Reason**

> A plausible targeting signal provides biological grounds to favor a mitochondrial context, and the GO definition/relationship makes the broad cytoplasm choice compatible with that context. This inference is not as specific as the reviewer-only annotations.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the only offered choice compatible with the supported mitochondrial location under the broad GO interpretation. However, if 'cytoplasm' is read narrowly as cytosol excluding organelles, none of the choices gives the more specific mitochondrial location.


### Important caveats

- The cytoplasm annotation is IBA (computationally inferred), while the mitochondrial complex annotation is IDA and the matrix annotation is ISS; these evidence types should not be conflated.
- The exact historical author snapshot is unknown, although a sequence-matched archived entry before the stated cutoff contains these annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is enriched in basic and hydrophobic residues and lacks acidic residues across the likely targeting segment, consistent with a mitochondrial targeting peptide. That favors a mitochondrial protein over a replisome component, RISC-loading component, or viral capsid protein. Of the choices, cytoplasm is the broad GO location compatible with mitochondria.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The protein-specific mitochondrial localization and its curated GO annotations would be needed to establish the more precise location, but are not required to distinguish the offered choices under the broad GO interpretation of cytoplasm.",
    "reason": "A plausible targeting signal provides biological grounds to favor a mitochondrial context, and the GO definition/relationship makes the broad cytoplasm choice compatible with that context. This inference is not as specific as the reviewer-only annotations."
  },
  "case_id": "GO_cellular_component_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "GO1",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a cytoplasm GO annotation (IBA), as well as annotations for the mitochondrial matrix (ISS) and mitochondrial [2Fe-2S] assembly complex (IDA). Under the supplied GO relationships, the mitochondrial annotations are compatible with the broader cytoplasm term. The evidence supports C, though it does not make cytoplasm the most specific location."
  },
  "important_caveats": [
    "The cytoplasm annotation is IBA (computationally inferred), while the mitochondrial complex annotation is IDA and the matrix annotation is ISS; these evidence types should not be conflated.",
    "The exact historical author snapshot is unknown, although a sequence-matched archived entry before the stated cutoff contains these annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only offered choice compatible with the supported mitochondrial location under the broad GO interpretation. However, if 'cytoplasm' is read narrowly as cytosol excluding organelles, none of the choices gives the more specific mitochondrial location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a cytoplasm GO annotation (IBA), as well as annotations for the mitochondrial matrix (ISS) and mitochondrial [2Fe-2S] assembly complex (IDA). Under the supplied GO relationships, the mitochondrial annotations are compatible with the broader cytoplasm term. The evidence supports C, though it does not make cytoplasm the most specific location.",
    "evidence_ids": ["H3", "H4", "H5", "GO1", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is enriched in basic and hydrophobic residues and lacks acidic residues across the likely targeting segment, consistent with a mitochondrial targeting peptide. That favors a mitochondrial protein over a replisome component, RISC-loading component, or viral capsid protein. Of the choices, cytoplasm is the broad GO location compatible with mitochondria.",
    "missing_item_specific_fact": "The protein-specific mitochondrial localization and its curated GO annotations would be needed to establish the more precise location, but are not required to distinguish the offered choices under the broad GO interpretation of cytoplasm.",
    "reason": "A plausible targeting signal provides biological grounds to favor a mitochondrial context, and the GO definition/relationship makes the broad cytoplasm choice compatible with that context. This inference is not as specific as the reviewer-only annotations."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only offered choice compatible with the supported mitochondrial location under the broad GO interpretation. However, if 'cytoplasm' is read narrowly as cytosol excluding organelles, none of the choices gives the more specific mitochondrial location."
  },
  "important_caveats": [
    "The cytoplasm annotation is IBA (computationally inferred), while the mitochondrial complex annotation is IDA and the matrix annotation is ISS; these evidence types should not be conflated.",
    "The exact historical author snapshot is unknown, although a sequence-matched archived entry before the stated cutoff contains these annotations."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is IscU (Q9VHK6), an iron-sulfur cluster assembly enzyme from Drosophila melanogaster. The UniProt entry carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). More importantly, the primary experimental annotation (IDA:FlyBase) places it in the mitochondrial &#91;2Fe-2S&#93; assembly complex (GO:0099128), which is part_of GO:1990229 (iron-sulfur cluster assembly complex), which is part_of GO:0005737 (cytoplasm) per the GO ontology. Thus cytoplasm is technically supported as an encompassing location. However, the most specific and experimentally direct annotation is mitochondrial matrix (ISS) and mitochondrial assembly complex (IDA), neither of which appears among the answer choices. Among the four provided options, cytoplasm is the only defensible answer; the other three (replisome, RISC-loading complex, T=4 viral capsid) are clearly incompatible with a small Fe-S cluster assembly enzyme.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO7](#evidence-go7), [GO8](#evidence-go8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 154-residue sequence encodes a small enzyme with a Rossmann-like nucleotide-binding fold (GLVGAPACGDVMKLQ, GCGSAIASSSLATEWV motifs). Replisome components (A) are large multi-domain DNA polymerases, helicases, or primases with specific catalytic and DNA-binding motifs absent here. RISC-loading complex components (B) are large RNA-processing proteins (Dicer ~2000 aa, Ago2 ~900 aa) with PIWI/PAZ RNA-binding domains, incompatible with this small sequence. A T=4 icosahedral viral capsid protein (D) would exhibit characteristic β-barrel or jelly-roll folding motifs and self-assembly interfaces not suggested by this sequence. By elimination, the remaining option is cytoplasm (C), the default compartment for a small soluble metabolic enzyme lacking obvious organelle-targeting signals.


**Missing item-specific fact**

> The sequence does not contain a canonical N-terminal mitochondrial targeting presequence (positively charged amphipathic helix), so a model cannot positively infer mitochondrial matrix localization from the sequence alone. The true primary experimental location (mitochondrial matrix, IDA evidence) is not among the choices, so the question is answerable by elimination but the 'correct' answer is a broad GO ancestor rather than the most specific location.


**Reason**

> General biological knowledge about the size, domain architecture, and function of replisome, RISC, and viral capsid proteins allows a model to eliminate A, B, and D, leaving C as the default. This constitutes a concrete elimination argument from the sequence and choices. The positive identification of 'cytoplasm' over 'mitochondrial matrix' is not achievable from the sequence, but since mitochondrial matrix is not an option, the elimination pathway is sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly incompatible with a 154-aa small metabolic enzyme. Only C is remotely plausible. No ambiguity among the provided choices, though the question is somewhat misleading because the protein's most specific experimentally determined location (mitochondrial matrix) is absent from the options, forcing selection of the broad GO ancestor 'cytoplasm.'


### Important caveats

- The primary experimental evidence (IDA:FlyBase, PMID:29491838) places this protein in the mitochondrial &#91;2Fe-2S&#93; assembly complex, not the general cytoplasm. The cytoplasm annotation is IBA:GO_Central (propagated from biological ancestors), not direct experimental evidence for this specific protein.
- In the GO ontology, mitochondrion is part_of cytoplasm, so annotating a mitochondrial protein as 'cytoplasm' is technically valid but biologically imprecise. In common usage, 'cytoplasm' often implies the cytosol excluding organelles.
- The sequence lacks a canonical mitochondrial targeting presequence, making mitochondrial localization not inferable from the sequence alone. The Drosophila IscU may use a non-canonical import mechanism.
- The question asks for the 'primary' cellular component, which by IDA evidence is the mitochondrial assembly complex. Choosing 'cytoplasm' is defensible only because the more specific answer is unavailable among the options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 154-residue sequence encodes a small enzyme with a Rossmann-like nucleotide-binding fold (GLVGAPACGDVMKLQ, GCGSAIASSSLATEWV motifs). Replisome components (A) are large multi-domain DNA polymerases, helicases, or primases with specific catalytic and DNA-binding motifs absent here. RISC-loading complex components (B) are large RNA-processing proteins (Dicer ~2000 aa, Ago2 ~900 aa) with PIWI/PAZ RNA-binding domains, incompatible with this small sequence. A T=4 icosahedral viral capsid protein (D) would exhibit characteristic β-barrel or jelly-roll folding motifs and self-assembly interfaces not suggested by this sequence. By elimination, the remaining option is cytoplasm (C), the default compartment for a small soluble metabolic enzyme lacking obvious organelle-targeting signals.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence does not contain a canonical N-terminal mitochondrial targeting presequence (positively charged amphipathic helix), so a model cannot positively infer mitochondrial matrix localization from the sequence alone. The true primary experimental location (mitochondrial matrix, IDA evidence) is not among the choices, so the question is answerable by elimination but the 'correct' answer is a broad GO ancestor rather than the most specific location.",
    "reason": "General biological knowledge about the size, domain architecture, and function of replisome, RISC, and viral capsid proteins allows a model to eliminate A, B, and D, leaving C as the default. This constitutes a concrete elimination argument from the sequence and choices. The positive identification of 'cytoplasm' over 'mitochondrial matrix' is not achievable from the sequence, but since mitochondrial matrix is not an option, the elimination pathway is sufficient."
  },
  "case_id": "GO_cellular_component_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5",
      "GO1",
      "GO2",
      "GO3",
      "GO7",
      "GO8"
    ],
    "judgment": "supported",
    "reason": "The protein is IscU (Q9VHK6), an iron-sulfur cluster assembly enzyme from Drosophila melanogaster. The UniProt entry carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). More importantly, the primary experimental annotation (IDA:FlyBase) places it in the mitochondrial [2Fe-2S] assembly complex (GO:0099128), which is part_of GO:1990229 (iron-sulfur cluster assembly complex), which is part_of GO:0005737 (cytoplasm) per the GO ontology. Thus cytoplasm is technically supported as an encompassing location. However, the most specific and experimentally direct annotation is mitochondrial matrix (ISS) and mitochondrial assembly complex (IDA), neither of which appears among the answer choices. Among the four provided options, cytoplasm is the only defensible answer; the other three (replisome, RISC-loading complex, T=4 viral capsid) are clearly incompatible with a small Fe-S cluster assembly enzyme."
  },
  "important_caveats": [
    "The primary experimental evidence (IDA:FlyBase, PMID:29491838) places this protein in the mitochondrial [2Fe-2S] assembly complex, not the general cytoplasm. The cytoplasm annotation is IBA:GO_Central (propagated from biological ancestors), not direct experimental evidence for this specific protein.",
    "In the GO ontology, mitochondrion is part_of cytoplasm, so annotating a mitochondrial protein as 'cytoplasm' is technically valid but biologically imprecise. In common usage, 'cytoplasm' often implies the cytosol excluding organelles.",
    "The sequence lacks a canonical mitochondrial targeting presequence, making mitochondrial localization not inferable from the sequence alone. The Drosophila IscU may use a non-canonical import mechanism.",
    "The question asks for the 'primary' cellular component, which by IDA evidence is the mitochondrial assembly complex. Choosing 'cytoplasm' is defensible only because the more specific answer is unavailable among the options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a 154-aa small metabolic enzyme. Only C is remotely plausible. No ambiguity among the provided choices, though the question is somewhat misleading because the protein's most specific experimentally determined location (mitochondrial matrix) is absent from the options, forcing selection of the broad GO ancestor 'cytoplasm.'"
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is IscU (Q9VHK6), an iron-sulfur cluster assembly enzyme from Drosophila melanogaster. The UniProt entry carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). More importantly, the primary experimental annotation (IDA:FlyBase) places it in the mitochondrial [2Fe-2S] assembly complex (GO:0099128), which is part_of GO:1990229 (iron-sulfur cluster assembly complex), which is part_of GO:0005737 (cytoplasm) per the GO ontology. Thus cytoplasm is technically supported as an encompassing location. However, the most specific and experimentally direct annotation is mitochondrial matrix (ISS) and mitochondrial assembly complex (IDA), neither of which appears among the answer choices. Among the four provided options, cytoplasm is the only defensible answer; the other three (replisome, RISC-loading complex, T=4 viral capsid) are clearly incompatible with a small Fe-S cluster assembly enzyme.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H5", "GO1", "GO2", "GO3", "GO7", "GO8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 154-residue sequence encodes a small enzyme with a Rossmann-like nucleotide-binding fold (GLVGAPACGDVMKLQ, GCGSAIASSSLATEWV motifs). Replisome components (A) are large multi-domain DNA polymerases, helicases, or primases with specific catalytic and DNA-binding motifs absent here. RISC-loading complex components (B) are large RNA-processing proteins (Dicer ~2000 aa, Ago2 ~900 aa) with PIWI/PAZ RNA-binding domains, incompatible with this small sequence. A T=4 icosahedral viral capsid protein (D) would exhibit characteristic β-barrel or jelly-roll folding motifs and self-assembly interfaces not suggested by this sequence. By elimination, the remaining option is cytoplasm (C), the default compartment for a small soluble metabolic enzyme lacking obvious organelle-targeting signals.",
    "missing_item_specific_fact": "The sequence does not contain a canonical N-terminal mitochondrial targeting presequence (positively charged amphipathic helix), so a model cannot positively infer mitochondrial matrix localization from the sequence alone. The true primary experimental location (mitochondrial matrix, IDA evidence) is not among the choices, so the question is answerable by elimination but the 'correct' answer is a broad GO ancestor rather than the most specific location.",
    "reason": "General biological knowledge about the size, domain architecture, and function of replisome, RISC, and viral capsid proteins allows a model to eliminate A, B, and D, leaving C as the default. This constitutes a concrete elimination argument from the sequence and choices. The positive identification of 'cytoplasm' over 'mitochondrial matrix' is not achievable from the sequence, but since mitochondrial matrix is not an option, the elimination pathway is sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a 154-aa small metabolic enzyme. Only C is remotely plausible. No ambiguity among the provided choices, though the question is somewhat misleading because the protein's most specific experimentally determined location (mitochondrial matrix) is absent from the options, forcing selection of the broad GO ancestor 'cytoplasm.'"
  },
  "important_caveats": [
    "The primary experimental evidence (IDA:FlyBase, PMID:29491838) places this protein in the mitochondrial [2Fe-2S] assembly complex, not the general cytoplasm. The cytoplasm annotation is IBA:GO_Central (propagated from biological ancestors), not direct experimental evidence for this specific protein.",
    "In the GO ontology, mitochondrion is part_of cytoplasm, so annotating a mitochondrial protein as 'cytoplasm' is technically valid but biologically imprecise. In common usage, 'cytoplasm' often implies the cytosol excluding organelles.",
    "The sequence lacks a canonical mitochondrial targeting presequence, making mitochondrial localization not inferable from the sequence alone. The Drosophila IscU may use a non-canonical import mechanism.",
    "The question asks for the 'primary' cellular component, which by IDA evidence is the mitochondrial assembly complex. Choosing 'cytoplasm' is defensible only because the more specific answer is unavailable among the options."
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
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"29491838","source":"PubMed"}],"id":"GO:0099128","properties":[{"key":"GoTerm","value":"C:mitochondrial [2Fe-2S] assembly complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHK6.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.640117+00:00.  

```json
{"database":"GO","id":"GO:0005759","properties":[{"key":"GoTerm","value":"C:mitochondrial matrix"},{"key":"GoEvidenceType","value":"ISS:FlyBase"}]}
```

Source SHA-256: `b19888860b6b7334262a7e391a64d052f6aaf30b31bf5475636fe359508915c5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 159-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 160-160`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
DR   GO; GO:0099128; C:mitochondrial [2Fe-2S] assembly complex; IDA:FlyBase.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHK6?format=txt&versions=196)  
**Locator:** `lines 161-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:26.936483+00:00.  

```text
DR   GO; GO:0005759; C:mitochondrial matrix; ISS:FlyBase.
```

Source SHA-256: `4a0c43d94d803f18617308f73644d45abb03d9ffba8aafb11bcad71275354d68`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58957-58974`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005737
name: cytoplasm
namespace: cellular_component
def: "The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures." [ISBN:0198547684]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
xref: Wikipedia:Cytoplasm
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005622 ! intracellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58975-58998`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005739
name: mitochondrion
namespace: cellular_component
def: "A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration." [GOC:giardia, ISBN:0198506732]
comment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "mitochondria" EXACT []
xref: NIF_Subcellular:sao1860313010
xref: Wikipedia:Mitochondrion
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59194-59206`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005759
name: mitochondrial matrix
namespace: cellular_component
alt_id: GO:0031980
def: "The gel-like material, with considerable fine structure, that lies in the matrix space, or lumen, of a mitochondrion. It contains the enzymes of the tricarboxylic acid cycle and, in some organisms, the enzymes concerned with fatty acid oxidation." [GOC:as, ISBN:0198506732]
synonym: "mitochondrial lumen" EXACT []
synonym: "mitochondrial stroma" NARROW []
xref: NIF_Subcellular:sao1804523077
xref: Wikipedia:Mitochondrial_matrix
is_a: GO:0070013 ! intracellular organelle lumen
relationship: part_of GO:0005739 ! mitochondrion

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 413997-414007`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0099128
name: mitochondrial [2Fe-2S] assembly complex
namespace: cellular_component
def: "A protein complex capable of forming 2Fe-2S clusters in mitochondria. In humans it consists of ISCU, NFS1, LYRM4, NDUFAB1 and FXN." [PMID:31101807, PMID:34660592]
synonym: "mitochondrial iron-sulfur cluster assembly complex" RELATED []
synonym: "mitochondrial ISCU complex" EXACT []
is_a: GO:0098798 ! mitochondrial protein-containing complex
is_a: GO:1990221 ! L-cysteine desulfurase complex
is_a: GO:1990229 ! iron-sulfur cluster assembly complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 550379-550388`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990229
name: iron-sulfur cluster assembly complex
namespace: cellular_component
def: "A protein complex capable of assembling an iron-sulfur (Fe-S) cluster." [GOC:bhm, PMID:17350958]
synonym: "Fe-S cluster assembly complex" NARROW [GOC:bhm]
synonym: "SufBCD complex" NARROW [GOC:bhm]
is_a: GO:0032991 ! protein-containing complex
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
