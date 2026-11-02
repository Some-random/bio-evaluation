# EC_number_0089

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.7.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. 2.7.7.1
B. 2.7.7.43
C. 2.7.1.52
D. 5.1.3.14
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the Drosophila NMNAT entry, whose annotation assigns EC 2.7.7.1 to NAD synthesis and cites experimental evidence. This supports choice A for the listed options.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing an enzyme-like protein, but the input gives no organism, protein name, substrate, or reaction context that establishes which specific nucleotide-transfer reaction it catalyzes.


**Missing item-specific fact**

> The protein-specific identification as Drosophila NMNAT and evidence that it catalyzes NAD synthesis from nicotinamide ribonucleotide and ATP.


**Reason**

> Distinguishing EC 2.7.7.1 from the alternatives requires identifying the protein's specific catalytic activity, a fact not directly supplied by the sequence prompt; recognizing the sequence from an external record would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the matched protein's experimentally supported NAD-synthesis activity corresponds to A. The database also lists EC 2.7.7.18, but that is not one of the choices and its cited evidence is computational.


### Important caveats

- The sequence match and annotation support are reviewer-only evidence and were not present in the evaluated input.
- The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing an enzyme-like protein, but the input gives no organism, protein name, substrate, or reaction context that establishes which specific nucleotide-transfer reaction it catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Drosophila NMNAT and evidence that it catalyzes NAD synthesis from nicotinamide ribonucleotide and ATP.",
    "reason": "Distinguishing EC 2.7.7.1 from the alternatives requires identifying the protein's specific catalytic activity, a fact not directly supplied by the sequence prompt; recognizing the sequence from an external record would be lookup or memorization."
  },
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Drosophila NMNAT entry, whose annotation assigns EC 2.7.7.1 to NAD synthesis and cites experimental evidence. This supports choice A for the listed options."
  },
  "important_caveats": [
    "The sequence match and annotation support are reviewer-only evidence and were not present in the evaluated input.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched protein's experimentally supported NAD-synthesis activity corresponds to A. The database also lists EC 2.7.7.18, but that is not one of the choices and its cited evidence is computational."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Drosophila NMNAT entry, whose annotation assigns EC 2.7.7.1 to NAD synthesis and cites experimental evidence. This supports choice A for the listed options.",
    "evidence_ids": ["C1", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing an enzyme-like protein, but the input gives no organism, protein name, substrate, or reaction context that establishes which specific nucleotide-transfer reaction it catalyzes.",
    "missing_item_specific_fact": "The protein-specific identification as Drosophila NMNAT and evidence that it catalyzes NAD synthesis from nicotinamide ribonucleotide and ATP.",
    "reason": "Distinguishing EC 2.7.7.1 from the alternatives requires identifying the protein's specific catalytic activity, a fact not directly supplied by the sequence prompt; recognizing the sequence from an external record would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched protein's experimentally supported NAD-synthesis activity corresponds to A. The database also lists EC 2.7.7.18, but that is not one of the choices and its cited evidence is computational."
  },
  "important_caveats": [
    "The sequence match and annotation support are reviewer-only evidence and were not present in the evaluated input.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VC03 (NMNA_DROME, Drosophila melanogaster NMNAT) with exact SHA-256 match. The EC 2.7.7.1 annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the catalytic reaction: beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+). The RuleBase computational annotation (ECO:0000255) also supports this. The EC 2.7.7.18 secondary annotation is computational-only (RuleBase) and is not among the choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Some partial reasoning is possible: the 'RAGSNPG' motif, Rossmann-like fold elements (e.g., 'GKKGLA', 'GADLLESFAVPGLWAEAD'), and the distinctive poly-glycine tract ('GGGGG') are characteristic of the NMNAT enzyme family. Eliminating 5.1.3.14 (isomerase) and 2.7.1.52 (kinase) is feasible from general sequence architecture. However, distinguishing 2.7.7.1 from 2.7.7.43—both nucleotidyltransferases within the same EC subclass—requires knowing the specific substrate (NMN vs. another nucleotide acceptor), which is not derivable from general enzymology principles.


**Missing item-specific fact**

> The precise substrate specificity that distinguishes EC 2.7.7.1 (NMN + ATP → NAD⁺ + PPi) from EC 2.7.7.43 (a different nucleotidyltransferase reaction) cannot be determined from the sequence alone without recognizing the NMNAT family or consulting a database/predictor. The 'RAGSNPG' motif is a family-specific pattern, not a general chemical principle.


**Reason**

> While coarse class elimination (isomerase, kinase) is reasoning-tractable, the critical distinction between the two nucleotidyltransferase options (A vs B) depends on recognizing the NMNAT fold and its specific substrate chemistry—a pattern-recognition task closer to database lookup than deductive reasoning from general biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (2.7.1.52, kinase) and D (5.1.3.14, isomerase) are clearly wrong enzyme classes. Option B (2.7.7.43) is a different nucleotidyltransferase reaction not matching the NMNAT fold. Only A (2.7.7.1) corresponds to the annotated and experimentally validated activity. No genuine ambiguity among choices.


### Important caveats

- The EC 2.7.7.18 secondary annotation (RuleBase-only, computational) is not among the choices, so it does not affect answer validity.
- The sequence is the Drosophila nuclear NMNAT isoform with a poly-glycine tract; alternative splicing variants exist but the supplied sequence matches the canonical Swiss-Prot entry.
- The identity of EC 2.7.7.43 was not independently verified from the evidence; it is treated as a distractor in a different nucleotidyltransferase subclass.
- All UniProt evidence is reviewer-only and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Some partial reasoning is possible: the 'RAGSNPG' motif, Rossmann-like fold elements (e.g., 'GKKGLA', 'GADLLESFAVPGLWAEAD'), and the distinctive poly-glycine tract ('GGGGG') are characteristic of the NMNAT enzyme family. Eliminating 5.1.3.14 (isomerase) and 2.7.1.52 (kinase) is feasible from general sequence architecture. However, distinguishing 2.7.7.1 from 2.7.7.43—both nucleotidyltransferases within the same EC subclass—requires knowing the specific substrate (NMN vs. another nucleotide acceptor), which is not derivable from general enzymology principles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise substrate specificity that distinguishes EC 2.7.7.1 (NMN + ATP → NAD⁺ + PPi) from EC 2.7.7.43 (a different nucleotidyltransferase reaction) cannot be determined from the sequence alone without recognizing the NMNAT family or consulting a database/predictor. The 'RAGSNPG' motif is a family-specific pattern, not a general chemical principle.",
    "reason": "While coarse class elimination (isomerase, kinase) is reasoning-tractable, the critical distinction between the two nucleotidyltransferase options (A vs B) depends on recognizing the NMNAT fold and its specific substrate chemistry—a pattern-recognition task closer to database lookup than deductive reasoning from general biology."
  },
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "C9",
      "H1",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VC03 (NMNA_DROME, Drosophila melanogaster NMNAT) with exact SHA-256 match. The EC 2.7.7.1 annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the catalytic reaction: beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+). The RuleBase computational annotation (ECO:0000255) also supports this. The EC 2.7.7.18 secondary annotation is computational-only (RuleBase) and is not among the choices."
  },
  "important_caveats": [
    "The EC 2.7.7.18 secondary annotation (RuleBase-only, computational) is not among the choices, so it does not affect answer validity.",
    "The sequence is the Drosophila nuclear NMNAT isoform with a poly-glycine tract; alternative splicing variants exist but the supplied sequence matches the canonical Swiss-Prot entry.",
    "The identity of EC 2.7.7.43 was not independently verified from the evidence; it is treated as a distractor in a different nucleotidyltransferase subclass.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.7.1.52, kinase) and D (5.1.3.14, isomerase) are clearly wrong enzyme classes. Option B (2.7.7.43) is a different nucleotidyltransferase reaction not matching the NMNAT fold. Only A (2.7.7.1) corresponds to the annotated and experimentally validated activity. No genuine ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VC03 (NMNA_DROME, Drosophila melanogaster NMNAT) with exact SHA-256 match. The EC 2.7.7.1 annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the catalytic reaction: beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+). The RuleBase computational annotation (ECO:0000255) also supports this. The EC 2.7.7.18 secondary annotation is computational-only (RuleBase) and is not among the choices.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "C9", "H1", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Some partial reasoning is possible: the 'RAGSNPG' motif, Rossmann-like fold elements (e.g., 'GKKGLA', 'GADLLESFAVPGLWAEAD'), and the distinctive poly-glycine tract ('GGGGG') are characteristic of the NMNAT enzyme family. Eliminating 5.1.3.14 (isomerase) and 2.7.1.52 (kinase) is feasible from general sequence architecture. However, distinguishing 2.7.7.1 from 2.7.7.43—both nucleotidyltransferases within the same EC subclass—requires knowing the specific substrate (NMN vs. another nucleotide acceptor), which is not derivable from general enzymology principles.",
    "missing_item_specific_fact": "The precise substrate specificity that distinguishes EC 2.7.7.1 (NMN + ATP → NAD⁺ + PPi) from EC 2.7.7.43 (a different nucleotidyltransferase reaction) cannot be determined from the sequence alone without recognizing the NMNAT family or consulting a database/predictor. The 'RAGSNPG' motif is a family-specific pattern, not a general chemical principle.",
    "reason": "While coarse class elimination (isomerase, kinase) is reasoning-tractable, the critical distinction between the two nucleotidyltransferase options (A vs B) depends on recognizing the NMNAT fold and its specific substrate chemistry—a pattern-recognition task closer to database lookup than deductive reasoning from general biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.7.1.52, kinase) and D (5.1.3.14, isomerase) are clearly wrong enzyme classes. Option B (2.7.7.43) is a different nucleotidyltransferase reaction not matching the NMNAT fold. Only A (2.7.7.1) corresponds to the annotated and experimentally validated activity. No genuine ambiguity among choices."
  },
  "important_caveats": [
    "The EC 2.7.7.18 secondary annotation (RuleBase-only, computational) is not among the choices, so it does not affect answer validity.",
    "The sequence is the Drosophila nuclear NMNAT isoform with a poly-glycine tract; alternative splicing variants exist but the supplied sequence matches the canonical Swiss-Prot entry.",
    "The identity of EC 2.7.7.43 was not independently verified from the evidence; it is treated as a distractor in a different nucleotidyltransferase subclass.",
    "All UniProt evidence is reviewer-only and was not available to the evaluated model."
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

**Accession:** `Q9VC03` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 187. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
"Q9VC03"
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039254","source":"FlyBase"}],"value":"Nicotinamide mononucleotide adenylyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039254","source":"FlyBase"}],"value":"dNmnat"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"17132048","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19403820","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26616331","source":"PubMed"}],"value":"2.7.7.1"},{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"}],"value":"2.7.7.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"}],"value":"Nicotinamide-nucleotide adenylyltransferase"}}}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"19403820","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26616331","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21361"}}],"reaction":{"ecNumber":"2.7.7.1","evidences":[{"evidenceCode":"ECO:0000255","id":"RU362021","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"17132048","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19403820","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26616331","source":"PubMed"}],"name":"beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21360"},{"database":"ChEBI","id":"CHEBI:14649"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57540"}]}}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Zhai R.G.","Cao Y.","Hiesinger P.R.","Zhou Y.","Mehta S.Q.","Schulze K.L.","Verstreken P.","Bellen H.J."],"citationCrossReferences":[{"database":"PubMed","id":"17132048"},{"database":"DOI","id":"10.1371/journal.pbio.0040416"}],"citationType":"journal article","firstPage":"e416","id":"17132048","journal":"PLoS Biol.","lastPage":"e416","publicationDate":"2006","title":"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.","volume":"4"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","TISSUE SPECIFICITY","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Sasaki Y.","Vohra B.P.","Lund F.E.","Milbrandt J."],"citationCrossReferences":[{"database":"PubMed","id":"19403820"},{"database":"DOI","id":"10.1523/jneurosci.5469-08.2009"}],"citationType":"journal article","firstPage":"5525","id":"19403820","journal":"J. Neurosci.","lastPage":"5535","publicationDate":"2009","title":"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.","volume":"29"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":7,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)  
**Locator:** `/references/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.289195+00:00.  

```json
{"citation":{"authors":["Ruan K.","Zhu Y.","Li C.","Brazill J.M.","Zhai R.G."],"citationCrossReferences":[{"database":"PubMed","id":"26616331"},{"database":"DOI","id":"10.1038/ncomms10057"}],"citationType":"journal article","firstPage":"10057","id":"26616331","journal":"Nat. Commun.","lastPage":"10057","publicationDate":"2015","title":"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":10,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","ALTERNATIVE SPLICING","INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS","NUCLEAR LOCALIZATION SIGNAL","MUTAGENESIS OF LYS-380"]}
```

Source SHA-256: `d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
ID   NMNA_DROME              Reviewed;         389 AA.
AC   Q9VC03; A0A0B4KHH7; Q7KS06; Q8T405;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 4.
DT   28-JAN-2026, entry version 187.
DE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};
DE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};
DE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};
DE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};
DE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};
GN   Name=Nmnat {ECO:0000303|PubMed:17132048, ECO:0000312|FlyBase:FBgn0039254};
GN   ORFNames=CG13645 {ECO:0000312|FlyBase:FBgn0039254};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
DE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};
DE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};
DE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};
DE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};
DE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 164-171`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate
CC         + NAD(+); Xref=Rhea:RHEA:21360, ChEBI:CHEBI:14649, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57540; EC=2.7.7.1;
CC         Evidence={ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048,
CC         ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21361;
CC         Evidence={ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
