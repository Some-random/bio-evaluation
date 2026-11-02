# GO_molecular_function_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. alpha-1,2-mannosyltransferase activity
B. calcium-dependent phospholipid binding
C. tubulin deacetylase activity
D. endo-1,4-beta-xylanase activity
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

> The supplied sequence exactly matches the Botrytis cinerea EIX2 entry, which is annotated as an endo-1,4-beta-xylanase. The function is supported by similarity and a PROSITE-ProRule catalytic annotation; the GO assignment is IEA:UniProtKB-EC. This supports D, but the excerpts do not establish a direct experimental enzyme assay on this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a signal peptide, and the sequence lacks an obvious additional transmembrane segment. That favors a secreted protein such as a xylanase over the other choices’ typical membrane-associated or intracellular functions, but it does not by itself identify xylan as the substrate.


**Missing item-specific fact**

> Identifying the precise catalytic function requires protein-specific family or homology evidence linking this sequence to a xylanase, or a relevant experimental characterization; that link is not provided in the question.


**Reason**

> The sequence architecture offers a useful but non-specific localization clue. Distinguishing xylan hydrolysis from other possible secreted-protein activities depends on the protein-specific functional annotation or homology evidence, not on the signal peptide alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D, and none of the alternatives is comparably supported by the sequence or reviewer-only annotation.


### Important caveats

- The reviewer-only database accession and annotations were absent from the evaluated model input and support the key without making the question lookup-independent.
- The evidence distinguishes similarity-based and rule-based annotation from direct experimental evidence for catalytic activity of this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide, and the sequence lacks an obvious additional transmembrane segment. That favors a secreted protein such as a xylanase over the other choices’ typical membrane-associated or intracellular functions, but it does not by itself identify xylan as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the precise catalytic function requires protein-specific family or homology evidence linking this sequence to a xylanase, or a relevant experimental characterization; that link is not provided in the question.",
    "reason": "The sequence architecture offers a useful but non-specific localization clue. Distinguishing xylan hydrolysis from other possible secreted-protein activities depends on the protein-specific functional annotation or homology evidence, not on the signal peptide alone."
  },
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Botrytis cinerea EIX2 entry, which is annotated as an endo-1,4-beta-xylanase. The function is supported by similarity and a PROSITE-ProRule catalytic annotation; the GO assignment is IEA:UniProtKB-EC. This supports D, but the excerpts do not establish a direct experimental enzyme assay on this exact protein."
  },
  "important_caveats": [
    "The reviewer-only database accession and annotations were absent from the evaluated model input and support the key without making the question lookup-independent.",
    "The evidence distinguishes similarity-based and rule-based annotation from direct experimental evidence for catalytic activity of this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and none of the alternatives is comparably supported by the sequence or reviewer-only annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Botrytis cinerea EIX2 entry, which is annotated as an endo-1,4-beta-xylanase. The function is supported by similarity and a PROSITE-ProRule catalytic annotation; the GO assignment is IEA:UniProtKB-EC. This supports D, but the excerpts do not establish a direct experimental enzyme assay on this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide, and the sequence lacks an obvious additional transmembrane segment. That favors a secreted protein such as a xylanase over the other choices’ typical membrane-associated or intracellular functions, but it does not by itself identify xylan as the substrate.",
    "missing_item_specific_fact": "Identifying the precise catalytic function requires protein-specific family or homology evidence linking this sequence to a xylanase, or a relevant experimental characterization; that link is not provided in the question.",
    "reason": "The sequence architecture offers a useful but non-specific localization clue. Distinguishing xylan hydrolysis from other possible secreted-protein activities depends on the protein-specific functional annotation or homology evidence, not on the signal peptide alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and none of the alternatives is comparably supported by the sequence or reviewer-only annotation."
  },
  "important_caveats": [
    "The reviewer-only database accession and annotations were absent from the evaluated model input and support the key without making the question lookup-independent.",
    "The evidence distinguishes similarity-based and rule-based annotation from direct experimental evidence for catalytic activity of this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384K474 (EIX2_BOTFB, Botrytis cinerea B05.10) annotates this 222-aa protein as 'Ethylene-inducing xylanase 2' with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA-256 confirmed in both current and archived records). The EC assignment is via PROSITE-ProRule (ECO:0000255, computational), the GO term is IEA:UniProtKB-EC, and the FUNCTION comment is partly 'by similarity' (ECO:0000250|B3VSG7) with a supporting PubMed reference (33205907) that discusses EIX-like protein perception rather than direct xylanase assay of this specific protein. Nevertheless, the annotation chain (PROSITE-ProRule → EC → GO) and the by-similarity transfer from a characterized xylanase provide reasonable database-level support for choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple general biological arguments distinguish D from the other three choices: (1) Tubulin deacetylases (HDAC6, HDAC8) are zinc-dependent metalloenzymes typically >400–1000+ aa with conserved His/Asp/His zinc-binding motifs; a 222-aa protein lacking any zinc-binding signature cannot be a tubulin deacetylase, eliminating C. (2) Alpha-1,2-mannosyltransferases (ALG9, ALG11) are integral membrane proteins of the ER/Golgi with multiple transmembrane helices; the supplied sequence shows only an N-terminal signal peptide and no internal TM segments, arguing against a membrane-bound glycosyltransferase, weakening A. (3) Calcium-dependent phospholipid binding is characteristic of C2-domain proteins (synaptotagmins, PKCs, PLCs), which display a conserved β-sandwich with clusters of acidic residues in variable loops; the sequence lacks the C2-domain signature (consecutive Asp/Glu clusters in defined loop geometry), weakening B. (4) The remaining profile—~200 aa, N-terminal signal peptide, secreted, aromatic-rich (multiple W, Y, F residues typical of carbohydrate-binding clefts), and conserved Glu residues consistent with GH11 catalytic acid/base and nucleophile pairs—is coherent with a small secreted glycoside hydrolase of the xylanase type. Among the four options, D is the only one consistent with all these features simultaneously.


**Missing item-specific fact**

> Positive confirmation that the sequence belongs specifically to glycoside hydrolase family 11 (rather than another secreted hydrolase family) would require recognizing GH11-specific sub-motifs (e.g., the conserved 'GWTTG' and 'GWSENPLVEYY' patterns flanking the catalytic cleft). However, among the four given choices, the elimination reasoning is sufficient to single out D without needing to resolve GH11 vs. GH10 vs. GH43.


**Reason**

> The four choices span very different protein classes (membrane GT, C2-domain binder, large zinc metalloenzyme, small secreted hydrolase). General reasoning about protein size, topology, cofactor requirements, and domain architecture meaningfully eliminates A, B, and C, leaving D as the only viable option. The positive identification of xylanase activity specifically (vs. another secreted hydrolase) adds a layer of family-level knowledge, but the question's answer is still distinguishable by elimination from the provided choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and functionally distinct protein classes. Size (222 aa vs. >400 aa for HDACs), subcellular topology (secreted vs. membrane-bound vs. cytosolic), and cofactor requirements (no Ca2+ or Zn2+ signature) cleanly separate the choices. No two options are simultaneously plausible for this sequence.


### Important caveats

- The EC 3.2.1.8 assignment is computational (PROSITE-ProRule, ECO:0000255) and the GO annotation is IEA (inferred from EC). No direct enzymatic assay of xylan hydrolysis on this exact protein is cited in the evidence excerpts.
- The FUNCTION comment's 'by similarity' evidence (ECO:0000250|B3VSG7) means the xylanase activity is transferred from a homolog rather than demonstrated experimentally on this sequence.
- The PubMed reference (33205907) studies perception of EIX-like proteins by a plant receptor, not xylanase catalysis of this specific enzyme.
- The UniProt entry was first publicly released on 2025-06-18; the benchmark author's source snapshot date is unknown, though the historical archived version (entry version 25, released 2026-01-28) already carries the same annotation and matched sequence.
- The reviewer-only accession (A0A384K474) was inferred from dataset image-path metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple general biological arguments distinguish D from the other three choices: (1) Tubulin deacetylases (HDAC6, HDAC8) are zinc-dependent metalloenzymes typically >400–1000+ aa with conserved His/Asp/His zinc-binding motifs; a 222-aa protein lacking any zinc-binding signature cannot be a tubulin deacetylase, eliminating C. (2) Alpha-1,2-mannosyltransferases (ALG9, ALG11) are integral membrane proteins of the ER/Golgi with multiple transmembrane helices; the supplied sequence shows only an N-terminal signal peptide and no internal TM segments, arguing against a membrane-bound glycosyltransferase, weakening A. (3) Calcium-dependent phospholipid binding is characteristic of C2-domain proteins (synaptotagmins, PKCs, PLCs), which display a conserved β-sandwich with clusters of acidic residues in variable loops; the sequence lacks the C2-domain signature (consecutive Asp/Glu clusters in defined loop geometry), weakening B. (4) The remaining profile—~200 aa, N-terminal signal peptide, secreted, aromatic-rich (multiple W, Y, F residues typical of carbohydrate-binding clefts), and conserved Glu residues consistent with GH11 catalytic acid/base and nucleophile pairs—is coherent with a small secreted glycoside hydrolase of the xylanase type. Among the four options, D is the only one consistent with all these features simultaneously.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive confirmation that the sequence belongs specifically to glycoside hydrolase family 11 (rather than another secreted hydrolase family) would require recognizing GH11-specific sub-motifs (e.g., the conserved 'GWTTG' and 'GWSENPLVEYY' patterns flanking the catalytic cleft). However, among the four given choices, the elimination reasoning is sufficient to single out D without needing to resolve GH11 vs. GH10 vs. GH43.",
    "reason": "The four choices span very different protein classes (membrane GT, C2-domain binder, large zinc metalloenzyme, small secreted hydrolase). General reasoning about protein size, topology, cofactor requirements, and domain architecture meaningfully eliminates A, B, and C, leaving D as the only viable option. The positive identification of xylanase activity specifically (vs. another secreted hydrolase) adds a layer of family-level knowledge, but the question's answer is still distinguishable by elimination from the provided choices."
  },
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384K474 (EIX2_BOTFB, Botrytis cinerea B05.10) annotates this 222-aa protein as 'Ethylene-inducing xylanase 2' with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA-256 confirmed in both current and archived records). The EC assignment is via PROSITE-ProRule (ECO:0000255, computational), the GO term is IEA:UniProtKB-EC, and the FUNCTION comment is partly 'by similarity' (ECO:0000250|B3VSG7) with a supporting PubMed reference (33205907) that discusses EIX-like protein perception rather than direct xylanase assay of this specific protein. Nevertheless, the annotation chain (PROSITE-ProRule → EC → GO) and the by-similarity transfer from a characterized xylanase provide reasonable database-level support for choice D."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is computational (PROSITE-ProRule, ECO:0000255) and the GO annotation is IEA (inferred from EC). No direct enzymatic assay of xylan hydrolysis on this exact protein is cited in the evidence excerpts.",
    "The FUNCTION comment's 'by similarity' evidence (ECO:0000250|B3VSG7) means the xylanase activity is transferred from a homolog rather than demonstrated experimentally on this sequence.",
    "The PubMed reference (33205907) studies perception of EIX-like proteins by a plant receptor, not xylanase catalysis of this specific enzyme.",
    "The UniProt entry was first publicly released on 2025-06-18; the benchmark author's source snapshot date is unknown, though the historical archived version (entry version 25, released 2026-01-28) already carries the same annotation and matched sequence.",
    "The reviewer-only accession (A0A384K474) was inferred from dataset image-path metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct protein classes. Size (222 aa vs. >400 aa for HDACs), subcellular topology (secreted vs. membrane-bound vs. cytosolic), and cofactor requirements (no Ca2+ or Zn2+ signature) cleanly separate the choices. No two options are simultaneously plausible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384K474 (EIX2_BOTFB, Botrytis cinerea B05.10) annotates this 222-aa protein as 'Ethylene-inducing xylanase 2' with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA-256 confirmed in both current and archived records). The EC assignment is via PROSITE-ProRule (ECO:0000255, computational), the GO term is IEA:UniProtKB-EC, and the FUNCTION comment is partly 'by similarity' (ECO:0000250|B3VSG7) with a supporting PubMed reference (33205907) that discusses EIX-like protein perception rather than direct xylanase assay of this specific protein. Nevertheless, the annotation chain (PROSITE-ProRule → EC → GO) and the by-similarity transfer from a characterized xylanase provide reasonable database-level support for choice D.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple general biological arguments distinguish D from the other three choices: (1) Tubulin deacetylases (HDAC6, HDAC8) are zinc-dependent metalloenzymes typically >400–1000+ aa with conserved His/Asp/His zinc-binding motifs; a 222-aa protein lacking any zinc-binding signature cannot be a tubulin deacetylase, eliminating C. (2) Alpha-1,2-mannosyltransferases (ALG9, ALG11) are integral membrane proteins of the ER/Golgi with multiple transmembrane helices; the supplied sequence shows only an N-terminal signal peptide and no internal TM segments, arguing against a membrane-bound glycosyltransferase, weakening A. (3) Calcium-dependent phospholipid binding is characteristic of C2-domain proteins (synaptotagmins, PKCs, PLCs), which display a conserved β-sandwich with clusters of acidic residues in variable loops; the sequence lacks the C2-domain signature (consecutive Asp/Glu clusters in defined loop geometry), weakening B. (4) The remaining profile—~200 aa, N-terminal signal peptide, secreted, aromatic-rich (multiple W, Y, F residues typical of carbohydrate-binding clefts), and conserved Glu residues consistent with GH11 catalytic acid/base and nucleophile pairs—is coherent with a small secreted glycoside hydrolase of the xylanase type. Among the four options, D is the only one consistent with all these features simultaneously.",
    "missing_item_specific_fact": "Positive confirmation that the sequence belongs specifically to glycoside hydrolase family 11 (rather than another secreted hydrolase family) would require recognizing GH11-specific sub-motifs (e.g., the conserved 'GWTTG' and 'GWSENPLVEYY' patterns flanking the catalytic cleft). However, among the four given choices, the elimination reasoning is sufficient to single out D without needing to resolve GH11 vs. GH10 vs. GH43.",
    "reason": "The four choices span very different protein classes (membrane GT, C2-domain binder, large zinc metalloenzyme, small secreted hydrolase). General reasoning about protein size, topology, cofactor requirements, and domain architecture meaningfully eliminates A, B, and C, leaving D as the only viable option. The positive identification of xylanase activity specifically (vs. another secreted hydrolase) adds a layer of family-level knowledge, but the question's answer is still distinguishable by elimination from the provided choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct protein classes. Size (222 aa vs. >400 aa for HDACs), subcellular topology (secreted vs. membrane-bound vs. cytosolic), and cofactor requirements (no Ca2+ or Zn2+ signature) cleanly separate the choices. No two options are simultaneously plausible for this sequence."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is computational (PROSITE-ProRule, ECO:0000255) and the GO annotation is IEA (inferred from EC). No direct enzymatic assay of xylan hydrolysis on this exact protein is cited in the evidence excerpts.",
    "The FUNCTION comment's 'by similarity' evidence (ECO:0000250|B3VSG7) means the xylanase activity is transferred from a homolog rather than demonstrated experimentally on this sequence.",
    "The PubMed reference (33205907) studies perception of EIX-like proteins by a plant receptor, not xylanase catalysis of this specific enzyme.",
    "The UniProt entry was first publicly released on 2025-06-18; the benchmark author's source snapshot date is unknown, though the historical archived version (entry version 25, released 2026-01-28) already carries the same annotation and matched sequence.",
    "The reviewer-only accession (A0A384K474) was inferred from dataset image-path metadata and was not available to the evaluated model."
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

**Accession:** `A0A384K474` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
"A0A384K474"
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"entryVersion":27,"firstPublicDate":"2025-06-18","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2018-11-07","sequenceVersion":1}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX2"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX21"}]}}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"B3VSG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)"}]}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:59.392996+00:00.  

```json
{"database":"GO","id":"GO:0031176","properties":[{"key":"GoTerm","value":"F:endo-1,4-beta-xylanase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
ID   EIX2_BOTFB              Reviewed;         222 AA.
AC   A0A384K474;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 25.
DE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};
DE            Short=EIX21 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 60-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). May act as an elicitor of plant
CC       defense responses in certain plants but does not exhibit any cell death
CC       when transiently expressed in N.benthamiana (PubMed:33205907).
CC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 67-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:01.435228+00:00.  

```text
DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 173997-174018`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031176
name: endo-1,4-beta-xylanase activity
namespace: molecular_function
def: "Catalysis of the endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans." [EC:3.2.1.8]
synonym: "1,4-beta-D-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "1,4-beta-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1,4)-beta-xylanase(1,4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1->4)-beta-xylanase(1->4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "xylanase" BROAD [EC:3.2.1.8]
xref: EC:3.2.1.8
xref: MetaCyc:3.2.1.8-RXN
is_a: GO:0097599 ! xylanase activity
property_value: skos:exactMatch EC:3.2.1.8

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
