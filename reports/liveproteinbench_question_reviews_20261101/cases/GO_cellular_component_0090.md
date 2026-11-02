# GO_cellular_component_0090

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — peroxisomal matrix

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. peroxisomal matrix
B. histone acetyltransferase complex
C. cell outer membrane
D. incipient cellular bud site
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

> The exact sequence has a computational GO annotation to peroxisomal matrix, and experimental evidence supports localization to peroxisomes in appressoria and infectious hyphae. The matrix-level assignment is computational rather than directly established by the cited localization evidence, and localization varies by fungal growth stage.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clearly decisive basis for distinguishing peroxisomal matrix localization from the other listed compartments; recognizing the protein or predicting from a trained model would not constitute reasoning from the supplied evidence.


**Missing item-specific fact**

> The protein-specific localization evidence and its stage dependence, along with the computational matrix annotation, are absent from the question input.


**Reason**

> Choosing A depends on item-specific localization knowledge. The choices make several alternatives biologically implausible, but that does not establish this protein's specific compartment from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the only listed option supported by the protein-specific evidence, but the wording's unqualified request for a primary location obscures stage-dependent localization, and cytosol—the reported main location in some stages—is not offered.


### Important caveats

- The exact sequence match supports applicability of the reviewed UniProt records, but the author's source snapshot is unknown.
- Experimental evidence establishes peroxisomal localization in particular fungal stages, not specifically matrix localization.
- The matrix-level GO assignment is computational; the protein is reported mainly in the cytosol in vegetative hyphae and conidia.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clearly decisive basis for distinguishing peroxisomal matrix localization from the other listed compartments; recognizing the protein or predicting from a trained model would not constitute reasoning from the supplied evidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence and its stage dependence, along with the computational matrix annotation, are absent from the question input.",
    "reason": "Choosing A depends on item-specific localization knowledge. The choices make several alternatives biologically implausible, but that does not establish this protein's specific compartment from the sequence."
  },
  "case_id": "GO_cellular_component_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence has a computational GO annotation to peroxisomal matrix, and experimental evidence supports localization to peroxisomes in appressoria and infectious hyphae. The matrix-level assignment is computational rather than directly established by the cited localization evidence, and localization varies by fungal growth stage."
  },
  "important_caveats": [
    "The exact sequence match supports applicability of the reviewed UniProt records, but the author's source snapshot is unknown.",
    "Experimental evidence establishes peroxisomal localization in particular fungal stages, not specifically matrix localization.",
    "The matrix-level GO assignment is computational; the protein is reported mainly in the cytosol in vegetative hyphae and conidia."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only listed option supported by the protein-specific evidence, but the wording's unqualified request for a primary location obscures stage-dependent localization, and cytosol—the reported main location in some stages—is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence has a computational GO annotation to peroxisomal matrix, and experimental evidence supports localization to peroxisomes in appressoria and infectious hyphae. The matrix-level assignment is computational rather than directly established by the cited localization evidence, and localization varies by fungal growth stage.",
    "evidence_ids": ["C5", "C7", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clearly decisive basis for distinguishing peroxisomal matrix localization from the other listed compartments; recognizing the protein or predicting from a trained model would not constitute reasoning from the supplied evidence.",
    "missing_item_specific_fact": "The protein-specific localization evidence and its stage dependence, along with the computational matrix annotation, are absent from the question input.",
    "reason": "Choosing A depends on item-specific localization knowledge. The choices make several alternatives biologically implausible, but that does not establish this protein's specific compartment from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only listed option supported by the protein-specific evidence, but the wording's unqualified request for a primary location obscures stage-dependent localization, and cytosol—the reported main location in some stages—is not offered."
  },
  "important_caveats": [
    "The exact sequence match supports applicability of the reviewed UniProt records, but the author's source snapshot is unknown.",
    "Experimental evidence establishes peroxisomal localization in particular fungal stages, not specifically matrix localization.",
    "The matrix-level GO assignment is computational; the protein is reported mainly in the cytosol in vegetative hyphae and conidia."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (G4NCP4, DCI1_PYRO7) is annotated as 'Peroxisomal di-isomerase DCI1' / Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, a peroxisomal beta-oxidation enzyme. Experimental evidence (ECO:0000269, PubMed:36774535) confirms peroxisomal localization (GO:0005777, EXP:UniProtKB). GO:0005782 (peroxisomal matrix) is annotated via IEA:TreeGrafter. The protein name explicitly includes 'Peroxisomal,' and its enzymatic function (dienoyl-CoA isomerase in beta-oxidation) is a canonical peroxisomal matrix activity. A complication exists: UniProt notes the protein is 'Mainly distributed in the cytosol in vegetative hyphae and conidia but localizes in peroxisomes in appressoria and infectious hyphae,' but cytosol is not among the answer choices, and the peroxisomal assignment remains the best-supported primary functional compartment among the given options.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of four options can be eliminated through general biological knowledge: (C) 'cell outer membrane' (GO:0009279) is a prokaryotic-specific term (goslim_prokaryote subset) describing a lipopolysaccharide-enriched outer membrane, inapplicable to a eukaryotic fungal cytoplasmic enzyme with no transmembrane/outer-membrane targeting features; (D) 'incipient cellular bud site' (GO:0000131) is defined specifically for budding yeast (S. cerevisiae) plasma membrane bud-site selection proteins, irrelevant to a filamentous ascomycete enzyme; (B) 'histone acetyltransferase complex' (GO:0000123) requires HAT domains, nuclear localization, and chromatin-part_of relationships, none of which are suggested by this 280-aa alpha/beta-hydrolase-fold metabolic enzyme. This leaves (A) peroxisomal matrix as the only viable option. Positive support for A comes from recognizing the sequence as a member of the alpha/beta-hydrolase superfamily involved in fatty acid beta-oxidation, a pathway compartmentalized in peroxisomes.


**Missing item-specific fact**

> Precise identification of the protein as dienoyl-CoA isomerase from sequence alone would require either memorization of this specific entry or confident structural/functional annotation; however, the elimination of B, C, D is robust enough that this is not strictly needed to select A.


**Reason**

> The elimination of options B, C, and D relies on general knowledge of GO term applicability (prokaryotic vs. eukaryotic, yeast-specific vs. general) and domain architecture (no HAT features), which is achievable without memorizing this particular protein's database entry. The remaining option A is consistent with the protein being a metabolic enzyme, and beta-oxidation enzymes are canonically peroxisomal.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has dual localization (cytosol and peroxisome depending on growth stage), cytosol is not among the options. Among the four given choices, only peroxisomal matrix is biologically defensible. The distinction between 'peroxisomal matrix' (IEA:TreeGrafter) and 'peroxisome' (EXP) is not relevant here since only 'peroxisomal matrix' appears as an option.


### Important caveats

- The GO annotation for 'peroxisomal matrix' (GO:0005782) is computational (IEA:TreeGrafter), not experimental; the experimental evidence supports 'peroxisome' (GO:0005777) at the organelle level.
- The protein's UniProt subcellular-location comment states it is 'Mainly distributed in the cytosol' in vegetative hyphae, with peroxisomal localization conditional on appressoria/infectious hyphae. The 'primary' assignment is somewhat context-dependent.
- The protein lacks a canonical PTS1 signal (C-terminus ends in ...KRHKL, not SKL/SRL), making peroxisomal targeting inference from sequence alone less straightforward.
- The identity of the protein (accession G4NCP4) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of four options can be eliminated through general biological knowledge: (C) 'cell outer membrane' (GO:0009279) is a prokaryotic-specific term (goslim_prokaryote subset) describing a lipopolysaccharide-enriched outer membrane, inapplicable to a eukaryotic fungal cytoplasmic enzyme with no transmembrane/outer-membrane targeting features; (D) 'incipient cellular bud site' (GO:0000131) is defined specifically for budding yeast (S. cerevisiae) plasma membrane bud-site selection proteins, irrelevant to a filamentous ascomycete enzyme; (B) 'histone acetyltransferase complex' (GO:0000123) requires HAT domains, nuclear localization, and chromatin-part_of relationships, none of which are suggested by this 280-aa alpha/beta-hydrolase-fold metabolic enzyme. This leaves (A) peroxisomal matrix as the only viable option. Positive support for A comes from recognizing the sequence as a member of the alpha/beta-hydrolase superfamily involved in fatty acid beta-oxidation, a pathway compartmentalized in peroxisomes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the protein as dienoyl-CoA isomerase from sequence alone would require either memorization of this specific entry or confident structural/functional annotation; however, the elimination of B, C, D is robust enough that this is not strictly needed to select A.",
    "reason": "The elimination of options B, C, and D relies on general knowledge of GO term applicability (prokaryotic vs. eukaryotic, yeast-specific vs. general) and domain architecture (no HAT features), which is achievable without memorizing this particular protein's database entry. The remaining option A is consistent with the protein being a metabolic enzyme, and beta-oxidation enzymes are canonically peroxisomal."
  },
  "case_id": "GO_cellular_component_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein (G4NCP4, DCI1_PYRO7) is annotated as 'Peroxisomal di-isomerase DCI1' / Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, a peroxisomal beta-oxidation enzyme. Experimental evidence (ECO:0000269, PubMed:36774535) confirms peroxisomal localization (GO:0005777, EXP:UniProtKB). GO:0005782 (peroxisomal matrix) is annotated via IEA:TreeGrafter. The protein name explicitly includes 'Peroxisomal,' and its enzymatic function (dienoyl-CoA isomerase in beta-oxidation) is a canonical peroxisomal matrix activity. A complication exists: UniProt notes the protein is 'Mainly distributed in the cytosol in vegetative hyphae and conidia but localizes in peroxisomes in appressoria and infectious hyphae,' but cytosol is not among the answer choices, and the peroxisomal assignment remains the best-supported primary functional compartment among the given options."
  },
  "important_caveats": [
    "The GO annotation for 'peroxisomal matrix' (GO:0005782) is computational (IEA:TreeGrafter), not experimental; the experimental evidence supports 'peroxisome' (GO:0005777) at the organelle level.",
    "The protein's UniProt subcellular-location comment states it is 'Mainly distributed in the cytosol' in vegetative hyphae, with peroxisomal localization conditional on appressoria/infectious hyphae. The 'primary' assignment is somewhat context-dependent.",
    "The protein lacks a canonical PTS1 signal (C-terminus ends in ...KRHKL, not SKL/SRL), making peroxisomal targeting inference from sequence alone less straightforward.",
    "The identity of the protein (accession G4NCP4) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual localization (cytosol and peroxisome depending on growth stage), cytosol is not among the options. Among the four given choices, only peroxisomal matrix is biologically defensible. The distinction between 'peroxisomal matrix' (IEA:TreeGrafter) and 'peroxisome' (EXP) is not relevant here since only 'peroxisomal matrix' appears as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (G4NCP4, DCI1_PYRO7) is annotated as 'Peroxisomal di-isomerase DCI1' / Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, a peroxisomal beta-oxidation enzyme. Experimental evidence (ECO:0000269, PubMed:36774535) confirms peroxisomal localization (GO:0005777, EXP:UniProtKB). GO:0005782 (peroxisomal matrix) is annotated via IEA:TreeGrafter. The protein name explicitly includes 'Peroxisomal,' and its enzymatic function (dienoyl-CoA isomerase in beta-oxidation) is a canonical peroxisomal matrix activity. A complication exists: UniProt notes the protein is 'Mainly distributed in the cytosol in vegetative hyphae and conidia but localizes in peroxisomes in appressoria and infectious hyphae,' but cytosol is not among the answer choices, and the peroxisomal assignment remains the best-supported primary functional compartment among the given options.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of four options can be eliminated through general biological knowledge: (C) 'cell outer membrane' (GO:0009279) is a prokaryotic-specific term (goslim_prokaryote subset) describing a lipopolysaccharide-enriched outer membrane, inapplicable to a eukaryotic fungal cytoplasmic enzyme with no transmembrane/outer-membrane targeting features; (D) 'incipient cellular bud site' (GO:0000131) is defined specifically for budding yeast (S. cerevisiae) plasma membrane bud-site selection proteins, irrelevant to a filamentous ascomycete enzyme; (B) 'histone acetyltransferase complex' (GO:0000123) requires HAT domains, nuclear localization, and chromatin-part_of relationships, none of which are suggested by this 280-aa alpha/beta-hydrolase-fold metabolic enzyme. This leaves (A) peroxisomal matrix as the only viable option. Positive support for A comes from recognizing the sequence as a member of the alpha/beta-hydrolase superfamily involved in fatty acid beta-oxidation, a pathway compartmentalized in peroxisomes.",
    "missing_item_specific_fact": "Precise identification of the protein as dienoyl-CoA isomerase from sequence alone would require either memorization of this specific entry or confident structural/functional annotation; however, the elimination of B, C, D is robust enough that this is not strictly needed to select A.",
    "reason": "The elimination of options B, C, and D relies on general knowledge of GO term applicability (prokaryotic vs. eukaryotic, yeast-specific vs. general) and domain architecture (no HAT features), which is achievable without memorizing this particular protein's database entry. The remaining option A is consistent with the protein being a metabolic enzyme, and beta-oxidation enzymes are canonically peroxisomal."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual localization (cytosol and peroxisome depending on growth stage), cytosol is not among the options. Among the four given choices, only peroxisomal matrix is biologically defensible. The distinction between 'peroxisomal matrix' (IEA:TreeGrafter) and 'peroxisome' (EXP) is not relevant here since only 'peroxisomal matrix' appears as an option."
  },
  "important_caveats": [
    "The GO annotation for 'peroxisomal matrix' (GO:0005782) is computational (IEA:TreeGrafter), not experimental; the experimental evidence supports 'peroxisome' (GO:0005777) at the organelle level.",
    "The protein's UniProt subcellular-location comment states it is 'Mainly distributed in the cytosol' in vegetative hyphae, with peroxisomal localization conditional on appressoria/infectious hyphae. The 'primary' assignment is somewhat context-dependent.",
    "The protein lacks a canonical PTS1 signal (C-terminus ends in ...KRHKL, not SKL/SRL), making peroxisomal targeting inference from sequence alone less straightforward.",
    "The identity of the protein (accession G4NCP4) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `G4NCP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"value":"Peroxisomal di-isomerase DCI1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36774535","source":"PubMed"}],"value":"5.3.3.21"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36774535","source":"PubMed"}],"value":"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase"}}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"value":"Mainly distributed in the cytosol in vegetative hyphae and conidia but localizes in peroxisomes in appressoria and infectious hyphae"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"id":"SL-0091","value":"Cytoplasm, cytosol"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"id":"SL-0204","value":"Peroxisome"}}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"database":"GO","id":"GO:0005782","properties":[{"key":"GoTerm","value":"C:peroxisomal matrix"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"id":"GO:0005777","properties":[{"key":"GoTerm","value":"C:peroxisome"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
ID   DCI1_PYRO7              Reviewed;         280 AA.
AC   G4NCP4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 50.
DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};
DE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};
DE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};
GN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 49-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:36774535}.
CC       Peroxisome {ECO:0000269|PubMed:36774535}. Note=Mainly distributed in
CC       the cytosol in vegetative hyphae and conidia but localizes in
CC       peroxisomes in appressoria and infectious hyphae.
CC       {ECO:0000269|PubMed:36774535}.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 89-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DR   GO; GO:0005782; C:peroxisomal matrix; IEA:TreeGrafter.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
