# EC_number_0132

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.2.1.9

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 4.2.1.18
B. 2.7.1.52
C. 4.2.1.9
D. 2.3.1.322
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

> The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).


**Reason**

> Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation.


### Important caveats

- The reviewer-only database evidence was not available to the evaluated model.
- The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).",
    "reason": "Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).",
    "reason": "Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial argument exists: (1) The protein contains &#91;4Fe-4S&#93; cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.


**Missing item-specific fact**

> The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the &#91;4Fe-4S&#93; cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.


**Reason**

> While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible.


### Important caveats

- The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.
- The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.
- The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.
- The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial argument exists: (1) The protein contains [4Fe-4S] cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the [4Fe-4S] cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.",
    "reason": "While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa)."
  },
  "important_caveats": [
    "The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.",
    "The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.",
    "The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.",
    "The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial argument exists: (1) The protein contains [4Fe-4S] cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.",
    "missing_item_specific_fact": "The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the [4Fe-4S] cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.",
    "reason": "While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.",
    "The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.",
    "The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.",
    "The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input."
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

**Accession:** `Q0CPG9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
"Q0CPG9"
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase astD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24810"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"name":"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24809"},{"database":"ChEBI","id":"CHEBI:11851"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:49072"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:27695"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"name":"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:27694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35146"},{"database":"ChEBI","id":"CHEBI:49258"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};
DE            Short=DHAD astD {ECO:0000303|PubMed:29995859};
DE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};
DE   Flags: Precursor;
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 52-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate
CC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:49072; EC=4.2.1.9;
CC         Evidence={ECO:0000269|PubMed:29995859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;
CC         Evidence={ECO:0000269|PubMed:29995859};
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 59-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-
CC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;
CC         Evidence={ECO:0000250|UniProtKB:P05791};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;
CC         Evidence={ECO:0000250|UniProtKB:P05791};
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
