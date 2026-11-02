# GO_molecular_function_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — endopeptidase inhibitor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRLLWGLAWVFSFCASSLQKPRLLLFSPSVVNLGTPLSVGVQLLDAPPGQEVKGSVFLRNPKGGSCSPKKDFKLSSGDDFVLLSLEVPLEDVRSCGLFDLRRAPYIQLVAQSPWLRNTAFKATETQGVNLLYSSRRGHIFVQTDQPIYNPGQRVRYRVFALDQKMRPSTDFLTITVENSHGLRVLKKEIFTSTSILQDTFTIPDISEPGTWKISARFSDGLESNRSTHFEVKKYVLPNFEVKITPWKPYILMVPSNSDEIQLDIQARYIYGKPVQGVAYTRFALMDEQGKRTFLRGLETQAKLVEGRTHISISKDQFQAALDKINIGVRDLEGLRLYAATAVIESPGGEMEEAELTSWRFVSSAFSLDLSRTKRHLVPGAHFLLQALVREISGSEASNVIVKVSPTLVSGSDSQVLNVQQSTNRIGQVSISFPIPPTVTGLRLLVSAGSLYPMIARLTVQSPPSRGTGFLSIEPLDPRSPRVGDTFILNLQAVGIPAPTFSHYYYMIISRGQIMAMSREARRTVTSVSVLVDHQLAPSFYFVAYFYHQGHPVANSLLINIQPRDCEGKLQLKVVGAKEYHNGDMMKLRIQTDSKALVALGAVDTALYAVGGWSHKPLDMSKVFEVINSYNVGCGPGGGDDAPQVFQDAGLAFSDGDRLTQTREDLSCPKEKKSRQKRNVNFLKALSEKLGQYSSPDAKRCCQDGMTKLPMKRTCEQRAARVPQQACREPFLSCCKFAEDLRRNQTRSQAPLARKVRDMVNLIEEDDILVRTSFPENWLWRVEPVDSSKLLTVRLPDSMTTWEIHGVSLSKSKGLCVAKPTRVRVFRKFHLHLRLPISVRRFEQLELRPVLYNYLNDDKNVSVHVTPVEGLCMAGGGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKGTLDSSDSVSKILQIEKEGAIHREEIVYNLDPLNNLGQMLEIPGSSDPNIVPEGDFSTFVKVTASEPLETLGSEEALSPGGVASLLRLPGCAEQTMIYLAPTLTASNYLDRTKQWSKLSPETKDHAVHLIQKGHVRIQQFRKKDGSFGAWLHRDSSTWLTAFVLKILSLAQEQVGNSPEKLQETASWLLAQQLGDGSFHDPCPVIHRAMQGGLVGSNETVALTAFVVIALHHGLNVFREGHAKQLKNRVEASITKANSFLGQKASAGLLGAHAAAITAYALTLTKASEDLRNVAHNSLMAMAEETGENLYWGLVLGSQDKVVLRPADPRSPTEPVPQAPALWIETTAYALLHLLLREGKGKMADKAASWLTHQGNFHGAFRSTQDTVVTLDALSAYWIASHTTEEKALKVTLSSMGRNGLKTHVLHLNNHQVKGLEEELKFSLGSTISVKVEGNSKGTLKILRTYNVLDMKNTTCQDLQIEVKVTDAVEYAWSAYEDYEDDYNMPATDDPSVPLQPVTPLQLFEGRRSRRRREAPKVAEERESRVHYTVCIWRNGKLGLSGMAIADITLLSGFHALRADLEKLTSLSDRYVSHFETDGPHVLLYFDSVPTTRECVGFGASQEVVVGLVQPASAVLYDYYSPDHKCSVFYAAPTKSQLLATLCSGDVCQCAEGKCPRLLRSLERRVEDKDGYRMRFACYYHQVEYGFTVKVLREDGRAAFRFFESKITQVLHFRTDTMASIGQTRNFLSRTSCRLRLEPNKEYLIMGMDGETSDNKGDPQYLLDSNTWIEEMPSEQMCKSTRHRAACFQLKDFLMEFSSRGCQV

[Multiple Choices]
A. endopeptidase inhibitor activity
B. translation elongation factor activity
C. RNA binding
D. GTPase activity
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

> The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.

Citations as saved: [C1](#evidence-c1), [C12](#evidence-c12), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.


**Missing item-specific fact**

> The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.


**Reason**

> Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function.


### Important caveats

- The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.
- The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.
- UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.",
    "reason": "Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C12",
      "H9",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation."
  },
  "important_caveats": [
    "The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.",
    "UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.",
    "evidence_ids": ["C1", "C12", "H9", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.",
    "missing_item_specific_fact": "The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.",
    "reason": "Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function."
  },
  "important_caveats": [
    "The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.",
    "The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.",
    "UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options.

Citations as saved: [C12](#evidence-c12), [H9](#evidence-h9), [GO4](#evidence-go4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.


**Missing item-specific fact**

> None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.


**Reason**

> A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices.


### Important caveats

- The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.
- If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.
- The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.",
    "reason": "A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup."
  },
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C12",
      "H9",
      "GO4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.",
    "If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.",
    "The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAQ4VMX2 (Complement C4-A, Mus musculus) carries GO:0004866 (endopeptidase inhibitor activity) annotated with evidence code IEA:InterPro (C12/H9). While this is a computational inference from InterPro domain matching rather than direct experimental evidence, it is a valid database annotation for this exact sequence. The protein's thioester-containing domain region shares structural homology with protease inhibitors (the GO term even lists 'alpha-2 macroglobulin' as a RELATED synonym, GO4). Among the four options, B (translation elongation factor), C (RNA binding), and D (GTPase activity) are entirely inconsistent with a 1734-aa secreted complement protein. The annotation, though IEA-level, supports A as the correct choice among the given options.",
    "evidence_ids": ["C12", "H9", "GO4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (MRLLWGLAWVFSFCASSL), a total length of 1734 residues, and a thioester motif (CGPGGG / GGMMAQWVIVPAGSALPVAFSVVPTASTNVPLKLVAKG), identifying it as a large secreted complement component. These features are incompatible with translation elongation factors (~400-500 aa, cytoplasmic, GTP-binding; B), RNA-binding proteins (which require RRM/KH/Zn-finger motifs absent here; C), and GTPases (which require canonical G1-G5 motifs and are typically 20-50 kDa; D). By elimination of these three clearly mismatched protein classes, A remains the only viable option. The positive assignment of 'endopeptidase inhibitor' to a complement component relies on the structural homology between the thioester/alpha-2 macroglobulin-like domain and serine protease inhibitors, which a knowledgeable model could infer from the CGPGGG-containing region.",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general protein-class knowledge (size, localization signal, absence of diagnostic motifs). Positive identification of A as 'endopeptidase inhibitor' rather than 'complement binding' requires awareness of the protease-inhibitor structural fold within the thioester domain, but this is not needed when the other three options are clearly excluded.",
    "reason": "A model can eliminate B (wrong size, signal peptide present, no translation-factor motifs), C (no RNA-binding domains, secreted protein), and D (no GTPase motifs, far too large) using general biological reasoning about protein classes. The remaining option A is then selected. This constitutes meaningful reasoning, not mere lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 1734-aa secreted complement protein bearing a thioester motif. Only A is consistent with any annotated molecular function of this protein. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The GO:0004866 annotation is IEA:InterPro (computational), not experimentally verified. The protein's primary biological role is complement pathway participation (opsonization, convertase assembly), not protease inhibition per se.",
    "If options like 'complement binding' (GO:0001848) or 'antigen binding' (GO:0003823) had been included, they would arguably be more representative of the protein's primary molecular function. The question's option set constrains the answer to A by elimination.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt), so annotations apply directly to the supplied sequence.",
    "The entry was first publicly released 2025-06-18; the historical entry version 6 was released 2026-01-28. The author's source snapshot date is unknown but the sequence is unchanged."
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

**Accession:** `A0AAQ4VMX2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 6. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.030340+00:00.  

```json
"A0AAQ4VMX2"
```

Source SHA-256: `ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.030340+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"6208559","source":"PubMed"}],"value":"Sex-limited protein"}}],"contains":[{"recommendedName":{"fullName":{"value":"Complement C4 beta chain"}}},{"recommendedName":{"fullName":{"value":"Complement C4-A alpha chain"}}},{"recommendedName":{"fullName":{"value":"C4a anaphylatoxin"}}},{"recommendedName":{"fullName":{"value":"Complement C4b-A"}}},{"recommendedName":{"fullName":{"value":"Complement C4 gamma chain"}}}],"flag":"Precursor","recommendedName":{"fullName":{"value":"Complement C4-A"}}}
```

Source SHA-256: `ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.030340+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32769120","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"8133084","source":"PubMed"}],"value":"Precursor of non-enzymatic components of the classical, lectin and GZMK complement pathways, which consist in a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system"}]}
```

Source SHA-256: `ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.030340+00:00.  

```json
{"commentType":"FUNCTION","molecule":"Complement C4b-A","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P0C0L4","source":"UniProtKB"}],"value":"Non-enzymatic component of C3 and C5 convertases (By similarity). Generated following cleavage by complement proteases (C1S, MASP2 or GZMK, depending on the complement pathway), it covalently attaches to the surface of pathogens, where it acts as an opsonin that marks the surface of antigens for removal (By similarity). It then recruits the serine protease complement C2b to form the C3 and C5 convertases, which cleave and activate C3 and C5, respectively, the next components of the complement pathways (By similarity). Complement C4b-A isotype is responsible for effective binding to form amide bonds with immune aggregates or protein antigens, while complement C4b-B isotype catalyzes the transacylation of the thioester carbonyl group to form ester bonds with carbohydrate antigens (By similarity)"}]}
```

Source SHA-256: `ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAQ4VMX2.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.030340+00:00.  

```json
{"database":"GO","id":"GO:0004866","properties":[{"key":"GoTerm","value":"F:endopeptidase inhibitor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ae5728c9fe9c34e27041b5ad346d9624bd9437857823ec28237abeb2980dc8be`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)  
**Locator:** `lines 87-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:26:31.699377+00:00.  

```text
CC   -!- FUNCTION: Precursor of non-enzymatic components of the classical,
CC       lectin and GZMK complement pathways, which consist in a cascade of
CC       proteins that leads to phagocytosis and breakdown of pathogens and
CC       signaling that strengthens the adaptive immune system.
CC       {ECO:0000269|PubMed:32769120, ECO:0000269|PubMed:8133084}.
```

Source SHA-256: `b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAQ4VMX2?format=txt&versions=6)  
**Locator:** `lines 200-200`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 6 / 1.  
**Retrieved:** 2026-11-02T04:26:31.699377+00:00.  

```text
DR   GO; GO:0004866; F:endopeptidase inhibitor activity; IEA:InterPro.
```

Source SHA-256: `b5f74ae72f6ee2ffd99fc6d277beacd769703d31a2abeea3667c28d75d5f03f9`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 51565-51575`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004866
name: endopeptidase inhibitor activity
namespace: molecular_function
def: "Binds to and stops, prevents or reduces the activity of an endopeptidase." [GOC:jl]
synonym: "alpha-2 macroglobulin" RELATED []
synonym: "endoproteinase inhibitor" NARROW []
synonym: "proteinase inhibitor" NARROW []
is_a: GO:0030414 ! peptidase inhibitor activity
is_a: GO:0061135 ! endopeptidase regulator activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
