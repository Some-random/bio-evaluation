# GO_cellular_component_0014

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — side of membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM

[Multiple Choices]
A. protein-DNA complex
B. side of membrane
C. peroxisomal membrane
D. Dbf4-dependent protein kinase complex
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

> The exact-sequence-matched historical UniProt record annotates side of membrane (IEA:UniProtKB-KW) and describes the protein as membrane-associated with a lipid/GPI anchor. This supports choice B, though the record also reports other locations.

Citations as saved: [H3](#evidence-h3), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, while the C-terminal hydrophobic tail is consistent with a GPI-anchor signal. That combination supports membrane anchoring and distinguishes B from the protein-DNA and kinase-complex options and the peroxisomal-membrane option.


**Missing item-specific fact**

> No protein-specific annotation is strictly needed to make this distinction from the sequence, although confirming the precise localization and anchor experimentally would require additional evidence.


**Reason**

> The sequence contains plausible secretory-pathway and GPI-anchor signals, providing a concrete biological basis for predicting a membrane-associated protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the sequence features support membrane association; the other choices are not comparably supported.


### Important caveats

- The reviewer-only annotation records vacuolar and endoplasmic-reticulum localization under saprophytic conditions, and secretion and host-cytoplasm observations during pathogenic development; localization is therefore context-dependent.
- The side-of-membrane GO annotation is computationally assigned, while the cited localization observations are reported as experimental. The question's use of “primary” does not specify a condition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, while the C-terminal hydrophobic tail is consistent with a GPI-anchor signal. That combination supports membrane anchoring and distinguishes B from the protein-DNA and kinase-complex options and the peroxisomal-membrane option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is strictly needed to make this distinction from the sequence, although confirming the precise localization and anchor experimentally would require additional evidence.",
    "reason": "The sequence contains plausible secretory-pathway and GPI-anchor signals, providing a concrete biological basis for predicting a membrane-associated protein."
  },
  "case_id": "GO_cellular_component_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched historical UniProt record annotates side of membrane (IEA:UniProtKB-KW) and describes the protein as membrane-associated with a lipid/GPI anchor. This supports choice B, though the record also reports other locations."
  },
  "important_caveats": [
    "The reviewer-only annotation records vacuolar and endoplasmic-reticulum localization under saprophytic conditions, and secretion and host-cytoplasm observations during pathogenic development; localization is therefore context-dependent.",
    "The side-of-membrane GO annotation is computationally assigned, while the cited localization observations are reported as experimental. The question's use of “primary” does not specify a condition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence features support membrane association; the other choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched historical UniProt record annotates side of membrane (IEA:UniProtKB-KW) and describes the protein as membrane-associated with a lipid/GPI anchor. This supports choice B, though the record also reports other locations.",
    "evidence_ids": ["H3", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, while the C-terminal hydrophobic tail is consistent with a GPI-anchor signal. That combination supports membrane anchoring and distinguishes B from the protein-DNA and kinase-complex options and the peroxisomal-membrane option.",
    "missing_item_specific_fact": "No protein-specific annotation is strictly needed to make this distinction from the sequence, although confirming the precise localization and anchor experimentally would require additional evidence.",
    "reason": "The sequence contains plausible secretory-pathway and GPI-anchor signals, providing a concrete biological basis for predicting a membrane-associated protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence features support membrane association; the other choices are not comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation records vacuolar and endoplasmic-reticulum localization under saprophytic conditions, and secretion and host-cytoplasm observations during pathogenic development; localization is therefore context-dependent.",
    "The side-of-membrane GO annotation is computationally assigned, while the cited localization observations are reported as experimental. The question's use of “primary” does not specify a condition."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry (A0A384J6C4) annotates GO:0098552 'side of membrane' (H8, evidence: IEA:UniProtKB-KW). The underlying basis is the GPI-anchor topology annotation (ECO:0000255, inferred by sequence analysis) in the SUBCELLULAR LOCATION comment (C5/H3), which states 'Membrane; Lipid-anchor, GPI-anchor.' GO:0098552 is defined as 'one leaflet of a membrane bilayer and any protein embedded or anchored in it' (GO4), which matches a GPI-anchored protein. However, the evidence for this specific GO term is computational (IEA from keyword), not experimental; the experimental evidence (PubMed:33846308) supports vacuole, ER, and secretion locations. The answer is supported by the database annotation but rests on a sequence-based GPI-anchor prediction rather than direct experimental localization to a membrane surface.

Citations as saved: [H8](#evidence-h8), [C5](#evidence-c5), [H3](#evidence-h3), [GO4](#evidence-go4), [C10](#evidence-c10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MRSSTISASAVVLLSGLASAQ...) indicating secretory-pathway entry, and a C-terminal hydrophobic GPI-anchor attachment signal (…VTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM) with a characteristic ω-site and hydrophobic tail. GPI-anchored proteins are tethered to the outer leaflet of a membrane bilayer, which corresponds to GO:0098552 'side of membrane.' Peroxisomal membrane proteins use PTS1/PTS2 targeting signals, which are absent here, and GPI-anchoring is mechanistically incompatible with peroxisomal import. Options A (protein-DNA complex) and D (Dbf4-dependent kinase complex) are incompatible with a secreted chitinase/transglycosylase. Thus, identifying the signal peptide, recognizing the GPI-anchor C-terminal motif, and applying general knowledge that GPI-anchored proteins reside on one membrane leaflet provides a defensible reasoning chain to select B.


**Missing item-specific fact**

> None strictly required. The GPI-anchor signal is a general sequence feature, and the GO mapping of GPI-anchored proteins to 'side of membrane' is standard ontology knowledge. However, precise recognition of the GPI-anchor ω-site from a 391-aa sequence without a dedicated predictor adds difficulty.


**Reason**

> A model with knowledge of signal peptides, GPI-anchor C-terminal signals, GO ontology structure, and peroxisomal targeting mechanisms can reason from the sequence to 'side of membrane' while eliminating the other three options. The reasoning does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are clearly incompatible with a secreted fungal chitinase. Option C (peroxisomal membrane) is excluded by the absence of peroxisomal targeting signals and the presence of a GPI-anchor signal incompatible with peroxisomal import. The experimental evidence also supports ER/vacuole/secreted locations, none of which appear as options, leaving B as the only membrane-related option consistent with the GPI-anchor annotation.


### Important caveats

- The GO:0098552 'side of membrane' annotation is IEA:UniProtKB-KW (keyword-derived), not experimentally determined for this specific GO term.
- The GPI-anchor topology itself is annotated with ECO:0000255 (inferred by sequence analysis), not experimentally confirmed for this protein.
- Experimental evidence (PubMed:33846308) primarily supports vacuolar, ER, and secreted/apoplasmic localization; 'side of membrane' is a computational inference from the GPI-anchor keyword.
- The question asks for 'primary Cellular Component,' but the protein has multiple experimentally supported locations (vacuole, ER, secreted, host cytoplasm), making 'primary' somewhat ambiguous.
- The author source snapshot is unknown; the historical entry (version 30, released 2026-01-28) already contains the GO:0098552 annotation, so timing is unlikely to be an issue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MRSSTISASAVVLLSGLASAQ...) indicating secretory-pathway entry, and a C-terminal hydrophobic GPI-anchor attachment signal (…VTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM) with a characteristic ω-site and hydrophobic tail. GPI-anchored proteins are tethered to the outer leaflet of a membrane bilayer, which corresponds to GO:0098552 'side of membrane.' Peroxisomal membrane proteins use PTS1/PTS2 targeting signals, which are absent here, and GPI-anchoring is mechanistically incompatible with peroxisomal import. Options A (protein-DNA complex) and D (Dbf4-dependent kinase complex) are incompatible with a secreted chitinase/transglycosylase. Thus, identifying the signal peptide, recognizing the GPI-anchor C-terminal motif, and applying general knowledge that GPI-anchored proteins reside on one membrane leaflet provides a defensible reasoning chain to select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The GPI-anchor signal is a general sequence feature, and the GO mapping of GPI-anchored proteins to 'side of membrane' is standard ontology knowledge. However, precise recognition of the GPI-anchor ω-site from a 391-aa sequence without a dedicated predictor adds difficulty.",
    "reason": "A model with knowledge of signal peptides, GPI-anchor C-terminal signals, GO ontology structure, and peroxisomal targeting mechanisms can reason from the sequence to 'side of membrane' while eliminating the other three options. The reasoning does not require memorizing this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "H8",
      "C5",
      "H3",
      "GO4",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry (A0A384J6C4) annotates GO:0098552 'side of membrane' (H8, evidence: IEA:UniProtKB-KW). The underlying basis is the GPI-anchor topology annotation (ECO:0000255, inferred by sequence analysis) in the SUBCELLULAR LOCATION comment (C5/H3), which states 'Membrane; Lipid-anchor, GPI-anchor.' GO:0098552 is defined as 'one leaflet of a membrane bilayer and any protein embedded or anchored in it' (GO4), which matches a GPI-anchored protein. However, the evidence for this specific GO term is computational (IEA from keyword), not experimental; the experimental evidence (PubMed:33846308) supports vacuole, ER, and secretion locations. The answer is supported by the database annotation but rests on a sequence-based GPI-anchor prediction rather than direct experimental localization to a membrane surface."
  },
  "important_caveats": [
    "The GO:0098552 'side of membrane' annotation is IEA:UniProtKB-KW (keyword-derived), not experimentally determined for this specific GO term.",
    "The GPI-anchor topology itself is annotated with ECO:0000255 (inferred by sequence analysis), not experimentally confirmed for this protein.",
    "Experimental evidence (PubMed:33846308) primarily supports vacuolar, ER, and secreted/apoplasmic localization; 'side of membrane' is a computational inference from the GPI-anchor keyword.",
    "The question asks for 'primary Cellular Component,' but the protein has multiple experimentally supported locations (vacuole, ER, secreted, host cytoplasm), making 'primary' somewhat ambiguous.",
    "The author source snapshot is unknown; the historical entry (version 30, released 2026-01-28) already contains the GO:0098552 annotation, so timing is unlikely to be an issue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly incompatible with a secreted fungal chitinase. Option C (peroxisomal membrane) is excluded by the absence of peroxisomal targeting signals and the presence of a GPI-anchor signal incompatible with peroxisomal import. The experimental evidence also supports ER/vacuole/secreted locations, none of which appear as options, leaving B as the only membrane-related option consistent with the GPI-anchor annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry (A0A384J6C4) annotates GO:0098552 'side of membrane' (H8, evidence: IEA:UniProtKB-KW). The underlying basis is the GPI-anchor topology annotation (ECO:0000255, inferred by sequence analysis) in the SUBCELLULAR LOCATION comment (C5/H3), which states 'Membrane; Lipid-anchor, GPI-anchor.' GO:0098552 is defined as 'one leaflet of a membrane bilayer and any protein embedded or anchored in it' (GO4), which matches a GPI-anchored protein. However, the evidence for this specific GO term is computational (IEA from keyword), not experimental; the experimental evidence (PubMed:33846308) supports vacuole, ER, and secretion locations. The answer is supported by the database annotation but rests on a sequence-based GPI-anchor prediction rather than direct experimental localization to a membrane surface.",
    "evidence_ids": ["H8", "C5", "H3", "GO4", "C10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MRSSTISASAVVLLSGLASAQ...) indicating secretory-pathway entry, and a C-terminal hydrophobic GPI-anchor attachment signal (…VTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM) with a characteristic ω-site and hydrophobic tail. GPI-anchored proteins are tethered to the outer leaflet of a membrane bilayer, which corresponds to GO:0098552 'side of membrane.' Peroxisomal membrane proteins use PTS1/PTS2 targeting signals, which are absent here, and GPI-anchoring is mechanistically incompatible with peroxisomal import. Options A (protein-DNA complex) and D (Dbf4-dependent kinase complex) are incompatible with a secreted chitinase/transglycosylase. Thus, identifying the signal peptide, recognizing the GPI-anchor C-terminal motif, and applying general knowledge that GPI-anchored proteins reside on one membrane leaflet provides a defensible reasoning chain to select B.",
    "missing_item_specific_fact": "None strictly required. The GPI-anchor signal is a general sequence feature, and the GO mapping of GPI-anchored proteins to 'side of membrane' is standard ontology knowledge. However, precise recognition of the GPI-anchor ω-site from a 391-aa sequence without a dedicated predictor adds difficulty.",
    "reason": "A model with knowledge of signal peptides, GPI-anchor C-terminal signals, GO ontology structure, and peroxisomal targeting mechanisms can reason from the sequence to 'side of membrane' while eliminating the other three options. The reasoning does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly incompatible with a secreted fungal chitinase. Option C (peroxisomal membrane) is excluded by the absence of peroxisomal targeting signals and the presence of a GPI-anchor signal incompatible with peroxisomal import. The experimental evidence also supports ER/vacuole/secreted locations, none of which appear as options, leaving B as the only membrane-related option consistent with the GPI-anchor annotation."
  },
  "important_caveats": [
    "The GO:0098552 'side of membrane' annotation is IEA:UniProtKB-KW (keyword-derived), not experimentally determined for this specific GO term.",
    "The GPI-anchor topology itself is annotated with ECO:0000255 (inferred by sequence analysis), not experimentally confirmed for this protein.",
    "Experimental evidence (PubMed:33846308) primarily supports vacuolar, ER, and secreted/apoplasmic localization; 'side of membrane' is a computational inference from the GPI-anchor keyword.",
    "The question asks for 'primary Cellular Component,' but the protein has multiple experimentally supported locations (vacuole, ER, secreted, host cytoplasm), making 'primary' somewhat ambiguous.",
    "The author source snapshot is unknown; the historical entry (version 30, released 2026-01-28) already contains the GO:0098552 annotation, so timing is unlikely to be an issue."
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

**Accession:** `A0A384J6C4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:56.188291+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"value":"Under saprophytic conditions, is localized inside vacuoles and the endoplasmic reticulum (PubMed:33846308). During pathogenic development, high levels of the protein are observed in developing infection cushions, before being secreted to the plant apoplasm (PubMed:33846308)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"id":"SL-0272","value":"Vacuole"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"id":"SL-0095","value":"Endoplasmic reticulum"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33846308","source":"PubMed"}],"id":"SL-0381","value":"Host cytoplasm"}}]}
```

Source SHA-256: `1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:56.188291+00:00.  

```json
{"database":"GO","id":"GO:0016020","properties":[{"key":"GoTerm","value":"C:membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)  
**Locator:** `lines 86-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:58.365606+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Lipid-anchor, GPI-anchor
CC       {ECO:0000255}. Vacuole {ECO:0000269|PubMed:33846308}. Endoplasmic
CC       reticulum {ECO:0000269|PubMed:33846308}. Secreted
CC       {ECO:0000269|PubMed:33846308}. Host cytoplasm
CC       {ECO:0000269|PubMed:33846308}. Note=Under saprophytic conditions, is
CC       localized inside vacuoles and the endoplasmic reticulum
CC       (PubMed:33846308). During pathogenic development, high levels of the
CC       protein are observed in developing infection cushions, before being
CC       secreted to the plant apoplasm (PubMed:33846308).
CC       {ECO:0000269|PubMed:33846308}.
```

Source SHA-256: `47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)  
**Locator:** `lines 124-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:58.365606+00:00.  

```text
DR   GO; GO:0098552; C:side of membrane; IEA:UniProtKB-KW.
```

Source SHA-256: `47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 408943-408950`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098552
name: side of membrane
namespace: cellular_component
def: "A cellular component consisting of one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface." [GOC:dos]
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0016020 ! membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
