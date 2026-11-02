# GO_molecular_function_0093

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — endopeptidase inhibitor activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.

Cited evidence: [C1](#evidence-c1), [C12](#evidence-c12), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence is consistent with a secreted protein, and the sequence does not show an obvious canonical GTPase or translation-factor signature. These clues weaken some distractors but do not establish endopeptidase inhibitor activity over RNA binding or identify the specific GO annotation.

**Missing item-specific fact**

> The protein-specific identification as complement C4-A and its InterPro-derived GO annotation for endopeptidase inhibitor activity are absent from the input.

**Reason**

> Choosing A depends on an item-specific family/domain annotation or prior knowledge of this protein, rather than a sufficiently discriminating inference from the sequence and choices alone.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied evidence directly supports only A among the listed options, although that support is computational and does not establish it as C4-A's primary experimentally demonstrated molecular function.

### Important caveats

- The sequence matches the current and historical UniProt records, but the author's exact source snapshot is unknown.
- The endopeptidase inhibitor annotation is IEA:InterPro; it should not be presented as direct experimental evidence.
- UniProt describes the protein's complement role as a precursor of non-enzymatic components, a major function not represented among the choices.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for mouse complement C4-A, which carries GO:0004866, endopeptidase inhibitor activity, assigned by IEA:InterPro. This supports the key as a computational annotation, not as experimentally established activity. The entry's description of C4 as a non-enzymatic complement component does not by itself contradict that annotation.",
    "evidence_ids": [
      "C1",
      "C12",
      "H9",
      "H5"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0AAQ4VMX2`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 6. The exact author source snapshot remains unknown.

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

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 93). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
