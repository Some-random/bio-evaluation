# catalytic_activity_0143

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0143.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — cholesterol(in) = cholesterol(out)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFVKNFIHKLKELKQKSLDKFANLLYDYGGYVYDRPCTFIICSLICCLLLTCGFYFKEHEKDIYKLYSISNSYAYETNETINDFFYKSRRCFILVESNVNLLKPKILRELQKFEEGTKDIEVDLSEINECKTNSELPPEQSHVAKELYKTLIQRSEENLKSGKINGSLFDYSDLDENGKSVLSLAGKENNDDTLIEGDNKNDEETSANNNNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEKQKSLREKLYRKIYEMLKKKKENIVLDENNPNVNFTDYKDDVFYPYQYIPPMLIKADRCKLQNVFGDKNLNIDLREASDGLKKQITYTLEDICEKKYGDCNFSSLFLYYEKGNGYIDYPIKVDNLDFYVNRRTYKEMMFKGILGNMVYEKSGSKYIIKSANAIMTVIPLLNSHTYEPYALAYEKKLIDYVRFYNLDDIIQDEETNDDNDPFIRFHVFTDRSLEDEVDRISKIDNLTRLLLLIGVLLIFMYALFNNVTSVLYRSKPLCAVMGIFCGFLGFLSGSGFLYFLGVKSVPPAETVPFLVIGVGVDDVFVILNSYSLLFMVKDNKKRIQMCLKDSALAITVTTLTNIIAFLISAISPFYSICAFSLFTASSLFFGYLMVLTFLLSFLCIEAKLEKKKRNIFTGTFHLFRSIFMKSSKKNKKENKENNIHDDGDNDNDEKKKDLSLEVKNNEDDYENISIYEWIHNLYLFEESINKKKKNAALVYASNNGMSSNLNNVNEDGFPNPSKIVSMEDVKKRNIKKDDAYINKEDEEGGGYYNKDDNKKKDILGKKQKKNNNNVTLVSKKGEDNELDVYYENLDEKTNDKYKMNNIKSSKLKYDNDKKDGAIINNRPSSDEEYKEEKDKNKINILNDVFNDITIKPNENILLDRGDVIKSSGYDSSYNDLQSSSLPNPSSNEVLNKTTMVYNETDLKDNKKEIKSSKKNVKDIKKSDMIHDDTYDIINSNNKNILLSSNEINNNSNNTNKFNNNSTELATKDTQQFINGHDKNIYLLSSHDNALFYKYIYEEPKGNIGKYFRSLVKNYYVPFLSSRFGKTIVYIMFTIIIAMSIYGCTLMKKGIKYDKAFPVDSYVRRFTTAKIKYFPDFGDFIEVYYFDKHFINKYRGLEKNTKEAASSFLYSDLTDRQIMNSPKINKNVHWENTNLQEELINMHNTLESQEFVTSVANGFTFFLNKNKSSLRKENPQEFYEIFANWLKKDFVGNLFKNDFVFLNGKLVAWRFHYFQKNVDDSEISSKWLKACKQITKLENHNVQMVCFHLSSIFNETDESIIEVTLINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH

[Multiple Choices]
A. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
B. methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)
C. cholesterol(in) = cholesterol(out)
D. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
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

> The sequence-matched historical UniProt entry records the reaction in choice C with experimental evidence (ECO:0000269, citing PubMed 39693420). This supports the key, though the annotation is database-reported evidence rather than an independent review of the experiment.

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic segments consistent with a large multipass membrane transporter, alongside substantial non-transmembrane regions. Its overall architecture is compatible with NPC1-related sterol transporters, for which cholesterol transport is a transferable family-level functional pattern. That makes choice C meaningfully more plausible than A, B, or D, which describe reactions of soluble enzyme types.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and offered reactions provide a credible basis for recognizing a sterol-transporter family pattern and selecting the only transport reaction. This is probabilistic family-level inference, not proof that this exact protein transports cholesterol.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, only C describes transport of a molecule without chemical conversion; the others describe distinct chemical reactions.


### Important caveats

- Choice C is a transport reaction rather than a conventional chemical transformation, despite the task's enzymatic-reaction framing.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic segments consistent with a large multipass membrane transporter, alongside substantial non-transmembrane regions. Its overall architecture is compatible with NPC1-related sterol transporters, for which cholesterol transport is a transferable family-level functional pattern. That makes choice C meaningfully more plausible than A, B, or D, which describe reactions of soluble enzyme types.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered reactions provide a credible basis for recognizing a sterol-transporter family pattern and selecting the only transport reaction. This is probabilistic family-level inference, not proof that this exact protein transports cholesterol."
  },
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry records the reaction in choice C with experimental evidence (ECO:0000269, citing PubMed 39693420). This supports the key, though the annotation is database-reported evidence rather than an independent review of the experiment."
  },
  "important_caveats": [
    "Choice C is a transport reaction rather than a conventional chemical transformation, despite the task's enzymatic-reaction framing."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, only C describes transport of a molecule without chemical conversion; the others describe distinct chemical reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry records the reaction in choice C with experimental evidence (ECO:0000269, citing PubMed 39693420). This supports the key, though the annotation is database-reported evidence rather than an independent review of the experiment.",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic segments consistent with a large multipass membrane transporter, alongside substantial non-transmembrane regions. Its overall architecture is compatible with NPC1-related sterol transporters, for which cholesterol transport is a transferable family-level functional pattern. That makes choice C meaningfully more plausible than A, B, or D, which describe reactions of soluble enzyme types.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered reactions provide a credible basis for recognizing a sterol-transporter family pattern and selecting the only transport reaction. This is probabilistic family-level inference, not proof that this exact protein transports cholesterol."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, only C describes transport of a molecule without chemical conversion; the others describe distinct chemical reactions."
  },
  "important_caveats": [
    "Choice C is a transport reaction rather than a conventional chemical transformation, despite the task's enzymatic-reaction framing."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I266 (NCR1_PLAF7, Niemann-Pick type C1-related protein from Plasmodium falciparum) explicitly lists the CATALYTIC ACTIVITY as 'cholesterol(in) = cholesterol(out)' (RHEA:39747, CHEBI:16113) with evidence code ECO:0000269 (direct assay) from PubMed:39693420. The 2024 Sci. Adv. paper provided cryo-EM structures in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol export function. The 2019 Elife paper also characterized function and disruption phenotype. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 match confirmed).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1470-aa sequence contains numerous hydrophobic transmembrane segments (~13+ TM helices) organized into a large hydrophilic N-terminal luminal domain (with characteristic charged-residue-rich regions like 'EDDNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEK') and a C-terminal sterol-sensing domain (SSD) with a dense cluster of TM helices ('LINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH'). This architecture is the hallmark of the NPC1/NCR1 protein family, well-known cholesterol transporters. Options A (acyl carrier protein synthase, ~100 aa soluble), B (methylarsonite dioxygenase, small soluble enzyme), and D (a phosphorylase, soluble enzyme) are all soluble enzymes with no transmembrane segments — completely incompatible with a 1470-aa multi-pass membrane protein. Option C (cholesterol transport across a membrane) is the only answer describing a membrane transport process, which is the sole activity type consistent with a multi-TM protein. Additionally, the NPC1/NCR1 family is well-characterized in the literature as cholesterol exporters, and the SSD architecture (shared with HMG-CoA reductase, Patched, SCAP) is a recognized sterol-transport/sensing module.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass transmembrane architecture (1470 aa, ~13+ TM helices, large luminal domain + SSD) immediately eliminates all three soluble-enzyme distractors (A, B, D) and points to a membrane transport activity. The NPC1/NCR1 family is a well-known cholesterol transporter family, and recognizing this architecture from sequence features plus general knowledge of membrane protein families is sufficient to select C without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe reactions catalyzed by small soluble enzymes (ACPS ~100 aa, a dioxygenase, a phosphorylase), which are structurally incompatible with a 1470-aa multi-pass transmembrane protein. Only option C describes a membrane transport process. There is no ambiguity.


### Important caveats

- The UniProt annotation for NCR1 was first publicly released in June 2025 (entry integrated into Swiss-Prot). If the benchmark was constructed before this date, the cholesterol transport activity may not have been in the public annotation, though the 2019 Elife paper (PubMed:30888318) already described the protein's role in membrane homeostasis and the 2024 Sci. Adv. paper provided definitive structural and functional evidence.
- The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model only had access to the raw sequence and the four choices.
- The NPC1/NCR1 family recognition from sequence alone requires familiarity with the characteristic domain architecture (large luminal domain + SSD), but this is standard knowledge in membrane biology and lipid transport.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1470-aa sequence contains numerous hydrophobic transmembrane segments (~13+ TM helices) organized into a large hydrophilic N-terminal luminal domain (with characteristic charged-residue-rich regions like 'EDDNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEK') and a C-terminal sterol-sensing domain (SSD) with a dense cluster of TM helices ('LINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH'). This architecture is the hallmark of the NPC1/NCR1 protein family, well-known cholesterol transporters. Options A (acyl carrier protein synthase, ~100 aa soluble), B (methylarsonite dioxygenase, small soluble enzyme), and D (a phosphorylase, soluble enzyme) are all soluble enzymes with no transmembrane segments — completely incompatible with a 1470-aa multi-pass membrane protein. Option C (cholesterol transport across a membrane) is the only answer describing a membrane transport process, which is the sole activity type consistent with a multi-TM protein. Additionally, the NPC1/NCR1 family is well-characterized in the literature as cholesterol exporters, and the SSD architecture (shared with HMG-CoA reductase, Patched, SCAP) is a recognized sterol-transport/sensing module.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane architecture (1470 aa, ~13+ TM helices, large luminal domain + SSD) immediately eliminates all three soluble-enzyme distractors (A, B, D) and points to a membrane transport activity. The NPC1/NCR1 family is a well-known cholesterol transporter family, and recognizing this architecture from sequence features plus general knowledge of membrane protein families is sufficient to select C without memorizing this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8I266 (NCR1_PLAF7, Niemann-Pick type C1-related protein from Plasmodium falciparum) explicitly lists the CATALYTIC ACTIVITY as 'cholesterol(in) = cholesterol(out)' (RHEA:39747, CHEBI:16113) with evidence code ECO:0000269 (direct assay) from PubMed:39693420. The 2024 Sci. Adv. paper provided cryo-EM structures in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol export function. The 2019 Elife paper also characterized function and disruption phenotype. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation for NCR1 was first publicly released in June 2025 (entry integrated into Swiss-Prot). If the benchmark was constructed before this date, the cholesterol transport activity may not have been in the public annotation, though the 2019 Elife paper (PubMed:30888318) already described the protein's role in membrane homeostasis and the 2024 Sci. Adv. paper provided definitive structural and functional evidence.",
    "The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model only had access to the raw sequence and the four choices.",
    "The NPC1/NCR1 family recognition from sequence alone requires familiarity with the characteristic domain architecture (large luminal domain + SSD), but this is standard knowledge in membrane biology and lipid transport."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe reactions catalyzed by small soluble enzymes (ACPS ~100 aa, a dioxygenase, a phosphorylase), which are structurally incompatible with a 1470-aa multi-pass transmembrane protein. Only option C describes a membrane transport process. There is no ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8I266 (NCR1_PLAF7, Niemann-Pick type C1-related protein from Plasmodium falciparum) explicitly lists the CATALYTIC ACTIVITY as 'cholesterol(in) = cholesterol(out)' (RHEA:39747, CHEBI:16113) with evidence code ECO:0000269 (direct assay) from PubMed:39693420. The 2024 Sci. Adv. paper provided cryo-EM structures in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol export function. The 2019 Elife paper also characterized function and disruption phenotype. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 match confirmed).",
    "evidence_ids": ["C5", "C7", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1470-aa sequence contains numerous hydrophobic transmembrane segments (~13+ TM helices) organized into a large hydrophilic N-terminal luminal domain (with characteristic charged-residue-rich regions like 'EDDNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEK') and a C-terminal sterol-sensing domain (SSD) with a dense cluster of TM helices ('LINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH'). This architecture is the hallmark of the NPC1/NCR1 protein family, well-known cholesterol transporters. Options A (acyl carrier protein synthase, ~100 aa soluble), B (methylarsonite dioxygenase, small soluble enzyme), and D (a phosphorylase, soluble enzyme) are all soluble enzymes with no transmembrane segments — completely incompatible with a 1470-aa multi-pass membrane protein. Option C (cholesterol transport across a membrane) is the only answer describing a membrane transport process, which is the sole activity type consistent with a multi-TM protein. Additionally, the NPC1/NCR1 family is well-characterized in the literature as cholesterol exporters, and the SSD architecture (shared with HMG-CoA reductase, Patched, SCAP) is a recognized sterol-transport/sensing module.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane architecture (1470 aa, ~13+ TM helices, large luminal domain + SSD) immediately eliminates all three soluble-enzyme distractors (A, B, D) and points to a membrane transport activity. The NPC1/NCR1 family is a well-known cholesterol transporter family, and recognizing this architecture from sequence features plus general knowledge of membrane protein families is sufficient to select C without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe reactions catalyzed by small soluble enzymes (ACPS ~100 aa, a dioxygenase, a phosphorylase), which are structurally incompatible with a 1470-aa multi-pass transmembrane protein. Only option C describes a membrane transport process. There is no ambiguity."
  },
  "important_caveats": [
    "The UniProt annotation for NCR1 was first publicly released in June 2025 (entry integrated into Swiss-Prot). If the benchmark was constructed before this date, the cholesterol transport activity may not have been in the public annotation, though the 2019 Elife paper (PubMed:30888318) already described the protein's role in membrane homeostasis and the 2024 Sci. Adv. paper provided definitive structural and functional evidence.",
    "The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model only had access to the raw sequence and the four choices.",
    "The NPC1/NCR1 family recognition from sequence alone requires familiarity with the characteristic domain architecture (large luminal domain + SSD), but this is standard knowledge in membrane biology and lipid transport."
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
  "benchmark_sequence_length": 1470,
  "benchmark_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "current_entry_audit": {
    "entryVersion": 126,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1470,
  "current_source_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 124,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8I266",
  "selected_historical_entry_version": 124,
  "selected_historical_record_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "selected_historical_source_sequence_length": 1470,
  "selected_historical_source_sequence_sha256": "07ace62be3d6e1b79adbe002f51a2784c4046a9b5a29e38e610e20b3ddca65a1",
  "selected_historical_version": {
    "accession": "Q8I266",
    "database": "Swiss-Prot",
    "entryVersion": 124,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NCR1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8I266\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":126,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30888318\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"Niemann-Pick type C1-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"NCR1 transporter\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30888318\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"value\":\"PfNCR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39693420\",\"source\":\"PubMed\"}],\"name\":\"cholesterol(in) = cholesterol(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:39747\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16113\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Istvan E.S.\",\"Das S.\",\"Bhatnagar S.\",\"Beck J.R.\",\"Owen E.\",\"Llinas M.\",\"Ganesan S.M.\",\"Niles J.C.\",\"Winzeler E.\",\"Vaidya A.B.\",\"Goldberg D.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30888318\"},{\"database\":\"DOI\",\"id\":\"10.7554/elife.40529\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30888318\",\"journal\":\"Elife\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Plasmodium Niemann-Pick type C1-related protein is a druggable target required for parasite membrane homeostasis.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF ALA-1108; ALA-1208 AND PHE-1436\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Lyu M.\",\"Han X.\",\"Bandara S.\",\"Cui M.\",\"Istvan E.S.\",\"Geng X.\",\"Tringides M.L.\",\"Gregor W.D.\",\"Miyagi M.\",\"Oberstaller J.\",\"Adams J.H.\",\"Zhang Y.\",\"Nieman M.T.\",\"von Lintig J.\",\"Goldberg D.E.\",\"Yu E.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39693420\"},{\"database\":\"DOI\",\"id\":\"10.1126/sciadv.adq6651\"}],\"citationType\":\"journal article\",\"firstPage\":\"eadq6651\",\"id\":\"39693420\",\"journal\":\"Sci. Adv.\",\"lastPage\":\"eadq6651\",\"publicationDate\":\"2024\",\"title\":\"The Plasmodium falciparum NCR1 transporter is an antimalarial target that exports cholesterol from the parasite's plasma membrane.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V0G\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V12\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8V1G\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"GLYCOSYLATION AT ASN-165 AND ASN-294\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:00.862431+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I266.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H1",
  "excerpt": "ID   NCR1_PLAF7              Reviewed;        1470 AA.\nAC   Q8I266;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 124.\nDE   RecName: Full=Niemann-Pick type C1-related protein {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\nDE            Short=NCR1 transporter {ECO:0000303|PubMed:39693420};\nDE            Short=PfNCR1 {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\nGN   Name=NCR1 {ECO:0000305};\nGN   ORFNames=PF3D7_0107500 {ECO:0000312|EMBL:CAD49035.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Niemann-Pick type C1-related protein {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\nDE            Short=NCR1 transporter {ECO:0000303|PubMed:39693420};\nDE            Short=PfNCR1 {ECO:0000303|PubMed:30888318, ECO:0000303|PubMed:39693420};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   ALA-1108; ALA-1208 AND PHE-1436.\nRX   PubMed=30888318; DOI=10.7554/elife.40529;\nRA   Istvan E.S., Das S., Bhatnagar S., Beck J.R., Owen E., Llinas M.,\nRA   Ganesan S.M., Niles J.C., Winzeler E., Vaidya A.B., Goldberg D.E.;\nRT   \"Plasmodium Niemann-Pick type C1-related protein is a druggable target\nRT   required for parasite membrane homeostasis.\";\nRL   Elife 8:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12, ECO:0007744|PDB:8V1G}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH\nRP   CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108, FUNCTION, TRANSPORTER\nRP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, AND\nRP   GLYCOSYLATION AT ASN-165 AND ASN-294.\nRX   PubMed=39693420; DOI=10.1126/sciadv.adq6651;\nRA   Zhang Z., Lyu M., Han X., Bandara S., Cui M., Istvan E.S., Geng X.,\nRA   Tringides M.L., Gregor W.D., Miyagi M., Oberstaller J., Adams J.H.,\nRA   Zhang Y., Nieman M.T., von Lintig J., Goldberg D.E., Yu E.W.;\nRT   \"The Plasmodium falciparum NCR1 transporter is an antimalarial target that\nRT   exports cholesterol from the parasite's plasma membrane.\";\nRL   Sci. Adv. 10:eadq6651-eadq6651(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)

```json
{
  "entry_version": 124,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cholesterol(in) = cholesterol(out); Xref=Rhea:RHEA:39747,\nCC         ChEBI:CHEBI:16113; Evidence={ECO:0000269|PubMed:39693420};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:03.056916+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7",
  "url": "https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
