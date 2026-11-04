# catalytic_activity_0044

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0044.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVGKSTLLSVLASASVAFAACSLDSHCPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCESASYTFTSMDGITSNTKYLGDASKSNWVYSGSPVIYNDNVLLTMSANSVGTVMASSTYMWYGNVKAKFKTSRGQGVITAFILFSDVKDEIDYEFVGSELTTAQSNYYFQGITNYDNELNITLSDTYANYHEYEIDWTPDEITWLVDGQVGRTKKRADTWNATANQWNFPQTPARVQLSLWPGGLASNGAGTIAWAGGEIDWNSEDIQNNGYYYAAFESVDISCYNAKSAPGTNSGKSYYYNSVLGTNNTVIDSKNATILSSLLATGTNMTAGESAAASGSTAASTAATVPGLTGSGGGGVGDNHSDDGSSSSDSSSGSATSSSSGSSSTGSSGFSQGDGSTSTSKSSADSLVANQERVLKGSLFAGIVAVVAMMAL

[Multiple Choices]
A. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
B. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
C. L-isoleucyl-tRNA(Ile) + acetyl-CoA = N-acetyl-L-isoleucyl-tRNA(Ile) + CoA + H(+)
D. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The matched-sequence UniProt annotation assigns EC 3.2.1.14 and the reaction in option A. However, the annotation is transferred by similarity from Q8J0P4, so it supports the key as a computationally inferred annotation, not as direct experimental confirmation for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like hydrophobic region, a cysteine-rich extracellular-looking region, and a C-terminal membrane-anchor-like segment. That architecture is more consistent with a secreted or cell-surface carbohydrate-active protein than with the cytosolic tRNA/protein acylation reactions in B and C or the ferredoxin-dependent carotenoid reaction in D. Among these choices, A is the plausible polysaccharide-hydrolysis reaction. This is a family-level and architectural inference, not proof of the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about secretory and membrane-associated protein architecture meaningfully separates A from the offered alternatives without needing the exact protein's recorded annotation. The exact chitinase activity is less secure from sequence architecture alone, but the alternatives make the qualitative distinction meaningful.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and no other option is comparably supported by the sequence architecture.


### Important caveats

- The supplied reviewer evidence indicates that the chitinase annotation was transferred from a homolog; it does not establish direct experimental measurement of this protein's activity.
- The sequence may support a broader carbohydrate-remodeling role, but the precise reaction and substrate specificity are not established by the sequence architecture alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region, a cysteine-rich extracellular-looking region, and a C-terminal membrane-anchor-like segment. That architecture is more consistent with a secreted or cell-surface carbohydrate-active protein than with the cytosolic tRNA/protein acylation reactions in B and C or the ferredoxin-dependent carotenoid reaction in D. Among these choices, A is the plausible polysaccharide-hydrolysis reaction. This is a family-level and architectural inference, not proof of the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about secretory and membrane-associated protein architecture meaningfully separates A from the offered alternatives without needing the exact protein's recorded annotation. The exact chitinase activity is less secure from sequence architecture alone, but the alternatives make the qualitative distinction meaningful."
  },
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.14 and the reaction in option A. However, the annotation is transferred by similarity from Q8J0P4, so it supports the key as a computationally inferred annotation, not as direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The supplied reviewer evidence indicates that the chitinase annotation was transferred from a homolog; it does not establish direct experimental measurement of this protein's activity.",
    "The sequence may support a broader carbohydrate-remodeling role, but the precise reaction and substrate specificity are not established by the sequence architecture alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and no other option is comparably supported by the sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.2.1.14 and the reaction in option A. However, the annotation is transferred by similarity from Q8J0P4, so it supports the key as a computationally inferred annotation, not as direct experimental confirmation for this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region, a cysteine-rich extracellular-looking region, and a C-terminal membrane-anchor-like segment. That architecture is more consistent with a secreted or cell-surface carbohydrate-active protein than with the cytosolic tRNA/protein acylation reactions in B and C or the ferredoxin-dependent carotenoid reaction in D. Among these choices, A is the plausible polysaccharide-hydrolysis reaction. This is a family-level and architectural inference, not proof of the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about secretory and membrane-associated protein architecture meaningfully separates A from the offered alternatives without needing the exact protein's recorded annotation. The exact chitinase activity is less secure from sequence architecture alone, but the alternatives make the qualitative distinction meaningful."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and no other option is comparably supported by the sequence architecture."
  },
  "important_caveats": [
    "The supplied reviewer evidence indicates that the chitinase annotation was transferred from a homolog; it does not establish direct experimental measurement of this protein's activity.",
    "The sequence may support a broader carbohydrate-remodeling role, but the precise reaction and substrate specificity are not established by the sequence architecture alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A384K116 (CRH3_BOTFB) annotates this protein with EC 3.2.1.14 and the exact catalytic activity text in option A. The evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental proof for this specific protein, but the annotation is recorded and the sequence features (CBM14 domain, GH18 catalytic domain, transmembrane anchor) are consistent with chitinase activity. The sequence matches the benchmark input exactly (444 AA, SHA256 match).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hallmarks of a fungal GH18 chitinase recognizable through family-level knowledge: (1) an N-terminal signal peptide (MVGKSTLLSVLASASVAFAACS) indicating secretion; (2) a cysteine-rich CBM14 chitin-binding domain in the first ~100 residues (CCPEETPCCSQYGECGTGAYCLGGCDPR...CVPEPVCESASYTFTSM) with the characteristic 6-8 cysteine spacing pattern found across fungal chitinases (Trichoderma, Aspergillus, etc.); (3) a central GH18 catalytic domain with the DxExD catalytic motif (DGLD...DSE...DNE...DSE...DNE...DSE...DNE pattern) and TIM-barrel-associated sequence features; (4) a C-terminal transmembrane anchor (GSLFAGIVAVVAMMAL) typical of Crh-type fungal chitinases. None of the other options match: B requires CoA-binding/acyltransferase motifs absent here; C requires NAT/NatA domain features; D requires a ferredoxin-dependent hydroxylase or carotenoid-binding domain. A model familiar with fungal GH18 chitinases (e.g., from Trichoderma, Aspergillus, or other plant-pathogenic fungi) can confidently assign chitinase activity from these domain features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The domain architecture (signal peptide + CBM14 + GH18 catalytic domain + TM anchor) is a well-conserved fungal chitinase signature transferable from knowledge of many other fungal GH18 enzymes. This meaningfully distinguishes option A from B, C, and D without requiring the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only A relates to chitin hydrolysis. Options B (benzoyl-CoA ligase), C (NAT on tRNA-Ile), and D (carotenoid hydroxylase) describe entirely unrelated enzyme classes with no sequence or structural support in this protein. The GH18 chitinase features are unambiguous among these alternatives.


### Important caveats

- The UniProt annotation for EC 3.2.1.14 is based on similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experimental characterization of this specific protein.
- The entry also annotates EC 2.4.-.- (chitin transglycosylase), suggesting the protein may have dual chitinase/transglycosylase activity, but transglycosylase is not among the offered choices.
- The PubMed reference (33846308) describes Crh1 transglycosylase function; the chitinase annotation for Crh3 is by similarity to Q8J0P4.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hallmarks of a fungal GH18 chitinase recognizable through family-level knowledge: (1) an N-terminal signal peptide (MVGKSTLLSVLASASVAFAACS) indicating secretion; (2) a cysteine-rich CBM14 chitin-binding domain in the first ~100 residues (CCPEETPCCSQYGECGTGAYCLGGCDPR...CVPEPVCESASYTFTSM) with the characteristic 6-8 cysteine spacing pattern found across fungal chitinases (Trichoderma, Aspergillus, etc.); (3) a central GH18 catalytic domain with the DxExD catalytic motif (DGLD...DSE...DNE...DSE...DNE...DSE...DNE pattern) and TIM-barrel-associated sequence features; (4) a C-terminal transmembrane anchor (GSLFAGIVAVVAMMAL) typical of Crh-type fungal chitinases. None of the other options match: B requires CoA-binding/acyltransferase motifs absent here; C requires NAT/NatA domain features; D requires a ferredoxin-dependent hydroxylase or carotenoid-binding domain. A model familiar with fungal GH18 chitinases (e.g., from Trichoderma, Aspergillus, or other plant-pathogenic fungi) can confidently assign chitinase activity from these domain features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The domain architecture (signal peptide + CBM14 + GH18 catalytic domain + TM anchor) is a well-conserved fungal chitinase signature transferable from knowledge of many other fungal GH18 enzymes. This meaningfully distinguishes option A from B, C, and D without requiring the specific UniProt annotation for this exact protein."
  },
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A384K116 (CRH3_BOTFB) annotates this protein with EC 3.2.1.14 and the exact catalytic activity text in option A. The evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental proof for this specific protein, but the annotation is recorded and the sequence features (CBM14 domain, GH18 catalytic domain, transmembrane anchor) are consistent with chitinase activity. The sequence matches the benchmark input exactly (444 AA, SHA256 match)."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.14 is based on similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experimental characterization of this specific protein.",
    "The entry also annotates EC 2.4.-.- (chitin transglycosylase), suggesting the protein may have dual chitinase/transglycosylase activity, but transglycosylase is not among the offered choices.",
    "The PubMed reference (33846308) describes Crh1 transglycosylase function; the chitinase annotation for Crh3 is by similarity to Q8J0P4."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A relates to chitin hydrolysis. Options B (benzoyl-CoA ligase), C (NAT on tRNA-Ile), and D (carotenoid hydroxylase) describe entirely unrelated enzyme classes with no sequence or structural support in this protein. The GH18 chitinase features are unambiguous among these alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A384K116 (CRH3_BOTFB) annotates this protein with EC 3.2.1.14 and the exact catalytic activity text in option A. The evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental proof for this specific protein, but the annotation is recorded and the sequence features (CBM14 domain, GH18 catalytic domain, transmembrane anchor) are consistent with chitinase activity. The sequence matches the benchmark input exactly (444 AA, SHA256 match).",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hallmarks of a fungal GH18 chitinase recognizable through family-level knowledge: (1) an N-terminal signal peptide (MVGKSTLLSVLASASVAFAACS) indicating secretion; (2) a cysteine-rich CBM14 chitin-binding domain in the first ~100 residues (CCPEETPCCSQYGECGTGAYCLGGCDPR...CVPEPVCESASYTFTSM) with the characteristic 6-8 cysteine spacing pattern found across fungal chitinases (Trichoderma, Aspergillus, etc.); (3) a central GH18 catalytic domain with the DxExD catalytic motif (DGLD...DSE...DNE...DSE...DNE...DSE...DNE pattern) and TIM-barrel-associated sequence features; (4) a C-terminal transmembrane anchor (GSLFAGIVAVVAMMAL) typical of Crh-type fungal chitinases. None of the other options match: B requires CoA-binding/acyltransferase motifs absent here; C requires NAT/NatA domain features; D requires a ferredoxin-dependent hydroxylase or carotenoid-binding domain. A model familiar with fungal GH18 chitinases (e.g., from Trichoderma, Aspergillus, or other plant-pathogenic fungi) can confidently assign chitinase activity from these domain features.",
    "missing_item_specific_fact": "",
    "reason": "The domain architecture (signal peptide + CBM14 + GH18 catalytic domain + TM anchor) is a well-conserved fungal chitinase signature transferable from knowledge of many other fungal GH18 enzymes. This meaningfully distinguishes option A from B, C, and D without requiring the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A relates to chitin hydrolysis. Options B (benzoyl-CoA ligase), C (NAT on tRNA-Ile), and D (carotenoid hydroxylase) describe entirely unrelated enzyme classes with no sequence or structural support in this protein. The GH18 chitinase features are unambiguous among these alternatives."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.1.14 is based on similarity (ECO:0000250|UniProtKB:Q8J0P4), not direct experimental characterization of this specific protein.",
    "The entry also annotates EC 2.4.-.- (chitin transglycosylase), suggesting the protein may have dual chitinase/transglycosylase activity, but transglycosylase is not among the offered choices.",
    "The PubMed reference (33846308) describes Crh1 transglycosylase function; the chitinase annotation for Crh3 is by similarity to Q8J0P4."
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
  "benchmark_sequence_length": 444,
  "benchmark_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 444,
  "current_source_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K116",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "selected_historical_source_sequence_length": 444,
  "selected_historical_source_sequence_sha256": "fb0633b17deb89eb19591d65a84515ea5ac98abe057826a49312d226bb2dc5e4",
  "selected_historical_version": {
    "accession": "A0A384K116",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH3_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K116\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh3\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh3\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"name\":\"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH CRH1 AND CRH2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:58.718541+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K116.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   CRH3_BOTFB              Reviewed;         444 AA.\nAC   A0A384K116;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh3 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_13g03640;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBUNIT, AND INTERACTION WITH CRH1 AND CRH2.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide\nCC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;\nCC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.844205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41",
  "url": "https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
