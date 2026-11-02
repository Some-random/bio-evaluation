# EC_number_0088

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 6.3.5.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. 5.6.2.4
B. 2.3.1.193
C. 6.3.5.1
D. 1.14.19.80
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

> The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.


**Missing item-specific fact**

> The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.


**Reason**

> Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information.


### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.
- The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, EC 6.3.5.1, with the catalytic activity and EC assignment attributed to the HAMAP rule. This supports the key as a database-based functional annotation, but does not establish direct experimental validation of the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognition of an enzyme with glutamine-processing and ATP-dependent ligase features, favoring a ligase over the other broad EC classes. Those features alone do not establish the specific NAD-synthetase reaction required for EC 6.3.5.1.",
    "missing_item_specific_fact": "The protein-specific identification as glutamine-dependent NAD(+) synthetase, or equivalent family/domain evidence establishing its substrate and reaction, is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on identifying this particular enzyme and its reaction; the sequence and unlabeled EC choices do not state that reaction. Recognizing the sequence through an external annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports C, and the listed EC numbers are distinct classifications. No competing option is comparably supported by the supplied information."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's precise source snapshot is unknown.",
    "The EC and catalytic-activity annotation is attributed to a computational HAMAP rule; the cited paper excerpt concerns a disruption phenotype and does not itself establish direct enzymatic measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).


**Missing item-specific fact**

> Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.


**Reason**

> The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization.


### Important caveats

- The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.
- The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.
- Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.
- The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.",
    "reason": "The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge."
  },
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment."
  },
  "important_caveats": [
    "The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.",
    "The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.",
    "Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.",
    "The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H2X6L3 (NADE_XANC8) matches the benchmark sequence exactly (552 AA, SHA256 match). The entry is annotated as Glutamine-dependent NAD(+) synthetase with EC=6.3.5.1, assigned via HAMAP-Rule MF_02090 (computational/curatorial evidence code ECO:0000255). The gene name is nadE. A 2024 PubMed reference (38429435) provides DISRUPTION PHENOTYPE evidence related to NAD+ biosynthesis in Xanthomonas campestris. The catalytic reaction (deamido-NAD(+) + L-glutamine + ATP + H2O → L-glutamate + AMP + diphosphate + NAD(+) + H(+)) is consistent with EC 6.3.5.1. The annotation is primarily curatorial (HAMAP rule) rather than direct experimental, but the gene name, organism context, and disruption phenotype support the assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span four different top-level EC classes (1=oxidoreductase, 2=transferase, 5=isomerase, 6=ligase). The sequence (~552 aa) exhibits a two-domain architecture characteristic of NadE: an N-terminal glutamine amidotransferase domain (containing a conserved Cys-His-Glu catalytic triad, e.g., the 'DGDNCVVTVKGVQVGVVICEDLWFAE' region with catalytic Cys) and a C-terminal nucleotide synthetase domain (containing the 'GDMCGGY' nucleotidyltransferase motif). The combination of a glutamine amidotransferase domain coupled to an ATP-dependent nucleotide synthetase domain is the hallmark of glutamine-dependent NAD(+) synthetase (NadE, EC 6.3.5.1), a ligase (EC 6) forming a C–N bond using glutamine as the nitrogen donor. This two-domain architecture is not consistent with an ABC transporter (EC 5.6.2.4), an acyltransferase (EC 2.3.1.193), or a cytochrome P450 oxidoreductase (EC 1.14.19.80).",
    "missing_item_specific_fact": "Precise recognition of the NadE family requires specialized knowledge of the glutamine amidotransferase + NAD synthetase two-domain fold. Without familiarity with this specific domain combination, distinguishing EC 6.3.5.1 from other EC 6 ligases that also use glutamine would be difficult. However, the four distractors are from entirely different EC classes, reducing the specificity needed.",
    "reason": "The sequence contains identifiable domain features (glutaminase catalytic Cys, nucleotidyltransferase motif) that support the ligase/glutamine-amidotransferase classification. The four options being from four different EC top-level classes means that recognizing the two-domain glutaminase+synthetase architecture is sufficient to select EC 6 over EC 1, 2, or 5. This constitutes a concrete biological argument from the sequence, though it requires specialized domain-recognition knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four distinct EC top-level classes (1, 2, 5, 6), and the sequence's two-domain glutaminase+synthetase architecture is most consistent with EC 6. No other option plausibly matches the observed domain organization."
  },
  "important_caveats": [
    "The EC 6.3.5.1 annotation is assigned via HAMAP-Rule (ECO:0000255), a computational/curatorial rule, not direct in vitro enzymatic assay evidence. The 2024 PubMed paper provides disruption phenotype and structural data but the entry does not cite direct kinetic characterization.",
    "The entry was first public on 2025-02-05 (entry version 50 current, version 49 at historical cutoff). The author's source snapshot date is unknown, but sequence match is confirmed across versions.",
    "Domain recognition from raw sequence without structural data or database lookup requires specialized knowledge of the NadE/glutamine amidotransferase superfamily architecture.",
    "The identity of the protein (NadE from Xanthomonas campestris) was inferred by the reviewer from dataset metadata; this accession was not provided to the evaluated model."
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

**Accession:** `A0A0H2X6L3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 49. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
"A0A0H2X6L3"
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"NAD(+) synthase [glutamine-hydrolyzing]"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAD(+) synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NADS"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"6.3.5.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Glutamine-dependent NAD(+) synthetase"}}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"6.3.5.1","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"name":"deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24384"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29985"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:58437"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"citation":{"authors":["Xu G.","Ma J.","Fang Q.","Peng Q.","Jiao X.","Hu W.","Zhao Q.","Kong Y.","Liu F.","Shi X.","Tang D.J.","Tang J.L.","Ming Z."],"citationCrossReferences":[{"database":"PubMed","id":"38429435"},{"database":"DOI","id":"10.1038/s42003-024-05921-3"}],"citationType":"journal article","firstPage":"255","id":"38429435","journal":"Commun. Biol.","lastPage":"255","publicationDate":"2024","title":"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.","volume":"7"},"referenceComments":[{"type":"STRAIN","value":"8004"}],"referenceNumber":2,"referencePositions":["DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
ID   NADE_XANC8              Reviewed;         552 AA.
AC   A0A0H2X6L3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 49.
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
GN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};
GN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 28-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
RN   [2]
RP   DISRUPTION PHENOTYPE.
RC   STRAIN=8004;
RX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;
RA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,
RA   Shi X., Tang D.J., Tang J.L., Ming Z.;
RT   "Structural insights into Xanthomonas campestris pv. campestris NAD+
RT   biosynthesis via the NAM salvage pathway.";
RL   Commun. Biol. 7:255-255(2024).
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP +
CC         diphosphate + NAD(+) + H(+); Xref=Rhea:RHEA:24384, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29985, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:33019, ChEBI:CHEBI:57540, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:58437, ChEBI:CHEBI:456215; EC=6.3.5.1;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_02090};
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
