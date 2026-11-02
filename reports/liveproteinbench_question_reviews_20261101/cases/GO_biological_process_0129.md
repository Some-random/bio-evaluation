# GO_biological_process_0129

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — lipopolysaccharide core region biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. carotenoid biosynthetic process
B. lipopolysaccharide core region biosynthetic process
C. meiotic DNA integrity checkpoint signaling
D. cell adhesion
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

### Expected-answer support: contradicted

> The sequence matches MCR-2, whose reported activity is adding phosphoethanolamine to lipid A. That is distinct from synthesizing the LPS core region. The B annotation exists, but it is computationally assigned (IEA:TreeGrafter) and does not outweigh the more specific functional evidence for the different process.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic segments and a large enzymatic region, but those features do not identify its substrate or distinguish the listed biosynthetic pathways with confidence.


**Missing item-specific fact**

> The protein-specific activity—that MCR-2 modifies lipid A by transferring phosphoethanolamine—and its database GO annotation are not supplied in the question.


**Reason**

> Choosing among these processes requires knowing the particular protein's function or annotation; exact-sequence recognition or a generic membrane-protein heuristic would not provide a biological argument for the specific GO term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices do not include lipid A modification, the reported activity. B is the only LPS-related option, but its specific reference to core-region biosynthesis does not describe that activity.


### Important caveats

- The B GO assignment applies to the sequence but is computationally inferred, not presented as experimental evidence.
- The reported functional annotation says MCR-2 probably catalyzes lipid A modification; it does not establish that the protein has no other biological effects.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments and a large enzymatic region, but those features do not identify its substrate or distinguish the listed biosynthetic pathways with confidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific activity—that MCR-2 modifies lipid A by transferring phosphoethanolamine—and its database GO annotation are not supplied in the question.",
    "reason": "Choosing among these processes requires knowing the particular protein's function or annotation; exact-sequence recognition or a generic membrane-protein heuristic would not provide a biological argument for the specific GO term."
  },
  "case_id": "GO_biological_process_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO2",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The sequence matches MCR-2, whose reported activity is adding phosphoethanolamine to lipid A. That is distinct from synthesizing the LPS core region. The B annotation exists, but it is computationally assigned (IEA:TreeGrafter) and does not outweigh the more specific functional evidence for the different process."
  },
  "important_caveats": [
    "The B GO assignment applies to the sequence but is computationally inferred, not presented as experimental evidence.",
    "The reported functional annotation says MCR-2 probably catalyzes lipid A modification; it does not establish that the protein has no other biological effects."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices do not include lipid A modification, the reported activity. B is the only LPS-related option, but its specific reference to core-region biosynthesis does not describe that activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0129",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence matches MCR-2, whose reported activity is adding phosphoethanolamine to lipid A. That is distinct from synthesizing the LPS core region. The B annotation exists, but it is computationally assigned (IEA:TreeGrafter) and does not outweigh the more specific functional evidence for the different process.",
    "evidence_ids": ["C4", "C5", "C6", "GO2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments and a large enzymatic region, but those features do not identify its substrate or distinguish the listed biosynthetic pathways with confidence.",
    "missing_item_specific_fact": "The protein-specific activity—that MCR-2 modifies lipid A by transferring phosphoethanolamine—and its database GO annotation are not supplied in the question.",
    "reason": "Choosing among these processes requires knowing the particular protein's function or annotation; exact-sequence recognition or a generic membrane-protein heuristic would not provide a biological argument for the specific GO term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices do not include lipid A modification, the reported activity. B is the only LPS-related option, but its specific reference to core-region biosynthesis does not describe that activity."
  },
  "important_caveats": [
    "The B GO assignment applies to the sequence but is computationally inferred, not presented as experimental evidence.",
    "The reported functional annotation says MCR-2 probably catalyzes lipid A modification; it does not establish that the protein has no other biological effects."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1C3NEV1 (MCR-2, Phosphatidylethanolamine transferase) carries GO:0009244 (lipopolysaccharide core region biosynthetic process) as an annotation (C6, H4). The protein's experimentally characterized function (PubMed:30194678, PDB:6A7W) is phosphoethanolamine transfer to lipid A, which is part of LPS modification. However, the GO annotation is IEA:TreeGrafter (automated/computational), and the term 'core region biosynthetic process' specifically refers to the ten-saccharide oligosaccharide core (GO2), whereas MCR-2 modifies lipid A rather than the core region. The annotation is present in the database and matches the expected answer, but it is an approximate automated assignment rather than a precise functional description.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a ~538-residue protein with multiple N-terminal transmembrane helices and a cytoplasmic/periplasmic catalytic domain, consistent with a membrane-associated transferase from a Gram-negative bacterium (E. coli). Among the four options: (C) meiotic DNA integrity checkpoint signaling is exclusively eukaryotic and irrelevant to a bacterial protein; (D) cell adhesion does not match a membrane transferase; (A) carotenoid biosynthetic process involves tetraterpenoid pathway enzymes with entirely different domain architecture. Option (B) is the only LPS/lipid-metabolism-related process, and recognizing the protein as a lipid-modifying membrane enzyme in E. coli (a LPS-containing organism) provides a defensible biological argument for selecting B over the clearly inappropriate distractors.


**Missing item-specific fact**

> Precise identification of the protein as a phosphatidylethanolamine transferase modifying lipid A (rather than, say, a general lipid kinase or acyltransferase) requires either domain-level recognition of the PptA/MCR fold or database lookup. The specific sub-process 'core region biosynthetic process' (as opposed to 'lipid A biosynthetic process') is an imprecise automated annotation assignment not derivable from sequence reasoning alone.


**Reason**

> While the exact GO term 'lipopolysaccharide core region biosynthetic process' is an automated (IEA:TreeGrafter) annotation that slightly mischaracterizes the lipid A modification function, the question's four options are sufficiently distinct that general biological reasoning—bacterial origin, membrane topology, transferase architecture, and elimination of eukaryotic-only or unrelated processes—can meaningfully narrow the answer to B without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (carotenoid biosynthesis, meiotic checkpoint signaling, cell adhesion) are clearly incompatible with a bacterial membrane transferase. No other option is defensible for this protein.


### Important caveats

- The GO:0009244 annotation is IEA:TreeGrafter (automated), not experimentally derived. The protein's experimentally validated function is phosphoethanolamine transfer to lipid A (EC 2.7.8.43), which is more precisely 'lipid A modification' than 'core region biosynthetic process.'
- The GO term definition specifies the ten-saccharide core oligosaccharide, which is distinct from lipid A. The automated annotation appears to place lipid A modification under the broader LPS biosynthesis umbrella via TreeGrafter inference.
- The protein is a plasmid-encoded polymyxin/colistin resistance factor (MCR-2), not a constitutive LPS biosynthetic enzyme, which adds contextual nuance to the 'biosynthetic process' framing.
- All reviewer evidence is from UniProt entry A0A1C3NEV1, which was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown but sequence matches confirmed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a ~538-residue protein with multiple N-terminal transmembrane helices and a cytoplasmic/periplasmic catalytic domain, consistent with a membrane-associated transferase from a Gram-negative bacterium (E. coli). Among the four options: (C) meiotic DNA integrity checkpoint signaling is exclusively eukaryotic and irrelevant to a bacterial protein; (D) cell adhesion does not match a membrane transferase; (A) carotenoid biosynthetic process involves tetraterpenoid pathway enzymes with entirely different domain architecture. Option (B) is the only LPS/lipid-metabolism-related process, and recognizing the protein as a lipid-modifying membrane enzyme in E. coli (a LPS-containing organism) provides a defensible biological argument for selecting B over the clearly inappropriate distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the protein as a phosphatidylethanolamine transferase modifying lipid A (rather than, say, a general lipid kinase or acyltransferase) requires either domain-level recognition of the PptA/MCR fold or database lookup. The specific sub-process 'core region biosynthetic process' (as opposed to 'lipid A biosynthetic process') is an imprecise automated annotation assignment not derivable from sequence reasoning alone.",
    "reason": "While the exact GO term 'lipopolysaccharide core region biosynthetic process' is an automated (IEA:TreeGrafter) annotation that slightly mischaracterizes the lipid A modification function, the question's four options are sufficiently distinct that general biological reasoning—bacterial origin, membrane topology, transferase architecture, and elimination of eukaryotic-only or unrelated processes—can meaningfully narrow the answer to B without memorizing this specific protein's database entry."
  },
  "case_id": "GO_biological_process_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, Phosphatidylethanolamine transferase) carries GO:0009244 (lipopolysaccharide core region biosynthetic process) as an annotation (C6, H4). The protein's experimentally characterized function (PubMed:30194678, PDB:6A7W) is phosphoethanolamine transfer to lipid A, which is part of LPS modification. However, the GO annotation is IEA:TreeGrafter (automated/computational), and the term 'core region biosynthetic process' specifically refers to the ten-saccharide oligosaccharide core (GO2), whereas MCR-2 modifies lipid A rather than the core region. The annotation is present in the database and matches the expected answer, but it is an approximate automated assignment rather than a precise functional description."
  },
  "important_caveats": [
    "The GO:0009244 annotation is IEA:TreeGrafter (automated), not experimentally derived. The protein's experimentally validated function is phosphoethanolamine transfer to lipid A (EC 2.7.8.43), which is more precisely 'lipid A modification' than 'core region biosynthetic process.'",
    "The GO term definition specifies the ten-saccharide core oligosaccharide, which is distinct from lipid A. The automated annotation appears to place lipid A modification under the broader LPS biosynthesis umbrella via TreeGrafter inference.",
    "The protein is a plasmid-encoded polymyxin/colistin resistance factor (MCR-2), not a constitutive LPS biosynthetic enzyme, which adds contextual nuance to the 'biosynthetic process' framing.",
    "All reviewer evidence is from UniProt entry A0A1C3NEV1, which was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown but sequence matches confirmed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (carotenoid biosynthesis, meiotic checkpoint signaling, cell adhesion) are clearly incompatible with a bacterial membrane transferase. No other option is defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, Phosphatidylethanolamine transferase) carries GO:0009244 (lipopolysaccharide core region biosynthetic process) as an annotation (C6, H4). The protein's experimentally characterized function (PubMed:30194678, PDB:6A7W) is phosphoethanolamine transfer to lipid A, which is part of LPS modification. However, the GO annotation is IEA:TreeGrafter (automated/computational), and the term 'core region biosynthetic process' specifically refers to the ten-saccharide oligosaccharide core (GO2), whereas MCR-2 modifies lipid A rather than the core region. The annotation is present in the database and matches the expected answer, but it is an approximate automated assignment rather than a precise functional description.",
    "evidence_ids": ["C6", "H4", "C5", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a ~538-residue protein with multiple N-terminal transmembrane helices and a cytoplasmic/periplasmic catalytic domain, consistent with a membrane-associated transferase from a Gram-negative bacterium (E. coli). Among the four options: (C) meiotic DNA integrity checkpoint signaling is exclusively eukaryotic and irrelevant to a bacterial protein; (D) cell adhesion does not match a membrane transferase; (A) carotenoid biosynthetic process involves tetraterpenoid pathway enzymes with entirely different domain architecture. Option (B) is the only LPS/lipid-metabolism-related process, and recognizing the protein as a lipid-modifying membrane enzyme in E. coli (a LPS-containing organism) provides a defensible biological argument for selecting B over the clearly inappropriate distractors.",
    "missing_item_specific_fact": "Precise identification of the protein as a phosphatidylethanolamine transferase modifying lipid A (rather than, say, a general lipid kinase or acyltransferase) requires either domain-level recognition of the PptA/MCR fold or database lookup. The specific sub-process 'core region biosynthetic process' (as opposed to 'lipid A biosynthetic process') is an imprecise automated annotation assignment not derivable from sequence reasoning alone.",
    "reason": "While the exact GO term 'lipopolysaccharide core region biosynthetic process' is an automated (IEA:TreeGrafter) annotation that slightly mischaracterizes the lipid A modification function, the question's four options are sufficiently distinct that general biological reasoning—bacterial origin, membrane topology, transferase architecture, and elimination of eukaryotic-only or unrelated processes—can meaningfully narrow the answer to B without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (carotenoid biosynthesis, meiotic checkpoint signaling, cell adhesion) are clearly incompatible with a bacterial membrane transferase. No other option is defensible for this protein."
  },
  "important_caveats": [
    "The GO:0009244 annotation is IEA:TreeGrafter (automated), not experimentally derived. The protein's experimentally validated function is phosphoethanolamine transfer to lipid A (EC 2.7.8.43), which is more precisely 'lipid A modification' than 'core region biosynthetic process.'",
    "The GO term definition specifies the ten-saccharide core oligosaccharide, which is distinct from lipid A. The automated annotation appears to place lipid A modification under the broader LPS biosynthesis umbrella via TreeGrafter inference.",
    "The protein is a plasmid-encoded polymyxin/colistin resistance factor (MCR-2), not a constitutive LPS biosynthetic enzyme, which adds contextual nuance to the 'biosynthetic process' framing.",
    "All reviewer evidence is from UniProt entry A0A1C3NEV1, which was first publicly released 2025-06-18; the benchmark author's source snapshot is unknown but sequence matches confirmed."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_annotations_require_qualification`.

> C5/H3 say probably lipid-A phosphoethanolamine addition, while C6/H4 explicitly carry the keyed LPS-core biosynthesis term with IEA:TreeGrafter. GO2 defines core-region synthesis.

**Remaining uncertainty:** Retain both annotations and the word probably; neither the existence nor the lower evidence class of a GO label alone resolves biological validity or exclusivity.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2), [H3](#evidence-h3), [H4](#evidence-h4).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"}],"value":"Polymyxin resistance protein MCR-2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30194678","source":"PubMed"}],"value":"2.7.8.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30194678","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"Ref.1","source":"Reference"}],"value":"Phosphatidylethanolamine transferase Mcr-2"}}}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0R6L508","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"30194678","source":"PubMed"}],"value":"Probably catalyzes the addition of a phosphoethanolamine moiety to lipid A (PubMed:30194678). Phosphoethanolamine modification of lipid A confers polymyxin resistance (By similarity). Confers resistance to polymyxin-type antibiotics such as colistin (PubMed:30194678)"}]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"database":"GO","id":"GO:0009244","properties":[{"key":"GoTerm","value":"P:lipopolysaccharide core region biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 66-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
CC   -!- FUNCTION: Probably catalyzes the addition of a phosphoethanolamine
CC       moiety to lipid A (PubMed:30194678). Phosphoethanolamine modification
CC       of lipid A confers polymyxin resistance (By similarity). Confers
CC       resistance to polymyxin-type antibiotics such as colistin
CC       (PubMed:30194678). {ECO:0000250|UniProtKB:A0A0R6L508,
CC       ECO:0000269|PubMed:30194678}.
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 108-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
DR   GO; GO:0009244; P:lipopolysaccharide core region biosynthetic process; IEA:TreeGrafter.
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 94389-94401`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009244
name: lipopolysaccharide core region biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of the core region of bacterial lipopolysaccharides, which contains ten saccharide residues." [ISBN:0198506732]
synonym: "lipopolysaccharide core region anabolism" EXACT []
synonym: "lipopolysaccharide core region biosynthesis" EXACT []
synonym: "lipopolysaccharide core region formation" EXACT []
synonym: "lipopolysaccharide core region synthesis" EXACT []
synonym: "LPS core region biosynthetic process" EXACT []
is_a: GO:0009312 ! oligosaccharide biosynthetic process
relationship: part_of GO:0009103 ! lipopolysaccharide biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
