# EC_number_0013

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0013.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.7.11.24

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
A. 2.7.13.3
B. 2.3.1.318
C. 2.1.1.353
D. 2.7.11.24
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches the cited UniProt entry, which assigns EC 2.7.11.24 and records serine- and threonine-phosphorylation reactions with evidence linked to a publication. This supports the key, though the database evidence code reflects curator inference from the literature rather than, by itself, proof of a specific assay.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable eukaryotic protein-kinase catalytic domain near its C-terminus, including conserved kinase motifs such as HRDLK and DFG. Its context is consistent with a signaling kinase. Transferable knowledge of kinase families supports a serine/threonine protein kinase (D), rather than a histidine kinase (A), acyltransferase (B), or methyltransferase (C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase-domain sequence features and the offered alternatives meaningfully distinguish the serine/threonine protein-kinase option. Assigning the more specific MAPKKK subtype may be less certain from sequence alone, but the alternatives do not require distinguishing it from other serine/threonine kinase EC entries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the protein-kinase domain supports D; the other options describe distinct enzyme classes.


### Important caveats

- The reviewer-only database annotation supports the key but was not part of the original model input.
- Sequence features support the kinase class more directly than the exact MAPKKK subtype.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain near its C-terminus, including conserved kinase motifs such as HRDLK and DFG. Its context is consistent with a signaling kinase. Transferable knowledge of kinase families supports a serine/threonine protein kinase (D), rather than a histidine kinase (A), acyltransferase (B), or methyltransferase (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase-domain sequence features and the offered alternatives meaningfully distinguish the serine/threonine protein-kinase option. Assigning the more specific MAPKKK subtype may be less certain from sequence alone, but the alternatives do not require distinguishing it from other serine/threonine kinase EC entries."
  },
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.7.11.24 and records serine- and threonine-phosphorylation reactions with evidence linked to a publication. This supports the key, though the database evidence code reflects curator inference from the literature rather than, by itself, proof of a specific assay."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the key but was not part of the original model input.",
    "Sequence features support the kinase class more directly than the exact MAPKKK subtype."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the protein-kinase domain supports D; the other options describe distinct enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.7.11.24 and records serine- and threonine-phosphorylation reactions with evidence linked to a publication. This supports the key, though the database evidence code reflects curator inference from the literature rather than, by itself, proof of a specific assay.",
    "evidence_ids": ["H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain near its C-terminus, including conserved kinase motifs such as HRDLK and DFG. Its context is consistent with a signaling kinase. Transferable knowledge of kinase families supports a serine/threonine protein kinase (D), rather than a histidine kinase (A), acyltransferase (B), or methyltransferase (C).",
    "missing_item_specific_fact": "",
    "reason": "The kinase-domain sequence features and the offered alternatives meaningfully distinguish the serine/threonine protein-kinase option. Assigning the more specific MAPKKK subtype may be less certain from sequence alone, but the alternatives do not require distinguishing it from other serine/threonine kinase EC entries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the protein-kinase domain supports D; the other options describe distinct enzyme classes."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the key but was not part of the original model input.",
    "Sequence features support the kinase class more directly than the exact MAPKKK subtype."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A194W8T8, MKH1_CYTMA) assigns EC 2.7.11.24 (MAP kinase kinase kinase) with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:39631571. The catalytic activity comments confirm L-seryl-&#91;protein&#93; + ATP → O-phospho-L-seryl-&#91;protein&#93; + ADP + H+ and L-threonyl-&#91;protein&#93; + ATP → O-phospho-L-threonyl-&#91;protein&#93; + ADP + H+, both under EC 2.7.11.24. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains unmistakable protein kinase domain signatures: the catalytic HRD motif ('HRDLKADNILLDVDG'), the DFG motif ('DFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK'), and a glycine-rich loop. These are hallmarks of the eukaryotic protein kinase (ePK) fold, which phosphorylates Ser/Thr residues. This immediately eliminates B (2.3.1.318, an acyltransferase with a completely different fold) and C (2.1.1.353, a methyltransferase). Option A (2.7.13.3, histidine kinase) uses a completely different phosphorelay mechanism (HisKA/HATPase_c/HisD domains) and does not possess the classical HRD/DFG protein kinase fold, so it can be excluded. The remaining option D (2.7.11.24, MAPKKK) is the only Ser/Thr protein kinase among the choices. Furthermore, the large N-terminal region rich in Ser/Thr residues and proline-rich stretches is architecturally consistent with MAPKKK-family proteins (e.g., RAF, MEKK, MLKK analogs in fungi), which have extensive regulatory N-terminal domains preceding the kinase domain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered alternatives span four distinct enzyme classes (Ser/Thr kinase, His kinase, acyltransferase, methyltransferase). The presence of the canonical ePK fold with HRD and DFG motifs is a transferable diagnostic feature learned from hundreds of characterized protein kinases. This feature positively identifies the protein as a Ser/Thr kinase and negatively excludes histidine kinases (different fold/mechanism), transferases, and methyltransferases. Since only one Ser/Thr kinase option (2.7.11.24) is offered, the model does not need to distinguish among multiple 2.7.11.x subtypes. The large regulatory N-terminal region with Ser/Thr-rich stretches further supports MAPKKK architecture over, say, a simple monomeric kinase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options belong to four different EC subclasses (2.7.13, 2.3.1, 2.1.1, 2.7.11). The sequence's clear ePK fold with HRD/DFG motifs unambiguously places it in the protein Ser/Thr kinase class (2.7.11.x), and only one such option is offered. No other choice is defensible given the sequence evidence.


### Important caveats

- The specific 4-digit assignment 2.7.11.24 (MAPKKK) vs. other 2.7.11.x numbers (e.g., 2.7.11.1, 2.7.11.22) is not independently derivable from the sequence alone; however, since only 2.7.11.24 is offered among the choices, the multiple-choice format resolves this.
- The UniProt annotation uses ECO:0000305 (inferred from direct assay) tied to a 2025 publication, indicating experimental validation of the kinase activity, though the specific MAPKKK designation may involve pathway context beyond pure sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains unmistakable protein kinase domain signatures: the catalytic HRD motif ('HRDLKADNILLDVDG'), the DFG motif ('DFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK'), and a glycine-rich loop. These are hallmarks of the eukaryotic protein kinase (ePK) fold, which phosphorylates Ser/Thr residues. This immediately eliminates B (2.3.1.318, an acyltransferase with a completely different fold) and C (2.1.1.353, a methyltransferase). Option A (2.7.13.3, histidine kinase) uses a completely different phosphorelay mechanism (HisKA/HATPase_c/HisD domains) and does not possess the classical HRD/DFG protein kinase fold, so it can be excluded. The remaining option D (2.7.11.24, MAPKKK) is the only Ser/Thr protein kinase among the choices. Furthermore, the large N-terminal region rich in Ser/Thr residues and proline-rich stretches is architecturally consistent with MAPKKK-family proteins (e.g., RAF, MEKK, MLKK analogs in fungi), which have extensive regulatory N-terminal domains preceding the kinase domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives span four distinct enzyme classes (Ser/Thr kinase, His kinase, acyltransferase, methyltransferase). The presence of the canonical ePK fold with HRD and DFG motifs is a transferable diagnostic feature learned from hundreds of characterized protein kinases. This feature positively identifies the protein as a Ser/Thr kinase and negatively excludes histidine kinases (different fold/mechanism), transferases, and methyltransferases. Since only one Ser/Thr kinase option (2.7.11.24) is offered, the model does not need to distinguish among multiple 2.7.11.x subtypes. The large regulatory N-terminal region with Ser/Thr-rich stretches further supports MAPKKK architecture over, say, a simple monomeric kinase."
  },
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A194W8T8, MKH1_CYTMA) assigns EC 2.7.11.24 (MAP kinase kinase kinase) with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:39631571. The catalytic activity comments confirm L-seryl-[protein] + ATP → O-phospho-L-seryl-[protein] + ADP + H+ and L-threonyl-[protein] + ATP → O-phospho-L-threonyl-[protein] + ADP + H+, both under EC 2.7.11.24. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The specific 4-digit assignment 2.7.11.24 (MAPKKK) vs. other 2.7.11.x numbers (e.g., 2.7.11.1, 2.7.11.22) is not independently derivable from the sequence alone; however, since only 2.7.11.24 is offered among the choices, the multiple-choice format resolves this.",
    "The UniProt annotation uses ECO:0000305 (inferred from direct assay) tied to a 2025 publication, indicating experimental validation of the kinase activity, though the specific MAPKKK designation may involve pathway context beyond pure sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four different EC subclasses (2.7.13, 2.3.1, 2.1.1, 2.7.11). The sequence's clear ePK fold with HRD/DFG motifs unambiguously places it in the protein Ser/Thr kinase class (2.7.11.x), and only one such option is offered. No other choice is defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A194W8T8, MKH1_CYTMA) assigns EC 2.7.11.24 (MAP kinase kinase kinase) with evidence code ECO:0000305 (inferred from direct assay) linked to PubMed:39631571. The catalytic activity comments confirm L-seryl-[protein] + ATP → O-phospho-L-seryl-[protein] + ADP + H+ and L-threonyl-[protein] + ATP → O-phospho-L-threonyl-[protein] + ADP + H+, both under EC 2.7.11.24. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains unmistakable protein kinase domain signatures: the catalytic HRD motif ('HRDLKADNILLDVDG'), the DFG motif ('DFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK'), and a glycine-rich loop. These are hallmarks of the eukaryotic protein kinase (ePK) fold, which phosphorylates Ser/Thr residues. This immediately eliminates B (2.3.1.318, an acyltransferase with a completely different fold) and C (2.1.1.353, a methyltransferase). Option A (2.7.13.3, histidine kinase) uses a completely different phosphorelay mechanism (HisKA/HATPase_c/HisD domains) and does not possess the classical HRD/DFG protein kinase fold, so it can be excluded. The remaining option D (2.7.11.24, MAPKKK) is the only Ser/Thr protein kinase among the choices. Furthermore, the large N-terminal region rich in Ser/Thr residues and proline-rich stretches is architecturally consistent with MAPKKK-family proteins (e.g., RAF, MEKK, MLKK analogs in fungi), which have extensive regulatory N-terminal domains preceding the kinase domain.",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives span four distinct enzyme classes (Ser/Thr kinase, His kinase, acyltransferase, methyltransferase). The presence of the canonical ePK fold with HRD and DFG motifs is a transferable diagnostic feature learned from hundreds of characterized protein kinases. This feature positively identifies the protein as a Ser/Thr kinase and negatively excludes histidine kinases (different fold/mechanism), transferases, and methyltransferases. Since only one Ser/Thr kinase option (2.7.11.24) is offered, the model does not need to distinguish among multiple 2.7.11.x subtypes. The large regulatory N-terminal region with Ser/Thr-rich stretches further supports MAPKKK architecture over, say, a simple monomeric kinase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options belong to four different EC subclasses (2.7.13, 2.3.1, 2.1.1, 2.7.11). The sequence's clear ePK fold with HRD/DFG motifs unambiguously places it in the protein Ser/Thr kinase class (2.7.11.x), and only one such option is offered. No other choice is defensible given the sequence evidence."
  },
  "important_caveats": [
    "The specific 4-digit assignment 2.7.11.24 (MAPKKK) vs. other 2.7.11.x numbers (e.g., 2.7.11.1, 2.7.11.22) is not independently derivable from the sequence alone; however, since only 2.7.11.24 is offered among the choices, the multiple-choice format resolves this.",
    "The UniProt annotation uses ECO:0000305 (inferred from direct assay) tied to a 2025 publication, indicating experimental validation of the kinase activity, though the specific MAPKKK designation may involve pathway context beyond pure sequence."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:17990\"}}],\"reaction\":{\"ecNumber\":\"2.7.11.24\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:46609\"}}],\"reaction\":{\"ecNumber\":\"2.7.11.24\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39631571\",\"source\":\"PubMed\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "DE   RecName: Full=Mitogen-activated protein kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};\nDE            Short=MAP kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};\nDE            Short=MAPKKK mkh1 {ECO:0000303|PubMed:39631571};\nDE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;\nCC         Evidence={ECO:0000305|PubMed:39631571};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;\nCC         Evidence={ECO:0000305|PubMed:39631571};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-44",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;\nCC         Evidence={ECO:0000305|PubMed:39631571};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;\nCC         Evidence={ECO:0000305|PubMed:39631571};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:22.695404+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a",
  "url": "https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
