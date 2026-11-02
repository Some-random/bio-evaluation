# cofactor_0113

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDLTTTSHARVDSGGVPFTSSLNDPTPPKLSASIALPAHLHLLAKAYGIPESHILQLAWALAANEQNARTAQWEHLELDERQAISWVLRHWQDPSVHRYLSPDELRGDKHQIPATVMAVVEEYSLFQTLALTGSETEIGMCFHPSTEQPWLRVIWNPEGMLASSASRLTRALESALHAVFLTPHVKVGDLTLFSIWDHQQILQWNSHYPQATDRLVHELFKDVVDASPQANAVAAWDGELTYRELDRLSSRLSGRLQDEFGVQPETIVVLCFEKSVWAIVAMLAVVKAGGAFLHVDPQHPAVRHQAMVQTTAAKLVLCSARTRSIISASVPECTSLVIDRRAFSVEPDHVQHETLLSSQNLSPRNAAYVVCTSGSTGTPKAIVVEHASLSTSVDAQANAMEISSGSRVLQYAAYTFDVSVGDIFTALTHGACICIPSDWERSHDLAGAINRLNVNQACLTSTVASILSPAEVPGLEKLTLGGEPATRQCVDAWAEQVRLKNVYGPAECTVWCMIQPEVSRHISVSNIGHGIGARAWIVHPEDHDRLMPVGAVGELLIEGPLVARGYLNDSTRTDEVFLSQPPRWLESFGPTPSRSRFYKTGDLARYGPAGALLFEGRKDTQIKLRGQRIELSEIEYRLHRALSDQVATAVELAHPKGSTAPVLAAFITWDQGIDLQNVQNVTLDARQEFEELASRIKAEIEQALPSYMVPALFIPVQTLPLTTSGKLDRKSLRHFCSQCSHEFLKKLDDSSPADAAPKESANPAEENLARLWAQVLERKSESIRRGDNFLSLGGDSLAAMRLVNLAARDLRLTLTVADVFNSPILADQANLLRPLVQTKHIAPFELVTDGDLPIQDLMDSVAKQCGLTSDQVEDVYPCTPYQEEMVRDSLSGTRTQMGQEVIQLASDLDLSRYLSACARVFQRCPILRTRFVEISGKLLQVVIREDISWQRPTSLAAYIEADNQTPPTLGKPLARWALTEDSTHLVLTMHHAIFDGISLGQIFGAIYAVYQSIPLPQVNLTFATFIGKIYRPHHDLPDASKQFWRSYLSPTAGSNDAPLSDVERASRPCANSGTQRLVTFQAGAVKALQQHGLTEATLARAAWACTLARGRQSPDSDVIFGTILTGRNIHLPGVDALAAPALAHTPIRVRMAAAQQEKPAHFLARVQADATAMIPFEHDGMDRIRALDEQVRVACDNMRTLLVIQPIPEGLILDSKSPFPGTMLSGPRVEAREMRHFHWYGLLMECTLLPMDGFFVRMSFDDTLYSPEAAERLLDEYSQTLHELAHGLTVDGSTE

[Multiple Choices]
A. [4Fe-4S] cluster
B. pantetheine 4'-phosphate
C. Ca(2+)
D. Cu(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for a nonribosomal peptide synthetase, which annotates pantetheine 4'-phosphate as its cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable NRPS-like features, including an adenylation-domain motif and a carrier-protein phosphopantetheinylation-site motif. NRPS carrier proteins require a 4'-phosphopantetheine group; this points to choice B rather than the metal-ion or iron-sulfur choices.


**Missing item-specific fact**

> No protein-specific database annotation is supplied, but the broad cofactor distinction can be inferred from the sequence’s NRPS-like features and established NRPS biology.


**Reason**

> Sequence-based recognition of an NRPS carrier-protein feature gives a concrete biological basis for selecting the phosphopantetheine cofactor. The reviewer-only annotation supports the key but is not needed as input to that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NRPS-associated phosphopantetheine cofactor is meaningfully distinguished from the listed metal and iron-sulfur alternatives.


### Important caveats

- The matched UniProt cofactor annotation is computationally inferred via PROSITE-ProRule; the cited excerpts do not establish direct experimental measurement of cofactor binding for this protein.
- The historical sequence match supports applicability, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS-like features, including an adenylation-domain motif and a carrier-protein phosphopantetheinylation-site motif. NRPS carrier proteins require a 4'-phosphopantetheine group; this points to choice B rather than the metal-ion or iron-sulfur choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific database annotation is supplied, but the broad cofactor distinction can be inferred from the sequence’s NRPS-like features and established NRPS biology.",
    "reason": "Sequence-based recognition of an NRPS carrier-protein feature gives a concrete biological basis for selecting the phosphopantetheine cofactor. The reviewer-only annotation supports the key but is not needed as input to that inference."
  },
  "case_id": "cofactor_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a nonribosomal peptide synthetase, which annotates pantetheine 4'-phosphate as its cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The matched UniProt cofactor annotation is computationally inferred via PROSITE-ProRule; the cited excerpts do not establish direct experimental measurement of cofactor binding for this protein.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS-associated phosphopantetheine cofactor is meaningfully distinguished from the listed metal and iron-sulfur alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a nonribosomal peptide synthetase, which annotates pantetheine 4'-phosphate as its cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS-like features, including an adenylation-domain motif and a carrier-protein phosphopantetheinylation-site motif. NRPS carrier proteins require a 4'-phosphopantetheine group; this points to choice B rather than the metal-ion or iron-sulfur choices.",
    "missing_item_specific_fact": "No protein-specific database annotation is supplied, but the broad cofactor distinction can be inferred from the sequence’s NRPS-like features and established NRPS biology.",
    "reason": "Sequence-based recognition of an NRPS carrier-protein feature gives a concrete biological basis for selecting the phosphopantetheine cofactor. The reviewer-only annotation supports the key but is not needed as input to that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS-associated phosphopantetheine cofactor is meaningfully distinguished from the listed metal and iron-sulfur alternatives."
  },
  "important_caveats": [
    "The matched UniProt cofactor annotation is computationally inferred via PROSITE-ProRule; the cited excerpts do not establish direct experimental measurement of cofactor binding for this protein.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV3 (RESC_ASPSL) explicitly annotates pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor (evidence C5/H4). The protein is a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-), and all NRPS enzymes require pantetheine 4'-phosphate as the prosthetic group of their peptidyl carrier protein (PCP) domains. The annotation evidence code is ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational, but the underlying biology—that PCP domains in NRPS are post-translationally modified with pantetheine 4'-phosphate by phosphopantetheinyl transferase—is universally established in biochemistry. The sequence contains the canonical 'GDSLA' PCP serine-attachment motif, consistent with the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1295-aa sequence contains recognizable NRPS domain signatures: the 'GDSLA' motif (PCP serine attachment site), adenylation-domain-like regions (e.g., 'LSSRLSGRLQDEFGVQPET'), and condensation-domain-like segments. A model with general knowledge of NRPS architecture can identify these motifs, classify the protein as a nonribosomal peptide synthetase, and apply the well-established rule that NRPS enzymes universally require pantetheine 4'-phosphate as the cofactor for their PCP domains. The distractors (&#91;4Fe-4S&#93;, Ca2+, Cu2+) are cofactors for entirely different enzyme classes (radical SAM, calcium-dependent hydrolases, oxidases) and lack any sequence signature in this protein.


**Missing item-specific fact**

> None essential. The PCP 'GDS' motif is present and identifiable in the supplied sequence, and the NRPS→pantetheine 4'-phosphate relationship is textbook biochemistry.


**Reason**

> The question can be resolved by recognizing NRPS domain architecture (PCP, A, C domains) in the sequence and applying general knowledge that NRPS enzymes require pantetheine 4'-phosphate. This does not require memorizing the specific UniProt entry for P0DXV3.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Pantetheine 4'-phosphate is the sole cofactor for NRPS PCP domains. The other options (4Fe-4S, Ca2+, Cu2+) have no plausible mechanistic role in NRPS catalysis. No ambiguity exists among the choices given the domain architecture.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational rather than direct experimental measurement. However, the underlying biology is universally established across all characterized NRPS enzymes.
- The protein entry was first public in February 2025, so the specific NRPS (resC) is relatively recently characterized; however, the cofactor assignment relies on the universal NRPS biochemistry rule, not on a unique experimental finding for this particular enzyme.
- The sequence contains the 'GDSLA' PCP motif but the full multi-domain NRPS architecture (A-PCP-C) would require more detailed domain-boundary analysis to confirm rigorously from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1295-aa sequence contains recognizable NRPS domain signatures: the 'GDSLA' motif (PCP serine attachment site), adenylation-domain-like regions (e.g., 'LSSRLSGRLQDEFGVQPET'), and condensation-domain-like segments. A model with general knowledge of NRPS architecture can identify these motifs, classify the protein as a nonribosomal peptide synthetase, and apply the well-established rule that NRPS enzymes universally require pantetheine 4'-phosphate as the cofactor for their PCP domains. The distractors ([4Fe-4S], Ca2+, Cu2+) are cofactors for entirely different enzyme classes (radical SAM, calcium-dependent hydrolases, oxidases) and lack any sequence signature in this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None essential. The PCP 'GDS' motif is present and identifiable in the supplied sequence, and the NRPS→pantetheine 4'-phosphate relationship is textbook biochemistry.",
    "reason": "The question can be resolved by recognizing NRPS domain architecture (PCP, A, C domains) in the sequence and applying general knowledge that NRPS enzymes require pantetheine 4'-phosphate. This does not require memorizing the specific UniProt entry for P0DXV3."
  },
  "case_id": "cofactor_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV3 (RESC_ASPSL) explicitly annotates pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor (evidence C5/H4). The protein is a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-), and all NRPS enzymes require pantetheine 4'-phosphate as the prosthetic group of their peptidyl carrier protein (PCP) domains. The annotation evidence code is ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational, but the underlying biology—that PCP domains in NRPS are post-translationally modified with pantetheine 4'-phosphate by phosphopantetheinyl transferase—is universally established in biochemistry. The sequence contains the canonical 'GDSLA' PCP serine-attachment motif, consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational rather than direct experimental measurement. However, the underlying biology is universally established across all characterized NRPS enzymes.",
    "The protein entry was first public in February 2025, so the specific NRPS (resC) is relatively recently characterized; however, the cofactor assignment relies on the universal NRPS biochemistry rule, not on a unique experimental finding for this particular enzyme.",
    "The sequence contains the 'GDSLA' PCP motif but the full multi-domain NRPS architecture (A-PCP-C) would require more detailed domain-boundary analysis to confirm rigorously from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the sole cofactor for NRPS PCP domains. The other options (4Fe-4S, Ca2+, Cu2+) have no plausible mechanistic role in NRPS catalysis. No ambiguity exists among the choices given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV3 (RESC_ASPSL) explicitly annotates pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor (evidence C5/H4). The protein is a nonribosomal peptide synthetase (NRPS, EC 6.3.2.-), and all NRPS enzymes require pantetheine 4'-phosphate as the prosthetic group of their peptidyl carrier protein (PCP) domains. The annotation evidence code is ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational, but the underlying biology—that PCP domains in NRPS are post-translationally modified with pantetheine 4'-phosphate by phosphopantetheinyl transferase—is universally established in biochemistry. The sequence contains the canonical 'GDSLA' PCP serine-attachment motif, consistent with the annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1295-aa sequence contains recognizable NRPS domain signatures: the 'GDSLA' motif (PCP serine attachment site), adenylation-domain-like regions (e.g., 'LSSRLSGRLQDEFGVQPET'), and condensation-domain-like segments. A model with general knowledge of NRPS architecture can identify these motifs, classify the protein as a nonribosomal peptide synthetase, and apply the well-established rule that NRPS enzymes universally require pantetheine 4'-phosphate as the cofactor for their PCP domains. The distractors ([4Fe-4S], Ca2+, Cu2+) are cofactors for entirely different enzyme classes (radical SAM, calcium-dependent hydrolases, oxidases) and lack any sequence signature in this protein.",
    "missing_item_specific_fact": "None essential. The PCP 'GDS' motif is present and identifiable in the supplied sequence, and the NRPS→pantetheine 4'-phosphate relationship is textbook biochemistry.",
    "reason": "The question can be resolved by recognizing NRPS domain architecture (PCP, A, C domains) in the sequence and applying general knowledge that NRPS enzymes require pantetheine 4'-phosphate. This does not require memorizing the specific UniProt entry for P0DXV3."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the sole cofactor for NRPS PCP domains. The other options (4Fe-4S, Ca2+, Cu2+) have no plausible mechanistic role in NRPS catalysis. No ambiguity exists among the choices given the domain architecture."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from PROSITE-ProRule pattern match), which is computational rather than direct experimental measurement. However, the underlying biology is universally established across all characterized NRPS enzymes.",
    "The protein entry was first public in February 2025, so the specific NRPS (resC) is relatively recently characterized; however, the cofactor assignment relies on the universal NRPS biochemistry rule, not on a unique experimental finding for this particular enzyme.",
    "The sequence contains the 'GDSLA' PCP motif but the full multi-domain NRPS architecture (A-PCP-C) would require more detailed domain-boundary analysis to confirm rigorously from sequence alone."
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

**Accession:** `P0DXV3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
"P0DXV3"
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Nonribosomal peptide synthetase resC"}}}
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV3?format=txt&versions=4)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:53.747402+00:00.  

```text
DE   RecName: Full=Nonribosomal peptide synthetase resC {ECO:0000303|PubMed:39105744};
DE            EC=6.3.2.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein C {ECO:0000303|PubMed:39105744};
```

Source SHA-256: `1b7003df6665300ef1ac888ec6d64f0457b8f53c5d0454d1efab44d4b6ba307d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV3?format=txt&versions=4)  
**Locator:** `lines 49-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:53.747402+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `1b7003df6665300ef1ac888ec6d64f0457b8f53c5d0454d1efab44d4b6ba307d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
