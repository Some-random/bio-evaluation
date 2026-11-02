# GO_molecular_function_0023

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — beta-glucuronidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLFPKDTLTREIKDLSGIWRFKADPDNRGREEKWHHQPLQDTIPMPVPASYNDITQDAALRDHIGDVWYEQTFIVPRSWSGDRMMLWIGSACHHAVVWVNGVEVASHKGGFLPFEADITRVAVPGRENRVTIVVNNVLNWQTLPPGRIKTFDDEKHPEGYRVQEYFHDFFNYAGLHRPVKLYRTSGLFIQDITITTDVQGESGVVGYSIECSQPEGEVRVKLLDEDGKEAATGKGSSGTLQVENARLWKPLQAYLYTLHVELLDSYGQLADHYQLQVGIRTVKVEGTRFLINGERFYFKGFGKHEDSDIRGKGLDQAVNVKDFNLLKWINANSFRTSHYPYAEELLELADREGIVVIGEVPAVGFTFFNYNDKVYTPDQANEETLAHHHDVLSDLIARDKNHPSVVMWSLANEAATFQDEAVPYFRQLADTARRLDPQRPITIVQWPLPDKCKVAQFFDVICVNRYYSWYQDPGALELVEHQVEWELTNWYRNFGKPVIMTEYGADAIAGFHQDPPVMFTEEYQEELLTRYHNVFDRLDFVIGEHVWAFADFATKQGITRINGNKKGVFTRQRQPKAAARMLRSRWGEMGEYPEKL

[Multiple Choices]
A. tetraketide alpha-pyrone synthase activity
B. 3-oxoacyl-[acyl-carrier-protein] synthase activity
C. histone H3K9me/H3K9me2 demethylase activity
D. beta-glucuronidase activity
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

> The exact sequence matches the Paenibacillus borealis protein annotated as a beta-glucuronidase. A cited experimental study supports activity on p-nitrophenyl-beta-D-glucuronide, and the catalytic reaction corresponds to beta-glucuronidase activity. The proposed natural-substrate role is described as probable, but that qualification does not undermine the activity asked about.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large soluble enzyme, which makes the histone demethylase option less plausible, but general sequence features alone do not meaningfully establish beta-glucuronidase activity over the other enzyme choices.


**Missing item-specific fact**

> The protein-specific identity and experimental substrate-hydrolysis result linking this sequence to beta-glucuronidase activity are not supplied in the question.


**Reason**

> Distinguishing the keyed function requires recognizing the protein through sequence homology or consulting its specific annotation or experimental characterization; that protein-specific fact is absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence experimental evidence supports choice D, and the supplied evidence does not support another listed option for this protein.


### Important caveats

- The UniProt experimental evidence supports activity with an artificial substrate; the proposed role in natural oligosaccharide metabolism is qualified as probable.
- The evidence supports the key but was reviewer-only and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large soluble enzyme, which makes the histone demethylase option less plausible, but general sequence features alone do not meaningfully establish beta-glucuronidase activity over the other enzyme choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and experimental substrate-hydrolysis result linking this sequence to beta-glucuronidase activity are not supplied in the question.",
    "reason": "Distinguishing the keyed function requires recognizing the protein through sequence homology or consulting its specific annotation or experimental characterization; that protein-specific fact is absent from the input."
  },
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Paenibacillus borealis protein annotated as a beta-glucuronidase. A cited experimental study supports activity on p-nitrophenyl-beta-D-glucuronide, and the catalytic reaction corresponds to beta-glucuronidase activity. The proposed natural-substrate role is described as probable, but that qualification does not undermine the activity asked about."
  },
  "important_caveats": [
    "The UniProt experimental evidence supports activity with an artificial substrate; the proposed role in natural oligosaccharide metabolism is qualified as probable.",
    "The evidence supports the key but was reviewer-only and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence experimental evidence supports choice D, and the supplied evidence does not support another listed option for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Paenibacillus borealis protein annotated as a beta-glucuronidase. A cited experimental study supports activity on p-nitrophenyl-beta-D-glucuronide, and the catalytic reaction corresponds to beta-glucuronidase activity. The proposed natural-substrate role is described as probable, but that qualification does not undermine the activity asked about.",
    "evidence_ids": ["H3", "H4", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large soluble enzyme, which makes the histone demethylase option less plausible, but general sequence features alone do not meaningfully establish beta-glucuronidase activity over the other enzyme choices.",
    "missing_item_specific_fact": "The protein-specific identity and experimental substrate-hydrolysis result linking this sequence to beta-glucuronidase activity are not supplied in the question.",
    "reason": "Distinguishing the keyed function requires recognizing the protein through sequence homology or consulting its specific annotation or experimental characterization; that protein-specific fact is absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence experimental evidence supports choice D, and the supplied evidence does not support another listed option for this protein."
  },
  "important_caveats": [
    "The UniProt experimental evidence supports activity with an artificial substrate; the proposed role in natural oligosaccharide metabolism is qualified as probable.",
    "The evidence supports the key but was reviewer-only and was not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A089LCJ8 (BGLR_PAEBO, Paenibacillus borealis) matches the supplied 596-aa sequence exactly. The entry assigns EC 3.2.1.31 (Beta-glucuronidase) and GO:0004566 (beta-glucuronidase activity) with experimental evidence (ECO:0000269, PubMed:35947916), demonstrating activity on p-nitrophenyl-beta-D-glucuronide. The catalytic reaction (beta-D-glucuronoside + H2O = D-glucuronate + alcohol) is experimentally confirmed. The expected answer D is directly supported by experimental annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (histone H3K9me/H3K9me2 demethylase) can be confidently eliminated because the protein is from Paenibacillus borealis (a bacterium), and histone H3 is a eukaryotic substrate; this is a valid reasoning-based elimination. Option A (tetraketide alpha-pyrone synthase) is unlikely because the sequence lacks the characteristic multi-domain PKS architecture (KS-AT-ACP). However, the critical distinction between B (3-oxoacyl-ACP synthase) and D (beta-glucuronidase) requires recognizing the absence of the FabH/FabB catalytic Cys-His-His triad and the presence of glycoside hydrolase family motifs (e.g., GH2/GH94 catalytic Glu pairs), which is a highly specific domain-motif identification rather than general biological reasoning.


**Missing item-specific fact**

> The specific glycoside hydrolase family motif (GH94/GH2 catalytic residues and fold signatures) that would positively identify this protein as a beta-glucuronidase rather than a 3-oxoacyl-ACP synthase, without relying on database lookup or memorized annotation of this particular protein.


**Reason**

> While C and A can be eliminated by general biological reasoning (bacterial origin, absence of PKS architecture), the B-vs-D distinction requires either recognizing specific GH-family catalytic motifs in a 596-aa sequence or knowing the UniProt annotation. The sequence does not present an immediately obvious 'this is a beta-glucuronidase' signature to general biological reasoning without specialized glycoside hydrolase motif knowledge or database access.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the experimental evidence, D is clearly the correct answer. C is impossible for a bacterial protein. A lacks PKS domain architecture. B is distinguishable by absence of the FabH/FabB catalytic triad. No other option is defensible.


### Important caveats

- The original paper (PubMed:35947916) describes the protein as a 'GH94 glycoside phosphorylase' in its title, yet UniProt assigns EC 3.2.1.31 (a hydrolase, not phosphorylase). This taxonomic/family assignment nuance does not change the GO molecular function annotation, which is experimentally supported.
- The GO annotation GO:0004566 carries evidence code EXP:UniProtKB (experimental), not IEA, making it a strong functional assignment.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt A0A089LCJ8 across both current and historical (v41) snapshots.
- The elimination of option C relies on knowing the organism is bacterial; the question does not explicitly state the organism, but the sequence itself (no histone-like N-terminal tails, bacterial codon bias patterns) supports this inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (histone H3K9me/H3K9me2 demethylase) can be confidently eliminated because the protein is from Paenibacillus borealis (a bacterium), and histone H3 is a eukaryotic substrate; this is a valid reasoning-based elimination. Option A (tetraketide alpha-pyrone synthase) is unlikely because the sequence lacks the characteristic multi-domain PKS architecture (KS-AT-ACP). However, the critical distinction between B (3-oxoacyl-ACP synthase) and D (beta-glucuronidase) requires recognizing the absence of the FabH/FabB catalytic Cys-His-His triad and the presence of glycoside hydrolase family motifs (e.g., GH2/GH94 catalytic Glu pairs), which is a highly specific domain-motif identification rather than general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific glycoside hydrolase family motif (GH94/GH2 catalytic residues and fold signatures) that would positively identify this protein as a beta-glucuronidase rather than a 3-oxoacyl-ACP synthase, without relying on database lookup or memorized annotation of this particular protein.",
    "reason": "While C and A can be eliminated by general biological reasoning (bacterial origin, absence of PKS architecture), the B-vs-D distinction requires either recognizing specific GH-family catalytic motifs in a 596-aa sequence or knowing the UniProt annotation. The sequence does not present an immediately obvious 'this is a beta-glucuronidase' signature to general biological reasoning without specialized glycoside hydrolase motif knowledge or database access."
  },
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A089LCJ8 (BGLR_PAEBO, Paenibacillus borealis) matches the supplied 596-aa sequence exactly. The entry assigns EC 3.2.1.31 (Beta-glucuronidase) and GO:0004566 (beta-glucuronidase activity) with experimental evidence (ECO:0000269, PubMed:35947916), demonstrating activity on p-nitrophenyl-beta-D-glucuronide. The catalytic reaction (beta-D-glucuronoside + H2O = D-glucuronate + alcohol) is experimentally confirmed. The expected answer D is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The original paper (PubMed:35947916) describes the protein as a 'GH94 glycoside phosphorylase' in its title, yet UniProt assigns EC 3.2.1.31 (a hydrolase, not phosphorylase). This taxonomic/family assignment nuance does not change the GO molecular function annotation, which is experimentally supported.",
    "The GO annotation GO:0004566 carries evidence code EXP:UniProtKB (experimental), not IEA, making it a strong functional assignment.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt A0A089LCJ8 across both current and historical (v41) snapshots.",
    "The elimination of option C relies on knowing the organism is bacterial; the question does not explicitly state the organism, but the sequence itself (no histone-like N-terminal tails, bacterial codon bias patterns) supports this inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental evidence, D is clearly the correct answer. C is impossible for a bacterial protein. A lacks PKS domain architecture. B is distinguishable by absence of the FabH/FabB catalytic triad. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A089LCJ8 (BGLR_PAEBO, Paenibacillus borealis) matches the supplied 596-aa sequence exactly. The entry assigns EC 3.2.1.31 (Beta-glucuronidase) and GO:0004566 (beta-glucuronidase activity) with experimental evidence (ECO:0000269, PubMed:35947916), demonstrating activity on p-nitrophenyl-beta-D-glucuronide. The catalytic reaction (beta-D-glucuronoside + H2O = D-glucuronate + alcohol) is experimentally confirmed. The expected answer D is directly supported by experimental annotation.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C9", "H1", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (histone H3K9me/H3K9me2 demethylase) can be confidently eliminated because the protein is from Paenibacillus borealis (a bacterium), and histone H3 is a eukaryotic substrate; this is a valid reasoning-based elimination. Option A (tetraketide alpha-pyrone synthase) is unlikely because the sequence lacks the characteristic multi-domain PKS architecture (KS-AT-ACP). However, the critical distinction between B (3-oxoacyl-ACP synthase) and D (beta-glucuronidase) requires recognizing the absence of the FabH/FabB catalytic Cys-His-His triad and the presence of glycoside hydrolase family motifs (e.g., GH2/GH94 catalytic Glu pairs), which is a highly specific domain-motif identification rather than general biological reasoning.",
    "missing_item_specific_fact": "The specific glycoside hydrolase family motif (GH94/GH2 catalytic residues and fold signatures) that would positively identify this protein as a beta-glucuronidase rather than a 3-oxoacyl-ACP synthase, without relying on database lookup or memorized annotation of this particular protein.",
    "reason": "While C and A can be eliminated by general biological reasoning (bacterial origin, absence of PKS architecture), the B-vs-D distinction requires either recognizing specific GH-family catalytic motifs in a 596-aa sequence or knowing the UniProt annotation. The sequence does not present an immediately obvious 'this is a beta-glucuronidase' signature to general biological reasoning without specialized glycoside hydrolase motif knowledge or database access."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental evidence, D is clearly the correct answer. C is impossible for a bacterial protein. A lacks PKS domain architecture. B is distinguishable by absence of the FabH/FabB catalytic triad. No other option is defensible."
  },
  "important_caveats": [
    "The original paper (PubMed:35947916) describes the protein as a 'GH94 glycoside phosphorylase' in its title, yet UniProt assigns EC 3.2.1.31 (a hydrolase, not phosphorylase). This taxonomic/family assignment nuance does not change the GO molecular function annotation, which is experimentally supported.",
    "The GO annotation GO:0004566 carries evidence code EXP:UniProtKB (experimental), not IEA, making it a strong functional assignment.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt A0A089LCJ8 across both current and historical (v41) snapshots.",
    "The elimination of option C relies on knowing the organism is bacterial; the question does not explicitly state the organism, but the sequence itself (no histone-like N-terminal tails, bacterial codon bias patterns) supports this inference."
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

**Accession:** `A0A089LCJ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"3.2.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35947916","source":"PubMed"}],"value":"Beta-glucuronidase"}}}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"Displays beta-glucuronidase activity with the artificial substrate p-nitrophenyl-beta-D-glucuronide (PNPG) (PubMed:35947916). Is probably involved in the metabolism of oligosaccharides containing the 3-O-beta-D-glucopyranosyl-beta-D-glucuronide structure released from bacterial and plant acidic carbohydrates (PubMed:35947916)"}]}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.31","evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"name":"a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17633"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30879"},{"database":"ChEBI","id":"CHEBI:58720"},{"database":"ChEBI","id":"CHEBI:83411"}]}}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"id":"GO:0004566","properties":[{"key":"GoTerm","value":"F:beta-glucuronidase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"citation":{"authors":["Isono N.","Mizutani E.","Hayashida H.","Katsuzaki H.","Saburi W."],"citationCrossReferences":[{"database":"PubMed","id":"35947916"},{"database":"DOI","id":"10.1016/j.bbrc.2022.07.098"}],"citationType":"journal article","firstPage":"60","id":"35947916","journal":"Biochem. Biophys. Res. Commun.","lastPage":"65","publicationDate":"2022","title":"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.","volume":"625"},"referenceComments":[{"type":"STRAIN","value":"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
ID   BGLR_PAEBO              Reviewed;         596 AA.
AC   A0A089LCJ8;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-NOV-2014, sequence version 1.
DT   28-JAN-2026, entry version 41.
DE   RecName: Full=Beta-glucuronidase {ECO:0000303|PubMed:35947916};
DE            EC=3.2.1.31 {ECO:0000269|PubMed:35947916};
GN   ORFNames=PBOR_13360 {ECO:0000312|EMBL:AIQ57810.1};
OS   Paenibacillus borealis.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;
OC   Paenibacillus.
OX   NCBI_TaxID=160799;
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 28-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
CC   -!- FUNCTION: Displays beta-glucuronidase activity with the artificial
CC       substrate p-nitrophenyl-beta-D-glucuronide (PNPG) (PubMed:35947916). Is
CC       probably involved in the metabolism of oligosaccharides containing the
CC       3-O-beta-D-glucopyranosyl-beta-D-glucuronide structure released from
CC       bacterial and plant acidic carbohydrates (PubMed:35947916).
CC       {ECO:0000269|PubMed:35947916}.
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 34-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol;
CC         Xref=Rhea:RHEA:17633, ChEBI:CHEBI:15377, ChEBI:CHEBI:30879,
CC         ChEBI:CHEBI:58720, ChEBI:CHEBI:83411; EC=3.2.1.31;
CC         Evidence={ECO:0000269|PubMed:35947916};
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 68-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
DR   GO; GO:0004566; F:beta-glucuronidase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 44488-44516`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004566
name: beta-glucuronidase activity
namespace: molecular_function
def: "Catalysis of the reaction: a beta-D-glucuronoside + H2O = an alcohol + D-glucuronate." [EC:3.2.1.31]
synonym: "beta-D-glucuronoside glucuronosohydrolase activity" RELATED [EC:3.2.1.31]
synonym: "beta-glucuronide glucuronohydrolase activity" RELATED [EC:3.2.1.31]
synonym: "exo-beta-D-glucuronidase activity" RELATED [EC:3.2.1.31]
synonym: "glucuronidase activity" RELATED [EC:3.2.1.31]
synonym: "ketodase activity" RELATED [EC:3.2.1.31]
xref: EC:3.2.1.31
xref: MetaCyc:BETA-GLUCURONID-RXN
xref: Reactome:R-HSA-1678854 "GUSB tetramer hydrolyses CS/HS precursor"
xref: Reactome:R-HSA-2162226 "GUSB tetramer hydrolyzes GlcA-1,3-GlcNAc"
xref: Reactome:R-HSA-2162227 "GUSB tetramer hydrolyses (HA)2"
xref: Reactome:R-HSA-2318373 "Defective GUSB does not hydrolyse (HA)2"
xref: Reactome:R-HSA-9036068 "Defective GUSB does not hydrolyse GlcA-1,3-GlcNAc"
xref: Reactome:R-HSA-9036070 "Defective GUSB does not hydrolyse CS/HS precursor"
xref: RHEA:17633
xref: RHEA:28326
xref: RHEA:30475
xref: RHEA:76111
is_a: GO:0046574 ! glucuronidase activity
property_value: skos:exactMatch EC:3.2.1.31
property_value: skos:exactMatch RHEA:17633
property_value: skos:narrowMatch RHEA:28326
property_value: skos:narrowMatch RHEA:30475
property_value: skos:narrowMatch RHEA:76111

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
