# pathway_0150

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Pigment biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. Antibiotic biosynthesis. .
B. Pigment biosynthesis. .
C. spheroidene biosynthesis. .
D. Carbohydrate degradation
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as indigoidine synthase, with the pathway recorded as pigment biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269, PubMed 17237222), whose title describes a Streptomyces enzyme catalyzing blue-pigment synthesis. This supports choice B, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large nonribosomal peptide synthetase, which makes spheroidene biosynthesis and carbohydrate degradation poor fits. But that general inference does not distinguish pigment production from other specialized-metabolite pathways such as antibiotic biosynthesis.


**Missing item-specific fact**

> The enzyme’s specific product/function—indigoidine synthase producing a blue pigment—is not supplied and is needed to distinguish pigment biosynthesis from antibiotic biosynthesis.


**Reason**

> The sequence and choices offer useful broad clues, but the decisive pathway assignment depends on protein-specific functional knowledge absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched-sequence functional annotation and cited pigment-synthesis evidence, pigment biosynthesis is the supported choice; the other options are not comparably supported.


### Important caveats

- The sequence match and functional/pathway annotations come from reviewer-only database evidence, not from information supplied to the evaluated model.
- The cited experimental evidence is retained through the database annotation; the primary study was not independently validated for this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large nonribosomal peptide synthetase, which makes spheroidene biosynthesis and carbohydrate degradation poor fits. But that general inference does not distinguish pigment production from other specialized-metabolite pathways such as antibiotic biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme’s specific product/function—indigoidine synthase producing a blue pigment—is not supplied and is needed to distinguish pigment biosynthesis from antibiotic biosynthesis.",
    "reason": "The sequence and choices offer useful broad clues, but the decisive pathway assignment depends on protein-specific functional knowledge absent from the prompt."
  },
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as indigoidine synthase, with the pathway recorded as pigment biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269, PubMed 17237222), whose title describes a Streptomyces enzyme catalyzing blue-pigment synthesis. This supports choice B, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and functional/pathway annotations come from reviewer-only database evidence, not from information supplied to the evaluated model.",
    "The cited experimental evidence is retained through the database annotation; the primary study was not independently validated for this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched-sequence functional annotation and cited pigment-synthesis evidence, pigment biosynthesis is the supported choice; the other options are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as indigoidine synthase, with the pathway recorded as pigment biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269, PubMed 17237222), whose title describes a Streptomyces enzyme catalyzing blue-pigment synthesis. This supports choice B, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large nonribosomal peptide synthetase, which makes spheroidene biosynthesis and carbohydrate degradation poor fits. But that general inference does not distinguish pigment production from other specialized-metabolite pathways such as antibiotic biosynthesis.",
    "missing_item_specific_fact": "The enzyme’s specific product/function—indigoidine synthase producing a blue pigment—is not supplied and is needed to distinguish pigment biosynthesis from antibiotic biosynthesis.",
    "reason": "The sequence and choices offer useful broad clues, but the decisive pathway assignment depends on protein-specific functional knowledge absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched-sequence functional annotation and cited pigment-synthesis evidence, pigment biosynthesis is the supported choice; the other options are not comparably supported."
  },
  "important_caveats": [
    "The sequence match and functional/pathway annotations come from reviewer-only database evidence, not from information supplied to the evaluated model.",
    "The cited experimental evidence is retained through the database annotation; the primary study was not independently validated for this audit."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q1MWN4 (INDGS_STRLA, Indigoidine synthase, EC 4.3.3.9) is annotated with PATHWAY: 'Pigment biosynthesis' (ECO:0000269|PubMed:17237222), which is experimental evidence from the 2007 J. Biol. Chem. paper by Takahashi et al. The sequence matches exactly (1282 AA, SHA256 confirmed). The protein is also named 'Blue-pigment synthetase' and the paper title explicitly states 'catalyzing a blue pigment synthesis.' Choice B directly matches the curated pathway annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable NRPS domain motifs (e.g., 'YSGSTGKPKG' adenylation-domain signature, 'HH' peptidyl-carrier-protein motif), allowing identification as a non-ribosomal peptide synthetase. However, NRPS enzymes in Streptomyces are overwhelmingly associated with antibiotic biosynthesis (e.g., vancomycin, daptomycin, bleomycin). Distinguishing 'pigment biosynthesis' (B) from 'antibiotic biosynthesis' (A) requires knowing that this specific single-module NRPS activates glutamine to form indigoidine (a blue pigment) rather than an antibiotic. Substrate specificity of the A domain is not reliably inferable from sequence by general reasoning.


**Missing item-specific fact**

> The experimental finding (PubMed:17237222) that bpsA from S. lavendulae produces indigoidine, a blue pigment, rather than an antibiotic. This product identity is the critical fact separating choice B from choice A and is not encoded in any generalizable sequence feature.


**Reason**

> While domain architecture (NRPS) can be recognized from sequence motifs, the critical distinction between options A and B depends on knowing the specific product (indigoidine) of this particular NRPS. Streptomyces NRPSs are predominantly antibiotic synthetases, so general biological reasoning would actually favor A. The correct answer requires memorization of this specific protein's characterized function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 'Antibiotic biosynthesis' (A) and 'Pigment biosynthesis' (B) are highly plausible pathways for a Streptomyces NRPS. Streptomyces are renowned for NRPS-derived antibiotics, making A a strong default guess from general knowledge. Only the specific experimental characterization of this enzyme as an indigoidine (blue pigment) synthetase resolves the ambiguity in favor of B. Options C (spheroidene/carotenoid biosynthesis, a photosynthetic-bacterial pathway) and D (carbohydrate degradation, unrelated to NRPS chemistry) can be eliminated by general reasoning.


### Important caveats

- The UniProt pathway annotation carries ECO:0000269 (experimental evidence), confirming the pigment role was established experimentally, not merely inferred computationally.
- The single-module NRPS architecture (1282 AA) is atypical for antibiotic-producing NRPSs (usually multi-module, >3000 AA), which could weakly hint at a simpler product, but this does not reliably distinguish pigment from small-molecule antibiotic.
- The entry was first public in 2025-02-05; if the benchmark was constructed before that date, the author may have relied on the 2007 paper or TrEMBL annotation rather than Swiss-Prot curation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain motifs (e.g., 'YSGSTGKPKG' adenylation-domain signature, 'HH' peptidyl-carrier-protein motif), allowing identification as a non-ribosomal peptide synthetase. However, NRPS enzymes in Streptomyces are overwhelmingly associated with antibiotic biosynthesis (e.g., vancomycin, daptomycin, bleomycin). Distinguishing 'pigment biosynthesis' (B) from 'antibiotic biosynthesis' (A) requires knowing that this specific single-module NRPS activates glutamine to form indigoidine (a blue pigment) rather than an antibiotic. Substrate specificity of the A domain is not reliably inferable from sequence by general reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental finding (PubMed:17237222) that bpsA from S. lavendulae produces indigoidine, a blue pigment, rather than an antibiotic. This product identity is the critical fact separating choice B from choice A and is not encoded in any generalizable sequence feature.",
    "reason": "While domain architecture (NRPS) can be recognized from sequence motifs, the critical distinction between options A and B depends on knowing the specific product (indigoidine) of this particular NRPS. Streptomyces NRPSs are predominantly antibiotic synthetases, so general biological reasoning would actually favor A. The correct answer requires memorization of this specific protein's characterized function."
  },
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (INDGS_STRLA, Indigoidine synthase, EC 4.3.3.9) is annotated with PATHWAY: 'Pigment biosynthesis' (ECO:0000269|PubMed:17237222), which is experimental evidence from the 2007 J. Biol. Chem. paper by Takahashi et al. The sequence matches exactly (1282 AA, SHA256 confirmed). The protein is also named 'Blue-pigment synthetase' and the paper title explicitly states 'catalyzing a blue pigment synthesis.' Choice B directly matches the curated pathway annotation."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries ECO:0000269 (experimental evidence), confirming the pigment role was established experimentally, not merely inferred computationally.",
    "The single-module NRPS architecture (1282 AA) is atypical for antibiotic-producing NRPSs (usually multi-module, >3000 AA), which could weakly hint at a simpler product, but this does not reliably distinguish pigment from small-molecule antibiotic.",
    "The entry was first public in 2025-02-05; if the benchmark was constructed before that date, the author may have relied on the 2007 paper or TrEMBL annotation rather than Swiss-Prot curation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 'Antibiotic biosynthesis' (A) and 'Pigment biosynthesis' (B) are highly plausible pathways for a Streptomyces NRPS. Streptomyces are renowned for NRPS-derived antibiotics, making A a strong default guess from general knowledge. Only the specific experimental characterization of this enzyme as an indigoidine (blue pigment) synthetase resolves the ambiguity in favor of B. Options C (spheroidene/carotenoid biosynthesis, a photosynthetic-bacterial pathway) and D (carbohydrate degradation, unrelated to NRPS chemistry) can be eliminated by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (INDGS_STRLA, Indigoidine synthase, EC 4.3.3.9) is annotated with PATHWAY: 'Pigment biosynthesis' (ECO:0000269|PubMed:17237222), which is experimental evidence from the 2007 J. Biol. Chem. paper by Takahashi et al. The sequence matches exactly (1282 AA, SHA256 confirmed). The protein is also named 'Blue-pigment synthetase' and the paper title explicitly states 'catalyzing a blue pigment synthesis.' Choice B directly matches the curated pathway annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain motifs (e.g., 'YSGSTGKPKG' adenylation-domain signature, 'HH' peptidyl-carrier-protein motif), allowing identification as a non-ribosomal peptide synthetase. However, NRPS enzymes in Streptomyces are overwhelmingly associated with antibiotic biosynthesis (e.g., vancomycin, daptomycin, bleomycin). Distinguishing 'pigment biosynthesis' (B) from 'antibiotic biosynthesis' (A) requires knowing that this specific single-module NRPS activates glutamine to form indigoidine (a blue pigment) rather than an antibiotic. Substrate specificity of the A domain is not reliably inferable from sequence by general reasoning.",
    "missing_item_specific_fact": "The experimental finding (PubMed:17237222) that bpsA from S. lavendulae produces indigoidine, a blue pigment, rather than an antibiotic. This product identity is the critical fact separating choice B from choice A and is not encoded in any generalizable sequence feature.",
    "reason": "While domain architecture (NRPS) can be recognized from sequence motifs, the critical distinction between options A and B depends on knowing the specific product (indigoidine) of this particular NRPS. Streptomyces NRPSs are predominantly antibiotic synthetases, so general biological reasoning would actually favor A. The correct answer requires memorization of this specific protein's characterized function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 'Antibiotic biosynthesis' (A) and 'Pigment biosynthesis' (B) are highly plausible pathways for a Streptomyces NRPS. Streptomyces are renowned for NRPS-derived antibiotics, making A a strong default guess from general knowledge. Only the specific experimental characterization of this enzyme as an indigoidine (blue pigment) synthetase resolves the ambiguity in favor of B. Options C (spheroidene/carotenoid biosynthesis, a photosynthetic-bacterial pathway) and D (carbohydrate degradation, unrelated to NRPS chemistry) can be eliminated by general reasoning."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries ECO:0000269 (experimental evidence), confirming the pigment role was established experimentally, not merely inferred computationally.",
    "The single-module NRPS architecture (1282 AA) is atypical for antibiotic-producing NRPSs (usually multi-module, >3000 AA), which could weakly hint at a simpler product, but this does not reliably distinguish pigment from small-molecule antibiotic.",
    "The entry was first public in 2025-02-05; if the benchmark was constructed before that date, the author may have relied on the 2007 paper or TrEMBL annotation rather than Swiss-Prot curation."
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

**Accession:** `Q1MWN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
"Q1MWN4"
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Kitasatosporales","Streptomycetaceae","Streptomyces"],"scientificName":"Streptomyces lavendulae","taxonId":1914}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue pigment synthetase-encoding gene A"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue-pigment synthetase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"value":"Pigment biosynthesis"}]}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"citation":{"authors":["Takahashi H.","Kumagai T.","Kitani K.","Mori M.","Matoba Y.","Sugiyama M."],"citationCrossReferences":[{"database":"PubMed","id":"17237222"},{"database":"DOI","id":"10.1074/jbc.m611319200"}],"citationType":"journal article","firstPage":"9073","id":"17237222","journal":"J. Biol. Chem.","lastPage":"9081","publicationDate":"2007","title":"Cloning and characterization of a Streptomyces single module type non-ribosomal peptide synthetase catalyzing a blue pigment synthesis.","volume":"282"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAE93896.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 11924 / 8197-20"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","DOMAIN","PHOSPHOPANTETHEINYLATION AT SER-972","MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608"]}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
ID   INDGS_STRLA             Reviewed;        1282 AA.
AC   Q1MWN4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   30-MAY-2006, sequence version 1.
DT   28-JAN-2026, entry version 86.
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};
DE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};
DE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};
GN   Name=bpsA {ECO:0000303|PubMed:17237222};
OS   Streptomyces lavendulae.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=1914;
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAE93896.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, DOMAIN, PHOSPHOPANTETHEINYLATION AT
RP   SER-972, AND MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608.
RC   STRAIN=ATCC 11924 / 8197-20;
RX   PubMed=17237222; DOI=10.1074/jbc.m611319200;
RA   Takahashi H., Kumagai T., Kitani K., Mori M., Matoba Y., Sugiyama M.;
RT   "Cloning and characterization of a Streptomyces single module type non-
RT   ribosomal peptide synthetase catalyzing a blue pigment synthesis.";
RL   J. Biol. Chem. 282:9073-9081(2007).
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
CC   -!- PATHWAY: Pigment biosynthesis. {ECO:0000269|PubMed:17237222}.
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
