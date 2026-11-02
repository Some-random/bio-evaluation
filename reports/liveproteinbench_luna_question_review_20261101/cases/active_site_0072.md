# active_site_0072

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 26 (Proton donor/acceptor)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. Position 1156 (Proton donor; for dehydratase activity)
B. Position 350 (Nucleophile)
C. Position 26 (Proton donor/acceptor)
D. Position 242 (Charge relay system)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the 107-residue protein record, which annotates position 26 as an active-site proton donor/acceptor. The annotation cites a primary study that reports structural and mutagenesis work, although the annotation itself is curated evidence rather than a direct experimental result shown here.

Cited evidence: [C5](#evidence-c5), [C10](#evidence-c10), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 107 residues long, so options at positions 242, 350, and 1156 cannot refer to residues in this protein. Position 26 is in range and is histidine, a residue chemically compatible with proton donor/acceptor activity.

**Missing item-specific fact**

> The specific assignment of His26 as this enzyme's catalytic proton donor/acceptor is protein-specific and is not established by sequence chemistry alone.

**Reason**

> The out-of-range positions provide a concrete way to distinguish the listed options from the supplied sequence; the exact catalytic role is independently supported by reviewer-only annotation, not proven from the sequence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Only position 26 lies within the 107-residue sequence.

### Important caveats

- The database annotation and cited primary study support the expected answer, but the exact catalytic assignment is not inferable with certainty from the sequence alone.
- Reviewer-only source information was not supplied to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "active_site_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 107-residue protein record, which annotates position 26 as an active-site proton donor/acceptor. The annotation cites a primary study that reports structural and mutagenesis work, although the annotation itself is curated evidence rather than a direct experimental result shown here.",
    "evidence_ids": [
      "C5",
      "C10",
      "H4",
      "H2"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 107 residues long, so options at positions 242, 350, and 1156 cannot refer to residues in this protein. Position 26 is in range and is histidine, a residue chemically compatible with proton donor/acceptor activity.",
    "missing_item_specific_fact": "The specific assignment of His26 as this enzyme's catalytic proton donor/acceptor is protein-specific and is not established by sequence chemistry alone.",
    "reason": "The out-of-range positions provide a concrete way to distinguish the listed options from the supplied sequence; the exact catalytic role is independently supported by reviewer-only annotation, not proven from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 26 lies within the 107-residue sequence."
  },
  "important_caveats": [
    "The database annotation and cited primary study support the expected answer, but the exact catalytic assignment is not inferable with certainty from the sequence alone.",
    "Reviewer-only source information was not supplied to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `C5MR76`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 66. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"description":"Proton donor/acceptor","evidences":[{"evidenceCode":"ECO:0000305","id":"19801657","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":26},"start":{"modifier":"EXACT","value":26}},"type":"Active site"}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"citation":{"authors":["Marin M.","Heinz D.W.","Pieper D.H.","Klink B.U."],"citationCrossReferences":[{"database":"PubMed","id":"19801657"},{"database":"DOI","id":"10.1074/jbc.m109.024604"}],"citationType":"journal article","firstPage":"32709","id":"19801657","journal":"J. Biol. Chem.","lastPage":"32716","publicationDate":"2009","title":"Crystal structure and catalytic mechanism of 4-methylmuconolactone methylisomerase.","volume":"284"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ACR82080.1","source":"EMBL"},{"evidenceCode":"ECO:0007744","id":"3HDS","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3HF5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3HFK","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 18361 / CCUG 53116 / MT1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS) IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH 4-METHYLMUCONOLACTONE","FUNCTION","CATALYTIC ACTIVITY","PROPOSED REACTION MECHANISM","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","ACTIVE SITE","MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67"]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 18-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ACR82080.1, ECO:0007744|PDB:3HDS, ECO:0007744|PDB:3HF5, ECO:0007744|PDB:3HFK}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS)
RP   IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH
RP   4-METHYLMUCONOLACTONE, FUNCTION, CATALYTIC ACTIVITY, PROPOSED REACTION
RP   MECHANISM, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,
RP   DOMAIN, ACTIVE SITE, AND MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67.
RC   STRAIN=DSM 18361 / CCUG 53116 / MT1;
RX   PubMed=19801657; DOI=10.1074/jbc.m109.024604;
RA   Marin M., Heinz D.W., Pieper D.H., Klink B.U.;
RT   "Crystal structure and catalytic mechanism of 4-methylmuconolactone
RT   methylisomerase.";
RL   J. Biol. Chem. 284:32709-32716(2009).
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 115-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
FT   ACT_SITE        26
FT                   /note="Proton donor/acceptor"
FT                   /evidence="ECO:0000305|PubMed:19801657"
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json) (zero-based source row 72). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
