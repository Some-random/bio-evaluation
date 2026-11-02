# catalytic_activity_0143

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — cholesterol(in) = cholesterol(out)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFVKNFIHKLKELKQKSLDKFANLLYDYGGYVYDRPCTFIICSLICCLLLTCGFYFKEHEKDIYKLYSISNSYAYETNETINDFFYKSRRCFILVESNVNLLKPKILRELQKFEEGTKDIEVDLSEINECKTNSELPPEQSHVAKELYKTLIQRSEENLKSGKINGSLFDYSDLDENGKSVLSLAGKENNDDTLIEGDNKNDEETSANNNNNEDDNNEDDNNEDDNNEDDNNENDNNNNNEDDNNNDDDDDEDNEEEDEEKQKSLREKLYRKIYEMLKKKKENIVLDENNPNVNFTDYKDDVFYPYQYIPPMLIKADRCKLQNVFGDKNLNIDLREASDGLKKQITYTLEDICEKKYGDCNFSSLFLYYEKGNGYIDYPIKVDNLDFYVNRRTYKEMMFKGILGNMVYEKSGSKYIIKSANAIMTVIPLLNSHTYEPYALAYEKKLIDYVRFYNLDDIIQDEETNDDNDPFIRFHVFTDRSLEDEVDRISKIDNLTRLLLLIGVLLIFMYALFNNVTSVLYRSKPLCAVMGIFCGFLGFLSGSGFLYFLGVKSVPPAETVPFLVIGVGVDDVFVILNSYSLLFMVKDNKKRIQMCLKDSALAITVTTLTNIIAFLISAISPFYSICAFSLFTASSLFFGYLMVLTFLLSFLCIEAKLEKKKRNIFTGTFHLFRSIFMKSSKKNKKENKENNIHDDGDNDNDEKKKDLSLEVKNNEDDYENISIYEWIHNLYLFEESINKKKKNAALVYASNNGMSSNLNNVNEDGFPNPSKIVSMEDVKKRNIKKDDAYINKEDEEGGGYYNKDDNKKKDILGKKQKKNNNNVTLVSKKGEDNELDVYYENLDEKTNDKYKMNNIKSSKLKYDNDKKDGAIINNRPSSDEEYKEEKDKNKINILNDVFNDITIKPNENILLDRGDVIKSSGYDSSYNDLQSSSLPNPSSNEVLNKTTMVYNETDLKDNKKEIKSSKKNVKDIKKSDMIHDDTYDIINSNNKNILLSSNEINNNSNNTNKFNNNSTELATKDTQQFINGHDKNIYLLSSHDNALFYKYIYEEPKGNIGKYFRSLVKNYYVPFLSSRFGKTIVYIMFTIIIAMSIYGCTLMKKGIKYDKAFPVDSYVRRFTTAKIKYFPDFGDFIEVYYFDKHFINKYRGLEKNTKEAASSFLYSDLTDRQIMNSPKINKNVHWENTNLQEELINMHNTLESQEFVTSVANGFTFFLNKNKSSLRKENPQEFYEIFANWLKKDFVGNLFKNDFVFLNGKLVAWRFHYFQKNVDDSEISSKWLKACKQITKLENHNVQMVCFHLSSIFNETDESIIEVTLINLGITILTILVVTAYIIKGFYSCVIIALIIFLIDLCIFGFMCLCGITMNIISMVILVLSVGFSIDHTSHIVQAFSHSMGRTRDEKMKESLHLMIGPVLHSGLSTWFVISTLFFSNKDFTVIFFQTLSLVLFFSITFSSMFLPVLLSSFGPLH

[Multiple Choices]
A. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
B. methylarsonous acid + AH2 + O2 = arsenite + methanol + A + H(+)
C. cholesterol(in) = cholesterol(out)
D. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
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

> The supplied sequence exactly matches the UniProt sequence for Plasmodium falciparum NCR1. Its catalytic-activity annotation gives cholesterol(in) = cholesterol(out), citing experimental evidence (ECO:0000269) from a 2024 publication. This supports C, though the cited study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic regions support a multipass membrane protein, making a transport choice more plausible than the soluble chemical reactions in A, B, and D.


**Missing item-specific fact**

> The sequence and prompt do not establish that this particular membrane protein transports cholesterol; that substrate specificity is the key item-specific fact needed to choose C.


**Reason**

> Sequence architecture and the choices provide a useful clue for transport, but not enough to identify cholesterol as the transported molecule. Selecting C requires protein-specific functional annotation or equivalent external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the matched protein's cited activity supports cholesterol transport rather than the chemical transformations in A, B, or D.


### Important caveats

- The annotation applies to an exact sequence match, but the author's source snapshot is unknown.
- The experimental evidence is cited by UniProt; the underlying primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic regions support a multipass membrane protein, making a transport choice more plausible than the soluble chemical reactions in A, B, and D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence and prompt do not establish that this particular membrane protein transports cholesterol; that substrate specificity is the key item-specific fact needed to choose C.",
    "reason": "Sequence architecture and the choices provide a useful clue for transport, but not enough to identify cholesterol as the transported molecule. Selecting C requires protein-specific functional annotation or equivalent external knowledge."
  },
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for Plasmodium falciparum NCR1. Its catalytic-activity annotation gives cholesterol(in) = cholesterol(out), citing experimental evidence (ECO:0000269) from a 2024 publication. This supports C, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The experimental evidence is cited by UniProt; the underlying primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched protein's cited activity supports cholesterol transport rather than the chemical transformations in A, B, or D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for Plasmodium falciparum NCR1. Its catalytic-activity annotation gives cholesterol(in) = cholesterol(out), citing experimental evidence (ECO:0000269) from a 2024 publication. This supports C, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic regions support a multipass membrane protein, making a transport choice more plausible than the soluble chemical reactions in A, B, and D.",
    "missing_item_specific_fact": "The sequence and prompt do not establish that this particular membrane protein transports cholesterol; that substrate specificity is the key item-specific fact needed to choose C.",
    "reason": "Sequence architecture and the choices provide a useful clue for transport, but not enough to identify cholesterol as the transported molecule. Selecting C requires protein-specific functional annotation or equivalent external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the matched protein's cited activity supports cholesterol transport rather than the chemical transformations in A, B, or D."
  },
  "important_caveats": [
    "The annotation applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The experimental evidence is cited by UniProt; the underlying primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8I266 (PfNCR1, Plasmodium falciparum Niemann-Pick type C1-related protein) explicitly annotates the catalytic activity as 'cholesterol(in) = cholesterol(out)' (Rhea:RHEA:39747) with direct experimental evidence (ECO:0000269, PubMed:39693420). The 2024 Sci. Adv. paper (Zhang et al.) provides cryo-EM structures (2.98 Å) in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol-export function. The 2019 eLife paper (Istvan et al.) established the functional role. The benchmark sequence SHA256 matches the UniProt sequence exactly (1470 aa).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1470-aa sequence contains numerous long hydrophobic stretches (e.g., regions around residues 30-50, 350-450, 1200-1470) indicating a multi-pass transmembrane protein, which immediately eliminates options A (cytoplasmic ACP synthase), B (soluble arsenite oxidoreductase), and D (glycoside phosphorylase). The domain architecture—multiple TM helices flanking a large lumenal/extracellular domain with conserved NPC1-family motifs—is recognizable as belonging to the Niemann-Pick type C1 (NPC1) superfamily. NPC1/NCR1 proteins are well-established cholesterol transporters/exporters in eukaryotic cells (a standard fact in lipid biology). Thus, recognizing the NPC1 domain fold and applying family-level functional knowledge (NPC1 → cholesterol transport) is sufficient to select C.


**Missing item-specific fact**

> None critical. The NPC1 domain is a well-known protein family with a defined structural fold, and its role in cholesterol trafficking is general textbook biochemistry. The specific Plasmodium NCR1 context adds detail but is not strictly required to eliminate the three non-transporter distractors.


**Reason**

> A model with knowledge of protein domain architecture can identify the multi-TM topology and NPC1-like domain organization from the sequence, then apply general knowledge that NPC1-family proteins mediate cholesterol transport. The three distractors describe small-molecule enzymes (ACP synthase, arsenite oxidoreductase, phosphorylase) with completely different domain architectures and no transmembrane segments, making them clearly incompatible with the observed sequence topology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe soluble enzymes (ACP synthase, arsenite-related oxidoreductase, phosphorylase) with no transmembrane topology, while the sequence clearly encodes a large multi-pass membrane protein. Option C is the only cholesterol-transport reaction and the only one consistent with an NPC1-family membrane protein. No ambiguity among choices.


### Important caveats

- The NPC1 domain recognition from raw 1470-aa sequence without computational domain-prediction tools is non-trivial but feasible for a model trained on protein families; the multi-TM topology alone already eliminates three of four options.
- The UniProt annotation was first integrated on 2025-06-18; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying 2019 and 2024 publications predate the cutoff.
- The catalytic activity annotation uses ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational support.
- The term 'catalytic activity' for a transporter reaction is a UniProt convention; NCR1 is a transporter, not a classical enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1470-aa sequence contains numerous long hydrophobic stretches (e.g., regions around residues 30-50, 350-450, 1200-1470) indicating a multi-pass transmembrane protein, which immediately eliminates options A (cytoplasmic ACP synthase), B (soluble arsenite oxidoreductase), and D (glycoside phosphorylase). The domain architecture—multiple TM helices flanking a large lumenal/extracellular domain with conserved NPC1-family motifs—is recognizable as belonging to the Niemann-Pick type C1 (NPC1) superfamily. NPC1/NCR1 proteins are well-established cholesterol transporters/exporters in eukaryotic cells (a standard fact in lipid biology). Thus, recognizing the NPC1 domain fold and applying family-level functional knowledge (NPC1 → cholesterol transport) is sufficient to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The NPC1 domain is a well-known protein family with a defined structural fold, and its role in cholesterol trafficking is general textbook biochemistry. The specific Plasmodium NCR1 context adds detail but is not strictly required to eliminate the three non-transporter distractors.",
    "reason": "A model with knowledge of protein domain architecture can identify the multi-TM topology and NPC1-like domain organization from the sequence, then apply general knowledge that NPC1-family proteins mediate cholesterol transport. The three distractors describe small-molecule enzymes (ACP synthase, arsenite oxidoreductase, phosphorylase) with completely different domain architectures and no transmembrane segments, making them clearly incompatible with the observed sequence topology."
  },
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8I266 (PfNCR1, Plasmodium falciparum Niemann-Pick type C1-related protein) explicitly annotates the catalytic activity as 'cholesterol(in) = cholesterol(out)' (Rhea:RHEA:39747) with direct experimental evidence (ECO:0000269, PubMed:39693420). The 2024 Sci. Adv. paper (Zhang et al.) provides cryo-EM structures (2.98 Å) in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol-export function. The 2019 eLife paper (Istvan et al.) established the functional role. The benchmark sequence SHA256 matches the UniProt sequence exactly (1470 aa)."
  },
  "important_caveats": [
    "The NPC1 domain recognition from raw 1470-aa sequence without computational domain-prediction tools is non-trivial but feasible for a model trained on protein families; the multi-TM topology alone already eliminates three of four options.",
    "The UniProt annotation was first integrated on 2025-06-18; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying 2019 and 2024 publications predate the cutoff.",
    "The catalytic activity annotation uses ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational support.",
    "The term 'catalytic activity' for a transporter reaction is a UniProt convention; NCR1 is a transporter, not a classical enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe soluble enzymes (ACP synthase, arsenite-related oxidoreductase, phosphorylase) with no transmembrane topology, while the sequence clearly encodes a large multi-pass membrane protein. Option C is the only cholesterol-transport reaction and the only one consistent with an NPC1-family membrane protein. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8I266 (PfNCR1, Plasmodium falciparum Niemann-Pick type C1-related protein) explicitly annotates the catalytic activity as 'cholesterol(in) = cholesterol(out)' (Rhea:RHEA:39747) with direct experimental evidence (ECO:0000269, PubMed:39693420). The 2024 Sci. Adv. paper (Zhang et al.) provides cryo-EM structures (2.98 Å) in complex with cholesterol and a synthetic inhibitor, confirming the cholesterol-export function. The 2019 eLife paper (Istvan et al.) established the functional role. The benchmark sequence SHA256 matches the UniProt sequence exactly (1470 aa).",
    "evidence_ids": ["C5", "C7", "H5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1470-aa sequence contains numerous long hydrophobic stretches (e.g., regions around residues 30-50, 350-450, 1200-1470) indicating a multi-pass transmembrane protein, which immediately eliminates options A (cytoplasmic ACP synthase), B (soluble arsenite oxidoreductase), and D (glycoside phosphorylase). The domain architecture—multiple TM helices flanking a large lumenal/extracellular domain with conserved NPC1-family motifs—is recognizable as belonging to the Niemann-Pick type C1 (NPC1) superfamily. NPC1/NCR1 proteins are well-established cholesterol transporters/exporters in eukaryotic cells (a standard fact in lipid biology). Thus, recognizing the NPC1 domain fold and applying family-level functional knowledge (NPC1 → cholesterol transport) is sufficient to select C.",
    "missing_item_specific_fact": "None critical. The NPC1 domain is a well-known protein family with a defined structural fold, and its role in cholesterol trafficking is general textbook biochemistry. The specific Plasmodium NCR1 context adds detail but is not strictly required to eliminate the three non-transporter distractors.",
    "reason": "A model with knowledge of protein domain architecture can identify the multi-TM topology and NPC1-like domain organization from the sequence, then apply general knowledge that NPC1-family proteins mediate cholesterol transport. The three distractors describe small-molecule enzymes (ACP synthase, arsenite oxidoreductase, phosphorylase) with completely different domain architectures and no transmembrane segments, making them clearly incompatible with the observed sequence topology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe soluble enzymes (ACP synthase, arsenite-related oxidoreductase, phosphorylase) with no transmembrane topology, while the sequence clearly encodes a large multi-pass membrane protein. Option C is the only cholesterol-transport reaction and the only one consistent with an NPC1-family membrane protein. No ambiguity among choices."
  },
  "important_caveats": [
    "The NPC1 domain recognition from raw 1470-aa sequence without computational domain-prediction tools is non-trivial but feasible for a model trained on protein families; the multi-TM topology alone already eliminates three of four options.",
    "The UniProt annotation was first integrated on 2025-06-18; if the benchmark was constructed before that date, the annotation may not have been available in the author's source snapshot, though the underlying 2019 and 2024 publications predate the cutoff.",
    "The catalytic activity annotation uses ECO:0000269 (direct assay evidence), indicating experimental rather than purely computational support.",
    "The term 'catalytic activity' for a transporter reaction is a UniProt convention; NCR1 is a transporter, not a classical enzyme."
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

**Accession:** `Q8I266` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 124. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
"Q8I266"
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39693420","source":"PubMed"}],"name":"cholesterol(in) = cholesterol(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:39747"},{"database":"ChEBI","id":"CHEBI:16113"}]}}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"citation":{"authors":["Istvan E.S.","Das S.","Bhatnagar S.","Beck J.R.","Owen E.","Llinas M.","Ganesan S.M.","Niles J.C.","Winzeler E.","Vaidya A.B.","Goldberg D.E."],"citationCrossReferences":[{"database":"PubMed","id":"30888318"},{"database":"DOI","id":"10.7554/elife.40529"}],"citationType":"journal article","firstPage":"0","id":"30888318","journal":"Elife","lastPage":"0","publicationDate":"2019","title":"Plasmodium Niemann-Pick type C1-related protein is a druggable target required for parasite membrane homeostasis.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF ALA-1108; ALA-1208 AND PHE-1436"]}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I266.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:00.862431+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Lyu M.","Han X.","Bandara S.","Cui M.","Istvan E.S.","Geng X.","Tringides M.L.","Gregor W.D.","Miyagi M.","Oberstaller J.","Adams J.H.","Zhang Y.","Nieman M.T.","von Lintig J.","Goldberg D.E.","Yu E.W."],"citationCrossReferences":[{"database":"PubMed","id":"39693420"},{"database":"DOI","id":"10.1126/sciadv.adq6651"}],"citationType":"journal article","firstPage":"eadq6651","id":"39693420","journal":"Sci. Adv.","lastPage":"eadq6651","publicationDate":"2024","title":"The Plasmodium falciparum NCR1 transporter is an antimalarial target that exports cholesterol from the parasite's plasma membrane.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8V0G","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V12","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8V1G","source":"PDB"}],"referenceNumber":4,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108","FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","GLYCOSYLATION AT ASN-165 AND ASN-294"]}
```

Source SHA-256: `48e01533a9789c0a87e7d04e741324e48211158647115ac991ae6fe921695917`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 58-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
RN   [4] {ECO:0007744|PDB:8V0G, ECO:0007744|PDB:8V12, ECO:0007744|PDB:8V1G}
RP   STRUCTURE BY ELECTRON MICROSCOPY (2.98 ANGSTROMS) IN COMPLEX WITH
RP   CHOLESTEROL AND SYNTHETIC INHIBITOR MMV009108, FUNCTION, TRANSPORTER
RP   ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, AND
RP   GLYCOSYLATION AT ASN-165 AND ASN-294.
RX   PubMed=39693420; DOI=10.1126/sciadv.adq6651;
RA   Zhang Z., Lyu M., Han X., Bandara S., Cui M., Istvan E.S., Geng X.,
RA   Tringides M.L., Gregor W.D., Miyagi M., Oberstaller J., Adams J.H.,
RA   Zhang Y., Nieman M.T., von Lintig J., Goldberg D.E., Yu E.W.;
RT   "The Plasmodium falciparum NCR1 transporter is an antimalarial target that
RT   exports cholesterol from the parasite's plasma membrane.";
RL   Sci. Adv. 10:eadq6651-eadq6651(2024).
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I266?format=txt&versions=124)  
**Locator:** `lines 76-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 124 / 1.  
**Retrieved:** 2026-11-02T04:32:03.056916+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cholesterol(in) = cholesterol(out); Xref=Rhea:RHEA:39747,
CC         ChEBI:CHEBI:16113; Evidence={ECO:0000269|PubMed:39693420};
```

Source SHA-256: `5da276982e783be3920b7838caf1b7888eb5ee16832af6b303a9fbd38dd05eb7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
