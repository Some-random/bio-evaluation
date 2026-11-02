# cofactor_0095

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMRRPPSQGRWSASHQKLLLAFAFILIPWLQLADAQQQPQQPQIRIHSQRGDAPLDKVADDANTRWYATHAAPDVHPEAKFDTVNRKQKQQSTASPQQHQKYRRAPYDYASKDKAQNRYAQHPIRESEKPNYVKVPNDASALATLAPAQPVRAPHTSRHHWPSSSAASGLASPQNARSLEDWEVEDFVLLATVDGDLYASDRKTGRHLWHLEVDQPVVETKHYRTNNSVLDDDYRPVDHYIWAVEPSRDGGLYVWIPDSGAGLVRTGFTMKHLVEELAPYAGDEPPVVYTGDKKTTMVTLDAATGRVLKWFGSSGSQVNEAESCLRPNAFDDRDTTECSSMGTITLGRTEYTVGIQRRDGRPIATLKYAEWGPNTFDSDLYQQYHASLDNHYITSQHDGRIYAFDKSQAENDLPLYTHKFSSPVARVFDVCRPWDANAGSNPELVVLPQPPIPALDESTVKMRSNSIFLNQTESGDWYALSGRAYPLILDAPVAQISRDDLWDMAHAFDSINPNKLSKALVGTHFLNPVKSTGYHQPPTLPAGALDEYYEDLENASNNAHAVTNTVPEEPTIITKVKALPQSAANSVIDFVSNPILIIFLIGSLIYNEKKLRRSYHRFRTHGTIKDVYPFFVIESEAGDESGDDKDGVFPSSPSPRSQPQDQNAEDHLSRHKVERNAGDQDKVKDNRSLHDVSDTLEPSNKTVEKTADVVKQVDVAGPDAPSTDSNGAAPEKKKKAHRGRRGGVKHRKGRPTDGSQSHENDPALTTVDEAVSNAKKLGDRPSLEPDVMTIYNDMQAVTGSVISMGNIEVDTDVELGMGSNGTVVFAGRFDGRDVAVKRMTIQFYDIATRETKLLRESDDHPNVIRYYSQVQRGDFLYIALERCAASLADVIEKPYAFGELAKAGQKDLPGVLYQITNGISHLHSLRIVHRDLKPQNILVNLDKDGRPRLLVSDFGLCKKLEDRQSSFGATTGRAAGTSGWRAPELLLDDDGQNPAAIDSSTHSGSHTILVGDPNSLSNGGRATRAIDIFSLGLVFFYVLTNGSHPFDCGDRYMREVNIRKGNYNLDPLDALGDFAYEAKDLIASMLQASPKARPDSREVMAHPFFWSPKKRLAFLCDVSDSLEKEVRDPPSPALVELERHAPEVIKGDFLKVLTRDFVESLGKQRKYTGNKLLDLLRALRNKRNHYEDMSDSLKRSVGSLPDGYLAYWTVKFPMLLLTCWNVVYNLEWEKTDRFREYYEPAGL

[Multiple Choices]
A. Mg(2+)
B. Co(2+)
C. Zn(2+)
D. pantetheine 4'-phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity from UniProtKB:P32361, rather than shown here as a direct experiment on this protein, but it supports the key.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein-kinase catalytic domain, including the HRDLK and DFG motifs. Kinases generally use Mg(2+) to support ATP-dependent catalysis, providing a biological basis to prefer Mg(2+) over Co(2+), Zn(2+), or pantetheine 4'-phosphate.


**Missing item-specific fact**

> No item-specific fact is necessary to distinguish these choices at the level asked; direct experimental confirmation for this exact protein is not supplied.


**Reason**

> The kinase-domain evidence and standard kinase chemistry meaningfully distinguish Mg(2+) from the alternatives. This is a defensible inference, though not proof of the exact protein's experimentally measured cofactor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, Mg(2+) is the biologically appropriate choice for the recognizable kinase activity.


### Important caveats

- The supporting database cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein.
- The reviewer-only annotation and sequence identity were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein-kinase catalytic domain, including the HRDLK and DFG motifs. Kinases generally use Mg(2+) to support ATP-dependent catalysis, providing a biological basis to prefer Mg(2+) over Co(2+), Zn(2+), or pantetheine 4'-phosphate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish these choices at the level asked; direct experimental confirmation for this exact protein is not supplied.",
    "reason": "The kinase-domain evidence and standard kinase chemistry meaningfully distinguish Mg(2+) from the alternatives. This is a defensible inference, though not proof of the exact protein's experimentally measured cofactor."
  },
  "case_id": "cofactor_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity from UniProtKB:P32361, rather than shown here as a direct experiment on this protein, but it supports the key."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein.",
    "The reviewer-only annotation and sequence identity were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, Mg(2+) is the biologically appropriate choice for the recognizable kinase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity from UniProtKB:P32361, rather than shown here as a direct experiment on this protein, but it supports the key.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein-kinase catalytic domain, including the HRDLK and DFG motifs. Kinases generally use Mg(2+) to support ATP-dependent catalysis, providing a biological basis to prefer Mg(2+) over Co(2+), Zn(2+), or pantetheine 4'-phosphate.",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish these choices at the level asked; direct experimental confirmation for this exact protein is not supplied.",
    "reason": "The kinase-domain evidence and standard kinase chemistry meaningfully distinguish Mg(2+) from the alternatives. This is a defensible inference, though not proof of the exact protein's experimentally measured cofactor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, Mg(2+) is the biologically appropriate choice for the recognizable kinase activity."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not direct experimental evidence for this exact protein.",
    "The reviewer-only annotation and sequence identity were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists Mg(2+) as the cofactor for this protein (G0RBE3, Serine/threonine-protein kinase/endoribonuclease IRE1). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from human IRE1 (P32361), not directly measured for this fungal ortholog. Nevertheless, the protein is annotated as a Ser/Thr protein kinase (EC 2.7.11.1), and the sequence contains canonical kinase-domain motifs (DFG motif 'DFGLCKK', HRD catalytic-loop motif 'HRDLKPQ', and a glycine-rich loop region). The universal biochemical requirement of Mg(2+) for phosphotransfer in protein kinases independently supports the key.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied 1243-aa sequence contains recognizable protein-kinase catalytic-domain motifs: the DFG motif ('DFGLCKK' near residue ~700), the HRD catalytic-loop motif ('HRDLKPQ'), and a glycine-rich phosphate-binding loop. Recognizing these motifs identifies the protein as a Ser/Thr kinase. General biochemistry establishes that all protein kinases require Mg(2+) to chelate the β- and γ-phosphates of ATP during phosphotransfer; no kinase uses Co(2+), Zn(2+), or pantetheine 4'-phosphate as its primary catalytic cofactor. The distractors correspond to other enzyme classes (Co(2+) in some oxidoreductases, Zn(2+) in metalloproteases/dehydrogenases, pantetheine 4'-phosphate in acyl-carrier/fatty-acid-synthase systems), making them readily eliminable by functional reasoning.


**Missing item-specific fact**

> None required beyond general kinase biochemistry and the ability to spot conserved kinase-domain motifs in the sequence.


**Reason**

> A model with knowledge of kinase-domain sequence signatures and the universal Mg(2+) requirement for phosphotransfer can identify the correct answer from the sequence and general biology without needing to recall the specific UniProt entry for G0RBE3.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has dual activities (kinase and endoribonuclease), but both are Mg(2+)-dependent in IRE1 orthologs. None of the other three choices (Co(2+), Zn(2+), pantetheine 4'-phosphate) is a plausible cofactor for either activity. The question is unambiguous.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human IRE1 P32361), not direct experimental measurement on the T. reesei protein. This is a database-transfer annotation, though the underlying biochemistry (Mg(2+) for kinase activity) is universally established.
- The protein also carries an endoribonuclease (EC 3.1.26.-) annotation; the question's phrasing 'the specific cofactor' is slightly imprecise given two catalytic activities, but both depend on Mg(2+), so this does not create ambiguity among the choices.
- The sequence is 1243 aa and matches the canonical UniProt entry exactly (SHA-256 match confirmed for both current and historical records).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied 1243-aa sequence contains recognizable protein-kinase catalytic-domain motifs: the DFG motif ('DFGLCKK' near residue ~700), the HRD catalytic-loop motif ('HRDLKPQ'), and a glycine-rich phosphate-binding loop. Recognizing these motifs identifies the protein as a Ser/Thr kinase. General biochemistry establishes that all protein kinases require Mg(2+) to chelate the β- and γ-phosphates of ATP during phosphotransfer; no kinase uses Co(2+), Zn(2+), or pantetheine 4'-phosphate as its primary catalytic cofactor. The distractors correspond to other enzyme classes (Co(2+) in some oxidoreductases, Zn(2+) in metalloproteases/dehydrogenases, pantetheine 4'-phosphate in acyl-carrier/fatty-acid-synthase systems), making them readily eliminable by functional reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required beyond general kinase biochemistry and the ability to spot conserved kinase-domain motifs in the sequence.",
    "reason": "A model with knowledge of kinase-domain sequence signatures and the universal Mg(2+) requirement for phosphotransfer can identify the correct answer from the sequence and general biology without needing to recall the specific UniProt entry for G0RBE3."
  },
  "case_id": "cofactor_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Mg(2+) as the cofactor for this protein (G0RBE3, Serine/threonine-protein kinase/endoribonuclease IRE1). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from human IRE1 (P32361), not directly measured for this fungal ortholog. Nevertheless, the protein is annotated as a Ser/Thr protein kinase (EC 2.7.11.1), and the sequence contains canonical kinase-domain motifs (DFG motif 'DFGLCKK', HRD catalytic-loop motif 'HRDLKPQ', and a glycine-rich loop region). The universal biochemical requirement of Mg(2+) for phosphotransfer in protein kinases independently supports the key."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human IRE1 P32361), not direct experimental measurement on the T. reesei protein. This is a database-transfer annotation, though the underlying biochemistry (Mg(2+) for kinase activity) is universally established.",
    "The protein also carries an endoribonuclease (EC 3.1.26.-) annotation; the question's phrasing 'the specific cofactor' is slightly imprecise given two catalytic activities, but both depend on Mg(2+), so this does not create ambiguity among the choices.",
    "The sequence is 1243 aa and matches the canonical UniProt entry exactly (SHA-256 match confirmed for both current and historical records)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has dual activities (kinase and endoribonuclease), but both are Mg(2+)-dependent in IRE1 orthologs. None of the other three choices (Co(2+), Zn(2+), pantetheine 4'-phosphate) is a plausible cofactor for either activity. The question is unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Mg(2+) as the cofactor for this protein (G0RBE3, Serine/threonine-protein kinase/endoribonuclease IRE1). The evidence code ECO:0000250 indicates the annotation is transferred by similarity from human IRE1 (P32361), not directly measured for this fungal ortholog. Nevertheless, the protein is annotated as a Ser/Thr protein kinase (EC 2.7.11.1), and the sequence contains canonical kinase-domain motifs (DFG motif 'DFGLCKK', HRD catalytic-loop motif 'HRDLKPQ', and a glycine-rich loop region). The universal biochemical requirement of Mg(2+) for phosphotransfer in protein kinases independently supports the key.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied 1243-aa sequence contains recognizable protein-kinase catalytic-domain motifs: the DFG motif ('DFGLCKK' near residue ~700), the HRD catalytic-loop motif ('HRDLKPQ'), and a glycine-rich phosphate-binding loop. Recognizing these motifs identifies the protein as a Ser/Thr kinase. General biochemistry establishes that all protein kinases require Mg(2+) to chelate the β- and γ-phosphates of ATP during phosphotransfer; no kinase uses Co(2+), Zn(2+), or pantetheine 4'-phosphate as its primary catalytic cofactor. The distractors correspond to other enzyme classes (Co(2+) in some oxidoreductases, Zn(2+) in metalloproteases/dehydrogenases, pantetheine 4'-phosphate in acyl-carrier/fatty-acid-synthase systems), making them readily eliminable by functional reasoning.",
    "missing_item_specific_fact": "None required beyond general kinase biochemistry and the ability to spot conserved kinase-domain motifs in the sequence.",
    "reason": "A model with knowledge of kinase-domain sequence signatures and the universal Mg(2+) requirement for phosphotransfer can identify the correct answer from the sequence and general biology without needing to recall the specific UniProt entry for G0RBE3."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has dual activities (kinase and endoribonuclease), but both are Mg(2+)-dependent in IRE1 orthologs. None of the other three choices (Co(2+), Zn(2+), pantetheine 4'-phosphate) is a plausible cofactor for either activity. The question is unambiguous."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from human IRE1 P32361), not direct experimental measurement on the T. reesei protein. This is a database-transfer annotation, though the underlying biochemistry (Mg(2+) for kinase activity) is universally established.",
    "The protein also carries an endoribonuclease (EC 3.1.26.-) annotation; the question's phrasing 'the specific cofactor' is slightly imprecise given two catalytic activities, but both depend on Mg(2+), so this does not create ambiguity among the choices.",
    "The sequence is 1243 aa and matches the canonical UniProt entry exactly (SHA-256 match confirmed for both current and historical records)."
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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"name":"Mg(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 6-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein kinase/endoribonuclease IRE1 {ECO:0000250|UniProtKB:P32361};
DE   AltName: Full=Endoplasmic reticulum-to-nucleus signaling 1 {ECO:0000250|UniProtKB:P32361};
DE   Includes:
DE     RecName: Full=Serine/threonine-protein kinase;
DE              EC=2.7.11.1 {ECO:0000250|UniProtKB:P32361};
DE   Includes:
DE     RecName: Full=Endoribonuclease;
DE              EC=3.1.26.- {ECO:0000250|UniProtKB:P32361};
DE   Flags: Precursor;
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 66-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:P32361};
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 95. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
