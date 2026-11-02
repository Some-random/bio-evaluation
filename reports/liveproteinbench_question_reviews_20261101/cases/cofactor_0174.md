# cofactor_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDNISNHAFNYPVLVLNKGLLPEHDDIALARYLFSALALAVSRITQNEEMIVGFHLHPQEITRWKDDECIRQYILPLNIRFNSATPIAGFIREIMTWMTPDAIHQKNAMGASVLTLGPQHALHDIFDLEISWQPPVESEPVQALTCHVASREDALVLTLRFNPARFSATQMQKLPEVWRQITASAAKNGAETLRDIGLIDDAERQRVLHAFNQTEQAWDGETTVAARLKNRAQRHPEQTAVVFRDETLSYRQLYQQAGALAHYLNALETERERCVGLFVEPSLTLMTGVWGILLSGNAYLPLSPEYPEDRLAYMLENSQTRIIVTQPHLRERLLALAPPGIQVVTSDDVDAFMRQHAHSLPDAPQNDIAPHHLAYVIYTSGSTGKPKGVMIEHHSVLNQMNWLAQTVGLNQETVILQKTPMSFDAAQWEILSPACGCRVVMGEPGVYRNPEQLVDMLAEYRVTTLQCVPTLLQALLDTERLTHCPALRQIFSGGEALQKHLAQACLETLPDCELINLYGPTECTINNSAFRVDPVSVRQGPDTLSIGAPVANTRYYILDNCLTPVAVGQIGELYIGGDGVARGYLNRDDLTAERFIVDPFAPAGSGRRLYQTGDIASWNPDGTVQYAGRADNQVKLRGYRVELDEIRSAIETHEWVKAAAVIVRNDPFTGYQNLISFIELNAREAALMDQGNHGSHHQSKADKAQVMLQLANKGCREFPAASQPYTLDLPGKQPDEKQRLTAFSRKTYRFYDGGAVSREDILSLLHEPLLTAISRQPDALTLDELGHWLRYLGQFTSAERLLPKYTYASPGALYATQVFLELNGVAGLTAGHYYYQPVHHQLVRVSEQAAVTPGSLRLHFVGKKSAIEPIYKNNIREVLQMEMGHIIGMLDIILPDYGLGVALCDAAALDPTPLAIDLDDDYLGACDVLSGPRLPTDDDLDIYVQTAGANIADLPVGTYRYVRGDLQHIADDVIDKKHVIAINQAVYERSSFGISVASRTEGWAGYVHVGRKLQRLQMNPLNIGLMSSGYSSETGNDLPAARRFWQILGHRTGPYYFFIGGRISDEQKYSEGMREDAVHMKGPAEMIRDDLAAFMPDYMMPNKVLILDEMPLTANGKIDMKALANINVELKHKTIVAPRNPLEHQVMAIWQAKLKREEMSVDDNFFESGGNSLIAVSLINELNATLNASLPLQVLFQAPTVEKLAAWLSRARREPVSRLVQLQPKGRQAPIYCWPGLGGYCMNLRLLARQLGAERPFFGIQAHGINPDETPYATIGEMAARDIELIRQHQPHGPYTLWGYSFGARVAFETAWQLELAGEVVENLYLLAPGSPKLRDERVAAMNRKADFDNPGYLTILFSVFIGSITDPELERCLETVRDEESFVAFITGLNPALDDGLVRRITRIVAQTFEFTYTFSELQQRQLNAPVTIIKAQGDDYSFIENHGGFSAQPPTVLELMADHYSMLKAPGIDELTSVIQYQQSPPSLVG

[Multiple Choices]
A. pantetheine 4'-phosphate
B. FMN
C. cob(II)alamin
D. Fe(2+)
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

> The supplied sequence exactly matches the UniProt sequence annotated with pantetheine 4'-phosphate as a cofactor. The annotation is attributed to a PROSITE-ProRule computational inference, so it supports the key but is not, by itself, experimental confirmation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an NRPS-like adenylation-domain signature, including YTSGSTGKPKGV, and a carrier-protein domain. NRPS carrier domains are activated by attachment of 4'-phosphopantetheine, distinguishing the listed pantetheine option from FMN, cobalamin, and Fe2+.


**Missing item-specific fact**

> No protein-specific fact is essential if the NRPS and carrier-protein features can be recognized from the sequence; the database annotation provides corroboration rather than the only basis for the choice.


**Reason**

> A defensible sequence-to-domain-to-cofactor inference distinguishes the options. Merely identifying the exact protein or recalling its database entry would not suffice, but the relevant NRPS biology supplies a concrete argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are chemically and biologically distinct, and the carrier-protein cofactor inference favors pantetheine 4'-phosphate.


### Important caveats

- The cited cofactor annotation is computational (PROSITE-ProRule), not direct experimental evidence in the supplied excerpts.
- The annotation supports the cofactor assignment; it does not independently establish the precise experimental meaning of 'required for catalytic activity.'

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an NRPS-like adenylation-domain signature, including YTSGSTGKPKGV, and a carrier-protein domain. NRPS carrier domains are activated by attachment of 4'-phosphopantetheine, distinguishing the listed pantetheine option from FMN, cobalamin, and Fe2+.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific fact is essential if the NRPS and carrier-protein features can be recognized from the sequence; the database annotation provides corroboration rather than the only basis for the choice.",
    "reason": "A defensible sequence-to-domain-to-cofactor inference distinguishes the options. Merely identifying the exact protein or recalling its database entry would not suffice, but the relevant NRPS biology supplies a concrete argument."
  },
  "case_id": "cofactor_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated with pantetheine 4'-phosphate as a cofactor. The annotation is attributed to a PROSITE-ProRule computational inference, so it supports the key but is not, by itself, experimental confirmation."
  },
  "important_caveats": [
    "The cited cofactor annotation is computational (PROSITE-ProRule), not direct experimental evidence in the supplied excerpts.",
    "The annotation supports the cofactor assignment; it does not independently establish the precise experimental meaning of 'required for catalytic activity.'"
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are chemically and biologically distinct, and the carrier-protein cofactor inference favors pantetheine 4'-phosphate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated with pantetheine 4'-phosphate as a cofactor. The annotation is attributed to a PROSITE-ProRule computational inference, so it supports the key but is not, by itself, experimental confirmation.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an NRPS-like adenylation-domain signature, including YTSGSTGKPKGV, and a carrier-protein domain. NRPS carrier domains are activated by attachment of 4'-phosphopantetheine, distinguishing the listed pantetheine option from FMN, cobalamin, and Fe2+.",
    "missing_item_specific_fact": "No protein-specific fact is essential if the NRPS and carrier-protein features can be recognized from the sequence; the database annotation provides corroboration rather than the only basis for the choice.",
    "reason": "A defensible sequence-to-domain-to-cofactor inference distinguishes the options. Merely identifying the exact protein or recalling its database entry would not suffice, but the relevant NRPS biology supplies a concrete argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are chemically and biologically distinct, and the carrier-protein cofactor inference favors pantetheine 4'-phosphate."
  },
  "important_caveats": [
    "The cited cofactor annotation is computational (PROSITE-ProRule), not direct experimental evidence in the supplied excerpts.",
    "The annotation supports the cofactor assignment; it does not independently establish the precise experimental meaning of 'required for catalytic activity.'"
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly annotates pantetheine 4'-phosphate as the cofactor (C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule:PRU00258), which is computational rather than experimental. However, this annotation rests on well-established biochemistry: indigoidine synthase is a nonribosomal peptide synthetase (NRPS), and all NRPS enzymes require a 4'-phosphopantetheine prosthetic group covalently attached to the serine of the thiolation (T) domain. The sequence contains the canonical T-domain signature 'ITSGSTGKPKG' (GxxGxxS motif), confirming the T-domain and thus the phosphopantetheine requirement. The expected answer is scientifically correct.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1488-aa sequence displays the hallmark multi-domain architecture of a single-module NRPS: condensation (C), adenylation (A), thiolation (T), and thioesterase (TE) domains. The T-domain signature 'GxxGxxS' (visible as 'ITSGSTGKPKG') is the phosphopantetheine attachment site. NRPS enzymes universally require 4'-phosphopantetheine as a prosthetic group to shuttle activated acyl/aminoacyl intermediates between catalytic domains. This cofactor requirement is a defining, general property of the NRPS enzyme class, not an idiosyncratic fact about this particular protein. FMN, cob(II)alamin, and Fe(2+) are cofactors for flavoproteins, B12-dependent enzymes, and metalloenzymes respectively—none of which match the NRPS domain architecture evident here.


**Missing item-specific fact**

> None critical. Recognizing the NRPS domain architecture from sequence motifs and applying the general rule that NRPS enzymes require phosphopantetheine constitutes valid biological reasoning. The specific identity as 'indigoidine synthase' is not needed to infer the cofactor.


**Reason**

> A model with general knowledge of NRPS biochemistry can identify the T-domain motif in the sequence, recognize the multi-domain NRPS architecture, and deduce that phosphopantetheine is the required cofactor. The distractors (FMN, cob(II)alamin, Fe2+) correspond to entirely different enzyme classes and can be excluded by the absence of flavin-binding, B12-binding, or metal-binding motifs. This is a class-level inference, not a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Pantetheine 4'-phosphate is the defining cofactor of NRPS enzymes. The other three options (FMN, cob(II)alamin, Fe2+) are cofactors for mechanistically unrelated enzyme classes and are inconsistent with the NRPS domain architecture visible in the sequence. No ambiguity exists.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000255 (electronic annotation via PROSITE-ProRule), not direct experimental evidence. However, the underlying biology (NRPS phosphopantetheine requirement) is extensively validated across hundreds of NRPS structures and biochemical studies.
- The sequence was first integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown. The sequence match is confirmed across both current and historical (entry version 107) records.
- Identifying the NRPS architecture from a raw sequence requires domain-level pattern recognition (T-domain GxxGxxS motif, A-domain core motifs, C-domain HHxxxSxxxH pattern). This is achievable with general biochemical training but does require some expertise.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1488-aa sequence displays the hallmark multi-domain architecture of a single-module NRPS: condensation (C), adenylation (A), thiolation (T), and thioesterase (TE) domains. The T-domain signature 'GxxGxxS' (visible as 'ITSGSTGKPKG') is the phosphopantetheine attachment site. NRPS enzymes universally require 4'-phosphopantetheine as a prosthetic group to shuttle activated acyl/aminoacyl intermediates between catalytic domains. This cofactor requirement is a defining, general property of the NRPS enzyme class, not an idiosyncratic fact about this particular protein. FMN, cob(II)alamin, and Fe(2+) are cofactors for flavoproteins, B12-dependent enzymes, and metalloenzymes respectively—none of which match the NRPS domain architecture evident here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the NRPS domain architecture from sequence motifs and applying the general rule that NRPS enzymes require phosphopantetheine constitutes valid biological reasoning. The specific identity as 'indigoidine synthase' is not needed to infer the cofactor.",
    "reason": "A model with general knowledge of NRPS biochemistry can identify the T-domain motif in the sequence, recognize the multi-domain NRPS architecture, and deduce that phosphopantetheine is the required cofactor. The distractors (FMN, cob(II)alamin, Fe2+) correspond to entirely different enzyme classes and can be excluded by the absence of flavin-binding, B12-binding, or metal-binding motifs. This is a class-level inference, not a protein-specific lookup."
  },
  "case_id": "cofactor_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly annotates pantetheine 4'-phosphate as the cofactor (C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule:PRU00258), which is computational rather than experimental. However, this annotation rests on well-established biochemistry: indigoidine synthase is a nonribosomal peptide synthetase (NRPS), and all NRPS enzymes require a 4'-phosphopantetheine prosthetic group covalently attached to the serine of the thiolation (T) domain. The sequence contains the canonical T-domain signature 'ITSGSTGKPKG' (GxxGxxS motif), confirming the T-domain and thus the phosphopantetheine requirement. The expected answer is scientifically correct."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (electronic annotation via PROSITE-ProRule), not direct experimental evidence. However, the underlying biology (NRPS phosphopantetheine requirement) is extensively validated across hundreds of NRPS structures and biochemical studies.",
    "The sequence was first integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown. The sequence match is confirmed across both current and historical (entry version 107) records.",
    "Identifying the NRPS architecture from a raw sequence requires domain-level pattern recognition (T-domain GxxGxxS motif, A-domain core motifs, C-domain HHxxxSxxxH pattern). This is achievable with general biochemical training but does require some expertise."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the defining cofactor of NRPS enzymes. The other three options (FMN, cob(II)alamin, Fe2+) are cofactors for mechanistically unrelated enzyme classes and are inconsistent with the NRPS domain architecture visible in the sequence. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9L391 (Indigoidine synthase, EC 4.3.3.9) explicitly annotates pantetheine 4'-phosphate as the cofactor (C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule:PRU00258), which is computational rather than experimental. However, this annotation rests on well-established biochemistry: indigoidine synthase is a nonribosomal peptide synthetase (NRPS), and all NRPS enzymes require a 4'-phosphopantetheine prosthetic group covalently attached to the serine of the thiolation (T) domain. The sequence contains the canonical T-domain signature 'ITSGSTGKPKG' (GxxGxxS motif), confirming the T-domain and thus the phosphopantetheine requirement. The expected answer is scientifically correct.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1488-aa sequence displays the hallmark multi-domain architecture of a single-module NRPS: condensation (C), adenylation (A), thiolation (T), and thioesterase (TE) domains. The T-domain signature 'GxxGxxS' (visible as 'ITSGSTGKPKG') is the phosphopantetheine attachment site. NRPS enzymes universally require 4'-phosphopantetheine as a prosthetic group to shuttle activated acyl/aminoacyl intermediates between catalytic domains. This cofactor requirement is a defining, general property of the NRPS enzyme class, not an idiosyncratic fact about this particular protein. FMN, cob(II)alamin, and Fe(2+) are cofactors for flavoproteins, B12-dependent enzymes, and metalloenzymes respectively—none of which match the NRPS domain architecture evident here.",
    "missing_item_specific_fact": "None critical. Recognizing the NRPS domain architecture from sequence motifs and applying the general rule that NRPS enzymes require phosphopantetheine constitutes valid biological reasoning. The specific identity as 'indigoidine synthase' is not needed to infer the cofactor.",
    "reason": "A model with general knowledge of NRPS biochemistry can identify the T-domain motif in the sequence, recognize the multi-domain NRPS architecture, and deduce that phosphopantetheine is the required cofactor. The distractors (FMN, cob(II)alamin, Fe2+) correspond to entirely different enzyme classes and can be excluded by the absence of flavin-binding, B12-binding, or metal-binding motifs. This is a class-level inference, not a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the defining cofactor of NRPS enzymes. The other three options (FMN, cob(II)alamin, Fe2+) are cofactors for mechanistically unrelated enzyme classes and are inconsistent with the NRPS domain architecture visible in the sequence. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (electronic annotation via PROSITE-ProRule), not direct experimental evidence. However, the underlying biology (NRPS phosphopantetheine requirement) is extensively validated across hundreds of NRPS structures and biochemical studies.",
    "The sequence was first integrated into Swiss-Prot in February 2025; the author's source snapshot date is unknown. The sequence match is confirmed across both current and historical (entry version 107) records.",
    "Identifying the NRPS architecture from a raw sequence requires domain-level pattern recognition (T-domain GxxGxxS motif, A-domain core motifs, C-domain HHxxxSxxxH pattern). This is achievable with general biochemical training but does require some expertise."
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

**Accession:** `Q9L391` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
"Q9L391"
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 68-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
