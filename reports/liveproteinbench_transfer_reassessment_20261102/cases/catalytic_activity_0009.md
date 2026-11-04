# catalytic_activity_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0009.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O

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
A. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
B. enterobactin + 3 H2O = 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H(+)
C. 2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O
D. a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates this protein as indigoidine synthase and gives the reaction in option C, citing a paper that reports its function as an indigoidine synthase. This supports the key, though the database annotation is curated evidence rather than a direct experimental record included here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,488-residue sequence has features consistent with a large ATP-dependent, NRPS-like biosynthetic enzyme, including a glycine-rich ATP-binding motif. Transferable knowledge of indigoidine synthases links this enzyme family to ATP- and glutamine-dependent indigoidine production, matching option C. The alternatives describe unrelated activities: small-molecule hydrolysis, enterobactin breakdown, and RNA acetylation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level and sequence-pattern recognition provides a credible basis to distinguish the indigoidine-biosynthesis reaction from the offered alternatives; identifying the exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C matches the transferable inference for a large ATP-dependent indigoidine-biosynthesis enzyme.


### Important caveats

- The reviewer-only evidence supports the key but was not available to the evaluated model.
- The source annotation cites a publication and is curator-asserted; the supplied evidence does not independently present the underlying experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,488-residue sequence has features consistent with a large ATP-dependent, NRPS-like biosynthetic enzyme, including a glycine-rich ATP-binding motif. Transferable knowledge of indigoidine synthases links this enzyme family to ATP- and glutamine-dependent indigoidine production, matching option C. The alternatives describe unrelated activities: small-molecule hydrolysis, enterobactin breakdown, and RNA acetylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-pattern recognition provides a credible basis to distinguish the indigoidine-biosynthesis reaction from the offered alternatives; identifying the exact protein's database record is not necessary."
  },
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as indigoidine synthase and gives the reaction in option C, citing a paper that reports its function as an indigoidine synthase. This supports the key, though the database annotation is curated evidence rather than a direct experimental record included here."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available to the evaluated model.",
    "The source annotation cites a publication and is curator-asserted; the supplied evidence does not independently present the underlying experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C matches the transferable inference for a large ATP-dependent indigoidine-biosynthesis enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as indigoidine synthase and gives the reaction in option C, citing a paper that reports its function as an indigoidine synthase. This supports the key, though the database annotation is curated evidence rather than a direct experimental record included here.",
    "evidence_ids": ["C4", "C5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,488-residue sequence has features consistent with a large ATP-dependent, NRPS-like biosynthetic enzyme, including a glycine-rich ATP-binding motif. Transferable knowledge of indigoidine synthases links this enzyme family to ATP- and glutamine-dependent indigoidine production, matching option C. The alternatives describe unrelated activities: small-molecule hydrolysis, enterobactin breakdown, and RNA acetylation.",
    "missing_item_specific_fact": "",
    "reason": "Family-level and sequence-pattern recognition provides a credible basis to distinguish the indigoidine-biosynthesis reaction from the offered alternatives; identifying the exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C matches the transferable inference for a large ATP-dependent indigoidine-biosynthesis enzyme."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available to the evaluated model.",
    "The source annotation cites a publication and is curator-asserted; the supplied evidence does not independently present the underlying experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9) lists exactly the reaction in Choice C: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O' (evidence codes ECO:0000305, PubMed:11790734). The sequence SHA256 matches the benchmark input (1488 aa). The annotation is supported by a 2002 J. Bacteriol. paper characterizing indigoidine biosynthetic genes in Erwinia chrysanthemi.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1488-aa sequence contains the canonical NRPS adenylation-domain motif 'TSGSTGKPG' (a highly conserved signature shared across hundreds of nonribosomal peptide synthetases), the PCP-domain 'YGP' motif, and a 'GAP' condensation-domain motif. This multi-domain NRPS architecture (A + PCP + C) is incompatible with the enzyme classes implied by the other choices: A (pyrrolizixenacetamide hydrolase, an α/β-hydrolase), B (enterobactin esterase, an α/β-hydrolase/esterase), and D (N4-acetylcytidine acetyltransferase, a GNAT-fold transferase). Only Choice C describes an NRPS-like condensation reaction (FMN + L-glutamine + ATP → indigoidine). The TSGSTGKPG motif is among the most widely taught and recognized sequence signatures in enzymology, appearing in virtually every NRPS textbook and database entry; recognizing it as an A-domain marker is standard transferable knowledge from many other proteins. Since only one offered option is consistent with NRPS catalysis, the family-level inference is sufficient to select C without knowing this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NRPS domain architecture (TSGSTGKPG A-domain, YGP PCP, GAP C-domain) is a well-known, transferable sequence signature shared across many nonribosomal peptide synthetases. It cleanly excludes the hydrolase (A, B) and acetyltransferase (D) alternatives, leaving only the NRPS-type reaction C. This is a concrete family-level inference from conserved motifs, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes (hydrolase, esterase, NRPS-like synthetase, acetyltransferase). The NRPS domain architecture in the sequence unambiguously selects C and excludes A, B, and D. No ambiguity among options.


### Important caveats

- The UniProt annotation carries evidence code ECO:0000305 (inferred by similarity to a related protein, Q1MWN4), not direct experimental characterization of Q9L391 itself, though the 2002 paper (PubMed:11790734) did functionally characterize the indigoidine biosynthetic pathway.
- The reviewer-only accession Q9L391 was inferred from dataset metadata and was not available to the evaluated model; the model must rely on sequence motifs alone.
- The FMN dependence of indigoidine synthase is unusual among NRPS enzymes (most use NADPH), but this specificity is not needed to distinguish among the four offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1488-aa sequence contains the canonical NRPS adenylation-domain motif 'TSGSTGKPG' (a highly conserved signature shared across hundreds of nonribosomal peptide synthetases), the PCP-domain 'YGP' motif, and a 'GAP' condensation-domain motif. This multi-domain NRPS architecture (A + PCP + C) is incompatible with the enzyme classes implied by the other choices: A (pyrrolizixenacetamide hydrolase, an α/β-hydrolase), B (enterobactin esterase, an α/β-hydrolase/esterase), and D (N4-acetylcytidine acetyltransferase, a GNAT-fold transferase). Only Choice C describes an NRPS-like condensation reaction (FMN + L-glutamine + ATP → indigoidine). The TSGSTGKPG motif is among the most widely taught and recognized sequence signatures in enzymology, appearing in virtually every NRPS textbook and database entry; recognizing it as an A-domain marker is standard transferable knowledge from many other proteins. Since only one offered option is consistent with NRPS catalysis, the family-level inference is sufficient to select C without knowing this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NRPS domain architecture (TSGSTGKPG A-domain, YGP PCP, GAP C-domain) is a well-known, transferable sequence signature shared across many nonribosomal peptide synthetases. It cleanly excludes the hydrolase (A, B) and acetyltransferase (D) alternatives, leaving only the NRPS-type reaction C. This is a concrete family-level inference from conserved motifs, not a lookup of this protein's specific annotation."
  },
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9) lists exactly the reaction in Choice C: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O' (evidence codes ECO:0000305, PubMed:11790734). The sequence SHA256 matches the benchmark input (1488 aa). The annotation is supported by a 2002 J. Bacteriol. paper characterizing indigoidine biosynthetic genes in Erwinia chrysanthemi."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000305 (inferred by similarity to a related protein, Q1MWN4), not direct experimental characterization of Q9L391 itself, though the 2002 paper (PubMed:11790734) did functionally characterize the indigoidine biosynthetic pathway.",
    "The reviewer-only accession Q9L391 was inferred from dataset metadata and was not available to the evaluated model; the model must rely on sequence motifs alone.",
    "The FMN dependence of indigoidine synthase is unusual among NRPS enzymes (most use NADPH), but this specificity is not needed to distinguish among the four offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (hydrolase, esterase, NRPS-like synthetase, acetyltransferase). The NRPS domain architecture in the sequence unambiguously selects C and excludes A, B, and D. No ambiguity among options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9) lists exactly the reaction in Choice C: '2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O' (evidence codes ECO:0000305, PubMed:11790734). The sequence SHA256 matches the benchmark input (1488 aa). The annotation is supported by a 2002 J. Bacteriol. paper characterizing indigoidine biosynthetic genes in Erwinia chrysanthemi.",
    "evidence_ids": ["C4", "C5", "C8", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1488-aa sequence contains the canonical NRPS adenylation-domain motif 'TSGSTGKPG' (a highly conserved signature shared across hundreds of nonribosomal peptide synthetases), the PCP-domain 'YGP' motif, and a 'GAP' condensation-domain motif. This multi-domain NRPS architecture (A + PCP + C) is incompatible with the enzyme classes implied by the other choices: A (pyrrolizixenacetamide hydrolase, an α/β-hydrolase), B (enterobactin esterase, an α/β-hydrolase/esterase), and D (N4-acetylcytidine acetyltransferase, a GNAT-fold transferase). Only Choice C describes an NRPS-like condensation reaction (FMN + L-glutamine + ATP → indigoidine). The TSGSTGKPG motif is among the most widely taught and recognized sequence signatures in enzymology, appearing in virtually every NRPS textbook and database entry; recognizing it as an A-domain marker is standard transferable knowledge from many other proteins. Since only one offered option is consistent with NRPS catalysis, the family-level inference is sufficient to select C without knowing this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "The NRPS domain architecture (TSGSTGKPG A-domain, YGP PCP, GAP C-domain) is a well-known, transferable sequence signature shared across many nonribosomal peptide synthetases. It cleanly excludes the hydrolase (A, B) and acetyltransferase (D) alternatives, leaving only the NRPS-type reaction C. This is a concrete family-level inference from conserved motifs, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (hydrolase, esterase, NRPS-like synthetase, acetyltransferase). The NRPS domain architecture in the sequence unambiguously selects C and excludes A, B, and D. No ambiguity among options."
  },
  "important_caveats": [
    "The UniProt annotation carries evidence code ECO:0000305 (inferred by similarity to a related protein, Q1MWN4), not direct experimental characterization of Q9L391 itself, though the 2002 paper (PubMed:11790734) did functionally characterize the indigoidine biosynthetic pathway.",
    "The reviewer-only accession Q9L391 was inferred from dataset metadata and was not available to the evaluated model; the model must rely on sequence motifs alone.",
    "The FMN dependence of indigoidine synthase is unusual among NRPS enzymes (most use NADPH), but this specificity is not needed to distinguish among the four offered choices."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11790734\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81500\"}}],\"reaction\":{\"ecNumber\":\"4.3.3.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"11790734\",\"source\":\"PubMed\"}],\"name\":\"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1MWN4\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81504\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1MWN4\",\"source\":\"UniProtKB\"}],\"name\":\"FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81503\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1MWN4\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81508\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1MWN4\",\"source\":\"UniProtKB\"}],\"name\":\"2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81507\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:04.012566+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282",
  "url": "https://rest.uniprot.org/uniprotkb/Q9L391.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)

```json
{
  "evidence_id": "C8",
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
  "excerpt": "DE   RecName: Full=Indigoidine synthase {ECO:0000305};\nDE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2\nCC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;\nCC         Evidence={ECO:0000305|PubMed:11790734};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;\nCC         Evidence={ECO:0000305|PubMed:11790734};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-\nCC         dione + FMNH2 + AMP + diphosphate; Xref=Rhea:RHEA:81503,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58359, ChEBI:CHEBI:231893,\nCC         ChEBI:CHEBI:456215; Evidence={ECO:0000250|UniProtKB:Q1MWN4};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81504;\nCC         Evidence={ECO:0000250|UniProtKB:Q1MWN4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2\nCC         H2O; Xref=Rhea:RHEA:81507, ChEBI:CHEBI:15377, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:231893;\nCC         Evidence={ECO:0000250|UniProtKB:Q1MWN4};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81508;\nCC         Evidence={ECO:0000250|UniProtKB:Q1MWN4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:06.750542+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877",
  "url": "https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
