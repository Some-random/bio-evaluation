# EC_number_0038

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.4.1.259

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MAPPAARARYIANKADNQILSKKPPKRPGLNGNNKTKEATPAGKKKDKDAKKRNQPTSGGQEKGLPNPIMPSVQTAFKTFVSARLCSAIWAYIADCDETFNYWEPLHYIINGHGLQTWEYSPQFGLRSYTYLLLQGVPGYFYQKLFNPSPILIFYMVRCMLGFGCAVMERYMYKSICQEFGIHIGRLWLIFQLFSVGMFVSSTALLPSSFSMYFGCAALAAWWQQNYCFAIFLTAISALLGWPFAALIGIPLVLEMLLRQRDWKTFVQWTLISGATVAIPMIAIDTSYFGKLTFAPLNIVWYNVFTSHGPNIFGTEPLSYYIINGFLNFNIIWLLALQLPIMLVIDYLIVPAKSKSTLNFPHYISLAPLYLWLLVFFAQPHKEERFLFPIYPLISLCGAITVDVYQRIFFRMKSVVFKIKAGVHYLDHSMFIAILVMVTSTLLGLSRVFALYRNYHAPMDLMLELNQFKATPQYDPDVIYNVCIGKDWHRYPGSFFFPAKNFRLRFLKSEFRGMLPAYYDEGQNATKVVQPYFNDLNQENEHMYFDYDRCDFLVDFDEGKYTALEPNYSKRSKDWSVMKSLPFLIPEKSHKVLRAFYVPFLTDNHIQYGDFNLLKRKTKRNGR

[Multiple Choices]
A. 2.4.1.392
B. 4.2.1.70
C. 2.4.1.259
D. 2.3.1.319
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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.

**Missing item-specific fact**

> Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.

**Reason**

> The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option.

### Important caveats

- The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.
- The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Alg9 record, which annotates EC 2.4.1.259 and describes the corresponding mannosyltransferase reaction. This support is transferred by similarity from Q9H6U8 (ECO:0000250), not evidence of direct experimental characterization of this exact protein.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a multipass membrane glycosyltransferase, but that broad inference does not determine its precise glycan substrate, reaction, or complete EC number.",
    "missing_item_specific_fact": "Identifying this protein as Alg9 and knowing its specific annotated mannosyltransferase activities requires protein-specific functional annotation or experimental knowledge absent from the input.",
    "reason": "The exact EC distinction among the choices depends on the specific reaction catalyzed, which cannot be established from the sequence and choices by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the evidence supports C. The matched record also annotates EC 2.4.1.261 for a second reaction, but that number is not offered as an option."
  },
  "important_caveats": [
    "The supporting EC annotations are similarity-based transfers, not direct experimental evidence for the supplied Drosophila protein.",
    "The exact author data snapshot is unknown, though the matched historical record available by the stated cutoff includes EC 2.4.1.259."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9VBV8`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 174. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
"Q9VBV8"
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"value":"2.4.1.259"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"value":"2.4.1.261"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0039293","source":"FlyBase"}],"value":"Alpha-1,2-mannosyltransferase Alg9"}}}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.193985+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.259","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9H6U8","source":"UniProtKB"}],"name":"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:29531"},{"database":"Rhea","id":"RHEA-COMP:19498"},{"database":"Rhea","id":"RHEA-COMP:19501"},{"database":"Rhea","id":"RHEA-COMP:19517"},{"database":"Rhea","id":"RHEA-COMP:19518"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57683"},{"database":"ChEBI","id":"CHEBI:58211"},{"database":"ChEBI","id":"CHEBI:132516"},{"database":"ChEBI","id":"CHEBI:132517"}]}}
```

Source SHA-256: `24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
ID   ALG9_DROME              Reviewed;         623 AA.
AC   Q9VBV8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 174.
DE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};
DE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};
DE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};
DE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
DE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};
GN   Name=Alg9 {ECO:0000312|FlyBase:FBgn0039293};
GN   ORFNames=CG11851 {ECO:0000312|FlyBase:FBgn0039293};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)  
**Locator:** `lines 104-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 174 / 1.  
**Retrieved:** 2026-11-01T06:28:51.427257+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-
CC         [alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-
CC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a
CC         di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-
CC         Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-
CC         alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-
CC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a
CC         di-trans,poly-cis-dolichyl phosphate + H(+); Xref=Rhea:RHEA:29531,
CC         Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501, Rhea:RHEA-COMP:19517,
CC         Rhea:RHEA-COMP:19518, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683,
CC         ChEBI:CHEBI:58211, ChEBI:CHEBI:132516, ChEBI:CHEBI:132517;
CC         EC=2.4.1.259; Evidence={ECO:0000250|UniProtKB:Q9H6U8};
```

Source SHA-256: `32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 38). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
