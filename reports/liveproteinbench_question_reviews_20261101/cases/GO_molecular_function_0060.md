# GO_molecular_function_0060

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — ubiquitin-like protein transferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MISAPSPDHLLLEQDLATPEIRCGEIEERWRHIRTSWPHVFFAVSAPQRPNGPKEFGFRFEYTGYRQTPVTAQLWDLEADAPLPHAKWPTGTYVVPSVFRKDWQQGNCLYIPCDRISIQGHTAWLNDHPSRLWQPARGIICYLEQLYELFNQGDYTGLVSA

[Multiple Choices]
A. peptidyl-lysine 3-dioxygenase activity
B. ubiquitin-like protein transferase activity
C. potassium channel regulator activity
D. enzyme activator activity
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

> The sequence exactly matches the UniProt record for BilB. That record describes BilB as an E2-like enzyme that transfers a ubiquitin-like moiety to target proteins, and annotates ubiquitin-like protein transferase activity with IDA evidence. This supports choice B for the supplied sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The short sequence might permit family-level clues, but the input gives no organism, pathway, substrate, or functional context that establishes BilB's role in the Bil system. The particular transferase function is not meaningfully distinguished from the choices by a concrete argument available from the supplied input alone.


**Missing item-specific fact**

> That this particular protein is BilB, an E2-like component of a bacterial ubiquitin-like protein conjugation system, and transfers the ubiquitin-like moiety to target proteins.


**Reason**

> The key is supported by protein-specific annotation and experimental evidence, but those facts are absent from the evaluated input. Recognizing or retrieving the exact protein's identity and function would be lookup or memorization, not reasoning from the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; no other listed choice is supported as a molecular function of this protein.


### Important caveats

- The UniProt record and GO annotation match the supplied sequence, but the exact source snapshot used by the author is unknown.
- The protein-specific functional evidence is reviewer-only and was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence might permit family-level clues, but the input gives no organism, pathway, substrate, or functional context that establishes BilB's role in the Bil system. The particular transferase function is not meaningfully distinguished from the choices by a concrete argument available from the supplied input alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein is BilB, an E2-like component of a bacterial ubiquitin-like protein conjugation system, and transfers the ubiquitin-like moiety to target proteins.",
    "reason": "The key is supported by protein-specific annotation and experimental evidence, but those facts are absent from the evaluated input. Recognizing or retrieving the exact protein's identity and function would be lookup or memorization, not reasoning from the supplied sequence and choices."
  },
  "case_id": "GO_molecular_function_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record for BilB. That record describes BilB as an E2-like enzyme that transfers a ubiquitin-like moiety to target proteins, and annotates ubiquitin-like protein transferase activity with IDA evidence. This supports choice B for the supplied sequence."
  },
  "important_caveats": [
    "The UniProt record and GO annotation match the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The protein-specific functional evidence is reviewer-only and was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no other listed choice is supported as a molecular function of this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record for BilB. That record describes BilB as an E2-like enzyme that transfers a ubiquitin-like moiety to target proteins, and annotates ubiquitin-like protein transferase activity with IDA evidence. This supports choice B for the supplied sequence.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The short sequence might permit family-level clues, but the input gives no organism, pathway, substrate, or functional context that establishes BilB's role in the Bil system. The particular transferase function is not meaningfully distinguished from the choices by a concrete argument available from the supplied input alone.",
    "missing_item_specific_fact": "That this particular protein is BilB, an E2-like component of a bacterial ubiquitin-like protein conjugation system, and transfers the ubiquitin-like moiety to target proteins.",
    "reason": "The key is supported by protein-specific annotation and experimental evidence, but those facts are absent from the evaluated input. Recognizing or retrieving the exact protein's identity and function would be lookup or memorization, not reasoning from the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no other listed choice is supported as a molecular function of this protein."
  },
  "important_caveats": [
    "The UniProt record and GO annotation match the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The protein-specific functional evidence is reviewer-only and was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A1I1NU27 (sequence SHA256 match confirmed) is annotated with GO:0019787 'ubiquitin-like protein transferase activity' with evidence code IDA:UniProtKB, supported by experimental data from Hoer et al. (Nature 2024, PMID:39020165). The protein is named 'Bacterial E2-like ubiquitin protein BilB' (EC 2.3.2.-) and functions as the E2 component of the Bil conjugation system, catalyzing covalent attachment of a ubiquitin-like moiety (BilA) to phage target proteins. The GO term matches option B exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination reasoning is possible: the sequence lacks 2-oxoglutarate-dependent dioxygenase motifs (rules out A), lacks transmembrane or ion-channel-binding features (rules out C), and the GO definition of enzyme activator activity (GO:0008047) explicitly excludes covalent modification, which is inconsistent with a transferase mechanism (weakly argues against D). However, positively identifying the protein as specifically a 'ubiquitin-like protein transferase' requires recognizing the UBC/E2 fold from a 161-residue bacterial sequence with a catalytic Cys-113, or knowing the Bil system (described only in 2024). The UBC fold is not trivially identifiable from primary sequence text without structural context or database comparison.


**Missing item-specific fact**

> The specific identity of this protein as BilB (E2 of the bacterial ISG15-like Bil antiviral system, described in Hoer et al. Nature 2024) and recognition of the E2/UBC catalytic fold from this particular bacterial sequence. Without prior knowledge of this novel 2024 system or the ability to computationally match the UBC fold, a model cannot positively assign 'ubiquitin-like protein transferase activity' over other small Cys-containing protein functions.


**Reason**

> While elimination of A and C is feasible through general motif knowledge, the positive identification of B requires either recognizing the exact sequence (lookup), knowing the 2024 Bil system publication, or identifying the UBC fold from primary sequence alone—which is a specialized structural biology skill not achievable from the text sequence without tools. The bacterial context further makes E2 identification non-obvious. The question effectively tests knowledge of a very recently characterized, protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct GO terms: dioxygenase (A), transferase (B), channel regulator (C), and enzyme activator (D). The GO definitions are mutually exclusive in practice. Option D is explicitly excluded by the GO definition (no covalent modification allowed), and A/C lack any sequence support. No two options are simultaneously defensible.


### Important caveats

- The Bil system was described in a single 2024 Nature paper (Hoer et al.); this is an extremely novel annotation with limited literature.
- The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental support, not purely computational inference.
- The protein is bacterial, making E2-like activity unusual and harder to predict from general biological priors that associate E2 enzymes primarily with eukaryotes.
- The reviewer-only evidence confirms sequence match and annotation but was absent from the evaluated model input; the model had only the raw sequence and four options.
- The catalytic Cys-113 (confirmed by mutagenesis in the reference) is present in the sequence, but recognizing it as an E2 catalytic residue without fold-level knowledge is very difficult.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination reasoning is possible: the sequence lacks 2-oxoglutarate-dependent dioxygenase motifs (rules out A), lacks transmembrane or ion-channel-binding features (rules out C), and the GO definition of enzyme activator activity (GO:0008047) explicitly excludes covalent modification, which is inconsistent with a transferase mechanism (weakly argues against D). However, positively identifying the protein as specifically a 'ubiquitin-like protein transferase' requires recognizing the UBC/E2 fold from a 161-residue bacterial sequence with a catalytic Cys-113, or knowing the Bil system (described only in 2024). The UBC fold is not trivially identifiable from primary sequence text without structural context or database comparison.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as BilB (E2 of the bacterial ISG15-like Bil antiviral system, described in Hoer et al. Nature 2024) and recognition of the E2/UBC catalytic fold from this particular bacterial sequence. Without prior knowledge of this novel 2024 system or the ability to computationally match the UBC fold, a model cannot positively assign 'ubiquitin-like protein transferase activity' over other small Cys-containing protein functions.",
    "reason": "While elimination of A and C is feasible through general motif knowledge, the positive identification of B requires either recognizing the exact sequence (lookup), knowing the 2024 Bil system publication, or identifying the UBC fold from primary sequence alone—which is a specialized structural biology skill not achievable from the text sequence without tools. The bacterial context further makes E2 identification non-obvious. The question effectively tests knowledge of a very recently characterized, protein-specific annotation."
  },
  "case_id": "GO_molecular_function_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1NU27 (sequence SHA256 match confirmed) is annotated with GO:0019787 'ubiquitin-like protein transferase activity' with evidence code IDA:UniProtKB, supported by experimental data from Hoer et al. (Nature 2024, PMID:39020165). The protein is named 'Bacterial E2-like ubiquitin protein BilB' (EC 2.3.2.-) and functions as the E2 component of the Bil conjugation system, catalyzing covalent attachment of a ubiquitin-like moiety (BilA) to phage target proteins. The GO term matches option B exactly."
  },
  "important_caveats": [
    "The Bil system was described in a single 2024 Nature paper (Hoer et al.); this is an extremely novel annotation with limited literature.",
    "The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental support, not purely computational inference.",
    "The protein is bacterial, making E2-like activity unusual and harder to predict from general biological priors that associate E2 enzymes primarily with eukaryotes.",
    "The reviewer-only evidence confirms sequence match and annotation but was absent from the evaluated model input; the model had only the raw sequence and four options.",
    "The catalytic Cys-113 (confirmed by mutagenesis in the reference) is present in the sequence, but recognizing it as an E2 catalytic residue without fold-level knowledge is very difficult."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct GO terms: dioxygenase (A), transferase (B), channel regulator (C), and enzyme activator (D). The GO definitions are mutually exclusive in practice. Option D is explicitly excluded by the GO definition (no covalent modification allowed), and A/C lack any sequence support. No two options are simultaneously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A1I1NU27 (sequence SHA256 match confirmed) is annotated with GO:0019787 'ubiquitin-like protein transferase activity' with evidence code IDA:UniProtKB, supported by experimental data from Hoer et al. (Nature 2024, PMID:39020165). The protein is named 'Bacterial E2-like ubiquitin protein BilB' (EC 2.3.2.-) and functions as the E2 component of the Bil conjugation system, catalyzing covalent attachment of a ubiquitin-like moiety (BilA) to phage target proteins. The GO term matches option B exactly.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination reasoning is possible: the sequence lacks 2-oxoglutarate-dependent dioxygenase motifs (rules out A), lacks transmembrane or ion-channel-binding features (rules out C), and the GO definition of enzyme activator activity (GO:0008047) explicitly excludes covalent modification, which is inconsistent with a transferase mechanism (weakly argues against D). However, positively identifying the protein as specifically a 'ubiquitin-like protein transferase' requires recognizing the UBC/E2 fold from a 161-residue bacterial sequence with a catalytic Cys-113, or knowing the Bil system (described only in 2024). The UBC fold is not trivially identifiable from primary sequence text without structural context or database comparison.",
    "missing_item_specific_fact": "The specific identity of this protein as BilB (E2 of the bacterial ISG15-like Bil antiviral system, described in Hoer et al. Nature 2024) and recognition of the E2/UBC catalytic fold from this particular bacterial sequence. Without prior knowledge of this novel 2024 system or the ability to computationally match the UBC fold, a model cannot positively assign 'ubiquitin-like protein transferase activity' over other small Cys-containing protein functions.",
    "reason": "While elimination of A and C is feasible through general motif knowledge, the positive identification of B requires either recognizing the exact sequence (lookup), knowing the 2024 Bil system publication, or identifying the UBC fold from primary sequence alone—which is a specialized structural biology skill not achievable from the text sequence without tools. The bacterial context further makes E2 identification non-obvious. The question effectively tests knowledge of a very recently characterized, protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct GO terms: dioxygenase (A), transferase (B), channel regulator (C), and enzyme activator (D). The GO definitions are mutually exclusive in practice. Option D is explicitly excluded by the GO definition (no covalent modification allowed), and A/C lack any sequence support. No two options are simultaneously defensible."
  },
  "important_caveats": [
    "The Bil system was described in a single 2024 Nature paper (Hoer et al.); this is an extremely novel annotation with limited literature.",
    "The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental support, not purely computational inference.",
    "The protein is bacterial, making E2-like activity unusual and harder to predict from general biological priors that associate E2 enzymes primarily with eukaryotes.",
    "The reviewer-only evidence confirms sequence match and annotation but was absent from the evaluated model input; the model had only the raw sequence and four options.",
    "The catalytic Cys-113 (confirmed by mutagenesis in the reference) is present in the sequence, but recognizing it as an E2 catalytic residue without fold-level knowledge is very difficult."
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

**Accession:** `A0A1I1NU27` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 11. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:36.666780+00:00.  

```json
"A0A1I1NU27"
```

Source SHA-256: `dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:36.666780+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"E2 ubiquitin-conjugating enzyme BilB"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39020165","source":"PubMed"}],"value":"2.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39020165","source":"PubMed"}],"value":"Bacterial E2-like ubiquitin protein BilB"}}}
```

Source SHA-256: `dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:36.666780+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39020165","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"39020165","source":"PubMed"}],"value":"Component of the Bil (bacterial ISG15-like) antiviral defense system, composed of BilA, BilB, BilC and BilD. The Bil system specifically conjugates a ubiquitin-like moiety (bilA) to the bacteriophage central tail fiber (CTF, or tip attachment protein J) via reactions involving E1 (bilD) and E2 (bilB). Modifies CTF of phage SECphi27 and SECphi4, which probably interferes with assembly of the phage tail. Also modifies T5 baseplate hub protein pb3 (gene D16), but not gp27 of phage T6 (Bil defends against T6). BilB probably accepts ubiquitin from the BilA-BilD (E1) complex and catalyzes its covalent attachment to target protein (CTF) (Probable) (PubMed:39020165). Bil-encoding bacteria produce mostly defective phage SECphi27, many of which have phage assembly defects, including no tails. SECphi27 phage progeny produced in E.coli with the Bil system inject less DNA into naive host cells, maybe because the phage are less able to adsorb and inject their DNA into host cells"}]}
```

Source SHA-256: `dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:36.666780+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39020165","source":"PubMed"}],"id":"GO:0019787","properties":[{"key":"GoTerm","value":"F:ubiquitin-like protein transferase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU27.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:36.666780+00:00.  

```json
{"citation":{"authors":["Hoer J.","Wolf S.G.","Sorek R."],"citationCrossReferences":[{"database":"PubMed","id":"39020165"},{"database":"DOI","id":"10.1038/s41586-024-07616-5"}],"citationType":"journal article","firstPage":"850","id":"39020165","journal":"Nature","lastPage":"856","publicationDate":"2024","title":"Bacteria conjugate ubiquitin-like proteins to interfere with phage assembly.","volume":"631"},"referenceNumber":2,"referencePositions":["FUNCTION","PROBABLE ACTIVE SITE","MUTAGENESIS OF CYS-113"]}
```

Source SHA-256: `dc1345a3f9e24cec733ddc2f361b20169223c3b2af22cdd9fd503d27975ae399`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11)  
**Locator:** `lines 27-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:24:42.543529+00:00.  

```text
CC   -!- FUNCTION: Component of the Bil (bacterial ISG15-like) antiviral defense
CC       system, composed of BilA, BilB, BilC and BilD. The Bil system
CC       specifically conjugates a ubiquitin-like moiety (bilA) to the
CC       bacteriophage central tail fiber (CTF, or tip attachment protein J) via
CC       reactions involving E1 (bilD) and E2 (bilB). Modifies CTF of phage
CC       SECphi27 and SECphi4, which probably interferes with assembly of the
CC       phage tail. Also modifies T5 baseplate hub protein pb3 (gene D16), but
CC       not gp27 of phage T6 (Bil defends against T6). BilB probably accepts
CC       ubiquitin from the BilA-BilD (E1) complex and catalyzes its covalent
CC       attachment to target protein (CTF) (Probable) (PubMed:39020165). Bil-
CC       encoding bacteria produce mostly defective phage SECphi27, many of
CC       which have phage assembly defects, including no tails. SECphi27 phage
CC       progeny produced in E.coli with the Bil system inject less DNA into
CC       naive host cells, maybe because the phage are less able to adsorb and
CC       inject their DNA into host cells. {ECO:0000269|PubMed:39020165,
CC       ECO:0000305|PubMed:39020165}.
```

Source SHA-256: `02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU27?format=txt&versions=11)  
**Locator:** `lines 59-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:24:42.543529+00:00.  

```text
DR   GO; GO:0019787; F:ubiquitin-like protein transferase activity; IDA:UniProtKB.
```

Source SHA-256: `02140c806e50b7c8fba6442df748ac8050a6b50ee7a254e8a2d0deb6a7a2c0c9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
