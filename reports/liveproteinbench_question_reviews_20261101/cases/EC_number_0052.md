# EC_number_0052

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 4.2.1.9

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. 4.2.1.18
B. 2.1.1.392
C. 3.2.1.20
D. 4.2.1.9
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

> The sequence-matched UniProt entry annotates this protein as dihydroxy-acid dehydratase pbrD with EC 4.2.1.9. Its listed catalytic reactions are also assigned EC 4.2.1.9, though those reaction details are transferred from homologs rather than shown here as direct assays of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a mitochondrial enzyme in the dihydroxy-acid dehydratase family, but the input supplies no organism, functional annotation, substrate, or reaction evidence that establishes this protein's complete EC assignment.


**Missing item-specific fact**

> The protein-specific identification and EC annotation as dihydroxy-acid dehydratase pbrD (EC 4.2.1.9), or equivalent reaction evidence, is absent from the question.


**Reason**

> Choosing the precise EC number depends on recognizing or looking up this particular protein's function; broad sequence-family inference alone does not establish the exact reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports D; the other listed choices are not supported by the supplied or reviewer-only evidence.


### Important caveats

- The database annotation links the EC assignment to a publication, but the excerpts do not independently establish that the protein's activity was directly measured.
- The detailed catalytic reactions are supported by similarity transfer from other UniProt entries, not direct evidence for this specific protein.
- The reviewer-only current and historical entries match the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a mitochondrial enzyme in the dihydroxy-acid dehydratase family, but the input supplies no organism, functional annotation, substrate, or reaction evidence that establishes this protein's complete EC assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and EC annotation as dihydroxy-acid dehydratase pbrD (EC 4.2.1.9), or equivalent reaction evidence, is absent from the question.",
    "reason": "Choosing the precise EC number depends on recognizing or looking up this particular protein's function; broad sequence-family inference alone does not establish the exact reaction."
  },
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as dihydroxy-acid dehydratase pbrD with EC 4.2.1.9. Its listed catalytic reactions are also assigned EC 4.2.1.9, though those reaction details are transferred from homologs rather than shown here as direct assays of this protein."
  },
  "important_caveats": [
    "The database annotation links the EC assignment to a publication, but the excerpts do not independently establish that the protein's activity was directly measured.",
    "The detailed catalytic reactions are supported by similarity transfer from other UniProt entries, not direct evidence for this specific protein.",
    "The reviewer-only current and historical entries match the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D; the other listed choices are not supported by the supplied or reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as dihydroxy-acid dehydratase pbrD with EC 4.2.1.9. Its listed catalytic reactions are also assigned EC 4.2.1.9, though those reaction details are transferred from homologs rather than shown here as direct assays of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a mitochondrial enzyme in the dihydroxy-acid dehydratase family, but the input supplies no organism, functional annotation, substrate, or reaction evidence that establishes this protein's complete EC assignment.",
    "missing_item_specific_fact": "The protein-specific identification and EC annotation as dihydroxy-acid dehydratase pbrD (EC 4.2.1.9), or equivalent reaction evidence, is absent from the question.",
    "reason": "Choosing the precise EC number depends on recognizing or looking up this particular protein's function; broad sequence-family inference alone does not establish the exact reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D; the other listed choices are not supported by the supplied or reviewer-only evidence."
  },
  "important_caveats": [
    "The database annotation links the EC assignment to a publication, but the excerpts do not independently establish that the protein's activity was directly measured.",
    "The detailed catalytic reactions are supported by similarity transfer from other UniProt entries, not direct evidence for this specific protein.",
    "The reviewer-only current and historical entries match the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0F7TWW9 (PBRD_PENBI, 596 AA, sequence matched) is annotated as 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC=4.2.1.9. The EC assignment carries evidence code ECO:0000305 (curator inference) supported by PubMed:39511739 (2024, aspterric acid biosynthesis). The two listed catalytic reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate and 2,3-dihydroxy-3-methylpentanoate) are both tagged EC 4.2.1.9 but carry evidence code ECO:0000250 (transferred by similarity from Q0CPG9 and P05791). Thus the key is supported by curated database annotation, though the underlying evidence is curatorial inference plus similarity transfer rather than direct experimental assay of this specific protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Distractors B (EC 2.1.1.392, methyltransferase) and C (EC 3.2.1.20, alpha-glucosidase) belong to entirely different EC top-level classes (transferase, hydrolase) and can be eliminated by recognizing the sequence lacks methyltransferase or glycosidase motifs. The real discrimination is between A (4.2.1.18, aconitase) and D (4.2.1.9, dihydroxy-acid dehydratase), both EC 4.2.1.x dehydratases using Fe-S clusters. Two general biological arguments favor D: (1) The protein is 596 AA, consistent with class II DHAD (~400–600 AA) but notably shorter than aconitase, which is typically ~700–750 AA even in fungi. (2) Class II DHAD uses a &#91;2Fe-2S&#93; cluster with a characteristic Cys spacing pattern, whereas aconitase uses a &#91;4Fe-4S&#93; cluster with a distinct Cys arrangement; the Cys residues in this sequence (e.g., in motifs like 'GCSAKG', 'GACGG') are more consistent with the &#91;2Fe-2S&#93; coordination geometry of DHAD. These length and cluster-type arguments provide a defensible biological basis for choosing D over A.


**Missing item-specific fact**

> None strictly missing; the length and Fe-S cluster-type arguments are general biochemical knowledge. However, precise motif-level confirmation of DHAD vs aconitase fold would require specialized structural knowledge or database lookup.


**Reason**

> The question provides a 596-residue sequence with recognizable dehydratase features. General knowledge of enzyme class sizes (DHAD ~500 AA vs aconitase ~700+ AA) and Fe-S cluster coordination patterns provides a concrete, non-memorization-based argument to distinguish the two plausible dehydratase options. The other two choices are eliminated by EC top-level class reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and C are clearly wrong enzyme classes. The A-vs-D distinction is narrowed by the 596 AA length (too short for aconitase) and Fe-S cluster type inference, making D the most defensible single answer. No other option is equally supported by the sequence.


### Important caveats

- The UniProt EC annotation for this protein is based on curator inference (ECO:0000305) and similarity transfer (ECO:0000250), not direct experimental enzymatic assay of this specific 596-AA protein. The PubMed reference (39511739) concerns aspterric acid biosynthesis in yeast, not isolated DHAD kinetics of pbrD.
- The protein is a mitochondrial precursor (N-terminal targeting sequence present), which is consistent with a branched-chain amino acid biosynthesis enzyme but does not by itself confirm DHAD over aconitase.
- The reviewer-only evidence confirms exact sequence match (596 AA, SHA-256 match) between the benchmark sequence and UniProt A0A0F7TWW9.
- Distinguishing DHAD from aconitase purely by sequence requires specialized knowledge of Fe-S cluster enzyme families; while general biological arguments exist, the margin between A and D is narrower than between A/D and B/C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Distractors B (EC 2.1.1.392, methyltransferase) and C (EC 3.2.1.20, alpha-glucosidase) belong to entirely different EC top-level classes (transferase, hydrolase) and can be eliminated by recognizing the sequence lacks methyltransferase or glycosidase motifs. The real discrimination is between A (4.2.1.18, aconitase) and D (4.2.1.9, dihydroxy-acid dehydratase), both EC 4.2.1.x dehydratases using Fe-S clusters. Two general biological arguments favor D: (1) The protein is 596 AA, consistent with class II DHAD (~400–600 AA) but notably shorter than aconitase, which is typically ~700–750 AA even in fungi. (2) Class II DHAD uses a [2Fe-2S] cluster with a characteristic Cys spacing pattern, whereas aconitase uses a [4Fe-4S] cluster with a distinct Cys arrangement; the Cys residues in this sequence (e.g., in motifs like 'GCSAKG', 'GACGG') are more consistent with the [2Fe-2S] coordination geometry of DHAD. These length and cluster-type arguments provide a defensible biological basis for choosing D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing; the length and Fe-S cluster-type arguments are general biochemical knowledge. However, precise motif-level confirmation of DHAD vs aconitase fold would require specialized structural knowledge or database lookup.",
    "reason": "The question provides a 596-residue sequence with recognizable dehydratase features. General knowledge of enzyme class sizes (DHAD ~500 AA vs aconitase ~700+ AA) and Fe-S cluster coordination patterns provides a concrete, non-memorization-based argument to distinguish the two plausible dehydratase options. The other two choices are eliminated by EC top-level class reasoning."
  },
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0F7TWW9 (PBRD_PENBI, 596 AA, sequence matched) is annotated as 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC=4.2.1.9. The EC assignment carries evidence code ECO:0000305 (curator inference) supported by PubMed:39511739 (2024, aspterric acid biosynthesis). The two listed catalytic reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate and 2,3-dihydroxy-3-methylpentanoate) are both tagged EC 4.2.1.9 but carry evidence code ECO:0000250 (transferred by similarity from Q0CPG9 and P05791). Thus the key is supported by curated database annotation, though the underlying evidence is curatorial inference plus similarity transfer rather than direct experimental assay of this specific protein."
  },
  "important_caveats": [
    "The UniProt EC annotation for this protein is based on curator inference (ECO:0000305) and similarity transfer (ECO:0000250), not direct experimental enzymatic assay of this specific 596-AA protein. The PubMed reference (39511739) concerns aspterric acid biosynthesis in yeast, not isolated DHAD kinetics of pbrD.",
    "The protein is a mitochondrial precursor (N-terminal targeting sequence present), which is consistent with a branched-chain amino acid biosynthesis enzyme but does not by itself confirm DHAD over aconitase.",
    "The reviewer-only evidence confirms exact sequence match (596 AA, SHA-256 match) between the benchmark sequence and UniProt A0A0F7TWW9.",
    "Distinguishing DHAD from aconitase purely by sequence requires specialized knowledge of Fe-S cluster enzyme families; while general biological arguments exist, the margin between A and D is narrower than between A/D and B/C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are clearly wrong enzyme classes. The A-vs-D distinction is narrowed by the 596 AA length (too short for aconitase) and Fe-S cluster type inference, making D the most defensible single answer. No other option is equally supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0F7TWW9 (PBRD_PENBI, 596 AA, sequence matched) is annotated as 'Dihydroxy-acid dehydratase pbrD, mitochondrial' with EC=4.2.1.9. The EC assignment carries evidence code ECO:0000305 (curator inference) supported by PubMed:39511739 (2024, aspterric acid biosynthesis). The two listed catalytic reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate and 2,3-dihydroxy-3-methylpentanoate) are both tagged EC 4.2.1.9 but carry evidence code ECO:0000250 (transferred by similarity from Q0CPG9 and P05791). Thus the key is supported by curated database annotation, though the underlying evidence is curatorial inference plus similarity transfer rather than direct experimental assay of this specific protein.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Distractors B (EC 2.1.1.392, methyltransferase) and C (EC 3.2.1.20, alpha-glucosidase) belong to entirely different EC top-level classes (transferase, hydrolase) and can be eliminated by recognizing the sequence lacks methyltransferase or glycosidase motifs. The real discrimination is between A (4.2.1.18, aconitase) and D (4.2.1.9, dihydroxy-acid dehydratase), both EC 4.2.1.x dehydratases using Fe-S clusters. Two general biological arguments favor D: (1) The protein is 596 AA, consistent with class II DHAD (~400–600 AA) but notably shorter than aconitase, which is typically ~700–750 AA even in fungi. (2) Class II DHAD uses a [2Fe-2S] cluster with a characteristic Cys spacing pattern, whereas aconitase uses a [4Fe-4S] cluster with a distinct Cys arrangement; the Cys residues in this sequence (e.g., in motifs like 'GCSAKG', 'GACGG') are more consistent with the [2Fe-2S] coordination geometry of DHAD. These length and cluster-type arguments provide a defensible biological basis for choosing D over A.",
    "missing_item_specific_fact": "None strictly missing; the length and Fe-S cluster-type arguments are general biochemical knowledge. However, precise motif-level confirmation of DHAD vs aconitase fold would require specialized structural knowledge or database lookup.",
    "reason": "The question provides a 596-residue sequence with recognizable dehydratase features. General knowledge of enzyme class sizes (DHAD ~500 AA vs aconitase ~700+ AA) and Fe-S cluster coordination patterns provides a concrete, non-memorization-based argument to distinguish the two plausible dehydratase options. The other two choices are eliminated by EC top-level class reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are clearly wrong enzyme classes. The A-vs-D distinction is narrowed by the 596 AA length (too short for aconitase) and Fe-S cluster type inference, making D the most defensible single answer. No other option is equally supported by the sequence."
  },
  "important_caveats": [
    "The UniProt EC annotation for this protein is based on curator inference (ECO:0000305) and similarity transfer (ECO:0000250), not direct experimental enzymatic assay of this specific 596-AA protein. The PubMed reference (39511739) concerns aspterric acid biosynthesis in yeast, not isolated DHAD kinetics of pbrD.",
    "The protein is a mitochondrial precursor (N-terminal targeting sequence present), which is consistent with a branched-chain amino acid biosynthesis enzyme but does not by itself confirm DHAD over aconitase.",
    "The reviewer-only evidence confirms exact sequence match (596 AA, SHA-256 match) between the benchmark sequence and UniProt A0A0F7TWW9.",
    "Distinguishing DHAD from aconitase purely by sequence requires specialized knowledge of Fe-S cluster enzyme families; while general biological arguments exist, the margin between A and D is narrower than between A/D and B/C."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
"A0A0F7TWW9"
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

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

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
ID   PBRD_PENBI              Reviewed;         596 AA.
AC   A0A0F7TWW9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
GN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
