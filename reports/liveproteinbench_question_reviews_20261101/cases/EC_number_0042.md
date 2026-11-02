# EC_number_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 4.3.3.9

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
A. 4.3.1.24
B. 4.3.3.9
C. 4.4.1.11
D. 3.4.21.62
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

> The supplied sequence exactly matches the 1488-aa sequence in UniProt entry Q9L391. That entry annotates the protein as indigoidine synthase with EC 4.3.3.9 and gives the corresponding catalytic reaction, citing PubMed 11790734. This supports choice B, though the evidence here is a database annotation citing a publication, not an independent review of the experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence may be consistent with a large biosynthetic enzyme rather than a protease, but that broad inference does not establish its specific reaction or distinguish EC 4.3.3.9 from other lyase EC choices.


**Missing item-specific fact**

> Identifying this exact protein as indigoidine synthase, and knowing its catalyzed reaction and EC assignment.


**Reason**

> The exact functional assignment is not supplied in the question. Choosing B requires an item-specific annotation, experimental knowledge, or sequence recognition tied to such knowledge; general sequence-based reasoning alone does not establish the complete four-part EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched database record assigns EC 4.3.3.9; the supplied reviewer evidence does not support another listed choice.


### Important caveats

- Reviewer-only annotations establish support for the key but were not available to the evaluated model.
- The exact author data-source snapshot is unknown, although the sequence matches the historical and current UniProt record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence may be consistent with a large biosynthetic enzyme rather than a protease, but that broad inference does not establish its specific reaction or distinguish EC 4.3.3.9 from other lyase EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this exact protein as indigoidine synthase, and knowing its catalyzed reaction and EC assignment.",
    "reason": "The exact functional assignment is not supplied in the question. Choosing B requires an item-specific annotation, experimental knowledge, or sequence recognition tied to such knowledge; general sequence-based reasoning alone does not establish the complete four-part EC number."
  },
  "case_id": "EC_number_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1488-aa sequence in UniProt entry Q9L391. That entry annotates the protein as indigoidine synthase with EC 4.3.3.9 and gives the corresponding catalytic reaction, citing PubMed 11790734. This supports choice B, though the evidence here is a database annotation citing a publication, not an independent review of the experiment."
  },
  "important_caveats": [
    "Reviewer-only annotations establish support for the key but were not available to the evaluated model.",
    "The exact author data-source snapshot is unknown, although the sequence matches the historical and current UniProt record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched database record assigns EC 4.3.3.9; the supplied reviewer evidence does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1488-aa sequence in UniProt entry Q9L391. That entry annotates the protein as indigoidine synthase with EC 4.3.3.9 and gives the corresponding catalytic reaction, citing PubMed 11790734. This supports choice B, though the evidence here is a database annotation citing a publication, not an independent review of the experiment.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence may be consistent with a large biosynthetic enzyme rather than a protease, but that broad inference does not establish its specific reaction or distinguish EC 4.3.3.9 from other lyase EC choices.",
    "missing_item_specific_fact": "Identifying this exact protein as indigoidine synthase, and knowing its catalyzed reaction and EC assignment.",
    "reason": "The exact functional assignment is not supplied in the question. Choosing B requires an item-specific annotation, experimental knowledge, or sequence recognition tied to such knowledge; general sequence-based reasoning alone does not establish the complete four-part EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched database record assigns EC 4.3.3.9; the supplied reviewer evidence does not support another listed choice."
  },
  "important_caveats": [
    "Reviewer-only annotations establish support for the key but were not available to the evaluated model.",
    "The exact author data-source snapshot is unknown, although the sequence matches the historical and current UniProt record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9L391 (Indigoidine synthase, INDGS_DICD3, 1488 AA) exactly (SHA256 confirmed). The UniProt entry annotates EC 4.3.3.9 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:11790734 (Reverchon et al., 2002, J. Bacteriol. 184:654-665), which characterized indigoidine biosynthetic genes in Erwinia chrysanthemi. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is annotated with Rhea cross-references. The evidence code ECO:0000305 indicates the annotation was made by similarity to characterized homologs rather than direct enzymatic assay of this specific protein, but the primary literature supports the function assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable NRPS (nonribosomal peptide synthetase) domain motifs: the adenylation-domain signature 'TSGSTGKPKG' (residues ~490-500), the 'YGPTEC' motif, a peptidyl-carrier-protein (PCP) region with the 'GHHQSK' phosphopantetheinylation motif, and condensation-domain motifs ('GHRTGPYYFFIGG'). This multi-domain A-PC-C architecture is incompatible with all three distractors: (1) Arginine deiminase (EC 4.3.1.24) is a ~40-50 kDa single-domain folditin-type enzyme with no NRPS domains; (2) Cysteine conjugate beta-lyase (EC 4.4.1.11) is a PLP-dependent enzyme with a TIM-barrel fold, not an NRPS; (3) Serine protease (EC 3.4.21.62, PCSK5) requires a His-Asp-Ser catalytic triad in a subtilisin-like fold, absent here. By elimination of architecturally incompatible options, B (4.3.3.9, indigoidine synthase—a standalone NRPS-like enzyme) is the only consistent choice.


**Missing item-specific fact**

> None strictly required for elimination-based reasoning, though positively confirming EC 4.3.3.9 (rather than a generic NRPS EC 6.3.2.-) from the sequence alone would require knowing that indigoidine synthase is uniquely classified under EC 4 (lyases) rather than EC 6 (ligases), a peculiar taxonomic choice in the EC scheme.


**Reason**

> The NRPS domain architecture is directly identifiable from well-known consensus motifs in the sequence. General knowledge that arginine deiminase, cysteine conjugate beta-lyase, and serine endopeptidases lack NRPS domains provides a concrete elimination argument. The reasoning does not require recalling the exact database entry for Q9L391; it relies on domain-architecture compatibility, which is standard structural biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors represent entirely different enzyme folds and catalytic mechanisms (simple hydrolase, PLP-dependent lyase, serine protease) that are architecturally incompatible with the clearly identifiable NRPS multi-domain structure in the sequence. Only one option (B) is consistent with the observed domain architecture.


### Important caveats

- The UniProt evidence code ECO:0000305 (inferred by similarity) indicates the EC annotation was assigned by homology to characterized indigoidine synthase homologs rather than by direct in vitro enzymatic assay of Q9L391 itself.
- The EC 4.3.3.9 classification of indigoidine synthase as a lyase (rather than a ligase, EC 6) is a somewhat unusual taxonomic choice in the EC scheme; a model relying solely on 'NRPS = ligase' reasoning might struggle to positively identify EC 4.3.3.9 without the elimination argument.
- The reasoning-based elimination works because of the specific distractor set; an alternative NRPS-like enzyme with a different EC number as a distractor would break the argument.
- The UniProt entry was first released 2025-02-05 (sequence version 2); the author's source snapshot date is unknown, but the sequence matches both current and archived (v107) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable NRPS (nonribosomal peptide synthetase) domain motifs: the adenylation-domain signature 'TSGSTGKPKG' (residues ~490-500), the 'YGPTEC' motif, a peptidyl-carrier-protein (PCP) region with the 'GHHQSK' phosphopantetheinylation motif, and condensation-domain motifs ('GHRTGPYYFFIGG'). This multi-domain A-PC-C architecture is incompatible with all three distractors: (1) Arginine deiminase (EC 4.3.1.24) is a ~40-50 kDa single-domain folditin-type enzyme with no NRPS domains; (2) Cysteine conjugate beta-lyase (EC 4.4.1.11) is a PLP-dependent enzyme with a TIM-barrel fold, not an NRPS; (3) Serine protease (EC 3.4.21.62, PCSK5) requires a His-Asp-Ser catalytic triad in a subtilisin-like fold, absent here. By elimination of architecturally incompatible options, B (4.3.3.9, indigoidine synthase—a standalone NRPS-like enzyme) is the only consistent choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning, though positively confirming EC 4.3.3.9 (rather than a generic NRPS EC 6.3.2.-) from the sequence alone would require knowing that indigoidine synthase is uniquely classified under EC 4 (lyases) rather than EC 6 (ligases), a peculiar taxonomic choice in the EC scheme.",
    "reason": "The NRPS domain architecture is directly identifiable from well-known consensus motifs in the sequence. General knowledge that arginine deiminase, cysteine conjugate beta-lyase, and serine endopeptidases lack NRPS domains provides a concrete elimination argument. The reasoning does not require recalling the exact database entry for Q9L391; it relies on domain-architecture compatibility, which is standard structural biology knowledge."
  },
  "case_id": "EC_number_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9L391 (Indigoidine synthase, INDGS_DICD3, 1488 AA) exactly (SHA256 confirmed). The UniProt entry annotates EC 4.3.3.9 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:11790734 (Reverchon et al., 2002, J. Bacteriol. 184:654-665), which characterized indigoidine biosynthetic genes in Erwinia chrysanthemi. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is annotated with Rhea cross-references. The evidence code ECO:0000305 indicates the annotation was made by similarity to characterized homologs rather than direct enzymatic assay of this specific protein, but the primary literature supports the function assignment."
  },
  "important_caveats": [
    "The UniProt evidence code ECO:0000305 (inferred by similarity) indicates the EC annotation was assigned by homology to characterized indigoidine synthase homologs rather than by direct in vitro enzymatic assay of Q9L391 itself.",
    "The EC 4.3.3.9 classification of indigoidine synthase as a lyase (rather than a ligase, EC 6) is a somewhat unusual taxonomic choice in the EC scheme; a model relying solely on 'NRPS = ligase' reasoning might struggle to positively identify EC 4.3.3.9 without the elimination argument.",
    "The reasoning-based elimination works because of the specific distractor set; an alternative NRPS-like enzyme with a different EC number as a distractor would break the argument.",
    "The UniProt entry was first released 2025-02-05 (sequence version 2); the author's source snapshot date is unknown, but the sequence matches both current and archived (v107) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors represent entirely different enzyme folds and catalytic mechanisms (simple hydrolase, PLP-dependent lyase, serine protease) that are architecturally incompatible with the clearly identifiable NRPS multi-domain structure in the sequence. Only one option (B) is consistent with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9L391 (Indigoidine synthase, INDGS_DICD3, 1488 AA) exactly (SHA256 confirmed). The UniProt entry annotates EC 4.3.3.9 with evidence code ECO:0000305 (inferred by similarity) citing PubMed:11790734 (Reverchon et al., 2002, J. Bacteriol. 184:654-665), which characterized indigoidine biosynthetic genes in Erwinia chrysanthemi. The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is annotated with Rhea cross-references. The evidence code ECO:0000305 indicates the annotation was made by similarity to characterized homologs rather than direct enzymatic assay of this specific protein, but the primary literature supports the function assignment.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable NRPS (nonribosomal peptide synthetase) domain motifs: the adenylation-domain signature 'TSGSTGKPKG' (residues ~490-500), the 'YGPTEC' motif, a peptidyl-carrier-protein (PCP) region with the 'GHHQSK' phosphopantetheinylation motif, and condensation-domain motifs ('GHRTGPYYFFIGG'). This multi-domain A-PC-C architecture is incompatible with all three distractors: (1) Arginine deiminase (EC 4.3.1.24) is a ~40-50 kDa single-domain folditin-type enzyme with no NRPS domains; (2) Cysteine conjugate beta-lyase (EC 4.4.1.11) is a PLP-dependent enzyme with a TIM-barrel fold, not an NRPS; (3) Serine protease (EC 3.4.21.62, PCSK5) requires a His-Asp-Ser catalytic triad in a subtilisin-like fold, absent here. By elimination of architecturally incompatible options, B (4.3.3.9, indigoidine synthase—a standalone NRPS-like enzyme) is the only consistent choice.",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning, though positively confirming EC 4.3.3.9 (rather than a generic NRPS EC 6.3.2.-) from the sequence alone would require knowing that indigoidine synthase is uniquely classified under EC 4 (lyases) rather than EC 6 (ligases), a peculiar taxonomic choice in the EC scheme.",
    "reason": "The NRPS domain architecture is directly identifiable from well-known consensus motifs in the sequence. General knowledge that arginine deiminase, cysteine conjugate beta-lyase, and serine endopeptidases lack NRPS domains provides a concrete elimination argument. The reasoning does not require recalling the exact database entry for Q9L391; it relies on domain-architecture compatibility, which is standard structural biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors represent entirely different enzyme folds and catalytic mechanisms (simple hydrolase, PLP-dependent lyase, serine protease) that are architecturally incompatible with the clearly identifiable NRPS multi-domain structure in the sequence. Only one option (B) is consistent with the observed domain architecture."
  },
  "important_caveats": [
    "The UniProt evidence code ECO:0000305 (inferred by similarity) indicates the EC annotation was assigned by homology to characterized indigoidine synthase homologs rather than by direct in vitro enzymatic assay of Q9L391 itself.",
    "The EC 4.3.3.9 classification of indigoidine synthase as a lyase (rather than a ligase, EC 6) is a somewhat unusual taxonomic choice in the EC scheme; a model relying solely on 'NRPS = ligase' reasoning might struggle to positively identify EC 4.3.3.9 without the elimination argument.",
    "The reasoning-based elimination works because of the specific distractor set; an alternative NRPS-like enzyme with a different EC number as a distractor would break the argument.",
    "The UniProt entry was first released 2025-02-05 (sequence version 2); the author's source snapshot date is unknown, but the sequence matches both current and archived (v107) records."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:04.012566+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81500"}}],"reaction":{"ecNumber":"4.3.3.9","evidences":[{"evidenceCode":"ECO:0000305","id":"11790734","source":"PubMed"}],"name":"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81499"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:79296"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `9c8d2e104ff5ea8d2790f76bf7752253a7253250c3262d0e137e123b56bf3282`.

### Evidence C8

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
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
DE   RecName: Full=Indigoidine synthase {ECO:0000305};
DE            EC=4.3.3.9 {ECO:0000305|PubMed:11790734};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

### Evidence H3

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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L391?format=txt&versions=107)  
**Locator:** `lines 44-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 2.  
**Retrieved:** 2026-11-02T04:33:06.750542+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2
CC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;
CC         Evidence={ECO:0000305|PubMed:11790734};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;
CC         Evidence={ECO:0000305|PubMed:11790734};
```

Source SHA-256: `8c41c7f4d955ab759c8a49f6d87170be08a554ecadfde2e1b065f5c3489df877`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
