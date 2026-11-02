# cofactor_0069

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVAHVALPVPLPRTFDYLLPEGMAVKAGCRVRVPFGKQERIGIVAAVSERSELPLDELKPVAEALDDEPVFSTTVWRLLMWAAEYYHHPIGDVLFHALPVMLRQGKPASATPLWYWFATEQGQVVDLNGLKRSRKQQQALAALRQGKIWRHQVGELEFNEAALQALRGKGLAELACEAPALTDWRSAYSVAGERLRLNTEQATAVGAIHSAADRFSAWLLAGITGSGKTEVYLSVLENVLAQGRQALVMVPEIGLTPQTIARFRQRFNAPVEVLHSGLNDSERLSAWLKAKNGEAAIVIGTRSSLFTPFKDLGVIVIDEEHDSSYKQQEGWRYHARDLAVWRAHSEQIPIILGSATPALETLHNVRQGKYRQLTLSKRAGNARPAQQHVLDLKGQPLQAGLSPALISRMRQHLQADNQVILFLNRRGFAPALLCHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCGSTHLVPVGIGTEQLEQALAPLFPEVPISRIDRDTTSRKGALEEHLAAVHRGGARILIGTQMLAKGHHFPDVTLVSLLDVDGALFSADFRSAERFAQLYTQVSGRAGRAGKQGEVILQTHHPEHPLLQTLLYKGYDAFAEQALAERQTMQLPPWTSHVLIRAEDHNNQQAPLFLQQLRNLLQASPLADEKLWVLGPVPALAPKRGGRWRWQILLQHPSRVRLQHIVSGTLALINTLPEARKVKWVLDVDPIEG

[Multiple Choices]
A. Zn(2+)
B. Co(2+)
C. Mg(2+)
D. tungstopterin
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

> The exact-matching UniProt record annotates Zn(2+) as a cofactor and says the protein binds two zinc ions per subunit; the cited structure includes Zn(2+). This supports Zn binding and the database cofactor assignment, though the excerpts do not independently establish that zinc is indispensable specifically for ATP hydrolysis.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a P-loop-like ATPase motif and a Cys/His-rich region, which suggest nucleotide-dependent activity and metal binding, respectively. Those clues do not establish which ion the question intends as the required catalytic cofactor.


**Missing item-specific fact**

> The protein-specific evidence that PriA binds two Zn(2+) ions per subunit, and whether those ions are required for catalytic activity rather than serving another functional or structural role.


**Reason**

> Identifying zinc as the annotated cofactor depends on protein-specific annotation or experimental evidence not supplied with the sequence. General ATPase knowledge also makes Mg(2+) plausible for ATP hydrolysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Zn(2+) is supported as a bound, annotated cofactor. However, the question specifically asks about catalytic activity, and PriA is an ATPase for which Mg(2+) is also a plausible catalytic ion. The supplied excerpts do not clarify whether the intended answer is the annotated zinc or the ion supporting ATP hydrolysis.


### Important caveats

- The sequence match and source annotations support Zn binding, but a bound cofactor is not by itself proof that it is essential for catalytic turnover.
- The supplied reviewer evidence is not information available to the model answering the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop-like ATPase motif and a Cys/His-rich region, which suggest nucleotide-dependent activity and metal binding, respectively. Those clues do not establish which ion the question intends as the required catalytic cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that PriA binds two Zn(2+) ions per subunit, and whether those ions are required for catalytic activity rather than serving another functional or structural role.",
    "reason": "Identifying zinc as the annotated cofactor depends on protein-specific annotation or experimental evidence not supplied with the sequence. General ATPase knowledge also makes Mg(2+) plausible for ATP hydrolysis."
  },
  "case_id": "cofactor_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates Zn(2+) as a cofactor and says the protein binds two zinc ions per subunit; the cited structure includes Zn(2+). This supports Zn binding and the database cofactor assignment, though the excerpts do not independently establish that zinc is indispensable specifically for ATP hydrolysis."
  },
  "important_caveats": [
    "The sequence match and source annotations support Zn binding, but a bound cofactor is not by itself proof that it is essential for catalytic turnover.",
    "The supplied reviewer evidence is not information available to the model answering the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Zn(2+) is supported as a bound, annotated cofactor. However, the question specifically asks about catalytic activity, and PriA is an ATPase for which Mg(2+) is also a plausible catalytic ion. The supplied excerpts do not clarify whether the intended answer is the annotated zinc or the ion supporting ATP hydrolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates Zn(2+) as a cofactor and says the protein binds two zinc ions per subunit; the cited structure includes Zn(2+). This supports Zn binding and the database cofactor assignment, though the excerpts do not independently establish that zinc is indispensable specifically for ATP hydrolysis.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a P-loop-like ATPase motif and a Cys/His-rich region, which suggest nucleotide-dependent activity and metal binding, respectively. Those clues do not establish which ion the question intends as the required catalytic cofactor.",
    "missing_item_specific_fact": "The protein-specific evidence that PriA binds two Zn(2+) ions per subunit, and whether those ions are required for catalytic activity rather than serving another functional or structural role.",
    "reason": "Identifying zinc as the annotated cofactor depends on protein-specific annotation or experimental evidence not supplied with the sequence. General ATPase knowledge also makes Mg(2+) plausible for ATP hydrolysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Zn(2+) is supported as a bound, annotated cofactor. However, the question specifically asks about catalytic activity, and PriA is an ATPase for which Mg(2+) is also a plausible catalytic ion. The supplied excerpts do not clarify whether the intended answer is the annotated zinc or the ion supporting ATP hydrolysis."
  },
  "important_caveats": [
    "The sequence match and source annotations support Zn binding, but a bound cofactor is not by itself proof that it is essential for catalytic turnover.",
    "The supplied reviewer evidence is not information available to the model answering the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry A6TGC5 (PriA, Klebsiella pneumoniae) explicitly annotates Zn(2+) as the cofactor with evidence codes ECO:0000255 (HAMAP-Rule MF_00983), ECO:0000269 (PubMed:24379377), and ECO:0007744 (PDB:4NL4). The note states 'Binds 2 zinc ions per subunit.' The X-ray crystallography reference (2.65 Å, complex with ADP and Zn(2+)) provides direct structural evidence. The sequence SHA256 matches exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains prominent Cys/His clusters (e.g., 'CHDCGWIAECPRCDSYY', 'RCHHCDSQRPIPRQCPSC') suggestive of zinc coordination, and tungstopterin (anaerobic oxidoreductases) and Co(2+) (rare in bacteria) can be eliminated by general knowledge. However, the Walker A/B motifs clearly indicate an ATPase/helicase, for which Mg(2+) is the canonical catalytic cofactor for ATP hydrolysis. Distinguishing Zn(2+) as 'the' cofactor rather than Mg(2+) requires specific knowledge that PriA's defining metal cofactor (per HAMAP rule MF_00983 and structural studies) is zinc, not the generic Mg-ATP requirement.


**Missing item-specific fact**

> The specific biochemical fact that PriA's annotated cofactor is Zn(2+) (structural zinc-binding domain) rather than Mg(2+) (ATPase cofactor), as assigned by HAMAP rule MF_00983 and confirmed by PDB 4NL4. Without this, a knowledgeable biologist could reasonably select Mg(2+) as the catalytic cofactor for ATP hydrolysis.


**Reason**

> While zinc-binding Cys/His motifs are visible in the sequence, the choice between Zn(2+) and Mg(2+) as 'the' cofactor for an ATP-dependent helicase cannot be definitively resolved from sequence features alone. Mg(2+) is universally required for ATP hydrolysis in helicases, making it a defensible alternative. The specific assignment of Zn(2+) as THE cofactor (over Mg(2+)) is a database annotation convention specific to PriA.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (Zn(2+))",
  "C (Mg(2+))"
]
```

> Mg(2+) is required for ATP hydrolysis in all P-loop helicases and is arguably 'required for catalytic activity.' The UniProt entry lists only Zn(2+) as the cofactor (not Mg(2+)), but from a biochemical standpoint, Mg-ATP is essential for PriA's helicase function. The question's phrasing 'specific cofactor required for catalytic activity' could reasonably point to Mg(2+) for the ATPase step, while Zn(2+) is more structural. The database convention resolves this in favor of Zn(2+), but the wording does not clearly exclude Mg(2+).


### Important caveats

- The Zn(2+) cofactor annotation carries HAMAP-Rule evidence (ECO:0000255, computational/curatorial) in addition to experimental evidence (PubMed:24379377, PDB:4NL4). The HAMAP rule is a family-level assignment transferred to this entry.
- The sequence match is exact (SHA256 identical), confirming the protein is PriA from K. pneumoniae MGH 78578.
- Mg(2+) is not annotated as a cofactor in this UniProt entry, but its requirement for ATP hydrolysis is biochemically universal for P-loop helicases.
- The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains prominent Cys/His clusters (e.g., 'CHDCGWIAECPRCDSYY', 'RCHHCDSQRPIPRQCPSC') suggestive of zinc coordination, and tungstopterin (anaerobic oxidoreductases) and Co(2+) (rare in bacteria) can be eliminated by general knowledge. However, the Walker A/B motifs clearly indicate an ATPase/helicase, for which Mg(2+) is the canonical catalytic cofactor for ATP hydrolysis. Distinguishing Zn(2+) as 'the' cofactor rather than Mg(2+) requires specific knowledge that PriA's defining metal cofactor (per HAMAP rule MF_00983 and structural studies) is zinc, not the generic Mg-ATP requirement.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific biochemical fact that PriA's annotated cofactor is Zn(2+) (structural zinc-binding domain) rather than Mg(2+) (ATPase cofactor), as assigned by HAMAP rule MF_00983 and confirmed by PDB 4NL4. Without this, a knowledgeable biologist could reasonably select Mg(2+) as the catalytic cofactor for ATP hydrolysis.",
    "reason": "While zinc-binding Cys/His motifs are visible in the sequence, the choice between Zn(2+) and Mg(2+) as 'the' cofactor for an ATP-dependent helicase cannot be definitively resolved from sequence features alone. Mg(2+) is universally required for ATP hydrolysis in helicases, making it a defensible alternative. The specific assignment of Zn(2+) as THE cofactor (over Mg(2+)) is a database annotation convention specific to PriA."
  },
  "case_id": "cofactor_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A6TGC5 (PriA, Klebsiella pneumoniae) explicitly annotates Zn(2+) as the cofactor with evidence codes ECO:0000255 (HAMAP-Rule MF_00983), ECO:0000269 (PubMed:24379377), and ECO:0007744 (PDB:4NL4). The note states 'Binds 2 zinc ions per subunit.' The X-ray crystallography reference (2.65 Å, complex with ADP and Zn(2+)) provides direct structural evidence. The sequence SHA256 matches exactly."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries HAMAP-Rule evidence (ECO:0000255, computational/curatorial) in addition to experimental evidence (PubMed:24379377, PDB:4NL4). The HAMAP rule is a family-level assignment transferred to this entry.",
    "The sequence match is exact (SHA256 identical), confirming the protein is PriA from K. pneumoniae MGH 78578.",
    "Mg(2+) is not annotated as a cofactor in this UniProt entry, but its requirement for ATP hydrolysis is biochemically universal for P-loop helicases.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (Zn(2+))",
      "C (Mg(2+))"
    ],
    "reason": "Mg(2+) is required for ATP hydrolysis in all P-loop helicases and is arguably 'required for catalytic activity.' The UniProt entry lists only Zn(2+) as the cofactor (not Mg(2+)), but from a biochemical standpoint, Mg-ATP is essential for PriA's helicase function. The question's phrasing 'specific cofactor required for catalytic activity' could reasonably point to Mg(2+) for the ATPase step, while Zn(2+) is more structural. The database convention resolves this in favor of Zn(2+), but the wording does not clearly exclude Mg(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A6TGC5 (PriA, Klebsiella pneumoniae) explicitly annotates Zn(2+) as the cofactor with evidence codes ECO:0000255 (HAMAP-Rule MF_00983), ECO:0000269 (PubMed:24379377), and ECO:0007744 (PDB:4NL4). The note states 'Binds 2 zinc ions per subunit.' The X-ray crystallography reference (2.65 Å, complex with ADP and Zn(2+)) provides direct structural evidence. The sequence SHA256 matches exactly.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains prominent Cys/His clusters (e.g., 'CHDCGWIAECPRCDSYY', 'RCHHCDSQRPIPRQCPSC') suggestive of zinc coordination, and tungstopterin (anaerobic oxidoreductases) and Co(2+) (rare in bacteria) can be eliminated by general knowledge. However, the Walker A/B motifs clearly indicate an ATPase/helicase, for which Mg(2+) is the canonical catalytic cofactor for ATP hydrolysis. Distinguishing Zn(2+) as 'the' cofactor rather than Mg(2+) requires specific knowledge that PriA's defining metal cofactor (per HAMAP rule MF_00983 and structural studies) is zinc, not the generic Mg-ATP requirement.",
    "missing_item_specific_fact": "The specific biochemical fact that PriA's annotated cofactor is Zn(2+) (structural zinc-binding domain) rather than Mg(2+) (ATPase cofactor), as assigned by HAMAP rule MF_00983 and confirmed by PDB 4NL4. Without this, a knowledgeable biologist could reasonably select Mg(2+) as the catalytic cofactor for ATP hydrolysis.",
    "reason": "While zinc-binding Cys/His motifs are visible in the sequence, the choice between Zn(2+) and Mg(2+) as 'the' cofactor for an ATP-dependent helicase cannot be definitively resolved from sequence features alone. Mg(2+) is universally required for ATP hydrolysis in helicases, making it a defensible alternative. The specific assignment of Zn(2+) as THE cofactor (over Mg(2+)) is a database annotation convention specific to PriA."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (Zn(2+))", "C (Mg(2+))"],
    "reason": "Mg(2+) is required for ATP hydrolysis in all P-loop helicases and is arguably 'required for catalytic activity.' The UniProt entry lists only Zn(2+) as the cofactor (not Mg(2+)), but from a biochemical standpoint, Mg-ATP is essential for PriA's helicase function. The question's phrasing 'specific cofactor required for catalytic activity' could reasonably point to Mg(2+) for the ATPase step, while Zn(2+) is more structural. The database convention resolves this in favor of Zn(2+), but the wording does not clearly exclude Mg(2+)."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries HAMAP-Rule evidence (ECO:0000255, computational/curatorial) in addition to experimental evidence (PubMed:24379377, PDB:4NL4). The HAMAP rule is a family-level assignment transferred to this entry.",
    "The sequence match is exact (SHA256 identical), confirming the protein is PriA from K. pneumoniae MGH 78578.",
    "Mg(2+) is not annotated as a cofactor in this UniProt entry, but its requirement for ATP hydrolysis is biochemically universal for P-loop helicases.",
    "The identity origin (accession inferred from dataset image-path metadata) is reviewer-only and was not available to the evaluated model."
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

**Accession:** `A6TGC5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 115. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000269","id":"24379377","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"4NL4","source":"PDB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00983","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000269","id":"24379377","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"4NL4","source":"PDB"}],"value":"Binds 2 zinc ions per subunit."}]}}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.788123+00:00.  

```json
{"citation":{"authors":["Bhattacharyya B.","George N.P.","Thurmes T.M.","Zhou R.","Jani N.","Wessel S.R.","Sandler S.J.","Ha T.","Keck J.L."],"citationCrossReferences":[{"database":"PubMed","id":"24379377"},{"database":"DOI","id":"10.1073/pnas.1318001111"}],"citationType":"journal article","firstPage":"1373","id":"24379377","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"1378","publicationDate":"2014","title":"Structural mechanisms of PriA-mediated DNA replication restart.","volume":"111"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4NL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4NL8","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 700721 / MGH 78578"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.65 ANGSTROMS) IN COMPLEX WITH ADP AND ZN(2+)","X-RAY CRYSTALLOGRAPHY (4.08 ANGSTROMS) IN COMPLEX WITH SSB","FUNCTION AS AN ATPASE","CATALYTIC ACTIVITY","DOMAIN","DNA-BINDING"]}
```

Source SHA-256: `6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)  
**Locator:** `lines 31-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:27:08.474025+00:00.  

```text
RN   [3] {ECO:0007744|PDB:4NL4, ECO:0007744|PDB:4NL8}
RP   X-RAY CRYSTALLOGRAPHY (2.65 ANGSTROMS) IN COMPLEX WITH ADP AND ZN(2+),
RP   X-RAY CRYSTALLOGRAPHY (4.08 ANGSTROMS) IN COMPLEX WITH SSB, FUNCTION AS AN
RP   ATPASE, CATALYTIC ACTIVITY, DOMAIN, AND DNA-BINDING.
RC   STRAIN=ATCC 700721 / MGH 78578;
RX   PubMed=24379377; DOI=10.1073/pnas.1318001111;
RA   Bhattacharyya B., George N.P., Thurmes T.M., Zhou R., Jani N., Wessel S.R.,
RA   Sandler S.J., Ha T., Keck J.L.;
RT   "Structural mechanisms of PriA-mediated DNA replication restart.";
RL   Proc. Natl. Acad. Sci. U.S.A. 111:1373-1378(2014).
```

Source SHA-256: `c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)  
**Locator:** `lines 71-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:27:08.474025+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_00983,
CC         ECO:0000269|PubMed:24379377, ECO:0007744|PDB:4NL4};
CC       Note=Binds 2 zinc ions per subunit. {ECO:0000255|HAMAP-Rule:MF_00983,
CC       ECO:0000269|PubMed:24379377, ECO:0007744|PDB:4NL4};
```

Source SHA-256: `c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
