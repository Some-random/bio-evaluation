# GO_cellular_component_0141

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFNNFLNMYMCTLAEKLCKFKKNNFNNIHRNNNFYRDNNFYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNLYTNNNLYRDNNFYNITLRKFHFIQTISNNNFNFEIIKKYGDVINKIMFIHTQKKNKQERFMFNNKKYIKRKEYILNDLNEFISIIPHPEINNEITNNSNQKKNKDNKQNVLSTNQQIITNYNLNHKENVTSNLNFNNKEEDEKKLDKLLKKRNIKKRDIVTITEEAKEELKKIISINKKENNNNYNNMNTICSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK

[Multiple Choices]
A. endoplasmic reticulum
B. perinuclear region of cytoplasm
C. cytoplasm
D. cytosolic small ribosomal subunit
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

> The sequence-matched UniProt record annotates cytoplasm by IBA, supporting C as a broad GO component. It also reports experimentally evidenced mitochondrial localization, a more specific location that is part of the cytoplasm in GO; thus C is supported but less specific than the experimental localization.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone gives no clear, reliable signal that distinguishes cytoplasm from the other listed subcellular locations. The protein-specific localization and its GO annotations are needed.


**Missing item-specific fact**

> The identity and localization annotation for this sequence: the matched record identifies it as Plasmodium falciparum IscA2 and reports mitochondrial localization, alongside a broad cytoplasm GO annotation.


**Reason**

> The reviewer-only record supports the key, but those annotations and the protein identity were absent from the question. Inferring a precise compartment from the sequence or generic function is not adequately justified by the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported as a broad GO location, while the more specific experimentally evidenced location, mitochondrion, is not an option. The evidence does not support another listed option as the protein’s specific location.


### Important caveats

- The sequence matches the historical and current UniProt record; the exact source snapshot used by the author is unknown.
- The cytoplasm annotation is IBA, whereas the mitochondrial localization is experimentally evidenced in the record.
- GO treats mitochondrion as part of cytoplasm, but that hierarchy does not make the terms equally specific.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone gives no clear, reliable signal that distinguishes cytoplasm from the other listed subcellular locations. The protein-specific localization and its GO annotations are needed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and localization annotation for this sequence: the matched record identifies it as Plasmodium falciparum IscA2 and reports mitochondrial localization, alongside a broad cytoplasm GO annotation.",
    "reason": "The reviewer-only record supports the key, but those annotations and the protein identity were absent from the question. Inferring a precise compartment from the sequence or generic function is not adequately justified by the supplied input."
  },
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "C5",
      "C6",
      "C7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cytoplasm by IBA, supporting C as a broad GO component. It also reports experimentally evidenced mitochondrial localization, a more specific location that is part of the cytoplasm in GO; thus C is supported but less specific than the experimental localization."
  },
  "important_caveats": [
    "The sequence matches the historical and current UniProt record; the exact source snapshot used by the author is unknown.",
    "The cytoplasm annotation is IBA, whereas the mitochondrial localization is experimentally evidenced in the record.",
    "GO treats mitochondrion as part of cytoplasm, but that hierarchy does not make the terms equally specific."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported as a broad GO location, while the more specific experimentally evidenced location, mitochondrion, is not an option. The evidence does not support another listed option as the protein’s specific location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates cytoplasm by IBA, supporting C as a broad GO component. It also reports experimentally evidenced mitochondrial localization, a more specific location that is part of the cytoplasm in GO; thus C is supported but less specific than the experimental localization.",
    "evidence_ids": ["H3", "H4", "H5", "C5", "C6", "C7", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone gives no clear, reliable signal that distinguishes cytoplasm from the other listed subcellular locations. The protein-specific localization and its GO annotations are needed.",
    "missing_item_specific_fact": "The identity and localization annotation for this sequence: the matched record identifies it as Plasmodium falciparum IscA2 and reports mitochondrial localization, alongside a broad cytoplasm GO annotation.",
    "reason": "The reviewer-only record supports the key, but those annotations and the protein identity were absent from the question. Inferring a precise compartment from the sequence or generic function is not adequately justified by the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported as a broad GO location, while the more specific experimentally evidenced location, mitochondrion, is not an option. The evidence does not support another listed option as the protein’s specific location."
  },
  "important_caveats": [
    "The sequence matches the historical and current UniProt record; the exact source snapshot used by the author is unknown.",
    "The cytoplasm annotation is IBA, whereas the mitochondrial localization is experimentally evidenced in the record.",
    "GO treats mitochondrion as part of cytoplasm, but that hierarchy does not make the terms equally specific."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (O97297, PfIscA2) is experimentally localized to the mitochondrion (ECO:0000269, Sadik et al. 2021). In the GO ontology, mitochondrion (GO:0005739) is part_of cytoplasm (GO:0005737), and a GO:0005737 annotation with IBA:GO_Central evidence exists for this entry. Since mitochondrion is not among the answer choices, 'cytoplasm' is the most specific correct option available: the protein is indeed in the cytoplasm broadly defined. The other options (ER, perinuclear region, ribosomal subunit) are not supported by any annotation or experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Through general biological knowledge, one can eliminate: (D) ribosomal subunit—no ribosomal protein motifs, no rRNA-binding domains, and the sequence lacks the compact basic structure of ribosomal proteins; (A) ER—no N-terminal hydrophobic signal peptide of the ER type (the N-terminus is asparagine-rich, typical of Plasmodium), no KDEL/HDEL retention signal, no transmembrane domains; (B) perinuclear region—no specific perinuclear targeting motifs. The remaining option (C) cytoplasm is the broadest correct compartment. A trained observer might additionally note Fe-S cluster-binding cysteine motifs (e.g., 'CPCGTSFHFSKKK', 'ITKGCNGLTHSFNFISKK') suggesting a mitochondrial Fe-S assembly role, but since mitochondrion is absent from the choices, the correct answer by elimination is cytoplasm (which contains mitochondria per GO).


**Missing item-specific fact**

> None strictly required to eliminate A, B, and D. However, identifying the protein as mitochondrial (rather than generic cytoplasmic) would require recognizing the IscA2 identity or the specific experimental subcellular localization data.


**Reason**

> The three distractors can be eliminated through general knowledge of protein targeting signals and structural motifs. Cytoplasm remains as the broadest compartment that encompasses the actual (mitochondrial) location. The reasoning is somewhat weak (essentially elimination of clearly wrong answers), but it does not require memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly incompatible with the sequence and known biology. Option C (cytoplasm) is the only defensible choice, though it is a very broad category that subsumes the true specific location (mitochondrion). No other option is supported by any annotation or sequence feature.


### Important caveats

- The PRIMARY experimentally determined location is the mitochondrion (ECO:0000269), not generic cytoplasm. The GO:0005737 (cytoplasm) annotation is IBA:GO_Central—a computational propagation through the part_of hierarchy—not an independent experimental finding.
- The question asks for the 'primary Cellular Component,' which would more precisely be 'mitochondrion.' The author's key of 'cytoplasm' is correct only because mitochondrion is absent from the option set, forcing selection of the broader parent term.
- The sequence is highly asparagine/tyrosine-rich, characteristic of Plasmodium falciparum proteins, which may obscure conventional targeting signal recognition.
- The GO:0000181 (obsolete 'cytosolic small ribosomal subunit') and GO:0022627 (current 'cytosolic small ribosomal subunit') are distinct terms; the option text matches the obsolete synonym, but this does not affect answerability since D is clearly wrong.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Through general biological knowledge, one can eliminate: (D) ribosomal subunit—no ribosomal protein motifs, no rRNA-binding domains, and the sequence lacks the compact basic structure of ribosomal proteins; (A) ER—no N-terminal hydrophobic signal peptide of the ER type (the N-terminus is asparagine-rich, typical of Plasmodium), no KDEL/HDEL retention signal, no transmembrane domains; (B) perinuclear region—no specific perinuclear targeting motifs. The remaining option (C) cytoplasm is the broadest correct compartment. A trained observer might additionally note Fe-S cluster-binding cysteine motifs (e.g., 'CPCGTSFHFSKKK', 'ITKGCNGLTHSFNFISKK') suggesting a mitochondrial Fe-S assembly role, but since mitochondrion is absent from the choices, the correct answer by elimination is cytoplasm (which contains mitochondria per GO).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required to eliminate A, B, and D. However, identifying the protein as mitochondrial (rather than generic cytoplasmic) would require recognizing the IscA2 identity or the specific experimental subcellular localization data.",
    "reason": "The three distractors can be eliminated through general knowledge of protein targeting signals and structural motifs. Cytoplasm remains as the broadest compartment that encompasses the actual (mitochondrial) location. The reasoning is somewhat weak (essentially elimination of clearly wrong answers), but it does not require memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein (O97297, PfIscA2) is experimentally localized to the mitochondrion (ECO:0000269, Sadik et al. 2021). In the GO ontology, mitochondrion (GO:0005739) is part_of cytoplasm (GO:0005737), and a GO:0005737 annotation with IBA:GO_Central evidence exists for this entry. Since mitochondrion is not among the answer choices, 'cytoplasm' is the most specific correct option available: the protein is indeed in the cytoplasm broadly defined. The other options (ER, perinuclear region, ribosomal subunit) are not supported by any annotation or experimental evidence for this protein."
  },
  "important_caveats": [
    "The PRIMARY experimentally determined location is the mitochondrion (ECO:0000269), not generic cytoplasm. The GO:0005737 (cytoplasm) annotation is IBA:GO_Central—a computational propagation through the part_of hierarchy—not an independent experimental finding.",
    "The question asks for the 'primary Cellular Component,' which would more precisely be 'mitochondrion.' The author's key of 'cytoplasm' is correct only because mitochondrion is absent from the option set, forcing selection of the broader parent term.",
    "The sequence is highly asparagine/tyrosine-rich, characteristic of Plasmodium falciparum proteins, which may obscure conventional targeting signal recognition.",
    "The GO:0000181 (obsolete 'cytosolic small ribosomal subunit') and GO:0022627 (current 'cytosolic small ribosomal subunit') are distinct terms; the option text matches the obsolete synonym, but this does not affect answerability since D is clearly wrong."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with the sequence and known biology. Option C (cytoplasm) is the only defensible choice, though it is a very broad category that subsumes the true specific location (mitochondrion). No other option is supported by any annotation or sequence feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (O97297, PfIscA2) is experimentally localized to the mitochondrion (ECO:0000269, Sadik et al. 2021). In the GO ontology, mitochondrion (GO:0005739) is part_of cytoplasm (GO:0005737), and a GO:0005737 annotation with IBA:GO_Central evidence exists for this entry. Since mitochondrion is not among the answer choices, 'cytoplasm' is the most specific correct option available: the protein is indeed in the cytoplasm broadly defined. The other options (ER, perinuclear region, ribosomal subunit) are not supported by any annotation or experimental evidence for this protein.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Through general biological knowledge, one can eliminate: (D) ribosomal subunit—no ribosomal protein motifs, no rRNA-binding domains, and the sequence lacks the compact basic structure of ribosomal proteins; (A) ER—no N-terminal hydrophobic signal peptide of the ER type (the N-terminus is asparagine-rich, typical of Plasmodium), no KDEL/HDEL retention signal, no transmembrane domains; (B) perinuclear region—no specific perinuclear targeting motifs. The remaining option (C) cytoplasm is the broadest correct compartment. A trained observer might additionally note Fe-S cluster-binding cysteine motifs (e.g., 'CPCGTSFHFSKKK', 'ITKGCNGLTHSFNFISKK') suggesting a mitochondrial Fe-S assembly role, but since mitochondrion is absent from the choices, the correct answer by elimination is cytoplasm (which contains mitochondria per GO).",
    "missing_item_specific_fact": "None strictly required to eliminate A, B, and D. However, identifying the protein as mitochondrial (rather than generic cytoplasmic) would require recognizing the IscA2 identity or the specific experimental subcellular localization data.",
    "reason": "The three distractors can be eliminated through general knowledge of protein targeting signals and structural motifs. Cytoplasm remains as the broadest compartment that encompasses the actual (mitochondrial) location. The reasoning is somewhat weak (essentially elimination of clearly wrong answers), but it does not require memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with the sequence and known biology. Option C (cytoplasm) is the only defensible choice, though it is a very broad category that subsumes the true specific location (mitochondrion). No other option is supported by any annotation or sequence feature."
  },
  "important_caveats": [
    "The PRIMARY experimentally determined location is the mitochondrion (ECO:0000269), not generic cytoplasm. The GO:0005737 (cytoplasm) annotation is IBA:GO_Central—a computational propagation through the part_of hierarchy—not an independent experimental finding.",
    "The question asks for the 'primary Cellular Component,' which would more precisely be 'mitochondrion.' The author's key of 'cytoplasm' is correct only because mitochondrion is absent from the option set, forcing selection of the broader parent term.",
    "The sequence is highly asparagine/tyrosine-rich, characteristic of Plasmodium falciparum proteins, which may obscure conventional targeting signal recognition.",
    "The GO:0000181 (obsolete 'cytosolic small ribosomal subunit') and GO:0022627 (current 'cytosolic small ribosomal subunit') are distinct terms; the option text matches the obsolete synonym, but this does not affect answerability since D is clearly wrong."
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

**Accession:** `O97297` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"database":"GO","id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"database":"GO","id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 87-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 109-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 110-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IBA:GO_Central.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence GO2

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

### Evidence GO3

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
