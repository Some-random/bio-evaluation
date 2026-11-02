# GO_cellular_component_0146

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
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMSVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPIKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTAYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRERH

[Multiple Choices]
A. microvillus membrane
B. midbody
C. plasma membrane
D. membrane attack complex
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

> The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.


**Missing item-specific fact**

> The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.


**Reason**

> The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane.


### Important caveats

- The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.",
    "reason": "The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for this protein. That entry annotates it to the cell membrane based on literature and assigns plasma membrane by computational GO inference. This supports choice C, while the evidence types should not be conflated.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, making midbody and membrane attack complex poor fits. That general inference does not establish plasma membrane rather than another membrane location or a specialized plasma-membrane domain.",
    "missing_item_specific_fact": "The protein-specific cell-membrane localization, or equivalent knowledge of this transporter’s localization, is needed to distinguish the offered membrane locations.",
    "reason": "The sequence offers a useful broad membrane-protein clue, but the choice between plasma membrane and microvillus membrane requires localization information not established by the sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No supplied evidence establishes microvillus localization for this protein. However, the options are not strictly disjoint: a microvillus membrane is a portion of the plasma membrane."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computationally inferred; the cited UniProt cell-membrane annotation is literature-based, not presented here as a directly verified experimental measurement.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.


**Missing item-specific fact**

> None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.


**Reason**

> The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism.


### Important caveats

- The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.
- The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.
- The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269."
  },
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.",
    "The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.",
    "The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O76269 (Nucleoside transporter 1.2, LdNT1.2 from Leishmania donovani) annotates the protein as 'Cell membrane; Multi-pass membrane protein' with evidence codes ECO:0000305 from PubMed:9707568 and PubMed:12835315. The GO cross-reference confirms GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The GO annotation evidence code is IEA (electronic), but the underlying subcellular location comment is curator-inferred from two experimental papers describing this as a plasma membrane nucleoside transporter. The sequence itself shows multiple hydrophobic transmembrane stretches consistent with a multi-pass integral membrane protein at the cell surface.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays numerous long hydrophobic stretches (at least 10-12 transmembrane segments), identifying it as a multi-pass integral membrane protein. General biological reasoning then distinguishes the options: (D) membrane attack complex is a mammalian complement-system pore-forming complex (C5b-C9), irrelevant to a Leishmania protozoan protein; (B) midbody is a transient cytokinetic bridge structure, not a residence for a constitutive transporter; (A) microvillus membrane is a highly specialized sub-domain of the plasma membrane found in polarized epithelial cells (e.g., intestinal brush border), and Leishmania donovani lacks this architecture; (C) plasma membrane is the logical primary location for a multi-pass membrane transporter that must access extracellular substrates. A nucleoside transporter must reside at the cell surface to import extracellular nucleosides, making plasma membrane the default and most general correct annotation.",
    "missing_item_specific_fact": "None critical. Identifying the protein specifically as a nucleoside transporter would strengthen the argument, but the multi-pass membrane topology visible in the sequence combined with general knowledge about membrane transporters and the biology of the distractor options suffices to select C over A, B, and D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein. Among the four choices, three can be eliminated by general biological reasoning: MAC is a mammalian complement complex, midbody is a cytokinesis structure, and microvillus membrane is a specialized epithelial sub-domain absent in protozoa. The remaining option (plasma membrane) is the expected primary location for any multi-pass membrane transporter. This reasoning path does not require memorizing the specific UniProt annotation for O76269."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While microvillus membrane (GO:0031528) is technically part_of plasma membrane (GO:0005886), it is a narrow sub-compartment restricted to specialized polarized cells. For a general nucleoside transporter in a protozoan, plasma membrane is unambiguously the correct primary cellular component. The other two options (midbody, membrane attack complex) are clearly incompatible with the protein's identity and organism."
  },
  "important_caveats": [
    "The GO annotation for this protein carries evidence code IEA (Inferred from Electronic Annotation), meaning the plasma membrane assignment is computationally propagated. However, the underlying UniProt SUBCELLULAR LOCATION comment uses ECO:0000305 (curator inference from experimental literature), providing stronger support.",
    "The UniProt entry is flagged as 'Fragment,' so the full-length protein topology is not fully resolved, though the supplied 491-aa sequence still shows clear multi-pass membrane architecture.",
    "The organism is Leishmania donovani, a protozoan parasite. Microvillus membrane as a GO term is primarily used in the context of metazoan epithelial biology, making option A biologically implausible for this organism."
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

**Accession:** `O76269` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"12835315","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"9707568","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:12835315,
CC       ECO:0000305|PubMed:9707568}; Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
