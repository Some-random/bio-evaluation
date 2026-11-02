# pathway_0052

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDTTLVEAGDPAEDAPEWPMKRDTGCPFDPPPGVRKLLAEKPLSRARIWDGSTPWVVTRHADQRALLSDPRVSHDGLRDGYPHISADFKFLSMAQPSFAGQDDPEHGRIRRMVTLPFTARRIEAMRPAIQKITDELIDGMLAGPKPVDLVEALALPVPVRVICEMLGVPYEDREFLQQNNNAMIYRDTAQGDAQKAAIAQAMYLKELVGTKLGDRGDDILSDLAVQVEAGEITQDDAAGIGMMLLGAGHETTANMIALGTLALLENPEQLAEVRDSDDPKVIVNTVEELLRYLTIAQDTVRRIAAEDIEIGGVVIKAGEGIVFPLNAANWDPDLYPEAPDRLDIHRANARRHLAFGYGVHQCLGATLARVELQIVYSTLLRRIPTLALAGTLDEIPFKHDQIAHGVYELPVTW

[Multiple Choices]
A. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
B. iron-sulfur cluster biosynthesis. .
C. tetrahydrofolate biosynthesis
D. Antibiotic biosynthesis. .
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

> The supplied sequence exactly matches the sequence in the UniProt record for cytochrome P450 GfsF. That record assigns it to antibiotic biosynthesis and cites literature with experimental-evidence codes for the pathway annotation. This supports D, though the underlying studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a cytochrome P450 enzyme, which may make antibiotic tailoring plausible, but that enzyme class alone does not establish the specific pathway in which this protein functions.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence linking this exact sequence to antibiotic biosynthesis.


**Reason**

> The pathway assignment is supported by reviewer-only, literature-linked annotation, not by a pathway-specific clue supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied input does not establish a pathway assignment, but the reviewer evidence supports D; no alternative choice is comparably supported by the evidence provided.


### Important caveats

- Reviewer-only sources were not available to the evaluated model.
- The current and historical UniProt records match the supplied sequence; the exact source snapshot used by the author is unknown.
- The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a cytochrome P450 enzyme, which may make antibiotic tailoring plausible, but that enzyme class alone does not establish the specific pathway in which this protein functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence linking this exact sequence to antibiotic biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only, literature-linked annotation, not by a pathway-specific clue supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "pathway_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt record for cytochrome P450 GfsF. That record assigns it to antibiotic biosynthesis and cites literature with experimental-evidence codes for the pathway annotation. This supports D, though the underlying studies were not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only sources were not available to the evaluated model.",
    "The current and historical UniProt records match the supplied sequence; the exact source snapshot used by the author is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input does not establish a pathway assignment, but the reviewer evidence supports D; no alternative choice is comparably supported by the evidence provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt record for cytochrome P450 GfsF. That record assigns it to antibiotic biosynthesis and cites literature with experimental-evidence codes for the pathway annotation. This supports D, though the underlying studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a cytochrome P450 enzyme, which may make antibiotic tailoring plausible, but that enzyme class alone does not establish the specific pathway in which this protein functions.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence linking this exact sequence to antibiotic biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only, literature-linked annotation, not by a pathway-specific clue supplied in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied input does not establish a pathway assignment, but the reviewer evidence supports D; no alternative choice is comparably supported by the evidence provided."
  },
  "important_caveats": [
    "Reviewer-only sources were not available to the evaluated model.",
    "The current and historical UniProt records match the supplied sequence; the exact source snapshot used by the author is unknown.",
    "The pathway annotation cites experimental evidence, but the cited primary studies were not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the pathway as 'Antibiotic biosynthesis' with experimental evidence codes (ECO:0000269) from two peer-reviewed publications (PMID 20589823 and 26630077). The protein is a P450 monooxygenase involved in post-PKS modification of the 16-membered macrolide antibiotic FD-891. The sequence matches the benchmark exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable cytochrome P450 heme-binding motif features (the conserved FxxGxxxCxG region is visible as '...AFGYGVHQCLGATLARVELQ...' near the C-terminus, with the critical Cys ligand and Gly-rich loop). P450s are monooxygenases that catalyze oxidative modifications (hydroxylation, epoxidation) in secondary metabolite/antibiotic biosynthesis pathways, particularly in actinomycetes. Critically, none of the other three listed pathways—L-histidine biosynthesis (HisG, HisA, HisB, HisF, HisD, etc.), iron-sulfur cluster assembly (IscS, IscU, IscA, NifS, etc.), or tetrahydrofolate biosynthesis (FolP, FolC, FolE, etc.)—employ P450 monooxygenases as their catalytic enzymes. Thus, identifying P450 features in the sequence and applying general knowledge of P450 pathway participation meaningfully eliminates options A, B, and C while supporting D.


**Missing item-specific fact**

> None critical. Knowing the specific protein identity (GfsF) or the organism (Streptomyces halstedii) would confirm the answer but is not strictly necessary; general P450 biology and the exclusion of P450s from the other three pathways suffices.


**Reason**

> A model that recognizes the P450 heme-binding signature in the sequence can apply general biological knowledge: P450s are oxidoreductases central to secondary metabolite and antibiotic biosynthesis, but are not catalytic components of histidine, Fe-S cluster, or folate biosynthesis. This provides a concrete, sequence-grounded biological argument distinguishing D from A, B, and C without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct pathways. Options A, B, and C involve enzyme classes (lyases, ligases, sulfur-transferases, synthetases) that are categorically different from P450 monooxygenases. Option D (antibiotic biosynthesis) is the only pathway among the four that routinely employs P450s. Once P450 features are recognized, the choices are cleanly separated.


### Important caveats

- The P450 heme-binding motif in this sequence is somewhat degenerate (bacterial P450s often deviate from the canonical FxxGxxxCxG); recognition requires some familiarity with bacterial P450 signatures.
- The organism (Streptomyces) is not provided in the question input, which would otherwise strongly reinforce the antibiotic-biosynthesis assignment, since Streptomyces are prolific antibiotic producers.
- The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications characterizing FD-891 biosynthesis, lending high confidence to the key.
- The historical UniProt entry (version 48, first released 2025-03) already contained the pathway annotation, so the answer was available in databases at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 heme-binding motif features (the conserved FxxGxxxCxG region is visible as '...AFGYGVHQCLGATLARVELQ...' near the C-terminus, with the critical Cys ligand and Gly-rich loop). P450s are monooxygenases that catalyze oxidative modifications (hydroxylation, epoxidation) in secondary metabolite/antibiotic biosynthesis pathways, particularly in actinomycetes. Critically, none of the other three listed pathways—L-histidine biosynthesis (HisG, HisA, HisB, HisF, HisD, etc.), iron-sulfur cluster assembly (IscS, IscU, IscA, NifS, etc.), or tetrahydrofolate biosynthesis (FolP, FolC, FolE, etc.)—employ P450 monooxygenases as their catalytic enzymes. Thus, identifying P450 features in the sequence and applying general knowledge of P450 pathway participation meaningfully eliminates options A, B, and C while supporting D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Knowing the specific protein identity (GfsF) or the organism (Streptomyces halstedii) would confirm the answer but is not strictly necessary; general P450 biology and the exclusion of P450s from the other three pathways suffices.",
    "reason": "A model that recognizes the P450 heme-binding signature in the sequence can apply general biological knowledge: P450s are oxidoreductases central to secondary metabolite and antibiotic biosynthesis, but are not catalytic components of histidine, Fe-S cluster, or folate biosynthesis. This provides a concrete, sequence-grounded biological argument distinguishing D from A, B, and C without requiring memorization of this specific protein's database entry."
  },
  "case_id": "pathway_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the pathway as 'Antibiotic biosynthesis' with experimental evidence codes (ECO:0000269) from two peer-reviewed publications (PMID 20589823 and 26630077). The protein is a P450 monooxygenase involved in post-PKS modification of the 16-membered macrolide antibiotic FD-891. The sequence matches the benchmark exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The P450 heme-binding motif in this sequence is somewhat degenerate (bacterial P450s often deviate from the canonical FxxGxxxCxG); recognition requires some familiarity with bacterial P450 signatures.",
    "The organism (Streptomyces) is not provided in the question input, which would otherwise strongly reinforce the antibiotic-biosynthesis assignment, since Streptomyces are prolific antibiotic producers.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications characterizing FD-891 biosynthesis, lending high confidence to the key.",
    "The historical UniProt entry (version 48, first released 2025-03) already contained the pathway annotation, so the answer was available in databases at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct pathways. Options A, B, and C involve enzyme classes (lyases, ligases, sulfur-transferases, synthetases) that are categorically different from P450 monooxygenases. Option D (antibiotic biosynthesis) is the only pathway among the four that routinely employs P450s. Once P450 features are recognized, the choices are cleanly separated."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the pathway as 'Antibiotic biosynthesis' with experimental evidence codes (ECO:0000269) from two peer-reviewed publications (PMID 20589823 and 26630077). The protein is a P450 monooxygenase involved in post-PKS modification of the 16-membered macrolide antibiotic FD-891. The sequence matches the benchmark exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 heme-binding motif features (the conserved FxxGxxxCxG region is visible as '...AFGYGVHQCLGATLARVELQ...' near the C-terminus, with the critical Cys ligand and Gly-rich loop). P450s are monooxygenases that catalyze oxidative modifications (hydroxylation, epoxidation) in secondary metabolite/antibiotic biosynthesis pathways, particularly in actinomycetes. Critically, none of the other three listed pathways—L-histidine biosynthesis (HisG, HisA, HisB, HisF, HisD, etc.), iron-sulfur cluster assembly (IscS, IscU, IscA, NifS, etc.), or tetrahydrofolate biosynthesis (FolP, FolC, FolE, etc.)—employ P450 monooxygenases as their catalytic enzymes. Thus, identifying P450 features in the sequence and applying general knowledge of P450 pathway participation meaningfully eliminates options A, B, and C while supporting D.",
    "missing_item_specific_fact": "None critical. Knowing the specific protein identity (GfsF) or the organism (Streptomyces halstedii) would confirm the answer but is not strictly necessary; general P450 biology and the exclusion of P450s from the other three pathways suffices.",
    "reason": "A model that recognizes the P450 heme-binding signature in the sequence can apply general biological knowledge: P450s are oxidoreductases central to secondary metabolite and antibiotic biosynthesis, but are not catalytic components of histidine, Fe-S cluster, or folate biosynthesis. This provides a concrete, sequence-grounded biological argument distinguishing D from A, B, and C without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct pathways. Options A, B, and C involve enzyme classes (lyases, ligases, sulfur-transferases, synthetases) that are categorically different from P450 monooxygenases. Option D (antibiotic biosynthesis) is the only pathway among the four that routinely employs P450s. Once P450 features are recognized, the choices are cleanly separated."
  },
  "important_caveats": [
    "The P450 heme-binding motif in this sequence is somewhat degenerate (bacterial P450s often deviate from the canonical FxxGxxxCxG); recognition requires some familiarity with bacterial P450 signatures.",
    "The organism (Streptomyces) is not provided in the question input, which would otherwise strongly reinforce the antibiotic-biosynthesis assignment, since Streptomyces are prolific antibiotic producers.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from two independent publications characterizing FD-891 biosynthesis, lending high confidence to the key.",
    "The historical UniProt entry (version 48, first released 2025-03) already contained the pathway annotation, so the answer was available in databases at the time of benchmark construction."
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

**Accession:** `E0D207` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 48. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
"E0D207"
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20589823","source":"PubMed"}],"value":"P450 monooxygenase GfsF"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20589823","source":"PubMed"}],"value":"1.14.-.-"}],"fullName":{"value":"Cytochrome P450 GfsF"}}}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20589823","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26630077","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"citation":{"authors":["Kudo F.","Motegi A.","Mizoue K.","Eguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"20589823"},{"database":"DOI","id":"10.1002/cbic.201000214"}],"citationType":"journal article","firstPage":"1574","id":"20589823","journal":"ChemBioChem","lastPage":"1582","publicationDate":"2010","title":"Cloning and characterization of the biosynthetic gene cluster of 16-membered macrolide antibiotic FD-891: involvement of a dual functional cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ16472.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"A-8890"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"citation":{"authors":["Kudo F.","Kawamura K.","Furuya T.","Yamanishi H.","Motegi A.","Komatsubara A.","Numakura M.","Miyanaga A.","Eguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"26630077"},{"database":"DOI","id":"10.1002/cbic.201500533"}],"citationType":"journal article","firstPage":"233","id":"26630077","journal":"ChemBioChem","lastPage":"238","publicationDate":"2016","title":"Parallel Post-Polyketide Synthase Modification Mechanism Involved in FD-891 Biosynthesis in Streptomyces graminofaciens A-8890.","volume":"17"},"referenceComments":[{"type":"STRAIN","value":"A-8890"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D207?format=txt&versions=48)  
**Locator:** `lines 14-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:27:56.758195+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAJ16472.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,
RP   AND DISRUPTION PHENOTYPE.
RC   STRAIN=A-8890;
RX   PubMed=20589823; DOI=10.1002/cbic.201000214;
RA   Kudo F., Motegi A., Mizoue K., Eguchi T.;
RT   "Cloning and characterization of the biosynthetic gene cluster of 16-
RT   membered macrolide antibiotic FD-891: involvement of a dual functional
RT   cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.";
RL   ChemBioChem 11:1574-1582(2010).
```

Source SHA-256: `b7ff243274350eac91391be3b79c5530cd2a2ec42701fd8dc7b36bcbeb0f7237`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D207?format=txt&versions=48)  
**Locator:** `lines 78-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:27:56.758195+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000269|PubMed:20589823,
CC       ECO:0000269|PubMed:26630077}.
```

Source SHA-256: `b7ff243274350eac91391be3b79c5530cd2a2ec42701fd8dc7b36bcbeb0f7237`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
