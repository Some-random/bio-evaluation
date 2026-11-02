# GO_cellular_component_0091

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVMKFTWRSIIPRCSKGIEEAEAEAEAETKKQDSKQGSFSRLAMIDFSYPSSMFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDENRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYGETSVASFVYTVPTHQKGGSPPKDDTDTKECEAKTELKKENGHHRNRHHHRRSHKSRDGHRHQNKSSSQSSVHSENDTSKQNLENGSNEECNID

[Multiple Choices]
A. inner membrane pellicle complex
B. plasma membrane
C. RQC complex
D. mitochondrial outer membrane
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

> The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.


**Missing item-specific fact**

> A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.


**Reason**

> General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein.


### Important caveats

- The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.
- The source snapshot available to the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.",
    "reason": "General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts."
  },
  "important_caveats": [
    "The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.",
    "The source snapshot available to the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cotton protein record, which annotates it to the cell membrane and maps it to the plasma membrane. The location evidence is transferred or computationally inferred, not direct experimental evidence in the excerpts.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence appears kinase-like and lacks an obvious transmembrane segment, making a soluble cytoplasmic kinase that associates peripherally with a membrane plausible. The specialized pellicle and RQC choices are poor fits, but these features do not establish plasma-membrane localization over other possibilities.",
    "missing_item_specific_fact": "A protein-specific localization annotation or experimental localization result is needed to identify the plasma membrane as the protein’s primary compartment.",
    "reason": "General sequence features and the choices can make B plausible, but they do not determine this protein’s specific localization; the supporting plasma-membrane annotation is external to the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B, and none of the alternatives is comparably supported for this protein."
  },
  "important_caveats": [
    "The matched record’s cell-membrane annotation is transferred by similarity, and its GO plasma-membrane annotation is inferred; the excerpts do not establish direct experimental localization.",
    "The source snapshot available to the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.


**Missing item-specific fact**

> The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.


**Reason**

> The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices.


### Important caveats

- The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.
- The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.
- The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.",
    "reason": "The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs."
  },
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization."
  },
  "important_caveats": [
    "The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.",
    "The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.",
    "The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB annotates this protein (A0A5J5NT52, GbEIR5D from Gossypium barbadense) with subcellular location 'Cell membrane' (C5, H3) and GO:0005886 'plasma membrane' (C6, H4). 'Cell membrane' is an EXACT synonym of GO:0005886 'plasma membrane' (GO2). The annotation is consistent with the protein being a receptor-like cytoplasmic kinase (RLCK), a family known to associate with the plasma membrane. However, the evidence code is ECO:0000250/ISS (similarity-based inference from Q9ZUF4), meaning this is computational transfer, not direct experimental localization.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four options, three can be eliminated through general biological reasoning from the sequence: (A) inner membrane pellicle complex is specific to apicomplexan parasites (GO3 definition confirms 'apicomplexan parasite cell'), incompatible with a plant protein; (C) RQC complex is a defined ribosome-associated quality-control complex with specific protein components (Cdc48, Rkr1, etc., per GO4), not a kinase; (D) mitochondrial outer membrane requires an N-terminal mitochondrial targeting signal, which is absent from this sequence's N-terminus (no amphipathic cationic helix typical of mitochondrial precursors). The sequence clearly contains a serine/threonine kinase domain (recognizable GxGxxG, DFG, and activation loop motifs), making it a signaling kinase. With A, C, and D eliminated, B (plasma membrane) is the only remaining viable compartment for a membrane-associated kinase.",
    "missing_item_specific_fact": "The positive assignment to plasma membrane specifically (rather than cytoplasm, which is not offered as an option) relies on knowing that RLCKs associate with the plasma membrane via lipid modifications or protein interactions. However, since 'cytoplasm' is not among the choices, elimination reasoning suffices.",
    "reason": "The four options are sufficiently heterogeneous that general biological knowledge (apicomplexan specificity of pellicle, defined composition of RQC, requirement of MTS for mitochondrial outer membrane) eliminates three choices, leaving plasma membrane as the only viable answer. The kinase domain is identifiable from sequence motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a plant serine/threonine kinase lacking mitochondrial targeting signals. Only B remains defensible among the four choices."
  },
  "important_caveats": [
    "The plasma membrane annotation is ISS (Inferred from Sequence Similarity, ECO:0000250), transferred from an Arabidopsis RLCK homolog, not experimentally determined for this specific protein.",
    "The protein name includes 'cytoplasmic' (receptor-like cytoplasmic kinase), which could mislead toward a cytoplasmic localization, but RLCKs are membrane-associated despite lacking transmembrane domains.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt entry A0A5J5NT52.",
    "The author's source snapshot is unknown; the entry was first public 2025-06-18, so the annotation may not have existed at the time the benchmark was constructed."
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

**Accession:** `A0A5J5NT52` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.363840+00:00.  

```json
"A0A5J5NT52"
```

Source SHA-256: `eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.363840+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9ZUF4","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"}}]}
```

Source SHA-256: `eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5NT52.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.363840+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `eb2977fae0d3ae6073a227e5a0f169c9c1e4b2c014cebddf63f41623ffadde49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:32.436038+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9ZUF4}.
```

Source SHA-256: `e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5NT52?format=txt&versions=17)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:32.436038+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `e263047c9f63471968fd369e2598de5a1153ccd3b4ee74301e83ce2121276d7a`.

### Evidence GO2

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

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 365849-365857`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0070258
name: inner membrane pellicle complex
namespace: cellular_component
def: "A membrane structure formed of two closely aligned lipid bilayers that lie beneath the plasma membrane and form part of the pellicle surrounding an apicomplexan parasite cell." [GOC:mah, PMID:12456714]
synonym: "inner membrane complex" BROAD []
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0020039 ! pellicle

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549333-549341`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990112
name: RQC complex
namespace: cellular_component
def: "A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins." [GOC:rb, PMID:23178123, PMID:23232563]
synonym: "ribosome quality control complex" EXACT [PMID:23178123, PMID:23232563]
synonym: "ribosome-bound quality control complex" EXACT []
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
