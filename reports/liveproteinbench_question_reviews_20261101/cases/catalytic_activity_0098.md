# catalytic_activity_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
B. 2 5'-deoxyadenosin-5'-yl radical + 2 dAMP + A = 2 4'-phospho-dehydrooxetanocin + 2 5'-deoxyadenosine + AH2
C. Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.
D. (7,8-dihydropterin-6-yl)methyl diphosphate + 4-aminobenzoate = 7,8-dihydropteroate + diphosphate
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

> The exact 630-aa sequence matches the UniProt entry annotated as Plasmodium vivax subtilisin-like protease 1, and that entry assigns EC 3.4.21.62 and the hydrolysis reaction in choice C. The annotation cites experimental-evidence codes, though the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the architecture and conserved catalytic-region features of a subtilisin-like serine protease; among the choices, C is the protein-hydrolysis reaction, whereas the others describe methyl transfer, radical chemistry, or pterin synthesis.


**Missing item-specific fact**

> The sequence alone does not establish the detailed P1 residue preference as confidently as a protein-specific functional annotation or experiment would.


**Reason**

> General family recognition provides a meaningful basis to select the protease reaction over the chemically distinct alternatives, even though the fine specificity stated in C is not independently derivable with certainty from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct enzyme activities, and the sequence's protease-family features distinguish C from the alternatives.


### Important caveats

- Reviewer-only database evidence supports the key but was not available to the evaluated model.
- The exact author source snapshot is unknown; the sequence match is confirmed for the cited current and historical UniProt records.
- The cited database annotation supports the detailed substrate preference, but that specificity is less directly inferable from sequence than the broad protease activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the architecture and conserved catalytic-region features of a subtilisin-like serine protease; among the choices, C is the protein-hydrolysis reaction, whereas the others describe methyl transfer, radical chemistry, or pterin synthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the detailed P1 residue preference as confidently as a protein-specific functional annotation or experiment would.",
    "reason": "General family recognition provides a meaningful basis to select the protease reaction over the chemically distinct alternatives, even though the fine specificity stated in C is not independently derivable with certainty from the sequence."
  },
  "case_id": "catalytic_activity_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact 630-aa sequence matches the UniProt entry annotated as Plasmodium vivax subtilisin-like protease 1, and that entry assigns EC 3.4.21.62 and the hydrolysis reaction in choice C. The annotation cites experimental-evidence codes, though the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The exact author source snapshot is unknown; the sequence match is confirmed for the cited current and historical UniProt records.",
    "The cited database annotation supports the detailed substrate preference, but that specificity is less directly inferable from sequence than the broad protease activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence's protease-family features distinguish C from the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 630-aa sequence matches the UniProt entry annotated as Plasmodium vivax subtilisin-like protease 1, and that entry assigns EC 3.4.21.62 and the hydrolysis reaction in choice C. The annotation cites experimental-evidence codes, though the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the architecture and conserved catalytic-region features of a subtilisin-like serine protease; among the choices, C is the protein-hydrolysis reaction, whereas the others describe methyl transfer, radical chemistry, or pterin synthesis.",
    "missing_item_specific_fact": "The sequence alone does not establish the detailed P1 residue preference as confidently as a protein-specific functional annotation or experiment would.",
    "reason": "General family recognition provides a meaningful basis to select the protease reaction over the chemically distinct alternatives, even though the fine specificity stated in C is not independently derivable with certainty from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence's protease-family features distinguish C from the alternatives."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The exact author source snapshot is unknown; the sequence match is confirmed for the cited current and historical UniProt records.",
    "The cited database annotation supports the detailed substrate preference, but that specificity is less directly inferable from sequence than the broad protease activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 630-aa sequence matches UniProt E6Y8B9 (SUB1_PLAVI, Plasmodium vivax Subtilisin-like protease 1, EC 3.4.21.62) exactly (sequence SHA256 identical in both current and historical snapshots). The UniProt CATALYTIC ACTIVITY annotation (ECO:0000269, experimental evidence from five independent publications including crystal structures 4TR2, 8COY/8COZ, 8QKE/8QKG) states verbatim: 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' This matches Choice C word-for-word.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical subtilisin catalytic-serine motif GDSG (visible as '…KICVIDSGIDYNHPDLRNN…') together with a His-rich region ('…VKELHGRKG…') consistent with the Asp-His-Ser catalytic triad of subtilisin-family serine proteases. The N-terminal hydrophobic stretch (MVLTRRAALLLCPWVIQLVIKRTLAGD…) is consistent with a signal peptide of a secreted protease precursor. Recognizing GDSG as the hallmark of subtilisin-like serine proteases is general enzymology knowledge. Among the four choices, only C describes a protease (peptide-bond hydrolysis); A is a SAM-dependent methyltransferase, B is a radical-SAM enzyme, and D is a dihydropteroate synthase—none of which would contain a GDSG catalytic motif or a signal peptide. Thus identifying the protease class from the sequence discriminates C from the others.


**Missing item-specific fact**

> The precise P1 specificity ('large uncharged residue') and the 'hydrolyzes peptide amides' qualifier are EC 3.4.21.62 database annotations not derivable from the sequence alone; however, the protease-vs-nonprotease distinction that separates C from A, B, and D is reachable via the GDSG motif.


**Reason**

> The GDSG subtilisin motif is a well-known, general-knowledge sequence signature. The three distractors describe entirely different enzyme classes (methyltransferase, radical SAM, synthase) that lack any protease catalytic architecture. A model familiar with protease families can reason from the motif to 'serine protease' and select C without needing to recall the exact EC 3.4.21.62 text.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes (methyltransferase, radical SAM enzyme, serine protease, dihydropteroate synthase). The GDSG motif unambiguously points to a subtilisin-family serine protease, making C the only defensible choice. No other option describes peptide-bond hydrolysis.


### Important caveats

- The exact wording of Choice C is the verbatim UniProt/EC 3.4.21.62 annotation text; a model that does not recognize GDSG but has memorized this annotation string could also select C via lookup.
- The 'preference for a large uncharged residue in P1' and 'hydrolyzes peptide amides' qualifiers are experimental characterizations (ECO:0000269) not inferable from sequence alone, though they do not affect the protease-vs-nonprotease discrimination needed to answer.
- The UniProt entry was first public 2025-04-09; the historical snapshot (entry version 78, released 2026-01-28) already contained the same catalytic-activity annotation, so the key was available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical subtilisin catalytic-serine motif GDSG (visible as '…KICVIDSGIDYNHPDLRNN…') together with a His-rich region ('…VKELHGRKG…') consistent with the Asp-His-Ser catalytic triad of subtilisin-family serine proteases. The N-terminal hydrophobic stretch (MVLTRRAALLLCPWVIQLVIKRTLAGD…) is consistent with a signal peptide of a secreted protease precursor. Recognizing GDSG as the hallmark of subtilisin-like serine proteases is general enzymology knowledge. Among the four choices, only C describes a protease (peptide-bond hydrolysis); A is a SAM-dependent methyltransferase, B is a radical-SAM enzyme, and D is a dihydropteroate synthase—none of which would contain a GDSG catalytic motif or a signal peptide. Thus identifying the protease class from the sequence discriminates C from the others.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise P1 specificity ('large uncharged residue') and the 'hydrolyzes peptide amides' qualifier are EC 3.4.21.62 database annotations not derivable from the sequence alone; however, the protease-vs-nonprotease distinction that separates C from A, B, and D is reachable via the GDSG motif.",
    "reason": "The GDSG subtilisin motif is a well-known, general-knowledge sequence signature. The three distractors describe entirely different enzyme classes (methyltransferase, radical SAM, synthase) that lack any protease catalytic architecture. A model familiar with protease families can reason from the motif to 'serine protease' and select C without needing to recall the exact EC 3.4.21.62 text."
  },
  "case_id": "catalytic_activity_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied 630-aa sequence matches UniProt E6Y8B9 (SUB1_PLAVI, Plasmodium vivax Subtilisin-like protease 1, EC 3.4.21.62) exactly (sequence SHA256 identical in both current and historical snapshots). The UniProt CATALYTIC ACTIVITY annotation (ECO:0000269, experimental evidence from five independent publications including crystal structures 4TR2, 8COY/8COZ, 8QKE/8QKG) states verbatim: 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' This matches Choice C word-for-word."
  },
  "important_caveats": [
    "The exact wording of Choice C is the verbatim UniProt/EC 3.4.21.62 annotation text; a model that does not recognize GDSG but has memorized this annotation string could also select C via lookup.",
    "The 'preference for a large uncharged residue in P1' and 'hydrolyzes peptide amides' qualifiers are experimental characterizations (ECO:0000269) not inferable from sequence alone, though they do not affect the protease-vs-nonprotease discrimination needed to answer.",
    "The UniProt entry was first public 2025-04-09; the historical snapshot (entry version 78, released 2026-01-28) already contained the same catalytic-activity annotation, so the key was available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (methyltransferase, radical SAM enzyme, serine protease, dihydropteroate synthase). The GDSG motif unambiguously points to a subtilisin-family serine protease, making C the only defensible choice. No other option describes peptide-bond hydrolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 630-aa sequence matches UniProt E6Y8B9 (SUB1_PLAVI, Plasmodium vivax Subtilisin-like protease 1, EC 3.4.21.62) exactly (sequence SHA256 identical in both current and historical snapshots). The UniProt CATALYTIC ACTIVITY annotation (ECO:0000269, experimental evidence from five independent publications including crystal structures 4TR2, 8COY/8COZ, 8QKE/8QKG) states verbatim: 'Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.' This matches Choice C word-for-word.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical subtilisin catalytic-serine motif GDSG (visible as '…KICVIDSGIDYNHPDLRNN…') together with a His-rich region ('…VKELHGRKG…') consistent with the Asp-His-Ser catalytic triad of subtilisin-family serine proteases. The N-terminal hydrophobic stretch (MVLTRRAALLLCPWVIQLVIKRTLAGD…) is consistent with a signal peptide of a secreted protease precursor. Recognizing GDSG as the hallmark of subtilisin-like serine proteases is general enzymology knowledge. Among the four choices, only C describes a protease (peptide-bond hydrolysis); A is a SAM-dependent methyltransferase, B is a radical-SAM enzyme, and D is a dihydropteroate synthase—none of which would contain a GDSG catalytic motif or a signal peptide. Thus identifying the protease class from the sequence discriminates C from the others.",
    "missing_item_specific_fact": "The precise P1 specificity ('large uncharged residue') and the 'hydrolyzes peptide amides' qualifier are EC 3.4.21.62 database annotations not derivable from the sequence alone; however, the protease-vs-nonprotease distinction that separates C from A, B, and D is reachable via the GDSG motif.",
    "reason": "The GDSG subtilisin motif is a well-known, general-knowledge sequence signature. The three distractors describe entirely different enzyme classes (methyltransferase, radical SAM, synthase) that lack any protease catalytic architecture. A model familiar with protease families can reason from the motif to 'serine protease' and select C without needing to recall the exact EC 3.4.21.62 text."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (methyltransferase, radical SAM enzyme, serine protease, dihydropteroate synthase). The GDSG motif unambiguously points to a subtilisin-family serine protease, making C the only defensible choice. No other option describes peptide-bond hydrolysis."
  },
  "important_caveats": [
    "The exact wording of Choice C is the verbatim UniProt/EC 3.4.21.62 annotation text; a model that does not recognize GDSG but has memorized this annotation string could also select C via lookup.",
    "The 'preference for a large uncharged residue in P1' and 'hydrolyzes peptide amides' qualifiers are experimental characterizations (ECO:0000269) not inferable from sequence alone, though they do not affect the protease-vs-nonprotease discrimination needed to answer.",
    "The UniProt entry was first public 2025-04-09; the historical snapshot (entry version 78, released 2026-01-28) already contained the same catalytic-activity annotation, so the key was available at benchmark construction time."
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

**Accession:** `E6Y8B9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 78. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
"E6Y8B9"
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"PvS1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"PvSUB1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"SUB1 protease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"Subtilase SUB1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38503166","source":"PubMed"}],"value":"3.4.21.62"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"Subtilisin-like protease 1"}}}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.62","evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38503166","source":"PubMed"}],"name":"Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides."}}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
ID   SUB1_PLAVI              Reviewed;         630 AA.
AC   E6Y8B9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   08-MAR-2011, sequence version 1.
DT   28-JAN-2026, entry version 78.
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};
DE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};
DE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};
DE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};
DE   Flags: Precursor;
GN   Name=sub1 {ECO:0000312|EMBL:ACT76164.1};
GN   ORFNames=PVC01_100035100 {ECO:0000312|EMBL:SCO73277.1},
GN   PVT01_100029100 {ECO:0000312|EMBL:SCO67822.1},
GN   PVW1_100050600 {ECO:0000312|EMBL:CAG9475055.1};
OS   Plasmodium vivax.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).
OX   NCBI_TaxID=5855 {ECO:0000312|EMBL:ACT76164.1};
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};
DE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};
DE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};
DE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};
DE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};
DE   Flags: Precursor;
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 91-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of proteins with broad specificity for peptide
CC         bonds, and a preference for a large uncharged residue in P1.
CC         Hydrolyzes peptide amides.; EC=3.4.21.62;
CC         Evidence={ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226,
CC         ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597,
CC         ECO:0000269|PubMed:38503166};
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
