# GO_cellular_component_0187

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — cytoplasmic vesicle

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MILDKFKNIVNLSNSNTEKEEGKNAEINENNDPNTQLAHEPSIVEADEKTFFDEMLGAPQYTYDEFLQVLKNPIEERGDTEDMKKHWGYPRRWKVILWDLHIQNYMNNDFNAFVDFDFGGNREECRIQRGSTMKIYAKGKTKNCLRTPVVTNVATEQKKNMNFRNVFEYRGSYLDLENEKLRIRVWEYKQFTLNKLEGIYEEPLLSFAVGEIYNETTLYKFIKDSRVKRCRLYFQLYFQELYDFELSFLNWSFSDLLSSSYIQAKSYNYLSNKNNVKKRYIDDTSCNIFPHMCKNFKRFHKKKIYRKVRNYDIDKNFSFNTALSDDSDERKNKNDRTIKNLEKLFVRNLTLMQNIEENEDMSYKNLQNINLPNPRVTITLSHTPKGHEGLNIISIEQKSIRFPIWENLGEIYFRGTLRDLDVSYLNIKVEDMSAPKSAREIGTCQISLKGIVDYPYVMHELEAPSWLVKEAKYEGWENKLNEWKLGTVEGKVIINRVPRYRQRGDIYHIDSKQPYLIVHIFNIDKIITVDNIKELDTYVEVSFDETSRRTRLMKKTLSPNYDSQISIPLRFNNKNDINYENLSKKGLIYIDVWGKSEDIVYIGGISISPYEIFFNEKNVRRNKTKLEHIDLETNVKITYDTVVYRGCKKLCFLHDDQRMSNIHFSIWTYPDILGNSTNQKKIVAPVSFNTTMNFPIKLAEKYNKLKKLFMEVLKTIKSIPENCTDVNTSTRFYNYELINQRKEKHFLPTLITSIKSPYCAESMNAIFHYVRCIPFIHKKENIIFTPDFTLQLKGGNALDHSLLLCSLFLGIPVLAFVCFGTLWDKQKHSWVATFEYNDEKNYGIVKFWETTTGNVYILKKRFIDHNRLKGLELKLKESKYKSHLRNGFLQRYENNTDINYIKEQTKRHIKQLFKNRINDIPIGGPSLPYKTIDLIFNHKNIYVNLQHSSPLNIWYDYWKFDFWFPFSSIEYNLQPSFTIKSFTHKMEDMELDKIAKELRTNIEKNINIYRASRNLSTRWNRDETLEIFLQVGLELLHQLNTSRKEDVLLAKLKIEDWKKALYHKVPQSHRLLGFPYHFNTYKSKFISDKLISTLAILESRDRSLCLSLAVCLYSLPGNFISCYIYIITCVKITQRELRKMEIIKEKAQRMAEIKNSQKKKKSSDDQNIDIKTMDDVEEKETFSSTNLDDTLHDEHTDIDTEKKKHEKDNYKNKKIKNTKLKDANIDNEEKDDHHHITDKKVSKSSDLIHSFDKNDISKNTFDKEEFINNLDKDKKYSSFKKGNVVNKKVSIKNEPSINIYEDHKIYDDENISNNIDNMENNQDEIYNLRQGKTIINEFQQVKKPQKYTINEKRDDIKTKKKRSKEKKKQDKLEFEKLIQSNAYFEQEKKKLQEDIKKLEKDKEQFQKEKIRREEKEKQLLLEEKIKLQKEKELFENEKLERKMSYMLKINELEKKKNERNKMEKSYKRMIQKDKEKKKKKESRDKIRRGEEEKMSADENMKEEQKMREEQKVGEEQKVGEEQKVGEEQKLREEQKMREEQKMREEQKMREEQKMREEQKVREEQKMREEQKMREEQKMREEQKVREEQKLREEQKMREEQKMREEQKMREEEKIREEEQMKREKKMRREEKKKRVQEPIKIDEIQVYDIIKNEKMKKKEEKEEKKRKKKKEDIEDKYKIGKEASLDENNNERQIKSKNIQEISDYEYKNIKENKNLNKFDEKLDLNQIYSKASNFYDNQEKKRRTIKVHANRKENSDSTFSHIDDSIKNKKEYLEDSNIARYLYEKRKHDLIGKGNYNFDEPHYGKKMNNVAYQDIKGSNLFKGFIEEPSSKKSPQKKKIVIVRKN

[Multiple Choices]
A. microtubule associated complex
B. cytoplasmic vesicle
C. virus tail, tube
D. vacuolar membrane
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

> The exact-matched protein has experimental annotation to cytoplasmic vesicle (IDA:GeneDB), and its reported punctate localization is described as reminiscent of vesicles. The evidence supports B, while also noting membrane localization and host-cell plasma-membrane annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> C2-domain features can support a general inference of membrane association, but the sequence alone does not establish localization specifically to cytoplasmic vesicles rather than another membrane compartment.


**Missing item-specific fact**

> The protein-specific localization evidence that PfDOC2 shows punctate, vesicle-like localization and has a cytoplasmic-vesicle annotation is absent from the input.


**Reason**

> Choosing B depends on a protein-specific localization annotation or experimental result, not a sufficiently discriminating sequence-based argument supplied by the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports cytoplasmic vesicle among the listed choices. Membrane and host-cell plasma-membrane annotations do not correspond to another listed option.


### Important caveats

- The sequence matches the referenced UniProt record, but the author's exact source snapshot is unknown.
- The localization evidence supports vesicle-like localization; it does not establish that cytoplasmic vesicle is the protein's exclusive location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "C2-domain features can support a general inference of membrane association, but the sequence alone does not establish localization specifically to cytoplasmic vesicles rather than another membrane compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence that PfDOC2 shows punctate, vesicle-like localization and has a cytoplasmic-vesicle annotation is absent from the input.",
    "reason": "Choosing B depends on a protein-specific localization annotation or experimental result, not a sufficiently discriminating sequence-based argument supplied by the question."
  },
  "case_id": "GO_cellular_component_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact-matched protein has experimental annotation to cytoplasmic vesicle (IDA:GeneDB), and its reported punctate localization is described as reminiscent of vesicles. The evidence supports B, while also noting membrane localization and host-cell plasma-membrane annotation."
  },
  "important_caveats": [
    "The sequence matches the referenced UniProt record, but the author's exact source snapshot is unknown.",
    "The localization evidence supports vesicle-like localization; it does not establish that cytoplasmic vesicle is the protein's exclusive location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasmic vesicle among the listed choices. Membrane and host-cell plasma-membrane annotations do not correspond to another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched protein has experimental annotation to cytoplasmic vesicle (IDA:GeneDB), and its reported punctate localization is described as reminiscent of vesicles. The evidence supports B, while also noting membrane localization and host-cell plasma-membrane annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "C2-domain features can support a general inference of membrane association, but the sequence alone does not establish localization specifically to cytoplasmic vesicles rather than another membrane compartment.",
    "missing_item_specific_fact": "The protein-specific localization evidence that PfDOC2 shows punctate, vesicle-like localization and has a cytoplasmic-vesicle annotation is absent from the input.",
    "reason": "Choosing B depends on a protein-specific localization annotation or experimental result, not a sufficiently discriminating sequence-based argument supplied by the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasmic vesicle among the listed choices. Membrane and host-cell plasma-membrane annotations do not correspond to another listed option."
  },
  "important_caveats": [
    "The sequence matches the referenced UniProt record, but the author's exact source snapshot is unknown.",
    "The localization evidence supports vesicle-like localization; it does not establish that cytoplasmic vesicle is the protein's exclusive location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I4Z1 (PfDOC2, Plasmodium falciparum) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0031410 'cytoplasmic vesicle' (evidence_id C6/H5, evidence code ECO:0000314 from PubMed:24992295). The subcellular location comment (C5/H4) states the protein 'Localizes in a punctate manner reminiscent of vesicles' (ECO:0000269, PubMed:22246776). The protein is a Double C2 domain protein essential for apicomplexan parasite exocytosis (C9/H2, Science 2012), which is consistent with cytoplasmic vesicle localization. The sequence matches the benchmark input exactly.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5), [C9](#evidence-c9), [H5](#evidence-h5), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains C2 (double C2) domains, which are textbook calcium-dependent lipid-binding modules found in vesicle-trafficking and membrane-fusion proteins (e.g., synaptotagmin, PKC, DOC2 family). Recognition of C2 domains provides a general biological argument linking the protein to cytoplasmic vesicles and exocytotic machinery. This reasoning distinguishes B from the distractors: (A) microtubule associated complex lacks tubulin-binding motifs or MAP-like domains; (C) virus tail/tube is a bacteriophage virion component, irrelevant for a eukaryotic parasite protein; (D) vacuolar membrane is less consistent with C2 domain biology, which is classically associated with secretory/synaptic vesicle fusion rather than vacuolar membranes.


**Missing item-specific fact**

> The precise distinction between 'cytoplasmic vesicle' (GO:0031410) and the co-annotated 'host cell plasma membrane' (GO:0020002, also IDA) as the primary location requires the specific experimental observation of punctate vesicle-like localization (PubMed:22246776). However, since 'host cell plasma membrane' is not among the answer choices, this does not create ambiguity within the provided options.


**Reason**

> The C2 domain identification and its well-established association with vesicle trafficking provides a concrete, general biological argument that meaningfully favors 'cytoplasmic vesicle' over the three distractors. The distractors are sufficiently distinct (a bacteriophage structure, a cytoskeletal complex, a vacuolar membrane) that C2-domain reasoning is adequate to select B without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different compartments. Virus tail/tube (C) is a bacteriophage-specific structure inapplicable to a eukaryotic protein. Microtubule associated complex (A) lacks supporting sequence features. Vacuolar membrane (D) is a plausible membrane location but is less consistent with C2-domain biology than cytoplasmic vesicle. The co-annotated 'host cell plasma membrane' (C7) is not among the options, so it does not create ambiguity within the provided choices.


### Important caveats

- The protein also carries an IDA annotation for 'host cell plasma membrane' (GO:0020002), reflecting transient membrane association during exocytosis. This is not among the answer choices and does not affect the answer, but a model reasoning purely from sequence might note general membrane affinity without specifying vesicle vs. plasma membrane.
- The GO annotation for cytoplasmic vesicle is IDA (experimental, from GeneDB), providing strong evidence. The punctate localization note is also experimentally supported (ECO:0000269).
- The identity of the protein as PfDOC2 was inferred from dataset metadata by the reviewer; the evaluated model only sees the raw sequence. Recognition of C2 domains from sequence is feasible but requires domain-level annotation or structural knowledge.
- The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 confirmed), and the historical entry version 105 (released 2026-01-28) already contains the cytoplasmic vesicle GO annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains C2 (double C2) domains, which are textbook calcium-dependent lipid-binding modules found in vesicle-trafficking and membrane-fusion proteins (e.g., synaptotagmin, PKC, DOC2 family). Recognition of C2 domains provides a general biological argument linking the protein to cytoplasmic vesicles and exocytotic machinery. This reasoning distinguishes B from the distractors: (A) microtubule associated complex lacks tubulin-binding motifs or MAP-like domains; (C) virus tail/tube is a bacteriophage virion component, irrelevant for a eukaryotic parasite protein; (D) vacuolar membrane is less consistent with C2 domain biology, which is classically associated with secretory/synaptic vesicle fusion rather than vacuolar membranes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise distinction between 'cytoplasmic vesicle' (GO:0031410) and the co-annotated 'host cell plasma membrane' (GO:0020002, also IDA) as the primary location requires the specific experimental observation of punctate vesicle-like localization (PubMed:22246776). However, since 'host cell plasma membrane' is not among the answer choices, this does not create ambiguity within the provided options.",
    "reason": "The C2 domain identification and its well-established association with vesicle trafficking provides a concrete, general biological argument that meaningfully favors 'cytoplasmic vesicle' over the three distractors. The distractors are sufficiently distinct (a bacteriophage structure, a cytoskeletal complex, a vacuolar membrane) that C2-domain reasoning is adequate to select B without memorizing the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5",
      "C9",
      "H5",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8I4Z1 (PfDOC2, Plasmodium falciparum) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0031410 'cytoplasmic vesicle' (evidence_id C6/H5, evidence code ECO:0000314 from PubMed:24992295). The subcellular location comment (C5/H4) states the protein 'Localizes in a punctate manner reminiscent of vesicles' (ECO:0000269, PubMed:22246776). The protein is a Double C2 domain protein essential for apicomplexan parasite exocytosis (C9/H2, Science 2012), which is consistent with cytoplasmic vesicle localization. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The protein also carries an IDA annotation for 'host cell plasma membrane' (GO:0020002), reflecting transient membrane association during exocytosis. This is not among the answer choices and does not affect the answer, but a model reasoning purely from sequence might note general membrane affinity without specifying vesicle vs. plasma membrane.",
    "The GO annotation for cytoplasmic vesicle is IDA (experimental, from GeneDB), providing strong evidence. The punctate localization note is also experimentally supported (ECO:0000269).",
    "The identity of the protein as PfDOC2 was inferred from dataset metadata by the reviewer; the evaluated model only sees the raw sequence. Recognition of C2 domains from sequence is feasible but requires domain-level annotation or structural knowledge.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 confirmed), and the historical entry version 105 (released 2026-01-28) already contains the cytoplasmic vesicle GO annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different compartments. Virus tail/tube (C) is a bacteriophage-specific structure inapplicable to a eukaryotic protein. Microtubule associated complex (A) lacks supporting sequence features. Vacuolar membrane (D) is a plausible membrane location but is less consistent with C2-domain biology than cytoplasmic vesicle. The co-annotated 'host cell plasma membrane' (C7) is not among the options, so it does not create ambiguity within the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8I4Z1 (PfDOC2, Plasmodium falciparum) carries an IDA (Inferred from Direct Assay) GO annotation for GO:0031410 'cytoplasmic vesicle' (evidence_id C6/H5, evidence code ECO:0000314 from PubMed:24992295). The subcellular location comment (C5/H4) states the protein 'Localizes in a punctate manner reminiscent of vesicles' (ECO:0000269, PubMed:22246776). The protein is a Double C2 domain protein essential for apicomplexan parasite exocytosis (C9/H2, Science 2012), which is consistent with cytoplasmic vesicle localization. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C6", "C5", "C9", "H5", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains C2 (double C2) domains, which are textbook calcium-dependent lipid-binding modules found in vesicle-trafficking and membrane-fusion proteins (e.g., synaptotagmin, PKC, DOC2 family). Recognition of C2 domains provides a general biological argument linking the protein to cytoplasmic vesicles and exocytotic machinery. This reasoning distinguishes B from the distractors: (A) microtubule associated complex lacks tubulin-binding motifs or MAP-like domains; (C) virus tail/tube is a bacteriophage virion component, irrelevant for a eukaryotic parasite protein; (D) vacuolar membrane is less consistent with C2 domain biology, which is classically associated with secretory/synaptic vesicle fusion rather than vacuolar membranes.",
    "missing_item_specific_fact": "The precise distinction between 'cytoplasmic vesicle' (GO:0031410) and the co-annotated 'host cell plasma membrane' (GO:0020002, also IDA) as the primary location requires the specific experimental observation of punctate vesicle-like localization (PubMed:22246776). However, since 'host cell plasma membrane' is not among the answer choices, this does not create ambiguity within the provided options.",
    "reason": "The C2 domain identification and its well-established association with vesicle trafficking provides a concrete, general biological argument that meaningfully favors 'cytoplasmic vesicle' over the three distractors. The distractors are sufficiently distinct (a bacteriophage structure, a cytoskeletal complex, a vacuolar membrane) that C2-domain reasoning is adequate to select B without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different compartments. Virus tail/tube (C) is a bacteriophage-specific structure inapplicable to a eukaryotic protein. Microtubule associated complex (A) lacks supporting sequence features. Vacuolar membrane (D) is a plausible membrane location but is less consistent with C2-domain biology than cytoplasmic vesicle. The co-annotated 'host cell plasma membrane' (C7) is not among the options, so it does not create ambiguity within the provided choices."
  },
  "important_caveats": [
    "The protein also carries an IDA annotation for 'host cell plasma membrane' (GO:0020002), reflecting transient membrane association during exocytosis. This is not among the answer choices and does not affect the answer, but a model reasoning purely from sequence might note general membrane affinity without specifying vesicle vs. plasma membrane.",
    "The GO annotation for cytoplasmic vesicle is IDA (experimental, from GeneDB), providing strong evidence. The punctate localization note is also experimentally supported (ECO:0000269).",
    "The identity of the protein as PfDOC2 was inferred from dataset metadata by the reviewer; the evaluated model only sees the raw sequence. Recognition of C2 domains from sequence is feasible but requires domain-level annotation or structural knowledge.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (SHA-256 confirmed), and the historical entry version 105 (released 2026-01-28) already contains the cytoplasmic vesicle GO annotation."
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

**Accession:** `Q8I4Z1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"entryVersion":107,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2003-03-01","sequenceVersion":1}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22246776","source":"PubMed"}],"value":"Localizes in a punctate manner reminiscent of vesicles"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24992295","source":"PubMed"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000305","id":"24992295","source":"PubMed"}],"id":"SL-9903","value":"Peripheral membrane protein"}}]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24992295","source":"PubMed"}],"id":"GO:0031410","properties":[{"key":"GoTerm","value":"C:cytoplasmic vesicle"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24992295","source":"PubMed"}],"id":"GO:0020002","properties":[{"key":"GoTerm","value":"C:host cell plasma membrane"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"citation":{"authors":["Farrell A.","Thirugnanam S.","Lorestani A.","Dvorin J.D.","Eidell K.P.","Ferguson D.J.","Anderson-White B.R.","Duraisingh M.T.","Marth G.T.","Gubbels M.J."],"citationCrossReferences":[{"database":"PubMed","id":"22246776"},{"database":"DOI","id":"10.1126/science.1210829"}],"citationType":"journal article","firstPage":"218","id":"22246776","journal":"Science","lastPage":"221","publicationDate":"2012","title":"A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.","volume":"335"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 28-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=22246776; DOI=10.1126/science.1210829;
RA   Farrell A., Thirugnanam S., Lorestani A., Dvorin J.D., Eidell K.P.,
RA   Ferguson D.J., Anderson-White B.R., Duraisingh M.T., Marth G.T.,
RA   Gubbels M.J.;
RT   "A DOC2 protein identified by mutational profiling is essential for
RT   apicomplexan parasite exocytosis.";
RL   Science 335:218-221(2012).
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 47-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000269|PubMed:24992295};
CC       Peripheral membrane protein {ECO:0000305|PubMed:24992295}.
CC       Note=Localizes in a punctate manner reminiscent of vesicles.
CC       {ECO:0000269|PubMed:22246776}.
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 76-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
DR   GO; GO:0031410; C:cytoplasmic vesicle; IDA:GeneDB.
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
DR   GO; GO:0020002; C:host cell plasma membrane; IDA:GeneDB.
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
