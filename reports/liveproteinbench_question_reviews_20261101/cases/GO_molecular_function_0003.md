# GO_molecular_function_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — carboxylesterase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNKVKVGDAQVSYCIDGKGPGLVLVHGTGGDSETNWGHLMPALTNDWTVVRPDYSGSGITSDEGKQLEVKEIAAQVVAAAEAARVVPFDLVGFSLGSAVVIAIAADYPHLVRRIVLLGAFLSSRDIRQKTQFELWRDLIRTDRAALSRLILLTGFSPDFISKQGHDGVSVIINSFVSEINWEGMARQVELDLSIDVSEAARRIEKPTLVIGCSHDHIVPSSQAKSVVRIIRGAQYTELHTGHLAHIENPEEFILLLRSFLLSEDVP

[Multiple Choices]
A. carboxylesterase activity
B. double-stranded DNA endonuclease activity
C. structural constituent of nuclear pore
D. manganese ion transmembrane transporter activity
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

### Expected-answer support: contradicted

> The matched sequence is annotated with experimentally supported N-deacetylation of pyrrolizixenacetamide, an amide hydrolysis reaction. Carboxylesterase activity specifically concerns hydrolysis of carboxylic esters, so the reported reaction does not support choice A; the broad carboxylic ester hydrolase annotation is computationally inferred and does not establish this more specific activity.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a compact, enzyme-like protein without an obvious multi-pass membrane topology, which weighs against the manganese transporter option. That broad clue does not establish ester hydrolysis or reliably distinguish it from a soluble nuclease.


**Missing item-specific fact**

> The protein-specific substrate and reaction—experimentally reported as N-deacetylation of pyrrolizixenacetamide—are needed to identify its activity; this fact is not supplied by the sequence and choices alone.


**Reason**

> No sequence feature or biological context in the prompt decisively identifies carboxylesterase activity. Recognizing the exact protein or retrieving its annotation would be necessary to distinguish its particular chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reported amide deacetylation activity is not represented by the listed choices. Choice A is broadly related to hydrolysis but specifies ester hydrolysis; the other options are not supported by the supplied evidence.


### Important caveats

- The sequence matches the protein record, whose reaction and function annotations cite experimental evidence; the underlying primary paper was not independently reviewed here.
- The carboxylic ester hydrolase annotation is marked IEA and is broader than the specific carboxylesterase activity in choice A.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, enzyme-like protein without an obvious multi-pass membrane topology, which weighs against the manganese transporter option. That broad clue does not establish ester hydrolysis or reliably distinguish it from a soluble nuclease.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and reaction—experimentally reported as N-deacetylation of pyrrolizixenacetamide—are needed to identify its activity; this fact is not supplied by the sequence and choices alone.",
    "reason": "No sequence feature or biological context in the prompt decisively identifies carboxylesterase activity. Recognizing the exact protein or retrieving its annotation would be necessary to distinguish its particular chemistry."
  },
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "contradicted",
    "reason": "The matched sequence is annotated with experimentally supported N-deacetylation of pyrrolizixenacetamide, an amide hydrolysis reaction. Carboxylesterase activity specifically concerns hydrolysis of carboxylic esters, so the reported reaction does not support choice A; the broad carboxylic ester hydrolase annotation is computationally inferred and does not establish this more specific activity."
  },
  "important_caveats": [
    "The sequence matches the protein record, whose reaction and function annotations cite experimental evidence; the underlying primary paper was not independently reviewed here.",
    "The carboxylic ester hydrolase annotation is marked IEA and is broader than the specific carboxylesterase activity in choice A."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported amide deacetylation activity is not represented by the listed choices. Choice A is broadly related to hydrolysis but specifies ester hydrolysis; the other options are not supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched sequence is annotated with experimentally supported N-deacetylation of pyrrolizixenacetamide, an amide hydrolysis reaction. Carboxylesterase activity specifically concerns hydrolysis of carboxylic esters, so the reported reaction does not support choice A; the broad carboxylic ester hydrolase annotation is computationally inferred and does not establish this more specific activity.",
    "evidence_ids": ["H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a compact, enzyme-like protein without an obvious multi-pass membrane topology, which weighs against the manganese transporter option. That broad clue does not establish ester hydrolysis or reliably distinguish it from a soluble nuclease.",
    "missing_item_specific_fact": "The protein-specific substrate and reaction—experimentally reported as N-deacetylation of pyrrolizixenacetamide—are needed to identify its activity; this fact is not supplied by the sequence and choices alone.",
    "reason": "No sequence feature or biological context in the prompt decisively identifies carboxylesterase activity. Recognizing the exact protein or retrieving its annotation would be necessary to distinguish its particular chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported amide deacetylation activity is not represented by the listed choices. Choice A is broadly related to hydrolysis but specifies ester hydrolysis; the other options are not supported by the supplied evidence."
  },
  "important_caveats": [
    "The sequence matches the protein record, whose reaction and function annotations cite experimental evidence; the underlying primary paper was not independently reviewed here.",
    "The carboxylic ester hydrolase annotation is marked IEA and is broader than the specific carboxylesterase activity in choice A."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A2G0QDP0, XHPG_XENHO) carries GO:0052689 (carboxylic ester hydrolase activity) as a molecular function annotation (evidence: IEA:UniProtKB-KW). GO:0106435 (carboxylesterase activity, option A) is a direct child (is_a) of GO:0052689. The protein's recommended name is 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-), and its experimentally characterized reaction (ECO:0000269, PubMed:39428351, PDB 8QZU) is N-deacetylation producing acetate. While the actual bond hydrolyzed is an amide (C-N) rather than an ester (C-O), the UniProt keyword-based annotation places the protein in the carboxylic ester hydrolase family, and among the four choices A is the only hydrolase option and is the closest match to the annotated term. The annotation is computational (IEA) rather than a direct experimental GO assignment, and the specific child term GO:0106435 is not directly annotated, but the parent-level annotation supports selecting A over B, C, or D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent reasoning pathways converge on A: (1) The organism is Xenorhabdus hominickii, a bacterium with no nucleus or nuclear pore complex, definitively eliminating C (structural constituent of nuclear pore) by basic cell biology. (2) The 266-residue sequence lacks the multi-pass transmembrane topology (repeated ~20-residue hydrophobic stretches) expected for a Mn²⁺ transporter, making D highly unlikely. (3) The sequence contains GxSxG-like nucleophile motifs ('GTGGDS' near residues 17-22 and 'GCS' near residues 218-220) characteristic of the α/β-hydrolase fold, which is the structural scaffold for esterases/amidases. No DNA-binding motifs (helix-turn-helix, zinc finger, etc.) are present, making B unlikely. Among the four options, only A (carboxylesterase activity) is a hydrolase, consistent with the GxSxG motifs and small globular size.


**Missing item-specific fact**

> None critical. The GxSxG motif is shared by both esterases and amidases, so the reasoning supports 'hydrolase of the α/β-hydrolase superfamily' broadly. Distinguishing carboxylesterase (EC 3.1.1.1) from amidase (EC 3.5.1.-) specifically would require the exact substrate or active-site geometry. However, among the four provided choices, only A is a hydrolase, so the reasoning is sufficient to select A.


**Reason**

> The bacterial context provides a definitive elimination of C. The absence of transmembrane topology weakens D. The absence of DNA-binding features weakens B. The presence of GxSxG-like motifs and small globular size positively supports a hydrolase assignment, and A is the only hydrolase among the options. This constitutes a concrete, multi-step biological argument from the sequence and context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different functional categories (hydrolase, nuclease, structural protein, transporter). The bacterial origin eliminates C outright. The sequence lacks TM topology for D and DNA-binding features for B. The GxSxG motifs positively indicate a hydrolase, and A is the sole hydrolase option. No other option is defensible.


### Important caveats

- The actual catalytic activity is N-deacetylation (amide hydrolysis, EC 3.5.1.-), not ester hydrolysis (EC 3.1.1.1). The GO:0052689 annotation is assigned via IEA:UniProtKB-KW (keyword-based inference), not by direct experimental GO curation.
- GO:0106435 (carboxylesterase activity) is a child of the annotated GO:0052689 (carboxylic ester hydrolase activity); the child term is not directly annotated on this entry.
- The PDB structure 8QZU (1.18 Å, mutant Ala-94 with acetate) provides experimental evidence for the catalytic mechanism and active site (Ser-94 nucleophile, Asn-35), confirming hydrolase activity but specifically amide hydrolysis.
- The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, and the annotation may not have been available at benchmark creation time.
- The GxSxG motif supports the α/β-hydrolase fold broadly; it does not by itself distinguish carboxylesterase from amidase without additional active-site context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent reasoning pathways converge on A: (1) The organism is Xenorhabdus hominickii, a bacterium with no nucleus or nuclear pore complex, definitively eliminating C (structural constituent of nuclear pore) by basic cell biology. (2) The 266-residue sequence lacks the multi-pass transmembrane topology (repeated ~20-residue hydrophobic stretches) expected for a Mn²⁺ transporter, making D highly unlikely. (3) The sequence contains GxSxG-like nucleophile motifs ('GTGGDS' near residues 17-22 and 'GCS' near residues 218-220) characteristic of the α/β-hydrolase fold, which is the structural scaffold for esterases/amidases. No DNA-binding motifs (helix-turn-helix, zinc finger, etc.) are present, making B unlikely. Among the four options, only A (carboxylesterase activity) is a hydrolase, consistent with the GxSxG motifs and small globular size.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The GxSxG motif is shared by both esterases and amidases, so the reasoning supports 'hydrolase of the α/β-hydrolase superfamily' broadly. Distinguishing carboxylesterase (EC 3.1.1.1) from amidase (EC 3.5.1.-) specifically would require the exact substrate or active-site geometry. However, among the four provided choices, only A is a hydrolase, so the reasoning is sufficient to select A.",
    "reason": "The bacterial context provides a definitive elimination of C. The absence of transmembrane topology weakens D. The absence of DNA-binding features weakens B. The presence of GxSxG-like motifs and small globular size positively supports a hydrolase assignment, and A is the only hydrolase among the options. This constitutes a concrete, multi-step biological argument from the sequence and context."
  },
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2G0QDP0, XHPG_XENHO) carries GO:0052689 (carboxylic ester hydrolase activity) as a molecular function annotation (evidence: IEA:UniProtKB-KW). GO:0106435 (carboxylesterase activity, option A) is a direct child (is_a) of GO:0052689. The protein's recommended name is 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-), and its experimentally characterized reaction (ECO:0000269, PubMed:39428351, PDB 8QZU) is N-deacetylation producing acetate. While the actual bond hydrolyzed is an amide (C-N) rather than an ester (C-O), the UniProt keyword-based annotation places the protein in the carboxylic ester hydrolase family, and among the four choices A is the only hydrolase option and is the closest match to the annotated term. The annotation is computational (IEA) rather than a direct experimental GO assignment, and the specific child term GO:0106435 is not directly annotated, but the parent-level annotation supports selecting A over B, C, or D."
  },
  "important_caveats": [
    "The actual catalytic activity is N-deacetylation (amide hydrolysis, EC 3.5.1.-), not ester hydrolysis (EC 3.1.1.1). The GO:0052689 annotation is assigned via IEA:UniProtKB-KW (keyword-based inference), not by direct experimental GO curation.",
    "GO:0106435 (carboxylesterase activity) is a child of the annotated GO:0052689 (carboxylic ester hydrolase activity); the child term is not directly annotated on this entry.",
    "The PDB structure 8QZU (1.18 Å, mutant Ala-94 with acetate) provides experimental evidence for the catalytic mechanism and active site (Ser-94 nucleophile, Asn-35), confirming hydrolase activity but specifically amide hydrolysis.",
    "The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, and the annotation may not have been available at benchmark creation time.",
    "The GxSxG motif supports the α/β-hydrolase fold broadly; it does not by itself distinguish carboxylesterase from amidase without additional active-site context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different functional categories (hydrolase, nuclease, structural protein, transporter). The bacterial origin eliminates C outright. The sequence lacks TM topology for D and DNA-binding features for B. The GxSxG motifs positively indicate a hydrolase, and A is the sole hydrolase option. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2G0QDP0, XHPG_XENHO) carries GO:0052689 (carboxylic ester hydrolase activity) as a molecular function annotation (evidence: IEA:UniProtKB-KW). GO:0106435 (carboxylesterase activity, option A) is a direct child (is_a) of GO:0052689. The protein's recommended name is 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-), and its experimentally characterized reaction (ECO:0000269, PubMed:39428351, PDB 8QZU) is N-deacetylation producing acetate. While the actual bond hydrolyzed is an amide (C-N) rather than an ester (C-O), the UniProt keyword-based annotation places the protein in the carboxylic ester hydrolase family, and among the four choices A is the only hydrolase option and is the closest match to the annotated term. The annotation is computational (IEA) rather than a direct experimental GO assignment, and the specific child term GO:0106435 is not directly annotated, but the parent-level annotation supports selecting A over B, C, or D.",
    "evidence_ids": ["C4", "C5", "C6", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent reasoning pathways converge on A: (1) The organism is Xenorhabdus hominickii, a bacterium with no nucleus or nuclear pore complex, definitively eliminating C (structural constituent of nuclear pore) by basic cell biology. (2) The 266-residue sequence lacks the multi-pass transmembrane topology (repeated ~20-residue hydrophobic stretches) expected for a Mn²⁺ transporter, making D highly unlikely. (3) The sequence contains GxSxG-like nucleophile motifs ('GTGGDS' near residues 17-22 and 'GCS' near residues 218-220) characteristic of the α/β-hydrolase fold, which is the structural scaffold for esterases/amidases. No DNA-binding motifs (helix-turn-helix, zinc finger, etc.) are present, making B unlikely. Among the four options, only A (carboxylesterase activity) is a hydrolase, consistent with the GxSxG motifs and small globular size.",
    "missing_item_specific_fact": "None critical. The GxSxG motif is shared by both esterases and amidases, so the reasoning supports 'hydrolase of the α/β-hydrolase superfamily' broadly. Distinguishing carboxylesterase (EC 3.1.1.1) from amidase (EC 3.5.1.-) specifically would require the exact substrate or active-site geometry. However, among the four provided choices, only A is a hydrolase, so the reasoning is sufficient to select A.",
    "reason": "The bacterial context provides a definitive elimination of C. The absence of transmembrane topology weakens D. The absence of DNA-binding features weakens B. The presence of GxSxG-like motifs and small globular size positively supports a hydrolase assignment, and A is the only hydrolase among the options. This constitutes a concrete, multi-step biological argument from the sequence and context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different functional categories (hydrolase, nuclease, structural protein, transporter). The bacterial origin eliminates C outright. The sequence lacks TM topology for D and DNA-binding features for B. The GxSxG motifs positively indicate a hydrolase, and A is the sole hydrolase option. No other option is defensible."
  },
  "important_caveats": [
    "The actual catalytic activity is N-deacetylation (amide hydrolysis, EC 3.5.1.-), not ester hydrolysis (EC 3.1.1.1). The GO:0052689 annotation is assigned via IEA:UniProtKB-KW (keyword-based inference), not by direct experimental GO curation.",
    "GO:0106435 (carboxylesterase activity) is a child of the annotated GO:0052689 (carboxylic ester hydrolase activity); the child term is not directly annotated on this entry.",
    "The PDB structure 8QZU (1.18 Å, mutant Ala-94 with acetate) provides experimental evidence for the catalytic mechanism and active site (Ser-94 nucleophile, Asn-35), confirming hydrolase activity but specifically amide hydrolysis.",
    "The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, and the annotation may not have been available at benchmark creation time.",
    "The GxSxG motif supports the α/β-hydrolase fold broadly; it does not by itself distinguish carboxylesterase from amidase without additional active-site context."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> H3/H4 report N-deacetylation of an amide; GO3 defines carboxylesterase as carboxylic-ester hydrolysis. H5 carries the broader carboxylic ester hydrolase term computationally.

**Remaining uncertainty:** The reported reaction differs from the keyed definition, but the supplied evidence does not exhaustively test additional ester substrates.

Evidence checked: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A2G0QDP0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39428351","source":"PubMed"}],"value":"Pyrrolizixenamide hydrolase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"value":"3.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39428351","source":"PubMed"}],"value":"Pyrrolizixenacetamide deacetylase"}}}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"value":"Involved in the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid. Catalyzes the N-deacetylation of pyrrolizixenacetamide"}]}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.833416+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83308"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"name":"pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83307"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:232461"},{"database":"ChEBI","id":"CHEBI:232462"}]}}
```

Source SHA-256: `ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 36-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
CC   -!- FUNCTION: Involved in the biosynthetic pathway of pyrrolizwilline, a
CC       pyrrolizidine alkaloid. Catalyzes the N-deacetylation of
CC       pyrrolizixenacetamide. {ECO:0000269|PubMed:39428351}.
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-
CC         pyrrolizin-1-one + acetate + H(+); Xref=Rhea:RHEA:83307,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30089,
CC         ChEBI:CHEBI:232461, ChEBI:CHEBI:232462;
CC         Evidence={ECO:0000269|PubMed:39428351};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83308;
CC         Evidence={ECO:0000269|PubMed:39428351};
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959052+00:00.  

```text
DR   GO; GO:0052689; F:carboxylic ester hydrolase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 430643-430695`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0106435
name: carboxylesterase activity
namespace: molecular_function
def: "Catalysis of the reaction: a carboxylic ester + H2O = a carboxylate + an alcohol + H+." [RHEA:21164]
comment: Note: This covers a broad range of specificity; also hydrolyzes vitamin A esters.
synonym: "ali-esterase activity" RELATED [EC:3.1.1.1]
synonym: "alpha-carboxylesterase activity" NARROW []
synonym: "B-esterase activity" NARROW [EC:3.1.1.1]
synonym: "cocaine esterase" NARROW [EC:3.1.1.1]
synonym: "nonspecific carboxylesterase activity" RELATED []
synonym: "procaine esterase" NARROW [] {comment="EC:3.1.1.1"}
synonym: "serine esterase activity" NARROW []
synonym: "triacetin esterase" NARROW []
synonym: "vitamin A esterase" NARROW []
xref: EC:3.1.1.1
xref: MetaCyc:CARBOXYLESTERASE-RXN
xref: Reactome:R-HSA-9619024 "CES1 trimer hydrolyses ACEI pro-drugs to ACEIs"
xref: Reactome:R-HSA-9727567 "CES1 hydrolyses sacubitril to sacubitrilat"
xref: Reactome:R-HSA-9749647 "CES2 hydrolyzes ASA-"
xref: RHEA:21164
xref: RHEA:31779
xref: RHEA:38555
xref: RHEA:47348
xref: RHEA:47352
xref: RHEA:47356
xref: RHEA:47360
xref: RHEA:47364
xref: RHEA:47388
xref: RHEA:47392
xref: RHEA:50136
xref: RHEA:50144
xref: RHEA:50148
xref: RHEA:59388
xref: RHEA:63052
is_a: GO:0052689 ! carboxylic ester hydrolase activity
property_value: skos:exactMatch EC:3.1.1.1
property_value: skos:exactMatch RHEA:21164
property_value: skos:narrowMatch RHEA:31779
property_value: skos:narrowMatch RHEA:38555
property_value: skos:narrowMatch RHEA:47348
property_value: skos:narrowMatch RHEA:47352
property_value: skos:narrowMatch RHEA:47356
property_value: skos:narrowMatch RHEA:47360
property_value: skos:narrowMatch RHEA:47364
property_value: skos:narrowMatch RHEA:47388
property_value: skos:narrowMatch RHEA:47392
property_value: skos:narrowMatch RHEA:50136
property_value: skos:narrowMatch RHEA:50144
property_value: skos:narrowMatch RHEA:50148
property_value: skos:narrowMatch RHEA:59388
property_value: skos:narrowMatch RHEA:63052

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
