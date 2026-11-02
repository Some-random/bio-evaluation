# GO_molecular_function_0082

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — aspartate kinase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. aspartate kinase activity
B. dioxygenase activity
C. mannose-6-phosphate isomerase activity
D. O-methyltransferase activity
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

> The supplied sequence exactly matches the Candida albicans aspartokinase entry. UniProt assigns aspartokinase activity and the corresponding reaction, but the cited functional evidence is transferred from P10869 (ECO:0000250); the GO annotation is also inferred by sequence orthology. This supports choice A as an annotation, not as direct experimental confirmation for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying an enzyme, but no supplied context or unmistakable general feature distinguishes aspartokinase from the other specific enzyme activities. Assigning this particular function requires protein-specific homology or annotation evidence.


**Missing item-specific fact**

> The sequence's correspondence to the Candida albicans HOM3/aspartokinase protein, or equivalent protein-specific functional evidence, is not provided in the question.


**Reason**

> Recognizing the sequence or using a homology database could select A, but that is an item-specific lookup rather than a distinction established by the input through general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein annotation specifically supports aspartokinase activity; the evidence does not support another listed option for this sequence.


### Important caveats

- The UniProt function and catalytic activity evidence are transferred from P10869 rather than cited as direct experimental evidence for the matched Candida sequence.
- The historical and current records match the supplied sequence, but the author's exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying an enzyme, but no supplied context or unmistakable general feature distinguishes aspartokinase from the other specific enzyme activities. Assigning this particular function requires protein-specific homology or annotation evidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's correspondence to the Candida albicans HOM3/aspartokinase protein, or equivalent protein-specific functional evidence, is not provided in the question.",
    "reason": "Recognizing the sequence or using a homology database could select A, but that is an item-specific lookup rather than a distinction established by the input through general biological reasoning."
  },
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Candida albicans aspartokinase entry. UniProt assigns aspartokinase activity and the corresponding reaction, but the cited functional evidence is transferred from P10869 (ECO:0000250); the GO annotation is also inferred by sequence orthology. This supports choice A as an annotation, not as direct experimental confirmation for this sequence."
  },
  "important_caveats": [
    "The UniProt function and catalytic activity evidence are transferred from P10869 rather than cited as direct experimental evidence for the matched Candida sequence.",
    "The historical and current records match the supplied sequence, but the author's exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation specifically supports aspartokinase activity; the evidence does not support another listed option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Candida albicans aspartokinase entry. UniProt assigns aspartokinase activity and the corresponding reaction, but the cited functional evidence is transferred from P10869 (ECO:0000250); the GO annotation is also inferred by sequence orthology. This supports choice A as an annotation, not as direct experimental confirmation for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying an enzyme, but no supplied context or unmistakable general feature distinguishes aspartokinase from the other specific enzyme activities. Assigning this particular function requires protein-specific homology or annotation evidence.",
    "missing_item_specific_fact": "The sequence's correspondence to the Candida albicans HOM3/aspartokinase protein, or equivalent protein-specific functional evidence, is not provided in the question.",
    "reason": "Recognizing the sequence or using a homology database could select A, but that is an item-specific lookup rather than a distinction established by the input through general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation specifically supports aspartokinase activity; the evidence does not support another listed option for this sequence."
  },
  "important_caveats": [
    "The UniProt function and catalytic activity evidence are transferred from P10869 rather than cited as direct experimental evidence for the matched Candida sequence.",
    "The historical and current records match the supplied sequence, but the author's exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A1D8PMB8 (AK_CANAL, Candida albicans HOM3) with 100% identity. The entry is annotated as Aspartokinase (EC 2.7.2.4) with catalytic activity L-aspartate + ATP = 4-phospho-L-aspartate + ADP, and carries GO:0004072 (aspartate kinase activity). The evidence codes are ECO:0000250 (Inferred from Sequence Similarity to P10869) and ISS/IBA, indicating computational transfer rather than direct experimentation, but the annotation is consistent and well-supported by homology to the characterized S. cerevisiae aspartokinase.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 544-residue sequence contains multiple glycine-rich loops (e.g., 'GATGGWIVQKFGGTSVGK', 'GVGRGYTDLCAALAA', 'GKGTIIYPDNIGRR') characteristic of nucleotide-binding/kinase architecture. This bilobal kinase fold with regulatory + catalytic domains is inconsistent with a dioxygenase (which requires iron-coordinating His/Asp/Glu clusters and a different fold), a mannose-6-phosphate isomerase (typically ~250 aa, aldose-ketose isomerase fold), or an O-methyltransferase (Rossmann-fold SAM-binding, typically ~250-350 aa). Among the four options, only 'aspartate kinase activity' corresponds to a kinase/transferase with this architecture. The N-terminal region containing 'CSARSS' and the overall regulatory+kinase bilobal arrangement is consistent with the ACT-domain-containing amino acid kinase family, of which aspartate kinase is the canonical member.


**Missing item-specific fact**

> Precise identification of 'aspartate' (vs. glutamate or N-acetylglutamate) kinase specificity from raw sequence requires recognition of the ACT regulatory domain and specific active-site residues that confer substrate selectivity within the amino acid kinase superfamily. However, among the four provided choices, the kinase architecture alone is sufficient to eliminate B, C, and D.


**Reason**

> The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase). The glycine-rich loops, ATP-binding motifs, and bilobal regulatory+catalytic architecture in the sequence provide a concrete biological argument for a kinase/transferase, which eliminates dioxygenase, isomerase, and methyltransferase. The ACT-domain-like N-terminal region further supports the amino acid kinase family. While pinpointing 'aspartate' specificity within the amino acid kinase superfamily is challenging from sequence alone, the question only requires choosing among the four given options, and the kinase architecture clearly distinguishes A from the other three.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (phosphotransferase, oxidoreductase, isomerase, methyltransferase). The kinase architecture in the sequence unambiguously points to option A among these choices. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) to S. cerevisiae P10869, not direct experimental characterization of the Candida albicans protein.
- The entry was first publicly released in 2025-02-05 and reviewed in 2025-03; the exact author data-construction date is unknown, though the sequence version has been stable since 2017.
- Identifying the ACT regulatory domain and confirming 'aspartate' (rather than another amino acid) specificity from raw sequence is a non-trivial structural inference; the reasoning argument primarily distinguishes kinase from non-kinase options among the four choices.
- The GO annotation evidence codes are ISS and IBA (computational), not ID (direct experimental), so the functional assignment is inferential.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 544-residue sequence contains multiple glycine-rich loops (e.g., 'GATGGWIVQKFGGTSVGK', 'GVGRGYTDLCAALAA', 'GKGTIIYPDNIGRR') characteristic of nucleotide-binding/kinase architecture. This bilobal kinase fold with regulatory + catalytic domains is inconsistent with a dioxygenase (which requires iron-coordinating His/Asp/Glu clusters and a different fold), a mannose-6-phosphate isomerase (typically ~250 aa, aldose-ketose isomerase fold), or an O-methyltransferase (Rossmann-fold SAM-binding, typically ~250-350 aa). Among the four options, only 'aspartate kinase activity' corresponds to a kinase/transferase with this architecture. The N-terminal region containing 'CSARSS' and the overall regulatory+kinase bilobal arrangement is consistent with the ACT-domain-containing amino acid kinase family, of which aspartate kinase is the canonical member.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of 'aspartate' (vs. glutamate or N-acetylglutamate) kinase specificity from raw sequence requires recognition of the ACT regulatory domain and specific active-site residues that confer substrate selectivity within the amino acid kinase superfamily. However, among the four provided choices, the kinase architecture alone is sufficient to eliminate B, C, and D.",
    "reason": "The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase). The glycine-rich loops, ATP-binding motifs, and bilobal regulatory+catalytic architecture in the sequence provide a concrete biological argument for a kinase/transferase, which eliminates dioxygenase, isomerase, and methyltransferase. The ACT-domain-like N-terminal region further supports the amino acid kinase family. While pinpointing 'aspartate' specificity within the amino acid kinase superfamily is challenging from sequence alone, the question only requires choosing among the four given options, and the kinase architecture clearly distinguishes A from the other three."
  },
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A1D8PMB8 (AK_CANAL, Candida albicans HOM3) with 100% identity. The entry is annotated as Aspartokinase (EC 2.7.2.4) with catalytic activity L-aspartate + ATP = 4-phospho-L-aspartate + ADP, and carries GO:0004072 (aspartate kinase activity). The evidence codes are ECO:0000250 (Inferred from Sequence Similarity to P10869) and ISS/IBA, indicating computational transfer rather than direct experimentation, but the annotation is consistent and well-supported by homology to the characterized S. cerevisiae aspartokinase."
  },
  "important_caveats": [
    "The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) to S. cerevisiae P10869, not direct experimental characterization of the Candida albicans protein.",
    "The entry was first publicly released in 2025-02-05 and reviewed in 2025-03; the exact author data-construction date is unknown, though the sequence version has been stable since 2017.",
    "Identifying the ACT regulatory domain and confirming 'aspartate' (rather than another amino acid) specificity from raw sequence is a non-trivial structural inference; the reasoning argument primarily distinguishes kinase from non-kinase options among the four choices.",
    "The GO annotation evidence codes are ISS and IBA (computational), not ID (direct experimental), so the functional assignment is inferential."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (phosphotransferase, oxidoreductase, isomerase, methyltransferase). The kinase architecture in the sequence unambiguously points to option A among these choices. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A1D8PMB8 (AK_CANAL, Candida albicans HOM3) with 100% identity. The entry is annotated as Aspartokinase (EC 2.7.2.4) with catalytic activity L-aspartate + ATP = 4-phospho-L-aspartate + ADP, and carries GO:0004072 (aspartate kinase activity). The evidence codes are ECO:0000250 (Inferred from Sequence Similarity to P10869) and ISS/IBA, indicating computational transfer rather than direct experimentation, but the annotation is consistent and well-supported by homology to the characterized S. cerevisiae aspartokinase.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 544-residue sequence contains multiple glycine-rich loops (e.g., 'GATGGWIVQKFGGTSVGK', 'GVGRGYTDLCAALAA', 'GKGTIIYPDNIGRR') characteristic of nucleotide-binding/kinase architecture. This bilobal kinase fold with regulatory + catalytic domains is inconsistent with a dioxygenase (which requires iron-coordinating His/Asp/Glu clusters and a different fold), a mannose-6-phosphate isomerase (typically ~250 aa, aldose-ketose isomerase fold), or an O-methyltransferase (Rossmann-fold SAM-binding, typically ~250-350 aa). Among the four options, only 'aspartate kinase activity' corresponds to a kinase/transferase with this architecture. The N-terminal region containing 'CSARSS' and the overall regulatory+kinase bilobal arrangement is consistent with the ACT-domain-containing amino acid kinase family, of which aspartate kinase is the canonical member.",
    "missing_item_specific_fact": "Precise identification of 'aspartate' (vs. glutamate or N-acetylglutamate) kinase specificity from raw sequence requires recognition of the ACT regulatory domain and specific active-site residues that confer substrate selectivity within the amino acid kinase superfamily. However, among the four provided choices, the kinase architecture alone is sufficient to eliminate B, C, and D.",
    "reason": "The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase). The glycine-rich loops, ATP-binding motifs, and bilobal regulatory+catalytic architecture in the sequence provide a concrete biological argument for a kinase/transferase, which eliminates dioxygenase, isomerase, and methyltransferase. The ACT-domain-like N-terminal region further supports the amino acid kinase family. While pinpointing 'aspartate' specificity within the amino acid kinase superfamily is challenging from sequence alone, the question only requires choosing among the four given options, and the kinase architecture clearly distinguishes A from the other three."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (phosphotransferase, oxidoreductase, isomerase, methyltransferase). The kinase architecture in the sequence unambiguously points to option A among these choices. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) to S. cerevisiae P10869, not direct experimental characterization of the Candida albicans protein.",
    "The entry was first publicly released in 2025-02-05 and reviewed in 2025-03; the exact author data-construction date is unknown, though the sequence version has been stable since 2017.",
    "Identifying the ACT regulatory domain and confirming 'aspartate' (rather than another amino acid) specificity from raw sequence is a non-trivial structural inference; the reasoning argument primarily distinguishes kinase from non-kinase options among the four choices.",
    "The GO annotation evidence codes are ISS and IBA (computational), not ID (direct experimental), so the functional assignment is inferential."
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

**Accession:** `A0A1D8PMB8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
"A0A1D8PMB8"
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"value":"Aspartokinase"}}}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"Phosphorylates aspartate, the first step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine"}]}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23777"}}],"reaction":{"ecNumber":"2.7.2.4","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"name":"L-aspartate + ATP = 4-phospho-L-aspartate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23776"},{"database":"ChEBI","id":"CHEBI:29991"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"database":"GO","id":"GO:0004072","properties":[{"key":"GoTerm","value":"F:aspartate kinase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
ID   AK_CANAL                Reviewed;         544 AA.
AC   A0A1D8PMB8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JAN-2017, sequence version 1.
DT   18-JUN-2025, entry version 39.
DE   RecName: Full=Aspartokinase;
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};
GN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},
GN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};
OS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
OX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 59-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
CC   -!- FUNCTION: Phosphorylates aspartate, the first step in the biosynthesis
CC       of amino acids that derive from aspartate (the aspartate family of
CC       amino acids), including methioinine and threonine, the latter of which
CC       is a precursor to isoleucine. {ECO:0000250|UniProtKB:P10869}.
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 63-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;
CC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 104-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
DR   GO; GO:0004072; F:aspartate kinase activity; IBA:GO_Central.
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 34816-34833`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004072
name: aspartate kinase activity
namespace: molecular_function
def: "Catalysis of the reaction: L-aspartate + ATP = 4-phospho-L-aspartate + ADP + H+." [EC:2.7.2.4, RHEA:23776]
synonym: "aspartic kinase activity" RELATED [EC:2.7.2.4]
synonym: "aspartokinase activity" RELATED [EC:2.7.2.4]
synonym: "ATP:L-aspartate 4-phosphotransferase activity" RELATED [EC:2.7.2.4]
synonym: "beta-aspartokinase activity" RELATED [EC:2.7.2.4]
xref: EC:2.7.2.4
xref: KEGG_REACTION:R00480
xref: MetaCyc:ASPARTATEKIN-RXN
xref: RHEA:23776
is_a: GO:0016774 ! phosphotransferase activity, carboxyl group as acceptor
is_a: GO:0019202 ! amino acid kinase activity
property_value: skos:exactMatch EC:2.7.2.4
property_value: skos:exactMatch RHEA:23776

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
