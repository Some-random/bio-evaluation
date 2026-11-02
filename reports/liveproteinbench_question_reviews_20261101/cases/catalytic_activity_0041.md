# catalytic_activity_0041

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — restrictinol + glycine + H(+) = restricticin + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSHSSHYSPVDSGMVPSSSSTEDHLSPTLSASIVLPAQLNPFAKAYDIPPSSIVQLGWALLLRCHLAIPSPCWSTIDDKTMPRGSDTHALQWESLHLEEGRSISWILQRWEDPSVHWYLSSDQLPGSKSPTLTTMLFLVKEYGLFDPVTPIDPGMGTIIYFYPSDEQPRLHISWNPDVVSSGHAFHLTRSLEHALQTIFLAPSVDIRDVNLFGIWDHQQLLQWNSYCPDPVDRLVQEMFQDVVAATPEASAVAAWDGELNYRELDRLSSRLAGVLQSDFGVVSETIVALCFEKSVWAIVAMLAVVKAGGAFLHIDPQHPPARHQAMIKSTASKLFLCSEQTRDTVVRSVPDCPSLVIHREMFAAQPDHAQQDTVISSGNLGPTNAAYVVCTSGSTGTPKAIVVEHVSLCSSVTAQAKAMDITAGSRVLQYAAYTFDVSIGDIFAALTHGACICIPSNWERAHDLSGAINRLGVNQACLTSTVASLLTPVEVPKLKKLTLGGEPATQQCINMWVDKVALKNIYGPAECTVWCIIQPDVSSGIAVSNIGHAIGARAWIVHPENHDRLMPIGAVGELLIEGPLVARGYLNDPVRTNAVFLAQPPIWLASFGPPPPRSRFYKTGDLARYGPGGALLFEGRKDTQVKLRGQRIELGEVEYRLHQALSDLSPSAAVELVHPKESTAPLLCAFITWDEGIDLDLQPAKPPLSACLTPNARKRFNHTVSLLQTEMERTLPAYMIPGLCIPVHKLPLTTSGKLDRKALRYFCTQHSLAFLSTFENNNVNSPTDGATDSFAAPLETVSPAESTLAQLWAQVLGRKTDSIGRKDNFLSLGGDSLAAMRLVNRAARDAQLTLTVADVFKCPVLADQASLVRPLVQTRNLVPFELMAPGDLQIEDLVAYVAEKCGVLHDQVEDIYPCTPLQDEMMRDSLSGDRTQMGQEVILLAEDLDIPRYLSACARVFQRFPILRTRFVQHSDRLIQVVIRENLGWQRPESLTEYVEADAKEAPALNKPLTRWALTSDSTHCILTMHHSIFDGISLGHILGAIYAVYQSIPLPPDSVSFAAFLAQINEHTSGLSDDSKQFWRSYLRPSPGSGDLPLPIVDSTYRPCANRGTQRLVTFQSGVVPALQQHGLTEATLIRGAWACTLAQLQTSSSTPSDVVFGTILTGRNLHLPGVDALVAPTLTHAPIRIRMSAASNEKPASFLARVQADATAMIPFEHDGMDRIRAIDAQVRAVCDQMQTLLVIQPIPEGLTSASTSPFPGPILSGPRVEAREMRHFHWYGLLVECTLLPTNGFFVRMCYDDKLFSSEDVERLLDDYSQALHELGGGLTEGEEVHLPTERKLDTLTLPGLVAPSGAEDMV

[Multiple Choices]
A. a beta-lactam + H2O = a substituted beta-amino acid
B. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
C. restrictinol + glycine + H(+) = restricticin + H2O
D. 2-oxospirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = 2,2'-dioxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the annotated protein, and both current and archived UniProt records list the restrictinol + glycine reaction with ECO:0000269 evidence linked to PubMed 33857369. This supports C as an experimentally supported annotation, though the cited paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain sequence has features consistent with a nonribosomal peptide synthetase, including adenylation, carrier-protein, and condensation-type regions. Among the options, C is the peptide-forming ligation of glycine to a natural-product substrate; the other choices describe hydrolysis, methyl transfer, or oxidation.


**Missing item-specific fact**

> The sequence alone does not establish the exact substrate identity restrictinol or independently specify the product restricticin; those exact names are not encoded transparently in the input.


**Reason**

> The sequence and choices provide a meaningful enzyme-class argument for selecting C over the alternatives, even though the exact substrate-specific reaction would require additional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions represent distinct enzyme classes, and the sequence's NRPS-like features favor the ligation reaction in C.


### Important caveats

- The reviewer-only database annotation supports the expected answer but was not supplied to the evaluated model.
- The cited catalytic-activity annotation is linked to a publication and carries an experimental evidence code; the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence has features consistent with a nonribosomal peptide synthetase, including adenylation, carrier-protein, and condensation-type regions. Among the options, C is the peptide-forming ligation of glycine to a natural-product substrate; the other choices describe hydrolysis, methyl transfer, or oxidation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the exact substrate identity restrictinol or independently specify the product restricticin; those exact names are not encoded transparently in the input.",
    "reason": "The sequence and choices provide a meaningful enzyme-class argument for selecting C over the alternatives, even though the exact substrate-specific reaction would require additional information."
  },
  "case_id": "catalytic_activity_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein, and both current and archived UniProt records list the restrictinol + glycine reaction with ECO:0000269 evidence linked to PubMed 33857369. This supports C as an experimentally supported annotation, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the expected answer but was not supplied to the evaluated model.",
    "The cited catalytic-activity annotation is linked to a publication and carries an experimental evidence code; the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions represent distinct enzyme classes, and the sequence's NRPS-like features favor the ligation reaction in C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated protein, and both current and archived UniProt records list the restrictinol + glycine reaction with ECO:0000269 evidence linked to PubMed 33857369. This supports C as an experimentally supported annotation, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain sequence has features consistent with a nonribosomal peptide synthetase, including adenylation, carrier-protein, and condensation-type regions. Among the options, C is the peptide-forming ligation of glycine to a natural-product substrate; the other choices describe hydrolysis, methyl transfer, or oxidation.",
    "missing_item_specific_fact": "The sequence alone does not establish the exact substrate identity restrictinol or independently specify the product restricticin; those exact names are not encoded transparently in the input.",
    "reason": "The sequence and choices provide a meaningful enzyme-class argument for selecting C over the alternatives, even though the exact substrate-specific reaction would require additional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions represent distinct enzyme classes, and the sequence's NRPS-like features favor the ligation reaction in C."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the expected answer but was not supplied to the evaluated model.",
    "The cited catalytic-activity annotation is linked to a publication and carries an experimental evidence code; the primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied protein sequence (1358 AA, SHA256 match) corresponds to UniProt entry A0A0L1JF11 (RSTN8_ASPN3), annotated as 'Nonribosomal peptide synthetase rstn8' with EC 6.3.2.-. The CATALYTIC ACTIVITY comment explicitly states 'restrictinol + glycine + H(+) = restricticin + H2O' (RHEA:81535), supported by experimental evidence (ECO:0000269, PubMed:33857369, JACS 2021). The expected answer matches this annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable NRPS domain motifs: the adenylation-domain signature 'SGSTGTPKAIVVEHV' (~position 405), the PCP/thiolation-domain 'GDS' motif in 'GDSLAAM' (~position 1050), and condensation-domain features 'GPGGALLFEG' (~position 750). These are well-established hallmarks of nonribosomal peptide synthetases (EC 6.3.x.x, ligases forming C–N bonds). Among the four choices, only option C represents a ligase/peptide-bond-forming reaction; options A (hydrolase/beta-lactamase), B (methyltransferase), and D (ferredoxin-dependent oxidoreductase) belong to entirely different EC classes with distinct domain architectures absent from this sequence. Identifying the enzyme as an NRPS/ligase is sufficient to eliminate A, B, and D.


**Missing item-specific fact**

> The specific substrate names (restrictinol, glycine, restricticin) and the identity of glycine as the activated amino acid require pathway-specific knowledge or adenylation-domain specificity-code analysis not trivially derivable from the raw sequence. However, this specificity is not needed to distinguish among the four choices, which differ at the enzyme-class level.


**Reason**

> The NRPS domain architecture (SGSTG adenylation motif, GDS PCP motif, C-domain features) is general, well-characterized biochemical knowledge that allows a knowledgeable reader to classify the enzyme as a peptide synthetase/ligase. Since the four options span four distinct enzyme classes (hydrolase, transferase, ligase, oxidoreductase), class-level identification uniquely selects option C without requiring memorization of this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four clearly distinct enzyme classes (EC 3 hydrolase, EC 2 transferase, EC 6 ligase, EC 1 oxidoreductase). Once the enzyme is identified as a peptide synthetase/ligase via NRPS domain motifs, only option C is consistent. No other option is defensible.


### Important caveats

- The specific substrate identity (glycine as the activated amino acid, restrictinol as the acceptor) is protein-pathway-specific and not derivable from general sequence features alone; however, the question's four-way choice is resolvable at the enzyme-class level.
- The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2021 JACS paper, not merely computational prediction.
- The sequence is 1358 AA, shorter than a full multi-module NRPS; it likely represents a single-module or tailoring component of the restricticin biosynthetic cluster, consistent with the 'cluster protein 8' designation.
- Recognition of NRPS motifs (SGSTG, GDS) is specialized but falls within standard biochemistry/secondary-metabolism knowledge rather than item-specific memorization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain motifs: the adenylation-domain signature 'SGSTGTPKAIVVEHV' (~position 405), the PCP/thiolation-domain 'GDS' motif in 'GDSLAAM' (~position 1050), and condensation-domain features 'GPGGALLFEG' (~position 750). These are well-established hallmarks of nonribosomal peptide synthetases (EC 6.3.x.x, ligases forming C–N bonds). Among the four choices, only option C represents a ligase/peptide-bond-forming reaction; options A (hydrolase/beta-lactamase), B (methyltransferase), and D (ferredoxin-dependent oxidoreductase) belong to entirely different EC classes with distinct domain architectures absent from this sequence. Identifying the enzyme as an NRPS/ligase is sufficient to eliminate A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate names (restrictinol, glycine, restricticin) and the identity of glycine as the activated amino acid require pathway-specific knowledge or adenylation-domain specificity-code analysis not trivially derivable from the raw sequence. However, this specificity is not needed to distinguish among the four choices, which differ at the enzyme-class level.",
    "reason": "The NRPS domain architecture (SGSTG adenylation motif, GDS PCP motif, C-domain features) is general, well-characterized biochemical knowledge that allows a knowledgeable reader to classify the enzyme as a peptide synthetase/ligase. Since the four options span four distinct enzyme classes (hydrolase, transferase, ligase, oxidoreductase), class-level identification uniquely selects option C without requiring memorization of this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied protein sequence (1358 AA, SHA256 match) corresponds to UniProt entry A0A0L1JF11 (RSTN8_ASPN3), annotated as 'Nonribosomal peptide synthetase rstn8' with EC 6.3.2.-. The CATALYTIC ACTIVITY comment explicitly states 'restrictinol + glycine + H(+) = restricticin + H2O' (RHEA:81535), supported by experimental evidence (ECO:0000269, PubMed:33857369, JACS 2021). The expected answer matches this annotation exactly."
  },
  "important_caveats": [
    "The specific substrate identity (glycine as the activated amino acid, restrictinol as the acceptor) is protein-pathway-specific and not derivable from general sequence features alone; however, the question's four-way choice is resolvable at the enzyme-class level.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2021 JACS paper, not merely computational prediction.",
    "The sequence is 1358 AA, shorter than a full multi-module NRPS; it likely represents a single-module or tailoring component of the restricticin biosynthetic cluster, consistent with the 'cluster protein 8' designation.",
    "Recognition of NRPS motifs (SGSTG, GDS) is specialized but falls within standard biochemistry/secondary-metabolism knowledge rather than item-specific memorization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four clearly distinct enzyme classes (EC 3 hydrolase, EC 2 transferase, EC 6 ligase, EC 1 oxidoreductase). Once the enzyme is identified as a peptide synthetase/ligase via NRPS domain motifs, only option C is consistent. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied protein sequence (1358 AA, SHA256 match) corresponds to UniProt entry A0A0L1JF11 (RSTN8_ASPN3), annotated as 'Nonribosomal peptide synthetase rstn8' with EC 6.3.2.-. The CATALYTIC ACTIVITY comment explicitly states 'restrictinol + glycine + H(+) = restricticin + H2O' (RHEA:81535), supported by experimental evidence (ECO:0000269, PubMed:33857369, JACS 2021). The expected answer matches this annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS domain motifs: the adenylation-domain signature 'SGSTGTPKAIVVEHV' (~position 405), the PCP/thiolation-domain 'GDS' motif in 'GDSLAAM' (~position 1050), and condensation-domain features 'GPGGALLFEG' (~position 750). These are well-established hallmarks of nonribosomal peptide synthetases (EC 6.3.x.x, ligases forming C–N bonds). Among the four choices, only option C represents a ligase/peptide-bond-forming reaction; options A (hydrolase/beta-lactamase), B (methyltransferase), and D (ferredoxin-dependent oxidoreductase) belong to entirely different EC classes with distinct domain architectures absent from this sequence. Identifying the enzyme as an NRPS/ligase is sufficient to eliminate A, B, and D.",
    "missing_item_specific_fact": "The specific substrate names (restrictinol, glycine, restricticin) and the identity of glycine as the activated amino acid require pathway-specific knowledge or adenylation-domain specificity-code analysis not trivially derivable from the raw sequence. However, this specificity is not needed to distinguish among the four choices, which differ at the enzyme-class level.",
    "reason": "The NRPS domain architecture (SGSTG adenylation motif, GDS PCP motif, C-domain features) is general, well-characterized biochemical knowledge that allows a knowledgeable reader to classify the enzyme as a peptide synthetase/ligase. Since the four options span four distinct enzyme classes (hydrolase, transferase, ligase, oxidoreductase), class-level identification uniquely selects option C without requiring memorization of this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four clearly distinct enzyme classes (EC 3 hydrolase, EC 2 transferase, EC 6 ligase, EC 1 oxidoreductase). Once the enzyme is identified as a peptide synthetase/ligase via NRPS domain motifs, only option C is consistent. No other option is defensible."
  },
  "important_caveats": [
    "The specific substrate identity (glycine as the activated amino acid, restrictinol as the acceptor) is protein-pathway-specific and not derivable from general sequence features alone; however, the question's four-way choice is resolvable at the enzyme-class level.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2021 JACS paper, not merely computational prediction.",
    "The sequence is 1358 AA, shorter than a full multi-module NRPS; it likely represents a single-module or tailoring component of the restricticin biosynthetic cluster, consistent with the 'cluster protein 8' designation.",
    "Recognition of NRPS motifs (SGSTG, GDS) is specialized but falls within standard biochemistry/secondary-metabolism knowledge rather than item-specific memorization."
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

**Accession:** `A0A0L1JF11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
"A0A0L1JF11"
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 8"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase rstn8"}}}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81536"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"name":"restrictinol + glycine + H(+) = restricticin + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81535"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57305"},{"database":"ChEBI","id":"CHEBI:231923"},{"database":"ChEBI","id":"CHEBI:231924"}]}}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY"]}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
ID   RSTN8_ASPN3             Reviewed;        1358 AA.
AC   A0A0L1JF11;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 41.
DE   RecName: Full=Nonribosomal peptide synthetase rstn8 {ECO:0000303|PubMed:33857369};
DE            EC=6.3.2.- {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 8 {ECO:0000303|PubMed:33857369};
GN   Name=rstn8 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001447;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
DE   RecName: Full=Nonribosomal peptide synthetase rstn8 {ECO:0000303|PubMed:33857369};
DE            EC=6.3.2.- {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 8 {ECO:0000303|PubMed:33857369};
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
RN   [2]
RP   FUNCTION, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 55-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=restrictinol + glycine + H(+) = restricticin + H2O;
CC         Xref=Rhea:RHEA:81535, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57305, ChEBI:CHEBI:231923, ChEBI:CHEBI:231924;
CC         Evidence={ECO:0000269|PubMed:33857369};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81536;
CC         Evidence={ECO:0000269|PubMed:33857369};
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
