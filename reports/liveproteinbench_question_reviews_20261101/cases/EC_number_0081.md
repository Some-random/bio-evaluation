# EC_number_0081

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.5.1.160

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. 2.5.1.56
B. 2.5.1.160
C. 2.4.1.392
D. 1.14.14.154
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the tobacco chloroplastic cystathionine gamma-synthase entry, which assigns EC 2.5.1.160 and links its O-phospho-L-homoserine reaction to experimental evidence (ECO:0000269, PubMed:10595588).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, but the choices include closely related EC classifications whose distinction depends on the enzyme's specific substrate and reaction; the sequence and choices alone do not establish that specificity.


**Missing item-specific fact**

> The protein-specific assignment of its principal catalytic reaction to O-phospho-L-homoserine, rather than the related O-succinyl-L-homoserine reaction.


**Reason**

> Choosing B requires a specific annotation or experimental fact about this enzyme's substrate and assigned reaction. General sequence-based knowledge does not meaningfully resolve that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched entry supports B as the assigned EC number. Its separate annotation of an O-succinyl-L-homoserine reaction is marked as curator inference and does not establish another listed EC assignment.


### Important caveats

- The supporting database evidence is reviewer-only and was not supplied in the original question.
- The sequence match and experimental evidence support the key, but the cited primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but the choices include closely related EC classifications whose distinction depends on the enzyme's specific substrate and reaction; the sequence and choices alone do not establish that specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of its principal catalytic reaction to O-phospho-L-homoserine, rather than the related O-succinyl-L-homoserine reaction.",
    "reason": "Choosing B requires a specific annotation or experimental fact about this enzyme's substrate and assigned reaction. General sequence-based knowledge does not meaningfully resolve that distinction."
  },
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the tobacco chloroplastic cystathionine gamma-synthase entry, which assigns EC 2.5.1.160 and links its O-phospho-L-homoserine reaction to experimental evidence (ECO:0000269, PubMed:10595588)."
  },
  "important_caveats": [
    "The supporting database evidence is reviewer-only and was not supplied in the original question.",
    "The sequence match and experimental evidence support the key, but the cited primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry supports B as the assigned EC number. Its separate annotation of an O-succinyl-L-homoserine reaction is marked as curator inference and does not establish another listed EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the tobacco chloroplastic cystathionine gamma-synthase entry, which assigns EC 2.5.1.160 and links its O-phospho-L-homoserine reaction to experimental evidence (ECO:0000269, PubMed:10595588).",
    "evidence_ids": ["C1", "C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, but the choices include closely related EC classifications whose distinction depends on the enzyme's specific substrate and reaction; the sequence and choices alone do not establish that specificity.",
    "missing_item_specific_fact": "The protein-specific assignment of its principal catalytic reaction to O-phospho-L-homoserine, rather than the related O-succinyl-L-homoserine reaction.",
    "reason": "Choosing B requires a specific annotation or experimental fact about this enzyme's substrate and assigned reaction. General sequence-based knowledge does not meaningfully resolve that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry supports B as the assigned EC number. Its separate annotation of an O-succinyl-L-homoserine reaction is marked as curator inference and does not establish another listed EC assignment."
  },
  "important_caveats": [
    "The supporting database evidence is reviewer-only and was not supplied in the original question.",
    "The sequence match and experimental evidence support the key, but the cited primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9ZPL5 (CGS1_TOBAC) is annotated as Cystathionine gamma-synthase 1, chloroplastic, with EC=2.5.1.160 supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999). The catalytic activity (O-phospho-L-homoserine + L-cysteine → L,L-cystathionine + phosphate) is experimentally verified. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 540 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can eliminate C (EC 2.4.1.392, glycosyltransferase) and D (EC 1.14.14.154, cytochrome P450) because the sequence lacks GT-B/GT-A folds and the P450 heme-binding motif (FxxGxxxCxG). The N-terminal Ser/Thr-rich region suggests a chloroplastic transit peptide, and PLP-associated motifs (e.g., the 'GADLVLHSATKFLGG' region) hint at a PLP-dependent enzyme in amino acid biosynthesis. However, both A (2.5.1.56) and B (2.5.1.160) fall within the same EC subclass (transferases transferring alkyl/aryl groups), and distinguishing between them requires knowing the exact reaction each EC number denotes.


**Missing item-specific fact**

> The specific reaction catalyzed by EC 2.5.1.56 (and whether it shares substrate/scaffold features with cystathionine gamma-synthase) is not derivable from the sequence alone. Without knowing what EC 2.5.1.56 encodes, one cannot definitively rule it out based on sequence motifs, since both options are in the 2.5.1.x family and the sequence does not encode its substrate specificity in a way that maps uniquely to one EC number versus the other.


**Reason**

> While C and D can be eliminated by general fold/motif reasoning, the critical A-vs-B distinction within EC 2.5.1.x requires item-specific knowledge of what reaction EC 2.5.1.56 refers to. The sequence provides no unambiguous signature that maps to 2.5.1.160 rather than 2.5.1.56 without database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although A and B are in the same EC subclass, the UniProt annotation with experimental evidence uniquely assigns this sequence to EC 2.5.1.160. EC 2.5.1.56 likely refers to a different enzyme reaction. No evidence suggests both are defensible for this sequence, but the reasoning gap between A and B is a difficulty issue rather than a true ambiguity in the ground truth.


### Important caveats

- The identity of EC 2.5.1.56 was not independently verified in the reviewer evidence; if it happens to refer to a closely related cystathionine-pathway enzyme, the A-vs-B distinction would be even harder without lookup.
- The EC 2.5.1.160 annotation carries ECO:0000269 (inferred from direct assay), making it experimentally grounded rather than purely computational.
- The sequence was annotated in Swiss-Prot only from 2025-06-18; if the benchmark was constructed earlier, the author may have relied on TrEMBL or other sources.
- The chloroplastic transit peptide and PLP motifs provide suggestive but not conclusive evidence distinguishing 2.5.1.160 from other 2.5.1.x enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can eliminate C (EC 2.4.1.392, glycosyltransferase) and D (EC 1.14.14.154, cytochrome P450) because the sequence lacks GT-B/GT-A folds and the P450 heme-binding motif (FxxGxxxCxG). The N-terminal Ser/Thr-rich region suggests a chloroplastic transit peptide, and PLP-associated motifs (e.g., the 'GADLVLHSATKFLGG' region) hint at a PLP-dependent enzyme in amino acid biosynthesis. However, both A (2.5.1.56) and B (2.5.1.160) fall within the same EC subclass (transferases transferring alkyl/aryl groups), and distinguishing between them requires knowing the exact reaction each EC number denotes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific reaction catalyzed by EC 2.5.1.56 (and whether it shares substrate/scaffold features with cystathionine gamma-synthase) is not derivable from the sequence alone. Without knowing what EC 2.5.1.56 encodes, one cannot definitively rule it out based on sequence motifs, since both options are in the 2.5.1.x family and the sequence does not encode its substrate specificity in a way that maps uniquely to one EC number versus the other.",
    "reason": "While C and D can be eliminated by general fold/motif reasoning, the critical A-vs-B distinction within EC 2.5.1.x requires item-specific knowledge of what reaction EC 2.5.1.56 refers to. The sequence provides no unambiguous signature that maps to 2.5.1.160 rather than 2.5.1.56 without database lookup."
  },
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9ZPL5 (CGS1_TOBAC) is annotated as Cystathionine gamma-synthase 1, chloroplastic, with EC=2.5.1.160 supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999). The catalytic activity (O-phospho-L-homoserine + L-cysteine → L,L-cystathionine + phosphate) is experimentally verified. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 540 aa)."
  },
  "important_caveats": [
    "The identity of EC 2.5.1.56 was not independently verified in the reviewer evidence; if it happens to refer to a closely related cystathionine-pathway enzyme, the A-vs-B distinction would be even harder without lookup.",
    "The EC 2.5.1.160 annotation carries ECO:0000269 (inferred from direct assay), making it experimentally grounded rather than purely computational.",
    "The sequence was annotated in Swiss-Prot only from 2025-06-18; if the benchmark was constructed earlier, the author may have relied on TrEMBL or other sources.",
    "The chloroplastic transit peptide and PLP motifs provide suggestive but not conclusive evidence distinguishing 2.5.1.160 from other 2.5.1.x enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and B are in the same EC subclass, the UniProt annotation with experimental evidence uniquely assigns this sequence to EC 2.5.1.160. EC 2.5.1.56 likely refers to a different enzyme reaction. No evidence suggests both are defensible for this sequence, but the reasoning gap between A and B is a difficulty issue rather than a true ambiguity in the ground truth."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9ZPL5 (CGS1_TOBAC) is annotated as Cystathionine gamma-synthase 1, chloroplastic, with EC=2.5.1.160 supported by experimental evidence (ECO:0000269, PubMed:10595588, Clausen et al. 1999). The catalytic activity (O-phospho-L-homoserine + L-cysteine → L,L-cystathionine + phosphate) is experimentally verified. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 540 aa).",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can eliminate C (EC 2.4.1.392, glycosyltransferase) and D (EC 1.14.14.154, cytochrome P450) because the sequence lacks GT-B/GT-A folds and the P450 heme-binding motif (FxxGxxxCxG). The N-terminal Ser/Thr-rich region suggests a chloroplastic transit peptide, and PLP-associated motifs (e.g., the 'GADLVLHSATKFLGG' region) hint at a PLP-dependent enzyme in amino acid biosynthesis. However, both A (2.5.1.56) and B (2.5.1.160) fall within the same EC subclass (transferases transferring alkyl/aryl groups), and distinguishing between them requires knowing the exact reaction each EC number denotes.",
    "missing_item_specific_fact": "The specific reaction catalyzed by EC 2.5.1.56 (and whether it shares substrate/scaffold features with cystathionine gamma-synthase) is not derivable from the sequence alone. Without knowing what EC 2.5.1.56 encodes, one cannot definitively rule it out based on sequence motifs, since both options are in the 2.5.1.x family and the sequence does not encode its substrate specificity in a way that maps uniquely to one EC number versus the other.",
    "reason": "While C and D can be eliminated by general fold/motif reasoning, the critical A-vs-B distinction within EC 2.5.1.x requires item-specific knowledge of what reaction EC 2.5.1.56 refers to. The sequence provides no unambiguous signature that maps to 2.5.1.160 rather than 2.5.1.56 without database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and B are in the same EC subclass, the UniProt annotation with experimental evidence uniquely assigns this sequence to EC 2.5.1.160. EC 2.5.1.56 likely refers to a different enzyme reaction. No evidence suggests both are defensible for this sequence, but the reasoning gap between A and B is a difficulty issue rather than a true ambiguity in the ground truth."
  },
  "important_caveats": [
    "The identity of EC 2.5.1.56 was not independently verified in the reviewer evidence; if it happens to refer to a closely related cystathionine-pathway enzyme, the A-vs-B distinction would be even harder without lookup.",
    "The EC 2.5.1.160 annotation carries ECO:0000269 (inferred from direct assay), making it experimentally grounded rather than purely computational.",
    "The sequence was annotated in Swiss-Prot only from 2025-06-18; if the benchmark was constructed earlier, the author may have relied on TrEMBL or other sources.",
    "The chloroplastic transit peptide and PLP motifs provide suggestive but not conclusive evidence distinguishing 2.5.1.160 from other 2.5.1.x enzymes."
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

**Accession:** `Q9ZPL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 110. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
"Q9ZPL5"
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"value":"2.5.1.160"}],"fullName":{"value":"Cystathionine gamma-synthase 1, chloroplastic"}}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.5.1.160","evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"name":"O-phospho-L-homoserine + L-cysteine = L,L-cystathionine + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80891"},{"database":"ChEBI","id":"CHEBI:35235"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:58161"}]}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"citation":{"authors":["Clausen T.","Wahl M.C.","Messerschmidt A.","Huber R.","Fuhrmann J.C.","Laber B.","Streber W.","Steegborn C."],"citationCrossReferences":[{"database":"PubMed","id":"10595588"},{"database":"DOI","id":"10.1515/bc.1999.157"}],"citationType":"journal article","firstPage":"1237","id":"10595588","journal":"Biol. Chem.","lastPage":"1242","publicationDate":"1999","title":"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.","volume":"380"},"referenceNumber":3,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] OF 97-540","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
DE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;
DE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};
DE   Flags: Precursor;
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
RN   [3]
RP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.
RX   PubMed=10595588; DOI=10.1515/bc.1999.157;
RA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,
RA   Streber W., Steegborn C.;
RT   "Cloning, purification and characterisation of cystathionine gamma-synthase
RT   from Nicotiana tabacum.";
RL   Biol. Chem. 380:1237-1242(1999).
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 58-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-homoserine + L-cysteine = L,L-cystathionine +
CC         phosphate; Xref=Rhea:RHEA:80891, ChEBI:CHEBI:35235,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57590, ChEBI:CHEBI:58161;
CC         EC=2.5.1.160; Evidence={ECO:0000269|PubMed:10595588};
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
