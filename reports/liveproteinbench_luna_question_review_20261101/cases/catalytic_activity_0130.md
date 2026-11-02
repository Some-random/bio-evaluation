# catalytic_activity_0130

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed UniProt entry for this protein, which records the reaction in choice A with experimental evidence codes and supporting publications. The archived annotation also contains that reaction. The annotation additionally records another catalytic activity, but that reaction is not among the choices.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or recognizable functional label that identifies which reaction this particular protein catalyzes. General biological knowledge alone does not establish the exact sequence-to-function match.

**Missing item-specific fact**

> The protein-specific identification as Plasmodium falciparum chorismate synthase and its experimentally supported catalytic activity are needed to select choice A.

**Reason**

> A sequence-to-function database lookup, prior knowledge of this specific protein, or experimental characterization is needed. Simply recognizing the sequence or asserting that a predictor could classify it would not make the answer reasoning-supported.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Choice A is supported among the listed options. Although the protein is also annotated with a second activity, that reaction is not listed as a choice.

### Important caveats

- The evidence is a database annotation tied to experimental evidence codes and cited publications; the primary papers were not independently reviewed here.
- The exact source snapshot used by the author is unknown, though the sequence matches both the current and checked historical entries.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for this protein, which records the reaction in choice A with experimental evidence codes and supporting publications. The archived annotation also contains that reaction. The annotation additionally records another catalytic activity, but that reaction is not among the choices.",
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `C6KT66`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 89. The exact author source snapshot remains unknown.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 130). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
