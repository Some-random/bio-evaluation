# catalytic_activity_0112

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MAGLNEILLPEVHLNSPIVRYKLFYYILHGQLPNDLEPDDLGPLANQNWKAIRAEESQVHARLKQIRVELIARIPSLRWTRSQREIAILIWPRILPILQAYDLRQSMQLPTVWEKLTQSTVNLISDGLERVVLHISNQLTGKPNLFTRSRAGQDTKDYSIPSTRELSQIWFNNEWSGSVKTWLMIKYRMRQLITNQKTGELTDLVTIVDTRSTLCIITPELVALYSSEHKALTYLTFEMVLMVTDMLEGRLNVSSLCTASHYLSPLKKRIEVLLTLVDDLALLMGDKVYGIVSSLESFVYAQLQYGDPVIDIKGTFYGFICNEILDLLTEDNIFTEEEANKVLLDLTSQFDNLSPDLTAELLCIMRLWGHPTLTASQAASKVRESMCAPKVLDFQTIMKTLAFFHAILINGYRRSHNGIWPPTTLHGNAPKSLIEMRHDNSELKYEYVLKNWKSISMLRIHKCFDASPDEDLSIFMKDKAISCPRQDWMGVFRRSLIKQRYRDANRPLPQPFNRRLLLNFLEDDRFDPIKELEYVTSGEYLRDPEFCASYSLKEKEIKATGRIFAKMTKRMRSCQVIAESLLANHAGKLMRENGVVLDQLKLTKSLLTMNQIGIISEHSRRSTADNMTLAHSGSNKHRINNSQFKKNKDNKHEMPDDGFEIAACFLTTDLTKYCLNWRYQVIIPFARTLNSMYGIPHLFEWIHLRLMRSTLYVGDPFNPPSDPTQLDLDTALNDDIFIVSPRGGIEGLCQKLWTMISISTIILSATEANTRVMSMVQGDNQAIAITTRVVRSLSHSEKKEQAYKASKLFFERLRANNHGIGHHLKEQETILSSDFFIYSKRVFYKGRILTQALKNVSKMCLTADILGDCSQASCSNLATTVMRLTENGVEKDLCYFLNAFMTIRQLCYDLVFPQTKSLSQDITNAYLNHPILISRLCLLPSQLGGLNFLSCSRLFNRNIGDPLVSAIADVKRLIKAGCLDIWVLYNILGRRPGKGKWSTLAADPYTLNIDYLVPSTTFLKKHAQYTLMERSVNPMLRGVFSENAAEEEEELAQYLLDREVVMPRVAHVILAQSSCGRRKQIQGYLDSTRTIIRYSLEVRPLSAKKLNTVIEYNLLYLSYNLEIIEKPNIVQPFLNAINVDTCSIDIARSLRKLSWATLLNGRPIEGLETPDPIELVHGCLIIGSDECEHCSSGDDKFTWFFLPKGIRLDDDPASNPPIRVPYIGSKTDERRVASMAYIKGASVSLKSALRLAGVYIWAFGDTEESWQDAYELASTRVNLTLEQLQSLTPLPTSANLVHRLDDGTTQLKFTPASSYAFSSFVHISNDCQILEIDDQVTDSNLIYQQVMITGLALIETWNNPPINFSVYETTLHLHTGSSCCIRPVESCVVNPPLLPVPLINVPQMNKFVYDPEPLSLLEMEKIEDIAYQTRIGGLDQIPLLEKIPLLAHLTAKQMVNSITGLDEATSIMNDAVVQADYTSNWISECCYTYIDSVFVYSGWALLLELSYQMYYLRIQGIQGILDYVYMTLRRIPGMAITGISSTISHPRILRRCINLDVIAPINSPHIASLDYTKLSIDAVMWGTKQVLTNISQGIDYEIVVPSESQLTLSDRVLNLVARKLSLLAIIWANYNYPPKVKGMSPEDKCQALTTHLLQTVEYVEYIQIEKTNIRRMIIEPKLTAYPSNLFYLSRKLLNAIRDSEEGQFLIASYYNSFGYLEPILMESKIFNLSSSESASLTEFDFILNLELSDASLEKYSLPSLLMTAENMDNPFPQPPLHHVLRPLGLSSTSWYKTISVLNYISHMKISDGAHLYLAEGSGASMSLIETFLPGETIWYNSLFNSGENPPQRNFAPLPTQFIESVPYRLIQAGIAAGNGIVQSFYPLWNGNSDITDLSTKTSVEYIIHKVGADTCALVHVDLEGVPGSMNSMLERAQVHALLITVTVLKPGGLLILKASWEPFNRFSFLLTVLWQFFSTIRILRSSYSDPNNHEVYIIATLAVDPTTSSFTTALNRARTLNEQGFSLIPPELVSEYWRKRVEQGQIIQDCIDKVISECVRDQYLADNNIILQAGGTPSTRKWLDLPDYSSFNELQSEMARLITIHLKEVIEILKGQASDHDTLLFTSYNVGPLGKINTILRLIVERILMYTVRNWCILPTQTRLTLRQSIELGEFRLRDVITPMEILKLSPNRKYLKSALNQSTFNHLMGETSDILLNRAYQKRIWKAIGCVIYCFGLLTPDVEGSERIDVDNDIPDYDIHGDII

[Multiple Choices]
A. deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
B. RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate
C. L-proline + 2-oxoglutarate + O2 = trans-4-hydroxy-L-proline + succinate + CO2
D. NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns this protein RNA-directed RNA polymerase activity and lists choice B's reaction. The specific reaction annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than establishing direct experimental measurement for this protein.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long viral protein sequence contains a GDNQ motif, characteristic of RNA-dependent RNA polymerases in this viral group. That enzyme class extends an RNA strand using ribonucleoside triphosphates, matching choice B; the other options describe unrelated transformations.

**Missing item-specific fact**

> No protein-specific external fact is needed to distinguish the listed reaction classes, although confirming the protein's precise annotation would require external evidence.

**Reason**

> The sequence supplies a recognizable polymerase-class signature that meaningfully favors RNA synthesis. This is a biological inference, not a claim that the sequence alone proves experimental activity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The protein may have additional catalytic activities, but the other listed reactions concern substrates and transformations not indicated by the sequence's polymerase signature.

### Important caveats

- The sequence match is exact to the cited UniProt record, but its RNA-polymerase reaction annotation is computationally supported rather than shown here as a direct assay of this specific protein.
- The protein is annotated with multiple activities; choice B is the listed reaction consistent with its RNA-directed RNA polymerase function.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein RNA-directed RNA polymerase activity and lists choice B's reaction. The specific reaction annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than establishing direct experimental measurement for this protein.",
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long viral protein sequence contains a GDNQ motif, characteristic of RNA-dependent RNA polymerases in this viral group. That enzyme class extends an RNA strand using ribonucleoside triphosphates, matching choice B; the other options describe unrelated transformations.",
    "missing_item_specific_fact": "No protein-specific external fact is needed to distinguish the listed reaction classes, although confirming the protein's precise annotation would require external evidence.",
    "reason": "The sequence supplies a recognizable polymerase-class signature that meaningfully favors RNA synthesis. This is a biological inference, not a claim that the sequence alone proves experimental activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may have additional catalytic activities, but the other listed reactions concern substrates and transformations not indicated by the sequence's polymerase signature."
  },
  "important_caveats": [
    "The sequence match is exact to the cited UniProt record, but its RNA-polymerase reaction annotation is computationally supported rather than shown here as a direct assay of this specific protein.",
    "The protein is annotated with multiple activities; choice B is the listed reaction consistent with its RNA-directed RNA polymerase function."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `C0JJA4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 43. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0JJA4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.290569+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Large structural protein"}},{"fullName":{"value":"Replicase"}},{"fullName":{"value":"Transcriptase"}}],"includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P28887","source":"UniProtKB"}],"value":"2.7.7.48"}],"fullName":{"value":"RNA-directed RNA polymerase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"3.6.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"GTP phosphohydrolase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PRNTase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"2.7.7.88"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"GDP polyribonucleotidyltransferase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"mRNA (guanine-N(7)-)-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"G-N7-MTase"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"mRNA (nucleoside-2'-O-)-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"N1-2'-O-MTase"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"mRNA cap methyltransferase"}}}],"recommendedName":{"fullName":{"value":"RNA-directed RNA polymerase L"},"shortNames":[{"value":"Protein L"}]}}
```

Source SHA-256: `216e02c512f5cecd74eab216e2d0f3cc6e876f4b6ec12c6f4ebd521486998c61`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0JJA4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.290569+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.7.48","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00539","source":"PROSITE-ProRule"}],"name":"RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21248"},{"database":"Rhea","id":"RHEA-COMP:14527"},{"database":"Rhea","id":"RHEA-COMP:17342"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:61557"},{"database":"ChEBI","id":"CHEBI:140395"}]}}
```

Source SHA-256: `216e02c512f5cecd74eab216e2d0f3cc6e876f4b6ec12c6f4ebd521486998c61`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0JJA4?format=txt&versions=43)  
**Locator:** `lines 114-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:27:32.393370+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) +
CC         diphosphate; Xref=Rhea:RHEA:21248, Rhea:RHEA-COMP:14527, Rhea:RHEA-
CC         COMP:17342, ChEBI:CHEBI:33019, ChEBI:CHEBI:61557, ChEBI:CHEBI:140395;
CC         EC=2.7.7.48; Evidence={ECO:0000255|PROSITE-ProRule:PRU00539};
```

Source SHA-256: `4c573a4feca316fb7d372837c51d98fb2e671a13fe2d74ffc0660485cf29ac79`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 112). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
