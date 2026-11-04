# cofactor_0162

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0162.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSEEVQERIWILITPDKCSGCRLCEVTCSLEHEGIIWPEASRIRVFELFPGINVPHTCVQCPDYPCVNACPTNALSVDEKTGAVVVNEEKCITCGACVLACPGKVPRIPAGKGSVVICDLCGGNPKCVEICHEAGHDALKIVTGNYRPIYRTFAKDPQEKSLDIARKVFGEDF

[Multiple Choices]
A. [2Fe-2S] cluster
B. [4Fe-4S] cluster
C. Ca(2+)
D. Zn(2+)
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

> The sequence matches the historical UniProt entry, which reports four &#91;4Fe-4S&#93; clusters per subunit with experimental evidence; the associated reference describes crystallography with &#91;4Fe-4S&#93; clusters. This supports choice B for the supplied protein.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated, closely spaced cysteine-rich motifs characteristic of iron-sulfur-cluster-binding proteins. Transferable knowledge of polyferredoxin-like proteins makes multiple &#91;4Fe-4S&#93; clusters a credible inference from this pattern, distinguishing B from the metal-ion options and, given the repeated motifs, from a single &#91;2Fe-2S&#93; cluster.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a meaningful family- and motif-level basis for the keyed choice; the exact target annotation is not necessary to distinguish the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The repeated cysteine-rich motifs favor iron-sulfur clusters, and the polyferredoxin-like pattern supports the offered &#91;4Fe-4S&#93; choice over the alternatives.


### Important caveats

- The reviewer-only entry supports the key but was not available as an input to the evaluated model.
- The sequence-based inference is probabilistic; the exact cluster type is supported by the matched protein's experimental and structural annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated, closely spaced cysteine-rich motifs characteristic of iron-sulfur-cluster-binding proteins. Transferable knowledge of polyferredoxin-like proteins makes multiple [4Fe-4S] clusters a credible inference from this pattern, distinguishing B from the metal-ion options and, given the repeated motifs, from a single [2Fe-2S] cluster.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful family- and motif-level basis for the keyed choice; the exact target annotation is not necessary to distinguish the offered alternatives."
  },
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt entry, which reports four [4Fe-4S] clusters per subunit with experimental evidence; the associated reference describes crystallography with [4Fe-4S] clusters. This supports choice B for the supplied protein."
  },
  "important_caveats": [
    "The reviewer-only entry supports the key but was not available as an input to the evaluated model.",
    "The sequence-based inference is probabilistic; the exact cluster type is supported by the matched protein's experimental and structural annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The repeated cysteine-rich motifs favor iron-sulfur clusters, and the polyferredoxin-like pattern supports the offered [4Fe-4S] choice over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt entry, which reports four [4Fe-4S] clusters per subunit with experimental evidence; the associated reference describes crystallography with [4Fe-4S] clusters. This supports choice B for the supplied protein.",
    "evidence_ids": ["H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated, closely spaced cysteine-rich motifs characteristic of iron-sulfur-cluster-binding proteins. Transferable knowledge of polyferredoxin-like proteins makes multiple [4Fe-4S] clusters a credible inference from this pattern, distinguishing B from the metal-ion options and, given the repeated motifs, from a single [2Fe-2S] cluster.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful family- and motif-level basis for the keyed choice; the exact target annotation is not necessary to distinguish the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The repeated cysteine-rich motifs favor iron-sulfur clusters, and the polyferredoxin-like pattern supports the offered [4Fe-4S] choice over the alternatives."
  },
  "important_caveats": [
    "The reviewer-only entry supports the key but was not available as an input to the evaluated model.",
    "The sequence-based inference is probabilistic; the exact cluster type is supported by the matched protein's experimental and structural annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8U0V2 annotates the cofactor as &#91;4Fe-4S&#93; cluster with experimental evidence (ECO:0000269, PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) showing iron-sulfur (4Fe-4S) clusters. The annotation specifies 'Binds 4 &#91;4Fe-4S&#93; clusters per subunit.' The sequence (173 AA, 16 cysteines in 4 tight groups of 4) is consistent with a polyferredoxin-like protein binding four &#91;4Fe-4S&#93; clusters.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 173-residue sequence contains 16 cysteines arranged in four groups of four with tight spacing: C18-C21-C24-C28 (spacings 3,3,4; span 10), C58-C61-C66-C70 (spacings 3,5,4; span 12), C91-C94-C97-C101 (spacings 3,3,4; span 10), C118-C121-C127-C131 (spacings 3,6,4; span 13). These CxxCxxCxxC motifs with ~10-13 residue spans are the hallmark &#91;4Fe-4S&#93; ferredoxin-type binding motifs, distinct from &#91;2Fe-2S&#93; motifs which require wider spacing (CxxCxxCxxCxxC, ~16 residue span). The architecture of four such clusters in a small protein is the classic 'polyferredoxin' arrangement well-documented across many archaeal and anaerobic bacterial proteins (e.g., ferredoxins, 2-oxoacid:ferredoxin oxidoreductases, pyruvate:ferredoxin oxidoreductases). Ca(2+) and Zn(2+) are eliminated by the cysteine-rich ferredoxin architecture; Zn(2+) uses C2H2/C4 motifs with different spacing, and Ca(2+) relies on Asp/Glu/carbonyl coordination. Distinguishing &#91;4Fe-4S&#93; from &#91;2Fe-2S&#93; relies on the well-established cysteine spacing rule transferable from hundreds of characterized ferredoxins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The cysteine spacing pattern (CxxCxxCxxC with ~10-13 residue spans) is a transferable structural signature that reliably distinguishes &#91;4Fe-4S&#93; from &#91;2Fe-2S&#93; binding sites, learned from the large family of characterized ferredoxins. The four-cluster polyferredoxin architecture with this spacing is a well-known pattern in archaeal anaerobic metabolism. A knowledgeable model can use this pattern without knowing the specific UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The tight CxxCxxCxxC spacing in all four cysteine groups clearly points to &#91;4Fe-4S&#93; over &#91;2Fe-2S&#93; (which requires wider spacing). Ca(2+) and Zn(2+) are incompatible with the ferredoxin-like cysteine architecture. No ambiguity among the offered choices.


### Important caveats

- The reviewer-only UniProt annotation confirms &#91;4Fe-4S&#93; experimentally (X-ray crystallography), but the model must rely on cysteine spacing patterns and polyferredoxin family knowledge from the sequence alone.
- The protein is from Pyrococcus furiosus, a hyperthermophilic archaeon; thermophilic ferredoxins predominantly use &#91;4Fe-4S&#93; clusters, which is transferable knowledge from many related archaeal proteins.
- The term 'polyferredoxin-like' in the UniProt name is reviewer-only information; the model must infer this from the four-cluster cysteine arrangement visible in the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 173-residue sequence contains 16 cysteines arranged in four groups of four with tight spacing: C18-C21-C24-C28 (spacings 3,3,4; span 10), C58-C61-C66-C70 (spacings 3,5,4; span 12), C91-C94-C97-C101 (spacings 3,3,4; span 10), C118-C121-C127-C131 (spacings 3,6,4; span 13). These CxxCxxCxxC motifs with ~10-13 residue spans are the hallmark [4Fe-4S] ferredoxin-type binding motifs, distinct from [2Fe-2S] motifs which require wider spacing (CxxCxxCxxCxxC, ~16 residue span). The architecture of four such clusters in a small protein is the classic 'polyferredoxin' arrangement well-documented across many archaeal and anaerobic bacterial proteins (e.g., ferredoxins, 2-oxoacid:ferredoxin oxidoreductases, pyruvate:ferredoxin oxidoreductases). Ca(2+) and Zn(2+) are eliminated by the cysteine-rich ferredoxin architecture; Zn(2+) uses C2H2/C4 motifs with different spacing, and Ca(2+) relies on Asp/Glu/carbonyl coordination. Distinguishing [4Fe-4S] from [2Fe-2S] relies on the well-established cysteine spacing rule transferable from hundreds of characterized ferredoxins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The cysteine spacing pattern (CxxCxxCxxC with ~10-13 residue spans) is a transferable structural signature that reliably distinguishes [4Fe-4S] from [2Fe-2S] binding sites, learned from the large family of characterized ferredoxins. The four-cluster polyferredoxin architecture with this spacing is a well-known pattern in archaeal anaerobic metabolism. A knowledgeable model can use this pattern without knowing the specific UniProt record."
  },
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8U0V2 annotates the cofactor as [4Fe-4S] cluster with experimental evidence (ECO:0000269, PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) showing iron-sulfur (4Fe-4S) clusters. The annotation specifies 'Binds 4 [4Fe-4S] clusters per subunit.' The sequence (173 AA, 16 cysteines in 4 tight groups of 4) is consistent with a polyferredoxin-like protein binding four [4Fe-4S] clusters."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms [4Fe-4S] experimentally (X-ray crystallography), but the model must rely on cysteine spacing patterns and polyferredoxin family knowledge from the sequence alone.",
    "The protein is from Pyrococcus furiosus, a hyperthermophilic archaeon; thermophilic ferredoxins predominantly use [4Fe-4S] clusters, which is transferable knowledge from many related archaeal proteins.",
    "The term 'polyferredoxin-like' in the UniProt name is reviewer-only information; the model must infer this from the four-cluster cysteine arrangement visible in the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The tight CxxCxxCxxC spacing in all four cysteine groups clearly points to [4Fe-4S] over [2Fe-2S] (which requires wider spacing). Ca(2+) and Zn(2+) are incompatible with the ferredoxin-like cysteine architecture. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8U0V2 annotates the cofactor as [4Fe-4S] cluster with experimental evidence (ECO:0000269, PubMed:36269456), confirmed by X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) showing iron-sulfur (4Fe-4S) clusters. The annotation specifies 'Binds 4 [4Fe-4S] clusters per subunit.' The sequence (173 AA, 16 cysteines in 4 tight groups of 4) is consistent with a polyferredoxin-like protein binding four [4Fe-4S] clusters.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 173-residue sequence contains 16 cysteines arranged in four groups of four with tight spacing: C18-C21-C24-C28 (spacings 3,3,4; span 10), C58-C61-C66-C70 (spacings 3,5,4; span 12), C91-C94-C97-C101 (spacings 3,3,4; span 10), C118-C121-C127-C131 (spacings 3,6,4; span 13). These CxxCxxCxxC motifs with ~10-13 residue spans are the hallmark [4Fe-4S] ferredoxin-type binding motifs, distinct from [2Fe-2S] motifs which require wider spacing (CxxCxxCxxCxxC, ~16 residue span). The architecture of four such clusters in a small protein is the classic 'polyferredoxin' arrangement well-documented across many archaeal and anaerobic bacterial proteins (e.g., ferredoxins, 2-oxoacid:ferredoxin oxidoreductases, pyruvate:ferredoxin oxidoreductases). Ca(2+) and Zn(2+) are eliminated by the cysteine-rich ferredoxin architecture; Zn(2+) uses C2H2/C4 motifs with different spacing, and Ca(2+) relies on Asp/Glu/carbonyl coordination. Distinguishing [4Fe-4S] from [2Fe-2S] relies on the well-established cysteine spacing rule transferable from hundreds of characterized ferredoxins.",
    "missing_item_specific_fact": "",
    "reason": "The cysteine spacing pattern (CxxCxxCxxC with ~10-13 residue spans) is a transferable structural signature that reliably distinguishes [4Fe-4S] from [2Fe-2S] binding sites, learned from the large family of characterized ferredoxins. The four-cluster polyferredoxin architecture with this spacing is a well-known pattern in archaeal anaerobic metabolism. A knowledgeable model can use this pattern without knowing the specific UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The tight CxxCxxCxxC spacing in all four cysteine groups clearly points to [4Fe-4S] over [2Fe-2S] (which requires wider spacing). Ca(2+) and Zn(2+) are incompatible with the ferredoxin-like cysteine architecture. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms [4Fe-4S] experimentally (X-ray crystallography), but the model must rely on cysteine spacing patterns and polyferredoxin family knowledge from the sequence alone.",
    "The protein is from Pyrococcus furiosus, a hyperthermophilic archaeon; thermophilic ferredoxins predominantly use [4Fe-4S] clusters, which is transferable knowledge from many related archaeal proteins.",
    "The term 'polyferredoxin-like' in the UniProt name is reviewer-only information; the model must infer this from the four-cluster cysteine arrangement visible in the sequence."
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
  "benchmark_sequence_length": 173,
  "benchmark_sequence_sha256": "c96fb96cf353a2a45daf7d7220a05907ec80320af9f23fca1b4787e65147800e",
  "current_entry_audit": {
    "entryVersion": 118,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 173,
  "current_source_sequence_sha256": "c96fb96cf353a2a45daf7d7220a05907ec80320af9f23fca1b4787e65147800e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 116,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8U0V2",
  "selected_historical_entry_version": 116,
  "selected_historical_record_sha256": "baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510",
  "selected_historical_source_sequence_length": 173,
  "selected_historical_source_sequence_sha256": "c96fb96cf353a2a45daf7d7220a05907ec80320af9f23fca1b4787e65147800e",
  "selected_historical_version": {
    "accession": "Q8U0V2",
    "database": "Swiss-Prot",
    "entryVersion": 116,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASORS_PYRFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8U0V2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":118,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Polyferredoxin-like protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 small subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-S\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, polyferredoxin-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:49883\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"[4Fe-4S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Binds 4 [4Fe-4S] clusters per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTERS\",\"FUNCTION\",\"COFACTOR\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:28.261641+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905",
  "url": "https://rest.uniprot.org/uniprotkb/Q8U0V2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H1",
  "excerpt": "ID   ASORS_PYRFU             Reviewed;         173 AA.\nAC   Q8U0V2; A0A5C0XS91;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 116.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, polyferredoxin-like subunit {ECO:0000305};\nDE   AltName: Full=Polyferredoxin-like protein {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=WOR5 small subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-S {ECO:0000303|PubMed:36269456};\nGN   OrderedLocusNames=PF1479 {ECO:0000312|EMBL:AAL81603.1};\nGN   ORFNames=PFDSM3638_07415 {ECO:0000312|EMBL:QEK79108.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:31.663381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510",
  "url": "https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aliphatic sulfonate oxidoreductase, polyferredoxin-like subunit {ECO:0000305};\nDE   AltName: Full=Polyferredoxin-like protein {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=WOR5 small subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-S {ECO:0000303|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:31.663381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510",
  "url": "https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) IN COMPLEX WITH IRON-SULFUR (4FE-4S)\nRP   CLUSTERS, FUNCTION, COFACTOR, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:31.663381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510",
  "url": "https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)

```json
{
  "entry_version": 116,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;\nCC         Evidence={ECO:0000269|PubMed:36269456};\nCC       Note=Binds 4 [4Fe-4S] clusters per subunit.\nCC       {ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:31.663381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510",
  "url": "https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
