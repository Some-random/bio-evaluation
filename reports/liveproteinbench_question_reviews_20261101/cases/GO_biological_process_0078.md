# GO_biological_process_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — iron-sulfur cluster assembly

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFNNFLNMYMCTLAEKLCKFKKNNFNNIHRNNNFYRDNNFYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNLYTNNNLYRDNNFYNITLRKFHFIQTISNNNFNFEIIKKYGDVINKIMFIHTQKKNKQERFMFNNKKYIKRKEYILNDLNEFISIIPHPEINNEITNNSNQKKNKDNKQNVLSTNQQIITNYNLNHKENVTSNLNFNNKEEDEKKLDKLLKKRNIKKRDIVTITEEAKEELKKIISINKKENNNNYNNMNTICSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK

[Multiple Choices]
A. symbiont entry into host cell
B. sporopollenin biosynthetic process
C. iron-sulfur cluster assembly
D. regulation of protein K48-linked ubiquitination
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches the reviewed Plasmodium falciparum IscA2 record. Its function annotation says it participates in iron-sulfur cluster biogenesis and can transfer &#91;4Fe-4S&#93; clusters; the record also assigns the GO term iron-sulfur cluster assembly. The function annotation cites experimental evidence, although the GO assignment itself is phylogenetically inferred.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains cysteines, but that feature alone does not establish iron-sulfur cluster assembly or distinguish it reliably from the other listed processes. Identifying this protein as IscA2 would supply the needed functional link, but that is a protein-specific identification rather than a conclusion warranted by the input alone.


**Missing item-specific fact**

> The sequence-specific identification as Plasmodium falciparum IscA2 and its experimentally supported role in iron-sulfur cluster biogenesis.


**Reason**

> The reviewer-only matched record supports choice C, but the supplied sequence and choices do not provide a sufficiently diagnostic biological argument to infer that specific process without the protein-specific annotation or identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports iron-sulfur cluster assembly among the listed choices; it does not establish another listed process as a competing answer.


### Important caveats

- The exact sequence match is established in reviewer-only evidence; the accession and annotation were not supplied to the evaluated model.
- The protein function annotation cites experimental evidence, while the GO iron-sulfur cluster assembly annotation is IBA (phylogenetically inferred).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains cysteines, but that feature alone does not establish iron-sulfur cluster assembly or distinguish it reliably from the other listed processes. Identifying this protein as IscA2 would supply the needed functional link, but that is a protein-specific identification rather than a conclusion warranted by the input alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification as Plasmodium falciparum IscA2 and its experimentally supported role in iron-sulfur cluster biogenesis.",
    "reason": "The reviewer-only matched record supports choice C, but the supplied sequence and choices do not provide a sufficiently diagnostic biological argument to infer that specific process without the protein-specific annotation or identification."
  },
  "case_id": "GO_biological_process_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the reviewed Plasmodium falciparum IscA2 record. Its function annotation says it participates in iron-sulfur cluster biogenesis and can transfer [4Fe-4S] clusters; the record also assigns the GO term iron-sulfur cluster assembly. The function annotation cites experimental evidence, although the GO assignment itself is phylogenetically inferred."
  },
  "important_caveats": [
    "The exact sequence match is established in reviewer-only evidence; the accession and annotation were not supplied to the evaluated model.",
    "The protein function annotation cites experimental evidence, while the GO iron-sulfur cluster assembly annotation is IBA (phylogenetically inferred)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports iron-sulfur cluster assembly among the listed choices; it does not establish another listed process as a competing answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the reviewed Plasmodium falciparum IscA2 record. Its function annotation says it participates in iron-sulfur cluster biogenesis and can transfer [4Fe-4S] clusters; the record also assigns the GO term iron-sulfur cluster assembly. The function annotation cites experimental evidence, although the GO assignment itself is phylogenetically inferred.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains cysteines, but that feature alone does not establish iron-sulfur cluster assembly or distinguish it reliably from the other listed processes. Identifying this protein as IscA2 would supply the needed functional link, but that is a protein-specific identification rather than a conclusion warranted by the input alone.",
    "missing_item_specific_fact": "The sequence-specific identification as Plasmodium falciparum IscA2 and its experimentally supported role in iron-sulfur cluster biogenesis.",
    "reason": "The reviewer-only matched record supports choice C, but the supplied sequence and choices do not provide a sufficiently diagnostic biological argument to infer that specific process without the protein-specific annotation or identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports iron-sulfur cluster assembly among the listed choices; it does not establish another listed process as a competing answer."
  },
  "important_caveats": [
    "The exact sequence match is established in reviewer-only evidence; the accession and annotation were not supplied to the evaluated model.",
    "The protein function annotation cites experimental evidence, while the GO iron-sulfur cluster assembly annotation is IBA (phylogenetically inferred)."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt O97297 (PfIscA2) from Plasmodium falciparum, experimentally characterized (PubMed:34032321, ECO:0000269) as participating in the iron-sulfur cluster formation (ISC) pathway and able to bind/transfer &#91;4Fe-4S&#93; clusters. GO:0016226 (iron-sulfur cluster assembly) is directly annotated. The sequence matches exactly (SHA256 confirmed). The expected answer C aligns with the GO annotation and experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains a CxxC motif (CPCG) and multiple cysteine residues clustered in the region 'CSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK'. The CxxC motif is a well-established signature of iron-sulfur cluster-binding proteins (ferredoxins, IscA-family, etc.). Additionally, the sequence lacks RING/HECT/RBR domains (required for K48-linked ubiquitination regulation, option D), lacks membrane-interaction/fusion domains (required for symbiont entry, option A), and lacks plant-specific enzyme features (sporopollenin biosynthesis, option B, is restricted to land plants). The combination of the CxxC motif and absence of alternative functional domains provides a concrete biological argument for Fe-S cluster assembly.


**Missing item-specific fact**

> None strictly required. The CxxC motif is identifiable directly from the supplied sequence, and elimination of distractors relies on general domain-knowledge.


**Reason**

> A knowledgeable biologist can identify the CxxC motif from the raw sequence and use general knowledge of Fe-S cluster protein signatures to select option C. The three distractors can be eliminated by the absence of characteristic domains (E3 ligase domains, membrane-fusion motifs, plant-specific biosynthetic enzymes). This constitutes a concrete, sequence-grounded biological argument rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The CxxC motif points specifically to Fe-S cluster binding. Option B (sporopollenin) is plant-specific and incompatible with the sequence composition. Option D requires ubiquitin-ligase machinery absent here. Option A requires membrane-interaction domains absent here. Only C is consistent with the identifiable sequence features.


### Important caveats

- The CxxC motif is not exclusively diagnostic of Fe-S cluster assembly; it occurs in other protein families. However, combined with the elimination of clearly incompatible alternatives, it provides meaningful grounds.
- The organism (Plasmodium falciparum) is not stated in the question, though the AT-rich amino-acid composition (high N, K, Y) is suggestive. Elimination of sporopollenin (B) partially relies on recognizing the sequence as non-plant.
- The GO annotation evidence code is IBA (Inferred by Biological Aspect), i.e., computational transfer from GO_Central, not direct experimental GO annotation. However, the underlying function is experimentally supported (PubMed:34032321).
- Reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and general knowledge provide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains a CxxC motif (CPCG) and multiple cysteine residues clustered in the region 'CSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK'. The CxxC motif is a well-established signature of iron-sulfur cluster-binding proteins (ferredoxins, IscA-family, etc.). Additionally, the sequence lacks RING/HECT/RBR domains (required for K48-linked ubiquitination regulation, option D), lacks membrane-interaction/fusion domains (required for symbiont entry, option A), and lacks plant-specific enzyme features (sporopollenin biosynthesis, option B, is restricted to land plants). The combination of the CxxC motif and absence of alternative functional domains provides a concrete biological argument for Fe-S cluster assembly.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The CxxC motif is identifiable directly from the supplied sequence, and elimination of distractors relies on general domain-knowledge.",
    "reason": "A knowledgeable biologist can identify the CxxC motif from the raw sequence and use general knowledge of Fe-S cluster protein signatures to select option C. The three distractors can be eliminated by the absence of characteristic domains (E3 ligase domains, membrane-fusion motifs, plant-specific biosynthetic enzymes). This constitutes a concrete, sequence-grounded biological argument rather than pure database lookup."
  },
  "case_id": "GO_biological_process_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt O97297 (PfIscA2) from Plasmodium falciparum, experimentally characterized (PubMed:34032321, ECO:0000269) as participating in the iron-sulfur cluster formation (ISC) pathway and able to bind/transfer [4Fe-4S] clusters. GO:0016226 (iron-sulfur cluster assembly) is directly annotated. The sequence matches exactly (SHA256 confirmed). The expected answer C aligns with the GO annotation and experimental evidence."
  },
  "important_caveats": [
    "The CxxC motif is not exclusively diagnostic of Fe-S cluster assembly; it occurs in other protein families. However, combined with the elimination of clearly incompatible alternatives, it provides meaningful grounds.",
    "The organism (Plasmodium falciparum) is not stated in the question, though the AT-rich amino-acid composition (high N, K, Y) is suggestive. Elimination of sporopollenin (B) partially relies on recognizing the sequence as non-plant.",
    "The GO annotation evidence code is IBA (Inferred by Biological Aspect), i.e., computational transfer from GO_Central, not direct experimental GO annotation. However, the underlying function is experimentally supported (PubMed:34032321).",
    "Reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and general knowledge provide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The CxxC motif points specifically to Fe-S cluster binding. Option B (sporopollenin) is plant-specific and incompatible with the sequence composition. Option D requires ubiquitin-ligase machinery absent here. Option A requires membrane-interaction domains absent here. Only C is consistent with the identifiable sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt O97297 (PfIscA2) from Plasmodium falciparum, experimentally characterized (PubMed:34032321, ECO:0000269) as participating in the iron-sulfur cluster formation (ISC) pathway and able to bind/transfer [4Fe-4S] clusters. GO:0016226 (iron-sulfur cluster assembly) is directly annotated. The sequence matches exactly (SHA256 confirmed). The expected answer C aligns with the GO annotation and experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C9", "H1", "H2", "H3", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains a CxxC motif (CPCG) and multiple cysteine residues clustered in the region 'CSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK'. The CxxC motif is a well-established signature of iron-sulfur cluster-binding proteins (ferredoxins, IscA-family, etc.). Additionally, the sequence lacks RING/HECT/RBR domains (required for K48-linked ubiquitination regulation, option D), lacks membrane-interaction/fusion domains (required for symbiont entry, option A), and lacks plant-specific enzyme features (sporopollenin biosynthesis, option B, is restricted to land plants). The combination of the CxxC motif and absence of alternative functional domains provides a concrete biological argument for Fe-S cluster assembly.",
    "missing_item_specific_fact": "None strictly required. The CxxC motif is identifiable directly from the supplied sequence, and elimination of distractors relies on general domain-knowledge.",
    "reason": "A knowledgeable biologist can identify the CxxC motif from the raw sequence and use general knowledge of Fe-S cluster protein signatures to select option C. The three distractors can be eliminated by the absence of characteristic domains (E3 ligase domains, membrane-fusion motifs, plant-specific biosynthetic enzymes). This constitutes a concrete, sequence-grounded biological argument rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The CxxC motif points specifically to Fe-S cluster binding. Option B (sporopollenin) is plant-specific and incompatible with the sequence composition. Option D requires ubiquitin-ligase machinery absent here. Option A requires membrane-interaction domains absent here. Only C is consistent with the identifiable sequence features."
  },
  "important_caveats": [
    "The CxxC motif is not exclusively diagnostic of Fe-S cluster assembly; it occurs in other protein families. However, combined with the elimination of clearly incompatible alternatives, it provides meaningful grounds.",
    "The organism (Plasmodium falciparum) is not stated in the question, though the AT-rich amino-acid composition (high N, K, Y) is suggestive. Elimination of sporopollenin (B) partially relies on recognizing the sequence as non-plant.",
    "The GO annotation evidence code is IBA (Inferred by Biological Aspect), i.e., computational transfer from GO_Central, not direct experimental GO annotation. However, the underlying function is experimentally supported (PubMed:34032321).",
    "Reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and general knowledge provide."
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

**Accession:** `O97297` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
"O97297"
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Iron-sulfur assembly protein IscA2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscA2"}]}}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind and transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321)"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cofactor biosynthesis; iron-sulfur cluster biosynthesis"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"database":"GO","id":"GO:0016226","properties":[{"key":"GoTerm","value":"P:iron-sulfur cluster assembly"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:14.613954+00:00.  

```json
{"citation":{"authors":["Sadik M.","Afsar M.","Ramachandran R.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"34032321"},{"database":"DOI","id":"10.1111/mmi.14735"}],"citationType":"journal article","firstPage":"606","id":"34032321","journal":"Mol. Microbiol.","lastPage":"623","publicationDate":"2021","title":"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
ID   ISCA2_PLAF7             Reviewed;         404 AA.
AC   O97297;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-1999, sequence version 1.
DT   28-JAN-2026, entry version 128.
DE   RecName: Full=Iron-sulfur assembly protein IscA2 {ECO:0000305};
DE            Short=PfIscA2 {ECO:0000303|PubMed:34032321};
GN   Name=IscA2 {ECO:0000305};
GN   ORFNames=PF3D7_0322500 {ECO:0000312|EMBL:CAB39044.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 62-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.
RX   PubMed=34032321; DOI=10.1111/mmi.14735;
RA   Sadik M., Afsar M., Ramachandran R., Habib S.;
RT   "[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the
RT   Plasmodium falciparum mitochondrion.";
RL   Mol. Microbiol. 116:606-623(2021).
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 78-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway
CC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind
CC       and transfer [4Fe-4S] clusters to target apo-proteins
CC       (PubMed:34032321). {ECO:0000269|PubMed:34032321}.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 82-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; iron-sulfur cluster biosynthesis.
CC       {ECO:0000305}.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)  
**Locator:** `lines 114-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:16.381564+00:00.  

```text
DR   GO; GO:0016226; P:iron-sulfur cluster assembly; IBA:GO_Central.
```

Source SHA-256: `f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 124825-124837`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016226
name: iron-sulfur cluster assembly
namespace: biological_process
def: "The incorporation of iron and exogenous sulfur into a metallo-sulfur cluster." [GOC:jl, GOC:mah, GOC:pde, GOC:vw]
subset: goslim_metagenomics
subset: goslim_pombe
synonym: "iron-sulfur cluster biosynthesis" RELATED []
synonym: "iron-sulphur cluster assembly" EXACT []
xref: Reactome:R-HSA-1362409 "Mitochondrial iron-sulfur cluster biogenesis"
xref: Reactome:R-HSA-2564830 "Cytosolic iron-sulfur cluster assembly"
is_a: GO:0031163 ! metallo-sulfur cluster assembly

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
