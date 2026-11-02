# GO_cellular_component_0082

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — endosome membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAKAIQYNIKVDLHEVKDLSFREAAGEKEIVPNPYIEVTVNGVTKTTIQKTQVVSATFNTSFNFTAYLTPDEFARSYVEVAVLHKYMLIGGVGLQSAVIGKYVFSFAYVYTKSQHWIYRQWVTLRNLDQPQDETGLLLITVGVFGPGDAMPVVDETVCVVNEGERTSTDVNVKLTHYSLSVNIFKGQDIPSVAGQFSTVLEPYVKVKHGGAELQTRPLPDSNPDWLASISIPACVPCFDGNVLVELWNGQDSSTAAGTLMGTVVLDYFQLIKNDLPPRWFNFYWRPPAEGLLGAVTDMMASAELREPIAYGGRILLSASAAKVQTPLPLGVRSARPIPDPATQECVWWLDLYEMTSATGYTSELRIEIAFGPHVIKTASLEANALGTYVIGDNLGRLPEMKIFAPVDEVQVWDVMMYVCSPPATTVAAGIADISNWFSGWGGSPTATQNTPEPAETPWTRLAWVRIPYDSRQFQNGKPQWYSLRSLDGSGTDMFSVLLGMEMFPTKAGKQRAPRLEYKLARFYFRALIYEGLHLPAVGYDVFPDPYIQVELASKTLRTSTIRQTLNPSYYEAYEIEIRLPENISLAPDINVEVISESNSLLSSDVVLGSVQYPIQKVPKEWTKAPVWLQLHSKAYPRCKARVLVAFELVPAEKAEDDTYPFYDDIRPSTKEGNIRLFLVGVRLFKPITQPFVTVCFGRDVENTAEPLWSQESSAPRTGEGGNWNFLEEFTVSVSLPKRMQHHSFLEVKIQDRTQGIGGESNVDVGMAYITLNPLLPWLDSRERAESLETFRLQMLEEVLIEDAENARRSADGGLAARTGGGSFDEDATKKKEMLAAERSRKMAIPYNDPDMANLKIEEVDDYVSFKVAPRPQASRLSREGTSRDERGKAPGKSLSGMPGPVARASPGAGEETEKKGDPVAEKKEGGAQAAPPVAPSAHQREALAASPEEETYGFTPEQLNFVLADLEEDDAEEMTRDEVPYELEADFTVDDLPYLRTPIFRPTDAGVPETVGYLKYVCRVFQSTDEDEGAEMDAVCKSLIETYNSTRDLVVRAYVLAARGLVPPSGASDIQTYVWIQDSENAATLPGGLSYNIRDTGYTKKQGFKPEFNRCYTLACSLPENSIVQIAVMNMGRLTDECIGRTYLDVEDRFFNKKVEQMVIEESTPIELRTLKNEGSTVSHGSLRGFFEIMRADYAQLHPPYTLASAEPDEYQLRVVIWRVKAVPLDDNSSISLFVRTIYQLEDSSEIVKDTDTHYNSTDGTAVYNWRMVFDVLIPAQIPVLKLQIWNYALLSSTEPIGEANFDLTADFFRARKRQQHYRVPRMWVRCSHPAHKGKLRGTIEIEASILPREEAEYTPVGNGRDEPNRDPFLPAVTTNRTYIDWQQIGETVGAASSAIMSGLKWTGVWMTVAGIIALVIFVMFLLK

[Multiple Choices]
A. mitochondrial inner membrane
B. external side of plasma membrane
C. host cell
D. endosome membrane
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

> The exact sequence matches the Toxoplasma gondii FER1 entry. Its subcellular-location annotation reports endosome membrane localization, and the GO endosome-membrane annotation is supported by IDA evidence. The annotation also describes localization to the trans-Golgi–endosome network in intracellular parasites.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic segment is consistent with a membrane anchor, which can support membrane association but does not distinguish an endosome membrane from the other candidate compartments.


**Missing item-specific fact**

> The protein-specific localization of Toxoplasma FER1 to the trans-Golgi–endosome network, including the endosome membrane, is not supplied in the question.


**Reason**

> Choosing D requires the protein-specific localization evidence; the sequence and general biological knowledge do not meaningfully resolve this precise compartment among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D among the listed options. The annotation reports other locations and varies by parasite state, but cytoplasm and trans-Golgi network membrane are not choices, and the supplied evidence does not support the other listed compartments.


### Important caveats

- The localization annotation is tied to cited experimental evidence (IDA); the underlying study was not independently reviewed here.
- The annotation describes different localization in intracellular and extracellular parasites, while the question does not specify parasite state.
- The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal hydrophobic segment is consistent with a membrane anchor, which can support membrane association but does not distinguish an endosome membrane from the other candidate compartments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization of Toxoplasma FER1 to the trans-Golgi–endosome network, including the endosome membrane, is not supplied in the question.",
    "reason": "Choosing D requires the protein-specific localization evidence; the sequence and general biological knowledge do not meaningfully resolve this precise compartment among the choices."
  },
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Toxoplasma gondii FER1 entry. Its subcellular-location annotation reports endosome membrane localization, and the GO endosome-membrane annotation is supported by IDA evidence. The annotation also describes localization to the trans-Golgi–endosome network in intracellular parasites."
  },
  "important_caveats": [
    "The localization annotation is tied to cited experimental evidence (IDA); the underlying study was not independently reviewed here.",
    "The annotation describes different localization in intracellular and extracellular parasites, while the question does not specify parasite state.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D among the listed options. The annotation reports other locations and varies by parasite state, but cytoplasm and trans-Golgi network membrane are not choices, and the supplied evidence does not support the other listed compartments."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Toxoplasma gondii FER1 entry. Its subcellular-location annotation reports endosome membrane localization, and the GO endosome-membrane annotation is supported by IDA evidence. The annotation also describes localization to the trans-Golgi–endosome network in intracellular parasites.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic segment is consistent with a membrane anchor, which can support membrane association but does not distinguish an endosome membrane from the other candidate compartments.",
    "missing_item_specific_fact": "The protein-specific localization of Toxoplasma FER1 to the trans-Golgi–endosome network, including the endosome membrane, is not supplied in the question.",
    "reason": "Choosing D requires the protein-specific localization evidence; the sequence and general biological knowledge do not meaningfully resolve this precise compartment among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D among the listed options. The annotation reports other locations and varies by parasite state, but cytoplasm and trans-Golgi network membrane are not choices, and the supplied evidence does not support the other listed compartments."
  },
  "important_caveats": [
    "The localization annotation is tied to cited experimental evidence (IDA); the underlying study was not independently reviewed here.",
    "The annotation describes different localization in intracellular and extracellular parasites, while the question does not specify parasite state.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7J6JXB6 (TgFER1) carries GO:0010008 (endosome membrane) with IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment explicitly lists 'Endosome membrane; Single-pass membrane protein' as an experimentally determined location. The protein also localizes to trans-Golgi network membrane (IMP evidence) and cytoplasm, but 'endosome membrane' is a directly annotated, experimentally supported location. Among the four options, D is the only correct subcellular compartment for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a ferlin-family protein (multiple C2 calcium-binding domains) with a single-pass transmembrane domain at the C-terminus and no mitochondrial targeting signal or signal peptide. Ferlins are well-characterized as intracellular membrane-trafficking proteins associated with endosomal/Golgi compartments, not mitochondria or the cell surface. This eliminates A (no MTS; ferlins are not mitochondrial), B (single-pass TM with cytoplasmic N-terminus inconsistent with external plasma membrane topology; ferlins are not surface proteins), and C ('host cell' is overly broad and misattributes the protein to the host organism rather than the parasite). The remaining option D (endosome membrane) is consistent with general ferlin biology of intracellular vesicle trafficking.


**Missing item-specific fact**

> The precise distinction between 'endosome membrane' and 'trans-Golgi network membrane' for TgFER1 is a protein-specific experimental finding (PubMed:39294204, 2024). However, since trans-Golgi network membrane is not offered as a distractor, the ferlin-family reasoning suffices to select D among the given options.


**Reason**

> General knowledge of ferlin domain architecture (C2 domains, single-pass TM, intracellular trafficking role) provides a concrete biological argument to eliminate options A, B, and C and select D. The reasoning does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although TgFER1 localizes to multiple compartments (trans-Golgi-endosome network, cytoplasm), only 'endosome membrane' among the four choices is a correct annotated location. The trans-Golgi network membrane (the other membrane location) is not offered as an option, so D is uniquely correct among the provided choices.


### Important caveats

- The protein's localization is dynamic: trans-Golgi-endosome network in intracellular parasites, cytoplasm upon egress or in extracellular tachyzoites. 'Primary' localization depends on the biological context.
- The IDA evidence for endosome membrane comes from a 2024 paper (PubMed:39294204); the entry was first public in Feb 2025. The author's source snapshot is unknown.
- The sequence-to-ferlin-family identification relies on recognizing C2 domain architecture, which is general protein-family knowledge rather than sequence-specific lookup.
- Option C ('host cell') is a valid GO term but is extremely broad and not a specific subcellular compartment for this protein; it does not compete meaningfully with D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a ferlin-family protein (multiple C2 calcium-binding domains) with a single-pass transmembrane domain at the C-terminus and no mitochondrial targeting signal or signal peptide. Ferlins are well-characterized as intracellular membrane-trafficking proteins associated with endosomal/Golgi compartments, not mitochondria or the cell surface. This eliminates A (no MTS; ferlins are not mitochondrial), B (single-pass TM with cytoplasmic N-terminus inconsistent with external plasma membrane topology; ferlins are not surface proteins), and C ('host cell' is overly broad and misattributes the protein to the host organism rather than the parasite). The remaining option D (endosome membrane) is consistent with general ferlin biology of intracellular vesicle trafficking.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise distinction between 'endosome membrane' and 'trans-Golgi network membrane' for TgFER1 is a protein-specific experimental finding (PubMed:39294204, 2024). However, since trans-Golgi network membrane is not offered as a distractor, the ferlin-family reasoning suffices to select D among the given options.",
    "reason": "General knowledge of ferlin domain architecture (C2 domains, single-pass TM, intracellular trafficking role) provides a concrete biological argument to eliminate options A, B, and C and select D. The reasoning does not require memorizing this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (TgFER1) carries GO:0010008 (endosome membrane) with IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment explicitly lists 'Endosome membrane; Single-pass membrane protein' as an experimentally determined location. The protein also localizes to trans-Golgi network membrane (IMP evidence) and cytoplasm, but 'endosome membrane' is a directly annotated, experimentally supported location. Among the four options, D is the only correct subcellular compartment for this protein."
  },
  "important_caveats": [
    "The protein's localization is dynamic: trans-Golgi-endosome network in intracellular parasites, cytoplasm upon egress or in extracellular tachyzoites. 'Primary' localization depends on the biological context.",
    "The IDA evidence for endosome membrane comes from a 2024 paper (PubMed:39294204); the entry was first public in Feb 2025. The author's source snapshot is unknown.",
    "The sequence-to-ferlin-family identification relies on recognizing C2 domain architecture, which is general protein-family knowledge rather than sequence-specific lookup.",
    "Option C ('host cell') is a valid GO term but is extremely broad and not a specific subcellular compartment for this protein; it does not compete meaningfully with D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although TgFER1 localizes to multiple compartments (trans-Golgi-endosome network, cytoplasm), only 'endosome membrane' among the four choices is a correct annotated location. The trans-Golgi network membrane (the other membrane location) is not offered as an option, so D is uniquely correct among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (TgFER1) carries GO:0010008 (endosome membrane) with IDA (Inferred from Direct Assay) evidence from PubMed:39294204. The subcellular location comment explicitly lists 'Endosome membrane; Single-pass membrane protein' as an experimentally determined location. The protein also localizes to trans-Golgi network membrane (IMP evidence) and cytoplasm, but 'endosome membrane' is a directly annotated, experimentally supported location. Among the four options, D is the only correct subcellular compartment for this protein.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a ferlin-family protein (multiple C2 calcium-binding domains) with a single-pass transmembrane domain at the C-terminus and no mitochondrial targeting signal or signal peptide. Ferlins are well-characterized as intracellular membrane-trafficking proteins associated with endosomal/Golgi compartments, not mitochondria or the cell surface. This eliminates A (no MTS; ferlins are not mitochondrial), B (single-pass TM with cytoplasmic N-terminus inconsistent with external plasma membrane topology; ferlins are not surface proteins), and C ('host cell' is overly broad and misattributes the protein to the host organism rather than the parasite). The remaining option D (endosome membrane) is consistent with general ferlin biology of intracellular vesicle trafficking.",
    "missing_item_specific_fact": "The precise distinction between 'endosome membrane' and 'trans-Golgi network membrane' for TgFER1 is a protein-specific experimental finding (PubMed:39294204, 2024). However, since trans-Golgi network membrane is not offered as a distractor, the ferlin-family reasoning suffices to select D among the given options.",
    "reason": "General knowledge of ferlin domain architecture (C2 domains, single-pass TM, intracellular trafficking role) provides a concrete biological argument to eliminate options A, B, and C and select D. The reasoning does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although TgFER1 localizes to multiple compartments (trans-Golgi-endosome network, cytoplasm), only 'endosome membrane' among the four choices is a correct annotated location. The trans-Golgi network membrane (the other membrane location) is not offered as an option, so D is uniquely correct among the provided choices."
  },
  "important_caveats": [
    "The protein's localization is dynamic: trans-Golgi-endosome network in intracellular parasites, cytoplasm upon egress or in extracellular tachyzoites. 'Primary' localization depends on the biological context.",
    "The IDA evidence for endosome membrane comes from a 2024 paper (PubMed:39294204); the entry was first public in Feb 2025. The author's source snapshot is unknown.",
    "The sequence-to-ferlin-family identification relies on recognizing C2 domain architecture, which is general protein-family knowledge rather than sequence-specific lookup.",
    "Option C ('host cell') is a valid GO term but is extremely broad and not a specific subcellular compartment for this protein; it does not compete meaningfully with D."
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

**Accession:** `A0A7J6JXB6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 14. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
"A0A7J6JXB6"
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"entryVersion":15,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-06-10","lastSequenceUpdateDate":"2021-04-07","sequenceVersion":1}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"UP000557509","source":"Proteomes"}],"lineage":["Eukaryota","Sar","Alveolata","Apicomplexa","Conoidasida","Coccidia","Eucoccidiorida","Eimeriorina","Sarcocystidae","Toxoplasma"],"scientificName":"Toxoplasma gondii","taxonId":5811}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294204","source":"PubMed"}],"value":"In intracellular parasites localizes to the trans-Golgi-endosome network; upon egress disperses into the cytoplasm (PubMed:39294204). In extracellular parasites, localizes throughout the cytoplasm (PubMed:39294204)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294204","source":"PubMed"}],"id":"SL-0267","value":"Golgi apparatus, trans-Golgi network membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294204","source":"PubMed"}],"id":"SL-0100","value":"Endosome membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294204","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:36.132368+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39294204","source":"PubMed"}],"id":"GO:0010008","properties":[{"key":"GoTerm","value":"C:endosome membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)  
**Locator:** `lines 46-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:38.159549+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Golgi apparatus, trans-Golgi network membrane
CC       {ECO:0000269|PubMed:39294204}; Single-pass membrane protein
CC       {ECO:0000255}. Endosome membrane {ECO:0000269|PubMed:39294204}; Single-
CC       pass membrane protein {ECO:0000255}. Cytoplasm
CC       {ECO:0000269|PubMed:39294204}. Note=In intracellular parasites
CC       localizes to the trans-Golgi-endosome network; upon egress disperses
CC       into the cytoplasm (PubMed:39294204). In extracellular parasites,
CC       localizes throughout the cytoplasm (PubMed:39294204).
CC       {ECO:0000269|PubMed:39294204}.
```

Source SHA-256: `11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:38.159549+00:00.  

```text
DR   GO; GO:0010008; C:endosome membrane; IDA:UniProtKB.
```

Source SHA-256: `11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
