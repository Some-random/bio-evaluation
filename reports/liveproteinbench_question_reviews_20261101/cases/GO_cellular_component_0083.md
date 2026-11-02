# GO_cellular_component_0083

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | invalid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MANILENQLFTAAKTIEQQLDQQLDRLDNLDSDDLKVLREQRLREMKDLNNKKQEWLRNGHGTYTELADEKEFFEMSKKSPNIVCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD

[Multiple Choices]
A. ATP-binding cassette (ABC) transporter complex
B. caveola
C. cytoplasm
D. site of double-strand break
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

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `expected_answer_check:invalid_evidence_ids`.

### Expected-answer support: supported

> The supplied sequence exactly matches the UniProt sequence annotated to cytoplasm and cytosol. The cytoplasm annotation is IBA (phylogenetic inference), while the cytosol annotation is NAS:FlyBase; these support the key but are not direct experimental localization evidence.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), `source_applicability` (not an assigned excerpt ID).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has no evident transmembrane segment or organellar targeting signal and is consistent with a soluble protein. That meaningfully favors cytoplasm over a membrane-associated caveola or ABC transporter complex, and the sequence offers no apparent basis for localization to a DNA double-strand break site.


**Missing item-specific fact**

> An experimentally established localization for this particular protein would strengthen the conclusion, but is not necessary to distinguish the broad cytoplasmic option from these alternatives.


**Reason**

> General sequence-based biological reasoning distinguishes the soluble cytoplasmic choice from the membrane-associated and DNA-lesion choices, though it does not independently establish the protein's precise localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Cytosol is a subcompartment of cytoplasm, but cytosol is not a separate option; the other listed choices are meaningfully distinct from the broad cytoplasmic localization.


### Important caveats

- The reviewer-only annotations support the key but were not available to the evaluated model.
- The cytoplasm annotation is computationally inferred, and the cytosol annotation is database-assigned; neither excerpt establishes direct experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has no evident transmembrane segment or organellar targeting signal and is consistent with a soluble protein. That meaningfully favors cytoplasm over a membrane-associated caveola or ABC transporter complex, and the sequence offers no apparent basis for localization to a DNA double-strand break site.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "An experimentally established localization for this particular protein would strengthen the conclusion, but is not necessary to distinguish the broad cytoplasmic option from these alternatives.",
    "reason": "General sequence-based biological reasoning distinguishes the soluble cytoplasmic choice from the membrane-associated and DNA-lesion choices, though it does not independently establish the protein's precise localization."
  },
  "case_id": "GO_cellular_component_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "source_applicability"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated to cytoplasm and cytosol. The cytoplasm annotation is IBA (phylogenetic inference), while the cytosol annotation is NAS:FlyBase; these support the key but are not direct experimental localization evidence."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available to the evaluated model.",
    "The cytoplasm annotation is computationally inferred, and the cytosol annotation is database-assigned; neither excerpt establishes direct experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cytosol is a subcompartment of cytoplasm, but cytosol is not a separate option; the other listed choices are meaningfully distinct from the broad cytoplasmic localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated to cytoplasm and cytosol. The cytoplasm annotation is IBA (phylogenetic inference), while the cytosol annotation is NAS:FlyBase; these support the key but are not direct experimental localization evidence.",
    "evidence_ids": ["H3", "H4", "C5", "source_applicability"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has no evident transmembrane segment or organellar targeting signal and is consistent with a soluble protein. That meaningfully favors cytoplasm over a membrane-associated caveola or ABC transporter complex, and the sequence offers no apparent basis for localization to a DNA double-strand break site.",
    "missing_item_specific_fact": "An experimentally established localization for this particular protein would strengthen the conclusion, but is not necessary to distinguish the broad cytoplasmic option from these alternatives.",
    "reason": "General sequence-based biological reasoning distinguishes the soluble cytoplasmic choice from the membrane-associated and DNA-lesion choices, though it does not independently establish the protein's precise localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cytosol is a subcompartment of cytoplasm, but cytosol is not a separate option; the other listed choices are meaningfully distinct from the broad cytoplasmic localization."
  },
  "important_caveats": [
    "The reviewer-only annotations support the key but were not available to the evaluated model.",
    "The cytoplasm annotation is computationally inferred, and the cytosol annotation is database-assigned; neither excerpt establishes direct experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q9VGV8, Phosducin-like protein 3 from Drosophila melanogaster) is annotated to GO:0005737 (cytoplasm) via IBA:GO_Central (H3) and to the more specific GO:0005829 (cytosol) via NAS:FlyBase (H4) and ECO:0000303 from a 2024 PubMed paper (C5). Since cytosol is part_of cytoplasm (GO2 ontology path), the broader annotation 'cytoplasm' is consistent with the evidence. The cytoplasm annotation itself is computational (IBA), but it is hierarchically supported by the more specific cytosol annotation. No annotation contradicts cytoplasmic localization.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 216-aa sequence lacks all hallmark targeting features for the three distractors: (1) No transmembrane helices (~20+ hydrophobic residues) or Walker A/B nucleotide-binding motifs, ruling out an ABC transporter complex; (2) No caveolin-binding motif (aromatic-phi-X-phi-X-X-X-X-X-X-X-X-phi pattern) or membrane-anchoring signal, ruling out caveola; (3) No DNA-repair-associated domains (BRCT, FHA, RRM, kinase domains) or nuclear localization signal, ruling out site of double-strand break. The sequence instead contains a thioredoxin-like fold (CxxC motif visible in 'VCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD'), a fold commonly found in soluble cytoplasmic proteins. The absence of any organellar targeting peptide (mitochondrial, ER signal, peroxisomal PTS) and the presence of a soluble thioredoxin-fold domain together support a default cytoplasmic localization.


**Missing item-specific fact**

> None critical. Recognizing the protein as PhLP3 specifically would require lookup, but the elimination of the three distractors and the positive identification of a cytoplasmic thioredoxin-fold protein are achievable from sequence features alone.


**Reason**

> The three distractors represent highly specific structural/functional contexts (transmembrane transporter complex, membrane microdomain, DNA-damage repair focus) that each require distinctive sequence signatures absent from this small soluble protein. The remaining option, cytoplasm, is the biologically default location for a soluble protein with no targeting signals and a thioredoxin-like fold. This is a defensible reasoning chain from general protein-targeting biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different cellular contexts (membrane transporter complex, plasma-membrane microdomain, soluble compartment, nuclear DNA-damage site). The sequence clearly lacks features for A, B, and D, leaving C as the only viable option. The minor distinction between 'cytoplasm' and 'cytosol' (the latter being the more specific UniProt annotation) does not create ambiguity because cytosol is part_of cytoplasm in the GO hierarchy, and the question asks for 'primary Cellular Component,' for which the broader term is acceptable.


### Important caveats

- The cytoplasm (GO:0005737) annotation is via IBA (Inferred by Biological Aspect) from GO_Central, a computational transfer, not direct experimental evidence. The more specific cytosol annotation has stronger evidence (FlyBase NAS and a 2024 PubMed paper).
- The protein was only integrated into Swiss-Prot in June 2025; the benchmark's author source snapshot is unknown. If the benchmark predates Swiss-Prot integration, the annotation may have originated from a TrEMBL entry or FlyBase rather than curated UniProt.
- The thioredoxin-fold identification is based on sequence pattern recognition (CxxC motif and structural similarity); it is a reasonable inference but not a definitive fold assignment without structural data.
- All reviewer evidence is post-hoc and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216-aa sequence lacks all hallmark targeting features for the three distractors: (1) No transmembrane helices (~20+ hydrophobic residues) or Walker A/B nucleotide-binding motifs, ruling out an ABC transporter complex; (2) No caveolin-binding motif (aromatic-phi-X-phi-X-X-X-X-X-X-X-X-phi pattern) or membrane-anchoring signal, ruling out caveola; (3) No DNA-repair-associated domains (BRCT, FHA, RRM, kinase domains) or nuclear localization signal, ruling out site of double-strand break. The sequence instead contains a thioredoxin-like fold (CxxC motif visible in 'VCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD'), a fold commonly found in soluble cytoplasmic proteins. The absence of any organellar targeting peptide (mitochondrial, ER signal, peroxisomal PTS) and the presence of a soluble thioredoxin-fold domain together support a default cytoplasmic localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the protein as PhLP3 specifically would require lookup, but the elimination of the three distractors and the positive identification of a cytoplasmic thioredoxin-fold protein are achievable from sequence features alone.",
    "reason": "The three distractors represent highly specific structural/functional contexts (transmembrane transporter complex, membrane microdomain, DNA-damage repair focus) that each require distinctive sequence signatures absent from this small soluble protein. The remaining option, cytoplasm, is the biologically default location for a soluble protein with no targeting signals and a thioredoxin-like fold. This is a defensible reasoning chain from general protein-targeting biology."
  },
  "case_id": "GO_cellular_component_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (Q9VGV8, Phosducin-like protein 3 from Drosophila melanogaster) is annotated to GO:0005737 (cytoplasm) via IBA:GO_Central (H3) and to the more specific GO:0005829 (cytosol) via NAS:FlyBase (H4) and ECO:0000303 from a 2024 PubMed paper (C5). Since cytosol is part_of cytoplasm (GO2 ontology path), the broader annotation 'cytoplasm' is consistent with the evidence. The cytoplasm annotation itself is computational (IBA), but it is hierarchically supported by the more specific cytosol annotation. No annotation contradicts cytoplasmic localization."
  },
  "important_caveats": [
    "The cytoplasm (GO:0005737) annotation is via IBA (Inferred by Biological Aspect) from GO_Central, a computational transfer, not direct experimental evidence. The more specific cytosol annotation has stronger evidence (FlyBase NAS and a 2024 PubMed paper).",
    "The protein was only integrated into Swiss-Prot in June 2025; the benchmark's author source snapshot is unknown. If the benchmark predates Swiss-Prot integration, the annotation may have originated from a TrEMBL entry or FlyBase rather than curated UniProt.",
    "The thioredoxin-fold identification is based on sequence pattern recognition (CxxC motif and structural similarity); it is a reasonable inference but not a definitive fold assignment without structural data.",
    "All reviewer evidence is post-hoc and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different cellular contexts (membrane transporter complex, plasma-membrane microdomain, soluble compartment, nuclear DNA-damage site). The sequence clearly lacks features for A, B, and D, leaving C as the only viable option. The minor distinction between 'cytoplasm' and 'cytosol' (the latter being the more specific UniProt annotation) does not create ambiguity because cytosol is part_of cytoplasm in the GO hierarchy, and the question asks for 'primary Cellular Component,' for which the broader term is acceptable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q9VGV8, Phosducin-like protein 3 from Drosophila melanogaster) is annotated to GO:0005737 (cytoplasm) via IBA:GO_Central (H3) and to the more specific GO:0005829 (cytosol) via NAS:FlyBase (H4) and ECO:0000303 from a 2024 PubMed paper (C5). Since cytosol is part_of cytoplasm (GO2 ontology path), the broader annotation 'cytoplasm' is consistent with the evidence. The cytoplasm annotation itself is computational (IBA), but it is hierarchically supported by the more specific cytosol annotation. No annotation contradicts cytoplasmic localization.",
    "evidence_ids": ["H3", "H4", "C5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 216-aa sequence lacks all hallmark targeting features for the three distractors: (1) No transmembrane helices (~20+ hydrophobic residues) or Walker A/B nucleotide-binding motifs, ruling out an ABC transporter complex; (2) No caveolin-binding motif (aromatic-phi-X-phi-X-X-X-X-X-X-X-X-phi pattern) or membrane-anchoring signal, ruling out caveola; (3) No DNA-repair-associated domains (BRCT, FHA, RRM, kinase domains) or nuclear localization signal, ruling out site of double-strand break. The sequence instead contains a thioredoxin-like fold (CxxC motif visible in 'VCHFYRDSTERCKIVDMHLKILAAKHVEAKFCKVNAEKTPFLTQRLRIKVIPTIALVKDSKTKDFIVGFTDLGNCDDFATEMLEWRIAHSGAIDYKGDLMQPPDVKRKPFINRPQKTIRGGYDSDDSDIDLDD'), a fold commonly found in soluble cytoplasmic proteins. The absence of any organellar targeting peptide (mitochondrial, ER signal, peroxisomal PTS) and the presence of a soluble thioredoxin-fold domain together support a default cytoplasmic localization.",
    "missing_item_specific_fact": "None critical. Recognizing the protein as PhLP3 specifically would require lookup, but the elimination of the three distractors and the positive identification of a cytoplasmic thioredoxin-fold protein are achievable from sequence features alone.",
    "reason": "The three distractors represent highly specific structural/functional contexts (transmembrane transporter complex, membrane microdomain, DNA-damage repair focus) that each require distinctive sequence signatures absent from this small soluble protein. The remaining option, cytoplasm, is the biologically default location for a soluble protein with no targeting signals and a thioredoxin-like fold. This is a defensible reasoning chain from general protein-targeting biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different cellular contexts (membrane transporter complex, plasma-membrane microdomain, soluble compartment, nuclear DNA-damage site). The sequence clearly lacks features for A, B, and D, leaving C as the only viable option. The minor distinction between 'cytoplasm' and 'cytosol' (the latter being the more specific UniProt annotation) does not create ambiguity because cytosol is part_of cytoplasm in the GO hierarchy, and the question asks for 'primary Cellular Component,' for which the broader term is acceptable."
  },
  "important_caveats": [
    "The cytoplasm (GO:0005737) annotation is via IBA (Inferred by Biological Aspect) from GO_Central, a computational transfer, not direct experimental evidence. The more specific cytosol annotation has stronger evidence (FlyBase NAS and a 2024 PubMed paper).",
    "The protein was only integrated into Swiss-Prot in June 2025; the benchmark's author source snapshot is unknown. If the benchmark predates Swiss-Prot integration, the annotation may have originated from a TrEMBL entry or FlyBase rather than curated UniProt.",
    "The thioredoxin-fold identification is based on sequence pattern recognition (CxxC motif and structural similarity); it is a reasonable inference but not a definitive fold assignment without structural data.",
    "All reviewer evidence is post-hoc and was not available to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Invalid citation retained

> source_applicability is the name of a packet metadata object, not an assigned evidence_id. H3, H4 and C5 are valid source excerpts. The saved JSON therefore remains an invalid structured review under the approved citation schema.

Invalid assigned citation: `source_applicability`.

The actual saved parsed review is reproduced above. It remains an invalid structured review and is excluded from the 1,735 format-valid totals.

- **H3** — Historical cytoplasm annotation with IBA evidence. The quoted fact is present in the exact-sequence archived record. [Source](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205).
- **H4** — Historical cytosol annotation with NAS:FlyBase evidence. The quoted fact is present in the exact-sequence archived record. [Source](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205).
- **C5** — Current cytosol annotation with NAS:FlyBase evidence. The quoted fact matches the current cached JSON field; its sequence exactly matches the original question. [Source](https://rest.uniprot.org/uniprotkb/Q9VGV8.json).

**Remaining qualifications**

- The matching annotations are IBA/NAS assertions, not direct experimental localization evidence in these excerpts.
- The source trace does not independently validate the model reasoning_supported judgment. Solubility alone does not establish exclusive cytoplasmic localization; supplied GO5 also describes ABC complexes with separate ATP-binding components.
- The historical cytoplasm annotation and current cytosol annotation must remain distinguished by source snapshot.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9VGV8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 205. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGV8.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.511607+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000303","id":"39480878","source":"PubMed"}],"id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"NAS:FlyBase"}]}
```

Source SHA-256: `001fc5745522d199a9c119f27c0032aedc0754c9aa981b45c9211e06c04ae925`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)  
**Locator:** `lines 143-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 205 / 1.  
**Retrieved:** 2026-11-01T06:28:51.609437+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.
```

Source SHA-256: `ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGV8?format=txt&versions=205)  
**Locator:** `lines 144-144`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 205 / 1.  
**Retrieved:** 2026-11-01T06:28:51.609437+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; NAS:FlyBase.
```

Source SHA-256: `ee39c846a943511e3d8538c029ddef37e863da08eae5ba56de2e5fb1d1d03f00`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59936-59953`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005829
name: cytosol
namespace: cellular_component
def: "The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes." [GOC:hjd, GOC:jl]
subset: goslim_agr
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_plant
xref: NIF_Subcellular:sao101633890
xref: Wikipedia:Cytosol
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 244782-244797`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0043190
name: ATP-binding cassette (ABC) transporter complex
namespace: cellular_component
alt_id: GO:0043191
alt_id: GO:0043192
def: "A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter." [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]
subset: goslim_metagenomics
subset: goslim_pir
synonym: "ABC-type efflux permease complex" NARROW []
synonym: "ABC-type efflux porter complex" NARROW []
synonym: "ABC-type uptake permease complex" NARROW []
synonym: "mating pheromone exporter" NARROW []
is_a: GO:0098533 ! ATPase dependent transmembrane transport complex
is_a: GO:0098797 ! plasma membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
