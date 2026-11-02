# GO_biological_process_0005

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — NAD biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHYLDNLLLNTDSYKASHWLQYPPGTDASFFYVESRGGVYDQTAFFGLQSILKEAINRPVTHADIDDAKALLAAHGEPFNEAGWRDIVDRLGGQLPIRIRAVPEGCVVPTHNVLMTIESTDAKAFWVPSYLETLLLRVWYPVTVATVSWQVKQIVRDFLQRTSDDPEGQLPFKLHDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHTPVAGYSIPAAEHSTITSWGREREVDAYRNMLTQFARPGAIVAVVSDSYDIYRAIREHWGTTLREEIIASGATVVIRPDSGDPVDVVEQCLLLLDEAFGHQVNGKGYKVLNHVRVIQGDGINPQSLRAILERITAAGYAADNVAFGMGGALLQKVDRDTQKFALKCSAVRVDGAWIDVYKDPITDQGKQSKRGRLTLLRDRATGQYRSALLDEVATHAGDSDDALVTVWENGQMLREWTLEQVRAHADAARL

[Multiple Choices]
A. regulation of fat cell differentiation
B. NAD biosynthetic process
C. heme biosynthetic process
D. fatty acid biosynthetic process
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the cited 468-aa Xanthomonas protein. Its curated function is nicotinamide phosphoribosyltransferase, which forms an NAD biosynthesis intermediate; the function and pathway are linked to experimental evidence, while the GO annotation itself is computationally inferred.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options are biologically distinct, but the sequence alone provides no clear, generally interpretable feature that identifies this specific enzyme and its pathway.


**Missing item-specific fact**

> That this sequence encodes nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD biosynthesis.


**Reason**

> Distinguishing B requires protein-specific functional identification, such as a homolog or enzyme annotation. Reviewer-only evidence supports the key but was not provided to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The documented enzymatic function supports NAD biosynthesis; the other choices describe different processes.


### Important caveats

- The GO annotation is listed with an IEA evidence code; the curated functional description cites experimental evidence.
- The source identity and exact sequence match were established using reviewer-only information, not the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options are biologically distinct, but the sequence alone provides no clear, generally interpretable feature that identifies this specific enzyme and its pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence encodes nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD biosynthesis.",
    "reason": "Distinguishing B requires protein-specific functional identification, such as a homolog or enzyme annotation. Reviewer-only evidence supports the key but was not provided to the evaluated model."
  },
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 468-aa Xanthomonas protein. Its curated function is nicotinamide phosphoribosyltransferase, which forms an NAD biosynthesis intermediate; the function and pathway are linked to experimental evidence, while the GO annotation itself is computationally inferred."
  },
  "important_caveats": [
    "The GO annotation is listed with an IEA evidence code; the curated functional description cites experimental evidence.",
    "The source identity and exact sequence match were established using reviewer-only information, not the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The documented enzymatic function supports NAD biosynthesis; the other choices describe different processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited 468-aa Xanthomonas protein. Its curated function is nicotinamide phosphoribosyltransferase, which forms an NAD biosynthesis intermediate; the function and pathway are linked to experimental evidence, while the GO annotation itself is computationally inferred.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options are biologically distinct, but the sequence alone provides no clear, generally interpretable feature that identifies this specific enzyme and its pathway.",
    "missing_item_specific_fact": "That this sequence encodes nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD biosynthesis.",
    "reason": "Distinguishing B requires protein-specific functional identification, such as a homolog or enzyme annotation. Reviewer-only evidence supports the key but was not provided to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The documented enzymatic function supports NAD biosynthesis; the other choices describe different processes."
  },
  "important_caveats": [
    "The GO annotation is listed with an IEA evidence code; the curated functional description cites experimental evidence.",
    "The source identity and exact sequence match were established using reviewer-only information, not the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris. Experimental evidence (ECO:0000269, PubMed:38429435, supported by X-ray crystallography PDB entries 7YQO-7YQR, 8IGZ) confirms it catalyzes condensation of nicotinamide with PRPP to yield NMN, an intermediate in NAD biosynthesis via the NAM salvage pathway. The GO annotation GO:0009435 (NAD+ biosynthetic process) is present in the entry (C7, H5). The pathway comment (C6, H4) explicitly places it in 'NAD(+) biosynthesis.' The sequence match is confirmed (SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PRTase (phosphoribosyltransferase) catalytic motif 'GDSDDALVTVWENGQ' near the C-terminus, characteristic of the PRTase superfamily fold. PRTases catalyze the transfer of phosphoribosyl groups to nitrogenous bases and are hallmarks of nucleotide/cofactor biosynthesis pathways (NAD, purines, pyrimidines, histidine, tryptophan). This fold is structurally and mechanistically distinct from fatty acid biosynthetic enzymes (FAS I/II: acyl-CoA synthetases, ketoacyl synthases, enoyl reductases) and heme biosynthetic enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase), which belong to entirely different enzyme families. Additionally, option A (regulation of fat cell differentiation) describes a eukaryotic-specific transcriptional/signaling process incompatible with a ~468-aa bacterial enzyme lacking DNA-binding or protein-protein interaction domains typical of transcription factors.


**Missing item-specific fact**

> None critical. Recognizing the PRTase fold and its association with cofactor/nucleotide biosynthesis is general biochemistry knowledge. However, distinguishing NAMPT specifically from other PRTase-family members (e.g., histidine biosynthesis HisZ, tryptophan biosynthesis TrpD) from sequence alone without a trained fold predictor would require additional motif-level discrimination.


**Reason**

> The PRTase catalytic motif and the general principle that phosphoribosyltransferases participate in nucleotide/cofactor biosynthesis (not fatty acid or heme pathways) provide a concrete biological argument to select B over C and D. Option A is eliminable by structural/functional incompatibility. The reasoning chain—PRTase fold → nucleotide/cofactor biosynthesis → NAD pathway—is defensible general biological inference, though the final step from 'PRTase' to 'NAD-specific' rather than 'histidine/tryptophan-specific' PRTase adds difficulty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is incompatible with a bacterial enzyme of this architecture. Options C (heme) and D (fatty acid) involve completely different enzyme superfamilies (tetrapyrrole pathway enzymes; FAS I/II multi-domain enzymes) with no PRTase catalytic motif. Only B aligns with the PRTase fold and its canonical role in cofactor biosynthesis. No other option is defensible given the sequence features.


### Important caveats

- The GO annotation for this protein is IEA (inferred from electronic annotation via UniPathway/InterPro), but the underlying function and pathway assignment are experimentally supported (ECO:0000269, PubMed:38429435, PDB structures).
- The organism (Xanthomonas, bacterium) is not stated in the question; elimination of option A relies on recognizing the protein architecture is incompatible with eukaryotic transcriptional regulation, not on knowing the taxon.
- The PRTase fold recognition from raw sequence is a specialized but general biochemistry skill; it does not require memorizing this specific UniProt entry.
- The reviewer evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A0A0H2X5R2.
- The entry was first publicly released 2025-02-05; if the benchmark was constructed before that date, the annotation available to the original authors may have differed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PRTase (phosphoribosyltransferase) catalytic motif 'GDSDDALVTVWENGQ' near the C-terminus, characteristic of the PRTase superfamily fold. PRTases catalyze the transfer of phosphoribosyl groups to nitrogenous bases and are hallmarks of nucleotide/cofactor biosynthesis pathways (NAD, purines, pyrimidines, histidine, tryptophan). This fold is structurally and mechanistically distinct from fatty acid biosynthetic enzymes (FAS I/II: acyl-CoA synthetases, ketoacyl synthases, enoyl reductases) and heme biosynthetic enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase), which belong to entirely different enzyme families. Additionally, option A (regulation of fat cell differentiation) describes a eukaryotic-specific transcriptional/signaling process incompatible with a ~468-aa bacterial enzyme lacking DNA-binding or protein-protein interaction domains typical of transcription factors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the PRTase fold and its association with cofactor/nucleotide biosynthesis is general biochemistry knowledge. However, distinguishing NAMPT specifically from other PRTase-family members (e.g., histidine biosynthesis HisZ, tryptophan biosynthesis TrpD) from sequence alone without a trained fold predictor would require additional motif-level discrimination.",
    "reason": "The PRTase catalytic motif and the general principle that phosphoribosyltransferases participate in nucleotide/cofactor biosynthesis (not fatty acid or heme pathways) provide a concrete biological argument to select B over C and D. Option A is eliminable by structural/functional incompatibility. The reasoning chain—PRTase fold → nucleotide/cofactor biosynthesis → NAD pathway—is defensible general biological inference, though the final step from 'PRTase' to 'NAD-specific' rather than 'histidine/tryptophan-specific' PRTase adds difficulty."
  },
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein is Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris. Experimental evidence (ECO:0000269, PubMed:38429435, supported by X-ray crystallography PDB entries 7YQO-7YQR, 8IGZ) confirms it catalyzes condensation of nicotinamide with PRPP to yield NMN, an intermediate in NAD biosynthesis via the NAM salvage pathway. The GO annotation GO:0009435 (NAD+ biosynthetic process) is present in the entry (C7, H5). The pathway comment (C6, H4) explicitly places it in 'NAD(+) biosynthesis.' The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (inferred from electronic annotation via UniPathway/InterPro), but the underlying function and pathway assignment are experimentally supported (ECO:0000269, PubMed:38429435, PDB structures).",
    "The organism (Xanthomonas, bacterium) is not stated in the question; elimination of option A relies on recognizing the protein architecture is incompatible with eukaryotic transcriptional regulation, not on knowing the taxon.",
    "The PRTase fold recognition from raw sequence is a specialized but general biochemistry skill; it does not require memorizing this specific UniProt entry.",
    "The reviewer evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A0A0H2X5R2.",
    "The entry was first publicly released 2025-02-05; if the benchmark was constructed before that date, the annotation available to the original authors may have differed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is incompatible with a bacterial enzyme of this architecture. Options C (heme) and D (fatty acid) involve completely different enzyme superfamilies (tetrapyrrole pathway enzymes; FAS I/II multi-domain enzymes) with no PRTase catalytic motif. Only B aligns with the PRTase fold and its canonical role in cofactor biosynthesis. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris. Experimental evidence (ECO:0000269, PubMed:38429435, supported by X-ray crystallography PDB entries 7YQO-7YQR, 8IGZ) confirms it catalyzes condensation of nicotinamide with PRPP to yield NMN, an intermediate in NAD biosynthesis via the NAM salvage pathway. The GO annotation GO:0009435 (NAD+ biosynthetic process) is present in the entry (C7, H5). The pathway comment (C6, H4) explicitly places it in 'NAD(+) biosynthesis.' The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PRTase (phosphoribosyltransferase) catalytic motif 'GDSDDALVTVWENGQ' near the C-terminus, characteristic of the PRTase superfamily fold. PRTases catalyze the transfer of phosphoribosyl groups to nitrogenous bases and are hallmarks of nucleotide/cofactor biosynthesis pathways (NAD, purines, pyrimidines, histidine, tryptophan). This fold is structurally and mechanistically distinct from fatty acid biosynthetic enzymes (FAS I/II: acyl-CoA synthetases, ketoacyl synthases, enoyl reductases) and heme biosynthetic enzymes (ALA synthase, porphobilinogen deaminase, ferrochelatase), which belong to entirely different enzyme families. Additionally, option A (regulation of fat cell differentiation) describes a eukaryotic-specific transcriptional/signaling process incompatible with a ~468-aa bacterial enzyme lacking DNA-binding or protein-protein interaction domains typical of transcription factors.",
    "missing_item_specific_fact": "None critical. Recognizing the PRTase fold and its association with cofactor/nucleotide biosynthesis is general biochemistry knowledge. However, distinguishing NAMPT specifically from other PRTase-family members (e.g., histidine biosynthesis HisZ, tryptophan biosynthesis TrpD) from sequence alone without a trained fold predictor would require additional motif-level discrimination.",
    "reason": "The PRTase catalytic motif and the general principle that phosphoribosyltransferases participate in nucleotide/cofactor biosynthesis (not fatty acid or heme pathways) provide a concrete biological argument to select B over C and D. Option A is eliminable by structural/functional incompatibility. The reasoning chain—PRTase fold → nucleotide/cofactor biosynthesis → NAD pathway—is defensible general biological inference, though the final step from 'PRTase' to 'NAD-specific' rather than 'histidine/tryptophan-specific' PRTase adds difficulty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is incompatible with a bacterial enzyme of this architecture. Options C (heme) and D (fatty acid) involve completely different enzyme superfamilies (tetrapyrrole pathway enzymes; FAS I/II multi-domain enzymes) with no PRTase catalytic motif. Only B aligns with the PRTase fold and its canonical role in cofactor biosynthesis. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (inferred from electronic annotation via UniPathway/InterPro), but the underlying function and pathway assignment are experimentally supported (ECO:0000269, PubMed:38429435, PDB structures).",
    "The organism (Xanthomonas, bacterium) is not stated in the question; elimination of option A relies on recognizing the protein architecture is incompatible with eukaryotic transcriptional regulation, not on knowing the taxon.",
    "The PRTase fold recognition from raw sequence is a specialized but general biochemistry skill; it does not require memorizing this specific UniProt entry.",
    "The reviewer evidence confirms sequence identity (SHA256 match) between the benchmark sequence and UniProt A0A0H2X5R2.",
    "The entry was first publicly released 2025-02-05; if the benchmark was constructed before that date, the annotation available to the original authors may have differed."
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

**Accession:** `A0A0H2X5R2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
"A0A0H2X5R2"
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38429435","source":"PubMed"}],"value":"2.4.2.12"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"Nicotinamide phosphoribosyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAM phosphoribosyltransferase"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAMPT"}]}}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38429435","source":"PubMed"}],"value":"Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD (PubMed:38429435). Plays an important role in the biosynthesis of NAD via the nicotinamide (NAM) salvage pathway (PubMed:38429435). Is also capable of hydrolyzing ATP and shows ATP-dependent autophosphorylation activity (PubMed:38429435)"}]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38429435","source":"PubMed"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1"}]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"database":"GO","id":"GO:0009435","properties":[{"key":"GoTerm","value":"P:NAD+ biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"citation":{"authors":["Xu G.","Ma J.","Fang Q.","Peng Q.","Jiao X.","Hu W.","Zhao Q.","Kong Y.","Liu F.","Shi X.","Tang D.J.","Tang J.L.","Ming Z."],"citationCrossReferences":[{"database":"PubMed","id":"38429435"},{"database":"DOI","id":"10.1038/s42003-024-05921-3"}],"citationType":"journal article","firstPage":"255","id":"38429435","journal":"Commun. Biol.","lastPage":"255","publicationDate":"2024","title":"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.","volume":"7"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7YQO","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQP","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQQ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQR","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8IGZ","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"8004"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE MUTANT PHE-175/PHE-224/PHE-291/PHE-332","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT","DOMAIN","PHOSPHORYLATION AT HIS-229","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332; ASP-335 AND ARG-373"]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 41-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the condensation of nicotinamide with 5-
CC       phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an
CC       intermediate in the biosynthesis of NAD (PubMed:38429435). Plays an
CC       important role in the biosynthesis of NAD via the nicotinamide (NAM)
CC       salvage pathway (PubMed:38429435). Is also capable of hydrolyzing ATP
CC       and shows ATP-dependent autophosphorylation activity (PubMed:38429435).
CC       {ECO:0000269|PubMed:38429435}.
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 70-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-
CC       ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and
CC       nicotinamide: step 1/1. {ECO:0000269|PubMed:38429435}.
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 117-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
DR   GO; GO:0009435; P:NAD+ biosynthetic process; IEA:InterPro.
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 96227-96257`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009435
name: NAD+ biosynthetic process
namespace: biological_process
alt_id: GO:0006736
def: "The chemical reactions and pathways resulting in the formation of nicotinamide adenine dinucleotide (NAD+), a coenzyme that interconverts with its reduced form, NADH, in many redox and catabolic reactions. NAD+ is derived from various sources including vitamin B3." [PMID:28648096]
synonym: "NAD (oxidized) biosynthesis" EXACT []
synonym: "NAD (oxidized) biosynthetic process" EXACT []
synonym: "NAD (reduced) biosynthesis" EXACT []
synonym: "NAD (reduced) biosynthetic process" EXACT []
synonym: "NAD anabolism" EXACT []
synonym: "NAD biosynthesis" EXACT []
synonym: "NAD biosynthetic process" EXACT []
synonym: "NAD formation" EXACT []
synonym: "NAD synthesis" EXACT []
synonym: "NADH biosynthesis" EXACT []
synonym: "NADH biosynthetic process" EXACT []
synonym: "nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "nicotinamide adenine dinucleotide biosynthetic process" EXACT []
synonym: "oxidized NAD biosynthesis" EXACT []
synonym: "oxidized NAD biosynthetic process" EXACT []
synonym: "oxidized nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "oxidized nicotinamide adenine dinucleotide biosynthetic process" EXACT []
synonym: "reduced NAD biosynthesis" EXACT []
synonym: "reduced NAD biosynthetic process" EXACT []
synonym: "reduced nicotinamide adenine dinucleotide biosynthesis" EXACT []
synonym: "reduced nicotinamide adenine dinucleotide biosynthetic process" EXACT []
is_a: GO:0006164 ! purine nucleotide biosynthetic process
is_a: GO:0019359 ! nicotinamide nucleotide biosynthetic process
is_a: GO:0019674 ! NAD+ metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
