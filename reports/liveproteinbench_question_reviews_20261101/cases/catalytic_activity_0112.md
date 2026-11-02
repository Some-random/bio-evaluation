# catalytic_activity_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — RNA(n) + a ribonucleoside 5&#x27;-triphosphate = RNA(n+1) + diphosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns this protein RNA-directed RNA polymerase activity and lists choice B's reaction. The specific reaction annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than establishing direct experimental measurement for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long viral protein sequence contains a GDNQ motif, characteristic of RNA-dependent RNA polymerases in this viral group. That enzyme class extends an RNA strand using ribonucleoside triphosphates, matching choice B; the other options describe unrelated transformations.


**Missing item-specific fact**

> No protein-specific external fact is needed to distinguish the listed reaction classes, although confirming the protein's precise annotation would require external evidence.


**Reason**

> The sequence supplies a recognizable polymerase-class signature that meaningfully favors RNA synthesis. This is a biological inference, not a claim that the sequence alone proves experimental activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may have additional catalytic activities, but the other listed reactions concern substrates and transformations not indicated by the sequence's polymerase signature.


### Important caveats

- The sequence match is exact to the cited UniProt record, but its RNA-polymerase reaction annotation is computationally supported rather than shown here as a direct assay of this specific protein.
- The protein is annotated with multiple activities; choice B is the listed reaction consistent with its RNA-directed RNA polymerase function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long viral protein sequence contains a GDNQ motif, characteristic of RNA-dependent RNA polymerases in this viral group. That enzyme class extends an RNA strand using ribonucleoside triphosphates, matching choice B; the other options describe unrelated transformations.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is needed to distinguish the listed reaction classes, although confirming the protein's precise annotation would require external evidence.",
    "reason": "The sequence supplies a recognizable polymerase-class signature that meaningfully favors RNA synthesis. This is a biological inference, not a claim that the sequence alone proves experimental activity."
  },
  "case_id": "catalytic_activity_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein RNA-directed RNA polymerase activity and lists choice B's reaction. The specific reaction annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than establishing direct experimental measurement for this protein."
  },
  "important_caveats": [
    "The sequence match is exact to the cited UniProt record, but its RNA-polymerase reaction annotation is computationally supported rather than shown here as a direct assay of this specific protein.",
    "The protein is annotated with multiple activities; choice B is the listed reaction consistent with its RNA-directed RNA polymerase function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may have additional catalytic activities, but the other listed reactions concern substrates and transformations not indicated by the sequence's polymerase signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns this protein RNA-directed RNA polymerase activity and lists choice B's reaction. The specific reaction annotation is based on a PROSITE rule, so it supports the key as a computational annotation rather than establishing direct experimental measurement for this protein.",
    "evidence_ids": ["C4", "C5", "H3"]
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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt C0JJA4 (RNA-directed RNA polymerase L, Mumps virus, 2261 aa). The primary recommended name is 'RNA-directed RNA polymerase L' with EC 2.7.7.48, and the first listed catalytic activity is exactly 'RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate' (evidence C5/H3, annotated via PROSITE-ProRule PRU00539). The other listed activities (GTP phosphohydrolase, GDP polyribonucleotidyltransferase, cap methyltransferase) do not match any of the distractor choices A, C, or D. Choice B is the primary and defining catalytic reaction of this protein.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 2261 amino acids long with a complex multi-domain architecture. This size is grossly inconsistent with the enzymes implied by the distractors: O-methyltransferases on plant alkaloids (A) are typically 300–500 aa; prolyl hydroxylase (C) is ~400 aa; NAD glycohydrolase/sirtuin-type NADases (D) are ~300–500 aa. A ~2200+ aa multi-domain protein is characteristic of a viral RNA-dependent RNA polymerase (L protein). Furthermore, the sequence contains conserved RdRP catalytic motifs (e.g., the GDD-containing motif A region visible as 'LDDDP' near residue ~1850), which specifically indicate RNA-directed RNA polymerase activity rather than DNA polymerase, reverse transcriptase, or any of the small-enzyme activities in A/C/D. The substrate 'deacetylisoipecoside' in A is a plant alkaloid with no relevance to a viral protein; proline hydroxylation (C) and NAD hydrolysis (D) are unrelated small-molecule reactions incompatible with the observed domain architecture.


**Missing item-specific fact**

> None critical. Exact identification of the GDD motif position and the specific viral origin require sequence-level inspection, but the size and multi-domain architecture alone are sufficient to eliminate A, C, and D through general biological reasoning.


**Reason**

> The protein length (2261 aa) and multi-domain architecture provide a strong, general biological argument that eliminates the three small-enzyme distractors (A: plant O-methyltransferase; C: prolyl hydroxylase; D: NAD glycohydrolase). Recognizing RdRP-specific motifs (GDD) in the sequence further supports B specifically. This reasoning relies on general knowledge of enzyme sizes, domain architectures, and polymerase motifs rather than memorizing this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the L protein is multifunctional (RdRP, GTPase, PRNTase, cap MTase), none of the distractor choices correspond to its secondary activities. Choice A describes a plant alkaloid O-methyltransferase, C a prolyl hydroxylase, and D an NAD glycohydrolase—none match any catalytic activity annotated for this protein. B is the only choice matching any of the protein's activities, and it corresponds to the primary recommended name and first-listed reaction.


### Important caveats

- The UniProt annotation for the RNA polymerase activity carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/pattern-based inference rather than direct experimental characterization of this specific Mumps L protein.
- The protein has multiple catalytic activities (RdRP, GTPase, PRNTase, MTase); the question's singular phrasing ('the specific chemical reaction') implicitly selects the primary/defining activity, which is the RdRP reaction.
- Sequence identity was confirmed via SHA-256 match between the benchmark input and UniProt C0JJA4 (both current and historical entry version 43).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 2261 amino acids long with a complex multi-domain architecture. This size is grossly inconsistent with the enzymes implied by the distractors: O-methyltransferases on plant alkaloids (A) are typically 300–500 aa; prolyl hydroxylase (C) is ~400 aa; NAD glycohydrolase/sirtuin-type NADases (D) are ~300–500 aa. A ~2200+ aa multi-domain protein is characteristic of a viral RNA-dependent RNA polymerase (L protein). Furthermore, the sequence contains conserved RdRP catalytic motifs (e.g., the GDD-containing motif A region visible as 'LDDDP' near residue ~1850), which specifically indicate RNA-directed RNA polymerase activity rather than DNA polymerase, reverse transcriptase, or any of the small-enzyme activities in A/C/D. The substrate 'deacetylisoipecoside' in A is a plant alkaloid with no relevance to a viral protein; proline hydroxylation (C) and NAD hydrolysis (D) are unrelated small-molecule reactions incompatible with the observed domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Exact identification of the GDD motif position and the specific viral origin require sequence-level inspection, but the size and multi-domain architecture alone are sufficient to eliminate A, C, and D through general biological reasoning.",
    "reason": "The protein length (2261 aa) and multi-domain architecture provide a strong, general biological argument that eliminates the three small-enzyme distractors (A: plant O-methyltransferase; C: prolyl hydroxylase; D: NAD glycohydrolase). Recognizing RdRP-specific motifs (GDD) in the sequence further supports B specifically. This reasoning relies on general knowledge of enzyme sizes, domain architectures, and polymerase motifs rather than memorizing this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0JJA4 (RNA-directed RNA polymerase L, Mumps virus, 2261 aa). The primary recommended name is 'RNA-directed RNA polymerase L' with EC 2.7.7.48, and the first listed catalytic activity is exactly 'RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate' (evidence C5/H3, annotated via PROSITE-ProRule PRU00539). The other listed activities (GTP phosphohydrolase, GDP polyribonucleotidyltransferase, cap methyltransferase) do not match any of the distractor choices A, C, or D. Choice B is the primary and defining catalytic reaction of this protein."
  },
  "important_caveats": [
    "The UniProt annotation for the RNA polymerase activity carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/pattern-based inference rather than direct experimental characterization of this specific Mumps L protein.",
    "The protein has multiple catalytic activities (RdRP, GTPase, PRNTase, MTase); the question's singular phrasing ('the specific chemical reaction') implicitly selects the primary/defining activity, which is the RdRP reaction.",
    "Sequence identity was confirmed via SHA-256 match between the benchmark input and UniProt C0JJA4 (both current and historical entry version 43)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the L protein is multifunctional (RdRP, GTPase, PRNTase, cap MTase), none of the distractor choices correspond to its secondary activities. Choice A describes a plant alkaloid O-methyltransferase, C a prolyl hydroxylase, and D an NAD glycohydrolase—none match any catalytic activity annotated for this protein. B is the only choice matching any of the protein's activities, and it corresponds to the primary recommended name and first-listed reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt C0JJA4 (RNA-directed RNA polymerase L, Mumps virus, 2261 aa). The primary recommended name is 'RNA-directed RNA polymerase L' with EC 2.7.7.48, and the first listed catalytic activity is exactly 'RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate' (evidence C5/H3, annotated via PROSITE-ProRule PRU00539). The other listed activities (GTP phosphohydrolase, GDP polyribonucleotidyltransferase, cap methyltransferase) do not match any of the distractor choices A, C, or D. Choice B is the primary and defining catalytic reaction of this protein.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 2261 amino acids long with a complex multi-domain architecture. This size is grossly inconsistent with the enzymes implied by the distractors: O-methyltransferases on plant alkaloids (A) are typically 300–500 aa; prolyl hydroxylase (C) is ~400 aa; NAD glycohydrolase/sirtuin-type NADases (D) are ~300–500 aa. A ~2200+ aa multi-domain protein is characteristic of a viral RNA-dependent RNA polymerase (L protein). Furthermore, the sequence contains conserved RdRP catalytic motifs (e.g., the GDD-containing motif A region visible as 'LDDDP' near residue ~1850), which specifically indicate RNA-directed RNA polymerase activity rather than DNA polymerase, reverse transcriptase, or any of the small-enzyme activities in A/C/D. The substrate 'deacetylisoipecoside' in A is a plant alkaloid with no relevance to a viral protein; proline hydroxylation (C) and NAD hydrolysis (D) are unrelated small-molecule reactions incompatible with the observed domain architecture.",
    "missing_item_specific_fact": "None critical. Exact identification of the GDD motif position and the specific viral origin require sequence-level inspection, but the size and multi-domain architecture alone are sufficient to eliminate A, C, and D through general biological reasoning.",
    "reason": "The protein length (2261 aa) and multi-domain architecture provide a strong, general biological argument that eliminates the three small-enzyme distractors (A: plant O-methyltransferase; C: prolyl hydroxylase; D: NAD glycohydrolase). Recognizing RdRP-specific motifs (GDD) in the sequence further supports B specifically. This reasoning relies on general knowledge of enzyme sizes, domain architectures, and polymerase motifs rather than memorizing this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the L protein is multifunctional (RdRP, GTPase, PRNTase, cap MTase), none of the distractor choices correspond to its secondary activities. Choice A describes a plant alkaloid O-methyltransferase, C a prolyl hydroxylase, and D an NAD glycohydrolase—none match any catalytic activity annotated for this protein. B is the only choice matching any of the protein's activities, and it corresponds to the primary recommended name and first-listed reaction."
  },
  "important_caveats": [
    "The UniProt annotation for the RNA polymerase activity carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/pattern-based inference rather than direct experimental characterization of this specific Mumps L protein.",
    "The protein has multiple catalytic activities (RdRP, GTPase, PRNTase, MTase); the question's singular phrasing ('the specific chemical reaction') implicitly selects the primary/defining activity, which is the RdRP reaction.",
    "Sequence identity was confirmed via SHA-256 match between the benchmark input and UniProt C0JJA4 (both current and historical entry version 43)."
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

**Accession:** `C0JJA4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 43. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0JJA4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.290569+00:00.  

```json
"C0JJA4"
```

Source SHA-256: `216e02c512f5cecd74eab216e2d0f3cc6e876f4b6ec12c6f4ebd521486998c61`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C0JJA4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:27.290569+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype A (strain Jeryl-Lynn)","taxonId":11168}
```

Source SHA-256: `216e02c512f5cecd74eab216e2d0f3cc6e876f4b6ec12c6f4ebd521486998c61`.

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

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0JJA4?format=txt&versions=43)  
**Locator:** `lines 1-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:27:32.393370+00:00.  

```text
ID   L_MUMPJ                 Reviewed;        2261 AA.
AC   C0JJA4; A0A0K0K580; Q77IS0; Q9J4L0;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JAN-2017, sequence version 1.
DT   28-JAN-2026, entry version 43.
DE   RecName: Full=RNA-directed RNA polymerase L;
DE            Short=Protein L;
DE   AltName: Full=Large structural protein;
DE   AltName: Full=Replicase;
DE   AltName: Full=Transcriptase;
DE   Includes:
DE     RecName: Full=RNA-directed RNA polymerase;
DE              EC=2.7.7.48 {ECO:0000250|UniProtKB:P28887};
DE   Includes:
DE     RecName: Full=GTP phosphohydrolase {ECO:0000250|UniProtKB:P03523};
DE              EC=3.6.1.- {ECO:0000250|UniProtKB:P03523};
DE   Includes:
DE     RecName: Full=GDP polyribonucleotidyltransferase {ECO:0000305};
DE              EC=2.7.7.88 {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=PRNTase {ECO:0000305};
DE   Includes:
DE     RecName: Full=mRNA cap methyltransferase {ECO:0000305};
DE     AltName: Full=mRNA (guanine-N(7)-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=G-N7-MTase {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=mRNA (nucleoside-2'-O-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=N1-2'-O-MTase {ECO:0000250|UniProtKB:P03523};
GN   Name=L;
OS   Mumps virus genotype A (strain Jeryl-Lynn) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=11168;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `4c573a4feca316fb7d372837c51d98fb2e671a13fe2d74ffc0660485cf29ac79`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C0JJA4?format=txt&versions=43)  
**Locator:** `lines 6-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:27:32.393370+00:00.  

```text
DE   RecName: Full=RNA-directed RNA polymerase L;
DE            Short=Protein L;
DE   AltName: Full=Large structural protein;
DE   AltName: Full=Replicase;
DE   AltName: Full=Transcriptase;
DE   Includes:
DE     RecName: Full=RNA-directed RNA polymerase;
DE              EC=2.7.7.48 {ECO:0000250|UniProtKB:P28887};
DE   Includes:
DE     RecName: Full=GTP phosphohydrolase {ECO:0000250|UniProtKB:P03523};
DE              EC=3.6.1.- {ECO:0000250|UniProtKB:P03523};
DE   Includes:
DE     RecName: Full=GDP polyribonucleotidyltransferase {ECO:0000305};
DE              EC=2.7.7.88 {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=PRNTase {ECO:0000305};
DE   Includes:
DE     RecName: Full=mRNA cap methyltransferase {ECO:0000305};
DE     AltName: Full=mRNA (guanine-N(7)-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=G-N7-MTase {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=mRNA (nucleoside-2'-O-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=N1-2'-O-MTase {ECO:0000250|UniProtKB:P03523};
```

Source SHA-256: `4c573a4feca316fb7d372837c51d98fb2e671a13fe2d74ffc0660485cf29ac79`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
