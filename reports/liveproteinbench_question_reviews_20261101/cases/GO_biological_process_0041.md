# GO_biological_process_0041

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — nuclear pore complex assembly

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASEAGGIGGGGGGGKIRTRRCHQGPVKPYQQGRPQHQGILSRVTESVKNIVPGWLQRYFNKSENACSCSPDADEVPPWPENREDEHAIYADENTNTDDGRITPDPAGSNTEEPSTTSTASNYPDVLTRPSLHRSHLNFSVLESPALHCQPSTSSAFPIGSSGFSLVKEIKDSTSQHDDDNISTTSGFSSRASEKDIAVSKNTSLPPLWSPEAERSHSLSQHTAISSKKPAFNLSAFGTLSTSLGNSSILKTSQLGDSPFYPGKTTYGGAAAAVRQNKVRSTPYQAPVRRQMKAKQLNAQSYGVTSSTARRILQSLEKMSSPLADAKRIPSAVSSPLNSPLDRSGIDNTVFQAKKEKVDSQYPPVQRLMTPKPVSIATNRTVYFKPSLTPSGDLRKTNQRIDKKNSTVDEKSISRQNREQESGFSYPNFSIPAANGLSSGVGGGGGKMRRERTHFVAPKPPENEEVEAPLLPQISLPISSSSLPTFSFSSPVTSASPSPVSSSQPLPNKVQMTSLGSTGSPVFTFSSPIVKSTQAAVLPPASIGFTFSVPLAKTEFSGSNSSSETVLSSSAQDITAVNSSSYKKRSAPCEDPFTPAKILREGSVLDILKTPGFASPKVDSPALQPTTTSSIVYTRPAISTFSSSGIEYGESLKAGSSWQCDTCLLQNKVTDNKCIACQAAKLPLKETAKQTGTGTPSKSDKPASTSGTGFGDKFKPAIGTWDCDTCLVQNKPEAVKCVACETPKPGTGVKRALTLTVASESPVTASSSTTVTTGTLGFGDKFKRPVGSWECPVCCVCNKAEDNRCVSCTSEKPGLVSASSSSPAPVSLSSGGCLGLDKFKKPEGSWDCEVCLVQNKADSAKCIACESAKPGTKSEFKGFGTSSSLNPAPSAFKFGIPSSSSGLSQTLTSTGNFKFGDQGGFKLGTSSDSGSTNTMNTNFKFSKPTGDFKFGVLSDSKPEEVKNDNKNDNFQFGSSSGLTNPASSAPFQFGVSTLGQQEKKEELPKSSPAGFSFGAGVNNPPNAAIDTTATSENKSGFNFGTLDTKSVSVTPFTYKTTEAKKEDAPATKGGFTFGKVGSSSLPSSSMFVLGRTEEKQQEPVTSTSLVFGKKADSEEPKCQPVFSFGNSEQTKDESSKPTFSFSVAKPSGKESEQLAKATFAFGNQTNTTTDQGAAKPVFSFLNSSSSSSSAPATSSSGGIFGSSTSSSNPPVAAFVFGQASNPVSSSAFGNAAESSTSQSLLFPQESEPATTSSTAPAASPFVFGTGASSNSVSSGFTFGATTTSSSSGSSFVFGTGHSAPSASPAFGANQTPTFGQSQGASQPNPPSFGSISSSTALFSAGSQPVPPPIFGTVSSSSQPPVFGQQPSQSAFGSGTANASSVFQFGSSTTNFNFTNNNPSGVFTFGASPSTPAASAQPSGSGVFSFSQSPASFTVGSNGKNMFSSSGTSVSGRKIKTAVRRKK

[Multiple Choices]
A. response to lead ion
B. cytosolic ribosome assembly
C. regulation of inflammatory response
D. nuclear pore complex assembly
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

> The supplied sequence matches the historical mouse Nup153 sequence, and that record annotates nuclear pore complex assembly (GO:0051292). The annotation is ISO:GO_Central, so it supports the key as an orthology-based inference, not as direct experimental evidence in the supplied record.

Citations as saved: [H6](#evidence-h6), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has extensive FG-repeat-rich low-complexity regions and cysteine-rich modules, a characteristic nucleoporin-like architecture. Of the choices, nuclear pore complex assembly is the one that fits this architecture; the other choices concern unrelated processes.


**Missing item-specific fact**

> The exact GO assignment of nuclear pore complex assembly is an annotation-level detail not established by sequence features alone; identifying that specific term with confidence would benefit from protein-specific functional or orthology annotation.


**Reason**

> Sequence architecture gives a meaningful basis to favor the sole nuclear-pore option, though it supports NPC involvement more directly than the specific assembly process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice D corresponds to the nucleoporin-like sequence features among the listed options.


### Important caveats

- The reviewer-only database evidence identifies the sequence as mouse Nup153; that identity was not supplied to the evaluated model.
- The GO annotation is computationally inferred by orthology, and the cited function description is transferred from another species; the supplied evidence does not establish direct experimental validation for this mouse sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has extensive FG-repeat-rich low-complexity regions and cysteine-rich modules, a characteristic nucleoporin-like architecture. Of the choices, nuclear pore complex assembly is the one that fits this architecture; the other choices concern unrelated processes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact GO assignment of nuclear pore complex assembly is an annotation-level detail not established by sequence features alone; identifying that specific term with confidence would benefit from protein-specific functional or orthology annotation.",
    "reason": "Sequence architecture gives a meaningful basis to favor the sole nuclear-pore option, though it supports NPC involvement more directly than the specific assembly process."
  },
  "case_id": "GO_biological_process_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical mouse Nup153 sequence, and that record annotates nuclear pore complex assembly (GO:0051292). The annotation is ISO:GO_Central, so it supports the key as an orthology-based inference, not as direct experimental evidence in the supplied record."
  },
  "important_caveats": [
    "The reviewer-only database evidence identifies the sequence as mouse Nup153; that identity was not supplied to the evaluated model.",
    "The GO annotation is computationally inferred by orthology, and the cited function description is transferred from another species; the supplied evidence does not establish direct experimental validation for this mouse sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice D corresponds to the nucleoporin-like sequence features among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical mouse Nup153 sequence, and that record annotates nuclear pore complex assembly (GO:0051292). The annotation is ISO:GO_Central, so it supports the key as an orthology-based inference, not as direct experimental evidence in the supplied record.",
    "evidence_ids": ["H6", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has extensive FG-repeat-rich low-complexity regions and cysteine-rich modules, a characteristic nucleoporin-like architecture. Of the choices, nuclear pore complex assembly is the one that fits this architecture; the other choices concern unrelated processes.",
    "missing_item_specific_fact": "The exact GO assignment of nuclear pore complex assembly is an annotation-level detail not established by sequence features alone; identifying that specific term with confidence would benefit from protein-specific functional or orthology annotation.",
    "reason": "Sequence architecture gives a meaningful basis to favor the sole nuclear-pore option, though it supports NPC involvement more directly than the specific assembly process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice D corresponds to the nucleoporin-like sequence features among the listed options."
  },
  "important_caveats": [
    "The reviewer-only database evidence identifies the sequence as mouse Nup153; that identity was not supplied to the evaluated model.",
    "The GO annotation is computationally inferred by orthology, and the cited function description is transferred from another species; the supplied evidence does not establish direct experimental validation for this mouse sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence is confirmed as UniProt E9Q3G8 (Nup153_MOUSE, 'Nuclear pore complex protein Nup153'). The UniProt entry directly annotates GO:0051292 'nuclear pore complex assembly' (ISO:GO_Central), and the protein's recommended name and function comment explicitly identify it as a component of the nuclear pore complex. The expected answer D matches this annotation exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous FG (Phe-Gly) dipeptide repeats scattered throughout the C-terminal half (e.g., FKFG, FGTGASS, FGNQT, FGQAS, FGATTT, FGTGHS, FGANQ, FGQSQ, FGSIS, FGTVS, FGQQP, FGSGT, FGSST, FGASP, FGSFS) and multiple C2H2-type zinc finger motifs (CDTCLLQNK, CPVCCVCNKA, CEVCLVQNK, CACETPK, CIACESAK). FG repeats are the defining structural hallmark of nucleoporins, the protein building blocks of the nuclear pore complex. Multiple zinc fingers in a large (~1462 aa) FG-repeat-containing protein are characteristic of Nup153 specifically. Among the four options, only 'nuclear pore complex assembly' (D) is compatible with a nucleoporin; lead ion response, cytosolic ribosome assembly, and regulation of inflammatory response are functionally unrelated to FG-repeat/zinc-finger nucleoporin architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A biologist familiar with nucleoporin structural biology can recognize the FG-repeat pattern and zinc finger array as hallmarks of a nucleoporin, then eliminate the three clearly unrelated options (A, B, C) to arrive at D. This is a sequence-feature-to-function inference grounded in well-established protein-family signatures, not a lookup of a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (response to lead ion, cytosolic ribosome assembly, regulation of inflammatory response) have no plausible mechanistic connection to a protein bearing extensive FG repeats and multiple zinc finger domains. Only option D aligns with nucleoporin biology. No other option is defensible given the sequence features.


### Important caveats

- The GO:0051292 annotation carries evidence code ISO:GO_Central (inferred by similarity to human Nup153, P49790), not direct experimental evidence for the mouse protein specifically.
- Nup153 is also annotated with 'nucleocytoplasmic transport' (GO:0006913) and 'protein import into nucleus' (GO:0006606), but neither appears as a distractor, so the single correct option among those given is unambiguous.
- The FG-repeat count and zinc-finger spacing in the sequence are consistent with Nup153 but a model must recognize the pattern without exact database lookup; the reasoning path is supported but requires familiarity with nucleoporin signatures.
- All reviewer evidence is from the current or archived UniProt snapshot; the exact author data-construction date and source snapshot are unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous FG (Phe-Gly) dipeptide repeats scattered throughout the C-terminal half (e.g., FKFG, FGTGASS, FGNQT, FGQAS, FGATTT, FGTGHS, FGANQ, FGQSQ, FGSIS, FGTVS, FGQQP, FGSGT, FGSST, FGASP, FGSFS) and multiple C2H2-type zinc finger motifs (CDTCLLQNK, CPVCCVCNKA, CEVCLVQNK, CACETPK, CIACESAK). FG repeats are the defining structural hallmark of nucleoporins, the protein building blocks of the nuclear pore complex. Multiple zinc fingers in a large (~1462 aa) FG-repeat-containing protein are characteristic of Nup153 specifically. Among the four options, only 'nuclear pore complex assembly' (D) is compatible with a nucleoporin; lead ion response, cytosolic ribosome assembly, and regulation of inflammatory response are functionally unrelated to FG-repeat/zinc-finger nucleoporin architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A biologist familiar with nucleoporin structural biology can recognize the FG-repeat pattern and zinc finger array as hallmarks of a nucleoporin, then eliminate the three clearly unrelated options (A, B, C) to arrive at D. This is a sequence-feature-to-function inference grounded in well-established protein-family signatures, not a lookup of a specific database annotation."
  },
  "case_id": "GO_biological_process_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence is confirmed as UniProt E9Q3G8 (Nup153_MOUSE, 'Nuclear pore complex protein Nup153'). The UniProt entry directly annotates GO:0051292 'nuclear pore complex assembly' (ISO:GO_Central), and the protein's recommended name and function comment explicitly identify it as a component of the nuclear pore complex. The expected answer D matches this annotation exactly."
  },
  "important_caveats": [
    "The GO:0051292 annotation carries evidence code ISO:GO_Central (inferred by similarity to human Nup153, P49790), not direct experimental evidence for the mouse protein specifically.",
    "Nup153 is also annotated with 'nucleocytoplasmic transport' (GO:0006913) and 'protein import into nucleus' (GO:0006606), but neither appears as a distractor, so the single correct option among those given is unambiguous.",
    "The FG-repeat count and zinc-finger spacing in the sequence are consistent with Nup153 but a model must recognize the pattern without exact database lookup; the reasoning path is supported but requires familiarity with nucleoporin signatures.",
    "All reviewer evidence is from the current or archived UniProt snapshot; the exact author data-construction date and source snapshot are unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (response to lead ion, cytosolic ribosome assembly, regulation of inflammatory response) have no plausible mechanistic connection to a protein bearing extensive FG repeats and multiple zinc finger domains. Only option D aligns with nucleoporin biology. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence is confirmed as UniProt E9Q3G8 (Nup153_MOUSE, 'Nuclear pore complex protein Nup153'). The UniProt entry directly annotates GO:0051292 'nuclear pore complex assembly' (ISO:GO_Central), and the protein's recommended name and function comment explicitly identify it as a component of the nuclear pore complex. The expected answer D matches this annotation exactly.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous FG (Phe-Gly) dipeptide repeats scattered throughout the C-terminal half (e.g., FKFG, FGTGASS, FGNQT, FGQAS, FGATTT, FGTGHS, FGANQ, FGQSQ, FGSIS, FGTVS, FGQQP, FGSGT, FGSST, FGASP, FGSFS) and multiple C2H2-type zinc finger motifs (CDTCLLQNK, CPVCCVCNKA, CEVCLVQNK, CACETPK, CIACESAK). FG repeats are the defining structural hallmark of nucleoporins, the protein building blocks of the nuclear pore complex. Multiple zinc fingers in a large (~1462 aa) FG-repeat-containing protein are characteristic of Nup153 specifically. Among the four options, only 'nuclear pore complex assembly' (D) is compatible with a nucleoporin; lead ion response, cytosolic ribosome assembly, and regulation of inflammatory response are functionally unrelated to FG-repeat/zinc-finger nucleoporin architecture.",
    "missing_item_specific_fact": "",
    "reason": "A biologist familiar with nucleoporin structural biology can recognize the FG-repeat pattern and zinc finger array as hallmarks of a nucleoporin, then eliminate the three clearly unrelated options (A, B, C) to arrive at D. This is a sequence-feature-to-function inference grounded in well-established protein-family signatures, not a lookup of a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (response to lead ion, cytosolic ribosome assembly, regulation of inflammatory response) have no plausible mechanistic connection to a protein bearing extensive FG repeats and multiple zinc finger domains. Only option D aligns with nucleoporin biology. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:0051292 annotation carries evidence code ISO:GO_Central (inferred by similarity to human Nup153, P49790), not direct experimental evidence for the mouse protein specifically.",
    "Nup153 is also annotated with 'nucleocytoplasmic transport' (GO:0006913) and 'protein import into nucleus' (GO:0006606), but neither appears as a distractor, so the single correct option among those given is unambiguous.",
    "The FG-repeat count and zinc-finger spacing in the sequence are consistent with Nup153 but a model must recognize the pattern without exact database lookup; the reasoning path is supported but requires familiarity with nucleoporin signatures.",
    "All reviewer evidence is from the current or archived UniProt snapshot; the exact author data-construction date and source snapshot are unknown."
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

**Accession:** `E9Q3G8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 108. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3G8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:07.166127+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"153 kDa nucleoporin"}},{"fullName":{"value":"Nucleoporin Nup153"}}],"recommendedName":{"fullName":{"value":"Nuclear pore complex protein Nup153"}}}
```

Source SHA-256: `ab17eb27867a9b9705e8ee5aab15af52a3372820947fb64315598a4d75f696a6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3G8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:07.166127+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P49790","source":"UniProtKB"}],"value":"Component of the nuclear pore complex (NPC), a complex required for the trafficking across the nuclear envelope. Functions as a scaffolding element in the nuclear phase of the NPC essential for normal nucleocytoplasmic transport of proteins and mRNAs. Involved in the quality control and retention of unspliced mRNAs in the nucleus; in association with TPR, regulates the nuclear export of unspliced mRNA species bearing constitutive transport element (CTE) in a NXF1- and KHDRBS1-independent manner. Mediates TPR anchoring to the nuclear membrane at NPC. The repeat-containing domain may be involved in anchoring other components of the NPC to the pore membrane. Possible DNA-binding subunit of the nuclear pore complex (NPC)"}]}
```

Source SHA-256: `ab17eb27867a9b9705e8ee5aab15af52a3372820947fb64315598a4d75f696a6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3G8.json)  
**Locator:** `/uniProtKBCrossReferences/80`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:07.166127+00:00.  

```json
{"database":"GO","id":"GO:0051292","properties":[{"key":"GoTerm","value":"P:nuclear pore complex assembly"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `ab17eb27867a9b9705e8ee5aab15af52a3372820947fb64315598a4d75f696a6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3G8?format=txt&versions=108)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 108 / 1.  
**Retrieved:** 2026-11-02T04:28:10.539906+00:00.  

```text
ID   NU153_MOUSE             Reviewed;        1462 AA.
AC   E9Q3G8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-APR-2011, sequence version 1.
DT   28-JAN-2026, entry version 108.
DE   RecName: Full=Nuclear pore complex protein Nup153;
DE   AltName: Full=153 kDa nucleoporin;
DE   AltName: Full=Nucleoporin Nup153;
GN   Name=Nup153;
OS   Mus musculus (Mouse).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Mus; Mus.
OX   NCBI_TaxID=10090 {ECO:0000312|Proteomes:UP000000589};
```

Source SHA-256: `2621d3bcc6ebd205d306166e3ca90bad9a7ba29993468087d17d98bac2ed53a2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3G8?format=txt&versions=108)  
**Locator:** `lines 64-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 108 / 1.  
**Retrieved:** 2026-11-02T04:28:10.539906+00:00.  

```text
CC   -!- FUNCTION: Component of the nuclear pore complex (NPC), a complex
CC       required for the trafficking across the nuclear envelope. Functions as
CC       a scaffolding element in the nuclear phase of the NPC essential for
CC       normal nucleocytoplasmic transport of proteins and mRNAs. Involved in
CC       the quality control and retention of unspliced mRNAs in the nucleus; in
CC       association with TPR, regulates the nuclear export of unspliced mRNA
CC       species bearing constitutive transport element (CTE) in a NXF1- and
CC       KHDRBS1-independent manner. Mediates TPR anchoring to the nuclear
CC       membrane at NPC. The repeat-containing domain may be involved in
CC       anchoring other components of the NPC to the pore membrane. Possible
CC       DNA-binding subunit of the nuclear pore complex (NPC).
CC       {ECO:0000250|UniProtKB:P49790}.
```

Source SHA-256: `2621d3bcc6ebd205d306166e3ca90bad9a7ba29993468087d17d98bac2ed53a2`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3G8?format=txt&versions=108)  
**Locator:** `lines 193-193`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 108 / 1.  
**Retrieved:** 2026-11-02T04:28:10.539906+00:00.  

```text
DR   GO; GO:0051292; P:nuclear pore complex assembly; ISO:GO_Central.
```

Source SHA-256: `2621d3bcc6ebd205d306166e3ca90bad9a7ba29993468087d17d98bac2ed53a2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
