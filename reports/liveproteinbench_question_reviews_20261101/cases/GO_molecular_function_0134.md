# GO_molecular_function_0134

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNQFNKVCVIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVVNDGYLKATTLPEEADAFIIAVPTPFKGDNHEPNLDYIEMASKAIAKVLKKGNLVILESTSPVGTTEQMAKWLAEERSDLSFPHQCGEVSDIKIAHCPERVLPGQVIRELVENDRIIGGMTQKCAEYAIRLYKIFVQGECIMTNARTAEMTKLTENSFRDLNIAFANELSILCDKLDINVWELIKLANRHPRVNILQPGCGVGGHCIAVDPWFIVYQNPNEAKIIKTAREVNDNKPNFVVQKIKKKIKDILGPKIACLGLAFKPDIDDLRESPALDIVIKLASENASQILVVEPNIKQLPLKLQNKRNIKLVCLSQALDEADVVAVLVRHKEFIEVQSDKVVSFC

[Multiple Choices]
A. calcium ion binding
B. oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
C. adenylyltransferase activity
D. double-stranded DNA binding
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

### Expected-answer support: contradicted

> The sequence-matched entry reports an experimentally evidenced NAD-dependent oxidation of UDP-ManNAc to UDP-ManNAcA (EC 1.1.1.336). That chemistry oxidizes an alcohol group, whereas option B specifically requires a CH-CH group donor. The entry's IEA:InterPro annotation of B is computational and does not override the mismatch with the reported reaction.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO3](#evidence-go3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A dinucleotide-binding/dehydrogenase-like sequence may favor an oxidoreductase over DNA binding or adenylyltransferase, but that does not establish the specific donor group required by option B.


**Missing item-specific fact**

> The protein's substrate and reaction chemistry—specifically, which group on UDP-ManNAc is oxidized—are not supplied in the question.


**Reason**

> Distinguishing the precise GO term requires protein-specific functional information, not merely broad sequence-based recognition of a likely oxidoreductase. In fact, the retrieved experimental reaction does not match B's stated CH-CH donor specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence does not support A, C, or D, and the reported reaction contradicts the defining donor-group specificity of B. Thus no listed option is supported as the precise molecular function by the experimental reaction.


### Important caveats

- The sequence exactly matches the current and historical UniProt sequence for the identified protein.
- The experimental function and reaction are cited in UniProt with ECO:0000269 evidence, but the primary paper was not independently reviewed here.
- The B annotation is IEA:InterPro; it is evidence of a database annotation, not experimental validation of that precise GO activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A dinucleotide-binding/dehydrogenase-like sequence may favor an oxidoreductase over DNA binding or adenylyltransferase, but that does not establish the specific donor group required by option B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate and reaction chemistry—specifically, which group on UDP-ManNAc is oxidized—are not supplied in the question.",
    "reason": "Distinguishing the precise GO term requires protein-specific functional information, not merely broad sequence-based recognition of a likely oxidoreductase. In fact, the retrieved experimental reaction does not match B's stated CH-CH donor specificity."
  },
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "GO3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched entry reports an experimentally evidenced NAD-dependent oxidation of UDP-ManNAc to UDP-ManNAcA (EC 1.1.1.336). That chemistry oxidizes an alcohol group, whereas option B specifically requires a CH-CH group donor. The entry's IEA:InterPro annotation of B is computational and does not override the mismatch with the reported reaction."
  },
  "important_caveats": [
    "The sequence exactly matches the current and historical UniProt sequence for the identified protein.",
    "The experimental function and reaction are cited in UniProt with ECO:0000269 evidence, but the primary paper was not independently reviewed here.",
    "The B annotation is IEA:InterPro; it is evidence of a database annotation, not experimental validation of that precise GO activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence does not support A, C, or D, and the reported reaction contradicts the defining donor-group specificity of B. Thus no listed option is supported as the precise molecular function by the experimental reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched entry reports an experimentally evidenced NAD-dependent oxidation of UDP-ManNAc to UDP-ManNAcA (EC 1.1.1.336). That chemistry oxidizes an alcohol group, whereas option B specifically requires a CH-CH group donor. The entry's IEA:InterPro annotation of B is computational and does not override the mismatch with the reported reaction.",
    "evidence_ids": ["C5", "C6", "C8", "GO3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A dinucleotide-binding/dehydrogenase-like sequence may favor an oxidoreductase over DNA binding or adenylyltransferase, but that does not establish the specific donor group required by option B.",
    "missing_item_specific_fact": "The protein's substrate and reaction chemistry—specifically, which group on UDP-ManNAc is oxidized—are not supplied in the question.",
    "reason": "Distinguishing the precise GO term requires protein-specific functional information, not merely broad sequence-based recognition of a likely oxidoreductase. In fact, the retrieved experimental reaction does not match B's stated CH-CH donor specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence does not support A, C, or D, and the reported reaction contradicts the defining donor-group specificity of B. Thus no listed option is supported as the precise molecular function by the experimental reaction."
  },
  "important_caveats": [
    "The sequence exactly matches the current and historical UniProt sequence for the identified protein.",
    "The experimental function and reaction are cited in UniProt with ECO:0000269 evidence, but the primary paper was not independently reviewed here.",
    "The B annotation is IEA:InterPro; it is evidence of a database annotation, not experimental validation of that precise GO activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3AB61 (sequence matched) carries GO:0016628 ('oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor') as an IEA:InterPro annotation (evidence C8, H6). The protein is experimentally characterized (ECO:0000269, PubMed:38382015) as a NAD+-dependent dehydrogenase (EC 1.1.1.336) catalyzing UDP-ManNAc → UDP-ManNAcA. The broad category 'oxidoreductase activity…NAD or NADP as acceptor' is correct. However, the 'CH-CH group' qualifier (EC 1.3.1.-) is imprecise for this enzyme, which acts on a CH-OH group (EC 1.1.1.-); the more accurate GO term would be GO:0016616 or the specific GO:0089714. Nonetheless, the annotation IS present in the database and the protein IS an NAD-dependent oxidoreductase, so the expected answer is supported by the annotation evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'VIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVV' displays a glycine-rich motif and hydrophobic β-strand architecture characteristic of a Rossmann-fold NAD(P)-binding domain found in dehydrogenases. The overall 407-residue α/β architecture, presence of catalytic residues (e.g., 'GCGVGGHC' region), and absence of EF-hand calcium-binding loops, helix-turn-helix/zinc-finger DNA-binding motifs, or nucleotidyltransferase PPase motifs allow elimination of options A (calcium binding), C (adenylyltransferase), and D (dsDNA binding). Among the four choices, B is the only oxidoreductase option, and the Rossmann-fold-like NAD-binding signature supports this broad category.


**Missing item-specific fact**

> The precise 'CH-CH group' vs 'CH-OH group' distinction cannot be determined from sequence alone; this requires knowledge of the specific substrate (UDP-ManNAc C6 hydroxyl). However, since B is the sole oxidoreductase among the four choices, the question effectively tests broad functional class identification, which the sequence supports.


**Reason**

> The four options span radically different molecular function classes (ion binding, oxidoreductase, transferase, DNA binding). The sequence's Rossmann-fold-like NAD-binding region and dehydrogenase-typical catalytic architecture provide a concrete biological argument for selecting the oxidoreductase option over the three non-oxidoreductase distractors. The imprecision in 'CH-CH' vs 'CH-OH' does not affect the ability to choose B over A, C, or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mutually exclusive functional classes. The sequence clearly supports a dehydrogenase/oxidoreductase assignment and lacks any features of calcium-binding proteins, nucleotidyltransferases, or DNA-binding domains. No other option is defensible.


### Important caveats

- The GO:0016628 annotation carries only IEA:InterPro evidence (automated), not experimental evidence. The experimentally supported GO term is GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity, ECO:0000269).
- The 'CH-CH group' qualifier in GO:0016628 (cross-referenced to EC 1.3.1.-) is technically imprecise for EC 1.1.1.336, which acts on a CH-OH group. The more appropriate broad GO term would be GO:0016616 (CH-OH group). The annotation's presence in UniProt supports the key but the underlying classification is debatable.
- The sequence resembles a medium-chain dehydrogenase/reductase (MDR) or SDR-family protein; recognition of this family from sequence provides reasoning support for the oxidoreductase category but not for the specific 'CH-CH' sub-classification.
- All reviewer evidence is database annotation; the evaluated model had access only to the raw sequence and four GO term labels.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'VIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVV' displays a glycine-rich motif and hydrophobic β-strand architecture characteristic of a Rossmann-fold NAD(P)-binding domain found in dehydrogenases. The overall 407-residue α/β architecture, presence of catalytic residues (e.g., 'GCGVGGHC' region), and absence of EF-hand calcium-binding loops, helix-turn-helix/zinc-finger DNA-binding motifs, or nucleotidyltransferase PPase motifs allow elimination of options A (calcium binding), C (adenylyltransferase), and D (dsDNA binding). Among the four choices, B is the only oxidoreductase option, and the Rossmann-fold-like NAD-binding signature supports this broad category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise 'CH-CH group' vs 'CH-OH group' distinction cannot be determined from sequence alone; this requires knowledge of the specific substrate (UDP-ManNAc C6 hydroxyl). However, since B is the sole oxidoreductase among the four choices, the question effectively tests broad functional class identification, which the sequence supports.",
    "reason": "The four options span radically different molecular function classes (ion binding, oxidoreductase, transferase, DNA binding). The sequence's Rossmann-fold-like NAD-binding region and dehydrogenase-typical catalytic architecture provide a concrete biological argument for selecting the oxidoreductase option over the three non-oxidoreductase distractors. The imprecision in 'CH-CH' vs 'CH-OH' does not affect the ability to choose B over A, C, or D."
  },
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C9",
      "H3",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3AB61 (sequence matched) carries GO:0016628 ('oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor') as an IEA:InterPro annotation (evidence C8, H6). The protein is experimentally characterized (ECO:0000269, PubMed:38382015) as a NAD+-dependent dehydrogenase (EC 1.1.1.336) catalyzing UDP-ManNAc → UDP-ManNAcA. The broad category 'oxidoreductase activity…NAD or NADP as acceptor' is correct. However, the 'CH-CH group' qualifier (EC 1.3.1.-) is imprecise for this enzyme, which acts on a CH-OH group (EC 1.1.1.-); the more accurate GO term would be GO:0016616 or the specific GO:0089714. Nonetheless, the annotation IS present in the database and the protein IS an NAD-dependent oxidoreductase, so the expected answer is supported by the annotation evidence."
  },
  "important_caveats": [
    "The GO:0016628 annotation carries only IEA:InterPro evidence (automated), not experimental evidence. The experimentally supported GO term is GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity, ECO:0000269).",
    "The 'CH-CH group' qualifier in GO:0016628 (cross-referenced to EC 1.3.1.-) is technically imprecise for EC 1.1.1.336, which acts on a CH-OH group. The more appropriate broad GO term would be GO:0016616 (CH-OH group). The annotation's presence in UniProt supports the key but the underlying classification is debatable.",
    "The sequence resembles a medium-chain dehydrogenase/reductase (MDR) or SDR-family protein; recognition of this family from sequence provides reasoning support for the oxidoreductase category but not for the specific 'CH-CH' sub-classification.",
    "All reviewer evidence is database annotation; the evaluated model had access only to the raw sequence and four GO term labels."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive functional classes. The sequence clearly supports a dehydrogenase/oxidoreductase assignment and lacks any features of calcium-binding proteins, nucleotidyltransferases, or DNA-binding domains. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3AB61 (sequence matched) carries GO:0016628 ('oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor') as an IEA:InterPro annotation (evidence C8, H6). The protein is experimentally characterized (ECO:0000269, PubMed:38382015) as a NAD+-dependent dehydrogenase (EC 1.1.1.336) catalyzing UDP-ManNAc → UDP-ManNAcA. The broad category 'oxidoreductase activity…NAD or NADP as acceptor' is correct. However, the 'CH-CH group' qualifier (EC 1.3.1.-) is imprecise for this enzyme, which acts on a CH-OH group (EC 1.1.1.-); the more accurate GO term would be GO:0016616 or the specific GO:0089714. Nonetheless, the annotation IS present in the database and the protein IS an NAD-dependent oxidoreductase, so the expected answer is supported by the annotation evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C9", "H3", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'VIGLGYIGLPTAAIFASRKIKVIGVDINQNIVDIINKGKIHIVEPGLDILVHMVV' displays a glycine-rich motif and hydrophobic β-strand architecture characteristic of a Rossmann-fold NAD(P)-binding domain found in dehydrogenases. The overall 407-residue α/β architecture, presence of catalytic residues (e.g., 'GCGVGGHC' region), and absence of EF-hand calcium-binding loops, helix-turn-helix/zinc-finger DNA-binding motifs, or nucleotidyltransferase PPase motifs allow elimination of options A (calcium binding), C (adenylyltransferase), and D (dsDNA binding). Among the four choices, B is the only oxidoreductase option, and the Rossmann-fold-like NAD-binding signature supports this broad category.",
    "missing_item_specific_fact": "The precise 'CH-CH group' vs 'CH-OH group' distinction cannot be determined from sequence alone; this requires knowledge of the specific substrate (UDP-ManNAc C6 hydroxyl). However, since B is the sole oxidoreductase among the four choices, the question effectively tests broad functional class identification, which the sequence supports.",
    "reason": "The four options span radically different molecular function classes (ion binding, oxidoreductase, transferase, DNA binding). The sequence's Rossmann-fold-like NAD-binding region and dehydrogenase-typical catalytic architecture provide a concrete biological argument for selecting the oxidoreductase option over the three non-oxidoreductase distractors. The imprecision in 'CH-CH' vs 'CH-OH' does not affect the ability to choose B over A, C, or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive functional classes. The sequence clearly supports a dehydrogenase/oxidoreductase assignment and lacks any features of calcium-binding proteins, nucleotidyltransferases, or DNA-binding domains. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0016628 annotation carries only IEA:InterPro evidence (automated), not experimental evidence. The experimentally supported GO term is GO:0089714 (UDP-N-acetyl-D-mannosamine dehydrogenase activity, ECO:0000269).",
    "The 'CH-CH group' qualifier in GO:0016628 (cross-referenced to EC 1.3.1.-) is technically imprecise for EC 1.1.1.336, which acts on a CH-OH group. The more appropriate broad GO term would be GO:0016616 (CH-OH group). The annotation's presence in UniProt supports the key but the underlying classification is debatable.",
    "The sequence resembles a medium-chain dehydrogenase/reductase (MDR) or SDR-family protein; recognition of this family from sequence provides reasoning support for the oxidoreductase category but not for the specific 'CH-CH' sub-classification.",
    "All reviewer evidence is database annotation; the evaluated model had access only to the raw sequence and four GO term labels."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C5/C6/H4 give EC1.1.1.336, UDP-ManNAc to uronate; GO3 defines the keyed CH-CH donor class as EC1.3.1.-, while C8/H6 assign it computationally.

**Remaining uncertainty:** The source-level reaction/class mismatch is traced; this does not independently assay every alternative donor chemistry.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO3](#evidence-go3), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A0U3AB61` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"UDP-ManNAc 6-dehydrogenase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"1.1.1.336"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-mannosamine dehydrogenase"}}}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"Dehydrogenase involved in the biosynthesis of capsular polysaccharides (PubMed:38382015). Catalyzes the NAD(+)-dependent oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc) to UDP-N-acetyl-D-mannosaminuronic acid (UDP-ManNAcA) (PubMed:38382015)"}]}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:25781"}}],"reaction":{"ecNumber":"1.1.1.336","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:25780"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:68623"},{"database":"ChEBI","id":"CHEBI:70731"}]}}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"database":"GO","id":"GO:0016628","properties":[{"key":"GoTerm","value":"F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3AB61.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.671066+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"id":"GO:0089714","properties":[{"key":"GoTerm","value":"F:UDP-N-acetyl-D-mannosamine dehydrogenase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `1ba44594297295985c473e4d8cdbee4c2c9ce9c395356065e2919dc560c56211`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 38-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
CC   -!- FUNCTION: Dehydrogenase involved in the biosynthesis of capsular
CC       polysaccharides (PubMed:38382015). Catalyzes the NAD(+)-dependent
CC       oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc) to UDP-N-acetyl-D-
CC       mannosaminuronic acid (UDP-ManNAcA) (PubMed:38382015).
CC       {ECO:0000269|PubMed:38382015}.
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 43-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-mannosamine + 2 NAD(+) + H2O = UDP-N-
CC         acetyl-alpha-D-mannosaminouronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:25780, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:68623,
CC         ChEBI:CHEBI:70731; EC=1.1.1.336;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:25781;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
DR   GO; GO:0016628; F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor; IEA:InterPro.
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3AB61?format=txt&versions=20)  
**Locator:** `lines 70-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-01T06:27:21.162556+00:00.  

```text
DR   GO; GO:0089714; F:UDP-N-acetyl-D-mannosamine dehydrogenase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `d19839216cf02dcf1b522686093bf66cffa8fdfff2eda11221074180623cea5a`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 128398-128409`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016628
name: oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
namespace: molecular_function
def: "Catalysis of an oxidation-reduction (redox) reaction in which a CH-CH group acts as a hydrogen or electron donor and reduces NAD or NADP." [EC:1.3.1.-]
xref: EC:1.3.1.-
xref: Reactome:R-HSA-4755572 "Defective SRD5A3 does not reduce pPNOL to DCHOL"
xref: Reactome:R-HSA-9661726 "An unknown reductase reduces D-UBGN to STBN"
xref: Reactome:R-HSA-9661745 "An unknown BILR reduces BIL to D-UBGN"
is_a: GO:0016627 ! oxidoreductase activity, acting on the CH-CH group of donors
property_value: skos:exactMatch EC:1.3.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
