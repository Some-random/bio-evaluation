# GO_molecular_function_0086

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0086.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — phosphoprotein phosphatase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. glucose-6-phosphate isomerase activity
B. chromatin DNA binding
C. phosphoprotein phosphatase activity
D. protein heterodimerization activity
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

### Expected-answer support: contradicted

> The matched-sequence record reports ADP-ribosylhydrolase activity, including hydrolysis of ADP-ribosyl-glutamate bonds, and probable ADP-ribosyltransferase activity. That is not phosphoprotein dephosphorylation, the activity specified by option C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

> A family-level inference of ADP-ribose processing would point toward hydrolase/transferase activity, not glucose-6-phosphate isomerization, chromatin DNA binding, phosphoprotein phosphatase activity, or heterodimerization. But that inference does not meaningfully select any offered option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence may support inference of an enzymatic ADP-ribose-related function from transferable family knowledge, but the inferred activity is absent from the choices. Choosing C merely because it is the offered catalytic option would conflate distinct reactions; the inputs provide no credible basis for selecting it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports an activity not represented among the choices, rather than identifying multiple defensible options.


### Important caveats

- Reviewer-only database and experimental evidence was not available as original model input.
- The sequence match is exact for the supplied sequence; the source record describes hydrolase activity experimentally and transferase activity as probable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A family-level inference of ADP-ribose processing would point toward hydrolase/transferase activity, not glucose-6-phosphate isomerization, chromatin DNA binding, phosphoprotein phosphatase activity, or heterodimerization. But that inference does not meaningfully select any offered option.",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "",
    "reason": "The sequence may support inference of an enzymatic ADP-ribose-related function from transferable family knowledge, but the inferred activity is absent from the choices. Choosing C merely because it is the offered catalytic option would conflate distinct reactions; the inputs provide no credible basis for selecting it."
  },
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "contradicted",
    "reason": "The matched-sequence record reports ADP-ribosylhydrolase activity, including hydrolysis of ADP-ribosyl-glutamate bonds, and probable ADP-ribosyltransferase activity. That is not phosphoprotein dephosphorylation, the activity specified by option C."
  },
  "important_caveats": [
    "Reviewer-only database and experimental evidence was not available as original model input.",
    "The sequence match is exact for the supplied sequence; the source record describes hydrolase activity experimentally and transferase activity as probable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports an activity not represented among the choices, rather than identifying multiple defensible options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched-sequence record reports ADP-ribosylhydrolase activity, including hydrolysis of ADP-ribosyl-glutamate bonds, and probable ADP-ribosyltransferase activity. That is not phosphoprotein dephosphorylation, the activity specified by option C.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "A family-level inference of ADP-ribose processing would point toward hydrolase/transferase activity, not glucose-6-phosphate isomerization, chromatin DNA binding, phosphoprotein phosphatase activity, or heterodimerization. But that inference does not meaningfully select any offered option.",
    "missing_item_specific_fact": "",
    "reason": "The sequence may support inference of an enzymatic ADP-ribose-related function from transferable family knowledge, but the inferred activity is absent from the choices. Choosing C merely because it is the offered catalytic option would conflate distinct reactions; the inputs provide no credible basis for selecting it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports an activity not represented among the choices, rather than identifying multiple defensible options."
  },
  "important_caveats": [
    "Reviewer-only database and experimental evidence was not available as original model input.",
    "The sequence match is exact for the supplied sequence; the source record describes hydrolase activity experimentally and transferase activity as probable."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein (A0A559KX76, Foc1Mfs1/Macrodomain-fused SirTM 1) is experimentally characterized as an ADP-ribosylhydrolase (EC 3.2.1.-) and probable ADP-ribosyltransferase (EC 2.4.2.-). Its catalytic activity is hydrolysis of ADP-ribosyl-glutamate bonds on proteins (5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H+), confirmed by X-ray crystallography and in vitro assays (PubMed:39270823). This is mechanistically and mechanistically distinct from phosphoprotein phosphatase activity (GO:0004721), which specifically catalyzes removal of phosphate groups from phosphoproteins. The UniProt GO annotations list glycosyltransferase activity, hydrolase activity acting on glycosyl bonds, metal ion binding, and nucleotidyltransferase activity — none is phosphoprotein phosphatase. The expected answer C is contradicted by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> No annotation, measurement, or fact exists that would make 'phosphoprotein phosphatase activity' correct for this protein. The experimentally validated function is ADP-ribosylhydrolase (removing ADP-ribose from glutamate residues on proteins), which is a glycosyl hydrolase activity (GO:0016798), not phosphatase activity (GO:0016791/GO:0004721). No transferable knowledge about macrodomains, SirTM proteins, or ADP-ribosylation biology supports classifying this enzyme as a phosphoprotein phosphatase. The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four offered choices.


**Reason**

> A knowledgeable model recognizing the macrodomain and SirTM domain architecture would identify this as an ADP-ribose hydrolase/transferase, not a phosphoprotein phosphatase. No sequence motif (DXD for PPP-family, PP2C, Cdc25, or other phosphatase signatures) is present. No family-level inference about macrodomains or SirTM proteins leads to phosphatase activity. The correct answer is absent from the options, and the expected answer C is factually incorrect for this protein. No reasoning path from sequence features or family knowledge distinguishes C over the other options in a biologically valid way.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four options. The expected answer C is contradicted by experimental evidence. None of the four options correctly describes this protein's function, so no option is truly 'defensible' as correct. The question appears to have an incorrect answer key.


### Important caveats

- The expected answer (C, phosphoprotein phosphatase activity) is contradicted by experimental evidence showing ADP-ribosylhydrolase activity. The protein removes ADP-ribose groups from protein glutamate residues, not phosphate groups.
- The correct molecular function (ADP-ribosylhydrolase, GO:0016798 or related glycosyl hydrolase terms) is not offered as an option, suggesting a benchmark annotation error.
- The protein was characterized in 2024 (PubMed:39270823) with X-ray crystallography at 2.22 Å showing Zn²⁺ coordination and mutagenesis of Cys-61 and His-144, providing strong experimental evidence against phosphatase activity.
- The macrodomain and SirTM domain architecture is well-characterized in other proteins (e.g., PARP1, macroH2A, viral macrodomains, SirT2) as ADP-ribose readers/hydrolases/transferases, not phosphatases.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "No annotation, measurement, or fact exists that would make 'phosphoprotein phosphatase activity' correct for this protein. The experimentally validated function is ADP-ribosylhydrolase (removing ADP-ribose from glutamate residues on proteins), which is a glycosyl hydrolase activity (GO:0016798), not phosphatase activity (GO:0016791/GO:0004721). No transferable knowledge about macrodomains, SirTM proteins, or ADP-ribosylation biology supports classifying this enzyme as a phosphoprotein phosphatase. The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four offered choices.",
    "reason": "A knowledgeable model recognizing the macrodomain and SirTM domain architecture would identify this as an ADP-ribose hydrolase/transferase, not a phosphoprotein phosphatase. No sequence motif (DXD for PPP-family, PP2C, Cdc25, or other phosphatase signatures) is present. No family-level inference about macrodomains or SirTM proteins leads to phosphatase activity. The correct answer is absent from the options, and the expected answer C is factually incorrect for this protein. No reasoning path from sequence features or family knowledge distinguishes C over the other options in a biologically valid way."
  },
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "contradicted",
    "reason": "The protein (A0A559KX76, Foc1Mfs1/Macrodomain-fused SirTM 1) is experimentally characterized as an ADP-ribosylhydrolase (EC 3.2.1.-) and probable ADP-ribosyltransferase (EC 2.4.2.-). Its catalytic activity is hydrolysis of ADP-ribosyl-glutamate bonds on proteins (5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H+), confirmed by X-ray crystallography and in vitro assays (PubMed:39270823). This is mechanistically and mechanistically distinct from phosphoprotein phosphatase activity (GO:0004721), which specifically catalyzes removal of phosphate groups from phosphoproteins. The UniProt GO annotations list glycosyltransferase activity, hydrolase activity acting on glycosyl bonds, metal ion binding, and nucleotidyltransferase activity — none is phosphoprotein phosphatase. The expected answer C is contradicted by experimental evidence."
  },
  "important_caveats": [
    "The expected answer (C, phosphoprotein phosphatase activity) is contradicted by experimental evidence showing ADP-ribosylhydrolase activity. The protein removes ADP-ribose groups from protein glutamate residues, not phosphate groups.",
    "The correct molecular function (ADP-ribosylhydrolase, GO:0016798 or related glycosyl hydrolase terms) is not offered as an option, suggesting a benchmark annotation error.",
    "The protein was characterized in 2024 (PubMed:39270823) with X-ray crystallography at 2.22 Å showing Zn²⁺ coordination and mutagenesis of Cys-61 and His-144, providing strong experimental evidence against phosphatase activity.",
    "The macrodomain and SirTM domain architecture is well-characterized in other proteins (e.g., PARP1, macroH2A, viral macrodomains, SirT2) as ADP-ribose readers/hydrolases/transferases, not phosphatases."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four options. The expected answer C is contradicted by experimental evidence. None of the four options correctly describes this protein's function, so no option is truly 'defensible' as correct. The question appears to have an incorrect answer key."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0086",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein (A0A559KX76, Foc1Mfs1/Macrodomain-fused SirTM 1) is experimentally characterized as an ADP-ribosylhydrolase (EC 3.2.1.-) and probable ADP-ribosyltransferase (EC 2.4.2.-). Its catalytic activity is hydrolysis of ADP-ribosyl-glutamate bonds on proteins (5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H+), confirmed by X-ray crystallography and in vitro assays (PubMed:39270823). This is mechanistically and mechanistically distinct from phosphoprotein phosphatase activity (GO:0004721), which specifically catalyzes removal of phosphate groups from phosphoproteins. The UniProt GO annotations list glycosyltransferase activity, hydrolase activity acting on glycosyl bonds, metal ion binding, and nucleotidyltransferase activity — none is phosphoprotein phosphatase. The expected answer C is contradicted by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "No annotation, measurement, or fact exists that would make 'phosphoprotein phosphatase activity' correct for this protein. The experimentally validated function is ADP-ribosylhydrolase (removing ADP-ribose from glutamate residues on proteins), which is a glycosyl hydrolase activity (GO:0016798), not phosphatase activity (GO:0016791/GO:0004721). No transferable knowledge about macrodomains, SirTM proteins, or ADP-ribosylation biology supports classifying this enzyme as a phosphoprotein phosphatase. The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four offered choices.",
    "reason": "A knowledgeable model recognizing the macrodomain and SirTM domain architecture would identify this as an ADP-ribose hydrolase/transferase, not a phosphoprotein phosphatase. No sequence motif (DXD for PPP-family, PP2C, Cdc25, or other phosphatase signatures) is present. No family-level inference about macrodomains or SirTM proteins leads to phosphatase activity. The correct answer is absent from the options, and the expected answer C is factually incorrect for this protein. No reasoning path from sequence features or family knowledge distinguishes C over the other options in a biologically valid way."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The correct molecular function (ADP-ribosylhydrolase/ADP-ribosyltransferase) is not among the four options. The expected answer C is contradicted by experimental evidence. None of the four options correctly describes this protein's function, so no option is truly 'defensible' as correct. The question appears to have an incorrect answer key."
  },
  "important_caveats": [
    "The expected answer (C, phosphoprotein phosphatase activity) is contradicted by experimental evidence showing ADP-ribosylhydrolase activity. The protein removes ADP-ribose groups from protein glutamate residues, not phosphate groups.",
    "The correct molecular function (ADP-ribosylhydrolase, GO:0016798 or related glycosyl hydrolase terms) is not offered as an option, suggesting a benchmark annotation error.",
    "The protein was characterized in 2024 (PubMed:39270823) with X-ray crystallography at 2.22 Å showing Zn²⁺ coordination and mutagenesis of Cys-61 and His-144, providing strong experimental evidence against phosphatase activity.",
    "The macrodomain and SirTM domain architecture is well-characterized in other proteins (e.g., PARP1, macroH2A, viral macrodomains, SirT2) as ADP-ribose readers/hydrolases/transferases, not phosphatases."
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
  "benchmark_sequence_length": 597,
  "benchmark_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 597,
  "current_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 22,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A559KX76",
  "selected_historical_entry_version": 22,
  "selected_historical_record_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "selected_historical_source_sequence_length": 597,
  "selected_historical_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "selected_historical_version": {
    "accession": "A0A559KX76",
    "database": "Swiss-Prot",
    "entryVersion": 22,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADRHT_FUSOC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A559KX76\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Nectriaceae\",\"Fusarium\",\"Fusarium oxysporum species complex\"],\"scientificName\":\"Fusarium oxysporum f. sp. cubense\",\"taxonId\":61366}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"Foc1Mfs1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WZU87063.1\",\"source\":\"EMBL\"}],\"value\":\"Macrodomain-fused SirTM 1\"}}],\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein-ADP-ribose hydrolase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0DN71\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable protein ADP-ribosyltransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Is probably a bifunctional enzyme with ADP-ribosyltransferase and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds (PubMed:39270823). It can remove the ADP-ribosyl modification from the human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily modified on glutamate site with only minor aspartate contribution (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond in ribosylated S.pyogenes GcvH-L (PubMed:39270823)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"name\":\"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58248\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10208\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29973\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142540\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Ariza A.\",\"Liu Q.\",\"Cowieson N.P.\",\"Ahel I.\",\"Filippov D.V.\",\"Rack J.G.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39270823\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107770\"}],\"citationType\":\"journal article\",\"firstPage\":\"107770\",\"id\":\"39270823\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107770\",\"publicationDate\":\"2024\",\"title\":\"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSN\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"race 1 / IMI 141109\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS) IN COMPLEX WITH ZN(2+)\",\"FUNCTION AS AN HYDROLASE\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF CYS-61 AND HIS-144\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H1",
  "excerpt": "ID   ADRHT_FUSOC             Reviewed;         597 AA.\nAC   A0A559KX76;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2019, sequence version 1.\nDT   28-JAN-2026, entry version 22.\nDE   RecName: Full=Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase {ECO:0000305};\nDE   AltName: Full=Foc1Mfs1 {ECO:0000303|PubMed:39270823};\nDE   AltName: Full=Macrodomain-fused SirTM 1 {ECO:0000312|EMBL:WZU87063.1};\nDE   Includes:\nDE     RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE              EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   Includes:\nDE     RecName: Full=Probable protein ADP-ribosyltransferase {ECO:0000305};\nDE              EC=2.4.2.- {ECO:0000250|UniProtKB:P0DN71};\nGN   Name=mfs1 {ECO:0000312|EMBL:WZU87063.1};\nGN   ORFNames=Focb16_v015632 {ECO:0000312|EMBL:TVY64815.1};\nOS   Fusarium oxysporum f. sp. cubense.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Nectriaceae; Fusarium;\nOC   Fusarium oxysporum species complex.\nOX   NCBI_TaxID=61366;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8RSN}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)\nRP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,\nRP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.\nRC   STRAIN=race 1 / IMI 141109;\nRX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;\nRA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;\nRT   \"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-\nRT   dependent macrodomains.\";\nRL   J. Biol. Chem. 300:107770-107770(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Is probably a bifunctional enzyme with ADP-ribosyltransferase\nCC       and ADP-ribosylhydrolase activities (Probable). In vitro, can act as an\nCC       ADP-ribosylhydrolase that hydrolyzes ADP-ribosyl-glutamate bonds\nCC       (PubMed:39270823). It can remove the ADP-ribosyl modification from the\nCC       human mono-ADP-ribosylated PARP1 E988Q mutant, which is primarily\nCC       modified on glutamate site with only minor aspartate contribution\nCC       (PubMed:39270823). It cannot hydrolyze the ADP-ribosyl-arpartate bond\nCC       in ribosylated S.pyogenes GcvH-L (PubMed:39270823).\nCC       {ECO:0000269|PubMed:39270823, ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-\nCC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-\nCC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,\nCC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0016757; F:glycosyltransferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016798; F:hydrolase activity, acting on glycosyl bonds; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0016779; F:nucleotidyltransferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004347\nname: glucose-6-phosphate isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate.\" [RHEA:11816]\nsynonym: \"D-glucose-6-phosphate aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"D-glucose-6-phosphate ketol-isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"glucose phosphate isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"hexose monophosphate isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"hexose phosphate isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"hexosephosphate isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"oxoisomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphoglucoisomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphoglucose isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphohexoisomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphohexomutase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphohexose isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphosaccharomutase activity\" BROAD [EC:5.3.1.9]\nxref: EC:5.3.1.9\nxref: MetaCyc:PGLUCISOM-RXN\nxref: Reactome:R-HSA-70471 \"GPI dimer isomerizes G6P\"\nxref: Reactome:R-HSA-70475 \"GPI dimer isomerizes Fru(6)P to G6P\"\nxref: RHEA:11816\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.9\nproperty_value: skos:exactMatch MetaCyc:PGLUCISOM-RXN\nproperty_value: skos:exactMatch RHEA:11816\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004347",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 40334-40361",
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
  "excerpt": "[Term]\nid: GO:0004721\nname: phosphoprotein phosphatase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a phosphoprotein + H2O = a protein + phosphate. Together with protein kinases, these enzymes control the state of phosphorylation of cellular proteins and thereby provide an important mechanism for regulating cellular activity.\" [ISBN:0198547684]\nsynonym: \"phosphoprotein phosphohydrolase activity\" EXACT []\nsynonym: \"protein phosphatase activity\" EXACT []\nsynonym: \"protein phosphatase-1 activity\" NARROW []\nsynonym: \"protein phosphatase-2A activity\" NARROW []\nsynonym: \"protein phosphatase-2B activity\" NARROW []\nsynonym: \"protein phosphatase-2C activity\" NARROW []\nxref: EC:3.1.3.55\nxref: Reactome:R-HSA-112383 \"Hypophosphorylation of RNA Pol II CTD by FCP1P protein\"\nxref: Reactome:R-HSA-113503 \"PP2A mediated localization of RB1 protein in chromatin\"\nxref: Reactome:R-HSA-1363274 \"Dephosphorylation of p107 (RBL1) by PP2A\"\nxref: Reactome:R-HSA-1363276 \"Dephosphorylation of p130 (RBL2) by PP2A\"\nxref: Reactome:R-HSA-167072 \"Hypophosphorylation of RNA Pol II CTD by FCP1P protein\"\nxref: Reactome:R-HSA-170153 \"Dephosphorylation of nuclear Cyclin B1:phospho-Cdc2 (Thr 14, Tyr15) complexes by Cdc25 phosphatases\"\nxref: Reactome:R-HSA-170158 \"CDC25A dephosphorylates CCNA:CDK1\"\nxref: Reactome:R-HSA-170161 \"Dephosphorylation of cytoplasmic Cyclin B1/B2:phospho-Cdc2 (Thr 14, Tyr 15) complexes by CDC25B\"\nxref: Reactome:R-HSA-174110 \"Cdc25A mediated dephosphorylation of Cyclin A:phospho-Cdk2\"\nxref: Reactome:R-HSA-174124 \"Dephosphorylation of phospho-Cdh1\"\nxref: Reactome:R-HSA-178178 \"PP1 dephosphorylates TGFBR1\"\nxref: Reactome:R-HSA-2529015 \"Dephosphorylation of CK2-modified condensin I\"\nxref: Reactome:R-HSA-69199 \"Dephosphorylation of Cyclin E:Cdk2 complexes by Cdc25A\"\nxref: Reactome:R-HSA-9636684 \"NdkA dephosphorylates RAB5A:GTP,RAB7A:GTP\"\nis_a: GO:0016791 ! phosphatase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:narrowMatch EC:3.1.3.55\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004721",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 48508-48537",
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
  "excerpt": "[Term]\nid: GO:0031490\nname: chromatin DNA binding\nnamespace: molecular_function\ndef: \"Binding to DNA that is assembled into chromatin.\" [GOC:mah]\nis_a: GO:0003677 ! DNA binding\nis_a: GO:0003682 ! chromatin binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031490",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177022-177029",
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
  "excerpt": "[Term]\nid: GO:0046982\nname: protein heterodimerization activity\nnamespace: molecular_function\ndef: \"Binding to a nonidentical protein to form a heterodimer.\" [GOC:ai]\nsubset: goslim_chembl\nis_a: GO:0046983 ! protein dimerization activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046982",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282546-282553",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
