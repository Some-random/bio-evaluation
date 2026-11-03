# catalytic_activity_0130: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0130.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **A** — 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate
B. acetaldehyde + NAD(+) + H2O = acetate + NADH + 2 H(+)
C. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
D. spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed UniProt entry for this protein, which records the reaction in choice A with experimental evidence codes and supporting publications. The archived annotation also contains that reaction. The annotation additionally records another catalytic activity, but that reaction is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or recognizable functional label that identifies which reaction this particular protein catalyzes. General biological knowledge alone does not establish the exact sequence-to-function match.


**Missing item-specific fact**

> The protein-specific identification as Plasmodium falciparum chorismate synthase and its experimentally supported catalytic activity are needed to select choice A.


**Reason**

> A sequence-to-function database lookup, prior knowledge of this specific protein, or experimental characterization is needed. Simply recognizing the sequence or asserting that a predictor could classify it would not make the answer reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is supported among the listed options. Although the protein is also annotated with a second activity, that reaction is not listed as a choice.


### Important caveats

- The evidence is a database annotation tied to experimental evidence codes and cited publications; the primary papers were not independently reviewed here.
- The exact source snapshot used by the author is unknown, though the sequence matches both the current and checked historical entries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or recognizable functional label that identifies which reaction this particular protein catalyzes. General biological knowledge alone does not establish the exact sequence-to-function match.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Plasmodium falciparum chorismate synthase and its experimentally supported catalytic activity are needed to select choice A.",
    "reason": "A sequence-to-function database lookup, prior knowledge of this specific protein, or experimental characterization is needed. Simply recognizing the sequence or asserting that a predictor could classify it would not make the answer reasoning-supported."
  },
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for this protein, which records the reaction in choice A with experimental evidence codes and supporting publications. The archived annotation also contains that reaction. The annotation additionally records another catalytic activity, but that reaction is not among the choices."
  },
  "important_caveats": [
    "The evidence is a database annotation tied to experimental evidence codes and cited publications; the primary papers were not independently reviewed here.",
    "The exact source snapshot used by the author is unknown, though the sequence matches both the current and checked historical entries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is supported among the listed options. Although the protein is also annotated with a second activity, that reaction is not listed as a choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for this protein, which records the reaction in choice A with experimental evidence codes and supporting publications. The archived annotation also contains that reaction. The annotation additionally records another catalytic activity, but that reaction is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or recognizable functional label that identifies which reaction this particular protein catalyzes. General biological knowledge alone does not establish the exact sequence-to-function match.",
    "missing_item_specific_fact": "The protein-specific identification as Plasmodium falciparum chorismate synthase and its experimentally supported catalytic activity are needed to select choice A.",
    "reason": "A sequence-to-function database lookup, prior knowledge of this specific protein, or experimental characterization is needed. Simply recognizing the sequence or asserting that a predictor could classify it would not make the answer reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is supported among the listed options. Although the protein is also annotated with a second activity, that reaction is not listed as a choice."
  },
  "important_caveats": [
    "The evidence is a database annotation tied to experimental evidence codes and cited publications; the primary papers were not independently reviewed here.",
    "The exact source snapshot used by the author is unknown, though the sequence matches both the current and checked historical entries."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt C6KT66 (AROC_PLAF7, Plasmodium falciparum chorismate synthase) exactly (527 aa, SHA-256 match confirmed in both current and historical snapshots). The UniProt entry explicitly annotates catalytic activity EC 4.2.3.5 as '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' with experimental evidence codes ECO:0000269 from PubMed:11298276 and PubMed:31381947. The expected answer text matches the UniProt reaction annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue by elimination: the sequence lacks a recognizable GNAT/MYST acetyltransferase fold (option C), lacks the characteristic aldehyde dehydrogenase catalytic Cys-His-Glu triad in a dehydrogenase scaffold (option B), and lacks a Rieske-type &#91;2Fe-2S&#93; cluster-binding motif expected for a ferredoxin-dependent monooxygenase (option D). However, this negative reasoning does not constitute a positive identification of chorismate synthase.


**Missing item-specific fact**

> Chorismate synthase (EC 4.2.3.5) has a unique α/β-barrel fold with no widely-recognized catalytic sequence motif analogous to, e.g., a kinase VAIK motif or a Rieske CxxH motif. Positively identifying this enzyme from a 527-aa sequence without database lookup or memorization of the specific PfCS sequence/fold is not feasible through general biological reasoning. The item requires recognition of this particular protein's identity.


**Reason**

> The sequence provides no easily identifiable catalytic signature that would allow a biologist to positively assign chorismate synthase activity without prior knowledge of this specific protein or database access. While absence of motifs for options B, C, and D provides weak negative evidence, chorismate synthase lacks a distinctive sequence motif that would serve as a positive identifier. Selection of A depends on knowing or looking up that this sequence is AROC/PfCS.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry annotates a second catalytic activity (EC 1.5.1.38, FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)), this reaction is not offered among the four choices. Among the provided options, only A corresponds to an annotated activity of this protein. The distractors (B, C, D) correspond to unrelated enzyme classes not associated with this sequence.


### Important caveats

- The UniProt entry documents this enzyme as bifunctional (EC 4.2.3.5 and EC 1.5.1.38). The question asks for 'the' catalytic activity but only one of the two annotated activities appears among the choices, so the question is answerable as posed.
- The identity of the protein (accession C6KT66) was inferred from dataset metadata and is reviewer-only; the evaluated model received only the raw sequence with no organism or accession hint.
- The annotation for EC 4.2.3.5 carries experimental evidence codes (ECO:0000269) from two independent publications, making it a well-supported annotation rather than a purely computational prediction.
- The historical entry (version 89, released 2026-01-28) already contained both catalytic activity annotations, so the bifunctional nature was known at the approximate benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks a recognizable GNAT/MYST acetyltransferase fold (option C), lacks the characteristic aldehyde dehydrogenase catalytic Cys-His-Glu triad in a dehydrogenase scaffold (option B), and lacks a Rieske-type [2Fe-2S] cluster-binding motif expected for a ferredoxin-dependent monooxygenase (option D). However, this negative reasoning does not constitute a positive identification of chorismate synthase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Chorismate synthase (EC 4.2.3.5) has a unique α/β-barrel fold with no widely-recognized catalytic sequence motif analogous to, e.g., a kinase VAIK motif or a Rieske CxxH motif. Positively identifying this enzyme from a 527-aa sequence without database lookup or memorization of the specific PfCS sequence/fold is not feasible through general biological reasoning. The item requires recognition of this particular protein's identity.",
    "reason": "The sequence provides no easily identifiable catalytic signature that would allow a biologist to positively assign chorismate synthase activity without prior knowledge of this specific protein or database access. While absence of motifs for options B, C, and D provides weak negative evidence, chorismate synthase lacks a distinctive sequence motif that would serve as a positive identifier. Selection of A depends on knowing or looking up that this sequence is AROC/PfCS."
  },
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt C6KT66 (AROC_PLAF7, Plasmodium falciparum chorismate synthase) exactly (527 aa, SHA-256 match confirmed in both current and historical snapshots). The UniProt entry explicitly annotates catalytic activity EC 4.2.3.5 as '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' with experimental evidence codes ECO:0000269 from PubMed:11298276 and PubMed:31381947. The expected answer text matches the UniProt reaction annotation verbatim."
  },
  "important_caveats": [
    "The UniProt entry documents this enzyme as bifunctional (EC 4.2.3.5 and EC 1.5.1.38). The question asks for 'the' catalytic activity but only one of the two annotated activities appears among the choices, so the question is answerable as posed.",
    "The identity of the protein (accession C6KT66) was inferred from dataset metadata and is reviewer-only; the evaluated model received only the raw sequence with no organism or accession hint.",
    "The annotation for EC 4.2.3.5 carries experimental evidence codes (ECO:0000269) from two independent publications, making it a well-supported annotation rather than a purely computational prediction.",
    "The historical entry (version 89, released 2026-01-28) already contained both catalytic activity annotations, so the bifunctional nature was known at the approximate benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates a second catalytic activity (EC 1.5.1.38, FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)), this reaction is not offered among the four choices. Among the provided options, only A corresponds to an annotated activity of this protein. The distractors (B, C, D) correspond to unrelated enzyme classes not associated with this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt C6KT66 (AROC_PLAF7, Plasmodium falciparum chorismate synthase) exactly (527 aa, SHA-256 match confirmed in both current and historical snapshots). The UniProt entry explicitly annotates catalytic activity EC 4.2.3.5 as '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' with experimental evidence codes ECO:0000269 from PubMed:11298276 and PubMed:31381947. The expected answer text matches the UniProt reaction annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue by elimination: the sequence lacks a recognizable GNAT/MYST acetyltransferase fold (option C), lacks the characteristic aldehyde dehydrogenase catalytic Cys-His-Glu triad in a dehydrogenase scaffold (option B), and lacks a Rieske-type [2Fe-2S] cluster-binding motif expected for a ferredoxin-dependent monooxygenase (option D). However, this negative reasoning does not constitute a positive identification of chorismate synthase.",
    "missing_item_specific_fact": "Chorismate synthase (EC 4.2.3.5) has a unique α/β-barrel fold with no widely-recognized catalytic sequence motif analogous to, e.g., a kinase VAIK motif or a Rieske CxxH motif. Positively identifying this enzyme from a 527-aa sequence without database lookup or memorization of the specific PfCS sequence/fold is not feasible through general biological reasoning. The item requires recognition of this particular protein's identity.",
    "reason": "The sequence provides no easily identifiable catalytic signature that would allow a biologist to positively assign chorismate synthase activity without prior knowledge of this specific protein or database access. While absence of motifs for options B, C, and D provides weak negative evidence, chorismate synthase lacks a distinctive sequence motif that would serve as a positive identifier. Selection of A depends on knowing or looking up that this sequence is AROC/PfCS."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates a second catalytic activity (EC 1.5.1.38, FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)), this reaction is not offered among the four choices. Among the provided options, only A corresponds to an annotated activity of this protein. The distractors (B, C, D) correspond to unrelated enzyme classes not associated with this sequence."
  },
  "important_caveats": [
    "The UniProt entry documents this enzyme as bifunctional (EC 4.2.3.5 and EC 1.5.1.38). The question asks for 'the' catalytic activity but only one of the two annotated activities appears among the choices, so the question is answerable as posed.",
    "The identity of the protein (accession C6KT66) was inferred from dataset metadata and is reviewer-only; the evaluated model received only the raw sequence with no organism or accession hint.",
    "The annotation for EC 4.2.3.5 carries experimental evidence codes (ECO:0000269) from two independent publications, making it a well-supported annotation rather than a purely computational prediction.",
    "The historical entry (version 89, released 2026-01-28) already contained both catalytic activity annotations, so the bifunctional nature was known at the approximate benchmark construction time."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry annotates the reaction in A as catalytic activity and cites experimental evidence (ECO:0000269). This supports the key, although the cited studies were not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is recognizable as belonging to the chorismate-synthase family through transferable sequence-family knowledge. Chorismate synthase catalyzes the shikimate-pathway conversion of 5-O-(1-carboxyvinyl)-3-phosphoshikimate to chorismate with phosphate release, matching A. The other options describe unrelated enzyme activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and knowledge of the conserved chorismate-synthase reaction give a meaningful basis to choose A without recalling an annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the chorismate-synthase reaction among the offered choices.


### Important caveats

- The database annotation cites experimental evidence, but the primary studies were not independently validated for this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is recognizable as belonging to the chorismate-synthase family through transferable sequence-family knowledge. Chorismate synthase catalyzes the shikimate-pathway conversion of 5-O-(1-carboxyvinyl)-3-phosphoshikimate to chorismate with phosphate release, matching A. The other options describe unrelated enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of the conserved chorismate-synthase reaction give a meaningful basis to choose A without recalling an annotation for this exact protein."
  },
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity and cites experimental evidence (ECO:0000269). This supports the key, although the cited studies were not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary studies were not independently validated for this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the chorismate-synthase reaction among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the reaction in A as catalytic activity and cites experimental evidence (ECO:0000269). This supports the key, although the cited studies were not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is recognizable as belonging to the chorismate-synthase family through transferable sequence-family knowledge. Chorismate synthase catalyzes the shikimate-pathway conversion of 5-O-(1-carboxyvinyl)-3-phosphoshikimate to chorismate with phosphate release, matching A. The other options describe unrelated enzyme activities.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and knowledge of the conserved chorismate-synthase reaction give a meaningful basis to choose A without recalling an annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the chorismate-synthase reaction among the offered choices."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary studies were not independently validated for this audit."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (527 aa, SHA256 matched) corresponds to UniProt C6KT66 (AROC_PLAF7), annotated as Chorismate synthase (EC 4.2.3.5) with experimental evidence (ECO:0000269) from PubMed:11298276 and PubMed:31381947. The catalytic activity '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' is directly annotated with experimental support. The enzyme is also bifunctional (EC 1.5.1.38, FMNH2 reductase activity, ECO:0000269 PubMed:31381947), but the primary chorismate synthase reaction is the main catalytic activity and matches Choice A exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Chorismate synthase (AroC) is a well-characterized FMN-dependent enzyme in the shikimate pathway with conserved sequence motifs (e.g., the 'SGFDEN' region visible near position ~95, conserved arginine residues in the active site, and a distinctive barrel-like fold architecture). The 527-aa length is consistent with eukaryotic chorismate synthases (bacterial AroC is ~420 aa; eukaryotic versions are longer). Critically, the other three options represent structurally and mechanistically distinct enzyme superfamilies: (B) aldehyde dehydrogenase requires a Rossmann-fold NAD-binding domain and a catalytic Cys/His/Glu triad; (C) lysine acetyltransferase requires a GNAT/PCAT fold with a distinctive CoA-binding motif; (D) spheroidene monooxygenase requires Rieske-type &#91;2Fe-2S&#93; cluster-binding motifs and a carotenoid oxygenase fold. The supplied sequence lacks all of these diagnostic features while containing motifs consistent with the AroC/chorismate synthase family. Family-level knowledge from bacterial chorismate synthases (E. coli AroC, N. gonorrhoeae CS) and other eukaryotic homologs provides a credible basis to identify the conserved core and exclude the three alternative enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The chorismate synthase family is sufficiently well-characterized across bacteria, fungi, plants, and protozoa that conserved sequence motifs (FMN-binding residues, conserved arginines, the SGFDEN region, barrel-fold architecture) are transferable knowledge. The three distractor enzyme classes (aldehyde dehydrogenase, lysine acetyltransferase, carotenoid monooxygenase) have highly distinctive structural and sequence signatures (Rossmann fold, GNAT fold, Rieske cluster motifs) whose absence in the supplied sequence provides a meaningful negative filter. This constitutes legitimate family-level generalization rather than lookup of this specific Plasmodium entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four mechanistically and structurally distinct enzyme classes. The sequence lacks Rossmann-fold features (excludes B), lacks GNAT-fold/CoA-binding motifs (excludes C), and lacks Rieske-cluster/carotenoid-oxygenase signatures (excludes D), while retaining chorismate synthase-conserved motifs. The bifunctional FMNH2 reductase activity (EC 1.5.1.38) of this enzyme is not among the choices, so it does not create ambiguity.


### Important caveats

- The enzyme is bifunctional (also EC 1.5.1.38, FMNH2 + NADP+ → FMN + NADPH + 2H+), but this secondary activity is not among the offered choices and does not affect the answer.
- Plasmodium chorismate synthase is somewhat divergent from bacterial AroC; however, the conserved core motifs remain identifiable at the family level.
- The reviewer evidence confirms the sequence match and experimental annotation, but this information was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Chorismate synthase (AroC) is a well-characterized FMN-dependent enzyme in the shikimate pathway with conserved sequence motifs (e.g., the 'SGFDEN' region visible near position ~95, conserved arginine residues in the active site, and a distinctive barrel-like fold architecture). The 527-aa length is consistent with eukaryotic chorismate synthases (bacterial AroC is ~420 aa; eukaryotic versions are longer). Critically, the other three options represent structurally and mechanistically distinct enzyme superfamilies: (B) aldehyde dehydrogenase requires a Rossmann-fold NAD-binding domain and a catalytic Cys/His/Glu triad; (C) lysine acetyltransferase requires a GNAT/PCAT fold with a distinctive CoA-binding motif; (D) spheroidene monooxygenase requires Rieske-type [2Fe-2S] cluster-binding motifs and a carotenoid oxygenase fold. The supplied sequence lacks all of these diagnostic features while containing motifs consistent with the AroC/chorismate synthase family. Family-level knowledge from bacterial chorismate synthases (E. coli AroC, N. gonorrhoeae CS) and other eukaryotic homologs provides a credible basis to identify the conserved core and exclude the three alternative enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The chorismate synthase family is sufficiently well-characterized across bacteria, fungi, plants, and protozoa that conserved sequence motifs (FMN-binding residues, conserved arginines, the SGFDEN region, barrel-fold architecture) are transferable knowledge. The three distractor enzyme classes (aldehyde dehydrogenase, lysine acetyltransferase, carotenoid monooxygenase) have highly distinctive structural and sequence signatures (Rossmann fold, GNAT fold, Rieske cluster motifs) whose absence in the supplied sequence provides a meaningful negative filter. This constitutes legitimate family-level generalization rather than lookup of this specific Plasmodium entry."
  },
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence (527 aa, SHA256 matched) corresponds to UniProt C6KT66 (AROC_PLAF7), annotated as Chorismate synthase (EC 4.2.3.5) with experimental evidence (ECO:0000269) from PubMed:11298276 and PubMed:31381947. The catalytic activity '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' is directly annotated with experimental support. The enzyme is also bifunctional (EC 1.5.1.38, FMNH2 reductase activity, ECO:0000269 PubMed:31381947), but the primary chorismate synthase reaction is the main catalytic activity and matches Choice A exactly."
  },
  "important_caveats": [
    "The enzyme is bifunctional (also EC 1.5.1.38, FMNH2 + NADP+ → FMN + NADPH + 2H+), but this secondary activity is not among the offered choices and does not affect the answer.",
    "Plasmodium chorismate synthase is somewhat divergent from bacterial AroC; however, the conserved core motifs remain identifiable at the family level.",
    "The reviewer evidence confirms the sequence match and experimental annotation, but this information was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four mechanistically and structurally distinct enzyme classes. The sequence lacks Rossmann-fold features (excludes B), lacks GNAT-fold/CoA-binding motifs (excludes C), and lacks Rieske-cluster/carotenoid-oxygenase signatures (excludes D), while retaining chorismate synthase-conserved motifs. The bifunctional FMNH2 reductase activity (EC 1.5.1.38) of this enzyme is not among the choices, so it does not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (527 aa, SHA256 matched) corresponds to UniProt C6KT66 (AROC_PLAF7), annotated as Chorismate synthase (EC 4.2.3.5) with experimental evidence (ECO:0000269) from PubMed:11298276 and PubMed:31381947. The catalytic activity '5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate' is directly annotated with experimental support. The enzyme is also bifunctional (EC 1.5.1.38, FMNH2 reductase activity, ECO:0000269 PubMed:31381947), but the primary chorismate synthase reaction is the main catalytic activity and matches Choice A exactly.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Chorismate synthase (AroC) is a well-characterized FMN-dependent enzyme in the shikimate pathway with conserved sequence motifs (e.g., the 'SGFDEN' region visible near position ~95, conserved arginine residues in the active site, and a distinctive barrel-like fold architecture). The 527-aa length is consistent with eukaryotic chorismate synthases (bacterial AroC is ~420 aa; eukaryotic versions are longer). Critically, the other three options represent structurally and mechanistically distinct enzyme superfamilies: (B) aldehyde dehydrogenase requires a Rossmann-fold NAD-binding domain and a catalytic Cys/His/Glu triad; (C) lysine acetyltransferase requires a GNAT/PCAT fold with a distinctive CoA-binding motif; (D) spheroidene monooxygenase requires Rieske-type [2Fe-2S] cluster-binding motifs and a carotenoid oxygenase fold. The supplied sequence lacks all of these diagnostic features while containing motifs consistent with the AroC/chorismate synthase family. Family-level knowledge from bacterial chorismate synthases (E. coli AroC, N. gonorrhoeae CS) and other eukaryotic homologs provides a credible basis to identify the conserved core and exclude the three alternative enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The chorismate synthase family is sufficiently well-characterized across bacteria, fungi, plants, and protozoa that conserved sequence motifs (FMN-binding residues, conserved arginines, the SGFDEN region, barrel-fold architecture) are transferable knowledge. The three distractor enzyme classes (aldehyde dehydrogenase, lysine acetyltransferase, carotenoid monooxygenase) have highly distinctive structural and sequence signatures (Rossmann fold, GNAT fold, Rieske cluster motifs) whose absence in the supplied sequence provides a meaningful negative filter. This constitutes legitimate family-level generalization rather than lookup of this specific Plasmodium entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four mechanistically and structurally distinct enzyme classes. The sequence lacks Rossmann-fold features (excludes B), lacks GNAT-fold/CoA-binding motifs (excludes C), and lacks Rieske-cluster/carotenoid-oxygenase signatures (excludes D), while retaining chorismate synthase-conserved motifs. The bifunctional FMNH2 reductase activity (EC 1.5.1.38) of this enzyme is not among the choices, so it does not create ambiguity."
  },
  "important_caveats": [
    "The enzyme is bifunctional (also EC 1.5.1.38, FMNH2 + NADP+ → FMN + NADPH + 2H+), but this secondary activity is not among the offered choices and does not affect the answer.",
    "Plasmodium chorismate synthase is somewhat divergent from bacterial AroC; however, the conserved core motifs remain identifiable at the family level.",
    "The reviewer evidence confirms the sequence match and experimental annotation, but this information was not available to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "C6KT66",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "benchmark_sequence_length": 527,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "current_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_source_sequence_length": 527,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 89,
  "selected_historical_version": {
    "accession": "C6KT66",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AROC_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "selected_historical_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "selected_historical_source_sequence_length": 527,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"C6KT66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"value\":\"PfCS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21021\"}}],\"reaction\":{\"ecNumber\":\"4.2.3.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21020\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57701\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21626\"}}],\"reaction\":{\"ecNumber\":\"1.5.1.38\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21624\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Fitzpatrick T.\",\"Ricken S.\",\"Lanzer M.\",\"Amrhein N.\",\"Macheroux P.\",\"Kappes B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11298276\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.2001.02366.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"65\",\"id\":\"11298276\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"75\",\"publicationDate\":\"2001\",\"title\":\"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"DD2\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   AROC_PLAF7              Reviewed;         527 AA.\nAC   C6KT66;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};\nGN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 50-58",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};\nRX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;\nRA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;\nRT   \"Subcellular localization and characterization of chorismate synthase in\nRT   the apicomplexan Plasmodium falciparum.\";\nRL   Mol. Microbiol. 40:65-75(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 59-64",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 72-78",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +\nCC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;\nCC         Evidence={ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 79-85",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMNH2 + NADP(+) = FMN + NADPH + 2 H(+); Xref=Rhea:RHEA:21624,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57618, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58349; EC=1.5.1.38;\nCC         Evidence={ECO:0000269|PubMed:31381947};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:21626;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
