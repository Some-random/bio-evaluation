# catalytic_activity_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)
B. D-ribose 5-phosphate + uracil = psi-UMP + H2O
C. 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 389-aa UniProtKB Q9VC03 sequence. The matched entry annotates the reaction in D as the enzyme's catalytic activity, with cited PubMed evidence as well as a computational RuleBase assignment. This supports D for the choices given, though the exact author source snapshot is unknown.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme reactions, but the input gives no organism, protein name, domain annotation, or other context that identifies which reaction this particular sequence catalyzes. Sequence-based enzyme-family recognition would itself require protein-specific inference rather than a clear general biological deduction from the supplied context.


**Missing item-specific fact**

> The sequence's identity or functional annotation as a nicotinamide-nucleotide adenylyltransferase, or equivalent experimental knowledge of its catalytic activity.


**Reason**

> The keyed reaction is supported by reviewer-only annotation, but that annotation was not supplied to the evaluated model. Recognizing the sequence from memory or consulting a protein database would be lookup or memorization, not reasoning supported by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D matches the reaction annotated for this sequence. The matched entry also lists another catalytic activity, but that reaction is not one of the options.


### Important caveats

- The sequence match establishes applicability to the canonical entry sequence; it does not establish the author's exact source snapshot.
- The evidence includes both a computational RuleBase assignment and PubMed-linked evidence; the cited studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the input gives no organism, protein name, domain annotation, or other context that identifies which reaction this particular sequence catalyzes. Sequence-based enzyme-family recognition would itself require protein-specific inference rather than a clear general biological deduction from the supplied context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity or functional annotation as a nicotinamide-nucleotide adenylyltransferase, or equivalent experimental knowledge of its catalytic activity.",
    "reason": "The keyed reaction is supported by reviewer-only annotation, but that annotation was not supplied to the evaluated model. Recognizing the sequence from memory or consulting a protein database would be lookup or memorization, not reasoning supported by the question."
  },
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 389-aa UniProtKB Q9VC03 sequence. The matched entry annotates the reaction in D as the enzyme's catalytic activity, with cited PubMed evidence as well as a computational RuleBase assignment. This supports D for the choices given, though the exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The sequence match establishes applicability to the canonical entry sequence; it does not establish the author's exact source snapshot.",
    "The evidence includes both a computational RuleBase assignment and PubMed-linked evidence; the cited studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D matches the reaction annotated for this sequence. The matched entry also lists another catalytic activity, but that reaction is not one of the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 389-aa UniProtKB Q9VC03 sequence. The matched entry annotates the reaction in D as the enzyme's catalytic activity, with cited PubMed evidence as well as a computational RuleBase assignment. This supports D for the choices given, though the exact author source snapshot is unknown.",
    "evidence_ids": ["C1", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the input gives no organism, protein name, domain annotation, or other context that identifies which reaction this particular sequence catalyzes. Sequence-based enzyme-family recognition would itself require protein-specific inference rather than a clear general biological deduction from the supplied context.",
    "missing_item_specific_fact": "The sequence's identity or functional annotation as a nicotinamide-nucleotide adenylyltransferase, or equivalent experimental knowledge of its catalytic activity.",
    "reason": "The keyed reaction is supported by reviewer-only annotation, but that annotation was not supplied to the evaluated model. Recognizing the sequence from memory or consulting a protein database would be lookup or memorization, not reasoning supported by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D matches the reaction annotated for this sequence. The matched entry also lists another catalytic activity, but that reaction is not one of the options."
  },
  "important_caveats": [
    "The sequence match establishes applicability to the canonical entry sequence; it does not establish the author's exact source snapshot.",
    "The evidence includes both a computational RuleBase assignment and PubMed-linked evidence; the cited studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (389 aa, SHA256 match) corresponds to UniProt Q9VC03 (NMNA_DROME), Drosophila melanogaster Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1). The catalytic activity 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)' is annotated with experimental evidence codes ECO:0000269 from three independent PubMed studies (17132048, 19403820, 26616331) and confirmed by physiological direction (left-to-right, RHEA:21361). Choice D matches this reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clearly visible GGGGGDD motif (residues ~105-111), which is the canonical glycine-rich ATP-binding motif of the nucleotidyltransferase superfamily. Among the four choices, only D (NMN + ATP → NAD+ + PPi) is a nucleotidyltransferase reaction that uses ATP as a substrate. Choice A is an O-methyltransferase (uses SAM, not ATP), Choice B is a pyrimidine salvage phosphorylase (no ATP), and Choice C is a CoA-transferase/thiolase (no ATP). The GGGGGDD motif thus eliminates A, B, and C and points specifically to D.


**Missing item-specific fact**

> None critical. Recognition of the GGGGGDD motif as a nucleotidyltransferase ATP-binding signature is general biochemical knowledge about a large enzyme superfamily, not an item-specific annotation.


**Reason**

> A biologist familiar with the nucleotidyltransferase fold can identify the GGGGGDD motif in the sequence, infer ATP-dependent nucleotidyltransferase activity, and select D as the only ATP-consuming nucleotidyltransferase reaction among the choices. This is a concrete, general-knowledge-based argument rather than reliance on an exact database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein also has secondary EC 2.7.7.18 activity (nicotinate adenylyltransferase), but that reaction (nicotinate ribonucleotide + ATP → deamido-NAD+ + PPi) does not appear among the four choices. The primary EC 2.7.7.1 reaction is unambiguously represented by D, and the other three choices belong to entirely different enzyme classes.


### Important caveats

- The GGGGGDD motif is shared across the broad nucleotidyltransferase superfamily; identifying the specific sub-family (NMNAT vs. other nucleotidyltransferases) from sequence alone would require additional motifs or structural knowledge. However, the question only requires distinguishing among four very different reaction types, which the ATP-dependence criterion achieves.
- The EC 2.7.7.18 annotation is supported only by RuleBase (ECO:0000255, computational), not by direct experimental evidence, whereas EC 2.7.7.1 has three independent experimental confirmations.
- All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clearly visible GGGGGDD motif (residues ~105-111), which is the canonical glycine-rich ATP-binding motif of the nucleotidyltransferase superfamily. Among the four choices, only D (NMN + ATP → NAD+ + PPi) is a nucleotidyltransferase reaction that uses ATP as a substrate. Choice A is an O-methyltransferase (uses SAM, not ATP), Choice B is a pyrimidine salvage phosphorylase (no ATP), and Choice C is a CoA-transferase/thiolase (no ATP). The GGGGGDD motif thus eliminates A, B, and C and points specifically to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the GGGGGDD motif as a nucleotidyltransferase ATP-binding signature is general biochemical knowledge about a large enzyme superfamily, not an item-specific annotation.",
    "reason": "A biologist familiar with the nucleotidyltransferase fold can identify the GGGGGDD motif in the sequence, infer ATP-dependent nucleotidyltransferase activity, and select D as the only ATP-consuming nucleotidyltransferase reaction among the choices. This is a concrete, general-knowledge-based argument rather than reliance on an exact database lookup."
  },
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "C9",
      "H2",
      "H6",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence (389 aa, SHA256 match) corresponds to UniProt Q9VC03 (NMNA_DROME), Drosophila melanogaster Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1). The catalytic activity 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)' is annotated with experimental evidence codes ECO:0000269 from three independent PubMed studies (17132048, 19403820, 26616331) and confirmed by physiological direction (left-to-right, RHEA:21361). Choice D matches this reaction verbatim."
  },
  "important_caveats": [
    "The GGGGGDD motif is shared across the broad nucleotidyltransferase superfamily; identifying the specific sub-family (NMNAT vs. other nucleotidyltransferases) from sequence alone would require additional motifs or structural knowledge. However, the question only requires distinguishing among four very different reaction types, which the ATP-dependence criterion achieves.",
    "The EC 2.7.7.18 annotation is supported only by RuleBase (ECO:0000255, computational), not by direct experimental evidence, whereas EC 2.7.7.1 has three independent experimental confirmations.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein also has secondary EC 2.7.7.18 activity (nicotinate adenylyltransferase), but that reaction (nicotinate ribonucleotide + ATP → deamido-NAD+ + PPi) does not appear among the four choices. The primary EC 2.7.7.1 reaction is unambiguously represented by D, and the other three choices belong to entirely different enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (389 aa, SHA256 match) corresponds to UniProt Q9VC03 (NMNA_DROME), Drosophila melanogaster Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1). The catalytic activity 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)' is annotated with experimental evidence codes ECO:0000269 from three independent PubMed studies (17132048, 19403820, 26616331) and confirmed by physiological direction (left-to-right, RHEA:21361). Choice D matches this reaction verbatim.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "C9", "H2", "H6", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clearly visible GGGGGDD motif (residues ~105-111), which is the canonical glycine-rich ATP-binding motif of the nucleotidyltransferase superfamily. Among the four choices, only D (NMN + ATP → NAD+ + PPi) is a nucleotidyltransferase reaction that uses ATP as a substrate. Choice A is an O-methyltransferase (uses SAM, not ATP), Choice B is a pyrimidine salvage phosphorylase (no ATP), and Choice C is a CoA-transferase/thiolase (no ATP). The GGGGGDD motif thus eliminates A, B, and C and points specifically to D.",
    "missing_item_specific_fact": "None critical. Recognition of the GGGGGDD motif as a nucleotidyltransferase ATP-binding signature is general biochemical knowledge about a large enzyme superfamily, not an item-specific annotation.",
    "reason": "A biologist familiar with the nucleotidyltransferase fold can identify the GGGGGDD motif in the sequence, infer ATP-dependent nucleotidyltransferase activity, and select D as the only ATP-consuming nucleotidyltransferase reaction among the choices. This is a concrete, general-knowledge-based argument rather than reliance on an exact database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein also has secondary EC 2.7.7.18 activity (nicotinate adenylyltransferase), but that reaction (nicotinate ribonucleotide + ATP → deamido-NAD+ + PPi) does not appear among the four choices. The primary EC 2.7.7.1 reaction is unambiguously represented by D, and the other three choices belong to entirely different enzyme classes."
  },
  "important_caveats": [
    "The GGGGGDD motif is shared across the broad nucleotidyltransferase superfamily; identifying the specific sub-family (NMNAT vs. other nucleotidyltransferases) from sequence alone would require additional motifs or structural knowledge. However, the question only requires distinguishing among four very different reaction types, which the ATP-dependence criterion achieves.",
    "The EC 2.7.7.18 annotation is supported only by RuleBase (ECO:0000255, computational), not by direct experimental evidence, whereas EC 2.7.7.1 has three independent experimental confirmations.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and four choices."
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 87-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,
RP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255.
RX   PubMed=17132048; DOI=10.1371/journal.pbio.0040416;
RA   Zhai R.G., Cao Y., Hiesinger P.R., Zhou Y., Mehta S.Q., Schulze K.L.,
RA   Verstreken P., Bellen H.J.;
RT   "Drosophila NMNAT maintains neural integrity independent of its NAD
RT   synthesis activity.";
RL   PLoS Biol. 4:e416-e416(2006).
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 104-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
RN   [7] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.
RX   PubMed=19403820; DOI=10.1523/jneurosci.5469-08.2009;
RA   Sasaki Y., Vohra B.P., Lund F.E., Milbrandt J.;
RT   "Nicotinamide mononucleotide adenylyl transferase-mediated axonal
RT   protection requires enzymatic activity but not increased levels of neuronal
RT   nicotinamide adenine dinucleotide.";
RL   J. Neurosci. 29:5525-5535(2009).
```

Source SHA-256: `6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)  
**Locator:** `lines 125-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 4.  
**Retrieved:** 2026-11-02T04:33:19.400018+00:00.  

```text
RN   [10] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, ALTERNATIVE SPLICING,
RP   INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS, NUCLEAR LOCALISAION SIGNAL,
RP   AND MUTAGENESIS OF LYS-380.
RX   PubMed=26616331; DOI=10.1038/ncomms10057;
RA   Ruan K., Zhu Y., Li C., Brazill J.M., Zhai R.G.;
RT   "Alternative splicing of Drosophila Nmnat functions as a switch to enhance
RT   neuroprotection under stress.";
RL   Nat. Commun. 6:10057-10057(2015).
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
