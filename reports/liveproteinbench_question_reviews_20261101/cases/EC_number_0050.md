# EC_number_0050

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.6.1.74

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPKSFRDNLAEILKTHDFRTVELEFRLGFQAPGEFITNINKHVWTTAKEKLGTPAQELVMVDKYIRSTPGESSRYVVFPDGQGYWEHKKKVAKETTTGGKYGVRSAFSLERRENGKPPVSFRMQRTKYRTTFVKGPWKIDFTRVESIPATDRDCESTYEIEVELYDMFYLFEKELDIIIQEGNKLVQSIVM

[Multiple Choices]
A. 3.6.1.5
B. 3.6.1.74
C. 1.5.1.38
D. 1.1.1.138
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

> The exact sequence matches the UniProt entry annotated as EC 3.6.1.74, and the catalytic-activity annotation cites experimental evidence for the RNA triphosphatase reaction. The source snapshot used by the author is unknown, but the historical and current records support the key.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, generally interpretable feature that distinguishes the specific EC 3.6.1.74 activity from the other listed enzyme classifications.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this viral protein catalyzes RNA 5′-triphosphate hydrolysis.


**Reason**

> Identifying the exact viral protein or recalling its annotation would select B, but that item-specific fact is not supplied. A possible prediction from sequence is not itself a concrete discriminating argument available from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B for the matched sequence; no evidence supports another listed option.


### Important caveats

- The accession and database evidence are reviewer-only and were absent from the evaluated model input.
- The UniProt annotation cites a publication with experimental evidence, but the primary paper was not independently reviewed here.
- The exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear, generally interpretable feature that distinguishes the specific EC 3.6.1.74 activity from the other listed enzyme classifications.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this viral protein catalyzes RNA 5′-triphosphate hydrolysis.",
    "reason": "Identifying the exact viral protein or recalling its annotation would select B, but that item-specific fact is not supplied. A possible prediction from sequence is not itself a concrete discriminating argument available from the input."
  },
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.6.1.74, and the catalytic-activity annotation cites experimental evidence for the RNA triphosphatase reaction. The source snapshot used by the author is unknown, but the historical and current records support the key."
  },
  "important_caveats": [
    "The accession and database evidence are reviewer-only and were absent from the evaluated model input.",
    "The UniProt annotation cites a publication with experimental evidence, but the primary paper was not independently reviewed here.",
    "The exact source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B for the matched sequence; no evidence supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 3.6.1.74, and the catalytic-activity annotation cites experimental evidence for the RNA triphosphatase reaction. The source snapshot used by the author is unknown, but the historical and current records support the key.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, generally interpretable feature that distinguishes the specific EC 3.6.1.74 activity from the other listed enzyme classifications.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this viral protein catalyzes RNA 5′-triphosphate hydrolysis.",
    "reason": "Identifying the exact viral protein or recalling its annotation would select B, but that item-specific fact is not supplied. A possible prediction from sequence is not itself a concrete discriminating argument available from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B for the matched sequence; no evidence supports another listed option."
  },
  "important_caveats": [
    "The accession and database evidence are reviewer-only and were absent from the evaluated model input.",
    "The UniProt annotation cites a publication with experimental evidence, but the primary paper was not independently reviewed here.",
    "The exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (193 AA) exactly matches UniProt Q98500 (TPASE_PBCV1, A449R from PBCV-1). UniProt annotates this protein as 5'RNA triphosphatase with EC 3.6.1.74, supported by experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction (5'-triphospho-ribonucleoside in mRNA + H2O → 5'-diphospho-ribonucleoside in mRNA + phosphate + H+) is consistent with EC 3.6.1.74. Both current and archived (entry v85) records confirm the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue against options C and D (oxidoreductases, EC 1.x.x.x) because the 193-residue sequence lacks obvious Rossmann-fold or other canonical oxidoreductase cofactor-binding motifs, and the viral context (large DNA virus encoding its own capping machinery) is more consistent with a hydrolase. However, this only narrows the choice to A vs. B, both of which are phosphatases (EC 3.6.1.x) acting on phosphoanhydride bonds. Distinguishing 3.6.1.5 (nucleoside diphosphate phosphatase, acts on free NDP) from 3.6.1.74 (5'RNA triphosphatase, acts on the 5'-triphosphate terminus of RNA) requires knowledge of the specific substrate target (free nucleotide vs. RNA 5'-end) and the viral mRNA-capping context, neither of which is encoded in recognizable sequence motifs within this 193-aa protein.


**Missing item-specific fact**

> The specific identification of this protein as the PBCV-1 A449R 5'RNA triphosphatase component of the viral mRNA capping apparatus, including its substrate specificity for the 5'-triphosphate end of RNA rather than free nucleoside diphosphates. No general sequence motif distinguishes EC 3.6.1.74 from EC 3.6.1.5 in this short viral protein.


**Reason**

> Selecting B over A requires recognizing this exact protein as a viral mRNA-capping triphosphatase or recalling its specific annotation. The sequence provides no catalytic motif or structural feature that a knowledgeable biologist could use to reason from first principles that this enzyme acts on the 5'-triphosphate end of RNA rather than on free nucleoside diphosphates. This is a protein-specific functional annotation, not a deduction from general enzyme chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 3.6.1.5 and 3.6.1.74 are phosphatases acting on phosphoanhydride bonds (EC subclass 3.6.1). Without the specific knowledge that this viral protein targets the 5'-triphosphate end of RNA (rather than free NDPs), a model or expert could reasonably argue for either A or B based solely on sequence. Options C and D (oxidoreductases) are weaker distractors because the sequence lacks typical oxidoreductase cofactor motifs, but they are not impossible from sequence alone.


### Important caveats

- The EC 3.6.1.74 annotation is backed by experimental evidence (PubMed:11160672, Ho/Gong/Shuman 2001, J. Virol.), not merely computational transfer.
- The sequence-to-accession match (Q98500) was established by reviewer-only metadata; the evaluated model received only the raw sequence.
- The protein is only 193 residues and lacks any widely-recognized, unique catalytic motif that would unambiguously signal '5'RNA triphosphatase' to a general biologist.
- The first public date of the UniProt entry is 2025-04-09, meaning this annotation may not have existed at the time the benchmark was constructed, depending on the author's data snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue against options C and D (oxidoreductases, EC 1.x.x.x) because the 193-residue sequence lacks obvious Rossmann-fold or other canonical oxidoreductase cofactor-binding motifs, and the viral context (large DNA virus encoding its own capping machinery) is more consistent with a hydrolase. However, this only narrows the choice to A vs. B, both of which are phosphatases (EC 3.6.1.x) acting on phosphoanhydride bonds. Distinguishing 3.6.1.5 (nucleoside diphosphate phosphatase, acts on free NDP) from 3.6.1.74 (5'RNA triphosphatase, acts on the 5'-triphosphate terminus of RNA) requires knowledge of the specific substrate target (free nucleotide vs. RNA 5'-end) and the viral mRNA-capping context, neither of which is encoded in recognizable sequence motifs within this 193-aa protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this protein as the PBCV-1 A449R 5'RNA triphosphatase component of the viral mRNA capping apparatus, including its substrate specificity for the 5'-triphosphate end of RNA rather than free nucleoside diphosphates. No general sequence motif distinguishes EC 3.6.1.74 from EC 3.6.1.5 in this short viral protein.",
    "reason": "Selecting B over A requires recognizing this exact protein as a viral mRNA-capping triphosphatase or recalling its specific annotation. The sequence provides no catalytic motif or structural feature that a knowledgeable biologist could use to reason from first principles that this enzyme acts on the 5'-triphosphate end of RNA rather than on free nucleoside diphosphates. This is a protein-specific functional annotation, not a deduction from general enzyme chemistry."
  },
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (193 AA) exactly matches UniProt Q98500 (TPASE_PBCV1, A449R from PBCV-1). UniProt annotates this protein as 5'RNA triphosphatase with EC 3.6.1.74, supported by experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction (5'-triphospho-ribonucleoside in mRNA + H2O → 5'-diphospho-ribonucleoside in mRNA + phosphate + H+) is consistent with EC 3.6.1.74. Both current and archived (entry v85) records confirm the annotation."
  },
  "important_caveats": [
    "The EC 3.6.1.74 annotation is backed by experimental evidence (PubMed:11160672, Ho/Gong/Shuman 2001, J. Virol.), not merely computational transfer.",
    "The sequence-to-accession match (Q98500) was established by reviewer-only metadata; the evaluated model received only the raw sequence.",
    "The protein is only 193 residues and lacks any widely-recognized, unique catalytic motif that would unambiguously signal '5'RNA triphosphatase' to a general biologist.",
    "The first public date of the UniProt entry is 2025-04-09, meaning this annotation may not have existed at the time the benchmark was constructed, depending on the author's data snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 3.6.1.5 and 3.6.1.74 are phosphatases acting on phosphoanhydride bonds (EC subclass 3.6.1). Without the specific knowledge that this viral protein targets the 5'-triphosphate end of RNA (rather than free NDPs), a model or expert could reasonably argue for either A or B based solely on sequence. Options C and D (oxidoreductases) are weaker distractors because the sequence lacks typical oxidoreductase cofactor motifs, but they are not impossible from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (193 AA) exactly matches UniProt Q98500 (TPASE_PBCV1, A449R from PBCV-1). UniProt annotates this protein as 5'RNA triphosphatase with EC 3.6.1.74, supported by experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction (5'-triphospho-ribonucleoside in mRNA + H2O → 5'-diphospho-ribonucleoside in mRNA + phosphate + H+) is consistent with EC 3.6.1.74. Both current and archived (entry v85) records confirm the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue against options C and D (oxidoreductases, EC 1.x.x.x) because the 193-residue sequence lacks obvious Rossmann-fold or other canonical oxidoreductase cofactor-binding motifs, and the viral context (large DNA virus encoding its own capping machinery) is more consistent with a hydrolase. However, this only narrows the choice to A vs. B, both of which are phosphatases (EC 3.6.1.x) acting on phosphoanhydride bonds. Distinguishing 3.6.1.5 (nucleoside diphosphate phosphatase, acts on free NDP) from 3.6.1.74 (5'RNA triphosphatase, acts on the 5'-triphosphate terminus of RNA) requires knowledge of the specific substrate target (free nucleotide vs. RNA 5'-end) and the viral mRNA-capping context, neither of which is encoded in recognizable sequence motifs within this 193-aa protein.",
    "missing_item_specific_fact": "The specific identification of this protein as the PBCV-1 A449R 5'RNA triphosphatase component of the viral mRNA capping apparatus, including its substrate specificity for the 5'-triphosphate end of RNA rather than free nucleoside diphosphates. No general sequence motif distinguishes EC 3.6.1.74 from EC 3.6.1.5 in this short viral protein.",
    "reason": "Selecting B over A requires recognizing this exact protein as a viral mRNA-capping triphosphatase or recalling its specific annotation. The sequence provides no catalytic motif or structural feature that a knowledgeable biologist could use to reason from first principles that this enzyme acts on the 5'-triphosphate end of RNA rather than on free nucleoside diphosphates. This is a protein-specific functional annotation, not a deduction from general enzyme chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 3.6.1.5 and 3.6.1.74 are phosphatases acting on phosphoanhydride bonds (EC subclass 3.6.1). Without the specific knowledge that this viral protein targets the 5'-triphosphate end of RNA (rather than free NDPs), a model or expert could reasonably argue for either A or B based solely on sequence. Options C and D (oxidoreductases) are weaker distractors because the sequence lacks typical oxidoreductase cofactor motifs, but they are not impossible from sequence alone."
  },
  "important_caveats": [
    "The EC 3.6.1.74 annotation is backed by experimental evidence (PubMed:11160672, Ho/Gong/Shuman 2001, J. Virol.), not merely computational transfer.",
    "The sequence-to-accession match (Q98500) was established by reviewer-only metadata; the evaluated model received only the raw sequence.",
    "The protein is only 193 residues and lacks any widely-recognized, unique catalytic motif that would unambiguously signal '5'RNA triphosphatase' to a general biologist.",
    "The first public date of the UniProt entry is 2025-04-09, meaning this annotation may not have existed at the time the benchmark was constructed, depending on the author's data snapshot."
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

**Accession:** `Q98500` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 85. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
"Q98500"
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"3.6.1.74"}],"fullName":{"value":"5'RNA triphosphatase A449R"}}}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:67005"}}],"reaction":{"ecNumber":"3.6.1.74","evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"name":"a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:67004"},{"database":"Rhea","id":"RHEA-COMP:17164"},{"database":"Rhea","id":"RHEA-COMP:17165"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:167616"},{"database":"ChEBI","id":"CHEBI:167618"}]}}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"citation":{"authors":["Ho C.K.","Gong C.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"11160672"},{"database":"DOI","id":"10.1128/jvi.75.4.1744-1750.2001"}],"citationType":"journal article","firstPage":"1744","id":"11160672","journal":"J. Virol.","lastPage":"1750","publicationDate":"2001","title":"RNA triphosphatase component of the mRNA capping apparatus of Paramecium bursaria Chlorella virus 1.","volume":"75"},"referenceNumber":2,"referencePositions":["FUNCTION","CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY","MUTAGENESIS OF GLU-26"]}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
DE   RecName: Full=5'RNA triphosphatase A449R;
DE            EC=3.6.1.74;
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 21-28`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
RN   [2]
RP   FUNCTION, CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY, AND MUTAGENESIS OF
RP   GLU-26.
RX   PubMed=11160672; DOI=10.1128/jvi.75.4.1744-1750.2001;
RA   Ho C.K., Gong C., Shuman S.;
RT   "RNA triphosphatase component of the mRNA capping apparatus of Paramecium
RT   bursaria Chlorella virus 1.";
RL   J. Virol. 75:1744-1750(2001).
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end
CC         diphospho-ribonucleoside in mRNA + phosphate + H(+);
CC         Xref=Rhea:RHEA:67004, Rhea:RHEA-COMP:17164, Rhea:RHEA-COMP:17165,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:167616, ChEBI:CHEBI:167618; EC=3.6.1.74;
CC         Evidence={ECO:0000269|PubMed:11160672};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:67005;
CC         Evidence={ECO:0000269|PubMed:11160672};
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
