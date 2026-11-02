# catalytic_activity_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
B. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
C. L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)
D. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
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

> The exact sequence matches the UniProt entry for FrzA, whose catalytic-activity annotation assigns the reaction in choice C and cites experimental evidence (ECO:0000269, PubMed 33372776). This supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large, multidomain enzyme, but its length and general sequence features do not establish the specific substrates and coupled reaction needed to distinguish choice C from the alternatives.


**Missing item-specific fact**

> The protein-specific catalytic assignment that FrzA catalyzes the L-tyrosinal-to-L-tyrosine reaction coupled to ATP formation and NADP reduction.


**Reason**

> Selecting C requires an annotation, experimental result, or protein-specific functional knowledge absent from the sequence and choices. General biological reasoning alone does not determine this precise reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence assigns the matched sequence to choice C; it does not support another listed reaction.


### Important caveats

- The evidence is a UniProt annotation citing a publication with experimental evidence; the primary paper was not independently validated.
- The exact author source snapshot is unknown, although the historical and current records both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large, multidomain enzyme, but its length and general sequence features do not establish the specific substrates and coupled reaction needed to distinguish choice C from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that FrzA catalyzes the L-tyrosinal-to-L-tyrosine reaction coupled to ATP formation and NADP reduction.",
    "reason": "Selecting C requires an annotation, experimental result, or protein-specific functional knowledge absent from the sequence and choices. General biological reasoning alone does not determine this precise reaction."
  },
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for FrzA, whose catalytic-activity annotation assigns the reaction in choice C and cites experimental evidence (ECO:0000269, PubMed 33372776). This supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The evidence is a UniProt annotation citing a publication with experimental evidence; the primary paper was not independently validated.",
    "The exact author source snapshot is unknown, although the historical and current records both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence assigns the matched sequence to choice C; it does not support another listed reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for FrzA, whose catalytic-activity annotation assigns the reaction in choice C and cites experimental evidence (ECO:0000269, PubMed 33372776). This supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large, multidomain enzyme, but its length and general sequence features do not establish the specific substrates and coupled reaction needed to distinguish choice C from the alternatives.",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that FrzA catalyzes the L-tyrosinal-to-L-tyrosine reaction coupled to ATP formation and NADP reduction.",
    "reason": "Selecting C requires an annotation, experimental result, or protein-specific functional knowledge absent from the sequence and choices. General biological reasoning alone does not determine this precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence assigns the matched sequence to choice C; it does not support another listed reaction."
  },
  "important_caveats": [
    "The evidence is a UniProt annotation citing a publication with experimental evidence; the primary paper was not independently validated.",
    "The exact author source snapshot is unknown, although the historical and current records both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7T8F1L4 (FRZA_CLASX), whose sequence matches the supplied sequence exactly (SHA256 confirmed), annotates the catalytic activity as 'L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS). The reaction text in Choice C matches the annotation verbatim. The physiological direction is right-to-left (RHEA:57414), consistent with the enzyme physiologically reducing L-tyrosine to L-tyrosinal.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable NRPS (nonribosomal peptide synthetase) domain architecture: adenylation (A) domain motifs (e.g., 'GADVLCIDDFDIADL' corresponding to A7 motif; 'GGSCAPMD' near A1), a peptidyl carrier protein (PCP) domain motif ('GDEGGESDQGELWIGGPGVSPGY'), and a C-terminal NAD(P)H-dependent reductase domain. The A-PCP-R module architecture is the hallmark of NRPS reductase domains that convert amino acids to aldehydes using NADPH with coupled ATP→AMP+PPi activation. Among the four choices, only C describes this exact reaction class (amino acid ↔ amino aldehyde, NADPH/NADP+, AMP/ATP/PPi). Choices A (SAM-dependent O-methyltransferase), B (NAD-dependent UDP-sugar oxidase), and D (dolichol-linked mannosyltransferase) involve entirely unrelated enzyme classes and cofactor chemistries inconsistent with the observed domain architecture.


**Missing item-specific fact**

> The precise substrate identity (L-tyrosine vs. another amino acid) would require reading the A-domain specificity-conferring code (8-10 residues in the binding pocket), which is difficult to extract reliably from raw sequence without specialized NRPS prediction tools. However, this is not needed to select C, because the reaction type alone eliminates all other choices.


**Reason**

> A model with knowledge of NRPS domain architecture can identify the A-PCP-R module from conserved sequence motifs, infer that the enzyme catalyzes amino acid→aldehyde reduction with NADPH and AMP/PPi coupling, and eliminate the three non-NRPS distractors. The specific substrate (tyrosine) is harder to confirm from sequence alone, but the reaction class is sufficient to uniquely select C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes (methyltransferase, oxidase, NRPS reductase, glycosyltransferase). The NRPS domain architecture in the sequence uniquely points to C; no other choice is consistent with the observed A-PCP-R module.


### Important caveats

- The physiological direction is right-to-left (L-tyrosine → L-tyrosinal), but the reaction as written in Choice C matches the UniProt annotation format exactly, so the expected answer is textually correct.
- Identifying the specific substrate as L-tyrosine (rather than another amino acid) from sequence alone would require A-domain specificity code analysis, which is beyond general reasoning; however, this specificity is not needed to distinguish C from the other choices.
- The evidence code ECO:0000269 indicates experimental (protein-level) evidence from the 2021 JACS paper, not computational inference.
- The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown, but the sequence has been unchanged since 2021-06-02.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS (nonribosomal peptide synthetase) domain architecture: adenylation (A) domain motifs (e.g., 'GADVLCIDDFDIADL' corresponding to A7 motif; 'GGSCAPMD' near A1), a peptidyl carrier protein (PCP) domain motif ('GDEGGESDQGELWIGGPGVSPGY'), and a C-terminal NAD(P)H-dependent reductase domain. The A-PCP-R module architecture is the hallmark of NRPS reductase domains that convert amino acids to aldehydes using NADPH with coupled ATP→AMP+PPi activation. Among the four choices, only C describes this exact reaction class (amino acid ↔ amino aldehyde, NADPH/NADP+, AMP/ATP/PPi). Choices A (SAM-dependent O-methyltransferase), B (NAD-dependent UDP-sugar oxidase), and D (dolichol-linked mannosyltransferase) involve entirely unrelated enzyme classes and cofactor chemistries inconsistent with the observed domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise substrate identity (L-tyrosine vs. another amino acid) would require reading the A-domain specificity-conferring code (8-10 residues in the binding pocket), which is difficult to extract reliably from raw sequence without specialized NRPS prediction tools. However, this is not needed to select C, because the reaction type alone eliminates all other choices.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A-PCP-R module from conserved sequence motifs, infer that the enzyme catalyzes amino acid→aldehyde reduction with NADPH and AMP/PPi coupling, and eliminate the three non-NRPS distractors. The specific substrate (tyrosine) is harder to confirm from sequence alone, but the reaction class is sufficient to uniquely select C."
  },
  "case_id": "catalytic_activity_0067",
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
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX), whose sequence matches the supplied sequence exactly (SHA256 confirmed), annotates the catalytic activity as 'L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS). The reaction text in Choice C matches the annotation verbatim. The physiological direction is right-to-left (RHEA:57414), consistent with the enzyme physiologically reducing L-tyrosine to L-tyrosinal."
  },
  "important_caveats": [
    "The physiological direction is right-to-left (L-tyrosine → L-tyrosinal), but the reaction as written in Choice C matches the UniProt annotation format exactly, so the expected answer is textually correct.",
    "Identifying the specific substrate as L-tyrosine (rather than another amino acid) from sequence alone would require A-domain specificity code analysis, which is beyond general reasoning; however, this specificity is not needed to distinguish C from the other choices.",
    "The evidence code ECO:0000269 indicates experimental (protein-level) evidence from the 2021 JACS paper, not computational inference.",
    "The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown, but the sequence has been unchanged since 2021-06-02."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (methyltransferase, oxidase, NRPS reductase, glycosyltransferase). The NRPS domain architecture in the sequence uniquely points to C; no other choice is consistent with the observed A-PCP-R module."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX), whose sequence matches the supplied sequence exactly (SHA256 confirmed), annotates the catalytic activity as 'L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)' with EC 1.2.1.101, supported by experimental evidence (ECO:0000269|PubMed:33372776, Zhang et al. 2021 JACS). The reaction text in Choice C matches the annotation verbatim. The physiological direction is right-to-left (RHEA:57414), consistent with the enzyme physiologically reducing L-tyrosine to L-tyrosinal.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS (nonribosomal peptide synthetase) domain architecture: adenylation (A) domain motifs (e.g., 'GADVLCIDDFDIADL' corresponding to A7 motif; 'GGSCAPMD' near A1), a peptidyl carrier protein (PCP) domain motif ('GDEGGESDQGELWIGGPGVSPGY'), and a C-terminal NAD(P)H-dependent reductase domain. The A-PCP-R module architecture is the hallmark of NRPS reductase domains that convert amino acids to aldehydes using NADPH with coupled ATP→AMP+PPi activation. Among the four choices, only C describes this exact reaction class (amino acid ↔ amino aldehyde, NADPH/NADP+, AMP/ATP/PPi). Choices A (SAM-dependent O-methyltransferase), B (NAD-dependent UDP-sugar oxidase), and D (dolichol-linked mannosyltransferase) involve entirely unrelated enzyme classes and cofactor chemistries inconsistent with the observed domain architecture.",
    "missing_item_specific_fact": "The precise substrate identity (L-tyrosine vs. another amino acid) would require reading the A-domain specificity-conferring code (8-10 residues in the binding pocket), which is difficult to extract reliably from raw sequence without specialized NRPS prediction tools. However, this is not needed to select C, because the reaction type alone eliminates all other choices.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A-PCP-R module from conserved sequence motifs, infer that the enzyme catalyzes amino acid→aldehyde reduction with NADPH and AMP/PPi coupling, and eliminate the three non-NRPS distractors. The specific substrate (tyrosine) is harder to confirm from sequence alone, but the reaction class is sufficient to uniquely select C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (methyltransferase, oxidase, NRPS reductase, glycosyltransferase). The NRPS domain architecture in the sequence uniquely points to C; no other choice is consistent with the observed A-PCP-R module."
  },
  "important_caveats": [
    "The physiological direction is right-to-left (L-tyrosine → L-tyrosinal), but the reaction as written in Choice C matches the UniProt annotation format exactly, so the expected answer is textually correct.",
    "Identifying the specific substrate as L-tyrosine (rather than another amino acid) from sequence alone would require A-domain specificity code analysis, which is beyond general reasoning; however, this specificity is not needed to distinguish C from the other choices.",
    "The evidence code ECO:0000269 indicates experimental (protein-level) evidence from the 2021 JACS paper, not computational inference.",
    "The UniProt entry was first public in 2025-06-18; the benchmark author's source snapshot is unknown, but the sequence has been unchanged since 2021-06-02."
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

**Accession:** `A0A7T8F1L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
"A0A7T8F1L4"
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.2.1.101"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Non-canonical nonribosomal peptide synthetase FrzA"}}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:57414"}}],"reaction":{"ecNumber":"1.2.1.101","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"name":"L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:57412"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58315"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:141668"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
ID   FRZA_CLASX              Reviewed;        1024 AA.
AC   A0A7T8F1L4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 18.
DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};
DE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};
GN   Name=FrzA {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};
DE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   PATHWAY.
RC   STRAIN=11231;
RX   PubMed=33372776; DOI=10.1021/jacs.0c12352;
RA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,
RA   Taniguchi M., Watanabe K., Tang Y.;
RT   "Biosynthesis of the Immunosuppressant (-)-FR901483.";
RL   J. Am. Chem. Soc. 143:132-136(2021).
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 53-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP +
CC         NADPH + H(+); Xref=Rhea:RHEA:57412, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58315, ChEBI:CHEBI:58349, ChEBI:CHEBI:141668,
CC         ChEBI:CHEBI:456215; EC=1.2.1.101;
CC         Evidence={ECO:0000269|PubMed:33372776};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:57414;
CC         Evidence={ECO:0000269|PubMed:33372776};
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
