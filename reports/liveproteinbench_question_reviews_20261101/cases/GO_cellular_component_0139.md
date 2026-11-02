# GO_cellular_component_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nucleolus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLRQIKPRNARSKRALEKRAPKIVENPKTCLFLRGTTCSQITQDAMNDLYAMRQVHAKRFHKKNAIHPFEDATSLCFFSEKNDCSLMVFGSSNKKRPHTLTFVRMFDYKVLDMLEFYLDPDTYRSISQFKTSKIPIGMRPMMVFAGTAFESPVPNAFTMAKSMLIDFFRGEPSDKIDVEGLRFVVVVTADEPTSSTSTNNDGENPAPLPGMTDPRSIDPSQKPILRLRVYGIRTKRSGTRLPRVEVEEHGPRMDFRLGRMREPDPAMLKEAMKKAKTPQEERTKKNISMDLLGDKIGRIHMGKTDLSKLQTRKMKGLKRGRDEDEGGEDDRTDVVEAGSGEKKKKKKVKG

[Multiple Choices]
A. inner membrane pellicle complex
B. virion membrane
C. mitochondrial outer membrane
D. nucleolus
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

> The exact sequence matches the UniProt entry for an RPF2 homolog, whose annotation places it in the nucleolus. The localization is supported by a RuleBase computational annotation and an IEA GO annotation; the cited structural study concerns nascent 5S RNPs but does not itself establish localization experimentally.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has prominent basic clusters and no obvious transmembrane segment, which weakly favors a soluble nuclear/rRNA-associated protein over the membrane-related choices. Those features are not specific enough to establish nucleolar localization.


**Missing item-specific fact**

> The protein-specific fact that this sequence is an RPF2 ribosome-biogenesis homolog annotated to the nucleolus, or direct localization evidence, is absent from the question input.


**Reason**

> The sequence can make the membrane options less plausible, but selecting the precise nucleolus compartment depends on protein-specific functional or localization knowledge, not a sufficiently discriminating sequence feature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence and choices do not provide a comparably strong alternative to nucleolus; the sequence-matched annotation supports D. The sequence alone, however, would not uniquely establish that localization.


### Important caveats

- The cited nucleolar localization evidence is computational (RuleBase and IEA), not direct experimental localization evidence in the supplied excerpts.
- The reviewer-only database evidence supports the key but was not available to the evaluated model.
- The exact author data snapshot is unknown, although the historical entry checked has the same sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has prominent basic clusters and no obvious transmembrane segment, which weakly favors a soluble nuclear/rRNA-associated protein over the membrane-related choices. Those features are not specific enough to establish nucleolar localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is an RPF2 ribosome-biogenesis homolog annotated to the nucleolus, or direct localization evidence, is absent from the question input.",
    "reason": "The sequence can make the membrane options less plausible, but selecting the precise nucleolus compartment depends on protein-specific functional or localization knowledge, not a sufficiently discriminating sequence feature."
  },
  "case_id": "GO_cellular_component_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for an RPF2 homolog, whose annotation places it in the nucleolus. The localization is supported by a RuleBase computational annotation and an IEA GO annotation; the cited structural study concerns nascent 5S RNPs but does not itself establish localization experimentally."
  },
  "important_caveats": [
    "The cited nucleolar localization evidence is computational (RuleBase and IEA), not direct experimental localization evidence in the supplied excerpts.",
    "The reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The exact author data snapshot is unknown, although the historical entry checked has the same sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence and choices do not provide a comparably strong alternative to nucleolus; the sequence-matched annotation supports D. The sequence alone, however, would not uniquely establish that localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for an RPF2 homolog, whose annotation places it in the nucleolus. The localization is supported by a RuleBase computational annotation and an IEA GO annotation; the cited structural study concerns nascent 5S RNPs but does not itself establish localization experimentally.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has prominent basic clusters and no obvious transmembrane segment, which weakly favors a soluble nuclear/rRNA-associated protein over the membrane-related choices. Those features are not specific enough to establish nucleolar localization.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is an RPF2 ribosome-biogenesis homolog annotated to the nucleolus, or direct localization evidence, is absent from the question input.",
    "reason": "The sequence can make the membrane options less plausible, but selecting the precise nucleolus compartment depends on protein-specific functional or localization knowledge, not a sufficiently discriminating sequence feature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence and choices do not provide a comparably strong alternative to nucleolus; the sequence-matched annotation supports D. The sequence alone, however, would not uniquely establish that localization."
  },
  "important_caveats": [
    "The cited nucleolar localization evidence is computational (RuleBase and IEA), not direct experimental localization evidence in the supplied excerpts.",
    "The reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The exact author data snapshot is unknown, although the historical entry checked has the same sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt G0SF80 (RPF2_CHATD, Ribosome production factor 2 homolog from Chaetomium thermophilum). The subcellular location annotation is 'Nucleus, nucleolus' (C5, H3), and the GO annotation is GO:0005730 (nucleolus) (C6, H4). The protein is named a ribosome biogenesis factor, and the PDB structure 7OZS shows it in a 5S RNP assembly complex (C7, H2), consistent with nucleolar ribosome assembly. However, the primary evidence code for the localization is ECO:0000255 (RuleBase computational inference) and the GO annotation is IEA (Inferred from Electronic Annotation), so the localization is computationally inferred rather than directly experimentally determined. The biological function (ribosome biogenesis) strongly supports nucleolar localization.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is from a eukaryotic fungal protein (no viral capsid/envelope motifs, no apicomplexan pellicle-specific domains). Option A (inner membrane pellicle complex) is specific to apicomplexan parasites (GO:0070258 definition: 'apicomplexan parasite cell') and is irrelevant to a fungal protein. Option B (virion membrane) applies to viral proteins, not cellular fungal proteins. Option C (mitochondrial outer membrane) would typically require an N-terminal amphipathic mitochondrial targeting sequence rich in Arg/Ser and devoid of acidic residues; the N-terminus MLRQIKPRNARSKRALEKRAPKIVENPK... contains Pro, Glu, and lacks the classic amphipathic helix pattern of an MTS. The C-terminal 'KKKKKK' basic patch is more consistent with nuclear/nucleolar localization signals. By elimination of A, B, and C through general biological knowledge, D (nucleolus) is the only remaining plausible option.


**Missing item-specific fact**

> Positive identification of 'nucleolus' specifically (as opposed to generic 'nucleus' or 'cytoplasm') would be strengthened by recognizing the protein as a ribosome biogenesis factor (RPF2 homolog), which requires either sequence recognition or database lookup. However, since 'nucleolus' is the only nuclear option among the four choices, the elimination-based reasoning path is sufficient to arrive at D without this specific knowledge.


**Reason**

> The four choices can be meaningfully distinguished through general biological reasoning: A is organism-specific (apicomplexan), B is protein-type-specific (viral), C requires a mitochondrial targeting signal absent from the sequence, and D is the sole remaining nuclear option. The elimination path relies on broadly applicable biological knowledge rather than a single protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A (apicomplexan-specific) and B (viral) are clearly inapplicable to a fungal cellular protein. C (mitochondrial outer membrane) is disfavored by the absence of a canonical MTS and the presence of a C-terminal basic patch. D is the only nuclear/nucleolar option and the only choice consistent with the elimination reasoning. No two options are equally defensible.


### Important caveats

- The subcellular location annotation carries evidence code ECO:0000255 (RuleBase), a computational/curated inference, not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation).
- The PDB structure (7OZS) confirms the protein participates in 5S RNP assembly (ribosome biogenesis), which is consistent with nucleolar localization, but the structure itself does not directly report the subcellular compartment.
- The model does not receive the organism name or protein identity in the input; the reasoning relies on recognizing the absence of features specific to other options.
- The sequence is 350 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed across current and historical versions).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is from a eukaryotic fungal protein (no viral capsid/envelope motifs, no apicomplexan pellicle-specific domains). Option A (inner membrane pellicle complex) is specific to apicomplexan parasites (GO:0070258 definition: 'apicomplexan parasite cell') and is irrelevant to a fungal protein. Option B (virion membrane) applies to viral proteins, not cellular fungal proteins. Option C (mitochondrial outer membrane) would typically require an N-terminal amphipathic mitochondrial targeting sequence rich in Arg/Ser and devoid of acidic residues; the N-terminus MLRQIKPRNARSKRALEKRAPKIVENPK... contains Pro, Glu, and lacks the classic amphipathic helix pattern of an MTS. The C-terminal 'KKKKKK' basic patch is more consistent with nuclear/nucleolar localization signals. By elimination of A, B, and C through general biological knowledge, D (nucleolus) is the only remaining plausible option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of 'nucleolus' specifically (as opposed to generic 'nucleus' or 'cytoplasm') would be strengthened by recognizing the protein as a ribosome biogenesis factor (RPF2 homolog), which requires either sequence recognition or database lookup. However, since 'nucleolus' is the only nuclear option among the four choices, the elimination-based reasoning path is sufficient to arrive at D without this specific knowledge.",
    "reason": "The four choices can be meaningfully distinguished through general biological reasoning: A is organism-specific (apicomplexan), B is protein-type-specific (viral), C requires a mitochondrial targeting signal absent from the sequence, and D is the sole remaining nuclear option. The elimination path relies on broadly applicable biological knowledge rather than a single protein-specific annotation."
  },
  "case_id": "GO_cellular_component_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt G0SF80 (RPF2_CHATD, Ribosome production factor 2 homolog from Chaetomium thermophilum). The subcellular location annotation is 'Nucleus, nucleolus' (C5, H3), and the GO annotation is GO:0005730 (nucleolus) (C6, H4). The protein is named a ribosome biogenesis factor, and the PDB structure 7OZS shows it in a 5S RNP assembly complex (C7, H2), consistent with nucleolar ribosome assembly. However, the primary evidence code for the localization is ECO:0000255 (RuleBase computational inference) and the GO annotation is IEA (Inferred from Electronic Annotation), so the localization is computationally inferred rather than directly experimentally determined. The biological function (ribosome biogenesis) strongly supports nucleolar localization."
  },
  "important_caveats": [
    "The subcellular location annotation carries evidence code ECO:0000255 (RuleBase), a computational/curated inference, not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation).",
    "The PDB structure (7OZS) confirms the protein participates in 5S RNP assembly (ribosome biogenesis), which is consistent with nucleolar localization, but the structure itself does not directly report the subcellular compartment.",
    "The model does not receive the organism name or protein identity in the input; the reasoning relies on recognizing the absence of features specific to other options.",
    "The sequence is 350 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed across current and historical versions)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (apicomplexan-specific) and B (viral) are clearly inapplicable to a fungal cellular protein. C (mitochondrial outer membrane) is disfavored by the absence of a canonical MTS and the presence of a C-terminal basic patch. D is the only nuclear/nucleolar option and the only choice consistent with the elimination reasoning. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt G0SF80 (RPF2_CHATD, Ribosome production factor 2 homolog from Chaetomium thermophilum). The subcellular location annotation is 'Nucleus, nucleolus' (C5, H3), and the GO annotation is GO:0005730 (nucleolus) (C6, H4). The protein is named a ribosome biogenesis factor, and the PDB structure 7OZS shows it in a 5S RNP assembly complex (C7, H2), consistent with nucleolar ribosome assembly. However, the primary evidence code for the localization is ECO:0000255 (RuleBase computational inference) and the GO annotation is IEA (Inferred from Electronic Annotation), so the localization is computationally inferred rather than directly experimentally determined. The biological function (ribosome biogenesis) strongly supports nucleolar localization.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is from a eukaryotic fungal protein (no viral capsid/envelope motifs, no apicomplexan pellicle-specific domains). Option A (inner membrane pellicle complex) is specific to apicomplexan parasites (GO:0070258 definition: 'apicomplexan parasite cell') and is irrelevant to a fungal protein. Option B (virion membrane) applies to viral proteins, not cellular fungal proteins. Option C (mitochondrial outer membrane) would typically require an N-terminal amphipathic mitochondrial targeting sequence rich in Arg/Ser and devoid of acidic residues; the N-terminus MLRQIKPRNARSKRALEKRAPKIVENPK... contains Pro, Glu, and lacks the classic amphipathic helix pattern of an MTS. The C-terminal 'KKKKKK' basic patch is more consistent with nuclear/nucleolar localization signals. By elimination of A, B, and C through general biological knowledge, D (nucleolus) is the only remaining plausible option.",
    "missing_item_specific_fact": "Positive identification of 'nucleolus' specifically (as opposed to generic 'nucleus' or 'cytoplasm') would be strengthened by recognizing the protein as a ribosome biogenesis factor (RPF2 homolog), which requires either sequence recognition or database lookup. However, since 'nucleolus' is the only nuclear option among the four choices, the elimination-based reasoning path is sufficient to arrive at D without this specific knowledge.",
    "reason": "The four choices can be meaningfully distinguished through general biological reasoning: A is organism-specific (apicomplexan), B is protein-type-specific (viral), C requires a mitochondrial targeting signal absent from the sequence, and D is the sole remaining nuclear option. The elimination path relies on broadly applicable biological knowledge rather than a single protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (apicomplexan-specific) and B (viral) are clearly inapplicable to a fungal cellular protein. C (mitochondrial outer membrane) is disfavored by the absence of a canonical MTS and the presence of a C-terminal basic patch. D is the only nuclear/nucleolar option and the only choice consistent with the elimination reasoning. No two options are equally defensible."
  },
  "important_caveats": [
    "The subcellular location annotation carries evidence code ECO:0000255 (RuleBase), a computational/curated inference, not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation).",
    "The PDB structure (7OZS) confirms the protein participates in 5S RNP assembly (ribosome biogenesis), which is consistent with nucleolar localization, but the structure itself does not directly report the subcellular compartment.",
    "The model does not receive the organism name or protein identity in the input; the reasoning relies on recognizing the absence of features specific to other options.",
    "The sequence is 350 aa and matches the canonical UniProt entry exactly (SHA-256 confirmed across current and historical versions)."
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

**Accession:** `G0SF80` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 44. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SF80.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:29.279109+00:00.  

```json
"G0SF80"
```

Source SHA-256: `713eefb19cc3ee13431209a02b335bb38ae4b3021d3748a442fa0948fba34362`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SF80.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:29.279109+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU367086","source":"RuleBase"}],"value":"Ribosome biogenesis protein RPF2 homolog"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"Ribosome production factor 2 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"ctRPF2"}]}}
```

Source SHA-256: `713eefb19cc3ee13431209a02b335bb38ae4b3021d3748a442fa0948fba34362`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SF80.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:29.279109+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU367086","source":"RuleBase"}],"id":"SL-0188","value":"Nucleus, nucleolus"}}]}
```

Source SHA-256: `713eefb19cc3ee13431209a02b335bb38ae4b3021d3748a442fa0948fba34362`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SF80.json)  
**Locator:** `/uniProtKBCrossReferences/41`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:29.279109+00:00.  

```json
{"database":"GO","id":"GO:0005730","properties":[{"key":"GoTerm","value":"C:nucleolus"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `713eefb19cc3ee13431209a02b335bb38ae4b3021d3748a442fa0948fba34362`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SF80.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:29.279109+00:00.  

```json
{"citation":{"authors":["Castillo Duque de Estrada N.M.","Thoms M.","Flemming D.","Hammaren H.M.","Buschauer R.","Ameismeier M.","Bassler J.","Beck M.","Beckmann R.","Hurt E."],"citationCrossReferences":[{"database":"PubMed","id":"37291423"},{"database":"DOI","id":"10.1038/s41594-023-01006-7"}],"citationType":"journal article","firstPage":"1119","id":"37291423","journal":"Nat. Struct. Mol. Biol.","lastPage":"1131","publicationDate":"2023","title":"Structure of nascent 5S RNPs at the crossroad between ribosome assembly and MDM2-p53 pathways.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7OZS","source":"PDB"}],"referenceNumber":4,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11; RPL5; RRS1; SYO1 AND 5S RNA","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `713eefb19cc3ee13431209a02b335bb38ae4b3021d3748a442fa0948fba34362`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SF80?format=txt&versions=44)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:28:35.962335+00:00.  

```text
ID   RPF2_CHATD              Reviewed;         350 AA.
AC   G0SF80;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   18-JUN-2025, entry version 44.
DE   RecName: Full=Ribosome production factor 2 homolog {ECO:0000305|PubMed:37291423};
DE            Short=ctRPF2 {ECO:0000305|PubMed:37291423};
DE   AltName: Full=Ribosome biogenesis protein RPF2 homolog {ECO:0000255|RuleBase:RU367086};
GN   ORFNames=HT_0061110 {ECO:0000312|EMBL:EGS18096.1};
OS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)
OS   (Thermochaetoides thermophila).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.
OX   NCBI_TaxID=759272;
```

Source SHA-256: `41a88a0aef5a59e991a8baa59e9753574227312863d146bada42194a2644daab`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SF80?format=txt&versions=44)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:28:35.962335+00:00.  

```text
RN   [4] {ECO:0007744|PDB:7OZS}
RP   STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11;
RP   RPL5; RRS1; SYO1 AND 5S RNA, FUNCTION, AND SUBUNIT.
RX   PubMed=37291423; DOI=10.1038/s41594-023-01006-7;
RA   Castillo Duque de Estrada N.M., Thoms M., Flemming D., Hammaren H.M.,
RA   Buschauer R., Ameismeier M., Bassler J., Beck M., Beckmann R., Hurt E.;
RT   "Structure of nascent 5S RNPs at the crossroad between ribosome assembly
RT   and MDM2-p53 pathways.";
RL   Nat. Struct. Mol. Biol. 30:1119-1131(2023).
```

Source SHA-256: `41a88a0aef5a59e991a8baa59e9753574227312863d146bada42194a2644daab`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SF80?format=txt&versions=44)  
**Locator:** `lines 54-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:28:35.962335+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus, nucleolus
CC       {ECO:0000255|RuleBase:RU367086}.
```

Source SHA-256: `41a88a0aef5a59e991a8baa59e9753574227312863d146bada42194a2644daab`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SF80?format=txt&versions=44)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:28:35.962335+00:00.  

```text
DR   GO; GO:0005730; C:nucleolus; IEA:UniProtKB-SubCell.
```

Source SHA-256: `41a88a0aef5a59e991a8baa59e9753574227312863d146bada42194a2644daab`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
