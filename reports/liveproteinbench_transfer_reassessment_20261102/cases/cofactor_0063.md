# cofactor_0063

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0063.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Ca(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTNGADPLGRFSALTREWFTTAFAAPTPAQADAWSAISEGNNTLVIAPTGSGKTLAAFLWAIDRLADPAREPSQGTQVLYVSPLKALAVDVERNLRTPLTGITRVAERHGLPAPSITVGVRSGDTPPNQRRAMIANPPDVLITTPESLFLMLTSAARETLTSVRTVIVDEVHAVAATKRGAHLALSLERLDQLLDTPAQRIGLSATVRPPEEVARFLSGQAPTTIVCPPAAKTFDLSVQVPVPDMANLDNNSIWPDVEERIVDLVEAHNSSIVFANSRRLAERLTSRLNEIHAERSGIELPAGPNPEVGGGAPAHLMGSGQANGAPPLLARAHHGSVSKEQRAQVEDDLKSGRLRAVVATSSLELGIDMGAVDLVIQVEAPPSVASGLQRVGRAGHQVGEISQGVLFPKHRTDLIGCAVTVQRMQTGDIETLRVPANPLDVLAQHTVAVAALEPVDADAWFDAVRRSAPFATLPRSAFEATLDLLSGKYPSTEFAELRPRLVYDRDTGTLTARPGAQRLAVTSGGAIPDRGMFTVYLASETEKPSRVGELDEEMVYESRPGDVISLGATSWRITEITHDRVLVIPAPGQPARLPFWRGDSVGRPAELGAAVGAFTGELASLDRKAFDKRCQKMGFAGYATDNLHQLLREQREATGVVPSDTTFVVERFRDELGDWRVILHSPYGLRVHGPLALAVGRRLRERYGIDEKPTASDDGIIVRLPDSGDTPPGADLFVFDADEIEPIVTAEVGGSALFASRFRECAARALLLPRRHPGKRSPLWHQRQRAAQLLDIARKYPDFPIVLEAVRECLQDVYDVPALIELMHKIAQRRLRIVEVETATPSPFAASLLFGYVGAFMYEGDSPLAERRAAALALDTVLLSELLGRVELRELLDPAVVASTSAQLQHLTPERAARDAEGVADLLRLLGPLTEADIAQRCTADNIGAWLDGLHAAKRALPVTYAGQTWWAAVEDIGLLRDGIGVPVPVGVPAAFTESASDPLGDLIGRYARTRGPFTTEQTAARFGLGVRVASDVLSRMAVDGRLIRGEFAADLSGEQWCDAQVLKILRRRSLAALRAQVEPVSTDAYARFLPSWQHVGSTNTTGIDGLATVIEQLAGVPIPASAVESLVFPQRVRDYQPAMLDELLASGEVMWSGAGQIGNGDGWVAFHLADTAPLTLTHGAEIEFTDTHRVILETLGHGGAYFFRQLTDGTVEGTAGQELKQALWELIWAGWVTGDTFAPVRAVLSGPRRSGAPAHRQRQRPPRLSRYSVAHAQTRGTDPTVSGRWSALPAAEPDSTVRAHFQAELLLGRHGVLTKGAVGAEGVPGGFATLYKVLSTFEDAGRCQRGYFVESLGGAQFAVASTVDRLRSYLDNVDPERPEYHAVVLAATDPANPYGAALGWPTDSEAHRPGRKAGALVALVDGRLVWFLERGGRSLLSFGADADAQRAAAGALTDLVSAGRIPSLLVERINGVAVLDPDVDAERAVVQDALLGAGLSRTPRGLRLR

[Multiple Choices]
A. Na(+)
B. Ca(2+)
C. Co(2+)
D. Mn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates Ca(2+) as a cofactor based on experimental evidence and says the ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the intended answer, though it establishes preference more directly than an exclusive requirement.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable ATPase/helicase nucleotide-binding motif, so transferable knowledge suggests ATP hydrolysis and a likely role for a divalent metal; that makes Na(+) less plausible. But this family-level information does not meaningfully distinguish Ca(2+) from Mn(2+) or Co(2+), since the specific metal preference is an empirical property rather than something established by the visible motif.


**Missing item-specific fact**

> The experimental metal-dependence or relative activity measurements for this particular helicase, which identify Ca(2+) as the most effective ion.


**Reason**

> General ATPase and helicase knowledge narrows the choices but does not justify selecting calcium over the other offered divalent ions. The relevant calcium preference is specific experimental information about this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence identifies Ca(2+) as the most effective ion, supporting the intended choice. However, the wording 'required' is stronger than the evidence that calcium is preferred, and the evidence does not establish that other ions cannot support activity.


### Important caveats

- The annotation describes Ca(2+) as most efficient, not necessarily as the sole ion capable of supporting activity.
- The source note repeats Mn(2+) when listing less-effective ions; the duplicated wording does not alter its explicit Ca(2+) cofactor annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable ATPase/helicase nucleotide-binding motif, so transferable knowledge suggests ATP hydrolysis and a likely role for a divalent metal; that makes Na(+) less plausible. But this family-level information does not meaningfully distinguish Ca(2+) from Mn(2+) or Co(2+), since the specific metal preference is an empirical property rather than something established by the visible motif.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental metal-dependence or relative activity measurements for this particular helicase, which identify Ca(2+) as the most effective ion.",
    "reason": "General ATPase and helicase knowledge narrows the choices but does not justify selecting calcium over the other offered divalent ions. The relevant calcium preference is specific experimental information about this protein."
  },
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Ca(2+) as a cofactor based on experimental evidence and says the ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the intended answer, though it establishes preference more directly than an exclusive requirement."
  },
  "important_caveats": [
    "The annotation describes Ca(2+) as most efficient, not necessarily as the sole ion capable of supporting activity.",
    "The source note repeats Mn(2+) when listing less-effective ions; the duplicated wording does not alter its explicit Ca(2+) cofactor annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence identifies Ca(2+) as the most effective ion, supporting the intended choice. However, the wording 'required' is stronger than the evidence that calcium is preferred, and the evidence does not establish that other ions cannot support activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates Ca(2+) as a cofactor based on experimental evidence and says the ssDNA-dependent ATPase is most efficient with Ca(2+). This supports B as the intended answer, though it establishes preference more directly than an exclusive requirement.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable ATPase/helicase nucleotide-binding motif, so transferable knowledge suggests ATP hydrolysis and a likely role for a divalent metal; that makes Na(+) less plausible. But this family-level information does not meaningfully distinguish Ca(2+) from Mn(2+) or Co(2+), since the specific metal preference is an empirical property rather than something established by the visible motif.",
    "missing_item_specific_fact": "The experimental metal-dependence or relative activity measurements for this particular helicase, which identify Ca(2+) as the most effective ion.",
    "reason": "General ATPase and helicase knowledge narrows the choices but does not justify selecting calcium over the other offered divalent ions. The relevant calcium preference is specific experimental information about this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence identifies Ca(2+) as the most effective ion, supporting the intended choice. However, the wording 'required' is stronger than the evidence that calcium is preferred, and the evidence does not establish that other ions cannot support activity."
  },
  "important_caveats": [
    "The annotation describes Ca(2+) as most efficient, not necessarily as the sole ion capable of supporting activity.",
    "The source note repeats Mn(2+) when listing less-effective ions; the duplicated wording does not alter its explicit Ca(2+) cofactor annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0QT91 (LHR_MYCS2, Lhr helicase from Mycolicibacterium smegmatis) explicitly annotates Ca(2+) (CHEBI:29108) as the cofactor with experimental evidence (ECO:0000269, PubMed:23549043, Ordonez & Shuman 2013 JBC). The annotation note states: 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental biochemical data.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally determined cofactor preference of the Lhr helicase for Ca(2+) over Mn(2+) is a specific quantitative measurement (Ca2+ most efficient; Mn2+ 60% less effective) from Ordonez & Shuman 2013. This preference is highly unusual for a RecA-fold/P-loop NTPase helicase, where Mg(2+) or Mn(2+) would be the expected cofactor by general biological principles. The Lhr family is described as 'a novel family of bacterial helicases' (Ejaz et al. 2018), meaning no established family-level cofactor pattern exists that would allow transfer-based inference. The PDB structure (5V9X) actually shows Mg(2+) bound, further confounding sequence-based prediction.


**Reason**

> The protein contains a Walker A motif (PTGSGKT) and RecA-fold domains characteristic of P-loop NTPases/helicases. General knowledge of helicase and ATPase biochemistry would predict Mg(2+) or Mn(2+) as the divalent metal cofactor, not Ca(2+). The preference for Ca(2+) over Mn(2+) in this specific novel helicase family is an unusual, experimentally determined fact (ECO:0000269) that cannot be inferred from sequence features, family membership, or general metal-coordination principles. A knowledgeable model relying on transfer from other helicases would more likely select Mn(2+) (option D) than Ca(2+) (option B). Distinguishing the correct answer requires knowing this specific protein's experimental cofactor data.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The UniProt note states Mn(2+) supports activity at 60% of Ca(2+) efficiency, meaning Mn(2+) is functionally relevant. However, the annotation designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required for catalytic activity.' While Mn(2+) is partially defensible as a functional cofactor, Ca(2+) is the clearly annotated primary cofactor. The ambiguity is minor since the annotation unambiguously selects Ca(2+).


### Important caveats

- The UniProt cofactor note appears to contain a typo: 'Mn(2+) and Mn(2+) are 60% less effective' likely should read 'Mg(2+) and Mn(2+) are 60% less effective.'
- The PDB crystal structure (5V9X) shows Mg(2+) in the active site, creating a discrepancy between structural and biochemical cofactor data that further complicates sequence-based prediction.
- The Lhr helicase family is described as novel (2018 paper), limiting the availability of transferable family-level cofactor patterns.
- Na(+) (option A) and Co(2+) (option C) are clearly implausible cofactors for an ATP-dependent helicase, making the real discrimination between B and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined cofactor preference of the Lhr helicase for Ca(2+) over Mn(2+) is a specific quantitative measurement (Ca2+ most efficient; Mn2+ 60% less effective) from Ordonez & Shuman 2013. This preference is highly unusual for a RecA-fold/P-loop NTPase helicase, where Mg(2+) or Mn(2+) would be the expected cofactor by general biological principles. The Lhr family is described as 'a novel family of bacterial helicases' (Ejaz et al. 2018), meaning no established family-level cofactor pattern exists that would allow transfer-based inference. The PDB structure (5V9X) actually shows Mg(2+) bound, further confounding sequence-based prediction.",
    "reason": "The protein contains a Walker A motif (PTGSGKT) and RecA-fold domains characteristic of P-loop NTPases/helicases. General knowledge of helicase and ATPase biochemistry would predict Mg(2+) or Mn(2+) as the divalent metal cofactor, not Ca(2+). The preference for Ca(2+) over Mn(2+) in this specific novel helicase family is an unusual, experimentally determined fact (ECO:0000269) that cannot be inferred from sequence features, family membership, or general metal-coordination principles. A knowledgeable model relying on transfer from other helicases would more likely select Mn(2+) (option D) than Ca(2+) (option B). Distinguishing the correct answer requires knowing this specific protein's experimental cofactor data."
  },
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0QT91 (LHR_MYCS2, Lhr helicase from Mycolicibacterium smegmatis) explicitly annotates Ca(2+) (CHEBI:29108) as the cofactor with experimental evidence (ECO:0000269, PubMed:23549043, Ordonez & Shuman 2013 JBC). The annotation note states: 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental biochemical data."
  },
  "important_caveats": [
    "The UniProt cofactor note appears to contain a typo: 'Mn(2+) and Mn(2+) are 60% less effective' likely should read 'Mg(2+) and Mn(2+) are 60% less effective.'",
    "The PDB crystal structure (5V9X) shows Mg(2+) in the active site, creating a discrepancy between structural and biochemical cofactor data that further complicates sequence-based prediction.",
    "The Lhr helicase family is described as novel (2018 paper), limiting the availability of transferable family-level cofactor patterns.",
    "Na(+) (option A) and Co(2+) (option C) are clearly implausible cofactors for an ATP-dependent helicase, making the real discrimination between B and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The UniProt note states Mn(2+) supports activity at 60% of Ca(2+) efficiency, meaning Mn(2+) is functionally relevant. However, the annotation designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required for catalytic activity.' While Mn(2+) is partially defensible as a functional cofactor, Ca(2+) is the clearly annotated primary cofactor. The ambiguity is minor since the annotation unambiguously selects Ca(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0QT91 (LHR_MYCS2, Lhr helicase from Mycolicibacterium smegmatis) explicitly annotates Ca(2+) (CHEBI:29108) as the cofactor with experimental evidence (ECO:0000269, PubMed:23549043, Ordonez & Shuman 2013 JBC). The annotation note states: 'ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental biochemical data.",
    "evidence_ids": ["C5", "H6", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally determined cofactor preference of the Lhr helicase for Ca(2+) over Mn(2+) is a specific quantitative measurement (Ca2+ most efficient; Mn2+ 60% less effective) from Ordonez & Shuman 2013. This preference is highly unusual for a RecA-fold/P-loop NTPase helicase, where Mg(2+) or Mn(2+) would be the expected cofactor by general biological principles. The Lhr family is described as 'a novel family of bacterial helicases' (Ejaz et al. 2018), meaning no established family-level cofactor pattern exists that would allow transfer-based inference. The PDB structure (5V9X) actually shows Mg(2+) bound, further confounding sequence-based prediction.",
    "reason": "The protein contains a Walker A motif (PTGSGKT) and RecA-fold domains characteristic of P-loop NTPases/helicases. General knowledge of helicase and ATPase biochemistry would predict Mg(2+) or Mn(2+) as the divalent metal cofactor, not Ca(2+). The preference for Ca(2+) over Mn(2+) in this specific novel helicase family is an unusual, experimentally determined fact (ECO:0000269) that cannot be inferred from sequence features, family membership, or general metal-coordination principles. A knowledgeable model relying on transfer from other helicases would more likely select Mn(2+) (option D) than Ca(2+) (option B). Distinguishing the correct answer requires knowing this specific protein's experimental cofactor data."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The UniProt note states Mn(2+) supports activity at 60% of Ca(2+) efficiency, meaning Mn(2+) is functionally relevant. However, the annotation designates Ca(2+) as THE cofactor, and the question asks for 'the specific cofactor required for catalytic activity.' While Mn(2+) is partially defensible as a functional cofactor, Ca(2+) is the clearly annotated primary cofactor. The ambiguity is minor since the annotation unambiguously selects Ca(2+)."
  },
  "important_caveats": [
    "The UniProt cofactor note appears to contain a typo: 'Mn(2+) and Mn(2+) are 60% less effective' likely should read 'Mg(2+) and Mn(2+) are 60% less effective.'",
    "The PDB crystal structure (5V9X) shows Mg(2+) in the active site, creating a discrepancy between structural and biochemical cofactor data that further complicates sequence-based prediction.",
    "The Lhr helicase family is described as novel (2018 paper), limiting the availability of transferable family-level cofactor patterns.",
    "Na(+) (option A) and Co(2+) (option C) are clearly implausible cofactors for an ATP-dependent helicase, making the real discrimination between B and D."
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
  "benchmark_sequence_length": 1507,
  "benchmark_sequence_sha256": "df6c8d2369c88ffbb7e9bcde2d7556ef9f3d2afd25392c0bf714c7b7ff56d20b",
  "current_entry_audit": {
    "entryVersion": 133,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1507,
  "current_source_sequence_sha256": "df6c8d2369c88ffbb7e9bcde2d7556ef9f3d2afd25392c0bf714c7b7ff56d20b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 131,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0QT91",
  "selected_historical_entry_version": 131,
  "selected_historical_record_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "selected_historical_source_sequence_length": 1507,
  "selected_historical_source_sequence_sha256": "df6c8d2369c88ffbb7e9bcde2d7556ef9f3d2afd25392c0bf714c7b7ff56d20b",
  "selected_historical_version": {
    "accession": "A0QT91",
    "database": "Swiss-Prot",
    "entryVersion": 131,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LHR_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0QT91\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":133,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DNA and RNA:DNA 3'-5' helicase Lhr\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23549043\",\"source\":\"PubMed\"}],\"value\":\"Long helicase-related protein\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P30015\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.2.27\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23549043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29165676\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23549043\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"value\":\"Lhr helicase/ probable uracil glycosylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29108\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23549043\",\"source\":\"PubMed\"}],\"name\":\"Ca(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23549043\",\"source\":\"PubMed\"}],\"value\":\"ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and Mn(2+) are 60% less effective.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ordonez H.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23549043\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.466854\"}],\"citationType\":\"journal article\",\"firstPage\":\"14125\",\"id\":\"23549043\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"14134\",\"publicationDate\":\"2013\",\"title\":\"Mycobacterium smegmatis Lhr Is a DNA-dependent ATPase and a 3'-to-5' DNA translocase and helicase that prefers to unwind 3'-tailed RNA:DNA hybrids.\",\"volume\":\"288\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"FUNCTION AS AN ATPASE\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DOMAIN\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Warren G.M.\",\"Ejaz A.\",\"Fay A.\",\"Glickman M.S.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36610794\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkac1222\"}],\"citationType\":\"journal article\",\"firstPage\":\"218\",\"id\":\"36610794\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"235\",\"publicationDate\":\"2023\",\"title\":\"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents mitomycin C and cisplatin.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION AS A HELICASE\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 170-ASP-GLU-171; TRP-597; 1199-HIS--ARG-1206 AND ARG-1286\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT91.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Ejaz A.\",\"Ordonez H.\",\"Jacewicz A.\",\"Ferrao R.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29165676\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkx1163\"}],\"citationType\":\"journal article\",\"firstPage\":\"442\",\"id\":\"29165676\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"455\",\"publicationDate\":\"2018\",\"title\":\"Structure of mycobacterial 3'-to-5' RNA:DNA helicase Lhr bound to a ssDNA tracking strand highlights distinctive features of a novel family of bacterial helicases.\",\"volume\":\"46\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5V9X\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.80 ANGSTROMS) OF 1-856 IN COMPLEX WITH SSDNA; MG(2+) AND ATP ANALOG\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"MUTAGENESIS OF ARG-122; THR-145; SER-148; ARG-279; ILE-528; GLU-550; TRP-597 AND ARG-777\",\"ATP-BINDING\",\"DNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-01T06:24:56.412187+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb6926ddf7c9a28e697ba0c8b0a3b7a3c722e11f49327d74524375c8aa0ebf18",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT91.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H1",
  "excerpt": "ID   LHR_MYCS2               Reviewed;        1507 AA.\nAC   A0QT91; I7FYR6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 131.\nDE   RecName: Full=Lhr helicase/ probable uracil glycosylase;\nDE            EC=3.2.2.27 {ECO:0000250|UniProtKB:P30015};\nDE            EC=5.6.2.- {ECO:0000269|PubMed:23549043, ECO:0000269|PubMed:29165676, ECO:0000269|PubMed:36610794};\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:23549043, ECO:0000269|PubMed:36610794};\nDE   AltName: Full=DNA and RNA:DNA 3'-5' helicase Lhr {ECO:0000305};\nDE   AltName: Full=Long helicase-related protein {ECO:0000303|PubMed:23549043};\nGN   Name=lhr {ECO:0000303|PubMed:23549043, ECO:0000312|EMBL:AFP38187.1};\nGN   OrderedLocusNames=MSMEG_1757 {ECO:0000312|EMBL:ABK70223.1},\nGN   MSMEI_1715 {ECO:0000312|EMBL:AFP38187.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Lhr helicase/ probable uracil glycosylase;\nDE            EC=3.2.2.27 {ECO:0000250|UniProtKB:P30015};\nDE            EC=5.6.2.- {ECO:0000269|PubMed:23549043, ECO:0000269|PubMed:29165676, ECO:0000269|PubMed:36610794};\nDE            EC=5.6.2.4 {ECO:0000269|PubMed:23549043, ECO:0000269|PubMed:36610794};\nDE   AltName: Full=DNA and RNA:DNA 3'-5' helicase Lhr {ECO:0000305};\nDE   AltName: Full=Long helicase-related protein {ECO:0000303|PubMed:23549043};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, CATALYTIC ACTIVITY,\nRP   COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND DOMAIN.\nRX   PubMed=23549043; DOI=10.1074/jbc.m113.466854;\nRA   Ordonez H., Shuman S.;\nRT   \"Mycobacterium smegmatis Lhr Is a DNA-dependent ATPase and a 3'-to-5' DNA\nRT   translocase and helicase that prefers to unwind 3'-tailed RNA:DNA\nRT   hybrids.\";\nRL   J. Biol. Chem. 288:14125-14134(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H4",
  "excerpt": "RN   [5]\nRP   FUNCTION AS A HELICASE, CATALYTIC ACTIVITY, DOMAIN, INDUCTION, DISRUPTION\nRP   PHENOTYPE, AND MUTAGENESIS OF 170-ASP-GLU-171; TRP-597; 1199-HIS--ARG-1206\nRP   AND ARG-1286.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=36610794; DOI=10.1093/nar/gkac1222;\nRA   Warren G.M., Ejaz A., Fay A., Glickman M.S., Shuman S.;\nRT   \"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents\nRT   mitomycin C and cisplatin.\";\nRL   Nucleic Acids Res. 51:218-235(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0007744|PDB:5V9X}\nRP   X-RAY CRYSTALLOGRAPHY (2.80 ANGSTROMS) OF 1-856 IN COMPLEX WITH SSDNA;\nRP   MG(2+) AND ATP ANALOG, FUNCTION, CATALYTIC ACTIVITY, DOMAIN, MUTAGENESIS OF\nRP   ARG-122; THR-145; SER-148; ARG-279; ILE-528; GLU-550; TRP-597 AND ARG-777,\nRP   ATP-BINDING, AND DNA-BINDING.\nRX   PubMed=29165676; DOI=10.1093/nar/gkx1163;\nRA   Ejaz A., Ordonez H., Jacewicz A., Ferrao R., Shuman S.;\nRT   \"Structure of mycobacterial 3'-to-5' RNA:DNA helicase Lhr bound to a ssDNA\nRT   tracking strand highlights distinctive features of a novel family of\nRT   bacterial helicases.\";\nRL   Nucleic Acids Res. 46:442-455(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Ca(2+); Xref=ChEBI:CHEBI:29108;\nCC         Evidence={ECO:0000269|PubMed:23549043};\nCC       Note=ssDNA-dependent ATPase is most efficient with Ca(2+); Mn(2+) and\nCC       Mn(2+) are 60% less effective. {ECO:0000269|PubMed:23549043};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.288105+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "63e7cfd39ab67732a5008a87dc7c46a64d5f6eba91cda925bc3db2059d72fec8",
  "url": "https://rest.uniprot.org/unisave/A0QT91?format=txt&versions=131"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
