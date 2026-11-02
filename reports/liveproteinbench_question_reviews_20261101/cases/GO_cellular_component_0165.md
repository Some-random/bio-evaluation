# GO_cellular_component_0165

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence match has a GO cytoplasm annotation with IBA evidence. It also has a more specific lysosomal-membrane localization supported by experimental evidence (IDA); that location is compatible with the broad cytoplasm term in the supplied ontology paths. The specific experimental localization is not itself an answer choice.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO8](#evidence-go8), [GO5](#evidence-go5), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a long, predominantly helical repeat protein, but that alone does not establish a precise cellular location or distinguish cytoplasm from the listed alternatives.


**Missing item-specific fact**

> The protein-specific localization evidence that it associates with lysosomal membranes, and its GO cytoplasm annotation, are absent from the input.


**Reason**

> Choosing cytoplasm depends on protein-specific annotation or localization knowledge. Broad sequence-based tendencies do not meaningfully discriminate these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is supported by the supplied evidence. The experimentally supported lysosomal-membrane location is not listed; cytoplasm is the broad GO option compatible with that localization.


### Important caveats

- The evidence supports cytoplasm as a broad GO annotation, not as the protein's most specific experimentally reported location.
- The experimental lysosomal-membrane annotation and the broader cytoplasm IBA annotation have different evidence types.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long, predominantly helical repeat protein, but that alone does not establish a precise cellular location or distinguish cytoplasm from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence that it associates with lysosomal membranes, and its GO cytoplasm annotation, are absent from the input.",
    "reason": "Choosing cytoplasm depends on protein-specific annotation or localization knowledge. Broad sequence-based tendencies do not meaningfully discriminate these choices."
  },
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6",
      "GO2",
      "GO3",
      "GO8",
      "GO5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a GO cytoplasm annotation with IBA evidence. It also has a more specific lysosomal-membrane localization supported by experimental evidence (IDA); that location is compatible with the broad cytoplasm term in the supplied ontology paths. The specific experimental localization is not itself an answer choice."
  },
  "important_caveats": [
    "The evidence supports cytoplasm as a broad GO annotation, not as the protein's most specific experimentally reported location.",
    "The experimental lysosomal-membrane annotation and the broader cytoplasm IBA annotation have different evidence types."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is supported by the supplied evidence. The experimentally supported lysosomal-membrane location is not listed; cytoplasm is the broad GO option compatible with that localization."
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
    "reason": "The exact sequence match has a GO cytoplasm annotation with IBA evidence. It also has a more specific lysosomal-membrane localization supported by experimental evidence (IDA); that location is compatible with the broad cytoplasm term in the supplied ontology paths. The specific experimental localization is not itself an answer choice.",
    "evidence_ids": ["H3", "H4", "C5", "C6", "GO2", "GO3", "GO8", "GO5", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a long, predominantly helical repeat protein, but that alone does not establish a precise cellular location or distinguish cytoplasm from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific localization evidence that it associates with lysosomal membranes, and its GO cytoplasm annotation, are absent from the input.",
    "reason": "Choosing cytoplasm depends on protein-specific annotation or localization knowledge. Broad sequence-based tendencies do not meaningfully discriminate these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is supported by the supplied evidence. The experimentally supported lysosomal-membrane location is not listed; cytoplasm is the broad GO option compatible with that localization."
  },
  "important_caveats": [
    "The evidence supports cytoplasm as a broad GO annotation, not as the protein's most specific experimentally reported location.",
    "The experimental lysosomal-membrane annotation and the broader cytoplasm IBA annotation have different evidence types."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (K8ERU3, HPO-27) is experimentally localized to the lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795). Lysosomal membrane is part_of cytoplasm in the GO hierarchy (GO:0005765 → GO:0098852 → GO:0005774 → GO:0005773 → GO:0005737). The entry also carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). Since 'lysosomal membrane' is not among the four options, 'cytoplasm' is the only option that correctly encompasses the protein's actual location. The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are unsupported by any annotation or sequence feature.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a large (~1768 AA) HEAT-repeat protein with no signal peptide (N-terminus lacks a hydrophobic cleavable leader), no multiple transmembrane segments (eliminating B, voltage-gated calcium channel), no nuclear localization signal or DNA-binding motif (making A, chromatin, unlikely), and no secretory-pathway targeting (eliminating C, Golgi). HEAT-repeat proteins are well-known cytoplasmic/nuclear adaptor scaffolds; absent an NLS, the default localization is cytoplasmic. Among the four options, D is the only compartment consistent with a large soluble HEAT-repeat protein lacking targeting signals.


**Missing item-specific fact**

> The true primary experimental location is the lysosomal membrane (recruited by rab-7), which is more specific than 'cytoplasm.' However, since lysosomal membrane is not offered as an option and is part_of cytoplasm in GO, the reasoning path to D is valid among the given choices.


**Reason**

> A biologist familiar with HEAT-repeat protein biology and organelle targeting signals can eliminate A, B, and C from the sequence (no TM helices, no signal peptide, no NLS) and select D as the default cytoplasmic localization. The argument does not require knowing the specific HPO-27/rab-7 lysosome recruitment paper.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a large HEAT-repeat protein lacking signal peptides, transmembrane domains, or NLS motifs. Only D (cytoplasm) is consistent with the sequence features and GO hierarchy. While the true location is more specifically 'lysosomal membrane,' that term is absent from the choices, leaving D unambiguously as the best answer.


### Important caveats

- The protein's experimentally determined primary location is 'lysosomal membrane' (IDA, PubMed:38538795, Nature 2024), not 'cytoplasm' per se. The answer D is correct only because cytoplasm is the broadest option that encompasses the lysosomal membrane in the GO part_of hierarchy.
- The GO annotation to cytoplasm (GO:0005737) carries IBA:GO_Central evidence (computational/phylogenetic inference), not experimental evidence. The experimental evidence points to the more specific lysosomal membrane location.
- The protein is 'recruited to the lysosome membrane by rab-7,' implying it is not a constitutive soluble cytoplasmic protein but a cytoplasmic protein that translocates to a membrane compartment. This nuance is not captured by any option.
- The sequence was matched to UniProt K8ERU3 (HPO27_CAEEL, C. elegans, 1768 AA, entry version 72/74). The protein description was added in June 2025; the benchmark author's snapshot date is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a large (~1768 AA) HEAT-repeat protein with no signal peptide (N-terminus lacks a hydrophobic cleavable leader), no multiple transmembrane segments (eliminating B, voltage-gated calcium channel), no nuclear localization signal or DNA-binding motif (making A, chromatin, unlikely), and no secretory-pathway targeting (eliminating C, Golgi). HEAT-repeat proteins are well-known cytoplasmic/nuclear adaptor scaffolds; absent an NLS, the default localization is cytoplasmic. Among the four options, D is the only compartment consistent with a large soluble HEAT-repeat protein lacking targeting signals.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The true primary experimental location is the lysosomal membrane (recruited by rab-7), which is more specific than 'cytoplasm.' However, since lysosomal membrane is not offered as an option and is part_of cytoplasm in GO, the reasoning path to D is valid among the given choices.",
    "reason": "A biologist familiar with HEAT-repeat protein biology and organelle targeting signals can eliminate A, B, and C from the sequence (no TM helices, no signal peptide, no NLS) and select D as the default cytoplasmic localization. The argument does not require knowing the specific HPO-27/rab-7 lysosome recruitment paper."
  },
  "case_id": "GO_cellular_component_0165",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "H5",
      "GO2",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (K8ERU3, HPO-27) is experimentally localized to the lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795). Lysosomal membrane is part_of cytoplasm in the GO hierarchy (GO:0005765 → GO:0098852 → GO:0005774 → GO:0005773 → GO:0005737). The entry also carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). Since 'lysosomal membrane' is not among the four options, 'cytoplasm' is the only option that correctly encompasses the protein's actual location. The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are unsupported by any annotation or sequence feature."
  },
  "important_caveats": [
    "The protein's experimentally determined primary location is 'lysosomal membrane' (IDA, PubMed:38538795, Nature 2024), not 'cytoplasm' per se. The answer D is correct only because cytoplasm is the broadest option that encompasses the lysosomal membrane in the GO part_of hierarchy.",
    "The GO annotation to cytoplasm (GO:0005737) carries IBA:GO_Central evidence (computational/phylogenetic inference), not experimental evidence. The experimental evidence points to the more specific lysosomal membrane location.",
    "The protein is 'recruited to the lysosome membrane by rab-7,' implying it is not a constitutive soluble cytoplasmic protein but a cytoplasmic protein that translocates to a membrane compartment. This nuance is not captured by any option.",
    "The sequence was matched to UniProt K8ERU3 (HPO27_CAEEL, C. elegans, 1768 AA, entry version 72/74). The protein description was added in June 2025; the benchmark author's snapshot date is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a large HEAT-repeat protein lacking signal peptides, transmembrane domains, or NLS motifs. Only D (cytoplasm) is consistent with the sequence features and GO hierarchy. While the true location is more specifically 'lysosomal membrane,' that term is absent from the choices, leaving D unambiguously as the best answer."
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
    "reason": "The protein (K8ERU3, HPO-27) is experimentally localized to the lysosomal membrane (GO:0005765, IDA evidence from PubMed:38538795). Lysosomal membrane is part_of cytoplasm in the GO hierarchy (GO:0005765 → GO:0098852 → GO:0005774 → GO:0005773 → GO:0005737). The entry also carries a direct GO annotation to cytoplasm (GO:0005737, IBA:GO_Central). Since 'lysosomal membrane' is not among the four options, 'cytoplasm' is the only option that correctly encompasses the protein's actual location. The other three options (chromatin, voltage-gated calcium channel complex, Golgi apparatus) are unsupported by any annotation or sequence feature.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "H5", "GO2", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a large (~1768 AA) HEAT-repeat protein with no signal peptide (N-terminus lacks a hydrophobic cleavable leader), no multiple transmembrane segments (eliminating B, voltage-gated calcium channel), no nuclear localization signal or DNA-binding motif (making A, chromatin, unlikely), and no secretory-pathway targeting (eliminating C, Golgi). HEAT-repeat proteins are well-known cytoplasmic/nuclear adaptor scaffolds; absent an NLS, the default localization is cytoplasmic. Among the four options, D is the only compartment consistent with a large soluble HEAT-repeat protein lacking targeting signals.",
    "missing_item_specific_fact": "The true primary experimental location is the lysosomal membrane (recruited by rab-7), which is more specific than 'cytoplasm.' However, since lysosomal membrane is not offered as an option and is part_of cytoplasm in GO, the reasoning path to D is valid among the given choices.",
    "reason": "A biologist familiar with HEAT-repeat protein biology and organelle targeting signals can eliminate A, B, and C from the sequence (no TM helices, no signal peptide, no NLS) and select D as the default cytoplasmic localization. The argument does not require knowing the specific HPO-27/rab-7 lysosome recruitment paper."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a large HEAT-repeat protein lacking signal peptides, transmembrane domains, or NLS motifs. Only D (cytoplasm) is consistent with the sequence features and GO hierarchy. While the true location is more specifically 'lysosomal membrane,' that term is absent from the choices, leaving D unambiguously as the best answer."
  },
  "important_caveats": [
    "The protein's experimentally determined primary location is 'lysosomal membrane' (IDA, PubMed:38538795, Nature 2024), not 'cytoplasm' per se. The answer D is correct only because cytoplasm is the broadest option that encompasses the lysosomal membrane in the GO part_of hierarchy.",
    "The GO annotation to cytoplasm (GO:0005737) carries IBA:GO_Central evidence (computational/phylogenetic inference), not experimental evidence. The experimental evidence points to the more specific lysosomal membrane location.",
    "The protein is 'recruited to the lysosome membrane by rab-7,' implying it is not a constitutive soluble cytoplasmic protein but a cytoplasmic protein that translocates to a membrane compartment. This nuance is not captured by any option.",
    "The sequence was matched to UniProt K8ERU3 (HPO27_CAEEL, C. elegans, 1768 AA, entry version 72/74). The protein description was added in June 2025; the benchmark author's snapshot date is unknown."
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

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38538795","source":"PubMed"}],"value":"Recruited to the lysosome membrane by rab-7"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38538795","source":"PubMed"}],"id":"SL-0157","value":"Lysosome membrane"}}]}
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K8ERU3.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.780786+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38538795","source":"PubMed"}],"id":"GO:0005765","properties":[{"key":"GoTerm","value":"C:lysosomal membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `e3167804d51f387cbba1074a8de97db9fc4b68c7a3ef3411172a43b1d00c82a2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 41-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Lysosome membrane {ECO:0000269|PubMed:38538795}.
CC       Note=Recruited to the lysosome membrane by rab-7.
CC       {ECO:0000269|PubMed:38538795}.
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IBA:GO_Central.
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K8ERU3?format=txt&versions=72)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 72 / 1.  
**Retrieved:** 2026-11-02T04:29:02.545982+00:00.  

```text
DR   GO; GO:0005765; C:lysosomal membrane; IDA:UniProtKB.
```

Source SHA-256: `59d5454e530ac3d4f72701b201f40cdb74bf23f3efe4ad36d8dd19698fa9687e`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58957-58974`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005737
name: cytoplasm
namespace: cellular_component
def: "The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures." [ISBN:0198547684]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
xref: Wikipedia:Cytoplasm
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005622 ! intracellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59259-59267`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005765
name: lysosomal membrane
namespace: cellular_component
def: "The lipid bilayer surrounding the lysosome and separating its contents from the cell cytoplasm." [GOC:ai]
synonym: "lysosome membrane" EXACT []
is_a: GO:0098852 ! lytic vacuole membrane
relationship: part_of GO:0005764 ! lysosome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59332-59353`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005773
name: vacuole
namespace: cellular_component
def: "A closed structure, found only in eukaryotic cells, that is completely surrounded by unit membrane and contains liquid material. Cells contain one or several vacuoles, that may have different functions from each other. Vacuoles have a diverse array of functions. They can act as a storage organelle for nutrients or waste products, as a degradative compartment, as a cost-effective way of increasing cell size, and as a homeostatic regulator controlling both turgor pressure and pH of the cytosol." [GOC:mtg_sensu, ISBN:0198506732]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "vacuolar carboxypeptidase Y" RELATED []
xref: Wikipedia:Vacuole
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59354-59361`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005774
name: vacuolar membrane
namespace: cellular_component
def: "The lipid bilayer surrounding the vacuole and separating its contents from the cytoplasm of the cell." [GOC:ai]
is_a: GO:0098588 ! bounding membrane of organelle
relationship: part_of GO:0005773 ! vacuole

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 411521-411528`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098852
name: lytic vacuole membrane
namespace: cellular_component
def: "The lipid bilayer surrounding a lytic vacuole and separating its contents from the cytoplasm of the cell." [GOC:dos]
is_a: GO:0005774 ! vacuolar membrane
relationship: part_of GO:0000323 ! lytic vacuole

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 165. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
