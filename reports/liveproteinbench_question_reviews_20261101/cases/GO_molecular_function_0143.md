# GO_molecular_function_0143

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — transferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSANTGKPARHYLISYPRTASNLLLKILALDSQPNFSSGGFDGGYFFMPADDILTDPRIRVRARSISDWTADERAQLKETFQACFEAQQRWLESAESQGQSVFVKEHTVFFADPTARSCLQFGPSATSEPAWTVEYAGGSTHSKLNITVLPDEFLLTWLPTFLIRHPALAFPSLYRTVIKREGKESAAADNFASLLTTVEWSRSLYDFYVQNRESLPCSPDQRLEWPIVLDADDIIAHPATVTLYCDKIGMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD

[Multiple Choices]
A. UMP/dUMP kinase activity
B. protein binding involved in heterotypic cell-cell adhesion
C. transferase activity
D. glucose-6-phosphate isomerase activity
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

> The sequence-matched UniProt record identifies the protein as sulfotransferase ppzF (EC 2.8.2.-), a transferase. Its annotation supports the broad transferase activity in choice C, though ppzF's specific pathway role is noted as undetermined.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [C4](#evidence-c4), [C5](#evidence-c5), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble enzyme-sized protein, but those features do not meaningfully distinguish a sulfotransferase from the other enzyme choices. Identifying a relevant family or homolog from the sequence would require protein-specific recognition or computational analysis, not a clear argument from the supplied context.


**Missing item-specific fact**

> The protein's identity or family as sulfotransferase ppzF, or equivalent evidence for its sulfotransferase activity, is absent from the input.


**Reason**

> The reviewer-only annotation supports C, but it was not supplied to the model. The sequence and choices alone do not provide a reliable, concrete basis for identifying this particular transferase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is broad and includes transferases, but the protein-specific evidence supports sulfotransferase activity, not UMP/dUMP kinase activity. The broad category's overlap with kinase activity does not make A a defensible function for this protein.


### Important caveats

- The matched UniProt annotation includes computationally transferred and literature-backed evidence; the exact experimental basis was not independently reviewed here.
- The annotation says ppzF's role within the pyrrolopyrazine biosynthesis pathway remains undetermined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble enzyme-sized protein, but those features do not meaningfully distinguish a sulfotransferase from the other enzyme choices. Identifying a relevant family or homolog from the sequence would require protein-specific recognition or computational analysis, not a clear argument from the supplied context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or family as sulfotransferase ppzF, or equivalent evidence for its sulfotransferase activity, is absent from the input.",
    "reason": "The reviewer-only annotation supports C, but it was not supplied to the model. The sequence and choices alone do not provide a reliable, concrete basis for identifying this particular transferase."
  },
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "C4",
      "C5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as sulfotransferase ppzF (EC 2.8.2.-), a transferase. Its annotation supports the broad transferase activity in choice C, though ppzF's specific pathway role is noted as undetermined."
  },
  "important_caveats": [
    "The matched UniProt annotation includes computationally transferred and literature-backed evidence; the exact experimental basis was not independently reviewed here.",
    "The annotation says ppzF's role within the pyrrolopyrazine biosynthesis pathway remains undetermined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is broad and includes transferases, but the protein-specific evidence supports sulfotransferase activity, not UMP/dUMP kinase activity. The broad category's overlap with kinase activity does not make A a defensible function for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as sulfotransferase ppzF (EC 2.8.2.-), a transferase. Its annotation supports the broad transferase activity in choice C, though ppzF's specific pathway role is noted as undetermined.",
    "evidence_ids": ["H4", "H5", "C4", "C5", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble enzyme-sized protein, but those features do not meaningfully distinguish a sulfotransferase from the other enzyme choices. Identifying a relevant family or homolog from the sequence would require protein-specific recognition or computational analysis, not a clear argument from the supplied context.",
    "missing_item_specific_fact": "The protein's identity or family as sulfotransferase ppzF, or equivalent evidence for its sulfotransferase activity, is absent from the input.",
    "reason": "The reviewer-only annotation supports C, but it was not supplied to the model. The sequence and choices alone do not provide a reliable, concrete basis for identifying this particular transferase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is broad and includes transferases, but the protein-specific evidence supports sulfotransferase activity, not UMP/dUMP kinase activity. The broad category's overlap with kinase activity does not make A a defensible function for this protein."
  },
  "important_caveats": [
    "The matched UniProt annotation includes computationally transferred and literature-backed evidence; the exact experimental basis was not independently reviewed here.",
    "The annotation says ppzF's role within the pyrrolopyrazine biosynthesis pathway remains undetermined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A455ZLR3, PPZF_METMF) annotates this protein as Sulfotransferase ppzF with EC 2.8.2.-, which falls under EC class 2 (transferases). The GO annotation GO:0016740 (transferase activity) is directly assigned with evidence code IEA:UniProtKB-KW. The GO definition of transferase activity explicitly covers EC class 2 enzymes. Sulfotransferases catalyze transfer of a sulfuryl group from PAPS to an acceptor, which is a group-transfer reaction. The answer is consistent with the protein's assigned EC number and recommended name. Note that the annotation is IEA (inferred from electronic annotation/keyword), not experimentally derived, but it is consistent with the protein's identity as a sulfotransferase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable sulfotransferase signature region: the 'RARS' motif at approximately positions 52-55 (DPRIRVRARSISDW), which corresponds to the well-known 51RARS sulfotransferase family signature. The broader region (~positions 50-340) shows characteristics of the sulfotransferase fold (conserved 51RARS motif, PAPS-binding residues, and the characteristic helical structure). This positively identifies the protein as a member of the sulfotransferase superfamily (EC 2.8.2.-), which is a subclass of transferases (EC class 2). Additionally, the sequence lacks TIM-barrel catalytic residues characteristic of glucose-6-phosphate isomerase (option D), lacks P-loop/nucleotide-binding motifs of UMP/dUMP kinase (option A), and lacks immunoglobulin, cadherin, or FN3 domain features expected for cell-cell adhesion proteins (option B).


**Missing item-specific fact**

> None strictly missing, though recognition of the degenerate 51RARS sulfotransferase signature requires specialized protein-family knowledge. A model unfamiliar with this motif would rely primarily on elimination of the other three options.


**Reason**

> The sulfotransferase signature (51RARS) is a general protein-family motif, not an item-specific annotation. Recognizing it is analogous to recognizing a kinase P-loop or a zinc finger — a form of general protein-structure knowledge. The sequence positively supports 'transferase' via this motif, and the other three options can be excluded by absence of their characteristic structural features. However, the identification requires somewhat specialized knowledge of the sulfotransferase family signature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive and belong to different enzyme/binding categories (nucleotide kinase, cell-adhesion binding, transferase, isomerase). The sulfotransferase identity clearly places the protein in the transferase category. No other option is defensible for a sulfotransferase.


### Important caveats

- The GO annotation GO:0016740 carries evidence code IEA (Inferred from Electronic Annotation), meaning it is keyword-derived rather than experimentally verified. The protein's role in the ppz pathway 'has still to be determined' per PubMed:38578094.
- The EC number 2.8.2.- has a wildcard suffix, indicating the exact acceptor substrate is not yet characterized. The 'transferase' classification is based on family assignment and partial experimental data.
- The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.
- The question asks for 'primary molecular function' — a more specific answer would be 'sulfotransferase activity' (GO:0016407), but among the given options, 'transferase activity' is the correct parent term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable sulfotransferase signature region: the 'RARS' motif at approximately positions 52-55 (DPRIRVRARSISDW), which corresponds to the well-known 51RARS sulfotransferase family signature. The broader region (~positions 50-340) shows characteristics of the sulfotransferase fold (conserved 51RARS motif, PAPS-binding residues, and the characteristic helical structure). This positively identifies the protein as a member of the sulfotransferase superfamily (EC 2.8.2.-), which is a subclass of transferases (EC class 2). Additionally, the sequence lacks TIM-barrel catalytic residues characteristic of glucose-6-phosphate isomerase (option D), lacks P-loop/nucleotide-binding motifs of UMP/dUMP kinase (option A), and lacks immunoglobulin, cadherin, or FN3 domain features expected for cell-cell adhesion proteins (option B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly missing, though recognition of the degenerate 51RARS sulfotransferase signature requires specialized protein-family knowledge. A model unfamiliar with this motif would rely primarily on elimination of the other three options.",
    "reason": "The sulfotransferase signature (51RARS) is a general protein-family motif, not an item-specific annotation. Recognizing it is analogous to recognizing a kinase P-loop or a zinc finger — a form of general protein-structure knowledge. The sequence positively supports 'transferase' via this motif, and the other three options can be excluded by absence of their characteristic structural features. However, the identification requires somewhat specialized knowledge of the sulfotransferase family signature."
  },
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZLR3, PPZF_METMF) annotates this protein as Sulfotransferase ppzF with EC 2.8.2.-, which falls under EC class 2 (transferases). The GO annotation GO:0016740 (transferase activity) is directly assigned with evidence code IEA:UniProtKB-KW. The GO definition of transferase activity explicitly covers EC class 2 enzymes. Sulfotransferases catalyze transfer of a sulfuryl group from PAPS to an acceptor, which is a group-transfer reaction. The answer is consistent with the protein's assigned EC number and recommended name. Note that the annotation is IEA (inferred from electronic annotation/keyword), not experimentally derived, but it is consistent with the protein's identity as a sulfotransferase."
  },
  "important_caveats": [
    "The GO annotation GO:0016740 carries evidence code IEA (Inferred from Electronic Annotation), meaning it is keyword-derived rather than experimentally verified. The protein's role in the ppz pathway 'has still to be determined' per PubMed:38578094.",
    "The EC number 2.8.2.- has a wildcard suffix, indicating the exact acceptor substrate is not yet characterized. The 'transferase' classification is based on family assignment and partial experimental data.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.",
    "The question asks for 'primary molecular function' — a more specific answer would be 'sulfotransferase activity' (GO:0016407), but among the given options, 'transferase activity' is the correct parent term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and belong to different enzyme/binding categories (nucleotide kinase, cell-adhesion binding, transferase, isomerase). The sulfotransferase identity clearly places the protein in the transferase category. No other option is defensible for a sulfotransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZLR3, PPZF_METMF) annotates this protein as Sulfotransferase ppzF with EC 2.8.2.-, which falls under EC class 2 (transferases). The GO annotation GO:0016740 (transferase activity) is directly assigned with evidence code IEA:UniProtKB-KW. The GO definition of transferase activity explicitly covers EC class 2 enzymes. Sulfotransferases catalyze transfer of a sulfuryl group from PAPS to an acceptor, which is a group-transfer reaction. The answer is consistent with the protein's assigned EC number and recommended name. Note that the annotation is IEA (inferred from electronic annotation/keyword), not experimentally derived, but it is consistent with the protein's identity as a sulfotransferase.",
    "evidence_ids": ["C4", "C5", "H1", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable sulfotransferase signature region: the 'RARS' motif at approximately positions 52-55 (DPRIRVRARSISDW), which corresponds to the well-known 51RARS sulfotransferase family signature. The broader region (~positions 50-340) shows characteristics of the sulfotransferase fold (conserved 51RARS motif, PAPS-binding residues, and the characteristic helical structure). This positively identifies the protein as a member of the sulfotransferase superfamily (EC 2.8.2.-), which is a subclass of transferases (EC class 2). Additionally, the sequence lacks TIM-barrel catalytic residues characteristic of glucose-6-phosphate isomerase (option D), lacks P-loop/nucleotide-binding motifs of UMP/dUMP kinase (option A), and lacks immunoglobulin, cadherin, or FN3 domain features expected for cell-cell adhesion proteins (option B).",
    "missing_item_specific_fact": "None strictly missing, though recognition of the degenerate 51RARS sulfotransferase signature requires specialized protein-family knowledge. A model unfamiliar with this motif would rely primarily on elimination of the other three options.",
    "reason": "The sulfotransferase signature (51RARS) is a general protein-family motif, not an item-specific annotation. Recognizing it is analogous to recognizing a kinase P-loop or a zinc finger — a form of general protein-structure knowledge. The sequence positively supports 'transferase' via this motif, and the other three options can be excluded by absence of their characteristic structural features. However, the identification requires somewhat specialized knowledge of the sulfotransferase family signature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and belong to different enzyme/binding categories (nucleotide kinase, cell-adhesion binding, transferase, isomerase). The sulfotransferase identity clearly places the protein in the transferase category. No other option is defensible for a sulfotransferase."
  },
  "important_caveats": [
    "The GO annotation GO:0016740 carries evidence code IEA (Inferred from Electronic Annotation), meaning it is keyword-derived rather than experimentally verified. The protein's role in the ppz pathway 'has still to be determined' per PubMed:38578094.",
    "The EC number 2.8.2.- has a wildcard suffix, indicating the exact acceptor substrate is not yet characterized. The 'transferase' classification is based on family assignment and partial experimental data.",
    "The sequence match is confirmed (SHA256 identical between benchmark and UniProt entry), so the annotation applies to the exact sequence presented.",
    "The question asks for 'primary molecular function' — a more specific answer would be 'sulfotransferase activity' (GO:0016407), but among the given options, 'transferase activity' is the correct parent term."
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

**Accession:** `A0A455ZLR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 10. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Pyrrolopyrazine biosynthesis cluster protein F"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30452111","source":"PubMed"}],"value":"2.8.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30452111","source":"PubMed"}],"value":"Sulfotransferase ppzF"}}}
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:16.946847+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4H424","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30452111","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38578094","source":"PubMed"}],"value":"Sulfotransferase; part of the gene cluster that mediates the biosynthesis of pyrrolopyrazines, secondary metabolites showing insecticidal activity (PubMed:30452111, PubMed:38578094). The role of ppzF within the pathway has still to be determined (PubMed:38578094). The single multifunctional NRPS ppzA is sufficient to produce peramine via condensation of 1-pyrroline-5-carboxylate and arginine, N-methylation of the alpha-amino group of arginine and reduction of the thioester and the cyclization to form an iminium ion resulting in release from the peptide synthetase. Deprotonation of this intermediate and oxidation of the pyrroline ring would give rise to peramine (By similarity). In Epichloe species that produce only peramine, the peramine synthetase gene is not localized in a gene cluster, in contrast to Metarhizium species that contain additional pyrrolopyrazine biosynthesis genes. The 2-oxoglutarate-Fe(II) type oxidoreductase ppzC hydroxylates peramine to yield the newly identified compound 8-hydroxyperamine whereas ppzD converts L-proline into trans-4-hydroxy-L-proline, a precursor of peramine biosynthesis (PubMed:38578094)"}]}
```

Source SHA-256: `4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-02T04:25:19.015576+00:00.  

```text
ID   PPZF_METMF              Reviewed;         340 AA.
AC   A0A455ZLR3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   09-APR-2025, entry version 10.
DE   RecName: Full=Sulfotransferase ppzF {ECO:0000303|PubMed:30452111};
DE            EC=2.8.2.- {ECO:0000305|PubMed:30452111};
DE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein F {ECO:0000303|PubMed:30452111};
GN   Name=ppzF {ECO:0000303|PubMed:30452111};
OS   Metarhizium majus (strain ARSEF 297).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;
OC   Metarhizium majus.
OX   NCBI_TaxID=1276143;
```

Source SHA-256: `ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)  
**Locator:** `lines 31-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-02T04:25:19.015576+00:00.  

```text
CC   -!- FUNCTION: Sulfotransferase; part of the gene cluster that mediates the
CC       biosynthesis of pyrrolopyrazines, secondary metabolites showing
CC       insecticidal activity (PubMed:30452111, PubMed:38578094). The role of
CC       ppzF within the pathway has still to be determined (PubMed:38578094).
CC       The single multifunctional NRPS ppzA is sufficient to produce peramine
CC       via condensation of 1-pyrroline-5-carboxylate and arginine, N-
CC       methylation of the alpha-amino group of arginine and reduction of the
CC       thioester and the cyclization to form an iminium ion resulting in
CC       release from the peptide synthetase. Deprotonation of this intermediate
CC       and oxidation of the pyrroline ring would give rise to peramine (By
CC       similarity). In Epichloe species that produce only peramine, the
CC       peramine synthetase gene is not localized in a gene cluster, in
CC       contrast to Metarhizium species that contain additional pyrrolopyrazine
CC       biosynthesis genes. The 2-oxoglutarate-Fe(II) type oxidoreductase ppzC
CC       hydroxylates peramine to yield the newly identified compound 8-
CC       hydroxyperamine whereas ppzD converts L-proline into trans-4-hydroxy-L-
CC       proline, a precursor of peramine biosynthesis (PubMed:38578094).
CC       {ECO:0000250|UniProtKB:Q4H424, ECO:0000269|PubMed:30452111,
CC       ECO:0000269|PubMed:38578094}.
```

Source SHA-256: `ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-02T04:25:19.015576+00:00.  

```text
DR   GO; GO:0016740; F:transferase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 129652-129675`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016740
name: transferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a group, e.g. a methyl group, glycosyl group, acyl group, phosphorus-containing, or other groups, from one compound (generally regarded as the donor) to another compound (generally regarded as the acceptor). Transferase is the systematic name for any enzyme of EC class 2." [EC:2.-.-.-]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_prokaryote
subset: goslim_yeast
xref: EC:2.-.-.-
xref: Reactome:R-HSA-1483089 "PE is converted to PS by PTDSS2"
xref: Reactome:R-HSA-1483186 "PC is converted to PS by PTDSS1"
xref: Reactome:R-HSA-5333607 "GSSeH combines with bGalNAc derivative to form GSSebGalNac"
xref: Reactome:R-HSA-5668414 "TRAF2 ubiquitinates cIAP1,2 in cIAP1,2:TRAF1:TRAF2:TRAF3:NIK"
xref: Reactome:R-HSA-8868783 "TSR3 transfers aminocarboxypropyl group from S-adenosylmethionine to N(1)-methylpseudouridine-1248 of 18SE rRNA yielding N(1)-methyl-N(3)-aminocarboxypropylpseudouridine-1248"
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:2.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
