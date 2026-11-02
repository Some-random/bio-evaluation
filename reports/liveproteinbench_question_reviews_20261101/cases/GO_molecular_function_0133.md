# GO_molecular_function_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — G protein-coupled receptor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEVSNMTTVTVFILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTDSHLCTPMYFFLRQLSFLDAFYSSIIVPKLLENLLSKGETISFLECFTQISLVIFSGATEACLLSVMAYDRFQAMCHPLLYVVIINRRVCAGLVGASWAIGMGTGLINTLLLAQQHFCGPNVIHSFACELPPVLLLTCSDPCASIVSILTTMSVLGLGTLVLLLGSYSCIIMTALRINSATGRSKIFSTCSSHFLVVTIFYTSGVLRYMIPASGSALEQVLSVQYSVITPLLNPLIYSLKSQEVKVALRRMLARKSRLPL

[Multiple Choices]
A. quercetin 7-O-glucosyltransferase activity
B. G protein-coupled receptor activity
C. histone crotonyltransferase activity
D. peptidase inhibitor activity
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

> The exact sequence matches a UniProt entry annotated as an odorant receptor and as having G protein-coupled receptor activity. The GO annotation is computationally inferred, not direct experimental evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a roughly 300-residue protein dominated by multiple hydrophobic segments, consistent with a seven-transmembrane receptor such as an olfactory GPCR. The other choices describe catalytic enzymes or a peptidase inhibitor and do not fit that membrane-protein architecture.


**Missing item-specific fact**

> No item-specific annotation is needed to distinguish the broad GPCR choice from these alternatives; the exact receptor identity or ligand would require additional information.


**Reason**

> The sequence architecture and the strong contrast among the choices provide a meaningful biological basis for selecting B, without relying on recognizing the exact sequence or recalling its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, GPCR activity best fits the sequence’s multi-pass membrane-receptor architecture.


### Important caveats

- The supporting GO and UniProt annotations are computationally inferred; the supplied evidence does not establish direct experimental validation of this specific protein's receptor activity.
- The annotation sources match the sequence, but their historical snapshot does not establish which source the benchmark author used.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a roughly 300-residue protein dominated by multiple hydrophobic segments, consistent with a seven-transmembrane receptor such as an olfactory GPCR. The other choices describe catalytic enzymes or a peptidase inhibitor and do not fit that membrane-protein architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish the broad GPCR choice from these alternatives; the exact receptor identity or ligand would require additional information.",
    "reason": "The sequence architecture and the strong contrast among the choices provide a meaningful biological basis for selecting B, without relying on recognizing the exact sequence or recalling its database entry."
  },
  "case_id": "GO_molecular_function_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as an odorant receptor and as having G protein-coupled receptor activity. The GO annotation is computationally inferred, not direct experimental evidence."
  },
  "important_caveats": [
    "The supporting GO and UniProt annotations are computationally inferred; the supplied evidence does not establish direct experimental validation of this specific protein's receptor activity.",
    "The annotation sources match the sequence, but their historical snapshot does not establish which source the benchmark author used."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, GPCR activity best fits the sequence’s multi-pass membrane-receptor architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as an odorant receptor and as having G protein-coupled receptor activity. The GO annotation is computationally inferred, not direct experimental evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a roughly 300-residue protein dominated by multiple hydrophobic segments, consistent with a seven-transmembrane receptor such as an olfactory GPCR. The other choices describe catalytic enzymes or a peptidase inhibitor and do not fit that membrane-protein architecture.",
    "missing_item_specific_fact": "No item-specific annotation is needed to distinguish the broad GPCR choice from these alternatives; the exact receptor identity or ligand would require additional information.",
    "reason": "The sequence architecture and the strong contrast among the choices provide a meaningful biological basis for selecting B, without relying on recognizing the exact sequence or recalling its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, GPCR activity best fits the sequence’s multi-pass membrane-receptor architecture."
  },
  "important_caveats": [
    "The supporting GO and UniProt annotations are computationally inferred; the supplied evidence does not establish direct experimental validation of this specific protein's receptor activity.",
    "The annotation sources match the sequence, but their historical snapshot does not establish which source the benchmark author used."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A2R8YED5 (O5BS1_HUMAN, Olfactory receptor 5BS1, 311 AA, SHA256 confirmed). UniProt annotates GO:0004930 (G protein-coupled receptor activity) via IEA:InterPro/UniProtKB-KW, and the protein is described as an 'Odorant receptor' (ECO:0000305). Olfactory receptors are the largest subfamily of Class A GPCRs; the GPCR annotation is a well-established family-level assignment. The other options (plant glucosyltransferase, nuclear crotonyltransferase, peptidase inhibitor) are entirely incompatible with a 7TM membrane receptor.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 311-residue sequence contains approximately seven long hydrophobic stretches (e.g., FILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTD; IINRRVCAGLVGASWAIGMGTGLINTLLLA; ILTTMSVLGLGTLVLLLGSYSCIIMTALRINS; etc.) separated by shorter hydrophilic loops, producing the canonical 7-transmembrane topology of Class A GPCRs. Conserved GPCR motifs are recognizable: an NPxxY-like motif (NPLIYSLK near the C-terminal end) and a DRY-like region. The overall length (~310–350 aa) and hydrophobicity profile are hallmarks of olfactory GPCRs. By contrast, quercetin 7-O-glucosyltransferase (a plant UDP-sugar–dependent enzyme, ~400–500 aa, soluble), histone crotonyltransferase (a nuclear acetyltransferase-fold enzyme), and peptidase inhibitor activity (typically small soluble proteins <100 aa with specific inhibitor folds) are all architecturally incompatible with a 7TM integral membrane protein. General knowledge that the only major protein superfamily with 7TM architecture is the GPCR superfamily allows elimination of A, C, and D.


**Missing item-specific fact**

> None critical. Exact identification as OR5BS1 would require database lookup, but the 7TM architecture and GPCR-typical motifs are discernible from the sequence and general structural biology knowledge.


**Reason**

> The sequence's seven hydrophobic transmembrane segments, ~311-aa length, and conserved GPCR motifs (NPxxY-like, DRY-like) constitute concrete, sequence-visible evidence for a 7TM receptor. The three distractors describe soluble enzymes or small inhibitors whose domain architectures and cellular localizations are fundamentally incompatible with the observed hydrophobicity pattern. A biologist with general knowledge of protein architecture can distinguish B from A/C/D without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span entirely different protein classes (plant glycosyltransferase, 7TM receptor, nuclear acyltransferase, small inhibitor). The 7TM topology visible in the sequence uniquely selects B. No other option is architecturally plausible for this sequence.


### Important caveats

- The GO:0004930 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB keyword, not direct experimental measurement. However, the GPCR classification of olfactory receptors is a well-established family-level fact supported by extensive structural and pharmacological literature.
- The UniProt entry was first publicly released on 2025-02-05 and reviewed (Swiss-Prot) on 2026-01-28; the benchmark author's source snapshot date is unknown but the sequence matches across checked versions.
- The more specific GO term GO:0004984 (olfactory receptor activity) is also annotated (IBA:GO_Central), but it is not offered as a distractor, so it does not create ambiguity among the given choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 311-residue sequence contains approximately seven long hydrophobic stretches (e.g., FILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTD; IINRRVCAGLVGASWAIGMGTGLINTLLLA; ILTTMSVLGLGTLVLLLGSYSCIIMTALRINS; etc.) separated by shorter hydrophilic loops, producing the canonical 7-transmembrane topology of Class A GPCRs. Conserved GPCR motifs are recognizable: an NPxxY-like motif (NPLIYSLK near the C-terminal end) and a DRY-like region. The overall length (~310–350 aa) and hydrophobicity profile are hallmarks of olfactory GPCRs. By contrast, quercetin 7-O-glucosyltransferase (a plant UDP-sugar–dependent enzyme, ~400–500 aa, soluble), histone crotonyltransferase (a nuclear acetyltransferase-fold enzyme), and peptidase inhibitor activity (typically small soluble proteins <100 aa with specific inhibitor folds) are all architecturally incompatible with a 7TM integral membrane protein. General knowledge that the only major protein superfamily with 7TM architecture is the GPCR superfamily allows elimination of A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Exact identification as OR5BS1 would require database lookup, but the 7TM architecture and GPCR-typical motifs are discernible from the sequence and general structural biology knowledge.",
    "reason": "The sequence's seven hydrophobic transmembrane segments, ~311-aa length, and conserved GPCR motifs (NPxxY-like, DRY-like) constitute concrete, sequence-visible evidence for a 7TM receptor. The three distractors describe soluble enzymes or small inhibitors whose domain architectures and cellular localizations are fundamentally incompatible with the observed hydrophobicity pattern. A biologist with general knowledge of protein architecture can distinguish B from A/C/D without memorizing this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2R8YED5 (O5BS1_HUMAN, Olfactory receptor 5BS1, 311 AA, SHA256 confirmed). UniProt annotates GO:0004930 (G protein-coupled receptor activity) via IEA:InterPro/UniProtKB-KW, and the protein is described as an 'Odorant receptor' (ECO:0000305). Olfactory receptors are the largest subfamily of Class A GPCRs; the GPCR annotation is a well-established family-level assignment. The other options (plant glucosyltransferase, nuclear crotonyltransferase, peptidase inhibitor) are entirely incompatible with a 7TM membrane receptor."
  },
  "important_caveats": [
    "The GO:0004930 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB keyword, not direct experimental measurement. However, the GPCR classification of olfactory receptors is a well-established family-level fact supported by extensive structural and pharmacological literature.",
    "The UniProt entry was first publicly released on 2025-02-05 and reviewed (Swiss-Prot) on 2026-01-28; the benchmark author's source snapshot date is unknown but the sequence matches across checked versions.",
    "The more specific GO term GO:0004984 (olfactory receptor activity) is also annotated (IBA:GO_Central), but it is not offered as a distractor, so it does not create ambiguity among the given choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different protein classes (plant glycosyltransferase, 7TM receptor, nuclear acyltransferase, small inhibitor). The 7TM topology visible in the sequence uniquely selects B. No other option is architecturally plausible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A2R8YED5 (O5BS1_HUMAN, Olfactory receptor 5BS1, 311 AA, SHA256 confirmed). UniProt annotates GO:0004930 (G protein-coupled receptor activity) via IEA:InterPro/UniProtKB-KW, and the protein is described as an 'Odorant receptor' (ECO:0000305). Olfactory receptors are the largest subfamily of Class A GPCRs; the GPCR annotation is a well-established family-level assignment. The other options (plant glucosyltransferase, nuclear crotonyltransferase, peptidase inhibitor) are entirely incompatible with a 7TM membrane receptor.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 311-residue sequence contains approximately seven long hydrophobic stretches (e.g., FILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTD; IINRRVCAGLVGASWAIGMGTGLINTLLLA; ILTTMSVLGLGTLVLLLGSYSCIIMTALRINS; etc.) separated by shorter hydrophilic loops, producing the canonical 7-transmembrane topology of Class A GPCRs. Conserved GPCR motifs are recognizable: an NPxxY-like motif (NPLIYSLK near the C-terminal end) and a DRY-like region. The overall length (~310–350 aa) and hydrophobicity profile are hallmarks of olfactory GPCRs. By contrast, quercetin 7-O-glucosyltransferase (a plant UDP-sugar–dependent enzyme, ~400–500 aa, soluble), histone crotonyltransferase (a nuclear acetyltransferase-fold enzyme), and peptidase inhibitor activity (typically small soluble proteins <100 aa with specific inhibitor folds) are all architecturally incompatible with a 7TM integral membrane protein. General knowledge that the only major protein superfamily with 7TM architecture is the GPCR superfamily allows elimination of A, C, and D.",
    "missing_item_specific_fact": "None critical. Exact identification as OR5BS1 would require database lookup, but the 7TM architecture and GPCR-typical motifs are discernible from the sequence and general structural biology knowledge.",
    "reason": "The sequence's seven hydrophobic transmembrane segments, ~311-aa length, and conserved GPCR motifs (NPxxY-like, DRY-like) constitute concrete, sequence-visible evidence for a 7TM receptor. The three distractors describe soluble enzymes or small inhibitors whose domain architectures and cellular localizations are fundamentally incompatible with the observed hydrophobicity pattern. A biologist with general knowledge of protein architecture can distinguish B from A/C/D without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span entirely different protein classes (plant glycosyltransferase, 7TM receptor, nuclear acyltransferase, small inhibitor). The 7TM topology visible in the sequence uniquely selects B. No other option is architecturally plausible for this sequence."
  },
  "important_caveats": [
    "The GO:0004930 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB keyword, not direct experimental measurement. However, the GPCR classification of olfactory receptors is a well-established family-level fact supported by extensive structural and pharmacological literature.",
    "The UniProt entry was first publicly released on 2025-02-05 and reviewed (Swiss-Prot) on 2026-01-28; the benchmark author's source snapshot date is unknown but the sequence matches across checked versions.",
    "The more specific GO term GO:0004984 (olfactory receptor activity) is also annotated (IBA:GO_Central), but it is not offered as a distractor, so it does not create ambiguity among the given choices."
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

**Accession:** `A0A2R8YED5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
"A0A2R8YED5"
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"HGNC:19627","source":"HGNC"}],"value":"Olfactory receptor family 5 subfamily BS member 1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Olfactory receptor 5BS1"}}}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Odorant receptor"}]}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"database":"GO","id":"GO:0004930","properties":[{"key":"GoTerm","value":"F:G protein-coupled receptor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
ID   O5BS1_HUMAN             Reviewed;         311 AA.
AC   A0A2R8YED5; Q8NH44;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-JUN-2018, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=Olfactory receptor 5BS1 {ECO:0000305};
DE   AltName: Full=Olfactory receptor family 5 subfamily BS member 1 {ECO:0000312|HGNC:HGNC:19627};
GN   Name=OR5BS1 {ECO:0000312|HGNC:HGNC:19627};
GN   Synonyms=OR5BS1P {ECO:0000312|HGNC:HGNC:19627};
OS   Homo sapiens (Human).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;
OC   Homo.
OX   NCBI_TaxID=9606;
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 76-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
CC   -!- FUNCTION: Odorant receptor. {ECO:0000305}.
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
DR   GO; GO:0004930; F:G protein-coupled receptor activity; IEA:UniProtKB-KW.
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 52078-52112`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004930
name: G protein-coupled receptor activity
namespace: molecular_function
alt_id: GO:0001622
alt_id: GO:0001623
alt_id: GO:0001624
alt_id: GO:0001625
alt_id: GO:0016526
def: "Combining with an extracellular signal and transmitting the signal across the membrane by activating an associated G-protein; promotes the exchange of GDP for GTP on the alpha subunit of a heterotrimeric G-protein complex." [GOC:bf, Wikipedia:GPCR]
subset: goslim_chembl
synonym: "EBV-induced receptor" NARROW []
synonym: "Epstein-Barr Virus-induced receptor activity" NARROW []
synonym: "G protein coupled receptor activity" EXACT []
synonym: "G protein linked receptor activity" EXACT []
synonym: "G-protein coupled receptor activity" EXACT []
synonym: "G-protein coupled receptor activity, unknown ligand" NARROW []
synonym: "G-protein linked receptor activity" EXACT []
synonym: "GPCR activity" EXACT []
synonym: "ligand-dependent GPCR activity" EXACT []
synonym: "Mas proto-oncogene receptor activity" NARROW []
synonym: "orphan G protein coupled receptor activity" NARROW []
synonym: "orphan G-protein coupled receptor activity" NARROW []
synonym: "orphan GPCR activity" NARROW []
synonym: "RDC1 receptor activity" NARROW []
synonym: "receptor activity, G-protein coupled" EXACT [GOC:bf]
synonym: "SREB receptor" NARROW []
synonym: "super conserved receptor expressed in brain receptor activity" NARROW []
xref: Reactome:R-HSA-114552 "Thrombin-activated PARs activate G12/13"
xref: Reactome:R-HSA-114558 "Thrombin-activated PARs activate Gq"
xref: Reactome:R-HSA-167408 "The high affinity receptor complex binds to G-protein"
xref: Reactome:R-HSA-381706 "GLP1R:GLP1 activates G(s)"
xref: Wikipedia:GPCR
is_a: GO:0004888 ! transmembrane signaling receptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
