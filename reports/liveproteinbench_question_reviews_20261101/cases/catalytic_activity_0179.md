# catalytic_activity_0179

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — a beta-lactam + H2O = a substituted beta-amino acid

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKLLKILSLVCLSISIGACAEHSMSRAKTSTIPQVNNSIIDQNVQALFNEISADAVFVTYDGQNIKKYGTHLDRAKTAYIPASTFKIANALIGLENHKATSTEIFKWDGKPRFFKAWDKDFTLGEAMQASTVPVYQELARRIGPSLMQSELQRIGYGNMQIGTEVDQFWLKGPLTITPIQEVKFVYDLAQGQLPFKPEVQQQVKEMLYVERRGENRLYAKSGWGMAVDPQVGWYVGFVEKADGQVVAFALNMQMKAGDDIALRKQLSLDVLDKLGVFHYL

[Multiple Choices]
A. deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)
B. a beta-lactam + H2O = a substituted beta-amino acid
C. folate(in) + H(+)(in) = folate(out) + H(+)(out)
D. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
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

> The matched sequence is annotated as beta-lactamase OXA-58, EC 3.5.2.6, with the reaction in choice B. The annotation cites experimental evidence codes, although the cited papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an S-X-X-K motif (in the segment ASTFK), a hallmark active-site motif of serine beta-lactamases. Beta-lactam ring hydrolysis fits choice B; the other choices describe unrelated NAD-dependent, transport, or oxidoreductase activities.


**Missing item-specific fact**

> No item-specific fact is necessary for a defensible distinction from these choices, though database annotation would confirm the exact enzyme identity.


**Reason**

> The sequence provides a recognizable catalytic-family signature that supports beta-lactam hydrolysis rather than relying only on memorized identification of the exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The beta-lactamase motif and the reaction choices distinguish B from the alternatives.


### Important caveats

- The database evidence is reviewer-only and was not supplied to the evaluated model.
- The UniProt annotation cites experimental evidence, but the cited primary studies were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an S-X-X-K motif (in the segment ASTFK), a hallmark active-site motif of serine beta-lactamases. Beta-lactam ring hydrolysis fits choice B; the other choices describe unrelated NAD-dependent, transport, or oxidoreductase activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary for a defensible distinction from these choices, though database annotation would confirm the exact enzyme identity.",
    "reason": "The sequence provides a recognizable catalytic-family signature that supports beta-lactam hydrolysis rather than relying only on memorized identification of the exact protein."
  },
  "case_id": "catalytic_activity_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as beta-lactamase OXA-58, EC 3.5.2.6, with the reaction in choice B. The annotation cites experimental evidence codes, although the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "The database evidence is reviewer-only and was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the cited primary studies were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The beta-lactamase motif and the reaction choices distinguish B from the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as beta-lactamase OXA-58, EC 3.5.2.6, with the reaction in choice B. The annotation cites experimental evidence codes, although the cited papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an S-X-X-K motif (in the segment ASTFK), a hallmark active-site motif of serine beta-lactamases. Beta-lactam ring hydrolysis fits choice B; the other choices describe unrelated NAD-dependent, transport, or oxidoreductase activities.",
    "missing_item_specific_fact": "No item-specific fact is necessary for a defensible distinction from these choices, though database annotation would confirm the exact enzyme identity.",
    "reason": "The sequence provides a recognizable catalytic-family signature that supports beta-lactam hydrolysis rather than relying only on memorized identification of the exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The beta-lactamase motif and the reaction choices distinguish B from the alternatives."
  },
  "important_caveats": [
    "The database evidence is reviewer-only and was not supplied to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the cited primary studies were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, EC 3.5.2.6) exactly (SHA256 confirmed). The UniProt entry annotates the catalytic activity as 'a beta-lactam + H2O = a substituted beta-amino acid' (Rhea:RHEA:20401), backed by experimental evidence (ECO:0000269) from three independent studies (PubMed:15616297, 26459904, 26701320) including X-ray crystallography with substrate analogs. The expected answer B matches this annotation verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent fundamentally different enzyme classes with incompatible sequence architectures. (1) Option A (NAD synthetase, EC 6.3.5.1) requires a multi-domain architecture (~500-600 aa in bacteria) with glutamine amidotransferase and adenylate-forming domains; the 280-aa sequence is far too small. (2) Option C (folate transporter) requires multiple transmembrane helices; the sequence has a signal peptide but lacks the 6-12 TM domain topology of a MFS/SLC-family transporter. (3) Option D (L-galactose dehydrogenase, an oxidoreductase) requires a Rossmann-fold NAD-binding motif (GxGxxG); no such motif is evident. (4) Option B (beta-lactamase) is consistent with the observed features: ~280 aa size, N-terminal signal peptide (secreted/periplasmic), and serine-containing active-site motifs (S-x-x-K equivalent) characteristic of class D beta-lactamases. Elimination of A, C, and D by architectural incompatibility leaves B as the only viable answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer can be reached through general protein-architecture reasoning: the sequence length eliminates the multi-domain synthetase, the absence of TM helices eliminates the transporter, and the absence of a Rossmann fold eliminates the dehydrogenase. The remaining option (a secreted hydrolase of ~280 aa with Ser-rich motifs) is consistent with a beta-lactamase. This relies on general knowledge of enzyme structural classes rather than memorization of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct EC classes (synthetase, hydrolase, transporter, oxidoreductase) with clearly incompatible structural requirements. The 280-aa sequence with a signal peptide and no TM domains or Rossmann fold uniquely fits a secreted hydrolase, leaving no genuine ambiguity among the choices.


### Important caveats

- Positive identification as specifically a class D (OXA-type) beta-lactamase rather than another secreted serine hydrolase would require recognizing the S-x-x-K and other class D motifs; however, among the four provided choices, elimination by architectural incompatibility is sufficient.
- The UniProt annotation for EC 3.5.2.6 is supported by experimental evidence (ECO:0000269) including crystallographic studies with carbapenem analogs, not merely computational prediction.
- The sequence is a precursor (280 aa including signal peptide); the mature enzyme is ~259 aa.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent fundamentally different enzyme classes with incompatible sequence architectures. (1) Option A (NAD synthetase, EC 6.3.5.1) requires a multi-domain architecture (~500-600 aa in bacteria) with glutamine amidotransferase and adenylate-forming domains; the 280-aa sequence is far too small. (2) Option C (folate transporter) requires multiple transmembrane helices; the sequence has a signal peptide but lacks the 6-12 TM domain topology of a MFS/SLC-family transporter. (3) Option D (L-galactose dehydrogenase, an oxidoreductase) requires a Rossmann-fold NAD-binding motif (GxGxxG); no such motif is evident. (4) Option B (beta-lactamase) is consistent with the observed features: ~280 aa size, N-terminal signal peptide (secreted/periplasmic), and serine-containing active-site motifs (S-x-x-K equivalent) characteristic of class D beta-lactamases. Elimination of A, C, and D by architectural incompatibility leaves B as the only viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached through general protein-architecture reasoning: the sequence length eliminates the multi-domain synthetase, the absence of TM helices eliminates the transporter, and the absence of a Rossmann fold eliminates the dehydrogenase. The remaining option (a secreted hydrolase of ~280 aa with Ser-rich motifs) is consistent with a beta-lactamase. This relies on general knowledge of enzyme structural classes rather than memorization of this specific UniProt entry."
  },
  "case_id": "catalytic_activity_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, EC 3.5.2.6) exactly (SHA256 confirmed). The UniProt entry annotates the catalytic activity as 'a beta-lactam + H2O = a substituted beta-amino acid' (Rhea:RHEA:20401), backed by experimental evidence (ECO:0000269) from three independent studies (PubMed:15616297, 26459904, 26701320) including X-ray crystallography with substrate analogs. The expected answer B matches this annotation verbatim."
  },
  "important_caveats": [
    "Positive identification as specifically a class D (OXA-type) beta-lactamase rather than another secreted serine hydrolase would require recognizing the S-x-x-K and other class D motifs; however, among the four provided choices, elimination by architectural incompatibility is sufficient.",
    "The UniProt annotation for EC 3.5.2.6 is supported by experimental evidence (ECO:0000269) including crystallographic studies with carbapenem analogs, not merely computational prediction.",
    "The sequence is a precursor (280 aa including signal peptide); the mature enzyme is ~259 aa."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC classes (synthetase, hydrolase, transporter, oxidoreductase) with clearly incompatible structural requirements. The 280-aa sequence with a signal peptide and no TM domains or Rossmann fold uniquely fits a secreted hydrolase, leaving no genuine ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, EC 3.5.2.6) exactly (SHA256 confirmed). The UniProt entry annotates the catalytic activity as 'a beta-lactam + H2O = a substituted beta-amino acid' (Rhea:RHEA:20401), backed by experimental evidence (ECO:0000269) from three independent studies (PubMed:15616297, 26459904, 26701320) including X-ray crystallography with substrate analogs. The expected answer B matches this annotation verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent fundamentally different enzyme classes with incompatible sequence architectures. (1) Option A (NAD synthetase, EC 6.3.5.1) requires a multi-domain architecture (~500-600 aa in bacteria) with glutamine amidotransferase and adenylate-forming domains; the 280-aa sequence is far too small. (2) Option C (folate transporter) requires multiple transmembrane helices; the sequence has a signal peptide but lacks the 6-12 TM domain topology of a MFS/SLC-family transporter. (3) Option D (L-galactose dehydrogenase, an oxidoreductase) requires a Rossmann-fold NAD-binding motif (GxGxxG); no such motif is evident. (4) Option B (beta-lactamase) is consistent with the observed features: ~280 aa size, N-terminal signal peptide (secreted/periplasmic), and serine-containing active-site motifs (S-x-x-K equivalent) characteristic of class D beta-lactamases. Elimination of A, C, and D by architectural incompatibility leaves B as the only viable answer.",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached through general protein-architecture reasoning: the sequence length eliminates the multi-domain synthetase, the absence of TM helices eliminates the transporter, and the absence of a Rossmann fold eliminates the dehydrogenase. The remaining option (a secreted hydrolase of ~280 aa with Ser-rich motifs) is consistent with a beta-lactamase. This relies on general knowledge of enzyme structural classes rather than memorization of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct EC classes (synthetase, hydrolase, transporter, oxidoreductase) with clearly incompatible structural requirements. The 280-aa sequence with a signal peptide and no TM domains or Rossmann fold uniquely fits a secreted hydrolase, leaving no genuine ambiguity among the choices."
  },
  "important_caveats": [
    "Positive identification as specifically a class D (OXA-type) beta-lactamase rather than another secreted serine hydrolase would require recognizing the S-x-x-K and other class D motifs; however, among the four provided choices, elimination by architectural incompatibility is sufficient.",
    "The UniProt annotation for EC 3.5.2.6 is supported by experimental evidence (ECO:0000269) including crystallographic studies with carbapenem analogs, not merely computational prediction.",
    "The sequence is a precursor (280 aa including signal peptide); the mature enzyme is ~259 aa."
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

**Accession:** `Q2TR58` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 133. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
"Q2TR58"
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"15616297","source":"PubMed"}],"value":"Beta-lactamase OXA-58"}}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.5.2.6","evidences":[{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"name":"a beta-lactam + H2O = a substituted beta-amino acid","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20401"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35627"},{"database":"ChEBI","id":"CHEBI:140347"}]}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Poirel L.","Marque S.","Heritier C.","Segonds C.","Chabanon G.","Nordmann P."],"citationCrossReferences":[{"database":"PubMed","id":"15616297"},{"database":"DOI","id":"10.1128/aac.49.1.202-208.2005"}],"citationType":"journal article","firstPage":"202","id":"15616297","journal":"Antimicrob. Agents Chemother.","lastPage":"208","publicationDate":"2005","title":"OXA-58, a novel class D {beta}-lactamase involved in resistance to carbapenems in Acinetobacter baumannii.","volume":"49"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"type":"STRAIN","value":"MAD"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Saino H.","Sugiyabu T.","Ueno G.","Yamamoto M.","Ishii Y.","Miyano M."],"citationCrossReferences":[{"database":"PubMed","id":"26701320"},{"database":"DOI","id":"10.1371/journal.pone.0145869"}],"citationType":"journal article","firstPage":"e0145869","id":"26701320","journal":"PLoS ONE","lastPage":"e0145869","publicationDate":"2015","title":"Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed State: Insights into the Mobility and Stability of the OXA-58 Structure.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5BOH","source":"PDB"}],"referenceNumber":23,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","CARBOXYLATION AT LYS-86","MUTAGENESIS OF SER-83 AND TRP-169"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Pratap S.","Katiki M.","Gill P.","Kumar P.","Golemi-Kotra D."],"citationCrossReferences":[{"database":"PubMed","id":"26459904"},{"database":"DOI","id":"10.1128/aac.01393-15"}],"citationType":"journal article","firstPage":"75","id":"26459904","journal":"Antimicrob. Agents Chemother.","lastPage":"86","publicationDate":"2016","title":"Active-Site Plasticity Is Essential to Carbapenem Hydrolysis by OXA-58 Class D beta-Lactamase of Acinetobacter baumannii.","volume":"60"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4Y0O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0T","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0U","source":"PDB"}],"referenceNumber":24,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.30 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH CARBAPENEM ANALOGS","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","CARBOXYLATION AT LYS-86","MUTAGENESIS OF PHE-113; PHE-114 AND MET-225"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 1-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
ID   OXA58_ACIBA             Reviewed;         280 AA.
AC   Q2TR58; A5H882;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-JAN-2006, sequence version 1.
DT   28-JAN-2026, entry version 133.
DE   RecName: Full=Beta-lactamase OXA-58 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:15616297};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904, ECO:0000269|PubMed:26701320};
DE   Flags: Precursor;
GN   Name=OXA-58 {ECO:0000303|PubMed:15616297};
GN   Synonyms=bla-oxa-58 {ECO:0000312|EMBL:ABU97485.1},
GN   bla-oxa58 {ECO:0000312|EMBL:ABQ23512.2},
GN   blaOXA-58 {ECO:0000312|EMBL:AAW57529.1};
GN   ORFNames=EKS29_04300 {ECO:0000312|EMBL:RTY12892.1},
GN   GSE42_20550 {ECO:0000312|EMBL:MYM80302.1},
GN   H0529_21805 {ECO:0000312|EMBL:QOJ62286.1},
GN   P9867_019230 {ECO:0000312|EMBL:MEC5498499.1},
GN   P9867_20895 {ECO:0000312|EMBL:MDK4883960.1};
OS   Acinetobacter baumannii.
OG   Plasmid pA2445 {ECO:0000312|EMBL:AGC51039.1},
OG   Plasmid pABIR {ECO:0000312|EMBL:ACB05799.1},
OG   Plasmid pABNA1 {ECO:0000312|EMBL:ACT98250.1},
OG   Plasmid pABNA2 {ECO:0000312|EMBL:ACT98258.1},
OG   Plasmid pAC1633-1 {ECO:0000312|EMBL:QOJ62286.1},
OG   Plasmid pOUR {ECO:0000312|EMBL:ABQ23503.1},
OG   Plasmid pWA3 {ECO:0000312|EMBL:AFF18250.1}, and
OG   Plasmid pWH8144 {ECO:0000312|EMBL:AFH57370.1}.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Moraxellales; Moraxellaceae; Acinetobacter;
OC   Acinetobacter calcoaceticus/baumannii complex.
OX   NCBI_TaxID=470 {ECO:0000312|EMBL:AAW57529.1};
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
DE   RecName: Full=Beta-lactamase OXA-58 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:15616297};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904, ECO:0000269|PubMed:26701320};
DE   Flags: Precursor;
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 39-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [2] {ECO:0000312|EMBL:AAW57529.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=MAD {ECO:0000312|EMBL:AAW57529.1};
RX   PubMed=15616297; DOI=10.1128/aac.49.1.202-208.2005;
RA   Poirel L., Marque S., Heritier C., Segonds C., Chabanon G., Nordmann P.;
RT   "OXA-58, a novel class D {beta}-lactamase involved in resistance to
RT   carbapenems in Acinetobacter baumannii.";
RL   Antimicrob. Agents Chemother. 49:202-208(2005).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 227-235`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [23] {ECO:0007744|PDB:5BOH}
RP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280, FUNCTION, CATALYTIC
RP   ACTIVITY, ACTIVITY REGULATION, CARBOXYLATION AT LYS-86, AND MUTAGENESIS OF
RP   SER-83 AND TRP-169.
RX   PubMed=26701320; DOI=10.1371/journal.pone.0145869;
RA   Saino H., Sugiyabu T., Ueno G., Yamamoto M., Ishii Y., Miyano M.;
RT   "Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed
RT   State: Insights into the Mobility and Stability of the OXA-58 Structure.";
RL   PLoS ONE 10:e0145869-e0145869(2015).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 236-245`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [24] {ECO:0007744|PDB:4Y0O, ECO:0007744|PDB:4Y0T, ECO:0007744|PDB:4Y0U}
RP   X-RAY CRYSTALLOGRAPHY (2.30 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH
RP   CARBAPENEM ANALOGS, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL
RP   PROPERTIES, CARBOXYLATION AT LYS-86, AND MUTAGENESIS OF PHE-113; PHE-114
RP   AND MET-225.
RX   PubMed=26459904; DOI=10.1128/aac.01393-15;
RA   Pratap S., Katiki M., Gill P., Kumar P., Golemi-Kotra D.;
RT   "Active-Site Plasticity Is Essential to Carbapenem Hydrolysis by OXA-58
RT   Class D beta-Lactamase of Acinetobacter baumannii.";
RL   Antimicrob. Agents Chemother. 60:75-86(2016).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 266-271`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-lactam + H2O = a substituted beta-amino acid;
CC         Xref=Rhea:RHEA:20401, ChEBI:CHEBI:15377, ChEBI:CHEBI:35627,
CC         ChEBI:CHEBI:140347; EC=3.5.2.6;
CC         Evidence={ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904,
CC         ECO:0000269|PubMed:26701320};
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
