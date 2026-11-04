# GO_molecular_function_0044

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0044.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — glycosyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM

[Multiple Choices]
A. GTPase activity
B. glycosyltransferase activity
C. nutrient reservoir activity
D. hydrolase activity, acting on glycosyl bonds
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched annotation describes the protein as a dual chitinase/transglycosylase and specifically reports transfer of chitin to beta-glucan, supporting glycosyltransferase activity. This support is not exclusive: the same evidence also reports chitin-hydrolyzing activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence is consistent with a chitin-active enzyme, and transferable knowledge of such enzymes can support both glycosyl-bond hydrolysis and transglycosylation. That does not establish which coupled activity should count as its primary function among B and D; the supplied input offers no basis to prioritize one.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The protein is annotated as having both transglycosylase activity (B) and chitinase activity, which is a glycosyl-bond hydrolase activity (D). The options do not define how to choose a primary activity when both are reported.


### Important caveats

- The evidence for B includes a computational GO annotation and functional annotation that combines evidence by similarity with a cited publication; the supplied excerpts do not establish that B is uniquely primary.
- The sequence match supports applying these annotations to the supplied sequence, but does not resolve the relative primacy of the two activities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "",
    "reason": "The sequence is consistent with a chitin-active enzyme, and transferable knowledge of such enzymes can support both glycosyl-bond hydrolysis and transglycosylation. That does not establish which coupled activity should count as its primary function among B and D; the supplied input offers no basis to prioritize one."
  },
  "case_id": "GO_molecular_function_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation describes the protein as a dual chitinase/transglycosylase and specifically reports transfer of chitin to beta-glucan, supporting glycosyltransferase activity. This support is not exclusive: the same evidence also reports chitin-hydrolyzing activity."
  },
  "important_caveats": [
    "The evidence for B includes a computational GO annotation and functional annotation that combines evidence by similarity with a cited publication; the supplied excerpts do not establish that B is uniquely primary.",
    "The sequence match supports applying these annotations to the supplied sequence, but does not resolve the relative primacy of the two activities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The protein is annotated as having both transglycosylase activity (B) and chitinase activity, which is a glycosyl-bond hydrolase activity (D). The options do not define how to choose a primary activity when both are reported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation describes the protein as a dual chitinase/transglycosylase and specifically reports transfer of chitin to beta-glucan, supporting glycosyltransferase activity. This support is not exclusive: the same evidence also reports chitin-hydrolyzing activity.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "",
    "reason": "The sequence is consistent with a chitin-active enzyme, and transferable knowledge of such enzymes can support both glycosyl-bond hydrolysis and transglycosylation. That does not establish which coupled activity should count as its primary function among B and D; the supplied input offers no basis to prioritize one."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The protein is annotated as having both transglycosylase activity (B) and chitinase activity, which is a glycosyl-bond hydrolase activity (D). The options do not define how to choose a primary activity when both are reported."
  },
  "important_caveats": [
    "The evidence for B includes a computational GO annotation and functional annotation that combines evidence by similarity with a cited publication; the supplied excerpts do not establish that B is uniquely primary.",
    "The sequence match supports applying these annotations to the supplied sequence, but does not resolve the relative primacy of the two activities."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates GO:0016757 (glycosyltransferase activity) with evidence code IEA:TreeGrafter, and the protein description explicitly includes 'Chitin transglycosylase crh1' with EC 2.4.-.-. The FUNCTION comment describes it as a 'Dual chitinase/transglycosylase' that 'transfers chitin to 1,6-beta-glucan in the cell wall.' The PubMed reference (33846308) provides experimental evidence for transglycosylase activity. However, the protein also carries GO:0008843 (endochitinase activity, a child of GO:0016798 hydrolase acting on glycosyl bonds) and EC 3.2.1.14, so option D is also annotation-supported. The answer B is supported but not uniquely so given the dual-activity annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence reveals a GH18 catalytic domain (DXXDXDXE-like motif around residues 116-124: D-D-L-D-E-I-D-W-E with catalytic Glu-120, Asp-122, Glu-124), a chitin-binding domain (CBM5/12 region with conserved cysteines), and a C-terminal transmembrane hydrophobic segment (MIDLGVMVLGLGLGYLVM). This architecture—signal peptide + GH18 + CBM + TM anchor—is characteristic of fungal Crh-family chitin transglycosylases involved in cell wall remodeling, as opposed to secreted chitinases (Chi family) that lack TM domains and function in chitin degradation. Knowledge from other fungal GH18 proteins (e.g., Crh1/Crh2 in S. cerevisiae, Crh-like proteins in other Ascomycetes) establishes that membrane-anchored GH18 proteins with CBM are predominantly transglycosylases (EC 2.4.-.-) rather than hydrolases (EC 3.2.1.14). Options A (GTPase) and C (nutrient reservoir) are eliminated by the presence of the GH18 catalytic motif. Between B and D, the TM domain and cell-wall-remodeling architecture provide a family-level probabilistic inference favoring transglycosylase (B) over secreted chitinase (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The C-terminal transmembrane domain and overall domain architecture (signal + GH18 + CBM + TM) are visible in the input sequence and constitute a family-level pattern learned from other fungal GH18 proteins (Crh family vs. Chi family). This distinguishes B from D as a probabilistic inference. Options A and C are eliminated by the GH18 motif. The inference is not absolute (the protein has dual activity), but it meaningfully favors B among the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The protein is explicitly annotated as a 'dual chitinase/transglycosylase' with both EC 3.2.1.14 (hydrolase, corresponding to option D) and EC 2.4.-.- (transferase, corresponding to option B). Both GO:0008843 (endochitinase, child of GO:0016798) and GO:0016757 (glycosyltransferase) are annotated. The question asks for 'primary molecular function,' but for a genuinely dual-activity protein, either B or D could be defended as the 'primary' function. The TM-domain architecture argument favors B, but the hydrolase activity is equally well-annotated.


### Important caveats

- The GO:0016757 (glycosyltransferase) annotation carries evidence code IEA:TreeGrafter (computational prediction), while GO:0008843 (endochitinase) carries ISS (inferred by sequence similarity). Neither has direct experimental evidence code for this specific protein's catalytic mechanism, though the PubMed paper demonstrates transglycosylase activity experimentally.
- The protein is a genuine dual-function enzyme (chitinase + transglycosylase), making the 'primary' designation inherently ambiguous.
- The TM-domain-based inference favoring transglycosylase is a family-level pattern from other fungal GH18 proteins and is probabilistic, not deterministic.
- The sequence itself does not contain explicit sequence determinants that absolutely distinguish transglycosylase from chitinase activity within the GH18 family; the distinction often requires structural or experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence reveals a GH18 catalytic domain (DXXDXDXE-like motif around residues 116-124: D-D-L-D-E-I-D-W-E with catalytic Glu-120, Asp-122, Glu-124), a chitin-binding domain (CBM5/12 region with conserved cysteines), and a C-terminal transmembrane hydrophobic segment (MIDLGVMVLGLGLGYLVM). This architecture—signal peptide + GH18 + CBM + TM anchor—is characteristic of fungal Crh-family chitin transglycosylases involved in cell wall remodeling, as opposed to secreted chitinases (Chi family) that lack TM domains and function in chitin degradation. Knowledge from other fungal GH18 proteins (e.g., Crh1/Crh2 in S. cerevisiae, Crh-like proteins in other Ascomycetes) establishes that membrane-anchored GH18 proteins with CBM are predominantly transglycosylases (EC 2.4.-.-) rather than hydrolases (EC 3.2.1.14). Options A (GTPase) and C (nutrient reservoir) are eliminated by the presence of the GH18 catalytic motif. Between B and D, the TM domain and cell-wall-remodeling architecture provide a family-level probabilistic inference favoring transglycosylase (B) over secreted chitinase (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal transmembrane domain and overall domain architecture (signal + GH18 + CBM + TM) are visible in the input sequence and constitute a family-level pattern learned from other fungal GH18 proteins (Crh family vs. Chi family). This distinguishes B from D as a probabilistic inference. Options A and C are eliminated by the GH18 motif. The inference is not absolute (the protein has dual activity), but it meaningfully favors B among the offered choices."
  },
  "case_id": "GO_molecular_function_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates GO:0016757 (glycosyltransferase activity) with evidence code IEA:TreeGrafter, and the protein description explicitly includes 'Chitin transglycosylase crh1' with EC 2.4.-.-. The FUNCTION comment describes it as a 'Dual chitinase/transglycosylase' that 'transfers chitin to 1,6-beta-glucan in the cell wall.' The PubMed reference (33846308) provides experimental evidence for transglycosylase activity. However, the protein also carries GO:0008843 (endochitinase activity, a child of GO:0016798 hydrolase acting on glycosyl bonds) and EC 3.2.1.14, so option D is also annotation-supported. The answer B is supported but not uniquely so given the dual-activity annotation."
  },
  "important_caveats": [
    "The GO:0016757 (glycosyltransferase) annotation carries evidence code IEA:TreeGrafter (computational prediction), while GO:0008843 (endochitinase) carries ISS (inferred by sequence similarity). Neither has direct experimental evidence code for this specific protein's catalytic mechanism, though the PubMed paper demonstrates transglycosylase activity experimentally.",
    "The protein is a genuine dual-function enzyme (chitinase + transglycosylase), making the 'primary' designation inherently ambiguous.",
    "The TM-domain-based inference favoring transglycosylase is a family-level pattern from other fungal GH18 proteins and is probabilistic, not deterministic.",
    "The sequence itself does not contain explicit sequence determinants that absolutely distinguish transglycosylase from chitinase activity within the GH18 family; the distinction often requires structural or experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The protein is explicitly annotated as a 'dual chitinase/transglycosylase' with both EC 3.2.1.14 (hydrolase, corresponding to option D) and EC 2.4.-.- (transferase, corresponding to option B). Both GO:0008843 (endochitinase, child of GO:0016798) and GO:0016757 (glycosyltransferase) are annotated. The question asks for 'primary molecular function,' but for a genuinely dual-activity protein, either B or D could be defended as the 'primary' function. The TM-domain architecture argument favors B, but the hydrolase activity is equally well-annotated."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates GO:0016757 (glycosyltransferase activity) with evidence code IEA:TreeGrafter, and the protein description explicitly includes 'Chitin transglycosylase crh1' with EC 2.4.-.-. The FUNCTION comment describes it as a 'Dual chitinase/transglycosylase' that 'transfers chitin to 1,6-beta-glucan in the cell wall.' The PubMed reference (33846308) provides experimental evidence for transglycosylase activity. However, the protein also carries GO:0008843 (endochitinase activity, a child of GO:0016798 hydrolase acting on glycosyl bonds) and EC 3.2.1.14, so option D is also annotation-supported. The answer B is supported but not uniquely so given the dual-activity annotation.",
    "evidence_ids": ["C4", "C5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence reveals a GH18 catalytic domain (DXXDXDXE-like motif around residues 116-124: D-D-L-D-E-I-D-W-E with catalytic Glu-120, Asp-122, Glu-124), a chitin-binding domain (CBM5/12 region with conserved cysteines), and a C-terminal transmembrane hydrophobic segment (MIDLGVMVLGLGLGYLVM). This architecture—signal peptide + GH18 + CBM + TM anchor—is characteristic of fungal Crh-family chitin transglycosylases involved in cell wall remodeling, as opposed to secreted chitinases (Chi family) that lack TM domains and function in chitin degradation. Knowledge from other fungal GH18 proteins (e.g., Crh1/Crh2 in S. cerevisiae, Crh-like proteins in other Ascomycetes) establishes that membrane-anchored GH18 proteins with CBM are predominantly transglycosylases (EC 2.4.-.-) rather than hydrolases (EC 3.2.1.14). Options A (GTPase) and C (nutrient reservoir) are eliminated by the presence of the GH18 catalytic motif. Between B and D, the TM domain and cell-wall-remodeling architecture provide a family-level probabilistic inference favoring transglycosylase (B) over secreted chitinase (D).",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal transmembrane domain and overall domain architecture (signal + GH18 + CBM + TM) are visible in the input sequence and constitute a family-level pattern learned from other fungal GH18 proteins (Crh family vs. Chi family). This distinguishes B from D as a probabilistic inference. Options A and C are eliminated by the GH18 motif. The inference is not absolute (the protein has dual activity), but it meaningfully favors B among the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The protein is explicitly annotated as a 'dual chitinase/transglycosylase' with both EC 3.2.1.14 (hydrolase, corresponding to option D) and EC 2.4.-.- (transferase, corresponding to option B). Both GO:0008843 (endochitinase, child of GO:0016798) and GO:0016757 (glycosyltransferase) are annotated. The question asks for 'primary molecular function,' but for a genuinely dual-activity protein, either B or D could be defended as the 'primary' function. The TM-domain architecture argument favors B, but the hydrolase activity is equally well-annotated."
  },
  "important_caveats": [
    "The GO:0016757 (glycosyltransferase) annotation carries evidence code IEA:TreeGrafter (computational prediction), while GO:0008843 (endochitinase) carries ISS (inferred by sequence similarity). Neither has direct experimental evidence code for this specific protein's catalytic mechanism, though the PubMed paper demonstrates transglycosylase activity experimentally.",
    "The protein is a genuine dual-function enzyme (chitinase + transglycosylase), making the 'primary' designation inherently ambiguous.",
    "The TM-domain-based inference favoring transglycosylase is a family-level pattern from other fungal GH18 proteins and is probabilistic, not deterministic.",
    "The sequence itself does not contain explicit sequence determinants that absolutely distinguish transglycosylase from chitinase activity within the GH18 family; the distinction often requires structural or experimental data."
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
  "benchmark_sequence_length": 391,
  "benchmark_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 391,
  "current_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384J6C4",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "selected_historical_source_sequence_length": 391,
  "selected_historical_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "selected_historical_version": {
    "accession": "A0A384J6C4",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_BOTFB",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384J6C4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Dual chitinase/transglycosylase that plays a role in cell wall architecture (PubMed:33846308). Chitinase and transglycosylase activities are coupled (By similarity). Required for the polysaccharide cross-linking at the septa and the cell wall (By similarity). More specifically, transfers chitin to 1,6-beta-glucan in the cell wall (By similarity). Acts as an elicitor that triggers AMP-triggered immunity (PTI) and induces host resistance against Botryotinia fuckeliana (PubMed:33846308). Cell death-inducing activity is independent of its transglycosylase activity (PubMed:33846308). Plays a possible role in infection cushion formation (PubMed:33846308)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008843\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:endochitinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016757\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:glycosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"DOMAIN\",\"MUTAGENESIS OF CYS-33; GLU-120; ASP-122 AND GLU-124\",\"SUBUNIT\",\"INTERACTION WITH CRH2 AND CRH3\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   CRH1_BOTFB              Reviewed;         391 AA.\nAC   A0A384J6C4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_01g06010;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, DOMAIN, MUTAGENESIS\nRP   OF CYS-33; GLU-120; ASP-122 AND GLU-124, SUBUNIT, AND INTERACTION WITH CRH2\nRP   AND CRH3.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Dual chitinase/transglycosylase that plays a role in cell\nCC       wall architecture (PubMed:33846308). Chitinase and transglycosylase\nCC       activities are coupled (By similarity). Required for the polysaccharide\nCC       cross-linking at the septa and the cell wall (By similarity). More\nCC       specifically, transfers chitin to 1,6-beta-glucan in the cell wall (By\nCC       similarity). Acts as an elicitor that triggers AMP-triggered immunity\nCC       (PTI) and induces host resistance against Botryotinia fuckeliana\nCC       (PubMed:33846308). Cell death-inducing activity is independent of its\nCC       transglycosylase activity (PubMed:33846308). Plays a possible role in\nCC       infection cushion formation (PubMed:33846308).\nCC       {ECO:0000250|UniProtKB:Q8J0P4, ECO:0000269|PubMed:33846308}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0008843; F:endochitinase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003924\nname: GTPase activity\nnamespace: molecular_function\nalt_id: GO:0061745\ndef: \"Catalysis of the reaction: GTP + H2O = GDP + H+ + phosphate.\" [PMID:26832457, PMID:27218782]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nsynonym: \"ARF small monomeric GTPase activity\" NARROW []\nsynonym: \"dynamin GTPase activity\" NARROW []\nsynonym: \"GTPase activity, coupled\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase activity\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, alpha-subunit\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, beta-subunit\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, gamma-subunit\" RELATED []\nsynonym: \"hydrolase activity, acting on acid anhydrides, acting on GTP, involved in cellular and subcellular movement\" BROAD []\nsynonym: \"protein-synthesizing GTPase activity\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, elongation\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, initiation\" NARROW []\nsynonym: \"protein-synthesizing GTPase activity, termination\" NARROW []\nsynonym: \"Rab small monomeric GTPase activity\" NARROW []\nsynonym: \"Ran small monomeric GTPase activity\" NARROW []\nsynonym: \"Ras small monomeric GTPase activity\" NARROW []\nsynonym: \"RHEB small monomeric GTPase activity\" NARROW []\nsynonym: \"Rho small monomeric GTPase activity\" NARROW []\nsynonym: \"Sar small monomeric GTPase activity\" NARROW []\nsynonym: \"signal-recognition-particle GTPase activity\" NARROW []\nsynonym: \"small monomeric GTPase activity\" NARROW []\nsynonym: \"tubulin GTPase activity\" NARROW []\nxref: MetaCyc:RXN0-5462\nxref: Reactome:R-HSA-1445143 \"RAB8A,10,13,14 hydrolyze GTP\"\nxref: Reactome:R-HSA-1458485 \"RALA hydrolyzes GTP\"\nxref: Reactome:R-HSA-156923 \"Hydrolysis of eEF1A:GTP\"\nxref: Reactome:R-HSA-164381 \"G alpha (s) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-165055 \"Hydrolysis of Ran:GTP to Ran:GDP\"\nxref: Reactome:R-HSA-167415 \"G-protein alpha subunit is inactivated\"\nxref: Reactome:R-HSA-170666 \"Adenylate cyclase increases the GTPase activity of G alpha-olf\"\nxref: Reactome:R-HSA-170685 \"Adenylaye cyclase increases the GTPase activity of G alpha-olf\"\nxref: Reactome:R-HSA-170686 \"Adenylate cyclase increases the GTPase activity of Gi alpha\"\nxref: Reactome:R-HSA-177501 \"Endocytosis (internalization) of clathrin-coated vesicle\"\nxref: Reactome:R-HSA-203973 \"Vesicle budding\"\nxref: Reactome:R-HSA-2130641 \"Translocation of TGN-lysosome vesicle to lysosome\"\nxref: Reactome:R-HSA-2130725 \"Internalization of MHC II:Ii clathrin coated vesicle\"\nxref: Reactome:R-HSA-2584246 \"GNAT1-GTP hydrolyses its bound GTP to GDP\"\nxref: Reactome:R-HSA-380979 \"RHEB in mTORC1:RHEB:GTP hydrolyses GTP\"\nxref: Reactome:R-HSA-392133 \"G alpha (z) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-392212 \"G alpha (i) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-418574 \"G alpha (12/13) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-418582 \"G alpha (q) auto-inactivates by hydrolysing GTP to GDP\"\nxref: Reactome:R-HSA-421835 \"trans-Golgi Network Vesicle Scission\"\nxref: Reactome:R-HSA-428941 \"P2Y purinoceptor 1 activates MAP kinase p38 alpha\"\nxref: Reactome:R-HSA-432707 \"trans-Golgi Network Lysosomal Vesicle Scission\"\nxref: Reactome:R-HSA-5333615 \"80S:Met-tRNAi:mRNA:SECISBP2:Sec-tRNA(Sec):EEFSEC:GTP is hydrolysed to 80S:Met-tRNAi:mRNA:SECISBP2:Sec and EEFSEC:GDP by EEFSEC\"\nxref: Reactome:R-HSA-5389839 \"39S subunit binds 28S subunit:mRNA:fMet-tRNA\"\nxref: Reactome:R-HSA-5389842 \"TUFM hydrolyzes GTP and TUFM:GDP dissociates from 55S ribosome\"\nxref: Reactome:R-HSA-5419273 \"Hydrolysis of GTP and dissociation of 28S and 39S subunits\"\nxref: Reactome:R-HSA-5419279 \"Translocation of peptidyl-tRNA from A-site to P-site (and translocation of 55S ribosome by 3 bases along mRNA)\"\nxref: Reactome:R-HSA-555065 \"Formation of clathrin coated vesicle\"\nxref: Reactome:R-HSA-5623513 \"ASAP1 stimulates GTPase activity of ARF4\"\nxref: Reactome:R-HSA-5638006 \"ARL3 hydrolyzes GTP\"\nxref: Reactome:R-HSA-5658231 \"RAS GAPs stimulate RAS GTPase activity\"\nxref: Reactome:R-HSA-5665809 \"SRGAP2 stimulates RAC1 GTP-ase activity and ends FMNL1-mediated elongation of actin filaments\"\nxref: Reactome:R-HSA-5672017 \"Rheb in the MTORC1 complex hydrolyses GTP\"\nxref: Reactome:R-HSA-5694527 \"Loss of SAR1B GTPase\"\nxref: Reactome:R-HSA-6807877 \"ARFGAPs stimulate ARF GTPase activity\"\nxref: Reactome:R-HSA-6814833 \"TBC1D20 stimulates GTPase activity of RAB1, resulting in hydrolysis of GTP\"\nxref: Reactome:R-HSA-8847534 \"RAB43 hydrolyses GTP\"\nxref: Reactome:R-HSA-8847883 \"CYTH proteins stimulate ARF1 GTPase activity\"\nxref: Reactome:R-HSA-8849082 \"ARHGAP35 stimulates RHOA GTPase activity\"\nxref: Reactome:R-HSA-8854173 \"TBC RabGAPs accelerate GTP hydrolysis by RAB35\"\nxref: Reactome:R-HSA-8854255 \"TBC1D2A accelerates GTP hydrolysis by RAB7\"\nxref: Reactome:R-HSA-8854329 \"TBC1D15 accelerates GTP hydrolysis by RAB7\"\nxref: Reactome:R-HSA-8854604 \"TBC1D16 accelerates GTP hydrolysis by RAB4A\"\nxref: Reactome:R-HSA-8854612 \"TBC1D25 accelerates GTP hydrolysis by RAB33B\"\nxref: Reactome:R-HSA-8868661 \"Dynamin-mediated GTP hydrolysis promotes vesicle scission\"\nxref: Reactome:R-HSA-8981353 \"RASA1 stimulates RAS GTPase activity\"\nxref: Reactome:R-HSA-8982020 \"G alpha (i)i1/i2/i3 in G (i):RGS complex is inactivated\"\nxref: Reactome:R-HSA-8982021 \"G alpha (z) in G alpha (z):RGS complex is inactivated\"\nxref: Reactome:R-HSA-8982025 \"G alpha (q) in G (q):RGS complex is inactivated\"\nxref: Reactome:R-HSA-9018814 \"RHOT1 hydrolyzes GTP\"\nxref: Reactome:R-HSA-9018826 \"RHOT2 hydrolyzes GTP\"\nxref: Reactome:R-HSA-9640195 \"RRAGA,B hydrolyzes GTP\"\nxref: Reactome:R-HSA-9645598 \"RRAGC,D hydrolyzes GTP\"\nxref: Reactome:R-HSA-9649736 \"RAS intrinsic GTPase activity hydrolyzes GTP to GDP\"\nxref: Reactome:R-HSA-983422 \"Disassembly of COPII coated vesicle\"\nxref: Reactome:R-HSA-9947842 \"GBP1 hydrolyzes GTP forming GBP1 oligomers\"\nxref: Reactome:R-HSA-9954919 \"ABCE1:ATP binds PELO:HBS1L-1:GTP:80S ribosome:non-stop mRNA:peptidyl-tRNA with nascent peptide and HBS1L-1:GDP is released\"\nxref: RHEA:19669\nis_a: GO:0017111 ! ribonucleoside triphosphate phosphatase activity\nproperty_value: skos:exactMatch RHEA:19669\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003924",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 31441-31534",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0004553\nname: hydrolase activity, hydrolyzing O-glycosyl compounds\nnamespace: molecular_function\nalt_id: GO:0016800\ndef: \"Catalysis of the hydrolysis of any O-glycosyl bond.\" [GOC:mah]\nsynonym: \"O-glucosyl hydrolase activity\" EXACT []\nxref: EC:3.2.1.-\nxref: Reactome:R-HSA-5694563 \"ABHD10 hydrolyses MPAG\"\nxref: Reactome:R-HSA-6786652 \"CHIT1 hydrolyses CHIT to 3xADGP\"\nxref: Reactome:R-HSA-9661820 \"Bacterial GUSB hydrolyses BDG to BIL\"\nis_a: GO:0016798 ! hydrolase activity, acting on glycosyl bonds\nproperty_value: skos:exactMatch EC:3.2.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004553",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44250-44263",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0004568\nname: chitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins.\" [GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nxref: Reactome:R-HSA-6786421 \"CHIA hydrolyses chitin\"\nis_a: GO:0004553 ! hydrolase activity, hydrolyzing O-glycosyl compounds\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004568",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44534-44541",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0008843\nname: endochitinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of nonterminal (1->4)-beta linkages of N-acetyl-D-glucosamine (GlcNAc) polymers of chitin and chitodextrins. Typically, endochitinases cleave randomly within the chitin chain.\" [EC:3.2.1.14, GOC:bf, GOC:kah, GOC:pde, PMID:11468293]\nsynonym: \"1,4-beta-poly-N-acetylglucosaminidase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitinase\" EXACT [EC:3.2.1.14]\nsynonym: \"chitodextrinase\" EXACT [EC:3.2.1.14]\nsynonym: \"poly-beta-glucosaminidase\" EXACT [EC:3.2.1.14]\nxref: EC:3.2.1.14\nxref: MetaCyc:3.2.1.14-RXN\nis_a: GO:0004568 ! chitinase activity\nproperty_value: skos:exactMatch EC:3.2.1.14\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008843",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 88913-88926",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0016757\nname: glycosyltransferase activity\nnamespace: molecular_function\nalt_id: GO:0016932\ndef: \"Catalysis of the transfer of a glycosyl group from one compound (donor) to another (acceptor).\" [GOC:jl, ISBN:0198506732]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"transferase activity, transferring glycosyl groups\" EXACT []\nsynonym: \"transferase activity, transferring other glycosyl groups\" NARROW []\nsynonym: \"transglycosidase activity\" EXACT []\nsynonym: \"transglycosylase activity\" EXACT []\nxref: EC:2.4.-.-\nxref: Reactome:R-HSA-5173005 \"B3GALTL transfers glucose to O-fucosyl-proteins\"\nxref: Reactome:R-HSA-6785565 \"Defective B3GALTL does not transfer glucose to O-fucosyl-proteins\"\nis_a: GO:0016740 ! transferase activity\nproperty_value: skos:exactMatch EC:2.4.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016757",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129828-129846",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0016798\nname: hydrolase activity, acting on glycosyl bonds\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of any glycosyl bond.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"glycosidase activity\" EXACT []\nsynonym: \"glycosylase\" NARROW []\nsynonym: \"N-glycosylase\" NARROW []\nxref: EC:3.2.-.-\nxref: Reactome:R-HSA-1793176 \"DS is cleaved from its proteoglycan\"\nxref: Reactome:R-HSA-2065233 \"CS is cleaved from its proteoglycan\"\nxref: Reactome:R-HSA-5333609 \"MeSebGalNac is hydrolysed to MeSeH and bGalNac\"\nis_a: GO:0016787 ! hydrolase activity\nproperty_value: skos:exactMatch EC:3.2.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016798",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130290-130307",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0045735\nname: nutrient reservoir activity\nnamespace: molecular_function\ndef: \"Functions in the storage of nutritious substrates.\" [GOC:ai]\ncomment: Note that this term can be used in place of the obsolete terms 'storage protein ; GO:0005187' and 'storage protein of fat body (sensu Insecta) ; GO:0008041'.\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsynonym: \"storage protein\" RELATED []\nsynonym: \"storage protein of fat body\" RELATED []\nsynonym: \"yolk protein\" RELATED []\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045735",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 268007-268020",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
