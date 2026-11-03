# GO_cellular_component_0031: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0031.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **C** — virion component

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAGLNEILLPEVHLNSPIVRYKLFYYILHGQLPNDLEPDDLGPLANQNWKAIRAEESQVHARLKQIRVELIARIPSLRWTRSQREIAILIWPRILPILQAYDLRQSMQLPTVWEKLTQSTVNLISDGLERVVLHISNQLTGKPNLFTRSRAGQDAKDYSIPSTRELSQIWFNNEWSGSVKTWLMIKYRMRQLITNQKTGELTDLVTIVDTRSTLCIITPELVALYSNEHKALTYLTFEMVLMVTDMLEGRLNVSSLCTASHYLSPLKKRIEILLTLVDDLALLMGDKVYGVVSSLESFVYAQLQYGDPVVDIKGTFYGFICNEILDLLTEDNIFTEEEANKVLLDLTSQFDNLSPDLTAELLCIMRLWGHPTLTASQAASKVRESMCAPKVLDFQTIMKTLAFFHAILINGYRRSHNGIWPPTTLHGNAPKSLIEMRHDNSELKYEYVLKNWKSISMLRIHKCFDASPDEDLSIFMKDKAISCPKQDWMGVFRRSLIKQRYRDANRPLPQPFNRRLLLNFLEDDRFDPIKELEYVTSGEYLRDPEFCASYSLKEKEIKATGRIFAKMTKRMRSCQVIAESLLANHAGKLMRENGVVLDQLKLTKSLLTMNQIGIISEHSRRSTADNMTLAHSGSNKHRINNSQFKKNKDSKHEMPDDGFEIAACFLTTDLTKYCLNWRYQVIIPFARTLNSMYGVPHLFEWIHLRLMRSTLYVGDPFNPPSDPTQLDLDTALNDDIFIVSPRGGIEGLCQKLWTMISISTIILSATEANTRVMSMVQGDNQAIAITTRVVRSLSHTEKKEQAYKASKLFFERLRANNHGIGHHLKEQETILSSDFFIYSKRVFYKGRILTQALKNVSKMCLTADILGECSQASCSNLATTVMRLTENGVEKDLCYFLNAFMTIRQLCYDLVFPQTKSLSQDITNAYLNHPILISRLCLLPSQLGGLNFFSCSRLFNRNIGDPLVSAIADVKRLIKAGCLDIWVLYNILGRRPGKGKWSTLAADPYTLNIDYLVPSTTFLKKHAQYTLMERSVNPMLRGVFSENAAEEEEELAQYLLDREVVMPRVAHVILAQSSCGRRKQIQGYLDSTRTIIRYSLEVRPLSAKKLNTVIEYNLLYLSYNLEIIEKPNIVQPFLNAINVDTCSIDIARSLRKLSWATLLNGRPIEGLETPDPIELVHGCLIIGSDECEHCSSGDDKFTWFFLPKGIRLDNDPAFNPPIRVPYIGSKTDERRVASMAYIKGASVSLKSALRLAGVYIWAFGDTEESWQDAYELASTRVNLTLEQLQSLTPLPTSANLVHRLDDGTTQLKFTPASSYAFSSFVHISNDCQVLEIDDQVTDSNLIYQQVMITGLALIETWNNPPINFSVYETTLHLHTGSSCCIRPVESCVVNPPLLPVPFINVPQMNKFVYDPEPLSLLEMEKIEDIAYQTRIGGLDQIPLLEKIPLLAHLTAKQMVNSITGLDEATSIVNDAVVQADYTSNWISECCYTYIDSVFVYSGWALLLELSYQMYYLRIQGIQGILDYVYMTLRRIPGMAITGISSTISHPRILRRCINLDVIAPINSPHIASLDYTKLSIDAVMWGTKQVLTNISQGIDYEIVVPSESQLTLSDRVLNLVARKLSLLAIIWANYNYPPKVKGMSPEDKCQALTTHLLQTVEYVEHIQIEKTNIRRMVIEPKLTAYPSNLFYLSRKLLNAIRDSEEGQFLIASYYNSFGYLEPILMESKIFNLSSSESASLTEFDFILNLELSETSLEKYSLPSLLMTAENMDNPFPQPPLHHVLRPLGLSSTSWYKTISVLNYISHMKIYDGAHLYLAEGSGASMSLIETFLPGETIWYNSLFNSGENPPQRNFAPLPTQFIESVPYRLIQAGIAAGSGVVQSFYPLWNGNSDITDLSTKTSVEYIIHKVGADTCALVHVDLEGVPGSMNSMLERAQVHALLITVTVLKPGGLLILKASWEPFNRFSFLLTILWQFFSTIRILRSSYSDPNNHEVYIIATLAVDPTTSSFTTALNRARTLNEQGFSLIPPELVSEYWRRRVEQGQIIQDRIDKVISECVRDQYLADNNIILQAGGTPSTRKWLDLPDYPSFNELQSEMARLITIHLKEVIEILKGQSSDHDTLLFTSYNVGPLGKINTILRLIVERILMYTVRNWCILPTQTRLTLRQSIELGEFRLRDVITPMEILKLSPNRKYLKSALNQSTFNHLMGETSDILLNRAYQKRIWKAIGCVIYCFGLLTPDVEDSERIDIDNDIPDYDIHGDII

[Multiple Choices]
A. host cell
B. synapse
C. virion component
D. fungal-type vacuole
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

### Expected-answer support: supported

> The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.


**Missing item-specific fact**

> Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.


**Reason**

> The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense.


### Important caveats

- The sequence match is exact, but the accession and database annotation were reviewer-only information.
- The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.
- The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.",
    "reason": "The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database annotation were reviewer-only information.",
    "The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.",
    "The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.",
    "missing_item_specific_fact": "Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.",
    "reason": "The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database annotation were reviewer-only information.",
    "The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.",
    "The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.


**Missing item-specific fact**

> The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.


**Reason**

> While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase.


### Important caveats

- The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).
- The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.
- The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.
- The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.",
    "reason": "While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational."
  },
  "important_caveats": [
    "The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).",
    "The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.",
    "missing_item_specific_fact": "The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.",
    "reason": "While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase."
  },
  "important_caveats": [
    "The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).",
    "The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the protein to the virion, citing experimental-evidence-coded publications. This supports choice C, although the cited studies were not independently assessed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence contains features consistent with a large, multidomain viral RNA-dependent RNA polymerase, including RNA-polymerase and RNA-processing functions. Transferable knowledge of negative-strand RNA virus polymerases supports their association with viral ribonucleoprotein complexes and incorporation into virions, making C meaningfully more likely than a synapse or fungal vacuole; host cell is a broader possible context.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the offered alternatives gives a credible basis for selecting virion component without recalling this exact protein's database entry. It is probabilistic: the sequence alone does not establish its precise localization or experimental annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The polymerase may function inside an infected host cell, but the options ask for a primary component and virion incorporation is a meaningful distinguishing inference; no second option is equally supported by the supplied sequence.


### Important caveats

- Virion component is a GO cellular-component term, but it is not a cellular compartment in the narrow sense implied by the task wording.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence contains features consistent with a large, multidomain viral RNA-dependent RNA polymerase, including RNA-polymerase and RNA-processing functions. Transferable knowledge of negative-strand RNA virus polymerases supports their association with viral ribonucleoprotein complexes and incorporation into virions, making C meaningfully more likely than a synapse or fungal vacuole; host cell is a broader possible context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the offered alternatives gives a credible basis for selecting virion component without recalling this exact protein's database entry. It is probabilistic: the sequence alone does not establish its precise localization or experimental annotation."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the virion, citing experimental-evidence-coded publications. This supports choice C, although the cited studies were not independently assessed here."
  },
  "important_caveats": [
    "Virion component is a GO cellular-component term, but it is not a cellular compartment in the narrow sense implied by the task wording."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polymerase may function inside an infected host cell, but the options ask for a primary component and virion incorporation is a meaningful distinguishing inference; no second option is equally supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the virion, citing experimental-evidence-coded publications. This supports choice C, although the cited studies were not independently assessed here.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence contains features consistent with a large, multidomain viral RNA-dependent RNA polymerase, including RNA-polymerase and RNA-processing functions. Transferable knowledge of negative-strand RNA virus polymerases supports their association with viral ribonucleoprotein complexes and incorporation into virions, making C meaningfully more likely than a synapse or fungal vacuole; host cell is a broader possible context.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the offered alternatives gives a credible basis for selecting virion component without recalling this exact protein's database entry. It is probabilistic: the sequence alone does not establish its precise localization or experimental annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polymerase may function inside an infected host cell, but the options ask for a primary component and virion incorporation is a meaningful distinguishing inference; no second option is equally supported by the supplied sequence."
  },
  "important_caveats": [
    "Virion component is a GO cellular-component term, but it is not a cellular compartment in the narrow sense implied by the task wording."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5SC50, Mumps virus L protein) annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, two mass spectrometry studies of purified virions: PMID 26768080 and PMID 30326905). The GO annotation GO:0044423 'virion component' is assigned via IEA:UniProtKB-KW, but the underlying evidence is experimental proteomic identification of the L protein in purified virion preparations. This is consistent with the well-established biology of Mononegavirales, where the L (RNA-dependent RNA polymerase) protein is an obligate structural component of the virion nucleocapsid complex, packaged to enable transcription upon host entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~2261-residue sequence contains the hallmark multi-domain architecture of a Mononegavirales L protein: conserved RNA-dependent RNA polymerase motifs (motifs A–F with the GDD catalytic triad region), a GTP-binding/helicase domain, a cap methyltransferase domain, and a PRNTase (polyribonucleotidyltransferase) domain. This architecture is shared across Paramyxoviridae, Rhabdoviridae, and Filoviridae L proteins. A transferable, order-level principle of Mononegavirales biology is that the L protein is ALWAYS packaged within the virion as part of the ribonucleoprotein (RNP) complex, because negative-strand RNA viruses must carry their own polymerase to initiate primary transcription immediately upon entry. This is a family/order-level regularity learned from many related viruses (VSV, rabies, measles, Nipah, Ebola L proteins are all virion components). Given this recognition, 'virion component' (C) is strongly favored. The alternatives are readily excluded: 'host cell' (A) applies to host-encoded proteins, not viral structural proteins; 'synapse' (B) requires neuronal localization signals and synaptic protein domains absent here; 'fungal-type vacuole' (D) requires fungal targeting signals and vacuolar hydrolase features absent here. The protein lacks eukaryotic signal peptides, nuclear localization signals, transmembrane segments typical of membrane proteins, or any neuronal/fungal targeting motifs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the RdRp/cap-MTase/GTPase domain architecture from sequence motifs, place it in the Mononegavirales L-protein family, and apply the well-established order-level rule that L proteins are obligate virion components. This is transferable family-level knowledge, not a lookup of this specific protein's annotation. The other three options are eliminated by the absence of host-cell, neuronal, or fungal targeting features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different biological contexts (host protein, neuronal protein, viral particle component, fungal organelle protein). The sequence's viral polymerase architecture and the Mononegavirales packaging rule cleanly select 'virion component' and exclude the others. No ambiguity exists among the offered choices.


### Important caveats

- The GO annotation for virion component is technically IEA (inferred from electronic annotation via UniProt keyword), but the underlying UniProt subcellular location comment is supported by two experimental mass-spectrometry studies of purified virions.
- The model must recognize the sequence as a viral RdRp from domain motifs alone; if it fails to do so, it might default to 'host cell' as a generic fallback, though the absence of eukaryotic targeting features argues against that.
- The reviewer-only evidence confirms the sequence matches Q5SC50 (Mumps virus L protein, strain L-Zagreb vaccine), but the model was not given the organism name or protein name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~2261-residue sequence contains the hallmark multi-domain architecture of a Mononegavirales L protein: conserved RNA-dependent RNA polymerase motifs (motifs A–F with the GDD catalytic triad region), a GTP-binding/helicase domain, a cap methyltransferase domain, and a PRNTase (polyribonucleotidyltransferase) domain. This architecture is shared across Paramyxoviridae, Rhabdoviridae, and Filoviridae L proteins. A transferable, order-level principle of Mononegavirales biology is that the L protein is ALWAYS packaged within the virion as part of the ribonucleoprotein (RNP) complex, because negative-strand RNA viruses must carry their own polymerase to initiate primary transcription immediately upon entry. This is a family/order-level regularity learned from many related viruses (VSV, rabies, measles, Nipah, Ebola L proteins are all virion components). Given this recognition, 'virion component' (C) is strongly favored. The alternatives are readily excluded: 'host cell' (A) applies to host-encoded proteins, not viral structural proteins; 'synapse' (B) requires neuronal localization signals and synaptic protein domains absent here; 'fungal-type vacuole' (D) requires fungal targeting signals and vacuolar hydrolase features absent here. The protein lacks eukaryotic signal peptides, nuclear localization signals, transmembrane segments typical of membrane proteins, or any neuronal/fungal targeting motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the RdRp/cap-MTase/GTPase domain architecture from sequence motifs, place it in the Mononegavirales L-protein family, and apply the well-established order-level rule that L proteins are obligate virion components. This is transferable family-level knowledge, not a lookup of this specific protein's annotation. The other three options are eliminated by the absence of host-cell, neuronal, or fungal targeting features."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5SC50, Mumps virus L protein) annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, two mass spectrometry studies of purified virions: PMID 26768080 and PMID 30326905). The GO annotation GO:0044423 'virion component' is assigned via IEA:UniProtKB-KW, but the underlying evidence is experimental proteomic identification of the L protein in purified virion preparations. This is consistent with the well-established biology of Mononegavirales, where the L (RNA-dependent RNA polymerase) protein is an obligate structural component of the virion nucleocapsid complex, packaged to enable transcription upon host entry."
  },
  "important_caveats": [
    "The GO annotation for virion component is technically IEA (inferred from electronic annotation via UniProt keyword), but the underlying UniProt subcellular location comment is supported by two experimental mass-spectrometry studies of purified virions.",
    "The model must recognize the sequence as a viral RdRp from domain motifs alone; if it fails to do so, it might default to 'host cell' as a generic fallback, though the absence of eukaryotic targeting features argues against that.",
    "The reviewer-only evidence confirms the sequence matches Q5SC50 (Mumps virus L protein, strain L-Zagreb vaccine), but the model was not given the organism name or protein name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different biological contexts (host protein, neuronal protein, viral particle component, fungal organelle protein). The sequence's viral polymerase architecture and the Mononegavirales packaging rule cleanly select 'virion component' and exclude the others. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5SC50, Mumps virus L protein) annotates the subcellular location as 'Virion' with experimental evidence (ECO:0000269, two mass spectrometry studies of purified virions: PMID 26768080 and PMID 30326905). The GO annotation GO:0044423 'virion component' is assigned via IEA:UniProtKB-KW, but the underlying evidence is experimental proteomic identification of the L protein in purified virion preparations. This is consistent with the well-established biology of Mononegavirales, where the L (RNA-dependent RNA polymerase) protein is an obligate structural component of the virion nucleocapsid complex, packaged to enable transcription upon host entry.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~2261-residue sequence contains the hallmark multi-domain architecture of a Mononegavirales L protein: conserved RNA-dependent RNA polymerase motifs (motifs A–F with the GDD catalytic triad region), a GTP-binding/helicase domain, a cap methyltransferase domain, and a PRNTase (polyribonucleotidyltransferase) domain. This architecture is shared across Paramyxoviridae, Rhabdoviridae, and Filoviridae L proteins. A transferable, order-level principle of Mononegavirales biology is that the L protein is ALWAYS packaged within the virion as part of the ribonucleoprotein (RNP) complex, because negative-strand RNA viruses must carry their own polymerase to initiate primary transcription immediately upon entry. This is a family/order-level regularity learned from many related viruses (VSV, rabies, measles, Nipah, Ebola L proteins are all virion components). Given this recognition, 'virion component' (C) is strongly favored. The alternatives are readily excluded: 'host cell' (A) applies to host-encoded proteins, not viral structural proteins; 'synapse' (B) requires neuronal localization signals and synaptic protein domains absent here; 'fungal-type vacuole' (D) requires fungal targeting signals and vacuolar hydrolase features absent here. The protein lacks eukaryotic signal peptides, nuclear localization signals, transmembrane segments typical of membrane proteins, or any neuronal/fungal targeting motifs.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the RdRp/cap-MTase/GTPase domain architecture from sequence motifs, place it in the Mononegavirales L-protein family, and apply the well-established order-level rule that L proteins are obligate virion components. This is transferable family-level knowledge, not a lookup of this specific protein's annotation. The other three options are eliminated by the absence of host-cell, neuronal, or fungal targeting features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different biological contexts (host protein, neuronal protein, viral particle component, fungal organelle protein). The sequence's viral polymerase architecture and the Mononegavirales packaging rule cleanly select 'virion component' and exclude the others. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The GO annotation for virion component is technically IEA (inferred from electronic annotation via UniProt keyword), but the underlying UniProt subcellular location comment is supported by two experimental mass-spectrometry studies of purified virions.",
    "The model must recognize the sequence as a viral RdRp from domain motifs alone; if it fails to do so, it might default to 'host cell' as a generic fallback, though the absence of eukaryotic targeting features argues against that.",
    "The reviewer-only evidence confirms the sequence matches Q5SC50 (Mumps virus L protein, strain L-Zagreb vaccine), but the model was not given the organism name or protein name."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q5SC50",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "a8af8dc510eed4cc7cb22e1027512593af3aa23ae6ff505aeb845075c7f383af",
  "benchmark_sequence_length": 2261,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 117,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "current_source_sequence_sha256": "a8af8dc510eed4cc7cb22e1027512593af3aa23ae6ff505aeb845075c7f383af",
  "current_source_sequence_length": 2261,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 115,
  "selected_historical_version": {
    "accession": "Q5SC50",
    "database": "Swiss-Prot",
    "entryVersion": 115,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "L_MUMPZ",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "selected_historical_source_sequence_sha256": "a8af8dc510eed4cc7cb22e1027512593af3aa23ae6ff505aeb845075c7f383af",
  "selected_historical_source_sequence_length": 2261,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 115,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q5SC50\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":117,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Large structural protein\"}},{\"fullName\":{\"value\":\"Replicase\"}},{\"fullName\":{\"value\":\"Transcriptase\"}}],\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P28887\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.7.48\"}],\"fullName\":{\"value\":\"RNA-directed RNA polymerase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"GTP phosphohydrolase\"}}},{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PRNTase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.7.88\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GDP polyribonucleotidyltransferase\"}}},{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"mRNA (guanine-N(7)-)-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"G-N7-MTase\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"mRNA (nucleoside-2'-O-)-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03523\",\"source\":\"UniProtKB\"}],\"value\":\"N1-2'-O-MTase\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"mRNA cap methyltransferase\"}}}],\"recommendedName\":{\"fullName\":{\"value\":\"RNA-directed RNA polymerase L\"},\"shortNames\":[{\"value\":\"Protein L\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/comments/8",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26768080\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30326905\",\"source\":\"PubMed\"}],\"id\":\"SL-0274\",\"value\":\"Virion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Brgles M.\",\"Bonta M.\",\"Santak M.\",\"Jagusic M.\",\"Forcic D.\",\"Halassy B.\",\"Allmaier G.\",\"Marchetti-Deschmann M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26768080\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12985-016-0463-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"9\",\"id\":\"26768080\",\"journal\":\"Virol. J.\",\"lastPage\":\"9\",\"publicationDate\":\"2016\",\"title\":\"Identification of mumps virus protein and lipid composition by mass spectrometry.\",\"volume\":\"13\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"L-Zagreb vaccine\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC50.json",
  "source_sha256": "4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341",
  "retrieved_utc": "2026-11-02T04:31:28.360866+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Sviben D.\",\"Forcic D.\",\"Halassy B.\",\"Allmaier G.\",\"Marchetti-Deschmann M.\",\"Brgles M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30326905\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12985-018-1073-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"160\",\"id\":\"30326905\",\"journal\":\"Virol. J.\",\"lastPage\":\"160\",\"publicationDate\":\"2018\",\"title\":\"Mass spectrometry-based investigation of measles and mumps virus proteome.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"L-Zagreb vaccine\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115",
  "source_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "retrieved_utc": "2026-11-02T04:31:32.272875+00:00",
  "source_locator": "lines 1-33",
  "excerpt": "ID   L_MUMPZ                 Reviewed;        2261 AA.\nAC   Q5SC50;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 115.\nDE   RecName: Full=RNA-directed RNA polymerase L;\nDE            Short=Protein L;\nDE   AltName: Full=Large structural protein;\nDE   AltName: Full=Replicase;\nDE   AltName: Full=Transcriptase;\nDE   Includes:\nDE     RecName: Full=RNA-directed RNA polymerase;\nDE              EC=2.7.7.48 {ECO:0000250|UniProtKB:P28887};\nDE   Includes:\nDE     RecName: Full=GTP phosphohydrolase {ECO:0000250|UniProtKB:P03523};\nDE              EC=3.6.1.- {ECO:0000250|UniProtKB:P03523};\nDE   Includes:\nDE     RecName: Full=GDP polyribonucleotidyltransferase {ECO:0000305};\nDE              EC=2.7.7.88 {ECO:0000250|UniProtKB:P03523};\nDE     AltName: Full=PRNTase {ECO:0000305};\nDE   Includes:\nDE     RecName: Full=mRNA cap methyltransferase {ECO:0000305};\nDE     AltName: Full=mRNA (guanine-N(7)-)-methyltransferase {ECO:0000250|UniProtKB:P03523};\nDE              Short=G-N7-MTase {ECO:0000250|UniProtKB:P03523};\nDE     AltName: Full=mRNA (nucleoside-2'-O-)-methyltransferase {ECO:0000250|UniProtKB:P03523};\nDE              Short=N1-2'-O-MTase {ECO:0000250|UniProtKB:P03523};\nGN   Name=L;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 115,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115",
  "source_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "retrieved_utc": "2026-11-02T04:31:32.272875+00:00",
  "source_locator": "lines 42-50",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=L-Zagreb vaccine;\nRX   PubMed=26768080; DOI=10.1186/s12985-016-0463-0;\nRA   Brgles M., Bonta M., Santak M., Jagusic M., Forcic D., Halassy B.,\nRA   Allmaier G., Marchetti-Deschmann M.;\nRT   \"Identification of mumps virus protein and lipid composition by mass\nRT   spectrometry.\";\nRL   Virol. J. 13:9-9(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 115,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115",
  "source_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "retrieved_utc": "2026-11-02T04:31:32.272875+00:00",
  "source_locator": "lines 51-59",
  "excerpt": "RN   [3]\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=L-Zagreb vaccine;\nRX   PubMed=30326905; DOI=10.1186/s12985-018-1073-9;\nRA   Sviben D., Forcic D., Halassy B., Allmaier G., Marchetti-Deschmann M.,\nRA   Brgles M.;\nRT   \"Mass spectrometry-based investigation of measles and mumps virus\nRT   proteome.\";\nRL   Virol. J. 15:160-160(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 115,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115",
  "source_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "retrieved_utc": "2026-11-02T04:31:32.272875+00:00",
  "source_locator": "lines 124-125",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000269|PubMed:26768080,\nCC       ECO:0000269|PubMed:30326905}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 115,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115",
  "source_sha256": "676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7",
  "retrieved_utc": "2026-11-02T04:31:32.272875+00:00",
  "source_locator": "lines 137-137",
  "excerpt": "DR   GO; GO:0044423; C:virion component; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 115,
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
  "source_locator": "lines 3480-3488",
  "excerpt": "[Term]\nid: GO:0000324\nname: fungal-type vacuole\nnamespace: cellular_component\ndef: \"A vacuole that has both lytic and storage functions. The fungal vacuole is a large, membrane-bounded organelle that functions as a reservoir for the storage of small molecules (including polyphosphate, amino acids, several divalent cations (e.g. calcium), other ions, and other small molecules) as well as being the primary compartment for degradation. It is an acidic compartment, containing an ensemble of acid hydrolases. At least in S. cerevisiae, there are indications that the morphology of the vacuole is variable and correlated with the cell cycle, with logarithmically growing cells having a multilobed, reticulated vacuole, while stationary phase cells contain a single large structure.\" [GOC:mah, GOC:mtg_sensu, ISBN:0879693649]\nsynonym: \"vacuole, cell cycle-correlated morphology\" EXACT []\nis_a: GO:0000322 ! storage vacuole\nis_a: GO:0000323 ! lytic vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0000324"
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
  "source_locator": "lines 249498-249504",
  "excerpt": "[Term]\nid: GO:0043657\nname: host cell\nnamespace: cellular_component\ndef: \"A cell within a host organism. Includes the host plasma membrane and any external encapsulating structures such as the host cell wall and cell envelope.\" [GOC:jl]\nis_a: GO:0018995 ! host cellular component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0043657"
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
  "source_locator": "lines 257048-257062",
  "excerpt": "[Term]\nid: GO:0044423\nname: virion component\nnamespace: cellular_component\nalt_id: GO:0019012\ndef: \"Any constituent part of a virion, a complete fully infectious extracellular virus particle.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"complete virus particle\" RELATED []\nsynonym: \"virion\" RELATED []\nsynonym: \"virion part\" EXACT []\nxref: Wikipedia:Virus\nis_a: GO:0005575 ! cellular_component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0044423"
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
  "source_locator": "lines 262894-262912",
  "excerpt": "[Term]\nid: GO:0045202\nname: synapse\nnamespace: cellular_component\ndef: \"The junction between an axon of one neuron and a dendrite of another neuron, a muscle fiber or a glial cell. As the axon approaches the synapse it enlarges into a specialized structure, the presynaptic terminal bouton, which contains mitochondria and synaptic vesicles. At the tip of the terminal bouton is the presynaptic membrane; facing it, and separated from it by a minute cleft (the synaptic cleft) is a specialized area of membrane on the receiving cell, known as the postsynaptic membrane. In response to the arrival of nerve impulses, the presynaptic terminal bouton secretes molecules of neurotransmitters into the synaptic cleft. These diffuse across the cleft and transmit the signal to the postsynaptic membrane.\" [GOC:aruk, ISBN:0198506732, PMID:24619342, PMID:29383328, PMID:31998110]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_synapse\nsynonym: \"electrotonic synapse\" RELATED [NIF_Subcellular:sao1311109124]\nsynonym: \"mixed synapse\" NARROW [NIF_Subcellular:sao1506103497]\nsynonym: \"synaptic junction\" EXACT []\nxref: NIF_Subcellular:sao914572699\nxref: Wikipedia:Chemical_synapse\nis_a: GO:0030054 ! cell junction\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0045202"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
