# EC_number_0111

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0111.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELVLCFVIITISGVIRESSALLLRSPTSNDVFGELVASAERAQPLATRLTKRISRLNFNDREDDFWEDHGDASWNNSYTLVNGRTTLGSENRRRPASHSLIERPYYRDGRLSPVLGVQERRGRSVHSYHEEPVSFFDQRAFDEYTFRRRSQLHRQRARAGLRSRIKQNVRRLWTSARGAVRGWGRRVRRKIGDLFVGHLMPQLRRLRFWDQGLPPVVPPLIGNEPGQASVALVAERMEARLREKTLTEKNPTEAQQAVGTYLINSAENTWFISIPGGRYILLKKRGFLGGGGFGLVYHVEHPTTGQPFALKIFVQRVMNNEVGDKISDLIEDEFGVMKYFPPEWTPARMYSELRFMVPLLKLRVLGKPEFQDARNHLRIFSVCALFPKAQGDLEEAAALLADMDRTNAYNMRMSSTIQMVKLLARFHAFGLVHGDVKLQNFLVDKSGLLLLSDFTQILRTNERRYPPVVTVLYMSPEIATCLITRLRNAIPYTAEIDSWMLGISLYRLWCGDFPFGITLDATALQVAGIVIRSSASSLDFASCHDIPEQFREMIVGFLRKTPGVRLSPQQALEQFSLLNWKGPSPASDTASESEPVSTEEAALLQKE

[Multiple Choices]
A. 2.7.11.24
B. 2.7.11.1
C. 3.2.1.55
D. 1.14.13.238
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact supplied sequence matches the UniProt entry, which assigns EC 2.7.11.1 and records serine- and threonine-phosphorylation reactions. The threonyl reaction carries experimental evidence (ECO:0000269); the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a eukaryotic protein-kinase-like catalytic domain, including a glycine-rich region and kinase catalytic motifs, so a protein kinase EC is a much better fit than the glycosidase or monooxygenase choices. Its signal-peptide-like N-terminus and long extension before the kinase domain are more consistent with a specialized secretory kinase than a conventional MAP kinase; the sequence also lacks the characteristic MAPK activation-loop TXY motif. These transferable features favor the broad serine/threonine-protein kinase class, B, over the MAPK-specific alternative A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and architecture features credibly distinguish the offered serine/threonine kinase option from the alternatives. They do not independently establish the exact physiological substrates or experimental activity, but that finer proof is not needed to make a meaningful choice among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase-like sequence supports a protein kinase classification, while the alternatives describe a more specific MAPK class or unrelated enzyme activities; no second option is comparably defensible from the supplied sequence.


### Important caveats

- The family-level inference supports the choice probabilistically; the reviewer-only experimental annotation is stronger evidence for the exact EC assignment.
- The reviewer-only organism and protein-name annotations were not inputs to the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a eukaryotic protein-kinase-like catalytic domain, including a glycine-rich region and kinase catalytic motifs, so a protein kinase EC is a much better fit than the glycosidase or monooxygenase choices. Its signal-peptide-like N-terminus and long extension before the kinase domain are more consistent with a specialized secretory kinase than a conventional MAP kinase; the sequence also lacks the characteristic MAPK activation-loop TXY motif. These transferable features favor the broad serine/threonine-protein kinase class, B, over the MAPK-specific alternative A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and architecture features credibly distinguish the offered serine/threonine kinase option from the alternatives. They do not independently establish the exact physiological substrates or experimental activity, but that finer proof is not needed to make a meaningful choice among these options."
  },
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which assigns EC 2.7.11.1 and records serine- and threonine-phosphorylation reactions. The threonyl reaction carries experimental evidence (ECO:0000269); the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The family-level inference supports the choice probabilistically; the reviewer-only experimental annotation is stronger evidence for the exact EC assignment.",
    "The reviewer-only organism and protein-name annotations were not inputs to the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase-like sequence supports a protein kinase classification, while the alternatives describe a more specific MAPK class or unrelated enzyme activities; no second option is comparably defensible from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry, which assigns EC 2.7.11.1 and records serine- and threonine-phosphorylation reactions. The threonyl reaction carries experimental evidence (ECO:0000269); the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a eukaryotic protein-kinase-like catalytic domain, including a glycine-rich region and kinase catalytic motifs, so a protein kinase EC is a much better fit than the glycosidase or monooxygenase choices. Its signal-peptide-like N-terminus and long extension before the kinase domain are more consistent with a specialized secretory kinase than a conventional MAP kinase; the sequence also lacks the characteristic MAPK activation-loop TXY motif. These transferable features favor the broad serine/threonine-protein kinase class, B, over the MAPK-specific alternative A.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and architecture features credibly distinguish the offered serine/threonine kinase option from the alternatives. They do not independently establish the exact physiological substrates or experimental activity, but that finer proof is not needed to make a meaningful choice among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase-like sequence supports a protein kinase classification, while the alternatives describe a more specific MAPK class or unrelated enzyme activities; no second option is comparably defensible from the supplied sequence."
  },
  "important_caveats": [
    "The family-level inference supports the choice probabilistically; the reviewer-only experimental annotation is stronger evidence for the exact EC assignment.",
    "The reviewer-only organism and protein-name annotations were not inputs to the answerability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 with experimental evidence (ECO:0000269, PubMed:24832449 - Etheridge et al. 2014). The catalytic activity comments confirm both threonine and serine phosphorylation of protein substrates consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence in the benchmark matches the UniProt entry (SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein kinase catalytic motifs (e.g., 'GDLFVGHL' resembling the VAIK/catalytic loop region, a modified 'DFP' in 'CGDFPFGITLD' resembling the DFG motif, and an 'HR'-containing catalytic loop), which immediately eliminates C (3.2.1.55, alpha-L-fucosidase, a glycosidase with GH29/GH95 folds) and D (1.14.13.238, a cytochrome P450 oxidoreductase requiring heme-binding Cys motifs). The remaining challenge is distinguishing A (2.7.11.24, MAP4K) from B (2.7.11.1, generic Ser/Thr protein kinase). MAP4K is a member of the Ste20-like kinase family, an intracellular component of the MAPK signaling cascade with characteristic SH3/PH domain architecture and specific activation-loop sequences. The given sequence begins with a hydrophobic signal peptide (MELVLCFVIITISGVIRESS...), indicating a secreted protein, which is incompatible with the intracellular signaling role of MAP4K. Additionally, the overall domain architecture (a single kinase-like domain embedded in a larger protein with N-terminal secretion signal and rhoptry-like features) does not match the Ste20/MAP4K family. EC 2.7.11.1 serves as the default classification for Ser/Thr protein kinases lacking a more specific EC assignment, making it the appropriate choice for a secreted effector kinase with general Ser/Thr activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify kinase motifs to eliminate C and D, then use the presence of a signal peptide (secreted protein) and absence of Ste20/MAP4K family features to distinguish B from A. This relies on transferable knowledge of MAP4K biology (intracellular, Ste20-like, MAPK cascade member) and the convention that EC 2.7.11.1 is the default for Ser/Thr kinases without more specific classification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are eliminated by basic enzyme class identification from sequence features. Between A and B, the signal peptide and non-Ste20 architecture provide a clear basis for selecting B over A. No ambiguity remains among the offered choices.


### Important caveats

- The distinction between EC 2.7.11.1 (generic Ser/Thr kinase) and EC 2.7.11.24 (MAP4K) relies on recognizing that EC 2.7.11.1 is the default category; a model unfamiliar with EC nomenclature conventions might struggle with this distinction.
- The kinase domain in ROP17 is somewhat atypical (it is described in literature as having an unusual kinase fold), but the presence of canonical motifs is sufficient for family-level classification.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general kinase biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase catalytic motifs (e.g., 'GDLFVGHL' resembling the VAIK/catalytic loop region, a modified 'DFP' in 'CGDFPFGITLD' resembling the DFG motif, and an 'HR'-containing catalytic loop), which immediately eliminates C (3.2.1.55, alpha-L-fucosidase, a glycosidase with GH29/GH95 folds) and D (1.14.13.238, a cytochrome P450 oxidoreductase requiring heme-binding Cys motifs). The remaining challenge is distinguishing A (2.7.11.24, MAP4K) from B (2.7.11.1, generic Ser/Thr protein kinase). MAP4K is a member of the Ste20-like kinase family, an intracellular component of the MAPK signaling cascade with characteristic SH3/PH domain architecture and specific activation-loop sequences. The given sequence begins with a hydrophobic signal peptide (MELVLCFVIITISGVIRESS...), indicating a secreted protein, which is incompatible with the intracellular signaling role of MAP4K. Additionally, the overall domain architecture (a single kinase-like domain embedded in a larger protein with N-terminal secretion signal and rhoptry-like features) does not match the Ste20/MAP4K family. EC 2.7.11.1 serves as the default classification for Ser/Thr protein kinases lacking a more specific EC assignment, making it the appropriate choice for a secreted effector kinase with general Ser/Thr activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify kinase motifs to eliminate C and D, then use the presence of a signal peptide (secreted protein) and absence of Ste20/MAP4K family features to distinguish B from A. This relies on transferable knowledge of MAP4K biology (intracellular, Ste20-like, MAPK cascade member) and the convention that EC 2.7.11.1 is the default for Ser/Thr kinases without more specific classification."
  },
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 with experimental evidence (ECO:0000269, PubMed:24832449 - Etheridge et al. 2014). The catalytic activity comments confirm both threonine and serine phosphorylation of protein substrates consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence in the benchmark matches the UniProt entry (SHA256 confirmed)."
  },
  "important_caveats": [
    "The distinction between EC 2.7.11.1 (generic Ser/Thr kinase) and EC 2.7.11.24 (MAP4K) relies on recognizing that EC 2.7.11.1 is the default category; a model unfamiliar with EC nomenclature conventions might struggle with this distinction.",
    "The kinase domain in ROP17 is somewhat atypical (it is described in literature as having an unusual kinase fold), but the presence of canonical motifs is sufficient for family-level classification.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general kinase biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are eliminated by basic enzyme class identification from sequence features. Between A and B, the signal peptide and non-Ste20 architecture provide a clear basis for selecting B over A. No ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for Q2PAY3 (ROP17_TOXGO) assigns EC 2.7.11.1 with experimental evidence (ECO:0000269, PubMed:24832449 - Etheridge et al. 2014). The catalytic activity comments confirm both threonine and serine phosphorylation of protein substrates consistent with EC 2.7.11.1 (non-specific serine/threonine protein kinase). The sequence in the benchmark matches the UniProt entry (SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein kinase catalytic motifs (e.g., 'GDLFVGHL' resembling the VAIK/catalytic loop region, a modified 'DFP' in 'CGDFPFGITLD' resembling the DFG motif, and an 'HR'-containing catalytic loop), which immediately eliminates C (3.2.1.55, alpha-L-fucosidase, a glycosidase with GH29/GH95 folds) and D (1.14.13.238, a cytochrome P450 oxidoreductase requiring heme-binding Cys motifs). The remaining challenge is distinguishing A (2.7.11.24, MAP4K) from B (2.7.11.1, generic Ser/Thr protein kinase). MAP4K is a member of the Ste20-like kinase family, an intracellular component of the MAPK signaling cascade with characteristic SH3/PH domain architecture and specific activation-loop sequences. The given sequence begins with a hydrophobic signal peptide (MELVLCFVIITISGVIRESS...), indicating a secreted protein, which is incompatible with the intracellular signaling role of MAP4K. Additionally, the overall domain architecture (a single kinase-like domain embedded in a larger protein with N-terminal secretion signal and rhoptry-like features) does not match the Ste20/MAP4K family. EC 2.7.11.1 serves as the default classification for Ser/Thr protein kinases lacking a more specific EC assignment, making it the appropriate choice for a secreted effector kinase with general Ser/Thr activity.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify kinase motifs to eliminate C and D, then use the presence of a signal peptide (secreted protein) and absence of Ste20/MAP4K family features to distinguish B from A. This relies on transferable knowledge of MAP4K biology (intracellular, Ste20-like, MAPK cascade member) and the convention that EC 2.7.11.1 is the default for Ser/Thr kinases without more specific classification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are eliminated by basic enzyme class identification from sequence features. Between A and B, the signal peptide and non-Ste20 architecture provide a clear basis for selecting B over A. No ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The distinction between EC 2.7.11.1 (generic Ser/Thr kinase) and EC 2.7.11.24 (MAP4K) relies on recognizing that EC 2.7.11.1 is the default category; a model unfamiliar with EC nomenclature conventions might struggle with this distinction.",
    "The kinase domain in ROP17 is somewhat atypical (it is described in literature as having an unusual kinase fold), but the presence of canonical motifs is sufficient for family-level classification.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning argument stands independently on sequence features and general kinase biology."
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
  "benchmark_sequence_length": 608,
  "benchmark_sequence_sha256": "5efc2102f3d29e95c5037c2e1a6472b612c3daed4aec52f46cef941c11510320",
  "current_entry_audit": {
    "entryVersion": 87,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-02-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 608,
  "current_source_sequence_sha256": "5efc2102f3d29e95c5037c2e1a6472b612c3daed4aec52f46cef941c11510320",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 86,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2PAY3",
  "selected_historical_entry_version": 86,
  "selected_historical_record_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "selected_historical_source_sequence_length": 608,
  "selected_historical_source_sequence_sha256": "5efc2102f3d29e95c5037c2e1a6472b612c3daed4aec52f46cef941c11510320",
  "selected_historical_version": {
    "accession": "Q2PAY3",
    "database": "Swiss-Prot",
    "entryVersion": 86,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ROP17_TOXGO",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2PAY3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":87,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-02-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAJ27112.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAJ27112.1\",\"source\":\"EMBL\"}],\"value\":\"Rhoptry protein 17\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34180401\",\"source\":\"PubMed\"}],\"value\":\"TgROP17\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24832449\",\"source\":\"PubMed\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine/threonine-protein kinase ROP17\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24832449\",\"source\":\"PubMed\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24832449\",\"source\":\"PubMed\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Etheridge R.D.\",\"Alaganan A.\",\"Tang K.\",\"Lou H.J.\",\"Turk B.E.\",\"Sibley L.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24832449\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.chom.2014.04.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"24832449\",\"journal\":\"Cell Host Microbe\",\"lastPage\":\"550\",\"publicationDate\":\"2014\",\"title\":\"The Toxoplasma pseudokinase ROP5 forms complexes with ROP18 and ROP17 kinases that synergize to control acute virulence in mice.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INTERACTION WITH ROP5\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo M.\",\"Sun J.\",\"Wang W.T.\",\"Liu H.Y.\",\"Liu Y.H.\",\"Qin K.R.\",\"Hu J.R.\",\"Li X.Y.\",\"Liu H.L.\",\"Wang W.\",\"Chen Z.Y.\",\"Wang C.F.\",\"Wang H.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34180401\"},{\"database\":\"DOI\",\"id\":\"10.14411/fp.2021.016\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"34180401\",\"journal\":\"Folia Parasitol.\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Toxoplasma gondii ROP17 promotes autophagy via the Bcl-2-Beclin 1 pathway.\",\"volume\":\"68\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH HUMAN BCL2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:30:36.273311+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6706ba31663e0eeb6d66fbdf81baeb771e31266ea82e6b187e4763189ddeb230",
  "url": "https://rest.uniprot.org/uniprotkb/Q2PAY3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H1",
  "excerpt": "ID   ROP17_TOXGO             Reviewed;         608 AA.\nAC   Q2PAY3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-FEB-2006, sequence version 1.\nDT   28-JAN-2026, entry version 86.\nDE   RecName: Full=Serine/threonine-protein kinase ROP17 {ECO:0000305};\nDE            EC=2.7.11.1 {ECO:0000269|PubMed:24832449};\nDE   AltName: Full=Rhoptry protein 17 {ECO:0000312|EMBL:CAJ27112.1};\nDE   AltName: Full=TgROP17 {ECO:0000303|PubMed:34180401};\nDE   Flags: Precursor;\nGN   Name=rop17 {ECO:0000312|EMBL:CAJ27112.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|EMBL:CAJ27112.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Serine/threonine-protein kinase ROP17 {ECO:0000305};\nDE            EC=2.7.11.1 {ECO:0000269|PubMed:24832449};\nDE   AltName: Full=Rhoptry protein 17 {ECO:0000312|EMBL:CAJ27112.1};\nDE   AltName: Full=TgROP17 {ECO:0000303|PubMed:34180401};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   IDENTIFICATION BY MASS SPECTROMETRY, FUNCTION, CATALYTIC ACTIVITY,\nRP   INTERACTION WITH ROP5, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=24832449; DOI=10.1016/j.chom.2014.04.002;\nRA   Etheridge R.D., Alaganan A., Tang K., Lou H.J., Turk B.E., Sibley L.D.;\nRT   \"The Toxoplasma pseudokinase ROP5 forms complexes with ROP18 and ROP17\nRT   kinases that synergize to control acute virulence in mice.\";\nRL   Cell Host Microbe 15:537-550(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H4",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH HUMAN BCL2.\nRX   PubMed=34180401; DOI=10.14411/fp.2021.016;\nRA   Guo M., Sun J., Wang W.T., Liu H.Y., Liu Y.H., Qin K.R., Hu J.R., Li X.Y.,\nRA   Liu H.L., Wang W., Chen Z.Y., Wang C.F., Wang H.L.;\nRT   \"Toxoplasma gondii ROP17 promotes autophagy via the Bcl-2-Beclin 1\nRT   pathway.\";\nRL   Folia Parasitol. 68:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000269|PubMed:24832449};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000305|PubMed:24832449};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:38.452820+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b556cca06da62f63e90c588009b9095a040ad3bb5a30da56151ae475acf8019a",
  "url": "https://rest.uniprot.org/unisave/Q2PAY3?format=txt&versions=86"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
