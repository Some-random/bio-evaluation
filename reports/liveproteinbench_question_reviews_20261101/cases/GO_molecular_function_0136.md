# GO_molecular_function_0136

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — hydrolase activity, hydrolyzing O-glycosyl compounds

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGSVNSFDGSGDITYDSNGASFTVAKSGDAPTLSSIFYIMFGKVQITMKAAPGAGIVSTLVLQSDDLDEIDMEWLGADDTEVQTNYFGKGKVTDYNRGAFNPAANNQGEFITYTIEWTSEQVVWSVGSTVVRVLTPATADTDQYPQSPMQIKFGAWSGGDSSNAAGTISWARGPTDYSNGPFTMVVQSIDVSDYSTGTQYKYGDQSGDWTSIEAIGGSVNGNVPASASSIQTAGAAAVTSSSPTIPAGINNGNSATRTGYPWVAGTQTVSEVTWSTGPSIPSGWEISSEGKIVPVSASPINISRINPLLLCGPFTFFFFAAIRRWP

[Multiple Choices]
A. carbohydrate derivative binding
B. mechanosensitive monoatomic cation channel activity
C. hydrolase activity, hydrolyzing O-glycosyl compounds
D. ankyrin repeat binding
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

> The sequence-matched UniProt entry describes a dual chitinase/transglycosylase and gives an endochitinase reaction (C4–C6). Its endochitinase GO annotation is a descendant of the option's broader O-glycosyl hydrolase term (GO1–GO3). The enzymatic evidence is partly transferred by similarity, so this supports the key without showing that every activity was directly assayed for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a secreted fungal cell-wall protein, which makes a membrane channel or ankyrin-binding protein less plausible. But that broad context does not establish hydrolysis rather than carbohydrate binding or another carbohydrate-related activity.


**Missing item-specific fact**

> A protein-specific functional annotation or experimental/homology evidence identifying chitinase activity is needed to distinguish C from the plausible carbohydrate-related alternative A.


**Reason**

> The supplied sequence and choices do not provide a sufficiently specific, independently interpretable motif or context that establishes the exact molecular activity. Recognizing the protein or relying on an external annotation would supply the needed fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported as a broad GO parent term for endochitinase activity. The evidence also describes transglycosylase activity, but that is not among the choices; it does not establish another listed option.


### Important caveats

- The sequence match and accession were established using reviewer-only sources and were not supplied to the evaluated model.
- The UniProt record's catalytic activity annotation is transferred by similarity; the exact experimental basis and source snapshot used by the question author are not established.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted fungal cell-wall protein, which makes a membrane channel or ankyrin-binding protein less plausible. But that broad context does not establish hydrolysis rather than carbohydrate binding or another carbohydrate-related activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental/homology evidence identifying chitinase activity is needed to distinguish C from the plausible carbohydrate-related alternative A.",
    "reason": "The supplied sequence and choices do not provide a sufficiently specific, independently interpretable motif or context that establishes the exact molecular activity. Recognizing the protein or relying on an external annotation would supply the needed fact."
  },
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes a dual chitinase/transglycosylase and gives an endochitinase reaction (C4–C6). Its endochitinase GO annotation is a descendant of the option's broader O-glycosyl hydrolase term (GO1–GO3). The enzymatic evidence is partly transferred by similarity, so this supports the key without showing that every activity was directly assayed for this exact protein."
  },
  "important_caveats": [
    "The sequence match and accession were established using reviewer-only sources and were not supplied to the evaluated model.",
    "The UniProt record's catalytic activity annotation is transferred by similarity; the exact experimental basis and source snapshot used by the question author are not established."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported as a broad GO parent term for endochitinase activity. The evidence also describes transglycosylase activity, but that is not among the choices; it does not establish another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes a dual chitinase/transglycosylase and gives an endochitinase reaction (C4–C6). Its endochitinase GO annotation is a descendant of the option's broader O-glycosyl hydrolase term (GO1–GO3). The enzymatic evidence is partly transferred by similarity, so this supports the key without showing that every activity was directly assayed for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "GO1", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a secreted fungal cell-wall protein, which makes a membrane channel or ankyrin-binding protein less plausible. But that broad context does not establish hydrolysis rather than carbohydrate binding or another carbohydrate-related activity.",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental/homology evidence identifying chitinase activity is needed to distinguish C from the plausible carbohydrate-related alternative A.",
    "reason": "The supplied sequence and choices do not provide a sufficiently specific, independently interpretable motif or context that establishes the exact molecular activity. Recognizing the protein or relying on an external annotation would supply the needed fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported as a broad GO parent term for endochitinase activity. The evidence also describes transglycosylase activity, but that is not among the choices; it does not establish another listed option."
  },
  "important_caveats": [
    "The sequence match and accession were established using reviewer-only sources and were not supplied to the evaluated model.",
    "The UniProt record's catalytic activity annotation is transferred by similarity; the exact experimental basis and source snapshot used by the question author are not established."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384JN58) annotates this protein as Crh-like protein 4 with chitinase activity (EC 3.2.1.14) and GO:0008843 (endochitinase activity). The GO ontology hierarchy places endochitinase activity (GO:0008843) under chitinase activity (GO:0004568), which is is_a hydrolase activity, hydrolyzing O-glycosyl compounds (GO:0004553). Chitin's β(1→4) glycosidic bonds are O-glycosidic (C1-O-C4 linkage), so the parent term correctly encompasses chitinase catalysis. The annotation evidence is primarily 'by similarity' (ECO:0000250 from Q8J0P4) for the EC assignment, with experimental support (PubMed:33846308) for the dual chitinase/transglycosylase function. The expected answer C is the correct parent GO term for the annotated molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a cleavable signal peptide (MFPKIFLTAATALLSAKS...) indicating a secreted protein, followed by multiple folded domains with conserved motifs (e.g., TFTTG, GKVTDYNRGAF, DVTSG patterns) characteristic of glycosyl hydrolase family 18 (GH18) chitinase-like domains. There are no transmembrane helices or channel-forming architecture (eliminating B: mechanosensitive cation channel). There are no tandem ~33-residue helix-loop-helix ankyrin repeats (eliminating D: ankyrin repeat binding). The presence of catalytic-looking motifs within structured domains, rather than isolated binding surfaces, supports an enzymatic hydrolase function (C) over a pure binding function (A). The overall domain architecture—signal peptide plus multiple GH18-like domains—is a hallmark of fungal secreted chitinases/transglycosylases.


**Missing item-specific fact**

> Precise identification of the GH18 catalytic motif (DXXDXDXE) is somewhat degenerate in Crh proteins, so exact family assignment from sequence alone requires familiarity with divergent GH18 members. However, the general reasoning (secreted enzyme with carbohydrate-active domains, not a channel, not an ankyrin binder) is sufficient to select C among the four options.


**Reason**

> The four choices span radically different molecular function classes (binding, channel, hydrolase, protein-domain binding). Sequence features—signal peptide, absence of transmembrane segments, absence of ankyrin repeats, presence of multi-domain catalytic architecture—provide concrete grounds to eliminate B and D and to favor a catalytic (hydrolase) over a pure-binding function. Recognizing the specific glycosyl hydrolase motifs strengthens the case for C but is not strictly necessary to exclude the other options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are clearly incompatible with the sequence (no channel architecture, no ankyrin repeats). Option A (carbohydrate derivative binding) describes a binding function, but the protein's primary annotated role is catalytic (chitinase/transglycosylase), making C the more specific and accurate choice. While the protein also has transglycosylase activity (EC 2.4.-.-), that option is not presented. Among the four given choices, C is uniquely defensible.


### Important caveats

- The chitinase EC assignment (3.2.1.14) is annotated 'by similarity' (ECO:0000250, transferred from Q8J0P4), not by direct experimental assay on this specific protein. The experimental evidence (PubMed:33846308) supports the dual chitinase/transglycosylase role but the specific EC number is inferred.
- The protein also possesses transglycosylase activity (EC 2.4.-.-), which is not captured by any of the four options. The question asks for the 'primary' molecular function, and the chitinase (hydrolase) activity is the dominant annotated catalytic function.
- The GO annotation for endochitinase activity uses ISS (inferred by sequence similarity) evidence, not ID (inferred by direct assay) for this specific protein.
- The sequence is 376 amino acids and matches the UniProt entry exactly (SHA-256 confirmed), so the annotation applies directly to the queried sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a cleavable signal peptide (MFPKIFLTAATALLSAKS...) indicating a secreted protein, followed by multiple folded domains with conserved motifs (e.g., TFTTG, GKVTDYNRGAF, DVTSG patterns) characteristic of glycosyl hydrolase family 18 (GH18) chitinase-like domains. There are no transmembrane helices or channel-forming architecture (eliminating B: mechanosensitive cation channel). There are no tandem ~33-residue helix-loop-helix ankyrin repeats (eliminating D: ankyrin repeat binding). The presence of catalytic-looking motifs within structured domains, rather than isolated binding surfaces, supports an enzymatic hydrolase function (C) over a pure binding function (A). The overall domain architecture—signal peptide plus multiple GH18-like domains—is a hallmark of fungal secreted chitinases/transglycosylases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the GH18 catalytic motif (DXXDXDXE) is somewhat degenerate in Crh proteins, so exact family assignment from sequence alone requires familiarity with divergent GH18 members. However, the general reasoning (secreted enzyme with carbohydrate-active domains, not a channel, not an ankyrin binder) is sufficient to select C among the four options.",
    "reason": "The four choices span radically different molecular function classes (binding, channel, hydrolase, protein-domain binding). Sequence features—signal peptide, absence of transmembrane segments, absence of ankyrin repeats, presence of multi-domain catalytic architecture—provide concrete grounds to eliminate B and D and to favor a catalytic (hydrolase) over a pure-binding function. Recognizing the specific glycosyl hydrolase motifs strengthens the case for C but is not strictly necessary to exclude the other options."
  },
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384JN58) annotates this protein as Crh-like protein 4 with chitinase activity (EC 3.2.1.14) and GO:0008843 (endochitinase activity). The GO ontology hierarchy places endochitinase activity (GO:0008843) under chitinase activity (GO:0004568), which is is_a hydrolase activity, hydrolyzing O-glycosyl compounds (GO:0004553). Chitin's β(1→4) glycosidic bonds are O-glycosidic (C1-O-C4 linkage), so the parent term correctly encompasses chitinase catalysis. The annotation evidence is primarily 'by similarity' (ECO:0000250 from Q8J0P4) for the EC assignment, with experimental support (PubMed:33846308) for the dual chitinase/transglycosylase function. The expected answer C is the correct parent GO term for the annotated molecular function."
  },
  "important_caveats": [
    "The chitinase EC assignment (3.2.1.14) is annotated 'by similarity' (ECO:0000250, transferred from Q8J0P4), not by direct experimental assay on this specific protein. The experimental evidence (PubMed:33846308) supports the dual chitinase/transglycosylase role but the specific EC number is inferred.",
    "The protein also possesses transglycosylase activity (EC 2.4.-.-), which is not captured by any of the four options. The question asks for the 'primary' molecular function, and the chitinase (hydrolase) activity is the dominant annotated catalytic function.",
    "The GO annotation for endochitinase activity uses ISS (inferred by sequence similarity) evidence, not ID (inferred by direct assay) for this specific protein.",
    "The sequence is 376 amino acids and matches the UniProt entry exactly (SHA-256 confirmed), so the annotation applies directly to the queried sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the sequence (no channel architecture, no ankyrin repeats). Option A (carbohydrate derivative binding) describes a binding function, but the protein's primary annotated role is catalytic (chitinase/transglycosylase), making C the more specific and accurate choice. While the protein also has transglycosylase activity (EC 2.4.-.-), that option is not presented. Among the four given choices, C is uniquely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384JN58) annotates this protein as Crh-like protein 4 with chitinase activity (EC 3.2.1.14) and GO:0008843 (endochitinase activity). The GO ontology hierarchy places endochitinase activity (GO:0008843) under chitinase activity (GO:0004568), which is is_a hydrolase activity, hydrolyzing O-glycosyl compounds (GO:0004553). Chitin's β(1→4) glycosidic bonds are O-glycosidic (C1-O-C4 linkage), so the parent term correctly encompasses chitinase catalysis. The annotation evidence is primarily 'by similarity' (ECO:0000250 from Q8J0P4) for the EC assignment, with experimental support (PubMed:33846308) for the dual chitinase/transglycosylase function. The expected answer C is the correct parent GO term for the annotated molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "GO2", "GO3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a cleavable signal peptide (MFPKIFLTAATALLSAKS...) indicating a secreted protein, followed by multiple folded domains with conserved motifs (e.g., TFTTG, GKVTDYNRGAF, DVTSG patterns) characteristic of glycosyl hydrolase family 18 (GH18) chitinase-like domains. There are no transmembrane helices or channel-forming architecture (eliminating B: mechanosensitive cation channel). There are no tandem ~33-residue helix-loop-helix ankyrin repeats (eliminating D: ankyrin repeat binding). The presence of catalytic-looking motifs within structured domains, rather than isolated binding surfaces, supports an enzymatic hydrolase function (C) over a pure binding function (A). The overall domain architecture—signal peptide plus multiple GH18-like domains—is a hallmark of fungal secreted chitinases/transglycosylases.",
    "missing_item_specific_fact": "Precise identification of the GH18 catalytic motif (DXXDXDXE) is somewhat degenerate in Crh proteins, so exact family assignment from sequence alone requires familiarity with divergent GH18 members. However, the general reasoning (secreted enzyme with carbohydrate-active domains, not a channel, not an ankyrin binder) is sufficient to select C among the four options.",
    "reason": "The four choices span radically different molecular function classes (binding, channel, hydrolase, protein-domain binding). Sequence features—signal peptide, absence of transmembrane segments, absence of ankyrin repeats, presence of multi-domain catalytic architecture—provide concrete grounds to eliminate B and D and to favor a catalytic (hydrolase) over a pure-binding function. Recognizing the specific glycosyl hydrolase motifs strengthens the case for C but is not strictly necessary to exclude the other options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are clearly incompatible with the sequence (no channel architecture, no ankyrin repeats). Option A (carbohydrate derivative binding) describes a binding function, but the protein's primary annotated role is catalytic (chitinase/transglycosylase), making C the more specific and accurate choice. While the protein also has transglycosylase activity (EC 2.4.-.-), that option is not presented. Among the four given choices, C is uniquely defensible."
  },
  "important_caveats": [
    "The chitinase EC assignment (3.2.1.14) is annotated 'by similarity' (ECO:0000250, transferred from Q8J0P4), not by direct experimental assay on this specific protein. The experimental evidence (PubMed:33846308) supports the dual chitinase/transglycosylase role but the specific EC number is inferred.",
    "The protein also possesses transglycosylase activity (EC 2.4.-.-), which is not captured by any of the four options. The question asks for the 'primary' molecular function, and the chitinase (hydrolase) activity is the dominant annotated catalytic function.",
    "The GO annotation for endochitinase activity uses ISS (inferred by sequence similarity) evidence, not ID (inferred by direct assay) for this specific protein.",
    "The sequence is 376 amino acids and matches the UniProt entry exactly (SHA-256 confirmed), so the annotation applies directly to the queried sequence."
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

**Accession:** `A0A384JN58` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
"A0A384JN58"
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitinase crh4"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitin transglycosylase crh4"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33846308","source":"PubMed"}],"value":"Crh-like protein 4"}}}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"value":"Dual chitinase/transglycosylase that plays a role in cell wall architecture (PubMed:33846308). Chitinase and transglycosylase activities are coupled (By similarity). Required for the polysaccharide cross-linking at the septa and the cell wall (By similarity). More specifically, transfers chitin to 1,6-beta-glucan in the cell wall (By similarity)"}]}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"database":"GO","id":"GO:0008843","properties":[{"key":"GoTerm","value":"F:endochitinase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)  
**Locator:** `lines 71-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:25:00.993379+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};
```

Source SHA-256: `4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:25:00.993379+00:00.  

```text
DR   GO; GO:0008843; F:endochitinase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44250-44263`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004553
name: hydrolase activity, hydrolyzing O-glycosyl compounds
namespace: molecular_function
alt_id: GO:0016800
def: "Catalysis of the hydrolysis of any O-glycosyl bond." [GOC:mah]
synonym: "O-glucosyl hydrolase activity" EXACT []
xref: EC:3.2.1.-
xref: Reactome:R-HSA-5694563 "ABHD10 hydrolyses MPAG"
xref: Reactome:R-HSA-6786652 "CHIT1 hydrolyses CHIT to 3xADGP"
xref: Reactome:R-HSA-9661820 "Bacterial GUSB hydrolyses BDG to BIL"
is_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds
property_value: skos:exactMatch EC:3.2.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44534-44541`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004568
name: chitinase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins." [GOC:bf, GOC:kah, GOC:pde, PMID:11468293]
xref: Reactome:R-HSA-6786421 "CHIA hydrolyses chitin"
is_a: GO:0004553 ! hydrolase activity, hydrolyzing O-glycosyl compounds

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 88913-88926`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008843
name: endochitinase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of nonterminal (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins. Typically, endochitinases cleave randomly within the chitin chain." [EC:3.2.1.14, GOC:bf, GOC:kah, GOC:pde, PMID:11468293]
synonym: "1,4-beta-poly-N-acetylglucosaminidase" EXACT [EC:3.2.1.14]
synonym: "chitinase" EXACT [EC:3.2.1.14]
synonym: "chitodextrinase" EXACT [EC:3.2.1.14]
synonym: "poly-beta-glucosaminidase" EXACT [EC:3.2.1.14]
xref: EC:3.2.1.14
xref: MetaCyc:3.2.1.14-RXN
is_a: GO:0004568 ! chitinase activity
property_value: skos:exactMatch EC:3.2.1.14

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
