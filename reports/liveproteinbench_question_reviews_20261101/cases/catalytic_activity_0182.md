# catalytic_activity_0182

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a 14alpha-methyl steroid + 3 reduced &#91;NADPH--hemoprotein reductase&#93; + 3 O2 = a Delta(14) steroid + formate + 3 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 4 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)
B. 3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = 4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
C. L-tyrosine + O2 = L-dopaquinone + H2O
D. a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)
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

> The exact sequence matches the UniProt entry annotated as sterol 14-alpha demethylase rstn2, and both the archived and current records list the reaction in D. The reaction annotation is transferred from a homolog (ECO:0000250), so this supports the key as a database annotation but is not direct experimental validation of this sequence’s activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450: it has an N-terminal hydrophobic anchor and a conserved P450 heme-binding cysteine-region motif. Of the choices, D is the P450-type monooxygenase reaction; A is a hydrolase reaction, B a methyltransferase reaction, and C a tyrosinase reaction.


**Missing item-specific fact**

> The sequence-based P450-family inference alone does not establish the precise CYP51 substrate specificity or prove the exact reaction stoichiometry; those details would require family-level identification or external annotation.


**Reason**

> The sequence and the contrast among the choices provide a meaningful biological basis for favoring D without needing to recall this exact accession. The finer claim that this particular P450 catalyzes sterol 14-alpha demethylation remains more specific than the broad sequence-class inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct enzyme reaction classes, and D is the choice consistent with the sequence’s P450 features.


### Important caveats

- The matched UniProt reaction annotation is supported by transfer from a homolog; the supplied evidence does not independently establish direct experimental measurement of this exact protein’s activity.
- The author’s source snapshot is unknown, although the sequence matches both the historical and current entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450: it has an N-terminal hydrophobic anchor and a conserved P450 heme-binding cysteine-region motif. Of the choices, D is the P450-type monooxygenase reaction; A is a hydrolase reaction, B a methyltransferase reaction, and C a tyrosinase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence-based P450-family inference alone does not establish the precise CYP51 substrate specificity or prove the exact reaction stoichiometry; those details would require family-level identification or external annotation.",
    "reason": "The sequence and the contrast among the choices provide a meaningful biological basis for favoring D without needing to recall this exact accession. The finer claim that this particular P450 catalyzes sterol 14-alpha demethylation remains more specific than the broad sequence-class inference."
  },
  "case_id": "catalytic_activity_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as sterol 14-alpha demethylase rstn2, and both the archived and current records list the reaction in D. The reaction annotation is transferred from a homolog (ECO:0000250), so this supports the key as a database annotation but is not direct experimental validation of this sequence’s activity."
  },
  "important_caveats": [
    "The matched UniProt reaction annotation is supported by transfer from a homolog; the supplied evidence does not independently establish direct experimental measurement of this exact protein’s activity.",
    "The author’s source snapshot is unknown, although the sequence matches both the historical and current entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme reaction classes, and D is the choice consistent with the sequence’s P450 features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as sterol 14-alpha demethylase rstn2, and both the archived and current records list the reaction in D. The reaction annotation is transferred from a homolog (ECO:0000250), so this supports the key as a database annotation but is not direct experimental validation of this sequence’s activity.",
    "evidence_ids": ["C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450: it has an N-terminal hydrophobic anchor and a conserved P450 heme-binding cysteine-region motif. Of the choices, D is the P450-type monooxygenase reaction; A is a hydrolase reaction, B a methyltransferase reaction, and C a tyrosinase reaction.",
    "missing_item_specific_fact": "The sequence-based P450-family inference alone does not establish the precise CYP51 substrate specificity or prove the exact reaction stoichiometry; those details would require family-level identification or external annotation.",
    "reason": "The sequence and the contrast among the choices provide a meaningful biological basis for favoring D without needing to recall this exact accession. The finer claim that this particular P450 catalyzes sterol 14-alpha demethylation remains more specific than the broad sequence-class inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme reaction classes, and D is the choice consistent with the sequence’s P450 features."
  },
  "important_caveats": [
    "The matched UniProt reaction annotation is supported by transfer from a homolog; the supplied evidence does not independently establish direct experimental measurement of this exact protein’s activity.",
    "The author’s source snapshot is unknown, although the sequence matches both the historical and current entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 513-aa sequence matches UniProt entry A0A0L1JEW4 exactly (sequence SHA256 confirmed). This entry is annotated as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154) from Aspergillus nomiae. Evidence C5/H4 lists the exact reaction in Choice D verbatim as a CATALYTIC ACTIVITY annotation. The EC number assignment carries experimental evidence (ECO:0000269, PubMed 33857369). The overall 3-step stoichiometry is annotated by similarity (ECO:0000250 to Q4WNT5), but the EC classification and protein identity are experimentally supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRHRCIGE' (matching the FxxGxxRxCxG signature), identifying this protein as a P450 monooxygenase. Among the four choices, only D involves NADPH--hemoprotein reductase and molecular oxygen in a P450-type oxidation (sterol 14α-demethylation). Choice A is an ADP-ribosyltransferase reaction, B is a methyltransferase reaction, and C is a copper-dependent tyrosinase reaction—none use heme or P450 reductase. Recognizing the heme-binding motif is general enzymology knowledge that eliminates all non-P450 options.


**Missing item-specific fact**

> None required. The heme-binding motif is a general structural signature of P450 enzymes, and only one answer option corresponds to a P450 reaction.


**Reason**

> A model with general knowledge of P450 heme-binding motifs (FxxGxxRxCxG) can locate 'FGAGRHRCIGE' in the sequence, classify the protein as a cytochrome P450, and then select D because it is the only option involving NADPH--hemoprotein reductase and O2 in a P450-catalyzed transformation. The other three choices describe mechanistically distinct enzyme classes (transferase, methyltransferase, copper oxidase) incompatible with a heme-containing monooxygenase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four mechanistically distinct enzyme classes (ADP-ribosyltransferase, methyltransferase, copper-dependent oxidase, P450 monooxygenase). The heme-binding motif uniquely selects the P450 reaction (D). No other option is compatible with a cytochrome P450.


### Important caveats

- The overall 3-step reaction stoichiometry in Choice D is annotated by similarity (ECO:0000250 to Q4WNT5, a yeast CYP51), not directly experimentally measured on this specific Aspergillus rstn2 protein. The EC number assignment itself has experimental support (ECO:0000269).
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning.
- The entry was first publicly released in 2025-02-05 (entry version 38 at historical cutoff); the author's source snapshot is unknown but sequence match is confirmed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRHRCIGE' (matching the FxxGxxRxCxG signature), identifying this protein as a P450 monooxygenase. Among the four choices, only D involves NADPH--hemoprotein reductase and molecular oxygen in a P450-type oxidation (sterol 14α-demethylation). Choice A is an ADP-ribosyltransferase reaction, B is a methyltransferase reaction, and C is a copper-dependent tyrosinase reaction—none use heme or P450 reductase. Recognizing the heme-binding motif is general enzymology knowledge that eliminates all non-P450 options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The heme-binding motif is a general structural signature of P450 enzymes, and only one answer option corresponds to a P450 reaction.",
    "reason": "A model with general knowledge of P450 heme-binding motifs (FxxGxxRxCxG) can locate 'FGAGRHRCIGE' in the sequence, classify the protein as a cytochrome P450, and then select D because it is the only option involving NADPH--hemoprotein reductase and O2 in a P450-catalyzed transformation. The other three choices describe mechanistically distinct enzyme classes (transferase, methyltransferase, copper oxidase) incompatible with a heme-containing monooxygenase."
  },
  "case_id": "catalytic_activity_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 513-aa sequence matches UniProt entry A0A0L1JEW4 exactly (sequence SHA256 confirmed). This entry is annotated as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154) from Aspergillus nomiae. Evidence C5/H4 lists the exact reaction in Choice D verbatim as a CATALYTIC ACTIVITY annotation. The EC number assignment carries experimental evidence (ECO:0000269, PubMed 33857369). The overall 3-step stoichiometry is annotated by similarity (ECO:0000250 to Q4WNT5), but the EC classification and protein identity are experimentally supported."
  },
  "important_caveats": [
    "The overall 3-step reaction stoichiometry in Choice D is annotated by similarity (ECO:0000250 to Q4WNT5, a yeast CYP51), not directly experimentally measured on this specific Aspergillus rstn2 protein. The EC number assignment itself has experimental support (ECO:0000269).",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning.",
    "The entry was first publicly released in 2025-02-05 (entry version 38 at historical cutoff); the author's source snapshot is unknown but sequence match is confirmed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four mechanistically distinct enzyme classes (ADP-ribosyltransferase, methyltransferase, copper-dependent oxidase, P450 monooxygenase). The heme-binding motif uniquely selects the P450 reaction (D). No other option is compatible with a cytochrome P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 513-aa sequence matches UniProt entry A0A0L1JEW4 exactly (sequence SHA256 confirmed). This entry is annotated as 'Sterol 14-alpha demethylase rstn2' (EC 1.14.14.154) from Aspergillus nomiae. Evidence C5/H4 lists the exact reaction in Choice D verbatim as a CATALYTIC ACTIVITY annotation. The EC number assignment carries experimental evidence (ECO:0000269, PubMed 33857369). The overall 3-step stoichiometry is annotated by similarity (ECO:0000250 to Q4WNT5), but the EC classification and protein identity are experimentally supported.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGAGRHRCIGE' (matching the FxxGxxRxCxG signature), identifying this protein as a P450 monooxygenase. Among the four choices, only D involves NADPH--hemoprotein reductase and molecular oxygen in a P450-type oxidation (sterol 14α-demethylation). Choice A is an ADP-ribosyltransferase reaction, B is a methyltransferase reaction, and C is a copper-dependent tyrosinase reaction—none use heme or P450 reductase. Recognizing the heme-binding motif is general enzymology knowledge that eliminates all non-P450 options.",
    "missing_item_specific_fact": "None required. The heme-binding motif is a general structural signature of P450 enzymes, and only one answer option corresponds to a P450 reaction.",
    "reason": "A model with general knowledge of P450 heme-binding motifs (FxxGxxRxCxG) can locate 'FGAGRHRCIGE' in the sequence, classify the protein as a cytochrome P450, and then select D because it is the only option involving NADPH--hemoprotein reductase and O2 in a P450-catalyzed transformation. The other three choices describe mechanistically distinct enzyme classes (transferase, methyltransferase, copper oxidase) incompatible with a heme-containing monooxygenase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four mechanistically distinct enzyme classes (ADP-ribosyltransferase, methyltransferase, copper-dependent oxidase, P450 monooxygenase). The heme-binding motif uniquely selects the P450 reaction (D). No other option is compatible with a cytochrome P450."
  },
  "important_caveats": [
    "The overall 3-step reaction stoichiometry in Choice D is annotated by similarity (ECO:0000250 to Q4WNT5, a yeast CYP51), not directly experimentally measured on this specific Aspergillus rstn2 protein. The EC number assignment itself has experimental support (ECO:0000269).",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence-derived reasoning.",
    "The entry was first publicly released in 2025-02-05 (entry version 38 at historical cutoff); the author's source snapshot is unknown but sequence match is confirmed."
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

**Accession:** `A0A0L1JEW4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
"A0A0L1JEW4"
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Ergosterol biosynthesis protein rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase rstn2"}}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:54029"}}],"reaction":{"ecNumber":"1.14.14.154","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"name":"a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54028"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:138029"},{"database":"ChEBI","id":"CHEBI:138031"}]}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
ID   RSTN2_ASPN3             Reviewed;         513 AA.
AC   A0A0L1JEW4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};
GN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 26-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 14alpha-methyl steroid + 3 reduced [NADPH--hemoprotein
CC         reductase] + 3 O2 = a Delta(14) steroid + formate + 3 oxidized
CC         [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+);
CC         Xref=Rhea:RHEA:54028, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,
CC         ChEBI:CHEBI:138029, ChEBI:CHEBI:138031; EC=1.14.14.154;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54029;
CC         Evidence={ECO:0000250|UniProtKB:Q4WNT5};
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
