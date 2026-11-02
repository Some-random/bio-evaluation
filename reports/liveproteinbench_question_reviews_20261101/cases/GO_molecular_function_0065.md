# GO_molecular_function_0065

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — nutrient reservoir activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVIMKAGFLFLASLCLLVQAVPNKVADKTYVTRQKNIYELFWHVDQPTVYHPELYQKARTFNLVENLDNYNDKEAVNEFMQLLKHGMLPRGQVFTMMNKEMRHQAVVLFRLLYSAKTFDVFYNTAVWARFNVNEQMYLYALSVAVIHRPDTKLMKLPPMYEVMPHLYFNDEVMQKAYNIAMGDTADMKKTYNNIDYYLLAANYTGWYLTKHNVPEQRLNYFTEDVGLNHFYFMLNHNYPPFMLSNSLNFPQIRGEFYFFLHKQVLNRYYLERLSNDMGEVSYVSLDHPIPTGYYPTMRFRNGLAFPQRETGATVPLHMQKYVQMIHDLHTRISTAIDLGYVVDSYGNHVKLYTKQGLNVLGNIVQGNGDSVNVQLYGQLDLLVRKVLGFGYESNVKYQVVPSALQMWSTSLRDPVFFSIYKTILDYYHKYKENLPKYTTEELNFPGVSIESVTVDKLITYFDHFESMLNNGVSIQSHAKAKNTMIKARQYRLNHKPFTYHIVVNSDKNVKGMVRIFLGPKYDEFGHEVDLVHNYMNFMQMDEFVVNLKSGSNTIERNSHESVFVVPDEVPSDVLYNRLVVSEDGSETFKYSSQPYGFPERLLLPKGKKEGMPYNVLVVVSPFDDSNVVQIDSPVWGRHIYDGRAMGFPLDKPVDPLLLVLSNIHVKEVLVHHREMEELNVAL

[Multiple Choices]
A. UDP-glucose 6-dehydrogenase activity
B. quercetin 3-O-glucosyltransferase activity
C. nutrient reservoir activity
D. hydrolase activity, acting on ester bonds
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

> The supplied sequence exactly matches the reviewed Apis mellifera Hexamerin 70b sequence. Its entry describes it as a storage protein that may supply nutrients and assigns nutrient reservoir activity with IDA evidence. This supports choice C, though the functional description retains the qualification “may function.”

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide and secretion, but that alone does not establish nutrient-reservoir activity or reliably distinguish it from the listed alternatives.


**Missing item-specific fact**

> The sequence’s identity as honeybee Hexamerin 70b and its storage-protein/nutrient-reservoir annotation are needed to select C confidently.


**Reason**

> The input provides no organism, protein name, or functional annotation. The key is supported by sequence-matched database and literature-linked evidence, but that protein-specific fact is not supplied, and generic sequence features do not decisively identify the GO function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched entry specifically supports nutrient reservoir activity; the evidence supplied does not support another listed option.


### Important caveats

- The cited GO annotation is IDA-linked, and the UniProt functional description is based on cited research; the primary papers were not independently reviewed here.
- The exact source snapshot used by the question author is unknown, although the historical and current records checked match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide and secretion, but that alone does not establish nutrient-reservoir activity or reliably distinguish it from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence’s identity as honeybee Hexamerin 70b and its storage-protein/nutrient-reservoir annotation are needed to select C confidently.",
    "reason": "The input provides no organism, protein name, or functional annotation. The key is supported by sequence-matched database and literature-linked evidence, but that protein-specific fact is not supplied, and generic sequence features do not decisively identify the GO function."
  },
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Apis mellifera Hexamerin 70b sequence. Its entry describes it as a storage protein that may supply nutrients and assigns nutrient reservoir activity with IDA evidence. This supports choice C, though the functional description retains the qualification “may function.”"
  },
  "important_caveats": [
    "The cited GO annotation is IDA-linked, and the UniProt functional description is based on cited research; the primary papers were not independently reviewed here.",
    "The exact source snapshot used by the question author is unknown, although the historical and current records checked match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched entry specifically supports nutrient reservoir activity; the evidence supplied does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Apis mellifera Hexamerin 70b sequence. Its entry describes it as a storage protein that may supply nutrients and assigns nutrient reservoir activity with IDA evidence. This supports choice C, though the functional description retains the qualification “may function.”",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide and secretion, but that alone does not establish nutrient-reservoir activity or reliably distinguish it from the listed alternatives.",
    "missing_item_specific_fact": "The sequence’s identity as honeybee Hexamerin 70b and its storage-protein/nutrient-reservoir annotation are needed to select C confidently.",
    "reason": "The input provides no organism, protein name, or functional annotation. The key is supported by sequence-matched database and literature-linked evidence, but that protein-specific fact is not supplied, and generic sequence features do not decisively identify the GO function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched entry specifically supports nutrient reservoir activity; the evidence supplied does not support another listed option."
  },
  "important_caveats": [
    "The cited GO annotation is IDA-linked, and the UniProt functional description is based on cited research; the primary papers were not independently reviewed here.",
    "The exact source snapshot used by the question author is unknown, although the historical and current records checked match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 (nutrient reservoir activity) with evidence code IDA (Inferred from Direct Assay) from PubMed:16055147 (C6/H6). The FUNCTION comment (C5/H5) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition (GO3) is 'Functions in the storage of nutritious substrates.' The protein is a hexamerin, a well-characterized class of insect storage proteins. The sequence matches the UniProt entry exactly (683 AA, SHA256 match).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H1](#evidence-h1), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks the characteristic motifs required for the three catalytic options: no Rossmann-fold NAD(P)-binding motif or catalytic residues for UDP-glucose 6-dehydrogenase (A); no PSPG motif or UDP-sugar-binding pocket for quercetin 3-O-glucosyltransferase (B); no catalytic triad (Ser-His-Asp/Glu or equivalent nucleophile) for ester-bond hydrolase activity (D). The protein is a large (~683 AA) secreted protein (N-terminal signal peptide MIVIMKAGFLFLASLCLLVQAVPNKV...) with no identifiable catalytic machinery, which is consistent with a storage/reservoir role. Among the four options, C (nutrient reservoir activity) is the only non-catalytic molecular function, making it the sole option compatible with a protein lacking enzymatic motifs. The GO term definition ('Functions in the storage of nutritious substrates') is intuitive and does not require memorizing a specific database entry.


**Missing item-specific fact**

> Positive identification of this protein as a hexamerin (a specific insect storage protein family) would strengthen the case for C, but is not strictly necessary given that elimination of all three catalytic options leaves C as the only viable choice. Knowledge that hexamerins are storage proteins aids confirmation but the elimination argument is sufficient.


**Reason**

> The three catalytic distractors (A, B, D) each require specific, well-defined active-site motifs absent from the sequence. The elimination of these through motif-absence reasoning is a standard and defensible biological argument. C is the only non-catalytic option, and its definition aligns with a large secreted protein lacking enzymatic features. While recognizing the hexamerin family would provide additional confirmation, the answer is reachable through negative evidence (absence of catalytic motifs) combined with the structural context (secreted, large, no active site).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three distinct catalytic mechanisms and one non-catalytic storage function. The absence of catalytic motifs in the sequence clearly disfavors A, B, and D. No two options are equally defensible given the sequence features.


### Important caveats

- The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:16055147, not merely computational transfer.
- The hexamerin family identification from sequence alone is not trivial; the reasoning-supported judgment relies primarily on elimination of catalytic options rather than positive family recognition.
- The identity_origin note states the UniProt accession was inferred from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.
- The sequence is a precursor (signal peptide present); mature protein numbering may differ, but this does not affect the molecular function assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks the characteristic motifs required for the three catalytic options: no Rossmann-fold NAD(P)-binding motif or catalytic residues for UDP-glucose 6-dehydrogenase (A); no PSPG motif or UDP-sugar-binding pocket for quercetin 3-O-glucosyltransferase (B); no catalytic triad (Ser-His-Asp/Glu or equivalent nucleophile) for ester-bond hydrolase activity (D). The protein is a large (~683 AA) secreted protein (N-terminal signal peptide MIVIMKAGFLFLASLCLLVQAVPNKV...) with no identifiable catalytic machinery, which is consistent with a storage/reservoir role. Among the four options, C (nutrient reservoir activity) is the only non-catalytic molecular function, making it the sole option compatible with a protein lacking enzymatic motifs. The GO term definition ('Functions in the storage of nutritious substrates') is intuitive and does not require memorizing a specific database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of this protein as a hexamerin (a specific insect storage protein family) would strengthen the case for C, but is not strictly necessary given that elimination of all three catalytic options leaves C as the only viable choice. Knowledge that hexamerins are storage proteins aids confirmation but the elimination argument is sufficient.",
    "reason": "The three catalytic distractors (A, B, D) each require specific, well-defined active-site motifs absent from the sequence. The elimination of these through motif-absence reasoning is a standard and defensible biological argument. C is the only non-catalytic option, and its definition aligns with a large secreted protein lacking enzymatic features. While recognizing the hexamerin family would provide additional confirmation, the answer is reachable through negative evidence (absence of catalytic motifs) combined with the structural context (secreted, large, no active site)."
  },
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H1",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 (nutrient reservoir activity) with evidence code IDA (Inferred from Direct Assay) from PubMed:16055147 (C6/H6). The FUNCTION comment (C5/H5) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition (GO3) is 'Functions in the storage of nutritious substrates.' The protein is a hexamerin, a well-characterized class of insect storage proteins. The sequence matches the UniProt entry exactly (683 AA, SHA256 match)."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:16055147, not merely computational transfer.",
    "The hexamerin family identification from sequence alone is not trivial; the reasoning-supported judgment relies primarily on elimination of catalytic options rather than positive family recognition.",
    "The identity_origin note states the UniProt accession was inferred from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "The sequence is a precursor (signal peptide present); mature protein numbering may differ, but this does not affect the molecular function assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct catalytic mechanisms and one non-catalytic storage function. The absence of catalytic motifs in the sequence clearly disfavors A, B, and D. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 (nutrient reservoir activity) with evidence code IDA (Inferred from Direct Assay) from PubMed:16055147 (C6/H6). The FUNCTION comment (C5/H5) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition (GO3) is 'Functions in the storage of nutritious substrates.' The protein is a hexamerin, a well-characterized class of insect storage proteins. The sequence matches the UniProt entry exactly (683 AA, SHA256 match).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C9", "H1", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks the characteristic motifs required for the three catalytic options: no Rossmann-fold NAD(P)-binding motif or catalytic residues for UDP-glucose 6-dehydrogenase (A); no PSPG motif or UDP-sugar-binding pocket for quercetin 3-O-glucosyltransferase (B); no catalytic triad (Ser-His-Asp/Glu or equivalent nucleophile) for ester-bond hydrolase activity (D). The protein is a large (~683 AA) secreted protein (N-terminal signal peptide MIVIMKAGFLFLASLCLLVQAVPNKV...) with no identifiable catalytic machinery, which is consistent with a storage/reservoir role. Among the four options, C (nutrient reservoir activity) is the only non-catalytic molecular function, making it the sole option compatible with a protein lacking enzymatic motifs. The GO term definition ('Functions in the storage of nutritious substrates') is intuitive and does not require memorizing a specific database entry.",
    "missing_item_specific_fact": "Positive identification of this protein as a hexamerin (a specific insect storage protein family) would strengthen the case for C, but is not strictly necessary given that elimination of all three catalytic options leaves C as the only viable choice. Knowledge that hexamerins are storage proteins aids confirmation but the elimination argument is sufficient.",
    "reason": "The three catalytic distractors (A, B, D) each require specific, well-defined active-site motifs absent from the sequence. The elimination of these through motif-absence reasoning is a standard and defensible biological argument. C is the only non-catalytic option, and its definition aligns with a large secreted protein lacking enzymatic features. While recognizing the hexamerin family would provide additional confirmation, the answer is reachable through negative evidence (absence of catalytic motifs) combined with the structural context (secreted, large, no active site)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct catalytic mechanisms and one non-catalytic storage function. The absence of catalytic motifs in the sequence clearly disfavors A, B, and D. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support from PubMed:16055147, not merely computational transfer.",
    "The hexamerin family identification from sequence alone is not trivial; the reasoning-supported judgment relies primarily on elimination of catalytic options rather than positive family recognition.",
    "The identity_origin note states the UniProt accession was inferred from dataset image-path metadata and was absent from the evaluated model input; the model sees only the raw sequence.",
    "The sequence is a precursor (signal peptide present); mature protein numbering may differ, but this does not affect the molecular function assignment."
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

**Accession:** `Q6J4Q1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 125. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
"Q6J4Q1"
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9692239","source":"PubMed"}],"value":"Hexamerin 70b"}}}
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16055147","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"26466725","source":"PubMed"}],"value":"Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause"}]}
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16055147","source":"PubMed"}],"id":"GO:0045735","properties":[{"key":"GoTerm","value":"F:nutrient reservoir activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
{"citation":{"authors":["Cunha A.D.","Nascimento A.M.","Guidugli K.R.","Simoes Z.L.","Bitondi M.M."],"citationCrossReferences":[{"database":"PubMed","id":"16055147"},{"database":"DOI","id":"10.1016/j.jinsphys.2005.06.004"}],"citationType":"journal article","firstPage":"1135","id":"16055147","journal":"J. Insect Physiol.","lastPage":"1147","publicationDate":"2005","title":"Molecular cloning and expression of a hexamerin cDNA from the honey bee, Apis mellifera.","volume":"51"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAT11850.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","DEVELOPMENTAL STAGE","INDUCTION BY JUVENILE HORMONE AND ECDYSTERONE"]}
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:33.250244+00:00.  

```json
{"citation":{"authors":["Martins J.R.","Bitondi M.M."],"citationCrossReferences":[{"database":"PubMed","id":"26466725"},{"database":"DOI","id":"10.3390/insects3041039"}],"citationType":"journal article","firstPage":"1039","id":"26466725","journal":"Insects","lastPage":"1055","publicationDate":"2012","title":"Nuclear Immunolocalization of Hexamerins in the Fat Body of Metamorphosing Honey Bees.","volume":"3"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":8,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","TISSUE SPECIFICITY","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 125 / 1.  
**Retrieved:** 2026-11-02T04:31:39.845057+00:00.  

```text
ID   HEX7B_APIME             Reviewed;         683 AA.
AC   Q6J4Q1; A0A7M6UKD0; A0A8B6WYY8; A0A8U0WQ75; Q9Y1C3;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   28-JAN-2026, entry version 125.
DE   RecName: Full=Hexamerin 70b {ECO:0000303|PubMed:9692239};
DE   Flags: Precursor;
GN   Name=Hex70b {ECO:0000303|PubMed:9692239,
GN   ECO:0000312|RefSeq:NP_001011600.1};
GN   Synonyms=406117 {ECO:0000312|EnsemblMetazoa:NP_001011600};
OS   Apis mellifera (Honeybee).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;
OC   Anthophila; Apidae; Apis.
OX   NCBI_TaxID=7460 {ECO:0000312|Proteomes:UP000005203};
```

Source SHA-256: `eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)  
**Locator:** `lines 94-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 125 / 1.  
**Retrieved:** 2026-11-02T04:31:39.845057+00:00.  

```text
CC   -!- FUNCTION: Storage protein produced during nutritional abundance, which
CC       may function as a nutrient supply to compensate for lack of dietary
CC       proteins during metamorphosis, egg production and diapause.
CC       {ECO:0000269|PubMed:16055147, ECO:0000305|PubMed:26466725}.
```

Source SHA-256: `eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)  
**Locator:** `lines 160-160`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 125 / 1.  
**Retrieved:** 2026-11-02T04:31:39.845057+00:00.  

```text
DR   GO; GO:0045735; F:nutrient reservoir activity; IDA:UniProtKB.
```

Source SHA-256: `eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 268007-268020`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045735
name: nutrient reservoir activity
namespace: molecular_function
def: "Functions in the storage of nutritious substrates." [GOC:ai]
comment: Note that this term can be used in place of the obsolete terms 'storage protein ; GO:0005187' and 'storage protein of fat body (sensu Insecta) ; GO:0008041'.
subset: goslim_generic
subset: goslim_pir
subset: goslim_prokaryote
synonym: "storage protein" RELATED []
synonym: "storage protein of fat body" RELATED []
synonym: "yolk protein" RELATED []
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
