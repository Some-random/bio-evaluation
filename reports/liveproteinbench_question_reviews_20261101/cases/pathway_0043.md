# pathway_0043

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Pigment biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDNISNHAFNYPVLVLNKGLLPEHDDIALARYLFSALALAVSRITQNEEMIVGFHLHPQEITRWKDDECIRQYILPLNIRFNSATPIAGFIREIMTWMTPDAIHQKNAMGASVLTLGPQHALHDIFDLEISWQPPVESEPVQALTCHVASREDALVLTLRFNPARFSATQMQKLPEVWRQITASAAKNGAETLRDIGLIDDAERQRVLHAFNQTEQAWDGETTVAARLKNRAQRHPEQTAVVFRDETLSYRQLYQQAGALAHYLNALETERERCVGLFVEPSLTLMTGVWGILLSGNAYLPLSPEYPEDRLAYMLENSQTRIIVTQPHLRERLLALAPPGIQVVTSDDVDAFMRQHAHSLPDAPQNDIAPHHLAYVIYTSGSTGKPKGVMIEHHSVLNQMNWLAQTVGLNQETVILQKTPMSFDAAQWEILSPACGCRVVMGEPGVYRNPEQLVDMLAEYRVTTLQCVPTLLQALLDTERLTHCPALRQIFSGGEALQKHLAQACLETLPDCELINLYGPTECTINNSAFRVDPVSVRQGPDTLSIGAPVANTRYYILDNCLTPVAVGQIGELYIGGDGVARGYLNRDDLTAERFIVDPFAPAGSGRRLYQTGDIASWNPDGTVQYAGRADNQVKLRGYRVELDEIRSAIETHEWVKAAAVIVRNDPFTGYQNLISFIELNAREAALMDQGNHGSHHQSKADKAQVMLQLANKGCREFPAASQPYTLDLPGKQPDEKQRLTAFSRKTYRFYDGGAVSREDILSLLHEPLLTAISRQPDALTLDELGHWLRYLGQFTSAERLLPKYTYASPGALYATQVFLELNGVAGLTAGHYYYQPVHHQLVRVSEQAAVTPGSLRLHFVGKKSAIEPIYKNNIREVLQMEMGHIIGMLDIILPDYGLGVALCDAAALDPTPLAIDLDDDYLGACDVLSGPRLPTDDDLDIYVQTAGANIADLPVGTYRYVRGDLQHIADDVIDKKHVIAINQAVYERSSFGISVASRTEGWAGYVHVGRKLQRLQMNPLNIGLMSSGYSSETGNDLPAARRFWQILGHRTGPYYFFIGGRISDEQKYSEGMREDAVHMKGPAEMIRDDLAAFMPDYMMPNKVLILDEMPLTANGKIDMKALANINVELKHKTIVAPRNPLEHQVMAIWQAKLKREEMSVDDNFFESGGNSLIAVSLINELNATLNASLPLQVLFQAPTVEKLAAWLSRARREPVSRLVQLQPKGRQAPIYCWPGLGGYCMNLRLLARQLGAERPFFGIQAHGINPDETPYATIGEMAARDIELIRQHQPHGPYTLWGYSFGARVAFETAWQLELAGEVVENLYLLAPGSPKLRDERVAAMNRKADFDNPGYLTILFSVFIGSITDPELERCLETVRDEESFVAFITGLNPALDDGLVRRITRIVAQTFEFTYTFSELQQRQLNAPVTIIKAQGDDYSFIENHGGFSAQPPTVLELMADHYSMLKAPGIDELTSVIQYQQSPPSLVG

[Multiple Choices]
A. Pigment biosynthesis. .
B. Alkaloid biosynthesis. .
C. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
D. L-threonine from L-aspartate: step 2/5. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the annotated indigoidine synthase. Its pathway annotation is “Pigment biosynthesis,” with experimental evidence cited to PubMed 11790734, supporting choice A for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is consistent with a large biosynthetic enzyme, which may help distinguish it from the small NAD-related or threonine-pathway enzymes in choices C and D. That general clue does not meaningfully distinguish pigment biosynthesis from alkaloid biosynthesis.


**Missing item-specific fact**

> The enzyme’s specific identity as indigoidine synthase and its product/pathway association are needed to select pigment biosynthesis over alkaloid biosynthesis.


**Reason**

> The sequence may support broad functional inference, but identifying this specific pathway requires item-specific knowledge not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence’s experimentally supported pathway annotation selects A; the other options are not equally supported.


### Important caveats

- The accession and annotation evidence are reviewer-only and were not provided to the evaluated model.
- The source sequence matches the benchmark sequence; the historical and current records identify the protein as indigoidine synthase.
- The author’s exact source snapshot is unknown, but the reviewed historical record also supports the pathway annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a large biosynthetic enzyme, which may help distinguish it from the small NAD-related or threonine-pathway enzymes in choices C and D. That general clue does not meaningfully distinguish pigment biosynthesis from alkaloid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme’s specific identity as indigoidine synthase and its product/pathway association are needed to select pigment biosynthesis over alkaloid biosynthesis.",
    "reason": "The sequence may support broad functional inference, but identifying this specific pathway requires item-specific knowledge not supplied in the question."
  },
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated indigoidine synthase. Its pathway annotation is “Pigment biosynthesis,” with experimental evidence cited to PubMed 11790734, supporting choice A for this sequence."
  },
  "important_caveats": [
    "The accession and annotation evidence are reviewer-only and were not provided to the evaluated model.",
    "The source sequence matches the benchmark sequence; the historical and current records identify the protein as indigoidine synthase.",
    "The author’s exact source snapshot is unknown, but the reviewed historical record also supports the pathway annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s experimentally supported pathway annotation selects A; the other options are not equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated indigoidine synthase. Its pathway annotation is “Pigment biosynthesis,” with experimental evidence cited to PubMed 11790734, supporting choice A for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is consistent with a large biosynthetic enzyme, which may help distinguish it from the small NAD-related or threonine-pathway enzymes in choices C and D. That general clue does not meaningfully distinguish pigment biosynthesis from alkaloid biosynthesis.",
    "missing_item_specific_fact": "The enzyme’s specific identity as indigoidine synthase and its product/pathway association are needed to select pigment biosynthesis over alkaloid biosynthesis.",
    "reason": "The sequence may support broad functional inference, but identifying this specific pathway requires item-specific knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence’s experimentally supported pathway annotation selects A; the other options are not equally supported."
  },
  "important_caveats": [
    "The accession and annotation evidence are reviewer-only and were not provided to the evaluated model.",
    "The source sequence matches the benchmark sequence; the historical and current records identify the protein as indigoidine synthase.",
    "The author’s exact source snapshot is unknown, but the reviewed historical record also supports the pathway annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9, IndC from Dickeya dadantii 3937) is annotated with PATHWAY: Pigment biosynthesis, supported by experimental evidence code ECO:0000269 (inferred from direct assay) from Reverchon et al. 2002 (PubMed:11790734), which characterized indigoidine biosynthetic genes and demonstrated the blue pigment's role in pathogenicity. The sequence matches exactly (SHA-256 confirmed). The annotation is experimentally grounded.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: a condensation-domain signature 'TSGSTGKPKG' (~position 530), adenylation-domain motifs ('YGPTEC', 'GAPVAN'), and a C-terminal thioesterase domain. NRPS enzymes synthesize peptide-type secondary metabolites (pigments such as indigoidine, violacein, prodigiosin; antibiotics; siderophores). Option C (NAD+ biosynthesis, a single-step transferase) and Option D (L-threonine biosynthesis step 2, homoserine dehydrogenase, ~450 aa) are eliminated because a 1488-aa multi-domain NRPS is categorically incompatible with those small single-domain enzymes. Option B (alkaloid biosynthesis) is disfavored because alkaloids are synthesized by entirely different enzymatic machinery (terpene synthases, P450 monooxygenases, methyltransferases), not NRPS assembly lines. Among the remaining choices, NRPS products that are colored compounds (e.g., indigoidine, a dipeptide of L-glutamine) fall squarely under pigment biosynthesis. Thus general NRPS biology plus elimination of incompatible options supports A over B, C, and D.


**Missing item-specific fact**

> Precise identification of this NRPS as indigoidine synthase (and thus the specific pigment) requires recognizing the exact sequence or knowing the product of IndC; however, the question can be answered by class-level reasoning without that specific fact.


**Reason**

> The NRPS domain architecture is extractable from sequence motifs, and general knowledge that NRPS products are peptide-type metabolites (not alkaloids, not single-step transferases, not amino-acid biosynthetic enzymes) meaningfully distinguishes A from B, C, and D. The argument does not require memorizing Q9L391's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are eliminated by enzyme class and size mismatch. B is disfavored because alkaloid biosynthesis does not employ NRPS assembly lines. A is the only option consistent with a large multi-domain NRPS producing a secondary metabolite among the listed categories. No other option is defensible.


### Important caveats

- The pathway annotation is experimentally supported (ECO:0000269) but the specific pigment identity (indigoidine) is not derivable from sequence motifs alone; the reasoning argument operates at the NRPS-class level.
- The UniProt entry was first publicly released 2025-02-05 (sequence version 2); the author's source snapshot is unknown. The 2002 primary paper predates the Swiss-Prot entry, so the underlying experimental data was available before the benchmark was constructed.
- NRPS enzymes also produce antibiotics and siderophores; the question's option set conveniently lacks those alternatives, making 'pigment biosynthesis' the only NRPS-compatible choice. A more challenging distractor set (e.g., 'antibiotic biosynthesis') could have made the question genuinely ambiguous without product-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: a condensation-domain signature 'TSGSTGKPKG' (~position 530), adenylation-domain motifs ('YGPTEC', 'GAPVAN'), and a C-terminal thioesterase domain. NRPS enzymes synthesize peptide-type secondary metabolites (pigments such as indigoidine, violacein, prodigiosin; antibiotics; siderophores). Option C (NAD+ biosynthesis, a single-step transferase) and Option D (L-threonine biosynthesis step 2, homoserine dehydrogenase, ~450 aa) are eliminated because a 1488-aa multi-domain NRPS is categorically incompatible with those small single-domain enzymes. Option B (alkaloid biosynthesis) is disfavored because alkaloids are synthesized by entirely different enzymatic machinery (terpene synthases, P450 monooxygenases, methyltransferases), not NRPS assembly lines. Among the remaining choices, NRPS products that are colored compounds (e.g., indigoidine, a dipeptide of L-glutamine) fall squarely under pigment biosynthesis. Thus general NRPS biology plus elimination of incompatible options supports A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this NRPS as indigoidine synthase (and thus the specific pigment) requires recognizing the exact sequence or knowing the product of IndC; however, the question can be answered by class-level reasoning without that specific fact.",
    "reason": "The NRPS domain architecture is extractable from sequence motifs, and general knowledge that NRPS products are peptide-type metabolites (not alkaloids, not single-step transferases, not amino-acid biosynthetic enzymes) meaningfully distinguishes A from B, C, and D. The argument does not require memorizing Q9L391's database entry."
  },
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9, IndC from Dickeya dadantii 3937) is annotated with PATHWAY: Pigment biosynthesis, supported by experimental evidence code ECO:0000269 (inferred from direct assay) from Reverchon et al. 2002 (PubMed:11790734), which characterized indigoidine biosynthetic genes and demonstrated the blue pigment's role in pathogenicity. The sequence matches exactly (SHA-256 confirmed). The annotation is experimentally grounded."
  },
  "important_caveats": [
    "The pathway annotation is experimentally supported (ECO:0000269) but the specific pigment identity (indigoidine) is not derivable from sequence motifs alone; the reasoning argument operates at the NRPS-class level.",
    "The UniProt entry was first publicly released 2025-02-05 (sequence version 2); the author's source snapshot is unknown. The 2002 primary paper predates the Swiss-Prot entry, so the underlying experimental data was available before the benchmark was constructed.",
    "NRPS enzymes also produce antibiotics and siderophores; the question's option set conveniently lacks those alternatives, making 'pigment biosynthesis' the only NRPS-compatible choice. A more challenging distractor set (e.g., 'antibiotic biosynthesis') could have made the question genuinely ambiguous without product-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are eliminated by enzyme class and size mismatch. B is disfavored because alkaloid biosynthesis does not employ NRPS assembly lines. A is the only option consistent with a large multi-domain NRPS producing a secondary metabolite among the listed categories. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9L391 (Indigoidine synthase, EC 4.3.3.9, IndC from Dickeya dadantii 3937) is annotated with PATHWAY: Pigment biosynthesis, supported by experimental evidence code ECO:0000269 (inferred from direct assay) from Reverchon et al. 2002 (PubMed:11790734), which characterized indigoidine biosynthetic genes and demonstrated the blue pigment's role in pathogenicity. The sequence matches exactly (SHA-256 confirmed). The annotation is experimentally grounded.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark non-ribosomal peptide synthetase (NRPS) domain motifs: a condensation-domain signature 'TSGSTGKPKG' (~position 530), adenylation-domain motifs ('YGPTEC', 'GAPVAN'), and a C-terminal thioesterase domain. NRPS enzymes synthesize peptide-type secondary metabolites (pigments such as indigoidine, violacein, prodigiosin; antibiotics; siderophores). Option C (NAD+ biosynthesis, a single-step transferase) and Option D (L-threonine biosynthesis step 2, homoserine dehydrogenase, ~450 aa) are eliminated because a 1488-aa multi-domain NRPS is categorically incompatible with those small single-domain enzymes. Option B (alkaloid biosynthesis) is disfavored because alkaloids are synthesized by entirely different enzymatic machinery (terpene synthases, P450 monooxygenases, methyltransferases), not NRPS assembly lines. Among the remaining choices, NRPS products that are colored compounds (e.g., indigoidine, a dipeptide of L-glutamine) fall squarely under pigment biosynthesis. Thus general NRPS biology plus elimination of incompatible options supports A over B, C, and D.",
    "missing_item_specific_fact": "Precise identification of this NRPS as indigoidine synthase (and thus the specific pigment) requires recognizing the exact sequence or knowing the product of IndC; however, the question can be answered by class-level reasoning without that specific fact.",
    "reason": "The NRPS domain architecture is extractable from sequence motifs, and general knowledge that NRPS products are peptide-type metabolites (not alkaloids, not single-step transferases, not amino-acid biosynthetic enzymes) meaningfully distinguishes A from B, C, and D. The argument does not require memorizing Q9L391's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are eliminated by enzyme class and size mismatch. B is disfavored because alkaloid biosynthesis does not employ NRPS assembly lines. A is the only option consistent with a large multi-domain NRPS producing a secondary metabolite among the listed categories. No other option is defensible."
  },
  "important_caveats": [
    "The pathway annotation is experimentally supported (ECO:0000269) but the specific pigment identity (indigoidine) is not derivable from sequence motifs alone; the reasoning argument operates at the NRPS-class level.",
    "The UniProt entry was first publicly released 2025-02-05 (sequence version 2); the author's source snapshot is unknown. The 2002 primary paper predates the Swiss-Prot entry, so the underlying experimental data was available before the benchmark was constructed.",
    "NRPS enzymes also produce antibiotics and siderophores; the question's option set conveniently lacks those alternatives, making 'pigment biosynthesis' the only NRPS-compatible choice. A more challenging distractor set (e.g., 'antibiotic biosynthesis') could have made the question genuinely ambiguous without product-specific knowledge."
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

**Accession:** `Q9L391` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
"Q9L391"
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11790734","source":"PubMed"}],"value":"Pigment biosynthesis"}]}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L391.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"citation":{"authors":["Reverchon S.","Rouanet C.","Expert D.","Nasser W."],"citationCrossReferences":[{"database":"PubMed","id":"11790734"},{"database":"DOI","id":"10.1128/jb.184.3.654-665.2002"}],"citationType":"journal article","firstPage":"654","id":"11790734","journal":"J. Bacteriol.","lastPage":"665","publicationDate":"2002","title":"Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi and role of this blue pigment in pathogenicity.","volume":"184"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAB87990.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"3937"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION AS AN INDIGOIDINE SYNTHASE","PATHWAY","INDUCTION","DOMAIN"]}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
ID   INDGS_DICD3             Reviewed;        1488 AA.
AC   Q9L391; E0SMH6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 107.
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};
GN   Name=indC {ECO:0000303|PubMed:11790734};
GN   OrderedLocusNames=Dda3937_00972 {ECO:0000312|EMBL:ADN00615.1};
OS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Pectobacteriaceae; Dickeya.
OX   NCBI_TaxID=198628;
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:CAB87990.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS AN INDIGOIDINE SYNTHASE,
RP   PATHWAY, INDUCTION, AND DOMAIN.
RC   STRAIN=3937;
RX   PubMed=11790734; DOI=10.1128/jb.184.3.654-665.2002;
RA   Reverchon S., Rouanet C., Expert D., Nasser W.;
RT   "Characterization of indigoidine biosynthetic genes in Erwinia chrysanthemi
RT   and role of this blue pigment in pathogenicity.";
RL   J. Bacteriol. 184:654-665(2002).
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
CC   -!- PATHWAY: Pigment biosynthesis. {ECO:0000269|PubMed:11790734}.
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
