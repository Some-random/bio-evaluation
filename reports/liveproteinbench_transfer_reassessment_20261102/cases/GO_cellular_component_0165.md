# GO_cellular_component_0165

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0165.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — cytoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAATSQVSSLLDLIMSLLDTATTYQHQESVKNEVAESLKTIGSHQPNVLLTACHQYLLQNPKLGAFKRAFVLQTISICVDNCEVVSKLDEQIIMLIINLATQEMNMTKDTDVEWAESSMEVLVTLAKNTRFVSHVIDAILQKFPPGQTTSPHRYIVLTMATIAVHNPFGLVPFLTDILSRTVPLLQHVKTDPLRCAWARAICSFCEAVRECETERPKEASEEYIGDHSRPNSASGHCQEVSNRATYSDQTEAVYDVIFSWIYSKDPKTRGEAAECVGELCLMIKQTRLVEDVKKIVTNMIPLYRKSYNESHMITQGICRFLEAACVDETCPLEPYLEDILNALFPNACLDPDDTTVTLSTQAIKNHSEAFRCFDVAATRFADRIVYYLLHKMQNVADSQKLGAINVLRHLLNATGQHMEDKRSLLTMGLKKLLAAENTTSIRVKRAIVQLCVALADHSYVDAEGGDYVIAFLVRNLVGPTEQESAAKKVEVDVAGLNQLRTQCAQALYTIANTCVCATKLLWPYLLEFICCERYTPVVGDLCKCLRTLVSREVEAGRKMDYVTGFDNPKVAGRHAVFARLFTSFCNAPLNGLLTRRAREAGGLIQAVAPWFHPSMEGPAARWSEKLEPLLDELSTTVSSGDSAPAELRGRKIARWHEACLDWLSACVAVVPEGDWRQDLAAAMGKQLDMYKELSDEKSFLLRCLGVTLARITAKQFVIDHMMLMFKSASHSVLTERQGCARGVGSIATSHMDLILIELENVSKWEHARKSSGIFGFIKDTMPIRQYPDIEMIHLRATLMLCYGHVVMACSLDTITQRLQNTIIVFLRNYFANSKQETVVREAMLETMRLIATAVHPSRIGGEWKFEARNELLAYAKDYLNGETPEWLTSSLRLLACKTTAALVQLEPPLSPADIEDIGTVLTRQILPMQREKSGLKTLAFDIFDYASSSVFSTFSGSSSSHTNIYMTPPLTANSVAEGPNGTPIHQRHRGIGGKMEDDESATIMDATMHQYGLALEQIVRMAPTTQTIMILLKILLPYYGKQADHERIRAVDMTVLVLRVYYECAEDISLGHASDFEPLSSLLGRLAPRLIDLLAHVRLQALSAIHWTLRLAYMHKGHGRDADQSLFSYSGFVEKYLTSGDVKLEGQKEKLAIEAIAQIIEYRLPQSQMQIYLSAIFEMLTDRQSHVSSAAAQLLTYAVMARGATLNAEAEILVTKMVEKLADIHHCVQTNTDVLAALVAFAVHQQQAVCDVLFKQPLPYSINITDAWECLSRDKLLFAVILDHLTELLGASLDQPFELMDSGGGVSAKVVNVEPCTYVAVLAEVVKNGEPESALMERLPLILTLLIHFICSVSDTQFPVMQKEGSKNPLIITPDLRRAAEKPAGMAVAAIKNLLNRTRSNMVIEDMNQARAWTDCLDKDSFIQAITVFIRSLVEQRPAWVSPLAKTMEEYANSESEPRRLAAVIIAASLIRRSTSENGEFNEQLLVKCIRRLEDSLTDPSLRIRKLCVKGLGELSECSSTDVISRFVHMAVEAAMSGLDDHGDRKDTVAIESIMALNKLVQLTNNDQLKSILPLVLLKIRPCFEKDSHTLRAASFSLFGELGSRVGENSEEFRGHLHTNIVSLLLHLNDDFEEVRQNCANSIYRLHGLLTSPNASICIERELKDGKQPASYNLFIKDFASILANSFPDRINQYALATSNYFKSSSARIRCNAAHLTGCLLDGLTAPLRATISRELVFTGLVALLKDSEDVNVRISATRAIANLHDFH

[Multiple Choices]
A. chromatin
B. voltage-gated calcium channel complex
C. Golgi apparatus
D. cytoplasm
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has a GO cytoplasm annotation (H4). It also has an experimentally supported lysosomal-membrane annotation (C6), a location within the cytoplasm in the GO hierarchy. Thus D is supported as the broad compartment among the offered choices, although the more specific reported location is not offered.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6), [GO3](#evidence-go3), [GO8](#evidence-go8), [GO5](#evidence-go5), [GO4](#evidence-go4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is rich in alpha-helical repeat-like regions and lacks an obvious multi-pass transmembrane/channel architecture or recognizable chromatin-binding features. Transferable knowledge makes a soluble intracellular scaffold more plausible than a voltage-gated calcium channel complex or chromatin-associated protein. It also lacks an obvious membrane-spanning architecture expected of many Golgi residents, making broad cytoplasm the most credible offered choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Sequence architecture and the alternatives provide a meaningful, though not definitive, basis for choosing cytoplasm. Peripheral association with an organelle membrane remains possible, so the sequence alone does not establish a precise localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The specific lysosomal-membrane location is not an option, but cytoplasm is a defensible broader compartment. The sequence does not provide comparable support for the other listed choices.


### Important caveats

- The direct cytoplasm annotation is computationally transferred (IBA), whereas lysosomal-membrane localization has experimental evidence.
- A broad cytoplasm choice does not convey the protein's more specific membrane-associated localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is rich in alpha-helical repeat-like regions and lacks an obvious multi-pass transmembrane/channel architecture or recognizable chromatin-binding features. Transferable knowledge makes a soluble intracellular scaffold more plausible than a voltage-gated calcium channel complex or chromatin-associated protein. It also lacks an obvious membrane-spanning architecture expected of many Golgi residents, making broad cytoplasm the most credible offered choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Sequence architecture and the alternatives provide a meaningful, though not definitive, basis for choosing cytoplasm. Peripheral association with an organelle membrane remains possible, so the sequence alone does not establish a precise localization."
  },
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6",
      "GO3",
      "GO8",
      "GO5",
      "GO4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a GO cytoplasm annotation (H4). It also has an experimentally supported lysosomal-membrane annotation (C6), a location within the cytoplasm in the GO hierarchy. Thus D is supported as the broad compartment among the offered choices, although the more specific reported location is not offered."
  },
  "important_caveats": [
    "The direct cytoplasm annotation is computationally transferred (IBA), whereas lysosomal-membrane localization has experimental evidence.",
    "A broad cytoplasm choice does not convey the protein's more specific membrane-associated localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific lysosomal-membrane location is not an option, but cytoplasm is a defensible broader compartment. The sequence does not provide comparable support for the other listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a GO cytoplasm annotation (H4). It also has an experimentally supported lysosomal-membrane annotation (C6), a location within the cytoplasm in the GO hierarchy. Thus D is supported as the broad compartment among the offered choices, although the more specific reported location is not offered.",
    "evidence_ids": ["H4", "C6", "GO3", "GO8", "GO5", "GO4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is rich in alpha-helical repeat-like regions and lacks an obvious multi-pass transmembrane/channel architecture or recognizable chromatin-binding features. Transferable knowledge makes a soluble intracellular scaffold more plausible than a voltage-gated calcium channel complex or chromatin-associated protein. It also lacks an obvious membrane-spanning architecture expected of many Golgi residents, making broad cytoplasm the most credible offered choice.",
    "missing_item_specific_fact": "",
    "reason": "Sequence architecture and the alternatives provide a meaningful, though not definitive, basis for choosing cytoplasm. Peripheral association with an organelle membrane remains possible, so the sequence alone does not establish a precise localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific lysosomal-membrane location is not an option, but cytoplasm is a defensible broader compartment. The sequence does not provide comparable support for the other listed choices."
  },
  "important_caveats": [
    "The direct cytoplasm annotation is computationally transferred (IBA), whereas lysosomal-membrane localization has experimental evidence.",
    "A broad cytoplasm choice does not convey the protein's more specific membrane-associated localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for K8ERU3 (HPO-27) includes GO:0005737 (cytoplasm) annotated via IBA:GO_Central. The experimental evidence (IDA, PubMed:38538795) places the protein at the lysosomal membrane (GO:0005765). The GO ontology hierarchy confirms lysosomal membrane → lytic vacuole membrane → vacuolar membrane → vacuole → part_of cytoplasm (GO:0005737). Since lysosomal membrane is not among the answer choices, cytoplasm is the broadest correct compartment containing the protein's experimentally determined location. The IBA annotation to cytoplasm is a computational inference (not direct experiment), but it is consistent with the ontology path from the experimental lysosomal membrane annotation. The answer is supported as the best available option, though the most specific experimental location (lysosomal membrane) is not offered.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO4](#evidence-go4), [GO8](#evidence-go8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~1768 aa) is characteristic of a HEAT repeat protein: a large, predominantly alpha-helical scaffold protein with multiple tandem repeat motifs. HEAT repeat proteins (Huntingtin, Elongation factor 3, PR65/PP2A-A, TOR1 family) are overwhelmingly cytoplasmic protein-protein interaction scaffolds. Critically, the sequence lacks: (1) an N-terminal signal peptide or transmembrane helices that would target it to the ER/Golgi/secretory pathway (eliminating C and B); (2) multiple transmembrane domains required for a voltage-gated calcium channel (eliminating B); (3) DNA-binding domains or histone-modification motifs (eliminating A). The absence of any membrane-targeting or nuclear-targeting signals, combined with the HEAT-repeat family regularity of cytoplasmic localization, provides a credible family-level inference favoring D (cytoplasm) over the other three options. While the actual experimental location is lysosomal membrane (a membrane-bound organelle within the cytoplasm), among the four offered choices, cytoplasm is the only one consistent with a HEAT repeat scaffold lacking ER/Golgi or ion-channel targeting features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the HEAT repeat architecture and the absence of signal peptides, transmembrane domains, or NLS motifs can use family-level knowledge (HEAT proteins are cytoplasmic scaffolds) to eliminate A (chromatin), B (voltage-gated calcium channel complex), and C (Golgi apparatus), arriving at D (cytoplasm). This is a legitimate transfer inference from other HEAT repeat proteins, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the protein's most specific experimental location is the lysosomal membrane, that option is not offered. Among the four choices, only cytoplasm (D) is consistent with the protein's location (lysosomal membrane is part_of cytoplasm in GO). The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are clearly incompatible with a HEAT repeat scaffold protein lacking membrane-spanning or DNA-binding features. No ambiguity among the offered choices.


### Important caveats

- The most specific experimentally determined location is lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795, Nature 2024), which is not among the answer choices.
- The cytoplasm annotation (GO:0005737) is via IBA:GO_Central (computational inference from ancestral annotation), not direct experimental evidence for this protein.
- The question asks for the 'primary Cellular Component'—arguably lysosomal membrane is more specific than cytoplasm, but since it is not offered, cytoplasm is the correct best-available answer.
- The protein is recruited to the lysosome membrane by rab-7, suggesting it may also have a cytoplasmic pool before recruitment, further supporting cytoplasm as a reasonable broad answer.
- The sequence match to K8ERU3 is confirmed (SHA256 match), but the accession and organism identity were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~1768 aa) is characteristic of a HEAT repeat protein: a large, predominantly alpha-helical scaffold protein with multiple tandem repeat motifs. HEAT repeat proteins (Huntingtin, Elongation factor 3, PR65/PP2A-A, TOR1 family) are overwhelmingly cytoplasmic protein-protein interaction scaffolds. Critically, the sequence lacks: (1) an N-terminal signal peptide or transmembrane helices that would target it to the ER/Golgi/secretory pathway (eliminating C and B); (2) multiple transmembrane domains required for a voltage-gated calcium channel (eliminating B); (3) DNA-binding domains or histone-modification motifs (eliminating A). The absence of any membrane-targeting or nuclear-targeting signals, combined with the HEAT-repeat family regularity of cytoplasmic localization, provides a credible family-level inference favoring D (cytoplasm) over the other three options. While the actual experimental location is lysosomal membrane (a membrane-bound organelle within the cytoplasm), among the four offered choices, cytoplasm is the only one consistent with a HEAT repeat scaffold lacking ER/Golgi or ion-channel targeting features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the HEAT repeat architecture and the absence of signal peptides, transmembrane domains, or NLS motifs can use family-level knowledge (HEAT proteins are cytoplasmic scaffolds) to eliminate A (chromatin), B (voltage-gated calcium channel complex), and C (Golgi apparatus), arriving at D (cytoplasm). This is a legitimate transfer inference from other HEAT repeat proteins, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "H5",
      "GO2",
      "GO3",
      "GO4",
      "GO8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for K8ERU3 (HPO-27) includes GO:0005737 (cytoplasm) annotated via IBA:GO_Central. The experimental evidence (IDA, PubMed:38538795) places the protein at the lysosomal membrane (GO:0005765). The GO ontology hierarchy confirms lysosomal membrane → lytic vacuole membrane → vacuolar membrane → vacuole → part_of cytoplasm (GO:0005737). Since lysosomal membrane is not among the answer choices, cytoplasm is the broadest correct compartment containing the protein's experimentally determined location. The IBA annotation to cytoplasm is a computational inference (not direct experiment), but it is consistent with the ontology path from the experimental lysosomal membrane annotation. The answer is supported as the best available option, though the most specific experimental location (lysosomal membrane) is not offered."
  },
  "important_caveats": [
    "The most specific experimentally determined location is lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795, Nature 2024), which is not among the answer choices.",
    "The cytoplasm annotation (GO:0005737) is via IBA:GO_Central (computational inference from ancestral annotation), not direct experimental evidence for this protein.",
    "The question asks for the 'primary Cellular Component'—arguably lysosomal membrane is more specific than cytoplasm, but since it is not offered, cytoplasm is the correct best-available answer.",
    "The protein is recruited to the lysosome membrane by rab-7, suggesting it may also have a cytoplasmic pool before recruitment, further supporting cytoplasm as a reasonable broad answer.",
    "The sequence match to K8ERU3 is confirmed (SHA256 match), but the accession and organism identity were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein's most specific experimental location is the lysosomal membrane, that option is not offered. Among the four choices, only cytoplasm (D) is consistent with the protein's location (lysosomal membrane is part_of cytoplasm in GO). The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are clearly incompatible with a HEAT repeat scaffold protein lacking membrane-spanning or DNA-binding features. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for K8ERU3 (HPO-27) includes GO:0005737 (cytoplasm) annotated via IBA:GO_Central. The experimental evidence (IDA, PubMed:38538795) places the protein at the lysosomal membrane (GO:0005765). The GO ontology hierarchy confirms lysosomal membrane → lytic vacuole membrane → vacuolar membrane → vacuole → part_of cytoplasm (GO:0005737). Since lysosomal membrane is not among the answer choices, cytoplasm is the broadest correct compartment containing the protein's experimentally determined location. The IBA annotation to cytoplasm is a computational inference (not direct experiment), but it is consistent with the ontology path from the experimental lysosomal membrane annotation. The answer is supported as the best available option, though the most specific experimental location (lysosomal membrane) is not offered.",
    "evidence_ids": ["C6", "H4", "H5", "GO2", "GO3", "GO4", "GO8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~1768 aa) is characteristic of a HEAT repeat protein: a large, predominantly alpha-helical scaffold protein with multiple tandem repeat motifs. HEAT repeat proteins (Huntingtin, Elongation factor 3, PR65/PP2A-A, TOR1 family) are overwhelmingly cytoplasmic protein-protein interaction scaffolds. Critically, the sequence lacks: (1) an N-terminal signal peptide or transmembrane helices that would target it to the ER/Golgi/secretory pathway (eliminating C and B); (2) multiple transmembrane domains required for a voltage-gated calcium channel (eliminating B); (3) DNA-binding domains or histone-modification motifs (eliminating A). The absence of any membrane-targeting or nuclear-targeting signals, combined with the HEAT-repeat family regularity of cytoplasmic localization, provides a credible family-level inference favoring D (cytoplasm) over the other three options. While the actual experimental location is lysosomal membrane (a membrane-bound organelle within the cytoplasm), among the four offered choices, cytoplasm is the only one consistent with a HEAT repeat scaffold lacking ER/Golgi or ion-channel targeting features.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the HEAT repeat architecture and the absence of signal peptides, transmembrane domains, or NLS motifs can use family-level knowledge (HEAT proteins are cytoplasmic scaffolds) to eliminate A (chromatin), B (voltage-gated calcium channel complex), and C (Golgi apparatus), arriving at D (cytoplasm). This is a legitimate transfer inference from other HEAT repeat proteins, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein's most specific experimental location is the lysosomal membrane, that option is not offered. Among the four choices, only cytoplasm (D) is consistent with the protein's location (lysosomal membrane is part_of cytoplasm in GO). The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are clearly incompatible with a HEAT repeat scaffold protein lacking membrane-spanning or DNA-binding features. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The most specific experimentally determined location is lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795, Nature 2024), which is not among the answer choices.",
    "The cytoplasm annotation (GO:0005737) is via IBA:GO_Central (computational inference from ancestral annotation), not direct experimental evidence for this protein.",
    "The question asks for the 'primary Cellular Component'—arguably lysosomal membrane is more specific than cytoplasm, but since it is not offered, cytoplasm is the correct best-available answer.",
    "The protein is recruited to the lysosome membrane by rab-7, suggesting it may also have a cytoplasmic pool before recruitment, further supporting cytoplasm as a reasonable broad answer.",
    "The sequence match to K8ERU3 is confirmed (SHA256 match), but the accession and organism identity were not provided to the evaluated model."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 1768,
  "benchmark_sequence_sha256": "f84e11eefe0b3ad8b854d3d0aeab86feac2c965d4461c15d76ad582cda8bffa2",
  "current_entry_audit": {
    "entryVersion": 74,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1768,
  "current_source_sequence_sha256": "f84e11eefe0b3ad8b854d3d0aeab86feac2c965d4461c15d76ad582cda8bffa2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 72,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "K8ERU3",
  "selected_historical_entry_version": 72,
  "selected_historical_record_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "selected_historical_source_sequence_length": 1768,
  "selected_historical_source_sequence_sha256": "f84e11eefe0b3ad8b854d3d0aeab86feac2c965d4461c15d76ad582cda8bffa2",
  "selected_historical_version": {
    "accession": "K8ERU3",
    "database": "Swiss-Prot",
    "entryVersion": 72,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HPO27_CAEEL",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

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

```json
{
  "evidence_id": "C1",
  "excerpt": "\"K8ERU3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":74,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Nematoda\",\"Chromadorea\",\"Rhabditida\",\"Rhabditina\",\"Rhabditomorpha\",\"Rhabditoidea\",\"Rhabditidae\",\"Peloderinae\",\"Caenorhabditis\"],\"scientificName\":\"Caenorhabditis elegans\",\"taxonId\":6239}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HEAT repeat protein 27\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Maestro heat-like repeat-containing protein family member 1 homolog\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538795\",\"source\":\"PubMed\"}],\"value\":\"Recruited to the lysosome membrane by rab-7\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38538795\",\"source\":\"PubMed\"}],\"id\":\"SL-0157\",\"value\":\"Lysosome membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38538795\",\"source\":\"PubMed\"}],\"id\":\"GO:0005765\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:lysosomal membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Li L.\",\"Liu X.\",\"Yang S.\",\"Li M.\",\"Wu Y.\",\"Hu S.\",\"Wang W.\",\"Jiang A.\",\"Zhang Q.\",\"Zhang J.\",\"Ma X.\",\"Hu J.\",\"Zhao Q.\",\"Liu Y.\",\"Li D.\",\"Hu J.\",\"Yang C.\",\"Feng W.\",\"Wang X.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38538795\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-024-07249-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"630\",\"id\":\"38538795\",\"journal\":\"Nature\",\"lastPage\":\"638\",\"publicationDate\":\"2024\",\"title\":\"The HEAT repeat protein HPO-27 is a lysosome fission factor.\",\"volume\":\"628\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:58.780786+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2",
  "url": "https://rest.uniprot.org/uniprotkb/K8ERU3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H1",
  "excerpt": "ID   HPO27_CAEEL             Reviewed;        1768 AA.\nAC   K8ERU3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2013, sequence version 1.\nDT   28-JAN-2026, entry version 72.\nDE   RecName: Full=Maestro heat-like repeat-containing protein family member 1 homolog {ECO:0000305};\nDE   AltName: Full=HEAT repeat protein 27 {ECO:0000305};\nGN   Name=hpo-27 {ECO:0000303|PubMed:38538795, ECO:0000312|WormBase:C34G6.1};\nGN   ORFNames=C34G6.1 {ECO:0000312|WormBase:C34G6.1};\nOS   Caenorhabditis elegans.\nOC   Eukaryota; Metazoa; Ecdysozoa; Nematoda; Chromadorea; Rhabditida;\nOC   Rhabditina; Rhabditomorpha; Rhabditoidea; Rhabditidae; Peloderinae;\nOC   Caenorhabditis.\nOX   NCBI_TaxID=6239;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.545982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "url": "https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.\nRX   PubMed=38538795; DOI=10.1038/s41586-024-07249-8;\nRA   Li L., Liu X., Yang S., Li M., Wu Y., Hu S., Wang W., Jiang A., Zhang Q.,\nRA   Zhang J., Ma X., Hu J., Zhao Q., Liu Y., Li D., Hu J., Yang C., Feng W.,\nRA   Wang X.;\nRT   \"The HEAT repeat protein HPO-27 is a lysosome fission factor.\";\nRL   Nature 628:630-638(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.545982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "url": "https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Lysosome membrane {ECO:0000269|PubMed:38538795}.\nCC       Note=Recruited to the lysosome membrane by rab-7.\nCC       {ECO:0000269|PubMed:38538795}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.545982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "url": "https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.545982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "url": "https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)

```json
{
  "entry_version": 72,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005765; C:lysosomal membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.545982+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e",
  "url": "https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000785\nname: chromatin\nnamespace: cellular_component\nalt_id: GO:0000789\nalt_id: GO:0000790\nalt_id: GO:0005717\ndef: \"The ordered and organized complex of DNA, protein, and sometimes RNA, that forms the chromosome.\" [GOC:elh, PMID:20404130]\ncomment: Chromosomes include parts that are not part of the chromatin. Examples include the kinetochore.\nsynonym: \"chromosome scaffold\" RELATED []\nsynonym: \"cytoplasmic chromatin\" NARROW []\nsynonym: \"nuclear chromatin\" NARROW []\nxref: NIF_Subcellular:sao1615953555\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005694 ! chromosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000785",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 5903-5918",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0005737\nname: cytoplasm\nnamespace: cellular_component\ndef: \"The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures.\" [ISBN:0198547684]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nxref: Wikipedia:Cytoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005622 ! intracellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005737",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58957-58974",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0005765\nname: lysosomal membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the lysosome and separating its contents from the cell cytoplasm.\" [GOC:ai]\nsynonym: \"lysosome membrane\" EXACT []\nis_a: GO:0098852 ! lytic vacuole membrane\nrelationship: part_of GO:0005764 ! lysosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005765",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59259-59267",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0005773\nname: vacuole\nnamespace: cellular_component\ndef: \"A closed structure, found only in eukaryotic cells, that is completely surrounded by unit membrane and contains liquid material. Cells contain one or several vacuoles, that may have different functions from each other. Vacuoles have a diverse array of functions. They can act as a storage organelle for nutrients or waste products, as a degradative compartment, as a cost-effective way of increasing cell size, and as a homeostatic regulator controlling both turgor pressure and pH of the cytosol.\" [GOC:mtg_sensu, ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"vacuolar carboxypeptidase Y\" RELATED []\nxref: Wikipedia:Vacuole\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005773",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59332-59353",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0005774\nname: vacuolar membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the vacuole and separating its contents from the cytoplasm of the cell.\" [GOC:ai]\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005773 ! vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005774",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59354-59361",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "excerpt": "[Term]\nid: GO:0005794\nname: Golgi apparatus\nnamespace: cellular_component\ndef: \"A membrane-bound cytoplasmic organelle of the endomembrane system that further processes the core oligosaccharides (e.g. N-glycans) added to proteins in the endoplasmic reticulum and packages them into membrane-bound vesicles. The Golgi apparatus operates at the intersection of the secretory, lysosomal, and endocytic pathways.\" [ISBN:0198506732, PMID:9695800]\ncomment: Note that the Golgi apparatus can be located in various places in the cytoplasm. In plants and lower animal cells, the Golgi apparatus exists as many copies of discrete stacks dispersed throughout the cytoplasm, while the Golgi apparatus of interphase mammalian cells is a juxtanuclear, often pericentriolar reticulum, where the discrete Golgi stacks are stitched together to form a compact and interconnected ribbon, sometimes called the Golgi ribbon.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"Golgi\" BROAD []\nsynonym: \"Golgi complex\" EXACT []\nsynonym: \"Golgi ribbon\" NARROW []\nxref: NIF_Subcellular:sao451912436\nxref: Wikipedia:Golgi_apparatus\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005794",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59587-59612",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "excerpt": "[Term]\nid: GO:0005891\nname: voltage-gated calcium channel complex\nnamespace: cellular_component\ndef: \"A protein complex that forms a transmembrane channel through which calcium ions may pass in response to changes in membrane potential.\" [GOC:mah]\nsubset: goslim_pir\nsynonym: \"voltage gated calcium channel complex\" EXACT []\nsynonym: \"voltage-dependent calcium channel complex\" EXACT []\nsynonym: \"voltage-sensitive calcium channel complex\" EXACT []\nis_a: GO:0034704 ! calcium channel complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005891",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60486-60497",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO8",
  "excerpt": "[Term]\nid: GO:0098852\nname: lytic vacuole membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding a lytic vacuole and separating its contents from the cytoplasm of the cell.\" [GOC:dos]\nis_a: GO:0005774 ! vacuolar membrane\nrelationship: part_of GO:0000323 ! lytic vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098852",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 411521-411528",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 165. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
