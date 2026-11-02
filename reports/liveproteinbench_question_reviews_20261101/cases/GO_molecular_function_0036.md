# GO_molecular_function_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — cadmium ion transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. dynein complex binding
B. beta-glucuronidase activity
C. cadmium ion transmembrane transporter activity
D. D-lactate dehydrogenase (cytochrome) activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated with cadmium ion transmembrane transporter activity, but that annotation is computational (IEA:TreeGrafter), not direct evidence of cadmium transport. The cited experimental evidence supports iron transport by this protein; it neither establishes cadmium transport nor contradicts possible transport of other divalent metals.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments suggest a multipass membrane protein and make a transporter more plausible than a soluble enzyme or dynein-binding function. That supports the broad transporter class, but does not identify cadmium as a transported substrate.


**Missing item-specific fact**

> Whether this particular protein transports cadmium, or a protein-specific annotation assigning that substrate.


**Reason**

> The sequence architecture provides a broad functional clue, but the substrate-specific choice depends on an item-specific annotation or experimental fact absent from the input. The reviewer-only TreeGrafter annotation cannot supply that information to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is supported by the supplied reviewer evidence. However, the experimentally supported iron-transport function is not offered, and cadmium transport is supported here only by computational annotation.


### Important caveats

- The sequence identity match is exact, but the author’s source snapshot is unknown.
- The evidence supports the keyed GO annotation as a computational assignment, not as experimentally verified cadmium transport.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make a transporter more plausible than a soluble enzyme or dynein-binding function. That supports the broad transporter class, but does not identify cadmium as a transported substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein transports cadmium, or a protein-specific annotation assigning that substrate.",
    "reason": "The sequence architecture provides a broad functional clue, but the substrate-specific choice depends on an item-specific annotation or experimental fact absent from the input. The reviewer-only TreeGrafter annotation cannot supply that information to the evaluated model."
  },
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with cadmium ion transmembrane transporter activity, but that annotation is computational (IEA:TreeGrafter), not direct evidence of cadmium transport. The cited experimental evidence supports iron transport by this protein; it neither establishes cadmium transport nor contradicts possible transport of other divalent metals."
  },
  "important_caveats": [
    "The sequence identity match is exact, but the author’s source snapshot is unknown.",
    "The evidence supports the keyed GO annotation as a computational assignment, not as experimentally verified cadmium transport."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is supported by the supplied reviewer evidence. However, the experimentally supported iron-transport function is not offered, and cadmium transport is supported here only by computational annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with cadmium ion transmembrane transporter activity, but that annotation is computational (IEA:TreeGrafter), not direct evidence of cadmium transport. The cited experimental evidence supports iron transport by this protein; it neither establishes cadmium transport nor contradicts possible transport of other divalent metals.",
    "evidence_ids": ["C7", "H5", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments suggest a multipass membrane protein and make a transporter more plausible than a soluble enzyme or dynein-binding function. That supports the broad transporter class, but does not identify cadmium as a transported substrate.",
    "missing_item_specific_fact": "Whether this particular protein transports cadmium, or a protein-specific annotation assigning that substrate.",
    "reason": "The sequence architecture provides a broad functional clue, but the substrate-specific choice depends on an item-specific annotation or experimental fact absent from the input. The reviewer-only TreeGrafter annotation cannot supply that information to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is supported by the supplied reviewer evidence. However, the experimentally supported iron-transport function is not offered, and cadmium transport is supported here only by computational annotation."
  },
  "important_caveats": [
    "The sequence identity match is exact, but the author’s source snapshot is unknown.",
    "The evidence supports the keyed GO annotation as a computational assignment, not as experimentally verified cadmium transport."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> GO:0015086 (cadmium ion transmembrane transporter activity) is annotated in the UniProt entry A0A077Y877 (C7, H5). However, the evidence code is IEA:TreeGrafter (computational homology transfer), not experimental. The experimentally validated function (ECO:0000269, PubMed:38049852; C5, C6, H3, H4) is iron transport (Fe²⁺ in/out). The protein is named 'Divalent metal transporter 1' (NRAMP family), which can transport multiple divalent metals including cadmium, but the primary experimental evidence supports iron transport specifically. The cadmium annotation is a computational inference from NRAMP-family homology, not a direct experimental measurement. The answer is supported as a database annotation but rests on computational inference rather than direct experimental validation for cadmium specifically.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied 696-aa sequence contains numerous long hydrophobic stretches (e.g., 'WIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS') characteristic of a polytopic (multi-pass) transmembrane protein. This architecture is incompatible with dynein complex binding (A, a protein-protein interaction function), beta-glucuronidase activity (B, a soluble glycosidase), or D-lactate dehydrogenase cytochrome activity (D, a soluble oxidoreductase). Only option C describes a transmembrane transporter activity, consistent with the observed multi-TM topology. A model can eliminate A, B, and D from sequence architecture alone.


**Missing item-specific fact**

> The specific identity of the transported ion (cadmium vs. iron vs. manganese) cannot be determined from sequence alone; the NRAMP family transports multiple divalent metals. However, this does not affect answerability because the distractors do not include alternative metal-transporter options.


**Reason**

> Although the specific metal ion (cadmium) is not derivable from the sequence, the question is answerable by structural reasoning: the polytopic membrane protein architecture uniquely selects the only transporter option (C) among four choices where the other three describe entirely incompatible molecular functions (binding, glycosidase, dehydrogenase). The elimination logic is concrete and sequence-based.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe functions (protein-complex binding, glycosidase catalysis, oxidoreductase catalysis) that are structurally incompatible with a polytopic membrane protein. No alternative among the four choices is defensible for a multi-TM transporter. The specific choice of 'cadmium' over 'iron' or 'manganese' is a database-annotation artifact but does not create ambiguity because no competing metal-transporter option is presented.


### Important caveats

- The GO:0015086 annotation carries evidence code IEA:TreeGrafter (automated computational transfer), not experimental evidence. The experimentally validated function is iron transport (PubMed:38049852, ECO:0000269).
- The protein is a Plasmodium yoelii NRAMP-family divalent metal transporter (PyDMT1/FVRT1), primarily characterized as an iron transporter. Cadmium transport is inferred by family homology.
- The question is answerable by elimination (only transporter option among non-transporter distractors), but the specific metal-ion label 'cadmium' is not the protein's primary experimentally supported function.
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown. The sequence matches at entry version 38 (2026-01-28).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied 696-aa sequence contains numerous long hydrophobic stretches (e.g., 'WIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS') characteristic of a polytopic (multi-pass) transmembrane protein. This architecture is incompatible with dynein complex binding (A, a protein-protein interaction function), beta-glucuronidase activity (B, a soluble glycosidase), or D-lactate dehydrogenase cytochrome activity (D, a soluble oxidoreductase). Only option C describes a transmembrane transporter activity, consistent with the observed multi-TM topology. A model can eliminate A, B, and D from sequence architecture alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identity of the transported ion (cadmium vs. iron vs. manganese) cannot be determined from sequence alone; the NRAMP family transports multiple divalent metals. However, this does not affect answerability because the distractors do not include alternative metal-transporter options.",
    "reason": "Although the specific metal ion (cadmium) is not derivable from the sequence, the question is answerable by structural reasoning: the polytopic membrane protein architecture uniquely selects the only transporter option (C) among four choices where the other three describe entirely incompatible molecular functions (binding, glycosidase, dehydrogenase). The elimination logic is concrete and sequence-based."
  },
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "H3",
      "C6",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "GO:0015086 (cadmium ion transmembrane transporter activity) is annotated in the UniProt entry A0A077Y877 (C7, H5). However, the evidence code is IEA:TreeGrafter (computational homology transfer), not experimental. The experimentally validated function (ECO:0000269, PubMed:38049852; C5, C6, H3, H4) is iron transport (Fe²⁺ in/out). The protein is named 'Divalent metal transporter 1' (NRAMP family), which can transport multiple divalent metals including cadmium, but the primary experimental evidence supports iron transport specifically. The cadmium annotation is a computational inference from NRAMP-family homology, not a direct experimental measurement. The answer is supported as a database annotation but rests on computational inference rather than direct experimental validation for cadmium specifically."
  },
  "important_caveats": [
    "The GO:0015086 annotation carries evidence code IEA:TreeGrafter (automated computational transfer), not experimental evidence. The experimentally validated function is iron transport (PubMed:38049852, ECO:0000269).",
    "The protein is a Plasmodium yoelii NRAMP-family divalent metal transporter (PyDMT1/FVRT1), primarily characterized as an iron transporter. Cadmium transport is inferred by family homology.",
    "The question is answerable by elimination (only transporter option among non-transporter distractors), but the specific metal-ion label 'cadmium' is not the protein's primary experimentally supported function.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown. The sequence matches at entry version 38 (2026-01-28)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe functions (protein-complex binding, glycosidase catalysis, oxidoreductase catalysis) that are structurally incompatible with a polytopic membrane protein. No alternative among the four choices is defensible for a multi-TM transporter. The specific choice of 'cadmium' over 'iron' or 'manganese' is a database-annotation artifact but does not create ambiguity because no competing metal-transporter option is presented."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "GO:0015086 (cadmium ion transmembrane transporter activity) is annotated in the UniProt entry A0A077Y877 (C7, H5). However, the evidence code is IEA:TreeGrafter (computational homology transfer), not experimental. The experimentally validated function (ECO:0000269, PubMed:38049852; C5, C6, H3, H4) is iron transport (Fe²⁺ in/out). The protein is named 'Divalent metal transporter 1' (NRAMP family), which can transport multiple divalent metals including cadmium, but the primary experimental evidence supports iron transport specifically. The cadmium annotation is a computational inference from NRAMP-family homology, not a direct experimental measurement. The answer is supported as a database annotation but rests on computational inference rather than direct experimental validation for cadmium specifically.",
    "evidence_ids": ["C7", "H5", "C5", "H3", "C6", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied 696-aa sequence contains numerous long hydrophobic stretches (e.g., 'WIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS') characteristic of a polytopic (multi-pass) transmembrane protein. This architecture is incompatible with dynein complex binding (A, a protein-protein interaction function), beta-glucuronidase activity (B, a soluble glycosidase), or D-lactate dehydrogenase cytochrome activity (D, a soluble oxidoreductase). Only option C describes a transmembrane transporter activity, consistent with the observed multi-TM topology. A model can eliminate A, B, and D from sequence architecture alone.",
    "missing_item_specific_fact": "The specific identity of the transported ion (cadmium vs. iron vs. manganese) cannot be determined from sequence alone; the NRAMP family transports multiple divalent metals. However, this does not affect answerability because the distractors do not include alternative metal-transporter options.",
    "reason": "Although the specific metal ion (cadmium) is not derivable from the sequence, the question is answerable by structural reasoning: the polytopic membrane protein architecture uniquely selects the only transporter option (C) among four choices where the other three describe entirely incompatible molecular functions (binding, glycosidase, dehydrogenase). The elimination logic is concrete and sequence-based."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe functions (protein-complex binding, glycosidase catalysis, oxidoreductase catalysis) that are structurally incompatible with a polytopic membrane protein. No alternative among the four choices is defensible for a multi-TM transporter. The specific choice of 'cadmium' over 'iron' or 'manganese' is a database-annotation artifact but does not create ambiguity because no competing metal-transporter option is presented."
  },
  "important_caveats": [
    "The GO:0015086 annotation carries evidence code IEA:TreeGrafter (automated computational transfer), not experimental evidence. The experimentally validated function is iron transport (PubMed:38049852, ECO:0000269).",
    "The protein is a Plasmodium yoelii NRAMP-family divalent metal transporter (PyDMT1/FVRT1), primarily characterized as an iron transporter. Cadmium transport is inferred by family homology.",
    "The question is answerable by elimination (only transporter option among non-transporter distractors), but the specific metal-ion label 'cadmium' is not the protein's primary experimentally supported function.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot date is unknown. The sequence matches at entry version 38 (2026-01-28)."
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

**Accession:** `A0A077Y877` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38049852","source":"PubMed"}],"value":"Iron transporter (PubMed:38049852). Required for parasite development during the blood stages (PubMed:38049852). Required for full pathogenicity (PubMed:38049852)"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38049852","source":"PubMed"}],"name":"Fe(2+)(in) = Fe(2+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:28486"},{"database":"ChEBI","id":"CHEBI:29033"}]}}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"database":"GO","id":"GO:0015086","properties":[{"key":"GoTerm","value":"F:cadmium ion transmembrane transporter activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 37-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
CC   -!- FUNCTION: Iron transporter (PubMed:38049852). Required for parasite
CC       development during the blood stages (PubMed:38049852). Required for
CC       full pathogenicity (PubMed:38049852). {ECO:0000269|PubMed:38049852}.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 40-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Fe(2+)(in) = Fe(2+)(out); Xref=Rhea:RHEA:28486,
CC         ChEBI:CHEBI:29033; Evidence={ECO:0000269|PubMed:38049852};
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
DR   GO; GO:0015086; F:cadmium ion transmembrane transporter activity; IEA:TreeGrafter.
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 114385-114393`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0015086
name: cadmium ion transmembrane transporter activity
namespace: molecular_function
def: "Enables the transfer of cadmium (Cd) ions from one side of a membrane to the other." [GOC:dgf]
synonym: "zinc, cadmium uptake permease activity" RELATED []
synonym: "zinc, cadmium, cobalt, nickel, lead-efflux ATPase activity" RELATED []
is_a: GO:0046915 ! transition metal ion transmembrane transporter activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
