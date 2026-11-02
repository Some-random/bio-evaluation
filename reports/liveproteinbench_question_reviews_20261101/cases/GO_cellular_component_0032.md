# GO_cellular_component_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDGYAVRAEAMEKRYGEKRALDGFDLAVGEGTVHGLLGPNGAGKTTAVRILSTLVRLDGGRATVAGLDVARQPREVRARIGLTGQYAAVDEVLTGRQNLEMFGRLFHLGGRRARLRATELLEQFDLTDAGDRGVGKYSGGMRRRLDLAASMILAPAVLFLDEPTTGLDPRSRGEVWESVRALVAGGTTVLLTTQYLEEADKLASRITVIDQGRAIADDTPDGLKNLVGGDRIEVVVAERAEIPRVVKVVARVADGEPEADETESRVHAPVTDRVTALTEVARTLQDEGVRVEDIGLRRPSLDDVFLRLTGHRTENTEAKEAA

[Multiple Choices]
A. food vacuole
B. ATP-binding cassette (ABC) transporter complex
C. plasma membrane
D. replisome
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

> The exact sequence matches the UniProt record, which assigns cell membrane localization by transfer from a homolog and includes a GO plasma-membrane annotation. This supports C, though the location evidence is inferred rather than a direct experimental localization measurement.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a P-loop ATP-binding motif, consistent with an ATP-binding transporter protein and making a transporter-related location more plausible than a food vacuole or replisome. That alone does not establish whether the relevant cellular component should be called the plasma membrane or the ABC transporter complex.


**Missing item-specific fact**

> A protein-specific localization or GO annotation, or validated information about this protein's association with a particular transporter complex, is needed to resolve the membrane-versus-complex distinction.


**Reason**

> The sequence offers a broad functional clue but not enough to select uniquely between two potentially overlapping cellular-component descriptions. The key is supported by a sequence-matched database annotation, not by a uniquely discriminating sequence argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> C is supported by the membrane-localization annotation. B is also biologically plausible for an ATP-binding ABC-transporter protein, since transporter-complex association can coexist with membrane localization; the question does not specify whether it seeks a location or complex membership.


### Important caveats

- The subcellular-location evidence is transferred from a homolog; the GO plasma-membrane annotation is electronically inferred.
- The cited study concerns daunorubicin efflux and transporter function, not direct localization of this protein.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop ATP-binding motif, consistent with an ATP-binding transporter protein and making a transporter-related location more plausible than a food vacuole or replisome. That alone does not establish whether the relevant cellular component should be called the plasma membrane or the ABC transporter complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific localization or GO annotation, or validated information about this protein's association with a particular transporter complex, is needed to resolve the membrane-versus-complex distinction.",
    "reason": "The sequence offers a broad functional clue but not enough to select uniquely between two potentially overlapping cellular-component descriptions. The key is supported by a sequence-matched database annotation, not by a uniquely discriminating sequence argument."
  },
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which assigns cell membrane localization by transfer from a homolog and includes a GO plasma-membrane annotation. This supports C, though the location evidence is inferred rather than a direct experimental localization measurement."
  },
  "important_caveats": [
    "The subcellular-location evidence is transferred from a homolog; the GO plasma-membrane annotation is electronically inferred.",
    "The cited study concerns daunorubicin efflux and transporter function, not direct localization of this protein.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "C is supported by the membrane-localization annotation. B is also biologically plausible for an ATP-binding ABC-transporter protein, since transporter-complex association can coexist with membrane localization; the question does not specify whether it seeks a location or complex membership."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which assigns cell membrane localization by transfer from a homolog and includes a GO plasma-membrane annotation. This supports C, though the location evidence is inferred rather than a direct experimental localization measurement.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a P-loop ATP-binding motif, consistent with an ATP-binding transporter protein and making a transporter-related location more plausible than a food vacuole or replisome. That alone does not establish whether the relevant cellular component should be called the plasma membrane or the ABC transporter complex.",
    "missing_item_specific_fact": "A protein-specific localization or GO annotation, or validated information about this protein's association with a particular transporter complex, is needed to resolve the membrane-versus-complex distinction.",
    "reason": "The sequence offers a broad functional clue but not enough to select uniquely between two potentially overlapping cellular-component descriptions. The key is supported by a sequence-matched database annotation, not by a uniquely discriminating sequence argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "C is supported by the membrane-localization annotation. B is also biologically plausible for an ATP-binding ABC-transporter protein, since transporter-complex association can coexist with membrane localization; the question does not specify whether it seeks a location or complex membership."
  },
  "important_caveats": [
    "The subcellular-location evidence is transferred from a homolog; the GO plasma-membrane annotation is electronically inferred.",
    "The cited study concerns daunorubicin efflux and transporter function, not direct localization of this protein.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU5 annotates this protein (Daunorubicin resistance ATP-binding protein DrrA2) to GO:0005886 (plasma membrane), with subcellular location 'Cell membrane; Peripheral membrane protein; Cytoplasmic side.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option C. The evidence code is ECO:0000250 (similarity to P32010), indicating computational inference by similarity rather than direct experimental determination, but the annotation is present and consistent with the protein's identity as a bacterial ABC transporter NBD. The GO cross-reference (IEA:UniProtKB-SubCell) directly maps to the answer choice.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A/P-loop motif (GLGPNGAGKTT) and Walker B-like motif (DEPTTGLD), identifying it as an ABC-type ATP-binding domain. Critically, the 322-residue protein lacks transmembrane helices, indicating it is a peripheral membrane protein (NBD) rather than a transmembrane transporter component. In bacteria, ABC transporters are located at the plasma membrane (cell membrane). A peripheral membrane protein on the cytoplasmic side has its primary cellular component as the plasma membrane. Option B (ABC transporter complex, GO:0043190) refers to the complete multi-subunit assembly including transmembrane domains; a single NBD subunit is not itself the complex but resides at the membrane. Options A (food vacuole, an Apicomplexa-specific organelle) and D (replisome, a DNA replication machine) are clearly incompatible with the ABC ATPase sequence features.


**Missing item-specific fact**

> The precise GO annotation semantics distinguishing 'plasma membrane' (location of the peripheral protein) from 'ABC transporter complex' (the full multi-protein assembly) is somewhat annotation-convention-specific, though the biological logic of peripheral vs. integral membrane proteins provides a defensible basis.


**Reason**

> The Walker A motif unambiguously identifies the protein family, the absence of TM helices indicates peripheral membrane association, and bacterial ABC transporters are at the plasma membrane. The distinction between C and B rests on recognizing that a single peripheral NBD subunit's location is the membrane itself, not the complete transporter complex. This is a defensible biological inference, though the GO-term-level distinction between 'location' and 'complex membership' adds a layer of annotation-specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Option B (ABC transporter complex) is not entirely unreasonable: the protein IS an ATP-binding component of an ABC transporter, and GO:0043190 is_a GO:0098797 (plasma membrane protein complex). A model recognizing the Walker A motif might select B as the more 'specific' annotation. However, the GO definition of GO:0043190 explicitly describes a multi-domain complex ('two membrane-associated domains and two ATP-binding domains'), and this protein is only the ATP-binding component. The UniProt annotation assigns only GO:0005886, not GO:0043190. The distinction is defensible but requires knowledge of GO term semantics regarding complexes vs. individual subunits.


### Important caveats

- The UniProt subcellular location annotation uses evidence code ECO:0000250 (similarity to P32010), meaning the membrane localization is inferred by homology, not directly experimentally determined for this protein.
- The GO annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation), not an independent experimental GO assignment.
- The protein was first released in UniProt in February 2025; the benchmark's exact author source snapshot is unknown.
- Option B is not wholly indefensible as a cellular component for an ABC transporter subunit, creating a subtle ambiguity between 'where it is' (plasma membrane) and 'what complex it belongs to' (ABC transporter complex).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A/P-loop motif (GLGPNGAGKTT) and Walker B-like motif (DEPTTGLD), identifying it as an ABC-type ATP-binding domain. Critically, the 322-residue protein lacks transmembrane helices, indicating it is a peripheral membrane protein (NBD) rather than a transmembrane transporter component. In bacteria, ABC transporters are located at the plasma membrane (cell membrane). A peripheral membrane protein on the cytoplasmic side has its primary cellular component as the plasma membrane. Option B (ABC transporter complex, GO:0043190) refers to the complete multi-subunit assembly including transmembrane domains; a single NBD subunit is not itself the complex but resides at the membrane. Options A (food vacuole, an Apicomplexa-specific organelle) and D (replisome, a DNA replication machine) are clearly incompatible with the ABC ATPase sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise GO annotation semantics distinguishing 'plasma membrane' (location of the peripheral protein) from 'ABC transporter complex' (the full multi-protein assembly) is somewhat annotation-convention-specific, though the biological logic of peripheral vs. integral membrane proteins provides a defensible basis.",
    "reason": "The Walker A motif unambiguously identifies the protein family, the absence of TM helices indicates peripheral membrane association, and bacterial ABC transporters are at the plasma membrane. The distinction between C and B rests on recognizing that a single peripheral NBD subunit's location is the membrane itself, not the complete transporter complex. This is a defensible biological inference, though the GO-term-level distinction between 'location' and 'complex membership' adds a layer of annotation-specificity."
  },
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU5 annotates this protein (Daunorubicin resistance ATP-binding protein DrrA2) to GO:0005886 (plasma membrane), with subcellular location 'Cell membrane; Peripheral membrane protein; Cytoplasmic side.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option C. The evidence code is ECO:0000250 (similarity to P32010), indicating computational inference by similarity rather than direct experimental determination, but the annotation is present and consistent with the protein's identity as a bacterial ABC transporter NBD. The GO cross-reference (IEA:UniProtKB-SubCell) directly maps to the answer choice."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses evidence code ECO:0000250 (similarity to P32010), meaning the membrane localization is inferred by homology, not directly experimentally determined for this protein.",
    "The GO annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation), not an independent experimental GO assignment.",
    "The protein was first released in UniProt in February 2025; the benchmark's exact author source snapshot is unknown.",
    "Option B is not wholly indefensible as a cellular component for an ABC transporter subunit, creating a subtle ambiguity between 'where it is' (plasma membrane) and 'what complex it belongs to' (ABC transporter complex)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Option B (ABC transporter complex) is not entirely unreasonable: the protein IS an ATP-binding component of an ABC transporter, and GO:0043190 is_a GO:0098797 (plasma membrane protein complex). A model recognizing the Walker A motif might select B as the more 'specific' annotation. However, the GO definition of GO:0043190 explicitly describes a multi-domain complex ('two membrane-associated domains and two ATP-binding domains'), and this protein is only the ATP-binding component. The UniProt annotation assigns only GO:0005886, not GO:0043190. The distinction is defensible but requires knowledge of GO term semantics regarding complexes vs. individual subunits."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU5 annotates this protein (Daunorubicin resistance ATP-binding protein DrrA2) to GO:0005886 (plasma membrane), with subcellular location 'Cell membrane; Peripheral membrane protein; Cytoplasmic side.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option C. The evidence code is ECO:0000250 (similarity to P32010), indicating computational inference by similarity rather than direct experimental determination, but the annotation is present and consistent with the protein's identity as a bacterial ABC transporter NBD. The GO cross-reference (IEA:UniProtKB-SubCell) directly maps to the answer choice.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A/P-loop motif (GLGPNGAGKTT) and Walker B-like motif (DEPTTGLD), identifying it as an ABC-type ATP-binding domain. Critically, the 322-residue protein lacks transmembrane helices, indicating it is a peripheral membrane protein (NBD) rather than a transmembrane transporter component. In bacteria, ABC transporters are located at the plasma membrane (cell membrane). A peripheral membrane protein on the cytoplasmic side has its primary cellular component as the plasma membrane. Option B (ABC transporter complex, GO:0043190) refers to the complete multi-subunit assembly including transmembrane domains; a single NBD subunit is not itself the complex but resides at the membrane. Options A (food vacuole, an Apicomplexa-specific organelle) and D (replisome, a DNA replication machine) are clearly incompatible with the ABC ATPase sequence features.",
    "missing_item_specific_fact": "The precise GO annotation semantics distinguishing 'plasma membrane' (location of the peripheral protein) from 'ABC transporter complex' (the full multi-protein assembly) is somewhat annotation-convention-specific, though the biological logic of peripheral vs. integral membrane proteins provides a defensible basis.",
    "reason": "The Walker A motif unambiguously identifies the protein family, the absence of TM helices indicates peripheral membrane association, and bacterial ABC transporters are at the plasma membrane. The distinction between C and B rests on recognizing that a single peripheral NBD subunit's location is the membrane itself, not the complete transporter complex. This is a defensible biological inference, though the GO-term-level distinction between 'location' and 'complex membership' adds a layer of annotation-specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Option B (ABC transporter complex) is not entirely unreasonable: the protein IS an ATP-binding component of an ABC transporter, and GO:0043190 is_a GO:0098797 (plasma membrane protein complex). A model recognizing the Walker A motif might select B as the more 'specific' annotation. However, the GO definition of GO:0043190 explicitly describes a multi-domain complex ('two membrane-associated domains and two ATP-binding domains'), and this protein is only the ATP-binding component. The UniProt annotation assigns only GO:0005886, not GO:0043190. The distinction is defensible but requires knowledge of GO term semantics regarding complexes vs. individual subunits."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses evidence code ECO:0000250 (similarity to P32010), meaning the membrane localization is inferred by homology, not directly experimentally determined for this protein.",
    "The GO annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation), not an independent experimental GO assignment.",
    "The protein was first released in UniProt in February 2025; the benchmark's exact author source snapshot is unknown.",
    "Option B is not wholly indefensible as a cellular component for an ABC transporter subunit, creating a subtle ambiguity between 'where it is' (plasma membrane) and 'what complex it belongs to' (ABC transporter complex)."
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

**Accession:** `P0DXU5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
"P0DXU5"
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32010","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"orientation":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32010","source":"UniProtKB"}],"id":"SL-9910","value":"Cytoplasmic side"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32010","source":"UniProtKB"}],"id":"SL-9903","value":"Peripheral membrane protein"}}]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 41-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32010};
CC       Peripheral membrane protein {ECO:0000250|UniProtKB:P32010}; Cytoplasmic
CC       side {ECO:0000250|UniProtKB:P32010}.
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 63-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
