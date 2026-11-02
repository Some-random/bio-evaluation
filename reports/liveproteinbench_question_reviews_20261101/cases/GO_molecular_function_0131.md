# GO_molecular_function_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — thioredoxin peroxidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPLQPGDSFPANVVFSYIPPTGSLDLTVCGRPIEYNASEALAKGTSVLVAVPGAFTPTCQEKHVTGFIAKLDQLRQAGVDRVLFIASNDAFVMSAWGKANGIKDESILFLSDSDTAFSSSIGWANAGRTGRYAIVVKDGKVVYAAVDTVRGSTEKSGVDAVLTVLGNQGKL

[Multiple Choices]
A. general transcription initiation factor binding
B. cystathionine gamma-lyase activity
C. thioredoxin peroxidase activity
D. ubiquitin-like protein peptidase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches the archived UniProt entry for Peroxiredoxin AHP1, whose annotation identifies thiol-specific peroxidase activity and a thioredoxin-linked hydroperoxide reaction. The support is primarily annotation transferred by similarity and an InterPro-based GO assignment, not direct experimental validation for this protein.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the conserved peroxiredoxin active-site pattern PxxxTxxC (in the segment PGAFTPTC), supporting a peroxiredoxin-family enzyme. That provides a meaningful sequence-based distinction for thioredoxin peroxidase activity over the unrelated binding, lyase, and ubiquitin-like peptidase choices.


**Missing item-specific fact**

> No protein-specific annotation is required to make the family-level distinction among these options; the exact protein identity and its database annotation were not supplied.


**Reason**

> A recognizable conserved sequence motif and the strongly contrasting choices provide a defensible biological inference, rather than requiring recognition of the exact sequence or lookup of its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence motif supports the peroxiredoxin choice, while the other options describe substantially different molecular functions.


### Important caveats

- The archived entry matches the supplied sequence, but its functional description is qualified as evidence transferred by similarity; the supplied evidence does not establish direct experimental characterization of this exact protein.
- The GO thioredoxin peroxidase annotation is an InterPro-based inference, not itself an experimental measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the conserved peroxiredoxin active-site pattern PxxxTxxC (in the segment PGAFTPTC), supporting a peroxiredoxin-family enzyme. That provides a meaningful sequence-based distinction for thioredoxin peroxidase activity over the unrelated binding, lyase, and ubiquitin-like peptidase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is required to make the family-level distinction among these options; the exact protein identity and its database annotation were not supplied.",
    "reason": "A recognizable conserved sequence motif and the strongly contrasting choices provide a defensible biological inference, rather than requiring recognition of the exact sequence or lookup of its database entry."
  },
  "case_id": "GO_molecular_function_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "H5",
      "C4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt entry for Peroxiredoxin AHP1, whose annotation identifies thiol-specific peroxidase activity and a thioredoxin-linked hydroperoxide reaction. The support is primarily annotation transferred by similarity and an InterPro-based GO assignment, not direct experimental validation for this protein."
  },
  "important_caveats": [
    "The archived entry matches the supplied sequence, but its functional description is qualified as evidence transferred by similarity; the supplied evidence does not establish direct experimental characterization of this exact protein.",
    "The GO thioredoxin peroxidase annotation is an InterPro-based inference, not itself an experimental measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif supports the peroxiredoxin choice, while the other options describe substantially different molecular functions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt entry for Peroxiredoxin AHP1, whose annotation identifies thiol-specific peroxidase activity and a thioredoxin-linked hydroperoxide reaction. The support is primarily annotation transferred by similarity and an InterPro-based GO assignment, not direct experimental validation for this protein.",
    "evidence_ids": ["H1", "H2", "H3", "H5", "C4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the conserved peroxiredoxin active-site pattern PxxxTxxC (in the segment PGAFTPTC), supporting a peroxiredoxin-family enzyme. That provides a meaningful sequence-based distinction for thioredoxin peroxidase activity over the unrelated binding, lyase, and ubiquitin-like peptidase choices.",
    "missing_item_specific_fact": "No protein-specific annotation is required to make the family-level distinction among these options; the exact protein identity and its database annotation were not supplied.",
    "reason": "A recognizable conserved sequence motif and the strongly contrasting choices provide a defensible biological inference, rather than requiring recognition of the exact sequence or lookup of its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif supports the peroxiredoxin choice, while the other options describe substantially different molecular functions."
  },
  "important_caveats": [
    "The archived entry matches the supplied sequence, but its functional description is qualified as evidence transferred by similarity; the supplied evidence does not establish direct experimental characterization of this exact protein.",
    "The GO thioredoxin peroxidase annotation is an InterPro-based inference, not itself an experimental measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G0S1P8 (sequence matched, 172 aa) annotates this protein as Peroxiredoxin AHP1 (EC 1.11.1.24) with GO:0008379 'thioredoxin peroxidase activity' (IEA:InterPro) and GO:0140824 'thioredoxin-dependent peroxiredoxin activity' (ISS:UniProtKB). The catalytic reaction 'a hydroperoxide + &#91;thioredoxin&#93;-dithiol = an alcohol + &#91;thioredoxin&#93;-disulfide + H2O' directly corresponds to GO:0008379. The annotation evidence code is IEA (inferred from InterPro domain match), not direct experimental characterization, but the functional assignment is consistent with the peroxiredoxin family assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark peroxiredoxin catalytic motif: a conserved cysteine in the context 'AFTPTCQEKHVTGF' (~residues 44-56), where the 'TPPTC' pattern with the peroxidatic cysteine is the defining signature of the peroxiredoxin/thioredoxin peroxidase superfamily. The ~172-residue alpha-helical size and the conserved 'SDSD' and 'GKVVYAAVDTVRG' C-terminal features further match the peroxiredoxin fold. The other options are clearly distinguishable: cystathionine gamma-lyase (PLP-dependent, ~400+ aa, different fold), ubiquitin-like protein peptidase (cysteine protease with Cys-His-Asn triad), and general transcription initiation factor binding (protein-protein interaction, no catalytic motif). A trained biochemist can identify the peroxiredoxin catalytic Cys motif and exclude the other enzyme classes.


**Missing item-specific fact**

> None critical. The fine distinction between GO:0008379 (thioredoxin peroxidase, H2O2-specific) and GO:0140824 (thioredoxin-dependent peroxiredoxin, broader) is not resolvable from sequence alone, but the protein preferentially reduces organic peroxides, making the broader term arguably more precise. However, GO:0008379 is the annotated child term and is the only peroxiredoxin-related option offered.


**Reason**

> The peroxiredoxin catalytic cysteine motif is a well-known, textbook-level biochemical feature. Recognizing it from the sequence and excluding PLP-lyase, cysteine-protease, and transcription-factor-binding alternatives constitutes general biological reasoning rather than lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C corresponds to a peroxiredoxin/thioredoxin peroxidase. The other three options represent entirely different enzyme classes (PLP-dependent lyase, cysteine protease, protein-binding) with incompatible sequence signatures. No ambiguity among the offered choices.


### Important caveats

- The GO:0008379 annotation is IEA:InterPro (inferred from domain match), not direct experimental evidence for this specific protein. The EC assignment (1.11.1.24) is transferred by similarity (ECO:0000250 from P38013, S. cerevisiae AHP1).
- The protein 'preferentially eliminates organic peroxides rather than hydrogen peroxide' (per UniProt FUNCTION comment), which is more consistent with the parent term GO:0140824 than the H2O2-specific child GO:0008379. However, GO:0008379 is the annotated term and the only peroxiredoxin option offered.
- The UniProt entry was first public on 2025-02-05, after the approximate benchmark construction period; the author's source snapshot is unknown. The historical archived record (v54) confirms the same annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark peroxiredoxin catalytic motif: a conserved cysteine in the context 'AFTPTCQEKHVTGF' (~residues 44-56), where the 'TPPTC' pattern with the peroxidatic cysteine is the defining signature of the peroxiredoxin/thioredoxin peroxidase superfamily. The ~172-residue alpha-helical size and the conserved 'SDSD' and 'GKVVYAAVDTVRG' C-terminal features further match the peroxiredoxin fold. The other options are clearly distinguishable: cystathionine gamma-lyase (PLP-dependent, ~400+ aa, different fold), ubiquitin-like protein peptidase (cysteine protease with Cys-His-Asn triad), and general transcription initiation factor binding (protein-protein interaction, no catalytic motif). A trained biochemist can identify the peroxiredoxin catalytic Cys motif and exclude the other enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The fine distinction between GO:0008379 (thioredoxin peroxidase, H2O2-specific) and GO:0140824 (thioredoxin-dependent peroxiredoxin, broader) is not resolvable from sequence alone, but the protein preferentially reduces organic peroxides, making the broader term arguably more precise. However, GO:0008379 is the annotated child term and is the only peroxiredoxin-related option offered.",
    "reason": "The peroxiredoxin catalytic cysteine motif is a well-known, textbook-level biochemical feature. Recognizing it from the sequence and excluding PLP-lyase, cysteine-protease, and transcription-factor-binding alternatives constitutes general biological reasoning rather than lookup of a specific database entry."
  },
  "case_id": "GO_molecular_function_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H3",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G0S1P8 (sequence matched, 172 aa) annotates this protein as Peroxiredoxin AHP1 (EC 1.11.1.24) with GO:0008379 'thioredoxin peroxidase activity' (IEA:InterPro) and GO:0140824 'thioredoxin-dependent peroxiredoxin activity' (ISS:UniProtKB). The catalytic reaction 'a hydroperoxide + [thioredoxin]-dithiol = an alcohol + [thioredoxin]-disulfide + H2O' directly corresponds to GO:0008379. The annotation evidence code is IEA (inferred from InterPro domain match), not direct experimental characterization, but the functional assignment is consistent with the peroxiredoxin family assignment."
  },
  "important_caveats": [
    "The GO:0008379 annotation is IEA:InterPro (inferred from domain match), not direct experimental evidence for this specific protein. The EC assignment (1.11.1.24) is transferred by similarity (ECO:0000250 from P38013, S. cerevisiae AHP1).",
    "The protein 'preferentially eliminates organic peroxides rather than hydrogen peroxide' (per UniProt FUNCTION comment), which is more consistent with the parent term GO:0140824 than the H2O2-specific child GO:0008379. However, GO:0008379 is the annotated term and the only peroxiredoxin option offered.",
    "The UniProt entry was first public on 2025-02-05, after the approximate benchmark construction period; the author's source snapshot is unknown. The historical archived record (v54) confirms the same annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C corresponds to a peroxiredoxin/thioredoxin peroxidase. The other three options represent entirely different enzyme classes (PLP-dependent lyase, cysteine protease, protein-binding) with incompatible sequence signatures. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G0S1P8 (sequence matched, 172 aa) annotates this protein as Peroxiredoxin AHP1 (EC 1.11.1.24) with GO:0008379 'thioredoxin peroxidase activity' (IEA:InterPro) and GO:0140824 'thioredoxin-dependent peroxiredoxin activity' (ISS:UniProtKB). The catalytic reaction 'a hydroperoxide + [thioredoxin]-dithiol = an alcohol + [thioredoxin]-disulfide + H2O' directly corresponds to GO:0008379. The annotation evidence code is IEA (inferred from InterPro domain match), not direct experimental characterization, but the functional assignment is consistent with the peroxiredoxin family assignment.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H3", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark peroxiredoxin catalytic motif: a conserved cysteine in the context 'AFTPTCQEKHVTGF' (~residues 44-56), where the 'TPPTC' pattern with the peroxidatic cysteine is the defining signature of the peroxiredoxin/thioredoxin peroxidase superfamily. The ~172-residue alpha-helical size and the conserved 'SDSD' and 'GKVVYAAVDTVRG' C-terminal features further match the peroxiredoxin fold. The other options are clearly distinguishable: cystathionine gamma-lyase (PLP-dependent, ~400+ aa, different fold), ubiquitin-like protein peptidase (cysteine protease with Cys-His-Asn triad), and general transcription initiation factor binding (protein-protein interaction, no catalytic motif). A trained biochemist can identify the peroxiredoxin catalytic Cys motif and exclude the other enzyme classes.",
    "missing_item_specific_fact": "None critical. The fine distinction between GO:0008379 (thioredoxin peroxidase, H2O2-specific) and GO:0140824 (thioredoxin-dependent peroxiredoxin, broader) is not resolvable from sequence alone, but the protein preferentially reduces organic peroxides, making the broader term arguably more precise. However, GO:0008379 is the annotated child term and is the only peroxiredoxin-related option offered.",
    "reason": "The peroxiredoxin catalytic cysteine motif is a well-known, textbook-level biochemical feature. Recognizing it from the sequence and excluding PLP-lyase, cysteine-protease, and transcription-factor-binding alternatives constitutes general biological reasoning rather than lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C corresponds to a peroxiredoxin/thioredoxin peroxidase. The other three options represent entirely different enzyme classes (PLP-dependent lyase, cysteine protease, protein-binding) with incompatible sequence signatures. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The GO:0008379 annotation is IEA:InterPro (inferred from domain match), not direct experimental evidence for this specific protein. The EC assignment (1.11.1.24) is transferred by similarity (ECO:0000250 from P38013, S. cerevisiae AHP1).",
    "The protein 'preferentially eliminates organic peroxides rather than hydrogen peroxide' (per UniProt FUNCTION comment), which is more consistent with the parent term GO:0140824 than the H2O2-specific child GO:0008379. However, GO:0008379 is the annotated term and the only peroxiredoxin option offered.",
    "The UniProt entry was first public on 2025-02-05, after the approximate benchmark construction period; the author's source snapshot is unknown. The historical archived record (v54) confirms the same annotations."
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

**Accession:** `G0S1P8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:23.003674+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Alkyl hydroperoxide reductase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P38013","source":"UniProtKB"}],"value":"1.11.1.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Peroxiredoxin AHP1"},"shortNames":[{"value":"Prx"}]}}
```

Source SHA-256: `ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:23.003674+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P38013","source":"UniProtKB"}],"value":"Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. Preferentially eliminates organic peroxides rather than hydrogen peroxide. Relays alkyl hydroperoxides as a signal to the transcription factor CAD1/YAP2 by inducing the formation of intramolecular disulfide bonds in CAD1, which causes its nuclear accumulation and activation. Involved in cellular Mn(2+) homeostasis"}]}
```

Source SHA-256: `ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:23.003674+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.11.1.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P38013","source":"UniProtKB"}],"name":"a hydroperoxide + [thioredoxin]-dithiol = an alcohol + [thioredoxin]-disulfide + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:62620"},{"database":"Rhea","id":"RHEA-COMP:10698"},{"database":"Rhea","id":"RHEA-COMP:10700"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29950"},{"database":"ChEBI","id":"CHEBI:30879"},{"database":"ChEBI","id":"CHEBI:35924"},{"database":"ChEBI","id":"CHEBI:50058"}]}}
```

Source SHA-256: `ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:23.003674+00:00.  

```json
{"database":"GO","id":"GO:0008379","properties":[{"key":"GoTerm","value":"F:thioredoxin peroxidase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0S1P8.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:23.003674+00:00.  

```json
{"database":"GO","id":"GO:0140824","properties":[{"key":"GoTerm","value":"F:thioredoxin-dependent peroxiredoxin activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `ac59354270103a00640e3456b661297eaa89577d53f69bd751d7eb36a829cb5f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:28.092103+00:00.  

```text
ID   AHP1_CHATD              Reviewed;         172 AA.
AC   G0S1P8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   28-JAN-2026, entry version 54.
DE   RecName: Full=Peroxiredoxin AHP1 {ECO:0000305};
DE            Short=Prx;
DE            EC=1.11.1.24 {ECO:0000250|UniProtKB:P38013};
DE   AltName: Full=Alkyl hydroperoxide reductase;
GN   Name=AHP1; ORFNames=CTHT_0014370;
OS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)
OS   (Thermochaetoides thermophila).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.
OX   NCBI_TaxID=759272;
```

Source SHA-256: `ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:28.092103+00:00.  

```text
CC   -!- FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of
CC       hydrogen peroxide and organic hydroperoxides to water and alcohols,
CC       respectively. Plays a role in cell protection against oxidative stress
CC       by detoxifying peroxides and as sensor of hydrogen peroxide-mediated
CC       signaling events. Preferentially eliminates organic peroxides rather
CC       than hydrogen peroxide. Relays alkyl hydroperoxides as a signal to the
CC       transcription factor CAD1/YAP2 by inducing the formation of
CC       intramolecular disulfide bonds in CAD1, which causes its nuclear
CC       accumulation and activation. Involved in cellular Mn(2+) homeostasis.
CC       {ECO:0000250|UniProtKB:P38013}.
```

Source SHA-256: `ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:28.092103+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a hydroperoxide + [thioredoxin]-dithiol = an alcohol +
CC         [thioredoxin]-disulfide + H2O; Xref=Rhea:RHEA:62620, Rhea:RHEA-
CC         COMP:10698, Rhea:RHEA-COMP:10700, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29950, ChEBI:CHEBI:30879, ChEBI:CHEBI:35924,
CC         ChEBI:CHEBI:50058; EC=1.11.1.24;
CC         Evidence={ECO:0000250|UniProtKB:P38013};
```

Source SHA-256: `ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0S1P8?format=txt&versions=54)  
**Locator:** `lines 111-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:28.092103+00:00.  

```text
DR   GO; GO:0008379; F:thioredoxin peroxidase activity; IEA:InterPro.
```

Source SHA-256: `ad6b8e635a2d1310f20d35c06db92e8909dc4cbae80b5fef229cdcd3da0ecf4f`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 82543-82560`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008379
name: thioredoxin peroxidase activity
namespace: molecular_function
alt_id: GO:0009031
def: "Catalysis of the reaction: [thioredoxin]-dithiol + H2O2 = [thioredoxin]-disulfide + H2O." [RHEA:63528]
synonym: "thiol peroxidase activity" EXACT []
synonym: "TPx activity" EXACT []
synonym: "TrxPx activity" EXACT []
xref: MetaCyc:RXN0-267
xref: Reactome:R-HSA-3322995 "PRDX3,5 catalyze TXN2 reduced + H2O2 => TXN2 oxidized + 2H2O"
xref: Reactome:R-HSA-3341343 "PRDX1,2,5 catalyze TXN reduced + H2O2 => TXN oxidized + 2H2O"
xref: Reactome:R-HSA-3697882 "PRDX5 reduces peroxynitrite to nitrite using TXN"
xref: Reactome:R-HSA-3697894 "PRDX5 reduces peroxynitrite to nitrite using TXN2"
xref: RHEA:63528
is_a: GO:0140824 ! thioredoxin-dependent peroxiredoxin activity
property_value: skos:exactMatch RHEA:63528

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
