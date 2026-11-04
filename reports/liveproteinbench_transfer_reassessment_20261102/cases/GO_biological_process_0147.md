# GO_biological_process_0147

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0147.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **C** — chorismate biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. transsulfuration
B. neuropeptide signaling pathway
C. chorismate biosynthetic process
D. peroxisome organization
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

> The sequence-matched record identifies the protein as chorismate synthase and reports experimentally supported conversion of EPSP to chorismate, which directly supports chorismate biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme in the conserved chorismate-synthase family. Family knowledge connects that enzyme to conversion of EPSP into chorismate, distinguishing option C from transsulfuration, neuropeptide signaling, and peroxisome organization. This is a family-level inference, not a claim of certain identification from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of the enzyme family and its conserved pathway role gives a meaningful basis to choose C among these alternatives; the exact protein's database annotation is not necessary for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct processes, and chorismate production specifically supports C.


### Important caveats

- The sequence-based family inference is probabilistic; the reviewer-only sequence-matched record provides stronger, experimentally supported confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the conserved chorismate-synthase family. Family knowledge connects that enzyme to conversion of EPSP into chorismate, distinguishing option C from transsulfuration, neuropeptide signaling, and peroxisome organization. This is a family-level inference, not a claim of certain identification from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the enzyme family and its conserved pathway role gives a meaningful basis to choose C among these alternatives; the exact protein's database annotation is not necessary for that distinction."
  },
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as chorismate synthase and reports experimentally supported conversion of EPSP to chorismate, which directly supports chorismate biosynthesis."
  },
  "important_caveats": [
    "The sequence-based family inference is probabilistic; the reviewer-only sequence-matched record provides stronger, experimentally supported confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct processes, and chorismate production specifically supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record identifies the protein as chorismate synthase and reports experimentally supported conversion of EPSP to chorismate, which directly supports chorismate biosynthesis.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme in the conserved chorismate-synthase family. Family knowledge connects that enzyme to conversion of EPSP into chorismate, distinguishing option C from transsulfuration, neuropeptide signaling, and peroxisome organization. This is a family-level inference, not a claim of certain identification from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the enzyme family and its conserved pathway role gives a meaningful basis to choose C among these alternatives; the exact protein's database annotation is not necessary for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct processes, and chorismate production specifically supports C."
  },
  "important_caveats": [
    "The sequence-based family inference is probabilistic; the reviewer-only sequence-matched record provides stronger, experimentally supported confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is Chorismate synthase (AROC_PLAVS, UniProt A5K264) from Plasmodium vivax. It is annotated with EC 4.2.3.5 (chorismate synthase), catalyzes EPSP → chorismate (experimental evidence, PubMed:31381947), and is explicitly assigned GO:0009423 'chorismate biosynthetic process' (evidence C8, H7). The pathway annotation states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C6, H4). The expected answer C is directly and strongly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~547 aa) contains a flavin-binding domain with recognizable motifs (e.g., 'GDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNL...') characteristic of flavin-dependent enzymes. Among the four options: (A) Transsulfuration enzymes (cystathionine β-synthase, cystathionine γ-lyase) are PLP-dependent and have distinct PLP-binding motifs not present here. (B) Neuropeptide signaling involves small peptide precursors or 7-TM GPCRs — the sequence shows neither signal peptides for secreted peptides nor transmembrane helices. (D) Peroxisome organization requires PEX proteins with specific domain architectures and/or PTS1/PTS2 targeting signals (SKL-type C-terminal tripeptide or N-terminal nonapeptide), neither of which is present. This leaves (C) chorismate biosynthetic process as the only viable option for a flavin-binding enzyme of this size. Chorismate synthase is the most prominent flavin-dependent enzyme in amino acid biosynthesis, and the bifunctional CS/flavin reductase architecture (with a C-terminal flavin reductase domain) is a well-documented family feature in parasite CS enzymes. A knowledgeable model can eliminate A, B, D by domain/architecture mismatch and identify C as the only flavin-dependent biosynthetic enzyme among the choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The three distractors (transsulfuration, neuropeptide signaling, peroxisome organization) are eliminable by standard domain/architecture reasoning: no PLP motifs, no GPCR/peptide-precursor features, no PEX domains or PTS signals. The remaining option (chorismate biosynthetic process) is the only one compatible with a flavin-binding enzyme of this size, and chorismate synthase is the canonical flavin-dependent enzyme in aromatic amino acid biosynthesis. Family-level knowledge of flavin-dependent enzymes and the shikimate pathway allows a positive inference toward C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different biological processes with distinct protein architectures. Transsulfuration (PLP enzymes), neuropeptide signaling (peptide precursors/GPCRs), and peroxisome organization (PEX proteins) are clearly incompatible with the observed sequence features. Chorismate biosynthetic process is the only option consistent with a flavin-binding enzyme of this size and architecture.


### Important caveats

- The GO annotation for chorismate biosynthetic process (GO:0009423) is assigned via IEA (Inferred from Electronic Annotation) in both the current and historical records, not by direct experimental GO assignment. However, the enzymatic function (chorismate synthase activity) is experimentally verified (ECO:0000269, PubMed:31381947).
- The bifunctional nature (CS + flavin reductase) is an experimentally demonstrated property specific to Plasmodium CS; the flavin reductase activity alone does not change the primary biological process assignment.
- The protein is from Plasmodium vivax, a parasite that retains the shikimate pathway (unlike humans), which is a well-known drug-target rationale but does not alter the GO process assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~547 aa) contains a flavin-binding domain with recognizable motifs (e.g., 'GDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNL...') characteristic of flavin-dependent enzymes. Among the four options: (A) Transsulfuration enzymes (cystathionine β-synthase, cystathionine γ-lyase) are PLP-dependent and have distinct PLP-binding motifs not present here. (B) Neuropeptide signaling involves small peptide precursors or 7-TM GPCRs — the sequence shows neither signal peptides for secreted peptides nor transmembrane helices. (D) Peroxisome organization requires PEX proteins with specific domain architectures and/or PTS1/PTS2 targeting signals (SKL-type C-terminal tripeptide or N-terminal nonapeptide), neither of which is present. This leaves (C) chorismate biosynthetic process as the only viable option for a flavin-binding enzyme of this size. Chorismate synthase is the most prominent flavin-dependent enzyme in amino acid biosynthesis, and the bifunctional CS/flavin reductase architecture (with a C-terminal flavin reductase domain) is a well-documented family feature in parasite CS enzymes. A knowledgeable model can eliminate A, B, D by domain/architecture mismatch and identify C as the only flavin-dependent biosynthetic enzyme among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The three distractors (transsulfuration, neuropeptide signaling, peroxisome organization) are eliminable by standard domain/architecture reasoning: no PLP motifs, no GPCR/peptide-precursor features, no PEX domains or PTS signals. The remaining option (chorismate biosynthetic process) is the only one compatible with a flavin-binding enzyme of this size, and chorismate synthase is the canonical flavin-dependent enzyme in aromatic amino acid biosynthesis. Family-level knowledge of flavin-dependent enzymes and the shikimate pathway allows a positive inference toward C."
  },
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Chorismate synthase (AROC_PLAVS, UniProt A5K264) from Plasmodium vivax. It is annotated with EC 4.2.3.5 (chorismate synthase), catalyzes EPSP → chorismate (experimental evidence, PubMed:31381947), and is explicitly assigned GO:0009423 'chorismate biosynthetic process' (evidence C8, H7). The pathway annotation states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C6, H4). The expected answer C is directly and strongly supported."
  },
  "important_caveats": [
    "The GO annotation for chorismate biosynthetic process (GO:0009423) is assigned via IEA (Inferred from Electronic Annotation) in both the current and historical records, not by direct experimental GO assignment. However, the enzymatic function (chorismate synthase activity) is experimentally verified (ECO:0000269, PubMed:31381947).",
    "The bifunctional nature (CS + flavin reductase) is an experimentally demonstrated property specific to Plasmodium CS; the flavin reductase activity alone does not change the primary biological process assignment.",
    "The protein is from Plasmodium vivax, a parasite that retains the shikimate pathway (unlike humans), which is a well-known drug-target rationale but does not alter the GO process assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different biological processes with distinct protein architectures. Transsulfuration (PLP enzymes), neuropeptide signaling (peptide precursors/GPCRs), and peroxisome organization (PEX proteins) are clearly incompatible with the observed sequence features. Chorismate biosynthetic process is the only option consistent with a flavin-binding enzyme of this size and architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is Chorismate synthase (AROC_PLAVS, UniProt A5K264) from Plasmodium vivax. It is annotated with EC 4.2.3.5 (chorismate synthase), catalyzes EPSP → chorismate (experimental evidence, PubMed:31381947), and is explicitly assigned GO:0009423 'chorismate biosynthetic process' (evidence C8, H7). The pathway annotation states 'chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7' (C6, H4). The expected answer C is directly and strongly supported.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~547 aa) contains a flavin-binding domain with recognizable motifs (e.g., 'GDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNL...') characteristic of flavin-dependent enzymes. Among the four options: (A) Transsulfuration enzymes (cystathionine β-synthase, cystathionine γ-lyase) are PLP-dependent and have distinct PLP-binding motifs not present here. (B) Neuropeptide signaling involves small peptide precursors or 7-TM GPCRs — the sequence shows neither signal peptides for secreted peptides nor transmembrane helices. (D) Peroxisome organization requires PEX proteins with specific domain architectures and/or PTS1/PTS2 targeting signals (SKL-type C-terminal tripeptide or N-terminal nonapeptide), neither of which is present. This leaves (C) chorismate biosynthetic process as the only viable option for a flavin-binding enzyme of this size. Chorismate synthase is the most prominent flavin-dependent enzyme in amino acid biosynthesis, and the bifunctional CS/flavin reductase architecture (with a C-terminal flavin reductase domain) is a well-documented family feature in parasite CS enzymes. A knowledgeable model can eliminate A, B, D by domain/architecture mismatch and identify C as the only flavin-dependent biosynthetic enzyme among the choices.",
    "missing_item_specific_fact": "",
    "reason": "The three distractors (transsulfuration, neuropeptide signaling, peroxisome organization) are eliminable by standard domain/architecture reasoning: no PLP motifs, no GPCR/peptide-precursor features, no PEX domains or PTS signals. The remaining option (chorismate biosynthetic process) is the only one compatible with a flavin-binding enzyme of this size, and chorismate synthase is the canonical flavin-dependent enzyme in aromatic amino acid biosynthesis. Family-level knowledge of flavin-dependent enzymes and the shikimate pathway allows a positive inference toward C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different biological processes with distinct protein architectures. Transsulfuration (PLP enzymes), neuropeptide signaling (peptide precursors/GPCRs), and peroxisome organization (PEX proteins) are clearly incompatible with the observed sequence features. Chorismate biosynthetic process is the only option consistent with a flavin-binding enzyme of this size and architecture."
  },
  "important_caveats": [
    "The GO annotation for chorismate biosynthetic process (GO:0009423) is assigned via IEA (Inferred from Electronic Annotation) in both the current and historical records, not by direct experimental GO assignment. However, the enzymatic function (chorismate synthase activity) is experimentally verified (ECO:0000269, PubMed:31381947).",
    "The bifunctional nature (CS + flavin reductase) is an experimentally demonstrated property specific to Plasmodium CS; the flavin reductase activity alone does not change the primary biological process assignment.",
    "The protein is from Plasmodium vivax, a parasite that retains the shikimate pathway (unlike humans), which is a well-known drug-target rationale but does not alter the GO process assignment."
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
  "benchmark_sequence_length": 547,
  "benchmark_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "current_entry_audit": {
    "entryVersion": 65,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-02-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 547,
  "current_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 64,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A5K264",
  "selected_historical_entry_version": 64,
  "selected_historical_record_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "selected_historical_source_sequence_length": 547,
  "selected_historical_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "selected_historical_version": {
    "accession": "A5K264",
    "database": "Swiss-Prot",
    "entryVersion": 64,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "AROC_PLAVS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A5K264\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":65,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-02-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008333\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax (strain Salvador I)\",\"taxonId\":126793}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional chorismate synthase and flavin reductase (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a flavin reductase (FR) able to generate reduced flavin mononucleotide in the presence of NADPH (PubMed:31381947)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q12640\",\"source\":\"UniProtKB\"}],\"value\":\"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009073\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:aromatic amino acid family biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009423\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:chorismate biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H1",
  "excerpt": "ID   AROC_PLAVS              Reviewed;         547 AA.\nAC   A5K264;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-FEB-2011, sequence version 1.\nDT   28-JAN-2026, entry version 64.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:31381947};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; ORFNames=PVX_114265 {ECO:0000312|EMBL:EDL46514.1};\nOS   Plasmodium vivax (strain Salvador I).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Bifunctional chorismate synthase and flavin reductase\nCC       (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate\nCC       3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a\nCC       flavin reductase (FR) able to generate reduced flavin mononucleotide in\nCC       the presence of NADPH (PubMed:31381947). {ECO:0000269|PubMed:31381947}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;\nCC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step\nCC       7/7. {ECO:0000250|UniProtKB:Q12640}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0008652; P:amino acid biosynthetic process; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0009073; P:aromatic amino acid family biosynthetic process; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0009423; P:chorismate biosynthetic process; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0007031\nname: peroxisome organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of a peroxisome. A peroxisome is a small, membrane-bounded organelle that uses dioxygen (O2) to oxidize organic molecules.\" [GOC:mah]\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_pombe\nsubset: goslim_yeast\nsynonym: \"peroxisome organisation\" EXACT []\nsynonym: \"peroxisome organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0006996 ! organelle organization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007031",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 72605-72618",
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
  "excerpt": "[Term]\nid: GO:0007218\nname: neuropeptide signaling pathway\nnamespace: biological_process\ndef: \"A G protein-coupled receptor signaling pathway initiated by a neuropeptide binding to its receptor on the surface of a target cell, and ending with the regulation of a downstream cellular process.\" [GOC:mah, ISBN:0815316194]\nsynonym: \"neuropeptide signalling pathway\" EXACT []\nis_a: GO:0007186 ! G protein-coupled receptor signaling pathway\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007218",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 74547-74554",
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
  "excerpt": "[Term]\nid: GO:0009423\nname: chorismate biosynthetic process\nnamespace: biological_process\nalt_id: GO:0033587\ndef: \"The chemical reactions and pathways resulting in the formation of the unsymmetrical ether derived from phosphoenolpyruvate and 5-phosphoshikimic acid formed as an intermediate in the biosynthesis of aromatic amino acids and many other compounds.\" [GOC:sm, ISBN:0198547684]\nsynonym: \"chorismate anabolism\" EXACT []\nsynonym: \"chorismate biosynthesis\" EXACT []\nsynonym: \"chorismate formation\" EXACT []\nsynonym: \"chorismate synthesis\" EXACT []\nsynonym: \"shikimate anabolism\" RELATED []\nsynonym: \"shikimate biosynthesis\" RELATED []\nsynonym: \"shikimate biosynthetic process\" RELATED []\nsynonym: \"shikimate pathway\" EXACT []\nsynonym: \"shikimate synthesis\" RELATED []\nxref: MetaCyc:ARO-PWY\nxref: MetaCyc:PWY-6163\nxref: MetaCyc:PWY-6165\nis_a: GO:0043650 ! dicarboxylic acid biosynthetic process\nis_a: GO:0046417 ! chorismate metabolic process\nproperty_value: skos:narrowMatch MetaCyc:ARO-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-6163\nproperty_value: skos:narrowMatch MetaCyc:PWY-6165\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009423",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 96113-96136",
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
  "excerpt": "[Term]\nid: GO:0019346\nname: transsulfuration\nnamespace: biological_process\ndef: \"The interconversion of homocysteine and cysteine via cystathionine. In contrast with enteric bacteria and mammals, Saccharomyces cerevisiae has two transsulfuration pathways employing two separate sets of enzymes.\" [MetaCyc:PWY-801]\nsynonym: \"homocysteine-cysteine interconversion\" NARROW []\nsynonym: \"transsulphuration\" EXACT []\nxref: MetaCyc:PWY-801\nxref: Reactome:R-HSA-1614603 \"Cysteine formation from homocysteine\"\nxref: Wikipedia:Transsulfuration_pathway\nis_a: GO:0050667 ! homocysteine metabolic process\nis_a: GO:0170039 ! proteinogenic amino acid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019346",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 148273-148285",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
