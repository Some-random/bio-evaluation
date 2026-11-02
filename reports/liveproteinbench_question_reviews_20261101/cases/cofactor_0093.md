# cofactor_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASEAGGIGGGGGGGKIRTRRCHQGPVKPYQQGRPQHQGILSRVTESVKNIVPGWLQRYFNKSENACSCSPDADEVPPWPENREDEHAIYADENTNTDDGRITPDPAGSNTEEPSTTSTASNYPDVLTRPSLHRSHLNFSVLESPALHCQPSTSSAFPIGSSGFSLVKEIKDSTSQHDDDNISTTSGFSSRASEKDIAVSKNTSLPPLWSPEAERSHSLSQHTAISSKKPAFNLSAFGTLSTSLGNSSILKTSQLGDSPFYPGKTTYGGAAAAVRQNKVRSTPYQAPVRRQMKAKQLNAQSYGVTSSTARRILQSLEKMSSPLADAKRIPSAVSSPLNSPLDRSGIDNTVFQAKKEKVDSQYPPVQRLMTPKPVSIATNRTVYFKPSLTPSGDLRKTNQRIDKKNSTVDEKSISRQNREQESGFSYPNFSIPAANGLSSGVGGGGGKMRRERTHFVAPKPPENEEVEAPLLPQISLPISSSSLPTFSFSSPVTSASPSPVSSSQPLPNKVQMTSLGSTGSPVFTFSSPIVKSTQAAVLPPASIGFTFSVPLAKTEFSGSNSSSETVLSSSAQDITAVNSSSYKKRSAPCEDPFTPAKILREGSVLDILKTPGFASPKVDSPALQPTTTSSIVYTRPAISTFSSSGIEYGESLKAGSSWQCDTCLLQNKVTDNKCIACQAAKLPLKETAKQTGTGTPSKSDKPASTSGTGFGDKFKPAIGTWDCDTCLVQNKPEAVKCVACETPKPGTGVKRALTLTVASESPVTASSSTTVTTGTLGFGDKFKRPVGSWECPVCCVCNKAEDNRCVSCTSEKPGLVSASSSSPAPVSLSSGGCLGLDKFKKPEGSWDCEVCLVQNKADSAKCIACESAKPGTKSEFKGFGTSSSLNPAPSAFKFGIPSSSSGLSQTLTSTGNFKFGDQGGFKLGTSSDSGSTNTMNTNFKFSKPTGDFKFGVLSDSKPEEVKNDNKNDNFQFGSSSGLTNPASSAPFQFGVSTLGQQEKKEELPKSSPAGFSFGAGVNNPPNAAIDTTATSENKSGFNFGTLDTKSVSVTPFTYKTTEAKKEDAPATKGGFTFGKVGSSSLPSSSMFVLGRTEEKQQEPVTSTSLVFGKKADSEEPKCQPVFSFGNSEQTKDESSKPTFSFSVAKPSGKESEQLAKATFAFGNQTNTTTDQGAAKPVFSFLNSSSSSSSAPATSSSGGIFGSSTSSSNPPVAAFVFGQASNPVSSSAFGNAAESSTSQSLLFPQESEPATTSSTAPAASPFVFGTGASSNSVSSGFTFGATTTSSSSGSSFVFGTGHSAPSASPAFGANQTPTFGQSQGASQPNPPSFGSISSSTALFSAGSQPVPPPIFGTVSSSSQPPVFGQQPSQSAFGSGTANASSVFQFGSSTTNFNFTNNNPSGVFTFGASPSTPAASAQPSGSGVFSFSQSPASFTVGSNGKNMFSSSGTSVSGRKIKTAVRRKK

[Multiple Choices]
A. Ca(2+)
B. Mg(2+)
C. Zn(2+)
D. heme b
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

### Expected-answer support: uncertain

> The exact-matched UniProt entry annotates Zn(2+) and says the protein binds at least four zinc ions per subunit. That supports zinc binding, but does not establish that zinc is required for catalytic activity; the entry identifies the protein as nucleoporin Nup153, not an enzyme.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated cysteine-rich motifs, including multiple closely spaced cysteines in tandem regions. Such motifs are characteristic of zinc-coordinating structural domains and meaningfully favor Zn(2+) over Ca(2+), Mg(2+), or heme b as the bound cofactor.


**Missing item-specific fact**

> The sequence alone does not establish that zinc is required for catalytic activity, or provide experimental evidence for that specific requirement.


**Reason**

> The repeated cysteine-rich sequence patterns provide a concrete biological basis for predicting zinc binding. That supports distinguishing Zn as a cofactor, but not the question's more specific catalytic-activity premise.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence gives a distinctive basis for zinc binding among the listed options. The ambiguity is instead whether the question means zinc binding generally or a cofactor required for catalysis.


### Important caveats

- Reviewer-only UniProt evidence is not information supplied to the original model.
- The current and archived UniProt records match the supplied sequence, but the cited cofactor annotation does not by itself establish experimental necessity for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated cysteine-rich motifs, including multiple closely spaced cysteines in tandem regions. Such motifs are characteristic of zinc-coordinating structural domains and meaningfully favor Zn(2+) over Ca(2+), Mg(2+), or heme b as the bound cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish that zinc is required for catalytic activity, or provide experimental evidence for that specific requirement.",
    "reason": "The repeated cysteine-rich sequence patterns provide a concrete biological basis for predicting zinc binding. That supports distinguishing Zn as a cofactor, but not the question's more specific catalytic-activity premise."
  },
  "case_id": "cofactor_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "cannot_determine",
    "reason": "The exact-matched UniProt entry annotates Zn(2+) and says the protein binds at least four zinc ions per subunit. That supports zinc binding, but does not establish that zinc is required for catalytic activity; the entry identifies the protein as nucleoporin Nup153, not an enzyme."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence is not information supplied to the original model.",
    "The current and archived UniProt records match the supplied sequence, but the cited cofactor annotation does not by itself establish experimental necessity for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence gives a distinctive basis for zinc binding among the listed options. The ambiguity is instead whether the question means zinc binding generally or a cofactor required for catalysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0093",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The exact-matched UniProt entry annotates Zn(2+) and says the protein binds at least four zinc ions per subunit. That supports zinc binding, but does not establish that zinc is required for catalytic activity; the entry identifies the protein as nucleoporin Nup153, not an enzyme.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated cysteine-rich motifs, including multiple closely spaced cysteines in tandem regions. Such motifs are characteristic of zinc-coordinating structural domains and meaningfully favor Zn(2+) over Ca(2+), Mg(2+), or heme b as the bound cofactor.",
    "missing_item_specific_fact": "The sequence alone does not establish that zinc is required for catalytic activity, or provide experimental evidence for that specific requirement.",
    "reason": "The repeated cysteine-rich sequence patterns provide a concrete biological basis for predicting zinc binding. That supports distinguishing Zn as a cofactor, but not the question's more specific catalytic-activity premise."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence gives a distinctive basis for zinc binding among the listed options. The ambiguity is instead whether the question means zinc binding generally or a cofactor required for catalysis."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence is not information supplied to the original model.",
    "The current and archived UniProt records match the supplied sequence, but the cited cofactor annotation does not by itself establish experimental necessity for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E9Q3G8 (Nup153, mouse) explicitly annotates Zn(2+) as the cofactor, stating 'Binds at least 4 zinc ions per subunit.' The sequence contains four recognizable C2H2-type zinc finger motifs (e.g., CDTCLLQNK...CIACQAAK, WDCDTCLVQNK...CVACETPK, WECPVCCVCNKA...CVSCTSEK, WDCEVCLVQNK...CIACESAK), consistent with the annotation. The sequence matches the benchmark input exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains four clearly identifiable C2H2-type zinc finger motifs (C-x2-4-C-x12-C-x2-4-C pattern), which are among the most well-characterized Zn(2+)-binding structural domains in biology. A model recognizing these motifs can infer Zn(2+) dependence from general knowledge that zinc fingers coordinate Zn(2+) via Cys and His residues. The other options are inconsistent: no EF-hand or Ca-binding loops are present (ruling out Ca2+), no Mg-binding motifs or nucleotide-binding folds are evident (ruling out Mg2+), and no heme-binding motifs such as Cys-rich pockets or bis-His ligation sites exist (ruling out heme b). The number of zinc finger domains (4) further corroborates Zn(2+) over other divalent cations.


**Missing item-specific fact**

> None critical. While the specific identity as Nup153 and its nuclear pore role require lookup, the zinc finger motifs are directly readable from the sequence and their Zn(2+) dependence is textbook biochemistry.


**Reason**

> The zinc finger domains are visually identifiable in the raw sequence without needing to recognize the protein as Nup153. The C2H2 pattern is a canonical Zn(2+)-binding motif, making the inference from sequence to cofactor a matter of applying general structural biology knowledge rather than recalling a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four C2H2 zinc finger motifs unambiguously point to Zn(2+). None of the other choices (Ca2+, Mg2+, heme b) have any structural signature in this sequence. The question's framing as 'catalytic activity' is slightly imprecise since Nup153 is a structural nuclear pore protein rather than an enzyme, but this does not create ambiguity among the answer choices.


### Important caveats

- Nup153 is a structural component of the nuclear pore complex, not an enzyme. The zinc ions are structural (stabilizing zinc finger folds) rather than catalytic cofactors. The question's framing as 'cofactor required for catalytic activity' is imprecise but does not affect the correct answer selection.
- The zinc finger identification relies on pattern recognition of well-known motifs; a model lacking training on zinc finger consensus patterns might struggle, but this is a knowledge gap rather than a missing item-specific fact.
- The UniProt annotation evidence codes are not fully specified in the excerpts; the zinc-binding annotation may derive from structural studies of human Nup153 zinc fingers transferred to the mouse ortholog.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains four clearly identifiable C2H2-type zinc finger motifs (C-x2-4-C-x12-C-x2-4-C pattern), which are among the most well-characterized Zn(2+)-binding structural domains in biology. A model recognizing these motifs can infer Zn(2+) dependence from general knowledge that zinc fingers coordinate Zn(2+) via Cys and His residues. The other options are inconsistent: no EF-hand or Ca-binding loops are present (ruling out Ca2+), no Mg-binding motifs or nucleotide-binding folds are evident (ruling out Mg2+), and no heme-binding motifs such as Cys-rich pockets or bis-His ligation sites exist (ruling out heme b). The number of zinc finger domains (4) further corroborates Zn(2+) over other divalent cations.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While the specific identity as Nup153 and its nuclear pore role require lookup, the zinc finger motifs are directly readable from the sequence and their Zn(2+) dependence is textbook biochemistry.",
    "reason": "The zinc finger domains are visually identifiable in the raw sequence without needing to recognize the protein as Nup153. The C2H2 pattern is a canonical Zn(2+)-binding motif, making the inference from sequence to cofactor a matter of applying general structural biology knowledge rather than recalling a specific database annotation."
  },
  "case_id": "cofactor_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E9Q3G8 (Nup153, mouse) explicitly annotates Zn(2+) as the cofactor, stating 'Binds at least 4 zinc ions per subunit.' The sequence contains four recognizable C2H2-type zinc finger motifs (e.g., CDTCLLQNK...CIACQAAK, WDCDTCLVQNK...CVACETPK, WECPVCCVCNKA...CVSCTSEK, WDCEVCLVQNK...CIACESAK), consistent with the annotation. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "Nup153 is a structural component of the nuclear pore complex, not an enzyme. The zinc ions are structural (stabilizing zinc finger folds) rather than catalytic cofactors. The question's framing as 'cofactor required for catalytic activity' is imprecise but does not affect the correct answer selection.",
    "The zinc finger identification relies on pattern recognition of well-known motifs; a model lacking training on zinc finger consensus patterns might struggle, but this is a knowledge gap rather than a missing item-specific fact.",
    "The UniProt annotation evidence codes are not fully specified in the excerpts; the zinc-binding annotation may derive from structural studies of human Nup153 zinc fingers transferred to the mouse ortholog."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four C2H2 zinc finger motifs unambiguously point to Zn(2+). None of the other choices (Ca2+, Mg2+, heme b) have any structural signature in this sequence. The question's framing as 'catalytic activity' is slightly imprecise since Nup153 is a structural nuclear pore protein rather than an enzyme, but this does not create ambiguity among the answer choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E9Q3G8 (Nup153, mouse) explicitly annotates Zn(2+) as the cofactor, stating 'Binds at least 4 zinc ions per subunit.' The sequence contains four recognizable C2H2-type zinc finger motifs (e.g., CDTCLLQNK...CIACQAAK, WDCDTCLVQNK...CVACETPK, WECPVCCVCNKA...CVSCTSEK, WDCEVCLVQNK...CIACESAK), consistent with the annotation. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains four clearly identifiable C2H2-type zinc finger motifs (C-x2-4-C-x12-C-x2-4-C pattern), which are among the most well-characterized Zn(2+)-binding structural domains in biology. A model recognizing these motifs can infer Zn(2+) dependence from general knowledge that zinc fingers coordinate Zn(2+) via Cys and His residues. The other options are inconsistent: no EF-hand or Ca-binding loops are present (ruling out Ca2+), no Mg-binding motifs or nucleotide-binding folds are evident (ruling out Mg2+), and no heme-binding motifs such as Cys-rich pockets or bis-His ligation sites exist (ruling out heme b). The number of zinc finger domains (4) further corroborates Zn(2+) over other divalent cations.",
    "missing_item_specific_fact": "None critical. While the specific identity as Nup153 and its nuclear pore role require lookup, the zinc finger motifs are directly readable from the sequence and their Zn(2+) dependence is textbook biochemistry.",
    "reason": "The zinc finger domains are visually identifiable in the raw sequence without needing to recognize the protein as Nup153. The C2H2 pattern is a canonical Zn(2+)-binding motif, making the inference from sequence to cofactor a matter of applying general structural biology knowledge rather than recalling a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four C2H2 zinc finger motifs unambiguously point to Zn(2+). None of the other choices (Ca2+, Mg2+, heme b) have any structural signature in this sequence. The question's framing as 'catalytic activity' is slightly imprecise since Nup153 is a structural nuclear pore protein rather than an enzyme, but this does not create ambiguity among the answer choices."
  },
  "important_caveats": [
    "Nup153 is a structural component of the nuclear pore complex, not an enzyme. The zinc ions are structural (stabilizing zinc finger folds) rather than catalytic cofactors. The question's framing as 'cofactor required for catalytic activity' is imprecise but does not affect the correct answer selection.",
    "The zinc finger identification relies on pattern recognition of well-known motifs; a model lacking training on zinc finger consensus patterns might struggle, but this is a knowledge gap rather than a missing item-specific fact.",
    "The UniProt annotation evidence codes are not fully specified in the excerpts; the zinc-binding annotation may derive from structural studies of human Nup153 zinc fingers transferred to the mouse ortholog."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3G8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:07.166127+00:00.  

```json
"E9Q3G8"
```

Source SHA-256: `ab17eb27867a9b9705e8ee5aab15af52a3372820947fb64315598a4d75f696a6`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:07.166127+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"value":"Binds at least 4 zinc ions per subunit."}]}}
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3G8?format=txt&versions=108)  
**Locator:** `lines 76-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 108 / 1.  
**Retrieved:** 2026-11-02T04:28:10.539906+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC       Note=Binds at least 4 zinc ions per subunit.;
```

Source SHA-256: `2621d3bcc6ebd205d306166e3ca90bad9a7ba29993468087d17d98bac2ed53a2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
