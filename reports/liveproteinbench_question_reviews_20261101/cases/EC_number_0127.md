# EC_number_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDGTGITLGPSKLDSKPTSLDSQQHVADKRWLATVGHYKHLAGATESTRDVSLLEERAQHRVNAQETNQRRTIFQRLLNLLRRRERDGEVSGSAADSSSRPRLSVRQRLAQLWRRAKSLFKRGIRRYFPQGRNRQRSLRAQRRRSELVFEKADSGCVIGKRILAHMQEQIGQPQALENSERLDRILTVAAWPPDVPKRFVSVTTGETRTLVRGAPLGSGGFATVYEATDVETNEELAVKVFMSEKEPTDETMLDLQRESSCYRNFSLAKTAKDAQESCRFMVPSDVVMLEGQPASTEVVIGLTTRWVPNYFLLMMRAEADMSKVISWVFGDASVNKSEFGLVVRMYLSSQAIKLVANVQAQGIVHTDIKPANFLLLKDGRLFLGDFGTYRINNSVGRAIGTPGYEPPERPFQATGITYTFPTDAWQLGITLYCIWCKERPTPADGIWDYLHFADCPSTPELVQDLIRSLLNRDPQKRMLPLQALETAAFKEMDSVVKGAAQNFEQQEHLHTE

[Multiple Choices]
A. 2.7.13.3
B. 2.8.1.7
C. 2.7.11.24
D. 2.7.11.1
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.


**Missing item-specific fact**

> The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.


**Reason**

> The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1.


### Important caveats

- The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.
- The exact sequence match is established, but the author's original database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.",
    "reason": "The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation)."
  },
  "important_caveats": [
    "The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.",
    "The exact sequence match is established, but the author's original database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 554-aa UniProt Q2PAY2 sequence. Its annotated EC number is 2.7.11.1, with catalytic-activity annotations for serine and threonine phosphorylation citing experimental evidence (alongside a curator-evidence citation).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain, which supports kinase activity and makes the kinase choices plausible. That alone does not establish this protein's precise substrate specificity or distinguish the broad serine/threonine kinase EC number from a more specific kinase subclass.",
    "missing_item_specific_fact": "The protein-specific functional assignment that ROP18 phosphorylates protein serine and threonine residues, needed to establish EC 2.7.11.1 rather than merely infer kinase activity.",
    "reason": "The exact EC assignment is supported by reviewer-only database and cited experimental evidence, but that annotation and the relevant functional measurements are absent from the question. Recognizing the kinase fold does not supply the item-specific specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D for this sequence. The other kinase choices describe different substrate or enzyme subclasses; the sequence alone may not decisively rule them out, but the supplied reviewer-only evidence identifies the protein's EC number as 2.7.11.1."
  },
  "important_caveats": [
    "The UniProt entry is a database annotation supported by cited publications; the primary papers were not independently reviewed here.",
    "The exact sequence match is established, but the author's original database snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [C11](#evidence-c11), [H1](#evidence-h1), [H2](#evidence-h2), [H8](#evidence-h8), [H9](#evidence-h9), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.


**Missing item-specific fact**

> None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.


**Reason**

> The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice.


### Important caveats

- The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.
- Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.
- EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.
- The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.",
    "reason": "The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup."
  },
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "C11",
      "H1",
      "H2",
      "H8",
      "H9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference."
  },
  "important_caveats": [
    "The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.",
    "Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.",
    "EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.",
    "The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2PAY2 (ROP18_TOXGO) assigns EC 2.7.11.1 with multiple experimental evidence codes (ECO:0000269 direct assay from PubMed 21147463, 21203588, 24129568; ECO:0000305 from PubMed 23144612). Catalytic activities are documented for both threonyl and seryl phosphorylation of protein substrates using ATP. X-ray crystallography (PDB 4JRN) confirms the kinase domain structure with ATP-analog and Mg²⁺ binding. The sequence matches exactly (SHA-256 confirmed). The evidence is experimental, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "C11", "H1", "H2", "H8", "H9", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: a glycine-rich loop (GTPGYEPPER region), the DFG motif (GDFGTYRIN), and a catalytic loop (GKRILAH). These identify it as a protein kinase, eliminating B (2.8.1.7, cystine synthase, a transferase unrelated to phosphorylation). The catalytic architecture is Ser/Thr-type (aspartate in catalytic loop, activation loop), eliminating A (2.7.13.3, histidine kinase, which uses a His-Asp phosphorelay mechanism and lacks the bilobal kinase fold). To distinguish C (2.7.11.24, CDK) from D (2.7.11.1, non-specific Ser/Thr kinase): CDKs are ~300 aa standalone proteins with the PSTAIRE helix-C motif, cyclin-binding interfaces, and cell-cycle regulatory context. This protein is 554 aa with an N-terminal signal peptide (MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNV…) indicating secretion, belongs to the rhoptry kinase family of a parasitic apicomplexan, and lacks CDK-specific sequence signatures. These general architectural and contextual features argue against CDK classification, leaving 2.7.11.1 as the appropriate non-specific Ser/Thr kinase EC number.",
    "missing_item_specific_fact": "None strictly required. Distinguishing C from D relies on general knowledge of CDK structural signatures (PSTAIRE, cyclin-binding, ~300 aa standalone domain) and recognizing the signal peptide and multi-domain architecture as incompatible with CDK classification.",
    "reason": "The sequence provides identifiable kinase motifs that support protein kinase classification, and the overall architecture (signal peptide, 554 aa length, parasitic origin, absence of CDK-specific motifs) provides biological grounds to eliminate CDK (C) in favor of non-specific Ser/Thr kinase (D). This is general kinase-family knowledge rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (histidine kinase) and B (cystine synthase) are clearly eliminated by the kinase fold and Ser/Thr catalytic mechanism. Option C (CDK) is eliminated by the absence of CDK-specific features and the presence of a secretion signal peptide. Option D is the only remaining defensible choice."
  },
  "important_caveats": [
    "The reviewer evidence confirms the EC assignment experimentally, but the evaluated model only sees the raw sequence and four options.",
    "Distinguishing 2.7.11.1 from 2.7.11.24 requires familiarity with CDK-specific sequence/structural signatures; a model lacking this knowledge might struggle between C and D.",
    "EC 2.7.11.1 is a broad 'non-specific' catch-all category; the assignment reflects the absence of a more specific EC entry rather than a unique mechanistic distinction.",
    "The signal peptide at the N-terminus is a general eukaryotic secretion signal and does not uniquely identify ROP18; it simply argues against a nuclear/cytoplasmic cell-cycle kinase."
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

**Accession:** `Q2PAY2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
"Q2PAY2"
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AFO54811.1","source":"EMBL"}],"value":"Rhoptry kinase family protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAJ27113.1","source":"EMBL"}],"value":"Rhoptry protein 18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"KAF4642700.1","source":"EMBL"}],"value":"Rhoptry protein ROP18"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21147463","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21203588","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24129568","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23144612","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19266027","source":"PubMed"}],"value":"Serine/threonine-protein kinase ROP18"}}}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000269","id":"21147463","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21203588","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24129568","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23144612","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"23144612","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Fentress S.J.","Behnke M.S.","Dunay I.R.","Mashayekhi M.","Rommereim L.M.","Fox B.A.","Bzik D.J.","Taylor G.A.","Turk B.E.","Lichti C.F.","Townsend R.R.","Qiu W.","Hui R.","Beatty W.L.","Sibley L.D."],"citationCrossReferences":[{"database":"PubMed","id":"21147463"},{"database":"DOI","id":"10.1016/j.chom.2010.11.005"}],"citationType":"journal article","firstPage":"484","id":"21147463","journal":"Cell Host Microbe","lastPage":"495","publicationDate":"2010","title":"Phosphorylation of immunity-related GTPases by a Toxoplasma gondii-secreted kinase promotes macrophage survival and virulence.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","INTERACTION WITH MOUSE IRGB6 (TGTP1/TGTP2)","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Steinfeldt T.","Koenen-Waisman S.","Tong L.","Pawlowski N.","Lamkemeyer T.","Sibley L.D.","Hunn J.P.","Howard J.C."],"citationCrossReferences":[{"database":"PubMed","id":"21203588"},{"database":"DOI","id":"10.1371/journal.pbio.1000576"}],"citationType":"journal article","firstPage":"e1000576","id":"21203588","journal":"PLoS Biol.","lastPage":"e1000576","publicationDate":"2010","title":"Phosphorylation of mouse immunity-related GTPase (IRG) resistance proteins is an evasion strategy for virulent Toxoplasma gondii.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Lim D.","Gold D.A.","Julien L.","Rosowski E.E.","Niedelman W.","Yaffe M.B.","Saeij J.P."],"citationCrossReferences":[{"database":"PubMed","id":"24129568"},{"database":"DOI","id":"10.1074/jbc.m113.523266"}],"citationType":"journal article","firstPage":"34968","id":"24129568","journal":"J. Biol. Chem.","lastPage":"34980","publicationDate":"2013","title":"Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second ligand binding pocket required for acute virulence.","volume":"288"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4JRN","source":"PDB"}],"referenceNumber":14,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP ANALOG AND MAGNESIUM ION","FUNCTION","CATALYTIC ACTIVITY","DOMAIN","DISULFIDE BOND","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
ID   ROP18_TOXGO             Reviewed;         554 AA.
AC   Q2PAY2; B9Q063; S7W304;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-FEB-2006, sequence version 1.
DT   28-JAN-2026, entry version 128.
DE   RecName: Full=Serine/threonine-protein kinase ROP18 {ECO:0000303|PubMed:19266027};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588, ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};
DE   AltName: Full=Rhoptry kinase family protein {ECO:0000312|EMBL:AFO54811.1};
DE   AltName: Full=Rhoptry protein 18 {ECO:0000312|EMBL:CAJ27113.1};
DE   AltName: Full=Rhoptry protein ROP18 {ECO:0000312|EMBL:KAF4642700.1};
GN   Name=ROP18 {ECO:0000312|EMBL:AFO54811.1};
GN   ORFNames=TGRH88_034260 {ECO:0000312|EMBL:KAF4642700.1};
OS   Toxoplasma gondii.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;
OC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.
OX   NCBI_TaxID=5811 {ECO:0000312|EMBL:CAJ27113.1};
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein kinase ROP18 {ECO:0000303|PubMed:19266027};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588, ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};
DE   AltName: Full=Rhoptry kinase family protein {ECO:0000312|EMBL:AFO54811.1};
DE   AltName: Full=Rhoptry protein 18 {ECO:0000312|EMBL:CAJ27113.1};
DE   AltName: Full=Rhoptry protein ROP18 {ECO:0000312|EMBL:KAF4642700.1};
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 124-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
RN   [14] {ECO:0007744|PDB:4JRN}
RP   X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP
RP   ANALOG AND MAGNESIUM ION, FUNCTION, CATALYTIC ACTIVITY, DOMAIN, DISULFIDE
RP   BOND, AND MUTAGENESIS OF ASP-409.
RX   PubMed=24129568; DOI=10.1074/jbc.m113.523266;
RA   Lim D., Gold D.A., Julien L., Rosowski E.E., Niedelman W., Yaffe M.B.,
RA   Saeij J.P.;
RT   "Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second
RT   ligand binding pocket required for acute virulence.";
RL   J. Biol. Chem. 288:34968-34980(2013).
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 158-164`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000269|PubMed:21147463, ECO:0000269|PubMed:21203588,
CC         ECO:0000269|PubMed:24129568, ECO:0000305|PubMed:23144612};
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 165-170`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000305|PubMed:23144612};
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
