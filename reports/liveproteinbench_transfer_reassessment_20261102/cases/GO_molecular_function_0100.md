# GO_molecular_function_0100

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0100.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — metal ion binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNTLQLINKNHPLKKNQEPPHLVLAPFSDHDVYLQPEVAKQWERLVRATGLEKDIRLVDGYRTEKEQRRLWEYSLKENGLAYTKQFVALPGCSEHQIGLAIDVGLKKQEDDDLICPHFRDSAAADLFMQQMMNYGFILRYPEDKQEITGISYEPWHFRYVGLPHSQVITAQKWTLEEYHDYLAQTVRQFA

[Multiple Choices]
A. large ribosomal subunit rRNA binding
B. ATPase inhibitor activity
C. metal ion binding
D. cAMP-dependent protein kinase activity
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

> The matched protein has a metal-ion-binding annotation, and structural evidence reports complexes with copper and zinc. This supports choice C, although metal binding is not its primary catalytic activity.

Citations as saved: [H5](#evidence-h5), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The short bacterial sequence has histidine- and acidic-residue-rich regions consistent with a metal-dependent peptidase active site. Transferable knowledge that metallopeptidases use metal ions for catalysis makes metal-ion binding a credible choice; the other options would ordinarily require recognizable ribosomal-binding, ATPase-inhibitor, or protein-kinase features not apparent here.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family- and motif-level inference gives a meaningful basis for choosing C among these alternatives, even though the sequence alone does not establish the exact bound metal or prove the annotation experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein's peptidase activity is not offered, but among the listed choices metal ion binding is the defensible option; the other alternatives are not similarly supported.


### Important caveats

- Metal ion binding is an ancillary molecular function here, not the protein's primary catalytic function.
- The supplied structural evidence shows metal-bound complexes, while the cited GO annotation is electronically inferred; these evidence types should not be conflated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short bacterial sequence has histidine- and acidic-residue-rich regions consistent with a metal-dependent peptidase active site. Transferable knowledge that metallopeptidases use metal ions for catalysis makes metal-ion binding a credible choice; the other options would ordinarily require recognizable ribosomal-binding, ATPase-inhibitor, or protein-kinase features not apparent here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family- and motif-level inference gives a meaningful basis for choosing C among these alternatives, even though the sequence alone does not establish the exact bound metal or prove the annotation experimentally."
  },
  "case_id": "GO_molecular_function_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The matched protein has a metal-ion-binding annotation, and structural evidence reports complexes with copper and zinc. This supports choice C, although metal binding is not its primary catalytic activity."
  },
  "important_caveats": [
    "Metal ion binding is an ancillary molecular function here, not the protein's primary catalytic function.",
    "The supplied structural evidence shows metal-bound complexes, while the cited GO annotation is electronically inferred; these evidence types should not be conflated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's peptidase activity is not offered, but among the listed choices metal ion binding is the defensible option; the other alternatives are not similarly supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein has a metal-ion-binding annotation, and structural evidence reports complexes with copper and zinc. This supports choice C, although metal binding is not its primary catalytic activity.",
    "evidence_ids": ["H5", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The short bacterial sequence has histidine- and acidic-residue-rich regions consistent with a metal-dependent peptidase active site. Transferable knowledge that metallopeptidases use metal ions for catalysis makes metal-ion binding a credible choice; the other options would ordinarily require recognizable ribosomal-binding, ATPase-inhibitor, or protein-kinase features not apparent here.",
    "missing_item_specific_fact": "",
    "reason": "Family- and motif-level inference gives a meaningful basis for choosing C among these alternatives, even though the sequence alone does not establish the exact bound metal or prove the annotation experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's peptidase activity is not offered, but among the listed choices metal ion binding is the defensible option; the other alternatives are not similarly supported."
  },
  "important_caveats": [
    "Metal ion binding is an ancillary molecular function here, not the protein's primary catalytic function.",
    "The supplied structural evidence shows metal-bound complexes, while the cited GO annotation is electronically inferred; these evidence types should not be conflated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q9JN36, VanXYC) is annotated with GO:0046872 (metal ion binding) in UniProt (H11, evidence code IEA:UniProtKB-KW). The X-ray crystallography reference (C12/H5, PubMed:24711382) explicitly describes complexes with copper and zinc, providing experimental confirmation of metal binding. While the protein's primary catalytic function is D-Ala-D-Ala dipeptidase/carboxypeptidase activity (EC 3.4.13.22, EC 3.4.17.-), metal ion binding is a genuine molecular function of this metalloenzyme and is the only correct option among the four offered. The other three choices (ribosomal rRNA binding, ATPase inhibitor, cAMP-dependent protein kinase) have no annotation or structural basis for this protein.

Citations as saved: [H11](#evidence-h11), [C12](#evidence-c12), [H5](#evidence-h5), [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 190-residue sequence lacks all hallmark motifs for options A, B, and D: no RRM/KH/arginine-rich RNA-binding domains (eliminating A), no ATPase-inhibitor fold (eliminating B), and no kinase signature motifs such as the HRD catalytic loop, DFG motif, glycine-rich ATP-binding loop, or cAMP-binding domain (eliminating D). In contrast, the sequence contains multiple metal-coordinating residue clusters in spatially suggestive arrangements: 'CPHF' (Cys-Pro-His-Phe), 'WHFRY' (Trp-His-Phe-Arg-Tyr), 'EDDDL' (Glu-Asp-Asp-Asp-Leu), and 'SDHD' (Ser-Asp-His-Asp). These patterns—His, Cys, Asp, Glu residues in proximity—are the canonical signature of metalloenzyme active sites found across many peptidase families (e.g., zinc-dependent metallo-peptidases). Knowledge from other metallo-peptidases (VanX homologs, carboxypeptidases, aminopeptidases) establishes that such residue arrangements indicate metal ion coordination. The overall small size and compact fold further exclude ribosomal or kinase functions. Thus, transferable family-level knowledge of metalloenzyme motifs meaningfully distinguishes C from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A, B, and D by the absence of their defining structural motifs and select C based on the presence of metal-coordinating residue patterns (His, Cys, Asp, Glu clusters) that are well-established markers of metalloenzyme active sites across many protein families. This is standard transferable knowledge about metallo-peptidase families and does not require memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the question asks for 'primary molecular function' and the true primary function (D-Ala-D-Ala dipeptidase/carboxypeptidase activity) is not among the choices, metal ion binding is the only option with any annotation or structural support for this protein. The other three options are clearly incompatible with the sequence. No ambiguity exists among the offered alternatives.


### Important caveats

- The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental annotation. However, the crystallographic structures (4MUR, 4MUS) showing copper and zinc complexes provide independent experimental support.
- The protein's primary catalytic function is peptidase/dipeptidase activity (EC 3.4.13.22, EC 3.4.17.-), not metal ion binding per se. Metal ion binding is an auxiliary molecular function component of its metalloenzyme mechanism. The question's phrasing 'primary molecular function' is slightly imprecise given the offered choices, but C remains the only correct option among A-D.
- The reviewed UniProt entry was first publicly released in Swiss-Prot on 2025-04-09 (entry version 132 archived); the author's source snapshot date is unknown, but the sequence matches exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 190-residue sequence lacks all hallmark motifs for options A, B, and D: no RRM/KH/arginine-rich RNA-binding domains (eliminating A), no ATPase-inhibitor fold (eliminating B), and no kinase signature motifs such as the HRD catalytic loop, DFG motif, glycine-rich ATP-binding loop, or cAMP-binding domain (eliminating D). In contrast, the sequence contains multiple metal-coordinating residue clusters in spatially suggestive arrangements: 'CPHF' (Cys-Pro-His-Phe), 'WHFRY' (Trp-His-Phe-Arg-Tyr), 'EDDDL' (Glu-Asp-Asp-Asp-Leu), and 'SDHD' (Ser-Asp-His-Asp). These patterns—His, Cys, Asp, Glu residues in proximity—are the canonical signature of metalloenzyme active sites found across many peptidase families (e.g., zinc-dependent metallo-peptidases). Knowledge from other metallo-peptidases (VanX homologs, carboxypeptidases, aminopeptidases) establishes that such residue arrangements indicate metal ion coordination. The overall small size and compact fold further exclude ribosomal or kinase functions. Thus, transferable family-level knowledge of metalloenzyme motifs meaningfully distinguishes C from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and D by the absence of their defining structural motifs and select C based on the presence of metal-coordinating residue patterns (His, Cys, Asp, Glu clusters) that are well-established markers of metalloenzyme active sites across many protein families. This is standard transferable knowledge about metallo-peptidase families and does not require memorizing this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "C12",
      "H5",
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The protein (Q9JN36, VanXYC) is annotated with GO:0046872 (metal ion binding) in UniProt (H11, evidence code IEA:UniProtKB-KW). The X-ray crystallography reference (C12/H5, PubMed:24711382) explicitly describes complexes with copper and zinc, providing experimental confirmation of metal binding. While the protein's primary catalytic function is D-Ala-D-Ala dipeptidase/carboxypeptidase activity (EC 3.4.13.22, EC 3.4.17.-), metal ion binding is a genuine molecular function of this metalloenzyme and is the only correct option among the four offered. The other three choices (ribosomal rRNA binding, ATPase inhibitor, cAMP-dependent protein kinase) have no annotation or structural basis for this protein."
  },
  "important_caveats": [
    "The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental annotation. However, the crystallographic structures (4MUR, 4MUS) showing copper and zinc complexes provide independent experimental support.",
    "The protein's primary catalytic function is peptidase/dipeptidase activity (EC 3.4.13.22, EC 3.4.17.-), not metal ion binding per se. Metal ion binding is an auxiliary molecular function component of its metalloenzyme mechanism. The question's phrasing 'primary molecular function' is slightly imprecise given the offered choices, but C remains the only correct option among A-D.",
    "The reviewed UniProt entry was first publicly released in Swiss-Prot on 2025-04-09 (entry version 132 archived); the author's source snapshot date is unknown, but the sequence matches exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function (D-Ala-D-Ala dipeptidase/carboxypeptidase activity) is not among the choices, metal ion binding is the only option with any annotation or structural support for this protein. The other three options are clearly incompatible with the sequence. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q9JN36, VanXYC) is annotated with GO:0046872 (metal ion binding) in UniProt (H11, evidence code IEA:UniProtKB-KW). The X-ray crystallography reference (C12/H5, PubMed:24711382) explicitly describes complexes with copper and zinc, providing experimental confirmation of metal binding. While the protein's primary catalytic function is D-Ala-D-Ala dipeptidase/carboxypeptidase activity (EC 3.4.13.22, EC 3.4.17.-), metal ion binding is a genuine molecular function of this metalloenzyme and is the only correct option among the four offered. The other three choices (ribosomal rRNA binding, ATPase inhibitor, cAMP-dependent protein kinase) have no annotation or structural basis for this protein.",
    "evidence_ids": ["H11", "C12", "H5", "C5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 190-residue sequence lacks all hallmark motifs for options A, B, and D: no RRM/KH/arginine-rich RNA-binding domains (eliminating A), no ATPase-inhibitor fold (eliminating B), and no kinase signature motifs such as the HRD catalytic loop, DFG motif, glycine-rich ATP-binding loop, or cAMP-binding domain (eliminating D). In contrast, the sequence contains multiple metal-coordinating residue clusters in spatially suggestive arrangements: 'CPHF' (Cys-Pro-His-Phe), 'WHFRY' (Trp-His-Phe-Arg-Tyr), 'EDDDL' (Glu-Asp-Asp-Asp-Leu), and 'SDHD' (Ser-Asp-His-Asp). These patterns—His, Cys, Asp, Glu residues in proximity—are the canonical signature of metalloenzyme active sites found across many peptidase families (e.g., zinc-dependent metallo-peptidases). Knowledge from other metallo-peptidases (VanX homologs, carboxypeptidases, aminopeptidases) establishes that such residue arrangements indicate metal ion coordination. The overall small size and compact fold further exclude ribosomal or kinase functions. Thus, transferable family-level knowledge of metalloenzyme motifs meaningfully distinguishes C from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and D by the absence of their defining structural motifs and select C based on the presence of metal-coordinating residue patterns (His, Cys, Asp, Glu clusters) that are well-established markers of metalloenzyme active sites across many protein families. This is standard transferable knowledge about metallo-peptidase families and does not require memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the question asks for 'primary molecular function' and the true primary function (D-Ala-D-Ala dipeptidase/carboxypeptidase activity) is not among the choices, metal ion binding is the only option with any annotation or structural support for this protein. The other three options are clearly incompatible with the sequence. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The GO annotation for metal ion binding (GO:0046872) carries evidence code IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental annotation. However, the crystallographic structures (4MUR, 4MUS) showing copper and zinc complexes provide independent experimental support.",
    "The protein's primary catalytic function is peptidase/dipeptidase activity (EC 3.4.13.22, EC 3.4.17.-), not metal ion binding per se. Metal ion binding is an auxiliary molecular function component of its metalloenzyme mechanism. The question's phrasing 'primary molecular function' is slightly imprecise given the offered choices, but C remains the only correct option among A-D.",
    "The reviewed UniProt entry was first publicly released in Swiss-Prot on 2025-04-09 (entry version 132 archived); the author's source snapshot date is unknown, but the sequence matches exactly."
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
  "benchmark_sequence_length": 190,
  "benchmark_sequence_sha256": "e03b1baec55fa6e3eef610e4058949e13d7355a383dd8c8b4a8bb29f277437fb",
  "current_entry_audit": {
    "entryVersion": 134,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 190,
  "current_source_sequence_sha256": "e03b1baec55fa6e3eef610e4058949e13d7355a383dd8c8b4a8bb29f277437fb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 132,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9JN36",
  "selected_historical_entry_version": 132,
  "selected_historical_record_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "selected_historical_source_sequence_length": 190,
  "selected_historical_source_sequence_sha256": "e03b1baec55fa6e3eef610e4058949e13d7355a383dd8c8b4a8bb29f277437fb",
  "selected_historical_version": {
    "accession": "Q9JN36",
    "database": "Swiss-Prot",
    "entryVersion": 132,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VANXY_ENTGA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9JN36\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":134,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Lactobacillales\",\"Enterococcaceae\",\"Enterococcus\"],\"scientificName\":\"Enterococcus gallinarum\",\"taxonId\":1353}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAY67969.1\",\"source\":\"EMBL\"}],\"value\":\"D,D-dipeptidase/D,D-carboxypeptidase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"MDT2689680.1\",\"source\":\"EMBL\"}],\"value\":\"D-Ala-D-Ala dipeptidase/D-Ala-D-Ala carboxypeptidase VanXY-C\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Vancomycin C-type resistance protein VanXYC\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"value\":\"3.4.13.22\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"value\":\"3.4.17.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10564477\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional D-Ala-D-Ala dipeptidase and D-Ala-D-Ala carboxypeptidase VanXYC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15728903\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional enzyme, exhibiting dipeptidase and carboxypeptidase activities (PubMed:10564477, PubMed:10817725, PubMed:24711382). Catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide (PubMed:10564477, PubMed:10817725, PubMed:24711382). Cleaves the C-terminal D-alanine residue of UDP-muramyl-pentapeptide[Ala] (UDP-MurNAc-L-Ala-D-Glu-L-Lys-D-Ala-D-Ala) (PubMed:10564477, PubMed:10817725, PubMed:24711382). Shows no activity against the pentapeptide with a C-terminal D-serine residue (PubMed:10564477). Together with VanC/VanC1 and VanT, required for vancomycin resistance in E.gallinarum strain BM4174 (PubMed:10817725, PubMed:15728903)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.13.22\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"name\":\"D-alanyl-D-alanine + H2O = 2 D-alanine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20661\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57416\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57822\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanyl-D-alanine + H2O = UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanine + D-alanine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83151\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57416\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:70758\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232760\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10564477\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10817725\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24711382\",\"source\":\"PubMed\"}],\"id\":\"GO:0160237\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:D-Ala-D-Ala dipeptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Reynolds P.E.\",\"Arias C.A.\",\"Courvalin P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10564477\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.1999.01604.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"341\",\"id\":\"10564477\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"349\",\"publicationDate\":\"1999\",\"title\":\"Gene vanXYC encodes D,D -dipeptidase (VanX) and D,D-carboxypeptidase (VanY) activities in vancomycin-resistant Enterococcus gallinarum BM4174.\",\"volume\":\"34\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"BM4174\"}],\"referenceNumber\":4,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Arias C.A.\",\"Courvalin P.\",\"Reynolds P.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10817725\"},{\"database\":\"DOI\",\"id\":\"10.1128/aac.44.6.1660-1666.2000\"}],\"citationType\":\"journal article\",\"firstPage\":\"1660\",\"id\":\"10817725\",\"journal\":\"Antimicrob. Agents Chemother.\",\"lastPage\":\"1666\",\"publicationDate\":\"2000\",\"title\":\"vanC cluster of vancomycin-resistant Enterococcus gallinarum BM4174.\",\"volume\":\"44\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF61331.1\",\"source\":\"EMBL\"}],\"type\":\"STRAIN\",\"value\":\"BM4174\"}],\"referenceNumber\":5,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Panesso D.\",\"Abadia-Patino L.\",\"Vanegas N.\",\"Reynolds P.E.\",\"Courvalin P.\",\"Arias C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15728903\"},{\"database\":\"DOI\",\"id\":\"10.1128/aac.49.3.1060-1066.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"1060\",\"id\":\"15728903\",\"journal\":\"Antimicrob. Agents Chemother.\",\"lastPage\":\"1066\",\"publicationDate\":\"2005\",\"title\":\"Transcriptional analysis of the vanC cluster from Enterococcus gallinarum strains with constitutive and inducible vancomycin resistance.\",\"volume\":\"49\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":12,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/11",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9JN36.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Meziane-Cherif D.\",\"Stogios P.J.\",\"Evdokimova E.\",\"Savchenko A.\",\"Courvalin P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24711382\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1402259111\"}],\"citationType\":\"journal article\",\"firstPage\":\"5872\",\"id\":\"24711382\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"5877\",\"publicationDate\":\"2014\",\"title\":\"Structural basis for the evolution of vancomycin resistance D,D-peptidases.\",\"volume\":\"111\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4MUR\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4MUS\",\"source\":\"PDB\"}],\"referenceNumber\":13,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) OF MUTANT SER-59 IN APO AND TRANSITION STATE ANALOG-BOUND FORMS IN COMPLEXES WITH COPPER AND ZINC AND IN COMPLEXES WITH D-ALA-D-ALA SUBSTRATE AND D-ALA PRODUCT IN COMPLEXES WITH COPPER AND ZINC\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"DISULFIDE BONDS\",\"MUTAGENESIS OF ASP-59 AND GLU-153\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/12",
  "retrieved_utc": "2026-11-02T04:32:55.055252+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c61428d8d87b7848c5beb0e3f3cbbe7bc3193337dc796d693a84387124a2b69f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9JN36.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H1",
  "excerpt": "ID   VANXY_ENTGA             Reviewed;         190 AA.\nAC   Q9JN36;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 132.\nDE   RecName: Full=Bifunctional D-Ala-D-Ala dipeptidase and D-Ala-D-Ala carboxypeptidase VanXYC {ECO:0000303|PubMed:10564477};\nDE            EC=3.4.13.22 {ECO:0000269|PubMed:10564477, ECO:0000269|PubMed:10817725, ECO:0000269|PubMed:24711382};\nDE            EC=3.4.17.- {ECO:0000269|PubMed:10564477, ECO:0000269|PubMed:10817725, ECO:0000269|PubMed:24711382};\nDE   AltName: Full=D,D-dipeptidase/D,D-carboxypeptidase {ECO:0000303|PubMed:10564477, ECO:0000312|EMBL:AAF61331.1, ECO:0000312|EMBL:AAY67969.1};\nDE   AltName: Full=D-Ala-D-Ala dipeptidase/D-Ala-D-Ala carboxypeptidase VanXY-C {ECO:0000312|EMBL:MDT2689680.1};\nDE   AltName: Full=Vancomycin C-type resistance protein VanXYC {ECO:0000305};\nGN   Name=vanXYC {ECO:0000303|PubMed:10564477, ECO:0000312|EMBL:AAF61331.1};\nGN   ORFNames=EGM181_06555 {ECO:0000312|EMBL:QOG26925.1},\nGN   GTI89_02115 {ECO:0000312|EMBL:MXS24888.1},\nGN   HZY99_04425 {ECO:0000312|EMBL:NYS81410.1},\nGN   NCTC12360_01404 {ECO:0000312|EMBL:STD82963.1},\nGN   P7E30_05555 {ECO:0000312|EMBL:MDT2689680.1};\nOS   Enterococcus gallinarum.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae;\nOC   Enterococcus.\nOX   NCBI_TaxID=1353 {ECO:0000312|EMBL:AAF61331.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000312|EMBL:AAF61331.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   SUBCELLULAR LOCATION.\nRC   STRAIN=BM4174 {ECO:0000312|EMBL:AAF61331.1};\nRX   PubMed=10564477; DOI=10.1046/j.1365-2958.1999.01604.x;\nRA   Reynolds P.E., Arias C.A., Courvalin P.;\nRT   \"Gene vanXYC encodes D,D -dipeptidase (VanX) and D,D-carboxypeptidase\nRT   (VanY) activities in vancomycin-resistant Enterococcus gallinarum BM4174.\";\nRL   Mol. Microbiol. 34:341-349(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000312|EMBL:AAF61331.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   INDUCTION.\nRC   STRAIN=BM4174 {ECO:0000312|EMBL:AAF61331.1};\nRX   PubMed=10817725; DOI=10.1128/aac.44.6.1660-1666.2000;\nRA   Arias C.A., Courvalin P., Reynolds P.E.;\nRT   \"vanC cluster of vancomycin-resistant Enterococcus gallinarum BM4174.\";\nRL   Antimicrob. Agents Chemother. 44:1660-1666(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H4",
  "excerpt": "RN   [12] {ECO:0000305}\nRP   FUNCTION, AND INDUCTION.\nRX   PubMed=15728903; DOI=10.1128/aac.49.3.1060-1066.2005;\nRA   Panesso D., Abadia-Patino L., Vanegas N., Reynolds P.E., Courvalin P.,\nRA   Arias C.A.;\nRT   \"Transcriptional analysis of the vanC cluster from Enterococcus gallinarum\nRT   strains with constitutive and inducible vancomycin resistance.\";\nRL   Antimicrob. Agents Chemother. 49:1060-1066(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H5",
  "excerpt": "RN   [13] {ECO:0007744|PDB:4MUR, ECO:0007744|PDB:4MUS}\nRP   X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) OF MUTANT SER-59 IN APO AND\nRP   TRANSITION STATE ANALOG-BOUND FORMS IN COMPLEXES WITH COPPER AND ZINC AND\nRP   IN COMPLEXES WITH D-ALA-D-ALA SUBSTRATE AND D-ALA PRODUCT IN COMPLEXES WITH\nRP   COPPER AND ZINC, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, DISULFIDE BONDS, AND MUTAGENESIS OF ASP-59 AND\nRP   GLU-153.\nRX   PubMed=24711382; DOI=10.1073/pnas.1402259111;\nRA   Meziane-Cherif D., Stogios P.J., Evdokimova E., Savchenko A., Courvalin P.;\nRT   \"Structural basis for the evolution of vancomycin resistance D,D-\nRT   peptidases.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 111:5872-5877(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Bifunctional enzyme, exhibiting dipeptidase and\nCC       carboxypeptidase activities (PubMed:10564477, PubMed:10817725,\nCC       PubMed:24711382). Catalyzes hydrolysis of the D-alanyl-D-alanine\nCC       dipeptide (PubMed:10564477, PubMed:10817725, PubMed:24711382). Cleaves\nCC       the C-terminal D-alanine residue of UDP-muramyl-pentapeptide[Ala] (UDP-\nCC       MurNAc-L-Ala-D-Glu-L-Lys-D-Ala-D-Ala) (PubMed:10564477,\nCC       PubMed:10817725, PubMed:24711382). Shows no activity against the\nCC       pentapeptide with a C-terminal D-serine residue (PubMed:10564477).\nCC       Together with VanC/VanC1 and VanT, required for vancomycin resistance\nCC       in E.gallinarum strain BM4174 (PubMed:10817725, PubMed:15728903).\nCC       {ECO:0000269|PubMed:10564477, ECO:0000269|PubMed:10817725,\nCC       ECO:0000269|PubMed:15728903, ECO:0000269|PubMed:24711382}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-alanyl-D-alanine + H2O = 2 D-alanine; Xref=Rhea:RHEA:20661,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:57416, ChEBI:CHEBI:57822;\nCC         EC=3.4.13.22; Evidence={ECO:0000269|PubMed:10564477,\nCC         ECO:0000269|PubMed:10817725, ECO:0000269|PubMed:24711382};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-L-\nCC         lysyl-D-alanyl-D-alanine + H2O = UDP-N-acetyl-alpha-D-muramoyl-L-\nCC         alanyl-gamma-D-glutamyl-L-lysyl-D-alanine + D-alanine;\nCC         Xref=Rhea:RHEA:83151, ChEBI:CHEBI:15377, ChEBI:CHEBI:57416,\nCC         ChEBI:CHEBI:70758, ChEBI:CHEBI:232760;\nCC         Evidence={ECO:0000269|PubMed:10564477, ECO:0000269|PubMed:10817725,\nCC         ECO:0000269|PubMed:24711382};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0004180; F:carboxypeptidase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0160237; F:D-Ala-D-Ala dipeptidase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-198",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H11",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:57.968809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 199-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7f772f88beb38cb0e2fc5f48e850e31133a58143b4864f5e0a26c3e6e5747e41",
  "url": "https://rest.uniprot.org/unisave/Q9JN36?format=txt&versions=132"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004691\nname: cAMP-dependent protein kinase activity\nnamespace: molecular_function\nalt_id: GO:0008602\ndef: \"cAMP-dependent catalysis of the reaction: ATP + a protein = ADP + a phosphoprotein.\" [PMID:32935175, PMID:35053423, PMID:35805104]\ncomment: This reaction requires the presence of cAMP.\nsynonym: \"3',5' cAMP-dependent protein kinase activity\" EXACT []\nsynonym: \"3',5'-cAMP-dependent protein kinase activity\" EXACT []\nsynonym: \"adenosine 3',5'-cyclophosphate-dependent protein kinase activity\" EXACT []\nsynonym: \"AMPK\" RELATED [EC:2.7.11.11]\nsynonym: \"ATP:protein phosphotransferase (cAMP-dependent) activity\" RELATED [EC:2.7.11.11]\nsynonym: \"cAMP-dependent protein kinase, intrinsic catalyst activity\" EXACT []\nsynonym: \"cyclic AMP-dependent protein kinase activity\" EXACT []\nsynonym: \"PKA\" RELATED [EC:2.7.11.11]\nsynonym: \"PKA C\" RELATED [EC:2.7.11.11]\nsynonym: \"protein kinase A activity\" BROAD [EC:2.7.11.11]\nsynonym: \"STK22\" RELATED [EC:2.7.11.11]\nxref: EC:2.7.11.11\nxref: Reactome:R-HSA-163672 \"Phosphorylation of ChREBP at Thr(653) by PKA\"\nxref: Reactome:R-HSA-163676 \"Phosphorylation of pChREBP (Thr 653) at Ser(196) by PKA\"\nxref: Reactome:R-HSA-163773 \"PKA tetramer:cAMP phosphorylates PF2K-Pase\"\nxref: Reactome:R-HSA-177275 \"PKA phosphorylates DARPP-32 on Thr34\"\nxref: Reactome:R-HSA-177284 \"PKA phosphorylates PDE4B\"\nxref: Reactome:R-HSA-432232 \"Phosphorylation of Aquaporin-2 by Protein Kinase A (PKA)\"\nxref: Reactome:R-HSA-5610717 \"PKA phosphorylates GLI2\"\nxref: Reactome:R-HSA-5610720 \"PKA phosphorylates GLI3\"\nxref: Reactome:R-HSA-5610741 \"PKA phosphorylates GLI1\"\nxref: Reactome:R-HSA-5617179 \"PRKACA phosphorylates TNNI3\"\nxref: Reactome:R-HSA-5617182 \"PRKACA phosphorylates PLN\"\nxref: Reactome:R-HSA-5687088 \"PKA phosphorylates MAPKAPK5\"\nxref: Reactome:R-HSA-913451 \"IL3RB is phosphorylated on Ser-585\"\nxref: Reactome:R-HSA-9838321 \"PRKACA phosphorylates TFAM in the mitochondrial matrix\"\nxref: Reactome:R-HSA-9861318 \"PKA phosphorylates NOS3 (eNOS) on serine-633\"\nis_a: GO:0004690 ! cyclic nucleotide-dependent protein kinase activity\nproperty_value: skos:exactMatch EC:2.7.11.11\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004691",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 47506-47542",
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
  "excerpt": "[Term]\nid: GO:0042030\nname: ATPase inhibitor activity\nnamespace: molecular_function\ndef: \"Binds to and stops, prevents or reduces an ATP hydrolysis activity.\" [GOC:jl]\nsynonym: \"adenosinetriphosphatase inhibitor\" EXACT []\nis_a: GO:0140678 ! molecular function inhibitor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042030",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 233725-233732",
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
  "excerpt": "[Term]\nid: GO:0046872\nname: metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a metal ion.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsynonym: \"heavy metal binding\" NARROW []\nsynonym: \"metal binding\" EXACT []\nis_a: GO:0043169 ! cation binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046872",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281280-281292",
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
  "excerpt": "[Term]\nid: GO:0070180\nname: large ribosomal subunit rRNA binding\nnamespace: molecular_function\ndef: \"Binding to large ribosomal subunit RNA (LSU rRNA), a constituent of the large ribosomal subunit. In S. cerevisiae, this is the 25S rRNA.\" [GOC:elh]\nsynonym: \"25S rRNA binding\" EXACT [GOC:elh]\nsynonym: \"LSU rRNA binding\" EXACT []\nis_a: GO:0019843 ! rRNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070180",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 364950-364958",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
