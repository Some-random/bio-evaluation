# GO_molecular_function_0032

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — nutrient reservoir activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFIPSHQVWLVGLLAFSLVGAEYYDTKTADKDFLLKQKKVYNLLYRVAQPALANITWYNEGQAWNIEANIDSYTNAAAVKEFLSIYKHGMLPRGELFSLYYPQLLREMSALFKLFYHAKDFDIFFKTALWAKNNINEAQYIYSLYTAVITRPDTKFIQLPPLYEMCPYFFFNSEVLQKANHALIFGKLDTKTSGKYKEYIIPANYSGWYLNHDYNLENKLIYFIEDIGLNTYYFFLRQAFPFWLPSKEYDLPDYRGEEYLYSHKLLLNRYYLERLSNDLPHLEEFDWQKPFYPGYYPTMTYSNGLPFPQRPIWSNFPIYKYKYIREIMNKESRISAAIDSGYILNNDGKWHNIYSEKGLNILGNIIEGNADSYNTEFYGSIDTLARKILGYNLEAASKYQIVPSALEIFSTSMKDPAFYRIYKRIIDYYHSYKMHQKPYNKDEIIYPNLKIESFTVDKLITYFEQFDTTINNGLLLEEQRNDDKPFLIKIRQYRLNHKPFNFHITINADKPMKAAIRIFIGPKYDSHHKLIEIPEDLKYFYEIDNWMLDLNSGLNKITRNSLDCFFTMNDLEPSEIFYEKIETSLNSDKPFTYNERIFGFPGRLLLPRGKKEGMPFQLFLYVSPVSSEYNQYNSRIWGGYKFDKRSFGFPLDKPLYDFNYEGPNMLFKDILIYHKDEFDMNITY

[Multiple Choices]
A. heparan sulfate 2-sulfotransferase activity
B. kinesin binding
C. nutrient reservoir activity
D. ATPase inhibitor activity
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

> The sequence matches the honeybee Hexamerin 70a protein. Its annotation describes a storage protein that may supply nutrients, and the matched UniProt record assigns nutrient reservoir activity with IDA evidence. The function is supported, though the broader function description is qualified as probable.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted precursor, but that alone does not establish nutrient storage rather than the other listed functions.


**Missing item-specific fact**

> Identifying this sequence as honeybee Hexamerin 70a, a storage protein with nutrient reservoir activity, is needed to confidently select C.


**Reason**

> The reviewer-only annotation supports the key, but the model input supplies only the sequence and choices. The protein-specific identity and functional evidence are absent; recognizing or recalling them would be lookup or memorization, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched protein annotation, nutrient reservoir activity is the only listed option supported by the evidence.


### Important caveats

- The GO annotation is reported as IDA, while the function description characterizes nutrient-supply activity as probable.
- The author’s exact source snapshot is unknown, although the sequence matches the historical and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted precursor, but that alone does not establish nutrient storage rather than the other listed functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as honeybee Hexamerin 70a, a storage protein with nutrient reservoir activity, is needed to confidently select C.",
    "reason": "The reviewer-only annotation supports the key, but the model input supplies only the sequence and choices. The protein-specific identity and functional evidence are absent; recognizing or recalling them would be lookup or memorization, not sequence-based reasoning."
  },
  "case_id": "GO_molecular_function_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the honeybee Hexamerin 70a protein. Its annotation describes a storage protein that may supply nutrients, and the matched UniProt record assigns nutrient reservoir activity with IDA evidence. The function is supported, though the broader function description is qualified as probable."
  },
  "important_caveats": [
    "The GO annotation is reported as IDA, while the function description characterizes nutrient-supply activity as probable.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched protein annotation, nutrient reservoir activity is the only listed option supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the honeybee Hexamerin 70a protein. Its annotation describes a storage protein that may supply nutrients, and the matched UniProt record assigns nutrient reservoir activity with IDA evidence. The function is supported, though the broader function description is qualified as probable.",
    "evidence_ids": ["C5", "C6", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted precursor, but that alone does not establish nutrient storage rather than the other listed functions.",
    "missing_item_specific_fact": "Identifying this sequence as honeybee Hexamerin 70a, a storage protein with nutrient reservoir activity, is needed to confidently select C.",
    "reason": "The reviewer-only annotation supports the key, but the model input supplies only the sequence and choices. The protein-specific identity and functional evidence are absent; recognizing or recalling them would be lookup or memorization, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched protein annotation, nutrient reservoir activity is the only listed option supported by the evidence."
  },
  "important_caveats": [
    "The GO annotation is reported as IDA, while the function description characterizes nutrient-supply activity as probable.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProtKB A0A8U0WQF3 (HEX7A_APIME), identified as Hexamerin 70a / Arylphorin Hex70a from Apis mellifera. The UniProt FUNCTION comment explicitly describes it as a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned with IDA:UniProtKB evidence, supported by multiple experimental publications (PMIDs 22205988, 36630080, 18472106). GO:0045735 is defined as 'Functions in the storage of nutritious substrates' with synonym 'storage protein,' directly matching the protein's characterized role as an arylphorin hexamerin storage protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO4](#evidence-go4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits several features that collectively point toward a storage/reservoir function: (1) an N-terminal hydrophobic signal peptide (MFIPSHQVWLVGLLAFSLVGAE...) indicating a secreted protein; (2) a large size (~70 kDa, 684 residues) consistent with hexamerin storage proteins; (3) notable enrichment of aromatic amino acids (Tyr, Phe, Trp) distributed throughout the sequence, characteristic of arylphorins that serve as aromatic amino acid reservoirs; (4) absence of recognizable catalytic motifs (no PAPS-binding or sulfotransferase domains for option A; no Walker A/B or P-loop for ATPase-related functions in D); (5) absence of specific binding motifs for kinesin motor proteins (option B). A large secreted protein rich in aromatic residues lacking enzymatic or specific-binding domains is most consistent with a nutrient storage/reservoir role.


**Missing item-specific fact**

> None strictly required, though recognizing the hexamerin family fold and the specific arylphorin subfamily would strengthen the identification. The aromatic amino acid enrichment and absence of catalytic domains are observable sequence features that support the reasoning.


**Reason**

> The sequence provides concrete, observable features (signal peptide, large size, aromatic amino acid enrichment, absence of catalytic/binding domains) that allow a knowledgeable biologist to reason toward a storage/reservoir function and away from enzymatic (A, D) or specific-binding (B) functions. While recognizing the hexamerin family specifically would benefit from database knowledge, the general biological argument from sequence features is meaningful and distinguishing.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct molecular function categories (enzymatic catalysis, motor protein binding, storage/reservoir, inhibitor activity). The sequence features—aromatic-rich large secreted protein without catalytic or specific-binding motifs—meaningfully favor C over A, B, and D. No other option is defensible given the observable sequence characteristics.


### Important caveats

- The GO annotation uses IDA:UniProtKB (curator-assigned from experimental literature), not a purely computational prediction.
- The protein also has a secondary role as a nuclear protein involved in gene expression regulation (PMIDs 22205988, 36630080), but nutrient reservoir is the primary molecular function.
- The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown.
- The aromatic amino acid enrichment is a qualitative observation from the linear sequence; rigorous statistical enrichment analysis was not performed here.
- The reviewer-only evidence establishes the key is correct but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits several features that collectively point toward a storage/reservoir function: (1) an N-terminal hydrophobic signal peptide (MFIPSHQVWLVGLLAFSLVGAE...) indicating a secreted protein; (2) a large size (~70 kDa, 684 residues) consistent with hexamerin storage proteins; (3) notable enrichment of aromatic amino acids (Tyr, Phe, Trp) distributed throughout the sequence, characteristic of arylphorins that serve as aromatic amino acid reservoirs; (4) absence of recognizable catalytic motifs (no PAPS-binding or sulfotransferase domains for option A; no Walker A/B or P-loop for ATPase-related functions in D); (5) absence of specific binding motifs for kinesin motor proteins (option B). A large secreted protein rich in aromatic residues lacking enzymatic or specific-binding domains is most consistent with a nutrient storage/reservoir role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required, though recognizing the hexamerin family fold and the specific arylphorin subfamily would strengthen the identification. The aromatic amino acid enrichment and absence of catalytic domains are observable sequence features that support the reasoning.",
    "reason": "The sequence provides concrete, observable features (signal peptide, large size, aromatic amino acid enrichment, absence of catalytic/binding domains) that allow a knowledgeable biologist to reason toward a storage/reservoir function and away from enzymatic (A, D) or specific-binding (B) functions. While recognizing the hexamerin family specifically would benefit from database knowledge, the general biological argument from sequence features is meaningful and distinguishing."
  },
  "case_id": "GO_molecular_function_0032",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "GO4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProtKB A0A8U0WQF3 (HEX7A_APIME), identified as Hexamerin 70a / Arylphorin Hex70a from Apis mellifera. The UniProt FUNCTION comment explicitly describes it as a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned with IDA:UniProtKB evidence, supported by multiple experimental publications (PMIDs 22205988, 36630080, 18472106). GO:0045735 is defined as 'Functions in the storage of nutritious substrates' with synonym 'storage protein,' directly matching the protein's characterized role as an arylphorin hexamerin storage protein."
  },
  "important_caveats": [
    "The GO annotation uses IDA:UniProtKB (curator-assigned from experimental literature), not a purely computational prediction.",
    "The protein also has a secondary role as a nuclear protein involved in gene expression regulation (PMIDs 22205988, 36630080), but nutrient reservoir is the primary molecular function.",
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown.",
    "The aromatic amino acid enrichment is a qualitative observation from the linear sequence; rigorous statistical enrichment analysis was not performed here.",
    "The reviewer-only evidence establishes the key is correct but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct molecular function categories (enzymatic catalysis, motor protein binding, storage/reservoir, inhibitor activity). The sequence features—aromatic-rich large secreted protein without catalytic or specific-binding motifs—meaningfully favor C over A, B, and D. No other option is defensible given the observable sequence characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0032",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProtKB A0A8U0WQF3 (HEX7A_APIME), identified as Hexamerin 70a / Arylphorin Hex70a from Apis mellifera. The UniProt FUNCTION comment explicitly describes it as a 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO annotation GO:0045735 (nutrient reservoir activity) is assigned with IDA:UniProtKB evidence, supported by multiple experimental publications (PMIDs 22205988, 36630080, 18472106). GO:0045735 is defined as 'Functions in the storage of nutritious substrates' with synonym 'storage protein,' directly matching the protein's characterized role as an arylphorin hexamerin storage protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "GO4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits several features that collectively point toward a storage/reservoir function: (1) an N-terminal hydrophobic signal peptide (MFIPSHQVWLVGLLAFSLVGAE...) indicating a secreted protein; (2) a large size (~70 kDa, 684 residues) consistent with hexamerin storage proteins; (3) notable enrichment of aromatic amino acids (Tyr, Phe, Trp) distributed throughout the sequence, characteristic of arylphorins that serve as aromatic amino acid reservoirs; (4) absence of recognizable catalytic motifs (no PAPS-binding or sulfotransferase domains for option A; no Walker A/B or P-loop for ATPase-related functions in D); (5) absence of specific binding motifs for kinesin motor proteins (option B). A large secreted protein rich in aromatic residues lacking enzymatic or specific-binding domains is most consistent with a nutrient storage/reservoir role.",
    "missing_item_specific_fact": "None strictly required, though recognizing the hexamerin family fold and the specific arylphorin subfamily would strengthen the identification. The aromatic amino acid enrichment and absence of catalytic domains are observable sequence features that support the reasoning.",
    "reason": "The sequence provides concrete, observable features (signal peptide, large size, aromatic amino acid enrichment, absence of catalytic/binding domains) that allow a knowledgeable biologist to reason toward a storage/reservoir function and away from enzymatic (A, D) or specific-binding (B) functions. While recognizing the hexamerin family specifically would benefit from database knowledge, the general biological argument from sequence features is meaningful and distinguishing."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct molecular function categories (enzymatic catalysis, motor protein binding, storage/reservoir, inhibitor activity). The sequence features—aromatic-rich large secreted protein without catalytic or specific-binding motifs—meaningfully favor C over A, B, and D. No other option is defensible given the observable sequence characteristics."
  },
  "important_caveats": [
    "The GO annotation uses IDA:UniProtKB (curator-assigned from experimental literature), not a purely computational prediction.",
    "The protein also has a secondary role as a nuclear protein involved in gene expression regulation (PMIDs 22205988, 36630080), but nutrient reservoir is the primary molecular function.",
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown.",
    "The aromatic amino acid enrichment is a qualitative observation from the linear sequence; rigorous statistical enrichment analysis was not performed here.",
    "The reviewer-only evidence establishes the key is correct but was not available to the evaluated model."
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

**Accession:** `A0A8U0WQF3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U0WQF3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:03.159081+00:00.  

```json
"A0A8U0WQF3"
```

Source SHA-256: `422e0c6dc403f531b564cfcb3c9c7eac0aba6f5f03104492b00758a6a2cc5405`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U0WQF3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:03.159081+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18472106","source":"PubMed"}],"value":"Arylphorin Hex70a"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9692239","source":"PubMed"}],"value":"Hexamerin 70a"}}}
```

Source SHA-256: `422e0c6dc403f531b564cfcb3c9c7eac0aba6f5f03104492b00758a6a2cc5405`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U0WQF3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:03.159081+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22205988","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36630080","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"18472106","source":"PubMed"}],"value":"Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause (Probable). Arylphorin that may be a source of aromatic amino acids during cuticle formation (PubMed:22205988, PubMed:36630080). May have a secondary role as a nuclear protein involved in regulation of gene expression (PubMed:22205988, PubMed:36630080). Involved in gonad cell proliferation (PubMed:22205988)"}]}
```

Source SHA-256: `422e0c6dc403f531b564cfcb3c9c7eac0aba6f5f03104492b00758a6a2cc5405`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U0WQF3.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:03.159081+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22205988","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"36630080","source":"PubMed"}],"id":"GO:0045735","properties":[{"key":"GoTerm","value":"F:nutrient reservoir activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `422e0c6dc403f531b564cfcb3c9c7eac0aba6f5f03104492b00758a6a2cc5405`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U0WQF3?format=txt&versions=13)  
**Locator:** `lines 78-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:08.185910+00:00.  

```text
CC   -!- FUNCTION: Storage protein produced during nutritional abundance, which
CC       may function as a nutrient supply to compensate for lack of dietary
CC       proteins during metamorphosis, egg production and diapause (Probable).
CC       Arylphorin that may be a source of aromatic amino acids during cuticle
CC       formation (PubMed:22205988, PubMed:36630080). May have a secondary role
CC       as a nuclear protein involved in regulation of gene expression
CC       (PubMed:22205988, PubMed:36630080). Involved in gonad cell
CC       proliferation (PubMed:22205988). {ECO:0000269|PubMed:22205988,
CC       ECO:0000269|PubMed:36630080, ECO:0000305|PubMed:18472106}.
```

Source SHA-256: `144c08f3491cc7cc86367c1ae7e7411550590bc196efb564975e976cd66c9ce7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U0WQF3?format=txt&versions=13)  
**Locator:** `lines 182-182`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:08.185910+00:00.  

```text
DR   GO; GO:0045735; F:nutrient reservoir activity; IDA:UniProtKB.
```

Source SHA-256: `144c08f3491cc7cc86367c1ae7e7411550590bc196efb564975e976cd66c9ce7`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 268007-268020`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045735
name: nutrient reservoir activity
namespace: molecular_function
def: "Functions in the storage of nutritious substrates." [GOC:ai]
comment: Note that this term can be used in place of the obsolete terms 'storage protein ; GO:0005187' and 'storage protein of fat body (sensu Insecta) ; GO:0008041'.
subset: goslim_generic
subset: goslim_pir
subset: goslim_prokaryote
synonym: "storage protein" RELATED []
synonym: "storage protein of fat body" RELATED []
synonym: "yolk protein" RELATED []
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 32. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
