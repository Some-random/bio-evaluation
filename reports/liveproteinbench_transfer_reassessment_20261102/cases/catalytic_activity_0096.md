# catalytic_activity_0096

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0096.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTQPCIISVAITGSLPRKRDNPAVPITVSEQVESTQAAFEAGATLVHLHVRNDDETPSSEPDRFARVLEGIRKHAPGIITQVSTGGRSGAGRERGGMLSLRPDMASLATGSVNFPTRVYDNPPDLVDWLAAEMKAYAIKPEIEAFDLSMIFQAVAMQQAGKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW

[Multiple Choices]
A. N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)
B. 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA
C. L-phenylalanine = (E)-cinnamate + NH4(+)
D. K(+)(in) = K(+)(out)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1377)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns the exact reaction in choice B and cites experimental evidence (ECO:0000269, PubMed 24240508). This supports the key, although the excerpt reports the database annotation rather than presenting the experiment itself.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 284-aa sequence is compact and lacks the long hydrophobic segments expected for a membrane K+ transporter. Its N-terminal cysteine-containing region and glycine-rich segments are plausible clues to a soluble CoA-dependent acyl-transfer enzyme. Among the choices, B is the CoA-dependent acyl-transfer reaction; A concerns tRNA deacetylation and C is an amino-acid ammonia-lyase reaction. These sequence and family-level patterns make B a meaningful inference, though they do not prove its substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about soluble CoA-dependent enzyme folds and the conspicuously different reaction classes in the alternatives provides a probabilistic basis for B without needing the exact protein's annotation. The sequence alone does not establish the precise reaction.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct reaction classes, and no second choice is comparably supported by the sequence-level inference."
  },
  "important_caveats": [
    "The positive experimental support comes from a database annotation citing a publication; the supplied excerpts do not independently show the experimental results.",
    "The proposed sequence-based family inference is suggestive rather than a definitive identification of the enzyme's substrate specificity."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0KAA1 (sequence matched exactly, 284 aa) annotates this protein as 3-oxoadipate:acetyl-CoA acetyltransferase (EC 2.3.1.318) with the catalytic activity '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' supported by experimental evidence (ECO:0000269, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B matches this experimentally validated annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of the crotonase (enoyl-CoA hydratase) superfamily: glycine-rich loops (GGRSGAGRERGG, GAGIGR), ~284 aa length typical of the family, and a hydrophobic core pattern consistent with the CoA-binding pocket. The crotonase superfamily is one of the best-characterized enzyme families, and ALL its members interact with CoA thioesters as substrates or products. Among the four choices, only B (3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA) involves CoA thioester chemistry. Choices A (peptidyl-tRNA hydrolase), C (phenylalanine ammonia-lyase), and D (potassium channel) belong to entirely unrelated enzyme/transporter classes with no structural or mechanistic connection to the crotonase fold. A knowledgeable model recognizing the crotonase superfamily from its conserved sequence signatures can eliminate A, C, and D on the basis that they do not involve CoA, leaving B as the only mechanistically compatible option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The crotonase superfamily is extensively characterized in the literature with well-known sequence and structural signatures. Family-level knowledge that all crotonase superfamily members process CoA thioesters is transferable from the many other characterized members (enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, etc.) and meaningfully distinguishes B from the three non-CoA alternatives without requiring the exact annotation of this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice B involves CoA thioester chemistry. Choices A, C, and D represent completely unrelated enzyme/transporter classes (tRNA hydrolase, amino acid lyase, ion channel) with no structural or mechanistic overlap with the crotonase superfamily fold evident in the sequence. There is no ambiguity among the offered alternatives.


### Important caveats

- The specific reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) was described as 'hidden functional diversity' within the crotonase superfamily, meaning the exact reaction type is unusual for the family. However, the question only requires distinguishing among four choices, and the CoA-involvement criterion suffices.
- The 2014 Bastard et al. paper provided experimental (ECO:0000269) evidence for the catalytic activity, so the annotation is experimentally supported rather than purely computational.
- The reviewer-only evidence confirms sequence match and experimental support, but these were not available to the evaluated model; the family-level inference from sequence features alone is the relevant reasoning path.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of the crotonase (enoyl-CoA hydratase) superfamily: glycine-rich loops (GGRSGAGRERGG, GAGIGR), ~284 aa length typical of the family, and a hydrophobic core pattern consistent with the CoA-binding pocket. The crotonase superfamily is one of the best-characterized enzyme families, and ALL its members interact with CoA thioesters as substrates or products. Among the four choices, only B (3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA) involves CoA thioester chemistry. Choices A (peptidyl-tRNA hydrolase), C (phenylalanine ammonia-lyase), and D (potassium channel) belong to entirely unrelated enzyme/transporter classes with no structural or mechanistic connection to the crotonase fold. A knowledgeable model recognizing the crotonase superfamily from its conserved sequence signatures can eliminate A, C, and D on the basis that they do not involve CoA, leaving B as the only mechanistically compatible option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The crotonase superfamily is extensively characterized in the literature with well-known sequence and structural signatures. Family-level knowledge that all crotonase superfamily members process CoA thioesters is transferable from the many other characterized members (enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, etc.) and meaningfully distinguishes B from the three non-CoA alternatives without requiring the exact annotation of this particular protein."
  },
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0KAA1 (sequence matched exactly, 284 aa) annotates this protein as 3-oxoadipate:acetyl-CoA acetyltransferase (EC 2.3.1.318) with the catalytic activity '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' supported by experimental evidence (ECO:0000269, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B matches this experimentally validated annotation exactly."
  },
  "important_caveats": [
    "The specific reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) was described as 'hidden functional diversity' within the crotonase superfamily, meaning the exact reaction type is unusual for the family. However, the question only requires distinguishing among four choices, and the CoA-involvement criterion suffices.",
    "The 2014 Bastard et al. paper provided experimental (ECO:0000269) evidence for the catalytic activity, so the annotation is experimentally supported rather than purely computational.",
    "The reviewer-only evidence confirms sequence match and experimental support, but these were not available to the evaluated model; the family-level inference from sequence features alone is the relevant reasoning path."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B involves CoA thioester chemistry. Choices A, C, and D represent completely unrelated enzyme/transporter classes (tRNA hydrolase, amino acid lyase, ion channel) with no structural or mechanistic overlap with the crotonase superfamily fold evident in the sequence. There is no ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0KAA1 (sequence matched exactly, 284 aa) annotates this protein as 3-oxoadipate:acetyl-CoA acetyltransferase (EC 2.3.1.318) with the catalytic activity '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' supported by experimental evidence (ECO:0000269, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B matches this experimentally validated annotation exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of the crotonase (enoyl-CoA hydratase) superfamily: glycine-rich loops (GGRSGAGRERGG, GAGIGR), ~284 aa length typical of the family, and a hydrophobic core pattern consistent with the CoA-binding pocket. The crotonase superfamily is one of the best-characterized enzyme families, and ALL its members interact with CoA thioesters as substrates or products. Among the four choices, only B (3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA) involves CoA thioester chemistry. Choices A (peptidyl-tRNA hydrolase), C (phenylalanine ammonia-lyase), and D (potassium channel) belong to entirely unrelated enzyme/transporter classes with no structural or mechanistic connection to the crotonase fold. A knowledgeable model recognizing the crotonase superfamily from its conserved sequence signatures can eliminate A, C, and D on the basis that they do not involve CoA, leaving B as the only mechanistically compatible option.",
    "missing_item_specific_fact": "",
    "reason": "The crotonase superfamily is extensively characterized in the literature with well-known sequence and structural signatures. Family-level knowledge that all crotonase superfamily members process CoA thioesters is transferable from the many other characterized members (enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, etc.) and meaningfully distinguishes B from the three non-CoA alternatives without requiring the exact annotation of this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B involves CoA thioester chemistry. Choices A, C, and D represent completely unrelated enzyme/transporter classes (tRNA hydrolase, amino acid lyase, ion channel) with no structural or mechanistic overlap with the crotonase superfamily fold evident in the sequence. There is no ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The specific reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) was described as 'hidden functional diversity' within the crotonase superfamily, meaning the exact reaction type is unusual for the family. However, the question only requires distinguishing among four choices, and the CoA-involvement criterion suffices.",
    "The 2014 Bastard et al. paper provided experimental (ECO:0000269) evidence for the catalytic activity, so the annotation is experimentally supported rather than purely computational.",
    "The reviewer-only evidence confirms sequence match and experimental support, but these were not available to the evaluated model; the family-level inference from sequence features alone is the relevant reasoning path."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 284,
  "benchmark_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 284,
  "current_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0KAA1",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "selected_historical_source_sequence_length": 284,
  "selected_historical_source_sequence_sha256": "578ee40d19a4187b96bbd813dd5b2ad6c5cd4952c2e58954fc66e0445da2dd06",
  "selected_historical_version": {
    "accession": "Q0KAA1",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "3OXCE_CUPNH",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0KAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ralstonia eutropha\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Burkholderiaceae\",\"Cupriavidus\"],\"scientificName\":\"Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442 / H16 / Stanier 337)\",\"taxonId\":381666}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate cleavage enzyme\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"BKACE_378\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.318\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"3-oxoadipate:acetyl-CoA acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.318\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24240508\",\"source\":\"PubMed\"}],\"name\":\"3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79651\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:13705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15775\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57292\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bastard K.\",\"Smith A.A.\",\"Vergne-Vaxelaire C.\",\"Perret A.\",\"Zaparucha A.\",\"De Melo-Minardi R.\",\"Mariage A.\",\"Boutard M.\",\"Debard A.\",\"Lechaplais C.\",\"Pelle C.\",\"Pellouin V.\",\"Perchat N.\",\"Petit J.L.\",\"Kreimeyer A.\",\"Medigue C.\",\"Weissenbach J.\",\"Artiguenave F.\",\"De Berardinis V.\",\"Vallenet D.\",\"Salanoubat M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24240508\"},{\"database\":\"DOI\",\"id\":\"10.1038/nchembio.1387\"}],\"citationType\":\"journal article\",\"firstPage\":\"42\",\"id\":\"24240508\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"49\",\"publicationDate\":\"2014\",\"title\":\"Revealing the hidden functional diversity of an enzyme family.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:26.682394+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140",
  "url": "https://rest.uniprot.org/uniprotkb/Q0KAA1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   3OXCE_CUPNH             Reviewed;         284 AA.\nAC   Q0KAA1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\nGN   OrderedLocusNames=H16_A1969 {ECO:0000312|EMBL:CAJ93070.1};\nGN   ORFNames=E6A55_10065 {ECO:0000312|EMBL:QCC00902.1};\nOS   Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442\nOS   / H16 / Stanier 337) (Ralstonia eutropha).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Burkholderiaceae; Cupriavidus.\nOX   NCBI_TaxID=381666;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};\nDE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};\nDE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=24240508; DOI=10.1038/nchembio.1387;\nRA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,\nRA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,\nRA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,\nRA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,\nRA   Salanoubat M.;\nRT   \"Revealing the hidden functional diversity of an enzyme family.\";\nRL   Nat. Chem. Biol. 10:42-49(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA;\nCC         Xref=Rhea:RHEA:79651, ChEBI:CHEBI:13705, ChEBI:CHEBI:15775,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:57292; EC=2.3.1.318;\nCC         Evidence={ECO:0000269|PubMed:24240508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:29.925890+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e",
  "url": "https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
