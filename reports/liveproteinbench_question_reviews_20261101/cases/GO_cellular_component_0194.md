# GO_cellular_component_0194

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMLPLLAVSAFASLGAAQTYTSCNPTNSLKTWSLSTDFTQGSSDGWTAISGNVTYGSNGAEFTINKRYDAPTLETNFYIFFGEVEVVMRAANGTGIVSSIVMESDDLDEIDWECTGTDTTQIQTNYFGKGNTTTYDRAIWETVSSPQDEFHTYKVVWTAAAITWYIDGTAVRTLEYADAVDGKNYPQTPMVVKLGIWAGGDPSNSEGTIEWAGGETDYDEVPFTMYVKSVNIINYNPAASYNYTDKTGSYTSIVASNSTTGSGIHSSNSVSVFAPSSSTSTFTSSRALIATASTYPASVQTSSSGVVSLSSSSASSSSAAASSTSGSASAVFTGAAVTNLPSFFFTVFFALAIALAF

[Multiple Choices]
A. peroxisome
B. ribosome
C. plasma membrane
D. H3 histone acetyltransferase complex
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

> The exact sequence matches the Crh-like protein 1 entry, whose annotation assigns it to the cell membrane with a GPI anchor and also to the cell wall. The plasma-membrane GO annotation is computational (IEA), not direct experimental localization evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal peptide and a hydrophobic C-terminal segment consistent with a GPI-anchor signal. Together these support entry into the secretory pathway and membrane association, distinguishing plasma membrane from the intracellular peroxisome, ribosome, and histone-acetyltransferase-complex choices.


**Missing item-specific fact**

> No item-specific annotation is needed to distinguish the listed choices; exact localization between plasma membrane and fungal cell wall would require additional information.


**Reason**

> The sequence contains meaningful targeting and anchoring cues for a secreted, GPI-anchored protein. These support the membrane choice among the options, though they do not establish its precise distribution in vivo.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports the plasma-membrane option over the other listed compartments. The protein may also be associated with the cell wall, but that is not an option.


### Important caveats

- The supplied sequence alone does not prove plasma-membrane localization or distinguish it conclusively from cell-wall localization.
- The supporting UniProt subcellular-location and GO annotations are computational; the cited functional paper is not, in the supplied evidence, direct validation of localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide and a hydrophobic C-terminal segment consistent with a GPI-anchor signal. Together these support entry into the secretory pathway and membrane association, distinguishing plasma membrane from the intracellular peroxisome, ribosome, and histone-acetyltransferase-complex choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish the listed choices; exact localization between plasma membrane and fungal cell wall would require additional information.",
    "reason": "The sequence contains meaningful targeting and anchoring cues for a secreted, GPI-anchored protein. These support the membrane choice among the options, though they do not establish its precise distribution in vivo."
  },
  "case_id": "GO_cellular_component_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Crh-like protein 1 entry, whose annotation assigns it to the cell membrane with a GPI anchor and also to the cell wall. The plasma-membrane GO annotation is computational (IEA), not direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied sequence alone does not prove plasma-membrane localization or distinguish it conclusively from cell-wall localization.",
    "The supporting UniProt subcellular-location and GO annotations are computational; the cited functional paper is not, in the supplied evidence, direct validation of localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports the plasma-membrane option over the other listed compartments. The protein may also be associated with the cell wall, but that is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Crh-like protein 1 entry, whose annotation assigns it to the cell membrane with a GPI anchor and also to the cell wall. The plasma-membrane GO annotation is computational (IEA), not direct experimental localization evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide and a hydrophobic C-terminal segment consistent with a GPI-anchor signal. Together these support entry into the secretory pathway and membrane association, distinguishing plasma membrane from the intracellular peroxisome, ribosome, and histone-acetyltransferase-complex choices.",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish the listed choices; exact localization between plasma membrane and fungal cell wall would require additional information.",
    "reason": "The sequence contains meaningful targeting and anchoring cues for a secreted, GPI-anchored protein. These support the membrane choice among the options, though they do not establish its precise distribution in vivo."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports the plasma-membrane option over the other listed compartments. The protein may also be associated with the cell wall, but that is not an option."
  },
  "important_caveats": [
    "The supplied sequence alone does not prove plasma-membrane localization or distinguish it conclusively from cell-wall localization.",
    "The supporting UniProt subcellular-location and GO annotations are computational; the cited functional paper is not, in the supplied evidence, direct validation of localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WD22 (CRH1_ASPFU) annotates the protein with 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255) and GO:0005886 (plasma membrane, IEA:UniProtKB-SubCell). The C-terminal hydrophobic region (FTGAAVTNLPSFFFTVFFALAIALAF) is consistent with a GPI-anchor signal sequence, supporting membrane association. The annotation is computational (ECO:0000255, IEA), not directly experimental, but GPI-anchored proteins are by definition tethered to the outer leaflet of the plasma membrane. The protein is also annotated 'Secreted, cell wall' (ECO:0000305), but among the four choices, plasma membrane is the only compartment consistent with a GPI-anchored secretory protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating entry into the secretory pathway, which immediately eliminates ribosome (B, cytoplasmic translation machinery) and H3 histone acetyltransferase complex (D, nuclear chromatin complex). The absence of peroxisomal targeting signals (PTS1: SKL-type tripeptide; PTS2: N-terminal nonapeptide) and the chitinase catalytic domain (WAGGDPS…WAGGETDYDE, GH18 family) eliminate peroxisome (A). The C-terminal hydrophobic stretch (FTGAAVTNLPSFFFTVFFALAIALAF) is a canonical GPI-anchor signal sequence, and the Ser/Thr-rich O-glycosylation linker is characteristic of fungal cell wall proteins. GPI-anchored proteins are tethered to the outer leaflet of the plasma membrane, making C the only viable option. This reasoning uses general knowledge of signal peptides, GPI anchors, and fungal cell wall protein architecture.


**Missing item-specific fact**

> None critical. The specific identification of this protein as Crh1 from A. fumigatus is not needed; the sequence features alone support the answer.


**Reason**

> The N-terminal signal peptide, C-terminal GPI-anchor signal, and absence of organelle-specific targeting sequences provide concrete, generalizable biological grounds to eliminate A, B, and D and select C. Recognizing a GPI-anchor signal and knowing GPI-anchored proteins associate with the plasma membrane is standard cell biology knowledge, not a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors (peroxisome, ribosome, H3 HAT complex) are clearly incompatible with a secreted, GPI-anchored fungal cell wall protein. The UniProt annotation also lists 'Secreted, cell wall,' but 'cell wall' is not among the choices, so no ambiguity arises. Plasma membrane is the only option consistent with a GPI-anchored protein.


### Important caveats

- The plasma membrane annotation in UniProt is computational (ECO:0000255, IEA:UniProtKB-SubCell), based on a GPI-anchor prediction rule, not direct experimental localization.
- The protein's functional site is the cell wall (chitin remodeling), where it is secreted and GPI-anchored; 'plasma membrane' reflects the tethering point rather than the site of enzymatic action.
- The sequence match to Q4WD22 is confirmed (SHA-256 identical, 357 AA), and the historical entry (v107, Swiss-Prot, first released Jan 2026) carries the same subcellular location annotation.
- The GO term plasma membrane (GO:0005886) has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating entry into the secretory pathway, which immediately eliminates ribosome (B, cytoplasmic translation machinery) and H3 histone acetyltransferase complex (D, nuclear chromatin complex). The absence of peroxisomal targeting signals (PTS1: SKL-type tripeptide; PTS2: N-terminal nonapeptide) and the chitinase catalytic domain (WAGGDPS…WAGGETDYDE, GH18 family) eliminate peroxisome (A). The C-terminal hydrophobic stretch (FTGAAVTNLPSFFFTVFFALAIALAF) is a canonical GPI-anchor signal sequence, and the Ser/Thr-rich O-glycosylation linker is characteristic of fungal cell wall proteins. GPI-anchored proteins are tethered to the outer leaflet of the plasma membrane, making C the only viable option. This reasoning uses general knowledge of signal peptides, GPI anchors, and fungal cell wall protein architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific identification of this protein as Crh1 from A. fumigatus is not needed; the sequence features alone support the answer.",
    "reason": "The N-terminal signal peptide, C-terminal GPI-anchor signal, and absence of organelle-specific targeting sequences provide concrete, generalizable biological grounds to eliminate A, B, and D and select C. Recognizing a GPI-anchor signal and knowing GPI-anchored proteins associate with the plasma membrane is standard cell biology knowledge, not a protein-specific lookup."
  },
  "case_id": "GO_cellular_component_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 (CRH1_ASPFU) annotates the protein with 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255) and GO:0005886 (plasma membrane, IEA:UniProtKB-SubCell). The C-terminal hydrophobic region (FTGAAVTNLPSFFFTVFFALAIALAF) is consistent with a GPI-anchor signal sequence, supporting membrane association. The annotation is computational (ECO:0000255, IEA), not directly experimental, but GPI-anchored proteins are by definition tethered to the outer leaflet of the plasma membrane. The protein is also annotated 'Secreted, cell wall' (ECO:0000305), but among the four choices, plasma membrane is the only compartment consistent with a GPI-anchored secretory protein."
  },
  "important_caveats": [
    "The plasma membrane annotation in UniProt is computational (ECO:0000255, IEA:UniProtKB-SubCell), based on a GPI-anchor prediction rule, not direct experimental localization.",
    "The protein's functional site is the cell wall (chitin remodeling), where it is secreted and GPI-anchored; 'plasma membrane' reflects the tethering point rather than the site of enzymatic action.",
    "The sequence match to Q4WD22 is confirmed (SHA-256 identical, 357 AA), and the historical entry (v107, Swiss-Prot, first released Jan 2026) carries the same subcellular location annotation.",
    "The GO term plasma membrane (GO:0005886) has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (peroxisome, ribosome, H3 HAT complex) are clearly incompatible with a secreted, GPI-anchored fungal cell wall protein. The UniProt annotation also lists 'Secreted, cell wall,' but 'cell wall' is not among the choices, so no ambiguity arises. Plasma membrane is the only option consistent with a GPI-anchored protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WD22 (CRH1_ASPFU) annotates the protein with 'Cell membrane; Lipid-anchor, GPI-anchor' (ECO:0000255) and GO:0005886 (plasma membrane, IEA:UniProtKB-SubCell). The C-terminal hydrophobic region (FTGAAVTNLPSFFFTVFFALAIALAF) is consistent with a GPI-anchor signal sequence, supporting membrane association. The annotation is computational (ECO:0000255, IEA), not directly experimental, but GPI-anchored proteins are by definition tethered to the outer leaflet of the plasma membrane. The protein is also annotated 'Secreted, cell wall' (ECO:0000305), but among the four choices, plasma membrane is the only compartment consistent with a GPI-anchored secretory protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MMLPLLAVSAFASLGAAQ) indicating entry into the secretory pathway, which immediately eliminates ribosome (B, cytoplasmic translation machinery) and H3 histone acetyltransferase complex (D, nuclear chromatin complex). The absence of peroxisomal targeting signals (PTS1: SKL-type tripeptide; PTS2: N-terminal nonapeptide) and the chitinase catalytic domain (WAGGDPS…WAGGETDYDE, GH18 family) eliminate peroxisome (A). The C-terminal hydrophobic stretch (FTGAAVTNLPSFFFTVFFALAIALAF) is a canonical GPI-anchor signal sequence, and the Ser/Thr-rich O-glycosylation linker is characteristic of fungal cell wall proteins. GPI-anchored proteins are tethered to the outer leaflet of the plasma membrane, making C the only viable option. This reasoning uses general knowledge of signal peptides, GPI anchors, and fungal cell wall protein architecture.",
    "missing_item_specific_fact": "None critical. The specific identification of this protein as Crh1 from A. fumigatus is not needed; the sequence features alone support the answer.",
    "reason": "The N-terminal signal peptide, C-terminal GPI-anchor signal, and absence of organelle-specific targeting sequences provide concrete, generalizable biological grounds to eliminate A, B, and D and select C. Recognizing a GPI-anchor signal and knowing GPI-anchored proteins associate with the plasma membrane is standard cell biology knowledge, not a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (peroxisome, ribosome, H3 HAT complex) are clearly incompatible with a secreted, GPI-anchored fungal cell wall protein. The UniProt annotation also lists 'Secreted, cell wall,' but 'cell wall' is not among the choices, so no ambiguity arises. Plasma membrane is the only option consistent with a GPI-anchored protein."
  },
  "important_caveats": [
    "The plasma membrane annotation in UniProt is computational (ECO:0000255, IEA:UniProtKB-SubCell), based on a GPI-anchor prediction rule, not direct experimental localization.",
    "The protein's functional site is the cell wall (chitin remodeling), where it is secreted and GPI-anchored; 'plasma membrane' reflects the tethering point rather than the site of enzymatic action.",
    "The sequence match to Q4WD22 is confirmed (SHA-256 identical, 357 AA), and the historical entry (v107, Swiss-Prot, first released Jan 2026) carries the same subcellular location annotation.",
    "The GO term plasma membrane (GO:0005886) has 'cell membrane' as an EXACT synonym, so the UniProt 'Cell membrane' annotation maps directly to the option text."
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

**Accession:** `Q4WD22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.374081+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitinase crh1"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30971696","source":"PubMed"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitin transglycosylase crh1"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Crh-like protein 1"}}}
```

Source SHA-256: `2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.374081+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0041","value":"Secreted, cell wall"}}]}
```

Source SHA-256: `2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WD22.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.374081+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `2b5098e0eef6293d750026739a991df11b8ed9fc88d7ba6c46a2dddd8788bf00`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)  
**Locator:** `lines 65-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:34.790448+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Lipid-anchor, GPI-
CC       anchor {ECO:0000255}. Secreted, cell wall {ECO:0000305}.
```

Source SHA-256: `77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:34.790448+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WD22?format=txt&versions=107)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:34.790448+00:00.  

```text
DR   GO; GO:0098552; C:side of membrane; IEA:UniProtKB-KW.
```

Source SHA-256: `77033a3b4dcbfe2a0b079eb850f5fe45877250853ab15f376544c19a4d49ea3b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
