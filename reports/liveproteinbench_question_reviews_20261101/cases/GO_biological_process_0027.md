# GO_biological_process_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — defense response to Gram-negative bacterium

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNFNRLFILVLVAVLVVLGQQQCGVEAAPRWKFGKKLEKVGKNVFNAAKKALPVVAGYKALG

[Multiple Choices]
A. drinking behavior
B. phosphate ion homeostasis
C. response to lipopolysaccharide
D. defense response to Gram-negative bacterium
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

> The sequence matches Aedes aegypti Cecropin-N. The matched record annotates defense response to Gram-negative bacterium (GO:0050829), but that annotation is computationally inferred by TreeGrafter, not direct experimental evidence for this exact process. The record also describes it as a putative antimicrobial peptide and reports experimental LPS-related effects, which are consistent with a defense role.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short sequence has a hydrophobic N-terminal leader followed by a highly basic, hydrophobic peptide, consistent with a secreted cationic antimicrobial peptide. That supports antibacterial defense more directly than drinking behavior or phosphate homeostasis; the LPS-response option is related to the reported LPS effects but is less directly indicated as the peptide’s primary role.


**Missing item-specific fact**

> A protein-specific annotation or experiment would be needed to verify the exact GO term for this sequence, but the broad antimicrobial-defense inference does not require that lookup.


**Reason**

> General sequence and biological knowledge offer a meaningful basis for favoring defense, although they do not establish Gram-negative specificity with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> LPS-related activity makes choice C relevant, but the evidence describes effects on LPS-induced responses, whereas choice D directly captures the antimicrobial-defense role.


### Important caveats

- The direct GO:0050829 annotation is computational (IEA:TreeGrafter); it should not be presented as experimental validation.
- Reported experiments establish LPS neutralization and anti-inflammatory effects, not necessarily direct killing of Gram-negative bacteria by this exact protein.
- The matched historical record supports that the annotation existed by the stated cutoff, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short sequence has a hydrophobic N-terminal leader followed by a highly basic, hydrophobic peptide, consistent with a secreted cationic antimicrobial peptide. That supports antibacterial defense more directly than drinking behavior or phosphate homeostasis; the LPS-response option is related to the reported LPS effects but is less directly indicated as the peptide’s primary role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A protein-specific annotation or experiment would be needed to verify the exact GO term for this sequence, but the broad antimicrobial-defense inference does not require that lookup.",
    "reason": "General sequence and biological knowledge offer a meaningful basis for favoring defense, although they do not establish Gram-negative specificity with certainty."
  },
  "case_id": "GO_biological_process_0027",
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
    "reason": "The sequence matches Aedes aegypti Cecropin-N. The matched record annotates defense response to Gram-negative bacterium (GO:0050829), but that annotation is computationally inferred by TreeGrafter, not direct experimental evidence for this exact process. The record also describes it as a putative antimicrobial peptide and reports experimental LPS-related effects, which are consistent with a defense role."
  },
  "important_caveats": [
    "The direct GO:0050829 annotation is computational (IEA:TreeGrafter); it should not be presented as experimental validation.",
    "Reported experiments establish LPS neutralization and anti-inflammatory effects, not necessarily direct killing of Gram-negative bacteria by this exact protein.",
    "The matched historical record supports that the annotation existed by the stated cutoff, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "LPS-related activity makes choice C relevant, but the evidence describes effects on LPS-induced responses, whereas choice D directly captures the antimicrobial-defense role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches Aedes aegypti Cecropin-N. The matched record annotates defense response to Gram-negative bacterium (GO:0050829), but that annotation is computationally inferred by TreeGrafter, not direct experimental evidence for this exact process. The record also describes it as a putative antimicrobial peptide and reports experimental LPS-related effects, which are consistent with a defense role.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short sequence has a hydrophobic N-terminal leader followed by a highly basic, hydrophobic peptide, consistent with a secreted cationic antimicrobial peptide. That supports antibacterial defense more directly than drinking behavior or phosphate homeostasis; the LPS-response option is related to the reported LPS effects but is less directly indicated as the peptide’s primary role.",
    "missing_item_specific_fact": "A protein-specific annotation or experiment would be needed to verify the exact GO term for this sequence, but the broad antimicrobial-defense inference does not require that lookup.",
    "reason": "General sequence and biological knowledge offer a meaningful basis for favoring defense, although they do not establish Gram-negative specificity with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "LPS-related activity makes choice C relevant, but the evidence describes effects on LPS-induced responses, whereas choice D directly captures the antimicrobial-defense role."
  },
  "important_caveats": [
    "The direct GO:0050829 annotation is computational (IEA:TreeGrafter); it should not be presented as experimental validation.",
    "Reported experiments establish LPS neutralization and anti-inflammatory effects, not necessarily direct killing of Gram-negative bacteria by this exact protein.",
    "The matched historical record supports that the annotation existed by the stated cutoff, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q17NR4 (Cecropin-N from Aedes aegypti) carries GO:0050829 (defense response to Gram-negative bacterium) as an annotation (evidence: IEA:TreeGrafter). The experimental function data (PubMed:30107813) confirm the protein is a putative antimicrobial peptide that partially neutralizes LPS and inhibits LPS-induced inflammatory signaling. Cecropins are a well-characterized family of insect antimicrobial peptides with primary activity against Gram-negative bacteria. The GO annotation for this exact sequence (matched, 62 AA) includes GO:0050829. The annotation evidence level is computational (IEA), but it is consistent with the experimental LPS-neutralization data and the established biology of cecropins.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 62-aa sequence shows a hydrophobic signal peptide (residues ~1–20) followed by a cationic, amphipathic mature peptide — hallmark features of insect antimicrobial peptides, specifically the cecropin family. Cecropins are textbook AMPs whose primary biological role is killing bacteria, preferentially Gram-negative ones (their amphipathic helices disrupt the outer membrane rich in LPS). The question asks for the 'primary biological process,' which for an AMP is defense against bacteria (D), not merely a downstream signaling response to an isolated stimulus molecule (C). The LPS-neutralization and anti-inflammatory activities are secondary mechanistic properties within the broader antibacterial defense program.


**Missing item-specific fact**

> None strictly required. Recognizing cecropin-family AMPs from sequence architecture (signal peptide + cationic amphipathic helix) and knowing their preferential Gram-negative targeting is general entomology/immunology knowledge. The specific database annotation for this exact protein reinforces but is not the sole basis for the choice.


**Reason**

> A knowledgeable model can reason from sequence features (signal peptide, cationic amphipathic mature domain) to 'antimicrobial peptide,' then from the well-established biology of cecropins to 'defense response to Gram-negative bacterium.' The distinction from option C rests on the conceptual hierarchy: an AMP's primary process is bacterial defense; LPS neutralization is a mechanism within that defense, not a standalone 'response to LPS' process. This is defensible general biological reasoning rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Option C (response to lipopolysaccharide, GO:0032496) is closely related because the protein's experimentally demonstrated activity includes LPS neutralization and suppression of LPS-induced inflammatory signaling. Without the 'primary' qualifier in the stem, a model could reasonably select C. However, the question explicitly asks for the 'overall biological objective' / 'primary biological process,' which favors the broader antibacterial defense category (D) over the narrower stimulus-response category (C). The GO ontology also does not annotate GO:0032496 for this protein, while GO:0050829 is present.


### Important caveats

- The GO:0050829 annotation is IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental evidence for this specific protein. The experimental data (PubMed:30107813) support LPS neutralization and anti-inflammatory activity but do not directly demonstrate killing of Gram-negative bacteria by this particular cecropin.
- The protein is also annotated with GO:0050830 (defense response to Gram-positive bacterium, IEA:UniProtKB-ARBA), so the Gram-negative specificity is not uniquely supported by annotation alone; it relies on general cecropin biology.
- Option C (response to lipopolysaccharide) is not annotated for this protein in UniProt but is mechanistically very close to the documented LPS-neutralization activity, making it a plausible but secondary distractor.
- The UniProt entry was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown, though the sequence has been stable since 2006.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 62-aa sequence shows a hydrophobic signal peptide (residues ~1–20) followed by a cationic, amphipathic mature peptide — hallmark features of insect antimicrobial peptides, specifically the cecropin family. Cecropins are textbook AMPs whose primary biological role is killing bacteria, preferentially Gram-negative ones (their amphipathic helices disrupt the outer membrane rich in LPS). The question asks for the 'primary biological process,' which for an AMP is defense against bacteria (D), not merely a downstream signaling response to an isolated stimulus molecule (C). The LPS-neutralization and anti-inflammatory activities are secondary mechanistic properties within the broader antibacterial defense program.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing cecropin-family AMPs from sequence architecture (signal peptide + cationic amphipathic helix) and knowing their preferential Gram-negative targeting is general entomology/immunology knowledge. The specific database annotation for this exact protein reinforces but is not the sole basis for the choice.",
    "reason": "A knowledgeable model can reason from sequence features (signal peptide, cationic amphipathic mature domain) to 'antimicrobial peptide,' then from the well-established biology of cecropins to 'defense response to Gram-negative bacterium.' The distinction from option C rests on the conceptual hierarchy: an AMP's primary process is bacterial defense; LPS neutralization is a mechanism within that defense, not a standalone 'response to LPS' process. This is defensible general biological reasoning rather than pure lookup."
  },
  "case_id": "GO_biological_process_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C7",
      "C9",
      "H1",
      "H3",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q17NR4 (Cecropin-N from Aedes aegypti) carries GO:0050829 (defense response to Gram-negative bacterium) as an annotation (evidence: IEA:TreeGrafter). The experimental function data (PubMed:30107813) confirm the protein is a putative antimicrobial peptide that partially neutralizes LPS and inhibits LPS-induced inflammatory signaling. Cecropins are a well-characterized family of insect antimicrobial peptides with primary activity against Gram-negative bacteria. The GO annotation for this exact sequence (matched, 62 AA) includes GO:0050829. The annotation evidence level is computational (IEA), but it is consistent with the experimental LPS-neutralization data and the established biology of cecropins."
  },
  "important_caveats": [
    "The GO:0050829 annotation is IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental evidence for this specific protein. The experimental data (PubMed:30107813) support LPS neutralization and anti-inflammatory activity but do not directly demonstrate killing of Gram-negative bacteria by this particular cecropin.",
    "The protein is also annotated with GO:0050830 (defense response to Gram-positive bacterium, IEA:UniProtKB-ARBA), so the Gram-negative specificity is not uniquely supported by annotation alone; it relies on general cecropin biology.",
    "Option C (response to lipopolysaccharide) is not annotated for this protein in UniProt but is mechanistically very close to the documented LPS-neutralization activity, making it a plausible but secondary distractor.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown, though the sequence has been stable since 2006."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Option C (response to lipopolysaccharide, GO:0032496) is closely related because the protein's experimentally demonstrated activity includes LPS neutralization and suppression of LPS-induced inflammatory signaling. Without the 'primary' qualifier in the stem, a model could reasonably select C. However, the question explicitly asks for the 'overall biological objective' / 'primary biological process,' which favors the broader antibacterial defense category (D) over the narrower stimulus-response category (C). The GO ontology also does not annotate GO:0032496 for this protein, while GO:0050829 is present."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q17NR4 (Cecropin-N from Aedes aegypti) carries GO:0050829 (defense response to Gram-negative bacterium) as an annotation (evidence: IEA:TreeGrafter). The experimental function data (PubMed:30107813) confirm the protein is a putative antimicrobial peptide that partially neutralizes LPS and inhibits LPS-induced inflammatory signaling. Cecropins are a well-characterized family of insect antimicrobial peptides with primary activity against Gram-negative bacteria. The GO annotation for this exact sequence (matched, 62 AA) includes GO:0050829. The annotation evidence level is computational (IEA), but it is consistent with the experimental LPS-neutralization data and the established biology of cecropins.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "C9", "H1", "H3", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 62-aa sequence shows a hydrophobic signal peptide (residues ~1–20) followed by a cationic, amphipathic mature peptide — hallmark features of insect antimicrobial peptides, specifically the cecropin family. Cecropins are textbook AMPs whose primary biological role is killing bacteria, preferentially Gram-negative ones (their amphipathic helices disrupt the outer membrane rich in LPS). The question asks for the 'primary biological process,' which for an AMP is defense against bacteria (D), not merely a downstream signaling response to an isolated stimulus molecule (C). The LPS-neutralization and anti-inflammatory activities are secondary mechanistic properties within the broader antibacterial defense program.",
    "missing_item_specific_fact": "None strictly required. Recognizing cecropin-family AMPs from sequence architecture (signal peptide + cationic amphipathic helix) and knowing their preferential Gram-negative targeting is general entomology/immunology knowledge. The specific database annotation for this exact protein reinforces but is not the sole basis for the choice.",
    "reason": "A knowledgeable model can reason from sequence features (signal peptide, cationic amphipathic mature domain) to 'antimicrobial peptide,' then from the well-established biology of cecropins to 'defense response to Gram-negative bacterium.' The distinction from option C rests on the conceptual hierarchy: an AMP's primary process is bacterial defense; LPS neutralization is a mechanism within that defense, not a standalone 'response to LPS' process. This is defensible general biological reasoning rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Option C (response to lipopolysaccharide, GO:0032496) is closely related because the protein's experimentally demonstrated activity includes LPS neutralization and suppression of LPS-induced inflammatory signaling. Without the 'primary' qualifier in the stem, a model could reasonably select C. However, the question explicitly asks for the 'overall biological objective' / 'primary biological process,' which favors the broader antibacterial defense category (D) over the narrower stimulus-response category (C). The GO ontology also does not annotate GO:0032496 for this protein, while GO:0050829 is present."
  },
  "important_caveats": [
    "The GO:0050829 annotation is IEA:TreeGrafter (computational phylogenetic transfer), not direct experimental evidence for this specific protein. The experimental data (PubMed:30107813) support LPS neutralization and anti-inflammatory activity but do not directly demonstrate killing of Gram-negative bacteria by this particular cecropin.",
    "The protein is also annotated with GO:0050830 (defense response to Gram-positive bacterium, IEA:UniProtKB-ARBA), so the Gram-negative specificity is not uniquely supported by annotation alone; it relies on general cecropin biology.",
    "Option C (response to lipopolysaccharide) is not annotated for this protein in UniProt but is mechanistically very close to the documented LPS-neutralization activity, making it a plausible but secondary distractor.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown, though the sequence has been stable since 2006."
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

**Accession:** `Q17NR4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
"Q17NR4"
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"commonName":"Yellowfever mosquito","evidences":[{"evidenceCode":"ECO:0000312","id":"AHH41648.1","source":"EMBL"}],"lineage":["Eukaryota","Metazoa","Ecdysozoa","Arthropoda","Altocrustacea","Allotriocarida","Hexapoda","Insecta","Pterygota","Neoptera","Eumetabola","Endopterygota","Aparaglossata","Panorpida","Diptera","Nematocera","Culicoidea","Culicidae","Culicinae","Aedini","Aedes","Stegomyia"],"scientificName":"Aedes aegypti","synonyms":["Culex aegypti"],"taxonId":7159}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30107813","source":"PubMed"}],"value":"AeaeCec5"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30107813","source":"PubMed"}],"value":"Cecropin-N"}}}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q17NR1","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30107813","source":"PubMed"}],"value":"Putative antimicrobial peptide (By similarity). Partially neutralizes lipopolysaccharides (LPS) (PubMed:30107813). Exhibits anti-inflammatory properties: inhibits LPS-induced iNOS/NOS2 transcription, nitric oxide (NO) and pro-inflammatory cytokine production in mouse macrophages and human peripheral blood mononuclear cells (PBMCs); inhibits LPS-induced activation of MAPK and NF-kappa-B signaling pathways in mouse macrophages (PubMed:30107813)"}]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"database":"GO","id":"GO:0050829","properties":[{"key":"GoTerm","value":"P:defense response to Gram-negative bacterium"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR4.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.756541+00:00.  

```json
{"citation":{"authors":["Wei L.","Yang Y.","Zhou Y.","Li M.","Yang H.","Mu L.","Qian Q.","Wu J.","Xu W."],"citationCrossReferences":[{"database":"PubMed","id":"30107813"},{"database":"DOI","id":"10.1186/s13071-018-3000-8"}],"citationType":"journal article","firstPage":"470","id":"30107813","journal":"Parasit. Vectors","lastPage":"470","publicationDate":"2018","title":"Anti-inflammatory activities of Aedes aegypti cecropins and their protection against murine endotoxin shock.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `5dd5228d85be4155ffeecd2aebc759d532ca9eff89a37d10111f7c7704f7b27e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
ID   CECN_AEDAE              Reviewed;          62 AA.
AC   Q17NR4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-JUL-2006, sequence version 1.
DT   28-JAN-2026, entry version 116.
DE   RecName: Full=Cecropin-N {ECO:0000303|PubMed:30107813};
DE   AltName: Full=AeaeCec5 {ECO:0000303|PubMed:30107813};
DE   Flags: Precursor;
GN   Name=CECN {ECO:0000305}; ORFNames=AAEL000621 {ECO:0000305};
OS   Aedes aegypti (Yellowfever mosquito) (Culex aegypti).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;
OC   Culicinae; Aedini; Aedes; Stegomyia.
OX   NCBI_TaxID=7159 {ECO:0000312|EMBL:AHH41648.1};
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 36-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
CC   -!- FUNCTION: Putative antimicrobial peptide (By similarity). Partially
CC       neutralizes lipopolysaccharides (LPS) (PubMed:30107813). Exhibits anti-
CC       inflammatory properties: inhibits LPS-induced iNOS/NOS2 transcription,
CC       nitric oxide (NO) and pro-inflammatory cytokine production in mouse
CC       macrophages and human peripheral blood mononuclear cells (PBMCs);
CC       inhibits LPS-induced activation of MAPK and NF-kappa-B signaling
CC       pathways in mouse macrophages (PubMed:30107813).
CC       {ECO:0000250|UniProtKB:Q17NR1, ECO:0000269|PubMed:30107813}.
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR4?format=txt&versions=116)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-01T06:28:29.854070+00:00.  

```text
DR   GO; GO:0050829; P:defense response to Gram-negative bacterium; IEA:TreeGrafter.
```

Source SHA-256: `d6ec678e9f74a2840167360e83614a6e35275d974e8fa612780550f8a53569f1`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 319898-319908`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0050829
name: defense response to Gram-negative bacterium
namespace: biological_process
def: "Reactions triggered in response to the presence of a Gram-negative bacterium that act to protect the cell or organism." [GOC:ai]
synonym: "defence response to Gram-negative bacteria" EXACT []
synonym: "defence response to Gram-negative bacterium" EXACT []
synonym: "defense response to Gram-negative bacteria" EXACT []
synonym: "Gram-negative antibacterial peptide activity" RELATED []
is_a: GO:0042742 ! defense response to bacterium

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
