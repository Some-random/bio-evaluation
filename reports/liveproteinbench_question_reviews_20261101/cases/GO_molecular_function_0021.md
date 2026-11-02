# GO_molecular_function_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — riboflavin reductase (NADPH) activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKADVFDPRALREAFGAFPTAVTVITASDPAGRPVGFTANSFTSVSLDPPLLLVCVAKTARDYSTMTAAEHFAINILSEAQKDVSIKFARPLEDRFAAVDWARAPNGCPIFAQVAAWFECSMHDVIEAGDHVMMVGRVTAFKSSGLNGLGYARGGYFAPSVAAKANSSAAGGEIGAVAVLERHAALFPLGDQNLSLPRYSAAGGDPAKTLASQLERSGLSVHDWLSLLDL

[Multiple Choices]
A. riboflavin reductase (NADPH) activity
B. fucokinase activity
C. class I DNA-(apurinic or apyrimidinic site) endonuclease activity
D. histone H3K18 acetyltransferase activity
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

> The exact sequence matches a historical UniProt record that assigns option A, but the GO assignment is computational (IEA:TreeGrafter), not direct experimental validation. The record describes Stc3 as a stachydrine-catabolism reductase subunit and says NAD(P)H electron transfer is probable, which does not independently establish riboflavin reductase catalysis.

Citations as saved: [H6](#evidence-h6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble enzyme, but the supplied sequence and choices do not provide a distinctive basis for inferring this specific riboflavin-reductase activity over other functions.


**Missing item-specific fact**

> The protein-specific GO assignment or functional characterization linking this exact sequence to riboflavin reductase activity.


**Reason**

> Selecting A depends on an item-specific annotation or remembered protein identity; the sequence alone does not establish the precise molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched record assigns A, and the alternatives describe distinct activities with no evidence here supporting them. However, the support for A is computational rather than direct experimental confirmation.


### Important caveats

- The historical and current records match the supplied sequence.
- The record's Stc3 function is associated with stachydrine catabolism; its proposed NAD(P)H electron-transfer role is qualified as probable.
- The GO term assignment should not be treated as experimental proof of the specific activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but the supplied sequence and choices do not provide a distinctive basis for inferring this specific riboflavin-reductase activity over other functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO assignment or functional characterization linking this exact sequence to riboflavin reductase activity.",
    "reason": "Selecting A depends on an item-specific annotation or remembered protein identity; the sequence alone does not establish the precise molecular function."
  },
  "case_id": "GO_molecular_function_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a historical UniProt record that assigns option A, but the GO assignment is computational (IEA:TreeGrafter), not direct experimental validation. The record describes Stc3 as a stachydrine-catabolism reductase subunit and says NAD(P)H electron transfer is probable, which does not independently establish riboflavin reductase catalysis."
  },
  "important_caveats": [
    "The historical and current records match the supplied sequence.",
    "The record's Stc3 function is associated with stachydrine catabolism; its proposed NAD(P)H electron-transfer role is qualified as probable.",
    "The GO term assignment should not be treated as experimental proof of the specific activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched record assigns A, and the alternatives describe distinct activities with no evidence here supporting them. However, the support for A is computational rather than direct experimental confirmation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a historical UniProt record that assigns option A, but the GO assignment is computational (IEA:TreeGrafter), not direct experimental validation. The record describes Stc3 as a stachydrine-catabolism reductase subunit and says NAD(P)H electron transfer is probable, which does not independently establish riboflavin reductase catalysis.",
    "evidence_ids": ["H6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but the supplied sequence and choices do not provide a distinctive basis for inferring this specific riboflavin-reductase activity over other functions.",
    "missing_item_specific_fact": "The protein-specific GO assignment or functional characterization linking this exact sequence to riboflavin reductase activity.",
    "reason": "Selecting A depends on an item-specific annotation or remembered protein identity; the sequence alone does not establish the precise molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched record assigns A, and the alternatives describe distinct activities with no evidence here supporting them. However, the support for A is computational rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The historical and current records match the supplied sequence.",
    "The record's Stc3 function is associated with stachydrine catabolism; its proposed NAD(P)H electron-transfer role is qualified as probable.",
    "The GO term assignment should not be treated as experimental proof of the specific activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO annotation GO:0042602 (riboflavin reductase (NADPH) activity) is present on UniProt entry Q92ZP7 (evidence_id C7/H6), matching the benchmark sequence exactly. However, the evidence code is IEA:TreeGrafter (computational inference), not experimental. The experimentally supported function (ECO:0000269, PubMed:10689197 and 22224443) describes this protein as a reductase transferring electrons from NAD(P)H to a Rieske-type oxygenase (Stc2) in stachydrine catabolism, with EC 1.5.1.- (generic). The riboflavin reductase annotation is a reasonable computational inference given FMN binding (GO:0010181, IEA:InterPro) and NAD(P)H electron-transfer role, but it is not directly experimentally demonstrated for this specific protein.

Citations as saved: [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Weak reasoning exists: the 230-AA bacterial protein size is inconsistent with histone acetyltransferase (D, eukaryotic GNAT-domain enzyme) and somewhat atypical for fucokinase (B, usually ~300+ AA with P-loop motifs). Small size and bacterial origin are loosely consistent with flavin reductases (A). However, distinguishing A from B or C with confidence requires recognizing specific FMN-binding motifs (e.g., the GxGxxG-like flavin-binding loops) versus kinase or AP-endonuclease motifs, which is not clearly extractable from the provided sequence by general reasoning alone.


**Missing item-specific fact**

> The experimentally determined function of this protein is stachydrine N-demethylase electron-transfer subunit (EC 1.5.1.-), not specifically riboflavin reductase (EC 1.5.1.30). The riboflavin reductase annotation is an IEA:TreeGrafter computational prediction. Identifying the correct option depends on knowing this specific annotation rather than deriving it from sequence motifs.


**Reason**

> The expected answer corresponds to a computational GO annotation (IEA:TreeGrafter) that approximates but does not precisely match the experimentally verified function. From the 230-aa sequence alone, general biological reasoning can eliminate D (eukaryotic histone modifier) with high confidence and perhaps C, but the A-vs-B distinction relies on recognizing specific flavin-reductase sequence signatures or recalling this protein's database annotation. The true experimental function (stachydrine demethylase electron transfer) matches none of the four options exactly, further indicating the answer depends on a specific annotation rather than derivable reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the experimental function (stachydrine demethylase electron transfer, EC 1.5.1.-) does not perfectly match any option, the four choices are sufficiently distinct (flavin reductase, kinase, DNA repair lyase, histone acetyltransferase) that only A is in the correct enzyme superfamily (oxidoreductase acting on CH-NH group, EC 1.5.x). The other three belong to entirely different EC classes (2.7.x, 4.2.x, and transferase). Thus A is the only defensible choice among the four, even if the precise GO term is a computational approximation.


### Important caveats

- The GO:0042602 annotation carries evidence code IEA:TreeGrafter (computational), not experimental evidence. The experimentally supported function is stachydrine demethylase electron transfer, not riboflavin reductase per se.
- The EC number is 1.5.1.- (generic), not 1.5.1.30 (riboflavin reductase), indicating the specific substrate is not experimentally confirmed as riboflavin/FMN in isolation.
- The protein's true role is as an electron-transfer subunit within a multi-enzyme Rieske-type oxygenase complex, which is broader than the riboflavin reductase term implies.
- The GO term GO:0042602 includes synonyms such as 'NADPH-FMN reductase activity' and 'NADPH-specific FMN reductase activity' that are closer to the protein's actual electron-transfer function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Weak reasoning exists: the 230-AA bacterial protein size is inconsistent with histone acetyltransferase (D, eukaryotic GNAT-domain enzyme) and somewhat atypical for fucokinase (B, usually ~300+ AA with P-loop motifs). Small size and bacterial origin are loosely consistent with flavin reductases (A). However, distinguishing A from B or C with confidence requires recognizing specific FMN-binding motifs (e.g., the GxGxxG-like flavin-binding loops) versus kinase or AP-endonuclease motifs, which is not clearly extractable from the provided sequence by general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined function of this protein is stachydrine N-demethylase electron-transfer subunit (EC 1.5.1.-), not specifically riboflavin reductase (EC 1.5.1.30). The riboflavin reductase annotation is an IEA:TreeGrafter computational prediction. Identifying the correct option depends on knowing this specific annotation rather than deriving it from sequence motifs.",
    "reason": "The expected answer corresponds to a computational GO annotation (IEA:TreeGrafter) that approximates but does not precisely match the experimentally verified function. From the 230-aa sequence alone, general biological reasoning can eliminate D (eukaryotic histone modifier) with high confidence and perhaps C, but the A-vs-B distinction relies on recognizing specific flavin-reductase sequence signatures or recalling this protein's database annotation. The true experimental function (stachydrine demethylase electron transfer) matches none of the four options exactly, further indicating the answer depends on a specific annotation rather than derivable reasoning."
  },
  "case_id": "GO_molecular_function_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H6",
      "C5",
      "H4",
      "C4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The GO annotation GO:0042602 (riboflavin reductase (NADPH) activity) is present on UniProt entry Q92ZP7 (evidence_id C7/H6), matching the benchmark sequence exactly. However, the evidence code is IEA:TreeGrafter (computational inference), not experimental. The experimentally supported function (ECO:0000269, PubMed:10689197 and 22224443) describes this protein as a reductase transferring electrons from NAD(P)H to a Rieske-type oxygenase (Stc2) in stachydrine catabolism, with EC 1.5.1.- (generic). The riboflavin reductase annotation is a reasonable computational inference given FMN binding (GO:0010181, IEA:InterPro) and NAD(P)H electron-transfer role, but it is not directly experimentally demonstrated for this specific protein."
  },
  "important_caveats": [
    "The GO:0042602 annotation carries evidence code IEA:TreeGrafter (computational), not experimental evidence. The experimentally supported function is stachydrine demethylase electron transfer, not riboflavin reductase per se.",
    "The EC number is 1.5.1.- (generic), not 1.5.1.30 (riboflavin reductase), indicating the specific substrate is not experimentally confirmed as riboflavin/FMN in isolation.",
    "The protein's true role is as an electron-transfer subunit within a multi-enzyme Rieske-type oxygenase complex, which is broader than the riboflavin reductase term implies.",
    "The GO term GO:0042602 includes synonyms such as 'NADPH-FMN reductase activity' and 'NADPH-specific FMN reductase activity' that are closer to the protein's actual electron-transfer function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the experimental function (stachydrine demethylase electron transfer, EC 1.5.1.-) does not perfectly match any option, the four choices are sufficiently distinct (flavin reductase, kinase, DNA repair lyase, histone acetyltransferase) that only A is in the correct enzyme superfamily (oxidoreductase acting on CH-NH group, EC 1.5.x). The other three belong to entirely different EC classes (2.7.x, 4.2.x, and transferase). Thus A is the only defensible choice among the four, even if the precise GO term is a computational approximation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO annotation GO:0042602 (riboflavin reductase (NADPH) activity) is present on UniProt entry Q92ZP7 (evidence_id C7/H6), matching the benchmark sequence exactly. However, the evidence code is IEA:TreeGrafter (computational inference), not experimental. The experimentally supported function (ECO:0000269, PubMed:10689197 and 22224443) describes this protein as a reductase transferring electrons from NAD(P)H to a Rieske-type oxygenase (Stc2) in stachydrine catabolism, with EC 1.5.1.- (generic). The riboflavin reductase annotation is a reasonable computational inference given FMN binding (GO:0010181, IEA:InterPro) and NAD(P)H electron-transfer role, but it is not directly experimentally demonstrated for this specific protein.",
    "evidence_ids": ["C7", "H6", "C5", "H4", "C4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Weak reasoning exists: the 230-AA bacterial protein size is inconsistent with histone acetyltransferase (D, eukaryotic GNAT-domain enzyme) and somewhat atypical for fucokinase (B, usually ~300+ AA with P-loop motifs). Small size and bacterial origin are loosely consistent with flavin reductases (A). However, distinguishing A from B or C with confidence requires recognizing specific FMN-binding motifs (e.g., the GxGxxG-like flavin-binding loops) versus kinase or AP-endonuclease motifs, which is not clearly extractable from the provided sequence by general reasoning alone.",
    "missing_item_specific_fact": "The experimentally determined function of this protein is stachydrine N-demethylase electron-transfer subunit (EC 1.5.1.-), not specifically riboflavin reductase (EC 1.5.1.30). The riboflavin reductase annotation is an IEA:TreeGrafter computational prediction. Identifying the correct option depends on knowing this specific annotation rather than deriving it from sequence motifs.",
    "reason": "The expected answer corresponds to a computational GO annotation (IEA:TreeGrafter) that approximates but does not precisely match the experimentally verified function. From the 230-aa sequence alone, general biological reasoning can eliminate D (eukaryotic histone modifier) with high confidence and perhaps C, but the A-vs-B distinction relies on recognizing specific flavin-reductase sequence signatures or recalling this protein's database annotation. The true experimental function (stachydrine demethylase electron transfer) matches none of the four options exactly, further indicating the answer depends on a specific annotation rather than derivable reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the experimental function (stachydrine demethylase electron transfer, EC 1.5.1.-) does not perfectly match any option, the four choices are sufficiently distinct (flavin reductase, kinase, DNA repair lyase, histone acetyltransferase) that only A is in the correct enzyme superfamily (oxidoreductase acting on CH-NH group, EC 1.5.x). The other three belong to entirely different EC classes (2.7.x, 4.2.x, and transferase). Thus A is the only defensible choice among the four, even if the precise GO term is a computational approximation."
  },
  "important_caveats": [
    "The GO:0042602 annotation carries evidence code IEA:TreeGrafter (computational), not experimental evidence. The experimentally supported function is stachydrine demethylase electron transfer, not riboflavin reductase per se.",
    "The EC number is 1.5.1.- (generic), not 1.5.1.30 (riboflavin reductase), indicating the specific substrate is not experimentally confirmed as riboflavin/FMN in isolation.",
    "The protein's true role is as an electron-transfer subunit within a multi-enzyme Rieske-type oxygenase complex, which is broader than the riboflavin reductase term implies.",
    "The GO term GO:0042602 includes synonyms such as 'NADPH-FMN reductase activity' and 'NADPH-specific FMN reductase activity' that are closer to the protein's actual electron-transfer function."
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

**Accession:** `Q92ZP7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:32.319062+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"10689197","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"22224443","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Stachydrine N-demethylase reductase subunit Stc3"}}}
```

Source SHA-256: `4ec6a47ccea73964177beeee14c9f04560387c431404c54ea6f974146c062395`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:32.319062+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10689197","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"10689197","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"22224443","source":"PubMed"}],"value":"Reductase involved in the catabolism of stachydrine (L-proline betaine), a source of carbon and nitrogen (PubMed:10689197). Part of a Rieske-type oxygenase system that catalyzes the demethylation of stachydrine to produce N-methyl-L-proline (monomethylproline) (PubMed:22224443). This subunit is probably involved in the transfer of electrons from NAD(P)H to the catalytic subunit Stc2 (Probable)"}]}
```

Source SHA-256: `4ec6a47ccea73964177beeee14c9f04560387c431404c54ea6f974146c062395`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP7.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:32.319062+00:00.  

```json
{"database":"GO","id":"GO:0042602","properties":[{"key":"GoTerm","value":"F:riboflavin reductase (NADPH) activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `4ec6a47ccea73964177beeee14c9f04560387c431404c54ea6f974146c062395`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP7?format=txt&versions=105)  
**Locator:** `lines 65-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:34.355639+00:00.  

```text
CC   -!- FUNCTION: Reductase involved in the catabolism of stachydrine (L-
CC       proline betaine), a source of carbon and nitrogen (PubMed:10689197).
CC       Part of a Rieske-type oxygenase system that catalyzes the demethylation
CC       of stachydrine to produce N-methyl-L-proline (monomethylproline)
CC       (PubMed:22224443). This subunit is probably involved in the transfer of
CC       electrons from NAD(P)H to the catalytic subunit Stc2 (Probable).
CC       {ECO:0000269|PubMed:10689197, ECO:0000269|PubMed:22224443,
CC       ECO:0000305|PubMed:10689197, ECO:0000305|PubMed:22224443}.
```

Source SHA-256: `a263da48ab6f77836342eb683b45ac54f75f86bcb5d144c7b1ba29c3e116fd50`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP7?format=txt&versions=105)  
**Locator:** `lines 95-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:34.355639+00:00.  

```text
DR   GO; GO:0042602; F:riboflavin reductase (NADPH) activity; IEA:TreeGrafter.
```

Source SHA-256: `a263da48ab6f77836342eb683b45ac54f75f86bcb5d144c7b1ba29c3e116fd50`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 239050-239075`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0042602
name: riboflavin reductase (NADPH) activity
namespace: molecular_function
def: "Catalysis of the reaction: reduced riboflavin + NADP+ = riboflavin + NADPH + 2 H+." [RHEA:19377]
synonym: "flavin reductase activity" RELATED [EC:1.5.1.30]
synonym: "FMN reductase (NADPH) activity" RELATED [EC:1.5.1.30]
synonym: "NADPH dehydrogenase (riboflavin) activity" RELATED [EC:1.5.1.30]
synonym: "NADPH-dependent FMN reductase activity" RELATED [EC:1.5.1.30]
synonym: "NADPH-FMN reductase activity" RELATED [EC:1.5.1.30]
synonym: "NADPH-riboflavin oxidoreductase activity" EXACT []
synonym: "NADPH-riboflavin reductase activity" RELATED [EC:1.5.1.30]
synonym: "NADPH-specific FMN reductase activity" RELATED [EC:1.5.1.30]
synonym: "NADPH:riboflavin oxidoreductase activity" RELATED [EC:1.5.1.30]
synonym: "reduced-riboflavin:NADP+ oxidoreductase activity" RELATED [EC:1.5.1.30]
synonym: "riboflavin mononucleotide (reduced nicotinamide adenine dinucleotide phosphate) reductase activity" RELATED [EC:1.5.1.30]
synonym: "riboflavin mononucleotide reductase activity" BROAD [EC:1.5.1.30]
synonym: "riboflavine mononucleotide reductase activity" BROAD [EC:1.5.1.30]
xref: EC:1.5.1.30
xref: KEGG_REACTION:R05707
xref: MetaCyc:NADPH-DEHYDROGENASE-FLAVIN-RXN
xref: RHEA:19377
is_a: GO:0052875 ! riboflavin reductase [NAD(P)H] activity
property_value: skos:exactMatch EC:1.5.1.30
property_value: skos:exactMatch RHEA:19377

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
