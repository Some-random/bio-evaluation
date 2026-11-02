# pathway_0111

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. capsule polysaccharide biosynthesis. .
B. peptidoglycan biosynthesis. .
C. Amino-acid biosynthesis
D. L-isoleucine from 2-oxobutanoate: step 3/4. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Candida albicans protein annotated as aspartate-semialdehyde dehydrogenase. Its pathway annotations place it in amino-acid biosynthesis, including methionine and threonine biosynthesis; those pathway annotations cite experimental evidence. This supports choice C rather than the more specific isoleucine-pathway step in D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices suggest distinguishing broad amino-acid biosynthesis from specific peptidoglycan, capsule, or isoleucine-pathway functions, but the supplied sequence alone does not establish which pathway this protein participates in without identifying its enzyme family and function.


**Missing item-specific fact**

> The protein-specific identification as aspartate-semialdehyde dehydrogenase, and its associated pathway annotation, is not provided in the question.


**Reason**

> Recognizing the protein family from sequence would require protein-specific homology or annotation knowledge; merely positing that a sequence predictor could identify it does not provide a biological argument from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although amino-acid biosynthesis is broad, the cited pathway annotations support that choice. The more specific isoleucine step does not match the annotated roles in methionine and threonine biosynthesis.


### Important caveats

- The evidence is a matched UniProt annotation whose pathway statements cite PubMed 20124701; the excerpts do not independently establish every pathway assignment.
- The accession and source annotations are reviewer-only and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices suggest distinguishing broad amino-acid biosynthesis from specific peptidoglycan, capsule, or isoleucine-pathway functions, but the supplied sequence alone does not establish which pathway this protein participates in without identifying its enzyme family and function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, and its associated pathway annotation, is not provided in the question.",
    "reason": "Recognizing the protein family from sequence would require protein-specific homology or annotation knowledge; merely positing that a sequence predictor could identify it does not provide a biological argument from the supplied input."
  },
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Candida albicans protein annotated as aspartate-semialdehyde dehydrogenase. Its pathway annotations place it in amino-acid biosynthesis, including methionine and threonine biosynthesis; those pathway annotations cite experimental evidence. This supports choice C rather than the more specific isoleucine-pathway step in D."
  },
  "important_caveats": [
    "The evidence is a matched UniProt annotation whose pathway statements cite PubMed 20124701; the excerpts do not independently establish every pathway assignment.",
    "The accession and source annotations are reviewer-only and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although amino-acid biosynthesis is broad, the cited pathway annotations support that choice. The more specific isoleucine step does not match the annotated roles in methionine and threonine biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Candida albicans protein annotated as aspartate-semialdehyde dehydrogenase. Its pathway annotations place it in amino-acid biosynthesis, including methionine and threonine biosynthesis; those pathway annotations cite experimental evidence. This supports choice C rather than the more specific isoleucine-pathway step in D.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices suggest distinguishing broad amino-acid biosynthesis from specific peptidoglycan, capsule, or isoleucine-pathway functions, but the supplied sequence alone does not establish which pathway this protein participates in without identifying its enzyme family and function.",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, and its associated pathway annotation, is not provided in the question.",
    "reason": "Recognizing the protein family from sequence would require protein-specific homology or annotation knowledge; merely positing that a sequence predictor could identify it does not provide a biological argument from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although amino-acid biosynthesis is broad, the cited pathway annotations support that choice. The more specific isoleucine step does not match the annotated roles in methionine and threonine biosynthesis."
  },
  "important_caveats": [
    "The evidence is a matched UniProt annotation whose pathway statements cite PubMed 20124701; the excerpts do not independently establish every pathway assignment.",
    "The accession and source annotations are reviewer-only and were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0) from Candida albicans. UniProt pathway annotations (evidence C5, C6, H7, H8) explicitly state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5,' both supported by experimental evidence (ECO:0000269, PubMed:20124701, crystallographic study). The expected answer 'Amino-acid biosynthesis' directly matches the top-level pathway category.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGSVGQRFILL, GxGxxG pattern), identifying the protein as an NAD(P)-dependent dehydrogenase/oxidoreductase. This eliminates option A (capsule polysaccharide biosynthesis, which primarily involves glycosyltransferases and nucleotide-sugar synthetases, not NAD(P)-binding dehydrogenases) and option B (peptidoglycan biosynthesis, which is irrelevant since the organism is a fungus lacking peptidoglycan cell walls). Between C and D, option D specifies 'L-isoleucine from 2-oxobutanoate: step 3/4,' which in canonical pathway databases corresponds to dihydroxy-acid dehydratase (EC 4.2.1.9) or branched-chain amino acid aminotransferase—neither of which is an NAD(P)-dependent dehydrogenase. The observed dehydrogenase architecture (NAD(P)-binding Rossmann fold, ~365 aa aldehyde dehydrogenase family size) is inconsistent with a dehydratase or aminotransferase mechanism, making D implausible. Amino-acid biosynthesis (C) encompasses numerous NAD(P)-dependent dehydrogenases (e.g., ASADH, threonine synthase pathway enzymes), making it the most consistent general pathway category.


**Missing item-specific fact**

> None strictly required, though precise identification as ASADH (vs. another dehydrogenase) would benefit from database lookup. The general reasoning chain (NAD(P)-binding dehydrogenase → not a glycosyltransferase → not a dehydratase/aminotransferase → amino acid biosynthesis) provides a defensible path without item-specific memorization.


**Reason**

> The sequence contains a recognizable NAD(P)-binding Rossmann fold motif that establishes dehydrogenase identity. Combined with general knowledge that (1) capsule biosynthesis uses transferases, (2) fungi lack peptidoglycan, and (3) the isoleucine-from-2-oxobutanoate step 3/4 is a dehydratase/aminotransferase reaction incompatible with NAD(P)-dependent oxidation, the answer C can be reached through biological reasoning without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are clearly eliminated (wrong enzyme class and wrong organism type respectively). Option D specifies a particular reaction step (dehydratase/aminotransferase) mechanistically incompatible with the observed NAD(P)-binding dehydrogenase architecture. Only C remains defensible.


### Important caveats

- The NAD(P)-binding Rossmann fold is shared by thousands of dehydrogenases across many pathways; the reasoning eliminates other options by mechanism incompatibility rather than positively confirming ASADH identity.
- Option D's pathway label ('L-isoleucine from 2-oxobutanoate: step 3/4') is a KEGG-style pathway annotation; a model unfamiliar with this specific pathway nomenclature may struggle to eliminate D on mechanistic grounds alone.
- The protein is from Candida albicans (a fungus), which is not stated in the question prompt but is inferable from sequence characteristics; however, elimination of B (peptidoglycan) also follows from the dehydrogenase architecture regardless of organism.
- The UniProt pathway annotation is supported by experimental evidence (crystal structure with NADP+, PubMed:20124701), not merely computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGSVGQRFILL, GxGxxG pattern), identifying the protein as an NAD(P)-dependent dehydrogenase/oxidoreductase. This eliminates option A (capsule polysaccharide biosynthesis, which primarily involves glycosyltransferases and nucleotide-sugar synthetases, not NAD(P)-binding dehydrogenases) and option B (peptidoglycan biosynthesis, which is irrelevant since the organism is a fungus lacking peptidoglycan cell walls). Between C and D, option D specifies 'L-isoleucine from 2-oxobutanoate: step 3/4,' which in canonical pathway databases corresponds to dihydroxy-acid dehydratase (EC 4.2.1.9) or branched-chain amino acid aminotransferase—neither of which is an NAD(P)-dependent dehydrogenase. The observed dehydrogenase architecture (NAD(P)-binding Rossmann fold, ~365 aa aldehyde dehydrogenase family size) is inconsistent with a dehydratase or aminotransferase mechanism, making D implausible. Amino-acid biosynthesis (C) encompasses numerous NAD(P)-dependent dehydrogenases (e.g., ASADH, threonine synthase pathway enzymes), making it the most consistent general pathway category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required, though precise identification as ASADH (vs. another dehydrogenase) would benefit from database lookup. The general reasoning chain (NAD(P)-binding dehydrogenase → not a glycosyltransferase → not a dehydratase/aminotransferase → amino acid biosynthesis) provides a defensible path without item-specific memorization.",
    "reason": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif that establishes dehydrogenase identity. Combined with general knowledge that (1) capsule biosynthesis uses transferases, (2) fungi lack peptidoglycan, and (3) the isoleucine-from-2-oxobutanoate step 3/4 is a dehydratase/aminotransferase reaction incompatible with NAD(P)-dependent oxidation, the answer C can be reached through biological reasoning without memorizing the specific UniProt entry."
  },
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0) from Candida albicans. UniProt pathway annotations (evidence C5, C6, H7, H8) explicitly state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5,' both supported by experimental evidence (ECO:0000269, PubMed:20124701, crystallographic study). The expected answer 'Amino-acid biosynthesis' directly matches the top-level pathway category."
  },
  "important_caveats": [
    "The NAD(P)-binding Rossmann fold is shared by thousands of dehydrogenases across many pathways; the reasoning eliminates other options by mechanism incompatibility rather than positively confirming ASADH identity.",
    "Option D's pathway label ('L-isoleucine from 2-oxobutanoate: step 3/4') is a KEGG-style pathway annotation; a model unfamiliar with this specific pathway nomenclature may struggle to eliminate D on mechanistic grounds alone.",
    "The protein is from Candida albicans (a fungus), which is not stated in the question prompt but is inferable from sequence characteristics; however, elimination of B (peptidoglycan) also follows from the dehydrogenase architecture regardless of organism.",
    "The UniProt pathway annotation is supported by experimental evidence (crystal structure with NADP+, PubMed:20124701), not merely computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly eliminated (wrong enzyme class and wrong organism type respectively). Option D specifies a particular reaction step (dehydratase/aminotransferase) mechanistically incompatible with the observed NAD(P)-binding dehydrogenase architecture. Only C remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11, UniProt Q5ALM0) from Candida albicans. UniProt pathway annotations (evidence C5, C6, H7, H8) explicitly state: 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5,' both supported by experimental evidence (ECO:0000269, PubMed:20124701, crystallographic study). The expected answer 'Amino-acid biosynthesis' directly matches the top-level pathway category.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGSVGQRFILL, GxGxxG pattern), identifying the protein as an NAD(P)-dependent dehydrogenase/oxidoreductase. This eliminates option A (capsule polysaccharide biosynthesis, which primarily involves glycosyltransferases and nucleotide-sugar synthetases, not NAD(P)-binding dehydrogenases) and option B (peptidoglycan biosynthesis, which is irrelevant since the organism is a fungus lacking peptidoglycan cell walls). Between C and D, option D specifies 'L-isoleucine from 2-oxobutanoate: step 3/4,' which in canonical pathway databases corresponds to dihydroxy-acid dehydratase (EC 4.2.1.9) or branched-chain amino acid aminotransferase—neither of which is an NAD(P)-dependent dehydrogenase. The observed dehydrogenase architecture (NAD(P)-binding Rossmann fold, ~365 aa aldehyde dehydrogenase family size) is inconsistent with a dehydratase or aminotransferase mechanism, making D implausible. Amino-acid biosynthesis (C) encompasses numerous NAD(P)-dependent dehydrogenases (e.g., ASADH, threonine synthase pathway enzymes), making it the most consistent general pathway category.",
    "missing_item_specific_fact": "None strictly required, though precise identification as ASADH (vs. another dehydrogenase) would benefit from database lookup. The general reasoning chain (NAD(P)-binding dehydrogenase → not a glycosyltransferase → not a dehydratase/aminotransferase → amino acid biosynthesis) provides a defensible path without item-specific memorization.",
    "reason": "The sequence contains a recognizable NAD(P)-binding Rossmann fold motif that establishes dehydrogenase identity. Combined with general knowledge that (1) capsule biosynthesis uses transferases, (2) fungi lack peptidoglycan, and (3) the isoleucine-from-2-oxobutanoate step 3/4 is a dehydratase/aminotransferase reaction incompatible with NAD(P)-dependent oxidation, the answer C can be reached through biological reasoning without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly eliminated (wrong enzyme class and wrong organism type respectively). Option D specifies a particular reaction step (dehydratase/aminotransferase) mechanistically incompatible with the observed NAD(P)-binding dehydrogenase architecture. Only C remains defensible."
  },
  "important_caveats": [
    "The NAD(P)-binding Rossmann fold is shared by thousands of dehydrogenases across many pathways; the reasoning eliminates other options by mechanism incompatibility rather than positively confirming ASADH identity.",
    "Option D's pathway label ('L-isoleucine from 2-oxobutanoate: step 3/4') is a KEGG-style pathway annotation; a model unfamiliar with this specific pathway nomenclature may struggle to eliminate D on mechanistic grounds alone.",
    "The protein is from Candida albicans (a fungus), which is not stated in the question prompt but is inferable from sequence characteristics; however, elimination of B (peptidoglycan) also follows from the dehydrogenase architecture regardless of organism.",
    "The UniProt pathway annotation is supported by experimental evidence (crystal structure with NADP+, PubMed:20124701), not merely computational inference."
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

**Accession:** `Q5ALM0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 145. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
"Q5ALM0"
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17419877","source":"PubMed"}],"value":"CaASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32383780","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"34469014","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3"}]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20124701","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
ID   DHAS_CANAL              Reviewed;         365 AA.
AC   Q5ALM0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   18-JUN-2025, entry version 145.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};
DE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};
GN   Name=HOM2 {ECO:0000303|PubMed:17419877};
GN   OrderedLocusNames=CAALFM_C202370CA {ECO:0000312|EMBL:AOW27277.1},
GN   orf19.9132 {ECO:0000312|CGD:CAL0000179646};
OS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
OX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 2/3.
CC       {ECO:0000269|PubMed:20124701}.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 117-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:20124701}.
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
