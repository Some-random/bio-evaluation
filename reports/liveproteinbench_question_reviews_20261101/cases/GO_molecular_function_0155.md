# GO_molecular_function_0155

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — protein heterodimerization activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTSGASNTDELNKSSHSKVSKKSTKSRSKSAKLELTGKNSLSASASSSIASAVSGGVAVGSLPATPTHLNMVTTPTTPTSSLGNYNLFDASFAVAGSGGHGLAGGIAGAEASGNSSRMGHQKSYAGFDPRSIKIFWEQHDQTDVELSQDVCARLAEDASYKVWELINNVKIYSRHSGGVVTYDLVNEVLKDADVPPMLGAMDSDWDRIDYDGSFYFHSDKIFELSAEFQKEVNLCTPDDADFQSICPVEDKHMDQLRQCVQSLVTAALFADSKSQTAAVCHAFQTPLMGSIYRVIVSKMVQLLAFKQQDHLSQRCWRLLRACNYNATANHNACRPEYFNLAEVLVSQLMAPYETIKAPHVDPDPGQTTSIKMEFEEELKVEPDQCHNPETQENPEVMGVEKQEQEPQMFPGESTMEHTIYKLQSEEEELNPQPEAEHLSSYFACPVGNGLVDELCETIGQLASQSGYLHAECLFLIKRRLARFFEGRHVSSERDFRYISRAVRGLIALGEYAFREFIPYIYKLRVEEIPDSLWPDLAPAAIFLGGHDDVYLYEWLEYGCGAALQPFLVHYARAYEKMVTRRYVKAKQPAYRIESVPGVRRLEWSTLAAAMCHGDDPSKALKPKPTLCEAFPDLQSPNLQLNCAGNIRFKFAGCRPVLLKPKVATVPHSEDSPSSAANGGGGGGASSDILIAKRKLFKPLTNVRKWSPISGYHYLRI

[Multiple Choices]
A. ubiquitin binding
B. phosphorelay sensor kinase activity
C. NAD+ binding
D. protein heterodimerization activity
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

> The supplied sequence matches the referenced 717-aa Drosophila Saf6 protein. Its GO annotation assigns protein heterodimerization activity based on physical-interaction evidence; the literature cited for the annotation identifies Saf6 as a histone-fold protein that replaces TAF6 in SAGA and reports interaction with TAF9. This supports D, while not establishing that it is the protein’s sole or primary function.

Citations as saved: [C6](#evidence-c6), [H8](#evidence-h8), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not show an obvious sensor-kinase or NAD-binding signature, and a histone-fold-like region could suggest protein interactions. But that alone does not establish this specific molecular function over other possible binding activities.


**Missing item-specific fact**

> The protein-specific identification as Saf6 and evidence that it interacts with a nonidentical partner such as TAF9.


**Reason**

> The answer is supported by sequence-matched external annotation and literature, but the input provides no protein identity, domain annotation, or interaction context. Inferring D from the exact sequence would require protein-specific recognition or lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence-matched protein heterodimerization annotation supports D; the evidence does not support another listed option.


### Important caveats

- The GO annotation is supported by physical-interaction evidence (IPI); the cited excerpts do not independently establish that heterodimerization is the protein’s primary or exclusive molecular function.
- The exact author source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not show an obvious sensor-kinase or NAD-binding signature, and a histone-fold-like region could suggest protein interactions. But that alone does not establish this specific molecular function over other possible binding activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as Saf6 and evidence that it interacts with a nonidentical partner such as TAF9.",
    "reason": "The answer is supported by sequence-matched external annotation and literature, but the input provides no protein identity, domain annotation, or interaction context. Inferring D from the exact sequence would require protein-specific recognition or lookup."
  },
  "case_id": "GO_molecular_function_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the referenced 717-aa Drosophila Saf6 protein. Its GO annotation assigns protein heterodimerization activity based on physical-interaction evidence; the literature cited for the annotation identifies Saf6 as a histone-fold protein that replaces TAF6 in SAGA and reports interaction with TAF9. This supports D, while not establishing that it is the protein’s sole or primary function."
  },
  "important_caveats": [
    "The GO annotation is supported by physical-interaction evidence (IPI); the cited excerpts do not independently establish that heterodimerization is the protein’s primary or exclusive molecular function.",
    "The exact author source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched protein heterodimerization annotation supports D; the evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the referenced 717-aa Drosophila Saf6 protein. Its GO annotation assigns protein heterodimerization activity based on physical-interaction evidence; the literature cited for the annotation identifies Saf6 as a histone-fold protein that replaces TAF6 in SAGA and reports interaction with TAF9. This supports D, while not establishing that it is the protein’s sole or primary function.",
    "evidence_ids": ["C6", "H8", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not show an obvious sensor-kinase or NAD-binding signature, and a histone-fold-like region could suggest protein interactions. But that alone does not establish this specific molecular function over other possible binding activities.",
    "missing_item_specific_fact": "The protein-specific identification as Saf6 and evidence that it interacts with a nonidentical partner such as TAF9.",
    "reason": "The answer is supported by sequence-matched external annotation and literature, but the input provides no protein identity, domain annotation, or interaction context. Inferring D from the exact sequence would require protein-specific recognition or lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched protein heterodimerization annotation supports D; the evidence does not support another listed option."
  },
  "important_caveats": [
    "The GO annotation is supported by physical-interaction evidence (IPI); the cited excerpts do not independently establish that heterodimerization is the protein’s primary or exclusive molecular function.",
    "The exact author source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VPT4 (SAGA factor-like TAF6, Saf6) carries GO:0046982 (protein heterodimerization activity) with IPI:FlyBase evidence code, backed by PubMed:20008933 which explicitly documents 'INTERACTION WITH TAF9' as a reference position. The protein is a histone fold domain-containing subunit of the SAGA complex that physically heterodimerizes with TAF9. The IPI evidence code indicates experimental (physical interaction) support, not merely computational inference. The GO term definition ('Binding to a nonidentical protein to form a heterodimer') matches the documented TAF6-TAF9 interaction.

Citations as saved: [C6](#evidence-c6), [H8](#evidence-h8), [C9](#evidence-c9), [H2](#evidence-h2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains a histone fold domain (HFD), a well-characterized ~60-70 residue structural motif defined by three alpha-helices separated by loops. In transcription factor biology, HFDs are the canonical heterodimerization modules (e.g., histone H2A-H2B, TAF6-TAF9, TAF11-TAF13). Recognizing an HFD in the sequence (alternating hydrophobic/charged residues forming helical interfaces) allows inference that the primary molecular function is heterodimerization. Options B (phosphorelay sensor kinase) and C (NAD+ binding) are eliminated by the absence of kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is eliminated because SAGA's deubiquitination activity resides in the Ubp6/USP22 subunit, not in HFD-containing structural subunits like TAF6-like proteins. Thus, among the four choices, heterodimerization is the only function consistent with an HFD-containing transcription complex subunit.


**Missing item-specific fact**

> The critical step is identifying the histone fold domain from the raw 717-residue sequence without external annotation. While the HFD-to-heterodimerization principle is general textbook knowledge, the specific domain boundary in this sequence is not marked, and the protein's identity as a TAF6-like protein (which contextualizes the HFD) requires either structural prediction or database recognition.


**Reason**

> A model with knowledge of histone fold domain biology can reason: (1) the sequence contains regions consistent with an HFD (helical, amphipathic segments with hydrophobic interfaces); (2) HFDs in transcription factors mediate heterodimerization; (3) the protein is part of a multiprotein complex (evidenced by its length, lack of catalytic motifs, and composition); (4) among the choices, only D matches an HFD-containing structural subunit. The distractors B and C are trivially eliminated. Option A is eliminable because ubiquitin-binding modules (UBA, UIM, NZF) have distinct sequence signatures absent here. The reasoning chain is defensible but depends on the non-trivial step of HFD recognition from sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (phosphorelay sensor kinase) and C (NAD+ binding) are clearly incompatible with a transcription factor subunit lacking kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is not supported for this specific subunit. The GO entry also lists 'transcription coactivator activity' (GO:0003713) and 'RNA polymerase II general transcription initiation factor activity' (GO:0016251), but neither appears among the choices, so no ambiguity arises within the given options.


### Important caveats

- The IPI:FlyBase annotation is the only experimentally supported molecular function GO term for this protein; other GO MF annotations (IEA:InterPro, IBA:GO_Central) are computational inferences.
- The histone fold domain identification from raw sequence is the critical reasoning step; without structural prediction tools or prior knowledge of TAF family proteins, this domain may not be reliably identified by a language model.
- The protein's 'primary' molecular function as heterodimerization reflects its structural/integrative role in SAGA rather than a catalytic or binding-to-nucleotide function; this is a contextual judgment about which molecular activity is most fundamental for this subunit.
- The GO annotation path shows no parent terms for GO:0046982 in the supplied graph (empty path), meaning it is a direct term with no broader context provided beyond its is_a to GO:0046983 (protein dimerization activity).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains a histone fold domain (HFD), a well-characterized ~60-70 residue structural motif defined by three alpha-helices separated by loops. In transcription factor biology, HFDs are the canonical heterodimerization modules (e.g., histone H2A-H2B, TAF6-TAF9, TAF11-TAF13). Recognizing an HFD in the sequence (alternating hydrophobic/charged residues forming helical interfaces) allows inference that the primary molecular function is heterodimerization. Options B (phosphorelay sensor kinase) and C (NAD+ binding) are eliminated by the absence of kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is eliminated because SAGA's deubiquitination activity resides in the Ubp6/USP22 subunit, not in HFD-containing structural subunits like TAF6-like proteins. Thus, among the four choices, heterodimerization is the only function consistent with an HFD-containing transcription complex subunit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The critical step is identifying the histone fold domain from the raw 717-residue sequence without external annotation. While the HFD-to-heterodimerization principle is general textbook knowledge, the specific domain boundary in this sequence is not marked, and the protein's identity as a TAF6-like protein (which contextualizes the HFD) requires either structural prediction or database recognition.",
    "reason": "A model with knowledge of histone fold domain biology can reason: (1) the sequence contains regions consistent with an HFD (helical, amphipathic segments with hydrophobic interfaces); (2) HFDs in transcription factors mediate heterodimerization; (3) the protein is part of a multiprotein complex (evidenced by its length, lack of catalytic motifs, and composition); (4) among the choices, only D matches an HFD-containing structural subunit. The distractors B and C are trivially eliminated. Option A is eliminable because ubiquitin-binding modules (UBA, UIM, NZF) have distinct sequence signatures absent here. The reasoning chain is defensible but depends on the non-trivial step of HFD recognition from sequence."
  },
  "case_id": "GO_molecular_function_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H8",
      "C9",
      "H2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VPT4 (SAGA factor-like TAF6, Saf6) carries GO:0046982 (protein heterodimerization activity) with IPI:FlyBase evidence code, backed by PubMed:20008933 which explicitly documents 'INTERACTION WITH TAF9' as a reference position. The protein is a histone fold domain-containing subunit of the SAGA complex that physically heterodimerizes with TAF9. The IPI evidence code indicates experimental (physical interaction) support, not merely computational inference. The GO term definition ('Binding to a nonidentical protein to form a heterodimer') matches the documented TAF6-TAF9 interaction."
  },
  "important_caveats": [
    "The IPI:FlyBase annotation is the only experimentally supported molecular function GO term for this protein; other GO MF annotations (IEA:InterPro, IBA:GO_Central) are computational inferences.",
    "The histone fold domain identification from raw sequence is the critical reasoning step; without structural prediction tools or prior knowledge of TAF family proteins, this domain may not be reliably identified by a language model.",
    "The protein's 'primary' molecular function as heterodimerization reflects its structural/integrative role in SAGA rather than a catalytic or binding-to-nucleotide function; this is a contextual judgment about which molecular activity is most fundamental for this subunit.",
    "The GO annotation path shows no parent terms for GO:0046982 in the supplied graph (empty path), meaning it is a direct term with no broader context provided beyond its is_a to GO:0046983 (protein dimerization activity)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (phosphorelay sensor kinase) and C (NAD+ binding) are clearly incompatible with a transcription factor subunit lacking kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is not supported for this specific subunit. The GO entry also lists 'transcription coactivator activity' (GO:0003713) and 'RNA polymerase II general transcription initiation factor activity' (GO:0016251), but neither appears among the choices, so no ambiguity arises within the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VPT4 (SAGA factor-like TAF6, Saf6) carries GO:0046982 (protein heterodimerization activity) with IPI:FlyBase evidence code, backed by PubMed:20008933 which explicitly documents 'INTERACTION WITH TAF9' as a reference position. The protein is a histone fold domain-containing subunit of the SAGA complex that physically heterodimerizes with TAF9. The IPI evidence code indicates experimental (physical interaction) support, not merely computational inference. The GO term definition ('Binding to a nonidentical protein to form a heterodimer') matches the documented TAF6-TAF9 interaction.",
    "evidence_ids": ["C6", "H8", "C9", "H2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains a histone fold domain (HFD), a well-characterized ~60-70 residue structural motif defined by three alpha-helices separated by loops. In transcription factor biology, HFDs are the canonical heterodimerization modules (e.g., histone H2A-H2B, TAF6-TAF9, TAF11-TAF13). Recognizing an HFD in the sequence (alternating hydrophobic/charged residues forming helical interfaces) allows inference that the primary molecular function is heterodimerization. Options B (phosphorelay sensor kinase) and C (NAD+ binding) are eliminated by the absence of kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is eliminated because SAGA's deubiquitination activity resides in the Ubp6/USP22 subunit, not in HFD-containing structural subunits like TAF6-like proteins. Thus, among the four choices, heterodimerization is the only function consistent with an HFD-containing transcription complex subunit.",
    "missing_item_specific_fact": "The critical step is identifying the histone fold domain from the raw 717-residue sequence without external annotation. While the HFD-to-heterodimerization principle is general textbook knowledge, the specific domain boundary in this sequence is not marked, and the protein's identity as a TAF6-like protein (which contextualizes the HFD) requires either structural prediction or database recognition.",
    "reason": "A model with knowledge of histone fold domain biology can reason: (1) the sequence contains regions consistent with an HFD (helical, amphipathic segments with hydrophobic interfaces); (2) HFDs in transcription factors mediate heterodimerization; (3) the protein is part of a multiprotein complex (evidenced by its length, lack of catalytic motifs, and composition); (4) among the choices, only D matches an HFD-containing structural subunit. The distractors B and C are trivially eliminated. Option A is eliminable because ubiquitin-binding modules (UBA, UIM, NZF) have distinct sequence signatures absent here. The reasoning chain is defensible but depends on the non-trivial step of HFD recognition from sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (phosphorelay sensor kinase) and C (NAD+ binding) are clearly incompatible with a transcription factor subunit lacking kinase or nucleotide-binding motifs. Option A (ubiquitin binding) is not supported for this specific subunit. The GO entry also lists 'transcription coactivator activity' (GO:0003713) and 'RNA polymerase II general transcription initiation factor activity' (GO:0016251), but neither appears among the choices, so no ambiguity arises within the given options."
  },
  "important_caveats": [
    "The IPI:FlyBase annotation is the only experimentally supported molecular function GO term for this protein; other GO MF annotations (IEA:InterPro, IBA:GO_Central) are computational inferences.",
    "The histone fold domain identification from raw sequence is the critical reasoning step; without structural prediction tools or prior knowledge of TAF family proteins, this domain may not be reliably identified by a language model.",
    "The protein's 'primary' molecular function as heterodimerization reflects its structural/integrative role in SAGA rather than a catalytic or binding-to-nucleotide function; this is a contextual judgment about which molecular activity is most fundamental for this subunit.",
    "The GO annotation path shows no parent terms for GO:0046982 in the supplied graph (empty path), meaning it is a direct term with no broader context provided beyond its is_a to GO:0046983 (protein dimerization activity)."
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

**Accession:** `Q9VPT4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 162. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:33.097127+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000353","id":"20008933","source":"PubMed"}],"id":"GO:0046982","properties":[{"key":"GoTerm","value":"F:protein heterodimerization activity"},{"key":"GoEvidenceType","value":"IPI:FlyBase"}]}
```

Source SHA-256: `5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VPT4.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:33.097127+00:00.  

```json
{"citation":{"authors":["Weake V.M.","Swanson S.K.","Mushegian A.","Florens L.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"20008933"},{"database":"DOI","id":"10.1101/gad.1846409"}],"citationType":"journal article","firstPage":"2818","id":"20008933","journal":"Genes Dev.","lastPage":"2823","publicationDate":"2009","title":"A novel histone fold domain-containing protein that replaces TAF6 in Drosophila SAGA is required for SAGA-dependent gene expression.","volume":"23"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","IDENTIFICATION IN THE SAGA COMPLEX","INTERACTION WITH TAF9","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `5bb29d60c0982033dc803a294900b30cec2f6c6b3f3aac32acb8b00148d3de27`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)  
**Locator:** `lines 77-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 162 / 2.  
**Retrieved:** 2026-11-02T04:33:41.451282+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, INTERACTION WITH TAF9,
RP   SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND IDENTIFICATION BY MASS
RP   SPECTROMETRY.
RX   PubMed=20008933; DOI=10.1101/gad.1846409;
RA   Weake V.M., Swanson S.K., Mushegian A., Florens L., Washburn M.P.,
RA   Abmayr S.M., Workman J.L.;
RT   "A novel histone fold domain-containing protein that replaces TAF6 in
RT   Drosophila SAGA is required for SAGA-dependent gene expression.";
RL   Genes Dev. 23:2818-2823(2009).
```

Source SHA-256: `0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VPT4?format=txt&versions=162)  
**Locator:** `lines 196-196`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 162 / 2.  
**Retrieved:** 2026-11-02T04:33:41.451282+00:00.  

```text
DR   GO; GO:0046982; F:protein heterodimerization activity; IPI:FlyBase.
```

Source SHA-256: `0b12479c6d76480f8d3ef0278def37f7ca4aa38dc8ab6658d44a996124b64063`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 282546-282553`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046982
name: protein heterodimerization activity
namespace: molecular_function
def: "Binding to a nonidentical protein to form a heterodimer." [GOC:ai]
subset: goslim_chembl
is_a: GO:0046983 ! protein dimerization activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
