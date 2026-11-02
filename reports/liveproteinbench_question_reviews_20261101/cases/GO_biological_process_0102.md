# GO_biological_process_0102

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — lysosome fission

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTRPYIKRLSFTLLDSITDKDPMVQEQVCSALCSLGDAQPDETLHACEEYLRQHDKLAHPYRTKILRAMETVLSSHIHDLDKDTAGAVILLATSEMTRTKELDCDWQQAAGSVLVAVGKRFTNQVMEEVLSRFQPGMLPHSSVLHTLANLSVSNAFDMVPFLPSILSTMLPMLSMAKQDALKVVFCGALQHFSESILEYLANLDQAPDPTVRKDTFGADIFGAYDVLFHHWLQSRDAKLRLAVVAALGPMSHLLPSERLEEQLPKLLPAVLGLYKKHAEAFQISKSLGQILEAAVNVSSRTLEVQLDALLVALHAQICVPVESSSPLVMNSQKEVLRCFTVLACCSPDRLLAFLLPRLDTSNERLRVGTLQILRHIINSAAAQMEAKQPFILSSMRLPLLDTNDKVKRAVVQVISAMAHHGYLEQPGGEVMVEYIVQQCALPAEEPEKPGPDGEDLAADSVRAVSIRTLYLVSTTVDRMNSVLWPYLLEFLTPVRFTAALTPLCRSLVHLALKRQEAGADDFLIQYNANANLPSPFAMTTRLLVVSSNPYLGDGRGAASLRLLKVMHQNIHPFLGQRWETTMPMLLEYLDEHTEESLSLKEWEEKLLMFLRDTLAVVSDNIWICQLSQEMCKQLPSYSGTPQEKNFLYKCIGTTLGAASSKEVVRKHLRELLETARYQEEAEQEGLACCFGICAITHLEDTLAQLEDFVRSDVFRKSTGIFSIFKDRSEHEVERMKSCLILCYGHVAAQAPRELVLARVESDILRSMFQCFNTKVLGIKVETKDPALKLCLVQSLCMVSQAMCSSAQASSFHFLRKTELVTQMMEFIRAEPPDCLRTPIRKKAMLACTYLVNLEPALEEQTQADVVHSCLHSVMALPPEAEGGDGVGREPLYLDTVCALEDLLTRLLRQNMTPQGLQIMVEHLSPWIKSPRGHERARALGLGACLLEFFQEHLLVSTLVPFHNLGLLVGLFAPRCADTWTTTRQKAVGCVYSLLYLQLGYEGFSRDHRDDVAERLLTLQDGLVNADPTILFHTCHSIAQVIAKRLPSDQLISLLLTVFESLGDPDKNCSRAATVMINCLLKERGNVLLEKVPEIVSVLRAKLRDTQEEHVLPAAQHSVYLLASQHCEAVVSSLLGSPLPFDSHTCALWRALAVEPGLTAQVLELLLEKMSKDVPFKESRAFLLGSTADRVATLLPLAATCALYEVLSAPSSGTVVLELYPQLFAALLLRVSCTVGVQLPRNLQAKERRSTSPARAARNLDPCSSAVDALQALLLRSGSQDMLRCVELERGWELLKTSAGHEDGVAQLASSMAKYAGPRLPPVTKALACTQNSVYEIQRVTSTAFLAELLSSNVVNDLMLLEPLLDNLTARLKDSSASVRRLVLRGLANMASGSPDKVRAHGPQLLTAMVSGLDDGDEPHSPVALEAMVGLSRLLDLVEPWDLRLVLLHTTIRIRPFFDSEKVEFRTASIRLFGHLNKACHGDCEDVFLEQVVGGLVPLLLHLRDPQVPVASACKFALCMCVPHLECAELAAAFYKYLQEGRSVHFGEFLNSTCKHLMHHFPDLLGRLVSTNLFYFKSSWDDVRAAAPMFTGFLVLHAEPEQKTQVDLEQLIVALQLLLKDPVPGVREKAAETLGRLVKFA

[Multiple Choices]
A. base-excision repair, AP site formation
B. lysosome fission
C. daunorubicin transport
D. ribosomal large subunit assembly
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

> The supplied sequence matches the mouse MROH1 entry, whose annotation identifies lysosome fission as a function and lists the corresponding GO biological-process term. The functional annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long protein sequence is compatible with a large repeat-containing protein, but that broad feature does not distinguish lysosome fission from the other specific processes in the choices.


**Missing item-specific fact**

> The protein-specific identity or functional annotation linking this sequence to lysosome fission is needed to select B.


**Reason**

> The supplied sequence and choices provide no sufficiently specific biological clue to infer lysosome fission; choosing B requires protein-specific annotation or equivalent external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein annotation specifically supports lysosome fission; none of the other listed choices is supported by the supplied evidence.


### Important caveats

- The annotation evidence is similarity-transferred, not a direct experimental demonstration for the mouse sequence.
- The reviewer-only accession and database annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long protein sequence is compatible with a large repeat-containing protein, but that broad feature does not distinguish lysosome fission from the other specific processes in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation linking this sequence to lysosome fission is needed to select B.",
    "reason": "The supplied sequence and choices provide no sufficiently specific biological clue to infer lysosome fission; choosing B requires protein-specific annotation or equivalent external knowledge."
  },
  "case_id": "GO_biological_process_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the mouse MROH1 entry, whose annotation identifies lysosome fission as a function and lists the corresponding GO biological-process term. The functional annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The annotation evidence is similarity-transferred, not a direct experimental demonstration for the mouse sequence.",
    "The reviewer-only accession and database annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation specifically supports lysosome fission; none of the other listed choices is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the mouse MROH1 entry, whose annotation identifies lysosome fission as a function and lists the corresponding GO biological-process term. The functional annotation is transferred by similarity (ECO:0000250), and the GO annotation is ISS, so this supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long protein sequence is compatible with a large repeat-containing protein, but that broad feature does not distinguish lysosome fission from the other specific processes in the choices.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation linking this sequence to lysosome fission is needed to select B.",
    "reason": "The supplied sequence and choices provide no sufficiently specific biological clue to infer lysosome fission; choosing B requires protein-specific annotation or equivalent external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation specifically supports lysosome fission; none of the other listed choices is supported by the supplied evidence."
  },
  "important_caveats": [
    "The annotation evidence is similarity-transferred, not a direct experimental demonstration for the mouse sequence.",
    "The reviewer-only accession and database annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E0CZ22 (MROH1_MOUSE) explicitly annotates the protein as a 'Lysosome fission factor' (C5/H2) and assigns GO:0170064 'P:lysosome fission' (C6/H3). The evidence code is ISS:UniProtKB (inferred from sequence similarity to human MROH1, Q8NDA8), which is a computational transfer rather than direct experimental evidence for the mouse protein. However, the human ortholog annotation is well-supported (PMID:31171420 cited in the GO term definition, GO4), and the mouse-human orthology is high-confidence. The sequence match is confirmed (SHA256 identical across current and historical records). The expected answer B is consistent with the database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1640-aa protein contains multiple Maestro heat-like (MAHR) repeat domains (protein-protein interaction modules) and potential amphipathic helices, but lacks: (1) DNA glycosylase catalytic motifs (e.g., HhH-GPD, helix-hairpin-helix) required for base-excision repair/AP site formation (option A); (2) transmembrane helix bundles and nucleotide-binding domains characteristic of drug efflux transporters needed for daunorubicin transport (option C); (3) RNA-recognition motifs (RRM), KH domains, or ribosomal-protein-like folds required for ribosomal large subunit assembly (option D). By elimination of these three mechanistically incompatible options, the remaining choice B (lysosome fission) is the only process compatible with a large cytoplasmic protein bearing protein-protein interaction repeats and membrane-severing amphipathic helices.


**Missing item-specific fact**

> Positive identification of 'lysosome fission' specifically (as opposed to other organelle-fission or membrane-remodeling processes) would require knowing the RAB7-interaction and scission-site recruitment mechanism of MROH1, which is not derivable from sequence alone. However, among the four provided options, elimination reasoning is sufficient to select B.


**Reason**

> The three distractors each require highly specific structural/functional features (glycosylase active sites, transporter TM domains, RNA-binding folds) that are clearly absent from this sequence. A knowledgeable model can exclude them through general domain-architecture reasoning. The positive assignment to 'lysosome fission' is weakly supported by the presence of amphipathic helices and interaction repeats consistent with membrane scission machinery, but the primary discriminating logic is elimination of incompatible alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D each require well-defined catalytic or structural features (DNA glycosylase motifs, transmembrane transporter domains, RNA-binding domains) that are absent from this sequence. Only option B is mechanistically compatible with the observed domain architecture (MAHR repeats + amphipathic helices, no enzymatic active site, no transport or RNA-binding motifs).


### Important caveats

- The UniProt annotation for lysosome fission is ISS (Inferred from Sequence Similarity to human Q8NDA8), not direct experimental evidence for the mouse protein. The underlying human evidence (PMID:31171420) supports the function for MROH1 as a family.
- The positive identification of 'lysosome fission' specifically (rather than a broader 'membrane fission' or 'organelle dynamics' category) relies on knowing the RAB7-recruitment mechanism, which is not inferable from sequence alone. The reasoning is primarily eliminative.
- The GO term GO:0170064 (lysosome fission) is relatively new (defined with PMIDs 31171420 and 38538795); the exact ontology version used by the benchmark authors is unknown.
- The protein sequence contains many hydrophobic stretches within the MAHR repeats that could superficially resemble transmembrane segments, but they lack the contiguous 20-25 residue hydrophobic runs of true TM domains and are interspersed with polar/charged residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1640-aa protein contains multiple Maestro heat-like (MAHR) repeat domains (protein-protein interaction modules) and potential amphipathic helices, but lacks: (1) DNA glycosylase catalytic motifs (e.g., HhH-GPD, helix-hairpin-helix) required for base-excision repair/AP site formation (option A); (2) transmembrane helix bundles and nucleotide-binding domains characteristic of drug efflux transporters needed for daunorubicin transport (option C); (3) RNA-recognition motifs (RRM), KH domains, or ribosomal-protein-like folds required for ribosomal large subunit assembly (option D). By elimination of these three mechanistically incompatible options, the remaining choice B (lysosome fission) is the only process compatible with a large cytoplasmic protein bearing protein-protein interaction repeats and membrane-severing amphipathic helices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of 'lysosome fission' specifically (as opposed to other organelle-fission or membrane-remodeling processes) would require knowing the RAB7-interaction and scission-site recruitment mechanism of MROH1, which is not derivable from sequence alone. However, among the four provided options, elimination reasoning is sufficient to select B.",
    "reason": "The three distractors each require highly specific structural/functional features (glycosylase active sites, transporter TM domains, RNA-binding folds) that are clearly absent from this sequence. A knowledgeable model can exclude them through general domain-architecture reasoning. The positive assignment to 'lysosome fission' is weakly supported by the presence of amphipathic helices and interaction repeats consistent with membrane scission machinery, but the primary discriminating logic is elimination of incompatible alternatives."
  },
  "case_id": "GO_biological_process_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E0CZ22 (MROH1_MOUSE) explicitly annotates the protein as a 'Lysosome fission factor' (C5/H2) and assigns GO:0170064 'P:lysosome fission' (C6/H3). The evidence code is ISS:UniProtKB (inferred from sequence similarity to human MROH1, Q8NDA8), which is a computational transfer rather than direct experimental evidence for the mouse protein. However, the human ortholog annotation is well-supported (PMID:31171420 cited in the GO term definition, GO4), and the mouse-human orthology is high-confidence. The sequence match is confirmed (SHA256 identical across current and historical records). The expected answer B is consistent with the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation for lysosome fission is ISS (Inferred from Sequence Similarity to human Q8NDA8), not direct experimental evidence for the mouse protein. The underlying human evidence (PMID:31171420) supports the function for MROH1 as a family.",
    "The positive identification of 'lysosome fission' specifically (rather than a broader 'membrane fission' or 'organelle dynamics' category) relies on knowing the RAB7-recruitment mechanism, which is not inferable from sequence alone. The reasoning is primarily eliminative.",
    "The GO term GO:0170064 (lysosome fission) is relatively new (defined with PMIDs 31171420 and 38538795); the exact ontology version used by the benchmark authors is unknown.",
    "The protein sequence contains many hydrophobic stretches within the MAHR repeats that could superficially resemble transmembrane segments, but they lack the contiguous 20-25 residue hydrophobic runs of true TM domains and are interspersed with polar/charged residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require well-defined catalytic or structural features (DNA glycosylase motifs, transmembrane transporter domains, RNA-binding domains) that are absent from this sequence. Only option B is mechanistically compatible with the observed domain architecture (MAHR repeats + amphipathic helices, no enzymatic active site, no transport or RNA-binding motifs)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E0CZ22 (MROH1_MOUSE) explicitly annotates the protein as a 'Lysosome fission factor' (C5/H2) and assigns GO:0170064 'P:lysosome fission' (C6/H3). The evidence code is ISS:UniProtKB (inferred from sequence similarity to human MROH1, Q8NDA8), which is a computational transfer rather than direct experimental evidence for the mouse protein. However, the human ortholog annotation is well-supported (PMID:31171420 cited in the GO term definition, GO4), and the mouse-human orthology is high-confidence. The sequence match is confirmed (SHA256 identical across current and historical records). The expected answer B is consistent with the database annotation.",
    "evidence_ids": ["C5", "C6", "H2", "H3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1640-aa protein contains multiple Maestro heat-like (MAHR) repeat domains (protein-protein interaction modules) and potential amphipathic helices, but lacks: (1) DNA glycosylase catalytic motifs (e.g., HhH-GPD, helix-hairpin-helix) required for base-excision repair/AP site formation (option A); (2) transmembrane helix bundles and nucleotide-binding domains characteristic of drug efflux transporters needed for daunorubicin transport (option C); (3) RNA-recognition motifs (RRM), KH domains, or ribosomal-protein-like folds required for ribosomal large subunit assembly (option D). By elimination of these three mechanistically incompatible options, the remaining choice B (lysosome fission) is the only process compatible with a large cytoplasmic protein bearing protein-protein interaction repeats and membrane-severing amphipathic helices.",
    "missing_item_specific_fact": "Positive identification of 'lysosome fission' specifically (as opposed to other organelle-fission or membrane-remodeling processes) would require knowing the RAB7-interaction and scission-site recruitment mechanism of MROH1, which is not derivable from sequence alone. However, among the four provided options, elimination reasoning is sufficient to select B.",
    "reason": "The three distractors each require highly specific structural/functional features (glycosylase active sites, transporter TM domains, RNA-binding folds) that are clearly absent from this sequence. A knowledgeable model can exclude them through general domain-architecture reasoning. The positive assignment to 'lysosome fission' is weakly supported by the presence of amphipathic helices and interaction repeats consistent with membrane scission machinery, but the primary discriminating logic is elimination of incompatible alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D each require well-defined catalytic or structural features (DNA glycosylase motifs, transmembrane transporter domains, RNA-binding domains) that are absent from this sequence. Only option B is mechanistically compatible with the observed domain architecture (MAHR repeats + amphipathic helices, no enzymatic active site, no transport or RNA-binding motifs)."
  },
  "important_caveats": [
    "The UniProt annotation for lysosome fission is ISS (Inferred from Sequence Similarity to human Q8NDA8), not direct experimental evidence for the mouse protein. The underlying human evidence (PMID:31171420) supports the function for MROH1 as a family.",
    "The positive identification of 'lysosome fission' specifically (rather than a broader 'membrane fission' or 'organelle dynamics' category) relies on knowing the RAB7-recruitment mechanism, which is not inferable from sequence alone. The reasoning is primarily eliminative.",
    "The GO term GO:0170064 (lysosome fission) is relatively new (defined with PMIDs 31171420 and 38538795); the exact ontology version used by the benchmark authors is unknown.",
    "The protein sequence contains many hydrophobic stretches within the MAHR repeats that could superficially resemble transmembrane segments, but they lack the contiguous 20-25 residue hydrophobic runs of true TM domains and are interspersed with polar/charged residues."
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

**Accession:** `E0CZ22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 93. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
"E0CZ22"
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8NDA8","source":"UniProtKB"}],"value":"Lysosome fission factor. Recruited to lysosomes by RAB7 (RAB7A or RAB7B) at scission sites and homooligomerizes to mediate the constriction and scission of lysosomal tubules. May sever membranes by inserting amphipathic helices into one bilayer leaflet. Lysosome fission is required to maintain their steady-state number, shape, size, composition and function, and to accomplish regeneration"}]}
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/uniProtKBCrossReferences/45`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
{"database":"GO","id":"GO:0170064","properties":[{"key":"GoTerm","value":"P:lysosome fission"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)  
**Locator:** `lines 37-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 93 / 1.  
**Retrieved:** 2026-11-02T04:27:56.152074+00:00.  

```text
CC   -!- FUNCTION: Lysosome fission factor. Recruited to lysosomes by RAB7
CC       (RAB7A or RAB7B) at scission sites and homooligomerizes to mediate the
CC       constriction and scission of lysosomal tubules. May sever membranes by
CC       inserting amphipathic helices into one bilayer leaflet. Lysosome
CC       fission is required to maintain their steady-state number, shape, size,
CC       composition and function, and to accomplish regeneration.
CC       {ECO:0000250|UniProtKB:Q8NDA8}.
```

Source SHA-256: `ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)  
**Locator:** `lines 107-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 93 / 1.  
**Retrieved:** 2026-11-02T04:27:56.152074+00:00.  

```text
DR   GO; GO:0170064; P:lysosome fission; ISS:UniProtKB.
```

Source SHA-256: `ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 452157-452163`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0170064
name: lysosome fission
namespace: biological_process
def: "The process by which lysosomes undergo budding and fission to maintain their steady-state number, shape, size, composition and function, and to accomplish regeneration." [PMID:31171420, PMID:38538795]
is_a: GO:0048285 ! organelle fission

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
