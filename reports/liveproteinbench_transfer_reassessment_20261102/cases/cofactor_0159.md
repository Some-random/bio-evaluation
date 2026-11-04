# cofactor_0159

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0159.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKFLQIIKHLKLQNKKNALDNFVNCRTYEHISNINKLFLNNFSSTKEHSEHGQVKHENFLNSTLKYEENSQNGSTNNLKNGKYNMYVSEGNVNINEEKYKDNNISSNNTQYNNNSSNSGSLNDEGPLWKEHIDDVVNENKKKKMNRFYLDSQATTMIDPRVLDKMLPYMTYIYGNAHSRNHFFGWESEKAVEDARTNLLNLINGKNNKEIIFTSGATESNNLALIGICTYYNKLNKQKNHIITSQIEHKCILQTCRFLQTKGFEVTYLKPDTNGLVKLDDIKNSIKDNTIMASFIFVNNEIGVIQDIENIGNLCKEKNILFHTDASQAAGKVPIDVQKMNIDLMSMSGHKLYGPKGIGALYIKRKKPNIRLNALIHGGGQERGLRSGTLPTHLIVGFGEAAKVCSLEMNRDEKKVRYFFNYVKDYLTKHLDYIVFNGCQINRYYGNMNISFLFVEGESLLMSLNEIALSSGSACTSSTLEPSYVLRSIGISEDIAHTSIRIGFNRFTTFFEVQQLCINLVKSVERLRSISPLYEMELEKKNPSNDDIPKFIWT

[Multiple Choices]
A. FMN
B. Mn(2+)
C. pyridoxal 5'-phosphate
D. Fe cation
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

> The matched-sequence UniProt annotation identifies the protein as cysteine desulfurase IscS and lists pyridoxal 5'-phosphate as its cofactor. The cofactor annotation cites a paper, though the excerpt alone does not establish the exact experimental basis.

Citations as saved: [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the IscS/cysteine-desulfurase family, including a conserved cysteine-containing catalytic region. Cysteine desulfurases use PLP in catalysis; this family-level inference distinguishes option C from FMN, Mn(2+), and Fe cation, which may be relevant elsewhere in iron-sulfur biology but are not the catalytic cofactor indicated here.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family and cofactor relationship provides a meaningful basis for selecting PLP without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> For an IscS cysteine desulfurase, PLP is the distinguishing catalytic cofactor among the offered choices.


### Important caveats

- The reviewer-only annotation supports the key but was not part of the original model input.
- The cited cofactor annotation is manually asserted and paper-linked; the supplied excerpt is not itself a detailed account of experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the IscS/cysteine-desulfurase family, including a conserved cysteine-containing catalytic region. Cysteine desulfurases use PLP in catalysis; this family-level inference distinguishes option C from FMN, Mn(2+), and Fe cation, which may be relevant elsewhere in iron-sulfur biology but are not the catalytic cofactor indicated here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family and cofactor relationship provides a meaningful basis for selecting PLP without needing the exact protein's database record."
  },
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies the protein as cysteine desulfurase IscS and lists pyridoxal 5'-phosphate as its cofactor. The cofactor annotation cites a paper, though the excerpt alone does not establish the exact experimental basis."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original model input.",
    "The cited cofactor annotation is manually asserted and paper-linked; the supplied excerpt is not itself a detailed account of experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For an IscS cysteine desulfurase, PLP is the distinguishing catalytic cofactor among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies the protein as cysteine desulfurase IscS and lists pyridoxal 5'-phosphate as its cofactor. The cofactor annotation cites a paper, though the excerpt alone does not establish the exact experimental basis.",
    "evidence_ids": ["H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the IscS/cysteine-desulfurase family, including a conserved cysteine-containing catalytic region. Cysteine desulfurases use PLP in catalysis; this family-level inference distinguishes option C from FMN, Mn(2+), and Fe cation, which may be relevant elsewhere in iron-sulfur biology but are not the catalytic cofactor indicated here.",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family and cofactor relationship provides a meaningful basis for selecting PLP without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For an IscS cysteine desulfurase, PLP is the distinguishing catalytic cofactor among the offered choices."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original model input.",
    "The cited cofactor annotation is manually asserted and paper-linked; the supplied excerpt is not itself a detailed account of experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Cysteine desulfurase IscS (EC 2.8.1.7) from Plasmodium falciparum. UniProt evidence (C5, H5) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:597326), supported by experimental evidence (ECO:0000305|PubMed:34032321, Sadik et al. 2021 Mol. Microbiol.). This is consistent with the universal biochemical knowledge that all known cysteine desulfurases are PLP-dependent enzymes using a fold type I PLP mechanism.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of fold type I PLP-dependent enzymes, specifically the cysteine desulfurase (IscS/NifS) family. Key features visible in the sequence include: (1) a catalytic cysteine motif 'ICTYY' (analogous to the CxxxC catalytic cysteine in E. coli IscS C183), (2) a PLP-binding lysine in the context 'GPKGIGALYIK' (the conserved lysine that forms the internal aldimine Schiff base with PLP, characteristic of fold type I enzymes), and (3) the overall domain architecture consistent with the dimeric fold type I PLP scaffold shared by aminotransferases, decarboxylases, and desulfurases. From family-level knowledge of homologs such as E. coli IscS, Azotobacter vinelandii NifS, and human NFS1, it is an extremely well-established and universal fact that ALL cysteine desulfurases require PLP for their β-elimination mechanism (PLP→internal aldimine→cysteine external aldimine→β-elimination of sulfur→persulfide + alanine). This family-level regularity is one of the most robust enzyme-cofactor relationships in biochemistry. Against the other options: FMN is a flavin cofactor for oxidoreductases, not desulfurases; Mn(2+) is not a recognized cofactor for this enzyme class; Fe cations participate in downstream Fe-S cluster assembly but are not the catalytic cofactor of the desulfurase itself. Thus, recognizing the fold type I PLP architecture and the cysteine desulfurase family from sequence motifs, combined with the universal PLP-dependence of this family learned from many homologs, meaningfully and confidently selects option C over A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PLP dependence of cysteine desulfurases is a fundamental, universally conserved family-level property transferable from knowledge of numerous homologs (E. coli IscS, NifS, human NFS1, etc.). The sequence contains identifiable fold type I PLP motifs (catalytic Cys in ICTYY, PLP-binding Lys in GPKGIGALYIK) that allow family recognition without needing to recall the specific UniProt annotation for this exact P. falciparum entry. The other three options are mechanistically incompatible with desulfurase catalysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mechanistically distinct and well-separated. FMN belongs to flavoproteins/oxidoreductases, Mn(2+) to certain transferases/hydrolases, and Fe to metalloproteins/Fe-S cluster assembly downstream. PLP is the only cofactor consistent with the β-elimination desulfurase mechanism and the fold type I PLP architecture evident in the sequence. No ambiguity exists among the choices.


### Important caveats

- The UniProt cofactor annotation (ECO:0000305) indicates it was assigned by the curators based on the 2021 Sadik et al. experimental study, not purely by similarity transfer, strengthening the experimental basis.
- The sequence motifs identified (ICTYY, GPKGIGALYIK) are consistent with fold type I PLP enzymes but are not absolutely unique to desulfurases; however, the combination of these motifs with the overall sequence length and architecture strongly supports the IscS/NifS family assignment.
- The reviewer-only evidence confirms the sequence matches Q8IBI5 (ISCS_PLAF7) exactly (553 AA, SHA256 match), but this accession identification was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of fold type I PLP-dependent enzymes, specifically the cysteine desulfurase (IscS/NifS) family. Key features visible in the sequence include: (1) a catalytic cysteine motif 'ICTYY' (analogous to the CxxxC catalytic cysteine in E. coli IscS C183), (2) a PLP-binding lysine in the context 'GPKGIGALYIK' (the conserved lysine that forms the internal aldimine Schiff base with PLP, characteristic of fold type I enzymes), and (3) the overall domain architecture consistent with the dimeric fold type I PLP scaffold shared by aminotransferases, decarboxylases, and desulfurases. From family-level knowledge of homologs such as E. coli IscS, Azotobacter vinelandii NifS, and human NFS1, it is an extremely well-established and universal fact that ALL cysteine desulfurases require PLP for their β-elimination mechanism (PLP→internal aldimine→cysteine external aldimine→β-elimination of sulfur→persulfide + alanine). This family-level regularity is one of the most robust enzyme-cofactor relationships in biochemistry. Against the other options: FMN is a flavin cofactor for oxidoreductases, not desulfurases; Mn(2+) is not a recognized cofactor for this enzyme class; Fe cations participate in downstream Fe-S cluster assembly but are not the catalytic cofactor of the desulfurase itself. Thus, recognizing the fold type I PLP architecture and the cysteine desulfurase family from sequence motifs, combined with the universal PLP-dependence of this family learned from many homologs, meaningfully and confidently selects option C over A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PLP dependence of cysteine desulfurases is a fundamental, universally conserved family-level property transferable from knowledge of numerous homologs (E. coli IscS, NifS, human NFS1, etc.). The sequence contains identifiable fold type I PLP motifs (catalytic Cys in ICTYY, PLP-binding Lys in GPKGIGALYIK) that allow family recognition without needing to recall the specific UniProt annotation for this exact P. falciparum entry. The other three options are mechanistically incompatible with desulfurase catalysis."
  },
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The protein is Cysteine desulfurase IscS (EC 2.8.1.7) from Plasmodium falciparum. UniProt evidence (C5, H5) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:597326), supported by experimental evidence (ECO:0000305|PubMed:34032321, Sadik et al. 2021 Mol. Microbiol.). This is consistent with the universal biochemical knowledge that all known cysteine desulfurases are PLP-dependent enzymes using a fold type I PLP mechanism."
  },
  "important_caveats": [
    "The UniProt cofactor annotation (ECO:0000305) indicates it was assigned by the curators based on the 2021 Sadik et al. experimental study, not purely by similarity transfer, strengthening the experimental basis.",
    "The sequence motifs identified (ICTYY, GPKGIGALYIK) are consistent with fold type I PLP enzymes but are not absolutely unique to desulfurases; however, the combination of these motifs with the overall sequence length and architecture strongly supports the IscS/NifS family assignment.",
    "The reviewer-only evidence confirms the sequence matches Q8IBI5 (ISCS_PLAF7) exactly (553 AA, SHA256 match), but this accession identification was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically distinct and well-separated. FMN belongs to flavoproteins/oxidoreductases, Mn(2+) to certain transferases/hydrolases, and Fe to metalloproteins/Fe-S cluster assembly downstream. PLP is the only cofactor consistent with the β-elimination desulfurase mechanism and the fold type I PLP architecture evident in the sequence. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Cysteine desulfurase IscS (EC 2.8.1.7) from Plasmodium falciparum. UniProt evidence (C5, H5) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:597326), supported by experimental evidence (ECO:0000305|PubMed:34032321, Sadik et al. 2021 Mol. Microbiol.). This is consistent with the universal biochemical knowledge that all known cysteine desulfurases are PLP-dependent enzymes using a fold type I PLP mechanism.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of fold type I PLP-dependent enzymes, specifically the cysteine desulfurase (IscS/NifS) family. Key features visible in the sequence include: (1) a catalytic cysteine motif 'ICTYY' (analogous to the CxxxC catalytic cysteine in E. coli IscS C183), (2) a PLP-binding lysine in the context 'GPKGIGALYIK' (the conserved lysine that forms the internal aldimine Schiff base with PLP, characteristic of fold type I enzymes), and (3) the overall domain architecture consistent with the dimeric fold type I PLP scaffold shared by aminotransferases, decarboxylases, and desulfurases. From family-level knowledge of homologs such as E. coli IscS, Azotobacter vinelandii NifS, and human NFS1, it is an extremely well-established and universal fact that ALL cysteine desulfurases require PLP for their β-elimination mechanism (PLP→internal aldimine→cysteine external aldimine→β-elimination of sulfur→persulfide + alanine). This family-level regularity is one of the most robust enzyme-cofactor relationships in biochemistry. Against the other options: FMN is a flavin cofactor for oxidoreductases, not desulfurases; Mn(2+) is not a recognized cofactor for this enzyme class; Fe cations participate in downstream Fe-S cluster assembly but are not the catalytic cofactor of the desulfurase itself. Thus, recognizing the fold type I PLP architecture and the cysteine desulfurase family from sequence motifs, combined with the universal PLP-dependence of this family learned from many homologs, meaningfully and confidently selects option C over A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The PLP dependence of cysteine desulfurases is a fundamental, universally conserved family-level property transferable from knowledge of numerous homologs (E. coli IscS, NifS, human NFS1, etc.). The sequence contains identifiable fold type I PLP motifs (catalytic Cys in ICTYY, PLP-binding Lys in GPKGIGALYIK) that allow family recognition without needing to recall the specific UniProt annotation for this exact P. falciparum entry. The other three options are mechanistically incompatible with desulfurase catalysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically distinct and well-separated. FMN belongs to flavoproteins/oxidoreductases, Mn(2+) to certain transferases/hydrolases, and Fe to metalloproteins/Fe-S cluster assembly downstream. PLP is the only cofactor consistent with the β-elimination desulfurase mechanism and the fold type I PLP architecture evident in the sequence. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt cofactor annotation (ECO:0000305) indicates it was assigned by the curators based on the 2021 Sadik et al. experimental study, not purely by similarity transfer, strengthening the experimental basis.",
    "The sequence motifs identified (ICTYY, GPKGIGALYIK) are consistent with fold type I PLP enzymes but are not absolutely unique to desulfurases; however, the combination of these motifs with the overall sequence length and architecture strongly supports the IscS/NifS family assignment.",
    "The reviewer-only evidence confirms the sequence matches Q8IBI5 (ISCS_PLAF7) exactly (553 AA, SHA256 match), but this accession identification was not available to the evaluated model."
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
  "benchmark_sequence_length": 553,
  "benchmark_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "current_entry_audit": {
    "entryVersion": 129,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 553,
  "current_source_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 127,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IBI5",
  "selected_historical_entry_version": 127,
  "selected_historical_record_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "selected_historical_source_sequence_length": 553,
  "selected_historical_source_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "selected_historical_version": {
    "accession": "Q8IBI5",
    "database": "Swiss-Prot",
    "entryVersion": 127,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCS_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IBI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":129,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"2.8.1.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cysteine desulfurase IscS\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"INTERACTION WITH ISD11 AND ISCU\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H1",
  "excerpt": "ID   ISCS_PLAF7              Reviewed;         553 AA.\nAC   Q8IBI5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 127.\nDE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};\nDE            Short=PfIscS {ECO:0000303|PubMed:34032321};\nDE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};\nGN   Name=IscS {ECO:0000303|PubMed:24086138, ECO:0000303|PubMed:34032321};\nGN   Synonyms=NFS1 {ECO:0000305};\nGN   ORFNames=PF3D7_0727200 {ECO:0000312|EMBL:CAD51015.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};\nDE            Short=PfIscS {ECO:0000303|PubMed:34032321};\nDE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=24086138; DOI=10.1371/journal.ppat.1003655;\nRA   Gisselberg J.E., Dellibovi-Ragheb T.A., Matthews K.A., Bosch G.,\nRA   Prigge S.T.;\nRT   \"The suf iron-sulfur cluster synthesis pathway is required for apicoplast\nRT   maintenance in malaria parasites.\";\nRL   PLoS Pathog. 9:e1003655-e1003655(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, AND INTERACTION WITH ISD11\nRP   AND ISCU.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000305|PubMed:34032321};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
