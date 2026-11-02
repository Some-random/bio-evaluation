# catalytic_activity_0125

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4&#x27;-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
C. spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
D. 4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the sequence in UniProt entries identifying this protein as Mcr-2 and annotating its catalytic activity as choice A. The annotation cites PubMed 30194678; this supports the key, though the excerpts do not independently establish the experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segments suggest a membrane-associated enzyme, making a lipid-modifying reaction more plausible than the soluble-enzyme reactions in B–D. That broad clue does not identify the lipid substrate or the specific transfer reaction in A.


**Missing item-specific fact**

> The Mcr-2-specific catalytic assignment that it transfers phosphoethanolamine from phosphatidylethanolamine to lipid A.


**Reason**

> Sequence architecture offers a broad functional clue but does not establish the precise reaction among the choices; distinguishing A requires protein-specific functional annotation or equivalent external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A, and the choices describe substantially different enzyme activities.


### Important caveats

- The supporting UniProt annotations are reviewer-only and were not supplied to the evaluated model.
- The cited annotation carries a manual assertion evidence code and cites a paper; the excerpts do not independently verify the primary experimental evidence for the exact reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segments suggest a membrane-associated enzyme, making a lipid-modifying reaction more plausible than the soluble-enzyme reactions in B–D. That broad clue does not identify the lipid substrate or the specific transfer reaction in A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The Mcr-2-specific catalytic assignment that it transfers phosphoethanolamine from phosphatidylethanolamine to lipid A.",
    "reason": "Sequence architecture offers a broad functional clue but does not establish the precise reaction among the choices; distinguishing A requires protein-specific functional annotation or equivalent external knowledge."
  },
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in UniProt entries identifying this protein as Mcr-2 and annotating its catalytic activity as choice A. The annotation cites PubMed 30194678; this supports the key, though the excerpts do not independently establish the experimental details."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not supplied to the evaluated model.",
    "The cited annotation carries a manual assertion evidence code and cites a paper; the excerpts do not independently verify the primary experimental evidence for the exact reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A, and the choices describe substantially different enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in UniProt entries identifying this protein as Mcr-2 and annotating its catalytic activity as choice A. The annotation cites PubMed 30194678; this supports the key, though the excerpts do not independently establish the experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segments suggest a membrane-associated enzyme, making a lipid-modifying reaction more plausible than the soluble-enzyme reactions in B–D. That broad clue does not identify the lipid substrate or the specific transfer reaction in A.",
    "missing_item_specific_fact": "The Mcr-2-specific catalytic assignment that it transfers phosphoethanolamine from phosphatidylethanolamine to lipid A.",
    "reason": "Sequence architecture offers a broad functional clue but does not establish the precise reaction among the choices; distinguishing A requires protein-specific functional annotation or equivalent external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A, and the choices describe substantially different enzyme activities."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not supplied to the evaluated model.",
    "The cited annotation carries a manual assertion evidence code and cites a paper; the excerpts do not independently verify the primary experimental evidence for the exact reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C4, C5, H2, H4) confirms the sequence (538 AA, SHA256 match) is UniProt A0A1C3NEV1, MCR-2 (Phosphatidylethanolamine transferase Mcr-2, EC 2.7.8.43) from E. coli. The exact catalytic reaction in Choice A is annotated with evidence ECO:0000305|PubMed:30194678 (Wang et al. 2018, Sci China Life Sci), supported by X-ray crystallography (PDB 6A7W), mutagenesis, and functional assays. This is experimental evidence, not mere computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 538-residue sequence contains multiple hydrophobic stretches consistent with transmembrane helices in the N-terminal ~200 residues, followed by a large globular periplasmic/cytoplasmic catalytic domain. Within this domain, motifs such as 'HQMGNHGP' and 'HGESLGENGVYLHGM' are consistent with a zinc-binding metalloenzyme architecture. This overall topology (N-terminal TM helices + large periplasmic zinc-binding catalytic domain acting at the membrane interface) is characteristic of phosphatidylethanolamine transferases that modify lipid substrates. This architecture is strongly inconsistent with the other options: a chitinase (option B) would be a soluble glycoside hydrolase with a (β/α)8 TIM-barrel and no TM helices; a carotenoid oxygenase (option C) would have a carotenoid-binding fold and no TM regions; a SAM-dependent methyltransferase (option D) would display a Rossmann-like fold with a catalytic Lys/Asp/Glu triad and no TM helices. Among the four choices, only option A (a phosphatidylethanolamine transferase reaction on lipid A) is consistent with a membrane-associated, zinc-dependent lipid-modifying enzyme.


**Missing item-specific fact**

> Precise identification of the enzyme as MCR-2 (rather than MCR-1, MCR-3, or another phosphatidylethanolamine transferase) and confirmation that the specific substrate is lipid A 4'-phosphate rather than another phosphatidylethanolamine acceptor would require recognizing the MCR-family sequence signature or consulting the database entry. However, since option A is the only phosphatidylethanolamine transferase reaction among the choices, the general architectural reasoning is sufficient to select it.


**Reason**

> The sequence architecture (TM helices + large periplasmic zinc-binding domain) provides a concrete biological argument that meaningfully distinguishes a membrane lipid-modifying transferase from a soluble hydrolase, a carotenoid oxygenase, and a methyltransferase. The reasoning does not require memorizing the exact UniProt entry, though specific MCR-family motif recognition strengthens confidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different enzyme classes (phosphatidylethanolamine transferase, glycoside hydrolase, carotenoid oxygenase, methyltransferase). The sequence's multi-TM topology and zinc-binding-like motifs are incompatible with options B, C, and D. No other option is defensible given the sequence features.


### Important caveats

- The specific stoichiometry and product naming in option A (lipid A 4'-(2-aminoethyl diphosphate)) are highly specific; a model might correctly infer 'phosphatidylethanolamine transferase' from architecture but still struggle with the exact reaction equation without MCR-family knowledge.
- The reviewer evidence confirms the sequence is MCR-2 with experimental support (X-ray crystallography, mutagenesis, PubMed 30194678), but this annotation was not available to the evaluated model.
- The MCR-family zinc-binding motifs (HQMGNHGP, HGM) are recognizable to a trained expert but represent a specific family signature rather than a universally derivable feature from first principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 538-residue sequence contains multiple hydrophobic stretches consistent with transmembrane helices in the N-terminal ~200 residues, followed by a large globular periplasmic/cytoplasmic catalytic domain. Within this domain, motifs such as 'HQMGNHGP' and 'HGESLGENGVYLHGM' are consistent with a zinc-binding metalloenzyme architecture. This overall topology (N-terminal TM helices + large periplasmic zinc-binding catalytic domain acting at the membrane interface) is characteristic of phosphatidylethanolamine transferases that modify lipid substrates. This architecture is strongly inconsistent with the other options: a chitinase (option B) would be a soluble glycoside hydrolase with a (β/α)8 TIM-barrel and no TM helices; a carotenoid oxygenase (option C) would have a carotenoid-binding fold and no TM regions; a SAM-dependent methyltransferase (option D) would display a Rossmann-like fold with a catalytic Lys/Asp/Glu triad and no TM helices. Among the four choices, only option A (a phosphatidylethanolamine transferase reaction on lipid A) is consistent with a membrane-associated, zinc-dependent lipid-modifying enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the enzyme as MCR-2 (rather than MCR-1, MCR-3, or another phosphatidylethanolamine transferase) and confirmation that the specific substrate is lipid A 4'-phosphate rather than another phosphatidylethanolamine acceptor would require recognizing the MCR-family sequence signature or consulting the database entry. However, since option A is the only phosphatidylethanolamine transferase reaction among the choices, the general architectural reasoning is sufficient to select it.",
    "reason": "The sequence architecture (TM helices + large periplasmic zinc-binding domain) provides a concrete biological argument that meaningfully distinguishes a membrane lipid-modifying transferase from a soluble hydrolase, a carotenoid oxygenase, and a methyltransferase. The reasoning does not require memorizing the exact UniProt entry, though specific MCR-family motif recognition strengthens confidence."
  },
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms the sequence (538 AA, SHA256 match) is UniProt A0A1C3NEV1, MCR-2 (Phosphatidylethanolamine transferase Mcr-2, EC 2.7.8.43) from E. coli. The exact catalytic reaction in Choice A is annotated with evidence ECO:0000305|PubMed:30194678 (Wang et al. 2018, Sci China Life Sci), supported by X-ray crystallography (PDB 6A7W), mutagenesis, and functional assays. This is experimental evidence, not mere computational inference."
  },
  "important_caveats": [
    "The specific stoichiometry and product naming in option A (lipid A 4'-(2-aminoethyl diphosphate)) are highly specific; a model might correctly infer 'phosphatidylethanolamine transferase' from architecture but still struggle with the exact reaction equation without MCR-family knowledge.",
    "The reviewer evidence confirms the sequence is MCR-2 with experimental support (X-ray crystallography, mutagenesis, PubMed 30194678), but this annotation was not available to the evaluated model.",
    "The MCR-family zinc-binding motifs (HQMGNHGP, HGM) are recognizable to a trained expert but represent a specific family signature rather than a universally derivable feature from first principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (phosphatidylethanolamine transferase, glycoside hydrolase, carotenoid oxygenase, methyltransferase). The sequence's multi-TM topology and zinc-binding-like motifs are incompatible with options B, C, and D. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms the sequence (538 AA, SHA256 match) is UniProt A0A1C3NEV1, MCR-2 (Phosphatidylethanolamine transferase Mcr-2, EC 2.7.8.43) from E. coli. The exact catalytic reaction in Choice A is annotated with evidence ECO:0000305|PubMed:30194678 (Wang et al. 2018, Sci China Life Sci), supported by X-ray crystallography (PDB 6A7W), mutagenesis, and functional assays. This is experimental evidence, not mere computational inference.",
    "evidence_ids": ["C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 538-residue sequence contains multiple hydrophobic stretches consistent with transmembrane helices in the N-terminal ~200 residues, followed by a large globular periplasmic/cytoplasmic catalytic domain. Within this domain, motifs such as 'HQMGNHGP' and 'HGESLGENGVYLHGM' are consistent with a zinc-binding metalloenzyme architecture. This overall topology (N-terminal TM helices + large periplasmic zinc-binding catalytic domain acting at the membrane interface) is characteristic of phosphatidylethanolamine transferases that modify lipid substrates. This architecture is strongly inconsistent with the other options: a chitinase (option B) would be a soluble glycoside hydrolase with a (β/α)8 TIM-barrel and no TM helices; a carotenoid oxygenase (option C) would have a carotenoid-binding fold and no TM regions; a SAM-dependent methyltransferase (option D) would display a Rossmann-like fold with a catalytic Lys/Asp/Glu triad and no TM helices. Among the four choices, only option A (a phosphatidylethanolamine transferase reaction on lipid A) is consistent with a membrane-associated, zinc-dependent lipid-modifying enzyme.",
    "missing_item_specific_fact": "Precise identification of the enzyme as MCR-2 (rather than MCR-1, MCR-3, or another phosphatidylethanolamine transferase) and confirmation that the specific substrate is lipid A 4'-phosphate rather than another phosphatidylethanolamine acceptor would require recognizing the MCR-family sequence signature or consulting the database entry. However, since option A is the only phosphatidylethanolamine transferase reaction among the choices, the general architectural reasoning is sufficient to select it.",
    "reason": "The sequence architecture (TM helices + large periplasmic zinc-binding domain) provides a concrete biological argument that meaningfully distinguishes a membrane lipid-modifying transferase from a soluble hydrolase, a carotenoid oxygenase, and a methyltransferase. The reasoning does not require memorizing the exact UniProt entry, though specific MCR-family motif recognition strengthens confidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different enzyme classes (phosphatidylethanolamine transferase, glycoside hydrolase, carotenoid oxygenase, methyltransferase). The sequence's multi-TM topology and zinc-binding-like motifs are incompatible with options B, C, and D. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The specific stoichiometry and product naming in option A (lipid A 4'-(2-aminoethyl diphosphate)) are highly specific; a model might correctly infer 'phosphatidylethanolamine transferase' from architecture but still struggle with the exact reaction equation without MCR-family knowledge.",
    "The reviewer evidence confirms the sequence is MCR-2 with experimental support (X-ray crystallography, mutagenesis, PubMed 30194678), but this annotation was not available to the evaluated model.",
    "The MCR-family zinc-binding motifs (HQMGNHGP, HGM) are recognizable to a trained expert but represent a specific family signature rather than a universally derivable feature from first principles."
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

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
"A0A1C3NEV1"
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"}],"value":"Polymyxin resistance protein MCR-2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"value":"2.7.8.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30194678","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"Ref.1","source":"Reference"}],"value":"Phosphatidylethanolamine transferase Mcr-2"}}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.43","evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"name":"lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46900"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17815"},{"database":"ChEBI","id":"CHEBI:64612"},{"database":"ChEBI","id":"CHEBI:87097"},{"database":"ChEBI","id":"CHEBI:134257"}]}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
DE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};
DE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};
DE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 44-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6A7W}
RP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),
RP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;
RP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;
RP   LYS-331 AND HIS-476.
RC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};
RX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;
RA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;
RT   "Structural and functional insights into MCR-2 mediated colistin
RT   resistance.";
RL   Sci. China Life Sci. 61:1432-1436(2018).
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 72-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-
CC         phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate)
CC         (E. coli) + a 1,2-diacyl-sn-glycerol; Xref=Rhea:RHEA:46900,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17815, ChEBI:CHEBI:64612,
CC         ChEBI:CHEBI:87097, ChEBI:CHEBI:134257; EC=2.7.8.43;
CC         Evidence={ECO:0000305|PubMed:30194678};
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
