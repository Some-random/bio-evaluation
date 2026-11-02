# GO_cellular_component_0080

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAASSMSSLTSSYHTTAMPSSNSVVPPFDARNLEIKTKSIEQTLIPLVTQITTLVNYKESYMASGKPKSERAMRAALKIGSAVEAAIERFVCVGETIADENADIQPEMYDACTEARLAGASMANLSCACNDDPNSVVDKAVLVRASRQLLSSVTRVLLLADRVLVKQVLRAEDKIAFSLSRLESTRSFNDFVKVFAVFGGEMVELAHRSGDRQHDLKSEKRKAQMSIARTSLERLTMLLLTASKTYLRHPDCDSALQCRDGVFYQMKLSLELIAICVCDGILTTEKSRYIQDEPDMPIDIALQLTANAAIKQLTEMLEMIRMTVRVGAGVRERIVSALDALCQLTQDFTDSAYTPHHQREQILDFLEECRFEMTNLIQPDENEQLAASGLEVTVERLNRRLKDLSKQLQIVAMEQISEVLRANEDQVLLSSMKACAVSGDIDGVEKYMHKFREHADHMQEVCRLLHHISITDALHVHTGHVERNMRALAPLTILAGRTLCVHPSSRIARENLEVFCDTWGQAVNDLSRVAKESDVAANGRVAAEKQAYMSLPRPGKHGTTQKPSKPITLDVEDQQKMAKVGLEMKLLTSEVDAEAEKWDEYAENDIVKRAKAMSSMAYNMYLFTRGDGPLKTTHDLFTQAEFFAEQANQMYRTVREFSYEVPGSAEKSDLSAILERIPLHCQQLQVMVKSPTVGKTATFGKVDSVIQETKNLMNEIAKLVTASFVCATKYEIEFRGGSVNGRTGADGERTSRESTVWRRTPSIRRAAPPTSSHLSANNSSSIHI

[Multiple Choices]
A. virus tail, tube
B. endoplasmic reticulum
C. plasma membrane
D. microtubule cytoskeleton
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

> The exact-sequence-matched UniProt record includes a plasma-membrane GO annotation with IDA:WormBase evidence, supporting choice C. The record also describes cytoplasmic localization near muscle dense bodies, so plasma membrane should not be read as an exclusive location.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not provide a clear plasma-membrane targeting signal or transmembrane segment; such a protein could associate peripherally with membranes, but that cannot be established from sequence alone.


**Missing item-specific fact**

> The protein-specific experimental localization evidence linking this alpha-catulin to the plasma membrane is absent from the input.


**Reason**

> The key distinction depends on localization knowledge specific to this protein, not a sufficiently discriminating general sequence-based argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the experimentally supported plasma-membrane annotation supports C. The additional cytoplasmic/dense-body localization is not one of the options and does not establish another listed choice.


### Important caveats

- The plasma-membrane GO annotation is reported as IDA:WormBase; the reviewer-only source evidence was not supplied to the evaluated model.
- The record also reports cytoplasmic localization near dense bodies in muscle cells, so the prompt's phrase “primary Cellular Component” may oversimplify a protein with multiple localization annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not provide a clear plasma-membrane targeting signal or transmembrane segment; such a protein could associate peripherally with membranes, but that cannot be established from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental localization evidence linking this alpha-catulin to the plasma membrane is absent from the input.",
    "reason": "The key distinction depends on localization knowledge specific to this protein, not a sufficiently discriminating general sequence-based argument."
  },
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record includes a plasma-membrane GO annotation with IDA:WormBase evidence, supporting choice C. The record also describes cytoplasmic localization near muscle dense bodies, so plasma membrane should not be read as an exclusive location."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is reported as IDA:WormBase; the reviewer-only source evidence was not supplied to the evaluated model.",
    "The record also reports cytoplasmic localization near dense bodies in muscle cells, so the prompt's phrase “primary Cellular Component” may oversimplify a protein with multiple localization annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the experimentally supported plasma-membrane annotation supports C. The additional cytoplasmic/dense-body localization is not one of the options and does not establish another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record includes a plasma-membrane GO annotation with IDA:WormBase evidence, supporting choice C. The record also describes cytoplasmic localization near muscle dense bodies, so plasma membrane should not be read as an exclusive location.",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not provide a clear plasma-membrane targeting signal or transmembrane segment; such a protein could associate peripherally with membranes, but that cannot be established from sequence alone.",
    "missing_item_specific_fact": "The protein-specific experimental localization evidence linking this alpha-catulin to the plasma membrane is absent from the input.",
    "reason": "The key distinction depends on localization knowledge specific to this protein, not a sufficiently discriminating general sequence-based argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the experimentally supported plasma-membrane annotation supports C. The additional cytoplasmic/dense-body localization is not one of the options and does not establish another listed choice."
  },
  "important_caveats": [
    "The plasma-membrane GO annotation is reported as IDA:WormBase; the reviewer-only source evidence was not supplied to the evaluated model.",
    "The record also reports cytoplasmic localization near dense bodies in muscle cells, so the prompt's phrase “primary Cellular Component” may oversimplify a protein with multiple localization annotations."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO annotation GO:0005886 (plasma membrane) is assigned to this protein (Alpha-catulin, CTN-1, UniProt G8JYB2) with IDA:WormBase evidence from PubMed 22577143, indicating direct experimental evidence for plasma membrane localization. This is consistent with alpha-catulin's role in the dystrophin-glycoprotein complex at the muscle cell membrane (dense bodies). However, the UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' with note 'Localizes near dense bodies in muscle cells,' creating a partial annotation conflict. The GO-specific annotation with IDA evidence supports the expected answer, and since the question explicitly asks about GO Cellular Component, the plasma membrane GO term is the relevant annotation.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3), [C8](#evidence-c8), [C10](#evidence-c10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can eliminate A (virus tail) because this is a eukaryotic C. elegans protein, and B (ER) because there is no N-terminal signal peptide or ER retention motif (KDEL/HDEL). Between C (plasma membrane) and D (microtubule cytoskeleton), the sequence lacks transmembrane domains, microtubule-binding motifs (e.g., MAP domains), or obvious plasma membrane targeting signals (myristoylation, palmitoylation, GPI anchor). The protein is a large (~784 aa) peripheral protein with coiled-coil regions that associates with the membrane indirectly through the dystrophin complex. Distinguishing C from D requires knowing that alpha-catulin is a component of the dystrophin-glycoprotein complex at the muscle membrane rather than a microtubule-associated protein.


**Missing item-specific fact**

> The specific protein-protein interaction knowledge that alpha-catulin (CTN-1) is a scaffolding component of the dystrophin complex at the muscle cell plasma membrane (dense bodies), rather than being a cytoplasmic or microtubule-associated protein. The sequence itself contains no intrinsic plasma membrane targeting signal; localization depends on indirect association through protein interactions that cannot be inferred from the primary sequence alone.


**Reason**

> The protein lacks any obvious sequence feature (transmembrane helix, lipid modification site, signal peptide, microtubule-binding domain) that would allow confident assignment to plasma membrane over other cytoplasmic/cytoskeletal compartments. The plasma membrane localization is an emergent property of its role in a multi-protein complex (dystrophin-glycoprotein complex) at the muscle membrane, which is protein-specific knowledge not derivable from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four given options, A (virus tail) and B (ER) are clearly eliminable. D (microtubule cytoskeleton) is unlikely for a catenin-family protein. While the UniProt SUBCELLULAR LOCATION says 'Cytoplasm,' this is not among the choices, so it does not create direct ambiguity within the provided options. Plasma membrane (C) is the most specific GO annotation with IDA evidence among the available choices. However, the 'Cytoplasm' vs. 'plasma membrane' annotation conflict in UniProt introduces some conceptual uncertainty about whether 'primary' location is cytoplasmic or membrane-associated, though this does not map to a different available option.


### Important caveats

- The UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' while the GO cross-reference states 'plasma membrane' (IDA). These are not fully consistent, though dense bodies are plasma-membrane-associated structures, reconciling the two.
- The expected answer relies on the GO annotation (GO:0005886) rather than the UniProt CC field, which is appropriate given the question asks about GO Cellular Component.
- The protein has no transmembrane domain; its plasma membrane association is indirect via protein-protein interactions (dystrophin complex, BK channels).
- The identity of this protein as alpha-catulin/CTN-1 from C. elegans was determined by reviewer-only sequence matching; the evaluated model only sees the raw sequence.
- Evidence code IDA (Inferred from Direct Assay) indicates experimental localization, lending stronger support to the plasma membrane GO annotation than computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can eliminate A (virus tail) because this is a eukaryotic C. elegans protein, and B (ER) because there is no N-terminal signal peptide or ER retention motif (KDEL/HDEL). Between C (plasma membrane) and D (microtubule cytoskeleton), the sequence lacks transmembrane domains, microtubule-binding motifs (e.g., MAP domains), or obvious plasma membrane targeting signals (myristoylation, palmitoylation, GPI anchor). The protein is a large (~784 aa) peripheral protein with coiled-coil regions that associates with the membrane indirectly through the dystrophin complex. Distinguishing C from D requires knowing that alpha-catulin is a component of the dystrophin-glycoprotein complex at the muscle membrane rather than a microtubule-associated protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific protein-protein interaction knowledge that alpha-catulin (CTN-1) is a scaffolding component of the dystrophin complex at the muscle cell plasma membrane (dense bodies), rather than being a cytoplasmic or microtubule-associated protein. The sequence itself contains no intrinsic plasma membrane targeting signal; localization depends on indirect association through protein interactions that cannot be inferred from the primary sequence alone.",
    "reason": "The protein lacks any obvious sequence feature (transmembrane helix, lipid modification site, signal peptide, microtubule-binding domain) that would allow confident assignment to plasma membrane over other cytoplasmic/cytoskeletal compartments. The plasma membrane localization is an emergent property of its role in a multi-protein complex (dystrophin-glycoprotein complex) at the muscle membrane, which is protein-specific knowledge not derivable from the sequence."
  },
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3",
      "C8",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The GO annotation GO:0005886 (plasma membrane) is assigned to this protein (Alpha-catulin, CTN-1, UniProt G8JYB2) with IDA:WormBase evidence from PubMed 22577143, indicating direct experimental evidence for plasma membrane localization. This is consistent with alpha-catulin's role in the dystrophin-glycoprotein complex at the muscle cell membrane (dense bodies). However, the UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' with note 'Localizes near dense bodies in muscle cells,' creating a partial annotation conflict. The GO-specific annotation with IDA evidence supports the expected answer, and since the question explicitly asks about GO Cellular Component, the plasma membrane GO term is the relevant annotation."
  },
  "important_caveats": [
    "The UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' while the GO cross-reference states 'plasma membrane' (IDA). These are not fully consistent, though dense bodies are plasma-membrane-associated structures, reconciling the two.",
    "The expected answer relies on the GO annotation (GO:0005886) rather than the UniProt CC field, which is appropriate given the question asks about GO Cellular Component.",
    "The protein has no transmembrane domain; its plasma membrane association is indirect via protein-protein interactions (dystrophin complex, BK channels).",
    "The identity of this protein as alpha-catulin/CTN-1 from C. elegans was determined by reviewer-only sequence matching; the evaluated model only sees the raw sequence.",
    "Evidence code IDA (Inferred from Direct Assay) indicates experimental localization, lending stronger support to the plasma membrane GO annotation than computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four given options, A (virus tail) and B (ER) are clearly eliminable. D (microtubule cytoskeleton) is unlikely for a catenin-family protein. While the UniProt SUBCELLULAR LOCATION says 'Cytoplasm,' this is not among the choices, so it does not create direct ambiguity within the provided options. Plasma membrane (C) is the most specific GO annotation with IDA evidence among the available choices. However, the 'Cytoplasm' vs. 'plasma membrane' annotation conflict in UniProt introduces some conceptual uncertainty about whether 'primary' location is cytoplasmic or membrane-associated, though this does not map to a different available option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO annotation GO:0005886 (plasma membrane) is assigned to this protein (Alpha-catulin, CTN-1, UniProt G8JYB2) with IDA:WormBase evidence from PubMed 22577143, indicating direct experimental evidence for plasma membrane localization. This is consistent with alpha-catulin's role in the dystrophin-glycoprotein complex at the muscle cell membrane (dense bodies). However, the UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' with note 'Localizes near dense bodies in muscle cells,' creating a partial annotation conflict. The GO-specific annotation with IDA evidence supports the expected answer, and since the question explicitly asks about GO Cellular Component, the plasma membrane GO term is the relevant annotation.",
    "evidence_ids": ["C6", "H4", "C5", "H3", "C8", "C10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can eliminate A (virus tail) because this is a eukaryotic C. elegans protein, and B (ER) because there is no N-terminal signal peptide or ER retention motif (KDEL/HDEL). Between C (plasma membrane) and D (microtubule cytoskeleton), the sequence lacks transmembrane domains, microtubule-binding motifs (e.g., MAP domains), or obvious plasma membrane targeting signals (myristoylation, palmitoylation, GPI anchor). The protein is a large (~784 aa) peripheral protein with coiled-coil regions that associates with the membrane indirectly through the dystrophin complex. Distinguishing C from D requires knowing that alpha-catulin is a component of the dystrophin-glycoprotein complex at the muscle membrane rather than a microtubule-associated protein.",
    "missing_item_specific_fact": "The specific protein-protein interaction knowledge that alpha-catulin (CTN-1) is a scaffolding component of the dystrophin complex at the muscle cell plasma membrane (dense bodies), rather than being a cytoplasmic or microtubule-associated protein. The sequence itself contains no intrinsic plasma membrane targeting signal; localization depends on indirect association through protein interactions that cannot be inferred from the primary sequence alone.",
    "reason": "The protein lacks any obvious sequence feature (transmembrane helix, lipid modification site, signal peptide, microtubule-binding domain) that would allow confident assignment to plasma membrane over other cytoplasmic/cytoskeletal compartments. The plasma membrane localization is an emergent property of its role in a multi-protein complex (dystrophin-glycoprotein complex) at the muscle membrane, which is protein-specific knowledge not derivable from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four given options, A (virus tail) and B (ER) are clearly eliminable. D (microtubule cytoskeleton) is unlikely for a catenin-family protein. While the UniProt SUBCELLULAR LOCATION says 'Cytoplasm,' this is not among the choices, so it does not create direct ambiguity within the provided options. Plasma membrane (C) is the most specific GO annotation with IDA evidence among the available choices. However, the 'Cytoplasm' vs. 'plasma membrane' annotation conflict in UniProt introduces some conceptual uncertainty about whether 'primary' location is cytoplasmic or membrane-associated, though this does not map to a different available option."
  },
  "important_caveats": [
    "The UniProt SUBCELLULAR LOCATION field states 'Cytoplasm' while the GO cross-reference states 'plasma membrane' (IDA). These are not fully consistent, though dense bodies are plasma-membrane-associated structures, reconciling the two.",
    "The expected answer relies on the GO annotation (GO:0005886) rather than the UniProt CC field, which is appropriate given the question asks about GO Cellular Component.",
    "The protein has no transmembrane domain; its plasma membrane association is indirect via protein-protein interactions (dystrophin complex, BK channels).",
    "The identity of this protein as alpha-catulin/CTN-1 from C. elegans was determined by reviewer-only sequence matching; the evaluated model only sees the raw sequence.",
    "Evidence code IDA (Inferred from Direct Assay) indicates experimental localization, lending stronger support to the plasma membrane GO annotation than computational prediction."
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

**Accession:** `G8JYB2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 84. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20865173","source":"PubMed"}],"value":"Localizes near dense bodies in muscle cells"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"20865173","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22577143","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IDA:WormBase"}]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Chen B.","Liu P.","Wang S.J.","Ge Q.","Zhan H.","Mohler W.A.","Wang Z.W."],"citationCrossReferences":[{"database":"PubMed","id":"20700105"},{"database":"DOI","id":"10.1038/emboj.2010.194"}],"citationType":"journal article","firstPage":"3184","id":"20700105","journal":"EMBO J.","lastPage":"3195","publicationDate":"2010","title":"alpha-Catulin CTN-1 is required for BK channel subcellular localization in C. elegans body-wall muscle cells.","volume":"29"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","INTERACTION WITH SLO-1","TISSUE SPECIFICITY","MUTAGENESIS OF 358-ARG--ILE-784"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:48.044451+00:00.  

```json
{"citation":{"authors":["Oh H.J.","Abraham L.S.","van Hengel J.","Stove C.","Proszynski T.J.","Gevaert K.","DiMario J.X.","Sanes J.R.","van Roy F.","Kim H."],"citationCrossReferences":[{"database":"PubMed","id":"22577143"},{"database":"DOI","id":"10.1074/jbc.m112.369496"}],"citationType":"journal article","firstPage":"21717","id":"22577143","journal":"J. Biol. Chem.","lastPage":"21728","publicationDate":"2012","title":"Interaction of alpha-catulin with dystrobrevin contributes to integrity of dystrophin complex in muscle.","volume":"287"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","INTERACTION WITH DYB-1","TISSUE SPECIFICITY","DOMAIN","MUTAGENESIS OF 382-ASN--ILE-416"]}
```

Source SHA-256: `ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:28:52.763286+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:20865173}.
CC       Note=Localizes near dense bodies in muscle cells.
CC       {ECO:0000269|PubMed:20865173}.
```

Source SHA-256: `bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)  
**Locator:** `lines 113-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 84 / 1.  
**Retrieved:** 2026-11-02T04:28:52.763286+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IDA:WormBase.
```

Source SHA-256: `bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
