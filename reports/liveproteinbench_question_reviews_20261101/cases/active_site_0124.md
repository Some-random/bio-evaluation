# active_site_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 154 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. Position 124 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 58 (Proton donor)
D. Position 207 (Proton donor)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.


**Missing item-specific fact**

> The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.


**Reason**

> Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence.


### Important caveats

- The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.
- The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.",
    "reason": "Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.",
    "The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice B matches the UniProt active-site annotation at position 154, described as an acyl-thioester intermediate. The annotation applies to the exact sequence supplied, but its evidence is computationally assigned by PIRSR rather than direct experimental evidence for this residue.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich region that may be consistent with a catalytic cysteine, but the input does not establish the protein’s identity, reaction mechanism, or which residue carries the acyl-thioester intermediate.",
    "missing_item_specific_fact": "The protein-specific assignment of position 154 as the acyl-thioester intermediate site, available here as a PIRSR-based active-site annotation.",
    "reason": "Selecting B requires an item-specific catalytic-site assignment not stated in the question. Recognizing or inferring the protein family from the sequence would not, by itself, supply that exact residue-role annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports position 154 and none of the other listed positions is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The annotation is computationally assigned (ECO:0000255; PIRSR), not shown here to be experimentally validated.",
    "The exact sequence match is established by reviewer-only evidence; this identity and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [C4](#evidence-c4), [C17](#evidence-c17), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.


**Missing item-specific fact**

> Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.


**Reason**

> The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers.


### Important caveats

- The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.
- The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.
- The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.
- The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.",
    "reason": "The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation."
  },
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "C4",
      "C17",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3)."
  },
  "important_caveats": [
    "The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.",
    "The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.",
    "The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.",
    "The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WWR8 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Aspergillus fumigatus) explicitly annotates position 154 as 'Active site: Acyl-thioester intermediate' (evidence C5, H4). The sequence at position 154 is indeed Cysteine, consistent with the known ASADH catalytic mechanism. The annotation evidence code is ECO:0000255 (inferred by similarity, PIRSR000148-1), meaning it is a computational/curatorial inference from homology to characterized ASADH enzymes rather than direct experimental measurement on this specific protein, but it is consistent with well-established ASADH biochemistry and supported by X-ray crystallography (PDB 5JW6, evidence H3).",
    "evidence_ids": ["C5", "H4", "C1", "C4", "C17", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the Rossmann fold motif 'GATGSVG' (positions 12-18), identifying this as an NAD(P)-binding dehydrogenase. The well-known ASADH catalytic mechanism requires a catalytic Cysteine to form an acyl-thioester intermediate with the aspartyl-phosphate substrate. Among the four options, only position 154 is a Cysteine; position 124 is Proline, position 58 is Threonine, and position 207 is Glycine. None of Pro, Thr, or Gly can form a thioester bond (which requires a thiol group). The described chemical role 'Acyl-thioester intermediate' is chemically incompatible with Pro, Thr, or Gly, leaving only the Cys at 154 as the viable answer. Additionally, Pro and Gly lack the side-chain functionality needed for proton donation, further eliminating A, C, and D.",
    "missing_item_specific_fact": "Precise recognition that this is ASADH (rather than another NAD(P)-dependent dehydrogenase) requires either homology knowledge or database lookup, though the Rossmann fold and overall sequence composition provide partial clues. The exact catalytic Cys position among the multiple Cys residues (9, 72, 80, 150, 154, 242, 286) in the sequence is not trivially derivable from sequence alone without structural context.",
    "reason": "The amino acid chemistry provides a concrete discriminating argument: only a Cys thiol can form an acyl-thioester intermediate, and only option B places a Cys at the stated position. The other three options assign roles (proton donor) to residues (Pro, Thr, Gly) that are chemically implausible for that role in a dehydrogenase active site. This chemical reasoning, combined with recognition of the Rossmann fold as an NAD(P)-binding motif, provides meaningful grounds to select B without requiring memorization of the specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The chemical requirement of a Cys thiol for acyl-thioester formation uniquely selects position 154 among the four options. The other options assign chemically implausible roles to their respective residues (Pro as proton donor, Thr as proton donor in this context, Gly as proton donor). No ambiguity in defensible answers."
  },
  "important_caveats": [
    "The UniProt active-site annotation (position 154) is based on ECO:0000255 (inferred by similarity via PIRSR000148-1), not direct experimental mutagenesis on this specific A. fumigatus enzyme. However, the ASADH catalytic mechanism (catalytic Cys forming acyl-thioester) is well-established across the enzyme family.",
    "The sequence contains multiple Cysteines (positions 9, 72, 80, 150, 154, 242, 286); identifying position 154 specifically as THE catalytic Cys among these requires structural or homology knowledge beyond simple amino-acid chemistry.",
    "The question does not name the enzyme; identification as ASADH relies on recognizing the Rossmann fold and sequence context, which is partially but not fully derivable from the provided sequence alone.",
    "The reviewer evidence is from UniProt entry Q4WWR8 (entry version 118-120), which post-dates the likely author construction date; the annotation may have been added after the benchmark was created."
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

**Accession:** `Q4WWR8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
"Q4WWR8"
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"28045392","source":"PubMed"}],"value":"AfASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"28045392","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"description":"Acyl-thioester intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR000148-1","source":"PIRSR"}],"location":{"end":{"modifier":"EXACT","value":154},"start":{"modifier":"EXACT","value":154}},"type":"Active site"}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:55.999038+00:00.  

```json
{"citation":{"authors":["Dahal G.P.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"28045392"},{"database":"DOI","id":"10.1107/s2053230x16020070"}],"citationType":"journal article","firstPage":"36","id":"28045392","journal":"Acta Crystallogr. F","lastPage":"44","publicationDate":"2017","title":"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.","volume":"73"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5JW6","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 57-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5JW6}
RP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=28045392; DOI=10.1107/s2053230x16020070;
RA   Dahal G.P., Viola R.E.;
RT   "Structure of a fungal form of aspartate-semialdehyde dehydrogenase from
RT   Aspergillus fumigatus.";
RL   Acta Crystallogr. F 73:36-44(2017).
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)  
**Locator:** `lines 165-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-02T04:31:00.563757+00:00.  

```text
FT   ACT_SITE        154
FT                   /note="Acyl-thioester intermediate"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR000148-1"
```

Source SHA-256: `048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
