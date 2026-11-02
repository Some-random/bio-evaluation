# catalytic_activity_0130

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `C6KT66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 89. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
"C6KT66"
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"31381947","source":"PubMed"}],"value":"1.5.1.38"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"4.2.3.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"31381947","source":"PubMed"}],"value":"Chorismate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"value":"PfCS"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21021"}}],"reaction":{"ecNumber":"4.2.3.5","evidences":[{"evidenceCode":"ECO:0000269","id":"11298276","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"name":"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21020"},{"database":"ChEBI","id":"CHEBI:29748"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57701"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21626"}}],"reaction":{"ecNumber":"1.5.1.38","evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"name":"FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21624"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"citation":{"authors":["Fitzpatrick T.","Ricken S.","Lanzer M.","Amrhein N.","Macheroux P.","Kappes B."],"citationCrossReferences":[{"database":"PubMed","id":"11298276"},{"database":"DOI","id":"10.1046/j.1365-2958.2001.02366.x"}],"citationType":"journal article","firstPage":"65","id":"11298276","journal":"Mol. Microbiol.","lastPage":"75","publicationDate":"2001","title":"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.","volume":"40"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11298276","source":"PubMed"}],"type":"STRAIN","value":"DD2"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.463877+00:00.  

```json
{"citation":{"authors":["Khera H.K.","Singh S.K.","Singh S."],"citationCrossReferences":[{"database":"PubMed","id":"31381947"},{"database":"DOI","id":"10.1016/j.molbiopara.2019.111202"}],"citationType":"journal article","firstPage":"111202","id":"31381947","journal":"Mol. Biochem. Parasitol.","lastPage":"111202","publicationDate":"2019","title":"Chorismate synthase from malaria parasites is bifunctional enzyme.","volume":"233"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
ID   AROC_PLAF7              Reviewed;         527 AA.
AC   C6KT66;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-SEP-2009, sequence version 1.
DT   28-JAN-2026, entry version 89.
DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};
DE            Short=PfCS {ECO:0000303|PubMed:11298276};
DE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};
DE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};
GN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};
GN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
DE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};
DE            Short=PfCS {ECO:0000303|PubMed:11298276};
DE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};
DE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 50-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL
RP   STAGE.
RC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};
RX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;
RA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;
RT   "Subcellular localization and characterization of chorismate synthase in
RT   the apicomplexan Plasmodium falciparum.";
RL   Mol. Microbiol. 40:65-75(2001).
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 59-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;
RA   Khera H.K., Singh S.K., Singh S.;
RT   "Chorismate synthase from malaria parasites is bifunctional enzyme.";
RL   Mol. Biochem. Parasitol. 233:111202-111202(2019).
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 72-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +
CC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;
CC         Evidence={ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)  
**Locator:** `lines 79-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 89 / 1.  
**Retrieved:** 2026-11-02T04:27:34.407274+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=FMNH2 + NADP(+) = FMN + NADPH + 2 H(+); Xref=Rhea:RHEA:21624,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57618, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58349; EC=1.5.1.38;
CC         Evidence={ECO:0000269|PubMed:31381947};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:21626;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
