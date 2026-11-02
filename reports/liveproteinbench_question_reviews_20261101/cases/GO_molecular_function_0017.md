# GO_molecular_function_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — calcium-dependent phospholipid binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MILDKFKNIVNLSNSNTEKEEGKNAEINENNDPNTQLAHEPSIVEADEKTFFDEMLGAPQYTYDEFLQVLKNPIEERGDTEDMKKHWGYPRRWKVILWDLHIQNYMNNDFNAFVDFDFGGNREECRIQRGSTMKIYAKGKTKNCLRTPVVTNVATEQKKNMNFRNVFEYRGSYLDLENEKLRIRVWEYKQFTLNKLEGIYEEPLLSFAVGEIYNETTLYKFIKDSRVKRCRLYFQLYFQELYDFELSFLNWSFSDLLSSSYIQAKSYNYLSNKNNVKKRYIDDTSCNIFPHMCKNFKRFHKKKIYRKVRNYDIDKNFSFNTALSDDSDERKNKNDRTIKNLEKLFVRNLTLMQNIEENEDMSYKNLQNINLPNPRVTITLSHTPKGHEGLNIISIEQKSIRFPIWENLGEIYFRGTLRDLDVSYLNIKVEDMSAPKSAREIGTCQISLKGIVDYPYVMHELEAPSWLVKEAKYEGWENKLNEWKLGTVEGKVIINRVPRYRQRGDIYHIDSKQPYLIVHIFNIDKIITVDNIKELDTYVEVSFDETSRRTRLMKKTLSPNYDSQISIPLRFNNKNDINYENLSKKGLIYIDVWGKSEDIVYIGGISISPYEIFFNEKNVRRNKTKLEHIDLETNVKITYDTVVYRGCKKLCFLHDDQRMSNIHFSIWTYPDILGNSTNQKKIVAPVSFNTTMNFPIKLAEKYNKLKKLFMEVLKTIKSIPENCTDVNTSTRFYNYELINQRKEKHFLPTLITSIKSPYCAESMNAIFHYVRCIPFIHKKENIIFTPDFTLQLKGGNALDHSLLLCSLFLGIPVLAFVCFGTLWDKQKHSWVATFEYNDEKNYGIVKFWETTTGNVYILKKRFIDHNRLKGLELKLKESKYKSHLRNGFLQRYENNTDINYIKEQTKRHIKQLFKNRINDIPIGGPSLPYKTIDLIFNHKNIYVNLQHSSPLNIWYDYWKFDFWFPFSSIEYNLQPSFTIKSFTHKMEDMELDKIAKELRTNIEKNINIYRASRNLSTRWNRDETLEIFLQVGLELLHQLNTSRKEDVLLAKLKIEDWKKALYHKVPQSHRLLGFPYHFNTYKSKFISDKLISTLAILESRDRSLCLSLAVCLYSLPGNFISCYIYIITCVKITQRELRKMEIIKEKAQRMAEIKNSQKKKKSSDDQNIDIKTMDDVEEKETFSSTNLDDTLHDEHTDIDTEKKKHEKDNYKNKKIKNTKLKDANIDNEEKDDHHHITDKKVSKSSDLIHSFDKNDISKNTFDKEEFINNLDKDKKYSSFKKGNVVNKKVSIKNEPSINIYEDHKIYDDENISNNIDNMENNQDEIYNLRQGKTIINEFQQVKKPQKYTINEKRDDIKTKKKRSKEKKKQDKLEFEKLIQSNAYFEQEKKKLQEDIKKLEKDKEQFQKEKIRREEKEKQLLLEEKIKLQKEKELFENEKLERKMSYMLKINELEKKKNERNKMEKSYKRMIQKDKEKKKKKESRDKIRRGEEEKMSADENMKEEQKMREEQKVGEEQKVGEEQKVGEEQKLREEQKMREEQKMREEQKMREEQKMREEQKVREEQKMREEQKMREEQKMREEQKVREEQKLREEQKMREEQKMREEQKMREEEKIREEEQMKREKKMRREEKKKRVQEPIKIDEIQVYDIIKNEKMKKKEEKEEKKRKKKKEDIEDKYKIGKEASLDENNNERQIKSKNIQEISDYEYKNIKENKNLNKFDEKLDLNQIYSKASNFYDNQEKKRRTIKVHANRKENSDSTFSHIDDSIKNKKEYLEDSNIARYLYEKRKHDLIGKGNYNFDEPHYGKKMNNVAYQDIKGSNLFKGFIEEPSSKKSPQKKKIVIVRKN

[Multiple Choices]
A. ATPase-coupled transmembrane transporter activity
B. monooxygenase activity
C. mechanosensitive monoatomic ion channel activity
D. calcium-dependent phospholipid binding
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

> The exact sequence matches the annotated PfDOC2 protein. Its UniProt function annotation reports calcium and phospholipid binding with experimental evidence, and its GO annotation assigns calcium-dependent phospholipid binding with IDA evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence does not show an obvious multipass transporter or ion-channel architecture, nor an evident monooxygenase catalytic architecture, making those alternatives less plausible. But that elimination does not establish calcium-dependent phospholipid binding.


**Missing item-specific fact**

> That this particular protein binds calcium and phospholipids; the supporting experimental annotation is not supplied in the question.


**Reason**

> A C2-domain-like sequence may suggest membrane or lipid interactions, but sequence-based inference alone does not establish calcium dependence or phospholipid binding for this protein. Choosing D depends on a protein-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports D for the sequence-matched protein; no evidence supports another listed option as an equally defensible answer.


### Important caveats

- The protein identity and functional annotations are reviewer-only evidence, not information provided to the evaluated model.
- The GO annotation is reported as IDA, and the UniProt function statement cites experimental evidence; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence does not show an obvious multipass transporter or ion-channel architecture, nor an evident monooxygenase catalytic architecture, making those alternatives less plausible. But that elimination does not establish calcium-dependent phospholipid binding.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein binds calcium and phospholipids; the supporting experimental annotation is not supplied in the question.",
    "reason": "A C2-domain-like sequence may suggest membrane or lipid interactions, but sequence-based inference alone does not establish calcium dependence or phospholipid binding for this protein. Choosing D depends on a protein-specific fact absent from the input."
  },
  "case_id": "GO_molecular_function_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated PfDOC2 protein. Its UniProt function annotation reports calcium and phospholipid binding with experimental evidence, and its GO annotation assigns calcium-dependent phospholipid binding with IDA evidence."
  },
  "important_caveats": [
    "The protein identity and functional annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The GO annotation is reported as IDA, and the UniProt function statement cites experimental evidence; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D for the sequence-matched protein; no evidence supports another listed option as an equally defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated PfDOC2 protein. Its UniProt function annotation reports calcium and phospholipid binding with experimental evidence, and its GO annotation assigns calcium-dependent phospholipid binding with IDA evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence does not show an obvious multipass transporter or ion-channel architecture, nor an evident monooxygenase catalytic architecture, making those alternatives less plausible. But that elimination does not establish calcium-dependent phospholipid binding.",
    "missing_item_specific_fact": "That this particular protein binds calcium and phospholipids; the supporting experimental annotation is not supplied in the question.",
    "reason": "A C2-domain-like sequence may suggest membrane or lipid interactions, but sequence-based inference alone does not establish calcium dependence or phospholipid binding for this protein. Choosing D depends on a protein-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D for the sequence-matched protein; no evidence supports another listed option as an equally defensible answer."
  },
  "important_caveats": [
    "The protein identity and functional annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The GO annotation is reported as IDA, and the UniProt function statement cites experimental evidence; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8I4Z1 (PfDOC2, C2 domain-containing protein) carries GO:0005544 (calcium-dependent phospholipid binding) with evidence code IDA (Inferred by Direct Assay, ECO:0000314). The FUNCTION comment explicitly states 'Binds calcium and phospholipids' supported by experimental evidence (ECO:0000269, PubMed:24992295 and PubMed:22246776). The protein is named 'C2 domain-containing protein' (PfDOC2 = Plasmodium falciparum Double C2 domain protein). The reference title (C8) confirms: 'Plasmodium falciparum double C2 domain protein, PfDOC2, binds to calcium when associated with membranes.' The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed in both current and historical snapshots).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C4](#evidence-c4), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination of distractors is partially feasible: (B) monooxygenase requires heme-binding motifs (e.g., FxxGxxxCxG for P450s) absent here; (A) ATPase-coupled transport requires Walker A/B motifs and transmembrane helices absent here; (C) mechanosensitive ion channel requires specific TM topology inconsistent with a 1846 AA protein dominated by a long C-terminal coiled-coil/repetitive region. However, the positive identification of C2 domains—clusters of conserved aspartate residues in a ~130 AA beta-sandwich fold—from a 1846 AA raw sequence is the critical discriminating step that cannot be reliably performed by general reasoning alone.


**Missing item-specific fact**

> The specific identification of two C2 domain motifs within this 1846 amino acid Plasmodium falciparum protein. While C2 domains are well-known calcium-dependent phospholipid binding modules, their sequence conservation is moderate, and identifying them from raw sequence without domain-prediction tools or prior annotation of this particular protein (PfDOC2) is not a straightforward reasoning task. The benchmark provides no domain annotations, no structural information, and no organism context beyond the raw sequence.


**Reason**

> The model must positively identify C2 domain architecture in this specific sequence to select D over the eliminated alternatives. While elimination of A, B, and C through absence of characteristic motifs provides partial reasoning support, the positive assignment to 'calcium-dependent phospholipid binding' requires recognizing C2 domain features (conserved Asp clusters, ~130 AA folds) embedded in a very long, compositionally heterogeneous sequence. This identification is effectively a domain-annotation lookup rather than a deductive inference from general principles. The protein's identity as PfDOC2 and its C2 domain content are item-specific facts absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct functional categories (transporter, enzyme, channel, binding protein). If C2 domains are correctly identified, only D is defensible. The distractors lack the defining motifs of their respective categories (no P450 heme-binding for B, no Walker motifs/TM topology for A, no channel architecture for C), so they are not genuinely ambiguous once the correct domain is recognized.


### Important caveats

- The GO annotation evidence code is IDA (direct assay), indicating experimental support, not mere computational prediction.
- The protein is from Plasmodium falciparum, a parasitic apicomplexan; C2 domain biology is well-characterized in mammalian systems (synaptotagmin, PKC) but the specific PfDOC2 annotation relies on parasite-specific experiments (PubMed:24992295, 22246776).
- The 1846 AA sequence contains a large C-terminal region (~600+ residues) rich in E/K/Q repeats (coiled-coil-like), which is atypical for any of the four functional categories and may add noise to domain identification.
- The benchmark provides no organism name, no domain annotations, and no structural context—only the raw amino acid sequence.
- The sequence match between benchmark input and UniProt Q8I4Z1 is exact (SHA256 confirmed), so the annotation applies directly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination of distractors is partially feasible: (B) monooxygenase requires heme-binding motifs (e.g., FxxGxxxCxG for P450s) absent here; (A) ATPase-coupled transport requires Walker A/B motifs and transmembrane helices absent here; (C) mechanosensitive ion channel requires specific TM topology inconsistent with a 1846 AA protein dominated by a long C-terminal coiled-coil/repetitive region. However, the positive identification of C2 domains—clusters of conserved aspartate residues in a ~130 AA beta-sandwich fold—from a 1846 AA raw sequence is the critical discriminating step that cannot be reliably performed by general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of two C2 domain motifs within this 1846 amino acid Plasmodium falciparum protein. While C2 domains are well-known calcium-dependent phospholipid binding modules, their sequence conservation is moderate, and identifying them from raw sequence without domain-prediction tools or prior annotation of this particular protein (PfDOC2) is not a straightforward reasoning task. The benchmark provides no domain annotations, no structural information, and no organism context beyond the raw sequence.",
    "reason": "The model must positively identify C2 domain architecture in this specific sequence to select D over the eliminated alternatives. While elimination of A, B, and C through absence of characteristic motifs provides partial reasoning support, the positive assignment to 'calcium-dependent phospholipid binding' requires recognizing C2 domain features (conserved Asp clusters, ~130 AA folds) embedded in a very long, compositionally heterogeneous sequence. This identification is effectively a domain-annotation lookup rather than a deductive inference from general principles. The protein's identity as PfDOC2 and its C2 domain content are item-specific facts absent from the model input."
  },
  "case_id": "GO_molecular_function_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C4",
      "C8",
      "H4",
      "H5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8I4Z1 (PfDOC2, C2 domain-containing protein) carries GO:0005544 (calcium-dependent phospholipid binding) with evidence code IDA (Inferred by Direct Assay, ECO:0000314). The FUNCTION comment explicitly states 'Binds calcium and phospholipids' supported by experimental evidence (ECO:0000269, PubMed:24992295 and PubMed:22246776). The protein is named 'C2 domain-containing protein' (PfDOC2 = Plasmodium falciparum Double C2 domain protein). The reference title (C8) confirms: 'Plasmodium falciparum double C2 domain protein, PfDOC2, binds to calcium when associated with membranes.' The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed in both current and historical snapshots)."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (direct assay), indicating experimental support, not mere computational prediction.",
    "The protein is from Plasmodium falciparum, a parasitic apicomplexan; C2 domain biology is well-characterized in mammalian systems (synaptotagmin, PKC) but the specific PfDOC2 annotation relies on parasite-specific experiments (PubMed:24992295, 22246776).",
    "The 1846 AA sequence contains a large C-terminal region (~600+ residues) rich in E/K/Q repeats (coiled-coil-like), which is atypical for any of the four functional categories and may add noise to domain identification.",
    "The benchmark provides no organism name, no domain annotations, and no structural context—only the raw amino acid sequence.",
    "The sequence match between benchmark input and UniProt Q8I4Z1 is exact (SHA256 confirmed), so the annotation applies directly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct functional categories (transporter, enzyme, channel, binding protein). If C2 domains are correctly identified, only D is defensible. The distractors lack the defining motifs of their respective categories (no P450 heme-binding for B, no Walker motifs/TM topology for A, no channel architecture for C), so they are not genuinely ambiguous once the correct domain is recognized."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8I4Z1 (PfDOC2, C2 domain-containing protein) carries GO:0005544 (calcium-dependent phospholipid binding) with evidence code IDA (Inferred by Direct Assay, ECO:0000314). The FUNCTION comment explicitly states 'Binds calcium and phospholipids' supported by experimental evidence (ECO:0000269, PubMed:24992295 and PubMed:22246776). The protein is named 'C2 domain-containing protein' (PfDOC2 = Plasmodium falciparum Double C2 domain protein). The reference title (C8) confirms: 'Plasmodium falciparum double C2 domain protein, PfDOC2, binds to calcium when associated with membranes.' The sequence in the benchmark matches the UniProt sequence exactly (SHA256 match confirmed in both current and historical snapshots).",
    "evidence_ids": ["C5", "C6", "C4", "C8", "H4", "H5", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination of distractors is partially feasible: (B) monooxygenase requires heme-binding motifs (e.g., FxxGxxxCxG for P450s) absent here; (A) ATPase-coupled transport requires Walker A/B motifs and transmembrane helices absent here; (C) mechanosensitive ion channel requires specific TM topology inconsistent with a 1846 AA protein dominated by a long C-terminal coiled-coil/repetitive region. However, the positive identification of C2 domains—clusters of conserved aspartate residues in a ~130 AA beta-sandwich fold—from a 1846 AA raw sequence is the critical discriminating step that cannot be reliably performed by general reasoning alone.",
    "missing_item_specific_fact": "The specific identification of two C2 domain motifs within this 1846 amino acid Plasmodium falciparum protein. While C2 domains are well-known calcium-dependent phospholipid binding modules, their sequence conservation is moderate, and identifying them from raw sequence without domain-prediction tools or prior annotation of this particular protein (PfDOC2) is not a straightforward reasoning task. The benchmark provides no domain annotations, no structural information, and no organism context beyond the raw sequence.",
    "reason": "The model must positively identify C2 domain architecture in this specific sequence to select D over the eliminated alternatives. While elimination of A, B, and C through absence of characteristic motifs provides partial reasoning support, the positive assignment to 'calcium-dependent phospholipid binding' requires recognizing C2 domain features (conserved Asp clusters, ~130 AA folds) embedded in a very long, compositionally heterogeneous sequence. This identification is effectively a domain-annotation lookup rather than a deductive inference from general principles. The protein's identity as PfDOC2 and its C2 domain content are item-specific facts absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct functional categories (transporter, enzyme, channel, binding protein). If C2 domains are correctly identified, only D is defensible. The distractors lack the defining motifs of their respective categories (no P450 heme-binding for B, no Walker motifs/TM topology for A, no channel architecture for C), so they are not genuinely ambiguous once the correct domain is recognized."
  },
  "important_caveats": [
    "The GO annotation evidence code is IDA (direct assay), indicating experimental support, not mere computational prediction.",
    "The protein is from Plasmodium falciparum, a parasitic apicomplexan; C2 domain biology is well-characterized in mammalian systems (synaptotagmin, PKC) but the specific PfDOC2 annotation relies on parasite-specific experiments (PubMed:24992295, 22246776).",
    "The 1846 AA sequence contains a large C-terminal region (~600+ residues) rich in E/K/Q repeats (coiled-coil-like), which is atypical for any of the four functional categories and may add noise to domain identification.",
    "The benchmark provides no organism name, no domain annotations, and no structural context—only the raw amino acid sequence.",
    "The sequence match between benchmark input and UniProt Q8I4Z1 is exact (SHA256 confirmed), so the annotation applies directly."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
"Q8I4Z1"
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

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

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"C2 domain-containing protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24992295","source":"PubMed"}],"value":"PfDOC2"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"22246776","source":"PubMed"}],"value":"PfDOC2.1"}]}}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22246776","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24992295","source":"PubMed"}],"value":"Binds calcium and phospholipids (PubMed:24992295). Regulates microneme secretion (PubMed:22246776)"}]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24992295","source":"PubMed"}],"id":"GO:0005544","properties":[{"key":"GoTerm","value":"F:calcium-dependent phospholipid binding"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I4Z1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:04.463619+00:00.  

```json
{"citation":{"authors":["Jean S.","Zapata-Jenks M.A.","Farley J.M.","Tracy E.","Mayer D.C."],"citationCrossReferences":[{"database":"PubMed","id":"24992295"},{"database":"DOI","id":"10.1016/j.exppara.2014.06.015"}],"citationType":"journal article","firstPage":"91","id":"24992295","journal":"Exp. Parasitol.","lastPage":"95","publicationDate":"2014","title":"Plasmodium falciparum double C2 domain protein, PfDOC2, binds to calcium when associated with membranes.","volume":"144"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `465966d49d354ed84688db9a7fdae65a19ac0336766daba70ba72191fea24934`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
ID   DOC2_PLAF7              Reviewed;        1846 AA.
AC   Q8I4Z1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2003, sequence version 1.
DT   28-JAN-2026, entry version 105.
DE   RecName: Full=C2 domain-containing protein {ECO:0000305};
DE            Short=PfDOC2 {ECO:0000303|PubMed:24992295};
DE            Short=PfDOC2.1 {ECO:0000303|PubMed:22246776};
GN   ORFNames=PF3D7_1243900 {ECO:0000312|EMBL:CZT99595.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 44-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
CC   -!- FUNCTION: Binds calcium and phospholipids (PubMed:24992295). Regulates
CC       microneme secretion (PubMed:22246776). {ECO:0000269|PubMed:22246776,
CC       ECO:0000269|PubMed:24992295}.
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I4Z1?format=txt&versions=105)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:32:07.535755+00:00.  

```text
DR   GO; GO:0005544; F:calcium-dependent phospholipid binding; IDA:GeneDB.
```

Source SHA-256: `1f08d96ca6a1c864937819889956f4679b1f1b28e0a8a6efdc799b93d2f51f99`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
