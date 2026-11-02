# GO_cellular_component_0113

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — virion component

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGSQIKIPLPKPPDSDSQRLNAFPVIMAQEGKGRLLRQIRLRKILSGDPSDQQITFVNTYGFIRATPETSEFISESSQQKVTPVVTACMLSFGAGPVLEDPQHMLKALDQTDIRVRKTASDKEQILFEINRIPNLFRHYQISADHLIQASSDKYVKSPAKLIAGVNYIYCVTFLSVTVCSASLKFRVARPLLAARSRLVRAVQMEILLRVTCKKDSQMAKSMLNDPDGEGCIASVWFHLCNLCKGRNKLRSYDENYFASKCRKMNLTVSIGDMWGPTILVHAGGHIPTTAKPFFNSRGWVCHPIHQSSPSLAKTLWSSGCEIKAASAILQGSDYASLAKTDDIIYSKIKVDKDAANYKGVSWSPFRKSASMRNL

[Multiple Choices]
A. rhoptry
B. caveola
C. early endosome membrane
D. virion component
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence matches the 375-aa Mumps virus matrix protein. UniProt records its location as virion with experimental evidence (ECO:0000269; PubMed 26768080), supporting choice D.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name compartments from very different biological contexts, but the supplied sequence alone does not establish that this protein is a viral matrix protein or show a distinctive signal that identifies virion association.


**Missing item-specific fact**

> The protein's identity as the Mumps virus matrix protein and evidence that it is associated with virions.


**Reason**

> The expected answer is supported by reviewer-only protein-specific annotation and experimental evidence, neither of which was supplied to the evaluated model. Recognizing or recalling this exact sequence would be lookup or memorization, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matching protein-specific evidence supports virion association, and none of the other listed options is supported by the supplied sequence or reviewer-only evidence.


### Important caveats

- The experimental subcellular-location annotation cites a mass-spectrometry study of Mumps virus strain Jeryl-Lynn 5; the supplied sequence matches the Mumps virus genotype A Jeryl-Lynn entry.
- A separate viral-envelope GO annotation is inferred electronically, whereas the virion location annotation is supported by experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name compartments from very different biological contexts, but the supplied sequence alone does not establish that this protein is a viral matrix protein or show a distinctive signal that identifies virion association.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as the Mumps virus matrix protein and evidence that it is associated with virions.",
    "reason": "The expected answer is supported by reviewer-only protein-specific annotation and experimental evidence, neither of which was supplied to the evaluated model. Recognizing or recalling this exact sequence would be lookup or memorization, not reasoning from the input."
  },
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the 375-aa Mumps virus matrix protein. UniProt records its location as virion with experimental evidence (ECO:0000269; PubMed 26768080), supporting choice D."
  },
  "important_caveats": [
    "The experimental subcellular-location annotation cites a mass-spectrometry study of Mumps virus strain Jeryl-Lynn 5; the supplied sequence matches the Mumps virus genotype A Jeryl-Lynn entry.",
    "A separate viral-envelope GO annotation is inferred electronically, whereas the virion location annotation is supported by experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching protein-specific evidence supports virion association, and none of the other listed options is supported by the supplied sequence or reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the 375-aa Mumps virus matrix protein. UniProt records its location as virion with experimental evidence (ECO:0000269; PubMed 26768080), supporting choice D.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name compartments from very different biological contexts, but the supplied sequence alone does not establish that this protein is a viral matrix protein or show a distinctive signal that identifies virion association.",
    "missing_item_specific_fact": "The protein's identity as the Mumps virus matrix protein and evidence that it is associated with virions.",
    "reason": "The expected answer is supported by reviewer-only protein-specific annotation and experimental evidence, neither of which was supplied to the evaluated model. Recognizing or recalling this exact sequence would be lookup or memorization, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching protein-specific evidence supports virion association, and none of the other listed options is supported by the supplied sequence or reviewer-only evidence."
  },
  "important_caveats": [
    "The experimental subcellular-location annotation cites a mass-spectrometry study of Mumps virus strain Jeryl-Lynn 5; the supplied sequence matches the Mumps virus genotype A Jeryl-Lynn entry.",
    "A separate viral-envelope GO annotation is inferred electronically, whereas the virion location annotation is supported by experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9J4L4 (Matrix protein of Mumps virus, strain Jeryl-Lynn). The subcellular location annotation is 'Virion' with experimental evidence code ECO:0000269 (direct assay) from a mass spectrometry study (PubMed:26768080). The GO annotation links to GO:0019031 (viral envelope), which is is_a GO:0036338 (viral membrane), which is is_a GO:0044423 (virion component). The protein is a structural matrix protein of the virus particle, consistent with the virion component annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO5](#evidence-go5), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks an N-terminal signal peptide (no hydrophobic stretch of ~10-15 residues followed by a cleavage site), which is required for rhoptry biogenesis (rhoptry proteins transit the ER→Golgi→rhoptry secretory pathway) and for insertion into endosomal membranes. The sequence also lacks transmembrane domains (~20-residue hydrophobic stretches), making it incompatible with membrane-embedded structures like caveola or early endosome membrane. By elimination of these three eukaryotic compartment options based on absent targeting features, virion component (a small structural protein with no eukaryotic targeting signals) remains.


**Missing item-specific fact**

> None strictly required for elimination, though positive identification as a viral matrix protein would require knowing the organism is a paramyxovirus.


**Reason**

> The elimination reasoning is biologically grounded: rhoptry proteins require signal peptides for secretory-pathway biogenesis; caveola and early endosome membrane components require membrane association (TM domains or lipid anchors); the supplied sequence has neither. This leaves virion component as the only compatible option among the four choices. The argument relies on absence of features rather than positive viral motif recognition, but it constitutes a concrete biological distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three eukaryotic options (rhoptry, caveola, early endosome membrane) each require specific structural features (signal peptide, TM domains, or both) that are clearly absent from the sequence. Only virion component is compatible with a small protein lacking all eukaryotic targeting signals.


### Important caveats

- The reasoning relies on elimination by absence of features rather than positive recognition of viral protein motifs; a model might struggle to articulate why the absence of a signal peptide specifically rules out rhoptry without explicit knowledge of apicomplexan secretory pathway requirements.
- The GO annotation for viral envelope (GO:0019031) is IEA (inferred from electronic annotation via UniProt keyword), while the primary virion localization evidence is experimental (ECO:0000269, mass spectrometry).
- The reviewer identified the sequence as Mumps virus Matrix protein via UniProt accession Q9J4L4, but this accession was not provided to the evaluated model.
- The ontology term 'virion component' (GO:0044423) is a broad parent term; the more specific annotation is 'viral envelope' (GO:0019031), but the question only offers the parent term as option D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks an N-terminal signal peptide (no hydrophobic stretch of ~10-15 residues followed by a cleavage site), which is required for rhoptry biogenesis (rhoptry proteins transit the ER→Golgi→rhoptry secretory pathway) and for insertion into endosomal membranes. The sequence also lacks transmembrane domains (~20-residue hydrophobic stretches), making it incompatible with membrane-embedded structures like caveola or early endosome membrane. By elimination of these three eukaryotic compartment options based on absent targeting features, virion component (a small structural protein with no eukaryotic targeting signals) remains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination, though positive identification as a viral matrix protein would require knowing the organism is a paramyxovirus.",
    "reason": "The elimination reasoning is biologically grounded: rhoptry proteins require signal peptides for secretory-pathway biogenesis; caveola and early endosome membrane components require membrane association (TM domains or lipid anchors); the supplied sequence has neither. This leaves virion component as the only compatible option among the four choices. The argument relies on absence of features rather than positive viral motif recognition, but it constitutes a concrete biological distinction."
  },
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO5",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9J4L4 (Matrix protein of Mumps virus, strain Jeryl-Lynn). The subcellular location annotation is 'Virion' with experimental evidence code ECO:0000269 (direct assay) from a mass spectrometry study (PubMed:26768080). The GO annotation links to GO:0019031 (viral envelope), which is is_a GO:0036338 (viral membrane), which is is_a GO:0044423 (virion component). The protein is a structural matrix protein of the virus particle, consistent with the virion component annotation."
  },
  "important_caveats": [
    "The reasoning relies on elimination by absence of features rather than positive recognition of viral protein motifs; a model might struggle to articulate why the absence of a signal peptide specifically rules out rhoptry without explicit knowledge of apicomplexan secretory pathway requirements.",
    "The GO annotation for viral envelope (GO:0019031) is IEA (inferred from electronic annotation via UniProt keyword), while the primary virion localization evidence is experimental (ECO:0000269, mass spectrometry).",
    "The reviewer identified the sequence as Mumps virus Matrix protein via UniProt accession Q9J4L4, but this accession was not provided to the evaluated model.",
    "The ontology term 'virion component' (GO:0044423) is a broad parent term; the more specific annotation is 'viral envelope' (GO:0019031), but the question only offers the parent term as option D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three eukaryotic options (rhoptry, caveola, early endosome membrane) each require specific structural features (signal peptide, TM domains, or both) that are clearly absent from the sequence. Only virion component is compatible with a small protein lacking all eukaryotic targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9J4L4 (Matrix protein of Mumps virus, strain Jeryl-Lynn). The subcellular location annotation is 'Virion' with experimental evidence code ECO:0000269 (direct assay) from a mass spectrometry study (PubMed:26768080). The GO annotation links to GO:0019031 (viral envelope), which is is_a GO:0036338 (viral membrane), which is is_a GO:0044423 (virion component). The protein is a structural matrix protein of the virus particle, consistent with the virion component annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO5", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks an N-terminal signal peptide (no hydrophobic stretch of ~10-15 residues followed by a cleavage site), which is required for rhoptry biogenesis (rhoptry proteins transit the ER→Golgi→rhoptry secretory pathway) and for insertion into endosomal membranes. The sequence also lacks transmembrane domains (~20-residue hydrophobic stretches), making it incompatible with membrane-embedded structures like caveola or early endosome membrane. By elimination of these three eukaryotic compartment options based on absent targeting features, virion component (a small structural protein with no eukaryotic targeting signals) remains.",
    "missing_item_specific_fact": "None strictly required for elimination, though positive identification as a viral matrix protein would require knowing the organism is a paramyxovirus.",
    "reason": "The elimination reasoning is biologically grounded: rhoptry proteins require signal peptides for secretory-pathway biogenesis; caveola and early endosome membrane components require membrane association (TM domains or lipid anchors); the supplied sequence has neither. This leaves virion component as the only compatible option among the four choices. The argument relies on absence of features rather than positive viral motif recognition, but it constitutes a concrete biological distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three eukaryotic options (rhoptry, caveola, early endosome membrane) each require specific structural features (signal peptide, TM domains, or both) that are clearly absent from the sequence. Only virion component is compatible with a small protein lacking all eukaryotic targeting signals."
  },
  "important_caveats": [
    "The reasoning relies on elimination by absence of features rather than positive recognition of viral protein motifs; a model might struggle to articulate why the absence of a signal peptide specifically rules out rhoptry without explicit knowledge of apicomplexan secretory pathway requirements.",
    "The GO annotation for viral envelope (GO:0019031) is IEA (inferred from electronic annotation via UniProt keyword), while the primary virion localization evidence is experimental (ECO:0000269, mass spectrometry).",
    "The reviewer identified the sequence as Mumps virus Matrix protein via UniProt accession Q9J4L4, but this accession was not provided to the evaluated model.",
    "The ontology term 'virion component' (GO:0044423) is a broad parent term; the more specific annotation is 'viral envelope' (GO:0019031), but the question only offers the parent term as option D."
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

**Accession:** `Q9J4L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 48. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
"Q9J4L4"
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype A (strain Jeryl-Lynn)","taxonId":11168}
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
{"recommendedName":{"fullName":{"value":"Matrix protein"}}}
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"26768080","source":"PubMed"}],"id":"SL-0274","value":"Virion"}}]}
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
{"database":"GO","id":"GO:0019031","properties":[{"key":"GoTerm","value":"C:viral envelope"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-KW"}]}
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9J4L4.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:51.770411+00:00.  

```json
{"citation":{"authors":["Brgles M.","Bonta M.","Santak M.","Jagusic M.","Forcic D.","Halassy B.","Allmaier G.","Marchetti-Deschmann M."],"citationCrossReferences":[{"database":"PubMed","id":"26768080"},{"database":"DOI","id":"10.1186/s12985-016-0463-0"}],"citationType":"journal article","firstPage":"9","id":"26768080","journal":"Virol. J.","lastPage":"9","publicationDate":"2016","title":"Identification of mumps virus protein and lipid composition by mass spectrometry.","volume":"13"},"referenceComments":[{"type":"STRAIN","value":"Jeryl-Lynn 5"}],"referenceNumber":3,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `db77b6503ed5d0f15f346c034f114ac4d786474391a7548711384f870fa87807`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:32:56.031444+00:00.  

```text
ID   MATRX_MUMPJ             Reviewed;         375 AA.
AC   Q9J4L4; Q77IS4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2000, sequence version 1.
DT   28-JAN-2026, entry version 48.
DE   RecName: Full=Matrix protein;
GN   Name=M;
OS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11168;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:32:56.031444+00:00.  

```text
RN   [3]
RP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.
RC   STRAIN=Jeryl-Lynn 5;
RX   PubMed=26768080; DOI=10.1186/s12985-016-0463-0;
RA   Brgles M., Bonta M., Santak M., Jagusic M., Forcic D., Halassy B.,
RA   Allmaier G., Marchetti-Deschmann M.;
RT   "Identification of mumps virus protein and lipid composition by mass
RT   spectrometry.";
RL   Virol. J. 13:9-9(2016).
```

Source SHA-256: `4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)  
**Locator:** `lines 41-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:32:56.031444+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000269|PubMed:26768080}.
```

Source SHA-256: `4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9J4L4?format=txt&versions=48)  
**Locator:** `lines 53-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:32:56.031444+00:00.  

```text
DR   GO; GO:0019031; C:viral envelope; IEA:UniProtKB-KW.
```

Source SHA-256: `4c03a3566bfe1aff85853ab34701a3a38f1d512544587e75fa59f6fd06a188e8`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 226661-226667`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0036338
name: viral membrane
namespace: cellular_component
def: "The lipid bilayer of a virion, a complete fully infectious extracellular virus particle." [GOC:bm]
is_a: GO:0044423 ! virion component

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 257048-257062`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044423
name: virion component
namespace: cellular_component
alt_id: GO:0019012
def: "Any constituent part of a virion, a complete fully infectious extracellular virus particle." [GOC:jl]
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
synonym: "complete virus particle" RELATED []
synonym: "virion" RELATED []
synonym: "virion part" EXACT []
xref: Wikipedia:Virus
is_a: GO:0005575 ! cellular_component

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
