# active_site_0125

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0125.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 118 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLLYLVALFVASICSVTAQTWTSCNPLTTTCPPDQALGINTTFTFNKTLDDTIWNVTNGVLSHTDEGTEFTITGENQSPTMQSNFYIFFGIVESHVKMAKGAGIISSIVLQSDDLDEIDWEWVGYNTSEVQSNYFGKGNNETFNRGGYHYVPNADTEFHNYTTYWTQEKLEWWIDGKLARTLTYEDSQGAGKYYPQTPCNIRYGIWPAGIKGNAQGTIEWAGGLVDYSKAPFTMVLQSVRVHDFHTGKEYNYTDHSGSWQSIDVIAGNSTIANAIQNPPKSLSEKWAELPTGAKAGVYIGAGCVGAALLAGFIFFFIAQRKKGRLEHALEDAKWANERTEMSTFQNDWKQSEWKHKGYQPVN

[Multiple Choices]
A. Position 118 (Nucleophile)
B. Position 161 (Proton donor)
C. Position 358 (For beta-ketoacyl synthase activity)
D. Position 166 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies position 118 as the nucleophile. Its evidence is transferred from a related protein, so this supports the key but is not direct experimental validation for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a signal-peptide-like N-terminus and a conserved acidic motif around positions 118–122, consistent with a secreted fungal glycoside hydrolase. Transferable knowledge of such enzymes supports a catalytic glutamate pair, with the first glutamate acting as nucleophile; this favors option A over the alternative positions and the unrelated beta-ketoacyl synthase choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence and catalytic-motif inference meaningfully distinguishes the offered choice without requiring recall of this protein's database record. The precise annotation remains transferable rather than direct evidence from this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A matches the supported nucleophile assignment among the choices.


### Important caveats

- The supplied annotation assigns position 118 by similarity to another protein; it does not establish direct experimental confirmation for this sequence.
- The available evidence also annotates a proton donor at position 122, which is not among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a conserved acidic motif around positions 118–122, consistent with a secreted fungal glycoside hydrolase. Transferable knowledge of such enzymes supports a catalytic glutamate pair, with the first glutamate acting as nucleophile; this favors option A over the alternative positions and the unrelated beta-ketoacyl synthase choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and catalytic-motif inference meaningfully distinguishes the offered choice without requiring recall of this protein's database record. The precise annotation remains transferable rather than direct evidence from this protein."
  },
  "case_id": "active_site_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 118 as the nucleophile. Its evidence is transferred from a related protein, so this supports the key but is not direct experimental validation for this exact protein."
  },
  "important_caveats": [
    "The supplied annotation assigns position 118 by similarity to another protein; it does not establish direct experimental confirmation for this sequence.",
    "The available evidence also annotates a proton donor at position 122, which is not among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A matches the supported nucleophile assignment among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 118 as the nucleophile. Its evidence is transferred from a related protein, so this supports the key but is not direct experimental validation for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a signal-peptide-like N-terminus and a conserved acidic motif around positions 118–122, consistent with a secreted fungal glycoside hydrolase. Transferable knowledge of such enzymes supports a catalytic glutamate pair, with the first glutamate acting as nucleophile; this favors option A over the alternative positions and the unrelated beta-ketoacyl synthase choice.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and catalytic-motif inference meaningfully distinguishes the offered choice without requiring recall of this protein's database record. The precise annotation remains transferable rather than direct evidence from this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A matches the supported nucleophile assignment among the choices."
  },
  "important_caveats": [
    "The supplied annotation assigns position 118 by similarity to another protein; it does not establish direct experimental confirmation for this sequence.",
    "The available evidence also annotates a proton donor at position 122, which is not among the offered choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q4WXE6 annotates position 118 as 'Nucleophile' (Active site) with evidence code ECO:0000250 (inferred by similarity to P27051). This is a computational transfer annotation, not direct experimental evidence for this specific protein, but it is the recorded annotation. The amino acid at position 118 in the supplied sequence is E (Glutamic acid), consistent with a nucleophile in a glycoside hydrolase. The expected answer 'Position 118 (Nucleophile)' matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains a well-known GH18 (glycoside hydrolase family 18) catalytic motif: E-X-X-X-E. Counting from the supplied sequence, position 118 is E and position 122 is E, separated by exactly 4 residues (I-D-W), giving the classic E118-X-X-X-E122 dyad. In GH18 chitinases/transglycosylases (a large family including lysozymes, chitinases, and chitin transglycosylases), the first glutamate in this pattern is the nucleophile and the second is the proton donor. This family-level motif is extensively documented across hundreds of GH18 members. The other options place catalytic labels on residues that are not catalytic in glycoside hydrolases: position 161 is N (Asparagine), position 166 is W (Tryptophan), and position 358 is G (Glycine)—none of which serve as nucleophiles or proton donors in this enzyme class. Additionally, option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (fatty acid synthesis), making it clearly inapplicable to a protein with glycoside hydrolase architecture (GAG motifs, ~363 aa GH domain, transmembrane segment near C-terminus). A knowledgeable model can recognize the E-X-X-X-E spacing as the GH18 catalytic signature and assign nucleophile to the first E.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The E-X-X-X-E catalytic dyad is a conserved, family-level feature of GH18 glycoside hydrolases, transferable from knowledge of other chitinases and lysozymes. The amino acid identities at the distractor positions (N, W, G) are incompatible with nucleophile or proton donor roles in any glycoside hydrolase. The 'beta-ketoacyl synthase' reference in option C is from a completely unrelated enzyme class. These features allow a model to select A without recalling this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 118 (E, Glutamic acid) is consistent with a nucleophile in a glycoside hydrolase. The other positions carry residues (N, W, G) that are not catalytic in this enzyme class, and option C references an unrelated enzyme function. No alternative is defensible.


### Important caveats

- The UniProt annotation for position 118 is by similarity (ECO:0000250, transferred from P27051), not direct experimental evidence for Crh3 itself.
- The protein is annotated as having both chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity; the nucleophile role is shared between these activities.
- The E-X-X-X-E motif is a strong family-level indicator but not absolutely diagnostic of GH18; however, combined with the overall sequence architecture (GAG motifs, domain length, transmembrane segment), the GH18 assignment is well-supported.
- The evidence code indicates the annotation was inferred from a homolog, so the exact catalytic mechanism in this specific protein may warrant experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains a well-known GH18 (glycoside hydrolase family 18) catalytic motif: E-X-X-X-E. Counting from the supplied sequence, position 118 is E and position 122 is E, separated by exactly 4 residues (I-D-W), giving the classic E118-X-X-X-E122 dyad. In GH18 chitinases/transglycosylases (a large family including lysozymes, chitinases, and chitin transglycosylases), the first glutamate in this pattern is the nucleophile and the second is the proton donor. This family-level motif is extensively documented across hundreds of GH18 members. The other options place catalytic labels on residues that are not catalytic in glycoside hydrolases: position 161 is N (Asparagine), position 166 is W (Tryptophan), and position 358 is G (Glycine)—none of which serve as nucleophiles or proton donors in this enzyme class. Additionally, option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (fatty acid synthesis), making it clearly inapplicable to a protein with glycoside hydrolase architecture (GAG motifs, ~363 aa GH domain, transmembrane segment near C-terminus). A knowledgeable model can recognize the E-X-X-X-E spacing as the GH18 catalytic signature and assign nucleophile to the first E.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The E-X-X-X-E catalytic dyad is a conserved, family-level feature of GH18 glycoside hydrolases, transferable from knowledge of other chitinases and lysozymes. The amino acid identities at the distractor positions (N, W, G) are incompatible with nucleophile or proton donor roles in any glycoside hydrolase. The 'beta-ketoacyl synthase' reference in option C is from a completely unrelated enzyme class. These features allow a model to select A without recalling this specific protein's database entry."
  },
  "case_id": "active_site_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 annotates position 118 as 'Nucleophile' (Active site) with evidence code ECO:0000250 (inferred by similarity to P27051). This is a computational transfer annotation, not direct experimental evidence for this specific protein, but it is the recorded annotation. The amino acid at position 118 in the supplied sequence is E (Glutamic acid), consistent with a nucleophile in a glycoside hydrolase. The expected answer 'Position 118 (Nucleophile)' matches the database annotation exactly."
  },
  "important_caveats": [
    "The UniProt annotation for position 118 is by similarity (ECO:0000250, transferred from P27051), not direct experimental evidence for Crh3 itself.",
    "The protein is annotated as having both chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity; the nucleophile role is shared between these activities.",
    "The E-X-X-X-E motif is a strong family-level indicator but not absolutely diagnostic of GH18; however, combined with the overall sequence architecture (GAG motifs, domain length, transmembrane segment), the GH18 assignment is well-supported.",
    "The evidence code indicates the annotation was inferred from a homolog, so the exact catalytic mechanism in this specific protein may warrant experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 118 (E, Glutamic acid) is consistent with a nucleophile in a glycoside hydrolase. The other positions carry residues (N, W, G) that are not catalytic in this enzyme class, and option C references an unrelated enzyme function. No alternative is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q4WXE6 annotates position 118 as 'Nucleophile' (Active site) with evidence code ECO:0000250 (inferred by similarity to P27051). This is a computational transfer annotation, not direct experimental evidence for this specific protein, but it is the recorded annotation. The amino acid at position 118 in the supplied sequence is E (Glutamic acid), consistent with a nucleophile in a glycoside hydrolase. The expected answer 'Position 118 (Nucleophile)' matches the database annotation exactly.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains a well-known GH18 (glycoside hydrolase family 18) catalytic motif: E-X-X-X-E. Counting from the supplied sequence, position 118 is E and position 122 is E, separated by exactly 4 residues (I-D-W), giving the classic E118-X-X-X-E122 dyad. In GH18 chitinases/transglycosylases (a large family including lysozymes, chitinases, and chitin transglycosylases), the first glutamate in this pattern is the nucleophile and the second is the proton donor. This family-level motif is extensively documented across hundreds of GH18 members. The other options place catalytic labels on residues that are not catalytic in glycoside hydrolases: position 161 is N (Asparagine), position 166 is W (Tryptophan), and position 358 is G (Glycine)—none of which serve as nucleophiles or proton donors in this enzyme class. Additionally, option C references 'beta-ketoacyl synthase activity,' an entirely unrelated enzyme class (fatty acid synthesis), making it clearly inapplicable to a protein with glycoside hydrolase architecture (GAG motifs, ~363 aa GH domain, transmembrane segment near C-terminus). A knowledgeable model can recognize the E-X-X-X-E spacing as the GH18 catalytic signature and assign nucleophile to the first E.",
    "missing_item_specific_fact": "",
    "reason": "The E-X-X-X-E catalytic dyad is a conserved, family-level feature of GH18 glycoside hydrolases, transferable from knowledge of other chitinases and lysozymes. The amino acid identities at the distractor positions (N, W, G) are incompatible with nucleophile or proton donor roles in any glycoside hydrolase. The 'beta-ketoacyl synthase' reference in option C is from a completely unrelated enzyme class. These features allow a model to select A without recalling this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 118 (E, Glutamic acid) is consistent with a nucleophile in a glycoside hydrolase. The other positions carry residues (N, W, G) that are not catalytic in this enzyme class, and option C references an unrelated enzyme function. No alternative is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for position 118 is by similarity (ECO:0000250, transferred from P27051), not direct experimental evidence for Crh3 itself.",
    "The protein is annotated as having both chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity; the nucleophile role is shared between these activities.",
    "The E-X-X-X-E motif is a strong family-level indicator but not absolutely diagnostic of GH18; however, combined with the overall sequence architecture (GAG motifs, domain length, transmembrane segment), the GH18 assignment is well-supported.",
    "The evidence code indicates the annotation was inferred from a homolog, so the exact catalytic mechanism in this specific protein may warrant experimental confirmation."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "current_entry_audit": {
    "entryVersion": 100,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-17",
    "sequenceVersion": 2
  },
  "current_record_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 98,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WXE6",
  "selected_historical_entry_version": 98,
  "selected_historical_record_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "3deb859056a8160d9cec48ee8776946ad4066ac14f699364c29390fefc1dc15d",
  "selected_historical_version": {
    "accession": "Q4WXE6",
    "database": "Swiss-Prot",
    "entryVersion": 98,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH3_ASPFU",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WXE6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":100,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-17\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitinase crh3\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Chitin transglycosylase crh3\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30971696\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P27051\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":122},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":122},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":203},\"start\":{\"modifier\":\"EXACT\",\"value\":203}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":207},\"start\":{\"modifier\":\"EXACT\",\"value\":207}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":218},\"start\":{\"modifier\":\"EXACT\",\"value\":218}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXE6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Fang W.\",\"Sanz A.B.\",\"Bartual S.G.\",\"Wang B.\",\"Ferenbach A.T.\",\"Farkas V.\",\"Hurtado-Guerrero R.\",\"Arroyo J.\",\"van Aalten D.M.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30971696\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-019-09674-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"1669\",\"id\":\"30971696\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"1669\",\"publicationDate\":\"2019\",\"title\":\"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.\",\"volume\":\"10\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:56.355475+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e1004c3faedfbf01d9968270612a17ecce9521032908c5e8d6ffdc02ba658e78",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXE6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H1",
  "excerpt": "ID   CRH3_ASPFU              Reviewed;         363 AA.\nAC   Q4WXE6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-APR-2007, sequence version 2.\nDT   28-JAN-2026, entry version 98.\nDE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000303|PubMed:30971696};\nDE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};\nDE   Flags: Precursor;\nGN   Name=crh3 {ECO:0000303|PubMed:30971696}; ORFNames=AFUA_3G09250;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;\nRA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,\nRA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;\nRT   \"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh\nRT   transglycosylases.\";\nRL   Nat. Commun. 10:1669-1669(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        118\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        122\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P27051\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         122\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         203\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         207\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         218\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.140024+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af4f50551f4ffbdc3078466e912cc6a0045c45d27fe12a91ec27846d9bdd773d",
  "url": "https://rest.uniprot.org/unisave/Q4WXE6?format=txt&versions=98"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
