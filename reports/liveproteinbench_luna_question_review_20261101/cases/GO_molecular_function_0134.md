# GO_molecular_function_0134

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| contradicted | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: contradicted

> The sequence-matched entry reports an experimentally evidenced NAD-dependent oxidation of UDP-ManNAc to UDP-ManNAcA (EC 1.1.1.336). That chemistry oxidizes an alcohol group, whereas option B specifically requires a CH-CH group donor. The entry's IEA:InterPro annotation of B is computational and does not override the mismatch with the reported reaction.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO3](#evidence-go3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A dinucleotide-binding/dehydrogenase-like sequence may favor an oxidoreductase over DNA binding or adenylyltransferase, but that does not establish the specific donor group required by option B.

**Missing item-specific fact**

> The protein's substrate and reaction chemistry—specifically, which group on UDP-ManNAc is oxidized—are not supplied in the question.

**Reason**

> Distinguishing the precise GO term requires protein-specific functional information, not merely broad sequence-based recognition of a likely oxidoreductase. In fact, the retrieved experimental reaction does not match B's stated CH-CH donor specificity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The evidence does not support A, C, or D, and the reported reaction contradicts the defining donor-group specificity of B. Thus no listed option is supported as the precise molecular function by the experimental reaction.

### Important caveats

- The sequence exactly matches the current and historical UniProt sequence for the identified protein.
- The experimental function and reaction are cited in UniProt with ECO:0000269 evidence, but the primary paper was not independently reviewed here.
- The B annotation is IEA:InterPro; it is evidence of a database annotation, not experimental validation of that precise GO activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0134",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched entry reports an experimentally evidenced NAD-dependent oxidation of UDP-ManNAc to UDP-ManNAcA (EC 1.1.1.336). That chemistry oxidizes an alcohol group, whereas option B specifically requires a CH-CH group donor. The entry's IEA:InterPro annotation of B is computational and does not override the mismatch with the reported reaction.",
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "GO3",
      "H4",
      "H6"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C5/C6/H4 give EC1.1.1.336, UDP-ManNAc to uronate; GO3 defines the keyed CH-CH donor class as EC1.3.1.-, while C8/H6 assign it computationally.

**Remaining uncertainty:** The source-level reaction/class mismatch is traced; this does not independently assay every alternative donor chemistry.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [GO3](#evidence-go3), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A0U3AB61`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 20. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 134). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
