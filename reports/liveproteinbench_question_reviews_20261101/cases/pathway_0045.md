# pathway_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELNGIRRRLATAKEAERHRLLLELIRAAAAEALDRPGPLPLDPGRAFGAQGVRGRAAGRLRERLSEATGLPLPATVVFDYPTPGALAGRLCALLLDEPAGPGGANGQMEAEEPIAIVGMGCRLPGDVRSPEGLWRLVHNGTDAISEFPEDRGWTVQQHPDPDHLGTTVTRHAGFLYDAPDFDAGFFAISPGEAVTIDPQHRLLLETTWKAVEDARIDPTSLRGSRTGVFVGLMYSEYGARIRRVPPGAEGYRVVGSMPSVASGRLAYTFGFEGPAVTVDTACSSSLVAMHLAAQSLRKGECTLAVAGGATVMATPWGYIEFSRQRGLAPDGRCRSFSADAAGSSWSEGVGVLLLERLSDARRHGHRVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRQALAHAGLTTAEVDAVDAHGAGTRLGDPIEAQALLATYGQGRPAGRPLWLGSLKSNIGHTQAAAGAAGVIKMVMAMRHGVLPRSLHITEPTPHVDWTSGAVELLTEARDWPADGRPRRAAVSSFGVGGTNAHIILEQAAPEPERPHAPEADGEPRPLPWPVSGHGAAGLRAQARRLADFLRAGPAAPDADLAYSLATTRATLTDRAVVVAADRAEAIARLTALAEGDQGPRVARATAVPRDRLAFVFPGQGSQWPGMAAELMSCYPVFRESIKECGRSLAPHTDWSLAKVLRGESGAPTLDRVDVVQPALFAVMVSLAALWRSFGVEPSAVAGHSQGEIAAARVAGALSLEDAARVVALRSRALRVLSGRGGMVSVAAPAGQVLRTLERWGGAVSVAAVNGPRSLVISGDPGALGEALAAFEAEGIRARRIPVDYASHSAQVEEIRDTLLTELSGIRPRPATVPFYSTVSGEPLDTTALDTGYWVRNLRDTVQFDRTVRRLLADGHTTFLEMSPHPVLTPGIQETAEEAGADEVLTVESLRRNEGGPARLLTAVAEAHVHGVAVDWSPAFAPHRSPARRPAVLRLSSGAATGLRTRPRPPPMFTTAGLDGIDHPLLGAAIPLADGGGGTLFTGTLSLATHPWLADHAVADVLVVPGTALVEAALRAGAECTGRAMLEELVLQAPLILPEQGTVRIQLSVGGPDGTGRRALILSSRPEDAGADEPWTRHAEGTLAPGGGHPRQDPGPWPPTGAREIDLDDCYRQLAKTGLHYGPAFQGLKRLWRLADDLCLEAELPDSAGESGRYGLHPALFDAALHAAALAGPSGAEPLTRLPFSWSGVALYTAGATRLRARLSFTGPQSLTLTAMDPLGHPVLSVGTLGMRPVTAEALHRAAGTAGTALLRLEWRRQAPEHPAGPDLTGWAWVGAGAPPAQPPDGRPYRDLAALRAELDAGAAVPPVIVLAEPATPEGTDPFTAARAALHRTLAAIQDWAAEERLAGTRLVVLTQGAVAATPGALPDPALAAVWGLVRSAQAEYPDRIGLVDTDDPGRSRAAVAAAVHAGEAQAAVRDGALLVPRLARVTATDGPGGPAWPADGTVLVTGGLGTLGRLVVRHLVTTHGARRLVILSRSGGDSAEVREFVGELLAQGANVQVVKGDAADPAVLERVLDGIPQEHPLAAVAHLAGALDDGVLAAQTPQRLDRVLRPKAEAAWQLHRLTARARVPLLAFSSLSGVLGPAGQAGYAAANAFVDALVQRRRGTGLPGVSMGWGMWATRSGLTGALSDTDARLIARTGVRPLTDEEGLALFDQARATGEPVVFPLGLDITALNSGAPDGIPPLLRGLTARTPARRAGAAEAPEPAGEDLAARLAATPEAERDALLLGVVRGHIAAVLGYDDPRAVAERRPFSDIGFDSLRALQLRNRLGAATGRRLPATLVFDHPNPAALSRYLRTLLLPDPAPAPTAPDGQPGPDQADQVIERLNSASLEEVLDFIDHQLGE

[Multiple Choices]
A. One-carbon metabolism
B. Antibiotic biosynthesis. .
C. peptidoglycan degradation. .
D. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
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

> The exact sequence matches a UniProt entry whose pathway annotation is “Antibiotic biosynthesis”; the historical entry available by the stated cutoff carries the same annotation. This supports the key as a database annotation, though the excerpts do not independently establish direct experimental validation.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long, multidomain sequence is consistent with a polyketide-synthase-like enzyme, making secondary-metabolite biosynthesis more plausible than one-carbon metabolism, peptidoglycan degradation, or folate synthesis.


**Missing item-specific fact**

> Sequence architecture alone does not establish that this particular polyketide product is an antibiotic; that product/pathway assignment requires protein-specific annotation or other item-specific evidence.


**Reason**

> The sequence offers a useful broad biosynthetic clue, but it does not by itself distinguish antibiotic production from other possible polyketide pathways. The specific assignment needed for B depends on a protein-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, B is supported by the matched pathway annotation. The sequence-based clue alone is broader than the antibiotic-specific pathway label.


### Important caveats

- Reviewer-only database evidence was not supplied to the evaluated model.
- The cited database pathway annotation is linked to a publication, but the supplied excerpts do not independently verify the primary experimental evidence.
- The actual author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a polyketide-synthase-like enzyme, making secondary-metabolite biosynthesis more plausible than one-carbon metabolism, peptidoglycan degradation, or folate synthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Sequence architecture alone does not establish that this particular polyketide product is an antibiotic; that product/pathway assignment requires protein-specific annotation or other item-specific evidence.",
    "reason": "The sequence offers a useful broad biosynthetic clue, but it does not by itself distinguish antibiotic production from other possible polyketide pathways. The specific assignment needed for B depends on a protein-specific fact absent from the input."
  },
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose pathway annotation is “Antibiotic biosynthesis”; the historical entry available by the stated cutoff carries the same annotation. This supports the key as a database annotation, though the excerpts do not independently establish direct experimental validation."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited database pathway annotation is linked to a publication, but the supplied excerpts do not independently verify the primary experimental evidence.",
    "The actual author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is supported by the matched pathway annotation. The sequence-based clue alone is broader than the antibiotic-specific pathway label."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose pathway annotation is “Antibiotic biosynthesis”; the historical entry available by the stated cutoff carries the same annotation. This supports the key as a database annotation, though the excerpts do not independently establish direct experimental validation.",
    "evidence_ids": ["H3", "C5", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a polyketide-synthase-like enzyme, making secondary-metabolite biosynthesis more plausible than one-carbon metabolism, peptidoglycan degradation, or folate synthesis.",
    "missing_item_specific_fact": "Sequence architecture alone does not establish that this particular polyketide product is an antibiotic; that product/pathway assignment requires protein-specific annotation or other item-specific evidence.",
    "reason": "The sequence offers a useful broad biosynthetic clue, but it does not by itself distinguish antibiotic production from other possible polyketide pathways. The specific assignment needed for B depends on a protein-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, B is supported by the matched pathway annotation. The sequence-based clue alone is broader than the antibiotic-specific pathway label."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not supplied to the evaluated model.",
    "The cited database pathway annotation is linked to a publication, but the supplied excerpts do not independently verify the primary experimental evidence.",
    "The actual author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA, EC 2.3.1.290) explicitly annotates the pathway as 'Antibiotic biosynthesis' with evidence code ECO:0000305 referencing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007). The sequence match is confirmed (SHA-256 identical, 1897 AA). The protein is a modular PKS producing spectinabilin, an antibiotic, in Streptomyces orinoci. The annotation is database-curated (Swiss-Prot) with a literature reference, not merely computational inference.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C7](#evidence-c7), [H3](#evidence-h3), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is ~1897 residues with a multi-domain modular architecture characteristic of polyketide synthases (repeated KS/AT/ACP/TE-like segments visible as conserved motifs such as 'GHSQGE', 'GAGAPPAQ', 'GGMVSVAAP'). Options A (one-carbon metabolism: e.g., methylenetetrahydrofolate reductase, methionine synthase), C (peptidoglycan degradation: lysozymes, amidases), and D (dihydropteroate synthase, ~300 AA) all involve small, single-domain enzymes incompatible with a ~1900 AA modular multi-domain protein. By eliminating these structurally incompatible options and recognizing the PKS-like domain organization (whose products in Actinomycetes are predominantly antibiotics), option B is the only viable choice. This reasoning uses general knowledge of enzyme size, domain architecture, and Streptomyces secondary metabolism without requiring memorization of this specific protein's database entry.


**Missing item-specific fact**

> None strictly required; however, precise identification of individual PKS domain boundaries from raw sequence without tools is challenging. The elimination logic (large modular enzyme ≠ small-molecule metabolic enzymes) provides a sufficient reasoning path among the four choices.


**Reason**

> The answer can be reached by noting the protein's exceptional length and modular domain architecture, then eliminating options A, C, and D which correspond to small single-domain enzymes in unrelated pathways. Recognizing PKS-like motifs and knowing that Streptomyces PKS products are typically antibiotics provides a positive identification of B. This constitutes general biological reasoning, though it requires specialized domain-knowledge of enzyme architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry also lists 'Polyketide biosynthesis' as a pathway, but this is not among the four choices. Among the provided options, only B (Antibiotic biosynthesis) is compatible with a large modular PKS. Options A, C, and D are structurally and functionally incompatible with the sequence.


### Important caveats

- The UniProt annotation evidence code ECO:0000305 indicates inference from a reference (PubMed:17763486), which describes the aureothin/neoaureothin PKS pathways; the spectinabilin assignment relies on homology to those characterized PKS systems.
- The 'Antibiotic biosynthesis' pathway label is a broad UniProt category; the specific product (spectinabilin) is a polyene antibiotic, but the pathway annotation is somewhat coarse.
- The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning assessment considers only what can be inferred from the raw sequence and general biological knowledge.
- Identifying individual PKS catalytic domains (KS, AT, ACP, TE) from a raw 1897-aa sequence without computational tools is difficult in practice, though the overall multi-domain modular architecture is apparent from length and repetitive segment structure.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is ~1897 residues with a multi-domain modular architecture characteristic of polyketide synthases (repeated KS/AT/ACP/TE-like segments visible as conserved motifs such as 'GHSQGE', 'GAGAPPAQ', 'GGMVSVAAP'). Options A (one-carbon metabolism: e.g., methylenetetrahydrofolate reductase, methionine synthase), C (peptidoglycan degradation: lysozymes, amidases), and D (dihydropteroate synthase, ~300 AA) all involve small, single-domain enzymes incompatible with a ~1900 AA modular multi-domain protein. By eliminating these structurally incompatible options and recognizing the PKS-like domain organization (whose products in Actinomycetes are predominantly antibiotics), option B is the only viable choice. This reasoning uses general knowledge of enzyme size, domain architecture, and Streptomyces secondary metabolism without requiring memorization of this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, precise identification of individual PKS domain boundaries from raw sequence without tools is challenging. The elimination logic (large modular enzyme ≠ small-molecule metabolic enzymes) provides a sufficient reasoning path among the four choices.",
    "reason": "The answer can be reached by noting the protein's exceptional length and modular domain architecture, then eliminating options A, C, and D which correspond to small single-domain enzymes in unrelated pathways. Recognizing PKS-like motifs and knowing that Streptomyces PKS products are typically antibiotics provides a positive identification of B. This constitutes general biological reasoning, though it requires specialized domain-knowledge of enzyme architecture."
  },
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C7",
      "H3",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA, EC 2.3.1.290) explicitly annotates the pathway as 'Antibiotic biosynthesis' with evidence code ECO:0000305 referencing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007). The sequence match is confirmed (SHA-256 identical, 1897 AA). The protein is a modular PKS producing spectinabilin, an antibiotic, in Streptomyces orinoci. The annotation is database-curated (Swiss-Prot) with a literature reference, not merely computational inference."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates inference from a reference (PubMed:17763486), which describes the aureothin/neoaureothin PKS pathways; the spectinabilin assignment relies on homology to those characterized PKS systems.",
    "The 'Antibiotic biosynthesis' pathway label is a broad UniProt category; the specific product (spectinabilin) is a polyene antibiotic, but the pathway annotation is somewhat coarse.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning assessment considers only what can be inferred from the raw sequence and general biological knowledge.",
    "Identifying individual PKS catalytic domains (KS, AT, ACP, TE) from a raw 1897-aa sequence without computational tools is difficult in practice, though the overall multi-domain modular architecture is apparent from length and repetitive segment structure."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway, but this is not among the four choices. Among the provided options, only B (Antibiotic biosynthesis) is compatible with a large modular PKS. Options A, C, and D are structurally and functionally incompatible with the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (Spectinabilin polyketide synthase system protein NorA, EC 2.3.1.290) explicitly annotates the pathway as 'Antibiotic biosynthesis' with evidence code ECO:0000305 referencing PubMed:17763486 (Traitcheva et al., ChemBioChem 2007). The sequence match is confirmed (SHA-256 identical, 1897 AA). The protein is a modular PKS producing spectinabilin, an antibiotic, in Streptomyces orinoci. The annotation is database-curated (Swiss-Prot) with a literature reference, not merely computational inference.",
    "evidence_ids": ["C5", "C4", "C7", "H3", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is ~1897 residues with a multi-domain modular architecture characteristic of polyketide synthases (repeated KS/AT/ACP/TE-like segments visible as conserved motifs such as 'GHSQGE', 'GAGAPPAQ', 'GGMVSVAAP'). Options A (one-carbon metabolism: e.g., methylenetetrahydrofolate reductase, methionine synthase), C (peptidoglycan degradation: lysozymes, amidases), and D (dihydropteroate synthase, ~300 AA) all involve small, single-domain enzymes incompatible with a ~1900 AA modular multi-domain protein. By eliminating these structurally incompatible options and recognizing the PKS-like domain organization (whose products in Actinomycetes are predominantly antibiotics), option B is the only viable choice. This reasoning uses general knowledge of enzyme size, domain architecture, and Streptomyces secondary metabolism without requiring memorization of this specific protein's database entry.",
    "missing_item_specific_fact": "None strictly required; however, precise identification of individual PKS domain boundaries from raw sequence without tools is challenging. The elimination logic (large modular enzyme ≠ small-molecule metabolic enzymes) provides a sufficient reasoning path among the four choices.",
    "reason": "The answer can be reached by noting the protein's exceptional length and modular domain architecture, then eliminating options A, C, and D which correspond to small single-domain enzymes in unrelated pathways. Recognizing PKS-like motifs and knowing that Streptomyces PKS products are typically antibiotics provides a positive identification of B. This constitutes general biological reasoning, though it requires specialized domain-knowledge of enzyme architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway, but this is not among the four choices. Among the provided options, only B (Antibiotic biosynthesis) is compatible with a large modular PKS. Options A, C, and D are structurally and functionally incompatible with the sequence."
  },
  "important_caveats": [
    "The UniProt annotation evidence code ECO:0000305 indicates inference from a reference (PubMed:17763486), which describes the aureothin/neoaureothin PKS pathways; the spectinabilin assignment relies on homology to those characterized PKS systems.",
    "The 'Antibiotic biosynthesis' pathway label is a broad UniProt category; the specific product (spectinabilin) is a polyene antibiotic, but the pathway annotation is somewhat coarse.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning assessment considers only what can be inferred from the raw sequence and general biological knowledge.",
    "Identifying individual PKS catalytic domains (KS, AT, ACP, TE) from a raw 1897-aa sequence without computational tools is difficult in practice, though the overall multi-domain modular architecture is apparent from length and repetitive segment structure."
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

**Accession:** `B4ER92` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 83. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85893.1","source":"EMBL"}],"value":"Modular polyketide synthase NorA"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"2.3.1.290"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin polyketide synthase system protein NorA"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin PKS system protein NorA"}]}}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.659517+00:00.  

```json
{"citation":{"authors":["Traitcheva N.","Jenke-Kodama H.","He J.","Dittmann E.","Hertweck C."],"citationCrossReferences":[{"database":"PubMed","id":"17763486"},{"database":"DOI","id":"10.1002/cbic.200700309"}],"citationType":"journal article","firstPage":"1841","id":"17763486","journal":"ChemBioChem","lastPage":"1849","publicationDate":"2007","title":"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85893.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"HKI-0260"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
ID   NORA_STRON              Reviewed;        1897 AA.
AC   B4ER92;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   23-SEP-2008, sequence version 1.
DT   28-JAN-2026, entry version 83.
DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};
DE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};
DE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};
DE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};
GN   Name=norA {ECO:0000303|PubMed:17763486};
OS   Streptomyces orinoci (Streptoverticillium orinoci).
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=67339;
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 83 / 1.  
**Retrieved:** 2026-11-01T06:27:51.676658+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000305|PubMed:17763486}.
```

Source SHA-256: `3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
