# GO_cellular_component_0101

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — ATP-binding cassette (ABC) transporter complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTSPGTVESTTPVSGQLRTVLSAGERPARATAVSATLTHLWRAMMAFKHFPVQLIDIVLMPLIFLLMFTYLFGGAFADSTEEYLQFYLPGVTVQAVVMMTVYTGTSLNTDIHKGVFDRFRTLPFWQPATLAGSLLGDVLRYVVALATTVFLGLLLGFRADGGFLGVVGAMLVLIVFGFSVSWIFAALGVVASEPERVSGTSMIVLYPLLFMSNIFVMPETMPGWMQAIVDANPMSHAATASRELMHGTAGFWDVGLVLCVSAGLVAVFAPLTMRLYRNKNAH

[Multiple Choices]
A. cytoplasmic vesicle
B. host cell plasma membrane
C. ATP-binding cassette (ABC) transporter complex
D. histone acetyltransferase complex
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

> The exact sequence matches a UniProt entry annotated as a daunorubicin-resistance ABC transporter permease, with GO:0043190 (ABC transporter complex) assigned by IEA:InterPro. This supports C as an annotation, though the complex assignment is computational rather than direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support a multipass membrane protein, but do not establish that it belongs to an ABC transporter complex rather than another membrane-associated component.


**Missing item-specific fact**

> The protein-specific identification as the DrrB1 ABC-transporter permease and its association with the ABC transporter complex.


**Reason**

> Choosing C over the distractors depends on protein-specific identity or annotation absent from the prompt. Sequence-based membrane topology alone does not distinguish the exact complex annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported by the sequence-matched GO annotation. Although the protein is also annotated as a cell-membrane multipass protein, option B specifies a host cell plasma membrane, which does not fit this bacterial protein.


### Important caveats

- The ABC transporter complex annotation is IEA:InterPro, not direct experimental evidence for complex membership.
- The cell-membrane annotation is supported by transferred evidence and a topology prediction; the available excerpts do not establish direct experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein, but do not establish that it belongs to an ABC transporter complex rather than another membrane-associated component.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB1 ABC-transporter permease and its association with the ABC transporter complex.",
    "reason": "Choosing C over the distractors depends on protein-specific identity or annotation absent from the prompt. Sequence-based membrane topology alone does not distinguish the exact complex annotation."
  },
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a daunorubicin-resistance ABC transporter permease, with GO:0043190 (ABC transporter complex) assigned by IEA:InterPro. This supports C as an annotation, though the complex assignment is computational rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The ABC transporter complex annotation is IEA:InterPro, not direct experimental evidence for complex membership.",
    "The cell-membrane annotation is supported by transferred evidence and a topology prediction; the available excerpts do not establish direct experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the sequence-matched GO annotation. Although the protein is also annotated as a cell-membrane multipass protein, option B specifies a host cell plasma membrane, which does not fit this bacterial protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a daunorubicin-resistance ABC transporter permease, with GO:0043190 (ABC transporter complex) assigned by IEA:InterPro. This supports C as an annotation, though the complex assignment is computational rather than direct experimental localization evidence.",
    "evidence_ids": ["C1", "C4", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein, but do not establish that it belongs to an ABC transporter complex rather than another membrane-associated component.",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB1 ABC-transporter permease and its association with the ABC transporter complex.",
    "reason": "Choosing C over the distractors depends on protein-specific identity or annotation absent from the prompt. Sequence-based membrane topology alone does not distinguish the exact complex annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the sequence-matched GO annotation. Although the protein is also annotated as a cell-membrane multipass protein, option B specifies a host cell plasma membrane, which does not fit this bacterial protein."
  },
  "important_caveats": [
    "The ABC transporter complex annotation is IEA:InterPro, not direct experimental evidence for complex membership.",
    "The cell-membrane annotation is supported by transferred evidence and a topology prediction; the available excerpts do not establish direct experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU4 annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with IEA:InterPro evidence (C6/H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4/H1), and its function in daunorubicin efflux via ABC transport was experimentally confirmed (H2, PubMed:39375957). The subcellular location is 'Cell membrane; Multi-pass membrane protein' (C5/H3), consistent with an ABC permease subunit. While the GO:0043190 annotation itself is IEA (computational via InterPro), the protein's identity as an ABC transporter permease is corroborated by experimental function data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows multiple hydrophobic stretches (~6-8 potential TM helices) in a 283-residue protein from a bacterium, indicating a multi-pass membrane protein. Option B ('host cell plasma membrane', GO:0020002) is explicitly defined as 'The plasma membrane surrounding a host cell' and belongs to the goslim_virus subset (GO2), making it a term reserved for viral proteins interacting with host membranes—not applicable to a bacterial protein. Option D (histone acetyltransferase complex, GO:0000123) is a eukaryotic chromatin-associated complex (GO1), incompatible with a multi-TM bacterial membrane protein. Option A (cytoplasmic vesicle, GO:0031410) is a eukaryotic vesicular compartment (GO3), inconsistent with a multi-pass membrane protein. By elimination and positive support (multi-TM, ~283 AA, bacterial origin consistent with an ABC permease subunit), C is the most defensible answer.


**Missing item-specific fact**

> Specific ABC permease sequence motifs (e.g., EAA motif, conserved TM helix packing patterns) are not trivially identifiable by eye in the raw sequence, so positive identification as an ABC transporter (vs. other multi-TM membrane proteins like MFS transporters) relies partly on domain-level pattern recognition rather than a single unambiguous motif visible in the sequence.


**Reason**

> The elimination of options A, B, and D is achievable through general biological knowledge: B is a virus-specific term, D is a eukaryotic chromatin complex, and A is a eukaryotic vesicle—none compatible with a multi-TM bacterial membrane protein. The positive identification of C is supported by the multi-pass TM topology, appropriate subunit length (~283 AA), and bacterial context, though the specific assignment to ABC transporter over other multi-TM transporters benefits from recognizing ABC-permease domain architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B ('host cell plasma membrane') might superficially seem plausible for a membrane protein, but the GO term GO:0020002 is specifically defined for host cell membranes in the virus-infection context (goslim_virus subset), making it inapplicable to a bacterial protein. Options A and D are clearly eukaryotic-specific and incompatible with a multi-TM bacterial membrane protein. No other option is defensible.


### Important caveats

- The GO:0043190 annotation in UniProt is IEA:InterPro (computational inference from domain matching), not direct experimental subcellular localization evidence.
- The subcellular location annotation (Cell membrane) is transferred by similarity (ECO:0000250 from P32011, a related ABC permease), not directly measured for this specific protein.
- The experimental evidence (PubMed:39375957) confirms ABC transporter function in daunorubicin efflux but does not independently confirm the GO cellular component assignment to the complex.
- The protein is the permease (transmembrane) subunit only; the full ABC transporter complex includes nucleotide-binding domains encoded by separate genes (DrrA/DrrC in this system).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows multiple hydrophobic stretches (~6-8 potential TM helices) in a 283-residue protein from a bacterium, indicating a multi-pass membrane protein. Option B ('host cell plasma membrane', GO:0020002) is explicitly defined as 'The plasma membrane surrounding a host cell' and belongs to the goslim_virus subset (GO2), making it a term reserved for viral proteins interacting with host membranes—not applicable to a bacterial protein. Option D (histone acetyltransferase complex, GO:0000123) is a eukaryotic chromatin-associated complex (GO1), incompatible with a multi-TM bacterial membrane protein. Option A (cytoplasmic vesicle, GO:0031410) is a eukaryotic vesicular compartment (GO3), inconsistent with a multi-pass membrane protein. By elimination and positive support (multi-TM, ~283 AA, bacterial origin consistent with an ABC permease subunit), C is the most defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific ABC permease sequence motifs (e.g., EAA motif, conserved TM helix packing patterns) are not trivially identifiable by eye in the raw sequence, so positive identification as an ABC transporter (vs. other multi-TM membrane proteins like MFS transporters) relies partly on domain-level pattern recognition rather than a single unambiguous motif visible in the sequence.",
    "reason": "The elimination of options A, B, and D is achievable through general biological knowledge: B is a virus-specific term, D is a eukaryotic chromatin complex, and A is a eukaryotic vesicle—none compatible with a multi-TM bacterial membrane protein. The positive identification of C is supported by the multi-pass TM topology, appropriate subunit length (~283 AA), and bacterial context, though the specific assignment to ABC transporter over other multi-TM transporters benefits from recognizing ABC-permease domain architecture."
  },
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with IEA:InterPro evidence (C6/H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4/H1), and its function in daunorubicin efflux via ABC transport was experimentally confirmed (H2, PubMed:39375957). The subcellular location is 'Cell membrane; Multi-pass membrane protein' (C5/H3), consistent with an ABC permease subunit. While the GO:0043190 annotation itself is IEA (computational via InterPro), the protein's identity as an ABC transporter permease is corroborated by experimental function data."
  },
  "important_caveats": [
    "The GO:0043190 annotation in UniProt is IEA:InterPro (computational inference from domain matching), not direct experimental subcellular localization evidence.",
    "The subcellular location annotation (Cell membrane) is transferred by similarity (ECO:0000250 from P32011, a related ABC permease), not directly measured for this specific protein.",
    "The experimental evidence (PubMed:39375957) confirms ABC transporter function in daunorubicin efflux but does not independently confirm the GO cellular component assignment to the complex.",
    "The protein is the permease (transmembrane) subunit only; the full ABC transporter complex includes nucleotide-binding domains encoded by separate genes (DrrA/DrrC in this system)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B ('host cell plasma membrane') might superficially seem plausible for a membrane protein, but the GO term GO:0020002 is specifically defined for host cell membranes in the virus-infection context (goslim_virus subset), making it inapplicable to a bacterial protein. Options A and D are clearly eukaryotic-specific and incompatible with a multi-TM bacterial membrane protein. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU4 annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with IEA:InterPro evidence (C6/H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB1' (C4/H1), and its function in daunorubicin efflux via ABC transport was experimentally confirmed (H2, PubMed:39375957). The subcellular location is 'Cell membrane; Multi-pass membrane protein' (C5/H3), consistent with an ABC permease subunit. While the GO:0043190 annotation itself is IEA (computational via InterPro), the protein's identity as an ABC transporter permease is corroborated by experimental function data.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows multiple hydrophobic stretches (~6-8 potential TM helices) in a 283-residue protein from a bacterium, indicating a multi-pass membrane protein. Option B ('host cell plasma membrane', GO:0020002) is explicitly defined as 'The plasma membrane surrounding a host cell' and belongs to the goslim_virus subset (GO2), making it a term reserved for viral proteins interacting with host membranes—not applicable to a bacterial protein. Option D (histone acetyltransferase complex, GO:0000123) is a eukaryotic chromatin-associated complex (GO1), incompatible with a multi-TM bacterial membrane protein. Option A (cytoplasmic vesicle, GO:0031410) is a eukaryotic vesicular compartment (GO3), inconsistent with a multi-pass membrane protein. By elimination and positive support (multi-TM, ~283 AA, bacterial origin consistent with an ABC permease subunit), C is the most defensible answer.",
    "missing_item_specific_fact": "Specific ABC permease sequence motifs (e.g., EAA motif, conserved TM helix packing patterns) are not trivially identifiable by eye in the raw sequence, so positive identification as an ABC transporter (vs. other multi-TM membrane proteins like MFS transporters) relies partly on domain-level pattern recognition rather than a single unambiguous motif visible in the sequence.",
    "reason": "The elimination of options A, B, and D is achievable through general biological knowledge: B is a virus-specific term, D is a eukaryotic chromatin complex, and A is a eukaryotic vesicle—none compatible with a multi-TM bacterial membrane protein. The positive identification of C is supported by the multi-pass TM topology, appropriate subunit length (~283 AA), and bacterial context, though the specific assignment to ABC transporter over other multi-TM transporters benefits from recognizing ABC-permease domain architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B ('host cell plasma membrane') might superficially seem plausible for a membrane protein, but the GO term GO:0020002 is specifically defined for host cell membranes in the virus-infection context (goslim_virus subset), making it inapplicable to a bacterial protein. Options A and D are clearly eukaryotic-specific and incompatible with a multi-TM bacterial membrane protein. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0043190 annotation in UniProt is IEA:InterPro (computational inference from domain matching), not direct experimental subcellular localization evidence.",
    "The subcellular location annotation (Cell membrane) is transferred by similarity (ECO:0000250 from P32011, a related ABC permease), not directly measured for this specific protein.",
    "The experimental evidence (PubMed:39375957) confirms ABC transporter function in daunorubicin efflux but does not independently confirm the GO cellular component assignment to the complex.",
    "The protein is the permease (transmembrane) subunit only; the full ABC transporter complex includes nucleotide-binding domains encoded by separate genes (DrrA/DrrC in this system)."
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

**Accession:** `P0DXU4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
"P0DXU4"
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ABC transporter permease protein DrrB1"}}}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32011","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU4.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:38.291851+00:00.  

```json
{"database":"GO","id":"GO:0043190","properties":[{"key":"GoTerm","value":"C:ATP-binding cassette (ABC) transporter complex"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `0485d691ed0d1c230bd6d0cc546400f66c74af103adcbfae303adf9cef833386`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
ID   DRRB1_STRC4             Reviewed;         283 AA.
AC   P0DXU4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB1 {ECO:0000305};
GN   Name=drrB1 {ECO:0000303|PubMed:39375957};
GN   Synonyms=drrB {ECO:0000312|EMBL:WOT33551.1};
GN   ORFNames=R5U08_05030 {ECO:0000312|EMBL:WOT33551.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 19-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
RN   [2]
RP   FUNCTION IN DAUNORUBICIN EFFLUX, AND DISRUPTION PHENOTYPE.
RX   PubMed=39375957; DOI=10.1111/1751-7915.70023;
RA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;
RT   "The involvement of multiple ABC transporters in daunorubicin efflux in
RT   Streptomyces coeruleorubidus.";
RL   Microb. Biotechnol. 17:e70023-e70023(2024).
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 34-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32011};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU4?format=txt&versions=4)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:40.349229+00:00.  

```text
DR   GO; GO:0043190; C:ATP-binding cassette (ABC) transporter complex; IEA:InterPro.
```

Source SHA-256: `d750c27539bcb0df22e75395c132bc01e7f57cee37b61c3a5ea940e8c526a55f`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 1242-1251`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000123
name: histone acetyltransferase complex
namespace: cellular_component
def: "A protein complex that possesses histone acetyltransferase activity." [GOC:mah]
comment: Note that this term represents a protein complex, not a function; the activity possessed by this complex is mentioned in the definition for the purpose of describing and distinguishing the complex. The function of this complex is represented by the molecular function term 'histone acetyltransferase activity ; GO:0004402'.
synonym: "histone acetylase complex" EXACT []
is_a: GO:0031248 ! protein acetyltransferase complex
relationship: part_of GO:0000785 ! chromatin

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 155120-155127`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0020002
name: host cell plasma membrane
namespace: cellular_component
def: "The plasma membrane surrounding a host cell." [GOC:mb]
subset: goslim_virus
is_a: GO:0033644 ! host cell membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 176239-176257`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031410
name: cytoplasmic vesicle
namespace: cellular_component
alt_id: GO:0016023
def: "A vesicle found in the cytoplasm of a cell." [GOC:ai, GOC:mah, GOC:vesicles]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_generic
subset: goslim_mouse
subset: goslim_yeast
synonym: "cytoplasmic membrane bounded vesicle" RELATED []
synonym: "cytoplasmic membrane-enclosed vesicle" RELATED []
synonym: "cytoplasmic, membrane-bounded vesicle" RELATED []
xref: NIF_Subcellular:sao180601769
is_a: GO:0097708 ! intracellular vesicle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
