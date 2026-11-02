# pathway_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRIRPSPPKKPTPGLLHEYADRLVAFEYSASKGLKPHTLLFISGLGDGLGTVAYLEDIVAALEGSQWSVFSPVISSSYGGWGTSGLGRDTDEMARCIEYIQKYKEGSGVHETERKIVIMGHSTGSQDVLTYISSPNPRHPQPGLDPGHGHRHKRMPPLRPQVDGAIMQAPVSDRQAIQTVLEEGNERHSAKYMRKVVNDAIAYAKKHTYEDYDSLDTIIPLPITAAIGYPASTAVSSRRFLSLTSPDSPDSPGEDDLFSSDLTDERLRKTFGMVRHRGVLKDQKGLLVLYSGNDPSVPAFVDKEGLLRRWRWATDADEKRAYWHGESGIIPGATHTLEGPGQVEQRKELVRRVWMFLADVEGDPRTSCHSARPLS

[Multiple Choices]
A. Secondary metabolite biosynthesis. .
B. L-fucose degradation. .
C. tetrahydrofolate interconversion. .
D. O-acetyl-L-homoserine from L-homoserine: step 1/1. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated with the pathway “Secondary metabolite biosynthesis.” The annotation carries ECO:0000269 evidence linked to a publication, though the supplied excerpts do not independently establish the details of that experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad enzyme-family inference, but it does not provide a defensible way to identify this protein’s specific pathway among the choices.


**Missing item-specific fact**

> The protein-specific functional association linking this esterase to secondary metabolite biosynthesis.


**Reason**

> That association is supplied by an external annotation and cited publication, not established by the sequence or other context given to the model. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports A; the supplied input alone does not distinguish the options, but that lack of answerability does not establish that another option is also correct.


### Important caveats

- The annotation’s cited evidence is experimental-code evidence in UniProt, but the primary study was not independently reviewed here.
- The author’s exact data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family inference, but it does not provide a defensible way to identify this protein’s specific pathway among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional association linking this esterase to secondary metabolite biosynthesis.",
    "reason": "That association is supplied by an external annotation and cited publication, not established by the sequence or other context given to the model. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "pathway_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with the pathway “Secondary metabolite biosynthesis.” The annotation carries ECO:0000269 evidence linked to a publication, though the supplied excerpts do not independently establish the details of that experiment."
  },
  "important_caveats": [
    "The annotation’s cited evidence is experimental-code evidence in UniProt, but the primary study was not independently reviewed here.",
    "The author’s exact data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports A; the supplied input alone does not distinguish the options, but that lack of answerability does not establish that another option is also correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with the pathway “Secondary metabolite biosynthesis.” The annotation carries ECO:0000269 evidence linked to a publication, though the supplied excerpts do not independently establish the details of that experiment.",
    "evidence_ids": ["C5", "H3", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family inference, but it does not provide a defensible way to identify this protein’s specific pathway among the choices.",
    "missing_item_specific_fact": "The protein-specific functional association linking this esterase to secondary metabolite biosynthesis.",
    "reason": "That association is supplied by an external annotation and cited publication, not established by the sequence or other context given to the model. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports A; the supplied input alone does not distinguish the options, but that lack of answerability does not establish that another option is also correct."
  },
  "important_caveats": [
    "The annotation’s cited evidence is experimental-code evidence in UniProt, but the primary study was not independently reviewed here.",
    "The author’s exact data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5AY37 (Esterase AN6793, Aspergillus nidulans) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:39334518 (2024 J. Nat. Prod. paper on an orsellinaldehyde derivative produced via an unlinked polyketide synthase gene). The sequence matches exactly (375 AA, same SHA256). The annotation is experimentally grounded.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a GHS motif (residues ~112-114: 'IMAGHSTGSQ') characteristic of serine hydrolases/esterases, which could weakly favor secondary metabolite biosynthesis (esterases are common in fungal polyketide assembly lines for deacetylation) over the other options: L-fucose degradation (involves kinases/isomerases), tetrahydrofolate interconversion (reductases/synthases), and O-acetyl-L-homoserine synthesis (a transferase reaction). However, this esterase heuristic is extremely general and does not uniquely identify 'secondary metabolite biosynthesis' as the pathway.


**Missing item-specific fact**

> The specific genomic context of AN6793 within a polyketide biosynthetic gene cluster in Aspergillus nidulans, and the 2024 experimental demonstration (PubMed:39334518) that this esterase participates in orsellinaldehyde derivative biosynthesis, are required to confidently assign this protein to 'Secondary metabolite biosynthesis' rather than to another esterase-containing pathway. The organism identity and gene-cluster context are not provided in the question input.


**Reason**

> While the GHS serine hydrolase motif is visible in the sequence and provides a weak general heuristic favoring secondary metabolism over the other three options (which involve non-hydrolase enzymes), the definitive pathway assignment depends on the item-specific fact that this particular esterase is embedded in a fungal polyketide gene cluster and was experimentally shown to participate in secondary metabolite biosynthesis. Without that context, 'esterase → secondary metabolism' is a very thin inference that could equally apply to lipid metabolism or other pathways not listed as distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four options, the esterase motif weakly disfavors B (kinases/isomerases), C (reductases/synthases), and D (transferase), making A the least contradictory choice. No other option is strongly defensible for an esterase.


### Important caveats

- The pathway annotation is from a 2024 publication (PubMed:39334518); the entry was first public in Feb 2025. The benchmark author's source snapshot date is unknown.
- The esterase motif (GHS) is visible in the sequence but does not by itself specify which secondary metabolite pathway or confirm fungal polyketide context.
- The organism (Aspergillus nidulans) and gene-cluster context are not provided in the model input, removing key reasoning context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GHS motif (residues ~112-114: 'IMAGHSTGSQ') characteristic of serine hydrolases/esterases, which could weakly favor secondary metabolite biosynthesis (esterases are common in fungal polyketide assembly lines for deacetylation) over the other options: L-fucose degradation (involves kinases/isomerases), tetrahydrofolate interconversion (reductases/synthases), and O-acetyl-L-homoserine synthesis (a transferase reaction). However, this esterase heuristic is extremely general and does not uniquely identify 'secondary metabolite biosynthesis' as the pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific genomic context of AN6793 within a polyketide biosynthetic gene cluster in Aspergillus nidulans, and the 2024 experimental demonstration (PubMed:39334518) that this esterase participates in orsellinaldehyde derivative biosynthesis, are required to confidently assign this protein to 'Secondary metabolite biosynthesis' rather than to another esterase-containing pathway. The organism identity and gene-cluster context are not provided in the question input.",
    "reason": "While the GHS serine hydrolase motif is visible in the sequence and provides a weak general heuristic favoring secondary metabolism over the other three options (which involve non-hydrolase enzymes), the definitive pathway assignment depends on the item-specific fact that this particular esterase is embedded in a fungal polyketide gene cluster and was experimentally shown to participate in secondary metabolite biosynthesis. Without that context, 'esterase → secondary metabolism' is a very thin inference that could equally apply to lipid metabolism or other pathways not listed as distractors."
  },
  "case_id": "pathway_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5AY37 (Esterase AN6793, Aspergillus nidulans) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:39334518 (2024 J. Nat. Prod. paper on an orsellinaldehyde derivative produced via an unlinked polyketide synthase gene). The sequence matches exactly (375 AA, same SHA256). The annotation is experimentally grounded."
  },
  "important_caveats": [
    "The pathway annotation is from a 2024 publication (PubMed:39334518); the entry was first public in Feb 2025. The benchmark author's source snapshot date is unknown.",
    "The esterase motif (GHS) is visible in the sequence but does not by itself specify which secondary metabolite pathway or confirm fungal polyketide context.",
    "The organism (Aspergillus nidulans) and gene-cluster context are not provided in the model input, removing key reasoning context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, the esterase motif weakly disfavors B (kinases/isomerases), C (reductases/synthases), and D (transferase), making A the least contradictory choice. No other option is strongly defensible for an esterase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5AY37 (Esterase AN6793, Aspergillus nidulans) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with evidence code ECO:0000269 (inferred from direct assay), citing PubMed:39334518 (2024 J. Nat. Prod. paper on an orsellinaldehyde derivative produced via an unlinked polyketide synthase gene). The sequence matches exactly (375 AA, same SHA256). The annotation is experimentally grounded.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a GHS motif (residues ~112-114: 'IMAGHSTGSQ') characteristic of serine hydrolases/esterases, which could weakly favor secondary metabolite biosynthesis (esterases are common in fungal polyketide assembly lines for deacetylation) over the other options: L-fucose degradation (involves kinases/isomerases), tetrahydrofolate interconversion (reductases/synthases), and O-acetyl-L-homoserine synthesis (a transferase reaction). However, this esterase heuristic is extremely general and does not uniquely identify 'secondary metabolite biosynthesis' as the pathway.",
    "missing_item_specific_fact": "The specific genomic context of AN6793 within a polyketide biosynthetic gene cluster in Aspergillus nidulans, and the 2024 experimental demonstration (PubMed:39334518) that this esterase participates in orsellinaldehyde derivative biosynthesis, are required to confidently assign this protein to 'Secondary metabolite biosynthesis' rather than to another esterase-containing pathway. The organism identity and gene-cluster context are not provided in the question input.",
    "reason": "While the GHS serine hydrolase motif is visible in the sequence and provides a weak general heuristic favoring secondary metabolism over the other three options (which involve non-hydrolase enzymes), the definitive pathway assignment depends on the item-specific fact that this particular esterase is embedded in a fungal polyketide gene cluster and was experimentally shown to participate in secondary metabolite biosynthesis. Without that context, 'esterase → secondary metabolism' is a very thin inference that could equally apply to lipid metabolism or other pathways not listed as distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, the esterase motif weakly disfavors B (kinases/isomerases), C (reductases/synthases), and D (transferase), making A the least contradictory choice. No other option is strongly defensible for an esterase."
  },
  "important_caveats": [
    "The pathway annotation is from a 2024 publication (PubMed:39334518); the entry was first public in Feb 2025. The benchmark author's source snapshot date is unknown.",
    "The esterase motif (GHS) is visible in the sequence but does not by itself specify which secondary metabolite pathway or confirm fungal polyketide context.",
    "The organism (Aspergillus nidulans) and gene-cluster context are not provided in the model input, removing key reasoning context."
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

**Accession:** `Q5AY37` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5AY37.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.777747+00:00.  

```json
"Q5AY37"
```

Source SHA-256: `a7b7825a8433d8f71b031c5c6eeecc95806f1862568e406629f31b7a66cc9617`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5AY37.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.777747+00:00.  

```json
{"commonName":"Aspergillus nidulans","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Eurotiomycetes","Eurotiomycetidae","Eurotiales","Aspergillaceae","Aspergillus","Nidulantes"],"scientificName":"Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 / M139)","taxonId":227321}
```

Source SHA-256: `a7b7825a8433d8f71b031c5c6eeecc95806f1862568e406629f31b7a66cc9617`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5AY37.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.777747+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39334518","source":"PubMed"}],"value":"3.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39334518","source":"PubMed"}],"value":"Esterase AN6793"}}}
```

Source SHA-256: `a7b7825a8433d8f71b031c5c6eeecc95806f1862568e406629f31b7a66cc9617`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5AY37.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.777747+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39334518","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `a7b7825a8433d8f71b031c5c6eeecc95806f1862568e406629f31b7a66cc9617`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5AY37.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.777747+00:00.  

```json
{"citation":{"authors":["Rabot C.","Grau M.F.","Entwistle R.","Chiang Y.M.","Zamora de Roberts Y.","Ahuja M.","Oakley C.E.","Wang C.C.C.","Todd R.B.","Oakley B.R."],"citationCrossReferences":[{"database":"PubMed","id":"39334518"},{"database":"DOI","id":"10.1021/acs.jnatprod.4c00483"}],"citationType":"journal article","firstPage":"0","id":"39334518","journal":"J. Nat. Prod.","lastPage":"0","publicationDate":"2024","title":"Transcription Factor Engineering in Aspergillus nidulans Leads to the Discovery of an Orsellinaldehyde Derivative Produced via an Unlinked Polyketide Synthase Gene.","volume":"0"},"referenceNumber":3,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `a7b7825a8433d8f71b031c5c6eeecc95806f1862568e406629f31b7a66cc9617`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AY37?format=txt&versions=86)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:31:08.148013+00:00.  

```text
ID   EST93_EMENI             Reviewed;         375 AA.
AC   Q5AY37; C8V283;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   28-JAN-2026, entry version 86.
DE   RecName: Full=Esterase AN6793 {ECO:0000303|PubMed:39334518};
DE            EC=3.1.-.- {ECO:0000269|PubMed:39334518};
GN   ORFNames=AN6793, ANIA_06793;
OS   Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 /
OS   M139) (Aspergillus nidulans).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Nidulantes.
OX   NCBI_TaxID=227321;
```

Source SHA-256: `0055cadbac4f13915eacdf632c2eb53ae550e02283575b43116e2745efc50fdc`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AY37?format=txt&versions=86)  
**Locator:** `lines 54-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:31:08.148013+00:00.  

```text
RN   [3]
RP   FUNCTION.
RX   PubMed=39334518; DOI=10.1021/acs.jnatprod.4c00483;
RA   Rabot C., Grau M.F., Entwistle R., Chiang Y.M., Zamora de Roberts Y.,
RA   Ahuja M., Oakley C.E., Wang C.C.C., Todd R.B., Oakley B.R.;
RT   "Transcription Factor Engineering in Aspergillus nidulans Leads to the
RT   Discovery of an Orsellinaldehyde Derivative Produced via an Unlinked
RT   Polyketide Synthase Gene.";
RL   J. Nat. Prod. 0:0-0(2024).
```

Source SHA-256: `0055cadbac4f13915eacdf632c2eb53ae550e02283575b43116e2745efc50fdc`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AY37?format=txt&versions=86)  
**Locator:** `lines 67-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:31:08.148013+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000269|PubMed:39334518}.
```

Source SHA-256: `0055cadbac4f13915eacdf632c2eb53ae550e02283575b43116e2745efc50fdc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
