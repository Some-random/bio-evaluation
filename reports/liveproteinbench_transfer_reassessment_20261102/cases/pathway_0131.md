# pathway_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0131.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Protein biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPYQMGEAMPDLVPVLAGAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTAETIADPEARSVANRAIVTLRRIGKVPVESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLSDKRLLATPEEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEEFVKHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAVLGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAELAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGHLEASGHNWVEGQGSGERIDKKAGDDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. L-isoleucine biosynthesis
B. Protein biosynthesis
C. terpenoid biosynthesis.
D. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
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

> The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred from a homolog (ECO:0000250), so it is not direct experimental proof for this exact sequence; it nevertheless supports the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a large protein with two recognizable P-loop ATPase nucleotide-binding domains, including Walker A-like GxxxxGKT motifs. That architecture, together with the protein's substantial non-ATPase regions, is characteristic of fungal elongation factor 3. Transferable knowledge of this translation factor's role as a ribosome-associated ATPase during elongation meaningfully favors protein biosynthesis over the offered metabolic pathways.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supplies family-level clues that can distinguish the offered pathway choices without recalling this exact protein's database record. The inference is strong but not a direct experimental determination from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, protein biosynthesis is the defensible pathway for an elongation factor; the other options describe distinct metabolic pathways.


### Important caveats

- The supplied pathway annotation is based on transfer from a homolog, not direct experimental evidence for this exact sequence.
- The reviewer-only accession, organism identity, and database annotations were not original model inputs and are not used as the basis for answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large protein with two recognizable P-loop ATPase nucleotide-binding domains, including Walker A-like GxxxxGKT motifs. That architecture, together with the protein's substantial non-ATPase regions, is characteristic of fungal elongation factor 3. Transferable knowledge of this translation factor's role as a ribosome-associated ATPase during elongation meaningfully favors protein biosynthesis over the offered metabolic pathways.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies family-level clues that can distinguish the offered pathway choices without recalling this exact protein's database record. The inference is strong but not a direct experimental determination from sequence alone."
  },
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred from a homolog (ECO:0000250), so it is not direct experimental proof for this exact sequence; it nevertheless supports the expected answer."
  },
  "important_caveats": [
    "The supplied pathway annotation is based on transfer from a homolog, not direct experimental evidence for this exact sequence.",
    "The reviewer-only accession, organism identity, and database annotations were not original model inputs and are not used as the basis for answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, protein biosynthesis is the defensible pathway for an elongation factor; the other options describe distinct metabolic pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred from a homolog (ECO:0000250), so it is not direct experimental proof for this exact sequence; it nevertheless supports the expected answer.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a large protein with two recognizable P-loop ATPase nucleotide-binding domains, including Walker A-like GxxxxGKT motifs. That architecture, together with the protein's substantial non-ATPase regions, is characteristic of fungal elongation factor 3. Transferable knowledge of this translation factor's role as a ribosome-associated ATPase during elongation meaningfully favors protein biosynthesis over the offered metabolic pathways.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies family-level clues that can distinguish the offered pathway choices without recalling this exact protein's database record. The inference is strong but not a direct experimental determination from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, protein biosynthesis is the defensible pathway for an elongation factor; the other options describe distinct metabolic pathways."
  },
  "important_caveats": [
    "The supplied pathway annotation is based on transfer from a homolog, not direct experimental evidence for this exact sequence.",
    "The reviewer-only accession, organism identity, and database annotations were not original model inputs and are not used as the basis for answerability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5KIM6 (EF3_CRYD1) annotates this protein as Elongation factor 3 (eEF3/CnEF3), an ATP-dependent translation factor from Cryptococcus deneoformans. The PATHWAY comment explicitly states 'Protein biosynthesis; polypeptide chain elongation' (ECO:0000250, transferred from O93796). The protein description confirms EC 3.6.4.- and association with ribosomes (PubMed:11244063). The sequence contains three tandem AAA+ ATPase domains (Walker A 'GSGKST' motifs and Walker B 'DEPT' motifs), consistent with the EF-3 family architecture. The answer B (Protein biosynthesis) is fully supported by the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays three tandem AAA+ ATPase domains, identifiable by repeated Walker A motifs (GSGKST at positions corresponding to three distinct domains) and Walker B motifs (DEPT...D). This three-AAA+ domain architecture in a ~1055 aa protein is a well-known family-level signature of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. EF-3 stimulates aminoacyl-tRNA accommodation at the ribosomal A-site and is classified under protein biosynthesis (translation). Transferable knowledge about AAA+ protein families allows a model to: (1) recognize the three-domain AAA+ arrangement as distinctive of EF-3 rather than single-domain AAA+ proteins (e.g., proteasome Rpt subunits ~400-500 aa with one domain), (2) note the absence of protease, helicase-specific, or small-molecule-catalytic domains that would indicate other pathways. The other options involve enzymes with entirely different architectures: L-isoleucine biosynthesis enzymes (e.g., dihydroxy-acid dehydratase ~350 aa, branched-chain keto acid dehydrogenase) lack AAA+ domains; terpenoid biosynthesis enzymes (HMG-CoA reductase, mevalonate kinase) have distinct catalytic folds; chorismate synthase is a small (~300 aa) flavin-dependent enzyme. Thus, family-level recognition of the three-AAA+ EF-3 architecture meaningfully distinguishes option B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The three tandem AAA+ domain architecture is a transferable family-level feature shared across EF-3 homologs in fungi. A model familiar with AAA+ protein families can recognize this pattern and associate it with translation/protein biosynthesis without needing to look up the specific UniProt entry for this exact protein. The distractor options (isoleucine biosynthesis, terpenoid biosynthesis, chorismate synthase) involve enzymes with fundamentally different domain architectures that are inconsistent with the observed sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three AAA+ domain architecture is specific enough to distinguish EF-3 (protein biosynthesis) from the other options. None of the other pathways (isoleucine biosynthesis, terpenoid biosynthesis, shikimate pathway step 7) involve multi-AAA+ domain proteins. The options are well-separated by protein architecture.


### Important caveats

- The EF-3 pathway annotation (ECO:0000250) is transferred by similarity from O93796 (S. cerevisiae EF-3), not directly experimentally determined for this exact protein, though the protein's function and ribosome association were experimentally characterized (PubMed:11244063).
- EF-3 is fungal-specific; a model trained primarily on bacterial or mammalian proteins might not be familiar with this family, though the three-AAA+ architecture is still recognizable as an unusual multi-domain AAA+ arrangement.
- The protein length (~1055 aa) and three-domain arrangement are consistent with EF-3 but the model would need to rule out other multi-AAA+ proteins (e.g., some helicases or chaperones), though none of the offered options correspond to such proteins.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays three tandem AAA+ ATPase domains, identifiable by repeated Walker A motifs (GSGKST at positions corresponding to three distinct domains) and Walker B motifs (DEPT...D). This three-AAA+ domain architecture in a ~1055 aa protein is a well-known family-level signature of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. EF-3 stimulates aminoacyl-tRNA accommodation at the ribosomal A-site and is classified under protein biosynthesis (translation). Transferable knowledge about AAA+ protein families allows a model to: (1) recognize the three-domain AAA+ arrangement as distinctive of EF-3 rather than single-domain AAA+ proteins (e.g., proteasome Rpt subunits ~400-500 aa with one domain), (2) note the absence of protease, helicase-specific, or small-molecule-catalytic domains that would indicate other pathways. The other options involve enzymes with entirely different architectures: L-isoleucine biosynthesis enzymes (e.g., dihydroxy-acid dehydratase ~350 aa, branched-chain keto acid dehydrogenase) lack AAA+ domains; terpenoid biosynthesis enzymes (HMG-CoA reductase, mevalonate kinase) have distinct catalytic folds; chorismate synthase is a small (~300 aa) flavin-dependent enzyme. Thus, family-level recognition of the three-AAA+ EF-3 architecture meaningfully distinguishes option B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The three tandem AAA+ domain architecture is a transferable family-level feature shared across EF-3 homologs in fungi. A model familiar with AAA+ protein families can recognize this pattern and associate it with translation/protein biosynthesis without needing to look up the specific UniProt entry for this exact protein. The distractor options (isoleucine biosynthesis, terpenoid biosynthesis, chorismate synthase) involve enzymes with fundamentally different domain architectures that are inconsistent with the observed sequence features."
  },
  "case_id": "pathway_0131",
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
    "reason": "The UniProt entry Q5KIM6 (EF3_CRYD1) annotates this protein as Elongation factor 3 (eEF3/CnEF3), an ATP-dependent translation factor from Cryptococcus deneoformans. The PATHWAY comment explicitly states 'Protein biosynthesis; polypeptide chain elongation' (ECO:0000250, transferred from O93796). The protein description confirms EC 3.6.4.- and association with ribosomes (PubMed:11244063). The sequence contains three tandem AAA+ ATPase domains (Walker A 'GSGKST' motifs and Walker B 'DEPT' motifs), consistent with the EF-3 family architecture. The answer B (Protein biosynthesis) is fully supported by the annotation."
  },
  "important_caveats": [
    "The EF-3 pathway annotation (ECO:0000250) is transferred by similarity from O93796 (S. cerevisiae EF-3), not directly experimentally determined for this exact protein, though the protein's function and ribosome association were experimentally characterized (PubMed:11244063).",
    "EF-3 is fungal-specific; a model trained primarily on bacterial or mammalian proteins might not be familiar with this family, though the three-AAA+ architecture is still recognizable as an unusual multi-domain AAA+ arrangement.",
    "The protein length (~1055 aa) and three-domain arrangement are consistent with EF-3 but the model would need to rule out other multi-AAA+ proteins (e.g., some helicases or chaperones), though none of the offered options correspond to such proteins."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three AAA+ domain architecture is specific enough to distinguish EF-3 (protein biosynthesis) from the other options. None of the other pathways (isoleucine biosynthesis, terpenoid biosynthesis, shikimate pathway step 7) involve multi-AAA+ domain proteins. The options are well-separated by protein architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5KIM6 (EF3_CRYD1) annotates this protein as Elongation factor 3 (eEF3/CnEF3), an ATP-dependent translation factor from Cryptococcus deneoformans. The PATHWAY comment explicitly states 'Protein biosynthesis; polypeptide chain elongation' (ECO:0000250, transferred from O93796). The protein description confirms EC 3.6.4.- and association with ribosomes (PubMed:11244063). The sequence contains three tandem AAA+ ATPase domains (Walker A 'GSGKST' motifs and Walker B 'DEPT' motifs), consistent with the EF-3 family architecture. The answer B (Protein biosynthesis) is fully supported by the annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays three tandem AAA+ ATPase domains, identifiable by repeated Walker A motifs (GSGKST at positions corresponding to three distinct domains) and Walker B motifs (DEPT...D). This three-AAA+ domain architecture in a ~1055 aa protein is a well-known family-level signature of eukaryotic elongation factor 3 (eEF3), a fungal-specific translation factor. EF-3 stimulates aminoacyl-tRNA accommodation at the ribosomal A-site and is classified under protein biosynthesis (translation). Transferable knowledge about AAA+ protein families allows a model to: (1) recognize the three-domain AAA+ arrangement as distinctive of EF-3 rather than single-domain AAA+ proteins (e.g., proteasome Rpt subunits ~400-500 aa with one domain), (2) note the absence of protease, helicase-specific, or small-molecule-catalytic domains that would indicate other pathways. The other options involve enzymes with entirely different architectures: L-isoleucine biosynthesis enzymes (e.g., dihydroxy-acid dehydratase ~350 aa, branched-chain keto acid dehydrogenase) lack AAA+ domains; terpenoid biosynthesis enzymes (HMG-CoA reductase, mevalonate kinase) have distinct catalytic folds; chorismate synthase is a small (~300 aa) flavin-dependent enzyme. Thus, family-level recognition of the three-AAA+ EF-3 architecture meaningfully distinguishes option B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The three tandem AAA+ domain architecture is a transferable family-level feature shared across EF-3 homologs in fungi. A model familiar with AAA+ protein families can recognize this pattern and associate it with translation/protein biosynthesis without needing to look up the specific UniProt entry for this exact protein. The distractor options (isoleucine biosynthesis, terpenoid biosynthesis, chorismate synthase) involve enzymes with fundamentally different domain architectures that are inconsistent with the observed sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three AAA+ domain architecture is specific enough to distinguish EF-3 (protein biosynthesis) from the other options. None of the other pathways (isoleucine biosynthesis, terpenoid biosynthesis, shikimate pathway step 7) involve multi-AAA+ domain proteins. The options are well-separated by protein architecture."
  },
  "important_caveats": [
    "The EF-3 pathway annotation (ECO:0000250) is transferred by similarity from O93796 (S. cerevisiae EF-3), not directly experimentally determined for this exact protein, though the protein's function and ribosome association were experimentally characterized (PubMed:11244063).",
    "EF-3 is fungal-specific; a model trained primarily on bacterial or mammalian proteins might not be familiar with this family, though the three-AAA+ architecture is still recognizable as an unusual multi-domain AAA+ arrangement.",
    "The protein length (~1055 aa) and three-domain arrangement are consistent with EF-3 but the model would need to rule out other multi-AAA+ proteins (e.g., some helicases or chaperones), though none of the offered options correspond to such proteins."
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
  "benchmark_sequence_length": 1055,
  "benchmark_sequence_sha256": "da4575a63eb192d39787f6fd7f81a2eac11b723684e0276f6772d5de325f4bdf",
  "current_entry_audit": {
    "entryVersion": 145,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-02-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1055,
  "current_source_sequence_sha256": "da4575a63eb192d39787f6fd7f81a2eac11b723684e0276f6772d5de325f4bdf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 144,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5KIM6",
  "selected_historical_entry_version": 144,
  "selected_historical_record_sha256": "f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67",
  "selected_historical_source_sequence_length": 1055,
  "selected_historical_source_sequence_sha256": "da4575a63eb192d39787f6fd7f81a2eac11b723684e0276f6772d5de325f4bdf",
  "selected_historical_version": {
    "accession": "Q5KIM6",
    "database": "Swiss-Prot",
    "entryVersion": 144,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "EF3_CRYD1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5KIM6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":145,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-02-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. neoformans serotype D\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002149\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565)\",\"taxonId\":214684}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11244063\",\"source\":\"PubMed\"}],\"value\":\"CnEF3\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Eukaryotic elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"eEF3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11244063\",\"source\":\"PubMed\"}],\"value\":\"3.6.4.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"EF-3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93796\",\"source\":\"UniProtKB\"}],\"value\":\"Protein biosynthesis; polypeptide chain elongation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Blakely G.\",\"Hekman J.\",\"Chakraburtty K.\",\"Williamson P.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11244063\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.183.7.2241-2248.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"2241\",\"id\":\"11244063\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2248\",\"publicationDate\":\"2001\",\"title\":\"Evolutionary divergence of an elongation factor 3 from Cryptococcus neoformans.\",\"volume\":\"183\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11244063\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"B-3501A\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ASSOCIATION WITH RIBOSOMES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:21.720628+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4",
  "url": "https://rest.uniprot.org/uniprotkb/Q5KIM6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)

```json
{
  "entry_version": 144,
  "evidence_id": "H1",
  "excerpt": "ID   EF3_CRYD1               Reviewed;        1055 AA.\nAC   Q5KIM6; Q55TQ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-FEB-2005, sequence version 1.\nDT   28-JAN-2026, entry version 144.\nDE   RecName: Full=Elongation factor 3 {ECO:0000305};\nDE            Short=EF-3 {ECO:0000305};\nDE            EC=3.6.4.- {ECO:0000269|PubMed:11244063};\nDE   AltName: Full=CnEF3 {ECO:0000303|PubMed:11244063};\nDE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};\nDE            Short=eEF3 {ECO:0000305};\nGN   Name=TEF3 {ECO:0000305};\nGN   OrderedLocusNames=CND02420 {ECO:0000312|EMBL:AAW42954.1};\nOS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus\nOS   neoformans var. neoformans serotype D).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:25.631379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67",
  "url": "https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)

```json
{
  "entry_version": 144,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   ASSOCIATION WITH RIBOSOMES.\nRC   STRAIN=B-3501A {ECO:0000303|PubMed:11244063};\nRX   PubMed=11244063; DOI=10.1128/jb.183.7.2241-2248.2001;\nRA   Blakely G., Hekman J., Chakraburtty K., Williamson P.R.;\nRT   \"Evolutionary divergence of an elongation factor 3 from Cryptococcus\nRT   neoformans.\";\nRL   J. Bacteriol. 183:2241-2248(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:25.631379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67",
  "url": "https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)

```json
{
  "entry_version": 144,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.\nCC       {ECO:0000250|UniProtKB:O93796}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:25.631379+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67",
  "url": "https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
