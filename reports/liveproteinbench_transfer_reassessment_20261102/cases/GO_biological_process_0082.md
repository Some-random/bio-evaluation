# GO_biological_process_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0082.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — MAPK cascade

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSKNIQRQRSISSISSRGVDRDRDPASGGLGLLSPYNSRSPLAGLHHSPGSLDATANQLSRPTFLLERKATEDIAKLDGVLFDDIPTLGSSNDHISSLGAGSPYPTINTSLAVTNPNYLSASSPGGPRRRANTASGPLSPAPPASPIDRLSKTTNRGSFVPSTARQPMNSQPPAPASSAPPPKQRTTSPSVASPPSQTRSQTVPYLSSNFGPTANMYGQRQPSGVDPSRPFHQVPLPPPPMSPPPAIGTINSIMTNIPPPPPRYPSAPAAAIHLPGPPGAPPPSGLPPPPGPPPNNTTNWQGTWIGAYGSYIPPPPPQQTHRPYNPQPYKTVNGQTIAIPPPPPPTESMQMSATYIPQGDSYGEGVGIPGLGMDDMAAWSATSQSSWLGGYNSIGSLAPTNASDTAASTPVDAYGSHNRDNSTTSNATSSGASGIPPELAAQWPLDRVLDWLQANNFSNDWRSTFRALDLHGNRFLEVGSANGGRGNFGMMHQLVYPRLAAECISSGTGWDQPREREEGKRMRRLIRHIVKGETPGTGMSSHTRKESISNTSLVPTSAGPDSGSPDTPIKAPGPGFSVGHPGGNHRKLLVGNFDDEGAHRRSPVASEPSEVGITFTERSSSNRGYSPAGSPAPTPGLFSSSTAPNLASSPGGRFGGHRNRNSTDSVSSNAAIYGSGVPPDASQVLRSQMNFGDMAKDTRRYGHDGGNRPSPLGDNASNGDRSAGASEPPGSAKEGKSFLSIFNHRKKKHHDDPDSPTSPMQHKSHSLGSRGNASETSLERPGSSVSTSHEHNTPASSMRSRRITTGRIFILATLDYWNYRMVDVSDVESASDLRQLICINLGLPDADGAQVYLTELGKFDHEDPLDDSQLVANKKVRADAAGSLKVFVRPGNMAGLAVNIGQSQNALSPAHLPAGAKMDEDTYARLNGQRRRSSSSPPASRQNTLTGGEHGKPTSTGADDDENKDPKSDDIAQQAEAHRIEMERKQQAYLAKRKHARENGNSPSENGTGSYTGIVGPKVIDFDEPRNSPFEDKKPFDSAFAPQRRAPAAPLDPSATLIKANSLSKRGSHQRNSQGSVDGFPSKRQGTGMTESPKHISEKRKPTNERQALGGIGAALAGMGRGLGGIAHPGGAGQRGTSPNRSSPGSAGESAGVASSTTDRGEDAKSRKPISSGNVSPTSSARTVSDEPPQLPKVVIKPRIFDGDSSSDEDSDDDSDDGLFAKPLAGRGGDDAAAKGKEPATKPVAKSPMSKHGTFWNDADSDGDEDPISESASNLNKRPSLTVNTKRGRKGLSVTFTSPDLPSSAGSKTAAGDEDDRSSRGSKRTPNTPHSEGWDSNNDKDVKLSRRKSFMEKDTSIWANRPPTDALINNLEDFFPNLDVDQPVLEEGELPGDLPPSPIAEAEEPHDQQQAKSMTTSRISNLYNDSDTLGSDESTLKALERPASIVSVARKNTRRSGGLGRMKSIREVAHKRYTQGAGAPPPVPAAPNNSNNSSSSGSKNSNLMRRKSTKMFNANIVQIRPERGSMILPQIPQDHLPSLPHNANNQIPKRQTTFRWFKGQLIGKGTYGRVYLGMNATTGEFLAVKEVEVNPKAAGGDKNKMKELVAALDQEIDTMQHLDHVNIVQYLGCERKETSISIFLEYIPGGSIGSCLRKHGKFEESVVSSLTRQTLSGLAYLHREGILHRDLKADNILLDVDGTAKISDFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK

[Multiple Choices]
A. protein polyubiquitination
B. MAPK cascade
C. determination of left/right symmetry
D. ribosomal small subunit assembly
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

> The matched protein is annotated as a MAP kinase kinase kinase in the mkh1-mkk1-spm1 MAPK cascade, with the function supported by experimental evidence (ECO:0000269). This supports choice B.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein kinase catalytic domain, including the HRDLK and DFG motifs, and a long, largely low-complexity regulatory region. A kinase of this sort is a credible contributor to a kinase-signaling cascade; among the choices, MAPK cascade fits, whereas polyubiquitination, left/right symmetry determination, and ribosomal subunit assembly do not fit the kinase-domain evidence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The conserved kinase-domain features provide a transferable basis for distinguishing the MAPK-cascade option from these alternatives. They do not by themselves establish the exact cascade or all of the protein's biological roles, but that finer identification is not needed to choose among the offered answers.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative offered is comparably supported by the recognizable kinase-domain features.


### Important caveats

- The sequence supports kinase activity and a signaling role more directly than it identifies a specific MAPK cascade; the matched experimental annotation supplies that target-specific support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain, including the HRDLK and DFG motifs, and a long, largely low-complexity regulatory region. A kinase of this sort is a credible contributor to a kinase-signaling cascade; among the choices, MAPK cascade fits, whereas polyubiquitination, left/right symmetry determination, and ribosomal subunit assembly do not fit the kinase-domain evidence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The conserved kinase-domain features provide a transferable basis for distinguishing the MAPK-cascade option from these alternatives. They do not by themselves establish the exact cascade or all of the protein's biological roles, but that finer identification is not needed to choose among the offered answers."
  },
  "case_id": "GO_biological_process_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched protein is annotated as a MAP kinase kinase kinase in the mkh1-mkk1-spm1 MAPK cascade, with the function supported by experimental evidence (ECO:0000269). This supports choice B."
  },
  "important_caveats": [
    "The sequence supports kinase activity and a signaling role more directly than it identifies a specific MAPK cascade; the matched experimental annotation supplies that target-specific support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered is comparably supported by the recognizable kinase-domain features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein is annotated as a MAP kinase kinase kinase in the mkh1-mkk1-spm1 MAPK cascade, with the function supported by experimental evidence (ECO:0000269). This supports choice B.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain, including the HRDLK and DFG motifs, and a long, largely low-complexity regulatory region. A kinase of this sort is a credible contributor to a kinase-signaling cascade; among the choices, MAPK cascade fits, whereas polyubiquitination, left/right symmetry determination, and ribosomal subunit assembly do not fit the kinase-domain evidence.",
    "missing_item_specific_fact": "",
    "reason": "The conserved kinase-domain features provide a transferable basis for distinguishing the MAPK-cascade option from these alternatives. They do not by themselves establish the exact cascade or all of the protein's biological roles, but that finer identification is not needed to choose among the offered answers."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered is comparably supported by the recognizable kinase-domain features."
  },
  "important_caveats": [
    "The sequence supports kinase activity and a signaling role more directly than it identifies a specific MAPK cascade; the matched experimental annotation supplies that target-specific support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A194W8T8) names the protein 'Mitogen-activated protein kinase kinase kinase mkh1' (EC 2.7.11.24) and describes its function as part of the mkh1-mkk1-spm1 MAPK cascade. The GO annotation GO:0000196 (cell integrity MAPK cascade) is_a GO:0051403 (stress-activated MAPK cascade) is_a GO:0000165 (MAPK cascade), so the option 'MAPK cascade' is a valid ancestral term for the protein's annotated biological process. The function comment (ECO:0000269, experimental evidence from PubMed:39631571) explicitly states participation in a MAPK cascade.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clearly identifiable protein kinase catalytic domain in the C-terminal region, with canonical motifs: the glycine-rich loop (GxGxxG-like 'GQLIGKGTYGR'), the VAIK catalytic lysine region, the HRD catalytic loop ('HRDLKADNILL'), the DFG motif ('DFGISKK'), and the APE motif ('APEVIRSQ'). This Ser/Thr kinase signature immediately eliminates options A (protein polyubiquitination requires E3/E2/E1 ligase domains such as RING, HECT, or UBC folds), C (determination of left/right symmetry is an animal developmental process involving ciliary signaling, Nodal, etc., irrelevant to a fungal kinase), and D (ribosomal small subunit assembly involves ribosomal proteins and assembly factors, not kinase domains). The overall architecture—a very long (~1300+ residue) N-terminal low-complexity/proline-rich regulatory region followed by a C-terminal kinase domain—is the hallmark of MAPKKKs (MAP3Ks) in fungi, analogous to S. cerevisiae Bck1 (~1827 aa, CWI pathway MAPKKK). Even without identifying the exact tier, recognizing a protein kinase among the four options uniquely points to MAPK cascade, as the other three processes do not have a kinase as their primary functional component.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the protein kinase domain from conserved sequence motifs (HRD, DFG, VAIK, glycine-rich loop) and recognize the long-N-terminal/C-terminal-kinase architecture as characteristic of MAPKKKs. Among the four offered choices, only 'MAPK cascade' involves a protein kinase as the primary functional unit, making the discrimination achievable through transferable knowledge of kinase domain recognition and the known architecture of MAPKKK family members (e.g., Bck1 in S. cerevisiae, MEKK1 in mammals).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase domain is unambiguous and none of the distractor processes (ubiquitination, left/right symmetry, ribosomal assembly) involve a protein kinase as their primary functional mechanism. The specific annotation 'cell integrity MAPK cascade' is a child of the offered 'MAPK cascade' term, making B the correct and only defensible choice.


### Important caveats

- The UniProt GO annotation is IEA (Inferred from Electronic Annotation) via ARBA, but the function statement is supported by experimental evidence (ECO:0000269, PubMed:39631571).
- The option 'MAPK cascade' (GO:0000165) is the grandparent of the specific annotation 'cell integrity MAPK cascade' (GO:0000196); the question asks for the 'primary biological process,' which the broader cascade term adequately captures.
- The organism (Cytospora mali, a fungus) is not stated in the model input but can be inferred from sequence composition and the absence of animal-specific features; this supports excluding option C (left/right symmetry, an animal developmental process).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clearly identifiable protein kinase catalytic domain in the C-terminal region, with canonical motifs: the glycine-rich loop (GxGxxG-like 'GQLIGKGTYGR'), the VAIK catalytic lysine region, the HRD catalytic loop ('HRDLKADNILL'), the DFG motif ('DFGISKK'), and the APE motif ('APEVIRSQ'). This Ser/Thr kinase signature immediately eliminates options A (protein polyubiquitination requires E3/E2/E1 ligase domains such as RING, HECT, or UBC folds), C (determination of left/right symmetry is an animal developmental process involving ciliary signaling, Nodal, etc., irrelevant to a fungal kinase), and D (ribosomal small subunit assembly involves ribosomal proteins and assembly factors, not kinase domains). The overall architecture—a very long (~1300+ residue) N-terminal low-complexity/proline-rich regulatory region followed by a C-terminal kinase domain—is the hallmark of MAPKKKs (MAP3Ks) in fungi, analogous to S. cerevisiae Bck1 (~1827 aa, CWI pathway MAPKKK). Even without identifying the exact tier, recognizing a protein kinase among the four options uniquely points to MAPK cascade, as the other three processes do not have a kinase as their primary functional component.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein kinase domain from conserved sequence motifs (HRD, DFG, VAIK, glycine-rich loop) and recognize the long-N-terminal/C-terminal-kinase architecture as characteristic of MAPKKKs. Among the four offered choices, only 'MAPK cascade' involves a protein kinase as the primary functional unit, making the discrimination achievable through transferable knowledge of kinase domain recognition and the known architecture of MAPKKK family members (e.g., Bck1 in S. cerevisiae, MEKK1 in mammals)."
  },
  "case_id": "GO_biological_process_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A194W8T8) names the protein 'Mitogen-activated protein kinase kinase kinase mkh1' (EC 2.7.11.24) and describes its function as part of the mkh1-mkk1-spm1 MAPK cascade. The GO annotation GO:0000196 (cell integrity MAPK cascade) is_a GO:0051403 (stress-activated MAPK cascade) is_a GO:0000165 (MAPK cascade), so the option 'MAPK cascade' is a valid ancestral term for the protein's annotated biological process. The function comment (ECO:0000269, experimental evidence from PubMed:39631571) explicitly states participation in a MAPK cascade."
  },
  "important_caveats": [
    "The UniProt GO annotation is IEA (Inferred from Electronic Annotation) via ARBA, but the function statement is supported by experimental evidence (ECO:0000269, PubMed:39631571).",
    "The option 'MAPK cascade' (GO:0000165) is the grandparent of the specific annotation 'cell integrity MAPK cascade' (GO:0000196); the question asks for the 'primary biological process,' which the broader cascade term adequately captures.",
    "The organism (Cytospora mali, a fungus) is not stated in the model input but can be inferred from sequence composition and the absence of animal-specific features; this supports excluding option C (left/right symmetry, an animal developmental process)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase domain is unambiguous and none of the distractor processes (ubiquitination, left/right symmetry, ribosomal assembly) involve a protein kinase as their primary functional mechanism. The specific annotation 'cell integrity MAPK cascade' is a child of the offered 'MAPK cascade' term, making B the correct and only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A194W8T8) names the protein 'Mitogen-activated protein kinase kinase kinase mkh1' (EC 2.7.11.24) and describes its function as part of the mkh1-mkk1-spm1 MAPK cascade. The GO annotation GO:0000196 (cell integrity MAPK cascade) is_a GO:0051403 (stress-activated MAPK cascade) is_a GO:0000165 (MAPK cascade), so the option 'MAPK cascade' is a valid ancestral term for the protein's annotated biological process. The function comment (ECO:0000269, experimental evidence from PubMed:39631571) explicitly states participation in a MAPK cascade.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO2", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clearly identifiable protein kinase catalytic domain in the C-terminal region, with canonical motifs: the glycine-rich loop (GxGxxG-like 'GQLIGKGTYGR'), the VAIK catalytic lysine region, the HRD catalytic loop ('HRDLKADNILL'), the DFG motif ('DFGISKK'), and the APE motif ('APEVIRSQ'). This Ser/Thr kinase signature immediately eliminates options A (protein polyubiquitination requires E3/E2/E1 ligase domains such as RING, HECT, or UBC folds), C (determination of left/right symmetry is an animal developmental process involving ciliary signaling, Nodal, etc., irrelevant to a fungal kinase), and D (ribosomal small subunit assembly involves ribosomal proteins and assembly factors, not kinase domains). The overall architecture—a very long (~1300+ residue) N-terminal low-complexity/proline-rich regulatory region followed by a C-terminal kinase domain—is the hallmark of MAPKKKs (MAP3Ks) in fungi, analogous to S. cerevisiae Bck1 (~1827 aa, CWI pathway MAPKKK). Even without identifying the exact tier, recognizing a protein kinase among the four options uniquely points to MAPK cascade, as the other three processes do not have a kinase as their primary functional component.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the protein kinase domain from conserved sequence motifs (HRD, DFG, VAIK, glycine-rich loop) and recognize the long-N-terminal/C-terminal-kinase architecture as characteristic of MAPKKKs. Among the four offered choices, only 'MAPK cascade' involves a protein kinase as the primary functional unit, making the discrimination achievable through transferable knowledge of kinase domain recognition and the known architecture of MAPKKK family members (e.g., Bck1 in S. cerevisiae, MEKK1 in mammals)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase domain is unambiguous and none of the distractor processes (ubiquitination, left/right symmetry, ribosomal assembly) involve a protein kinase as their primary functional mechanism. The specific annotation 'cell integrity MAPK cascade' is a child of the offered 'MAPK cascade' term, making B the correct and only defensible choice."
  },
  "important_caveats": [
    "The UniProt GO annotation is IEA (Inferred from Electronic Annotation) via ARBA, but the function statement is supported by experimental evidence (ECO:0000269, PubMed:39631571).",
    "The option 'MAPK cascade' (GO:0000165) is the grandparent of the specific annotation 'cell integrity MAPK cascade' (GO:0000196); the question asks for the 'primary biological process,' which the broader cascade term adequately captures.",
    "The organism (Cytospora mali, a fungus) is not stated in the model input but can be inferred from sequence composition and the absence of animal-specific features; this supports excluding option C (left/right symmetry, an animal developmental process)."
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
  "benchmark_sequence_length": 1849,
  "benchmark_sequence_sha256": "21169fd5c9ada96ecaccfcc8b1582efbb6293bd310fe994f922fdeb56b88895a",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-10-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1849,
  "current_source_sequence_sha256": "21169fd5c9ada96ecaccfcc8b1582efbb6293bd310fe994f922fdeb56b88895a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A194W8T8",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "selected_historical_source_sequence_length": 1849,
  "selected_historical_source_sequence_sha256": "21169fd5c9ada96ecaccfcc8b1582efbb6293bd310fe994f922fdeb56b88895a",
  "selected_historical_version": {
    "accession": "A0A194W8T8",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MKH1_CYTMA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A194W8T8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-10-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Apple Valsa canker fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Diaporthales\",\"Cytosporaceae\",\"Cytospora\"],\"scientificName\":\"Cytospora mali\",\"synonyms\":[\"Valsa mali\"],\"taxonId\":578113}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"value\":\"2.7.11.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"value\":\"Mitogen-activated protein kinase kinase kinase mkh1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"value\":\"MAP kinase kinase kinase mkh1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"value\":\"MAPKKK mkh1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"value\":\"Mitogen-activated protein kinase kinase kinase, part of the mkh1-mkk1-spm1 MAPK cascade that regulates vegetative growth, conidial formation, colony surface hydrophobicity, osmotic stress, cell wall integrity maintenance, carbon and nitrogen source utilization, chitin distribution, septa formation, and pathogenicity\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000196\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:cell integrity MAPK cascade\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Diao Y.\",\"Xiong X.\",\"Jin J.\",\"Yu C.\",\"Tian Y.\",\"Zhao C.\",\"Wu Y.\",\"Liu H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39631571\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.micpath.2024.107194\"}],\"citationType\":\"journal article\",\"firstPage\":\"107194\",\"id\":\"39631571\",\"journal\":\"Microb. Pathog.\",\"lastPage\":\"107194\",\"publicationDate\":\"2025\",\"title\":\"Mitogen-activated protein (MAP) kinase signalling pathway VmMkh1-VmMkk1-VmSpm1 regulates cell wall integrity in Valsamali.\",\"volume\":\"198\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:41.396358+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36",
  "url": "https://rest.uniprot.org/uniprotkb/A0A194W8T8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   MKH1_CYTMA              Reviewed;        1849 AA.\nAC   A0A194W8T8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-OCT-2016, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Mitogen-activated protein kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};\nDE            Short=MAP kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};\nDE            Short=MAPKKK mkh1 {ECO:0000303|PubMed:39631571};\nDE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};\nGN   Name=mkh1 {ECO:0000303|PubMed:39631571}; ORFNames=VM1G_08015;\nOS   Cytospora mali (Apple Valsa canker fungus) (Valsa mali).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Diaporthales; Cytosporaceae; Cytospora.\nOX   NCBI_TaxID=578113;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39631571; DOI=10.1016/j.micpath.2024.107194;\nRA   Diao Y., Xiong X., Jin J., Yu C., Tian Y., Zhao C., Wu Y., Liu H.;\nRT   \"Mitogen-activated protein (MAP) kinase signalling pathway VmMkh1-VmMkk1-\nRT   VmSpm1 regulates cell wall integrity in Valsamali.\";\nRL   Microb. Pathog. 198:107194-107194(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Mitogen-activated protein kinase kinase kinase, part of the\nCC       mkh1-mkk1-spm1 MAPK cascade that regulates vegetative growth, conidial\nCC       formation, colony surface hydrophobicity, osmotic stress, cell wall\nCC       integrity maintenance, carbon and nitrogen source utilization, chitin\nCC       distribution, septa formation, and pathogenicity.\nCC       {ECO:0000269|PubMed:39631571}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0000196; P:cell integrity MAPK cascade; IEA:UniProtKB-ARBA.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0048315; P:conidium formation; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0030435; P:sporulation resulting in formation of a cellular spore; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000028\nname: ribosomal small subunit assembly\nnamespace: biological_process\ndef: \"The aggregation, arrangement and bonding together of constituent RNAs and proteins to form the small ribosomal subunit.\" [GOC:jl, PMID:30467428]\nsynonym: \"30S ribosomal subunit assembly\" NARROW [GOC:mah]\nsynonym: \"40S ribosomal subunit assembly\" NARROW [GOC:mah]\nis_a: GO:0022618 ! protein-RNA complex assembly\nrelationship: part_of GO:0042255 ! ribosome assembly\nrelationship: part_of GO:0042274 ! ribosomal small subunit biogenesis\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000028",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 306-316",
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
  "excerpt": "[Term]\nid: GO:0000165\nname: MAPK cascade\nnamespace: biological_process\nalt_id: GO:0007255\ndef: \"An intracellular protein kinase cascade containing at least a MAP kinase (MAPK). It starts with the activation of a MAP3K, and the consecutive activation of a MPK2K and a MAPK. The cascade can also contain an additional tier: the upstream MAP4K. The kinases in each tier phosphorylate and activate the kinase in the downstream tier to transmit a signal within a cell.\" [PMID:20811974, PMID:9561267]\ncomment: MAPK cascades lie downstream of many cell surface receptors and cooperate in transmitting various extracellular signals to the nucleus. One way by which the specificity of each cascade is regulated is through the existence of several distinct components in each tier of the different cascades. The cascades are typically named according to the component in the MAPK tier.\nsynonym: \"ERK/MAPK cascade\" NARROW []\nsynonym: \"MAP kinase cascade\" EXACT []\nsynonym: \"MAP kinase kinase kinase cascade\" EXACT []\nsynonym: \"MAPK signal transduction\" EXACT [GOC:signaling]\nsynonym: \"MAPK signaling\" RELATED []\nsynonym: \"MAPK signalling\" RELATED []\nsynonym: \"MAPKKK cascade\" EXACT []\nsynonym: \"MAPKKK cascade during sporulation\" NARROW []\nsynonym: \"mitogen-activated protein kinase cascade\" EXACT [GOC:bf]\nxref: Reactome:R-HSA-169893 \"Prolonged ERK activation events\"\nxref: Reactome:R-HSA-5673001 \"RAF/MAP kinase cascade\"\nxref: Wikipedia:MAPK_cascade\nxref: Wikipedia:Mitogen-activated_protein_kinase\nis_a: GO:0141124 ! intracellular signaling cassette\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000165",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1649-1670",
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
  "excerpt": "[Term]\nid: GO:0000196\nname: cell integrity MAPK cascade\nnamespace: biological_process\ndef: \"A MAPK cascade that specifically ensures the maintenance and regulation of cellular structure in response to external signals, including plasma membrane stretching or cell wall alteration, to coordinate cellular responses such as growth, differentiation, and stress adaptation, thereby preserving cell integrity. Contains the  SLT2 (S.cerevisiae)/Pmk1 (S.pombe) MAP kinase or orthologs.\" [GOC:vw]\nsynonym: \"cell integrity MAPK pathway\" EXACT [GOC:vw, PMID:23934882]\nsynonym: \"cell wall integrity MAPK cascade\" NARROW []\nsynonym: \"CWI pathway\" RELATED []\nsynonym: \"Mpk1 cascade\" NARROW [PMID:10523653]\nsynonym: \"Pmk1 MAPK cell integrity signaling\" NARROW [PMID:20032302]\nsynonym: \"Pmk1 mitogen-activated protein kinase (MAPK) cell integrity pathway\" NARROW [PMID:23934882]\nsynonym: \"PMK1-MAPK signal transduction pathway\" NARROW [PMID:23454094]\nsynonym: \"Slt2 cascade\" NARROW [PMID:10523653]\nis_a: GO:0051403 ! stress-activated MAPK cascade\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000196",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1969-1983",
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
  "excerpt": "[Term]\nid: GO:0000209\nname: protein polyubiquitination\nnamespace: biological_process\ndef: \"Addition of multiple ubiquitin groups to a protein, forming a ubiquitin chain.\" [PMID:26906419]\nsynonym: \"polyubiquitin\" RELATED []\nsynonym: \"protein polyubiquitinylation\" EXACT []\nsynonym: \"protein polyubiquitylation\" EXACT []\nxref: Reactome:R-HSA-983168 \"Antigen processing: Ubiquitination & Proteasome degradation\"\nis_a: GO:0016567 ! protein ubiquitination\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000209",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 2121-2131",
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
  "excerpt": "[Term]\nid: GO:0007368\nname: determination of left/right symmetry\nnamespace: biological_process\ndef: \"The establishment of an organism's body plan or part of an organism with respect to the left and right halves. The pattern can either be symmetric, such that the halves are mirror images, or asymmetric where the pattern deviates from this symmetry.\" [GOC:dph, GOC:jid]\nsynonym: \"determination of left/right asymmetry\" EXACT [GOC:dph]\nis_a: GO:0009855 ! determination of bilateral symmetry\nrelationship: part_of GO:0060972 ! left/right pattern formation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0007368",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 75940-75948",
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
  "excerpt": "[Term]\nid: GO:0051403\nname: stress-activated MAPK cascade\nnamespace: biological_process\ndef: \"A MAPK cascade that starts with the activation of a stress-activated MAP kinase cascade.\" [GOC:ai, PMID:15936270]\nsynonym: \"MAPK11 cascade\" NARROW [GOC:add]\nsynonym: \"MAPK12 cascade\" NARROW [GOC:add]\nsynonym: \"MAPK13 cascade\" NARROW [GOC:add]\nsynonym: \"MAPK14 cascade\" RELATED []\nsynonym: \"SAPK cascade\" BROAD [GOC:add]\nsynonym: \"stress-activated MAPK signaling pathway\" EXACT []\nsynonym: \"stress-activated MAPK signalling pathway\" EXACT []\nsynonym: \"stress-activated MAPKKK cascade\" EXACT []\nsynonym: \"stress-activated MAPKKK signaling pathway\" EXACT []\nsynonym: \"stress-activated MAPKKK signalling pathway\" EXACT []\nxref: Reactome:R-HSA-450294 \"MAP kinase activation\"\nis_a: GO:0000165 ! MAPK cascade\nis_a: GO:0031098 ! stress-activated protein kinase signaling cascade\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051403",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 326368-326386",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
