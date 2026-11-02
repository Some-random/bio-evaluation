# GO_cellular_component_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. apical part of cell
B. viral nucleocapsid
C. cytosol
D. SCF ubiquitin ligase complex
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

> The exact sequence matches a UniProt record annotated to cytosol (GO:0005829). This is computational evidence (IEA:TreeGrafter), not evidence of direct experimental localization; the record also identifies the protein as indigoidine synthase from Streptomyces lavendulae.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long, enzyme-like protein with no obvious N-terminal secretion signal or extended hydrophobic transmembrane segment. A soluble bacterial enzyme is plausibly cytosolic, whereas the other choices describe a polarized-cell region, a viral structure, or a eukaryotic ubiquitin-ligase complex.


**Missing item-specific fact**

> Direct localization evidence would be needed to establish the protein's actual cellular location, but the sequence and choices provide a meaningful basis for selecting cytosol as the most likely option.


**Reason**

> The distractors are biologically poorly matched to a soluble bacterial enzyme, so general sequence and biological reasoning meaningfully favors cytosol. The reviewer-only annotation supports the key but is not needed as input for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, cytosol is the clearly best fit for a soluble bacterial enzyme.


### Important caveats

- The cited UniProt cellular-component annotation is computational (IEA:TreeGrafter), not experimentally established in the supplied evidence.
- Reviewer-only accession and annotation evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long, enzyme-like protein with no obvious N-terminal secretion signal or extended hydrophobic transmembrane segment. A soluble bacterial enzyme is plausibly cytosolic, whereas the other choices describe a polarized-cell region, a viral structure, or a eukaryotic ubiquitin-ligase complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct localization evidence would be needed to establish the protein's actual cellular location, but the sequence and choices provide a meaningful basis for selecting cytosol as the most likely option.",
    "reason": "The distractors are biologically poorly matched to a soluble bacterial enzyme, so general sequence and biological reasoning meaningfully favors cytosol. The reviewer-only annotation supports the key but is not needed as input for that inference."
  },
  "case_id": "GO_cellular_component_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to cytosol (GO:0005829). This is computational evidence (IEA:TreeGrafter), not evidence of direct experimental localization; the record also identifies the protein as indigoidine synthase from Streptomyces lavendulae."
  },
  "important_caveats": [
    "The cited UniProt cellular-component annotation is computational (IEA:TreeGrafter), not experimentally established in the supplied evidence.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, cytosol is the clearly best fit for a soluble bacterial enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated to cytosol (GO:0005829). This is computational evidence (IEA:TreeGrafter), not evidence of direct experimental localization; the record also identifies the protein as indigoidine synthase from Streptomyces lavendulae.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long, enzyme-like protein with no obvious N-terminal secretion signal or extended hydrophobic transmembrane segment. A soluble bacterial enzyme is plausibly cytosolic, whereas the other choices describe a polarized-cell region, a viral structure, or a eukaryotic ubiquitin-ligase complex.",
    "missing_item_specific_fact": "Direct localization evidence would be needed to establish the protein's actual cellular location, but the sequence and choices provide a meaningful basis for selecting cytosol as the most likely option.",
    "reason": "The distractors are biologically poorly matched to a soluble bacterial enzyme, so general sequence and biological reasoning meaningfully favors cytosol. The reviewer-only annotation supports the key but is not needed as input for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, cytosol is the clearly best fit for a soluble bacterial enzyme."
  },
  "important_caveats": [
    "The cited UniProt cellular-component annotation is computational (IEA:TreeGrafter), not experimentally established in the supplied evidence.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Q1MWN4, Indigoidine synthase (bpsA), a single-module non-ribosomal peptide synthetase (NRPS, EC 4.3.3.9) from Streptomyces lavendulae. UniProt annotates GO:0005829 (cytosol) with evidence code IEA:TreeGrafter (computational transfer). However, the biological reasoning independently and strongly supports cytosol: (1) it is a bacterial enzyme with no signal peptide, no transmembrane domains, and no organelle-targeting motifs; (2) NRPS enzymes are well-characterized cytoplasmic multi-domain enzymes that synthesize secondary metabolite peptides in the bacterial cytoplasm; (3) the sequence contains canonical NRPS adenylation (A) domain motifs (e.g., 'YTSFGSTGKPKG') and a thiolation (T/PCP) domain with phosphopantetheinylation at Ser-972, confirming it as a soluble cytoplasmic biosynthetic enzyme. The distractors are all eukaryotic- or virus-specific structures inapplicable to a bacterial NRPS.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark NRPS domain signatures (adenylation domain motif 'TSGSTGKPKG', thiolation/PCP domain with phosphopantetheinylation site), identifying it as a non-ribosomal peptide synthetase. NRPS enzymes in bacteria are soluble cytoplasmic enzymes that catalyze peptide bond formation for secondary metabolite biosynthesis. The organism is a bacterium (Streptomyces), which lacks membrane-bound organelles, membrane polarity (no apical/basal distinction), and eukaryotic protein-degradation machinery (SCF complex). The protein is not a viral structural protein. These general biological facts allow elimination of all three distractors and selection of cytosol without knowing this specific protein's database annotation.


**Missing item-specific fact**

> None critical. The GO annotation is IEA:TreeGrafter (computational), but the answer follows from general knowledge of bacterial cell biology, NRPS biochemistry, and the inapplicability of eukaryotic/viral structures to a bacterial enzyme.


**Reason**

> A model with general biological knowledge can: (1) recognize NRPS domain architecture from the sequence motifs, (2) recall that bacterial NRPS enzymes are cytoplasmic, (3) eliminate 'apical part of cell' as a eukaryotic epithelial concept, (4) eliminate 'viral nucleocapsid' because this is a bacterial enzyme not a viral protein, and (5) eliminate 'SCF ubiquitin ligase complex' as a eukaryotic protein-degradation complex absent in bacteria. No item-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> All three distractors are clearly inapplicable to a bacterial NRPS enzyme. 'Apical part of cell' refers to polarized eukaryotic epithelial cells; 'viral nucleocapsid' applies to viral structural proteins; 'SCF ubiquitin ligase complex' is a eukaryotic protein-degradation complex. None of these compartments or structures exist in or apply to a Streptomyces cytoplasmic biosynthetic enzyme. Cytosol is the sole defensible answer.


### Important caveats

- The GO:0005829 annotation carries evidence code IEA:TreeGrafter, meaning it is a computational phylogenetic transfer rather than direct experimental localization. However, the biological reasoning independently supports cytosol.
- The UniProt entry was first publicly released in 2025-02-05, so the benchmark author may have sourced this from a pre-publication or early-release snapshot; the sequence match is confirmed across versions.
- The identity of this protein (accession Q1MWN4) was inferred by the reviewer from dataset metadata, not from the model input; the model must rely on sequence-based reasoning alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark NRPS domain signatures (adenylation domain motif 'TSGSTGKPKG', thiolation/PCP domain with phosphopantetheinylation site), identifying it as a non-ribosomal peptide synthetase. NRPS enzymes in bacteria are soluble cytoplasmic enzymes that catalyze peptide bond formation for secondary metabolite biosynthesis. The organism is a bacterium (Streptomyces), which lacks membrane-bound organelles, membrane polarity (no apical/basal distinction), and eukaryotic protein-degradation machinery (SCF complex). The protein is not a viral structural protein. These general biological facts allow elimination of all three distractors and selection of cytosol without knowing this specific protein's database annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The GO annotation is IEA:TreeGrafter (computational), but the answer follows from general knowledge of bacterial cell biology, NRPS biochemistry, and the inapplicability of eukaryotic/viral structures to a bacterial enzyme.",
    "reason": "A model with general biological knowledge can: (1) recognize NRPS domain architecture from the sequence motifs, (2) recall that bacterial NRPS enzymes are cytoplasmic, (3) eliminate 'apical part of cell' as a eukaryotic epithelial concept, (4) eliminate 'viral nucleocapsid' because this is a bacterial enzyme not a viral protein, and (5) eliminate 'SCF ubiquitin ligase complex' as a eukaryotic protein-degradation complex absent in bacteria. No item-specific memorization is required."
  },
  "case_id": "GO_cellular_component_0043",
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
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is Q1MWN4, Indigoidine synthase (bpsA), a single-module non-ribosomal peptide synthetase (NRPS, EC 4.3.3.9) from Streptomyces lavendulae. UniProt annotates GO:0005829 (cytosol) with evidence code IEA:TreeGrafter (computational transfer). However, the biological reasoning independently and strongly supports cytosol: (1) it is a bacterial enzyme with no signal peptide, no transmembrane domains, and no organelle-targeting motifs; (2) NRPS enzymes are well-characterized cytoplasmic multi-domain enzymes that synthesize secondary metabolite peptides in the bacterial cytoplasm; (3) the sequence contains canonical NRPS adenylation (A) domain motifs (e.g., 'YTSFGSTGKPKG') and a thiolation (T/PCP) domain with phosphopantetheinylation at Ser-972, confirming it as a soluble cytoplasmic biosynthetic enzyme. The distractors are all eukaryotic- or virus-specific structures inapplicable to a bacterial NRPS."
  },
  "important_caveats": [
    "The GO:0005829 annotation carries evidence code IEA:TreeGrafter, meaning it is a computational phylogenetic transfer rather than direct experimental localization. However, the biological reasoning independently supports cytosol.",
    "The UniProt entry was first publicly released in 2025-02-05, so the benchmark author may have sourced this from a pre-publication or early-release snapshot; the sequence match is confirmed across versions.",
    "The identity of this protein (accession Q1MWN4) was inferred by the reviewer from dataset metadata, not from the model input; the model must rely on sequence-based reasoning alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors are clearly inapplicable to a bacterial NRPS enzyme. 'Apical part of cell' refers to polarized eukaryotic epithelial cells; 'viral nucleocapsid' applies to viral structural proteins; 'SCF ubiquitin ligase complex' is a eukaryotic protein-degradation complex. None of these compartments or structures exist in or apply to a Streptomyces cytoplasmic biosynthetic enzyme. Cytosol is the sole defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Q1MWN4, Indigoidine synthase (bpsA), a single-module non-ribosomal peptide synthetase (NRPS, EC 4.3.3.9) from Streptomyces lavendulae. UniProt annotates GO:0005829 (cytosol) with evidence code IEA:TreeGrafter (computational transfer). However, the biological reasoning independently and strongly supports cytosol: (1) it is a bacterial enzyme with no signal peptide, no transmembrane domains, and no organelle-targeting motifs; (2) NRPS enzymes are well-characterized cytoplasmic multi-domain enzymes that synthesize secondary metabolite peptides in the bacterial cytoplasm; (3) the sequence contains canonical NRPS adenylation (A) domain motifs (e.g., 'YTSFGSTGKPKG') and a thiolation (T/PCP) domain with phosphopantetheinylation at Ser-972, confirming it as a soluble cytoplasmic biosynthetic enzyme. The distractors are all eukaryotic- or virus-specific structures inapplicable to a bacterial NRPS.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark NRPS domain signatures (adenylation domain motif 'TSGSTGKPKG', thiolation/PCP domain with phosphopantetheinylation site), identifying it as a non-ribosomal peptide synthetase. NRPS enzymes in bacteria are soluble cytoplasmic enzymes that catalyze peptide bond formation for secondary metabolite biosynthesis. The organism is a bacterium (Streptomyces), which lacks membrane-bound organelles, membrane polarity (no apical/basal distinction), and eukaryotic protein-degradation machinery (SCF complex). The protein is not a viral structural protein. These general biological facts allow elimination of all three distractors and selection of cytosol without knowing this specific protein's database annotation.",
    "missing_item_specific_fact": "None critical. The GO annotation is IEA:TreeGrafter (computational), but the answer follows from general knowledge of bacterial cell biology, NRPS biochemistry, and the inapplicability of eukaryotic/viral structures to a bacterial enzyme.",
    "reason": "A model with general biological knowledge can: (1) recognize NRPS domain architecture from the sequence motifs, (2) recall that bacterial NRPS enzymes are cytoplasmic, (3) eliminate 'apical part of cell' as a eukaryotic epithelial concept, (4) eliminate 'viral nucleocapsid' because this is a bacterial enzyme not a viral protein, and (5) eliminate 'SCF ubiquitin ligase complex' as a eukaryotic protein-degradation complex absent in bacteria. No item-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors are clearly inapplicable to a bacterial NRPS enzyme. 'Apical part of cell' refers to polarized eukaryotic epithelial cells; 'viral nucleocapsid' applies to viral structural proteins; 'SCF ubiquitin ligase complex' is a eukaryotic protein-degradation complex. None of these compartments or structures exist in or apply to a Streptomyces cytoplasmic biosynthetic enzyme. Cytosol is the sole defensible answer."
  },
  "important_caveats": [
    "The GO:0005829 annotation carries evidence code IEA:TreeGrafter, meaning it is a computational phylogenetic transfer rather than direct experimental localization. However, the biological reasoning independently supports cytosol.",
    "The UniProt entry was first publicly released in 2025-02-05, so the benchmark author may have sourced this from a pre-publication or early-release snapshot; the sequence match is confirmed across versions.",
    "The identity of this protein (accession Q1MWN4) was inferred by the reviewer from dataset metadata, not from the model input; the model must rely on sequence-based reasoning alone."
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

**Accession:** `Q1MWN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
"Q1MWN4"
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Kitasatosporales","Streptomycetaceae","Streptomyces"],"scientificName":"Streptomyces lavendulae","taxonId":1914}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue pigment synthetase-encoding gene A"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue-pigment synthetase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"citation":{"authors":["Takahashi H.","Kumagai T.","Kitani K.","Mori M.","Matoba Y.","Sugiyama M."],"citationCrossReferences":[{"database":"PubMed","id":"17237222"},{"database":"DOI","id":"10.1074/jbc.m611319200"}],"citationType":"journal article","firstPage":"9073","id":"17237222","journal":"J. Biol. Chem.","lastPage":"9081","publicationDate":"2007","title":"Cloning and characterization of a Streptomyces single module type non-ribosomal peptide synthetase catalyzing a blue pigment synthesis.","volume":"282"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAE93896.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 11924 / 8197-20"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","DOMAIN","PHOSPHOPANTETHEINYLATION AT SER-972","MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608"]}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
ID   INDGS_STRLA             Reviewed;        1282 AA.
AC   Q1MWN4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   30-MAY-2006, sequence version 1.
DT   28-JAN-2026, entry version 86.
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};
DE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};
DE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};
GN   Name=bpsA {ECO:0000303|PubMed:17237222};
OS   Streptomyces lavendulae.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=1914;
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAE93896.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, DOMAIN, PHOSPHOPANTETHEINYLATION AT
RP   SER-972, AND MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608.
RC   STRAIN=ATCC 11924 / 8197-20;
RX   PubMed=17237222; DOI=10.1074/jbc.m611319200;
RA   Takahashi H., Kumagai T., Kitani K., Mori M., Matoba Y., Sugiyama M.;
RT   "Cloning and characterization of a Streptomyces single module type non-
RT   ribosomal peptide synthetase catalyzing a blue pigment synthesis.";
RL   J. Biol. Chem. 282:9073-9081(2007).
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 78-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence GO1

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
