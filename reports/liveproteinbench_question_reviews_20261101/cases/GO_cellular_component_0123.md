# GO_cellular_component_0123

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — checkpoint clamp complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDVEPSPYGDCKFVARVEHIKTFIQAIKSICFNDYGMVQVSEDGLRITVEQGKSIQATLFMPPGAFMEFRVQDFQCFGVKMNVLSECLSLFGSADCSLRMMYRDKGDPLKIILYPHDDDDVSTECAIKTMDCDEPIDYDQNLKDPDLNVIFVRGPNLSKVFNELEKSAEEFEFVTSPNRPHFKITTVGIMQAVFSVEVAKTSPMMMMFNCKQTVVARYKSQQIRMTNKAMQSATKVAIKTNSVGLLELHLVMQGDSQEEIFIQFFIIPLLNTD

[Multiple Choices]
A. checkpoint clamp complex
B. mitochondrial matrix
C. helical viral capsid
D. trans-Golgi network membrane
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

> The sequence matches the Drosophila Rad1 entry, which has a checkpoint clamp complex GO annotation with IDA:FlyBase evidence. The archived annotation also predates the likely benchmark cutoff.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone provides no clear signal that meaningfully identifies checkpoint-clamp membership over the alternatives; recognizing a DNA-repair clamp subunit requires protein-specific knowledge.


**Missing item-specific fact**

> That this sequence is Drosophila Rad1 and is annotated as part of the checkpoint clamp complex.


**Reason**

> The supporting Rad1 identity and complex-membership annotation are external, item-specific facts, not supplied in the question. General sequence heuristics do not establish this complex association.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the matched sequence has direct support for A; the evidence does not support the other listed terms.


### Important caveats

- Checkpoint clamp complex is a complex-membership cellular-component term, not a spatial compartment in the narrow sense.
- The cited evidence also reports cytoplasm, nucleus, and nuclear-envelope localization, including nuclear-periphery localization in the 9-1-1 complex; these are not listed options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone provides no clear signal that meaningfully identifies checkpoint-clamp membership over the alternatives; recognizing a DNA-repair clamp subunit requires protein-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is Drosophila Rad1 and is annotated as part of the checkpoint clamp complex.",
    "reason": "The supporting Rad1 identity and complex-membership annotation are external, item-specific facts, not supplied in the question. General sequence heuristics do not establish this complex association."
  },
  "case_id": "GO_cellular_component_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Rad1 entry, which has a checkpoint clamp complex GO annotation with IDA:FlyBase evidence. The archived annotation also predates the likely benchmark cutoff."
  },
  "important_caveats": [
    "Checkpoint clamp complex is a complex-membership cellular-component term, not a spatial compartment in the narrow sense.",
    "The cited evidence also reports cytoplasm, nucleus, and nuclear-envelope localization, including nuclear-periphery localization in the 9-1-1 complex; these are not listed options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched sequence has direct support for A; the evidence does not support the other listed terms."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila Rad1 entry, which has a checkpoint clamp complex GO annotation with IDA:FlyBase evidence. The archived annotation also predates the likely benchmark cutoff.",
    "evidence_ids": ["C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone provides no clear signal that meaningfully identifies checkpoint-clamp membership over the alternatives; recognizing a DNA-repair clamp subunit requires protein-specific knowledge.",
    "missing_item_specific_fact": "That this sequence is Drosophila Rad1 and is annotated as part of the checkpoint clamp complex.",
    "reason": "The supporting Rad1 identity and complex-membership annotation are external, item-specific facts, not supplied in the question. General sequence heuristics do not establish this complex association."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched sequence has direct support for A; the evidence does not support the other listed terms."
  },
  "important_caveats": [
    "Checkpoint clamp complex is a complex-membership cellular-component term, not a spatial compartment in the narrow sense.",
    "The cited evidence also reports cytoplasm, nucleus, and nuclear-envelope localization, including nuclear-periphery localization in the 9-1-1 complex; these are not listed options."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VQD4 (DNA repair protein Rad1, Drosophila melanogaster, 274 aa). GO:0030896 (checkpoint clamp complex) is annotated with IDA:FlyBase evidence (C6/H4), indicating direct experimental evidence that Rad1 is a subunit of the 9-1-1 checkpoint clamp complex. The GO term definition (GO3) explicitly lists Rad1 as a subunit. The subcellular location annotation (C5/H3) notes localization to nuclear periphery when part of the 9-1-1 complex. The expected answer is supported by experimental (IDA) database annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks an N-terminal mitochondrial targeting signal (no amphipathic α-helix enriched in positively charged residues), eliminating B (mitochondrial matrix). The protein is clearly eukaryotic with no repetitive capsid-assembly motifs, eliminating C (helical viral capsid). The sequence contains no hydrophobic transmembrane segments or signal peptides, eliminating D (trans-Golgi network membrane). The checkpoint clamp complex is a nuclear DNA-damage-response complex; among the four options, A is the only nuclear/chromatin-associated compartment, and the protein's features (short ~274 aa, no targeting signals, no TM domains) are consistent with a soluble nuclear protein. General knowledge that DNA repair and checkpoint proteins operate in the nucleus supports selecting A by elimination and positive nuclear context.


**Missing item-specific fact**

> Positive identification of this specific sequence as a PCNA-like fold protein or as the Rad1 subunit of the 9-1-1 complex would require sequence-family knowledge or structural prediction not derivable from raw sequence alone. However, this is not strictly needed given the elimination strategy.


**Reason**

> A model can distinguish the answer by applying general biological knowledge: absence of mitochondrial targeting signals, absence of viral capsid structural features, absence of transmembrane domains, and recognition that 'checkpoint clamp complex' is the only nuclear option. This constitutes a concrete elimination-based biological argument using general knowledge rather than memorizing the specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a eukaryotic nuclear protein lacking mitochondrial signals, viral structural motifs, or transmembrane domains. Only A is a nuclear/chromatin-associated complex. No other option is defensible given the sequence features.


### Important caveats

- The positive identification of 'checkpoint clamp complex' specifically (vs. generic 'nucleus') relies on knowing that this GO term is nuclear and DNA-repair-related; a model unfamiliar with the term might struggle even after eliminating B, C, D.
- The UniProt entry also annotates cytoplasm, nucleus, and nuclear envelope with EXP evidence; 'checkpoint clamp complex' is a more specific complex-level annotation (IDA:FlyBase) rather than the only location.
- The reasoning pathway is primarily elimination-based; strong positive sequence-level evidence for PCNA-like fold or 9-1-1 membership is not available from the raw 274-aa sequence without structural prediction tools.
- Identity of the protein (Q9VQD4/Rad1) was inferred by reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks an N-terminal mitochondrial targeting signal (no amphipathic α-helix enriched in positively charged residues), eliminating B (mitochondrial matrix). The protein is clearly eukaryotic with no repetitive capsid-assembly motifs, eliminating C (helical viral capsid). The sequence contains no hydrophobic transmembrane segments or signal peptides, eliminating D (trans-Golgi network membrane). The checkpoint clamp complex is a nuclear DNA-damage-response complex; among the four options, A is the only nuclear/chromatin-associated compartment, and the protein's features (short ~274 aa, no targeting signals, no TM domains) are consistent with a soluble nuclear protein. General knowledge that DNA repair and checkpoint proteins operate in the nucleus supports selecting A by elimination and positive nuclear context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of this specific sequence as a PCNA-like fold protein or as the Rad1 subunit of the 9-1-1 complex would require sequence-family knowledge or structural prediction not derivable from raw sequence alone. However, this is not strictly needed given the elimination strategy.",
    "reason": "A model can distinguish the answer by applying general biological knowledge: absence of mitochondrial targeting signals, absence of viral capsid structural features, absence of transmembrane domains, and recognition that 'checkpoint clamp complex' is the only nuclear option. This constitutes a concrete elimination-based biological argument using general knowledge rather than memorizing the specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VQD4 (DNA repair protein Rad1, Drosophila melanogaster, 274 aa). GO:0030896 (checkpoint clamp complex) is annotated with IDA:FlyBase evidence (C6/H4), indicating direct experimental evidence that Rad1 is a subunit of the 9-1-1 checkpoint clamp complex. The GO term definition (GO3) explicitly lists Rad1 as a subunit. The subcellular location annotation (C5/H3) notes localization to nuclear periphery when part of the 9-1-1 complex. The expected answer is supported by experimental (IDA) database annotation."
  },
  "important_caveats": [
    "The positive identification of 'checkpoint clamp complex' specifically (vs. generic 'nucleus') relies on knowing that this GO term is nuclear and DNA-repair-related; a model unfamiliar with the term might struggle even after eliminating B, C, D.",
    "The UniProt entry also annotates cytoplasm, nucleus, and nuclear envelope with EXP evidence; 'checkpoint clamp complex' is a more specific complex-level annotation (IDA:FlyBase) rather than the only location.",
    "The reasoning pathway is primarily elimination-based; strong positive sequence-level evidence for PCNA-like fold or 9-1-1 membership is not available from the raw 274-aa sequence without structural prediction tools.",
    "Identity of the protein (Q9VQD4/Rad1) was inferred by reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a eukaryotic nuclear protein lacking mitochondrial signals, viral structural motifs, or transmembrane domains. Only A is a nuclear/chromatin-associated complex. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VQD4 (DNA repair protein Rad1, Drosophila melanogaster, 274 aa). GO:0030896 (checkpoint clamp complex) is annotated with IDA:FlyBase evidence (C6/H4), indicating direct experimental evidence that Rad1 is a subunit of the 9-1-1 checkpoint clamp complex. The GO term definition (GO3) explicitly lists Rad1 as a subunit. The subcellular location annotation (C5/H3) notes localization to nuclear periphery when part of the 9-1-1 complex. The expected answer is supported by experimental (IDA) database annotation.",
    "evidence_ids": ["C1", "C4", "C6", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks an N-terminal mitochondrial targeting signal (no amphipathic α-helix enriched in positively charged residues), eliminating B (mitochondrial matrix). The protein is clearly eukaryotic with no repetitive capsid-assembly motifs, eliminating C (helical viral capsid). The sequence contains no hydrophobic transmembrane segments or signal peptides, eliminating D (trans-Golgi network membrane). The checkpoint clamp complex is a nuclear DNA-damage-response complex; among the four options, A is the only nuclear/chromatin-associated compartment, and the protein's features (short ~274 aa, no targeting signals, no TM domains) are consistent with a soluble nuclear protein. General knowledge that DNA repair and checkpoint proteins operate in the nucleus supports selecting A by elimination and positive nuclear context.",
    "missing_item_specific_fact": "Positive identification of this specific sequence as a PCNA-like fold protein or as the Rad1 subunit of the 9-1-1 complex would require sequence-family knowledge or structural prediction not derivable from raw sequence alone. However, this is not strictly needed given the elimination strategy.",
    "reason": "A model can distinguish the answer by applying general biological knowledge: absence of mitochondrial targeting signals, absence of viral capsid structural features, absence of transmembrane domains, and recognition that 'checkpoint clamp complex' is the only nuclear option. This constitutes a concrete elimination-based biological argument using general knowledge rather than memorizing the specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a eukaryotic nuclear protein lacking mitochondrial signals, viral structural motifs, or transmembrane domains. Only A is a nuclear/chromatin-associated complex. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The positive identification of 'checkpoint clamp complex' specifically (vs. generic 'nucleus') relies on knowing that this GO term is nuclear and DNA-repair-related; a model unfamiliar with the term might struggle even after eliminating B, C, D.",
    "The UniProt entry also annotates cytoplasm, nucleus, and nuclear envelope with EXP evidence; 'checkpoint clamp complex' is a more specific complex-level annotation (IDA:FlyBase) rather than the only location.",
    "The reasoning pathway is primarily elimination-based; strong positive sequence-level evidence for PCNA-like fold or 9-1-1 membership is not available from the raw 274-aa sequence without structural prediction tools.",
    "Identity of the protein (Q9VQD4/Rad1) was inferred by reviewer from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `Q9VQD4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 171. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VQD4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:35.143975+00:00.  

```json
"Q9VQD4"
```

Source SHA-256: `16ce921df5b3e4a4b1cc7a458f452776bd0bde1fd36a87d16966b22696795c75`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VQD4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:35.143975+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0026778","source":"FlyBase"}],"value":"Protein radiation insensitive 1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DNA repair protein Rad1"}}}
```

Source SHA-256: `16ce921df5b3e4a4b1cc7a458f452776bd0bde1fd36a87d16966b22696795c75`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VQD4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:35.143975+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"value":"Localizes to the nuclear periphery when part of the 9-1-1 complex with Rad9 isoform A and Rad1"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"id":"SL-0178","value":"Nucleus envelope"}}]}
```

Source SHA-256: `16ce921df5b3e4a4b1cc7a458f452776bd0bde1fd36a87d16966b22696795c75`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VQD4.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:35.143975+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22666434","source":"PubMed"}],"id":"GO:0030896","properties":[{"key":"GoTerm","value":"C:checkpoint clamp complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `16ce921df5b3e4a4b1cc7a458f452776bd0bde1fd36a87d16966b22696795c75`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VQD4?format=txt&versions=171)  
**Locator:** `lines 100-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 2.  
**Retrieved:** 2026-11-02T04:33:38.224183+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:22666434}. Nucleus
CC       {ECO:0000269|PubMed:22666434}. Nucleus envelope
CC       {ECO:0000269|PubMed:22666434}. Note=Localizes to the nuclear periphery
CC       when part of the 9-1-1 complex with Rad9 isoform A and Rad1.
CC       {ECO:0000269|PubMed:22666434}.
```

Source SHA-256: `226a333b948bbec737d27994428fb188c8fdd2b4aec9d399b7236dc3888da8f4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VQD4?format=txt&versions=171)  
**Locator:** `lines 142-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 2.  
**Retrieved:** 2026-11-02T04:33:38.224183+00:00.  

```text
DR   GO; GO:0030896; C:checkpoint clamp complex; IDA:FlyBase.
```

Source SHA-256: `226a333b948bbec737d27994428fb188c8fdd2b4aec9d399b7236dc3888da8f4`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 171270-171280`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0030896
name: checkpoint clamp complex
namespace: cellular_component
def: "Conserved heterotrimeric complex of PCNA-like proteins that is loaded onto DNA at sites of DNA damage." [PMID:12531008]
comment: Note that the following subunit names have been used: human RAD9/RAD1/HUS1; S. pombe Rad9/Rad1/Hus1; S. cerevisiae Ddc1p/Rad17p/Mec3p.
synonym: "CCC" EXACT []
synonym: "Rad9-Hus1-Rad1 (9-1-1) clamp complex" EXACT []
is_a: GO:0140513 ! nuclear protein-containing complex
relationship: part_of GO:0000794 ! condensed nuclear chromosome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
