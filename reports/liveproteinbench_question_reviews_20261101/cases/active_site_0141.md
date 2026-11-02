# active_site_0141

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 240 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEQFGGPSGFMPPASYTAPLGKYPTKQPSAAYPSDGGRHATKENPRPAEGQASRQSSSVPSAMASKPIQDPEGHSAQPTSSYCRAQTPRSTPLPVALDEEARLSQYEVIRQIGAGRFGEVFIIRHKATKALLCWKLVFYKGLREKEKKQLVSEVNVMRELRHANIVRYHDRIVCRSRQCLYIVMEYCDAGDLAKQIEAAHKHHGGIDQDRIVLVVVQLIHALAYCHEGVGQERRRVLHRDLKPCNIFLASHPEYPDDSSRCIAKLGDFGLSRHLNMHSMAHSCVGTPYYWSPELLEDGQKTYNVKSDMWALGCVIYEMCTGKTPFAQAQTMPQLKERVRCGPVLPVPGFSDSLNALMASLLQPNPNNRPSALQCLGYTIFRGCSYTPPPLYRSSSAPSWTPRNASPARGSPSSAVSTVSTVTTSPGSSSRTSFSAPSSHDAAASSPASASASSRYQHQRSSSYSSDSAGPSGASAPSQKAPGPGRPPETPSRESFDLASKARPGFFAEAPPPHAFAEASPPESHASEFLPPANGAANEARNERTQRDRTRRAASATAAAAVSAFERQQREGRSMSPDPSAPLASIEEEEEGEGDDAGCGSLGSGSGVTRRMPGASLNREDRREAPGLRHADTHKRDDRDGAIWTGRREEAPFSRPGSELARDFGAASQNKVDTSRFSGASSGKPRPGNPQNEDRASFASDTSARQTVYLSGLSRRCSEPPAAFHSAVSPWDPAPPRLSSAASSSSSSRAVSPSSLRRASSREMKYPTDDRPAVAAGSSGVALARAERGPEPGAPWGNEETEGLHVHGRPSAAPASSFSSERTSRPGHPDEARESEHCFQGRGRFAEAEASPATEGKDPRDSGFEERSGRRDEGRTDGGEAQSFGYWPNGRSDEARDRLGAPSVSPFSSKRITRRSSTAAGLSTYASPSDPAPSARAPAEWRRGAAGSSTVSAAGACGRFLPSPRSWQGNEKSFPSSSDHPSAYPALPHPAAPAYPEPGAQASNQFPRRRQSAFPSVKRLDYEEEHASSACLPTLLSPRFPHHPVSRPAGGVSPRSSQRQALAPTLAGMTFERRLSAGPLSSAPFSAPQERTTRLVGHRHALAADAERAEAPFSHAFRPGHHDRTPVGARRVPPRAETPGVSLDPGFRTGGPLDRGPVGSGGLEGQSFDFAHPTHASSEKKEAETEWSNPTAPVFYSPRSPRNDLPPGDGARSPYSAHLRPGVSEACSSFSVPPTERYEDDKNSHHAGSGGAFSPPTFGSPTPGPVPVGNERTFGRNPSPAATCASFSAKTGLRTPAPNGLAGDSGAFRSTNSLQRTPMSRRVSAPFGAGSAEGATAFGSRYASSGSFSKKFPQGSSSGVHEGGGAFGRRQEGDVSRVDAHGSVSPRSFSFLQRSDAPLSRGQPEGSHFQKHGETRASPDFARKGDSTQTHASGGRDFSQSGPFETQDFTFGEQPTRETRHMAPSPRGIERGGPQGSFVGHDTSFSVYAPRAGHAEGVESGCSAFEAPSESLSRRDGEADRENTVPNANGQMPVSGMPASKQTYGDDCDLYDNSAWTAQKHAPENFHAAVAPYPSSLLTGFAEGQQKAASRSSCLGGDR

[Multiple Choices]
A. Position 113 (Nucleophile)
B. Position 1978 (For beta-ketoacyl synthase 2 activity)
C. Position 240 (Proton acceptor)
D. Position 5828 (For beta-ketoacyl synthase 4 activity)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact-matching UniProt record annotates residue 240 as an active-site proton acceptor. This annotation is based on the computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a protein-kinase catalytic-loop HRDLK motif. Kinases commonly use the conserved Asp in this motif as a catalytic base, consistent with the proton-acceptor role in choice C. Choices B and D also specify positions beyond the 1,598-residue sequence.


**Missing item-specific fact**

> No external protein-specific annotation is needed for the broad identification; mapping the motif to the stated residue number requires numbering the supplied sequence.


**Reason**

> A recognizable kinase motif and established kinase catalytic chemistry provide a concrete basis for distinguishing the proton-acceptor choice. This is a sequence-based inference, not proof of experimentally measured catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase catalytic-loop Asp supports C; the other specified positions are inconsistent with the sequence length or the indicated catalytic role.


### Important caveats

- The supporting database feature is computationally inferred via PROSITE-ProRule; the excerpts do not independently establish the role experimentally.
- The sequence matches the source record, but the author's exact annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic-loop HRDLK motif. Kinases commonly use the conserved Asp in this motif as a catalytic base, consistent with the proton-acceptor role in choice C. Choices B and D also specify positions beyond the 1,598-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external protein-specific annotation is needed for the broad identification; mapping the motif to the stated residue number requires numbering the supplied sequence.",
    "reason": "A recognizable kinase motif and established kinase catalytic chemistry provide a concrete basis for distinguishing the proton-acceptor choice. This is a sequence-based inference, not proof of experimentally measured catalytic activity."
  },
  "case_id": "active_site_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates residue 240 as an active-site proton acceptor. This annotation is based on the computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supporting database feature is computationally inferred via PROSITE-ProRule; the excerpts do not independently establish the role experimentally.",
    "The sequence matches the source record, but the author's exact annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase catalytic-loop Asp supports C; the other specified positions are inconsistent with the sequence length or the indicated catalytic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates residue 240 as an active-site proton acceptor. This annotation is based on the computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic-loop HRDLK motif. Kinases commonly use the conserved Asp in this motif as a catalytic base, consistent with the proton-acceptor role in choice C. Choices B and D also specify positions beyond the 1,598-residue sequence.",
    "missing_item_specific_fact": "No external protein-specific annotation is needed for the broad identification; mapping the motif to the stated residue number requires numbering the supplied sequence.",
    "reason": "A recognizable kinase motif and established kinase catalytic chemistry provide a concrete basis for distinguishing the proton-acceptor choice. This is a sequence-based inference, not proof of experimentally measured catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase catalytic-loop Asp supports C; the other specified positions are inconsistent with the sequence length or the indicated catalytic role."
  },
  "important_caveats": [
    "The supporting database feature is computationally inferred via PROSITE-ProRule; the excerpts do not independently establish the role experimentally.",
    "The sequence matches the source record, but the author's exact annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt S8GI44 (Serine/threonine-protein kinase Nek1, Toxoplasma gondii) annotates position 240 as an 'Active site' with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). The sequence is 1598 residues; positions 1978 (B) and 5828 (D) are outside the sequence entirely. The HRD-motif aspartate in protein kinases functions as the catalytic base/proton acceptor, consistent with the annotation. The evidence code indicates computational (PROSITE-ProRule) assignment rather than direct experimental determination, but the mechanistic role is well-established for protein kinases.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 1598 amino acids long, immediately eliminating options B (position 1978) and D (position 5828) as impossible positions. The sequence contains recognizable protein kinase motifs: a glycine-rich loop, the VAIK lysine, the HRD motif (HRDLKPCNIFLAS), and the DFG motif (GDFGLS). In protein kinase catalysis, the HRD aspartate acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl for phosphotransfer from ATP. Option A labels position 113 as a 'nucleophile,' which is mechanistically incorrect for a kinase—the nucleophile is the substrate's hydroxyl, not a residue in the enzyme. Option C correctly identifies the proton-acceptor role of the HRD aspartate. A model with general kinase biochemistry knowledge can identify the HRD motif in the sequence and reason that its aspartate is the proton acceptor, distinguishing C from A.


**Missing item-specific fact**

> None critical. The exact position number 240 requires counting through the sequence, but the functional role (proton acceptor vs. nucleophile) and the impossibility of positions beyond 1598 provide sufficient reasoning grounds.


**Reason**

> The question is answerable by (1) checking sequence length to eliminate B and D, (2) recognizing kinase domain motifs in the sequence, and (3) applying general knowledge that the HRD aspartate is the proton acceptor in protein kinase catalysis, not a nucleophile. This distinguishes C from A without needing to look up the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D reference positions (1978, 5828) that exceed the 1598-residue protein length and invoke unrelated 'beta-ketoacyl synthase' activity, making them trivially incorrect. Option A misattributes a 'nucleophile' role inconsistent with kinase mechanism. Only C is mechanistically and structurally consistent with the protein's identity as a Ser/Thr kinase.


### Important caveats

- The active-site annotation at position 240 carries evidence code ECO:0000255 (PROSITE-ProRule), indicating a computational/protein-rule-based assignment rather than direct experimental mutagenesis or crystallographic proof of proton-acceptor function.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence analysis and general kinase biochemistry.
- The distractors B and D are extremely weak (impossible positions, unrelated enzyme class), making the question easier than typical active-site prediction tasks.
- The UniProt entry was first released 2025-06-18; the author's source snapshot date is unknown, though the sequence has been stable since 2013 (sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 1598 amino acids long, immediately eliminating options B (position 1978) and D (position 5828) as impossible positions. The sequence contains recognizable protein kinase motifs: a glycine-rich loop, the VAIK lysine, the HRD motif (HRDLKPCNIFLAS), and the DFG motif (GDFGLS). In protein kinase catalysis, the HRD aspartate acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl for phosphotransfer from ATP. Option A labels position 113 as a 'nucleophile,' which is mechanistically incorrect for a kinase—the nucleophile is the substrate's hydroxyl, not a residue in the enzyme. Option C correctly identifies the proton-acceptor role of the HRD aspartate. A model with general kinase biochemistry knowledge can identify the HRD motif in the sequence and reason that its aspartate is the proton acceptor, distinguishing C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact position number 240 requires counting through the sequence, but the functional role (proton acceptor vs. nucleophile) and the impossibility of positions beyond 1598 provide sufficient reasoning grounds.",
    "reason": "The question is answerable by (1) checking sequence length to eliminate B and D, (2) recognizing kinase domain motifs in the sequence, and (3) applying general knowledge that the HRD aspartate is the proton acceptor in protein kinase catalysis, not a nucleophile. This distinguishes C from A without needing to look up the specific UniProt entry."
  },
  "case_id": "active_site_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6",
      "C7",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt S8GI44 (Serine/threonine-protein kinase Nek1, Toxoplasma gondii) annotates position 240 as an 'Active site' with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). The sequence is 1598 residues; positions 1978 (B) and 5828 (D) are outside the sequence entirely. The HRD-motif aspartate in protein kinases functions as the catalytic base/proton acceptor, consistent with the annotation. The evidence code indicates computational (PROSITE-ProRule) assignment rather than direct experimental determination, but the mechanistic role is well-established for protein kinases."
  },
  "important_caveats": [
    "The active-site annotation at position 240 carries evidence code ECO:0000255 (PROSITE-ProRule), indicating a computational/protein-rule-based assignment rather than direct experimental mutagenesis or crystallographic proof of proton-acceptor function.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence analysis and general kinase biochemistry.",
    "The distractors B and D are extremely weak (impossible positions, unrelated enzyme class), making the question easier than typical active-site prediction tasks.",
    "The UniProt entry was first released 2025-06-18; the author's source snapshot date is unknown, though the sequence has been stable since 2013 (sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D reference positions (1978, 5828) that exceed the 1598-residue protein length and invoke unrelated 'beta-ketoacyl synthase' activity, making them trivially incorrect. Option A misattributes a 'nucleophile' role inconsistent with kinase mechanism. Only C is mechanistically and structurally consistent with the protein's identity as a Ser/Thr kinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt S8GI44 (Serine/threonine-protein kinase Nek1, Toxoplasma gondii) annotates position 240 as an 'Active site' with description 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). The sequence is 1598 residues; positions 1978 (B) and 5828 (D) are outside the sequence entirely. The HRD-motif aspartate in protein kinases functions as the catalytic base/proton acceptor, consistent with the annotation. The evidence code indicates computational (PROSITE-ProRule) assignment rather than direct experimental determination, but the mechanistic role is well-established for protein kinases.",
    "evidence_ids": ["C5", "H4", "C4", "C6", "C7", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 1598 amino acids long, immediately eliminating options B (position 1978) and D (position 5828) as impossible positions. The sequence contains recognizable protein kinase motifs: a glycine-rich loop, the VAIK lysine, the HRD motif (HRDLKPCNIFLAS), and the DFG motif (GDFGLS). In protein kinase catalysis, the HRD aspartate acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl for phosphotransfer from ATP. Option A labels position 113 as a 'nucleophile,' which is mechanistically incorrect for a kinase—the nucleophile is the substrate's hydroxyl, not a residue in the enzyme. Option C correctly identifies the proton-acceptor role of the HRD aspartate. A model with general kinase biochemistry knowledge can identify the HRD motif in the sequence and reason that its aspartate is the proton acceptor, distinguishing C from A.",
    "missing_item_specific_fact": "None critical. The exact position number 240 requires counting through the sequence, but the functional role (proton acceptor vs. nucleophile) and the impossibility of positions beyond 1598 provide sufficient reasoning grounds.",
    "reason": "The question is answerable by (1) checking sequence length to eliminate B and D, (2) recognizing kinase domain motifs in the sequence, and (3) applying general knowledge that the HRD aspartate is the proton acceptor in protein kinase catalysis, not a nucleophile. This distinguishes C from A without needing to look up the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D reference positions (1978, 5828) that exceed the 1598-residue protein length and invoke unrelated 'beta-ketoacyl synthase' activity, making them trivially incorrect. Option A misattributes a 'nucleophile' role inconsistent with kinase mechanism. Only C is mechanistically and structurally consistent with the protein's identity as a Ser/Thr kinase."
  },
  "important_caveats": [
    "The active-site annotation at position 240 carries evidence code ECO:0000255 (PROSITE-ProRule), indicating a computational/protein-rule-based assignment rather than direct experimental mutagenesis or crystallographic proof of proton-acceptor function.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence analysis and general kinase biochemistry.",
    "The distractors B and D are extremely weak (impossible positions, unrelated enzyme class), making the question easier than typical active-site prediction tasks.",
    "The UniProt entry was first released 2025-06-18; the author's source snapshot date is unknown, though the sequence has been stable since 2013 (sequence version 1)."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `S8GI44` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"NIMA-related protein kinase NIMA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein kinase Nek1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30865554","source":"PubMed"}],"value":"TgNek1"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/features/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":240},"start":{"modifier":"EXACT","value":240}},"type":"Active site"}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/features/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:30616"}],"ligand":{"id":"ChEBI:CHEBI:30616","name":"ATP"},"location":{"end":{"modifier":"EXACT","value":120},"start":{"modifier":"EXACT","value":112}},"type":"Binding site"}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/features/34`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:30616"}],"ligand":{"id":"ChEBI:CHEBI:30616","name":"ATP"},"location":{"end":{"modifier":"EXACT","value":135},"start":{"modifier":"EXACT","value":135}},"type":"Binding site"}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 222-224`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
FT   ACT_SITE        240
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 225-228`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
FT   BINDING         112..120
FT                   /ligand="ATP"
FT                   /ligand_id="ChEBI:CHEBI:30616"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 229-232`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
FT   BINDING         135
FT                   /ligand="ATP"
FT                   /ligand_id="ChEBI:CHEBI:30616"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
