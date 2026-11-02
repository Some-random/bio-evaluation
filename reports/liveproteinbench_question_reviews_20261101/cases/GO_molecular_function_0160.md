# GO_molecular_function_0160

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLHSASVIFLSLSVLAAVGVWGPFVRDGGFDAMDAVVARHPSTGIPGLQHYPEFDRGLMSIVAFNLSAVNSIAYCFMMQFLANVAVIPVILCTEDSSAAPGSWVRYSTIWGLLSQLGTSAVIYPLYAMSFIRQSSREPSQTRQPMSDMALILNMAMGYALPAAITLNVLHSSLNMQIWGILAFTVYPICMKLMARIIKVFTGFRKFPTRSRHQSIPTLRYAVAGGVALQGHLWYLGTELGIFKGHTPSLSAEKMDSEGGARLVLRFLQVDYAITFLAMLLLAWHELIYHRILPAWRALGGLIIGWILVGPGATLAAAWYLRSRFIMAPGKRKKRYGD

[Multiple Choices]
A. isomerase activity
B. osmolarity-sensing monoatomic cation channel activity
C. polyubiquitin modification-dependent protein binding
D. inward rectifier potassium channel activity
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

> The exact-matched sequence is annotated as a terpene cyclase, EC 5.4.99.-, and has a GO isomerase-activity annotation. This supports A, although the GO annotation itself is marked IEA (keyword-based), not a direct experimental GO assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence does not provide a clear, specific basis for identifying terpene-cyclase/isomerase activity over the channel or binding choices. Its hydrophobic stretches alone do not establish a channel function.


**Missing item-specific fact**

> Identifying this protein as the lanomycin-cluster terpene cyclase, or knowing its EC 5.4.99.- assignment, is needed to select isomerase activity.


**Reason**

> The answer is supported by the matched protein-specific annotation, but that annotation and the functional characterization are absent from the model input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific evidence supports A; the sequence's hydrophobicity may be suggestive of a membrane protein but does not by itself substantiate either channel option.


### Important caveats

- The GO isomerase annotation is computationally assigned by UniProtKB keyword mapping (IEA).
- The cited database function describes the protein as a cyclase and links it to a publication, but the supplied excerpts do not independently detail a direct assay of this protein's catalytic activity.
- The sequence match is exact; the author’s source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence does not provide a clear, specific basis for identifying terpene-cyclase/isomerase activity over the channel or binding choices. Its hydrophobic stretches alone do not establish a channel function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this protein as the lanomycin-cluster terpene cyclase, or knowing its EC 5.4.99.- assignment, is needed to select isomerase activity.",
    "reason": "The answer is supported by the matched protein-specific annotation, but that annotation and the functional characterization are absent from the model input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence."
  },
  "case_id": "GO_molecular_function_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as a terpene cyclase, EC 5.4.99.-, and has a GO isomerase-activity annotation. This supports A, although the GO annotation itself is marked IEA (keyword-based), not a direct experimental GO assignment."
  },
  "important_caveats": [
    "The GO isomerase annotation is computationally assigned by UniProtKB keyword mapping (IEA).",
    "The cited database function describes the protein as a cyclase and links it to a publication, but the supplied excerpts do not independently detail a direct assay of this protein's catalytic activity.",
    "The sequence match is exact; the author’s source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports A; the sequence's hydrophobicity may be suggestive of a membrane protein but does not by itself substantiate either channel option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated as a terpene cyclase, EC 5.4.99.-, and has a GO isomerase-activity annotation. This supports A, although the GO annotation itself is marked IEA (keyword-based), not a direct experimental GO assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence does not provide a clear, specific basis for identifying terpene-cyclase/isomerase activity over the channel or binding choices. Its hydrophobic stretches alone do not establish a channel function.",
    "missing_item_specific_fact": "Identifying this protein as the lanomycin-cluster terpene cyclase, or knowing its EC 5.4.99.- assignment, is needed to select isomerase activity.",
    "reason": "The answer is supported by the matched protein-specific annotation, but that annotation and the functional characterization are absent from the model input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports A; the sequence's hydrophobicity may be suggestive of a membrane protein but does not by itself substantiate either channel option."
  },
  "important_caveats": [
    "The GO isomerase annotation is computationally assigned by UniProtKB keyword mapping (IEA).",
    "The cited database function describes the protein as a cyclase and links it to a publication, but the supplied excerpts do not independently detail a direct assay of this protein's catalytic activity.",
    "The sequence match is exact; the author’s source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW1 (LAN5_PYRDE) annotates this protein as a terpene cyclase with EC 5.4.99.- (intramolecular transferases, subclass of EC 5 = Isomerases). GO:0016853 'isomerase activity' is directly assigned via IEA:UniProtKB-KW. The experimental evidence (PubMed:33857369, ECO:0000269) supports the cyclase function in lanomycin biosynthesis, and the EC classification under isomerases is assigned by curator inference (ECO:0000305). The sequence matches (337 aa, SHA256 confirmed). The GO annotation is electronic (IEA), not direct experimental, but the underlying experimental work supports the cyclase/isomerase classification.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can eliminate D (inward rectifier K+ channel) by noting the absence of the canonical Kir selectivity filter motif (T-V-G-Y-G) and the characteristic two-TM + pore-helix topology. One can eliminate C (polyubiquitin binding) by the absence of UBA, UIM, or NZF domains. However, distinguishing A (isomerase) from B (osmolarity-sensing channel) is difficult from sequence alone: the protein has a signal peptide and multiple hydrophobic stretches (consistent with both a terpene cyclase's hydrophobic substrate cavity and a membrane channel's TM helices). Positive identification as a terpene cyclase/isomerase requires recognizing DDxxD or NSE/DTE motifs (present but not canonical here) and knowing that cyclase activity falls under EC 5 (isomerases), which is specialized biochemical knowledge.


**Missing item-specific fact**

> Knowledge that this specific protein is a terpene cyclase (EC 5.4.99.-) involved in lanomycin biosynthesis, and that terpene cyclase/cyclase activity is classified under EC class 5 (Isomerases) rather than, e.g., lyase or ligase. Without this, the hydrophobic stretches and signal peptide are ambiguous between a secreted enzyme and a membrane channel.


**Reason**

> While elimination of D and C is achievable through general knowledge of Kir channel motifs and ubiquitin-binding domains, the remaining discrimination between A and B requires specialized knowledge of terpene cyclase biochemistry and EC classification. The sequence's hydrophobic stretches and signal peptide are genuinely ambiguous between a membrane-associated channel and a secreted enzyme with a hydrophobic active-site cavity. The answer depends on item-specific knowledge of this protein's identity and EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the database annotation and EC classification, A is the correct answer. B, C, and D are clearly incorrect for this protein (no channel topology, no ubiquitin-binding domain). No other option is defensible as the primary molecular function of a terpene cyclase.


### Important caveats

- The GO:0016853 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB keyword), not direct experimental evidence. The experimental paper (PubMed:33857369) supports the cyclase function but the isomerase EC classification is curator-inferred (ECO:0000305).
- The protein was only integrated into Swiss-Prot on 2025-02-05, so the author's source snapshot timing is uncertain relative to the benchmark construction.
- The sequence contains a signal peptide and multiple hydrophobic stretches that could mislead a model toward membrane/channel predictions, making the question harder than the answer's database simplicity suggests.
- The EC number 5.4.99.- is a placeholder for intramolecular transferases; the exact reaction is a cyclization, which is a structural rearrangement within one molecule, justifying the isomerase classification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can eliminate D (inward rectifier K+ channel) by noting the absence of the canonical Kir selectivity filter motif (T-V-G-Y-G) and the characteristic two-TM + pore-helix topology. One can eliminate C (polyubiquitin binding) by the absence of UBA, UIM, or NZF domains. However, distinguishing A (isomerase) from B (osmolarity-sensing channel) is difficult from sequence alone: the protein has a signal peptide and multiple hydrophobic stretches (consistent with both a terpene cyclase's hydrophobic substrate cavity and a membrane channel's TM helices). Positive identification as a terpene cyclase/isomerase requires recognizing DDxxD or NSE/DTE motifs (present but not canonical here) and knowing that cyclase activity falls under EC 5 (isomerases), which is specialized biochemical knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this specific protein is a terpene cyclase (EC 5.4.99.-) involved in lanomycin biosynthesis, and that terpene cyclase/cyclase activity is classified under EC class 5 (Isomerases) rather than, e.g., lyase or ligase. Without this, the hydrophobic stretches and signal peptide are ambiguous between a secreted enzyme and a membrane channel.",
    "reason": "While elimination of D and C is achievable through general knowledge of Kir channel motifs and ubiquitin-binding domains, the remaining discrimination between A and B requires specialized knowledge of terpene cyclase biochemistry and EC classification. The sequence's hydrophobic stretches and signal peptide are genuinely ambiguous between a membrane-associated channel and a secreted enzyme with a hydrophobic active-site cavity. The answer depends on item-specific knowledge of this protein's identity and EC assignment."
  },
  "case_id": "GO_molecular_function_0160",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW1 (LAN5_PYRDE) annotates this protein as a terpene cyclase with EC 5.4.99.- (intramolecular transferases, subclass of EC 5 = Isomerases). GO:0016853 'isomerase activity' is directly assigned via IEA:UniProtKB-KW. The experimental evidence (PubMed:33857369, ECO:0000269) supports the cyclase function in lanomycin biosynthesis, and the EC classification under isomerases is assigned by curator inference (ECO:0000305). The sequence matches (337 aa, SHA256 confirmed). The GO annotation is electronic (IEA), not direct experimental, but the underlying experimental work supports the cyclase/isomerase classification."
  },
  "important_caveats": [
    "The GO:0016853 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB keyword), not direct experimental evidence. The experimental paper (PubMed:33857369) supports the cyclase function but the isomerase EC classification is curator-inferred (ECO:0000305).",
    "The protein was only integrated into Swiss-Prot on 2025-02-05, so the author's source snapshot timing is uncertain relative to the benchmark construction.",
    "The sequence contains a signal peptide and multiple hydrophobic stretches that could mislead a model toward membrane/channel predictions, making the question harder than the answer's database simplicity suggests.",
    "The EC number 5.4.99.- is a placeholder for intramolecular transferases; the exact reaction is a cyclization, which is a structural rearrangement within one molecule, justifying the isomerase classification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the database annotation and EC classification, A is the correct answer. B, C, and D are clearly incorrect for this protein (no channel topology, no ubiquitin-binding domain). No other option is defensible as the primary molecular function of a terpene cyclase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0160",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW1 (LAN5_PYRDE) annotates this protein as a terpene cyclase with EC 5.4.99.- (intramolecular transferases, subclass of EC 5 = Isomerases). GO:0016853 'isomerase activity' is directly assigned via IEA:UniProtKB-KW. The experimental evidence (PubMed:33857369, ECO:0000269) supports the cyclase function in lanomycin biosynthesis, and the EC classification under isomerases is assigned by curator inference (ECO:0000305). The sequence matches (337 aa, SHA256 confirmed). The GO annotation is electronic (IEA), not direct experimental, but the underlying experimental work supports the cyclase/isomerase classification.",
    "evidence_ids": ["C4", "C5", "H1", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can eliminate D (inward rectifier K+ channel) by noting the absence of the canonical Kir selectivity filter motif (T-V-G-Y-G) and the characteristic two-TM + pore-helix topology. One can eliminate C (polyubiquitin binding) by the absence of UBA, UIM, or NZF domains. However, distinguishing A (isomerase) from B (osmolarity-sensing channel) is difficult from sequence alone: the protein has a signal peptide and multiple hydrophobic stretches (consistent with both a terpene cyclase's hydrophobic substrate cavity and a membrane channel's TM helices). Positive identification as a terpene cyclase/isomerase requires recognizing DDxxD or NSE/DTE motifs (present but not canonical here) and knowing that cyclase activity falls under EC 5 (isomerases), which is specialized biochemical knowledge.",
    "missing_item_specific_fact": "Knowledge that this specific protein is a terpene cyclase (EC 5.4.99.-) involved in lanomycin biosynthesis, and that terpene cyclase/cyclase activity is classified under EC class 5 (Isomerases) rather than, e.g., lyase or ligase. Without this, the hydrophobic stretches and signal peptide are ambiguous between a secreted enzyme and a membrane channel.",
    "reason": "While elimination of D and C is achievable through general knowledge of Kir channel motifs and ubiquitin-binding domains, the remaining discrimination between A and B requires specialized knowledge of terpene cyclase biochemistry and EC classification. The sequence's hydrophobic stretches and signal peptide are genuinely ambiguous between a membrane-associated channel and a secreted enzyme with a hydrophobic active-site cavity. The answer depends on item-specific knowledge of this protein's identity and EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the database annotation and EC classification, A is the correct answer. B, C, and D are clearly incorrect for this protein (no channel topology, no ubiquitin-binding domain). No other option is defensible as the primary molecular function of a terpene cyclase."
  },
  "important_caveats": [
    "The GO:0016853 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB keyword), not direct experimental evidence. The experimental paper (PubMed:33857369) supports the cyclase function but the isomerase EC classification is curator-inferred (ECO:0000305).",
    "The protein was only integrated into Swiss-Prot on 2025-02-05, so the author's source snapshot timing is uncertain relative to the benchmark construction.",
    "The sequence contains a signal peptide and multiple hydrophobic stretches that could mislead a model toward membrane/channel predictions, making the question harder than the answer's database simplicity suggests.",
    "The EC number 5.4.99.- is a placeholder for intramolecular transferases; the exact reaction is a cyclization, which is a structural rearrangement within one molecule, justifying the isomerase classification."
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

**Accession:** `P0DXW1` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
"P0DXW1"
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 5"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"5.4.99.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Terpene cyclase"}}}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:16.733133+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Cyclase; part of the gene cluster that mediates the biosynthesis of the tetrahydropyranyl antifungal agent lanomycin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:33857369). The biosynthesis probably begins with the formation of an hexaketide, followed by methionine mediated alkylation of C-2 and C-6, and methylation of the reduced C-3 oxygen, pyran forming reductive ring closure, oxygenation of C-4, beta-keto reduction, enoyl reduction and dehydration of the remaining oxygens, and finally, acylation with glycine to complete the biosynthesis (Probable)"}]}
```

Source SHA-256: `3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
ID   LAN5_PYRDE              Reviewed;         337 AA.
AC   P0DXW1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   09-APR-2025, entry version 2.
DE   RecName: Full=Terpene cyclase {ECO:0000303|PubMed:33857369};
DE            EC=5.4.99.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 5 {ECO:0000303|PubMed:33857369};
GN   Name=ORF5 {ECO:0000303|PubMed:33857369};
OS   Pyrenophora dematioidea (Helminthosporium dematioideum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;
OC   Pyrenophora.
OX   NCBI_TaxID=139229;
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 24-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
CC   -!- FUNCTION: Cyclase; part of the gene cluster that mediates the
CC       biosynthesis of the tetrahydropyranyl antifungal agent lanomycin that
CC       acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis
CC       (PubMed:33857369). The biosynthesis probably begins with the formation
CC       of an hexaketide, followed by methionine mediated alkylation of C-2 and
CC       C-6, and methylation of the reduced C-3 oxygen, pyran forming reductive
CC       ring closure, oxygenation of C-4, beta-keto reduction, enoyl reduction
CC       and dehydration of the remaining oxygens, and finally, acylation with
CC       glycine to complete the biosynthesis (Probable).
CC       {ECO:0000269|PubMed:33857369, ECO:0000305}.
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)  
**Locator:** `lines 45-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.266216+00:00.  

```text
DR   GO; GO:0016853; F:isomerase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704`.

### Evidence GO2

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 160. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
