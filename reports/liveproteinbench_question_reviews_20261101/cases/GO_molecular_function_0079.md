# GO_molecular_function_0079

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPRPVSVVFVSLIIAAAVGVWGVFAWNGGFEELDAIVNRHPSTGIPGLNHFPSLDQGLMSMAAFNLPVVGREPLFAEGRHFMAQLLANVFAIPIVLLTEDFRAAPGSVARYSTSWGVFSQLATSAVMCPLYGVCFSRRSNPRRVAVLPGRSTWIVLISVLIGYGAPAMLIFDPFSWGLKPQIWGVLAFTVYPLYVCLTASLLLKTVSSKRGRASRSVQKDSDSNSSLHYVVAGIVGVAGHLSYIGFHLGEHTGTAATRPDRVAQLVLRFLQIDYVITFAAMLTLAWHELTHSGRISLKPWRVAGYLLLGWLFIGPGATLAAAWALRERWIRQDTQEEKKRKL

[Multiple Choices]
A. double-stranded DNA endonuclease activity
B. isomerase activity
C. threonine synthase activity
D. ribonuclease III activity
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for terpene cyclase resF, whose EC number is 5.4.99.-, an isomerase class. UniProt also assigns GO:0016853, though that GO annotation is marked IEA:UniProtKB-KW; the function record cites both similarity-based and publication-based evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic, suggesting a membrane-associated protein, but that does not establish isomerase activity or distinguish it decisively from the listed catalytic functions.


**Missing item-specific fact**

> The protein-specific identification and functional annotation as terpene cyclase resF, including its isomerase-class EC number, are absent from the question input.


**Reason**

> The supplied sequence and choices provide no decisive, recognizable functional motif or biological context that supports the specific isomerase answer. Selecting B depends on the protein-specific function annotation, not merely on general reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports B; the other choices describe distinct activities not supported by the matched protein record.


### Important caveats

- The GO isomerase annotation is computationally assigned by keyword (IEA), while the function record combines similarity-based and publication-based evidence.
- The reviewer-only accession and annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, suggesting a membrane-associated protein, but that does not establish isomerase activity or distinguish it decisively from the listed catalytic functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as terpene cyclase resF, including its isomerase-class EC number, are absent from the question input.",
    "reason": "The supplied sequence and choices provide no decisive, recognizable functional motif or biological context that supports the specific isomerase answer. Selecting B depends on the protein-specific function annotation, not merely on general reasoning from the sequence."
  },
  "case_id": "GO_molecular_function_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for terpene cyclase resF, whose EC number is 5.4.99.-, an isomerase class. UniProt also assigns GO:0016853, though that GO annotation is marked IEA:UniProtKB-KW; the function record cites both similarity-based and publication-based evidence."
  },
  "important_caveats": [
    "The GO isomerase annotation is computationally assigned by keyword (IEA), while the function record combines similarity-based and publication-based evidence.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports B; the other choices describe distinct activities not supported by the matched protein record."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for terpene cyclase resF, whose EC number is 5.4.99.-, an isomerase class. UniProt also assigns GO:0016853, though that GO annotation is marked IEA:UniProtKB-KW; the function record cites both similarity-based and publication-based evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, suggesting a membrane-associated protein, but that does not establish isomerase activity or distinguish it decisively from the listed catalytic functions.",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as terpene cyclase resF, including its isomerase-class EC number, are absent from the question input.",
    "reason": "The supplied sequence and choices provide no decisive, recognizable functional motif or biological context that supports the specific isomerase answer. Selecting B depends on the protein-specific function annotation, not merely on general reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports B; the other choices describe distinct activities not supported by the matched protein record."
  },
  "important_caveats": [
    "The GO isomerase annotation is computationally assigned by keyword (IEA), while the function record combines similarity-based and publication-based evidence.",
    "The reviewer-only accession and annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXW0 (sequence matched, 342 AA) annotates this protein as 'Terpene cyclase resF' with EC 5.4.99.- (isomerase class) and assigns GO:0016853 (isomerase activity). The function comment describes a 6-endo cyclization via epoxide opening, which is an intramolecular rearrangement consistent with EC 5 (isomerases). The GO annotation carries evidence code IEA:UniProtKB-KW (inferred from keyword), and the EC number carries ECO:0000305 (curator-inferred). The PubMed reference (39105744) provides experimental support for the cyclase function in the restricticin biosynthetic pathway. While the GO assignment itself is electronic inference from the 'Isomerase' keyword rather than direct experimental GO curation, the underlying biochemical activity (intramolecular cyclization/rearrangement) is experimentally supported, making 'isomerase activity' a defensible annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> By elimination, one could argue the sequence lacks PLP-binding motifs (ruling out threonine synthase), lacks RNase III domain architecture (ruling out RNase III), and lacks restriction-enzyme catalytic centers (ruling out dsDNA endonuclease). The hydrophobic transmembrane-like segments and small size are loosely consistent with a terpene cyclase. However, this negative reasoning does not positively identify the protein as an isomerase; 'isomerase activity' (GO:0016853, EC 5) is an extremely broad umbrella covering many unrelated folds. Positive assignment requires recognizing the terpene cyclase superfamily fold or knowing the specific protein.


**Missing item-specific fact**

> Recognition of the terpene cyclase fold (or the specific identity of resF from the restricticin biosynthetic cluster) and the knowledge that 6-endo cyclization via epoxide opening is classified under EC 5.4.99.- (intramolecular transferases, a subclass of isomerases). Without this protein-family-level identification, the broad term 'isomerase activity' cannot be positively assigned from sequence features alone.


**Reason**

> The four options are mechanistically distinct, and elimination of A, C, and D is somewhat possible from sequence (no nuclease motifs, no PLP-binding site, no RNase III domain). However, positively selecting 'isomerase activity' from the remaining option requires recognizing the terpene cyclase architecture or having prior knowledge of this protein's EC classification. The GO annotation itself is IEA (electronic inference from keyword), confirming that even the database assignment is a lookup/annotation transfer rather than a sequence-derived prediction. A model would essentially need to identify this specific protein or its family to answer correctly.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct enzyme classes (hydrolase acting on DNA, isomerase, lyase, hydrolase acting on RNA). There is no genuine ambiguity in which class a terpene cyclase belongs to. The main concern is not ambiguity between options but the difficulty of positive identification from sequence alone.


### Important caveats

- The GO annotation GO:0016853 carries evidence code IEA:UniProtKB-KW, meaning it was assigned by automated keyword mapping, not by direct experimental GO curation. The underlying EC 5.4.99.- carries ECO:0000305 (inferred by curator).
- The protein was first released in UniProt in February 2025 (entry version 1, published 2025-02-05), making it a very recent annotation. The PubMed paper (2024) provides experimental pathway context but the GO assignment is electronic inference.
- The sequence contains multiple hydrophobic segments suggestive of membrane association, consistent with a terpene cyclase acting on hydrophobic polyketide intermediates, but this is not diagnostic of isomerase activity per se.
- The benchmark sequence matches the UniProt canonical sequence exactly (SHA256 confirmed), so the annotation applies directly to the queried sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "By elimination, one could argue the sequence lacks PLP-binding motifs (ruling out threonine synthase), lacks RNase III domain architecture (ruling out RNase III), and lacks restriction-enzyme catalytic centers (ruling out dsDNA endonuclease). The hydrophobic transmembrane-like segments and small size are loosely consistent with a terpene cyclase. However, this negative reasoning does not positively identify the protein as an isomerase; 'isomerase activity' (GO:0016853, EC 5) is an extremely broad umbrella covering many unrelated folds. Positive assignment requires recognizing the terpene cyclase superfamily fold or knowing the specific protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of the terpene cyclase fold (or the specific identity of resF from the restricticin biosynthetic cluster) and the knowledge that 6-endo cyclization via epoxide opening is classified under EC 5.4.99.- (intramolecular transferases, a subclass of isomerases). Without this protein-family-level identification, the broad term 'isomerase activity' cannot be positively assigned from sequence features alone.",
    "reason": "The four options are mechanistically distinct, and elimination of A, C, and D is somewhat possible from sequence (no nuclease motifs, no PLP-binding site, no RNase III domain). However, positively selecting 'isomerase activity' from the remaining option requires recognizing the terpene cyclase architecture or having prior knowledge of this protein's EC classification. The GO annotation itself is IEA (electronic inference from keyword), confirming that even the database assignment is a lookup/annotation transfer rather than a sequence-derived prediction. A model would essentially need to identify this specific protein or its family to answer correctly."
  },
  "case_id": "GO_molecular_function_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXW0 (sequence matched, 342 AA) annotates this protein as 'Terpene cyclase resF' with EC 5.4.99.- (isomerase class) and assigns GO:0016853 (isomerase activity). The function comment describes a 6-endo cyclization via epoxide opening, which is an intramolecular rearrangement consistent with EC 5 (isomerases). The GO annotation carries evidence code IEA:UniProtKB-KW (inferred from keyword), and the EC number carries ECO:0000305 (curator-inferred). The PubMed reference (39105744) provides experimental support for the cyclase function in the restricticin biosynthetic pathway. While the GO assignment itself is electronic inference from the 'Isomerase' keyword rather than direct experimental GO curation, the underlying biochemical activity (intramolecular cyclization/rearrangement) is experimentally supported, making 'isomerase activity' a defensible annotation."
  },
  "important_caveats": [
    "The GO annotation GO:0016853 carries evidence code IEA:UniProtKB-KW, meaning it was assigned by automated keyword mapping, not by direct experimental GO curation. The underlying EC 5.4.99.- carries ECO:0000305 (inferred by curator).",
    "The protein was first released in UniProt in February 2025 (entry version 1, published 2025-02-05), making it a very recent annotation. The PubMed paper (2024) provides experimental pathway context but the GO assignment is electronic inference.",
    "The sequence contains multiple hydrophobic segments suggestive of membrane association, consistent with a terpene cyclase acting on hydrophobic polyketide intermediates, but this is not diagnostic of isomerase activity per se.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA256 confirmed), so the annotation applies directly to the queried sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (hydrolase acting on DNA, isomerase, lyase, hydrolase acting on RNA). There is no genuine ambiguity in which class a terpene cyclase belongs to. The main concern is not ambiguity between options but the difficulty of positive identification from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXW0 (sequence matched, 342 AA) annotates this protein as 'Terpene cyclase resF' with EC 5.4.99.- (isomerase class) and assigns GO:0016853 (isomerase activity). The function comment describes a 6-endo cyclization via epoxide opening, which is an intramolecular rearrangement consistent with EC 5 (isomerases). The GO annotation carries evidence code IEA:UniProtKB-KW (inferred from keyword), and the EC number carries ECO:0000305 (curator-inferred). The PubMed reference (39105744) provides experimental support for the cyclase function in the restricticin biosynthetic pathway. While the GO assignment itself is electronic inference from the 'Isomerase' keyword rather than direct experimental GO curation, the underlying biochemical activity (intramolecular cyclization/rearrangement) is experimentally supported, making 'isomerase activity' a defensible annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "By elimination, one could argue the sequence lacks PLP-binding motifs (ruling out threonine synthase), lacks RNase III domain architecture (ruling out RNase III), and lacks restriction-enzyme catalytic centers (ruling out dsDNA endonuclease). The hydrophobic transmembrane-like segments and small size are loosely consistent with a terpene cyclase. However, this negative reasoning does not positively identify the protein as an isomerase; 'isomerase activity' (GO:0016853, EC 5) is an extremely broad umbrella covering many unrelated folds. Positive assignment requires recognizing the terpene cyclase superfamily fold or knowing the specific protein.",
    "missing_item_specific_fact": "Recognition of the terpene cyclase fold (or the specific identity of resF from the restricticin biosynthetic cluster) and the knowledge that 6-endo cyclization via epoxide opening is classified under EC 5.4.99.- (intramolecular transferases, a subclass of isomerases). Without this protein-family-level identification, the broad term 'isomerase activity' cannot be positively assigned from sequence features alone.",
    "reason": "The four options are mechanistically distinct, and elimination of A, C, and D is somewhat possible from sequence (no nuclease motifs, no PLP-binding site, no RNase III domain). However, positively selecting 'isomerase activity' from the remaining option requires recognizing the terpene cyclase architecture or having prior knowledge of this protein's EC classification. The GO annotation itself is IEA (electronic inference from keyword), confirming that even the database assignment is a lookup/annotation transfer rather than a sequence-derived prediction. A model would essentially need to identify this specific protein or its family to answer correctly."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (hydrolase acting on DNA, isomerase, lyase, hydrolase acting on RNA). There is no genuine ambiguity in which class a terpene cyclase belongs to. The main concern is not ambiguity between options but the difficulty of positive identification from sequence alone."
  },
  "important_caveats": [
    "The GO annotation GO:0016853 carries evidence code IEA:UniProtKB-KW, meaning it was assigned by automated keyword mapping, not by direct experimental GO curation. The underlying EC 5.4.99.- carries ECO:0000305 (inferred by curator).",
    "The protein was first released in UniProt in February 2025 (entry version 1, published 2025-02-05), making it a very recent annotation. The PubMed paper (2024) provides experimental pathway context but the GO assignment is electronic inference.",
    "The sequence contains multiple hydrophobic segments suggestive of membrane association, consistent with a terpene cyclase acting on hydrophobic polyketide intermediates, but this is not diagnostic of isomerase activity per se.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA256 confirmed), so the annotation applies directly to the queried sequence."
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

**Accession:** `P0DXW0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
"P0DXW0"
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"5.4.99.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Terpene cyclase resF"}}}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:50.537709+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P9WEG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39105744","source":"PubMed"}],"value":"Cyclase; part of the gene cluster that mediates the biosynthesis of the tetrahydropyranyl antifungal agent restricticin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:39105744). The highly reducing polyketide synthase resH, the short chain dehydrogenase resG, the cyclase resF, the FAD-dependent monooxygenase resA and the enoylreductase resD are required to generate the first stable intermediate desmethylrestrictinol. ResH with resD biosynthesize the first polyketide chain intermediate that is reduced by resG, followed by epoxidation by resA before 6-endo cyclization via epoxide opening by resF leads to desmethylrestrictinol. The methyltransferase resE then catalyzes the C4 O-methylation of desmethylrestrictinol to produce restrictinol, and the nonribosomal peptide synthetase resC catalyzes the C3 esterification of restrictinol with glycine that leads to restricticin (By similarity)"}]}
```

Source SHA-256: `20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
ID   RESF_ASPSL              Reviewed;         342 AA.
AC   P0DXW0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   09-APR-2025, entry version 2.
DE   RecName: Full=Terpene cyclase resF {ECO:0000303|PubMed:39105744};
DE            EC=5.4.99.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein F {ECO:0000303|PubMed:39105744};
GN   Name=resF {ECO:0000303|PubMed:39105744};
OS   Aspergillus sclerotiorum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=138282;
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 22-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
CC   -!- FUNCTION: Cyclase; part of the gene cluster that mediates the
CC       biosynthesis of the tetrahydropyranyl antifungal agent restricticin
CC       that acts as an inhibitor of CYP51 and blocks the ergosterol
CC       biosynthesis (PubMed:39105744). The highly reducing polyketide synthase
CC       resH, the short chain dehydrogenase resG, the cyclase resF, the FAD-
CC       dependent monooxygenase resA and the enoylreductase resD are required
CC       to generate the first stable intermediate desmethylrestrictinol. ResH
CC       with resD biosynthesize the first polyketide chain intermediate that is
CC       reduced by resG, followed by epoxidation by resA before 6-endo
CC       cyclization via epoxide opening by resF leads to desmethylrestrictinol.
CC       The methyltransferase resE then catalyzes the C4 O-methylation of
CC       desmethylrestrictinol to produce restrictinol, and the nonribosomal
CC       peptide synthetase resC catalyzes the C3 esterification of restrictinol
CC       with glycine that leads to restricticin (By similarity).
CC       {ECO:0000250|UniProtKB:P9WEG7, ECO:0000269|PubMed:39105744}.
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)  
**Locator:** `lines 47-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:54.246056+00:00.  

```text
DR   GO; GO:0016853; F:isomerase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130892-130912`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016853
name: isomerase activity
namespace: molecular_function
def: "Catalysis of the geometric or structural changes within one molecule. Isomerase is the systematic name for any enzyme of EC class 5." [ISBN:0198506732]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "other isomerase activity" NARROW []
xref: EC:5.-.-.-
xref: Reactome:R-HSA-2161666 "PGA2 is isomerised to PGC2"
xref: Reactome:R-HSA-2161735 "PGC2 is isomerised to PGB2"
xref: Reactome:R-HSA-6787623 "GFUS dimer epimerises GDP-DHDMan to GDP-KDGal"
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:5.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
