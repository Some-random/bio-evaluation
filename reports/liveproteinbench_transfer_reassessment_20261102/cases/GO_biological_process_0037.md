# GO_biological_process_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0037.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — regulation of locomotion

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
A. envenomation resulting in negative regulation of voltage-gated potassium channel activity in another organism
B. regulation of locomotion
C. cytoplasmic translational elongation
D. amino acid activation for nonribosomal peptide biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched record annotates regulation of locomotion with IMP evidence, and the experimentally supported role in potassium-channel localization at muscle and presynaptic sites provides a plausible connection to locomotor regulation.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, soluble, predominantly alpha-helical sequence is consistent with a cytoskeletal/scaffolding protein, rather than a venom peptide, translation-elongation factor, or nonribosomal peptide-activating enzyme. Transferable knowledge that such scaffolds organize muscle or neuronal components makes regulation of locomotion a credible choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the sharply different alternatives provide a meaningful family/architecture-based distinction for B, even though they do not independently establish the specific locomotion phenotype.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives are distinct, and the experimental annotation supports B; none of the other choices is comparably supported by the sequence or the protein's reported role.


### Important caveats

- The direct GO annotation is experimental-inference evidence, not proof that locomotion regulation is the protein's sole or primary biological process.
- The source evidence is sequence-matched, but the author's exact annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, soluble, predominantly alpha-helical sequence is consistent with a cytoskeletal/scaffolding protein, rather than a venom peptide, translation-elongation factor, or nonribosomal peptide-activating enzyme. Transferable knowledge that such scaffolds organize muscle or neuronal components makes regulation of locomotion a credible choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the sharply different alternatives provide a meaningful family/architecture-based distinction for B, even though they do not independently establish the specific locomotion phenotype."
  },
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates regulation of locomotion with IMP evidence, and the experimentally supported role in potassium-channel localization at muscle and presynaptic sites provides a plausible connection to locomotor regulation."
  },
  "important_caveats": [
    "The direct GO annotation is experimental-inference evidence, not proof that locomotion regulation is the protein's sole or primary biological process.",
    "The source evidence is sequence-matched, but the author's exact annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the experimental annotation supports B; none of the other choices is comparably supported by the sequence or the protein's reported role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates regulation of locomotion with IMP evidence, and the experimentally supported role in potassium-channel localization at muscle and presynaptic sites provides a plausible connection to locomotor regulation.",
    "evidence_ids": ["C5", "C7", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, soluble, predominantly alpha-helical sequence is consistent with a cytoskeletal/scaffolding protein, rather than a venom peptide, translation-elongation factor, or nonribosomal peptide-activating enzyme. Transferable knowledge that such scaffolds organize muscle or neuronal components makes regulation of locomotion a credible choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the sharply different alternatives provide a meaningful family/architecture-based distinction for B, even though they do not independently establish the specific locomotion phenotype."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives are distinct, and the experimental annotation supports B; none of the other choices is comparably supported by the sequence or the protein's reported role."
  },
  "important_caveats": [
    "The direct GO annotation is experimental-inference evidence, not proof that locomotion regulation is the protein's sole or primary biological process.",
    "The source evidence is sequence-matched, but the author's exact annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO annotation GO:0040012 (regulation of locomotion) is assigned with IMP evidence (genetic manipulation) from PubMed:22577143, a strong experimental evidence code. The UniProt FUNCTION comment describes alpha-catulin (CTN-1) as required for slo-1 BK potassium channel localization to dense bodies in body wall muscle cells and for dystrophin complex maintenance in muscle, directly connecting the protein to neuromuscular function whose organismal readout in C. elegans is locomotion. Multiple independent publications (EMBO J 2010, PLoS Genet 2010, JBC 2012, Sci Rep 2019) support this muscle/neuromuscular role.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The three distractors are incompatible with the protein's identity as a eukaryotic structural/scaffolding protein. (A) Envenomation targeting voltage-gated K+ channels requires a small cysteine-rich venom peptide (typically 30-80 aa) from a venomous animal; this 784-aa eukaryotic protein has no such features. (C) Cytoplasmic translational elongation requires GTPase elongation factors (EF1A/EF2) or ribosomal proteins with characteristic nucleotide-binding and ribosome-interaction motifs absent here. (D) Amino acid activation for NRPS requires adenylation-domain architecture (A-T-C multi-domain, ~1000+ aa per module) found in bacterial/fungal NRPS systems, not in a nematode structural protein. By elimination, only (B) regulation of locomotion is compatible with a eukaryotic muscle/neuromuscular scaffolding protein. Furthermore, recognition of catenin-family sequence features (alpha-helical rod domain architecture, ~780 aa length, conserved N-terminal actin-binding region) connects to cell adhesion and cytoskeletal anchoring; in a motile organism, disruption of muscle-associated scaffolding proteins (like alpha-catulin/alpha-catenin family members) manifests as locomotion defects, a well-established paradigm in C. elegans genetics where muscle and neuromuscular-junction mutants are scored by locomotion assays.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Elimination of A, C, and D relies on general knowledge of protein families (venom peptides, translation factors, NRPS enzymes) and their sequence/size characteristics, which are clearly incompatible with this 784-aa eukaryotic structural protein. Positive support for B follows from recognizing catenin-family architecture and the well-known connection between muscle scaffolding proteins and locomotion phenotypes in model organisms. No fact specific to this exact protein's database entry is needed to distinguish the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only B is compatible with a eukaryotic structural/scaffolding protein involved in muscle or cell-adhesion biology. A, C, and D describe processes carried out by entirely different protein classes (venom peptides, translation elongation factors, NRPS adenylation domains) with no sequence or structural resemblance to this protein.


### Important caveats

- The organism (C. elegans) is not explicitly stated in the model input; the locomotion connection is strongest in that organism context, though the elimination reasoning for A/C/D holds regardless of organism.
- The protein is also annotated with 'cell adhesion' and 'Rho protein signal transduction' (IEA:InterPro), but neither is offered as a choice, so no ambiguity arises among the provided options.
- The IMP genetic evidence for GO:0040012 is specific to C. elegans muscle function; in other organisms, alpha-catenin homologs are more commonly associated with cell adhesion rather than locomotion per se.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The three distractors are incompatible with the protein's identity as a eukaryotic structural/scaffolding protein. (A) Envenomation targeting voltage-gated K+ channels requires a small cysteine-rich venom peptide (typically 30-80 aa) from a venomous animal; this 784-aa eukaryotic protein has no such features. (C) Cytoplasmic translational elongation requires GTPase elongation factors (EF1A/EF2) or ribosomal proteins with characteristic nucleotide-binding and ribosome-interaction motifs absent here. (D) Amino acid activation for NRPS requires adenylation-domain architecture (A-T-C multi-domain, ~1000+ aa per module) found in bacterial/fungal NRPS systems, not in a nematode structural protein. By elimination, only (B) regulation of locomotion is compatible with a eukaryotic muscle/neuromuscular scaffolding protein. Furthermore, recognition of catenin-family sequence features (alpha-helical rod domain architecture, ~780 aa length, conserved N-terminal actin-binding region) connects to cell adhesion and cytoskeletal anchoring; in a motile organism, disruption of muscle-associated scaffolding proteins (like alpha-catulin/alpha-catenin family members) manifests as locomotion defects, a well-established paradigm in C. elegans genetics where muscle and neuromuscular-junction mutants are scored by locomotion assays.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Elimination of A, C, and D relies on general knowledge of protein families (venom peptides, translation factors, NRPS enzymes) and their sequence/size characteristics, which are clearly incompatible with this 784-aa eukaryotic structural protein. Positive support for B follows from recognizing catenin-family architecture and the well-known connection between muscle scaffolding proteins and locomotion phenotypes in model organisms. No fact specific to this exact protein's database entry is needed to distinguish the options."
  },
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "C10",
      "C11",
      "C12",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The GO annotation GO:0040012 (regulation of locomotion) is assigned with IMP evidence (genetic manipulation) from PubMed:22577143, a strong experimental evidence code. The UniProt FUNCTION comment describes alpha-catulin (CTN-1) as required for slo-1 BK potassium channel localization to dense bodies in body wall muscle cells and for dystrophin complex maintenance in muscle, directly connecting the protein to neuromuscular function whose organismal readout in C. elegans is locomotion. Multiple independent publications (EMBO J 2010, PLoS Genet 2010, JBC 2012, Sci Rep 2019) support this muscle/neuromuscular role."
  },
  "important_caveats": [
    "The organism (C. elegans) is not explicitly stated in the model input; the locomotion connection is strongest in that organism context, though the elimination reasoning for A/C/D holds regardless of organism.",
    "The protein is also annotated with 'cell adhesion' and 'Rho protein signal transduction' (IEA:InterPro), but neither is offered as a choice, so no ambiguity arises among the provided options.",
    "The IMP genetic evidence for GO:0040012 is specific to C. elegans muscle function; in other organisms, alpha-catenin homologs are more commonly associated with cell adhesion rather than locomotion per se."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is compatible with a eukaryotic structural/scaffolding protein involved in muscle or cell-adhesion biology. A, C, and D describe processes carried out by entirely different protein classes (venom peptides, translation elongation factors, NRPS adenylation domains) with no sequence or structural resemblance to this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO annotation GO:0040012 (regulation of locomotion) is assigned with IMP evidence (genetic manipulation) from PubMed:22577143, a strong experimental evidence code. The UniProt FUNCTION comment describes alpha-catulin (CTN-1) as required for slo-1 BK potassium channel localization to dense bodies in body wall muscle cells and for dystrophin complex maintenance in muscle, directly connecting the protein to neuromuscular function whose organismal readout in C. elegans is locomotion. Multiple independent publications (EMBO J 2010, PLoS Genet 2010, JBC 2012, Sci Rep 2019) support this muscle/neuromuscular role.",
    "evidence_ids": ["C5", "C7", "C9", "C10", "C11", "C12", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The three distractors are incompatible with the protein's identity as a eukaryotic structural/scaffolding protein. (A) Envenomation targeting voltage-gated K+ channels requires a small cysteine-rich venom peptide (typically 30-80 aa) from a venomous animal; this 784-aa eukaryotic protein has no such features. (C) Cytoplasmic translational elongation requires GTPase elongation factors (EF1A/EF2) or ribosomal proteins with characteristic nucleotide-binding and ribosome-interaction motifs absent here. (D) Amino acid activation for NRPS requires adenylation-domain architecture (A-T-C multi-domain, ~1000+ aa per module) found in bacterial/fungal NRPS systems, not in a nematode structural protein. By elimination, only (B) regulation of locomotion is compatible with a eukaryotic muscle/neuromuscular scaffolding protein. Furthermore, recognition of catenin-family sequence features (alpha-helical rod domain architecture, ~780 aa length, conserved N-terminal actin-binding region) connects to cell adhesion and cytoskeletal anchoring; in a motile organism, disruption of muscle-associated scaffolding proteins (like alpha-catulin/alpha-catenin family members) manifests as locomotion defects, a well-established paradigm in C. elegans genetics where muscle and neuromuscular-junction mutants are scored by locomotion assays.",
    "missing_item_specific_fact": "",
    "reason": "Elimination of A, C, and D relies on general knowledge of protein families (venom peptides, translation factors, NRPS enzymes) and their sequence/size characteristics, which are clearly incompatible with this 784-aa eukaryotic structural protein. Positive support for B follows from recognizing catenin-family architecture and the well-known connection between muscle scaffolding proteins and locomotion phenotypes in model organisms. No fact specific to this exact protein's database entry is needed to distinguish the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is compatible with a eukaryotic structural/scaffolding protein involved in muscle or cell-adhesion biology. A, C, and D describe processes carried out by entirely different protein classes (venom peptides, translation elongation factors, NRPS adenylation domains) with no sequence or structural resemblance to this protein."
  },
  "important_caveats": [
    "The organism (C. elegans) is not explicitly stated in the model input; the locomotion connection is strongest in that organism context, though the elimination reasoning for A/C/D holds regardless of organism.",
    "The protein is also annotated with 'cell adhesion' and 'Rho protein signal transduction' (IEA:InterPro), but neither is offered as a choice, so no ambiguity arises among the provided options.",
    "The IMP genetic evidence for GO:0040012 is specific to C. elegans muscle function; in other organisms, alpha-catenin homologs are more commonly associated with cell adhesion rather than locomotion per se."
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
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20700105\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20865173\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22577143\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31308408\",\"source\":\"PubMed\"}],\"value\":\"Required for slo-1 potassium ion channel clustering at presynaptic terminals and in egg-laying muscles; clustering of slo-1 mediates the intoxicating and sedatory effects of ethanol on worms (PubMed:31308408). Required for slo-1 localization to dense bodies in body wall muscle cells (PubMed:20700105). Maintains the localization of the dystrophin complex near muscle cell dense bodies via its interaction with complex member dyb-1 which is required for slo-1 localization in muscle while slo-1 localization in neurons is independent of the dystrophin complex (PubMed:20865173, PubMed:22577143)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0007155\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:cell adhesion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
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
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"22577143\",\"source\":\"PubMed\"}],\"id\":\"GO:0040012\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:regulation of locomotion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:WormBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/24",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0007266\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:Rho protein signal transduction\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/25",
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

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C10",
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

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C11",
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

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G8JYB2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Oh K.H.\",\"Kim H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31308408\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-019-46615-9\"}],\"citationType\":\"journal article\",\"firstPage\":\"10224\",\"id\":\"31308408\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"10224\",\"publicationDate\":\"2019\",\"title\":\"BK channel clustering is required for normal behavioral alcohol sensitivity in C. elegans.\",\"volume\":\"9\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"MUTAGENESIS OF 144-ARG--ILE-784\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
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
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH SLO-1, TISSUE SPECIFICITY, AND MUTAGENESIS OF\nRP   358-ARG--ILE-784.\nRX   PubMed=20700105; DOI=10.1038/emboj.2010.194;\nRA   Chen B., Liu P., Wang S.J., Ge Q., Zhan H., Mohler W.A., Wang Z.W.;\nRT   \"alpha-Catulin CTN-1 is required for BK channel subcellular localization in\nRT   C. elegans body-wall muscle cells.\";\nRL   EMBO J. 29:3184-3195(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-29",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH DYB-1, TISSUE SPECIFICITY, DOMAIN, AND\nRP   MUTAGENESIS OF 382-ASN--ILE-416.\nRX   PubMed=22577143; DOI=10.1074/jbc.m112.369496;\nRA   Oh H.J., Abraham L.S., van Hengel J., Stove C., Proszynski T.J.,\nRA   Gevaert K., DiMario J.X., Sanes J.R., van Roy F., Kim H.;\nRT   \"Interaction of alpha-catulin with dystrobrevin contributes to integrity of\nRT   dystrophin complex in muscle.\";\nRL   J. Biol. Chem. 287:21717-21728(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-47",
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
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, AND MUTAGENESIS OF 144-ARG--ILE-784.\nRX   PubMed=31308408; DOI=10.1038/s41598-019-46615-9;\nRA   Oh K.H., Kim H.;\nRT   \"BK channel clustering is required for normal behavioral alcohol\nRT   sensitivity in C. elegans.\";\nRL   Sci. Rep. 9:10224-10224(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Required for slo-1 potassium ion channel clustering at\nCC       presynaptic terminals and in egg-laying muscles; clustering of slo-1\nCC       mediates the intoxicating and sedatory effects of ethanol on worms\nCC       (PubMed:31308408). Required for slo-1 localization to dense bodies in\nCC       body wall muscle cells (PubMed:20700105). Maintains the localization of\nCC       the dystrophin complex near muscle cell dense bodies via its\nCC       interaction with complex member dyb-1 which is required for slo-1\nCC       localization in muscle while slo-1 localization in neurons is\nCC       independent of the dystrophin complex (PubMed:20865173,\nCC       PubMed:22577143). {ECO:0000269|PubMed:20700105,\nCC       ECO:0000269|PubMed:20865173, ECO:0000269|PubMed:22577143,\nCC       ECO:0000269|PubMed:31308408}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0007155; P:cell adhesion; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0040012; P:regulation of locomotion; IMP:WormBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bf87987c82d82a88ea26dde006bb515a237f3e6146cef040ef28592e203d1ffa",
  "url": "https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G8JYB2?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0007266; P:Rho protein signal transduction; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:52.763286+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-119",
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
  "excerpt": "[Term]\nid: GO:0002182\nname: cytoplasmic translational elongation\nnamespace: biological_process\ndef: \"The successive addition of amino acid residues to a nascent polypeptide chain during protein biosynthesis in the cytoplasm.\" [GOC:hjd]\nis_a: GO:0006414 ! translational elongation\nrelationship: part_of GO:0002181 ! cytoplasmic translation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0002182",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 15691-15698",
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
  "excerpt": "[Term]\nid: GO:0040012\nname: regulation of locomotion\nnamespace: biological_process\ndef: \"Any process that modulates the frequency, rate or extent of locomotion of a cell or organism.\" [GOC:ems]\nis_a: GO:0050789 ! regulation of biological process\nrelationship: regulates GO:0040011 ! locomotion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0040012",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 233200-233207",
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
  "excerpt": "[Term]\nid: GO:0043041\nname: amino acid activation for nonribosomal peptide biosynthetic process\nnamespace: biological_process\ndef: \"Activation of an amino acid for incorporation into a peptide by a nonribosomal process.\" [GOC:jl]\nsynonym: \"nonribosomal amino acid activation\" RELATED []\nis_a: GO:0043038 ! amino acid activation\nrelationship: part_of GO:0019184 ! nonribosomal peptide biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043041",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 243406-243414",
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
  "excerpt": "[Term]\nid: GO:0044562\nname: venom-mediated inhibition of voltage-gated potassium channel activity\nnamespace: biological_process\ndef: \"A process in which an organism inhibits or disrupts the activity of a  voltage-gated potassium channel in another organism via the action of a venom.\" [GOC:fj, GOC:jl]\nsynonym: \"envenomation resulting in negative regulation of voltage-gated potassium channel activity in another organism\" EXACT []\nsynonym: \"envenomation resulting in negative regulation of voltage-gated potassium channel activity in other organism\" EXACT []\nis_a: GO:0044559 ! venom-mediated perturbation of voltage-gated potassium channel activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044562",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 258418-258426",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
