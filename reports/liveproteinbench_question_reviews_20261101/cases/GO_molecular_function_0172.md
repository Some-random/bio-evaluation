# GO_molecular_function_0172

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — peptidase inhibitor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTYVLQALLLTLAVAVVRAANTGIEWPPKPQKCAEGETWKECVGSSCAELTCEHPEPSLGCTYDCNYGCYCAPDFFRNANKECVKKDKCP

[Multiple Choices]
A. heparan sulfate 2-sulfotransferase activity
B. guanyl-nucleotide exchange factor activity
C. peptidase inhibitor activity
D. protein lysine deacetylase activity
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

> The sequence matches the Ixodes scapularis protein identified as ixochymostatin. Its annotated and experimentally evidenced function is inhibition of chymotrypsin-like proteases, supporting peptidase inhibitor activity (option C).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich mature region, consistent with a secreted disulfide-stabilized peptide inhibitor. The options for sulfotransferase, nucleotide exchange factor, and lysine deacetylase are catalytic or regulatory activities not suggested by this compact sequence.


**Missing item-specific fact**

> No protein-specific annotation is necessary for a defensible sequence-based choice, though identifying its exact inhibitor target would require additional information.


**Reason**

> The sequence features meaningfully favor a secreted peptidase inhibitor over the other listed functions; this is a biological inference, not reliance on remembering the database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these choices, the signal-peptide and cysteine-rich small-protein pattern most strongly supports peptidase inhibitor activity.


### Important caveats

- Reviewer-only evidence confirms the specific protein identity and function but was not available to the evaluated model.
- Sequence features support the choice but do not alone establish the protein's precise protease targets.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich mature region, consistent with a secreted disulfide-stabilized peptide inhibitor. The options for sulfotransferase, nucleotide exchange factor, and lysine deacetylase are catalytic or regulatory activities not suggested by this compact sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is necessary for a defensible sequence-based choice, though identifying its exact inhibitor target would require additional information.",
    "reason": "The sequence features meaningfully favor a secreted peptidase inhibitor over the other listed functions; this is a biological inference, not reliance on remembering the database entry."
  },
  "case_id": "GO_molecular_function_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Ixodes scapularis protein identified as ixochymostatin. Its annotated and experimentally evidenced function is inhibition of chymotrypsin-like proteases, supporting peptidase inhibitor activity (option C)."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the specific protein identity and function but was not available to the evaluated model.",
    "Sequence features support the choice but do not alone establish the protein's precise protease targets."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, the signal-peptide and cysteine-rich small-protein pattern most strongly supports peptidase inhibitor activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Ixodes scapularis protein identified as ixochymostatin. Its annotated and experimentally evidenced function is inhibition of chymotrypsin-like proteases, supporting peptidase inhibitor activity (option C).",
    "evidence_ids": ["C1", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich mature region, consistent with a secreted disulfide-stabilized peptide inhibitor. The options for sulfotransferase, nucleotide exchange factor, and lysine deacetylase are catalytic or regulatory activities not suggested by this compact sequence.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary for a defensible sequence-based choice, though identifying its exact inhibitor target would require additional information.",
    "reason": "The sequence features meaningfully favor a secreted peptidase inhibitor over the other listed functions; this is a biological inference, not reliance on remembering the database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these choices, the signal-peptide and cysteine-rich small-protein pattern most strongly supports peptidase inhibitor activity."
  },
  "important_caveats": [
    "Reviewer-only evidence confirms the specific protein identity and function but was not available to the evaluated model.",
    "Sequence features support the choice but do not alone establish the protein's precise protease targets."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (B7PCV3, Ixochymostatin from Ixodes scapularis) is experimentally characterized as a 'tight-binding competitive inhibitor of chymotrypsin-like proteases; inhibits host chymase, cathepsin G and chymotrypsin' (PubMed:39579814, ECO:0000269). The UniProt GO annotation is GO:0004867 (serine-type endopeptidase inhibitor activity), which is_a GO:0004866 (endopeptidase inhibitor activity) is_a GO:0030414 (peptidase inhibitor activity). The expected answer C is therefore directly supported by both experimental functional data and the ontology hierarchy.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4), [GO5](#evidence-go5), [GO3](#evidence-go3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 91 residues long, contains a signal peptide (N-terminal hydrophobic stretch MKTYVLQALLLTLAVAVVRA), and has ~10 cysteines forming a dense cysteine-rich pattern. Heparan sulfate 2-sulfotransferases (typically 300–500+ residues with a sulfotransferase catalytic domain), guanyl-nucleotide exchange factors (typically 500–1000+ residues with SEC7/PH/C2 domains), and protein lysine deacetylases (HDACs, typically 300–1000+ residues with a specific deacetylase catalytic domain) are all large multidomain enzymes whose architecture is fundamentally incompatible with a 91-residue secreted protein. In contrast, small secreted cysteine-rich proteins with multiple disulfide bonds are a well-known class of protease inhibitors (Kunitz-type, TIL-type, etc.). Among the four options, only peptidase inhibitor activity is structurally and size-compatible with the given sequence.


**Missing item-specific fact**

> None critical. While exact domain identification (TIL domain) would strengthen the assignment, the size-based elimination of the three large-enzyme options and the cysteine-rich secreted-protein heuristic are sufficient general biological reasoning to select C.


**Reason**

> A model with general knowledge of protein size constraints (sulfotransferases, GEFs, and HDACs are large enzymes) and the well-established association of small cysteine-rich secreted proteins with protease-inhibitor function can meaningfully distinguish C from A, B, and D without needing to recognize this specific protein or its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractor options (A, B, D) describe catalytic activities of large multidomain enzymes that are structurally incompatible with a 91-residue cysteine-rich secreted protein. Option C is the only biologically plausible choice given the sequence characteristics.


### Important caveats

- The UniProt entry B7PCV3 was first public in June 2025; the experimental characterization (PubMed:39579814) was published in 2025, making this a relatively recent annotation.
- The GO annotation GO:0004867 is tagged IEA:UniProtKB-KW (inferred from keyword), but the underlying functional data is experimental (ECO:0000269, PubMed:39579814).
- The expected answer uses the parent term GO:0030414 (peptidase inhibitor activity) rather than the more specific GO:0004867 (serine-type endopeptidase inhibitor activity); this is ontologically valid since the specific term is_a the parent.
- The cysteine-rich secreted-protein heuristic strongly favors protease inhibitor but is not absolutely exclusive; however, combined with the size-based elimination of the other three options, C is the uniquely defensible answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 91 residues long, contains a signal peptide (N-terminal hydrophobic stretch MKTYVLQALLLTLAVAVVRA), and has ~10 cysteines forming a dense cysteine-rich pattern. Heparan sulfate 2-sulfotransferases (typically 300–500+ residues with a sulfotransferase catalytic domain), guanyl-nucleotide exchange factors (typically 500–1000+ residues with SEC7/PH/C2 domains), and protein lysine deacetylases (HDACs, typically 300–1000+ residues with a specific deacetylase catalytic domain) are all large multidomain enzymes whose architecture is fundamentally incompatible with a 91-residue secreted protein. In contrast, small secreted cysteine-rich proteins with multiple disulfide bonds are a well-known class of protease inhibitors (Kunitz-type, TIL-type, etc.). Among the four options, only peptidase inhibitor activity is structurally and size-compatible with the given sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While exact domain identification (TIL domain) would strengthen the assignment, the size-based elimination of the three large-enzyme options and the cysteine-rich secreted-protein heuristic are sufficient general biological reasoning to select C.",
    "reason": "A model with general knowledge of protein size constraints (sulfotransferases, GEFs, and HDACs are large enzymes) and the well-established association of small cysteine-rich secreted proteins with protease-inhibitor function can meaningfully distinguish C from A, B, and D without needing to recognize this specific protein or its database entry."
  },
  "case_id": "GO_molecular_function_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4",
      "GO5",
      "GO3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (B7PCV3, Ixochymostatin from Ixodes scapularis) is experimentally characterized as a 'tight-binding competitive inhibitor of chymotrypsin-like proteases; inhibits host chymase, cathepsin G and chymotrypsin' (PubMed:39579814, ECO:0000269). The UniProt GO annotation is GO:0004867 (serine-type endopeptidase inhibitor activity), which is_a GO:0004866 (endopeptidase inhibitor activity) is_a GO:0030414 (peptidase inhibitor activity). The expected answer C is therefore directly supported by both experimental functional data and the ontology hierarchy."
  },
  "important_caveats": [
    "The UniProt entry B7PCV3 was first public in June 2025; the experimental characterization (PubMed:39579814) was published in 2025, making this a relatively recent annotation.",
    "The GO annotation GO:0004867 is tagged IEA:UniProtKB-KW (inferred from keyword), but the underlying functional data is experimental (ECO:0000269, PubMed:39579814).",
    "The expected answer uses the parent term GO:0030414 (peptidase inhibitor activity) rather than the more specific GO:0004867 (serine-type endopeptidase inhibitor activity); this is ontologically valid since the specific term is_a the parent.",
    "The cysteine-rich secreted-protein heuristic strongly favors protease inhibitor but is not absolutely exclusive; however, combined with the size-based elimination of the other three options, C is the uniquely defensible answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractor options (A, B, D) describe catalytic activities of large multidomain enzymes that are structurally incompatible with a 91-residue cysteine-rich secreted protein. Option C is the only biologically plausible choice given the sequence characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (B7PCV3, Ixochymostatin from Ixodes scapularis) is experimentally characterized as a 'tight-binding competitive inhibitor of chymotrypsin-like proteases; inhibits host chymase, cathepsin G and chymotrypsin' (PubMed:39579814, ECO:0000269). The UniProt GO annotation is GO:0004867 (serine-type endopeptidase inhibitor activity), which is_a GO:0004866 (endopeptidase inhibitor activity) is_a GO:0030414 (peptidase inhibitor activity). The expected answer C is therefore directly supported by both experimental functional data and the ontology hierarchy.",
    "evidence_ids": ["C5", "H3", "H4", "GO5", "GO3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 91 residues long, contains a signal peptide (N-terminal hydrophobic stretch MKTYVLQALLLTLAVAVVRA), and has ~10 cysteines forming a dense cysteine-rich pattern. Heparan sulfate 2-sulfotransferases (typically 300–500+ residues with a sulfotransferase catalytic domain), guanyl-nucleotide exchange factors (typically 500–1000+ residues with SEC7/PH/C2 domains), and protein lysine deacetylases (HDACs, typically 300–1000+ residues with a specific deacetylase catalytic domain) are all large multidomain enzymes whose architecture is fundamentally incompatible with a 91-residue secreted protein. In contrast, small secreted cysteine-rich proteins with multiple disulfide bonds are a well-known class of protease inhibitors (Kunitz-type, TIL-type, etc.). Among the four options, only peptidase inhibitor activity is structurally and size-compatible with the given sequence.",
    "missing_item_specific_fact": "None critical. While exact domain identification (TIL domain) would strengthen the assignment, the size-based elimination of the three large-enzyme options and the cysteine-rich secreted-protein heuristic are sufficient general biological reasoning to select C.",
    "reason": "A model with general knowledge of protein size constraints (sulfotransferases, GEFs, and HDACs are large enzymes) and the well-established association of small cysteine-rich secreted proteins with protease-inhibitor function can meaningfully distinguish C from A, B, and D without needing to recognize this specific protein or its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractor options (A, B, D) describe catalytic activities of large multidomain enzymes that are structurally incompatible with a 91-residue cysteine-rich secreted protein. Option C is the only biologically plausible choice given the sequence characteristics."
  },
  "important_caveats": [
    "The UniProt entry B7PCV3 was first public in June 2025; the experimental characterization (PubMed:39579814) was published in 2025, making this a relatively recent annotation.",
    "The GO annotation GO:0004867 is tagged IEA:UniProtKB-KW (inferred from keyword), but the underlying functional data is experimental (ECO:0000269, PubMed:39579814).",
    "The expected answer uses the parent term GO:0030414 (peptidase inhibitor activity) rather than the more specific GO:0004867 (serine-type endopeptidase inhibitor activity); this is ontologically valid since the specific term is_a the parent.",
    "The cysteine-rich secreted-protein heuristic strongly favors protease inhibitor but is not absolutely exclusive; however, combined with the size-based elimination of the other three options, C is the uniquely defensible answer."
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

**Accession:** `B7PCV3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 71. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7PCV3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.659456+00:00.  

```json
"B7PCV3"
```

Source SHA-256: `795a5bdcea28a11ebc582cb83993d36dff74a489e0824a2b76a884d8104b3f60`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7PCV3.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.659456+00:00.  

```json
{"entryVersion":73,"firstPublicDate":"2025-06-18","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2009-02-10","sequenceVersion":1}
```

Source SHA-256: `795a5bdcea28a11ebc582cb83993d36dff74a489e0824a2b76a884d8104b3f60`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7PCV3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.659456+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39579814","source":"PubMed"}],"value":"Tight-binding competitive inhibitor of chymotrypsin-like proteases; inhibits host chymase, cathepsin G (CTSG) and chymotrypsin (PubMed:39579814). Inhibits chymase-mediated generation of vasoconstrictor peptides: angiotensin II and endothelin I (PubMed:39579814). Reduces chymase-mediated vascular permeability and vascular endothelial-cadherin degradation (PubMed:39579814)"}]}
```

Source SHA-256: `795a5bdcea28a11ebc582cb83993d36dff74a489e0824a2b76a884d8104b3f60`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7PCV3?format=txt&versions=71)  
**Locator:** `lines 33-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 71 / 1.  
**Retrieved:** 2026-11-02T04:27:24.936082+00:00.  

```text
CC   -!- FUNCTION: Tight-binding competitive inhibitor of chymotrypsin-like
CC       proteases; inhibits host chymase, cathepsin G (CTSG) and chymotrypsin
CC       (PubMed:39579814). Inhibits chymase-mediated generation of
CC       vasoconstrictor peptides: angiotensin II and endothelin I
CC       (PubMed:39579814). Reduces chymase-mediated vascular permeability and
CC       vascular endothelial-cadherin degradation (PubMed:39579814).
CC       {ECO:0000269|PubMed:39579814}.
```

Source SHA-256: `3e0406e62036a160c723e24051a4bc018515287ff3469b7e4bb1bb5302d12b34`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7PCV3?format=txt&versions=71)  
**Locator:** `lines 68-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 71 / 1.  
**Retrieved:** 2026-11-02T04:27:24.936082+00:00.  

```text
DR   GO; GO:0004867; F:serine-type endopeptidase inhibitor activity; IEA:UniProtKB-KW.
```

Source SHA-256: `3e0406e62036a160c723e24051a4bc018515287ff3469b7e4bb1bb5302d12b34`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 51565-51575`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004866
name: endopeptidase inhibitor activity
namespace: molecular_function
def: "Binds to and stops, prevents or reduces the activity of an endopeptidase." [GOC:jl]
synonym: "alpha-2 macroglobulin" RELATED []
synonym: "endoproteinase inhibitor" NARROW []
synonym: "proteinase inhibitor" NARROW []
is_a: GO:0030414 ! peptidase inhibitor activity
is_a: GO:0061135 ! endopeptidase regulator activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 51576-51590`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004867
name: serine-type endopeptidase inhibitor activity
namespace: molecular_function
def: "Binds to and stops, prevents or reduces the activity of a serine-type endopeptidase." [GOC:ai]
synonym: "serine protease inhibitor activity" NARROW []
synonym: "serine proteinase inhibitor activity" NARROW []
synonym: "serpin activity" NARROW []
xref: Reactome:R-HSA-158795 "fibrin multimer, crosslinked:tissue plasminogen activator (one-chain) + plasminogen activator inhibitor 1 -> fibrin multimer, crosslinked:tissue plasminogen activator (one-chain):plasminogen activator inhibitor 1"
xref: Reactome:R-HSA-158800 "fibrin multimer, crosslinked:tissue plasminogen activator (two-chain) + plasminogen activator inhibitor 1 -> fibrin multimer, crosslinked:tissue plasminogen activator (two-chain):plasminogen activator inhibitor 1"
xref: Reactome:R-HSA-158893 "alpha-2-antiplasmin + plasmin -> alpha-2-antiplasmin:plasmin"
xref: Reactome:R-HSA-159001 "urokinase plasminogen activator (two-chain):uPAR + plasminogen activator inhibitor 2 (PAI-2) -> PAI-2:urokinase plasminogen activator (two-chain):uPAR"
xref: Reactome:R-HSA-159005 "urokinase plasminogen activator (two-chain):uPAR + plasminogen activator inhibitor 1 (PAI-1) -> PAI-1:urokinase plasminogen activator (two-chain):uPAR"
is_a: GO:0004866 ! endopeptidase inhibitor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 165960-165968`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0030414
name: peptidase inhibitor activity
namespace: molecular_function
def: "Binds to and stops, prevents or reduces the activity of a peptidase, any enzyme that catalyzes the hydrolysis peptide bonds." [GOC:jl]
synonym: "protease inhibitor activity" NARROW [GOC:mah]
is_a: GO:0004857 ! enzyme inhibitor activity
is_a: GO:0061134 ! peptidase regulator activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
