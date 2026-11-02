# catalytic_activity_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. 4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)
B. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
C. (19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
D. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
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

> The supplied sequence exactly matches the reviewed UniProt entry annotated as mitochondrial dihydroxy-acid dehydratase (EC 4.2.1.9), and that entry lists the reaction in choice D. The catalytic-activity annotation is transferred from homologs (ECO:0000250), so this supports D as an annotation-based inference, not as direct experimental verification of this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has an N-terminal region consistent with mitochondrial targeting and a cysteine-containing architecture consistent with the iron-sulfur-dependent IlvD/dihydroxy-acid dehydratase family. That family-level inference favors D over the SAM-dependent methylation in A and the P450-type oxidations in B and C, which would require different catalytic machinery.


**Missing item-specific fact**

> No specific database accession or experimentally established activity is supplied; identifying the enzyme family from sequence features is the relevant inference.


**Reason**

> The choices describe substantially different enzyme classes, and sequence family features provide a biological basis to favor the DHAD reaction. This supports family-level discrimination, though the exact substrate reaction is not independently demonstrated by the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options represent distinct transformations, and the sequence-based DHAD-family inference supports D rather than the methylation or oxidative reactions.


### Important caveats

- The reviewer-only UniProt record matches the sequence, but the exact source snapshot used by the question author is unknown.
- The listed catalytic activity is supported by transfer from homolog annotations; the supplied evidence does not establish direct experimental measurement of this protein's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has an N-terminal region consistent with mitochondrial targeting and a cysteine-containing architecture consistent with the iron-sulfur-dependent IlvD/dihydroxy-acid dehydratase family. That family-level inference favors D over the SAM-dependent methylation in A and the P450-type oxidations in B and C, which would require different catalytic machinery.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No specific database accession or experimentally established activity is supplied; identifying the enzyme family from sequence features is the relevant inference.",
    "reason": "The choices describe substantially different enzyme classes, and sequence family features provide a biological basis to favor the DHAD reaction. This supports family-level discrimination, though the exact substrate reaction is not independently demonstrated by the input alone."
  },
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry annotated as mitochondrial dihydroxy-acid dehydratase (EC 4.2.1.9), and that entry lists the reaction in choice D. The catalytic-activity annotation is transferred from homologs (ECO:0000250), so this supports D as an annotation-based inference, not as direct experimental verification of this exact protein."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the sequence, but the exact source snapshot used by the question author is unknown.",
    "The listed catalytic activity is supported by transfer from homolog annotations; the supplied evidence does not establish direct experimental measurement of this protein's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct transformations, and the sequence-based DHAD-family inference supports D rather than the methylation or oxidative reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry annotated as mitochondrial dihydroxy-acid dehydratase (EC 4.2.1.9), and that entry lists the reaction in choice D. The catalytic-activity annotation is transferred from homologs (ECO:0000250), so this supports D as an annotation-based inference, not as direct experimental verification of this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has an N-terminal region consistent with mitochondrial targeting and a cysteine-containing architecture consistent with the iron-sulfur-dependent IlvD/dihydroxy-acid dehydratase family. That family-level inference favors D over the SAM-dependent methylation in A and the P450-type oxidations in B and C, which would require different catalytic machinery.",
    "missing_item_specific_fact": "No specific database accession or experimentally established activity is supplied; identifying the enzyme family from sequence features is the relevant inference.",
    "reason": "The choices describe substantially different enzyme classes, and sequence family features provide a biological basis to favor the DHAD reaction. This supports family-level discrimination, though the exact substrate reaction is not independently demonstrated by the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct transformations, and the sequence-based DHAD-family inference supports D rather than the methylation or oxidative reactions."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the sequence, but the exact source snapshot used by the question author is unknown.",
    "The listed catalytic activity is supported by transfer from homolog annotations; the supplied evidence does not establish direct experimental measurement of this protein's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F7TWW9 (PBRD_PENBI, Dihydroxy-acid dehydratase pbrD, mitochondrial, EC 4.2.1.9) explicitly lists the reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' as its catalytic activity (evidence C5/H4), matching option D verbatim. The sequence is an exact match (596 AA, SHA256 identical). Note: the reaction-level evidence code is ECO:0000250 (similarity to Q0CPG9), indicating computational transfer rather than direct experimental characterization of this specific protein, though the EC number assignment (ECO:0000305) is based on PubMed:39511739.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could attempt elimination reasoning: options B and C describe cytochrome P450 reactions requiring a canonical heme-binding motif (FxxGxxxCxG), which is absent from the sequence; option A describes a SAM-dependent methyltransferase requiring a Rossmann-like SAM-binding motif, also not clearly present. This partially eliminates three choices. However, positively identifying the protein as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from sequence alone requires recognizing specific DHAD-family motifs (e.g., the conserved region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the C-terminal nucleotide-binding-like 'GKITGKEGLRFEG'), which is a specialized family-level annotation knowledge rather than general biological reasoning. The mitochondrial targeting sequence (N-terminal Arg/Ser-rich region) is consistent with fungal DHAD localization but does not uniquely identify the enzyme class.


**Missing item-specific fact**

> Recognition of specific DHAD (PF00367) family catalytic motifs sufficient to positively assign EC 4.2.1.9 activity from a 596-residue fungal sequence, or prior knowledge that this specific Penicillium brasilianum protein (pbrD) is annotated as a dihydroxy-acid dehydratase.


**Reason**

> While absence of P450 and SAM-binding motifs allows partial elimination of options A-C, the positive identification of DHAD catalytic activity requires either detailed family-motif recognition or direct database lookup. The sequence does not contain a universally recognizable 'this is DHAD' signature that general biological knowledge would reliably extract without specialized enzymology training.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry lists two DHAD reactions (C5 and C6), but only the valine-pathway reaction (option D) appears among the choices. The isoleucine-pathway reaction is not offered as a distractor, so no ambiguity exists among the given options. The four choices span clearly distinct enzyme classes (methyltransferase, P450, P450, dehydratase), making them mutually exclusive.


### Important caveats

- The reaction evidence for this specific protein is ECO:0000250 (similarity-based transfer from Q0CPG9), not direct experimental kinetics on pbrD itself. The EC assignment (ECO:0000305) is curator-inferred from PubMed:39511739.
- The protein also catalyzes a second DHAD reaction (C6/H5) on the isoleucine pathway substrate, which is not among the answer choices.
- The identity of the UniProt accession was inferred by the reviewer from dataset metadata, not provided to the evaluated model.
- The protein is a mitochondrial precursor (N-terminal targeting sequence), which is consistent with fungal DHAD localization but not uniquely diagnostic of the enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could attempt elimination reasoning: options B and C describe cytochrome P450 reactions requiring a canonical heme-binding motif (FxxGxxxCxG), which is absent from the sequence; option A describes a SAM-dependent methyltransferase requiring a Rossmann-like SAM-binding motif, also not clearly present. This partially eliminates three choices. However, positively identifying the protein as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from sequence alone requires recognizing specific DHAD-family motifs (e.g., the conserved region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the C-terminal nucleotide-binding-like 'GKITGKEGLRFEG'), which is a specialized family-level annotation knowledge rather than general biological reasoning. The mitochondrial targeting sequence (N-terminal Arg/Ser-rich region) is consistent with fungal DHAD localization but does not uniquely identify the enzyme class.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of specific DHAD (PF00367) family catalytic motifs sufficient to positively assign EC 4.2.1.9 activity from a 596-residue fungal sequence, or prior knowledge that this specific Penicillium brasilianum protein (pbrD) is annotated as a dihydroxy-acid dehydratase.",
    "reason": "While absence of P450 and SAM-binding motifs allows partial elimination of options A-C, the positive identification of DHAD catalytic activity requires either detailed family-motif recognition or direct database lookup. The sequence does not contain a universally recognizable 'this is DHAD' signature that general biological knowledge would reliably extract without specialized enzymology training."
  },
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (PBRD_PENBI, Dihydroxy-acid dehydratase pbrD, mitochondrial, EC 4.2.1.9) explicitly lists the reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' as its catalytic activity (evidence C5/H4), matching option D verbatim. The sequence is an exact match (596 AA, SHA256 identical). Note: the reaction-level evidence code is ECO:0000250 (similarity to Q0CPG9), indicating computational transfer rather than direct experimental characterization of this specific protein, though the EC number assignment (ECO:0000305) is based on PubMed:39511739."
  },
  "important_caveats": [
    "The reaction evidence for this specific protein is ECO:0000250 (similarity-based transfer from Q0CPG9), not direct experimental kinetics on pbrD itself. The EC assignment (ECO:0000305) is curator-inferred from PubMed:39511739.",
    "The protein also catalyzes a second DHAD reaction (C6/H5) on the isoleucine pathway substrate, which is not among the answer choices.",
    "The identity of the UniProt accession was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The protein is a mitochondrial precursor (N-terminal targeting sequence), which is consistent with fungal DHAD localization but not uniquely diagnostic of the enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry lists two DHAD reactions (C5 and C6), but only the valine-pathway reaction (option D) appears among the choices. The isoleucine-pathway reaction is not offered as a distractor, so no ambiguity exists among the given options. The four choices span clearly distinct enzyme classes (methyltransferase, P450, P450, dehydratase), making them mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (PBRD_PENBI, Dihydroxy-acid dehydratase pbrD, mitochondrial, EC 4.2.1.9) explicitly lists the reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' as its catalytic activity (evidence C5/H4), matching option D verbatim. The sequence is an exact match (596 AA, SHA256 identical). Note: the reaction-level evidence code is ECO:0000250 (similarity to Q0CPG9), indicating computational transfer rather than direct experimental characterization of this specific protein, though the EC number assignment (ECO:0000305) is based on PubMed:39511739.",
    "evidence_ids": ["C5", "C4", "H4", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could attempt elimination reasoning: options B and C describe cytochrome P450 reactions requiring a canonical heme-binding motif (FxxGxxxCxG), which is absent from the sequence; option A describes a SAM-dependent methyltransferase requiring a Rossmann-like SAM-binding motif, also not clearly present. This partially eliminates three choices. However, positively identifying the protein as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from sequence alone requires recognizing specific DHAD-family motifs (e.g., the conserved region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the C-terminal nucleotide-binding-like 'GKITGKEGLRFEG'), which is a specialized family-level annotation knowledge rather than general biological reasoning. The mitochondrial targeting sequence (N-terminal Arg/Ser-rich region) is consistent with fungal DHAD localization but does not uniquely identify the enzyme class.",
    "missing_item_specific_fact": "Recognition of specific DHAD (PF00367) family catalytic motifs sufficient to positively assign EC 4.2.1.9 activity from a 596-residue fungal sequence, or prior knowledge that this specific Penicillium brasilianum protein (pbrD) is annotated as a dihydroxy-acid dehydratase.",
    "reason": "While absence of P450 and SAM-binding motifs allows partial elimination of options A-C, the positive identification of DHAD catalytic activity requires either detailed family-motif recognition or direct database lookup. The sequence does not contain a universally recognizable 'this is DHAD' signature that general biological knowledge would reliably extract without specialized enzymology training."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry lists two DHAD reactions (C5 and C6), but only the valine-pathway reaction (option D) appears among the choices. The isoleucine-pathway reaction is not offered as a distractor, so no ambiguity exists among the given options. The four choices span clearly distinct enzyme classes (methyltransferase, P450, P450, dehydratase), making them mutually exclusive."
  },
  "important_caveats": [
    "The reaction evidence for this specific protein is ECO:0000250 (similarity-based transfer from Q0CPG9), not direct experimental kinetics on pbrD itself. The EC assignment (ECO:0000305) is curator-inferred from PubMed:39511739.",
    "The protein also catalyzes a second DHAD reaction (C6/H5) on the isoleucine pathway substrate, which is not among the answer choices.",
    "The identity of the UniProt accession was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The protein is a mitochondrial precursor (N-terminal targeting sequence), which is consistent with fungal DHAD localization but not uniquely diagnostic of the enzyme class."
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

**Accession:** `A0A0F7TWW9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24810"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"name":"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24809"},{"database":"ChEBI","id":"CHEBI:11851"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:49072"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:27695"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"name":"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:27694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35146"},{"database":"ChEBI","id":"CHEBI:49258"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 24-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
RN   [2]
RP   FUNCTION.
RX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;
RA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;
RT   "Yeast synthesis and herbicidal activity evaluation of aspterric acid.";
RL   J. Agric. Food Chem. 72:25755-25766(2024).
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 44-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate
CC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:49072; EC=4.2.1.9;
CC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;
CC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 51-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-
CC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;
CC         Evidence={ECO:0000250|UniProtKB:P05791};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;
CC         Evidence={ECO:0000250|UniProtKB:P05791};
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
