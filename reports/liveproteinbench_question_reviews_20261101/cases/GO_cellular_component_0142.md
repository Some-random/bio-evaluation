# GO_cellular_component_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — mitochondrial inner membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQPPTRAPFFPFSLLRGRKARETCTCRSVASTEGPNTFGPRARPGCHAHQVAPSKESFHSSAFQLVSASRLSPLMSSCFVSFLRYPSFRPSAPFSAPPSSSTVPISTPSDFSHSAPASWRCVPTAPSALHAPFSFTTQAAHLSSCVFDGCSRLPCSEPGSPQTLQRALATTSATAFLRTACMSHRLRRRPDAWTSGCSGQTDNATASPCVRPLLRPPVDTASRAAANDKDAPQPTCFWRNARTSRAVHRNQTDMNFSSFSCSLRPCRHTLAKAAGHHAPLSRHSLQSLPESRIRGGTVSRGDSPGSLTLSPRNMSSDAMPVHPLYFPSAVPFSTTSGSNSSTFSCPSPSSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSTSSPFLLSRSHSVDCRACPVSRAPPNPTSLQLLFSLFPFLWPTALKDRLRVLGSVACLVTAKVLTIQAPLLLANLVDAFQVLPHNSPLSPSGASPSSGDTSLLASSGETSSSLSPSAAPAEGAREAGKSGESAGRERRDEGSTVRLSPLAEGPASPATEERTAAGKAGTSVGGRDAGAVHALDTEHLRNTAQIVSVPLGVVCGFPVARIAATGFNELRSTLFTRVSQNASCDFSCHAFLHLHALALFHDKRAGELSVLISRGMKSVTALLNVLLFQMVPTALEFALVLYLLGSKVGGPVACITSLTMAVYVAFTAAVTARRTKIRKEMIAAEQQSVGLLVDSLANAEAVRFFTAEKGELSRFEAVQRRYAEKHVSVNQSLAFLNFGQQLIFNVGVLGSLAYTASQVAAGLLPVGHIVLVSSLLLQLAVPLNFVGTIYRETSLNLADLEKLYELMNHHPPIVNPPDARPFVLKGGAVAFENVRFAYPPSPLRPGSLPSKTGDDEKPEASRMLLDDVSFSVDAGKKVAIVGPSGVGKSTLIKLLFRMFDPASGTVRIDDQDVKELDLHSFRRQIGVVPQDMVLFNDTIEFNIKYGCPSATDEEMRAAAKQAEIDDVIMRMPQGYSTVVGERGLKLSGGERQRIGIARCLLRNPAIAVFDEATSALDSHTEQKILKAFRAMARGRTTLVIAHRLSTISDADKIIYLKEGKIAEMGTHAELLEKERGLYRALWESQQHQEQEEAVSTPDLTLS

[Multiple Choices]
A. chloroplast
B. endoplasmic reticulum
C. host cell
D. mitochondrial inner membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt sequence for Toxoplasma gondii ATM1. The record reports experimentally supported localization to the mitochondrion membrane, while the more specific mitochondrial inner membrane assignment is a computational GO annotation (IEA:TreeGrafter), not direct experimental evidence in the excerpts. This supports D, with that evidence distinction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic membrane-spanning regions and an ABC-transporter-like ATPase domain, supporting a multi-pass membrane transporter. Those features alone do not reliably distinguish mitochondrial inner membrane from ER membrane; the sequence does not provide a decisive localization signal in the supplied input.


**Missing item-specific fact**

> The protein-specific identity and localization evidence for T. gondii ATM1/ABCB7-like, including its mitochondrial membrane localization and the inner-membrane GO assignment.


**Reason**

> The exact choice depends on protein-specific localization information absent from the question. Recognizing or looking up this sequence as ATM1 would provide that fact, but would not make the selection reasoning-supported from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is supported by the matched sequence’s inner-membrane GO annotation. The cited experimental localization is broader (mitochondrion membrane), but the evidence does not establish a competing listed compartment.


### Important caveats

- The inner-membrane GO annotation is computationally inferred; the cited experimental subcellular-location evidence specifies mitochondrion membrane, not explicitly the inner membrane.
- Reviewer-only accession and annotation evidence establishes support for the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and an ABC-transporter-like ATPase domain, supporting a multi-pass membrane transporter. Those features alone do not reliably distinguish mitochondrial inner membrane from ER membrane; the sequence does not provide a decisive localization signal in the supplied input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and localization evidence for T. gondii ATM1/ABCB7-like, including its mitochondrial membrane localization and the inner-membrane GO assignment.",
    "reason": "The exact choice depends on protein-specific localization information absent from the question. Recognizing or looking up this sequence as ATM1 would provide that fact, but would not make the selection reasoning-supported from the supplied input."
  },
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for Toxoplasma gondii ATM1. The record reports experimentally supported localization to the mitochondrion membrane, while the more specific mitochondrial inner membrane assignment is a computational GO annotation (IEA:TreeGrafter), not direct experimental evidence in the excerpts. This supports D, with that evidence distinction."
  },
  "important_caveats": [
    "The inner-membrane GO annotation is computationally inferred; the cited experimental subcellular-location evidence specifies mitochondrion membrane, not explicitly the inner membrane.",
    "Reviewer-only accession and annotation evidence establishes support for the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported by the matched sequence’s inner-membrane GO annotation. The cited experimental localization is broader (mitochondrion membrane), but the evidence does not establish a competing listed compartment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for Toxoplasma gondii ATM1. The record reports experimentally supported localization to the mitochondrion membrane, while the more specific mitochondrial inner membrane assignment is a computational GO annotation (IEA:TreeGrafter), not direct experimental evidence in the excerpts. This supports D, with that evidence distinction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and an ABC-transporter-like ATPase domain, supporting a multi-pass membrane transporter. Those features alone do not reliably distinguish mitochondrial inner membrane from ER membrane; the sequence does not provide a decisive localization signal in the supplied input.",
    "missing_item_specific_fact": "The protein-specific identity and localization evidence for T. gondii ATM1/ABCB7-like, including its mitochondrial membrane localization and the inner-membrane GO assignment.",
    "reason": "The exact choice depends on protein-specific localization information absent from the question. Recognizing or looking up this sequence as ATM1 would provide that fact, but would not make the selection reasoning-supported from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is supported by the matched sequence’s inner-membrane GO annotation. The cited experimental localization is broader (mitochondrion membrane), but the evidence does not establish a competing listed compartment."
  },
  "important_caveats": [
    "The inner-membrane GO annotation is computationally inferred; the cited experimental subcellular-location evidence specifies mitochondrion membrane, not explicitly the inner membrane.",
    "Reviewer-only accession and annotation evidence establishes support for the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry S8EXU2 (ATM1_TOXGM, ABC transporter ATM1/ABCB7-like from Toxoplasma gondii) carries GO:0005743 (mitochondrial inner membrane) annotation. The experimental subcellular location annotation states 'Mitochondrion membrane' (ECO:0000269, direct assay from PubMed:39207139; ECO:0000305 from PubMed:39348385), and the GO:0005743 assignment is via IEA:TreeGrafter (homology-based inference). The ABCB7/ATM1 family is well-characterized in yeast and other eukaryotes as a mitochondrial inner membrane transporter involved in Fe-S cluster export. The sequence matches the benchmark exactly. The expected answer is supported by both the GO annotation and the family-level biological knowledge, though the direct experimental evidence specifies the broader 'mitochondrion membrane' term.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains clear ABC transporter motifs (Walker A: 'GPSGVGKSTLIKLLFRMF', ABC signature region, and two transmembrane domains forming a multi-pass membrane protein). In eukaryotic cells, multi-pass alpha-helical ABC transporters localized to mitochondria are exclusively inner membrane proteins—the outer mitochondrial membrane contains beta-barrel porins, not ABC transporters. The long N-terminal Ser/Thr-rich extension is consistent with apicomplexan mitochondrial targeting signals. Chloroplast is excluded because the domain architecture does not match chloroplast envelope ABC transporters and no bipartite transit peptide is evident. Host cell is excluded because the protein is a membrane-bound organellar transporter, not a secreted/exported effector. ER is less likely given the N-terminal organellar targeting extension.


**Missing item-specific fact**

> Precise identification of this protein as the ABCB7/ATM1 family (rather than other mitochondrial ABC transporters like ABCB10) adds confidence but is not strictly required for the inner-membrane conclusion, since all mitochondrial multi-pass ABC transporters reside in the inner membrane.


**Reason**

> A model recognizing ABC transporter domain architecture and applying the general biological principle that mitochondrial ABC transporters are inner membrane proteins can distinguish D from the other options. The Ser/Thr-rich N-terminal extension provides additional support for organellar (mitochondrial) targeting in an apicomplexan context. Chloroplast and host cell are eliminable on structural grounds. ER is less likely given the targeting extension, though this distinction is the most challenging.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct. Chloroplast is excluded by domain architecture and absence of plastid-targeting features. Host cell is excluded by the membrane-bound organellar nature of the protein. ER is disfavored by the N-terminal targeting extension. Mitochondrial inner membrane is the only option consistent with a multi-pass ABC transporter bearing an organellar targeting signal in Toxoplasma.


### Important caveats

- The GO:0005743 (mitochondrial inner membrane) annotation carries only IEA:TreeGrafter evidence (computational homology transfer), while the experimental evidence supports the broader 'Mitochondrion membrane' term. The specific inner-membrane assignment relies on family-level knowledge of ABCB7/ATM1.
- The UniProt entry was first publicly released 2025-04-09; the benchmark sequence matches but the author's exact source snapshot is unknown.
- Apicomplexan mitochondrial targeting signals are atypical (Ser/Thr-rich, non-canonical), making sequence-based recognition of mitochondrial targeting more difficult than in model organisms.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely solely on sequence analysis and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains clear ABC transporter motifs (Walker A: 'GPSGVGKSTLIKLLFRMF', ABC signature region, and two transmembrane domains forming a multi-pass membrane protein). In eukaryotic cells, multi-pass alpha-helical ABC transporters localized to mitochondria are exclusively inner membrane proteins—the outer mitochondrial membrane contains beta-barrel porins, not ABC transporters. The long N-terminal Ser/Thr-rich extension is consistent with apicomplexan mitochondrial targeting signals. Chloroplast is excluded because the domain architecture does not match chloroplast envelope ABC transporters and no bipartite transit peptide is evident. Host cell is excluded because the protein is a membrane-bound organellar transporter, not a secreted/exported effector. ER is less likely given the N-terminal organellar targeting extension.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this protein as the ABCB7/ATM1 family (rather than other mitochondrial ABC transporters like ABCB10) adds confidence but is not strictly required for the inner-membrane conclusion, since all mitochondrial multi-pass ABC transporters reside in the inner membrane.",
    "reason": "A model recognizing ABC transporter domain architecture and applying the general biological principle that mitochondrial ABC transporters are inner membrane proteins can distinguish D from the other options. The Ser/Thr-rich N-terminal extension provides additional support for organellar (mitochondrial) targeting in an apicomplexan context. Chloroplast and host cell are eliminable on structural grounds. ER is less likely given the targeting extension, though this distinction is the most challenging."
  },
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry S8EXU2 (ATM1_TOXGM, ABC transporter ATM1/ABCB7-like from Toxoplasma gondii) carries GO:0005743 (mitochondrial inner membrane) annotation. The experimental subcellular location annotation states 'Mitochondrion membrane' (ECO:0000269, direct assay from PubMed:39207139; ECO:0000305 from PubMed:39348385), and the GO:0005743 assignment is via IEA:TreeGrafter (homology-based inference). The ABCB7/ATM1 family is well-characterized in yeast and other eukaryotes as a mitochondrial inner membrane transporter involved in Fe-S cluster export. The sequence matches the benchmark exactly. The expected answer is supported by both the GO annotation and the family-level biological knowledge, though the direct experimental evidence specifies the broader 'mitochondrion membrane' term."
  },
  "important_caveats": [
    "The GO:0005743 (mitochondrial inner membrane) annotation carries only IEA:TreeGrafter evidence (computational homology transfer), while the experimental evidence supports the broader 'Mitochondrion membrane' term. The specific inner-membrane assignment relies on family-level knowledge of ABCB7/ATM1.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark sequence matches but the author's exact source snapshot is unknown.",
    "Apicomplexan mitochondrial targeting signals are atypical (Ser/Thr-rich, non-canonical), making sequence-based recognition of mitochondrial targeting more difficult than in model organisms.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely solely on sequence analysis and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct. Chloroplast is excluded by domain architecture and absence of plastid-targeting features. Host cell is excluded by the membrane-bound organellar nature of the protein. ER is disfavored by the N-terminal targeting extension. Mitochondrial inner membrane is the only option consistent with a multi-pass ABC transporter bearing an organellar targeting signal in Toxoplasma."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry S8EXU2 (ATM1_TOXGM, ABC transporter ATM1/ABCB7-like from Toxoplasma gondii) carries GO:0005743 (mitochondrial inner membrane) annotation. The experimental subcellular location annotation states 'Mitochondrion membrane' (ECO:0000269, direct assay from PubMed:39207139; ECO:0000305 from PubMed:39348385), and the GO:0005743 assignment is via IEA:TreeGrafter (homology-based inference). The ABCB7/ATM1 family is well-characterized in yeast and other eukaryotes as a mitochondrial inner membrane transporter involved in Fe-S cluster export. The sequence matches the benchmark exactly. The expected answer is supported by both the GO annotation and the family-level biological knowledge, though the direct experimental evidence specifies the broader 'mitochondrion membrane' term.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains clear ABC transporter motifs (Walker A: 'GPSGVGKSTLIKLLFRMF', ABC signature region, and two transmembrane domains forming a multi-pass membrane protein). In eukaryotic cells, multi-pass alpha-helical ABC transporters localized to mitochondria are exclusively inner membrane proteins—the outer mitochondrial membrane contains beta-barrel porins, not ABC transporters. The long N-terminal Ser/Thr-rich extension is consistent with apicomplexan mitochondrial targeting signals. Chloroplast is excluded because the domain architecture does not match chloroplast envelope ABC transporters and no bipartite transit peptide is evident. Host cell is excluded because the protein is a membrane-bound organellar transporter, not a secreted/exported effector. ER is less likely given the N-terminal organellar targeting extension.",
    "missing_item_specific_fact": "Precise identification of this protein as the ABCB7/ATM1 family (rather than other mitochondrial ABC transporters like ABCB10) adds confidence but is not strictly required for the inner-membrane conclusion, since all mitochondrial multi-pass ABC transporters reside in the inner membrane.",
    "reason": "A model recognizing ABC transporter domain architecture and applying the general biological principle that mitochondrial ABC transporters are inner membrane proteins can distinguish D from the other options. The Ser/Thr-rich N-terminal extension provides additional support for organellar (mitochondrial) targeting in an apicomplexan context. Chloroplast and host cell are eliminable on structural grounds. ER is less likely given the targeting extension, though this distinction is the most challenging."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct. Chloroplast is excluded by domain architecture and absence of plastid-targeting features. Host cell is excluded by the membrane-bound organellar nature of the protein. ER is disfavored by the N-terminal targeting extension. Mitochondrial inner membrane is the only option consistent with a multi-pass ABC transporter bearing an organellar targeting signal in Toxoplasma."
  },
  "important_caveats": [
    "The GO:0005743 (mitochondrial inner membrane) annotation carries only IEA:TreeGrafter evidence (computational homology transfer), while the experimental evidence supports the broader 'Mitochondrion membrane' term. The specific inner-membrane assignment relies on family-level knowledge of ABCB7/ATM1.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark sequence matches but the author's exact source snapshot is unknown.",
    "Apicomplexan mitochondrial targeting signals are atypical (Ser/Thr-rich, non-canonical), making sequence-based recognition of mitochondrial targeting more difficult than in model organisms.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely solely on sequence analysis and general biological knowledge."
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

**Accession:** `S8EXU2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
"S8EXU2"
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39207139","source":"PubMed"}],"value":"ABCB7-like"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39207139","source":"PubMed"}],"value":"ABCB7L"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"39207139","source":"PubMed"}],"value":"TgABCB7L"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IDH9","source":"UniProtKB"}],"value":"7.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ABC transporter ATM1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39348385","source":"PubMed"}],"value":"TgATM1"}]}}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39207139","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"39348385","source":"PubMed"}],"id":"SL-0171","value":"Mitochondrion membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"database":"GO","id":"GO:0005743","properties":[{"key":"GoTerm","value":"C:mitochondrial inner membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"citation":{"authors":["Maclean A.E.","Sloan M.A.","Renaud E.A.","Argyle B.E.","Lewis W.H.","Ovciarikova J.","Demolombe V.","Waller R.F.","Besteiro S.","Sheiner L."],"citationCrossReferences":[{"database":"PubMed","id":"39207139"},{"database":"DOI","id":"10.1128/mbio.00872-24"}],"citationType":"journal article","firstPage":"e0087224","id":"39207139","journal":"MBio","lastPage":"e0087224","publicationDate":"2024","title":"The Toxoplasma gondii mitochondrial transporter ABCB7L is essential for the biogenesis of cytosolic and nuclear iron-sulfur cluster proteins and cytosolic translation.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","SUBUNIT","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8EXU2.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:58.976860+00:00.  

```json
{"citation":{"authors":["Shrivastava D.","Abboud E.","Ramchandra J.P.","Jha A.","Marq J.B.","Chaurasia A.","Mitra K.","Sadik M.","Siddiqi M.I.","Soldati-Favre D.","Kloehn J.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"39348385"},{"database":"DOI","id":"10.1371/journal.ppat.1012593"}],"citationType":"journal article","firstPage":"e1012593","id":"39348385","journal":"PLoS Pathog.","lastPage":"e1012593","publicationDate":"2024","title":"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.","volume":"20"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBUNIT","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `3c83d344f397e32f2e3203caf9b9d84cd10eaa76ba1ff03d22e5572308e0add9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 51-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane
CC       {ECO:0000269|PubMed:39207139, ECO:0000305|PubMed:39348385}; Multi-pass
CC       membrane protein {ECO:0000255}.
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8EXU2?format=txt&versions=59)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:34:03.453043+00:00.  

```text
DR   GO; GO:0005743; C:mitochondrial inner membrane; IEA:TreeGrafter.
```

Source SHA-256: `04a3f19563f6135254ffb6c7af171b94f9aa3d04e072b07ad86e250f49183933`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
