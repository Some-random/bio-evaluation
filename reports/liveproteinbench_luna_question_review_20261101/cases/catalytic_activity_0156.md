# catalytic_activity_0156

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. L-tyrosine + reduced [NADPH--hemoprotein reductase] + O2 = L-dopa + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
B. (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)
D. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
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

> The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.

**Missing item-specific fact**

> The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.

**Reason**

> Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction.

### Important caveats

- The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.",
    "missing_item_specific_fact": "The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.",
    "reason": "Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A223HDH4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 15. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
"A0A223HDH4"
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"value":"1.1.1.17"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Mannitol-1-phosphate 5-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MPDH"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.17","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"name":"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19661"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57634"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:61381"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
ID   MPDH_AURME              Reviewed;         386 AA.
AC   A0A223HDH4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-OCT-2017, sequence version 1.
DT   28-JAN-2026, entry version 15.
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 53-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate
CC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:61381; EC=1.1.1.17;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 156). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
