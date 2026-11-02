# catalytic_activity_0029

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

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
A. 1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2
B. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
C. D-alanyl-D-alanine + H2O = 2 D-alanine
D. a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as an IRE1 serine/threonine-protein kinase/endoribonuclease, and the entry lists the reaction in B. That catalytic-activity annotation is transferred by similarity from UniProtKB:P32361 (ECO:0000250), so it supports B but is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein-kinase catalytic region, including HRDLK and DFG motifs, supporting ATP-dependent protein phosphorylation. Of the choices, B is the protein-phosphorylation reaction; the other choices describe unrelated enzyme activities.


**Missing item-specific fact**

> No item-specific fact is needed to distinguish the broad reaction class among these choices. The exact physiological substrates and direct confirmation of serine phosphorylation for this protein are not established by the supplied input.


**Reason**

> The kinase motifs provide a concrete sequence-based basis for choosing the phosphorylation option, rather than requiring recognition of the exact protein or recall of its database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although IRE1 is also annotated as an endoribonuclease, choice D describes removal of terminal phosphate from an mRNA 5′ end, not endonucleolytic RNA cleavage. B is the only choice matching the kinase activity.


### Important caveats

- The cited annotation is transferred from a homolog, not direct experimental evidence for this sequence.
- The entry also annotates threonine phosphorylation, but that reaction is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein-kinase catalytic region, including HRDLK and DFG motifs, supporting ATP-dependent protein phosphorylation. Of the choices, B is the protein-phosphorylation reaction; the other choices describe unrelated enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is needed to distinguish the broad reaction class among these choices. The exact physiological substrates and direct confirmation of serine phosphorylation for this protein are not established by the supplied input.",
    "reason": "The kinase motifs provide a concrete sequence-based basis for choosing the phosphorylation option, rather than requiring recognition of the exact protein or recall of its database annotation."
  },
  "case_id": "catalytic_activity_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an IRE1 serine/threonine-protein kinase/endoribonuclease, and the entry lists the reaction in B. That catalytic-activity annotation is transferred by similarity from UniProtKB:P32361 (ECO:0000250), so it supports B but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited annotation is transferred from a homolog, not direct experimental evidence for this sequence.",
    "The entry also annotates threonine phosphorylation, but that reaction is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although IRE1 is also annotated as an endoribonuclease, choice D describes removal of terminal phosphate from an mRNA 5′ end, not endonucleolytic RNA cleavage. B is the only choice matching the kinase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an IRE1 serine/threonine-protein kinase/endoribonuclease, and the entry lists the reaction in B. That catalytic-activity annotation is transferred by similarity from UniProtKB:P32361 (ECO:0000250), so it supports B but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein-kinase catalytic region, including HRDLK and DFG motifs, supporting ATP-dependent protein phosphorylation. Of the choices, B is the protein-phosphorylation reaction; the other choices describe unrelated enzyme activities.",
    "missing_item_specific_fact": "No item-specific fact is needed to distinguish the broad reaction class among these choices. The exact physiological substrates and direct confirmation of serine phosphorylation for this protein are not established by the supplied input.",
    "reason": "The kinase motifs provide a concrete sequence-based basis for choosing the phosphorylation option, rather than requiring recognition of the exact protein or recall of its database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although IRE1 is also annotated as an endoribonuclease, choice D describes removal of terminal phosphate from an mRNA 5′ end, not endonucleolytic RNA cleavage. B is the only choice matching the kinase activity."
  },
  "important_caveats": [
    "The cited annotation is transferred from a homolog, not direct experimental evidence for this sequence.",
    "The entry also annotates threonine phosphorylation, but that reaction is not among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G0RBE3 (IRE1_HYPJQ, Trichoderma reesei) explicitly annotates the catalytic activity 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)' (EC 2.7.11.1), matching choice B verbatim. The annotation is based on similarity inference (ECO:0000250) to human IRE1 (P32361) rather than direct experimental evidence for this fungal ortholog, but the protein-kinase fold motifs (HRD catalytic loop 'HRDLKPQ', DFG motif 'DFGLCKK', activation segment 'GDFLKVLTRDFVESLGKQRKY') are genuinely present in the supplied sequence and are consistent with a serine/threonine kinase. The entry also lists an endoribonuclease activity (EC 3.1.26.-), but none of the choices describe internal RNA cleavage; choice D describes 5'-cap decapping, which is mechanistically distinct from IRE1's endoribonuclease function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains canonical protein-kinase catalytic motifs: the HRD catalytic loop ('HRDLKPQNILV'), the DFG motif ('DFGLCKK'), a glycine-rich loop region, and a full activation segment ('GDFLKVLTRDFVESLGKQRKY'). A model familiar with kinase architecture can recognize the protein-kinase fold and conclude the enzyme transfers a phosphate from ATP to a protein substrate. This immediately eliminates A (FAD-dependent decarboxylase), C (D-alanyl-D-alanine dipeptidase), and D (mRNA decapping enzyme), all of which involve entirely different catalytic mechanisms and cofactors. The 'HRDLKPQ' pattern (as opposed to the 'HRDLAARN' variant common in tyrosine kinases) further supports a serine/threonine specificity, though this finer distinction is not strictly required since B is the only kinase reaction offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase motifs are directly readable from the sequence and constitute a concrete biological argument that distinguishes B from the non-kinase distractors. No item-specific database lookup is required to eliminate A, C, and D once the kinase fold is recognized.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D describe mechanistically unrelated reactions (decarboxylation, dipeptide hydrolysis, 5'-cap removal) that are incompatible with a protein-kinase catalytic core. IRE1's second activity (endoribonuclease) is not represented among the options, so no ambiguity arises from the bifunctional annotation.


### Important caveats

- The UniProt annotation for G0RBE3 is based on similarity inference (ECO:0000250) to human IRE1 (P32361), not direct in vitro enzymatic characterization of the fungal ortholog. The kinase motifs in the sequence are real, but the precise substrate specificity (Ser vs. Thr preference, specific downstream targets) has not been experimentally validated for this fungal protein.
- The entry is a precursor (transmembrane protein with luminal sensor domain, kinase domain, and RNase domain); the question addresses only the kinase activity and ignores the endoribonuclease function, which is acceptable since no matching option is provided.
- Sequence match is confirmed (SHA-256 identical) between the benchmark input and the UniProt entry G0RBE3.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains canonical protein-kinase catalytic motifs: the HRD catalytic loop ('HRDLKPQNILV'), the DFG motif ('DFGLCKK'), a glycine-rich loop region, and a full activation segment ('GDFLKVLTRDFVESLGKQRKY'). A model familiar with kinase architecture can recognize the protein-kinase fold and conclude the enzyme transfers a phosphate from ATP to a protein substrate. This immediately eliminates A (FAD-dependent decarboxylase), C (D-alanyl-D-alanine dipeptidase), and D (mRNA decapping enzyme), all of which involve entirely different catalytic mechanisms and cofactors. The 'HRDLKPQ' pattern (as opposed to the 'HRDLAARN' variant common in tyrosine kinases) further supports a serine/threonine specificity, though this finer distinction is not strictly required since B is the only kinase reaction offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase motifs are directly readable from the sequence and constitute a concrete biological argument that distinguishes B from the non-kinase distractors. No item-specific database lookup is required to eliminate A, C, and D once the kinase fold is recognized."
  },
  "case_id": "catalytic_activity_0029",
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
    "reason": "The UniProt entry G0RBE3 (IRE1_HYPJQ, Trichoderma reesei) explicitly annotates the catalytic activity 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (EC 2.7.11.1), matching choice B verbatim. The annotation is based on similarity inference (ECO:0000250) to human IRE1 (P32361) rather than direct experimental evidence for this fungal ortholog, but the protein-kinase fold motifs (HRD catalytic loop 'HRDLKPQ', DFG motif 'DFGLCKK', activation segment 'GDFLKVLTRDFVESLGKQRKY') are genuinely present in the supplied sequence and are consistent with a serine/threonine kinase. The entry also lists an endoribonuclease activity (EC 3.1.26.-), but none of the choices describe internal RNA cleavage; choice D describes 5'-cap decapping, which is mechanistically distinct from IRE1's endoribonuclease function."
  },
  "important_caveats": [
    "The UniProt annotation for G0RBE3 is based on similarity inference (ECO:0000250) to human IRE1 (P32361), not direct in vitro enzymatic characterization of the fungal ortholog. The kinase motifs in the sequence are real, but the precise substrate specificity (Ser vs. Thr preference, specific downstream targets) has not been experimentally validated for this fungal protein.",
    "The entry is a precursor (transmembrane protein with luminal sensor domain, kinase domain, and RNase domain); the question addresses only the kinase activity and ignores the endoribonuclease function, which is acceptable since no matching option is provided.",
    "Sequence match is confirmed (SHA-256 identical) between the benchmark input and the UniProt entry G0RBE3."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D describe mechanistically unrelated reactions (decarboxylation, dipeptide hydrolysis, 5'-cap removal) that are incompatible with a protein-kinase catalytic core. IRE1's second activity (endoribonuclease) is not represented among the options, so no ambiguity arises from the bifunctional annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"catalytic_activity_0029","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry G0RBE3 (IRE1_HYPJQ, Trichoderma reesei) explicitly annotates the catalytic activity 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (EC 2.7.11.1), matching choice B verbatim. The annotation is based on similarity inference (ECO:0000250) to human IRE1 (P32361) rather than direct experimental evidence for this fungal ortholog, but the protein-kinase fold motifs (HRD catalytic loop 'HRDLKPQ', DFG motif 'DFGLCKK', activation segment 'GDFLKVLTRDFVESLGKQRKY') are genuinely present in the supplied sequence and are consistent with a serine/threonine kinase. The entry also lists an endoribonuclease activity (EC 3.1.26.-), but none of the choices describe internal RNA cleavage; choice D describes 5'-cap decapping, which is mechanistically distinct from IRE1's endoribonuclease function.","evidence_ids":["C4","C5","C6","H2","H4","H5"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The supplied sequence contains canonical protein-kinase catalytic motifs: the HRD catalytic loop ('HRDLKPQNILV'), the DFG motif ('DFGLCKK'), a glycine-rich loop region, and a full activation segment ('GDFLKVLTRDFVESLGKQRKY'). A model familiar with kinase architecture can recognize the protein-kinase fold and conclude the enzyme transfers a phosphate from ATP to a protein substrate. This immediately eliminates A (FAD-dependent decarboxylase), C (D-alanyl-D-alanine dipeptidase), and D (mRNA decapping enzyme), all of which involve entirely different catalytic mechanisms and cofactors. The 'HRDLKPQ' pattern (as opposed to the 'HRDLAARN' variant common in tyrosine kinases) further supports a serine/threonine specificity, though this finer distinction is not strictly required since B is the only kinase reaction offered.","missing_item_specific_fact":"","reason":"The kinase motifs are directly readable from the sequence and constitute a concrete biological argument that distinguishes B from the non-kinase distractors. No item-specific database lookup is required to eliminate A, C, and D once the kinase fold is recognized."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Choices A, C, and D describe mechanistically unrelated reactions (decarboxylation, dipeptide hydrolysis, 5'-cap removal) that are incompatible with a protein-kinase catalytic core. IRE1's second activity (endoribonuclease) is not represented among the options, so no ambiguity arises from the bifunctional annotation."},"important_caveats":["The UniProt annotation for G0RBE3 is based on similarity inference (ECO:0000250) to human IRE1 (P32361), not direct in vitro enzymatic characterization of the fungal ortholog. The kinase motifs in the sequence are real, but the precise substrate specificity (Ser vs. Thr preference, specific downstream targets) has not been experimentally validated for this fungal protein.","The entry is a precursor (transmembrane protein with luminal sensor domain, kinase domain, and RNase domain); the question addresses only the kinase activity and ignores the endoribonuclease function, which is acceptable since no matching option is provided.","Sequence match is confirmed (SHA-256 identical) between the benchmark input and the UniProt entry G0RBE3."]}
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.334411+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P32361","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
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
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000250|UniProtKB:P32361};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000250|UniProtKB:P32361};
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)  
**Locator:** `lines 58-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 77 / 1.  
**Retrieved:** 2026-11-02T04:28:23.459878+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000250|UniProtKB:P32361};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000250|UniProtKB:P32361};
```

Source SHA-256: `fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
