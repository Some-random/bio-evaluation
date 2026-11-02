# cofactor_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGLQLMTPASSPMGPFFGLPWQQEAIHDNIYTPRKYQVELLEAALDHNIIVCLNSGSGKTFIAVLLSKELSYQIRGDFSKNAKRTVFLVNSEKQVSQQVSAVRTHTDLKVGEYSDLQKTQCWAKEKWYQEFQTHQVLVMTCHIFLNVLKTGNVSLSNINLLVFDECHLAIQDHPYRDIMKICESCQTCPRILGLTASILNGKCDPHDLEEKIQNLEEILRSNAETATDLVVLDRYASQPCEIVLDCGPYVDRSGLYQRLLNELDEALNFLTDCNISTHSKERDSTIISKQILSDCWAVLLVLGPWCADKVAGMMVRELQKYIKHEQEELHRKFLLFTDTILRKIHALCEEHFSPASLDMKFVTPKVIKLLEILRKYKPYERQQFESVEWYNNRNQDNYVSWSDSEDDDDDEDEEIEEKEKTETSFPSPFTNILCGIIFVERRYTAVVLNRLIKEAGKQDPELAYISSNFITGHGIGKNQPRNKQMEVEFRKQEEVLRKFRAHETNLLIATSIVEEGVDIPKCNLVVRFDLPSEYRSYVQSKGRARAPISNYIMLADSDKIKAFEEDLKTYKAIEKILRNKCSKSMDCGNTESEPIVDDDEIFPPYVLRQDDGSPRVTINTAIGHINRYCARLPSDPFTHLAPKCRTRELPDGPYRSTLYLPINSPLRAPIVGPPMNCARLAERAVALICCKKLHEIGELDDHLMPVGKETVKYEEELDLHDEEETSVPGRPGSTKRRQCYPKAIPECLRNSYPKPGQPCYLYVIGMVLTTPLPDELNFRRRKLYPPEDTTRCFGILTAKPIPQIPHFPVYTRSGEVTISIELKKSGFSLNLEQLELITRLHRYIFSHILRLEKPALEFKPTVADCAYCVLPLNVVNDSGTLDIDFKFVEDIEKSEARTGIPNTQYSAEGPFIFKLEDYQDAVIIPRYRNFDQPHRFYVADVYTDLTPLSKFPSPEYETFAEYYKTKYNLDLTNLNQPLLDVDHTSSRLNLLTPRHLNQKGKALPLSSAEKRKAKWESLQNKQILVPELCAIHPVPASLWRKAVCLPSILYRLHCLLTAEELRAQTAIDAGVGVKSLPEDFRYPNLDFGWKRSIDGKTFISNQSFSAMERESDCRLDITTVPDSATSSAAHHVMYTQMNDQMSVNCTPPCPKSLSDLQGVCFSDDCKAINGITCNGLTNGNWEAESGVCFQKDELIACKQEIPEKSTSFHVQNLPNDNQPILNECTLSKKFLDGNVGKPISDECPSTCTSDINYESGLSSGYSSKTLGPNPGLILQALTLSNASDGFNLERLEMLGDSFLKHAITTYLFCTYPDSHEGRLSYMRSKKVSNCNLYRLGKKKGSPSRMVVSIFDPPVNWLPPGYIVNQDKNCDKWESNETSGESVMANGKIDEDFEDEEDEDLMWRNPKEETDFDDDFLEYDQEHIKFIDNMLMGSGAFVKKIQLSAFAPPDQNYEWRPPKKPPLESAPFRSEFDDFDYSSWDAMCYLDPSKAVEEDDFVVGFWNPSEENGGADAGKQSISYDLHTEQCIADKSIADCVEALLGCYLTSCGERAAQLFLCSLGLKVLPEVRKPVTNTSTRGNYSLDGRTNSELSCKGIEYGYLKIPPRCMFEHPEAEKTLDHLISGFENFEKKINYQFKNKAYLLQAFTHASYHYNTITDCYQRLEFLGDAILDYLITKHLYEDPRQHSPGVLTDLRSALVNNTIFASLAVKYDYHKYFKAISPELFHVIDDFVQFQLEKNEMQGMDSELRRSEEDEEKEEDIEVPKAMGDIFESLAGAIYMDSGMSLETVWRVYYPMMQPLIEKFSANVPRSPVRELLEMEPETAKFSPAERTYDGKVRVMVEVVGKGKFKGVGRSYRIAKSAAARRALRSLKANQSQVPNS

[Multiple Choices]
A. Fe cation
B. FMN
C. Mg(2+)
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

> The supplied sequence matches Xenopus laevis Dicer-S. UniProt annotates Mg(2+) as a cofactor and says the protein binds two magnesium or manganese ions per subunit. This supports choice C, though the annotation is transferred by similarity from human Q9UPY3 rather than direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If the protein were identified as a Dicer/RNase III nuclease, its divalent-metal-dependent RNA cleavage would make Mg(2+) biologically plausible among these choices. The input, however, provides no protein identity or function, and that family assignment is not established by a clear, self-contained sequence clue.


**Missing item-specific fact**

> The protein's identity/function and its annotated or experimentally established metal dependence; the available annotation for this sequence is similarity-transferred from human Dicer.


**Reason**

> Selecting Mg(2+) relies on recognizing or looking up this protein's identity and cofactor annotation, rather than on a sufficiently discriminating argument supplied by the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports Mg(2+); it also mentions Mn(2+), but manganese is not offered. The listed alternatives are not supported by the provided evidence.


### Important caveats

- The reviewer-only annotation is not information supplied to the evaluated model.
- The cofactor evidence is transferred by similarity from human Q9UPY3, not direct experimental evidence for the Xenopus sequence.
- The annotation says magnesium or manganese, so magnesium is supported but is not necessarily the only metal that can serve.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If the protein were identified as a Dicer/RNase III nuclease, its divalent-metal-dependent RNA cleavage would make Mg(2+) biologically plausible among these choices. The input, however, provides no protein identity or function, and that family assignment is not established by a clear, self-contained sequence clue.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/function and its annotated or experimentally established metal dependence; the available annotation for this sequence is similarity-transferred from human Dicer.",
    "reason": "Selecting Mg(2+) relies on recognizing or looking up this protein's identity and cofactor annotation, rather than on a sufficiently discriminating argument supplied by the sequence and choices alone."
  },
  "case_id": "cofactor_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches Xenopus laevis Dicer-S. UniProt annotates Mg(2+) as a cofactor and says the protein binds two magnesium or manganese ions per subunit. This supports choice C, though the annotation is transferred by similarity from human Q9UPY3 rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation is not information supplied to the evaluated model.",
    "The cofactor evidence is transferred by similarity from human Q9UPY3, not direct experimental evidence for the Xenopus sequence.",
    "The annotation says magnesium or manganese, so magnesium is supported but is not necessarily the only metal that can serve."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports Mg(2+); it also mentions Mn(2+), but manganese is not offered. The listed alternatives are not supported by the provided evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches Xenopus laevis Dicer-S. UniProt annotates Mg(2+) as a cofactor and says the protein binds two magnesium or manganese ions per subunit. This supports choice C, though the annotation is transferred by similarity from human Q9UPY3 rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If the protein were identified as a Dicer/RNase III nuclease, its divalent-metal-dependent RNA cleavage would make Mg(2+) biologically plausible among these choices. The input, however, provides no protein identity or function, and that family assignment is not established by a clear, self-contained sequence clue.",
    "missing_item_specific_fact": "The protein's identity/function and its annotated or experimentally established metal dependence; the available annotation for this sequence is similarity-transferred from human Dicer.",
    "reason": "Selecting Mg(2+) relies on recognizing or looking up this protein's identity and cofactor annotation, rather than on a sufficiently discriminating argument supplied by the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports Mg(2+); it also mentions Mn(2+), but manganese is not offered. The listed alternatives are not supported by the provided evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation is not information supplied to the evaluated model.",
    "The cofactor evidence is transferred by similarity from human Q9UPY3, not direct experimental evidence for the Xenopus sequence.",
    "The annotation says magnesium or manganese, so magnesium is supported but is not necessarily the only metal that can serve."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A8J1LLF7 (Endoribonuclease Dicer-S, Xenopus laevis) annotates Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 magnesium or manganese ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity from human Dicer-1, Q9UPY3), so it is a computational transfer rather than direct experimental measurement on this Xenopus protein. However, the Mg(2+) requirement for RNase III-family Dicer enzymes is well-established across multiple species by structural and biochemical studies. Among the four choices, Mg(2+) is the only annotated cofactor; Mn(2+) is also listed but absent from the options. Fe cation, FMN, and Fe(2+) are not associated with Dicer catalysis.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If one could identify the protein as an RNase III-family endoribonuclease (Dicer), general biochemistry dictates that Mg(2+) is the canonical catalytic cofactor for RNase III enzymes, immediately eliminating FMN (a redox/flavin cofactor) and Fe-based cofactors (associated with oxidoreductases and heme proteins). However, recognizing this 1881-aa sequence as Dicer or even as a nuclease from the raw sequence alone requires specific domain-level knowledge (PAZ, RNase III, helicase architecture) that is not extractable through general biological reasoning without prior familiarity with the protein family.


**Missing item-specific fact**

> Identification of the protein as Endoribonuclease Dicer-S / RNase III-family enzyme. Without knowing the protein's identity or family, a model cannot reliably distinguish a nuclease (Mg-dependent) from other large multi-domain proteins that might use different cofactors. The sequence does not contain a short, universally recognizable catalytic motif that would allow a general biologist to classify it as a nuclease from scratch.


**Reason**

> The correct answer follows logically IF the protein is identified as Dicer/RNase III, but that identification from a raw 1881-aa sequence depends on memorized or database-lookup knowledge of the protein's identity and domain architecture. General biological reasoning cannot reliably classify this sequence as a nuclease versus, say, a large scaffold or helicase-only protein without specific training on Dicer sequences.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only Mg(2+) is annotated as a cofactor for this protein. Mn(2+) is also a cofactor per UniProt but is not offered as an option. Fe cation (A) and Fe(2+) (D) are not associated with Dicer catalysis, and FMN (B) is a flavin/redox cofactor unrelated to RNase III activity. No ambiguity among the provided options.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from human Dicer-1 Q9UPY3), meaning it is a computational transfer, not direct experimental measurement on Xenopus Dicer-S. The broader RNase III Mg(2+) requirement is well-supported experimentally in other systems.
- Mn(2+) is also listed as a cofactor in the annotation but is absent from the answer choices, so it does not create ambiguity within the given options.
- The protein was only integrated into Swiss-Prot on 2025-06-18 (entry version 19 first released 2026-01-28), so it may not have been in databases at the time the benchmark was constructed; the author may have relied on the human ortholog Q9UPY3 or on sequence-based prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If one could identify the protein as an RNase III-family endoribonuclease (Dicer), general biochemistry dictates that Mg(2+) is the canonical catalytic cofactor for RNase III enzymes, immediately eliminating FMN (a redox/flavin cofactor) and Fe-based cofactors (associated with oxidoreductases and heme proteins). However, recognizing this 1881-aa sequence as Dicer or even as a nuclease from the raw sequence alone requires specific domain-level knowledge (PAZ, RNase III, helicase architecture) that is not extractable through general biological reasoning without prior familiarity with the protein family.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of the protein as Endoribonuclease Dicer-S / RNase III-family enzyme. Without knowing the protein's identity or family, a model cannot reliably distinguish a nuclease (Mg-dependent) from other large multi-domain proteins that might use different cofactors. The sequence does not contain a short, universally recognizable catalytic motif that would allow a general biologist to classify it as a nuclease from scratch.",
    "reason": "The correct answer follows logically IF the protein is identified as Dicer/RNase III, but that identification from a raw 1881-aa sequence depends on memorized or database-lookup knowledge of the protein's identity and domain architecture. General biological reasoning cannot reliably classify this sequence as a nuclease versus, say, a large scaffold or helicase-only protein without specific training on Dicer sequences."
  },
  "case_id": "cofactor_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A8J1LLF7 (Endoribonuclease Dicer-S, Xenopus laevis) annotates Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 magnesium or manganese ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity from human Dicer-1, Q9UPY3), so it is a computational transfer rather than direct experimental measurement on this Xenopus protein. However, the Mg(2+) requirement for RNase III-family Dicer enzymes is well-established across multiple species by structural and biochemical studies. Among the four choices, Mg(2+) is the only annotated cofactor; Mn(2+) is also listed but absent from the options. Fe cation, FMN, and Fe(2+) are not associated with Dicer catalysis."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from human Dicer-1 Q9UPY3), meaning it is a computational transfer, not direct experimental measurement on Xenopus Dicer-S. The broader RNase III Mg(2+) requirement is well-supported experimentally in other systems.",
    "Mn(2+) is also listed as a cofactor in the annotation but is absent from the answer choices, so it does not create ambiguity within the given options.",
    "The protein was only integrated into Swiss-Prot on 2025-06-18 (entry version 19 first released 2026-01-28), so it may not have been in databases at the time the benchmark was constructed; the author may have relied on the human ortholog Q9UPY3 or on sequence-based prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only Mg(2+) is annotated as a cofactor for this protein. Mn(2+) is also a cofactor per UniProt but is not offered as an option. Fe cation (A) and Fe(2+) (D) are not associated with Dicer catalysis, and FMN (B) is a flavin/redox cofactor unrelated to RNase III activity. No ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A8J1LLF7 (Endoribonuclease Dicer-S, Xenopus laevis) annotates Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 magnesium or manganese ions per subunit.' The evidence code is ECO:0000250 (inferred by similarity from human Dicer-1, Q9UPY3), so it is a computational transfer rather than direct experimental measurement on this Xenopus protein. However, the Mg(2+) requirement for RNase III-family Dicer enzymes is well-established across multiple species by structural and biochemical studies. Among the four choices, Mg(2+) is the only annotated cofactor; Mn(2+) is also listed but absent from the options. Fe cation, FMN, and Fe(2+) are not associated with Dicer catalysis.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If one could identify the protein as an RNase III-family endoribonuclease (Dicer), general biochemistry dictates that Mg(2+) is the canonical catalytic cofactor for RNase III enzymes, immediately eliminating FMN (a redox/flavin cofactor) and Fe-based cofactors (associated with oxidoreductases and heme proteins). However, recognizing this 1881-aa sequence as Dicer or even as a nuclease from the raw sequence alone requires specific domain-level knowledge (PAZ, RNase III, helicase architecture) that is not extractable through general biological reasoning without prior familiarity with the protein family.",
    "missing_item_specific_fact": "Identification of the protein as Endoribonuclease Dicer-S / RNase III-family enzyme. Without knowing the protein's identity or family, a model cannot reliably distinguish a nuclease (Mg-dependent) from other large multi-domain proteins that might use different cofactors. The sequence does not contain a short, universally recognizable catalytic motif that would allow a general biologist to classify it as a nuclease from scratch.",
    "reason": "The correct answer follows logically IF the protein is identified as Dicer/RNase III, but that identification from a raw 1881-aa sequence depends on memorized or database-lookup knowledge of the protein's identity and domain architecture. General biological reasoning cannot reliably classify this sequence as a nuclease versus, say, a large scaffold or helicase-only protein without specific training on Dicer sequences."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only Mg(2+) is annotated as a cofactor for this protein. Mn(2+) is also a cofactor per UniProt but is not offered as an option. Fe cation (A) and Fe(2+) (D) are not associated with Dicer catalysis, and FMN (B) is a flavin/redox cofactor unrelated to RNase III activity. No ambiguity among the provided options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from human Dicer-1 Q9UPY3), meaning it is a computational transfer, not direct experimental measurement on Xenopus Dicer-S. The broader RNase III Mg(2+) requirement is well-supported experimentally in other systems.",
    "Mn(2+) is also listed as a cofactor in the annotation but is absent from the answer choices, so it does not create ambiguity within the given options.",
    "The protein was only integrated into Swiss-Prot on 2025-06-18 (entry version 19 first released 2026-01-28), so it may not have been in databases at the time the benchmark was constructed; the author may have relied on the human ortholog Q9UPY3 or on sequence-based prediction."
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

**Accession:** `A0A8J1LLF7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
"A0A8J1LLF7"
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"3.1.26.3"}],"fullName":{"value":"Endoribonuclease Dicer-S"}}}
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8J1LLF7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:02.871482+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UPY3","source":"UniProtKB"}],"name":"Mg(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UPY3","source":"UniProtKB"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9UPY3","source":"UniProtKB"}],"value":"Binds 2 magnesium or manganese ions per subunit."}]}}
```

Source SHA-256: `1743c4c7e1fb45c35a3ab6a13e0377d823fc271578ce1e8cc74605edb08e6a17`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8J1LLF7?format=txt&versions=19)  
**Locator:** `lines 55-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:05.098009+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:Q9UPY3};
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000250|UniProtKB:Q9UPY3};
CC       Note=Binds 2 magnesium or manganese ions per subunit.
CC       {ECO:0000250|UniProtKB:Q9UPY3};
```

Source SHA-256: `1ee78b98ec19d73b1d687d332eb3f9b6453d7a8816c912104ab16c4b4c2b5ead`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
