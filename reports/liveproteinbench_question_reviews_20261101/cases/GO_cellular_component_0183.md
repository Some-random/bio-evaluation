# GO_cellular_component_0183

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLPSASNHAHAASPVYSNSNNNKSSASSKKTSSKNDLLRCAVGLLLKQKNYVSNERFRRSDFLLLQNKQQFAVNKMLDTDLHGGNSFTFSNVQVITNNQHTVDQQFGRFSQFVEAQAEPLRLEMKRFYGPMLCHFYLDLLKAREPRGAVELLRKYAHLVAPVDMYDAPPPTKINGCSTTANESTFNIRFAKEAQDTGDTELDYFMRLVQTLSGYTRLEAAESDDTVAHFRSSKYELHTTAVVVNRICAYLQRRGHVLIMNLLYTWLHVHIVENEQRAFSEDHLLGLTDDLEGEDGEDDVVSKPAVTLNTRGDIRPSKSLTEKSNRKRPAEEPNIMLETDIKQEVETDESAELSKLQLNIDACLDTLKSATEQILKSQVELPRFLRISERSRGLTSAHLDPSECHMLAGFDNSAVQLWQLNQSYCRGKSFYRRYPQKRCPWELNNCANQEEETDEDSSDEDVKCSEEERRERNRARHCKYADNSYNEYGGFQLRGHTKGVTDVRFSAHYPLMYSVSKDATMRCWRAHNLHCAAIYRSHNYPIWCLDESPVGQYVVTGSKDLSARLWSLEKEHALIIYAGHTQDVECVAFHPNGNYIATGSADHSVRLWCATSGKLMRVFADCRQAVTQLAFSPDGKMLAAAGEETKVRIFDLAAGAQLAELKDHSASISSLSWSTHNRHLATACSDGTLRLWDIKKLSPMSDNSSAGSSSSATTNRVLTVNSSCQRLVDVFYGTSKTLYCIGT

[Multiple Choices]
A. IRE1-TRAF2-ASK1 complex
B. virus tail, tube
C. nucleus
D. myelin sheath
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

> The exact sequence match is annotated to the nucleus, with experimental support: UniProt records nuclear localization based on cited studies, and the GO nucleus annotation is IDA:FlyBase. This supports choice C for this protein.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks an obvious transmembrane segment or secretion signal, making the ER-membrane complex and myelin-sheath options less plausible; basic residue clusters could be consistent with nuclear targeting. These features do not establish nuclear rather than cytosolic localization.


**Missing item-specific fact**

> The protein-specific evidence that this sequence is a SAGA-associated protein localized to the nucleus is absent from the input.


**Reason**

> The sequence provides suggestive clues but no decisive localization signal. Distinguishing the nucleus from other possible locations for a soluble protein depends on protein-specific functional or localization knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports nucleus, and none of the other listed options is comparably supported for this sequence.


### Important caveats

- The localization annotation is backed by experimental evidence, but the reviewer-only annotation and protein identity were not available to the evaluated model.
- The sequence matches the cited UniProt record; the actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks an obvious transmembrane segment or secretion signal, making the ER-membrane complex and myelin-sheath options less plausible; basic residue clusters could be consistent with nuclear targeting. These features do not establish nuclear rather than cytosolic localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this sequence is a SAGA-associated protein localized to the nucleus is absent from the input.",
    "reason": "The sequence provides suggestive clues but no decisive localization signal. Distinguishing the nucleus from other possible locations for a soluble protein depends on protein-specific functional or localization knowledge."
  },
  "case_id": "GO_cellular_component_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated to the nucleus, with experimental support: UniProt records nuclear localization based on cited studies, and the GO nucleus annotation is IDA:FlyBase. This supports choice C for this protein."
  },
  "important_caveats": [
    "The localization annotation is backed by experimental evidence, but the reviewer-only annotation and protein identity were not available to the evaluated model.",
    "The sequence matches the cited UniProt record; the actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports nucleus, and none of the other listed options is comparably supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated to the nucleus, with experimental support: UniProt records nuclear localization based on cited studies, and the GO nucleus annotation is IDA:FlyBase. This supports choice C for this protein.",
    "evidence_ids": ["C5", "C7", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks an obvious transmembrane segment or secretion signal, making the ER-membrane complex and myelin-sheath options less plausible; basic residue clusters could be consistent with nuclear targeting. These features do not establish nuclear rather than cytosolic localization.",
    "missing_item_specific_fact": "The protein-specific evidence that this sequence is a SAGA-associated protein localized to the nucleus is absent from the input.",
    "reason": "The sequence provides suggestive clues but no decisive localization signal. Distinguishing the nucleus from other possible locations for a soluble protein depends on protein-specific functional or localization knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports nucleus, and none of the other listed options is comparably supported for this sequence."
  },
  "important_caveats": [
    "The localization annotation is backed by experimental evidence, but the reviewer-only annotation and protein identity were not available to the evaluated model.",
    "The sequence matches the cited UniProt record; the actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VCN9 (TAF5L_DROME, protein 'will decrease acetylation' / wda, a WD40 repeat subunit of the Drosophila SAGA complex) is annotated with GO:0005634 (nucleus) with IDA:FlyBase evidence from PubMed:16980620 and 21764853, and the SUBCELLULAR LOCATION comment states 'Nucleus' with experimental evidence (ECO:0000269) from multiple publications (16980620, 20008933, 24493646). The protein is part of the SAGA chromatin-modifying complex that associates with chromosomes near transcriptional start sites. The sequence matches (SHA-256 identical, 743 aa). The answer 'nucleus' is the primary cellular component; 'chromosome' and 'SAGA complex' are sub-compartment/complex annotations within the nucleus.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of four options can be eliminated through general sequence analysis: (1) Option A (IRE1-TRAF2-ASK1 complex, an ER-membrane complex) requires transmembrane domains or ER-targeting signals; the 743-aa sequence lacks any ~20-residue hydrophobic TM segment. (2) Option B (virus tail, tube) refers to a bacteriophage structural protein; this sequence displays complex eukaryotic domain architecture including recognizable WD40 beta-propeller repeats in the C-terminal region, incompatible with a simple viral tail tube. (3) Option D (myelin sheath) requires highly hydrophobic membrane-associating proteins (e.g., MBP, PLP); this sequence is strongly hydrophilic with abundant charged and serine/threonine-rich regions. The remaining option C (nucleus) is positively supported by the WD40 repeat architecture (hallmark of nuclear chromatin-associated proteins), the hydrophilic/charged composition typical of nuclear regulatory proteins, and the absence of any non-nuclear targeting signal.


**Missing item-specific fact**

> None strictly required. Recognizing the WD40 repeats and applying general knowledge that they are prevalent in nuclear chromatin-remodeling complexes provides positive support beyond mere elimination.


**Reason**

> The elimination of A (no TM domain), B (eukaryotic multi-domain architecture with WD40 repeats, not a viral structural protein), and D (hydrophilic, not a myelin-type hydrophobic protein) relies on general biological knowledge of protein targeting and composition. The positive identification of nuclear localization via WD40 repeats and composition is achievable without database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different biological contexts (ER membrane complex, bacteriophage structure, nucleus, peripheral nerve myelin). Only 'nucleus' is consistent with the sequence's domain architecture and physicochemical properties. No other option is defensible for this sequence.


### Important caveats

- The protein is also annotated as part of the SAGA complex (GO:0000124) and on chromosomes (GO:0005694); however, 'nucleus' is the correct primary cellular component as the broadest compartment annotation.
- The identity of the protein as wda/TAF5L (SAGA subunit) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and choices.
- WD40 repeat recognition from sequence alone requires pattern-matching skill but is within the scope of general biological knowledge for a trained model.
- The UniProt entry was first publicly released 2025-06-18 (entry version 198); historical version 196 (2026-01-28) also matches the sequence and contains the same nucleus annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of four options can be eliminated through general sequence analysis: (1) Option A (IRE1-TRAF2-ASK1 complex, an ER-membrane complex) requires transmembrane domains or ER-targeting signals; the 743-aa sequence lacks any ~20-residue hydrophobic TM segment. (2) Option B (virus tail, tube) refers to a bacteriophage structural protein; this sequence displays complex eukaryotic domain architecture including recognizable WD40 beta-propeller repeats in the C-terminal region, incompatible with a simple viral tail tube. (3) Option D (myelin sheath) requires highly hydrophobic membrane-associating proteins (e.g., MBP, PLP); this sequence is strongly hydrophilic with abundant charged and serine/threonine-rich regions. The remaining option C (nucleus) is positively supported by the WD40 repeat architecture (hallmark of nuclear chromatin-associated proteins), the hydrophilic/charged composition typical of nuclear regulatory proteins, and the absence of any non-nuclear targeting signal.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the WD40 repeats and applying general knowledge that they are prevalent in nuclear chromatin-remodeling complexes provides positive support beyond mere elimination.",
    "reason": "The elimination of A (no TM domain), B (eukaryotic multi-domain architecture with WD40 repeats, not a viral structural protein), and D (hydrophilic, not a myelin-type hydrophobic protein) relies on general biological knowledge of protein targeting and composition. The positive identification of nuclear localization via WD40 repeats and composition is achievable without database lookup."
  },
  "case_id": "GO_cellular_component_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "C9",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VCN9 (TAF5L_DROME, protein 'will decrease acetylation' / wda, a WD40 repeat subunit of the Drosophila SAGA complex) is annotated with GO:0005634 (nucleus) with IDA:FlyBase evidence from PubMed:16980620 and 21764853, and the SUBCELLULAR LOCATION comment states 'Nucleus' with experimental evidence (ECO:0000269) from multiple publications (16980620, 20008933, 24493646). The protein is part of the SAGA chromatin-modifying complex that associates with chromosomes near transcriptional start sites. The sequence matches (SHA-256 identical, 743 aa). The answer 'nucleus' is the primary cellular component; 'chromosome' and 'SAGA complex' are sub-compartment/complex annotations within the nucleus."
  },
  "important_caveats": [
    "The protein is also annotated as part of the SAGA complex (GO:0000124) and on chromosomes (GO:0005694); however, 'nucleus' is the correct primary cellular component as the broadest compartment annotation.",
    "The identity of the protein as wda/TAF5L (SAGA subunit) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "WD40 repeat recognition from sequence alone requires pattern-matching skill but is within the scope of general biological knowledge for a trained model.",
    "The UniProt entry was first publicly released 2025-06-18 (entry version 198); historical version 196 (2026-01-28) also matches the sequence and contains the same nucleus annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (ER membrane complex, bacteriophage structure, nucleus, peripheral nerve myelin). Only 'nucleus' is consistent with the sequence's domain architecture and physicochemical properties. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VCN9 (TAF5L_DROME, protein 'will decrease acetylation' / wda, a WD40 repeat subunit of the Drosophila SAGA complex) is annotated with GO:0005634 (nucleus) with IDA:FlyBase evidence from PubMed:16980620 and 21764853, and the SUBCELLULAR LOCATION comment states 'Nucleus' with experimental evidence (ECO:0000269) from multiple publications (16980620, 20008933, 24493646). The protein is part of the SAGA chromatin-modifying complex that associates with chromosomes near transcriptional start sites. The sequence matches (SHA-256 identical, 743 aa). The answer 'nucleus' is the primary cellular component; 'chromosome' and 'SAGA complex' are sub-compartment/complex annotations within the nucleus.",
    "evidence_ids": ["C5", "C7", "C8", "C9", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of four options can be eliminated through general sequence analysis: (1) Option A (IRE1-TRAF2-ASK1 complex, an ER-membrane complex) requires transmembrane domains or ER-targeting signals; the 743-aa sequence lacks any ~20-residue hydrophobic TM segment. (2) Option B (virus tail, tube) refers to a bacteriophage structural protein; this sequence displays complex eukaryotic domain architecture including recognizable WD40 beta-propeller repeats in the C-terminal region, incompatible with a simple viral tail tube. (3) Option D (myelin sheath) requires highly hydrophobic membrane-associating proteins (e.g., MBP, PLP); this sequence is strongly hydrophilic with abundant charged and serine/threonine-rich regions. The remaining option C (nucleus) is positively supported by the WD40 repeat architecture (hallmark of nuclear chromatin-associated proteins), the hydrophilic/charged composition typical of nuclear regulatory proteins, and the absence of any non-nuclear targeting signal.",
    "missing_item_specific_fact": "None strictly required. Recognizing the WD40 repeats and applying general knowledge that they are prevalent in nuclear chromatin-remodeling complexes provides positive support beyond mere elimination.",
    "reason": "The elimination of A (no TM domain), B (eukaryotic multi-domain architecture with WD40 repeats, not a viral structural protein), and D (hydrophilic, not a myelin-type hydrophobic protein) relies on general biological knowledge of protein targeting and composition. The positive identification of nuclear localization via WD40 repeats and composition is achievable without database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (ER membrane complex, bacteriophage structure, nucleus, peripheral nerve myelin). Only 'nucleus' is consistent with the sequence's domain architecture and physicochemical properties. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The protein is also annotated as part of the SAGA complex (GO:0000124) and on chromosomes (GO:0005694); however, 'nucleus' is the correct primary cellular component as the broadest compartment annotation.",
    "The identity of the protein as wda/TAF5L (SAGA subunit) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "WD40 repeat recognition from sequence alone requires pattern-matching skill but is within the scope of general biological knowledge for a trained model.",
    "The UniProt entry was first publicly released 2025-06-18 (entry version 198); historical version 196 (2026-01-28) also matches the sequence and contains the same nucleus annotation."
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

**Accession:** `Q9VCN9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 196. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VCN9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.425946+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34807910","source":"PubMed"}],"value":"As part of the SAGA complex associates with chromosomes near transcriptional start sites, matching the distribution of RNA polymerase II"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20008933","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24493646","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34807910","source":"PubMed"}],"id":"SL-0468","value":"Chromosome"}}]}
```

Source SHA-256: `e06e8594df8cd0f806b950526bb3a98abb9e72fead87f94e4a8f3e0a673f93bd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VCN9.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.425946+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"21764853","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `e06e8594df8cd0f806b950526bb3a98abb9e72fead87f94e4a8f3e0a673f93bd`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VCN9.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.425946+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"16980620","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"21764853","source":"PubMed"}],"id":"GO:0000124","properties":[{"key":"GoTerm","value":"C:SAGA complex"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `e06e8594df8cd0f806b950526bb3a98abb9e72fead87f94e4a8f3e0a673f93bd`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VCN9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:14.425946+00:00.  

```json
{"citation":{"authors":["Guelman S.","Suganuma T.","Florens L.","Weake V.","Swanson S.K.","Washburn M.P.","Abmayr S.M.","Workman J.L."],"citationCrossReferences":[{"database":"PubMed","id":"16980620"},{"database":"DOI","id":"10.1128/mcb.00130-06"}],"citationType":"journal article","firstPage":"7178","id":"16980620","journal":"Mol. Cell. Biol.","lastPage":"7189","publicationDate":"2006","title":"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.","volume":"26"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","IDENTIFICATION IN SAGA COMPLEX","INTERACTION WITH GCN5; SEPT3 AND ADA2B","SUBCELLULAR LOCATION","WD DOMAIN","DISRUPTION PHENOTYPE","IDENTIFICATION BY MASS SPECTROMETRY"]}
```

Source SHA-256: `e06e8594df8cd0f806b950526bb3a98abb9e72fead87f94e4a8f3e0a673f93bd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VCN9?format=txt&versions=196)  
**Locator:** `lines 156-160`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:17.365794+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:16980620,
CC       ECO:0000269|PubMed:20008933, ECO:0000269|PubMed:24493646}. Chromosome
CC       {ECO:0000269|PubMed:34807910}. Note=As part of the SAGA complex
CC       associates with chromosomes near transcriptional start sites, matching
CC       the distribution of RNA polymerase II. {ECO:0000269|PubMed:34807910}.
```

Source SHA-256: `0c329a857fbbbc109643fb075760f11b782911eb16e23e0c96422d481f05316c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VCN9?format=txt&versions=196)  
**Locator:** `lines 208-208`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:17.365794+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IDA:FlyBase.
```

Source SHA-256: `0c329a857fbbbc109643fb075760f11b782911eb16e23e0c96422d481f05316c`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VCN9?format=txt&versions=196)  
**Locator:** `lines 209-209`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 196 / 1.  
**Retrieved:** 2026-11-02T04:33:17.365794+00:00.  

```text
DR   GO; GO:0000124; C:SAGA complex; IDA:FlyBase.
```

Source SHA-256: `0c329a857fbbbc109643fb075760f11b782911eb16e23e0c96422d481f05316c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
