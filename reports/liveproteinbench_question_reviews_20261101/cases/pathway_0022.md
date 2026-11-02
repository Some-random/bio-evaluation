# pathway_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antifungal biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHISPSKDTPSQRLPIPLSLPTHLGLLAKAYGVPPASILQLAWGLVLRCYFTTSSSRWGTIDMAHEYKEKKNLPIRCEVLELDDTRSIGWILQNWNDPSVHRHLPAEEDTSNVPVSAGSIVILTEDAKDLEVLRDFELTAEWIICFSTSTEKPLLRLSWRPDVIHSELASHLAQLLERALDTTFLSPDIPLSQINLFSILDHQKLLQWNHQYPQSVNRLVHEMFEDMVAARPQATAVAAWDGEVTYQQLDRLSTRLAIKLQTIDLQPESIVALCFEKSVWAIVAMLGVLRAGGAFLHIDPKHPTARQQAMISTTAARIILCSEQTRDTVSRFDSESLSLVVDRKMFAQEPDHKQVALPSPNNLGPRNAAYIVCTSGSTGLPKAIVVEHVSLCTSVTAQAEAMAVGGESRILQYAAYTFDVSVGDVFTALTHGACVCIPSDWERTQDLVGAINRLDVNQACLTSTVASFLTPMNVPKLQKLTLGGEPASKQCIDLWSGKVALKNVYGPAECTVWCVIQKNASSEIPASNIGRGIGARTWIVHPENHNQLMPIGAVGELLIEGPLVARGYLNDAERTTAVFLERAPSWLATFGPLPPQTRFYKTGDLARFEQNGTLFFEGRKDTQVKLRGQRIELGEIEYQIQQACNPVPPLAVELIETKDLQAPLLGAFITWTGGLEISLDQSAVPNGLGPDLDARSHFNELVSRIQANIDRTLPPYMMPGLYIPVQKLPLSTSGKLDRKVLRQYCTQHTRSFLTASEAESSDVIADDATKDDVALHEIVNPGEITLAQLWAHALGRRMESINAKDNFLSLGGDSLAAMRLVNLAARDAQVTLTVANIFESPVLADQARLLRPLSKTKSLAPFELMTRGEASIEDIVGFAAQQCRLLPAQIEDVYPCTPLQEEMMRDSLSNDRTQMGQEVVQISEELDLVRYQVACASVYRRFPILRTRFIEHSGRLVQVVVREDLCWKQPTSLAEYKALDSRERPALGKPLTRWALTSDGTHFILSLHHAMFDGITLGQIQGAIYAVYQCIPLPPPSVSFATFLAHLDDQNAPLSQESQRFWQSYLCPSASLDASITPETQKIDRPRASCGTQRLVQFTSGEVSALQRHGLTEATLVRGAWACTLARHQQKPHASAFSDVIFGTMLTGRNFHLPGVDMLAAPSLTHVPIRIRIDEGDLNGHSARALLARVQADATAMIPYEHDGMNRIRSIEVQTRAVFNRIRTLLVIQPIPEGLTSVSTSPFPGSIVSGPRVEAKEMGHFHWYGLLVECTLLPTKGFFVRVSYDNKMFGTEQVESLLDDYSTTLHTLANGLMDTDIPASLHV

[Multiple Choices]
A. Lipid metabolism. .
B. Antifungal biosynthesis. .
C. spheroidene biosynthesis. .
D. One-carbon metabolism
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

> The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The entry identifies the protein as a nonribosomal peptide synthetase and cites a publication for its function and pathway annotation. This supports choice B as a database- and literature-linked annotation, though the excerpts do not independently establish the experimental basis of the pathway assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is compatible with a large biosynthetic enzyme such as a nonribosomal peptide synthetase, which supports a broad biosynthesis role. That does not establish the specific antifungal pathway rather than another natural-product pathway.


**Missing item-specific fact**

> The protein’s association with the lanomycin biosynthetic cluster and its pathway annotation as antifungal biosynthesis are not supplied in the question.


**Reason**

> Identifying the precise pathway requires protein- or cluster-specific annotation or literature knowledge; general sequence reasoning does not distinguish the specific pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone does not make the pathway clear, but the cited annotation supports B among the listed choices.


### Important caveats

- The reviewer-only source identifies the matched sequence as a nonribosomal peptide synthetase from Pyrenophora dematioidea and annotates its pathway as antifungal biosynthesis.
- The pathway annotation is linked to a publication, but the supplied evidence excerpts do not independently validate the experimental strength of that assignment.
- The source identity and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is compatible with a large biosynthetic enzyme such as a nonribosomal peptide synthetase, which supports a broad biosynthesis role. That does not establish the specific antifungal pathway rather than another natural-product pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s association with the lanomycin biosynthetic cluster and its pathway annotation as antifungal biosynthesis are not supplied in the question.",
    "reason": "Identifying the precise pathway requires protein- or cluster-specific annotation or literature knowledge; general sequence reasoning does not distinguish the specific pathway."
  },
  "case_id": "pathway_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The entry identifies the protein as a nonribosomal peptide synthetase and cites a publication for its function and pathway annotation. This supports choice B as a database- and literature-linked annotation, though the excerpts do not independently establish the experimental basis of the pathway assignment."
  },
  "important_caveats": [
    "The reviewer-only source identifies the matched sequence as a nonribosomal peptide synthetase from Pyrenophora dematioidea and annotates its pathway as antifungal biosynthesis.",
    "The pathway annotation is linked to a publication, but the supplied evidence excerpts do not independently validate the experimental strength of that assignment.",
    "The source identity and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not make the pathway clear, but the cited annotation supports B among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with the pathway “Antifungal biosynthesis.” The entry identifies the protein as a nonribosomal peptide synthetase and cites a publication for its function and pathway annotation. This supports choice B as a database- and literature-linked annotation, though the excerpts do not independently establish the experimental basis of the pathway assignment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is compatible with a large biosynthetic enzyme such as a nonribosomal peptide synthetase, which supports a broad biosynthesis role. That does not establish the specific antifungal pathway rather than another natural-product pathway.",
    "missing_item_specific_fact": "The protein’s association with the lanomycin biosynthetic cluster and its pathway annotation as antifungal biosynthesis are not supplied in the question.",
    "reason": "Identifying the precise pathway requires protein- or cluster-specific annotation or literature knowledge; general sequence reasoning does not distinguish the specific pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone does not make the pathway clear, but the cited annotation supports B among the listed choices."
  },
  "important_caveats": [
    "The reviewer-only source identifies the matched sequence as a nonribosomal peptide synthetase from Pyrenophora dematioidea and annotates its pathway as antifungal biosynthesis.",
    "The pathway annotation is linked to a publication, but the supplied evidence excerpts do not independently validate the experimental strength of that assignment.",
    "The source identity and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry P0DXV4 (LAN2_PYRDE, 1325 AA, sequence SHA256 matched). The UniProt PATHWAY comment explicitly states 'Antifungal biosynthesis' (ECO:0000305, PubMed:33857369). The protein is annotated as a Nonribosomal peptide synthetase / Lanomycin biosynthesis cluster protein 1 from Pyrenophora dematioidea. The underlying paper (Liu et al., JACS 2021) describes genome mining of CYP51-inhibitor biosynthetic gene clusters, providing experimental context for the antifungal pathway assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable NRPS domain signatures (e.g., 'TSGSTG' adenylation-domain motif, 'HHAMFDG' condensation-domain motif), which could allow identification as a nonribosomal peptide synthetase. NRPS enzymes are involved in secondary metabolite biosynthesis, which could help eliminate lipid metabolism (fatty acid synthases/desaturases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and one-carbon metabolism (folate/methionine enzymes) as unlikely NRPS pathways. However, the specific assignment to 'antifungal' biosynthesis (vs. antibacterial, siderophore, immunosuppressant, or other NRPS-product pathways) cannot be derived from sequence features alone.


**Missing item-specific fact**

> Knowledge that this particular NRPS is part of the lanomycin biosynthetic gene cluster and that lanomycin is specifically an antifungal (CYP51 inhibitor) compound. The sequence provides no information distinguishing this NRPS's product as antifungal rather than antibacterial or another secondary metabolite class.


**Reason**

> While NRPS domain architecture recognition might narrow choices by eliminating clearly non-NRPS pathways (A, C, D), the specific pathway label 'Antifungal biosynthesis' requires item-specific knowledge of the gene cluster context and product bioactivity. NRPS enzymes produce diverse secondary metabolites; the antifungal designation is a database annotation derived from the underlying genomics paper, not a property inferable from the amino acid sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'Antifungal biosynthesis' is a secondary-metabolite/NRPS pathway. Lipid metabolism, spheroidene biosynthesis, and one-carbon metabolism are clearly distinct pathway classes not associated with NRPS enzymes. So if NRPS is recognized, B is the only viable option. However, this elimination still depends on the specific pathway taxonomy used by the benchmark.


### Important caveats

- The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation source may differ.
- The pathway annotation carries evidence code ECO:0000305 (inferred from curator), though the underlying PubMed reference (33857369) provides experimental genome-mining support.
- The protein is 1325 AA, which is relatively small for a multi-module NRPS; it may represent a single module or a partial assembly line, which could complicate domain recognition.
- The reviewer-only evidence was not available to the evaluated model; the model only sees the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain signatures (e.g., 'TSGSTG' adenylation-domain motif, 'HHAMFDG' condensation-domain motif), which could allow identification as a nonribosomal peptide synthetase. NRPS enzymes are involved in secondary metabolite biosynthesis, which could help eliminate lipid metabolism (fatty acid synthases/desaturases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and one-carbon metabolism (folate/methionine enzymes) as unlikely NRPS pathways. However, the specific assignment to 'antifungal' biosynthesis (vs. antibacterial, siderophore, immunosuppressant, or other NRPS-product pathways) cannot be derived from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this particular NRPS is part of the lanomycin biosynthetic gene cluster and that lanomycin is specifically an antifungal (CYP51 inhibitor) compound. The sequence provides no information distinguishing this NRPS's product as antifungal rather than antibacterial or another secondary metabolite class.",
    "reason": "While NRPS domain architecture recognition might narrow choices by eliminating clearly non-NRPS pathways (A, C, D), the specific pathway label 'Antifungal biosynthesis' requires item-specific knowledge of the gene cluster context and product bioactivity. NRPS enzymes produce diverse secondary metabolites; the antifungal designation is a database annotation derived from the underlying genomics paper, not a property inferable from the amino acid sequence alone."
  },
  "case_id": "pathway_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry P0DXV4 (LAN2_PYRDE, 1325 AA, sequence SHA256 matched). The UniProt PATHWAY comment explicitly states 'Antifungal biosynthesis' (ECO:0000305, PubMed:33857369). The protein is annotated as a Nonribosomal peptide synthetase / Lanomycin biosynthesis cluster protein 1 from Pyrenophora dematioidea. The underlying paper (Liu et al., JACS 2021) describes genome mining of CYP51-inhibitor biosynthetic gene clusters, providing experimental context for the antifungal pathway assignment."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation source may differ.",
    "The pathway annotation carries evidence code ECO:0000305 (inferred from curator), though the underlying PubMed reference (33857369) provides experimental genome-mining support.",
    "The protein is 1325 AA, which is relatively small for a multi-module NRPS; it may represent a single module or a partial assembly line, which could complicate domain recognition.",
    "The reviewer-only evidence was not available to the evaluated model; the model only sees the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'Antifungal biosynthesis' is a secondary-metabolite/NRPS pathway. Lipid metabolism, spheroidene biosynthesis, and one-carbon metabolism are clearly distinct pathway classes not associated with NRPS enzymes. So if NRPS is recognized, B is the only viable option. However, this elimination still depends on the specific pathway taxonomy used by the benchmark."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry P0DXV4 (LAN2_PYRDE, 1325 AA, sequence SHA256 matched). The UniProt PATHWAY comment explicitly states 'Antifungal biosynthesis' (ECO:0000305, PubMed:33857369). The protein is annotated as a Nonribosomal peptide synthetase / Lanomycin biosynthesis cluster protein 1 from Pyrenophora dematioidea. The underlying paper (Liu et al., JACS 2021) describes genome mining of CYP51-inhibitor biosynthetic gene clusters, providing experimental context for the antifungal pathway assignment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain signatures (e.g., 'TSGSTG' adenylation-domain motif, 'HHAMFDG' condensation-domain motif), which could allow identification as a nonribosomal peptide synthetase. NRPS enzymes are involved in secondary metabolite biosynthesis, which could help eliminate lipid metabolism (fatty acid synthases/desaturases), spheroidene biosynthesis (carotenoid desaturases/cyclases), and one-carbon metabolism (folate/methionine enzymes) as unlikely NRPS pathways. However, the specific assignment to 'antifungal' biosynthesis (vs. antibacterial, siderophore, immunosuppressant, or other NRPS-product pathways) cannot be derived from sequence features alone.",
    "missing_item_specific_fact": "Knowledge that this particular NRPS is part of the lanomycin biosynthetic gene cluster and that lanomycin is specifically an antifungal (CYP51 inhibitor) compound. The sequence provides no information distinguishing this NRPS's product as antifungal rather than antibacterial or another secondary metabolite class.",
    "reason": "While NRPS domain architecture recognition might narrow choices by eliminating clearly non-NRPS pathways (A, C, D), the specific pathway label 'Antifungal biosynthesis' requires item-specific knowledge of the gene cluster context and product bioactivity. NRPS enzymes produce diverse secondary metabolites; the antifungal designation is a database annotation derived from the underlying genomics paper, not a property inferable from the amino acid sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'Antifungal biosynthesis' is a secondary-metabolite/NRPS pathway. Lipid metabolism, spheroidene biosynthesis, and one-carbon metabolism are clearly distinct pathway classes not associated with NRPS enzymes. So if NRPS is recognized, B is the only viable option. However, this elimination still depends on the specific pathway taxonomy used by the benchmark."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-02-05; the benchmark construction date is unknown. If the benchmark was constructed before this date, the annotation source may differ.",
    "The pathway annotation carries evidence code ECO:0000305 (inferred from curator), though the underlying PubMed reference (33857369) provides experimental genome-mining support.",
    "The protein is 1325 AA, which is relatively small for a multi-module NRPS; it may represent a single module or a partial assembly line, which could complicate domain recognition.",
    "The reviewer-only evidence was not available to the evaluated model; the model only sees the raw sequence and four choices."
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

**Accession:** `P0DXV4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
"P0DXV4"
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Lanomycin biosynthesis cluster protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase"}}}
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"33857369","source":"PubMed"}],"value":"Antifungal biosynthesis"}]}
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"TTI-1096"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `6306f5ce87df5ee04db986988c948755e8b2c4fe4ace8282933e84b394cf62fd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV4?format=txt&versions=4)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
ID   LAN2_PYRDE              Reviewed;        1325 AA.
AC   P0DXV4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Nonribosomal peptide synthetase {ECO:0000303|PubMed:33857369};
DE            EC=6.3.2.- {ECO:0000305|PubMed:33857369};
DE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};
GN   Name=ORF2 {ECO:0000303|PubMed:33857369};
OS   Pyrenophora dematioidea (Helminthosporium dematioideum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;
OC   Pyrenophora.
OX   NCBI_TaxID=139229;
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV4?format=txt&versions=4)  
**Locator:** `lines 37-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
CC   -!- PATHWAY: Antifungal biosynthesis. {ECO:0000305|PubMed:33857369}.
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
