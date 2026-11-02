# GO_cellular_component_0031

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — virion component

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGLNEILLPEVHLNSPIVRYKLFYYILHGQLPNDLEPDDLGPLANQNWKAIRAEESQVHARLKQIRVELIARIPSLRWTRSQREIAILIWPRILPILQAYDLRQSMQLPTVWEKLTQSTVNLISDGLERVVLHISNQLTGKPNLFTRSRAGQDAKDYSIPSTRELSQIWFNNEWSGSVKTWLMIKYRMRQLITNQKTGELTDLVTIVDTRSTLCIITPELVALYSNEHKALTYLTFEMVLMVTDMLEGRLNVSSLCTASHYLSPLKKRIEILLTLVDDLALLMGDKVYGVVSSLESFVYAQLQYGDPVVDIKGTFYGFICNEILDLLTEDNIFTEEEANKVLLDLTSQFDNLSPDLTAELLCIMRLWGHPTLTASQAASKVRESMCAPKVLDFQTIMKTLAFFHAILINGYRRSHNGIWPPTTLHGNAPKSLIEMRHDNSELKYEYVLKNWKSISMLRIHKCFDASPDEDLSIFMKDKAISCPKQDWMGVFRRSLIKQRYRDANRPLPQPFNRRLLLNFLEDDRFDPIKELEYVTSGEYLRDPEFCASYSLKEKEIKATGRIFAKMTKRMRSCQVIAESLLANHAGKLMRENGVVLDQLKLTKSLLTMNQIGIISEHSRRSTADNMTLAHSGSNKHRINNSQFKKNKDSKHEMPDDGFEIAACFLTTDLTKYCLNWRYQVIIPFARTLNSMYGVPHLFEWIHLRLMRSTLYVGDPFNPPSDPTQLDLDTALNDDIFIVSPRGGIEGLCQKLWTMISISTIILSATEANTRVMSMVQGDNQAIAITTRVVRSLSHTEKKEQAYKASKLFFERLRANNHGIGHHLKEQETILSSDFFIYSKRVFYKGRILTQALKNVSKMCLTADILGECSQASCSNLATTVMRLTENGVEKDLCYFLNAFMTIRQLCYDLVFPQTKSLSQDITNAYLNHPILISRLCLLPSQLGGLNFFSCSRLFNRNIGDPLVSAIADVKRLIKAGCLDIWVLYNILGRRPGKGKWSTLAADPYTLNIDYLVPSTTFLKKHAQYTLMERSVNPMLRGVFSENAAEEEEELAQYLLDREVVMPRVAHVILAQSSCGRRKQIQGYLDSTRTIIRYSLEVRPLSAKKLNTVIEYNLLYLSYNLEIIEKPNIVQPFLNAINVDTCSIDIARSLRKLSWATLLNGRPIEGLETPDPIELVHGCLIIGSDECEHCSSGDDKFTWFFLPKGIRLDNDPAFNPPIRVPYIGSKTDERRVASMAYIKGASVSLKSALRLAGVYIWAFGDTEESWQDAYELASTRVNLTLEQLQSLTPLPTSANLVHRLDDGTTQLKFTPASSYAFSSFVHISNDCQVLEIDDQVTDSNLIYQQVMITGLALIETWNNPPINFSVYETTLHLHTGSSCCIRPVESCVVNPPLLPVPFINVPQMNKFVYDPEPLSLLEMEKIEDIAYQTRIGGLDQIPLLEKIPLLAHLTAKQMVNSITGLDEATSIVNDAVVQADYTSNWISECCYTYIDSVFVYSGWALLLELSYQMYYLRIQGIQGILDYVYMTLRRIPGMAITGISSTISHPRILRRCINLDVIAPINSPHIASLDYTKLSIDAVMWGTKQVLTNISQGIDYEIVVPSESQLTLSDRVLNLVARKLSLLAIIWANYNYPPKVKGMSPEDKCQALTTHLLQTVEYVEHIQIEKTNIRRMVIEPKLTAYPSNLFYLSRKLLNAIRDSEEGQFLIASYYNSFGYLEPILMESKIFNLSSSESASLTEFDFILNLELSETSLEKYSLPSLLMTAENMDNPFPQPPLHHVLRPLGLSSTSWYKTISVLNYISHMKIYDGAHLYLAEGSGASMSLIETFLPGETIWYNSLFNSGENPPQRNFAPLPTQFIESVPYRLIQAGIAAGSGVVQSFYPLWNGNSDITDLSTKTSVEYIIHKVGADTCALVHVDLEGVPGSMNSMLERAQVHALLITVTVLKPGGLLILKASWEPFNRFSFLLTILWQFFSTIRILRSSYSDPNNHEVYIIATLAVDPTTSSFTTALNRARTLNEQGFSLIPPELVSEYWRRRVEQGQIIQDRIDKVISECVRDQYLADNNIILQAGGTPSTRKWLDLPDYPSFNELQSEMARLITIHLKEVIEILKGQSSDHDTLLFTSYNVGPLGKINTILRLIVERILMYTVRNWCILPTQTRLTLRQSIELGEFRLRDVITPMEILKLSPNRKYLKSALNQSTFNHLMGETSDILLNRAYQKRIWKAIGCVIYCFGLLTPDVEDSERIDIDNDIPDYDIHGDII

[Multiple Choices]
A. host cell
B. synapse
C. virion component
D. fungal-type vacuole
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

> The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.


**Missing item-specific fact**

> Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.


**Reason**

> The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense.


### Important caveats

- The sequence match is exact, but the accession and database annotation were reviewer-only information.
- The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.
- The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.",
    "reason": "The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database annotation were reviewer-only information.",
    "The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.",
    "The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mumps virus L protein. UniProt records its virion location with experimental evidence codes citing two mass-spectrometry studies; the historical record also contains this annotation. This supports choice C, though the primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large viral RNA-directed RNA polymerase, making a viral association plausible. That alone does not establish that this particular protein is incorporated into virions rather than being present only in infected host cells.",
    "missing_item_specific_fact": "Whether this mumps virus L protein is physically present in virions, as reported by the cited protein-composition studies.",
    "reason": "The key distinction depends on protein-specific localization evidence absent from the sequence and choices. Recognizing the protein or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choice C is supported as a virion component, but the viral polymerase also functions in infected host cells. Because the question asks for a primary location without specifying whether it means virion incorporation or intracellular location during replication, A may also be defensible in a broad sense."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database annotation were reviewer-only information.",
    "The UniProt location annotation cites experimental evidence; the cited papers were not independently assessed here.",
    "The historical source snapshot supports that the annotation existed by the retrieved historical record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.


**Missing item-specific fact**

> The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.


**Reason**

> While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase.


### Important caveats

- The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).
- The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.
- The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.
- The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.",
    "reason": "While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity."
  },
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational."
  },
  "important_caveats": [
    "The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).",
    "The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC50 (RNA-directed RNA polymerase L of Mumps virus, strain L-Zagreb vaccine) exactly (SHA256 confirmed, 2261 aa). The UniProt subcellular location annotation states 'Virion' with experimental evidence codes ECO:0000269 from two mass-spectrometry studies (PubMed 26768080, 30326905) that identified the L protein in purified virions. The GO annotation GO:0044423 (virion component) is assigned via IEA:UniProtKB-KW. This is consistent with Mononegavirales biology: the L polymerase must be packaged within the virion to initiate transcription upon entry. The evidence is experimental (direct assay), not merely computational.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A trained virologist might note the protein's large size (~2261 aa), absence of eukaryotic targeting signals (no NLS, no mitochondrial presequence, no ER signal peptide), and presence of RdRp-conserved motifs, suggesting a viral polymerase. General knowledge that negative-strand RNA viruses (Mononegavirales) package their L polymerase into the virion could then favor 'virion component.' However, recognizing the protein specifically as a Mononegavirales L protein from raw sequence (vs. a positive-strand RNA virus polymerase, a retroviral RT, or a host RNA polymerase) is extremely difficult without database lookup, and the critical distinction between 'virion component' (C) and 'host cell' (A) — since the L protein is synthesized and functions in the host cytoplasm — is a protein-specific annotation decision.",
    "missing_item_specific_fact": "The specific fact that this protein is a structural component of the virus particle (packaged into the virion) rather than merely a protein that functions within the host cell. This requires either recognizing the exact protein identity from sequence (lookup) or knowing that the L protein of this particular virus is annotated as a virion component in databases.",
    "reason": "While general virology principles (Mononegavirales package their polymerase) provide a partial reasoning path, the model must first correctly identify the protein as a viral RdRp of the correct viral family from 2261 residues of sequence alone, and then know the packaging requirement. The distinction between 'virion component' and 'host cell' for a protein that functions in the host cytoplasm but is also structurally packaged is a protein-specific annotation fact. The unusual distractor set (synapse, fungal-type vacuole) further suggests the question was constructed with knowledge of the protein's database identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The L protein is synthesized and functions in the host cell cytoplasm (RNA replication/transcription), making 'host cell' (GO:0043657) a superficially defensible answer. The UniProt annotation specifically assigns 'Virion' based on mass-spectrometry detection in purified virions, establishing it as a structural virion component. However, without that specific annotation knowledge, a reasoner might argue the 'primary' location is where the protein is made and functions (host cell). Options B (synapse) and D (fungal-type vacuole) are clearly inapplicable to a viral polymerase."
  },
  "important_caveats": [
    "The GO annotation GO:0044423 is assigned via IEA:UniProtKB-KW (inferred from keyword), while the underlying subcellular location evidence is experimental (ECO:0000269, direct assay from mass spectrometry of purified virions).",
    "The sequence is from a virus (Mumps virus genotype N, L-Zagreb vaccine strain); the 'cellular component' framework is applied to a non-cellular entity, which introduces conceptual tension in the GO annotation.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) and accession identity, but this identification was not available to the evaluated model.",
    "The protein was first publicly released in UniProt on 2025-04-09; the benchmark construction date is unknown but the historical entry version 115 (released 2026-01) already contains the virion annotation."
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

**Accession:** `Q5SC50` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 115. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
"Q5SC50"
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis","Mumps orthorubulavirus"],"scientificName":"Mumps virus genotype N (strain L-Zagreb vaccine)","taxonId":301186}
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Large structural protein"}},{"fullName":{"value":"Replicase"}},{"fullName":{"value":"Transcriptase"}}],"includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P28887","source":"UniProtKB"}],"value":"2.7.7.48"}],"fullName":{"value":"RNA-directed RNA polymerase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"3.6.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"GTP phosphohydrolase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PRNTase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"2.7.7.88"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"GDP polyribonucleotidyltransferase"}}},{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"mRNA (guanine-N(7)-)-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"G-N7-MTase"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"mRNA (nucleoside-2'-O-)-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03523","source":"UniProtKB"}],"value":"N1-2'-O-MTase"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"mRNA cap methyltransferase"}}}],"recommendedName":{"fullName":{"value":"RNA-directed RNA polymerase L"},"shortNames":[{"value":"Protein L"}]}}
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"26768080","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30326905","source":"PubMed"}],"id":"SL-0274","value":"Virion"}}]}
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
{"citation":{"authors":["Brgles M.","Bonta M.","Santak M.","Jagusic M.","Forcic D.","Halassy B.","Allmaier G.","Marchetti-Deschmann M."],"citationCrossReferences":[{"database":"PubMed","id":"26768080"},{"database":"DOI","id":"10.1186/s12985-016-0463-0"}],"citationType":"journal article","firstPage":"9","id":"26768080","journal":"Virol. J.","lastPage":"9","publicationDate":"2016","title":"Identification of mumps virus protein and lipid composition by mass spectrometry.","volume":"13"},"referenceComments":[{"type":"STRAIN","value":"L-Zagreb vaccine"}],"referenceNumber":2,"referencePositions":["SUBCELLULAR LOCATION"]}
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC50.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:28.360866+00:00.  

```json
{"citation":{"authors":["Sviben D.","Forcic D.","Halassy B.","Allmaier G.","Marchetti-Deschmann M.","Brgles M."],"citationCrossReferences":[{"database":"PubMed","id":"30326905"},{"database":"DOI","id":"10.1186/s12985-018-1073-9"}],"citationType":"journal article","firstPage":"160","id":"30326905","journal":"Virol. J.","lastPage":"160","publicationDate":"2018","title":"Mass spectrometry-based investigation of measles and mumps virus proteome.","volume":"15"},"referenceComments":[{"type":"STRAIN","value":"L-Zagreb vaccine"}],"referenceNumber":3,"referencePositions":["SUBCELLULAR LOCATION"]}
```

Source SHA-256: `4e69a2df089cd4a5fce65ebdc72930cc412ef87044994566f3719738b83af341`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)  
**Locator:** `lines 1-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:31:32.272875+00:00.  

```text
ID   L_MUMPZ                 Reviewed;        2261 AA.
AC   Q5SC50;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-DEC-2004, sequence version 1.
DT   28-JAN-2026, entry version 115.
DE   RecName: Full=RNA-directed RNA polymerase L;
DE            Short=Protein L;
DE   AltName: Full=Large structural protein;
DE   AltName: Full=Replicase;
DE   AltName: Full=Transcriptase;
DE   Includes:
DE     RecName: Full=RNA-directed RNA polymerase;
DE              EC=2.7.7.48 {ECO:0000250|UniProtKB:P28887};
DE   Includes:
DE     RecName: Full=GTP phosphohydrolase {ECO:0000250|UniProtKB:P03523};
DE              EC=3.6.1.- {ECO:0000250|UniProtKB:P03523};
DE   Includes:
DE     RecName: Full=GDP polyribonucleotidyltransferase {ECO:0000305};
DE              EC=2.7.7.88 {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=PRNTase {ECO:0000305};
DE   Includes:
DE     RecName: Full=mRNA cap methyltransferase {ECO:0000305};
DE     AltName: Full=mRNA (guanine-N(7)-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=G-N7-MTase {ECO:0000250|UniProtKB:P03523};
DE     AltName: Full=mRNA (nucleoside-2'-O-)-methyltransferase {ECO:0000250|UniProtKB:P03523};
DE              Short=N1-2'-O-MTase {ECO:0000250|UniProtKB:P03523};
GN   Name=L;
OS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.
OX   NCBI_TaxID=301186;
OH   NCBI_TaxID=9606; Homo sapiens (Human).
```

Source SHA-256: `676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)  
**Locator:** `lines 42-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:31:32.272875+00:00.  

```text
RN   [2]
RP   SUBCELLULAR LOCATION.
RC   STRAIN=L-Zagreb vaccine;
RX   PubMed=26768080; DOI=10.1186/s12985-016-0463-0;
RA   Brgles M., Bonta M., Santak M., Jagusic M., Forcic D., Halassy B.,
RA   Allmaier G., Marchetti-Deschmann M.;
RT   "Identification of mumps virus protein and lipid composition by mass
RT   spectrometry.";
RL   Virol. J. 13:9-9(2016).
```

Source SHA-256: `676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)  
**Locator:** `lines 51-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:31:32.272875+00:00.  

```text
RN   [3]
RP   SUBCELLULAR LOCATION.
RC   STRAIN=L-Zagreb vaccine;
RX   PubMed=30326905; DOI=10.1186/s12985-018-1073-9;
RA   Sviben D., Forcic D., Halassy B., Allmaier G., Marchetti-Deschmann M.,
RA   Brgles M.;
RT   "Mass spectrometry-based investigation of measles and mumps virus
RT   proteome.";
RL   Virol. J. 15:160-160(2018).
```

Source SHA-256: `676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)  
**Locator:** `lines 124-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:31:32.272875+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Virion {ECO:0000269|PubMed:26768080,
CC       ECO:0000269|PubMed:30326905}.
```

Source SHA-256: `676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC50?format=txt&versions=115)  
**Locator:** `lines 137-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 115 / 1.  
**Retrieved:** 2026-11-02T04:31:32.272875+00:00.  

```text
DR   GO; GO:0044423; C:virion component; IEA:UniProtKB-KW.
```

Source SHA-256: `676968ba30768891b0cb22832ede3d7414c5ea7b859f1cce1787e8afbc144ec7`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 257048-257062`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044423
name: virion component
namespace: cellular_component
alt_id: GO:0019012
def: "Any constituent part of a virion, a complete fully infectious extracellular virus particle." [GOC:jl]
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
synonym: "complete virus particle" RELATED []
synonym: "virion" RELATED []
synonym: "virion part" EXACT []
xref: Wikipedia:Virus
is_a: GO:0005575 ! cellular_component

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
