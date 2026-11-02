# GO_molecular_function_0105

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — xylan 1,4-beta-xylosidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPQVRNPILPGFNPDPSILRVGEDYYIATSTFEWYPGVQIHHSRDLANWELVARPLNRKSQLDMRGNPDSCGIWAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEGIVLQEFDPKAGKLVGPRKNIFTGTDLALVEGPHLYKRNGWYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI

[Multiple Choices]
A. chromatin insulator sequence binding
B. nucleotidyltransferase activity
C. enzyme activator activity
D. xylan 1,4-beta-xylosidase activity
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

> The sequence matches the annotated 538-aa Humicola insolens protein. Its annotation reports experimentally supported beta-xylosidase activity, with the cited catalytic reaction matching option D. The protein is bifunctional and also has alpha-L-arabinofuranosidase activity, but that is not an option.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a globular enzyme, but the supplied sequence and choices do not provide a reliable general biological argument identifying its specific substrate or catalytic activity.


**Missing item-specific fact**

> The protein-specific substrate and activity profile—especially its experimentally reported beta-xylosidase activity—is needed to distinguish D from the alternatives.


**Reason**

> Although the key is supported by experimental evidence for this sequence, that evidence is reviewer-only. Selecting D from the input requires protein-specific functional knowledge or an external annotation, not merely recognizing a broad enzyme-like sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is supported among the listed options. The protein has an additional alpha-L-arabinofuranosidase activity, but that function is not offered as a choice.


### Important caveats

- The experimental evidence is reported in UniProt with a citation to PubMed:24262572; the primary paper was not independently reviewed here.
- The evidence supports D but does not establish that it is the protein's only molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a globular enzyme, but the supplied sequence and choices do not provide a reliable general biological argument identifying its specific substrate or catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and activity profile—especially its experimentally reported beta-xylosidase activity—is needed to distinguish D from the alternatives.",
    "reason": "Although the key is supported by experimental evidence for this sequence, that evidence is reviewer-only. Selecting D from the input requires protein-specific functional knowledge or an external annotation, not merely recognizing a broad enzyme-like sequence."
  },
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated 538-aa Humicola insolens protein. Its annotation reports experimentally supported beta-xylosidase activity, with the cited catalytic reaction matching option D. The protein is bifunctional and also has alpha-L-arabinofuranosidase activity, but that is not an option."
  },
  "important_caveats": [
    "The experimental evidence is reported in UniProt with a citation to PubMed:24262572; the primary paper was not independently reviewed here.",
    "The evidence supports D but does not establish that it is the protein's only molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported among the listed options. The protein has an additional alpha-L-arabinofuranosidase activity, but that function is not offered as a choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated 538-aa Humicola insolens protein. Its annotation reports experimentally supported beta-xylosidase activity, with the cited catalytic reaction matching option D. The protein is bifunctional and also has alpha-L-arabinofuranosidase activity, but that is not an option.",
    "evidence_ids": ["C5", "C6", "C9", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a globular enzyme, but the supplied sequence and choices do not provide a reliable general biological argument identifying its specific substrate or catalytic activity.",
    "missing_item_specific_fact": "The protein-specific substrate and activity profile—especially its experimentally reported beta-xylosidase activity—is needed to distinguish D from the alternatives.",
    "reason": "Although the key is supported by experimental evidence for this sequence, that evidence is reviewer-only. Selecting D from the input requires protein-specific functional knowledge or an external annotation, not merely recognizing a broad enzyme-like sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported among the listed options. The protein has an additional alpha-L-arabinofuranosidase activity, but that function is not offered as a choice."
  },
  "important_caveats": [
    "The experimental evidence is reported in UniProt with a citation to PubMed:24262572; the primary paper was not independently reviewed here.",
    "The evidence supports D but does not establish that it is the protein's only molecular function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProtKB V9TT49 (XY43B_HUMIN, 538 aa, Humicola insolens) exactly. The entry carries GO:0009044 'xylan 1,4-beta-xylosidase activity' with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity EC 3.2.1.37 is confirmed experimentally, and the FUNCTION comment states the enzyme is most active on pNPX (100%), consistent with primary beta-xylosidase activity. The GO term definition matches the option text exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The four options span radically different molecular function categories (DNA-binding, transferase, regulatory activator, glycoside hydrolase). A knowledgeable biologist could partially eliminate A (no obvious DNA-binding motifs like zinc fingers or homeodomains), B (no nucleotidyltransferase motifs), and C (the protein appears to be a standalone enzyme rather than a regulatory activator). However, positively identifying the protein as specifically a 'xylan 1,4-beta-xylosidase' (GH43 family) from raw 538-aa sequence requires recognizing GH43 β-propeller fold features, catalytic Asp/Glu residues in specific spatial arrangement, or simply recognizing this exact sequence as a known xylosidase.


**Missing item-specific fact**

> Identification of the protein as belonging to glycoside hydrolase family 43 (GH43) and specifically as a beta-xylosidase requires either (a) recognizing the specific sequence as a known protein, (b) knowledge of GH43-family catalytic and structural motifs absent from the prompt, or (c) a sequence-similarity search against a database. None of these are derivable from general biological reasoning applied to the raw sequence alone.


**Reason**

> While the extreme category mismatch of distractors A-C provides a weak elimination path, the positive identification of 'xylan 1,4-beta-xylosidase' among all possible hydrolase activities (cellulase, mannosidase, arabinosidase, etc.) depends on protein-specific annotation knowledge or sequence recognition, not general biological reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is bifunctional (beta-xylosidase + alpha-L-arabinofuranosidase), but 'alpha-L-arabinofuranosidase activity' is not among the choices. Among the four provided options, D is unambiguously the only one matching any annotated activity of this protein. The primary activity (100% on pNPX) aligns with GO:0009044.


### Important caveats

- The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the question asks for 'primary molecular function,' which the experimental data supports as beta-xylosidase (100% relative activity on pNPX vs. 56.6% on pNPA).
- The UniProt entry was first public in 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.
- Sequence match is exact (SHA-256 identical) between benchmark input and UniProt V9TT49 sequence version 1.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span radically different molecular function categories (DNA-binding, transferase, regulatory activator, glycoside hydrolase). A knowledgeable biologist could partially eliminate A (no obvious DNA-binding motifs like zinc fingers or homeodomains), B (no nucleotidyltransferase motifs), and C (the protein appears to be a standalone enzyme rather than a regulatory activator). However, positively identifying the protein as specifically a 'xylan 1,4-beta-xylosidase' (GH43 family) from raw 538-aa sequence requires recognizing GH43 β-propeller fold features, catalytic Asp/Glu residues in specific spatial arrangement, or simply recognizing this exact sequence as a known xylosidase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of the protein as belonging to glycoside hydrolase family 43 (GH43) and specifically as a beta-xylosidase requires either (a) recognizing the specific sequence as a known protein, (b) knowledge of GH43-family catalytic and structural motifs absent from the prompt, or (c) a sequence-similarity search against a database. None of these are derivable from general biological reasoning applied to the raw sequence alone.",
    "reason": "While the extreme category mismatch of distractors A-C provides a weak elimination path, the positive identification of 'xylan 1,4-beta-xylosidase' among all possible hydrolase activities (cellulase, mannosidase, arabinosidase, etc.) depends on protein-specific annotation knowledge or sequence recognition, not general biological reasoning from the supplied input."
  },
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C9",
      "H1",
      "H3",
      "H4",
      "H7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProtKB V9TT49 (XY43B_HUMIN, 538 aa, Humicola insolens) exactly. The entry carries GO:0009044 'xylan 1,4-beta-xylosidase activity' with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity EC 3.2.1.37 is confirmed experimentally, and the FUNCTION comment states the enzyme is most active on pNPX (100%), consistent with primary beta-xylosidase activity. The GO term definition matches the option text exactly."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the question asks for 'primary molecular function,' which the experimental data supports as beta-xylosidase (100% relative activity on pNPX vs. 56.6% on pNPA).",
    "The UniProt entry was first public in 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.",
    "Sequence match is exact (SHA-256 identical) between benchmark input and UniProt V9TT49 sequence version 1.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (beta-xylosidase + alpha-L-arabinofuranosidase), but 'alpha-L-arabinofuranosidase activity' is not among the choices. Among the four provided options, D is unambiguously the only one matching any annotated activity of this protein. The primary activity (100% on pNPX) aligns with GO:0009044."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProtKB V9TT49 (XY43B_HUMIN, 538 aa, Humicola insolens) exactly. The entry carries GO:0009044 'xylan 1,4-beta-xylosidase activity' with experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity EC 3.2.1.37 is confirmed experimentally, and the FUNCTION comment states the enzyme is most active on pNPX (100%), consistent with primary beta-xylosidase activity. The GO term definition matches the option text exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C9", "H1", "H3", "H4", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The four options span radically different molecular function categories (DNA-binding, transferase, regulatory activator, glycoside hydrolase). A knowledgeable biologist could partially eliminate A (no obvious DNA-binding motifs like zinc fingers or homeodomains), B (no nucleotidyltransferase motifs), and C (the protein appears to be a standalone enzyme rather than a regulatory activator). However, positively identifying the protein as specifically a 'xylan 1,4-beta-xylosidase' (GH43 family) from raw 538-aa sequence requires recognizing GH43 β-propeller fold features, catalytic Asp/Glu residues in specific spatial arrangement, or simply recognizing this exact sequence as a known xylosidase.",
    "missing_item_specific_fact": "Identification of the protein as belonging to glycoside hydrolase family 43 (GH43) and specifically as a beta-xylosidase requires either (a) recognizing the specific sequence as a known protein, (b) knowledge of GH43-family catalytic and structural motifs absent from the prompt, or (c) a sequence-similarity search against a database. None of these are derivable from general biological reasoning applied to the raw sequence alone.",
    "reason": "While the extreme category mismatch of distractors A-C provides a weak elimination path, the positive identification of 'xylan 1,4-beta-xylosidase' among all possible hydrolase activities (cellulase, mannosidase, arabinosidase, etc.) depends on protein-specific annotation knowledge or sequence recognition, not general biological reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (beta-xylosidase + alpha-L-arabinofuranosidase), but 'alpha-L-arabinofuranosidase activity' is not among the choices. Among the four provided options, D is unambiguously the only one matching any annotated activity of this protein. The primary activity (100% on pNPX) aligns with GO:0009044."
  },
  "important_caveats": [
    "The protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55); the question asks for 'primary molecular function,' which the experimental data supports as beta-xylosidase (100% relative activity on pNPX vs. 56.6% on pNPA).",
    "The UniProt entry was first public in 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed at benchmark creation time.",
    "Sequence match is exact (SHA-256 identical) between benchmark input and UniProt V9TT49 sequence version 1.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model."
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

**Accession:** `V9TT49` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
"V9TT49"
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"1,4-beta-D-xylan xylohydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylan 1,4-beta-xylosidase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.37"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Beta-xylosidase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Arabinosidase"}]}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylosidase/arabinosidase 43B"}}}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"Bifunctional beta-xylosidase/alpha-L-arabinosidases with a low level of xylanase activity (PubMed:24262572). Is most active on 4-nitrophenyl beta-D-xylopyranoside (pNPX) (defined as 100%), moderate on p-nitrophenyl-alpha-L-arabinofuranoside (pNPA) (56.6%), and weak on beechwood xylan (5.7%) and birchwood xylan (2.7%) (PubMed:24262572). Is able to attack xylooligosacchardies with degrees of polymerization of 2-5, releasing the amounts of reducing sugars in the order of xylopentose > xylotetraose > xylotriose > xylobiose, i.e. the rate of xylose released from xylooligosacchardies increased with the chain length (PubMed:24262572). No activity was detected in the presence of carboxymethyl cellulose-sodium (CMC-Na), sugar beet arabinan, AZCL-arabinan (debranched), 4-nitrophenyl a-D - galactopyranoside, 2-nitrophenyl beta-D-galactopyranoside, and 4-nitrophenyl alpha-D-glucopyranoside (PubMed:24262572)"}]}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.37","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini."}}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"id":"GO:0009044","properties":[{"key":"GoTerm","value":"F:xylan 1,4-beta-xylosidase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
ID   XY43B_HUMIN             Reviewed;         538 AA.
AC   V9TT49;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-MAR-2014, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Xylosidase/arabinosidase 43B {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};
DE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};
DE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};
DE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};
GN   Name=Xyl43B {ECO:0000303|PubMed:24262572};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 32-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
CC   -!- FUNCTION: Bifunctional beta-xylosidase/alpha-L-arabinosidases with a
CC       low level of xylanase activity (PubMed:24262572). Is most active on 4-
CC       nitrophenyl beta-D-xylopyranoside (pNPX) (defined as 100%), moderate on
CC       p-nitrophenyl-alpha-L-arabinofuranoside (pNPA) (56.6%), and weak on
CC       beechwood xylan (5.7%) and birchwood xylan (2.7%) (PubMed:24262572). Is
CC       able to attack xylooligosacchardies with degrees of polymerisation of
CC       2-5, releasing the amounts of reducing sugars in the order of
CC       xylopentose > xylotetraose > xylotriose > xylobiose, i.e. the rate of
CC       xylose released from xylooligosacchardies increased with the chain
CC       length (PubMed:24262572). No activity was detected in the presence of
CC       carboxymethyl cellulose-sodium (CMC-Na), sugar beet arabinan, AZCL-
CC       arabinan (debranched), 4-nitrophenyl a-D - galactopyranoside, 2-
CC       nitrophenyl beta-D-galactopyranoside, and 4-nitrophenyl alpha-D-
CC       glucopyranoside (PubMed:24262572). {ECO:0000269|PubMed:24262572}.
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-
CC         xylose residues from the non-reducing termini.; EC=3.2.1.37;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 50-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside
CC         residues in alpha-L-arabinosides.; EC=3.2.1.55;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
DR   GO; GO:0009044; F:xylan 1,4-beta-xylosidase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 92065-92081`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009044
name: xylan 1,4-beta-xylosidase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of (1->4)-beta-D-xylans so as to remove successive D-xylose residues from the non-reducing termini." [EC:3.2.1.37]
synonym: "1,4-beta-D-xylan xylohydrolase activity" RELATED [EC:3.2.1.37]
synonym: "beta-D-xylopyranosidase activity" RELATED [EC:3.2.1.37]
synonym: "beta-xylosidase activity" RELATED [EC:3.2.1.37]
synonym: "exo-1,4-beta-D-xylosidase activity" RELATED [EC:3.2.1.37]
synonym: "exo-1,4-beta-xylosidase activity" RELATED [EC:3.2.1.37]
synonym: "exo-1,4-xylosidase activity" RELATED [EC:3.2.1.37]
synonym: "xylobiase activity" RELATED [EC:3.2.1.37]
xref: EC:3.2.1.37
xref: MetaCyc:3.2.1.37-RXN
is_a: GO:0097599 ! xylanase activity
property_value: skos:exactMatch EC:3.2.1.37

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
