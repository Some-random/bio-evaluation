# EC_number_0142

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0142.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEQFGGPSGFMPPASYTAPLGKYPTKQPSAAYPSDGGRHATKENPRPAEGQASRQSSSVPSAMASKPIQDPEGHSAQPTSSYCRAQTPRSTPLPVALDEEARLSQYEVIRQIGAGRFGEVFIIRHKATKALLCWKLVFYKGLREKEKKQLVSEVNVMRELRHANIVRYHDRIVCRSRQCLYIVMEYCDAGDLAKQIEAAHKHHGGIDQDRIVLVVVQLIHALAYCHEGVGQERRRVLHRDLKPCNIFLASHPEYPDDSSRCIAKLGDFGLSRHLNMHSMAHSCVGTPYYWSPELLEDGQKTYNVKSDMWALGCVIYEMCTGKTPFAQAQTMPQLKERVRCGPVLPVPGFSDSLNALMASLLQPNPNNRPSALQCLGYTIFRGCSYTPPPLYRSSSAPSWTPRNASPARGSPSSAVSTVSTVTTSPGSSSRTSFSAPSSHDAAASSPASASASSRYQHQRSSSYSSDSAGPSGASAPSQKAPGPGRPPETPSRESFDLASKARPGFFAEAPPPHAFAEASPPESHASEFLPPANGAANEARNERTQRDRTRRAASATAAAAVSAFERQQREGRSMSPDPSAPLASIEEEEEGEGDDAGCGSLGSGSGVTRRMPGASLNREDRREAPGLRHADTHKRDDRDGAIWTGRREEAPFSRPGSELARDFGAASQNKVDTSRFSGASSGKPRPGNPQNEDRASFASDTSARQTVYLSGLSRRCSEPPAAFHSAVSPWDPAPPRLSSAASSSSSSRAVSPSSLRRASSREMKYPTDDRPAVAAGSSGVALARAERGPEPGAPWGNEETEGLHVHGRPSAAPASSFSSERTSRPGHPDEARESEHCFQGRGRFAEAEASPATEGKDPRDSGFEERSGRRDEGRTDGGEAQSFGYWPNGRSDEARDRLGAPSVSPFSSKRITRRSSTAAGLSTYASPSDPAPSARAPAEWRRGAAGSSTVSAAGACGRFLPSPRSWQGNEKSFPSSSDHPSAYPALPHPAAPAYPEPGAQASNQFPRRRQSAFPSVKRLDYEEEHASSACLPTLLSPRFPHHPVSRPAGGVSPRSSQRQALAPTLAGMTFERRLSAGPLSSAPFSAPQERTTRLVGHRHALAADAERAEAPFSHAFRPGHHDRTPVGARRVPPRAETPGVSLDPGFRTGGPLDRGPVGSGGLEGQSFDFAHPTHASSEKKEAETEWSNPTAPVFYSPRSPRNDLPPGDGARSPYSAHLRPGVSEACSSFSVPPTERYEDDKNSHHAGSGGAFSPPTFGSPTPGPVPVGNERTFGRNPSPAATCASFSAKTGLRTPAPNGLAGDSGAFRSTNSLQRTPMSRRVSAPFGAGSAEGATAFGSRYASSGSFSKKFPQGSSSGVHEGGGAFGRRQEGDVSRVDAHGSVSPRSFSFLQRSDAPLSRGQPEGSHFQKHGETRASPDFARKGDSTQTHASGGRDFSQSGPFETQDFTFGEQPTRETRHMAPSPRGIERGGPQGSFVGHDTSFSVYAPRAGHAEGVESGCSAFEAPSESLSRRDGEADRENTVPNANGQMPVSGMPASKQTYGDDCDLYDNSAWTAQKHAPENFHAAVAPYPSSLLTGFAEGQQKAASRSSCLGGDR

[Multiple Choices]
A. 2.7.11.11
B. 1.14.13.238
C. 2.7.11.1
D. 4.2.99.18
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

> The sequence-matched UniProt record assigns EC 2.7.11.1 and lists serine- and threonine-phosphorylation reactions under that EC. The annotation cites a publication, though the supplied excerpts do not independently establish the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein kinase domain, including conserved kinase catalytic motifs, and a large low-complexity regulatory region. Transferable knowledge about kinase families supports a serine/threonine protein kinase rather than an oxidoreductase or lyase. Its kinase-family pattern also supports the broad protein-serine/threonine kinase choice over the more specific myosin-light-chain kinase alternative.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supports a meaningful family-level inference for the offered choices; the recorded annotation for this exact protein is not required to distinguish the broad kinase class from the unrelated enzyme classes or the narrower myosin-light-chain kinase option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these alternatives, the sequence's kinase-domain features support the serine/threonine protein kinase option; the other kinase option is a more specific enzyme classification, while the remaining options are different enzyme classes.


### Important caveats

- The reviewer-only database annotation is not evidence that the evaluated model had access to the protein's identity or database record.
- The cited source evidence supports the annotation but does not independently document or validate the underlying experimental findings.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase domain, including conserved kinase catalytic motifs, and a large low-complexity regulatory region. Transferable knowledge about kinase families supports a serine/threonine protein kinase rather than an oxidoreductase or lyase. Its kinase-family pattern also supports the broad protein-serine/threonine kinase choice over the more specific myosin-light-chain kinase alternative.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a meaningful family-level inference for the offered choices; the recorded annotation for this exact protein is not required to distinguish the broad kinase class from the unrelated enzyme classes or the narrower myosin-light-chain kinase option."
  },
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.11.1 and lists serine- and threonine-phosphorylation reactions under that EC. The annotation cites a publication, though the supplied excerpts do not independently establish the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only database annotation is not evidence that the evaluated model had access to the protein's identity or database record.",
    "The cited source evidence supports the annotation but does not independently document or validate the underlying experimental findings."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the sequence's kinase-domain features support the serine/threonine protein kinase option; the other kinase option is a more specific enzyme classification, while the remaining options are different enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.11.1 and lists serine- and threonine-phosphorylation reactions under that EC. The annotation cites a publication, though the supplied excerpts do not independently establish the underlying experiments.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase domain, including conserved kinase catalytic motifs, and a large low-complexity regulatory region. Transferable knowledge about kinase families supports a serine/threonine protein kinase rather than an oxidoreductase or lyase. Its kinase-family pattern also supports the broad protein-serine/threonine kinase choice over the more specific myosin-light-chain kinase alternative.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a meaningful family-level inference for the offered choices; the recorded annotation for this exact protein is not required to distinguish the broad kinase class from the unrelated enzyme classes or the narrower myosin-light-chain kinase option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, the sequence's kinase-domain features support the serine/threonine protein kinase option; the other kinase option is a more specific enzyme classification, while the remaining options are different enzyme classes."
  },
  "important_caveats": [
    "The reviewer-only database annotation is not evidence that the evaluated model had access to the protein's identity or database record.",
    "The cited source evidence supports the annotation but does not independently document or validate the underlying experimental findings."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry S8GI44 (NEK_TOXGM, Toxoplasma gondii Nek1) is annotated with EC 2.7.11.1 based on experimental evidence (PubMed:23729737, ECO:0000305). The catalytic activities are explicitly listed as phosphorylation of L-seryl-&#91;protein&#93; and L-threonyl-&#91;protein&#93; using ATP, consistent with EC 2.7.11.1 (Serine/threonine-protein kinase). The sequence match is confirmed.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: the glycine-rich loop (GAGRFGEV ~ GxGxxG), the VAIK lysine (KATK), the catalytic HRD motif (HRDLKPCNIF), and the DFG activation-loop motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL). These immediately eliminate B (EC 1.14.13.238, a P450-type oxidoreductase) and D (EC 4.2.99.18, a hyaluronidase/lyase), neither of which has kinase folds. The key discrimination is between A (EC 2.7.11.11, MAP4KKK) and C (EC 2.7.11.1, general Ser/Thr kinase). The sequence shows a single, self-contained kinase domain followed by a long intrinsically disordered C-terminal region (~1100 residues), which is the hallmark architecture of the NIMA-related kinase (NEK) family. MAP4KKKs (e.g., MEKK, MLK, DLK families) typically possess additional regulatory domains (e.g., PB1, SH3, leucine-rich repeats) flanking the kinase domain and belong to the STE/STE20-like or RAF-like subfamilies, not the NEK family. The NEK family is a well-characterized, evolutionarily distinct group of Ser/Thr kinases involved in cell-cycle and centrosome regulation, universally classified under EC 2.7.11.1 rather than the hyper-specific EC 2.7.11.11. Recognizing the single-domain NEK architecture from the sequence and applying family-level knowledge that NEKs are not MAP4KKKs meaningfully selects C over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the kinase fold from conserved motifs, eliminate B and D trivially, and then use the single-kinase-domain architecture plus NEK-family-level knowledge (NEKs are not MAP4KKKs) to distinguish C from A. This is legitimate transfer from well-characterized kinase family biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and D are trivially eliminated by the presence of kinase motifs. A is eliminated by the single-domain NEK architecture inconsistent with MAP4KKKs. C is the only remaining defensible choice.


### Important caveats

- The NEK family assignment is inferred from sequence architecture and conserved motifs visible in the input; the model does not receive the protein name or organism.
- EC 2.7.11.11 is an extremely specific activity (MAP4KKK) held by very few proteins; its inclusion as a distractor is somewhat unusual but does not create genuine ambiguity given the family-level reasoning.
- The annotation evidence code ECO:0000305 indicates the EC assignment was made by the curator based on the cited experimental paper, not solely by sequence similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: the glycine-rich loop (GAGRFGEV ~ GxGxxG), the VAIK lysine (KATK), the catalytic HRD motif (HRDLKPCNIF), and the DFG activation-loop motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL). These immediately eliminate B (EC 1.14.13.238, a P450-type oxidoreductase) and D (EC 4.2.99.18, a hyaluronidase/lyase), neither of which has kinase folds. The key discrimination is between A (EC 2.7.11.11, MAP4KKK) and C (EC 2.7.11.1, general Ser/Thr kinase). The sequence shows a single, self-contained kinase domain followed by a long intrinsically disordered C-terminal region (~1100 residues), which is the hallmark architecture of the NIMA-related kinase (NEK) family. MAP4KKKs (e.g., MEKK, MLK, DLK families) typically possess additional regulatory domains (e.g., PB1, SH3, leucine-rich repeats) flanking the kinase domain and belong to the STE/STE20-like or RAF-like subfamilies, not the NEK family. The NEK family is a well-characterized, evolutionarily distinct group of Ser/Thr kinases involved in cell-cycle and centrosome regulation, universally classified under EC 2.7.11.1 rather than the hyper-specific EC 2.7.11.11. Recognizing the single-domain NEK architecture from the sequence and applying family-level knowledge that NEKs are not MAP4KKKs meaningfully selects C over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the kinase fold from conserved motifs, eliminate B and D trivially, and then use the single-kinase-domain architecture plus NEK-family-level knowledge (NEKs are not MAP4KKKs) to distinguish C from A. This is legitimate transfer from well-characterized kinase family biology."
  },
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry S8GI44 (NEK_TOXGM, Toxoplasma gondii Nek1) is annotated with EC 2.7.11.1 based on experimental evidence (PubMed:23729737, ECO:0000305). The catalytic activities are explicitly listed as phosphorylation of L-seryl-[protein] and L-threonyl-[protein] using ATP, consistent with EC 2.7.11.1 (Serine/threonine-protein kinase). The sequence match is confirmed."
  },
  "important_caveats": [
    "The NEK family assignment is inferred from sequence architecture and conserved motifs visible in the input; the model does not receive the protein name or organism.",
    "EC 2.7.11.11 is an extremely specific activity (MAP4KKK) held by very few proteins; its inclusion as a distractor is somewhat unusual but does not create genuine ambiguity given the family-level reasoning.",
    "The annotation evidence code ECO:0000305 indicates the EC assignment was made by the curator based on the cited experimental paper, not solely by sequence similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are trivially eliminated by the presence of kinase motifs. A is eliminated by the single-domain NEK architecture inconsistent with MAP4KKKs. C is the only remaining defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry S8GI44 (NEK_TOXGM, Toxoplasma gondii Nek1) is annotated with EC 2.7.11.1 based on experimental evidence (PubMed:23729737, ECO:0000305). The catalytic activities are explicitly listed as phosphorylation of L-seryl-[protein] and L-threonyl-[protein] using ATP, consistent with EC 2.7.11.1 (Serine/threonine-protein kinase). The sequence match is confirmed.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: the glycine-rich loop (GAGRFGEV ~ GxGxxG), the VAIK lysine (KATK), the catalytic HRD motif (HRDLKPCNIF), and the DFG activation-loop motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL). These immediately eliminate B (EC 1.14.13.238, a P450-type oxidoreductase) and D (EC 4.2.99.18, a hyaluronidase/lyase), neither of which has kinase folds. The key discrimination is between A (EC 2.7.11.11, MAP4KKK) and C (EC 2.7.11.1, general Ser/Thr kinase). The sequence shows a single, self-contained kinase domain followed by a long intrinsically disordered C-terminal region (~1100 residues), which is the hallmark architecture of the NIMA-related kinase (NEK) family. MAP4KKKs (e.g., MEKK, MLK, DLK families) typically possess additional regulatory domains (e.g., PB1, SH3, leucine-rich repeats) flanking the kinase domain and belong to the STE/STE20-like or RAF-like subfamilies, not the NEK family. The NEK family is a well-characterized, evolutionarily distinct group of Ser/Thr kinases involved in cell-cycle and centrosome regulation, universally classified under EC 2.7.11.1 rather than the hyper-specific EC 2.7.11.11. Recognizing the single-domain NEK architecture from the sequence and applying family-level knowledge that NEKs are not MAP4KKKs meaningfully selects C over A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the kinase fold from conserved motifs, eliminate B and D trivially, and then use the single-kinase-domain architecture plus NEK-family-level knowledge (NEKs are not MAP4KKKs) to distinguish C from A. This is legitimate transfer from well-characterized kinase family biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are trivially eliminated by the presence of kinase motifs. A is eliminated by the single-domain NEK architecture inconsistent with MAP4KKKs. C is the only remaining defensible choice."
  },
  "important_caveats": [
    "The NEK family assignment is inferred from sequence architecture and conserved motifs visible in the input; the model does not receive the protein name or organism.",
    "EC 2.7.11.11 is an extremely specific activity (MAP4KKK) held by very few proteins; its inclusion as a distractor is somewhat unusual but does not create genuine ambiguity given the family-level reasoning.",
    "The annotation evidence code ECO:0000305 indicates the EC assignment was made by the curator based on the cited experimental paper, not solely by sequence similarity."
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
  "benchmark_sequence_length": 1598,
  "benchmark_sequence_sha256": "ab6db6c7f1b507247aead50ff77b5cf5cf47c47d81065d7bb0f292936dc66224",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-10-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1598,
  "current_source_sequence_sha256": "ab6db6c7f1b507247aead50ff77b5cf5cf47c47d81065d7bb0f292936dc66224",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "S8GI44",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "selected_historical_source_sequence_length": 1598,
  "selected_historical_source_sequence_sha256": "ab6db6c7f1b507247aead50ff77b5cf5cf47c47d81065d7bb0f292936dc66224",
  "selected_historical_version": {
    "accession": "S8GI44",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEK_TOXGM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"S8GI44\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001529\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii (strain ATCC 50611 / Me49)\",\"taxonId\":508771}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"NIMA-related protein kinase NIMA1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23729737\",\"source\":\"PubMed\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine/threonine-protein kinase Nek1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30865554\",\"source\":\"PubMed\"}],\"value\":\"TgNek1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23729737\",\"source\":\"PubMed\"}],\"name\":\"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17989\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9863\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83421\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.11.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23729737\",\"source\":\"PubMed\"}],\"name\":\"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46608\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11060\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11605\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30013\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61977\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen C.T.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23729737\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.123364\"}],\"citationType\":\"journal article\",\"firstPage\":\"3344\",\"id\":\"23729737\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"3355\",\"publicationDate\":\"2013\",\"title\":\"The Toxoplasma gondii centrosome is the platform for internal daughter budding as revealed by a Nek1 kinase mutant.\",\"volume\":\"126\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"ISOFORM TGNEK1-1\",\"ISOFORM TGNEK1-2\",\"DEVELOPMENTAL STAGE\",\"MUTAGENESIS OF LYS-135; SER-278; SER-282; THR-286 AND CYS-319\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Chen C.T.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30865554\"},{\"database\":\"DOI\",\"id\":\"10.1091/mbc.e18-10-0608\"}],\"citationType\":\"journal article\",\"firstPage\":\"1160\",\"id\":\"30865554\",\"journal\":\"Mol. Biol. Cell\",\"lastPage\":\"1169\",\"publicationDate\":\"2019\",\"title\":\"TgCep250 is dynamically processed through the division cycle and is essential for structural integrity of the Toxoplasma centrosome.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:59.328831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6",
  "url": "https://rest.uniprot.org/uniprotkb/S8GI44.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   NEK_TOXGM               Reviewed;        1598 AA.\nAC   S8GI44;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2013, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Serine/threonine-protein kinase Nek1 {ECO:0000305};\nDE            Short=TgNek1 {ECO:0000303|PubMed:30865554};\nDE            EC=2.7.11.1 {ECO:0000305|PubMed:23729737};\nDE   AltName: Full=NIMA-related protein kinase NIMA1 {ECO:0000305};\nGN   Name=NEK {ECO:0000312|EMBL:EPT28124.1};\nGN   ORFNames=TGME49_292140 {ECO:0000312|EMBL:EPT28124.1};\nOS   Toxoplasma gondii (strain ATCC 50611 / Me49).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Serine/threonine-protein kinase Nek1 {ECO:0000305};\nDE            Short=TgNek1 {ECO:0000303|PubMed:30865554};\nDE            EC=2.7.11.1 {ECO:0000305|PubMed:23729737};\nDE   AltName: Full=NIMA-related protein kinase NIMA1 {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, SUBCELLULAR LOCATION,\nRP   ALTERNATIVE SPLICING, ISOFORM TGNEK1-1, ISOFORM TGNEK1-2, DEVELOPMENTAL\nRP   STAGE, AND MUTAGENESIS OF LYS-135; SER-278; SER-282; THR-286 AND CYS-319.\nRX   PubMed=23729737; DOI=10.1242/jcs.123364;\nRA   Chen C.T., Gubbels M.J.;\nRT   \"The Toxoplasma gondii centrosome is the platform for internal daughter\nRT   budding as revealed by a Nek1 kinase mutant.\";\nRL   J. Cell Sci. 126:3344-3355(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30865554; DOI=10.1091/mbc.e18-10-0608;\nRA   Chen C.T., Gubbels M.J.;\nRT   \"TgCep250 is dynamically processed through the division cycle and is\nRT   essential for structural integrity of the Toxoplasma centrosome.\";\nRL   Mol. Biol. Cell 30:1160-1169(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +\nCC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-\nCC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000305|PubMed:23729737};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +\nCC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-\nCC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;\nCC         Evidence={ECO:0000305|PubMed:23729737};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:03.906590+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f",
  "url": "https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
