# GO_molecular_function_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — transcription cis-regulatory region binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDLANTAERRGEKRPAGGNRRGNRLPRDERRGQLLIAASEVFVDRGYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLQRHVDNLVSGVRQALRTTTDNRQRLRAAVEAFFDFIEHDSQGYRLIFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWLNNDRPIDKDSAVEGTVQFAWGGLSHVPLTRS

[Multiple Choices]
A. ATPase-coupled transmembrane transporter activity
B. RNA polymerase II cis-regulatory region sequence-specific DNA binding
C. transcription cis-regulatory region binding
D. quercetin 7-O-glucosyltransferase activity
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

> The matched sequence is annotated as a transcriptional activator that binds promoter operator sequences; its GO annotation includes transcription cis-regulatory region binding. The GO annotation is computational (IEA:TreeGrafter), while the cited functional description includes experimental evidence for transcriptional regulation. The specific operator-binding statement is qualified as by similarity.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble, helical DNA-binding regulator, which makes the transcription-related choices more plausible than a membrane transporter or a specialized glucosyltransferase. But that broad inference does not establish binding to a transcription cis-regulatory region or resolve the precise GO term.


**Missing item-specific fact**

> The protein-specific fact that this sequence is FasR, a mycobacterial transcriptional activator that binds promoter operator sequences; neither the organism nor that binding activity is provided in the question.


**Reason**

> Sequence features can suggest a regulator, but the decisive promoter-binding function and its scope require protein-specific annotation or experimental knowledge. Recognizing this exact sequence would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-specific evidence supports the broader transcription cis-regulatory region binding option. The RNA polymerase II option is more specific and does not fit the annotated bacterial regulator.


### Important caveats

- The sequence match is exact, but the author's source snapshot is unknown.
- The GO annotation is computational; the cited functional description includes experimental support, while the specific operator-binding detail is reported by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble, helical DNA-binding regulator, which makes the transcription-related choices more plausible than a membrane transporter or a specialized glucosyltransferase. But that broad inference does not establish binding to a transcription cis-regulatory region or resolve the precise GO term.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is FasR, a mycobacterial transcriptional activator that binds promoter operator sequences; neither the organism nor that binding activity is provided in the question.",
    "reason": "Sequence features can suggest a regulator, but the decisive promoter-binding function and its scope require protein-specific annotation or experimental knowledge. Recognizing this exact sequence would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a transcriptional activator that binds promoter operator sequences; its GO annotation includes transcription cis-regulatory region binding. The GO annotation is computational (IEA:TreeGrafter), while the cited functional description includes experimental evidence for transcriptional regulation. The specific operator-binding statement is qualified as by similarity."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description includes experimental support, while the specific operator-binding detail is reported by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific evidence supports the broader transcription cis-regulatory region binding option. The RNA polymerase II option is more specific and does not fit the annotated bacterial regulator."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a transcriptional activator that binds promoter operator sequences; its GO annotation includes transcription cis-regulatory region binding. The GO annotation is computational (IEA:TreeGrafter), while the cited functional description includes experimental evidence for transcriptional regulation. The specific operator-binding statement is qualified as by similarity.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble, helical DNA-binding regulator, which makes the transcription-related choices more plausible than a membrane transporter or a specialized glucosyltransferase. But that broad inference does not establish binding to a transcription cis-regulatory region or resolve the precise GO term.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is FasR, a mycobacterial transcriptional activator that binds promoter operator sequences; neither the organism nor that binding activity is provided in the question.",
    "reason": "Sequence features can suggest a regulator, but the decisive promoter-binding function and its scope require protein-specific annotation or experimental knowledge. Recognizing this exact sequence would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-specific evidence supports the broader transcription cis-regulatory region binding option. The RNA polymerase II option is more specific and does not fit the annotated bacterial regulator."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description includes experimental support, while the specific operator-binding detail is reported by similarity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0QTR3 (FASR_MYCS2) is annotated with GO:0000976 'transcription cis-regulatory region binding' (C7/H5, IEA:TreeGrafter). The protein is experimentally characterized (PubMed:23721164, ECO:0000269) as a transcriptional activator that 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region' (C5/H3), which is a cis-regulatory region. The GO term definition (GO1) covers 'binding to a specific sequence of DNA that is part of a regulatory region that controls transcription,' consistent with operator binding. The evidence code for the GO annotation is computational (TreeGrafter), but the underlying function is experimentally supported.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable helix-turn-helix (HTH) DNA-binding domain motif (the region 'GYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLQRHVDNLVSGVRQALRTTTDNRQRLRAAVEAFFDFIEHDSQGYRLIFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWLNNDRPIDKDSAVEGTVQFAWGGLSHVPLTRS' shows the characteristic HTH fold). This eliminates options A (no transmembrane helices or Walker A/B ATP-binding motifs) and D (no glucosyltransferase catalytic residues or PSPG box). The small size (~219 aa), single HTH domain, and absence of eukaryotic-specific features (nuclear localization signals, activation domains, zinc fingers) indicate a bacterial-type transcriptional regulator, eliminating option B which is restricted to RNA polymerase II cis-regulatory regions (a eukaryotic-specific concept). The HTH domain in bacterial regulators classically binds operator/promoter sequences, i.e., cis-regulatory regions, supporting option C.


**Missing item-specific fact**

> None critical. The HTH domain identification and elimination of eukaryotic/transporter/glycosyltransferase options rely on general domain-architecture knowledge.


**Reason**

> A knowledgeable model can identify the HTH motif as a DNA-binding domain, recognize the overall architecture as bacterial (excluding RNA Pol II–specific option B), and eliminate transporter and glycosyltransferase options by absence of relevant structural features. The remaining option C (transcription cis-regulatory region binding) follows naturally from HTH-type bacterial transcriptional regulators binding operator/promoter sequences.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is excluded because RNA polymerase II is eukaryotic and the protein architecture is bacterial. Options A and D are excluded by absence of transmembrane/ATPase and glucosyltransferase structural features respectively. The GO term GO:0000976 even lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym (GO1), further confirming applicability to a bacterial HTH regulator.


### Important caveats

- The GO annotation for the expected answer (GO:0000976) carries evidence code IEA:TreeGrafter (computational inference), not direct experimental evidence for this specific term, though the underlying operator-binding activity is experimentally supported (ECO:0000269).
- The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 219-aa sequence and general biological knowledge.
- Recognizing the HTH domain from a 219-aa sequence requires moderate expertise but falls within general molecular biology knowledge.
- The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 121 already includes GO:0000976.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable helix-turn-helix (HTH) DNA-binding domain motif (the region 'GYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLQRHVDNLVSGVRQALRTTTDNRQRLRAAVEAFFDFIEHDSQGYRLIFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWLNNDRPIDKDSAVEGTVQFAWGGLSHVPLTRS' shows the characteristic HTH fold). This eliminates options A (no transmembrane helices or Walker A/B ATP-binding motifs) and D (no glucosyltransferase catalytic residues or PSPG box). The small size (~219 aa), single HTH domain, and absence of eukaryotic-specific features (nuclear localization signals, activation domains, zinc fingers) indicate a bacterial-type transcriptional regulator, eliminating option B which is restricted to RNA polymerase II cis-regulatory regions (a eukaryotic-specific concept). The HTH domain in bacterial regulators classically binds operator/promoter sequences, i.e., cis-regulatory regions, supporting option C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The HTH domain identification and elimination of eukaryotic/transporter/glycosyltransferase options rely on general domain-architecture knowledge.",
    "reason": "A knowledgeable model can identify the HTH motif as a DNA-binding domain, recognize the overall architecture as bacterial (excluding RNA Pol II–specific option B), and eliminate transporter and glycosyltransferase options by absence of relevant structural features. The remaining option C (transcription cis-regulatory region binding) follows naturally from HTH-type bacterial transcriptional regulators binding operator/promoter sequences."
  },
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0QTR3 (FASR_MYCS2) is annotated with GO:0000976 'transcription cis-regulatory region binding' (C7/H5, IEA:TreeGrafter). The protein is experimentally characterized (PubMed:23721164, ECO:0000269) as a transcriptional activator that 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region' (C5/H3), which is a cis-regulatory region. The GO term definition (GO1) covers 'binding to a specific sequence of DNA that is part of a regulatory region that controls transcription,' consistent with operator binding. The evidence code for the GO annotation is computational (TreeGrafter), but the underlying function is experimentally supported."
  },
  "important_caveats": [
    "The GO annotation for the expected answer (GO:0000976) carries evidence code IEA:TreeGrafter (computational inference), not direct experimental evidence for this specific term, though the underlying operator-binding activity is experimentally supported (ECO:0000269).",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 219-aa sequence and general biological knowledge.",
    "Recognizing the HTH domain from a 219-aa sequence requires moderate expertise but falls within general molecular biology knowledge.",
    "The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 121 already includes GO:0000976."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is excluded because RNA polymerase II is eukaryotic and the protein architecture is bacterial. Options A and D are excluded by absence of transmembrane/ATPase and glucosyltransferase structural features respectively. The GO term GO:0000976 even lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym (GO1), further confirming applicability to a bacterial HTH regulator."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0QTR3 (FASR_MYCS2) is annotated with GO:0000976 'transcription cis-regulatory region binding' (C7/H5, IEA:TreeGrafter). The protein is experimentally characterized (PubMed:23721164, ECO:0000269) as a transcriptional activator that 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region' (C5/H3), which is a cis-regulatory region. The GO term definition (GO1) covers 'binding to a specific sequence of DNA that is part of a regulatory region that controls transcription,' consistent with operator binding. The evidence code for the GO annotation is computational (TreeGrafter), but the underlying function is experimentally supported.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable helix-turn-helix (HTH) DNA-binding domain motif (the region 'GYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLQRHVDNLVSGVRQALRTTTDNRQRLRAAVEAFFDFIEHDSQGYRLIFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWLNNDRPIDKDSAVEGTVQFAWGGLSHVPLTRS' shows the characteristic HTH fold). This eliminates options A (no transmembrane helices or Walker A/B ATP-binding motifs) and D (no glucosyltransferase catalytic residues or PSPG box). The small size (~219 aa), single HTH domain, and absence of eukaryotic-specific features (nuclear localization signals, activation domains, zinc fingers) indicate a bacterial-type transcriptional regulator, eliminating option B which is restricted to RNA polymerase II cis-regulatory regions (a eukaryotic-specific concept). The HTH domain in bacterial regulators classically binds operator/promoter sequences, i.e., cis-regulatory regions, supporting option C.",
    "missing_item_specific_fact": "None critical. The HTH domain identification and elimination of eukaryotic/transporter/glycosyltransferase options rely on general domain-architecture knowledge.",
    "reason": "A knowledgeable model can identify the HTH motif as a DNA-binding domain, recognize the overall architecture as bacterial (excluding RNA Pol II–specific option B), and eliminate transporter and glycosyltransferase options by absence of relevant structural features. The remaining option C (transcription cis-regulatory region binding) follows naturally from HTH-type bacterial transcriptional regulators binding operator/promoter sequences."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is excluded because RNA polymerase II is eukaryotic and the protein architecture is bacterial. Options A and D are excluded by absence of transmembrane/ATPase and glucosyltransferase structural features respectively. The GO term GO:0000976 even lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym (GO1), further confirming applicability to a bacterial HTH regulator."
  },
  "important_caveats": [
    "The GO annotation for the expected answer (GO:0000976) carries evidence code IEA:TreeGrafter (computational inference), not direct experimental evidence for this specific term, though the underlying operator-binding activity is experimentally supported (ECO:0000269).",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 219-aa sequence and general biological knowledge.",
    "Recognizing the HTH domain from a 219-aa sequence requires moderate expertise but falls within general molecular biology knowledge.",
    "The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 121 already includes GO:0000976."
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

**Accession:** `A0QTR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.364123+00:00.  

```json
"A0QTR3"
```

Source SHA-256: `8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.364123+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"O05858","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"23721164","source":"PubMed"}],"value":"Transcriptional activator that plays a central role in sensing mycobacterial long-chain fatty acids and regulating lipid biosynthesis (PubMed:23721164). Activates the expression of the genes encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products are involved in the fatty acid and mycolic acid biosynthesis (PubMed:23721164). Specifically binds to three conserved operator sequences present in the fas-acpS promoter region (By similarity). Essential for M.smegmatis viability (PubMed:23721164)"}]}
```

Source SHA-256: `8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:56.364123+00:00.  

```json
{"database":"GO","id":"GO:0000976","properties":[{"key":"GoTerm","value":"F:transcription cis-regulatory region binding"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)  
**Locator:** `lines 47-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-01T06:27:44.625980+00:00.  

```text
CC   -!- FUNCTION: Transcriptional activator that plays a central role in
CC       sensing mycobacterial long-chain fatty acids and regulating lipid
CC       biosynthesis (PubMed:23721164). Activates the expression of the genes
CC       encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl
CC       transferase (acpS), whose products are involved in the fatty acid and
CC       mycolic acid biosynthesis (PubMed:23721164). Specifically binds to
CC       three conserved operator sequences present in the fas-acpS promoter
CC       region (By similarity). Essential for M.smegmatis viability
CC       (PubMed:23721164). {ECO:0000250|UniProtKB:O05858,
CC       ECO:0000269|PubMed:23721164}.
```

Source SHA-256: `bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-01T06:27:44.625980+00:00.  

```text
DR   GO; GO:0000976; F:transcription cis-regulatory region binding; IEA:TreeGrafter.
```

Source SHA-256: `bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 7096-7115`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000976
name: transcription cis-regulatory region binding
namespace: molecular_function
alt_id: GO:0000975
alt_id: GO:0000984
alt_id: GO:0001017
alt_id: GO:0044212
def: "Binding to a specific sequence of DNA that is part of a regulatory region that controls transcription of that section of the DNA. The transcribed region might be described as a gene, cistron, or operon." [GOC:txnOH]
comment: Note that this term is meant to also capture non-specific binding to regulatory regions. Also, to minimize ambiguity in the use of the word "promoter" in GO, we have chosen the phrase "transcription regulatory region" to refer to all of the regulatory regions. Regulatory regions in the DNA which control initiation may include the "core promoter" where the basal transcription machinery binds, the "core promoter proximal region" where regulatory factors other than the basal machinery bind. There are also additional regulatory regions, in both the DNA and the RNA transcript, which regulate elongation or termination of transcription.
synonym: "bacterial-type RNA polymerase regulatory region DNA binding" NARROW []
synonym: "bacterial-type RNA polymerase transcription regulatory region sequence-specific DNA binding" NARROW []
synonym: "eubacterial-type RNA polymerase regulatory region DNA binding" NARROW []
synonym: "eubacterial-type RNA polymerase regulatory region sequence-specific DNA binding" NARROW []
synonym: "regulatory region DNA binding" BROAD []
synonym: "transcription regulatory region DNA binding" RELATED []
synonym: "transcription regulatory region sequence-specific DNA binding" EXACT []
is_a: GO:0001067 ! transcription regulatory region nucleic acid binding
is_a: GO:1990837 ! sequence-specific double-stranded DNA binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
