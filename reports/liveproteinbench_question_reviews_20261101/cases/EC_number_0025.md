# EC_number_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.2.1.101

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. 1.1.1.336
B. 2.7.8.43
C. 4.1.1.128
D. 1.2.1.101
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

> The supplied sequence exactly matches the 1024-aa UniProt entry for FrzA. That entry assigns EC 1.2.1.101 and cites experimental evidence for the catalytic activity and reaction, supporting choice D for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence may suggest a specialized multidomain enzyme, but its general sequence features do not establish the specific reaction or complete EC number among these choices.


**Missing item-specific fact**

> The protein-specific catalytic activity—reported as the conversion involving L-tyrosinal, AMP, diphosphate, and NADP(+)—is needed to distinguish EC 1.2.1.101.


**Reason**

> The sequence is supplied, but the substrate specificity and unusual catalytic reaction that determine the exact EC number are not inferable from a concrete argument in the prompt. Identifying the answer therefore depends on a protein-specific annotation or experimental fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are distinct complete EC numbers, and the matched entry assigns 1.2.1.101.


### Important caveats

- The UniProt annotation is linked to experimental evidence (ECO:0000269) and a cited 2021 publication, but that primary paper was not independently reviewed here.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence may suggest a specialized multidomain enzyme, but its general sequence features do not establish the specific reaction or complete EC number among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—reported as the conversion involving L-tyrosinal, AMP, diphosphate, and NADP(+)—is needed to distinguish EC 1.2.1.101.",
    "reason": "The sequence is supplied, but the substrate specificity and unusual catalytic reaction that determine the exact EC number are not inferable from a concrete argument in the prompt. Identifying the answer therefore depends on a protein-specific annotation or experimental fact."
  },
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1024-aa UniProt entry for FrzA. That entry assigns EC 1.2.1.101 and cites experimental evidence for the catalytic activity and reaction, supporting choice D for this sequence."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence (ECO:0000269) and a cited 2021 publication, but that primary paper was not independently reviewed here.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct complete EC numbers, and the matched entry assigns 1.2.1.101."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1024-aa UniProt entry for FrzA. That entry assigns EC 1.2.1.101 and cites experimental evidence for the catalytic activity and reaction, supporting choice D for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence may suggest a specialized multidomain enzyme, but its general sequence features do not establish the specific reaction or complete EC number among these choices.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—reported as the conversion involving L-tyrosinal, AMP, diphosphate, and NADP(+)—is needed to distinguish EC 1.2.1.101.",
    "reason": "The sequence is supplied, but the substrate specificity and unusual catalytic reaction that determine the exact EC number are not inferable from a concrete argument in the prompt. Identifying the answer therefore depends on a protein-specific annotation or experimental fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct complete EC numbers, and the matched entry assigns 1.2.1.101."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence (ECO:0000269) and a cited 2021 publication, but that primary paper was not independently reviewed here.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1L4 (sequence SHA-256 matched exactly) annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269, in vitro) from PubMed:33372776 (Zhang et al., JACS 2021). The catalytic reaction is L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+), which is an aldehyde dehydrogenase (NADP+) reaction fitting EC 1.2.1.x. The expected answer D is well-supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options B (transferase 2.7.8.43) and C (lyase 4.1.1.128) can be broadly excluded because the sequence lacks transferase or decarboxylase/lyase motifs and instead shows NRPS-like domain architecture (adenylation, condensation, thiolation motifs). However, the critical distinction is between A (1.1.1.336, alcohol dehydrogenase acting on CH-OH) and D (1.2.1.101, aldehyde dehydrogenase acting on aldehyde/oxo with NADP+). Both are oxidoreductases with overlapping fold families. The protein is primarily an NRPS component whose aldehyde dehydrogenase activity is a non-canonical, recently characterized (2021) function. Identifying the specific aldehyde-oxidizing active site (Cys-His-Glu catalytic triad for aldehyde dehydrogenase) embedded within a large NRPS scaffold, and distinguishing it from an alcohol dehydrogenase active site, requires either recognizing this exact protein or possessing a specialized predictor trained on this niche annotation.


**Missing item-specific fact**

> The specific experimental finding (PubMed:33372776, 2021) that this non-canonical NRPS FrzA catalyzes the NADP+-dependent oxidation of L-tyrosinal to L-tyrosine (aldehyde dehydrogenase activity, EC 1.2.1.101) rather than an alcohol dehydrogenase reaction (EC 1.1.1.336). This is a protein-specific, experimentally determined catalytic activity that is not inferable from general sequence features without item-specific knowledge.


**Reason**

> The protein's dominant sequence identity is as a nonribosomal peptide synthetase, which does not naturally carry EC 1.x.x.x numbers. Its aldehyde dehydrogenase activity is a non-canonical function discovered in 2021. Distinguishing EC 1.1.1.336 from EC 1.2.1.101 from a 1024-AA NRPS sequence requires either recognizing this specific protein and its database annotation or identifying subtle active-site differences (aldehyde vs. alcohol substrate specificity) that are not reliably extractable by general biological reasoning from the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (1.1.1.336, oxidoreductase on CH-OH with NADP+) and D (1.2.1.101, oxidoreductase on aldehyde/oxo with NADP+) are oxidoreductases that could plausibly be assigned to a dehydrogenase-like domain embedded in a large multi-domain protein. Without the specific experimental substrate data showing aldehyde (L-tyrosinal) rather than alcohol oxidation, the sequence alone does not clearly distinguish these two EC sub-classes. B and C are more clearly excluded by the absence of transferase or lyase motifs.


### Important caveats

- The EC 1.2.1.101 annotation is backed by in vitro experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.
- The protein was integrated into Swiss-Prot only in June 2025 (entry version 18 archived, version 20 current), so this is a very recent annotation; the author's data-construction snapshot is unknown.
- The protein's primary identity is as an NRPS component; the aldehyde dehydrogenase activity is a non-canonical secondary function, making sequence-based EC prediction inherently difficult.
- The identity of the accession (A0A7T8F1L4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (transferase 2.7.8.43) and C (lyase 4.1.1.128) can be broadly excluded because the sequence lacks transferase or decarboxylase/lyase motifs and instead shows NRPS-like domain architecture (adenylation, condensation, thiolation motifs). However, the critical distinction is between A (1.1.1.336, alcohol dehydrogenase acting on CH-OH) and D (1.2.1.101, aldehyde dehydrogenase acting on aldehyde/oxo with NADP+). Both are oxidoreductases with overlapping fold families. The protein is primarily an NRPS component whose aldehyde dehydrogenase activity is a non-canonical, recently characterized (2021) function. Identifying the specific aldehyde-oxidizing active site (Cys-His-Glu catalytic triad for aldehyde dehydrogenase) embedded within a large NRPS scaffold, and distinguishing it from an alcohol dehydrogenase active site, requires either recognizing this exact protein or possessing a specialized predictor trained on this niche annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:33372776, 2021) that this non-canonical NRPS FrzA catalyzes the NADP+-dependent oxidation of L-tyrosinal to L-tyrosine (aldehyde dehydrogenase activity, EC 1.2.1.101) rather than an alcohol dehydrogenase reaction (EC 1.1.1.336). This is a protein-specific, experimentally determined catalytic activity that is not inferable from general sequence features without item-specific knowledge.",
    "reason": "The protein's dominant sequence identity is as a nonribosomal peptide synthetase, which does not naturally carry EC 1.x.x.x numbers. Its aldehyde dehydrogenase activity is a non-canonical function discovered in 2021. Distinguishing EC 1.1.1.336 from EC 1.2.1.101 from a 1024-AA NRPS sequence requires either recognizing this specific protein and its database annotation or identifying subtle active-site differences (aldehyde vs. alcohol substrate specificity) that are not reliably extractable by general biological reasoning from the raw sequence."
  },
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence SHA-256 matched exactly) annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269, in vitro) from PubMed:33372776 (Zhang et al., JACS 2021). The catalytic reaction is L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+), which is an aldehyde dehydrogenase (NADP+) reaction fitting EC 1.2.1.x. The expected answer D is well-supported by experimental data."
  },
  "important_caveats": [
    "The EC 1.2.1.101 annotation is backed by in vitro experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.",
    "The protein was integrated into Swiss-Prot only in June 2025 (entry version 18 archived, version 20 current), so this is a very recent annotation; the author's data-construction snapshot is unknown.",
    "The protein's primary identity is as an NRPS component; the aldehyde dehydrogenase activity is a non-canonical secondary function, making sequence-based EC prediction inherently difficult.",
    "The identity of the accession (A0A7T8F1L4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (1.1.1.336, oxidoreductase on CH-OH with NADP+) and D (1.2.1.101, oxidoreductase on aldehyde/oxo with NADP+) are oxidoreductases that could plausibly be assigned to a dehydrogenase-like domain embedded in a large multi-domain protein. Without the specific experimental substrate data showing aldehyde (L-tyrosinal) rather than alcohol oxidation, the sequence alone does not clearly distinguish these two EC sub-classes. B and C are more clearly excluded by the absence of transferase or lyase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence SHA-256 matched exactly) annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269, in vitro) from PubMed:33372776 (Zhang et al., JACS 2021). The catalytic reaction is L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+), which is an aldehyde dehydrogenase (NADP+) reaction fitting EC 1.2.1.x. The expected answer D is well-supported by experimental data.",
    "evidence_ids": ["C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options B (transferase 2.7.8.43) and C (lyase 4.1.1.128) can be broadly excluded because the sequence lacks transferase or decarboxylase/lyase motifs and instead shows NRPS-like domain architecture (adenylation, condensation, thiolation motifs). However, the critical distinction is between A (1.1.1.336, alcohol dehydrogenase acting on CH-OH) and D (1.2.1.101, aldehyde dehydrogenase acting on aldehyde/oxo with NADP+). Both are oxidoreductases with overlapping fold families. The protein is primarily an NRPS component whose aldehyde dehydrogenase activity is a non-canonical, recently characterized (2021) function. Identifying the specific aldehyde-oxidizing active site (Cys-His-Glu catalytic triad for aldehyde dehydrogenase) embedded within a large NRPS scaffold, and distinguishing it from an alcohol dehydrogenase active site, requires either recognizing this exact protein or possessing a specialized predictor trained on this niche annotation.",
    "missing_item_specific_fact": "The specific experimental finding (PubMed:33372776, 2021) that this non-canonical NRPS FrzA catalyzes the NADP+-dependent oxidation of L-tyrosinal to L-tyrosine (aldehyde dehydrogenase activity, EC 1.2.1.101) rather than an alcohol dehydrogenase reaction (EC 1.1.1.336). This is a protein-specific, experimentally determined catalytic activity that is not inferable from general sequence features without item-specific knowledge.",
    "reason": "The protein's dominant sequence identity is as a nonribosomal peptide synthetase, which does not naturally carry EC 1.x.x.x numbers. Its aldehyde dehydrogenase activity is a non-canonical function discovered in 2021. Distinguishing EC 1.1.1.336 from EC 1.2.1.101 from a 1024-AA NRPS sequence requires either recognizing this specific protein and its database annotation or identifying subtle active-site differences (aldehyde vs. alcohol substrate specificity) that are not reliably extractable by general biological reasoning from the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (1.1.1.336, oxidoreductase on CH-OH with NADP+) and D (1.2.1.101, oxidoreductase on aldehyde/oxo with NADP+) are oxidoreductases that could plausibly be assigned to a dehydrogenase-like domain embedded in a large multi-domain protein. Without the specific experimental substrate data showing aldehyde (L-tyrosinal) rather than alcohol oxidation, the sequence alone does not clearly distinguish these two EC sub-classes. B and C are more clearly excluded by the absence of transferase or lyase motifs."
  },
  "important_caveats": [
    "The EC 1.2.1.101 annotation is backed by in vitro experimental evidence (ECO:0000269), not computational inference, strengthening the key's validity.",
    "The protein was integrated into Swiss-Prot only in June 2025 (entry version 18 archived, version 20 current), so this is a very recent annotation; the author's data-construction snapshot is unknown.",
    "The protein's primary identity is as an NRPS component; the aldehyde dehydrogenase activity is a non-canonical secondary function, making sequence-based EC prediction inherently difficult.",
    "The identity of the accession (A0A7T8F1L4) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model."
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

**Accession:** `A0A7T8F1L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
"A0A7T8F1L4"
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.2.1.101"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Non-canonical nonribosomal peptide synthetase FrzA"}}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:57414"}}],"reaction":{"ecNumber":"1.2.1.101","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"name":"L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:57412"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58315"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:141668"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};
DE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   PATHWAY.
RC   STRAIN=11231;
RX   PubMed=33372776; DOI=10.1021/jacs.0c12352;
RA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,
RA   Taniguchi M., Watanabe K., Tang Y.;
RT   "Biosynthesis of the Immunosuppressant (-)-FR901483.";
RL   J. Am. Chem. Soc. 143:132-136(2021).
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 53-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP +
CC         NADPH + H(+); Xref=Rhea:RHEA:57412, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58315, ChEBI:CHEBI:58349, ChEBI:CHEBI:141668,
CC         ChEBI:CHEBI:456215; EC=1.2.1.101;
CC         Evidence={ECO:0000269|PubMed:33372776};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:57414;
CC         Evidence={ECO:0000269|PubMed:33372776};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
