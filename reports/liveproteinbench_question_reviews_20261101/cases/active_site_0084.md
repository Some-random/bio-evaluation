# active_site_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 931 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMRRPPSQGRWSASHQKLLLAFAFILIPWLQLADAQQQPQQPQIRIHSQRGDAPLDKVADDANTRWYATHAAPDVHPEAKFDTVNRKQKQQSTASPQQHQKYRRAPYDYASKDKAQNRYAQHPIRESEKPNYVKVPNDASALATLAPAQPVRAPHTSRHHWPSSSAASGLASPQNARSLEDWEVEDFVLLATVDGDLYASDRKTGRHLWHLEVDQPVVETKHYRTNNSVLDDDYRPVDHYIWAVEPSRDGGLYVWIPDSGAGLVRTGFTMKHLVEELAPYAGDEPPVVYTGDKKTTMVTLDAATGRVLKWFGSSGSQVNEAESCLRPNAFDDRDTTECSSMGTITLGRTEYTVGIQRRDGRPIATLKYAEWGPNTFDSDLYQQYHASLDNHYITSQHDGRIYAFDKSQAENDLPLYTHKFSSPVARVFDVCRPWDANAGSNPELVVLPQPPIPALDESTVKMRSNSIFLNQTESGDWYALSGRAYPLILDAPVAQISRDDLWDMAHAFDSINPNKLSKALVGTHFLNPVKSTGYHQPPTLPAGALDEYYEDLENASNNAHAVTNTVPEEPTIITKVKALPQSAANSVIDFVSNPILIIFLIGSLIYNEKKLRRSYHRFRTHGTIKDVYPFFVIESEAGDESGDDKDGVFPSSPSPRSQPQDQNAEDHLSRHKVERNAGDQDKVKDNRSLHDVSDTLEPSNKTVEKTADVVKQVDVAGPDAPSTDSNGAAPEKKKKAHRGRRGGVKHRKGRPTDGSQSHENDPALTTVDEAVSNAKKLGDRPSLEPDVMTIYNDMQAVTGSVISMGNIEVDTDVELGMGSNGTVVFAGRFDGRDVAVKRMTIQFYDIATRETKLLRESDDHPNVIRYYSQVQRGDFLYIALERCAASLADVIEKPYAFGELAKAGQKDLPGVLYQITNGISHLHSLRIVHRDLKPQNILVNLDKDGRPRLLVSDFGLCKKLEDRQSSFGATTGRAAGTSGWRAPELLLDDDGQNPAAIDSSTHSGSHTILVGDPNSLSNGGRATRAIDIFSLGLVFFYVLTNGSHPFDCGDRYMREVNIRKGNYNLDPLDALGDFAYEAKDLIASMLQASPKARPDSREVMAHPFFWSPKKRLAFLCDVSDSLEKEVRDPPSPALVELERHAPEVIKGDFLKVLTRDFVESLGKQRKYTGNKLLDLLRALRNKRNHYEDMSDSLKRSVGSLPDGYLAYWTVKFPMLLLTCWNVVYNLEWEKTDRFREYYEPAGL

[Multiple Choices]
A. Position 218 (Proton donor)
B. Position 2056 (For beta-ketoacyl synthase 2 activity)
C. Position 1371 (For beta-ketoacyl synthase activity)
D. Position 931 (Proton acceptor)
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

> The exact matched sequence has a UniProt active-site annotation at position 931 labeled “Proton acceptor,” supporting choice D. The annotation is attributed to a PROSITE-ProRule, so it is computationally inferred rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a reliable general biological route to identify residue 931 as the proton acceptor. The out-of-range positions in choices B and C can be excluded from this 1243-residue sequence, but that does not establish D over the remaining in-range alternative.


**Missing item-specific fact**

> The protein-specific catalytic-site annotation identifying residue 931 as the proton acceptor.


**Reason**

> Determining the precise catalytic residue and its role requires protein-specific annotation or equivalent external knowledge; recognizing or predicting the protein would not itself make the answer derivable from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence’s active-site annotation supports D; the evidence provided does not support another listed option.


### Important caveats

- The annotation is PROSITE-rule based, not shown here as experimentally established.
- The exact sequence match and the annotation’s historical presence are reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a reliable general biological route to identify residue 931 as the proton acceptor. The out-of-range positions in choices B and C can be excluded from this 1243-residue sequence, but that does not establish D over the remaining in-range alternative.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic-site annotation identifying residue 931 as the proton acceptor.",
    "reason": "Determining the precise catalytic residue and its role requires protein-specific annotation or equivalent external knowledge; recognizing or predicting the protein would not itself make the answer derivable from the supplied information."
  },
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt active-site annotation at position 931 labeled “Proton acceptor,” supporting choice D. The annotation is attributed to a PROSITE-ProRule, so it is computationally inferred rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The annotation is PROSITE-rule based, not shown here as experimentally established.",
    "The exact sequence match and the annotation’s historical presence are reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s active-site annotation supports D; the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt active-site annotation at position 931 labeled “Proton acceptor,” supporting choice D. The annotation is attributed to a PROSITE-ProRule, so it is computationally inferred rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a reliable general biological route to identify residue 931 as the proton acceptor. The out-of-range positions in choices B and C can be excluded from this 1243-residue sequence, but that does not establish D over the remaining in-range alternative.",
    "missing_item_specific_fact": "The protein-specific catalytic-site annotation identifying residue 931 as the proton acceptor.",
    "reason": "Determining the precise catalytic residue and its role requires protein-specific annotation or equivalent external knowledge; recognizing or predicting the protein would not itself make the answer derivable from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s active-site annotation supports D; the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The annotation is PROSITE-rule based, not shown here as experimentally established.",
    "The exact sequence match and the annotation’s historical presence are reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G0RBE3 (Serine/threonine-protein kinase/endoribonuclease IRE1 from Trichoderma reesei, 1243 AA, sequence matched) annotates an Active site at position 931 described as 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). This is a computational/prosite-pattern annotation rather than experimental, but it is the official database annotation and is consistent with the HRD-motif catalytic aspartate of protein kinases. The surrounding ATP-binding (815-823, 837) and Mg2+-binding (936, 953) sites confirm position 931 lies in the kinase catalytic loop.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C12](#evidence-c12), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple general-knowledge reasoning steps distinguish D: (1) Position 2056 exceeds the 1243-residue protein length, eliminating B trivially. (2) Choices B and C reference 'beta-ketoacyl synthase' activity, which is entirely inconsistent with the visible kinase motifs (HRD, DFG, glycine-rich loop) in the C-terminal region; no beta-ketoacyl synthase motifs are present, eliminating C. (3) In protein kinases the catalytic aspartate in the HRD motif acts as a proton acceptor (accepting the proton from the substrate hydroxyl during phosphoryl transfer), not a proton donor—making the functional description in A ('Proton donor') mechanistically wrong for a kinase. (4) Position 218 falls in the N-terminal ER-luminal regulatory region, far from the kinase catalytic domain (ATP-binding at 815-823, Mg2+ at 936), while position 931 aligns with the HRD catalytic aspartate. A model with general kinase catalytic knowledge can reach D without memorizing this specific UniProt entry.


**Missing item-specific fact**

> None critical. Precise residue counting to confirm position 931 is tedious but the HRD motif ('HRDLKPQN') is identifiable by pattern, and the proton-acceptor role of the HRD aspartate is general kinase biochemistry.


**Reason**

> The distractors are eliminable by general biological reasoning (sequence-length check, wrong enzyme class, wrong catalytic mechanism for kinases). The correct answer follows from recognizing kinase motifs and applying the well-established principle that the HRD aspartate is the catalytic proton acceptor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is impossible (position > sequence length), C references a completely unrelated enzyme class, and A assigns the wrong catalytic role (proton donor) and wrong domain location. Only D is consistent with both the sequence content and kinase catalytic mechanism.


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., computational inference from a conserved motif, not direct experimental measurement.
- The protein is annotated as a bifunctional kinase/endoribonuclease; only the kinase active site is annotated at position 931. The endoribonuclease active site (in the RNase domain) is not annotated, so the question implicitly targets the kinase function.
- Position 2056 in choice B exceeds the 1243-residue sequence length, making it trivially eliminable and reducing the effective difficulty of the question.
- The UniProt entry was first released in February 2025; the benchmark construction date is unknown, so the author may have used an earlier TrEMBL record or a different annotation source.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple general-knowledge reasoning steps distinguish D: (1) Position 2056 exceeds the 1243-residue protein length, eliminating B trivially. (2) Choices B and C reference 'beta-ketoacyl synthase' activity, which is entirely inconsistent with the visible kinase motifs (HRD, DFG, glycine-rich loop) in the C-terminal region; no beta-ketoacyl synthase motifs are present, eliminating C. (3) In protein kinases the catalytic aspartate in the HRD motif acts as a proton acceptor (accepting the proton from the substrate hydroxyl during phosphoryl transfer), not a proton donor—making the functional description in A ('Proton donor') mechanistically wrong for a kinase. (4) Position 218 falls in the N-terminal ER-luminal regulatory region, far from the kinase catalytic domain (ATP-binding at 815-823, Mg2+ at 936), while position 931 aligns with the HRD catalytic aspartate. A model with general kinase catalytic knowledge can reach D without memorizing this specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Precise residue counting to confirm position 931 is tedious but the HRD motif ('HRDLKPQN') is identifiable by pattern, and the proton-acceptor role of the HRD aspartate is general kinase biochemistry.",
    "reason": "The distractors are eliminable by general biological reasoning (sequence-length check, wrong enzyme class, wrong catalytic mechanism for kinases). The correct answer follows from recognizing kinase motifs and applying the well-established principle that the HRD aspartate is the catalytic proton acceptor."
  },
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C12",
      "H1",
      "H3",
      "H4",
      "H10"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G0RBE3 (Serine/threonine-protein kinase/endoribonuclease IRE1 from Trichoderma reesei, 1243 AA, sequence matched) annotates an Active site at position 931 described as 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). This is a computational/prosite-pattern annotation rather than experimental, but it is the official database annotation and is consistent with the HRD-motif catalytic aspartate of protein kinases. The surrounding ATP-binding (815-823, 837) and Mg2+-binding (936, 953) sites confirm position 931 lies in the kinase catalytic loop."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., computational inference from a conserved motif, not direct experimental measurement.",
    "The protein is annotated as a bifunctional kinase/endoribonuclease; only the kinase active site is annotated at position 931. The endoribonuclease active site (in the RNase domain) is not annotated, so the question implicitly targets the kinase function.",
    "Position 2056 in choice B exceeds the 1243-residue sequence length, making it trivially eliminable and reducing the effective difficulty of the question.",
    "The UniProt entry was first released in February 2025; the benchmark construction date is unknown, so the author may have used an earlier TrEMBL record or a different annotation source."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is impossible (position > sequence length), C references a completely unrelated enzyme class, and A assigns the wrong catalytic role (proton donor) and wrong domain location. Only D is consistent with both the sequence content and kinase catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G0RBE3 (Serine/threonine-protein kinase/endoribonuclease IRE1 from Trichoderma reesei, 1243 AA, sequence matched) annotates an Active site at position 931 described as 'Proton acceptor' (evidence ECO:0000255|PROSITE-ProRule:PRU00159). This is a computational/prosite-pattern annotation rather than experimental, but it is the official database annotation and is consistent with the HRD-motif catalytic aspartate of protein kinases. The surrounding ATP-binding (815-823, 837) and Mg2+-binding (936, 953) sites confirm position 931 lies in the kinase catalytic loop.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C12", "H1", "H3", "H4", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple general-knowledge reasoning steps distinguish D: (1) Position 2056 exceeds the 1243-residue protein length, eliminating B trivially. (2) Choices B and C reference 'beta-ketoacyl synthase' activity, which is entirely inconsistent with the visible kinase motifs (HRD, DFG, glycine-rich loop) in the C-terminal region; no beta-ketoacyl synthase motifs are present, eliminating C. (3) In protein kinases the catalytic aspartate in the HRD motif acts as a proton acceptor (accepting the proton from the substrate hydroxyl during phosphoryl transfer), not a proton donor—making the functional description in A ('Proton donor') mechanistically wrong for a kinase. (4) Position 218 falls in the N-terminal ER-luminal regulatory region, far from the kinase catalytic domain (ATP-binding at 815-823, Mg2+ at 936), while position 931 aligns with the HRD catalytic aspartate. A model with general kinase catalytic knowledge can reach D without memorizing this specific UniProt entry.",
    "missing_item_specific_fact": "None critical. Precise residue counting to confirm position 931 is tedious but the HRD motif ('HRDLKPQN') is identifiable by pattern, and the proton-acceptor role of the HRD aspartate is general kinase biochemistry.",
    "reason": "The distractors are eliminable by general biological reasoning (sequence-length check, wrong enzyme class, wrong catalytic mechanism for kinases). The correct answer follows from recognizing kinase motifs and applying the well-established principle that the HRD aspartate is the catalytic proton acceptor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is impossible (position > sequence length), C references a completely unrelated enzyme class, and A assigns the wrong catalytic role (proton donor) and wrong domain location. Only D is consistent with both the sequence content and kinase catalytic mechanism."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., computational inference from a conserved motif, not direct experimental measurement.",
    "The protein is annotated as a bifunctional kinase/endoribonuclease; only the kinase active site is annotated at position 931. The endoribonuclease active site (in the RNase domain) is not annotated, so the question implicitly targets the kinase function.",
    "Position 2056 in choice B exceeds the 1243-residue sequence length, making it trivially eliminable and reducing the effective difficulty of the question.",
    "The UniProt entry was first released in February 2025; the benchmark construction date is unknown, so the author may have used an earlier TrEMBL record or a different annotation source."
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

**Accession:** `G0RBE3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 77. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
"G0RBE3"
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"value":"Endoplasmic reticulum-to-nucleus signaling 1"}}],"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"value":"2.7.11.1"}],"fullName":{"value":"Serine/threonine-protein kinase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"value":"3.1.26.-"}],"fullName":{"value":"Endoribonuclease"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"value":"Serine/threonine-protein kinase/endoribonuclease IRE1"}}}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":931},"start":{"modifier":"EXACT","value":931}},"type":"Active site"}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/features/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:30616"}],"ligand":{"id":"ChEBI:CHEBI:30616","name":"ATP"},"location":{"end":{"modifier":"EXACT","value":823},"start":{"modifier":"EXACT","value":815}},"type":"Binding site"}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/features/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:18420"}],"ligand":{"id":"ChEBI:CHEBI:18420","name":"Mg(2+)"},"location":{"end":{"modifier":"EXACT","value":936},"start":{"modifier":"EXACT","value":936}},"type":"Binding site"}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
ID   IRE1_HYPJQ              Reviewed;        1243 AA.
AC   G0RBE3; Q7Z8F3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   28-JAN-2026, entry version 77.
DE   RecName: Full=Serine/threonine-protein kinase/endoribonuclease IRE1 {ECO:0000250|UniProtKB:P32361};
DE   AltName: Full=Endoplasmic reticulum-to-nucleus signaling 1 {ECO:0000250|UniProtKB:P32361};
DE   Includes:
DE     RecName: Full=Serine/threonine-protein kinase;
DE              EC=2.7.11.1 {ECO:0000250|UniProtKB:P32361};
DE   Includes:
DE     RecName: Full=Endoribonuclease;
DE              EC=3.1.26.- {ECO:0000250|UniProtKB:P32361};
DE   Flags: Precursor;
GN   Name=IRE1 {ECO:0000303|PubMed:15480788};
GN   ORFNames=TRIREDRAFT_45242 {ECO:0000312|EMBL:EGR51316.1};
OS   Hypocrea jecorina (strain QM6a) (Trichoderma reesei).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.
OX   NCBI_TaxID=431241 {ECO:0000312|Proteomes:UP000008984};
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 190-192`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
FT   ACT_SITE        931
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 193-196`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
FT   BINDING         815..823
FT                   /ligand="ATP"
FT                   /ligand_id="ChEBI:CHEBI:30616"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 217-220`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
FT   BINDING         936
FT                   /ligand="Mg(2+)"
FT                   /ligand_id="ChEBI:CHEBI:18420"
FT                   /evidence="ECO:0000250|UniProtKB:P32361"
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
