# GO_cellular_component_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — mitochondrial inner membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNELSVNDAFDDIEIESFDFIWEEWEEYKGDVPLWQHIFCGSIAGLMEHVFMYPLDTLKTYFQTNGHMKYNMIYDNCNTINNNNNNIYRGNNSSYKNTCDKNYKDMNNHRNMQTFKRNFCSSTNCDKCIINNFCKYKTNCYNVMAALHTKNNRYIHNIAEPLKNMANYKINTTNNNNVNNIINNNNNNNKKKSRNIFSYPSHTKQYRNVTYVVNKKMQQNLFNNYISNKCINDPFCCRTKTNVLNMKKDIHKFCHLSKEKYNNVFYQNDTYHPNIYGRKRKTLCRNKNNINLFKNHVHKKYCHSLDDQICHSKIKEDMRNLQNFKNYTCAKNMKRHLYSTVPFFNLKNKGNKNITLPYKEIRSKYILKNGYKSMYQRNAGYYKNLIKMQSAKKNRHQLLALRKCLMSEKKYTIIKNEPFIIRKKKNMRNEYFIGNMKGRCIINTSLNSYTLKRNCLDYHHFVNNLKNICYSIMNICYNIKNTILINPSLPINNNNNNNNNTKMDTFIKLINKCLYNNNAHKIDHKILLSNYLNLFKHTNYSYYYILNNFLKNNAPCTSRKNEWNIFSNFINVLKNKIITNNVDYIRNPNVRRNQILRNNYLYSFLRNYNKNLKRNTHMILNKLTSFKYSIPYIKNKYSNVLINNINTNNNTYSNRNVLNSIRYNNIYKNIMHPIFFPGYYNTIHFRYYNYFSRIIDDKDKGKNKNIINISTKRNNCSSIIRNNLSNLYKGVNVVVLGCIPAHALYFSTFEYSKKYFSRMTSNNSSLKMNNRNISTVSNDIKSEKSNFKLYDLNYFSIAVSGFLATLVHDLIITPIDTLKQRIQLGINKNSKDSLKLLKQNGIRSLYLSLPITLLMNIPYQIIMICTNEKMKKIYFEYICGLNTQNNKKNMENKVIDKVHDETRNQDNIGKDIKNDTYNMDKNGTFLRNQEMINKENRIYNSGALEKHVTSQEKEDKILQSVKQENVSSNNDIVNFYEGQSIYNNDAHNIIRDDINKMTHKNLENNIDNTINSNESDVNRIDNMTNDMNKECDIFSINKNNNSTVLYDQIMKRLEMNSSNKNFSLNFHDKIIRQESSPFEKENYNMNLKNIWIDNYKNDFFNKPFNHITSYFVCAGIGGGIAAVLTNPLDVIKTRIQTECFQTKGFNFFRIVSNIYYREGMRSFFKGSLARMALCIPASAVSWGTYETMKRFFKINFNTT

[Multiple Choices]
A. voltage-gated calcium channel complex
B. virus tail, tube
C. mitochondrial inner membrane
D. cellular bud neck septin ring
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

> The exact sequence match is annotated as a putative mitoferrin/mitochondrial carrier protein, and its subcellular location is reported as mitochondrial membrane with experimental evidence. The inner-membrane assignment is consistent with a mitochondrial carrier, although the cited location annotation itself specifies only mitochondrial membrane.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic, multipass membrane-protein region, which disfavors the soluble septin-ring and viral-tail choices. But multipass topology alone does not distinguish a mitochondrial carrier from a calcium-channel protein or establish mitochondrial localization.


**Missing item-specific fact**

> The protein-specific identification as a putative mitoferrin/MRS3 mitochondrial carrier and its mitochondrial localization are not given in the question; the sequence would need to be recognized as that protein or matched to an external annotation.


**Reason**

> The choices make some alternatives implausible, but the supplied sequence and context do not provide a robust basis for assigning this particular multipass protein to the mitochondrial inner membrane rather than another membrane-associated class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports mitochondrial membrane localization, and the carrier identity makes the inner-membrane choice the best-supported option. The evidence is less specific than the wording of choice C.


### Important caveats

- The experimental subcellular-location evidence reports mitochondrial membrane, not explicitly mitochondrial inner membrane.
- The GO annotations provided are broader mitochondrial-membrane annotations; they do not independently establish the narrower inner-membrane term.
- The current and historical database records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic, multipass membrane-protein region, which disfavors the soluble septin-ring and viral-tail choices. But multipass topology alone does not distinguish a mitochondrial carrier from a calcium-channel protein or establish mitochondrial localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a putative mitoferrin/MRS3 mitochondrial carrier and its mitochondrial localization are not given in the question; the sequence would need to be recognized as that protein or matched to an external annotation.",
    "reason": "The choices make some alternatives implausible, but the supplied sequence and context do not provide a robust basis for assigning this particular multipass protein to the mitochondrial inner membrane rather than another membrane-associated class."
  },
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a putative mitoferrin/mitochondrial carrier protein, and its subcellular location is reported as mitochondrial membrane with experimental evidence. The inner-membrane assignment is consistent with a mitochondrial carrier, although the cited location annotation itself specifies only mitochondrial membrane."
  },
  "important_caveats": [
    "The experimental subcellular-location evidence reports mitochondrial membrane, not explicitly mitochondrial inner membrane.",
    "The GO annotations provided are broader mitochondrial-membrane annotations; they do not independently establish the narrower inner-membrane term.",
    "The current and historical database records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports mitochondrial membrane localization, and the carrier identity makes the inner-membrane choice the best-supported option. The evidence is less specific than the wording of choice C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a putative mitoferrin/mitochondrial carrier protein, and its subcellular location is reported as mitochondrial membrane with experimental evidence. The inner-membrane assignment is consistent with a mitochondrial carrier, although the cited location annotation itself specifies only mitochondrial membrane.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic, multipass membrane-protein region, which disfavors the soluble septin-ring and viral-tail choices. But multipass topology alone does not distinguish a mitochondrial carrier from a calcium-channel protein or establish mitochondrial localization.",
    "missing_item_specific_fact": "The protein-specific identification as a putative mitoferrin/MRS3 mitochondrial carrier and its mitochondrial localization are not given in the question; the sequence would need to be recognized as that protein or matched to an external annotation.",
    "reason": "The choices make some alternatives implausible, but the supplied sequence and context do not provide a robust basis for assigning this particular multipass protein to the mitochondrial inner membrane rather than another membrane-associated class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports mitochondrial membrane localization, and the carrier identity makes the inner-membrane choice the best-supported option. The evidence is less specific than the wording of choice C."
  },
  "important_caveats": [
    "The experimental subcellular-location evidence reports mitochondrial membrane, not explicitly mitochondrial inner membrane.",
    "The GO annotations provided are broader mitochondrial-membrane annotations; they do not independently establish the narrower inner-membrane term.",
    "The current and historical database records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates Q8I397 as 'Mitochondrion membrane' (GO:0031966) with experimental evidence (ECO:0000269, PubMed:39575308) and multi-pass membrane topology (ECO:0000255). The protein is a putative mitoferrin (PfMFRN), a family of inner mitochondrial membrane iron carriers. GO:0005743 (mitochondrial inner membrane) is a child of GO:0031966 (mitochondrial membrane) per the ontology. The annotation is at the parent level ('mitochondrial membrane') rather than explicitly 'inner membrane,' but the mitoferrin/carrier identity and multi-pass topology are consistent with inner membrane localization. The expected answer is supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The extreme N-richness of the sequence is a hallmark of Plasmodium falciparum, a eukaryotic apicomplexan parasite. This organism context eliminates option B (virus tail, tube — a bacteriophage structural component; eukaryotes do not encode phage tail tubes) and option D (cellular bud neck septin ring — the GO definition explicitly specifies S. cerevisiae budding cytokinesis; Plasmodium does not bud). Option A (voltage-gated calcium channel complex) requires the characteristic four-domain, six-transmembrane-segment voltage-sensor architecture and is found in excitable animal cells; the sequence lacks this architecture and Plasmodium has no excitable-cell machinery. The remaining option C (mitochondrial inner membrane) is the only biologically plausible compartment for a multi-pass membrane protein in a eukaryotic parasite. The C-terminal region contains hydrophobic segments consistent with multi-pass membrane topology, further supporting C.


**Missing item-specific fact**

> None required for selection among the four choices. Positive identification of the protein as a mitoferrin and the inner-vs-outer membrane distinction would require protein-specific knowledge, but among the four provided options, general biological reasoning about organism type and domain architecture suffices to eliminate A, B, and D.


**Reason**

> The elimination of B (bacteriophage component in a eukaryote), D (yeast-specific septin ring), and A (voltage-gated channel architecture absent; no excitable-cell biology) relies on general biological knowledge about organism types, GO term definitions, and protein domain architecture. The sequence's N-richness signals P. falciparum, and the hydrophobic segments in the C-terminal region are consistent with a multi-pass membrane protein. This is a concrete biological argument from the supplied sequence and choices, not a lookup of a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are biologically impossible for a Plasmodium falciparum protein (bacteriophage tail tube; yeast bud-neck septin ring). Option A lacks the required domain architecture and organism context. Only C is a plausible mitochondrial compartment for a eukaryotic parasite multi-pass membrane protein. No other option is defensible.


### Important caveats

- The UniProt subcellular location annotation is 'Mitochondrion membrane' (GO:0031966), the parent of 'mitochondrial inner membrane' (GO:0005743). The 'inner' specification in the answer choice is more precise than the annotation term, though it is consistent with the mitoferrin family identity.
- The multi-pass membrane topology is annotated with ECO:0000255 (computational inference), not experimental determination.
- The mitochondrial targeting signal in P. falciparum is atypical due to the organism's extreme AT bias; standard MTS prediction heuristics may not apply, making positive mitochondrial identification from sequence alone difficult. However, among the four choices, elimination-based reasoning suffices.
- The GO evidence for the mitochondrial membrane annotation in the current snapshot is IEA (inferred from electronic annotation / UniProt-SubCell), while the underlying UniProt comment carries experimental evidence (ECO:0000269).
- The identity of the protein as Q8I397 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The extreme N-richness of the sequence is a hallmark of Plasmodium falciparum, a eukaryotic apicomplexan parasite. This organism context eliminates option B (virus tail, tube — a bacteriophage structural component; eukaryotes do not encode phage tail tubes) and option D (cellular bud neck septin ring — the GO definition explicitly specifies S. cerevisiae budding cytokinesis; Plasmodium does not bud). Option A (voltage-gated calcium channel complex) requires the characteristic four-domain, six-transmembrane-segment voltage-sensor architecture and is found in excitable animal cells; the sequence lacks this architecture and Plasmodium has no excitable-cell machinery. The remaining option C (mitochondrial inner membrane) is the only biologically plausible compartment for a multi-pass membrane protein in a eukaryotic parasite. The C-terminal region contains hydrophobic segments consistent with multi-pass membrane topology, further supporting C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required for selection among the four choices. Positive identification of the protein as a mitoferrin and the inner-vs-outer membrane distinction would require protein-specific knowledge, but among the four provided options, general biological reasoning about organism type and domain architecture suffices to eliminate A, B, and D.",
    "reason": "The elimination of B (bacteriophage component in a eukaryote), D (yeast-specific septin ring), and A (voltage-gated channel architecture absent; no excitable-cell biology) relies on general biological knowledge about organism types, GO term definitions, and protein domain architecture. The sequence's N-richness signals P. falciparum, and the hydrophobic segments in the C-terminal region are consistent with a multi-pass membrane protein. This is a concrete biological argument from the supplied sequence and choices, not a lookup of a specific database annotation."
  },
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates Q8I397 as 'Mitochondrion membrane' (GO:0031966) with experimental evidence (ECO:0000269, PubMed:39575308) and multi-pass membrane topology (ECO:0000255). The protein is a putative mitoferrin (PfMFRN), a family of inner mitochondrial membrane iron carriers. GO:0005743 (mitochondrial inner membrane) is a child of GO:0031966 (mitochondrial membrane) per the ontology. The annotation is at the parent level ('mitochondrial membrane') rather than explicitly 'inner membrane,' but the mitoferrin/carrier identity and multi-pass topology are consistent with inner membrane localization. The expected answer is supported."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation is 'Mitochondrion membrane' (GO:0031966), the parent of 'mitochondrial inner membrane' (GO:0005743). The 'inner' specification in the answer choice is more precise than the annotation term, though it is consistent with the mitoferrin family identity.",
    "The multi-pass membrane topology is annotated with ECO:0000255 (computational inference), not experimental determination.",
    "The mitochondrial targeting signal in P. falciparum is atypical due to the organism's extreme AT bias; standard MTS prediction heuristics may not apply, making positive mitochondrial identification from sequence alone difficult. However, among the four choices, elimination-based reasoning suffices.",
    "The GO evidence for the mitochondrial membrane annotation in the current snapshot is IEA (inferred from electronic annotation / UniProt-SubCell), while the underlying UniProt comment carries experimental evidence (ECO:0000269).",
    "The identity of the protein as Q8I397 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are biologically impossible for a Plasmodium falciparum protein (bacteriophage tail tube; yeast bud-neck septin ring). Option A lacks the required domain architecture and organism context. Only C is a plausible mitochondrial compartment for a eukaryotic parasite multi-pass membrane protein. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates Q8I397 as 'Mitochondrion membrane' (GO:0031966) with experimental evidence (ECO:0000269, PubMed:39575308) and multi-pass membrane topology (ECO:0000255). The protein is a putative mitoferrin (PfMFRN), a family of inner mitochondrial membrane iron carriers. GO:0005743 (mitochondrial inner membrane) is a child of GO:0031966 (mitochondrial membrane) per the ontology. The annotation is at the parent level ('mitochondrial membrane') rather than explicitly 'inner membrane,' but the mitoferrin/carrier identity and multi-pass topology are consistent with inner membrane localization. The expected answer is supported.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The extreme N-richness of the sequence is a hallmark of Plasmodium falciparum, a eukaryotic apicomplexan parasite. This organism context eliminates option B (virus tail, tube — a bacteriophage structural component; eukaryotes do not encode phage tail tubes) and option D (cellular bud neck septin ring — the GO definition explicitly specifies S. cerevisiae budding cytokinesis; Plasmodium does not bud). Option A (voltage-gated calcium channel complex) requires the characteristic four-domain, six-transmembrane-segment voltage-sensor architecture and is found in excitable animal cells; the sequence lacks this architecture and Plasmodium has no excitable-cell machinery. The remaining option C (mitochondrial inner membrane) is the only biologically plausible compartment for a multi-pass membrane protein in a eukaryotic parasite. The C-terminal region contains hydrophobic segments consistent with multi-pass membrane topology, further supporting C.",
    "missing_item_specific_fact": "None required for selection among the four choices. Positive identification of the protein as a mitoferrin and the inner-vs-outer membrane distinction would require protein-specific knowledge, but among the four provided options, general biological reasoning about organism type and domain architecture suffices to eliminate A, B, and D.",
    "reason": "The elimination of B (bacteriophage component in a eukaryote), D (yeast-specific septin ring), and A (voltage-gated channel architecture absent; no excitable-cell biology) relies on general biological knowledge about organism types, GO term definitions, and protein domain architecture. The sequence's N-richness signals P. falciparum, and the hydrophobic segments in the C-terminal region are consistent with a multi-pass membrane protein. This is a concrete biological argument from the supplied sequence and choices, not a lookup of a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are biologically impossible for a Plasmodium falciparum protein (bacteriophage tail tube; yeast bud-neck septin ring). Option A lacks the required domain architecture and organism context. Only C is a plausible mitochondrial compartment for a eukaryotic parasite multi-pass membrane protein. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation is 'Mitochondrion membrane' (GO:0031966), the parent of 'mitochondrial inner membrane' (GO:0005743). The 'inner' specification in the answer choice is more precise than the annotation term, though it is consistent with the mitoferrin family identity.",
    "The multi-pass membrane topology is annotated with ECO:0000255 (computational inference), not experimental determination.",
    "The mitochondrial targeting signal in P. falciparum is atypical due to the organism's extreme AT bias; standard MTS prediction heuristics may not apply, making positive mitochondrial identification from sequence alone difficult. However, among the four choices, elimination-based reasoning suffices.",
    "The GO evidence for the mitochondrial membrane annotation in the current snapshot is IEA (inferred from electronic annotation / UniProt-SubCell), while the underlying UniProt comment carries experimental evidence (ECO:0000269).",
    "The identity of the protein as Q8I397 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence."
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

**Accession:** `Q8I397` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 135. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
"Q8I397"
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39575308","source":"PubMed"}],"value":"Mitochondrial carrier protein MRS3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39575308","source":"PubMed"}],"value":"PfMRS3"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Putative mitoferrin"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39575308","source":"PubMed"}],"value":"PfMFRN"}]}}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39575308","source":"PubMed"}],"id":"SL-0171","value":"Mitochondrion membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I397.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.528080+00:00.  

```json
{"database":"GO","id":"GO:0031966","properties":[{"key":"GoTerm","value":"C:mitochondrial membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `64a07ac833bcdaa5f16916503d17a527091a2554f2b767b74f3db8b2cbd72f0d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 59-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane
CC       {ECO:0000269|PubMed:39575308}; Multi-pass membrane protein
CC       {ECO:0000255}.
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I397?format=txt&versions=135)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 135 / 1.  
**Retrieved:** 2026-11-02T04:32:05.771018+00:00.  

```text
DR   GO; GO:0031966; C:mitochondrial membrane; IBA:GO_Central.
```

Source SHA-256: `bf15e883316270849a9a16a7cc13d9d57f408c43c32b3e33427c843bd980f455`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59031-59043`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005743
name: mitochondrial inner membrane
namespace: cellular_component
def: "The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae." [GOC:ai]
synonym: "inner mitochondrial membrane" EXACT []
synonym: "inner mitochondrion membrane" EXACT []
synonym: "mitochondrion inner membrane" EXACT []
xref: NIF_Subcellular:sao1371347282
xref: Wikipedia:Inner_mitochondrial_membrane
is_a: GO:0019866 ! organelle inner membrane
is_a: GO:0031966 ! mitochondrial membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
