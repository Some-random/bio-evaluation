# EC_number_0094

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.4.2.14

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. 2.4.1.392
B. 1.14.15.37
C. 2.4.2.14
D. 4.4.1.11
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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14. The annotation cites experimental evidence, and the catalytic-activity annotation specifies the corresponding reaction.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glutamine amidotransferase domain (including an N-terminal catalytic cysteine) coupled to a phosphoribosyltransferase domain. That combination supports a glutamine-dependent phosphoribosyl transfer reaction and distinguishes choice C from the unrelated oxidoreductase and lyase options and the other glycosyltransferase option.

**Missing item-specific fact**

> No essential item-specific fact is needed to distinguish these choices by the sequence-based functional inference, although direct reaction evidence would be needed to confirm the exact EC annotation independently.

**Reason**

> The sequence provides a concrete domain and catalytic-residue basis for inferring the enzyme class and selecting the matching listed EC number; this is more than remembering a database entry.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The sequence features support the phosphoribosyl amidotransferase option, while the other choices describe different enzyme classes.

### Important caveats

- The supporting UniProt annotations are reviewer-only and were not part of the original input.
- The matched database annotation cites experimental evidence, but the primary paper was not independently reviewed here.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14. The annotation cites experimental evidence, and the catalytic-activity annotation specifies the corresponding reaction.",
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glutamine amidotransferase domain (including an N-terminal catalytic cysteine) coupled to a phosphoribosyltransferase domain. That combination supports a glutamine-dependent phosphoribosyl transfer reaction and distinguishes choice C from the unrelated oxidoreductase and lyase options and the other glycosyltransferase option.",
    "missing_item_specific_fact": "No essential item-specific fact is needed to distinguish these choices by the sequence-based functional inference, although direct reaction evidence would be needed to confirm the exact EC annotation independently.",
    "reason": "The sequence provides a concrete domain and catalytic-residue basis for inferring the enzyme class and selecting the matching listed EC number; this is more than remembering a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features support the phosphoribosyl amidotransferase option, while the other choices describe different enzyme classes."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not part of the original input.",
    "The matched database annotation cites experimental evidence, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A7T8J1U7`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 16. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis clusters protein K"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Glutamine phosphoribosylpyrophosphate amidotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.4.2.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Phosphoribosylpyrophosphate amidotransferase FrzK"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"ATase FrzK"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14907"}}],"reaction":{"ecNumber":"2.4.2.14","evidences":[{"evidenceCode":"ECO:0000305","id":"33372776","source":"PubMed"}],"name":"5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14905"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29985"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:58017"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:58681"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
DE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};
DE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};
DE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};
DE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-
CC         phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O;
CC         Xref=Rhea:RHEA:14905, ChEBI:CHEBI:15377, ChEBI:CHEBI:29985,
CC         ChEBI:CHEBI:33019, ChEBI:CHEBI:58017, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:58681; EC=2.4.2.14;
CC         Evidence={ECO:0000305|PubMed:33372776};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:14907;
CC         Evidence={ECO:0000305|PubMed:33372776};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 94). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
