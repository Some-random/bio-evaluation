# GO_biological_process_0144

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — lysosome fission

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAATSQVSSLLDLIMSLLDTATTYQHQESVKNEVAESLKTIGSHQPNVLLTACHQYLLQNPKLGAFKRAFVLQTISICVDNCEVVSKLDEQIIMLIINLATQEMNMTKDTDVEWAESSMEVLVTLAKNTRFVSHVIDAILQKFPPGQTTSPHRYIVLTMATIAVHNPFGLVPFLTDILSRTVPLLQHVKTDPLRCAWARAICSFCEAVRECETERPKEASEEYIGDHSRPNSASGHCQEVSNRATYSDQTEAVYDVIFSWIYSKDPKTRGEAAECVGELCLMIKQTRLVEDVKKIVTNMIPLYRKSYNESHMITQGICRFLEAACVDETCPLEPYLEDILNALFPNACLDPDDTTVTLSTQAIKNHSEAFRCFDVAATRFADRIVYYLLHKMQNVADSQKLGAINVLRHLLNATGQHMEDKRSLLTMGLKKLLAAENTTSIRVKRAIVQLCVALADHSYVDAEGGDYVIAFLVRNLVGPTEQESAAKKVEVDVAGLNQLRTQCAQALYTIANTCVCATKLLWPYLLEFICCERYTPVVGDLCKCLRTLVSREVEAGRKMDYVTGFDNPKVAGRHAVFARLFTSFCNAPLNGLLTRRAREAGGLIQAVAPWFHPSMEGPAARWSEKLEPLLDELSTTVSSGDSAPAELRGRKIARWHEACLDWLSACVAVVPEGDWRQDLAAAMGKQLDMYKELSDEKSFLLRCLGVTLARITAKQFVIDHMMLMFKSASHSVLTERQGCARGVGSIATSHMDLILIELENVSKWEHARKSSGIFGFIKDTMPIRQYPDIEMIHLRATLMLCYGHVVMACSLDTITQRLQNTIIVFLRNYFANSKQETVVREAMLETMRLIATAVHPSRIGGEWKFEARNELLAYAKDYLNGETPEWLTSSLRLLACKTTAALVQLEPPLSPADIEDIGTVLTRQILPMQREKSGLKTLAFDIFDYASSSVFSTFSGSSSSHTNIYMTPPLTANSVAEGPNGTPIHQRHRGIGGKMEDDESATIMDATMHQYGLALEQIVRMAPTTQTIMILLKILLPYYGKQADHERIRAVDMTVLVLRVYYECAEDISLGHASDFEPLSSLLGRLAPRLIDLLAHVRLQALSAIHWTLRLAYMHKGHGRDADQSLFSYSGFVEKYLTSGDVKLEGQKEKLAIEAIAQIIEYRLPQSQMQIYLSAIFEMLTDRQSHVSSAAAQLLTYAVMARGATLNAEAEILVTKMVEKLADIHHCVQTNTDVLAALVAFAVHQQQAVCDVLFKQPLPYSINITDAWECLSRDKLLFAVILDHLTELLGASLDQPFELMDSGGGVSAKVVNVEPCTYVAVLAEVVKNGEPESALMERLPLILTLLIHFICSVSDTQFPVMQKEGSKNPLIITPDLRRAAEKPAGMAVAAIKNLLNRTRSNMVIEDMNQARAWTDCLDKDSFIQAITVFIRSLVEQRPAWVSPLAKTMEEYANSESEPRRLAAVIIAASLIRRSTSENGEFNEQLLVKCIRRLEDSLTDPSLRIRKLCVKGLGELSECSSTDVISRFVHMAVEAAMSGLDDHGDRKDTVAIESIMALNKLVQLTNNDQLKSILPLVLLKIRPCFEKDSHTLRAASFSLFGELGSRVGENSEEFRGHLHTNIVSLLLHLNDDFEEVRQNCANSIYRLHGLLTSPNASICIERELKDGKQPASYNLFIKDFASILANSFPDRINQYALATSNYFKSSSARIRCNAAHLTGCLLDGLTAPLRATISRELVFTGLVALLKDSEDVNVRISATRAIANLHDFH

[Multiple Choices]
A. chromatin organization
B. carotenoid biosynthetic process
C. lysosome fission
D. negative stranded viral RNA replication
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

> The supplied sequence exactly matches the C. elegans HPO-27 entry, which identifies the protein as a lysosome fission factor. The entry links this function and the GO annotation for lysosome fission to a cited 2024 study, with experimental evidence codes (ECO:0000269 and IDA:UniProtKB).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence is consistent with a large HEAT-repeat protein, but that feature does not establish lysosome fission or meaningfully distinguish it from the other specific biological processes listed.


**Missing item-specific fact**

> The protein-specific identification of HPO-27 and its experimentally reported role in lysosome fission.


**Reason**

> Selecting C requires functional knowledge about this particular protein that is not provided by the sequence or task context. General sequence-based reasoning may make some distractors less plausible, but it does not identify lysosome fission.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and cited experimental evidence support lysosome fission; no other listed option has comparable support in the supplied evidence.


### Important caveats

- The accession and annotation evidence are reviewer-only and were not available to the evaluated model.
- The author’s exact source snapshot is unknown, although the sequence-matched historical UniProt entry available by the stated cutoff also supports the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a large HEAT-repeat protein, but that feature does not establish lysosome fission or meaningfully distinguish it from the other specific biological processes listed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification of HPO-27 and its experimentally reported role in lysosome fission.",
    "reason": "Selecting C requires functional knowledge about this particular protein that is not provided by the sequence or task context. General sequence-based reasoning may make some distractors less plausible, but it does not identify lysosome fission."
  },
  "case_id": "GO_biological_process_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the C. elegans HPO-27 entry, which identifies the protein as a lysosome fission factor. The entry links this function and the GO annotation for lysosome fission to a cited 2024 study, with experimental evidence codes (ECO:0000269 and IDA:UniProtKB)."
  },
  "important_caveats": [
    "The accession and annotation evidence are reviewer-only and were not available to the evaluated model.",
    "The author’s exact source snapshot is unknown, although the sequence-matched historical UniProt entry available by the stated cutoff also supports the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited experimental evidence support lysosome fission; no other listed option has comparable support in the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the C. elegans HPO-27 entry, which identifies the protein as a lysosome fission factor. The entry links this function and the GO annotation for lysosome fission to a cited 2024 study, with experimental evidence codes (ECO:0000269 and IDA:UniProtKB).",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence is consistent with a large HEAT-repeat protein, but that feature does not establish lysosome fission or meaningfully distinguish it from the other specific biological processes listed.",
    "missing_item_specific_fact": "The protein-specific identification of HPO-27 and its experimentally reported role in lysosome fission.",
    "reason": "Selecting C requires functional knowledge about this particular protein that is not provided by the sequence or task context. General sequence-based reasoning may make some distractors less plausible, but it does not identify lysosome fission."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited experimental evidence support lysosome fission; no other listed option has comparable support in the supplied evidence."
  },
  "important_caveats": [
    "The accession and annotation evidence are reviewer-only and were not available to the evaluated model.",
    "The author’s exact source snapshot is unknown, although the sequence-matched historical UniProt entry available by the stated cutoff also supports the annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry K8ERU3 (HPO-27_CAEEL) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0170064 (lysosome fission), supported by experimental evidence from PubMed:38538795 (Nature 2024). The FUNCTION comment explicitly states the protein is a 'Lysosome fission factor' recruited to lysosomes by rab-7 at scission sites. The sequence matches the benchmark input exactly (SHA256 confirmed). Evidence is experimental (ECO:0000269/ECO:0000314), not computational.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could eliminate B (carotenoid biosynthesis) and D (negative-stranded viral RNA replication) by recognizing that a long HEAT-repeat-containing eukaryotic protein lacks enzymatic motifs for terpene biosynthesis and lacks RdRp catalytic signatures. However, distinguishing A (chromatin organization) from C (lysosome fission) is not achievable through general sequence reasoning: HEAT repeats are a ubiquitous protein-protein interaction scaffold found in chromatin regulators (e.g., condensin, Mlh1), vesicle-trafficking factors, and many other process-specific proteins. No sequence motif in this 1768-aa HEAT-repeat protein uniquely predicts lysosome fission over chromatin organization.


**Missing item-specific fact**

> The specific experimental finding (Li et al., Nature 2024, PMID:38538795) that HPO-27 is recruited by rab-7 to lysosomal scission sites and homooligomerizes to mediate tubule constriction. This 2024 discovery established the lysosome fission role experimentally; it is not inferable from HEAT-repeat architecture or any general biological principle.


**Reason**

> The answer depends on knowing the specific 2024 experimental characterization of this C. elegans protein. While B and D can be excluded by broad biological reasoning (wrong domain architecture, wrong organism context), the A-vs-C distinction requires item-specific knowledge of this protein's experimentally determined function. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> Without specific knowledge of HPO-27, a model reasoning from HEAT-repeat architecture could plausibly assign chromatin organization (A), since many HEAT-repeat proteins participate in chromatin remodeling and assembly. The question wording ('primary biological process') does not provide contextual clues (e.g., subcellular localization, interaction partners) that would exclude A in favor of C. However, A is ultimately incorrect per experimental evidence.


### Important caveats

- The lysosome fission annotation (GO:0170064) is a relatively new GO term; the supporting Nature paper is from 2024. Models trained before mid-2024 would lack this annotation in their training data.
- The GO term GO:0170064 (lysosome fission) is itself recent (defined citing PMID:31171420 and PMID:38538795), meaning older ontology snapshots may not contain it.
- The UniProt entry was first released 2025-06-18; the functional annotation depends on a single primary reference (Nature 2024), though with IDA evidence code indicating direct experimental validation.
- The identity of the protein (accession K8ERU3) was inferred by the reviewer from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could eliminate B (carotenoid biosynthesis) and D (negative-stranded viral RNA replication) by recognizing that a long HEAT-repeat-containing eukaryotic protein lacks enzymatic motifs for terpene biosynthesis and lacks RdRp catalytic signatures. However, distinguishing A (chromatin organization) from C (lysosome fission) is not achievable through general sequence reasoning: HEAT repeats are a ubiquitous protein-protein interaction scaffold found in chromatin regulators (e.g., condensin, Mlh1), vesicle-trafficking factors, and many other process-specific proteins. No sequence motif in this 1768-aa HEAT-repeat protein uniquely predicts lysosome fission over chromatin organization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental finding (Li et al., Nature 2024, PMID:38538795) that HPO-27 is recruited by rab-7 to lysosomal scission sites and homooligomerizes to mediate tubule constriction. This 2024 discovery established the lysosome fission role experimentally; it is not inferable from HEAT-repeat architecture or any general biological principle.",
    "reason": "The answer depends on knowing the specific 2024 experimental characterization of this C. elegans protein. While B and D can be excluded by broad biological reasoning (wrong domain architecture, wrong organism context), the A-vs-C distinction requires item-specific knowledge of this protein's experimentally determined function. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning."
  },
  "case_id": "GO_biological_process_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry K8ERU3 (HPO-27_CAEEL) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0170064 (lysosome fission), supported by experimental evidence from PubMed:38538795 (Nature 2024). The FUNCTION comment explicitly states the protein is a 'Lysosome fission factor' recruited to lysosomes by rab-7 at scission sites. The sequence matches the benchmark input exactly (SHA256 confirmed). Evidence is experimental (ECO:0000269/ECO:0000314), not computational."
  },
  "important_caveats": [
    "The lysosome fission annotation (GO:0170064) is a relatively new GO term; the supporting Nature paper is from 2024. Models trained before mid-2024 would lack this annotation in their training data.",
    "The GO term GO:0170064 (lysosome fission) is itself recent (defined citing PMID:31171420 and PMID:38538795), meaning older ontology snapshots may not contain it.",
    "The UniProt entry was first released 2025-06-18; the functional annotation depends on a single primary reference (Nature 2024), though with IDA evidence code indicating direct experimental validation.",
    "The identity of the protein (accession K8ERU3) was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "Without specific knowledge of HPO-27, a model reasoning from HEAT-repeat architecture could plausibly assign chromatin organization (A), since many HEAT-repeat proteins participate in chromatin remodeling and assembly. The question wording ('primary biological process') does not provide contextual clues (e.g., subcellular localization, interaction partners) that would exclude A in favor of C. However, A is ultimately incorrect per experimental evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry K8ERU3 (HPO-27_CAEEL) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0170064 (lysosome fission), supported by experimental evidence from PubMed:38538795 (Nature 2024). The FUNCTION comment explicitly states the protein is a 'Lysosome fission factor' recruited to lysosomes by rab-7 at scission sites. The sequence matches the benchmark input exactly (SHA256 confirmed). Evidence is experimental (ECO:0000269/ECO:0000314), not computational.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could eliminate B (carotenoid biosynthesis) and D (negative-stranded viral RNA replication) by recognizing that a long HEAT-repeat-containing eukaryotic protein lacks enzymatic motifs for terpene biosynthesis and lacks RdRp catalytic signatures. However, distinguishing A (chromatin organization) from C (lysosome fission) is not achievable through general sequence reasoning: HEAT repeats are a ubiquitous protein-protein interaction scaffold found in chromatin regulators (e.g., condensin, Mlh1), vesicle-trafficking factors, and many other process-specific proteins. No sequence motif in this 1768-aa HEAT-repeat protein uniquely predicts lysosome fission over chromatin organization.",
    "missing_item_specific_fact": "The specific experimental finding (Li et al., Nature 2024, PMID:38538795) that HPO-27 is recruited by rab-7 to lysosomal scission sites and homooligomerizes to mediate tubule constriction. This 2024 discovery established the lysosome fission role experimentally; it is not inferable from HEAT-repeat architecture or any general biological principle.",
    "reason": "The answer depends on knowing the specific 2024 experimental characterization of this C. elegans protein. While B and D can be excluded by broad biological reasoning (wrong domain architecture, wrong organism context), the A-vs-C distinction requires item-specific knowledge of this protein's experimentally determined function. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "Without specific knowledge of HPO-27, a model reasoning from HEAT-repeat architecture could plausibly assign chromatin organization (A), since many HEAT-repeat proteins participate in chromatin remodeling and assembly. The question wording ('primary biological process') does not provide contextual clues (e.g., subcellular localization, interaction partners) that would exclude A in favor of C. However, A is ultimately incorrect per experimental evidence."
  },
  "important_caveats": [
    "The lysosome fission annotation (GO:0170064) is a relatively new GO term; the supporting Nature paper is from 2024. Models trained before mid-2024 would lack this annotation in their training data.",
    "The GO term GO:0170064 (lysosome fission) is itself recent (defined citing PMID:31171420 and PMID:38538795), meaning older ontology snapshots may not contain it.",
    "The UniProt entry was first released 2025-06-18; the functional annotation depends on a single primary reference (Nature 2024), though with IDA evidence code indicating direct experimental validation.",
    "The identity of the protein (accession K8ERU3) was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
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

**Accession:** `K8ERU3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 72. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
"K8ERU3"
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38538795","source":"PubMed"}],"value":"Lysosome fission factor (PubMed:38538795). Recruited to lysosomes by rab-7 at scission sites and homooligomerizes to mediate the constriction and scission of lysosomal tubules (PubMed:38538795). May sever membranes by inserting amphipathic helices into one bilayer leaflet (PubMed:38538795). Lysosome fission is required to maintain their steady-state number, shape, size, composition and function, and to accomplish regeneration (PubMed:38538795)"}]}
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38538795","source":"PubMed"}],"id":"GO:0170064","properties":[{"key":"GoTerm","value":"P:lysosome fission"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
{"citation":{"authors":["Li L.","Liu X.","Yang S.","Li M.","Wu Y.","Hu S.","Wang W.","Jiang A.","Zhang Q.","Zhang J.","Ma X.","Hu J.","Zhao Q.","Liu Y.","Li D.","Hu J.","Yang C.","Feng W.","Wang X."],"citationCrossReferences":[{"database":"PubMed","id":"38538795"},{"database":"DOI","id":"10.1038/s41586-024-07249-8"}],"citationType":"journal article","firstPage":"630","id":"38538795","journal":"Nature","lastPage":"638","publicationDate":"2024","title":"The HEAT repeat protein HPO-27 is a lysosome fission factor.","volume":"628"},"referenceNumber":2,"referencePositions":["FUNCTION","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 23-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
RN   [2]
RP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.
RX   PubMed=38538795; DOI=10.1038/s41586-024-07249-8;
RA   Li L., Liu X., Yang S., Li M., Wu Y., Hu S., Wang W., Jiang A., Zhang Q.,
RA   Zhang J., Ma X., Hu J., Zhao Q., Liu Y., Li D., Hu J., Yang C., Feng W.,
RA   Wang X.;
RT   "The HEAT repeat protein HPO-27 is a lysosome fission factor.";
RL   Nature 628:630-638(2024).
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 31-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
CC   -!- FUNCTION: Lysosome fission factor (PubMed:38538795). Recruited to
CC       lysosomes by rab-7 at scission sites and homooligomerizes to mediate
CC       the constriction and scission of lysosomal tubules (PubMed:38538795).
CC       May sever membranes by inserting amphipathic helices into one bilayer
CC       leaflet (PubMed:38538795). Lysosome fission is required to maintain
CC       their steady-state number, shape, size, composition and function, and
CC       to accomplish regeneration (PubMed:38538795).
CC       {ECO:0000269|PubMed:38538795}.
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
DR   GO; GO:0170064; P:lysosome fission; IDA:UniProtKB.
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
