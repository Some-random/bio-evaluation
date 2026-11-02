# catalytic_activity_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVKVRFDKEVRDYAKGEKVKDSILKLTETALAQALENFHRRMIVIEGDTLRKAELAGILAGASARVLSGILEELMKKRLRDESEDKIEVLYATDALGEETFGRKRYEAFRKHFDVLAGSNVEVKAVTFKHTRDILGRTYDLLILDMSYDYSPNDLGRIIETVRGGGLIFILAHPFEKWKNMWTGFHKSLVTPPYTIDDVKKRFNRRLIRKFTEHDGIYIITEGGKARKKPKRSKSQARIKARKGVPIPEETLFPKELYEMALTEGQVEVLKAFEELVEGGMLVLTADRGRGKSVSVGIGAIGLALALKKRTRIVVTAPELENVQALFRFAKRALERLGFKPYVVEERGLIKELYARKIGLRYYPPADGYKKSADLYILDEAAGIHVPILHKYLNKERVVYSSTIHGYEGAGRGFSVKFLKRAREKREFKELHMDEPIRYAENDPIERWLFDVLLLDAEPVELTEEDFELIEKKEVYLEEPDLDDWFENDREDLRNFVGIYILAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAIQIAKEGGIPKKVIEKMAKGYKPRGNIIPDMMVKHHYLKEFAKLKGYRIVRIATHPDAMDRGLGSKALELLEKEAREKGLDWIGSGFGASEELVRFWVRNGFAVVHLSPARNPVSGEFTAIVLKPISERAKKLIKKANDEFRIRLTEWLGDTHRELEPEIARWLFETPFGEAVDYPVHLTEIQKKRLDAFTGKVLTYDTVVDAVKPIVKLYFLDGWMKPYLDERQIRLLIYRVLQAHSWEETAKLIDRTETFTMIEVRDIIRGLWYYYKRLLKA

[Multiple Choices]
A. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
B. L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O
C. L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine
D. L-leucyl-tRNA(Leu) + acetyl-CoA = N-acetyl-L-leucyl-tRNA(Leu) + CoA + H(+)
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

> The exact sequence matches the annotated Thermococcus sp. AM4 TmcA protein. UniProt assigns it EC 2.3.1.193 and gives the reaction in choice A, based on a HAMAP computational rule. Related catalytic-activity annotations also cite a publication for broader RNA cytidine acetylation; the evidence provided does not independently establish experimental validation of the exact tRNA(Met) C34 reaction for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct, specialized enzyme activities, but the supplied sequence alone offers no clear general biological clue that identifies tRNA(Met) cytidine acetylation rather than the other listed reactions.


**Missing item-specific fact**

> The protein-specific functional annotation that this sequence encodes TmcA, a tRNA cytidine acetyltransferase, and its substrate specificity.


**Reason**

> Identifying this exact reaction requires protein-specific functional knowledge not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A matches the sequence-linked annotation. The evidence for broader RNA cytidine acetylation does not make any of the other listed, chemically distinct reactions an equally supported choice.


### Important caveats

- The exact sequence match is established by reviewer-only evidence, not information provided to the evaluated model.
- The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication supports broader RNA acetylation, not necessarily this precise substrate assignment for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct, specialized enzyme activities, but the supplied sequence alone offers no clear general biological clue that identifies tRNA(Met) cytidine acetylation rather than the other listed reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation that this sequence encodes TmcA, a tRNA cytidine acetyltransferase, and its substrate specificity.",
    "reason": "Identifying this exact reaction requires protein-specific functional knowledge not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Thermococcus sp. AM4 TmcA protein. UniProt assigns it EC 2.3.1.193 and gives the reaction in choice A, based on a HAMAP computational rule. Related catalytic-activity annotations also cite a publication for broader RNA cytidine acetylation; the evidence provided does not independently establish experimental validation of the exact tRNA(Met) C34 reaction for this protein."
  },
  "important_caveats": [
    "The exact sequence match is established by reviewer-only evidence, not information provided to the evaluated model.",
    "The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication supports broader RNA acetylation, not necessarily this precise substrate assignment for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A matches the sequence-linked annotation. The evidence for broader RNA cytidine acetylation does not make any of the other listed, chemically distinct reactions an equally supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Thermococcus sp. AM4 TmcA protein. UniProt assigns it EC 2.3.1.193 and gives the reaction in choice A, based on a HAMAP computational rule. Related catalytic-activity annotations also cite a publication for broader RNA cytidine acetylation; the evidence provided does not independently establish experimental validation of the exact tRNA(Met) C34 reaction for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct, specialized enzyme activities, but the supplied sequence alone offers no clear general biological clue that identifies tRNA(Met) cytidine acetylation rather than the other listed reactions.",
    "missing_item_specific_fact": "The protein-specific functional annotation that this sequence encodes TmcA, a tRNA cytidine acetyltransferase, and its substrate specificity.",
    "reason": "Identifying this exact reaction requires protein-specific functional knowledge not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A matches the sequence-linked annotation. The evidence for broader RNA cytidine acetylation does not make any of the other listed, chemically distinct reactions an equally supported choice."
  },
  "important_caveats": [
    "The exact sequence match is established by reviewer-only evidence, not information provided to the evaluated model.",
    "The exact tRNA(Met) C34 reaction annotation is attributed to a computational HAMAP rule; the cited publication supports broader RNA acetylation, not necessarily this precise substrate assignment for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B7R4L8 (sequence matched exactly, 811 AA, Thermococcus sp. AM4) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193). The catalytic activity comment (C5/H4) reproduces the expected answer text verbatim. However, the primary evidence code is ECO:0000255 (HAMAP-Rule, computational inference by similarity), not direct experimental characterization of this specific enzyme. Broader RNA acetylation activity is supported by PubMed:32555463 (Sas-Chen et al., Nature 2020) with ECO:0000305 (inferred by curator). The specific 'cytidine(34) in elongator tRNA(Met)' formulation derives from the HAMAP rule annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choices B (monooxygenase/demethylase requiring FAD or Fe-S clusters) and C (cobalamin-dependent methyltransferase) can potentially be eliminated by noting the absence of canonical cofactor-binding motifs in the sequence. Both A and D are acetyl-CoA-dependent acetyltransferases, and the sequence does contain GNAT-like motifs (e.g., 'GSGFGAS' region). However, distinguishing A (tRNA cytidine acetyltransferase, TmcA architecture with dedicated tRNA-binding domains) from D (GNAT aminoacyl-tRNA acetyltransferase) requires recognizing the specific multi-domain TmcA fold and its tRNA-substrate specificity, which is not inferable from generic acetyltransferase motif recognition alone.


**Missing item-specific fact**

> Recognition that this specific 811-aa archaeal protein belongs to the TmcA family (tRNA(Met) cytidine acetyltransferase) rather than a GNAT-type aminoacyl-tRNA acetyltransferase. The UniProt annotation itself is assigned by HAMAP-Rule computational similarity, meaning even the database annotation does not rest on direct experimental characterization of this enzyme's substrate specificity.


**Reason**

> The question requires identifying a specific enzyme's catalytic reaction from a raw amino acid sequence. While broad enzyme-class elimination (ruling out B and C) is feasible via cofactor-domain reasoning, the critical distinction between A and D—both acetyl-CoA acetyltransferases—depends on recognizing the specific TmcA domain architecture and its tRNA anticodon-modification function. This is an item-specific protein-family identification, not a general biological inference derivable from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although A and D both involve acetyl-CoA-dependent acetylation, D specifies acetylation of the amino group of a leucyl-tRNA (a GNAT-type reaction on the amino acid moiety), whereas A specifies N4-acetylation of a cytidine base in tRNA. These are mechanistically and structurally distinct reactions. Given the UniProt annotation, only A is correct. No other option is defensible for this protein.


### Important caveats

- The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational inference by similarity, not direct experimental characterization of this specific enzyme.
- The 2020 Nature paper (Sas-Chen et al., PubMed:32555463) demonstrated RNA acetylation activity in the TmcA family but with ECO:0000305 (inferred by curator), not direct biochemical assay of this exact protein.
- The sequence match to B7R4L8 is exact (SHA-256 confirmed), and the historical entry (version 76, released 2026-01-28) also carries the same annotation.
- The accession B7R4L8 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choices B (monooxygenase/demethylase requiring FAD or Fe-S clusters) and C (cobalamin-dependent methyltransferase) can potentially be eliminated by noting the absence of canonical cofactor-binding motifs in the sequence. Both A and D are acetyl-CoA-dependent acetyltransferases, and the sequence does contain GNAT-like motifs (e.g., 'GSGFGAS' region). However, distinguishing A (tRNA cytidine acetyltransferase, TmcA architecture with dedicated tRNA-binding domains) from D (GNAT aminoacyl-tRNA acetyltransferase) requires recognizing the specific multi-domain TmcA fold and its tRNA-substrate specificity, which is not inferable from generic acetyltransferase motif recognition alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this specific 811-aa archaeal protein belongs to the TmcA family (tRNA(Met) cytidine acetyltransferase) rather than a GNAT-type aminoacyl-tRNA acetyltransferase. The UniProt annotation itself is assigned by HAMAP-Rule computational similarity, meaning even the database annotation does not rest on direct experimental characterization of this enzyme's substrate specificity.",
    "reason": "The question requires identifying a specific enzyme's catalytic reaction from a raw amino acid sequence. While broad enzyme-class elimination (ruling out B and C) is feasible via cofactor-domain reasoning, the critical distinction between A and D—both acetyl-CoA acetyltransferases—depends on recognizing the specific TmcA domain architecture and its tRNA anticodon-modification function. This is an item-specific protein-family identification, not a general biological inference derivable from the sequence alone."
  },
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B7R4L8 (sequence matched exactly, 811 AA, Thermococcus sp. AM4) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193). The catalytic activity comment (C5/H4) reproduces the expected answer text verbatim. However, the primary evidence code is ECO:0000255 (HAMAP-Rule, computational inference by similarity), not direct experimental characterization of this specific enzyme. Broader RNA acetylation activity is supported by PubMed:32555463 (Sas-Chen et al., Nature 2020) with ECO:0000305 (inferred by curator). The specific 'cytidine(34) in elongator tRNA(Met)' formulation derives from the HAMAP rule annotation."
  },
  "important_caveats": [
    "The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational inference by similarity, not direct experimental characterization of this specific enzyme.",
    "The 2020 Nature paper (Sas-Chen et al., PubMed:32555463) demonstrated RNA acetylation activity in the TmcA family but with ECO:0000305 (inferred by curator), not direct biochemical assay of this exact protein.",
    "The sequence match to B7R4L8 is exact (SHA-256 confirmed), and the historical entry (version 76, released 2026-01-28) also carries the same annotation.",
    "The accession B7R4L8 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D both involve acetyl-CoA-dependent acetylation, D specifies acetylation of the amino group of a leucyl-tRNA (a GNAT-type reaction on the amino acid moiety), whereas A specifies N4-acetylation of a cytidine base in tRNA. These are mechanistically and structurally distinct reactions. Given the UniProt annotation, only A is correct. No other option is defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B7R4L8 (sequence matched exactly, 811 AA, Thermococcus sp. AM4) annotates this protein as 'tRNA(Met) cytidine acetyltransferase TmcA' (EC 2.3.1.193). The catalytic activity comment (C5/H4) reproduces the expected answer text verbatim. However, the primary evidence code is ECO:0000255 (HAMAP-Rule, computational inference by similarity), not direct experimental characterization of this specific enzyme. Broader RNA acetylation activity is supported by PubMed:32555463 (Sas-Chen et al., Nature 2020) with ECO:0000305 (inferred by curator). The specific 'cytidine(34) in elongator tRNA(Met)' formulation derives from the HAMAP rule annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choices B (monooxygenase/demethylase requiring FAD or Fe-S clusters) and C (cobalamin-dependent methyltransferase) can potentially be eliminated by noting the absence of canonical cofactor-binding motifs in the sequence. Both A and D are acetyl-CoA-dependent acetyltransferases, and the sequence does contain GNAT-like motifs (e.g., 'GSGFGAS' region). However, distinguishing A (tRNA cytidine acetyltransferase, TmcA architecture with dedicated tRNA-binding domains) from D (GNAT aminoacyl-tRNA acetyltransferase) requires recognizing the specific multi-domain TmcA fold and its tRNA-substrate specificity, which is not inferable from generic acetyltransferase motif recognition alone.",
    "missing_item_specific_fact": "Recognition that this specific 811-aa archaeal protein belongs to the TmcA family (tRNA(Met) cytidine acetyltransferase) rather than a GNAT-type aminoacyl-tRNA acetyltransferase. The UniProt annotation itself is assigned by HAMAP-Rule computational similarity, meaning even the database annotation does not rest on direct experimental characterization of this enzyme's substrate specificity.",
    "reason": "The question requires identifying a specific enzyme's catalytic reaction from a raw amino acid sequence. While broad enzyme-class elimination (ruling out B and C) is feasible via cofactor-domain reasoning, the critical distinction between A and D—both acetyl-CoA acetyltransferases—depends on recognizing the specific TmcA domain architecture and its tRNA anticodon-modification function. This is an item-specific protein-family identification, not a general biological inference derivable from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D both involve acetyl-CoA-dependent acetylation, D specifies acetylation of the amino group of a leucyl-tRNA (a GNAT-type reaction on the amino acid moiety), whereas A specifies N4-acetylation of a cytidine base in tRNA. These are mechanistically and structurally distinct reactions. Given the UniProt annotation, only A is correct. No other option is defensible for this protein."
  },
  "important_caveats": [
    "The primary annotation evidence is ECO:0000255 (HAMAP-Rule), a computational inference by similarity, not direct experimental characterization of this specific enzyme.",
    "The 2020 Nature paper (Sas-Chen et al., PubMed:32555463) demonstrated RNA acetylation activity in the TmcA family but with ECO:0000305 (inferred by curator), not direct biochemical assay of this exact protein.",
    "The sequence match to B7R4L8 is exact (SHA-256 confirmed), and the historical entry (version 76, released 2026-01-28) also carries the same annotation.",
    "The accession B7R4L8 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `B7R4L8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 76. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
"B7R4L8"
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA"}}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B7R4L8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:23.286634+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:82211"},{"database":"Rhea","id":"RHEA-COMP:15704"},{"database":"Rhea","id":"RHEA-COMP:19834"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `03548e55c88bf9348a6f65fb414f93b7437267df4d20530afc1cfd7ab5fb87ce`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 24-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
RN   [2]
RP   FUNCTION.
RC   STRAIN=AM4;
RX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;
RA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,
RA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,
RA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,
RA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,
RA   Shalev-Benami M., Meier J.L., Schwartz S.;
RT   "Dynamic RNA acetylation revealed by quantitative cross-evolutionary
RT   mapping.";
RL   Nature 583:638-643(2020).
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 44-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B7R4L8?format=txt&versions=76)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 76 / 1.  
**Retrieved:** 2026-11-02T04:27:25.333292+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `2b39581803c115006a73d534827c01e6b71ccb3d0024965b8d497beced6710ad`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
