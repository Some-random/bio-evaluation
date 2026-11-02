# GO_biological_process_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — DNA-templated transcription

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTHDLNDTLIFVKVVEQGSFIAAANSLGLPKTTVSRKVQELETRLGARLLHRTTRRIGLTEAGAVYHEHCQRIARELEEAESAVGQLQSGPRGWLRFTVPYSLGITWIAPLLGEFHAQYPEIQLDMHLGNEKLDLIGGEADLALRVGALPDSNLVARKLGSLRTQVFASPSYIERYGEPLHPDELQFHRTLALRKNRNVHNNRFFWSLSDGSDVREFPVNPLMVANDPAALNGAVLCGEGLLLTGDVMAKPFVQSGMVRRVLAGWTGPEVDFNAVFAGGRLVSPKVRAFVDFLVTRLNFDADYMMAQCPARLAAQRANGDAEVEVEVEAELRAEGKRILEKATA

[Multiple Choices]
A. cellular response to osmotic stress
B. chorismate biosynthetic process
C. DNA-templated transcription
D. Rho-activating G protein-coupled receptor signaling pathway
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

> The supplied sequence exactly matches the referenced protein. Its annotation describes a transcriptional regulator that regulates virulence-related gene expression and binds target promoters; DNA-templated transcription is therefore supported. The specific GO annotation is computationally assigned (IEA:TreeGrafter), while the functional evidence cited for transcriptional regulation is experimental.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble bacterial protein, making the GPCR signaling option an implausible fit, but the supplied sequence and context do not establish whether its biological role is transcriptional regulation, osmotic-stress response, or another process.


**Missing item-specific fact**

> The protein-specific functional identification as a transcriptional regulator, or equivalent homology/experimental evidence connecting this sequence to transcriptional regulation.


**Reason**

> The key is supported by reviewer-only protein-specific annotation and functional evidence. Those facts are not supplied in the question, and generic sequence features alone do not distinguish the remaining biological-process choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific evidence supports transcriptional regulation, aligning with choice C; none of the other options is comparably supported.


### Important caveats

- The sequence match establishes that the cited annotation concerns this protein, but the author’s exact source snapshot is unknown.
- The GO term assignment is computational; the cited experimental function supports transcriptional regulation but does not itself establish that this is the protein’s sole or primary process.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble bacterial protein, making the GPCR signaling option an implausible fit, but the supplied sequence and context do not establish whether its biological role is transcriptional regulation, osmotic-stress response, or another process.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as a transcriptional regulator, or equivalent homology/experimental evidence connecting this sequence to transcriptional regulation.",
    "reason": "The key is supported by reviewer-only protein-specific annotation and functional evidence. Those facts are not supplied in the question, and generic sequence features alone do not distinguish the remaining biological-process choices."
  },
  "case_id": "GO_biological_process_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced protein. Its annotation describes a transcriptional regulator that regulates virulence-related gene expression and binds target promoters; DNA-templated transcription is therefore supported. The specific GO annotation is computationally assigned (IEA:TreeGrafter), while the functional evidence cited for transcriptional regulation is experimental."
  },
  "important_caveats": [
    "The sequence match establishes that the cited annotation concerns this protein, but the author’s exact source snapshot is unknown.",
    "The GO term assignment is computational; the cited experimental function supports transcriptional regulation but does not itself establish that this is the protein’s sole or primary process."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports transcriptional regulation, aligning with choice C; none of the other options is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced protein. Its annotation describes a transcriptional regulator that regulates virulence-related gene expression and binds target promoters; DNA-templated transcription is therefore supported. The specific GO annotation is computationally assigned (IEA:TreeGrafter), while the functional evidence cited for transcriptional regulation is experimental.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble bacterial protein, making the GPCR signaling option an implausible fit, but the supplied sequence and context do not establish whether its biological role is transcriptional regulation, osmotic-stress response, or another process.",
    "missing_item_specific_fact": "The protein-specific functional identification as a transcriptional regulator, or equivalent homology/experimental evidence connecting this sequence to transcriptional regulation.",
    "reason": "The key is supported by reviewer-only protein-specific annotation and functional evidence. Those facts are not supplied in the question, and generic sequence features alone do not distinguish the remaining biological-process choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports transcriptional regulation, aligning with choice C; none of the other options is comparably supported."
  },
  "important_caveats": [
    "The sequence match establishes that the cited annotation concerns this protein, but the author’s exact source snapshot is unknown.",
    "The GO term assignment is computational; the cited experimental function supports transcriptional regulation but does not itself establish that this is the protein’s sole or primary process."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (A0A0H2XAU1, XC_2801 from Xanthomonas campestris pv. campestris 8004) is annotated as an 'HTH-type transcriptional regulator' (C4, H1). Experimental evidence (ECO:0000269, PubMed:25329577; C5, H3) demonstrates it 'directly or indirectly regulates the expression of virulence-related genes' and 'binds to the promoter of the target genes.' The GO annotation GO:0006351 (DNA-templated transcription) is present but carries an IEA:TreeGrafter evidence code (C6, H4), i.e., computational inference rather than direct experimental GO curation. Nevertheless, the underlying experimental data clearly establish the protein as a transcriptional regulator that binds DNA promoters, making the assignment to DNA-templated transcription well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option D (Rho-activating GPCR signaling) is a eukaryotic pathway involving Rho-family GTPases (RhoA, Cdc42, Rac1) and 7TM GPCRs; the sequence is from a bacterium (Xanthomonas) with no transmembrane helices or GPCR architecture, so D is eliminable by general knowledge. Option B (chorismate biosynthetic process) requires specific shikimate-pathway enzymes (e.g., DAHP synthase, shikimate dehydrogenase, chorismate synthase) with distinctive catalytic folds; the sequence lacks these enzyme signatures. Between A and C, the C-terminal region of the sequence contains features consistent with a helix-turn-helix (HTH) DNA-binding domain, a motif canonically associated with transcriptional regulation. A transcriptional regulator's primary molecular biological process is DNA-templated transcription by definition, whereas 'cellular response to osmotic stress' (A) is a broad stimulus-response category not specifically indicated by the sequence. Thus, recognizing the HTH-like domain and applying the definitional link between transcription factors and transcription supports C.


**Missing item-specific fact**

> The YajQ-family HTH domain is less canonical than textbook HTH motifs (e.g., LacI, homeodomain), so confident identification from raw sequence alone is non-trivial. Knowledge that this specific protein is a cyclic di-GMP-responsive transcriptional regulator would strengthen the case but is not strictly necessary given the HTH reasoning and distractor elimination.


**Reason**

> A model with general biological knowledge can eliminate D (eukaryotic pathway in a bacterium) and B (no shikimate-pathway enzyme features), and can plausibly identify HTH-like structural features in the C-terminal region to reason toward transcription. The remaining choice between A and C is resolved by the definitional link between HTH transcription factors and DNA-templated transcription, and by the absence of osmotic-sensor or compatible-solute-transport features. The reasoning chain is concrete though the HTH identification in this non-canonical family adds difficulty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is clearly inapplicable (eukaryotic GPCR/Rho pathway in a bacterium). B is clearly inapplicable (no shikimate-pathway catalytic domains). A is a broad stress-response category not specifically supported by the sequence. C is the single best-supported option given the HTH transcription-factor identity.


### Important caveats

- The GO:0006351 annotation carries evidence code IEA:TreeGrafter (computational), not direct experimental GO curation. The experimental evidence (PubMed:25329577) supports the transcriptional-regulator function but the GO term assignment itself is inferred.
- The YajQ-family HTH domain is structurally distinct from classic HTH motifs; sequence-based recognition without prior training on YajQ proteins is challenging.
- The protein's biological role is specifically as a cyclic di-GMP effector regulating virulence genes; 'DNA-templated transcription' is the correct GO biological process but is a very broad term (GO:0006351) that encompasses all transcription.
- All reviewer evidence is from UniProt entries retrieved in 2026; the author's original data snapshot is unknown, though the sequence matches exactly across checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option D (Rho-activating GPCR signaling) is a eukaryotic pathway involving Rho-family GTPases (RhoA, Cdc42, Rac1) and 7TM GPCRs; the sequence is from a bacterium (Xanthomonas) with no transmembrane helices or GPCR architecture, so D is eliminable by general knowledge. Option B (chorismate biosynthetic process) requires specific shikimate-pathway enzymes (e.g., DAHP synthase, shikimate dehydrogenase, chorismate synthase) with distinctive catalytic folds; the sequence lacks these enzyme signatures. Between A and C, the C-terminal region of the sequence contains features consistent with a helix-turn-helix (HTH) DNA-binding domain, a motif canonically associated with transcriptional regulation. A transcriptional regulator's primary molecular biological process is DNA-templated transcription by definition, whereas 'cellular response to osmotic stress' (A) is a broad stimulus-response category not specifically indicated by the sequence. Thus, recognizing the HTH-like domain and applying the definitional link between transcription factors and transcription supports C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The YajQ-family HTH domain is less canonical than textbook HTH motifs (e.g., LacI, homeodomain), so confident identification from raw sequence alone is non-trivial. Knowledge that this specific protein is a cyclic di-GMP-responsive transcriptional regulator would strengthen the case but is not strictly necessary given the HTH reasoning and distractor elimination.",
    "reason": "A model with general biological knowledge can eliminate D (eukaryotic pathway in a bacterium) and B (no shikimate-pathway enzyme features), and can plausibly identify HTH-like structural features in the C-terminal region to reason toward transcription. The remaining choice between A and C is resolved by the definitional link between HTH transcription factors and DNA-templated transcription, and by the absence of osmotic-sensor or compatible-solute-transport features. The reasoning chain is concrete though the HTH identification in this non-canonical family adds difficulty."
  },
  "case_id": "GO_biological_process_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein (A0A0H2XAU1, XC_2801 from Xanthomonas campestris pv. campestris 8004) is annotated as an 'HTH-type transcriptional regulator' (C4, H1). Experimental evidence (ECO:0000269, PubMed:25329577; C5, H3) demonstrates it 'directly or indirectly regulates the expression of virulence-related genes' and 'binds to the promoter of the target genes.' The GO annotation GO:0006351 (DNA-templated transcription) is present but carries an IEA:TreeGrafter evidence code (C6, H4), i.e., computational inference rather than direct experimental GO curation. Nevertheless, the underlying experimental data clearly establish the protein as a transcriptional regulator that binds DNA promoters, making the assignment to DNA-templated transcription well-supported."
  },
  "important_caveats": [
    "The GO:0006351 annotation carries evidence code IEA:TreeGrafter (computational), not direct experimental GO curation. The experimental evidence (PubMed:25329577) supports the transcriptional-regulator function but the GO term assignment itself is inferred.",
    "The YajQ-family HTH domain is structurally distinct from classic HTH motifs; sequence-based recognition without prior training on YajQ proteins is challenging.",
    "The protein's biological role is specifically as a cyclic di-GMP effector regulating virulence genes; 'DNA-templated transcription' is the correct GO biological process but is a very broad term (GO:0006351) that encompasses all transcription.",
    "All reviewer evidence is from UniProt entries retrieved in 2026; the author's original data snapshot is unknown, though the sequence matches exactly across checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly inapplicable (eukaryotic GPCR/Rho pathway in a bacterium). B is clearly inapplicable (no shikimate-pathway catalytic domains). A is a broad stress-response category not specifically supported by the sequence. C is the single best-supported option given the HTH transcription-factor identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (A0A0H2XAU1, XC_2801 from Xanthomonas campestris pv. campestris 8004) is annotated as an 'HTH-type transcriptional regulator' (C4, H1). Experimental evidence (ECO:0000269, PubMed:25329577; C5, H3) demonstrates it 'directly or indirectly regulates the expression of virulence-related genes' and 'binds to the promoter of the target genes.' The GO annotation GO:0006351 (DNA-templated transcription) is present but carries an IEA:TreeGrafter evidence code (C6, H4), i.e., computational inference rather than direct experimental GO curation. Nevertheless, the underlying experimental data clearly establish the protein as a transcriptional regulator that binds DNA promoters, making the assignment to DNA-templated transcription well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option D (Rho-activating GPCR signaling) is a eukaryotic pathway involving Rho-family GTPases (RhoA, Cdc42, Rac1) and 7TM GPCRs; the sequence is from a bacterium (Xanthomonas) with no transmembrane helices or GPCR architecture, so D is eliminable by general knowledge. Option B (chorismate biosynthetic process) requires specific shikimate-pathway enzymes (e.g., DAHP synthase, shikimate dehydrogenase, chorismate synthase) with distinctive catalytic folds; the sequence lacks these enzyme signatures. Between A and C, the C-terminal region of the sequence contains features consistent with a helix-turn-helix (HTH) DNA-binding domain, a motif canonically associated with transcriptional regulation. A transcriptional regulator's primary molecular biological process is DNA-templated transcription by definition, whereas 'cellular response to osmotic stress' (A) is a broad stimulus-response category not specifically indicated by the sequence. Thus, recognizing the HTH-like domain and applying the definitional link between transcription factors and transcription supports C.",
    "missing_item_specific_fact": "The YajQ-family HTH domain is less canonical than textbook HTH motifs (e.g., LacI, homeodomain), so confident identification from raw sequence alone is non-trivial. Knowledge that this specific protein is a cyclic di-GMP-responsive transcriptional regulator would strengthen the case but is not strictly necessary given the HTH reasoning and distractor elimination.",
    "reason": "A model with general biological knowledge can eliminate D (eukaryotic pathway in a bacterium) and B (no shikimate-pathway enzyme features), and can plausibly identify HTH-like structural features in the C-terminal region to reason toward transcription. The remaining choice between A and C is resolved by the definitional link between HTH transcription factors and DNA-templated transcription, and by the absence of osmotic-sensor or compatible-solute-transport features. The reasoning chain is concrete though the HTH identification in this non-canonical family adds difficulty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly inapplicable (eukaryotic GPCR/Rho pathway in a bacterium). B is clearly inapplicable (no shikimate-pathway catalytic domains). A is a broad stress-response category not specifically supported by the sequence. C is the single best-supported option given the HTH transcription-factor identity."
  },
  "important_caveats": [
    "The GO:0006351 annotation carries evidence code IEA:TreeGrafter (computational), not direct experimental GO curation. The experimental evidence (PubMed:25329577) supports the transcriptional-regulator function but the GO term assignment itself is inferred.",
    "The YajQ-family HTH domain is structurally distinct from classic HTH motifs; sequence-based recognition without prior training on YajQ proteins is challenging.",
    "The protein's biological role is specifically as a cyclic di-GMP effector regulating virulence genes; 'DNA-templated transcription' is the correct GO biological process but is a very broad term (GO:0006351) that encompasses all transcription.",
    "All reviewer evidence is from UniProt entries retrieved in 2026; the author's original data snapshot is unknown, though the sequence matches exactly across checked versions."
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

**Accession:** `A0A0H2XAU1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 52. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2XAU1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:08.022572+00:00.  

```json
"A0A0H2XAU1"
```

Source SHA-256: `b75adc0c6efc0702465f433f4be9eb9a440d34557935e8293dc1a2fa6dbd37d0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2XAU1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:08.022572+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional regulator XC_2801"}}}
```

Source SHA-256: `b75adc0c6efc0702465f433f4be9eb9a440d34557935e8293dc1a2fa6dbd37d0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2XAU1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:08.022572+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25329577","source":"PubMed"}],"value":"Transcriptional regulator that directly or indirectly regulates the expression of virulence-related genes, including flhB, aaeA, fliL and flgG (PubMed:25329577). Binds to the promoter of the target genes only in the presence of XC_3703 (PubMed:25329577)"}]}
```

Source SHA-256: `b75adc0c6efc0702465f433f4be9eb9a440d34557935e8293dc1a2fa6dbd37d0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2XAU1.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:08.022572+00:00.  

```json
{"database":"GO","id":"GO:0006351","properties":[{"key":"GoTerm","value":"P:DNA-templated transcription"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `b75adc0c6efc0702465f433f4be9eb9a440d34557935e8293dc1a2fa6dbd37d0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2XAU1?format=txt&versions=52)  
**Locator:** `lines 1-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:24:10.817174+00:00.  

```text
ID   R2801_XANC8             Reviewed;         344 AA.
AC   A0A0H2XAU1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 52.
DE   RecName: Full=HTH-type transcriptional regulator XC_2801 {ECO:0000305};
GN   OrderedLocusNames=XC_2801 {ECO:0000312|EMBL:AAY49850.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `f97eefa003cd1d83c4ce23905ffa935218f47efb464b690425bc6c7e600189a5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2XAU1?format=txt&versions=52)  
**Locator:** `lines 33-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:24:10.817174+00:00.  

```text
CC   -!- FUNCTION: Transcriptional regulator that directly or indirectly
CC       regulates the expression of virulence-related genes, including flhB,
CC       aaeA, fliL and flgG (PubMed:25329577). Binds to the promoter of the
CC       target genes only in the presence of XC_3703 (PubMed:25329577).
CC       {ECO:0000269|PubMed:25329577}.
```

Source SHA-256: `f97eefa003cd1d83c4ce23905ffa935218f47efb464b690425bc6c7e600189a5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2XAU1?format=txt&versions=52)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:24:10.817174+00:00.  

```text
DR   GO; GO:0006351; P:DNA-templated transcription; IEA:TreeGrafter.
```

Source SHA-256: `f97eefa003cd1d83c4ce23905ffa935218f47efb464b690425bc6c7e600189a5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
