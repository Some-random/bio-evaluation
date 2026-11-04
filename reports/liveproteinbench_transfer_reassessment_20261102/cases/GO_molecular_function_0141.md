# GO_molecular_function_0141

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0141.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — heparan sulfate 2-sulfotransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQKLEESRAKLERAIARHEVREIEQRHTMDGPRQDAAVDEEEDIVIIYNRVPKTASTSFTNIAYDLCAKNRYHVLHINTTKNNPVMSLQDQVRFVKNITTWNEMKPGFYHGHISYLDFAKFGVKKKPIYINVIRDPIERLVSYYYFLRFGDDYRPGLRRRKQGDKKTFDECVAEGGSDCAPEKLWLQIPFFCGHSSECWNVGSRWAMDQAKYNLINEYFLVGVTEELEDFIMLLEAALPRFFRGATDLYRTGKKSHLRKTTEKKLPTKQTIAKLQQSDIWKMENEFYEFALEQFQFIRAHAVREKDGDLYILAQNFFYEKIYPKSN

[Multiple Choices]
A. nucleotide binding
B. RNA binding
C. heparan sulfate 2-sulfotransferase activity
D. nucleotidyltransferase activity
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

> The supplied sequence matches the UniProt sequence annotated as heparan sulfate 2-sulfotransferase, and the record assigns this activity with IDA evidence linked to a PubMed study. Its function description specifies transfer of a sulfo group to heparan sulfate. This supports choice C, while retaining the source’s evidence qualifications.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a short N-terminal hydrophobic membrane anchor followed by a large catalytic domain, a pattern consistent with Golgi-lumen glycosaminoglycan-modifying enzymes. Transferable knowledge of Golgi sulfotransferases and their PAPS-dependent catalytic domains makes a sulfotransferase activity a credible inference, distinguishing C from RNA binding and nucleotidyltransferase activity. Nucleotide binding is a less specific alternative: PAPS-dependent enzymes can bind a nucleotide-containing cofactor, but that does not make nucleotide binding their best primary activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture and family-level functional pattern provide a meaningful basis for choosing the specific sulfotransferase option without needing the target’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> PAPS binding may accompany the catalytic activity, but the question asks for the best description of primary molecular function; the specific sulfotransferase activity is more informative than generic nucleotide binding.


### Important caveats

- The sequence pattern supports a family-level inference, not independent experimental confirmation of the exact substrate or regioselectivity.
- The reviewer-only record supports the key, but its sequence match and evidence codes do not establish that every cited experiment tested this exact species’ protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a short N-terminal hydrophobic membrane anchor followed by a large catalytic domain, a pattern consistent with Golgi-lumen glycosaminoglycan-modifying enzymes. Transferable knowledge of Golgi sulfotransferases and their PAPS-dependent catalytic domains makes a sulfotransferase activity a credible inference, distinguishing C from RNA binding and nucleotidyltransferase activity. Nucleotide binding is a less specific alternative: PAPS-dependent enzymes can bind a nucleotide-containing cofactor, but that does not make nucleotide binding their best primary activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and family-level functional pattern provide a meaningful basis for choosing the specific sulfotransferase option without needing the target’s database record."
  },
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence annotated as heparan sulfate 2-sulfotransferase, and the record assigns this activity with IDA evidence linked to a PubMed study. Its function description specifies transfer of a sulfo group to heparan sulfate. This supports choice C, while retaining the source’s evidence qualifications."
  },
  "important_caveats": [
    "The sequence pattern supports a family-level inference, not independent experimental confirmation of the exact substrate or regioselectivity.",
    "The reviewer-only record supports the key, but its sequence match and evidence codes do not establish that every cited experiment tested this exact species’ protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PAPS binding may accompany the catalytic activity, but the question asks for the best description of primary molecular function; the specific sulfotransferase activity is more informative than generic nucleotide binding."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence annotated as heparan sulfate 2-sulfotransferase, and the record assigns this activity with IDA evidence linked to a PubMed study. Its function description specifies transfer of a sulfo group to heparan sulfate. This supports choice C, while retaining the source’s evidence qualifications.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a short N-terminal hydrophobic membrane anchor followed by a large catalytic domain, a pattern consistent with Golgi-lumen glycosaminoglycan-modifying enzymes. Transferable knowledge of Golgi sulfotransferases and their PAPS-dependent catalytic domains makes a sulfotransferase activity a credible inference, distinguishing C from RNA binding and nucleotidyltransferase activity. Nucleotide binding is a less specific alternative: PAPS-dependent enzymes can bind a nucleotide-containing cofactor, but that does not make nucleotide binding their best primary activity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture and family-level functional pattern provide a meaningful basis for choosing the specific sulfotransferase option without needing the target’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "PAPS binding may accompany the catalytic activity, but the question asks for the best description of primary molecular function; the specific sulfotransferase activity is more informative than generic nucleotide binding."
  },
  "important_caveats": [
    "The sequence pattern supports a family-level inference, not independent experimental confirmation of the exact substrate or regioselectivity.",
    "The reviewer-only record supports the key, but its sequence match and evidence codes do not establish that every cited experiment tested this exact species’ protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR) is annotated with GO:0004394 'heparan sulfate 2-sulfotransferase activity' with IDA evidence from PubMed:17227754 (Xu et al., JBC 2007, mutational study of HS2ST). The function comment confirms catalysis of sulfo group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate. The sequence matches the benchmark input (356 aa, identical SHA256).

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits features consistent with a Golgi-resident carbohydrate sulfotransferase: (1) an N-terminal hydrophobic stretch (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQK) characteristic of a type II membrane anchor, which is the hallmark topology of the carbohydrate sulfotransferase (CBST) family; (2) a ~350-aa catalytic domain downstream of the TM segment, matching the typical architecture of CBSTs such as HS2ST1, HS6ST, HS3ST, and CHST members. Among the four offered choices, only C is a sulfotransferase catalytic activity. Option B (RNA binding) is excluded by the absence of RRM, KH, or other nucleic-acid-binding motifs. Option D (nucleotidyltransferase, EC 2.7.7) is a different transferase subclass that catalyzes nucleotidyl-group transfer, inconsistent with the sulfotransferase fold and the absence of nucleotidyltransferase motifs. Option A (nucleotide binding) is a general binding term; while sulfotransferases do bind PAPS (a nucleotide derivative), the question asks for the 'primary molecular function' or 'fundamental activity' of the protein, which for an enzyme is its catalytic reaction, not co-substrate binding. GO:0050656 (PAPS binding) is an ancestor of the catalytic term via is_a paths, confirming that nucleotide binding is a subordinate annotation. Thus, recognizing the protein as a member of the sulfotransferase superfamily from its type II topology, length, and overall sequence composition, and noting that C is the sole sulfotransferase option, meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition of the sulfotransferase superfamily from the type II membrane topology, ~350-aa catalytic domain length, and general sequence composition is a transferable inference learned from other CBST homologs. Among the four choices, only C represents a sulfotransferase catalytic activity, so family-level identification suffices to select C without needing to distinguish 2-O from 6-O specificity. The other options are excluded by the absence of RNA-binding domains (B), the wrong EC class (D), and the distinction between catalytic vs. binding function (A vs. C).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (nucleotide binding) could be loosely argued because sulfotransferases bind PAPS, but the question explicitly asks for the 'primary molecular function' or 'fundamental activity,' which for an enzyme is its catalytic reaction. GO ontology places PAPS binding as an is_a descendant of nucleotide binding, making it a subordinate annotation. C is the most specific and primary catalytic function. B and D are clearly inconsistent with the sequence architecture.


### Important caveats

- Distinguishing HS2ST1 specifically from other CBST family members (HS6ST, HS3ST, CHST) from sequence alone would require detailed residue-level knowledge; however, only one sulfotransferase option is offered, so family-level recognition is sufficient.
- The sulfotransferase superfamily lacks a single short, universally recognized sequence motif analogous to the Walker A/B or kinase glycine-rich loop; recognition relies more on topology, domain architecture, and learned statistical patterns from related proteins.
- The UniProt annotation for this Chinese hamster entry is largely transferred by similarity (ECO:0000250) from the human/rat orthologs, with experimental IDA evidence from the 2007 mutational study on the mouse/rat protein (PubMed:17227754).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits features consistent with a Golgi-resident carbohydrate sulfotransferase: (1) an N-terminal hydrophobic stretch (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQK) characteristic of a type II membrane anchor, which is the hallmark topology of the carbohydrate sulfotransferase (CBST) family; (2) a ~350-aa catalytic domain downstream of the TM segment, matching the typical architecture of CBSTs such as HS2ST1, HS6ST, HS3ST, and CHST members. Among the four offered choices, only C is a sulfotransferase catalytic activity. Option B (RNA binding) is excluded by the absence of RRM, KH, or other nucleic-acid-binding motifs. Option D (nucleotidyltransferase, EC 2.7.7) is a different transferase subclass that catalyzes nucleotidyl-group transfer, inconsistent with the sulfotransferase fold and the absence of nucleotidyltransferase motifs. Option A (nucleotide binding) is a general binding term; while sulfotransferases do bind PAPS (a nucleotide derivative), the question asks for the 'primary molecular function' or 'fundamental activity' of the protein, which for an enzyme is its catalytic reaction, not co-substrate binding. GO:0050656 (PAPS binding) is an ancestor of the catalytic term via is_a paths, confirming that nucleotide binding is a subordinate annotation. Thus, recognizing the protein as a member of the sulfotransferase superfamily from its type II topology, length, and overall sequence composition, and noting that C is the sole sulfotransferase option, meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the sulfotransferase superfamily from the type II membrane topology, ~350-aa catalytic domain length, and general sequence composition is a transferable inference learned from other CBST homologs. Among the four choices, only C represents a sulfotransferase catalytic activity, so family-level identification suffices to select C without needing to distinguish 2-O from 6-O specificity. The other options are excluded by the absence of RNA-binding domains (B), the wrong EC class (D), and the distinction between catalytic vs. binding function (A vs. C)."
  },
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "C8",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR) is annotated with GO:0004394 'heparan sulfate 2-sulfotransferase activity' with IDA evidence from PubMed:17227754 (Xu et al., JBC 2007, mutational study of HS2ST). The function comment confirms catalysis of sulfo group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate. The sequence matches the benchmark input (356 aa, identical SHA256)."
  },
  "important_caveats": [
    "Distinguishing HS2ST1 specifically from other CBST family members (HS6ST, HS3ST, CHST) from sequence alone would require detailed residue-level knowledge; however, only one sulfotransferase option is offered, so family-level recognition is sufficient.",
    "The sulfotransferase superfamily lacks a single short, universally recognized sequence motif analogous to the Walker A/B or kinase glycine-rich loop; recognition relies more on topology, domain architecture, and learned statistical patterns from related proteins.",
    "The UniProt annotation for this Chinese hamster entry is largely transferred by similarity (ECO:0000250) from the human/rat orthologs, with experimental IDA evidence from the 2007 mutational study on the mouse/rat protein (PubMed:17227754)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (nucleotide binding) could be loosely argued because sulfotransferases bind PAPS, but the question explicitly asks for the 'primary molecular function' or 'fundamental activity,' which for an enzyme is its catalytic reaction. GO ontology places PAPS binding as an is_a descendant of nucleotide binding, making it a subordinate annotation. C is the most specific and primary catalytic function. B and D are clearly inconsistent with the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A8C2LVE3 (HS2ST_CRIGR) is annotated with GO:0004394 'heparan sulfate 2-sulfotransferase activity' with IDA evidence from PubMed:17227754 (Xu et al., JBC 2007, mutational study of HS2ST). The function comment confirms catalysis of sulfo group transfer from PAPS to the 2-OH of IdoA/GlcA in heparan sulfate. The sequence matches the benchmark input (356 aa, identical SHA256).",
    "evidence_ids": ["C7", "C5", "C8", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits features consistent with a Golgi-resident carbohydrate sulfotransferase: (1) an N-terminal hydrophobic stretch (MGLLRIMMPPKLQLLAVVAFAVAMLFLENQIQK) characteristic of a type II membrane anchor, which is the hallmark topology of the carbohydrate sulfotransferase (CBST) family; (2) a ~350-aa catalytic domain downstream of the TM segment, matching the typical architecture of CBSTs such as HS2ST1, HS6ST, HS3ST, and CHST members. Among the four offered choices, only C is a sulfotransferase catalytic activity. Option B (RNA binding) is excluded by the absence of RRM, KH, or other nucleic-acid-binding motifs. Option D (nucleotidyltransferase, EC 2.7.7) is a different transferase subclass that catalyzes nucleotidyl-group transfer, inconsistent with the sulfotransferase fold and the absence of nucleotidyltransferase motifs. Option A (nucleotide binding) is a general binding term; while sulfotransferases do bind PAPS (a nucleotide derivative), the question asks for the 'primary molecular function' or 'fundamental activity' of the protein, which for an enzyme is its catalytic reaction, not co-substrate binding. GO:0050656 (PAPS binding) is an ancestor of the catalytic term via is_a paths, confirming that nucleotide binding is a subordinate annotation. Thus, recognizing the protein as a member of the sulfotransferase superfamily from its type II topology, length, and overall sequence composition, and noting that C is the sole sulfotransferase option, meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the sulfotransferase superfamily from the type II membrane topology, ~350-aa catalytic domain length, and general sequence composition is a transferable inference learned from other CBST homologs. Among the four choices, only C represents a sulfotransferase catalytic activity, so family-level identification suffices to select C without needing to distinguish 2-O from 6-O specificity. The other options are excluded by the absence of RNA-binding domains (B), the wrong EC class (D), and the distinction between catalytic vs. binding function (A vs. C)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (nucleotide binding) could be loosely argued because sulfotransferases bind PAPS, but the question explicitly asks for the 'primary molecular function' or 'fundamental activity,' which for an enzyme is its catalytic reaction. GO ontology places PAPS binding as an is_a descendant of nucleotide binding, making it a subordinate annotation. C is the most specific and primary catalytic function. B and D are clearly inconsistent with the sequence architecture."
  },
  "important_caveats": [
    "Distinguishing HS2ST1 specifically from other CBST family members (HS6ST, HS3ST, CHST) from sequence alone would require detailed residue-level knowledge; however, only one sulfotransferase option is offered, so family-level recognition is sufficient.",
    "The sulfotransferase superfamily lacks a single short, universally recognized sequence motif analogous to the Walker A/B or kinase glycine-rich loop; recognition relies more on topology, domain architecture, and learned statistical patterns from related proteins.",
    "The UniProt annotation for this Chinese hamster entry is largely transferred by similarity (ECO:0000250) from the human/rat orthologs, with experimental IDA evidence from the 2007 mutational study on the mouse/rat protein (PubMed:17227754)."
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
  "benchmark_sequence_length": 356,
  "benchmark_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 356,
  "current_source_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8C2LVE3",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "selected_historical_source_sequence_length": 356,
  "selected_historical_source_sequence_sha256": "a438080c10ef2ba2b4b0a97657c783c3e1a5599568ecacaea65e61097d20104d",
  "selected_historical_version": {
    "accession": "A0A8C2LVE3",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HS2ST_CRIGR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8C2LVE3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP001108280\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2-O-sulfotransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2-OST\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q76KB1\",\"source\":\"UniProtKB\"}],\"value\":\"2OST\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"HS 2-O-sulfotransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"Heparan sulfate 2-sulfotransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"}],\"value\":\"2.8.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q7LGA3\",\"source\":\"UniProtKB\"}],\"value\":\"Heparan sulfate 2-O-sulfotransferase 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8R3H7\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17227754\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the transfer of a sulfo group from 3'-phospho-5'-adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or glucuronic acid (GlcA) within the heparan sulfate (HS) chain and participates in HS biosynthesis (PubMed:17227754). Required for metanephric development of kidney formation, suggesting that 2-O-sulfation within HS is essential for signaling between ureteric bud and metanephric mesenchyme (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"17227754\",\"source\":\"PubMed\"}],\"id\":\"GO:0050656\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:3'-phosphoadenosine 5'-phosphosulfate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"17227754\",\"source\":\"PubMed\"}],\"id\":\"GO:0004394\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:heparan sulfate 2-sulfotransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu D.\",\"Song D.\",\"Pedersen L.C.\",\"Liu J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17227754\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m608062200\"}],\"citationType\":\"journal article\",\"firstPage\":\"8356\",\"id\":\"17227754\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"8367\",\"publicationDate\":\"2007\",\"title\":\"Mutational study of heparan sulfate 2-O-sulfotransferase and chondroitin sulfate 2-O-sulfotransferase.\",\"volume\":\"282\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVE SITE\",\"MUTAGENESIS OF ARG-80; LYS-83; THR-84; SER-86; THR-87; HIS-140; HIS-142; ARG-164; SER-172; ARG-178; ASP-181; ARG-188; ARG-189; ARG-190; LYS-191 AND ARG-288\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:56.866768+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3ae0ae5ef516524f45ece4202b2e4a49d7ab8d354dec6f6098830001d44574",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2LVE3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   HS2ST_CRIGR             Reviewed;         356 AA.\nAC   A0A8C2LVE3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Heparan sulfate 2-O-sulfotransferase 1 {ECO:0000250|UniProtKB:Q7LGA3};\nDE            EC=2.8.2.- {ECO:0000250|UniProtKB:Q8R3H7};\nDE   AltName: Full=2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nDE            Short=2-OST {ECO:0000250|UniProtKB:Q8R3H7};\nDE            Short=2OST {ECO:0000250|UniProtKB:Q76KB1};\nDE   AltName: Full=HS 2-O-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nDE   AltName: Full=Heparan sulfate 2-sulfotransferase {ECO:0000250|UniProtKB:Q8R3H7};\nGN   Name=HS2ST1 {ECO:0000250|UniProtKB:Q7LGA3}; Synonyms=LOC100760748;\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029 {ECO:0000312|Proteomes:UP001108280};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, ACTIVE SITE,\nRP   AND MUTAGENESIS OF ARG-80; LYS-83; THR-84; SER-86; THR-87; HIS-140;\nRP   HIS-142; ARG-164; SER-172; ARG-178; ASP-181; ARG-188; ARG-189; ARG-190;\nRP   LYS-191 AND ARG-288.\nRX   PubMed=17227754; DOI=10.1074/jbc.m608062200;\nRA   Xu D., Song D., Pedersen L.C., Liu J.;\nRT   \"Mutational study of heparan sulfate 2-O-sulfotransferase and chondroitin\nRT   sulfate 2-O-sulfotransferase.\";\nRL   J. Biol. Chem. 282:8356-8367(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the transfer of a sulfo group from 3'-phospho-5'-\nCC       adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or\nCC       glucuronic acid (GlcA) within the heparan sulfate (HS) chain and\nCC       participates in HS biosynthesis (PubMed:17227754). Required for\nCC       metanephric development of kidney formation, suggesting that 2-O-\nCC       sulfation within HS is essential for signaling between ureteric bud and\nCC       metanephric mesenchyme (By similarity). {ECO:0000250|UniProtKB:Q8R3H7,\nCC       ECO:0000269|PubMed:17227754}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0050656; F:3'-phosphoadenosine 5'-phosphosulfate binding; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004394; F:heparan sulfate 2-sulfotransferase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.260576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c78db6d4bdbc3208dbc3401f5215ab34d630f3586e718f4eb0558db0f9ef4abb",
  "url": "https://rest.uniprot.org/unisave/A0A8C2LVE3?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000166\nname: nucleotide binding\nnamespace: molecular_function\ndef: \"Binding to a nucleotide, any compound consisting of a nucleoside that is esterified with (ortho)phosphate or an oligophosphate at any hydroxyl group on the ribose or deoxyribose.\" [GOC:mah, ISBN:0198547684]\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nis_a: GO:1901265 ! nucleoside phosphate binding\nis_a: GO:1901363 ! heterocyclic compound binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000166",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1671-1682",
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
  "excerpt": "[Term]\nid: GO:0003723\nname: RNA binding\nnamespace: molecular_function\nalt_id: GO:0000498\nalt_id: GO:0044822\ndef: \"Binding to an RNA molecule or a portion thereof.\" [GOC:jl, GOC:mah]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"base pairing with RNA\" NARROW []\nsynonym: \"poly(A) RNA binding\" RELATED []\nsynonym: \"poly(A)-RNA binding\" RELATED []\nsynonym: \"poly-A RNA binding\" RELATED []\nxref: Reactome:R-HSA-203922 \"Exportin-5 recognizes 3' overhang of pre-miRNA\"\nis_a: GO:0003676 ! nucleic acid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003723",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28242-28268",
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
  "excerpt": "[Term]\nid: GO:0004394\nname: heparan sulfate 2-sulfotransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 3'-phosphoadenosine 5'-phosphosulfate + heparan sulfate = adenosine 3',5'-bisphosphate + heparan sulfate 2-O-sulfate; results in 2-O-sulfation of iduronic acid residues in heparan sulfate.\" [PMID:9153262]\nsynonym: \"heparan sulfate 2-O-sulfotransferase activity\" EXACT []\nsynonym: \"heparan-sulfate 2-O-sulphotransferase activity\" EXACT []\nsynonym: \"heparin 2-sulfotransferase activity\" RELATED []\nsynonym: \"heparin-sulphate 2-sulphotransferase activity\" RELATED []\nxref: MetaCyc:RXN-11558\nxref: Reactome:R-HSA-2076508 \"HS2ST1 trimer sulfates IdoA at C2 in heparan sulfate\"\nis_a: GO:0034483 ! heparan sulfate sulfotransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004394",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 41261-41273",
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
  "excerpt": "[Term]\nid: GO:0016779\nname: nucleotidyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a nucleotidyl group from one compound (donor) to another (acceptor).\" [EC:2.7.7.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_metagenomics\nsubset: goslim_yeast\nxref: EC:2.7.7.-\nxref: Reactome:R-HSA-6782434 \"THG1L transfers GMP to 5' end of tRNA(His)\"\nis_a: GO:0016772 ! transferase activity, transferring phosphorus-containing groups\nproperty_value: skos:exactMatch EC:2.7.7.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016779",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130076-130090",
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
  "excerpt": "[Term]\nid: GO:0017076\nname: purine nucleotide binding\nnamespace: molecular_function\ndef: \"Binding to a purine nucleotide, a compound consisting of a purine nucleoside esterified with (ortho)phosphate.\" [GOC:ai]\nis_a: GO:0000166 ! nucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0017076",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 133091-133097",
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
  "excerpt": "[Term]\nid: GO:0030554\nname: adenyl nucleotide binding\nnamespace: molecular_function\ndef: \"Binding to an adenyl nucleotide, an adenosine esterified with (ortho)phosphate.\" [ISBN:0198506732]\nsubset: goslim_chembl\nis_a: GO:0017076 ! purine nucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030554",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 167202-167209",
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
  "excerpt": "[Term]\nid: GO:0032559\nname: adenyl ribonucleotide binding\nnamespace: molecular_function\ndef: \"Binding to an adenyl ribonucleotide, any compound consisting of adenosine esterified with (ortho)phosphate or an oligophosphate at any hydroxyl group on the ribose moiety.\" [GOC:mah]\nis_a: GO:0030554 ! adenyl nucleotide binding\nis_a: GO:0032555 ! purine ribonucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032559",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 187354-187361",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO8",
  "excerpt": "[Term]\nid: GO:0050656\nname: 3'-phosphoadenosine 5'-phosphosulfate binding\nnamespace: molecular_function\ndef: \"Binding to 3'-phosphoadenosine 5'-phosphosulfate (PAPS), a naturally occurring mixed anhydride. It is an intermediate in the formation of a variety of sulfo compounds in biological systems.\" [GOC:ai]\nsynonym: \"3'-phosphoadenosine 5'-phosphosulphate binding\" EXACT []\nsynonym: \"3'-phosphoadenylyl-sulfate binding\" EXACT []\nsynonym: \"adenosine 3'-phosphate 5'-phosphosulfate binding\" EXACT []\nsynonym: \"PAPS binding\" EXACT []\nsynonym: \"phosphoadenosine phosphosulfate binding\" EXACT []\nis_a: GO:0032559 ! adenyl ribonucleotide binding\nis_a: GO:0043168 ! anion binding\nis_a: GO:1901681 ! sulfur compound binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050656",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318338-318351",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
