# GO_cellular_component_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMPVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPMKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTTYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRATY

[Multiple Choices]
A. lysosomal membrane
B. helical viral capsid
C. plasma membrane
D. histone acetyltransferase complex
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

> The exact-match UniProt record annotates this protein to the cell membrane, and the archived GO annotation assigns plasma membrane. The GO ontology treats “cell membrane” as an exact synonym of “plasma membrane.”

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support that this is a multipass membrane protein, but they do not establish which cellular membrane it occupies.


**Missing item-specific fact**

> The protein-specific localization of this nucleoside transporter to the cell/plasma membrane, rather than another membrane such as the lysosomal membrane.


**Reason**

> Choosing plasma membrane requires localization information not supplied by the sequence. Identifying the exact protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> From the supplied sequence alone, both lysosomal membrane and plasma membrane are plausible destinations for a multipass membrane protein; the sequence does not distinguish them. The external localization evidence supports C.


### Important caveats

- The current and archived records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The GO plasma-membrane annotation is computationally inferred, while the cell-membrane annotation is linked to cited literature; the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, but they do not establish which cellular membrane it occupies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization of this nucleoside transporter to the cell/plasma membrane, rather than another membrane such as the lysosomal membrane.",
    "reason": "Choosing plasma membrane requires localization information not supplied by the sequence. Identifying the exact protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning."
  },
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates this protein to the cell membrane, and the archived GO annotation assigns plasma membrane. The GO ontology treats “cell membrane” as an exact synonym of “plasma membrane.”"
  },
  "important_caveats": [
    "The current and archived records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The GO plasma-membrane annotation is computationally inferred, while the cell-membrane annotation is linked to cited literature; the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "From the supplied sequence alone, both lysosomal membrane and plasma membrane are plausible destinations for a multipass membrane protein; the sequence does not distinguish them. The external localization evidence supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match UniProt record annotates this protein to the cell membrane, and the archived GO annotation assigns plasma membrane. The GO ontology treats “cell membrane” as an exact synonym of “plasma membrane.”",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support that this is a multipass membrane protein, but they do not establish which cellular membrane it occupies.",
    "missing_item_specific_fact": "The protein-specific localization of this nucleoside transporter to the cell/plasma membrane, rather than another membrane such as the lysosomal membrane.",
    "reason": "Choosing plasma membrane requires localization information not supplied by the sequence. Identifying the exact protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "From the supplied sequence alone, both lysosomal membrane and plasma membrane are plausible destinations for a multipass membrane protein; the sequence does not distinguish them. The external localization evidence supports C."
  },
  "important_caveats": [
    "The current and archived records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The GO plasma-membrane annotation is computationally inferred, while the cell-membrane annotation is linked to cited literature; the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O76343 (LdNT1.1, nucleoside transporter from Leishmania donovani) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence ECO:0000305, based on functional studies in PubMed 9707568 and 12835315). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym, and the UniProt cross-reference explicitly maps to GO:0005886 C:plasma membrane (IEA:UniProtKB-SubCell). The sequence matches the benchmark sequence exactly. The annotation is curator-inferred from functional transporter studies rather than direct experimental localization (e.g., immunofluorescence), but it is a well-supported database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options B (helical viral capsid) and D (histone acetyltransferase complex) are clearly eliminable by general reasoning: the sequence is from a eukaryotic parasite (Leishmania), not a virus, and the multi-pass membrane architecture is incompatible with a chromatin-associated complex. However, distinguishing A (lysosomal membrane) from C (plasma membrane) for a multi-pass membrane transporter from sequence alone is very difficult. Both compartments host multi-pass membrane proteins. The sequence lacks definitive lysosomal targeting motifs (dileucine, tyrosine-based), but their absence is not conclusive. The key fact—that this is a nucleoside transporter functioning in nutrient uptake at the cell surface—is a protein-specific annotation not derivable from general sequence features.


**Missing item-specific fact**

> The specific identity of the protein as a nucleoside transporter (LdNT1.1) whose function is to import extracellular nucleosides across the plasma membrane. Without knowing this, a multi-pass membrane protein could plausibly reside in either the plasma membrane or the lysosomal membrane.


**Reason**

> While B and D are trivially eliminable, the A-vs-C distinction requires knowing that this specific multi-pass membrane protein is a nutrient-uptake transporter localized to the cell surface. Sequence features (multiple TM domains, hydrophilic loops) confirm it is a membrane transporter but do not uniquely identify which membrane. The absence of canonical lysosomal targeting motifs is suggestive but not definitive, and general heuristics about 'most transporters are at the plasma membrane' are too weak to override the possibility of a lysosomal membrane transporter.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the database annotation, C is clearly the correct answer. Options B and D are clearly wrong. Option A is the only plausible alternative but is not supported by any annotation or experimental evidence for this protein. No genuine ambiguity exists in the correct answer, though the reasoning path from sequence to answer is weak.


### Important caveats

- The GO:0005886 annotation carries evidence code IEA (inferred from electronic annotation), propagated from the UniProt 'Cell membrane' subcellular location comment, which itself is ECO:0000305 (inferred by curator from functional studies). This is not direct experimental proof of membrane localization (e.g., immunofluorescence or subcellular fractionation).
- The topology annotation (multi-pass membrane protein) is ECO:0000255 (inferred by similarity), not experimentally determined.
- The sequence is from Leishmania donovani, a trypanosomatid parasite. Its membrane biology may differ from well-studied model organisms, and lysosomal membrane protein characteristics may not follow mammalian paradigms exactly.
- The reviewer-only evidence was absent from the evaluated model's input; the model sees only the 491-aa sequence and four options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (helical viral capsid) and D (histone acetyltransferase complex) are clearly eliminable by general reasoning: the sequence is from a eukaryotic parasite (Leishmania), not a virus, and the multi-pass membrane architecture is incompatible with a chromatin-associated complex. However, distinguishing A (lysosomal membrane) from C (plasma membrane) for a multi-pass membrane transporter from sequence alone is very difficult. Both compartments host multi-pass membrane proteins. The sequence lacks definitive lysosomal targeting motifs (dileucine, tyrosine-based), but their absence is not conclusive. The key fact—that this is a nucleoside transporter functioning in nutrient uptake at the cell surface—is a protein-specific annotation not derivable from general sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the protein as a nucleoside transporter (LdNT1.1) whose function is to import extracellular nucleosides across the plasma membrane. Without knowing this, a multi-pass membrane protein could plausibly reside in either the plasma membrane or the lysosomal membrane.",
    "reason": "While B and D are trivially eliminable, the A-vs-C distinction requires knowing that this specific multi-pass membrane protein is a nutrient-uptake transporter localized to the cell surface. Sequence features (multiple TM domains, hydrophilic loops) confirm it is a membrane transporter but do not uniquely identify which membrane. The absence of canonical lysosomal targeting motifs is suggestive but not definitive, and general heuristics about 'most transporters are at the plasma membrane' are too weak to override the possibility of a lysosomal membrane transporter."
  },
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O76343 (LdNT1.1, nucleoside transporter from Leishmania donovani) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence ECO:0000305, based on functional studies in PubMed 9707568 and 12835315). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym, and the UniProt cross-reference explicitly maps to GO:0005886 C:plasma membrane (IEA:UniProtKB-SubCell). The sequence matches the benchmark sequence exactly. The annotation is curator-inferred from functional transporter studies rather than direct experimental localization (e.g., immunofluorescence), but it is a well-supported database annotation."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries evidence code IEA (inferred from electronic annotation), propagated from the UniProt 'Cell membrane' subcellular location comment, which itself is ECO:0000305 (inferred by curator from functional studies). This is not direct experimental proof of membrane localization (e.g., immunofluorescence or subcellular fractionation).",
    "The topology annotation (multi-pass membrane protein) is ECO:0000255 (inferred by similarity), not experimentally determined.",
    "The sequence is from Leishmania donovani, a trypanosomatid parasite. Its membrane biology may differ from well-studied model organisms, and lysosomal membrane protein characteristics may not follow mammalian paradigms exactly.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model sees only the 491-aa sequence and four options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the database annotation, C is clearly the correct answer. Options B and D are clearly wrong. Option A is the only plausible alternative but is not supported by any annotation or experimental evidence for this protein. No genuine ambiguity exists in the correct answer, though the reasoning path from sequence to answer is weak."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O76343 (LdNT1.1, nucleoside transporter from Leishmania donovani) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence ECO:0000305, based on functional studies in PubMed 9707568 and 12835315). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym, and the UniProt cross-reference explicitly maps to GO:0005886 C:plasma membrane (IEA:UniProtKB-SubCell). The sequence matches the benchmark sequence exactly. The annotation is curator-inferred from functional transporter studies rather than direct experimental localization (e.g., immunofluorescence), but it is a well-supported database annotation.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options B (helical viral capsid) and D (histone acetyltransferase complex) are clearly eliminable by general reasoning: the sequence is from a eukaryotic parasite (Leishmania), not a virus, and the multi-pass membrane architecture is incompatible with a chromatin-associated complex. However, distinguishing A (lysosomal membrane) from C (plasma membrane) for a multi-pass membrane transporter from sequence alone is very difficult. Both compartments host multi-pass membrane proteins. The sequence lacks definitive lysosomal targeting motifs (dileucine, tyrosine-based), but their absence is not conclusive. The key fact—that this is a nucleoside transporter functioning in nutrient uptake at the cell surface—is a protein-specific annotation not derivable from general sequence features.",
    "missing_item_specific_fact": "The specific identity of the protein as a nucleoside transporter (LdNT1.1) whose function is to import extracellular nucleosides across the plasma membrane. Without knowing this, a multi-pass membrane protein could plausibly reside in either the plasma membrane or the lysosomal membrane.",
    "reason": "While B and D are trivially eliminable, the A-vs-C distinction requires knowing that this specific multi-pass membrane protein is a nutrient-uptake transporter localized to the cell surface. Sequence features (multiple TM domains, hydrophilic loops) confirm it is a membrane transporter but do not uniquely identify which membrane. The absence of canonical lysosomal targeting motifs is suggestive but not definitive, and general heuristics about 'most transporters are at the plasma membrane' are too weak to override the possibility of a lysosomal membrane transporter."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the database annotation, C is clearly the correct answer. Options B and D are clearly wrong. Option A is the only plausible alternative but is not supported by any annotation or experimental evidence for this protein. No genuine ambiguity exists in the correct answer, though the reasoning path from sequence to answer is weak."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries evidence code IEA (inferred from electronic annotation), propagated from the UniProt 'Cell membrane' subcellular location comment, which itself is ECO:0000305 (inferred by curator from functional studies). This is not direct experimental proof of membrane localization (e.g., immunofluorescence or subcellular fractionation).",
    "The topology annotation (multi-pass membrane protein) is ECO:0000255 (inferred by similarity), not experimentally determined.",
    "The sequence is from Leishmania donovani, a trypanosomatid parasite. Its membrane biology may differ from well-studied model organisms, and lysosomal membrane protein characteristics may not follow mammalian paradigms exactly.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model sees only the 491-aa sequence and four options."
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

**Accession:** `O76343` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 70. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"12835315","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"9707568","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 75-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:12835315,
CC       ECO:0000305|PubMed:9707568}; Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
