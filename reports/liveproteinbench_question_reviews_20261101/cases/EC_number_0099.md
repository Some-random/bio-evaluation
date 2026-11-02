# EC_number_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 5.4.99.39

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWRLKIAEGGNDPYLYSTNNFVGRQTWEFDSEYGTPEAIKEVEEARQIFYKNRFQVKPCGDLLWRFQFLREKNFKQTIPQVKVGDGEEVTYEAASTTLKRSVNLLTALQADDGHWPAEIAGPQFFLPPLVFCLYITGHLNVVFNVHHREEILRSIYYHQNEDGGWGLHIEGHSTMFCTALNYICLRMLGVGPDEGDDNACPRARKWILDHGSVTHIPSWGKTWLSILGLFDWSGSNPMPPEFWILPTFMPMYPAKMWCYCRMVYMPMSYLYGKRFVGPITPLIKQLREELFSEPFEEIKWKKVRHLCAPEDLYYPHPLIQDLMWDSLYLFTEPLLTRWPFNNLIRQKALQVTMDHIHYEDENSRYITIGCVEKVLCMLACWVEDPNGVCYKKHLARVPDYIWIAEDGLKMQSFGSQQWDCGFAVQALLASNMSLDEIGPALKKGHFFIKESQVKDNPSGDFKSMHRHISKGSWTFSDQDHGWQVSDCTAEGLKCCLILSTMPPEIVGEKMDPERLYDSVNVLLSLQSENGGLSAWEPAGAQAWLELLNPTEFFADIVIEHEYVECTGASIQALVLFKKMYPGHRKKEIENFIAKAAKYLEDTQYPNGSWYGNWGVCFTYGTWFALGGLAAAGKTYANCAAMRKGVEFLLKSQKEDGGWGESYVSCPKKDFVPLEGPSNLTQTAWALMGLIYARQMERDPTPLHQAAKLLINSQLENGDFPQQEITGVFMKNCMLHYPMYRTIYPLWAIAEYRTHVPLRLS

[Multiple Choices]
A. 5.4.99.14
B. 1.14.18.1
C. 3.2.1.18
D. 5.4.99.39
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as beta-amyrin synthase 1, EC 5.4.99.39. Its catalytic-activity annotation specifies conversion of (S)-2,3-epoxysqualene to beta-amyrin and cites experimental evidence (ECO:0000269, PubMed:39043959).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large plant oxidosqualene cyclase, which makes the isomerase choices more plausible than the oxidoreductase or glycosidase choices. However, that broad family-level inference does not establish which specific cyclization product this protein makes.


**Missing item-specific fact**

> The protein-specific product/function—beta-amyrin formation rather than the product associated with the other oxidosqualene-cyclase EC option—is not supplied in the question and requires an annotation, prior knowledge of this protein, or functional evidence.


**Reason**

> The exact EC distinction between the two isomerase choices depends on the enzyme's specific reaction, not something determined by general sequence-family recognition alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone leaves the precise oxidosqualene-cyclase product underdetermined, but the reviewer-only evidence supports D for this matched protein.


### Important caveats

- The UniProt sequence match and cited catalytic-activity evidence support the key, but the primary paper was not independently reviewed here.
- The accession and database evidence were reviewer-only and were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large plant oxidosqualene cyclase, which makes the isomerase choices more plausible than the oxidoreductase or glycosidase choices. However, that broad family-level inference does not establish which specific cyclization product this protein makes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific product/function—beta-amyrin formation rather than the product associated with the other oxidosqualene-cyclase EC option—is not supplied in the question and requires an annotation, prior knowledge of this protein, or functional evidence.",
    "reason": "The exact EC distinction between the two isomerase choices depends on the enzyme's specific reaction, not something determined by general sequence-family recognition alone."
  },
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as beta-amyrin synthase 1, EC 5.4.99.39. Its catalytic-activity annotation specifies conversion of (S)-2,3-epoxysqualene to beta-amyrin and cites experimental evidence (ECO:0000269, PubMed:39043959)."
  },
  "important_caveats": [
    "The UniProt sequence match and cited catalytic-activity evidence support the key, but the primary paper was not independently reviewed here.",
    "The accession and database evidence were reviewer-only and were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the precise oxidosqualene-cyclase product underdetermined, but the reviewer-only evidence supports D for this matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as beta-amyrin synthase 1, EC 5.4.99.39. Its catalytic-activity annotation specifies conversion of (S)-2,3-epoxysqualene to beta-amyrin and cites experimental evidence (ECO:0000269, PubMed:39043959).",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large plant oxidosqualene cyclase, which makes the isomerase choices more plausible than the oxidoreductase or glycosidase choices. However, that broad family-level inference does not establish which specific cyclization product this protein makes.",
    "missing_item_specific_fact": "The protein-specific product/function—beta-amyrin formation rather than the product associated with the other oxidosqualene-cyclase EC option—is not supplied in the question and requires an annotation, prior knowledge of this protein, or functional evidence.",
    "reason": "The exact EC distinction between the two isomerase choices depends on the enzyme's specific reaction, not something determined by general sequence-family recognition alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the precise oxidosqualene-cyclase product underdetermined, but the reviewer-only evidence supports D for this matched protein."
  },
  "important_caveats": [
    "The UniProt sequence match and cited catalytic-activity evidence support the key, but the primary paper was not independently reviewed here.",
    "The accession and database evidence were reviewer-only and were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1L0L7 (BAMS1_SAPOF) annotates this exact 760-aa sequence as Beta-amyrin synthase 1 with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic reaction (S)-2,3-epoxysqualene → beta-amyrin is explicitly recorded. Sequence SHA256 matches between the benchmark input and the database entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the DCTAE motif (…SDCTAEGLKCCLILST…) and a DDM-like motif, which are hallmarks of oxidosqualene cyclases (OSCs). This allows a knowledgeable model to eliminate B (1.14.18.1, copper monooxygenase) and C (3.2.1.18, glycosidase) because neither enzyme class uses a triterpene-cyclase fold or these motifs. However, both remaining options A (5.4.99.14) and D (5.4.99.39) fall within the same EC sub-subclass 5.4.99 (other intramolecular transferases / cyclases), and distinguishing the 4th digit—i.e., the specific triterpene product (beta-amyrin vs. another cyclization product)—cannot be reliably inferred from general sequence features alone.


**Missing item-specific fact**

> The precise product specificity of this particular oxidosqualene cyclase (beta-amyrin vs. another triterpene such as lupeol, taraxasterol, etc.) is determined by a small number of active-site residues and cannot be confidently assigned from the full sequence by general biological reasoning. Additionally, whether EC 5.4.99.14 is a valid, currently assigned EC number for a distinct cyclase or a fabricated distractor is an item-specific fact not derivable from the sequence.


**Reason**

> General knowledge of OSC motifs (DCTAE, DDM) narrows the answer to the 5.4.99.x class, eliminating B and C. But the final A-vs-D distinction requires knowing the exact cyclization product of this specific enzyme, which is an item-specific experimental annotation rather than something derivable from broad biological principles applied to the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the experimental annotation and the DCTAE motif confirming an oxidosqualene cyclase, D (5.4.99.39) is the only option consistent with the full evidence. Options B and C are clearly incompatible with the sequence architecture. Option A (5.4.99.14) is in the correct EC class but represents a different product specificity; without evidence that 5.4.99.14 corresponds to this sequence, D is the single defensible answer. The question is not ambiguous in its correct answer, though the A-vs-D gap is narrow.


### Important caveats

- The EC annotation is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper (PubMed:39043959), not merely by sequence-similarity transfer.
- The DCTAE motif reasoning eliminates B and C but does not uniquely determine the 4th EC digit; the final A-vs-D choice effectively depends on the specific experimental product characterization.
- EC 5.4.99.14 may or may not be a currently assigned EC number; if it is a fabricated distractor, the question becomes easier, but this is an item-specific fact the model would need to know.
- The sequence length (760 aa) and overall fold are consistent with plant OSCs, but many plant OSCs share high sequence identity while producing different triterpenes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the DCTAE motif (…SDCTAEGLKCCLILST…) and a DDM-like motif, which are hallmarks of oxidosqualene cyclases (OSCs). This allows a knowledgeable model to eliminate B (1.14.18.1, copper monooxygenase) and C (3.2.1.18, glycosidase) because neither enzyme class uses a triterpene-cyclase fold or these motifs. However, both remaining options A (5.4.99.14) and D (5.4.99.39) fall within the same EC sub-subclass 5.4.99 (other intramolecular transferases / cyclases), and distinguishing the 4th digit—i.e., the specific triterpene product (beta-amyrin vs. another cyclization product)—cannot be reliably inferred from general sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise product specificity of this particular oxidosqualene cyclase (beta-amyrin vs. another triterpene such as lupeol, taraxasterol, etc.) is determined by a small number of active-site residues and cannot be confidently assigned from the full sequence by general biological reasoning. Additionally, whether EC 5.4.99.14 is a valid, currently assigned EC number for a distinct cyclase or a fabricated distractor is an item-specific fact not derivable from the sequence.",
    "reason": "General knowledge of OSC motifs (DCTAE, DDM) narrows the answer to the 5.4.99.x class, eliminating B and C. But the final A-vs-D distinction requires knowing the exact cyclization product of this specific enzyme, which is an item-specific experimental annotation rather than something derivable from broad biological principles applied to the sequence."
  },
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1L0L7 (BAMS1_SAPOF) annotates this exact 760-aa sequence as Beta-amyrin synthase 1 with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic reaction (S)-2,3-epoxysqualene → beta-amyrin is explicitly recorded. Sequence SHA256 matches between the benchmark input and the database entry."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper (PubMed:39043959), not merely by sequence-similarity transfer.",
    "The DCTAE motif reasoning eliminates B and C but does not uniquely determine the 4th EC digit; the final A-vs-D choice effectively depends on the specific experimental product characterization.",
    "EC 5.4.99.14 may or may not be a currently assigned EC number; if it is a fabricated distractor, the question becomes easier, but this is an item-specific fact the model would need to know.",
    "The sequence length (760 aa) and overall fold are consistent with plant OSCs, but many plant OSCs share high sequence identity while producing different triterpenes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation and the DCTAE motif confirming an oxidosqualene cyclase, D (5.4.99.39) is the only option consistent with the full evidence. Options B and C are clearly incompatible with the sequence architecture. Option A (5.4.99.14) is in the correct EC class but represents a different product specificity; without evidence that 5.4.99.14 corresponds to this sequence, D is the single defensible answer. The question is not ambiguous in its correct answer, though the A-vs-D gap is narrow."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1L0L7 (BAMS1_SAPOF) annotates this exact 760-aa sequence as Beta-amyrin synthase 1 with EC 5.4.99.39, supported by experimental evidence (ECO:0000269, PubMed:39043959). The catalytic reaction (S)-2,3-epoxysqualene → beta-amyrin is explicitly recorded. Sequence SHA256 matches between the benchmark input and the database entry.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the DCTAE motif (…SDCTAEGLKCCLILST…) and a DDM-like motif, which are hallmarks of oxidosqualene cyclases (OSCs). This allows a knowledgeable model to eliminate B (1.14.18.1, copper monooxygenase) and C (3.2.1.18, glycosidase) because neither enzyme class uses a triterpene-cyclase fold or these motifs. However, both remaining options A (5.4.99.14) and D (5.4.99.39) fall within the same EC sub-subclass 5.4.99 (other intramolecular transferases / cyclases), and distinguishing the 4th digit—i.e., the specific triterpene product (beta-amyrin vs. another cyclization product)—cannot be reliably inferred from general sequence features alone.",
    "missing_item_specific_fact": "The precise product specificity of this particular oxidosqualene cyclase (beta-amyrin vs. another triterpene such as lupeol, taraxasterol, etc.) is determined by a small number of active-site residues and cannot be confidently assigned from the full sequence by general biological reasoning. Additionally, whether EC 5.4.99.14 is a valid, currently assigned EC number for a distinct cyclase or a fabricated distractor is an item-specific fact not derivable from the sequence.",
    "reason": "General knowledge of OSC motifs (DCTAE, DDM) narrows the answer to the 5.4.99.x class, eliminating B and C. But the final A-vs-D distinction requires knowing the exact cyclization product of this specific enzyme, which is an item-specific experimental annotation rather than something derivable from broad biological principles applied to the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation and the DCTAE motif confirming an oxidosqualene cyclase, D (5.4.99.39) is the only option consistent with the full evidence. Options B and C are clearly incompatible with the sequence architecture. Option A (5.4.99.14) is in the correct EC class but represents a different product specificity; without evidence that 5.4.99.14 corresponds to this sequence, D is the single defensible answer. The question is not ambiguous in its correct answer, though the A-vs-D gap is narrow."
  },
  "important_caveats": [
    "The EC annotation is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper (PubMed:39043959), not merely by sequence-similarity transfer.",
    "The DCTAE motif reasoning eliminates B and C but does not uniquely determine the 4th EC digit; the final A-vs-D choice effectively depends on the specific experimental product characterization.",
    "EC 5.4.99.14 may or may not be a currently assigned EC number; if it is a fabricated distractor, the question becomes easier, but this is an item-specific fact the model would need to know.",
    "The sequence length (760 aa) and overall fold are consistent with plant OSCs, but many plant OSCs share high sequence identity while producing different triterpenes."
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

**Accession:** `A0AAW1L0L7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
"A0AAW1L0L7"
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"5.4.99.39"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Beta-amyrin synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SobAS1"}]}}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:31008"}}],"reaction":{"ecNumber":"5.4.99.39","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"name":"(S)-2,3-epoxysqualene = beta-amyrin","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:31007"},{"database":"ChEBI","id":"CHEBI:10352"},{"database":"ChEBI","id":"CHEBI:15441"}]}}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48160.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
ID   BAMS1_SAPOF             Reviewed;         760 AA.
AC   A0AAW1L0L7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=Beta-amyrin synthase 1 {ECO:0000303|PubMed:39043959};
DE            Short=SobAS1 {ECO:0000303|PubMed:39043959};
DE            EC=5.4.99.39 {ECO:0000269|PubMed:39043959};
GN   Name=bAS1 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11027757m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_05G236200 {ECO:0000312|EMBL:KAK9726778.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
DE   RecName: Full=Beta-amyrin synthase 1 {ECO:0000303|PubMed:39043959};
DE            Short=SobAS1 {ECO:0000303|PubMed:39043959};
DE            EC=5.4.99.39 {ECO:0000269|PubMed:39043959};
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(S)-2,3-epoxysqualene = beta-amyrin; Xref=Rhea:RHEA:31007,
CC         ChEBI:CHEBI:10352, ChEBI:CHEBI:15441; EC=5.4.99.39;
CC         Evidence={ECO:0000269|PubMed:39043959};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:31008;
CC         Evidence={ECO:0000269|PubMed:39043959};
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
