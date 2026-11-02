# pathway_0046

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP

[Multiple Choices]
A. Bacterial outer membrane biogenesis
B. coenzyme A biosynthesis
C. Alkaloid biosynthesis
D. fatty acid beta-oxidation. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry for vinorine hydroxylase, whose annotated pathway is alkaloid biosynthesis, including ajmaline biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with a microsomal cytochrome P450, which makes bacterial outer membrane biogenesis less plausible. But P450 identity alone does not establish that this particular enzyme acts in alkaloid biosynthesis rather than another pathway.


**Missing item-specific fact**

> The enzyme's identity and experimentally established role as vinorine hydroxylase in alkaloid/ajmaline biosynthesis.


**Reason**

> The supplied sequence and choices do not provide the substrate or organism context needed to assign this P450 to a specific metabolic pathway. Distinguishing the keyed pathway requires protein-specific annotation or prior knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the keyed pathway for the exact sequence; none of the other choices is comparably supported.


### Important caveats

- The cited UniProt pathway annotation is linked to experimental evidence, but the primary papers were not independently reviewed here.
- The author's exact source snapshot is unknown; the sequence matches both the current and retrieved historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with a microsomal cytochrome P450, which makes bacterial outer membrane biogenesis less plausible. But P450 identity alone does not establish that this particular enzyme acts in alkaloid biosynthesis rather than another pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's identity and experimentally established role as vinorine hydroxylase in alkaloid/ajmaline biosynthesis.",
    "reason": "The supplied sequence and choices do not provide the substrate or organism context needed to assign this P450 to a specific metabolic pathway. Distinguishing the keyed pathway requires protein-specific annotation or prior knowledge."
  },
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for vinorine hydroxylase, whose annotated pathway is alkaloid biosynthesis, including ajmaline biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The cited UniProt pathway annotation is linked to experimental evidence, but the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current and retrieved historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the keyed pathway for the exact sequence; none of the other choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for vinorine hydroxylase, whose annotated pathway is alkaloid biosynthesis, including ajmaline biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with a microsomal cytochrome P450, which makes bacterial outer membrane biogenesis less plausible. But P450 identity alone does not establish that this particular enzyme acts in alkaloid biosynthesis rather than another pathway.",
    "missing_item_specific_fact": "The enzyme's identity and experimentally established role as vinorine hydroxylase in alkaloid/ajmaline biosynthesis.",
    "reason": "The supplied sequence and choices do not provide the substrate or organism context needed to assign this P450 to a specific metabolic pathway. Distinguishing the keyed pathway requires protein-specific annotation or prior knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the keyed pathway for the exact sequence; none of the other choices is comparably supported."
  },
  "important_caveats": [
    "The cited UniProt pathway annotation is linked to experimental evidence, but the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown; the sequence matches both the current and retrieved historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A218NGS0 (Vinorine hydroxylase / CYP82S18 from Rauvolfia serpentina) is annotated with pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:28654178, PubMed:38212296). The sequence matches exactly (480 AA, SHA256 confirmed). The protein is a cytochrome P450 that catalyzes vinorine hydroxylation, a committed step in ajmaline (monoterpene indole alkaloid) biosynthesis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable P450 heme-binding motif (FGSGRRACPG matching FxxGxxxCxG at ~residue 370) and an N-terminal signal peptide (MDLLQILLAIAGLLAILLLQ), identifying it as an ER-targeted cytochrome P450. General biological knowledge eliminates: (A) bacterial outer membrane biogenesis — irrelevant for a eukaryotic P450 with a signal peptide; (B) coenzyme A biosynthesis — does not involve P450 enzymes; (D) fatty acid beta-oxidation — a mitochondrial/peroxisomal process using acyl-CoA dehydrogenases, hydratases, and thiolases, not P450s. Alkaloid biosynthesis (C) is a well-established P450-dependent secondary metabolic pathway in plants, making it the only option consistent with a plant cytochrome P450.


**Missing item-specific fact**

> None strictly required for elimination among the four given choices. However, distinguishing 'alkaloid biosynthesis' from other P450-dependent plant secondary pathways (e.g., terpenoid, flavonoid biosynthesis) would require substrate or gene-family knowledge not derivable from sequence alone; this is mitigated by the fact that no such alternative P450 pathway appears among the options.


**Reason**

> The P450 heme-binding motif is extractable from the sequence, and the three distractors are eliminable through general knowledge that P450s do not participate in bacterial membrane assembly, CoA synthesis, or beta-oxidation. The remaining option (alkaloid biosynthesis) is a canonical P450 pathway in plants. Reasoning from sequence features plus pathway biochemistry is sufficient to select C among the four choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly incompatible with a cytochrome P450 enzyme. Only C (alkaloid biosynthesis) is a recognized P450-dependent pathway among the choices. No ambiguity among the given options.


### Important caveats

- The specific identification as 'alkaloid biosynthesis' (rather than, e.g., terpenoid or phenylpropanoid biosynthesis, which are also P450-dependent) relies on the elimination of non-P450 pathways among the four options rather than on sequence-specific substrate recognition.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269) from two independent studies, providing strong support for the pathway assignment.
- The P450 heme-binding motif FxxGxxxCxG is identifiable but somewhat degenerate in this sequence (FGSGRRACPG); recognition requires familiarity with P450 structural biology.
- The N-terminal hydrophobic stretch is consistent with an ER signal peptide typical of plant microsomal P450s, further supporting eukaryotic (not bacterial) origin.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (FGSGRRACPG matching FxxGxxxCxG at ~residue 370) and an N-terminal signal peptide (MDLLQILLAIAGLLAILLLQ), identifying it as an ER-targeted cytochrome P450. General biological knowledge eliminates: (A) bacterial outer membrane biogenesis — irrelevant for a eukaryotic P450 with a signal peptide; (B) coenzyme A biosynthesis — does not involve P450 enzymes; (D) fatty acid beta-oxidation — a mitochondrial/peroxisomal process using acyl-CoA dehydrogenases, hydratases, and thiolases, not P450s. Alkaloid biosynthesis (C) is a well-established P450-dependent secondary metabolic pathway in plants, making it the only option consistent with a plant cytochrome P450.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination among the four given choices. However, distinguishing 'alkaloid biosynthesis' from other P450-dependent plant secondary pathways (e.g., terpenoid, flavonoid biosynthesis) would require substrate or gene-family knowledge not derivable from sequence alone; this is mitigated by the fact that no such alternative P450 pathway appears among the options.",
    "reason": "The P450 heme-binding motif is extractable from the sequence, and the three distractors are eliminable through general knowledge that P450s do not participate in bacterial membrane assembly, CoA synthesis, or beta-oxidation. The remaining option (alkaloid biosynthesis) is a canonical P450 pathway in plants. Reasoning from sequence features plus pathway biochemistry is sufficient to select C among the four choices."
  },
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A218NGS0 (Vinorine hydroxylase / CYP82S18 from Rauvolfia serpentina) is annotated with pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:28654178, PubMed:38212296). The sequence matches exactly (480 AA, SHA256 confirmed). The protein is a cytochrome P450 that catalyzes vinorine hydroxylation, a committed step in ajmaline (monoterpene indole alkaloid) biosynthesis."
  },
  "important_caveats": [
    "The specific identification as 'alkaloid biosynthesis' (rather than, e.g., terpenoid or phenylpropanoid biosynthesis, which are also P450-dependent) relies on the elimination of non-P450 pathways among the four options rather than on sequence-specific substrate recognition.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269) from two independent studies, providing strong support for the pathway assignment.",
    "The P450 heme-binding motif FxxGxxxCxG is identifiable but somewhat degenerate in this sequence (FGSGRRACPG); recognition requires familiarity with P450 structural biology.",
    "The N-terminal hydrophobic stretch is consistent with an ER signal peptide typical of plant microsomal P450s, further supporting eukaryotic (not bacterial) origin."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a cytochrome P450 enzyme. Only C (alkaloid biosynthesis) is a recognized P450-dependent pathway among the choices. No ambiguity among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A218NGS0 (Vinorine hydroxylase / CYP82S18 from Rauvolfia serpentina) is annotated with pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:28654178, PubMed:38212296). The sequence matches exactly (480 AA, SHA256 confirmed). The protein is a cytochrome P450 that catalyzes vinorine hydroxylation, a committed step in ajmaline (monoterpene indole alkaloid) biosynthesis.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable P450 heme-binding motif (FGSGRRACPG matching FxxGxxxCxG at ~residue 370) and an N-terminal signal peptide (MDLLQILLAIAGLLAILLLQ), identifying it as an ER-targeted cytochrome P450. General biological knowledge eliminates: (A) bacterial outer membrane biogenesis — irrelevant for a eukaryotic P450 with a signal peptide; (B) coenzyme A biosynthesis — does not involve P450 enzymes; (D) fatty acid beta-oxidation — a mitochondrial/peroxisomal process using acyl-CoA dehydrogenases, hydratases, and thiolases, not P450s. Alkaloid biosynthesis (C) is a well-established P450-dependent secondary metabolic pathway in plants, making it the only option consistent with a plant cytochrome P450.",
    "missing_item_specific_fact": "None strictly required for elimination among the four given choices. However, distinguishing 'alkaloid biosynthesis' from other P450-dependent plant secondary pathways (e.g., terpenoid, flavonoid biosynthesis) would require substrate or gene-family knowledge not derivable from sequence alone; this is mitigated by the fact that no such alternative P450 pathway appears among the options.",
    "reason": "The P450 heme-binding motif is extractable from the sequence, and the three distractors are eliminable through general knowledge that P450s do not participate in bacterial membrane assembly, CoA synthesis, or beta-oxidation. The remaining option (alkaloid biosynthesis) is a canonical P450 pathway in plants. Reasoning from sequence features plus pathway biochemistry is sufficient to select C among the four choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a cytochrome P450 enzyme. Only C (alkaloid biosynthesis) is a recognized P450-dependent pathway among the choices. No ambiguity among the given options."
  },
  "important_caveats": [
    "The specific identification as 'alkaloid biosynthesis' (rather than, e.g., terpenoid or phenylpropanoid biosynthesis, which are also P450-dependent) relies on the elimination of non-P450 pathways among the four options rather than on sequence-specific substrate recognition.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269) from two independent studies, providing strong support for the pathway assignment.",
    "The P450 heme-binding motif FxxGxxxCxG is identifiable but somewhat degenerate in this sequence (FGSGRRACPG); recognition requires familiarity with P450 structural biology.",
    "The N-terminal hydrophobic stretch is consistent with an ER signal peptide typical of plant microsomal P450s, further supporting eukaryotic (not bacterial) origin."
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

**Accession:** `A0A218NGS0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
"A0A218NGS0"
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"Cytochrome P450 5437"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"value":"RsCYP5437"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Cytochrome P450 82S18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Perakine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"}],"value":"Vomilenine isomerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.14.14.104"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Vinorine hydroxylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsVH"}]}}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28654178","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"citation":{"authors":["Dang T.T.","Franke J.","Tatsis E.","O'Connor S.E."],"citationCrossReferences":[{"database":"PubMed","id":"28654178"},{"database":"DOI","id":"10.1002/anie.201705010"}],"citationType":"journal article","firstPage":"9440","id":"28654178","journal":"Angew. Chem. Int. Ed.","lastPage":"9444","publicationDate":"2017","title":"Dual catalytic activity of a cytochrome P450 controls bifurcation at a metabolic branch point of alkaloid biosynthesis in Rauwolfia serpentina.","volume":"56"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ASG81458.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES","TISSUE SPECIFICITY"]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 1-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
ID   VINHY_RAUSE             Reviewed;         480 AA.
AC   A0A218NGS0;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-SEP-2017, sequence version 1.
DT   28-JAN-2026, entry version 26.
DE   RecName: Full=Vinorine hydroxylase {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};
DE            Short=RsVH {ECO:0000303|PubMed:38212296};
DE            EC=1.14.14.104 {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296};
DE   AltName: Full=Cytochrome P450 5437 {ECO:0000312|EMBL:ASG81458.1};
DE            Short=RsCYP5437 {ECO:0000312|EMBL:ASG81458.1};
DE   AltName: Full=Cytochrome P450 82S18 {ECO:0000303|PubMed:28654178};
DE   AltName: Full=Perakine synthase {ECO:0000303|PubMed:28654178};
DE            Short=Vomilenine isomerase {ECO:0000303|PubMed:28654178};
GN   Name=VH {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};
GN   Synonyms=CYP5437 {ECO:0000312|EMBL:ASG81458.1},
GN   CYP82S18 {ECO:0000303|PubMed:28654178};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 23-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ASG81458.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND TISSUE SPECIFICITY.
RX   PubMed=28654178; DOI=10.1002/anie.201705010;
RA   Dang T.T., Franke J., Tatsis E., O'Connor S.E.;
RT   "Dual catalytic activity of a cytochrome P450 controls bifurcation at a
RT   metabolic branch point of alkaloid biosynthesis in Rauwolfia serpentina.";
RL   Angew. Chem. Int. Ed. 56:9440-9444(2017).
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND
RP   BIOTECHNOLOGY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
