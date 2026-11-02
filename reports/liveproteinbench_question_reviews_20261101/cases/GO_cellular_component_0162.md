# GO_cellular_component_0162

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
MQVTSLLILVCFIAAFQVFSRASSPVNCKWDSYGPWSECNGCTKTQTRRRSVAVYGQYGGYPCEGSAFETQSCKPERGCPTEEGCGDRFRCFSGQCISKSLVCNGDPDCEEDGADEDKCENVANPSCNIDKPPPNIELTGYGYNVVTGQGKKRVINTKSFGGQCRKVFSGDGKDFYRLSGNILSYTFQVKVDNDFNYEFYNSSWSYIKHTSTEQNTFYSWKGLFSHSRNTYGHGSAKEEIDTKMKSYKLLVVQNTVEVAQFTNNNPEFLQVAEPFWKELSHLPTLYDYSAYRRLIDQYGTHYLQSGSLGGEYRVLFYVDSGSAKETGFQSDQDNACSSADFQFLFTSSADQRCMKQLETEKSTSGNKGRLLRGKPLVRGGDSGFVADLSFLDLDNPAGNKQRYSSWAGSVTRLPQVIKEKLAPLYELVKEVPCASVKRLYLKRAIEEYFDEFDPCHCRPCQNGGLAIVVETQCQCLCKPYTFGSACEQGVLVGDQAGGVDGGWNCWSSWSPCVQGKRTRSRECNNPPPRDDGKSCLGETTESKQCEDQDLEKLRLLEPHCFHSSLAPKEFCLSPPALKDGFVQGEGTMVPVGQSVVYACDEGYSLIGDPVARCGEDLQWLVGEMHCQKLACVLPGEMNGMQSHPQKPFYMVGEKVTLSCVGGMSLEGPSTLLCGSSLKWSPELKDAKCVQKATSTPPPAAPACQPWEKLQNSKCICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ

[Multiple Choices]
A. host cell nucleus
B. P-body
C. plasma membrane
D. perinuclear region of cytoplasm
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

> The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.


**Missing item-specific fact**

> The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.


**Reason**

> The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident.


### Important caveats

- The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.
- The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.",
    "reason": "The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context."
  },
  "important_caveats": [
    "The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.",
    "The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.",
    "missing_item_specific_fact": "The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.",
    "reason": "The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident."
  },
  "important_caveats": [
    "The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.",
    "The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.


**Missing item-specific fact**

> None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.


**Reason**

> The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features.


### Important caveats

- The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.
- C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.
- The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.
- The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.",
    "reason": "The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "H2",
      "H4",
      "H6",
      "GO2",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.",
    "C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.",
    "The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.",
    "The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment.",
    "evidence_ids": ["C5", "C7", "C9", "H2", "H4", "H6", "GO2", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.",
    "missing_item_specific_fact": "None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.",
    "reason": "The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.",
    "C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.",
    "The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.",
    "The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor."
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

**Accession:** `D3YXF5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Complement component C7"}}}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"value":"Secreted as soluble protein. Inserts into the cell membrane of target cells"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"id":"SL-0451","value":"Target cell membrane"}}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/39`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","id":"GO:0005579","properties":[{"key":"GoTerm","value":"C:membrane attack complex"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/41`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000303","id":"30552328","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"NAS:ComplexPortal"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 49-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:P10643}. Target
CC       cell membrane {ECO:0000250|UniProtKB:P10643}. Note=Secreted as soluble
CC       protein. Inserts into the cell membrane of target cells.
CC       {ECO:0000250|UniProtKB:P10643}.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
DR   GO; GO:0005579; C:membrane attack complex; ISO:GO_Central.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 100-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; NAS:ComplexPortal.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57517-57530`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005579
name: membrane attack complex
namespace: cellular_component
def: "A protein complex produced by sequentially activated components of the complement cascade inserted into a target cell membrane and forming a pore leading to cell lysis via ion and water flow." [GOC:add, ISBN:0198547684, ISBN:068340007X, ISBN:0781735149]
synonym: "MAC" EXACT []
synonym: "membrane attack complex protein alphaM chain" NARROW []
synonym: "membrane attack complex protein beta2 chain" NARROW []
synonym: "TCC" EXACT []
synonym: "terminal complement complex" EXACT []
xref: Wikipedia:Complement_membrane_attack_complex
is_a: GO:0046930 ! pore complex
is_a: GO:0098797 ! plasma membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

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

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 411036-411043`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098797
name: plasma membrane protein complex
namespace: cellular_component
def: "Any protein complex that is part of the plasma membrane." [GOC:dos]
is_a: GO:0098796 ! membrane protein complex
relationship: part_of GO:0005886 ! plasma membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
