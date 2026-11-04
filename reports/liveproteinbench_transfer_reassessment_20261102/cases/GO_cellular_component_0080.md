# GO_cellular_component_0080

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0080.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAASSMSSLTSSYHTTAMPSSNSVVPPFDARNLEIKTKSIEQTLIPLVTQITTLVNYKESYMASGKPKSERAMRAALKIGSAVEAAIERFVCVGETIADENADIQPEMYDACTEARLAGASMANLSCACNDDPNSVVDKAVLVRASRQLLSSVTRVLLLADRVLVKQVLRAEDKIAFSLSRLESTRSFNDFVKVFAVFGGEMVELAHRSGDRQHDLKSEKRKAQMSIARTSLERLTMLLLTASKTYLRHPDCDSALQCRDGVFYQMKLSLELIAICVCDGILTTEKSRYIQDEPDMPIDIALQLTANAAIKQLTEMLEMIRMTVRVGAGVRERIVSALDALCQLTQDFTDSAYTPHHQREQILDFLEECRFEMTNLIQPDENEQLAASGLEVTVERLNRRLKDLSKQLQIVAMEQISEVLRANEDQVLLSSMKACAVSGDIDGVEKYMHKFREHADHMQEVCRLLHHISITDALHVHTGHVERNMRALAPLTILAGRTLCVHPSSRIARENLEVFCDTWGQAVNDLSRVAKESDVAANGRVAAEKQAYMSLPRPGKHGTTQKPSKPITLDVEDQQKMAKVGLEMKLLTSEVDAEAEKWDEYAENDIVKRAKAMSSMAYNMYLFTRGDGPLKTTHDLFTQAEFFAEQANQMYRTVREFSYEVPGSAEKSDLSAILERIPLHCQQLQVMVKSPTVGKTATFGKVDSVIQETKNLMNEIAKLVTASFVCATKYEIEFRGGSVNGRTGADGERTSRESTVWRRTPSIRRAAPPTSSHLSANNSSSIHI

[Multiple Choices]
A. virus tail, tube
B. endoplasmic reticulum
C. plasma membrane
D. microtubule cytoskeleton
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched record has an experimentally supported GO annotation to plasma membrane (IDA: WormBase). A separate annotation places the protein in the cytoplasm near muscle dense bodies; that is compatible with a peripheral or context-dependent plasma-membrane association, rather than contradicting choice C.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, largely helical sequence lacks an evident signal peptide or transmembrane segment, making an integral ER or plasma-membrane protein unlikely. Its scaffold-like architecture is consistent with catulin/catenin-family proteins, which can associate with cortical or membrane complexes; that gives a transferable, probabilistic basis for plasma membrane over the specifically microtubule-associated alternative. This supports a peripheral association, not membrane insertion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level scaffold inference meaningfully favor C among these choices, although they do not establish localization as decisively as the target-specific experimental annotation does.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cytoplasmic dense-body localization does not itself make another offered choice equally defensible; the evidence also supports a plasma-membrane annotation.


### Important caveats

- The experimental plasma-membrane GO annotation and cytoplasmic localization are distinct annotations; neither establishes that plasma membrane is the protein's sole or primary location in every cell context.
- The exact target identity and its annotations were reviewer-only and are not used as original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, largely helical sequence lacks an evident signal peptide or transmembrane segment, making an integral ER or plasma-membrane protein unlikely. Its scaffold-like architecture is consistent with catulin/catenin-family proteins, which can associate with cortical or membrane complexes; that gives a transferable, probabilistic basis for plasma membrane over the specifically microtubule-associated alternative. This supports a peripheral association, not membrane insertion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level scaffold inference meaningfully favor C among these choices, although they do not establish localization as decisively as the target-specific experimental annotation does."
  },
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record has an experimentally supported GO annotation to plasma membrane (IDA: WormBase). A separate annotation places the protein in the cytoplasm near muscle dense bodies; that is compatible with a peripheral or context-dependent plasma-membrane association, rather than contradicting choice C."
  },
  "important_caveats": [
    "The experimental plasma-membrane GO annotation and cytoplasmic localization are distinct annotations; neither establishes that plasma membrane is the protein's sole or primary location in every cell context.",
    "The exact target identity and its annotations were reviewer-only and are not used as original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cytoplasmic dense-body localization does not itself make another offered choice equally defensible; the evidence also supports a plasma-membrane annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record has an experimentally supported GO annotation to plasma membrane (IDA: WormBase). A separate annotation places the protein in the cytoplasm near muscle dense bodies; that is compatible with a peripheral or context-dependent plasma-membrane association, rather than contradicting choice C.",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, largely helical sequence lacks an evident signal peptide or transmembrane segment, making an integral ER or plasma-membrane protein unlikely. Its scaffold-like architecture is consistent with catulin/catenin-family proteins, which can associate with cortical or membrane complexes; that gives a transferable, probabilistic basis for plasma membrane over the specifically microtubule-associated alternative. This supports a peripheral association, not membrane insertion.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level scaffold inference meaningfully favor C among these choices, although they do not establish localization as decisively as the target-specific experimental annotation does."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cytoplasmic dense-body localization does not itself make another offered choice equally defensible; the evidence also supports a plasma-membrane annotation."
  },
  "important_caveats": [
    "The experimental plasma-membrane GO annotation and cytoplasmic localization are distinct annotations; neither establishes that plasma membrane is the protein's sole or primary location in every cell context.",
    "The exact target identity and its annotations were reviewer-only and are not used as original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (G8JYB2, Alpha-catulin/CTN-1 from C. elegans) carries a GO:0005886 (plasma membrane) annotation with IDA evidence (evidence_id C6, H4). The protein interacts with the dystrophin complex and BK channels at the muscle cell periphery. However, the primary SUBCELLULAR LOCATION comment states 'Cytoplasm' with a note 'Localizes near dense bodies in muscle cells' (C5, H3). Since 'Cytoplasm' is not among the offered options and 'plasma membrane' is explicitly annotated with experimental evidence, the author's key of C is supported by the available annotation, though with the caveat that the primary location comment is 'Cytoplasm' rather than 'plasma membrane.'

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> From the 784-aa sequence alone, a knowledgeable model can eliminate three options: (A) virus tail/tube is excluded because the sequence is clearly eukaryotic in composition and length with no viral capsid/tail protein features; (B) endoplasmic reticulum is excluded because there is no N-terminal signal peptide or transmembrane domain characteristic of ER-resident or ER-targeted proteins; (D) microtubule cytoskeleton is excluded because the sequence lacks tubulin motifs, kinesin/dynein motor domains, or typical MAP structural features. This leaves C (plasma membrane) as the only viable option. Additionally, transferable knowledge about the catulin/catenin superfamily (alpha-catenin, p120-catenin, alpha-catulin) supports peripheral membrane association: these are large alpha-helical repeat proteins that scaffold at the cell periphery, linking cytoskeleton to membrane complexes. The sequence's overall composition (no TM helices, no signal peptide, large size, alpha-helical character) is consistent with a peripheral membrane-associated adaptor protein, a pattern shared with catenins, vinculin, and talin—all annotated as plasma membrane in GO despite being cytoplasmic in a strict sense.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of three clearly wrong options (viral, ER, microtubule) combined with general knowledge about large cytoplasmic adaptor/scaffold proteins at the cell periphery being annotated as 'plasma membrane' in GO provides a credible transferable inference. The catulin/catenin family association with the cell periphery is a well-established pattern across multiple proteins (alpha-catenin at adherens junctions, p120-catenin at cell-cell contacts, alpha-catulin at dense bodies near the sarcolemma), making this a legitimate family-level inference rather than a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt primary SUBCELLULAR LOCATION comment says 'Cytoplasm' rather than 'plasma membrane,' 'Cytoplasm' is not among the four offered choices. Among A, B, C, D, only C is defensible: A is impossible (eukaryotic protein), B is excluded (no signal peptide/TM), D is excluded (no microtubule-protein features). The GO:0005886 annotation with IDA evidence confirms C as the best match among the given options.


### Important caveats

- The UniProt primary SUBCELLULAR LOCATION annotation is 'Cytoplasm' (near dense bodies), not 'plasma membrane.' The plasma membrane GO term (GO:0005886) is a secondary annotation. This creates a slight tension with the question's phrasing 'primary Cellular Component,' but since 'Cytoplasm' is not an option, C remains the best answer.
- The protein is from C. elegans (nematode), not a mammalian system; the dense body is the invertebrate analog of the focal adhesion/sarcolemma complex.
- The reviewer-only evidence confirms sequence match (784 aa, SHA256 matched) but the evaluated model had no access to the UniProt accession, organism name, or protein name.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the 784-aa sequence alone, a knowledgeable model can eliminate three options: (A) virus tail/tube is excluded because the sequence is clearly eukaryotic in composition and length with no viral capsid/tail protein features; (B) endoplasmic reticulum is excluded because there is no N-terminal signal peptide or transmembrane domain characteristic of ER-resident or ER-targeted proteins; (D) microtubule cytoskeleton is excluded because the sequence lacks tubulin motifs, kinesin/dynein motor domains, or typical MAP structural features. This leaves C (plasma membrane) as the only viable option. Additionally, transferable knowledge about the catulin/catenin superfamily (alpha-catenin, p120-catenin, alpha-catulin) supports peripheral membrane association: these are large alpha-helical repeat proteins that scaffold at the cell periphery, linking cytoskeleton to membrane complexes. The sequence's overall composition (no TM helices, no signal peptide, large size, alpha-helical character) is consistent with a peripheral membrane-associated adaptor protein, a pattern shared with catenins, vinculin, and talin—all annotated as plasma membrane in GO despite being cytoplasmic in a strict sense.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three clearly wrong options (viral, ER, microtubule) combined with general knowledge about large cytoplasmic adaptor/scaffold proteins at the cell periphery being annotated as 'plasma membrane' in GO provides a credible transferable inference. The catulin/catenin family association with the cell periphery is a well-established pattern across multiple proteins (alpha-catenin at adherens junctions, p120-catenin at cell-cell contacts, alpha-catulin at dense bodies near the sarcolemma), making this a legitimate family-level inference rather than a lookup of this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (G8JYB2, Alpha-catulin/CTN-1 from C. elegans) carries a GO:0005886 (plasma membrane) annotation with IDA evidence (evidence_id C6, H4). The protein interacts with the dystrophin complex and BK channels at the muscle cell periphery. However, the primary SUBCELLULAR LOCATION comment states 'Cytoplasm' with a note 'Localizes near dense bodies in muscle cells' (C5, H3). Since 'Cytoplasm' is not among the offered options and 'plasma membrane' is explicitly annotated with experimental evidence, the author's key of C is supported by the available annotation, though with the caveat that the primary location comment is 'Cytoplasm' rather than 'plasma membrane.'"
  },
  "important_caveats": [
    "The UniProt primary SUBCELLULAR LOCATION annotation is 'Cytoplasm' (near dense bodies), not 'plasma membrane.' The plasma membrane GO term (GO:0005886) is a secondary annotation. This creates a slight tension with the question's phrasing 'primary Cellular Component,' but since 'Cytoplasm' is not an option, C remains the best answer.",
    "The protein is from C. elegans (nematode), not a mammalian system; the dense body is the invertebrate analog of the focal adhesion/sarcolemma complex.",
    "The reviewer-only evidence confirms sequence match (784 aa, SHA256 matched) but the evaluated model had no access to the UniProt accession, organism name, or protein name."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt primary SUBCELLULAR LOCATION comment says 'Cytoplasm' rather than 'plasma membrane,' 'Cytoplasm' is not among the four offered choices. Among A, B, C, D, only C is defensible: A is impossible (eukaryotic protein), B is excluded (no signal peptide/TM), D is excluded (no microtubule-protein features). The GO:0005886 annotation with IDA evidence confirms C as the best match among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (G8JYB2, Alpha-catulin/CTN-1 from C. elegans) carries a GO:0005886 (plasma membrane) annotation with IDA evidence (evidence_id C6, H4). The protein interacts with the dystrophin complex and BK channels at the muscle cell periphery. However, the primary SUBCELLULAR LOCATION comment states 'Cytoplasm' with a note 'Localizes near dense bodies in muscle cells' (C5, H3). Since 'Cytoplasm' is not among the offered options and 'plasma membrane' is explicitly annotated with experimental evidence, the author's key of C is supported by the available annotation, though with the caveat that the primary location comment is 'Cytoplasm' rather than 'plasma membrane.'",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "From the 784-aa sequence alone, a knowledgeable model can eliminate three options: (A) virus tail/tube is excluded because the sequence is clearly eukaryotic in composition and length with no viral capsid/tail protein features; (B) endoplasmic reticulum is excluded because there is no N-terminal signal peptide or transmembrane domain characteristic of ER-resident or ER-targeted proteins; (D) microtubule cytoskeleton is excluded because the sequence lacks tubulin motifs, kinesin/dynein motor domains, or typical MAP structural features. This leaves C (plasma membrane) as the only viable option. Additionally, transferable knowledge about the catulin/catenin superfamily (alpha-catenin, p120-catenin, alpha-catulin) supports peripheral membrane association: these are large alpha-helical repeat proteins that scaffold at the cell periphery, linking cytoskeleton to membrane complexes. The sequence's overall composition (no TM helices, no signal peptide, large size, alpha-helical character) is consistent with a peripheral membrane-associated adaptor protein, a pattern shared with catenins, vinculin, and talin—all annotated as plasma membrane in GO despite being cytoplasmic in a strict sense.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of three clearly wrong options (viral, ER, microtubule) combined with general knowledge about large cytoplasmic adaptor/scaffold proteins at the cell periphery being annotated as 'plasma membrane' in GO provides a credible transferable inference. The catulin/catenin family association with the cell periphery is a well-established pattern across multiple proteins (alpha-catenin at adherens junctions, p120-catenin at cell-cell contacts, alpha-catulin at dense bodies near the sarcolemma), making this a legitimate family-level inference rather than a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt primary SUBCELLULAR LOCATION comment says 'Cytoplasm' rather than 'plasma membrane,' 'Cytoplasm' is not among the four offered choices. Among A, B, C, D, only C is defensible: A is impossible (eukaryotic protein), B is excluded (no signal peptide/TM), D is excluded (no microtubule-protein features). The GO:0005886 annotation with IDA evidence confirms C as the best match among the given options."
  },
  "important_caveats": [
    "The UniProt primary SUBCELLULAR LOCATION annotation is 'Cytoplasm' (near dense bodies), not 'plasma membrane.' The plasma membrane GO term (GO:0005886) is a secondary annotation. This creates a slight tension with the question's phrasing 'primary Cellular Component,' but since 'Cytoplasm' is not an option, C remains the best answer.",
    "The protein is from C. elegans (nematode), not a mammalian system; the dense body is the invertebrate analog of the focal adhesion/sarcolemma complex.",
    "The reviewer-only evidence confirms sequence match (784 aa, SHA256 matched) but the evaluated model had no access to the UniProt accession, organism name, or protein name."
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
  "benchmark_sequence_length": 784,
  "benchmark_sequence_sha256": "79cca718e7db69cfd4d632efd2b31e25301f477c1a5619d65bbc76401e5844d7",
  "current_entry_audit": {
    "entryVersion": 85,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2012-01-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 784,
  "current_source_sequence_sha256": "79cca718e7db69cfd4d632efd2b31e25301f477c1a5619d65bbc76401e5844d7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G8JYB2",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "selected_historical_source_sequence_length": 784,
  "selected_historical_source_sequence_sha256": "79cca718e7db69cfd4d632efd2b31e25301f477c1a5619d65bbc76401e5844d7",
  "selected_historical_version": {
    "accession": "G8JYB2",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CTNL1_CAEEL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G8JYB2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":85,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2012-01-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001940\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Nematoda\",\"Chromadorea\",\"Rhabditida\",\"Rhabditina\",\"Rhabditomorpha\",\"Rhabditoidea\",\"Rhabditidae\",\"Peloderinae\",\"Caenorhabditis\"],\"scientificName\":\"Caenorhabditis elegans\",\"taxonId\":6239}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"Y23H5A.5d\",\"source\":\"WormBase\"}],\"value\":\"Alpha-catulin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20865173\",\"source\":\"PubMed\"}],\"value\":\"Localizes near dense bodies in muscle cells\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20865173\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22577143\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:WormBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"20700105\",\"source\":\"PubMed\"}],\"id\":\"GO:0055120\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:striated muscle dense body\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:WormBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen B.\",\"Liu P.\",\"Wang S.J.\",\"Ge Q.\",\"Zhan H.\",\"Mohler W.A.\",\"Wang Z.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20700105\"},{\"database\":\"DOI\",\"id\":\"10.1038/emboj.2010.194\"}],\"citationType\":\"journal article\",\"firstPage\":\"3184\",\"id\":\"20700105\",\"journal\":\"EMBO J.\",\"lastPage\":\"3195\",\"publicationDate\":\"2010\",\"title\":\"alpha-Catulin CTN-1 is required for BK channel subcellular localization in C. elegans body-wall muscle cells.\",\"volume\":\"29\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH SLO-1\",\"TISSUE SPECIFICITY\",\"MUTAGENESIS OF 358-ARG--ILE-784\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Abraham L.S.\",\"Oh H.J.\",\"Sancar F.\",\"Richmond J.E.\",\"Kim H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20865173\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pgen.1001077\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"20865173\",\"journal\":\"PLoS Genet.\",\"lastPage\":\"0\",\"publicationDate\":\"2010\",\"title\":\"An alpha-catulin homologue controls neuromuscular function through localization of the dystrophin complex and BK channels in Caenorhabditis elegans.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH SLO-1\",\"TISSUE SPECIFICITY\",\"MUTAGENESIS OF 144-ARG--ILE-784 AND 521-GLN--ILE-784\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Oh H.J.\",\"Abraham L.S.\",\"van Hengel J.\",\"Stove C.\",\"Proszynski T.J.\",\"Gevaert K.\",\"DiMario J.X.\",\"Sanes J.R.\",\"van Roy F.\",\"Kim H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22577143\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m112.369496\"}],\"citationType\":\"journal article\",\"firstPage\":\"21717\",\"id\":\"22577143\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"21728\",\"publicationDate\":\"2012\",\"title\":\"Interaction of alpha-catulin with dystrobrevin contributes to integrity of dystrophin complex in muscle.\",\"volume\":\"287\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH DYB-1\",\"TISSUE SPECIFICITY\",\"DOMAIN\",\"MUTAGENESIS OF 382-ASN--ILE-416\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:28:48.044451+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce687c63aaebfe277622b8edcb694e92a3682a393304c42138b7010357d3f75b",
  "url": "https://rest.uniprot.org/uniprotkb/G8JYB2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   CTNL1_CAEEL             Reviewed;         784 AA.\nAC   G8JYB2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-JAN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Alpha-catulin {ECO:0000312|WormBase:Y23H5A.5d};\nGN   Name=ctn-1 {ECO:0000312|WormBase:Y23H5A.5d};\nGN   ORFNames=Y23H5A.5 {ECO:0000312|WormBase:Y23H5A.5d};\nOS   Caenorhabditis elegans.\nOC   Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;\nOC   Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;\nOC   Caenorhabditis.\nOX   NCBI_TaxID=6239 {ECO:0000312|Proteomes:UP000001940};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH SLO-1, TISSUE SPECIFICITY, AND MUTAGENESIS OF\nRP   144-ARG--ILE-784 AND 521-GLN--ILE-784.\nRX   PubMed=20865173; DOI=10.1371/journal.pgen.1001077;\nRA   Abraham L.S., Oh H.J., Sancar F., Richmond J.E., Kim H.;\nRT   \"An alpha-catulin homologue controls neuromuscular function through\nRT   localization of the dystrophin complex and BK channels in Caenorhabditis\nRT   elegans.\";\nRL   PLoS Genet. 6:0-0(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:20865173}.\nCC       Note=Localizes near dense bodies in muscle cells.\nCC       {ECO:0000269|PubMed:20865173}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:WormBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0055120; C:striated muscle dense body; IDA:WormBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59450-59472",
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
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0015630\nname: microtubule cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of microtubules and associated proteins.\" [GOC:jl, ISBN:0395825172]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015630",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119409-119415",
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
  "excerpt": "[Term]\nid: GO:0098026\nname: virus tail, tube\nnamespace: cellular_component\ndef: \"The internal tube of the tail of some viruses. The virus tail tube is the channel for DNA ejection into the host cytoplasm.\" [PMID:33188213, VZ:3960]\ncomment: Applies in particular the Myoviridae bacteriophages. Many bacteriophages with dsDNA genomes, or Caudovirales, have a tail. The viral tail can be short (Podoviridae), long and non-contractile (Siphoviridae) or long and contractile (Myoviridae). The tail is the channel through which the phage genome is injected into the host bacterial cell.\nsynonym: \"bacteriophage tail tube\" NARROW [GOC:bm]\nxref: VZ:3960 \"Viral tail tube protein\"\nis_a: GO:0044423 ! virion component\nrelationship: part_of GO:0098015 ! virus tail\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098026",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 408367-408377",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
