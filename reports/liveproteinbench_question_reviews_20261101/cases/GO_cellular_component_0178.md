# GO_cellular_component_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — primosome complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVAHVALPVPLPRTFDYLLPEGMAVKAGCRVRVPFGKQERIGIVAAVSERSELPLDELKPVAEALDDEPVFSTTVWRLLMWAAEYYHHPIGDVLFHALPVMLRQGKPASATPLWYWFATEQGQVVDLNGLKRSRKQQQALAALRQGKIWRHQVGELEFNEAALQALRGKGLAELACEAPALTDWRSAYSVAGERLRLNTEQATAVGAIHSAADRFSAWLLAGITGSGKTEVYLSVLENVLAQGRQALVMVPEIGLTPQTIARFRQRFNAPVEVLHSGLNDSERLSAWLKAKNGEAAIVIGTRSSLFTPFKDLGVIVIDEEHDSSYKQQEGWRYHARDLAVWRAHSEQIPIILGSATPALETLHNVRQGKYRQLTLSKRAGNARPAQQHVLDLKGQPLQAGLSPALISRMRQHLQADNQVILFLNRRGFAPALLCHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCGSTHLVPVGIGTEQLEQALAPLFPEVPISRIDRDTTSRKGALEEHLAAVHRGGARILIGTQMLAKGHHFPDVTLVSLLDVDGALFSADFRSAERFAQLYTQVSGRAGRAGKQGEVILQTHHPEHPLLQTLLYKGYDAFAEQALAERQTMQLPPWTSHVLIRAEDHNNQQAPLFLQQLRNLLQASPLADEKLWVLGPVPALAPKRGGRWRWQILLQHPSRVRLQHIVSGTLALINTLPEARKVKWVLDVDPIEG

[Multiple Choices]
A. early endosome membrane
B. host cell plasma membrane
C. glutamatergic synapse
D. primosome complex
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

> The exact sequence matches a UniProt entry for bacterial replication restart protein PriA, and that entry annotates it to the primosome complex. The GO annotation is computational (IEA:UniProtKB-UniRule), not direct experimental evidence of localization, but it supports the keyed choice.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble ATP-dependent helicase, which makes the membrane and synapse choices implausible. But that general inference does not establish membership in the specific primosome complex.


**Missing item-specific fact**

> The protein's identity and function as PriA, a replication-restart helicase associated with the primosome, or an equivalent protein-specific annotation.


**Reason**

> Choosing D over the broad intracellular alternatives depends on identifying the particular protein or knowing its complex association; those facts are not explicitly supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the primosome complex is supported for this sequence; the other options describe eukaryotic membrane or synaptic components inconsistent with the bacterial protein.


### Important caveats

- The primosome annotation is computationally assigned by UniRule, not shown here as a direct experimental localization measurement.
- The reviewer-only sequence match and annotation support the answer key but were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble ATP-dependent helicase, which makes the membrane and synapse choices implausible. But that general inference does not establish membership in the specific primosome complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and function as PriA, a replication-restart helicase associated with the primosome, or an equivalent protein-specific annotation.",
    "reason": "Choosing D over the broad intracellular alternatives depends on identifying the particular protein or knowing its complex association; those facts are not explicitly supplied in the question."
  },
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry for bacterial replication restart protein PriA, and that entry annotates it to the primosome complex. The GO annotation is computational (IEA:UniProtKB-UniRule), not direct experimental evidence of localization, but it supports the keyed choice."
  },
  "important_caveats": [
    "The primosome annotation is computationally assigned by UniRule, not shown here as a direct experimental localization measurement.",
    "The reviewer-only sequence match and annotation support the answer key but were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the primosome complex is supported for this sequence; the other options describe eukaryotic membrane or synaptic components inconsistent with the bacterial protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry for bacterial replication restart protein PriA, and that entry annotates it to the primosome complex. The GO annotation is computational (IEA:UniProtKB-UniRule), not direct experimental evidence of localization, but it supports the keyed choice.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble ATP-dependent helicase, which makes the membrane and synapse choices implausible. But that general inference does not establish membership in the specific primosome complex.",
    "missing_item_specific_fact": "The protein's identity and function as PriA, a replication-restart helicase associated with the primosome, or an equivalent protein-specific annotation.",
    "reason": "Choosing D over the broad intracellular alternatives depends on identifying the particular protein or knowing its complex association; those facts are not explicitly supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the primosome complex is supported for this sequence; the other options describe eukaryotic membrane or synaptic components inconsistent with the bacterial protein."
  },
  "important_caveats": [
    "The primosome annotation is computationally assigned by UniRule, not shown here as a direct experimental localization measurement.",
    "The reviewer-only sequence match and annotation support the answer key but were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A6TGC5 annotates this protein (Replication restart protein PriA, EC 5.6.2.4) with GO:1990077 'primosome complex' (evidence IEA:UniProtKB-UniRule). The GO term definition describes protein complexes forming at stalled replication forks for replication restart, which matches PriA's well-established function. Structural evidence (PDB 4NL4, 4NL8) shows PriA in complex with SSB, consistent with primosome membership. The annotation is computational (IEA) rather than direct experimental, but PriA's role in the primosome is strongly supported by literature and structural biology.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO4](#evidence-go4), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The three distractors (early endosome membrane, host cell plasma membrane, glutamatergic synapse) are all eukaryotic-specific cellular structures. Klebsiella pneumoniae is a bacterium with no endosomes, no synapses, and no 'host cell plasma membrane' (a term describing viral context in eukaryotic hosts). This eliminates A, B, and C by basic organism biology. Additionally, the sequence contains a Walker A motif (ITGSGKTEVYLS), a Walker B-like motif (DEHDSSYK), and multiple zinc-binding motifs (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG), which are hallmarks of a RecA-like helicase/ATPase involved in DNA metabolism—consistent with a primosome-associated replication restart helicase. Among the four options, only 'primosome complex' (D) is a structure that exists in bacteria and matches a DNA helicase.


**Missing item-specific fact**

> None critical. Identifying the protein as specifically PriA (rather than any helicase) would require database lookup, but the elimination logic from organism type plus helicase motifs sufficiently distinguishes D from the three eukaryotic-only distractors.


**Reason**

> A model with general biological knowledge can (1) recognize the sequence is bacterial (no eukaryotic targeting signals, prokaryotic codon usage patterns), (2) eliminate A, B, C as eukaryotic-only structures, and (3) note helicase/ATPase motifs supporting a replication-complex assignment. The answer is reachable through reasoning without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (D, primosome complex) is compatible with a bacterial protein. The other three are strictly eukaryotic structures, leaving no ambiguity among the choices.


### Important caveats

- The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), not direct experimental evidence, though PriA's primosome role is well-supported by structural and biochemical literature.
- The reviewer identified the accession (A6TGC5) from dataset image-path metadata; this was not available to the evaluated model.
- The reasoning relies on recognizing the protein as bacterial and identifying helicase motifs; a model that fails to notice the Walker A motif or the organism context might struggle, though the elimination of three eukaryotic-only options remains a valid path.
- The 'host cell plasma membrane' term (GO:0020002) is defined in a viral/host context and is not applicable to a standalone bacterial protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The three distractors (early endosome membrane, host cell plasma membrane, glutamatergic synapse) are all eukaryotic-specific cellular structures. Klebsiella pneumoniae is a bacterium with no endosomes, no synapses, and no 'host cell plasma membrane' (a term describing viral context in eukaryotic hosts). This eliminates A, B, and C by basic organism biology. Additionally, the sequence contains a Walker A motif (ITGSGKTEVYLS), a Walker B-like motif (DEHDSSYK), and multiple zinc-binding motifs (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG), which are hallmarks of a RecA-like helicase/ATPase involved in DNA metabolism—consistent with a primosome-associated replication restart helicase. Among the four options, only 'primosome complex' (D) is a structure that exists in bacteria and matches a DNA helicase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the protein as specifically PriA (rather than any helicase) would require database lookup, but the elimination logic from organism type plus helicase motifs sufficiently distinguishes D from the three eukaryotic-only distractors.",
    "reason": "A model with general biological knowledge can (1) recognize the sequence is bacterial (no eukaryotic targeting signals, prokaryotic codon usage patterns), (2) eliminate A, B, C as eukaryotic-only structures, and (3) note helicase/ATPase motifs supporting a replication-complex assignment. The answer is reachable through reasoning without memorizing the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO4",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A6TGC5 annotates this protein (Replication restart protein PriA, EC 5.6.2.4) with GO:1990077 'primosome complex' (evidence IEA:UniProtKB-UniRule). The GO term definition describes protein complexes forming at stalled replication forks for replication restart, which matches PriA's well-established function. Structural evidence (PDB 4NL4, 4NL8) shows PriA in complex with SSB, consistent with primosome membership. The annotation is computational (IEA) rather than direct experimental, but PriA's role in the primosome is strongly supported by literature and structural biology."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), not direct experimental evidence, though PriA's primosome role is well-supported by structural and biochemical literature.",
    "The reviewer identified the accession (A6TGC5) from dataset image-path metadata; this was not available to the evaluated model.",
    "The reasoning relies on recognizing the protein as bacterial and identifying helicase motifs; a model that fails to notice the Walker A motif or the organism context might struggle, though the elimination of three eukaryotic-only options remains a valid path.",
    "The 'host cell plasma membrane' term (GO:0020002) is defined in a viral/host context and is not applicable to a standalone bacterial protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, primosome complex) is compatible with a bacterial protein. The other three are strictly eukaryotic structures, leaving no ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A6TGC5 annotates this protein (Replication restart protein PriA, EC 5.6.2.4) with GO:1990077 'primosome complex' (evidence IEA:UniProtKB-UniRule). The GO term definition describes protein complexes forming at stalled replication forks for replication restart, which matches PriA's well-established function. Structural evidence (PDB 4NL4, 4NL8) shows PriA in complex with SSB, consistent with primosome membership. The annotation is computational (IEA) rather than direct experimental, but PriA's role in the primosome is strongly supported by literature and structural biology.",
    "evidence_ids": ["C4", "C5", "C6", "GO4", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The three distractors (early endosome membrane, host cell plasma membrane, glutamatergic synapse) are all eukaryotic-specific cellular structures. Klebsiella pneumoniae is a bacterium with no endosomes, no synapses, and no 'host cell plasma membrane' (a term describing viral context in eukaryotic hosts). This eliminates A, B, and C by basic organism biology. Additionally, the sequence contains a Walker A motif (ITGSGKTEVYLS), a Walker B-like motif (DEHDSSYK), and multiple zinc-binding motifs (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG), which are hallmarks of a RecA-like helicase/ATPase involved in DNA metabolism—consistent with a primosome-associated replication restart helicase. Among the four options, only 'primosome complex' (D) is a structure that exists in bacteria and matches a DNA helicase.",
    "missing_item_specific_fact": "None critical. Identifying the protein as specifically PriA (rather than any helicase) would require database lookup, but the elimination logic from organism type plus helicase motifs sufficiently distinguishes D from the three eukaryotic-only distractors.",
    "reason": "A model with general biological knowledge can (1) recognize the sequence is bacterial (no eukaryotic targeting signals, prokaryotic codon usage patterns), (2) eliminate A, B, C as eukaryotic-only structures, and (3) note helicase/ATPase motifs supporting a replication-complex assignment. The answer is reachable through reasoning without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, primosome complex) is compatible with a bacterial protein. The other three are strictly eukaryotic structures, leaving no ambiguity among the choices."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA (Inferred from Electronic Annotation via UniRule), not direct experimental evidence, though PriA's primosome role is well-supported by structural and biochemical literature.",
    "The reviewer identified the accession (A6TGC5) from dataset image-path metadata; this was not available to the evaluated model.",
    "The reasoning relies on recognizing the protein as bacterial and identifying helicase motifs; a model that fails to notice the Walker A motif or the organism context might struggle, though the elimination of three eukaryotic-only options remains a valid path.",
    "The 'host cell plasma membrane' term (GO:0020002) is defined in a viral/host context and is not applicable to a standalone bacterial protein."
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

**Accession:** `A6TGC5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 115. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
"A6TGC5"
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Gammaproteobacteria","Enterobacterales","Enterobacteriaceae","Klebsiella","Klebsiella pneumoniae complex"],"scientificName":"Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578)","taxonId":272620}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"24379377","source":"PubMed"}],"value":"5.6.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"ATP-dependent DNA helicase PriA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305"}],"value":"DNA 3'-5' helicase PriA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24379377","source":"PubMed"}],"value":"PriA DNA helicase"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"}],"value":"Replication restart protein PriA"}}}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"database":"GO","id":"GO:1990077","properties":[{"key":"GoTerm","value":"C:primosome complex"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"citation":{"authors":["Bhattacharyya B.","George N.P.","Thurmes T.M.","Zhou R.","Jani N.","Wessel S.R.","Sandler S.J.","Ha T.","Keck J.L."],"citationCrossReferences":[{"database":"PubMed","id":"24379377"},{"database":"DOI","id":"10.1073/pnas.1318001111"}],"citationType":"journal article","firstPage":"1373","id":"24379377","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"1378","publicationDate":"2014","title":"Structural mechanisms of PriA-mediated DNA replication restart.","volume":"111"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4NL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4NL8","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 700721 / MGH 78578"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.65 ANGSTROMS) IN COMPLEX WITH ADP AND ZN(2+)","X-RAY CRYSTALLOGRAPHY (4.08 ANGSTROMS) IN COMPLEX WITH SSB","FUNCTION AS AN ATPASE","CATALYTIC ACTIVITY","DOMAIN","DNA-BINDING"]}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:27:08.474025+00:00.  

```text
ID   PRIA_KLEP7              Reviewed;         731 AA.
AC   A6TGC5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-AUG-2007, sequence version 1.
DT   28-JAN-2026, entry version 115.
DE   RecName: Full=Replication restart protein PriA {ECO:0000255|HAMAP-Rule:MF_00983};
DE   AltName: Full=ATP-dependent DNA helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};
DE            EC=5.6.2.4 {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305|PubMed:24379377};
DE   AltName: Full=DNA 3'-5' helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305};
DE   AltName: Full=PriA DNA helicase {ECO:0000303|PubMed:24379377};
GN   Name=priA {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000312|EMBL:ABR79609.1};
GN   ORFNames=KPN_04230 {ECO:0000312|EMBL:ABR79609.1};
OS   Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;
OC   Klebsiella; Klebsiella pneumoniae complex.
OX   NCBI_TaxID=272620;
```

Source SHA-256: `c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)  
**Locator:** `lines 116-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:27:08.474025+00:00.  

```text
DR   GO; GO:1990077; C:primosome complex; IEA:UniProtKB-UniRule.
```

Source SHA-256: `c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549032-549040`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990077
name: primosome complex
namespace: cellular_component
def: "Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart." [GOC:bhm, GOC:mah, PMID:21856207]
synonym: "primosome" EXACT []
is_a: GO:0032993 ! protein-DNA complex
relationship: part_of GO:0030894 ! replisome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
