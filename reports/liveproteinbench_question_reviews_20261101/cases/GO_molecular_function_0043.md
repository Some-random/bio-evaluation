# GO_molecular_function_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — ligase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHISPSKDTPSQRLPIPLSLPTHLGLLAKAYGVPPASILQLAWGLVLRCYFTTSSSRWGTIDMAHEYKEKKNLPIRCEVLELDDTRSIGWILQNWNDPSVHRHLPAEEDTSNVPVSAGSIVILTEDAKDLEVLRDFELTAEWIICFSTSTEKPLLRLSWRPDVIHSELASHLAQLLERALDTTFLSPDIPLSQINLFSILDHQKLLQWNHQYPQSVNRLVHEMFEDMVAARPQATAVAAWDGEVTYQQLDRLSTRLAIKLQTIDLQPESIVALCFEKSVWAIVAMLGVLRAGGAFLHIDPKHPTARQQAMISTTAARIILCSEQTRDTVSRFDSESLSLVVDRKMFAQEPDHKQVALPSPNNLGPRNAAYIVCTSGSTGLPKAIVVEHVSLCTSVTAQAEAMAVGGESRILQYAAYTFDVSVGDVFTALTHGACVCIPSDWERTQDLVGAINRLDVNQACLTSTVASFLTPMNVPKLQKLTLGGEPASKQCIDLWSGKVALKNVYGPAECTVWCVIQKNASSEIPASNIGRGIGARTWIVHPENHNQLMPIGAVGELLIEGPLVARGYLNDAERTTAVFLERAPSWLATFGPLPPQTRFYKTGDLARFEQNGTLFFEGRKDTQVKLRGQRIELGEIEYQIQQACNPVPPLAVELIETKDLQAPLLGAFITWTGGLEISLDQSAVPNGLGPDLDARSHFNELVSRIQANIDRTLPPYMMPGLYIPVQKLPLSTSGKLDRKVLRQYCTQHTRSFLTASEAESSDVIADDATKDDVALHEIVNPGEITLAQLWAHALGRRMESINAKDNFLSLGGDSLAAMRLVNLAARDAQVTLTVANIFESPVLADQARLLRPLSKTKSLAPFELMTRGEASIEDIVGFAAQQCRLLPAQIEDVYPCTPLQEEMMRDSLSNDRTQMGQEVVQISEELDLVRYQVACASVYRRFPILRTRFIEHSGRLVQVVVREDLCWKQPTSLAEYKALDSRERPALGKPLTRWALTSDGTHFILSLHHAMFDGITLGQIQGAIYAVYQCIPLPPPSVSFATFLAHLDDQNAPLSQESQRFWQSYLCPSASLDASITPETQKIDRPRASCGTQRLVQFTSGEVSALQRHGLTEATLVRGAWACTLARHQQKPHASAFSDVIFGTMLTGRNFHLPGVDMLAAPSLTHVPIRIRIDEGDLNGHSARALLARVQADATAMIPYEHDGMNRIRSIEVQTRAVFNRIRTLLVIQPIPEGLTSVSTSPFPGSIVSGPRVEAKEMGHFHWYGLLVECTLLPTKGFFVRVSYDNKMFGTEQVESLLDDYSTTLHTLANGLMDTDIPASLHV

[Multiple Choices]
A. mRNA binding
B. ligase activity
C. mannose-6-phosphate isomerase activity
D. isomerase activity
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

> The exact sequence matches a UniProt entry annotated as a nonribosomal peptide synthetase with EC 6.3.2.-, consistent with ligase activity. Its GO ligase annotation is computational (IEA:UniProtKB-KW); the cited literature also supports its role in the lanomycin biosynthetic cluster, but does not by itself establish a specific catalytic reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has features consistent with a modular nonribosomal peptide synthetase, including an adenylation-domain-like motif and carrier-protein features. NRPS adenylation activates substrates using ATP, supporting ligase activity over mRNA binding or mannose-6-phosphate isomerase activity.


**Missing item-specific fact**

> The exact substrate and reaction are not specified by the sequence alone, but are not necessary to distinguish the broad ligase option from these alternatives.


**Reason**

> Sequence-based recognition of NRPS domain features provides a concrete family-level biological argument for ligase activity; the answer need not depend solely on recalling this protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied choices distinguish ligase activity from unrelated binding and isomerase functions; the sequence supports an NRPS interpretation and does not provide comparable support for the isomerase choices.


### Important caveats

- The database GO ligase annotation cited here is computationally assigned, not direct experimental evidence for a specific ligase reaction.
- The reviewer-only accession and annotations support assessment of the key but were not supplied to the original model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has features consistent with a modular nonribosomal peptide synthetase, including an adenylation-domain-like motif and carrier-protein features. NRPS adenylation activates substrates using ATP, supporting ligase activity over mRNA binding or mannose-6-phosphate isomerase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate and reaction are not specified by the sequence alone, but are not necessary to distinguish the broad ligase option from these alternatives.",
    "reason": "Sequence-based recognition of NRPS domain features provides a concrete family-level biological argument for ligase activity; the answer need not depend solely on recalling this protein's database annotation."
  },
  "case_id": "GO_molecular_function_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a nonribosomal peptide synthetase with EC 6.3.2.-, consistent with ligase activity. Its GO ligase annotation is computational (IEA:UniProtKB-KW); the cited literature also supports its role in the lanomycin biosynthetic cluster, but does not by itself establish a specific catalytic reaction."
  },
  "important_caveats": [
    "The database GO ligase annotation cited here is computationally assigned, not direct experimental evidence for a specific ligase reaction.",
    "The reviewer-only accession and annotations support assessment of the key but were not supplied to the original model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices distinguish ligase activity from unrelated binding and isomerase functions; the sequence supports an NRPS interpretation and does not provide comparable support for the isomerase choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a nonribosomal peptide synthetase with EC 6.3.2.-, consistent with ligase activity. Its GO ligase annotation is computational (IEA:UniProtKB-KW); the cited literature also supports its role in the lanomycin biosynthetic cluster, but does not by itself establish a specific catalytic reaction.",
    "evidence_ids": ["C4", "C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has features consistent with a modular nonribosomal peptide synthetase, including an adenylation-domain-like motif and carrier-protein features. NRPS adenylation activates substrates using ATP, supporting ligase activity over mRNA binding or mannose-6-phosphate isomerase activity.",
    "missing_item_specific_fact": "The exact substrate and reaction are not specified by the sequence alone, but are not necessary to distinguish the broad ligase option from these alternatives.",
    "reason": "Sequence-based recognition of NRPS domain features provides a concrete family-level biological argument for ligase activity; the answer need not depend solely on recalling this protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices distinguish ligase activity from unrelated binding and isomerase functions; the sequence supports an NRPS interpretation and does not provide comparable support for the isomerase choices."
  },
  "important_caveats": [
    "The database GO ligase annotation cited here is computationally assigned, not direct experimental evidence for a specific ligase reaction.",
    "The reviewer-only accession and annotations support assessment of the key but were not supplied to the original model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt P0DXV4 is annotated as a Nonribosomal peptide synthetase with EC 6.3.2.- (peptide synthetase), which falls squarely in EC class 6 (ligases). The UniProt entry carries GO:0016874 (ligase activity) via IEA:UniProtKB-KW (evidence H4). The functional description (PubMed:33857369) confirms NRPS activity involving ATP-dependent peptide bond formation (acylation with glycine to complete lanomycin biosynthesis). The EC number assignment and GO annotation are consistent and well-supported by the cited experimental study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 1325 amino acids long, far exceeding the typical size of mannose-6-phosphate isomerase (~250 aa, option C) or most small isomerases (option D). The sequence lacks recognizable RRM or other canonical RNA-binding motifs expected for mRNA binding (option A). The large multi-domain architecture, with identifiable phosphopantetheine-attachment-like motifs (GxxLxxLxxD patterns) and adenylation/condensation domain signatures, is characteristic of nonribosomal peptide synthetases. NRPS enzymes catalyze ATP-dependent amide bond formation (EC 6.3.2.-), which is ligation chemistry. Even without exact domain identification, the combination of very large size, multi-domain organization, and the absence of small-enzyme or RNA-binding signatures meaningfully favors ligase activity over isomerase or mRNA binding.


**Missing item-specific fact**

> Precise identification of NRPS adenylation (A), condensation (C), and peptidyl-carrier-protein (T/PCP) domain boundaries from raw sequence without specialized tools would strengthen the reasoning, but the general architectural clues (size, phosphopantetheine motifs, multi-domain organization) provide a defensible inference path.


**Reason**

> A knowledgeable model can reason from protein size (1325 aa eliminates small isomerases), absence of RNA-binding domain signatures (eliminates A), presence of phosphopantetheine-attachment-like motifs and multi-domain organization (suggesting a large biosynthetic enzyme performing ATP-dependent bond formation), to conclude ligase activity. The distractors are sufficiently distinct to allow meaningful discrimination through general structural and functional biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different functional classes: RNA binding (A), ligase (B), specific isomerase (C), and general isomerase (D). The protein's size, domain architecture, and EC class unambiguously point to B. Options C and D are both isomerase-related but neither matches a 1325-aa multi-domain NRPS. No two options are genuinely defensible for this sequence.


### Important caveats

- The GO:0016874 annotation in UniProt is IEA (Inferred from Electronic Annotation via keyword), not directly experimental. However, the EC 6.3.2.- assignment and the NRPS functional description are supported by the experimental study PubMed:33857369.
- The protein was first publicly released in UniProt on 2025-02-05, so this is a relatively recent annotation; the benchmark author's source snapshot date is unknown.
- Identifying NRPS domain signatures from raw sequence is specialized knowledge; a model without this training would rely primarily on size-based elimination of options C and D and absence of RNA-binding motifs for A.
- The GO annotation evidence code is IEA:UniProtKB-KW, meaning the ligase assignment is derived from the EC number keyword rather than a direct experimental GO curation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 1325 amino acids long, far exceeding the typical size of mannose-6-phosphate isomerase (~250 aa, option C) or most small isomerases (option D). The sequence lacks recognizable RRM or other canonical RNA-binding motifs expected for mRNA binding (option A). The large multi-domain architecture, with identifiable phosphopantetheine-attachment-like motifs (GxxLxxLxxD patterns) and adenylation/condensation domain signatures, is characteristic of nonribosomal peptide synthetases. NRPS enzymes catalyze ATP-dependent amide bond formation (EC 6.3.2.-), which is ligation chemistry. Even without exact domain identification, the combination of very large size, multi-domain organization, and the absence of small-enzyme or RNA-binding signatures meaningfully favors ligase activity over isomerase or mRNA binding.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of NRPS adenylation (A), condensation (C), and peptidyl-carrier-protein (T/PCP) domain boundaries from raw sequence without specialized tools would strengthen the reasoning, but the general architectural clues (size, phosphopantetheine motifs, multi-domain organization) provide a defensible inference path.",
    "reason": "A knowledgeable model can reason from protein size (1325 aa eliminates small isomerases), absence of RNA-binding domain signatures (eliminates A), presence of phosphopantetheine-attachment-like motifs and multi-domain organization (suggesting a large biosynthetic enzyme performing ATP-dependent bond formation), to conclude ligase activity. The distractors are sufficiently distinct to allow meaningful discrimination through general structural and functional biology knowledge."
  },
  "case_id": "GO_molecular_function_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt P0DXV4 is annotated as a Nonribosomal peptide synthetase with EC 6.3.2.- (peptide synthetase), which falls squarely in EC class 6 (ligases). The UniProt entry carries GO:0016874 (ligase activity) via IEA:UniProtKB-KW (evidence H4). The functional description (PubMed:33857369) confirms NRPS activity involving ATP-dependent peptide bond formation (acylation with glycine to complete lanomycin biosynthesis). The EC number assignment and GO annotation are consistent and well-supported by the cited experimental study."
  },
  "important_caveats": [
    "The GO:0016874 annotation in UniProt is IEA (Inferred from Electronic Annotation via keyword), not directly experimental. However, the EC 6.3.2.- assignment and the NRPS functional description are supported by the experimental study PubMed:33857369.",
    "The protein was first publicly released in UniProt on 2025-02-05, so this is a relatively recent annotation; the benchmark author's source snapshot date is unknown.",
    "Identifying NRPS domain signatures from raw sequence is specialized knowledge; a model without this training would rely primarily on size-based elimination of options C and D and absence of RNA-binding motifs for A.",
    "The GO annotation evidence code is IEA:UniProtKB-KW, meaning the ligase assignment is derived from the EC number keyword rather than a direct experimental GO curation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different functional classes: RNA binding (A), ligase (B), specific isomerase (C), and general isomerase (D). The protein's size, domain architecture, and EC class unambiguously point to B. Options C and D are both isomerase-related but neither matches a 1325-aa multi-domain NRPS. No two options are genuinely defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt P0DXV4 is annotated as a Nonribosomal peptide synthetase with EC 6.3.2.- (peptide synthetase), which falls squarely in EC class 6 (ligases). The UniProt entry carries GO:0016874 (ligase activity) via IEA:UniProtKB-KW (evidence H4). The functional description (PubMed:33857369) confirms NRPS activity involving ATP-dependent peptide bond formation (acylation with glycine to complete lanomycin biosynthesis). The EC number assignment and GO annotation are consistent and well-supported by the cited experimental study.",
    "evidence_ids": ["C4", "C5", "H1", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 1325 amino acids long, far exceeding the typical size of mannose-6-phosphate isomerase (~250 aa, option C) or most small isomerases (option D). The sequence lacks recognizable RRM or other canonical RNA-binding motifs expected for mRNA binding (option A). The large multi-domain architecture, with identifiable phosphopantetheine-attachment-like motifs (GxxLxxLxxD patterns) and adenylation/condensation domain signatures, is characteristic of nonribosomal peptide synthetases. NRPS enzymes catalyze ATP-dependent amide bond formation (EC 6.3.2.-), which is ligation chemistry. Even without exact domain identification, the combination of very large size, multi-domain organization, and the absence of small-enzyme or RNA-binding signatures meaningfully favors ligase activity over isomerase or mRNA binding.",
    "missing_item_specific_fact": "Precise identification of NRPS adenylation (A), condensation (C), and peptidyl-carrier-protein (T/PCP) domain boundaries from raw sequence without specialized tools would strengthen the reasoning, but the general architectural clues (size, phosphopantetheine motifs, multi-domain organization) provide a defensible inference path.",
    "reason": "A knowledgeable model can reason from protein size (1325 aa eliminates small isomerases), absence of RNA-binding domain signatures (eliminates A), presence of phosphopantetheine-attachment-like motifs and multi-domain organization (suggesting a large biosynthetic enzyme performing ATP-dependent bond formation), to conclude ligase activity. The distractors are sufficiently distinct to allow meaningful discrimination through general structural and functional biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different functional classes: RNA binding (A), ligase (B), specific isomerase (C), and general isomerase (D). The protein's size, domain architecture, and EC class unambiguously point to B. Options C and D are both isomerase-related but neither matches a 1325-aa multi-domain NRPS. No two options are genuinely defensible for this sequence."
  },
  "important_caveats": [
    "The GO:0016874 annotation in UniProt is IEA (Inferred from Electronic Annotation via keyword), not directly experimental. However, the EC 6.3.2.- assignment and the NRPS functional description are supported by the experimental study PubMed:33857369.",
    "The protein was first publicly released in UniProt on 2025-02-05, so this is a relatively recent annotation; the benchmark author's source snapshot date is unknown.",
    "Identifying NRPS domain signatures from raw sequence is specialized knowledge; a model without this training would rely primarily on size-based elimination of options C and D and absence of RNA-binding motifs for A.",
    "The GO annotation evidence code is IEA:UniProtKB-KW, meaning the ligase assignment is derived from the EC number keyword rather than a direct experimental GO curation."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:46.025798+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Nonribosomal peptide synthetase; part of the gene cluster that mediates the biosynthesis of the tetrahydropyranyl antifungal agent lanomycin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:33857369). The biosynthesis probably begins with the formation of an hexaketide, followed by methionine mediated alkylation of C-2 and C-6, and methylation of the reduced C-3 oxygen, pyran forming reductive ring closure, oxygenation of C-4, beta-keto reduction, enoyl reduction and dehydration of the remaining oxygens, and finally, acylation with glycine to complete the biosynthesis (Probable)"}]}
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
**Locator:** `lines 24-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
CC   -!- FUNCTION: Nonribosomal peptide synthetase; part of the gene cluster
CC       that mediates the biosynthesis of the tetrahydropyranyl antifungal
CC       agent lanomycin that acts as an inhibitor of CYP51 and blocks the
CC       ergosterol biosynthesis (PubMed:33857369). The biosynthesis probably
CC       begins with the formation of an hexaketide, followed by methionine
CC       mediated alkylation of C-2 and C-6, and methylation of the reduced C-3
CC       oxygen, pyran forming reductive ring closure, oxygenation of C-4, beta-
CC       keto reduction, enoyl reduction and dehydration of the remaining
CC       oxygens, and finally, acylation with glycine to complete the
CC       biosynthesis (Probable). {ECO:0000269|PubMed:33857369, ECO:0000305}.
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV4?format=txt&versions=4)  
**Locator:** `lines 57-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:48.541613+00:00.  

```text
DR   GO; GO:0016874; F:ligase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `ba16325a29b0d20c33cbeceb3d33ee2d578da70c3cbda9228dab9fae89b8c8fd`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 131127-131145`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016874
name: ligase activity
namespace: molecular_function
def: "Catalysis of the joining of two molecules, or two groups within a single molecule, using the energy from the hydrolysis of ATP, a similar triphosphate, or a pH gradient." [EC:6.-.-.-]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "synthetase activity" EXACT [GOC:jh2]
xref: EC:6.-.-.-
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:6.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
