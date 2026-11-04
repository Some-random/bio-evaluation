# pathway_0043

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0043.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Pigment biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDNISNHAFNYPVLVLNKGLLPEHDDIALARYLFSALALAVSRITQNEEMIVGFHLHPQEITRWKDDECIRQYILPLNIRFNSATPIAGFIREIMTWMTPDAIHQKNAMGASVLTLGPQHALHDIFDLEISWQPPVESEPVQALTCHVASREDALVLTLRFNPARFSATQMQKLPEVWRQITASAAKNGAETLRDIGLIDDAERQRVLHAFNQTEQAWDGETTVAARLKNRAQRHPEQTAVVFRDETLSYRQLYQQAGALAHYLNALETERERCVGLFVEPSLTLMTGVWGILLSGNAYLPLSPEYPEDRLAYMLENSQTRIIVTQPHLRERLLALAPPGIQVVTSDDVDAFMRQHAHSLPDAPQNDIAPHHLAYVIYTSGSTGKPKGVMIEHHSVLNQMNWLAQTVGLNQETVILQKTPMSFDAAQWEILSPACGCRVVMGEPGVYRNPEQLVDMLAEYRVTTLQCVPTLLQALLDTERLTHCPALRQIFSGGEALQKHLAQACLETLPDCELINLYGPTECTINNSAFRVDPVSVRQGPDTLSIGAPVANTRYYILDNCLTPVAVGQIGELYIGGDGVARGYLNRDDLTAERFIVDPFAPAGSGRRLYQTGDIASWNPDGTVQYAGRADNQVKLRGYRVELDEIRSAIETHEWVKAAAVIVRNDPFTGYQNLISFIELNAREAALMDQGNHGSHHQSKADKAQVMLQLANKGCREFPAASQPYTLDLPGKQPDEKQRLTAFSRKTYRFYDGGAVSREDILSLLHEPLLTAISRQPDALTLDELGHWLRYLGQFTSAERLLPKYTYASPGALYATQVFLELNGVAGLTAGHYYYQPVHHQLVRVSEQAAVTPGSLRLHFVGKKSAIEPIYKNNIREVLQMEMGHIIGMLDIILPDYGLGVALCDAAALDPTPLAIDLDDDYLGACDVLSGPRLPTDDDLDIYVQTAGANIADLPVGTYRYVRGDLQHIADDVIDKKHVIAINQAVYERSSFGISVASRTEGWAGYVHVGRKLQRLQMNPLNIGLMSSGYSSETGNDLPAARRFWQILGHRTGPYYFFIGGRISDEQKYSEGMREDAVHMKGPAEMIRDDLAAFMPDYMMPNKVLILDEMPLTANGKIDMKALANINVELKHKTIVAPRNPLEHQVMAIWQAKLKREEMSVDDNFFESGGNSLIAVSLINELNATLNASLPLQVLFQAPTVEKLAAWLSRARREPVSRLVQLQPKGRQAPIYCWPGLGGYCMNLRLLARQLGAERPFFGIQAHGINPDETPYATIGEMAARDIELIRQHQPHGPYTLWGYSFGARVAFETAWQLELAGEVVENLYLLAPGSPKLRDERVAAMNRKADFDNPGYLTILFSVFIGSITDPELERCLETVRDEESFVAFITGLNPALDDGLVRRITRIVAQTFEFTYTFSELQQRQLNAPVTIIKAQGDDYSFIENHGGFSAQPPTVLELMADHYSMLKAPGIDELTSVIQYQQSPPSLVG

[Multiple Choices]
A. Pigment biosynthesis. .
B. Alkaloid biosynthesis. .
C. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
D. L-threonine from L-aspartate: step 2/5. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and linked to experimental evidence. Indigoidine is a pigment, so this supports choice A. The cited primary paper is identified in the record but was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1488-residue sequence has the scale and motif-rich architecture of a large ATP-dependent nonribosomal-peptide-like synthetase, rather than the kind of enzyme expected for the single-step NAD+ or threonine choices. Transferable knowledge that specialized synthetases of this kind produce complex natural products, including pigment products such as indigoidine, makes pigment biosynthesis a credible choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and broad enzyme-family pattern provide a meaningful probabilistic basis for A over the small-molecule pathway-step options. They do not by themselves establish the exact product, and the distinction from the broad alkaloid category is less direct; nevertheless, family-level knowledge of pigment-producing synthetases makes A a defensible inference rather than requiring the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is as well supported by the sequence-level family inference and the supplied validation evidence.


### Important caveats

- The pathway annotation is linked to experimental evidence, but the underlying paper was not independently assessed.
- The reviewer-only accession and target-specific annotation are not treated as information available in the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1488-residue sequence has the scale and motif-rich architecture of a large ATP-dependent nonribosomal-peptide-like synthetase, rather than the kind of enzyme expected for the single-step NAD+ or threonine choices. Transferable knowledge that specialized synthetases of this kind produce complex natural products, including pigment products such as indigoidine, makes pigment biosynthesis a credible choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and broad enzyme-family pattern provide a meaningful probabilistic basis for A over the small-molecule pathway-step options. They do not by themselves establish the exact product, and the distinction from the broad alkaloid category is less direct; nevertheless, family-level knowledge of pigment-producing synthetases makes A a defensible inference rather than requiring the exact protein's database record."
  },
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and linked to experimental evidence. Indigoidine is a pigment, so this supports choice A. The cited primary paper is identified in the record but was not independently reviewed here."
  },
  "important_caveats": [
    "The pathway annotation is linked to experimental evidence, but the underlying paper was not independently assessed.",
    "The reviewer-only accession and target-specific annotation are not treated as information available in the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is as well supported by the sequence-level family inference and the supplied validation evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as indigoidine synthase, with the pathway listed as pigment biosynthesis and linked to experimental evidence. Indigoidine is a pigment, so this supports choice A. The cited primary paper is identified in the record but was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1488-residue sequence has the scale and motif-rich architecture of a large ATP-dependent nonribosomal-peptide-like synthetase, rather than the kind of enzyme expected for the single-step NAD+ or threonine choices. Transferable knowledge that specialized synthetases of this kind produce complex natural products, including pigment products such as indigoidine, makes pigment biosynthesis a credible choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and broad enzyme-family pattern provide a meaningful probabilistic basis for A over the small-molecule pathway-step options. They do not by themselves establish the exact product, and the distinction from the broad alkaloid category is less direct; nevertheless, family-level knowledge of pigment-producing synthetases makes A a defensible inference rather than requiring the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is as well supported by the sequence-level family inference and the supplied validation evidence."
  },
  "important_caveats": [
    "The pathway annotation is linked to experimental evidence, but the underlying paper was not independently assessed.",
    "The reviewer-only accession and target-specific annotation are not treated as information available in the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly lists the pathway as 'Pigment biosynthesis' with evidence code ECO:0000269 and PubMed:11790734, which experimentally characterizes indigoidine as a blue pigment and its biosynthetic genes in Erwinia chrysanthemi/Dickeya dadantii. The sequence matches the benchmark sequence (1488 AA, sha256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical nonribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain core 'TSGSTGKPKG', condensation (C) domain motif 'GAPVAN', and a phosphopantetheinyl carrier (PCP) region with the conserved serine attachment site. This identifies the protein as an NRPS. Among the four choices: (C) NAD+ from nicotinamide D-ribonucleotide is a simple adenylyltransferase reaction—completely inconsistent with an NRPS; (D) L-threonine from L-aspartate step 2/5 is a dehydrogenase (homoserine dehydrogenase)—also inconsistent with an NRPS. This leaves (A) Pigment biosynthesis and (B) Alkaloid biosynthesis. Transferable knowledge from many bacterial NRPS systems (indigoidine, actinorhodin, violacein, pyoluteorin-related pigments, etc.) establishes NRPS as a hallmark enzymatic platform for bacterial pigment biosynthesis. In contrast, alkaloid biosynthesis pathways predominantly employ decarboxylases, transaminases, P450 monooxygenases, methyltransferases, and terpene cyclases—not NRPS modules. While rare NRPS-derived alkaloids exist (e.g., some fungal ergot alkaloids), the dominant and well-known bacterial NRPS product classes are pigments, antibiotics, siderophores, and toxins. Thus, recognizing NRPS architecture plus the well-established NRPS-pigment association in bacteria meaningfully distinguishes A from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the NRPS domain architecture from conserved sequence motifs (TSGSTGKPKG, GAPVAN, PCP serine site), then apply the well-established family-level pattern that bacterial NRPS enzymes produce pigments (and antibiotics/siderophores) rather than alkaloids, and are not transferases or dehydrogenases. This eliminates C and D by enzyme-class mismatch and eliminates B by the NRPS-product-class association learned from many other NRPS systems. No fact specific to this exact protein's annotation is strictly required to make the distinction among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the protein is identified as an NRPS, choices C (transferase) and D (dehydrogenase) are clearly incompatible. Between A and B, the strong and well-documented association of bacterial NRPS with pigment biosynthesis versus the general absence of NRPS in alkaloid biosynthesis pathways makes A the clearly superior choice. No reasonable ambiguity remains among the four options.


### Important caveats

- The A-domain specificity-conferring residues (Stachelhaus code) could in principle confirm glutamine activation (consistent with indigoidine), but this level of detail is not necessary to distinguish the offered choices.
- The UniProt annotation uses ECO:0000269 (manual assertion) linked to PubMed:11790734, which provides experimental characterization of indigoidine as a blue pigment and its biosynthetic genes.
- A small number of NRPS enzymes have been annotated under 'Alkaloid biosynthesis' in databases (e.g., some fungal pathways), but these are exceptions and do not undermine the general NRPS-pigment association in bacteria.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical nonribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain core 'TSGSTGKPKG', condensation (C) domain motif 'GAPVAN', and a phosphopantetheinyl carrier (PCP) region with the conserved serine attachment site. This identifies the protein as an NRPS. Among the four choices: (C) NAD+ from nicotinamide D-ribonucleotide is a simple adenylyltransferase reaction—completely inconsistent with an NRPS; (D) L-threonine from L-aspartate step 2/5 is a dehydrogenase (homoserine dehydrogenase)—also inconsistent with an NRPS. This leaves (A) Pigment biosynthesis and (B) Alkaloid biosynthesis. Transferable knowledge from many bacterial NRPS systems (indigoidine, actinorhodin, violacein, pyoluteorin-related pigments, etc.) establishes NRPS as a hallmark enzymatic platform for bacterial pigment biosynthesis. In contrast, alkaloid biosynthesis pathways predominantly employ decarboxylases, transaminases, P450 monooxygenases, methyltransferases, and terpene cyclases—not NRPS modules. While rare NRPS-derived alkaloids exist (e.g., some fungal ergot alkaloids), the dominant and well-known bacterial NRPS product classes are pigments, antibiotics, siderophores, and toxins. Thus, recognizing NRPS architecture plus the well-established NRPS-pigment association in bacteria meaningfully distinguishes A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the NRPS domain architecture from conserved sequence motifs (TSGSTGKPKG, GAPVAN, PCP serine site), then apply the well-established family-level pattern that bacterial NRPS enzymes produce pigments (and antibiotics/siderophores) rather than alkaloids, and are not transferases or dehydrogenases. This eliminates C and D by enzyme-class mismatch and eliminates B by the NRPS-product-class association learned from many other NRPS systems. No fact specific to this exact protein's annotation is strictly required to make the distinction among the four offered choices."
  },
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly lists the pathway as 'Pigment biosynthesis' with evidence code ECO:0000269 and PubMed:11790734, which experimentally characterizes indigoidine as a blue pigment and its biosynthetic genes in Erwinia chrysanthemi/Dickeya dadantii. The sequence matches the benchmark sequence (1488 AA, sha256 match confirmed)."
  },
  "important_caveats": [
    "The A-domain specificity-conferring residues (Stachelhaus code) could in principle confirm glutamine activation (consistent with indigoidine), but this level of detail is not necessary to distinguish the offered choices.",
    "The UniProt annotation uses ECO:0000269 (manual assertion) linked to PubMed:11790734, which provides experimental characterization of indigoidine as a blue pigment and its biosynthetic genes.",
    "A small number of NRPS enzymes have been annotated under 'Alkaloid biosynthesis' in databases (e.g., some fungal pathways), but these are exceptions and do not undermine the general NRPS-pigment association in bacteria."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as an NRPS, choices C (transferase) and D (dehydrogenase) are clearly incompatible. Between A and B, the strong and well-documented association of bacterial NRPS with pigment biosynthesis versus the general absence of NRPS in alkaloid biosynthesis pathways makes A the clearly superior choice. No reasonable ambiguity remains among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly lists the pathway as 'Pigment biosynthesis' with evidence code ECO:0000269 and PubMed:11790734, which experimentally characterizes indigoidine as a blue pigment and its biosynthetic genes in Erwinia chrysanthemi/Dickeya dadantii. The sequence matches the benchmark sequence (1488 AA, sha256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical nonribosomal peptide synthetase (NRPS) domain motifs: the adenylation (A) domain core 'TSGSTGKPKG', condensation (C) domain motif 'GAPVAN', and a phosphopantetheinyl carrier (PCP) region with the conserved serine attachment site. This identifies the protein as an NRPS. Among the four choices: (C) NAD+ from nicotinamide D-ribonucleotide is a simple adenylyltransferase reaction—completely inconsistent with an NRPS; (D) L-threonine from L-aspartate step 2/5 is a dehydrogenase (homoserine dehydrogenase)—also inconsistent with an NRPS. This leaves (A) Pigment biosynthesis and (B) Alkaloid biosynthesis. Transferable knowledge from many bacterial NRPS systems (indigoidine, actinorhodin, violacein, pyoluteorin-related pigments, etc.) establishes NRPS as a hallmark enzymatic platform for bacterial pigment biosynthesis. In contrast, alkaloid biosynthesis pathways predominantly employ decarboxylases, transaminases, P450 monooxygenases, methyltransferases, and terpene cyclases—not NRPS modules. While rare NRPS-derived alkaloids exist (e.g., some fungal ergot alkaloids), the dominant and well-known bacterial NRPS product classes are pigments, antibiotics, siderophores, and toxins. Thus, recognizing NRPS architecture plus the well-established NRPS-pigment association in bacteria meaningfully distinguishes A from B.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the NRPS domain architecture from conserved sequence motifs (TSGSTGKPKG, GAPVAN, PCP serine site), then apply the well-established family-level pattern that bacterial NRPS enzymes produce pigments (and antibiotics/siderophores) rather than alkaloids, and are not transferases or dehydrogenases. This eliminates C and D by enzyme-class mismatch and eliminates B by the NRPS-product-class association learned from many other NRPS systems. No fact specific to this exact protein's annotation is strictly required to make the distinction among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the protein is identified as an NRPS, choices C (transferase) and D (dehydrogenase) are clearly incompatible. Between A and B, the strong and well-documented association of bacterial NRPS with pigment biosynthesis versus the general absence of NRPS in alkaloid biosynthesis pathways makes A the clearly superior choice. No reasonable ambiguity remains among the four options."
  },
  "important_caveats": [
    "The A-domain specificity-conferring residues (Stachelhaus code) could in principle confirm glutamine activation (consistent with indigoidine), but this level of detail is not necessary to distinguish the offered choices.",
    "The UniProt annotation uses ECO:0000269 (manual assertion) linked to PubMed:11790734, which provides experimental characterization of indigoidine as a blue pigment and its biosynthetic genes.",
    "A small number of NRPS enzymes have been annotated under 'Alkaloid biosynthesis' in databases (e.g., some fungal pathways), but these are exceptions and do not undermine the general NRPS-pigment association in bacteria."
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
  "benchmark_sequence_length": 1488,
  "benchmark_sequence_sha256": "3e683829c8442e0bf03ec13937dea8f96def35b5488452f2558692c05563ba91",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_record_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1488,
  "current_source_sequence_sha256": "3e683829c8442e0bf03ec13937dea8f96def35b5488452f2558692c05563ba91",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9L391",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "selected_historical_source_sequence_length": 1488,
  "selected_historical_source_sequence_sha256": "3e683829c8442e0bf03ec13937dea8f96def35b5488452f2558692c05563ba91",
  "selected_historical_version": {
    "accession": "Q9L391",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "INDGS_DICD3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9L391\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Erwinia chrysanthemi (strain 3937)\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Pectobacteriaceae\",\"Dickeya\"],\"scientificName\":\"Dickeya dadantii (strain 3937)\",\"taxonId\":198628}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11790734\",\"source\":\"PubMed\"}],\"value\":\"4.3.3.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Indigoidine synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11790734\",\"source\":\"PubMed\"}],\"value\":\"Pigment biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Reverchon S.\",\"Rouanet C.\",\"Expert D.\",\"Nasser W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11790734\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.184.3.654-665.2002\"}],\"citationType\":\"journal article\",\"firstPage\":\"654\",\"id\":\"11790734\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"665\",\"publicationDate\":\"2002\",\"title\":\"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi and role of this blue pigment in pathogenicity.\",\"volume\":\"184\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAB87990.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"3937\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS AN INDIGOIDINE SYNTHASE\",\"PATHWAY\",\"INDUCTION\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   INDGS_DICD3             Reviewed;        1488 AA.\nAC   Q9L391; E0SMH6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Indigoidine synthase {ECO:0000305};\nDE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};\nGN   Name=indC {ECO:0000303|PubMed:11790734};\nGN   OrderedLocusNames=Dda3937_00972 {ECO:0000312|EMBL:ADN00615.1};\nOS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Pectobacteriaceae; Dickeya.\nOX   NCBI_TaxID=198628;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB87990.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS AN INDIGOIDINE SYNTHASE,\nRP   PATHWAY, INDUCTION, AND DOMAIN.\nRC   STRAIN=3937;\nRX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;\nRA   Reverchon S., Rouanet C., Expert D., Nasser W.;\nRT   \"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi\nRT   and role of this blue pigment in pathogenicity.\";\nRL   J. Bacteriol. 184:654-665(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Pigment biosynthesis. {ECO:0000269|PubMed:11790734}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
