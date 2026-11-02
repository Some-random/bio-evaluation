# GO_molecular_function_0030

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| contradicted | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MPISIPKGEKLMDLLSMKGKVTIVTGASGPRGMGIEAARGIAEMGGNVALTYAGRKEGGEKNAAALEKEYGIKAKAYKLDVANYESCCQLVKDVIADFGQIDAFVANAGKTADSGVLDGEISAFEEVIQTDLLGVAYCAKAVGHHFKERQTGSFVITASMSGHIANFPQEQTSYNVAKAGCIHMARSLANEWRDFARVNSISPGYIDTGLSDFVDKETQKLWHSMIPMGRDGDAKELKAAYVYFCSDASTYTTGSDLVIDGGYCAR

[Multiple Choices]
A. glycolipid mannosyltransferase activity
B. transcription coregulator activity
C. cysteine desulfurase activity
D. oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The exact sequence match is annotated as an NADP-dependent mannitol dehydrogenase, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). That reaction uses NADP(+) as the electron acceptor, not oxygen as required by option D. The D-term annotation is computational (IEA:TreeGrafter), whereas the cited catalytic activity has ECO:0000305 evidence.

Cited evidence: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich sequence is compatible with a nucleotide-binding oxidoreductase, making an enzyme more plausible than a transcription coregulator. But that general clue does not establish oxygen as the acceptor or distinguish the protein's actual substrate-specific activity.

**Missing item-specific fact**

> The protein-specific catalytic reaction: mannitol/fructose interconversion with NADP(+)/NADPH, rather than an oxygen-accepting NAD(P)H oxidoreductase reaction.

**Reason**

> The sequence alone does not supply enough evidence for the precise acceptor specified in D. Identifying the enzyme's reaction requires protein-specific functional information; moreover, the characterized reaction does not match D's wording.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> None of the options accurately states the supported mannitol dehydrogenase activity. D is broadly oxidoreductase-related, but its oxygen-acceptor specification conflicts with the reported NADP-dependent reaction; A, B, and C do not describe that reaction.

### Important caveats

- The reviewer-only UniProt records match the supplied 266-aa sequence, but the author's exact source snapshot is unknown.
- The catalytic reaction evidence is cited to a publication but was not independently checked here; the GO annotation supporting D is explicitly computational.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0030",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact sequence match is annotated as an NADP-dependent mannitol dehydrogenase, catalyzing D-mannitol + NADP(+) = D-fructose + NADPH + H(+). That reaction uses NADP(+) as the electron acceptor, not oxygen as required by option D. The D-term annotation is computational (IEA:TreeGrafter), whereas the cited catalytic activity has ECO:0000305 evidence.",
    "evidence_ids": [
      "C4",
      "C6",
      "C8",
      "H4",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with a nucleotide-binding oxidoreductase, making an enzyme more plausible than a transcription coregulator. But that general clue does not establish oxygen as the acceptor or distinguish the protein's actual substrate-specific activity.",
    "missing_item_specific_fact": "The protein-specific catalytic reaction: mannitol/fructose interconversion with NADP(+)/NADPH, rather than an oxygen-accepting NAD(P)H oxidoreductase reaction.",
    "reason": "The sequence alone does not supply enough evidence for the precise acceptor specified in D. Identifying the enzyme's reaction requires protein-specific functional information; moreover, the characterized reaction does not match D's wording."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the options accurately states the supported mannitol dehydrogenase activity. D is broadly oxidoreductase-related, but its oxygen-acceptor specification conflicts with the reported NADP-dependent reaction; A, B, and C do not describe that reaction."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied 266-aa sequence, but the author's exact source snapshot is unknown.",
    "The catalytic reaction evidence is cited to a publication but was not independently checked here; the GO annotation supporting D is explicitly computational."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C6/H4 describe mannitol plus NADP+ yielding fructose plus NADPH, while C8/H6 carry the oxygen-acceptor term via IEA:TreeGrafter.

**Remaining uncertainty:** The cited reaction is ECO:0000305 and reversible; neither direction uses oxygen as acceptor. Additional oxidase activity is not exhaustively tested by these excerpts.

Evidence checked: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A223HDI5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 15. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"}],"value":"1.1.1.138"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"NADP-dependent mannitol dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MtDH"}]}}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16766"}},{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16767"}}],"reaction":{"ecNumber":"1.1.1.138","evidences":[{"evidenceCode":"ECO:0000305","id":"32003433","source":"PubMed"}],"name":"D-mannitol + NADP(+) = D-fructose + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16765"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16899"},{"database":"ChEBI","id":"CHEBI:37721"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI5.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.241345+00:00.  

```json
{"database":"GO","id":"GO:0050664","properties":[{"key":"GoTerm","value":"F:oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `c6aa71c90f5754236176b13ca1a049caba09e755d0ca2e57921409a1d945c654`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol + NADP(+) = D-fructose + NADPH + H(+);
CC         Xref=Rhea:RHEA:16765, ChEBI:CHEBI:15378, ChEBI:CHEBI:16899,
CC         ChEBI:CHEBI:37721, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.1.1.138; Evidence={ECO:0000305|PubMed:32003433};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16766;
CC         Evidence={ECO:0000305|PubMed:32003433};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:16767;
CC         Evidence={ECO:0000305|PubMed:32003433};
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI5?format=txt&versions=15)  
**Locator:** `lines 84-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.627063+00:00.  

```text
DR   GO; GO:0050664; F:oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor; IEA:TreeGrafter.
```

Source SHA-256: `cd858973dafcf9f7eafcc69467bc9fac51732b2bdf6281c7e18de2db9ff34dd6`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 30). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
