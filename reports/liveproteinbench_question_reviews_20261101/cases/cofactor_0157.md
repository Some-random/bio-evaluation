# cofactor_0157

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPAATDLANAWFAKRGWKPFAFQRRVWAAVERGESGLLHASTGAGKTYAVWLAALRAFKPRPQGRHLAPIQVLWVTPMRALAADTARALQAPLDELQLPWSVGVRSGDTNSAERARQARRLPSVLITTPESLTLLLTRAKAREDFATLQLVVVDEWHELLGNKRGVQLQLALARLRHWHPGLPTWGLSATLGNLQHARDVLLPQGGLLVQGRQDKALQVDTLLPKAIERFPWAGHMGLKMLDQVCHEIDASASSLVFTNTRAQAEIWYQALLEARPDWAGLIALHHASLARDTRDWVERSLKQGSLKAVICTSSLDLGVDFLPVERVLQIGSAKGIARLMQRAGRSGHAPGRRSRVTLVPTHSLELVEAAAARQALLAGHIEARFSPRLCMDVLVQHLVSMALGSGFRPEQLLAEVRSTWAFRQLRDSQWQWALDFVCHGGSSLTAYPDYQRVERQADGVYRVTSERLARRHRMGIGTIVSDANLQLKYWSKGGGGKTLGSVEEAFIARLRPGDTLVFAGRVLELVRVENMTAYVRRSTARKAAVARWNGGRMPLSSELADALVEQLDAAAHERFEGPEMRAVRPLLALQAQWSALPTTSTLLAETFKSRQGWHLFLYPFAGRMANLGLANLIAWRVSRAQPLSVSIAVNDYGFELLSPAQVDWASHLPQALGTADLLEDVLASLNAGEMALRRFREIAQIAGLVFGGYPAAQKSTRQIQASSGLFYEVFRKHDAGNLLLGQARDEVLSEELEIERLHRQLLKMSELQLDLQALRRPGPLAFALLVEGMRETLSTEKLADRIARMVAELEQAANAG

[Multiple Choices]
A. FAD
B. Fe(2+)
C. Mg(2+)
D. Mn(2+)
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

> The sequence matches the annotated Lhr-Core helicase, whose cited cofactor annotation reports Mg(2+) and says its ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. This supports Mg(2+) among the listed choices.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an ATP-dependent helicase, and general knowledge makes Mg(2+) a plausible ATPase cofactor. But that does not establish this protein's preference over Mn(2+), another listed metal.


**Missing item-specific fact**

> The protein-specific finding that its ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+) stimulates only at low concentrations.


**Reason**

> The supplied sequence can suggest ATPase activity, but distinguishing Mg(2+) from Mn(2+) as the relevant cofactor depends on a protein-specific activity result not provided in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the annotation also reports high activity with Ca(2+), Ca(2+) is not an option; among the listed choices, Mg(2+) is supported.


### Important caveats

- The cofactor evidence is a curated annotation citing a publication; the primary study was not independently reviewed here.
- The cited finding describes highest activity with Mg(2+) or Ca(2+), not an absolute inability to function with other ions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent helicase, and general knowledge makes Mg(2+) a plausible ATPase cofactor. But that does not establish this protein's preference over Mn(2+), another listed metal.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that its ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+) stimulates only at low concentrations.",
    "reason": "The supplied sequence can suggest ATPase activity, but distinguishing Mg(2+) from Mn(2+) as the relevant cofactor depends on a protein-specific activity result not provided in the question."
  },
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated Lhr-Core helicase, whose cited cofactor annotation reports Mg(2+) and says its ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. This supports Mg(2+) among the listed choices."
  },
  "important_caveats": [
    "The cofactor evidence is a curated annotation citing a publication; the primary study was not independently reviewed here.",
    "The cited finding describes highest activity with Mg(2+) or Ca(2+), not an absolute inability to function with other ions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the annotation also reports high activity with Ca(2+), Ca(2+) is not an option; among the listed choices, Mg(2+) is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated Lhr-Core helicase, whose cited cofactor annotation reports Mg(2+) and says its ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+) stimulates only at low concentrations. This supports Mg(2+) among the listed choices.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent helicase, and general knowledge makes Mg(2+) a plausible ATPase cofactor. But that does not establish this protein's preference over Mn(2+), another listed metal.",
    "missing_item_specific_fact": "The protein-specific finding that its ATPase is most active with Mg(2+) or Ca(2+), while Mn(2+) stimulates only at low concentrations.",
    "reason": "The supplied sequence can suggest ATPase activity, but distinguishing Mg(2+) from Mn(2+) as the relevant cofactor depends on a protein-specific activity result not provided in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the annotation also reports high activity with Ca(2+), Ca(2+) is not an option; among the listed choices, Mg(2+) is supported."
  },
  "important_caveats": [
    "The cofactor evidence is a curated annotation citing a publication; the primary study was not independently reviewed here.",
    "The cited finding describes highest activity with Mg(2+) or Ca(2+), not an absolute inability to function with other ions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H4) explicitly lists Mg(2+) (ChEBI:CHEBI:18420) as the cofactor for Lhr-Core (Q88NV1), supported by direct experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018 J. Biol. Chem.). The note specifies 'ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only,' confirming Mg(2+) as the primary required cofactor. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 identical, 816 AA).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 35-40) and a Walker B-like motif 'VVVDE' (~residues 170-175), identifying the protein as a P-loop NTPase/helicase. P-loop NTPases canonically require Mg(2+) for ATP binding and hydrolysis. FAD is the cofactor of flavoprotein oxidoreductases (not NTPases); Fe(2+) is associated with iron-dependent enzymes (e.g., dioxygenases, ribonucleotide reductases) with distinct structural contexts. Mn(2+) can substitute in some NTPases but is not the canonical primary cofactor for ATP-dependent helicases. Thus, Walker A/B motif recognition → P-loop NTPase → Mg(2+) provides a concrete sequence-based biological argument distinguishing C from A, B, and D.


**Missing item-specific fact**

> The precise experimental finding that Mn(2+) 'stimulates at low concentrations only' for this specific helicase (vs. being a fully functional alternative) is an item-specific measurement. However, the general preference of P-loop NTPases for Mg(2+) over Mn(2+) is well-established textbook knowledge, so the Mg(2+) vs Mn(2+) distinction does not require memorizing this particular paper's data.


**Reason**

> The Walker A motif (GAGKTY) and Walker B motif (VVVDE) are identifiable from the raw sequence and provide a concrete structural-biological argument for classifying this as a P-loop NTPase/helicase, which canonically uses Mg(2+). This meaningfully eliminates FAD (flavoproteins) and Fe(2+) (iron-dependent enzymes). The Mg(2+) vs Mn(2+) distinction relies on the well-known general preference of ATPases for Mg(2+), not on an obscure protein-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While Mn(2+) does provide low-level stimulation for this helicase, the UniProt annotation and experimental data clearly designate Mg(2+) as the primary required cofactor. The question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is unambiguously the answer. FAD and Fe(2+) are inconsistent with the P-loop NTPase architecture evident from the sequence.


### Important caveats

- The protein identity (Lhr-Core, Q88NV1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or name.
- The UniProt entry was first publicly released in June 2025 (entry version 134 at historical cutoff); the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.
- The experimental evidence (PubMed:30224353, 2018) predates the Swiss-Prot entry creation (2025), so the underlying data existed well before the annotation was curated.
- Mn(2+) is not entirely inactive for this protein (low-concentration stimulation), but it is not the required/primary cofactor, so D is not a defensible alternative to C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 35-40) and a Walker B-like motif 'VVVDE' (~residues 170-175), identifying the protein as a P-loop NTPase/helicase. P-loop NTPases canonically require Mg(2+) for ATP binding and hydrolysis. FAD is the cofactor of flavoprotein oxidoreductases (not NTPases); Fe(2+) is associated with iron-dependent enzymes (e.g., dioxygenases, ribonucleotide reductases) with distinct structural contexts. Mn(2+) can substitute in some NTPases but is not the canonical primary cofactor for ATP-dependent helicases. Thus, Walker A/B motif recognition → P-loop NTPase → Mg(2+) provides a concrete sequence-based biological argument distinguishing C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise experimental finding that Mn(2+) 'stimulates at low concentrations only' for this specific helicase (vs. being a fully functional alternative) is an item-specific measurement. However, the general preference of P-loop NTPases for Mg(2+) over Mn(2+) is well-established textbook knowledge, so the Mg(2+) vs Mn(2+) distinction does not require memorizing this particular paper's data.",
    "reason": "The Walker A motif (GAGKTY) and Walker B motif (VVVDE) are identifiable from the raw sequence and provide a concrete structural-biological argument for classifying this as a P-loop NTPase/helicase, which canonically uses Mg(2+). This meaningfully eliminates FAD (flavoproteins) and Fe(2+) (iron-dependent enzymes). The Mg(2+) vs Mn(2+) distinction relies on the well-known general preference of ATPases for Mg(2+), not on an obscure protein-specific fact."
  },
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H4) explicitly lists Mg(2+) (ChEBI:CHEBI:18420) as the cofactor for Lhr-Core (Q88NV1), supported by direct experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018 J. Biol. Chem.). The note specifies 'ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only,' confirming Mg(2+) as the primary required cofactor. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 identical, 816 AA)."
  },
  "important_caveats": [
    "The protein identity (Lhr-Core, Q88NV1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or name.",
    "The UniProt entry was first publicly released in June 2025 (entry version 134 at historical cutoff); the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.",
    "The experimental evidence (PubMed:30224353, 2018) predates the Swiss-Prot entry creation (2025), so the underlying data existed well before the annotation was curated.",
    "Mn(2+) is not entirely inactive for this protein (low-concentration stimulation), but it is not the required/primary cofactor, so D is not a defensible alternative to C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Mn(2+) does provide low-level stimulation for this helicase, the UniProt annotation and experimental data clearly designate Mg(2+) as the primary required cofactor. The question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is unambiguously the answer. FAD and Fe(2+) are inconsistent with the P-loop NTPase architecture evident from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H4) explicitly lists Mg(2+) (ChEBI:CHEBI:18420) as the cofactor for Lhr-Core (Q88NV1), supported by direct experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018 J. Biol. Chem.). The note specifies 'ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only,' confirming Mg(2+) as the primary required cofactor. The sequence in the benchmark matches the UniProt entry exactly (SHA-256 identical, 816 AA).",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Walker A (P-loop) motif 'GAGKTY' (~residues 35-40) and a Walker B-like motif 'VVVDE' (~residues 170-175), identifying the protein as a P-loop NTPase/helicase. P-loop NTPases canonically require Mg(2+) for ATP binding and hydrolysis. FAD is the cofactor of flavoprotein oxidoreductases (not NTPases); Fe(2+) is associated with iron-dependent enzymes (e.g., dioxygenases, ribonucleotide reductases) with distinct structural contexts. Mn(2+) can substitute in some NTPases but is not the canonical primary cofactor for ATP-dependent helicases. Thus, Walker A/B motif recognition → P-loop NTPase → Mg(2+) provides a concrete sequence-based biological argument distinguishing C from A, B, and D.",
    "missing_item_specific_fact": "The precise experimental finding that Mn(2+) 'stimulates at low concentrations only' for this specific helicase (vs. being a fully functional alternative) is an item-specific measurement. However, the general preference of P-loop NTPases for Mg(2+) over Mn(2+) is well-established textbook knowledge, so the Mg(2+) vs Mn(2+) distinction does not require memorizing this particular paper's data.",
    "reason": "The Walker A motif (GAGKTY) and Walker B motif (VVVDE) are identifiable from the raw sequence and provide a concrete structural-biological argument for classifying this as a P-loop NTPase/helicase, which canonically uses Mg(2+). This meaningfully eliminates FAD (flavoproteins) and Fe(2+) (iron-dependent enzymes). The Mg(2+) vs Mn(2+) distinction relies on the well-known general preference of ATPases for Mg(2+), not on an obscure protein-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Mn(2+) does provide low-level stimulation for this helicase, the UniProt annotation and experimental data clearly designate Mg(2+) as the primary required cofactor. The question asks for 'the specific cofactor required for catalytic activity,' and Mg(2+) is unambiguously the answer. FAD and Fe(2+) are inconsistent with the P-loop NTPase architecture evident from the sequence."
  },
  "important_caveats": [
    "The protein identity (Lhr-Core, Q88NV1) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without accession or name.",
    "The UniProt entry was first publicly released in June 2025 (entry version 134 at historical cutoff); the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.",
    "The experimental evidence (PubMed:30224353, 2018) predates the Swiss-Prot entry creation (2025), so the underlying data existed well before the annotation was curated.",
    "Mn(2+) is not entirely inactive for this protein (low-concentration stimulation), but it is not the required/primary cofactor, so D is not a defensible alternative to C."
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

**Accession:** `Q88NV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 134. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000269","id":"30224353","source":"PubMed"}],"name":"Mg(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30224353","source":"PubMed"}],"value":"ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+); Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only."}]}}
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
{"citation":{"authors":["Ejaz A.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"30224353"},{"database":"DOI","id":"10.1074/jbc.ra118.005296"}],"citationType":"journal article","firstPage":"17491","id":"30224353","journal":"J. Biol. Chem.","lastPage":"17504","publicationDate":"2018","title":"Characterization of Lhr-Core DNA helicase and manganese- dependent DNA nuclease components of a bacterial gene cluster encoding nucleic acid repair enzymes.","volume":"293"},"referenceComments":[{"type":"STRAIN","value":"ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440"}],"referenceNumber":2,"referencePositions":["FUNCTION AS A HELICASE","FUNCTION AS AN ATPASE","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)  
**Locator:** `lines 32-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 134 / 1.  
**Retrieved:** 2026-11-02T04:32:03.031844+00:00.  

```text
RN   [2]
RP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, COFACTOR, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440;
RX   PubMed=30224353; DOI=10.1074/jbc.ra118.005296;
RA   Ejaz A., Shuman S.;
RT   "Characterization of Lhr-Core DNA helicase and manganese- dependent DNA
RT   nuclease components of a bacterial gene cluster encoding nucleic acid
RT   repair enzymes.";
RL   J. Biol. Chem. 293:17491-17504(2018).
```

Source SHA-256: `abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 134 / 1.  
**Retrieved:** 2026-11-02T04:32:03.031844+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000269|PubMed:30224353};
CC       Note=ssDNA-stimulated ATPase is most active with Mg(2+) or Ca(2+);
CC       Mn(2+), Co(2+), Ni(2+) and Zn(2+) stimulate at low concentrations only.
CC       {ECO:0000269|PubMed:30224353};
```

Source SHA-256: `abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
