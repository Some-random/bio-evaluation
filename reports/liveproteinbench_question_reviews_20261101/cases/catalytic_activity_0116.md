# catalytic_activity_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (1S,4S)-4-&#91;(4-hydroxyphenyl)methyl&#93;-2,5-diazaspiro&#91;bicyclo&#91;3.2.1&#93;octane-6,1&#x27;-cyclohexan&#93;-4&#x27;-one + S-adenosyl-L-methionine = (1S,4S)-4-&#91;(4-methoxyphenyl)methyl&#93;-2,5-diazaspiro&#91;bicyclo&#91;3.2.1&#93;octane-6,1&#x27;-cyclohexan&#93;-4&#x27;-one + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTIRGTLSELSRAADAFAHEVDEAGYGDYTFLPDNSPFDLSFLTSKGLEARGSLIAAAEKILRLAKGPQGCLASFADTKGIEMGTIQALTQLEVPDKVPLQGSITYEELAGVIRVAPELLQRLVRLAALAGFLIEDESGAVRHTAMSAVFLRDTAAGDTARFLFDVDMRAYSFFADSLRLDPSGQNIGDGPTALAFQHDSDDQGNRPTIWDILERNPIQRARFHSTMQALGSFPSHLLKHILVAHDWHSIGSLVDVGGSLGHASLVIAENFPEIRITVQDLPDVVERGRSSLPTVPHAERVSFQAHDLFQEQAIIADAYFLRQILHDWPDGDAERIVRCLIPAMRPGAKLLIMDIVVPEPGAISPYMEKYLRTYDVSMFSMFSAKERTVQQLRDLVERCSARLQFQGISCPPGSATSLLSWVYSAE

[Multiple Choices]
A. Na(+)(in) = Na(+)(out)
B. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
C. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. L-isoleucyl-tRNA(Ile) + acetyl-CoA = N-acetyl-L-isoleucyl-tRNA(Ile) + CoA + H(+)
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

> The sequence matches the cited UniProt entry, which annotates this protein's catalytic activity as the exact reaction in choice C, with ECO:0000269 evidence citing PubMed 33372776. The archived annotation also records this reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C is an SAM-dependent O-methylation, while the other choices describe unrelated reaction types. The sequence might suggest an enzyme class, but the input supplies no clear, diagnostic basis for identifying this protein's specific substrate and reaction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental finding that this enzyme methylates the substrate shown in choice C.


**Reason**

> Selecting the exact transformation depends on a protein-specific fact absent from the question. The reviewer-only annotation supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions are distinct, and the matched sequence's annotated reaction corresponds to choice C.


### Important caveats

- The annotation is linked to experimental evidence code ECO:0000269 and a cited publication, but the primary paper was not independently reviewed here.
- The sequence matches the historical entry, although the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C is an SAM-dependent O-methylation, while the other choices describe unrelated reaction types. The sequence might suggest an enzyme class, but the input supplies no clear, diagnostic basis for identifying this protein's specific substrate and reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme methylates the substrate shown in choice C.",
    "reason": "Selecting the exact transformation depends on a protein-specific fact absent from the question. The reviewer-only annotation supports the key but was not supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates this protein's catalytic activity as the exact reaction in choice C, with ECO:0000269 evidence citing PubMed 33372776. The archived annotation also records this reaction."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence code ECO:0000269 and a cited publication, but the primary paper was not independently reviewed here.",
    "The sequence matches the historical entry, although the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are distinct, and the matched sequence's annotated reaction corresponds to choice C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates this protein's catalytic activity as the exact reaction in choice C, with ECO:0000269 evidence citing PubMed 33372776. The archived annotation also records this reaction.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C is an SAM-dependent O-methylation, while the other choices describe unrelated reaction types. The sequence might suggest an enzyme class, but the input supplies no clear, diagnostic basis for identifying this protein's specific substrate and reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental finding that this enzyme methylates the substrate shown in choice C.",
    "reason": "Selecting the exact transformation depends on a protein-specific fact absent from the question. The reviewer-only annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are distinct, and the matched sequence's annotated reaction corresponds to choice C."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence code ECO:0000269 and a cited publication, but the primary paper was not independently reviewed here.",
    "The sequence matches the historical entry, although the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A7T8J1Z8 (O-methyltransferase FrzF, EC 2.1.1.-) exactly (427 AA, SHA-256 confirmed). The catalytic activity annotation in evidence C5/H4 lists the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The protein is annotated as an O-methyltransferase in the FR901483 biosynthetic pathway, and the reaction (phenol → methoxy using SAM) is consistent with EC 2.1.1.- classification.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> By elimination, one could argue: (A) Na+ transport requires transmembrane helices absent from this 427 AA sequence; (B) P450 monooxygenases require a heme-binding FxxGxxxCxG motif and are typically 450–600+ AA, neither present here; (D) GNAT-fold acetyltransferases have distinct motifs not evident. This weakly favors C as a SAM-dependent methyltransferase. However, identifying the exact substrate (the diazaspiro phenol) and confirming O-methylation specificity cannot be derived from sequence alone.


**Missing item-specific fact**

> The identity of the specific substrate (the 2,5-diazaspiro&#91;bicyclo&#91;3.2.1&#93;octane&#93; intermediate in FR901483 biosynthesis) and the confirmation that this particular methyltransferase acts as an O-methyltransferase on this phenolic compound rather than a C- or N-methyltransferase on a different substrate. This requires knowledge of the Cladobotryum FR901483 gene cluster or the specific UniProt/PubMed annotation.


**Reason**

> While sequence-based elimination of A, B, and D is partially possible through general enzyme-class heuristics (absence of TM helices, P450 heme motif, GNAT fold), the positive identification of this protein as an O-methyltransferase acting on the specific diazaspiro substrate is an item-specific database/experimental fact. The sequence lacks a canonical VLDLGCG SAM-binding motif, making even the broad methyltransferase assignment uncertain without external annotation. The exact reaction stoichiometry and substrate identity cannot be inferred from primary structure.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent clearly distinct enzyme classes (ion transporter, P450, SAM-dependent methyltransferase, GNAT acetyltransferase). The sequence characteristics (427 AA, no TM domains, no heme-binding motif, no GNAT signature) make A, B, and D clearly implausible. Only C remains as a defensible option by elimination, though positive confirmation requires external knowledge.


### Important caveats

- The sequence lacks the canonical VLDLGCG SAM-binding motif, so even identifying this as a methyltransferase from sequence alone is non-trivial; some SAM-MTs use variant motifs.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing high confidence for the key.
- The historical entry (version 19, released Jan 2026) already contained this annotation, so the key was available at the approximate benchmark construction date.
- The elimination reasoning (ruling out A, B, D) provides partial but not complete justification for C; the specific substrate identity remains a lookup fact.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "By elimination, one could argue: (A) Na+ transport requires transmembrane helices absent from this 427 AA sequence; (B) P450 monooxygenases require a heme-binding FxxGxxxCxG motif and are typically 450–600+ AA, neither present here; (D) GNAT-fold acetyltransferases have distinct motifs not evident. This weakly favors C as a SAM-dependent methyltransferase. However, identifying the exact substrate (the diazaspiro phenol) and confirming O-methylation specificity cannot be derived from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the specific substrate (the 2,5-diazaspiro[bicyclo[3.2.1]octane] intermediate in FR901483 biosynthesis) and the confirmation that this particular methyltransferase acts as an O-methyltransferase on this phenolic compound rather than a C- or N-methyltransferase on a different substrate. This requires knowledge of the Cladobotryum FR901483 gene cluster or the specific UniProt/PubMed annotation.",
    "reason": "While sequence-based elimination of A, B, and D is partially possible through general enzyme-class heuristics (absence of TM helices, P450 heme motif, GNAT fold), the positive identification of this protein as an O-methyltransferase acting on the specific diazaspiro substrate is an item-specific database/experimental fact. The sequence lacks a canonical VLDLGCG SAM-binding motif, making even the broad methyltransferase assignment uncertain without external annotation. The exact reaction stoichiometry and substrate identity cannot be inferred from primary structure."
  },
  "case_id": "catalytic_activity_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A7T8J1Z8 (O-methyltransferase FrzF, EC 2.1.1.-) exactly (427 AA, SHA-256 confirmed). The catalytic activity annotation in evidence C5/H4 lists the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The protein is annotated as an O-methyltransferase in the FR901483 biosynthetic pathway, and the reaction (phenol → methoxy using SAM) is consistent with EC 2.1.1.- classification."
  },
  "important_caveats": [
    "The sequence lacks the canonical VLDLGCG SAM-binding motif, so even identifying this as a methyltransferase from sequence alone is non-trivial; some SAM-MTs use variant motifs.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing high confidence for the key.",
    "The historical entry (version 19, released Jan 2026) already contained this annotation, so the key was available at the approximate benchmark construction date.",
    "The elimination reasoning (ruling out A, B, D) provides partial but not complete justification for C; the specific substrate identity remains a lookup fact."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (ion transporter, P450, SAM-dependent methyltransferase, GNAT acetyltransferase). The sequence characteristics (427 AA, no TM domains, no heme-binding motif, no GNAT signature) make A, B, and D clearly implausible. Only C remains as a defensible option by elimination, though positive confirmation requires external knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A7T8J1Z8 (O-methyltransferase FrzF, EC 2.1.1.-) exactly (427 AA, SHA-256 confirmed). The catalytic activity annotation in evidence C5/H4 lists the reaction in Choice C verbatim, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The protein is annotated as an O-methyltransferase in the FR901483 biosynthetic pathway, and the reaction (phenol → methoxy using SAM) is consistent with EC 2.1.1.- classification.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "By elimination, one could argue: (A) Na+ transport requires transmembrane helices absent from this 427 AA sequence; (B) P450 monooxygenases require a heme-binding FxxGxxxCxG motif and are typically 450–600+ AA, neither present here; (D) GNAT-fold acetyltransferases have distinct motifs not evident. This weakly favors C as a SAM-dependent methyltransferase. However, identifying the exact substrate (the diazaspiro phenol) and confirming O-methylation specificity cannot be derived from sequence alone.",
    "missing_item_specific_fact": "The identity of the specific substrate (the 2,5-diazaspiro[bicyclo[3.2.1]octane] intermediate in FR901483 biosynthesis) and the confirmation that this particular methyltransferase acts as an O-methyltransferase on this phenolic compound rather than a C- or N-methyltransferase on a different substrate. This requires knowledge of the Cladobotryum FR901483 gene cluster or the specific UniProt/PubMed annotation.",
    "reason": "While sequence-based elimination of A, B, and D is partially possible through general enzyme-class heuristics (absence of TM helices, P450 heme motif, GNAT fold), the positive identification of this protein as an O-methyltransferase acting on the specific diazaspiro substrate is an item-specific database/experimental fact. The sequence lacks a canonical VLDLGCG SAM-binding motif, making even the broad methyltransferase assignment uncertain without external annotation. The exact reaction stoichiometry and substrate identity cannot be inferred from primary structure."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (ion transporter, P450, SAM-dependent methyltransferase, GNAT acetyltransferase). The sequence characteristics (427 AA, no TM domains, no heme-binding motif, no GNAT signature) make A, B, and D clearly implausible. Only C remains as a defensible option by elimination, though positive confirmation requires external knowledge."
  },
  "important_caveats": [
    "The sequence lacks the canonical VLDLGCG SAM-binding motif, so even identifying this as a methyltransferase from sequence alone is non-trivial; some SAM-MTs use variant motifs.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing high confidence for the key.",
    "The historical entry (version 19, released Jan 2026) already contained this annotation, so the key was available at the approximate benchmark construction date.",
    "The elimination reasoning (ruling out A, B, D) provides partial but not complete justification for C; the specific substrate identity remains a lookup fact."
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

**Accession:** `A0A7T8J1Z8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
"A0A7T8J1Z8"
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"O-methyltransferase FrzF"}}}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83592"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"name":"(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83591"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:233175"},{"database":"ChEBI","id":"CHEBI:233177"}]}}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1Z8.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:52.176056+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `32ede02f32517874979e874842ff451de632a768dc1939171d1d3596a08918bd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
ID   FRZF_CLASX              Reviewed;         427 AA.
AC   A0A7T8J1Z8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};
GN   Name=FrzF {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
DE   RecName: Full=O-methyltransferase FrzF {ECO:0000303|PubMed:33372776};
DE            EC=2.1.1.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein F {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1Z8?format=txt&versions=19)  
**Locator:** `lines 52-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:54.122159+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-
CC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-
CC         L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-
CC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-
CC         L-homocysteine + H(+); Xref=Rhea:RHEA:83591, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:233175,
CC         ChEBI:CHEBI:233177; Evidence={ECO:0000269|PubMed:33372776};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83592;
CC         Evidence={ECO:0000269|PubMed:33372776};
```

Source SHA-256: `b04f01db868e607e76a98568774abea21dd993afd1fc87f063a28fcc2ed40a7b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
