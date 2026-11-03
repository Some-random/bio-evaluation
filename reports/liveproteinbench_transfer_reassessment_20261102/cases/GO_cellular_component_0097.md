# GO_cellular_component_0097: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0097.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **A** — plasma membrane

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | uncertain | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. plasma membrane
B. early endosome membrane
C. striated muscle dense body
D. midbody
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.


**Missing item-specific fact**

> PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.


**Reason**

> The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization.


### Important caveats

- The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.
- The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.",
    "reason": "The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.",
    "The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the vacuole membrane, which conflicts with plasma membrane as the primary location asked for. Plasma membrane is present only as an IEA:TreeGrafter GO annotation, not as experimental localization evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions, supporting that it is a membrane protein, but this does not distinguish plasma membrane from an endosomal or vacuolar membrane.",
    "missing_item_specific_fact": "PyDMT1's specific subcellular localization, which requires protein-specific annotation or experimental evidence.",
    "reason": "The sequence supports membrane association but supplies no reliable targeting or trafficking clue that resolves these membrane compartments. The experimental localization is item-specific and was not provided to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence points to vacuole membrane, which is not offered. Plasma membrane has a computational GO annotation, but no supplied evidence supports early endosome membrane, striated muscle dense body, or midbody; the available choices therefore do not capture the reported experimental localization."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited experimental localization is a UniProt annotation attributed to a publication, not an independent review of that study.",
    "The plasma membrane annotation is computational and does not establish that plasma membrane is the primary location."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C4](#evidence-c4), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.


**Missing item-specific fact**

> The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.


**Reason**

> While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data.


### Important caveats

- The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.
- The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.
- The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.
- The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.
- The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.",
    "reason": "While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "C4",
      "C8"
    ],
    "judgment": "contradicted",
    "reason": "The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.",
    "The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.",
    "The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.",
    "The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.",
    "The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The experimental subcellular location (ECO:0000269, PubMed:38049852) places this protein at the 'Vacuole membrane' (food vacuole), as a multi-pass membrane protein. The protein is named 'Food vacuole resident transporter 1' / 'Divalent metal transporter 1 (PyDMT1).' The only annotation supporting 'plasma membrane' (GO:0005886) carries evidence code IEA:TreeGrafter, a purely computational homology transfer, not experimental evidence. The experimental data contradicts the plasma membrane assignment; the true location is the food vacuole membrane, which is neither plasma membrane nor early endosome membrane.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5", "C4", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane transporter (multiple long hydrophobic stretches in the C-terminal ~450 residues, preceded by a very long hydrophilic N-terminal domain). This eliminates options C (striated muscle dense body — impossible in Plasmodium, which lacks striated muscle) and D (midbody — a cytokinesis bridge structure, not a transporter location). However, distinguishing between plasma membrane (A) and early endosome membrane (B) for a multi-pass transporter requires knowledge of the specific protein identity, its targeting signals, or its experimentally determined localization — none of which are derivable from the sequence alone.",
    "missing_item_specific_fact": "The experimental localization of this protein to the food vacuole membrane (per PubMed:38049852) is the critical fact. Without knowing this is PyDMT1/FVRT1 localized to the food vacuole (a compartment more analogous to endosome/lysosome than plasma membrane), a model cannot distinguish A from B by sequence reasoning alone.",
    "reason": "While the sequence supports 'membrane protein' and eliminates C and D, the A-vs-B distinction for a multi-pass transporter cannot be resolved by general biological reasoning from the sequence. It requires the specific experimental annotation that this transporter resides on the food vacuole membrane."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The true experimental location is the food vacuole membrane, which is not among the options. Between the two membrane options (A: plasma membrane, B: early endosome membrane), the food vacuole is functionally and topologically closer to an endosomal/lysosomal compartment than to the plasma membrane, making B arguably more defensible than A. The expected answer A is supported only by a weak IEA:TreeGrafter computational annotation that is contradicted by experimental data."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is supported only by an IEA:TreeGrafter (automated computational transfer) annotation, not by experimental evidence.",
    "The experimentally determined location (ECO:0000269, PubMed:38049852) is 'Vacuole membrane' (food vacuole), which is not offered as an option.",
    "The food vacuole in Plasmodium is a digestive organelle more analogous to a lysosome/endosome than to the plasma membrane, making option B potentially closer to the true location than option A.",
    "The GO:0005886 (plasma membrane) annotation is a homology-based computational transfer (IEA:TreeGrafter) and should not be treated as equivalent to experimental evidence.",
    "The sequence matches the UniProt entry A0A077Y877 exactly (696 aa), confirmed in both current and historical (v38) records."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: uncertain

> The exact-sequence record contains a computational GO annotation to plasma membrane, but also reports experimentally supported vacuole-membrane localization. These support different locations, and the evidence does not establish whether plasma membrane is the protein’s primary location or whether it also localizes there.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments strongly suggest a multipass membrane protein, making the membrane choices A and B more plausible than the specialized structures C and D. But multipass topology alone does not distinguish plasma membrane from early endosome membrane; transport activity or membrane insertion does not determine the destination.


**Missing item-specific fact**

> The protein’s actual trafficking destination or experimentally established cellular localization is needed to choose between plasma membrane and early endosome membrane.


**Reason**

> Transferable sequence-based reasoning can identify a membrane protein, but does not meaningfully resolve the two offered membrane locations. A localization fact about this protein is needed for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the original sequence, both plasma membrane and early endosome membrane are plausible destinations for a multipass membrane protein, and the sequence does not clearly distinguish them. The reviewer-only evidence additionally reports vacuole-membrane localization, a location not offered.


### Important caveats

- The plasma-membrane GO annotation is computational (IEA:TreeGrafter), whereas the vacuole-membrane location is reported with experimental evidence.
- The source evidence is reviewer-only and was not available as an input to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments strongly suggest a multipass membrane protein, making the membrane choices A and B more plausible than the specialized structures C and D. But multipass topology alone does not distinguish plasma membrane from early endosome membrane; transport activity or membrane insertion does not determine the destination.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s actual trafficking destination or experimentally established cellular localization is needed to choose between plasma membrane and early endosome membrane.",
    "reason": "Transferable sequence-based reasoning can identify a membrane protein, but does not meaningfully resolve the two offered membrane locations. A localization fact about this protein is needed for that distinction."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "cannot_determine",
    "reason": "The exact-sequence record contains a computational GO annotation to plasma membrane, but also reports experimentally supported vacuole-membrane localization. These support different locations, and the evidence does not establish whether plasma membrane is the protein’s primary location or whether it also localizes there."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computational (IEA:TreeGrafter), whereas the vacuole-membrane location is reported with experimental evidence.",
    "The source evidence is reviewer-only and was not available as an input to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the original sequence, both plasma membrane and early endosome membrane are plausible destinations for a multipass membrane protein, and the sequence does not clearly distinguish them. The reviewer-only evidence additionally reports vacuole-membrane localization, a location not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The exact-sequence record contains a computational GO annotation to plasma membrane, but also reports experimentally supported vacuole-membrane localization. These support different locations, and the evidence does not establish whether plasma membrane is the protein’s primary location or whether it also localizes there.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments strongly suggest a multipass membrane protein, making the membrane choices A and B more plausible than the specialized structures C and D. But multipass topology alone does not distinguish plasma membrane from early endosome membrane; transport activity or membrane insertion does not determine the destination.",
    "missing_item_specific_fact": "The protein’s actual trafficking destination or experimentally established cellular localization is needed to choose between plasma membrane and early endosome membrane.",
    "reason": "Transferable sequence-based reasoning can identify a membrane protein, but does not meaningfully resolve the two offered membrane locations. A localization fact about this protein is needed for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the original sequence, both plasma membrane and early endosome membrane are plausible destinations for a multipass membrane protein, and the sequence does not clearly distinguish them. The reviewer-only evidence additionally reports vacuole-membrane localization, a location not offered."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is computational (IEA:TreeGrafter), whereas the vacuole-membrane location is reported with experimental evidence.",
    "The source evidence is reviewer-only and was not available as an input to the evaluated model."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The experimental subcellular location annotation (ECO:0000269, PubMed:38049852) explicitly places this protein at the 'Vacuole membrane' (food vacuole membrane) as a multi-pass membrane protein. The GO:0005886 'plasma membrane' annotation exists only as IEA:TreeGrafter (a computational homology-based prediction), not as experimental evidence. The GO:0005774 'vacuolar membrane' annotation (IEA:UniProtKB-SubCell) is derived from the actual experimental UniProt comment. The strongest evidence (experimental, ECO:0000269) contradicts 'plasma membrane' by placing the protein at the food vacuole membrane, a distinct intracellular compartment. The author's key relies on the weaker IEA:TreeGrafter prediction rather than the experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence clearly encodes a multi-pass membrane protein with numerous hydrophobic transmembrane segments (~10+ predicted TM helices), immediately eliminating C (striated muscle dense body, a cytoplasmic/cytoskeletal structure found in nematodes) and D (midbody, a transient cytoplasmic bridge during cytokinesis). Between A (plasma membrane) and B (early endosome membrane), a weak but defensible transferable argument favors A: the protein has a very long N-terminal region (~150+ residues) before the first TM helix, consistent with a large cytoplasmic domain typical of plasma membrane transporters; no canonical endosomal sorting motifs (dileucine &#91;DE&#93;XXXL&#91;LI&#93;, tyrosine-based YXXΦ) are readily identifiable; and the overall multi-TM transporter architecture resembles well-known plasma membrane divalent metal transporters (e.g., human DMT1/SLC11A2 family members at the apical enterocyte membrane). Family-level knowledge of NRAMP/DMT1-type transporters in other organisms supports plasma membrane localization as the default for this transporter class absent specific endosomal targeting signals.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D definitively (non-membrane, non-transporter structures) and use general multi-pass membrane protein topology, absence of endosomal sorting motifs, and family-level analogy to DMT1/NRAMP transporters to weakly favor plasma membrane over early endosome membrane. The A-vs-B distinction is not strongly supported by sequence alone, but the offered alternatives make A the more defensible default among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> For a multi-pass membrane transporter without obvious endosomal targeting signals, both plasma membrane (A) and early endosome membrane (B) are plausible from sequence alone. Many membrane transporters traffic through or reside in endosomal compartments. The experimental evidence actually places this protein at the food vacuole membrane (neither A nor B), making the question's premise imperfect. However, among the four offered choices, C and D are clearly eliminable, leaving A and B as the contestable pair.


### Important caveats

- The experimental evidence (ECO:0000269) places the protein at the food vacuole membrane, which is neither 'plasma membrane' nor 'early endosome membrane' among the offered choices. The author's key (A) is supported only by IEA:TreeGrafter computational prediction, not by the experimental data.
- The protein is from Plasmodium yoelii (an apicomplexan parasite); the 'food vacuole' is a parasite-specific digestive compartment, not a standard eukaryotic endosome or plasma membrane. The GO ontology does not have a 'food vacuole membrane' term, forcing an imperfect mapping.
- The N-rich, low-complexity regions in the sequence are characteristic of Plasmodium proteins but do not by themselves indicate a specific membrane compartment.
- The IEA:TreeGrafter annotation for 'plasma membrane' is a homology-based prediction that appears to conflict with the experimental finding of food vacuole localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane protein with numerous hydrophobic transmembrane segments (~10+ predicted TM helices), immediately eliminating C (striated muscle dense body, a cytoplasmic/cytoskeletal structure found in nematodes) and D (midbody, a transient cytoplasmic bridge during cytokinesis). Between A (plasma membrane) and B (early endosome membrane), a weak but defensible transferable argument favors A: the protein has a very long N-terminal region (~150+ residues) before the first TM helix, consistent with a large cytoplasmic domain typical of plasma membrane transporters; no canonical endosomal sorting motifs (dileucine [DE]XXXL[LI], tyrosine-based YXXΦ) are readily identifiable; and the overall multi-TM transporter architecture resembles well-known plasma membrane divalent metal transporters (e.g., human DMT1/SLC11A2 family members at the apical enterocyte membrane). Family-level knowledge of NRAMP/DMT1-type transporters in other organisms supports plasma membrane localization as the default for this transporter class absent specific endosomal targeting signals.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D definitively (non-membrane, non-transporter structures) and use general multi-pass membrane protein topology, absence of endosomal sorting motifs, and family-level analogy to DMT1/NRAMP transporters to weakly favor plasma membrane over early endosome membrane. The A-vs-B distinction is not strongly supported by sequence alone, but the offered alternatives make A the more defensible default among the choices."
  },
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "contradicted",
    "reason": "The experimental subcellular location annotation (ECO:0000269, PubMed:38049852) explicitly places this protein at the 'Vacuole membrane' (food vacuole membrane) as a multi-pass membrane protein. The GO:0005886 'plasma membrane' annotation exists only as IEA:TreeGrafter (a computational homology-based prediction), not as experimental evidence. The GO:0005774 'vacuolar membrane' annotation (IEA:UniProtKB-SubCell) is derived from the actual experimental UniProt comment. The strongest evidence (experimental, ECO:0000269) contradicts 'plasma membrane' by placing the protein at the food vacuole membrane, a distinct intracellular compartment. The author's key relies on the weaker IEA:TreeGrafter prediction rather than the experimental determination."
  },
  "important_caveats": [
    "The experimental evidence (ECO:0000269) places the protein at the food vacuole membrane, which is neither 'plasma membrane' nor 'early endosome membrane' among the offered choices. The author's key (A) is supported only by IEA:TreeGrafter computational prediction, not by the experimental data.",
    "The protein is from Plasmodium yoelii (an apicomplexan parasite); the 'food vacuole' is a parasite-specific digestive compartment, not a standard eukaryotic endosome or plasma membrane. The GO ontology does not have a 'food vacuole membrane' term, forcing an imperfect mapping.",
    "The N-rich, low-complexity regions in the sequence are characteristic of Plasmodium proteins but do not by themselves indicate a specific membrane compartment.",
    "The IEA:TreeGrafter annotation for 'plasma membrane' is a homology-based prediction that appears to conflict with the experimental finding of food vacuole localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "For a multi-pass membrane transporter without obvious endosomal targeting signals, both plasma membrane (A) and early endosome membrane (B) are plausible from sequence alone. Many membrane transporters traffic through or reside in endosomal compartments. The experimental evidence actually places this protein at the food vacuole membrane (neither A nor B), making the question's premise imperfect. However, among the four offered choices, C and D are clearly eliminable, leaving A and B as the contestable pair."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0097",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The experimental subcellular location annotation (ECO:0000269, PubMed:38049852) explicitly places this protein at the 'Vacuole membrane' (food vacuole membrane) as a multi-pass membrane protein. The GO:0005886 'plasma membrane' annotation exists only as IEA:TreeGrafter (a computational homology-based prediction), not as experimental evidence. The GO:0005774 'vacuolar membrane' annotation (IEA:UniProtKB-SubCell) is derived from the actual experimental UniProt comment. The strongest evidence (experimental, ECO:0000269) contradicts 'plasma membrane' by placing the protein at the food vacuole membrane, a distinct intracellular compartment. The author's key relies on the weaker IEA:TreeGrafter prediction rather than the experimental determination.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence clearly encodes a multi-pass membrane protein with numerous hydrophobic transmembrane segments (~10+ predicted TM helices), immediately eliminating C (striated muscle dense body, a cytoplasmic/cytoskeletal structure found in nematodes) and D (midbody, a transient cytoplasmic bridge during cytokinesis). Between A (plasma membrane) and B (early endosome membrane), a weak but defensible transferable argument favors A: the protein has a very long N-terminal region (~150+ residues) before the first TM helix, consistent with a large cytoplasmic domain typical of plasma membrane transporters; no canonical endosomal sorting motifs (dileucine [DE]XXXL[LI], tyrosine-based YXXΦ) are readily identifiable; and the overall multi-TM transporter architecture resembles well-known plasma membrane divalent metal transporters (e.g., human DMT1/SLC11A2 family members at the apical enterocyte membrane). Family-level knowledge of NRAMP/DMT1-type transporters in other organisms supports plasma membrane localization as the default for this transporter class absent specific endosomal targeting signals.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D definitively (non-membrane, non-transporter structures) and use general multi-pass membrane protein topology, absence of endosomal sorting motifs, and family-level analogy to DMT1/NRAMP transporters to weakly favor plasma membrane over early endosome membrane. The A-vs-B distinction is not strongly supported by sequence alone, but the offered alternatives make A the more defensible default among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "For a multi-pass membrane transporter without obvious endosomal targeting signals, both plasma membrane (A) and early endosome membrane (B) are plausible from sequence alone. Many membrane transporters traffic through or reside in endosomal compartments. The experimental evidence actually places this protein at the food vacuole membrane (neither A nor B), making the question's premise imperfect. However, among the four offered choices, C and D are clearly eliminable, leaving A and B as the contestable pair."
  },
  "important_caveats": [
    "The experimental evidence (ECO:0000269) places the protein at the food vacuole membrane, which is neither 'plasma membrane' nor 'early endosome membrane' among the offered choices. The author's key (A) is supported only by IEA:TreeGrafter computational prediction, not by the experimental data.",
    "The protein is from Plasmodium yoelii (an apicomplexan parasite); the 'food vacuole' is a parasite-specific digestive compartment, not a standard eukaryotic endosome or plasma membrane. The GO ontology does not have a 'food vacuole membrane' term, forcing an imperfect mapping.",
    "The N-rich, low-complexity regions in the sequence are characteristic of Plasmodium proteins but do not by themselves indicate a specific membrane compartment.",
    "The IEA:TreeGrafter annotation for 'plasma membrane' is a homology-based prediction that appears to conflict with the experimental finding of food vacuole localization."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_location_annotations_require_qualification`.

> C5/H3 annotate vacuole membrane with ECO:0000269; C6/H4 separately carry plasma membrane as IEA:TreeGrafter.

**Remaining uncertainty:** The excerpts favor a different experimentally annotated location but do not independently establish that plasma-membrane localization never occurs.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A077Y877",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "benchmark_sequence_length": 696,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "current_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "current_source_sequence_length": 696,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 38,
  "selected_historical_version": {
    "accession": "A0A077Y877",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DMT1_PLAYE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "selected_historical_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "selected_historical_source_sequence_length": 696,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A077Y877\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium yoelii\",\"taxonId\":5861}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I3M7\",\"source\":\"UniProtKB\"}],\"value\":\"Food vacuole resident transporter 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"Divalent metal transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"PyDMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"id\":\"SL-0271\",\"value\":\"Vacuole membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005774\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:vacuolar membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhong M.\",\"Zhou B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38049852\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12915-023-01776-y\"}],\"citationType\":\"journal article\",\"firstPage\":\"279\",\"id\":\"38049852\",\"journal\":\"BMC Biol.\",\"lastPage\":\"279\",\"publicationDate\":\"2023\",\"title\":\"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and is required in full activity for malarial pathogenesis.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   DMT1_PLAYE              Reviewed;         696 AA.\nAC   A0A077Y877;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};\nDE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};\nDE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   Name=FVRT1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   ORFNames=PY17X_1241800 {ECO:0000312|EMBL:VTZ80216.1},\nGN   PYYM_1241000 {ECO:0000312|EMBL:CDU19580.1};\nOS   Plasmodium yoelii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5861 {ECO:0000312|Proteomes:UP000072904};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 38,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "source_locator": "lines 29-36",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=38049852; DOI=10.1186/s12915-023-01776-y;\nRA   Zhong M., Zhou B.;\nRT   \"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and\nRT   is required in full activity for malarial pathogenesis.\";\nRL   BMC Biol. 21:279-279(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 38,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "source_locator": "lines 43-44",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Vacuole membrane {ECO:0000269|PubMed:38049852};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 38,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "source_locator": "lines 73-73",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 38,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "source_locator": "lines 74-74",
  "excerpt": "DR   GO; GO:0005774; C:vacuolar membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 38,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 166648-166656",
  "excerpt": "[Term]\nid: GO:0030496\nname: midbody\nnamespace: cellular_component\ndef: \"A thin cytoplasmic bridge formed between daughter cells at the end of cytokinesis. The midbody forms where the contractile ring constricts, and may persist for some time before finally breaking to complete cytokinesis.\" [ISBN:0815316194]\nsubset: goslim_pir\nxref: Wikipedia:Midbody_(cell_biology)\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0030496"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 180777-180784",
  "excerpt": "[Term]\nid: GO:0031901\nname: early endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an early endosome.\" [GOC:pz]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0005769 ! early endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031901"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 343547-343554",
  "excerpt": "[Term]\nid: GO:0055120\nname: striated muscle dense body\nnamespace: cellular_component\ndef: \"A vinculin-containing myofibril attachment structure of striated muscle that connects sarcomeres to the extracellular matrix. In nematode body wall muscle, the dense body performs the dual role of Z-disk and costamere.\" [GOC:kmv, PMID:17492481]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0043292 ! contractile muscle fiber\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0055120"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
