# GO_molecular_function_0153

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — ligase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDLTTTSHARVDSGGVPFTSSLNDPTPPKLSASIALPAHLHLLAKAYGIPESHILQLAWALAANEQNARTAQWEHLELDERQAISWVLRHWQDPSVHRYLSPDELRGDKHQIPATVMAVVEEYSLFQTLALTGSETEIGMCFHPSTEQPWLRVIWNPEGMLASSASRLTRALESALHAVFLTPHVKVGDLTLFSIWDHQQILQWNSHYPQATDRLVHELFKDVVDASPQANAVAAWDGELTYRELDRLSSRLSGRLQDEFGVQPETIVVLCFEKSVWAIVAMLAVVKAGGAFLHVDPQHPAVRHQAMVQTTAAKLVLCSARTRSIISASVPECTSLVIDRRAFSVEPDHVQHETLLSSQNLSPRNAAYVVCTSGSTGTPKAIVVEHASLSTSVDAQANAMEISSGSRVLQYAAYTFDVSVGDIFTALTHGACICIPSDWERSHDLAGAINRLNVNQACLTSTVASILSPAEVPGLEKLTLGGEPATRQCVDAWAEQVRLKNVYGPAECTVWCMIQPEVSRHISVSNIGHGIGARAWIVHPEDHDRLMPVGAVGELLIEGPLVARGYLNDSTRTDEVFLSQPPRWLESFGPTPSRSRFYKTGDLARYGPAGALLFEGRKDTQIKLRGQRIELSEIEYRLHRALSDQVATAVELAHPKGSTAPVLAAFITWDQGIDLQNVQNVTLDARQEFEELASRIKAEIEQALPSYMVPALFIPVQTLPLTTSGKLDRKSLRHFCSQCSHEFLKKLDDSSPADAAPKESANPAEENLARLWAQVLERKSESIRRGDNFLSLGGDSLAAMRLVNLAARDLRLTLTVADVFNSPILADQANLLRPLVQTKHIAPFELVTDGDLPIQDLMDSVAKQCGLTSDQVEDVYPCTPYQEEMVRDSLSGTRTQMGQEVIQLASDLDLSRYLSACARVFQRCPILRTRFVEISGKLLQVVIREDISWQRPTSLAAYIEADNQTPPTLGKPLARWALTEDSTHLVLTMHHAIFDGISLGQIFGAIYAVYQSIPLPQVNLTFATFIGKIYRPHHDLPDASKQFWRSYLSPTAGSNDAPLSDVERASRPCANSGTQRLVTFQAGAVKALQQHGLTEATLARAAWACTLARGRQSPDSDVIFGTILTGRNIHLPGVDALAAPALAHTPIRVRMAAAQQEKPAHFLARVQADATAMIPFEHDGMDRIRALDEQVRVACDNMRTLLVIQPIPEGLILDSKSPFPGTMLSGPRVEAREMRHFHWYGLLMECTLLPMDGFFVRMSFDDTLYSPEAAERLLDEYSQTLHELAHGLTVDGSTE

[Multiple Choices]
A. peptidyl-lysine 3-dioxygenase activity
B. nutrient reservoir activity
C. ligase activity
D. transferase activity, transferring alkyl or aryl (other than methyl) groups
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

### Expected-answer support: supported

> The sequence-matched UniProt record identifies the protein as an NRPS-like ligase, and its annotated catalytic reaction joins restrictinol and glycine to form restricticin. The GO ligase annotation is computationally assigned (IEA:UniProtKB-KW), while the function and catalytic activity are linked to a cited publication.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has NRPS-like catalytic architecture, including adenylation-domain-like features and a carrier-domain-like region. Such enzymes activate and join substrates, supporting ligase activity over the unrelated dioxygenase, nutrient-reservoir, and alkyl/aryl-transferase choices.

**Missing item-specific fact**

> No protein-specific database fact is required to distinguish these broad choices, although identifying the precise substrate reaction would require additional information.

**Reason**

> The sequence provides a defensible basis for recognizing an NRPS-like enzyme and inferring ligase activity; this is more than recognizing a stored accession or relying on a generic predictor.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, ligase activity best fits the NRPS-like sequence and the documented substrate-joining reaction.

### Important caveats

- The GO ligase annotation itself is an electronic inference, not an experimental-evidence GO assignment.
- The cited function and catalytic-activity annotations support the key, but the detailed pathway description includes statements qualified as being by similarity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as an NRPS-like ligase, and its annotated catalytic reaction joins restrictinol and glycine to form restricticin. The GO ligase annotation is computationally assigned (IEA:UniProtKB-KW), while the function and catalytic activity are linked to a cited publication.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has NRPS-like catalytic architecture, including adenylation-domain-like features and a carrier-domain-like region. Such enzymes activate and join substrates, supporting ligase activity over the unrelated dioxygenase, nutrient-reservoir, and alkyl/aryl-transferase choices.",
    "missing_item_specific_fact": "No protein-specific database fact is required to distinguish these broad choices, although identifying the precise substrate reaction would require additional information.",
    "reason": "The sequence provides a defensible basis for recognizing an NRPS-like enzyme and inferring ligase activity; this is more than recognizing a stored accession or relying on a generic predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, ligase activity best fits the NRPS-like sequence and the documented substrate-joining reaction."
  },
  "important_caveats": [
    "The GO ligase annotation itself is an electronic inference, not an experimental-evidence GO assignment.",
    "The cited function and catalytic-activity annotations support the key, but the detailed pathway description includes statements qualified as being by similarity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DXV3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 4. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
"P0DXV3"
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Nonribosomal peptide synthetase resC"}}}
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0L1JF11","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39105744","source":"PubMed"}],"value":"Nonribosomal peptide synthetase; part of the gene cluster that mediates the biosynthesis of the tetrahydropyranyl antifungal agent restricticin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:39105744). Within the pathway, resC catalyzes the C3 esterification of restrictinol with glycine to yield restricticin. ResC represents an example of the emerging class of single-module NRPS-like enzymes that perform esterification reactions (By similarity). The highly reducing polyketide synthase resH, the short chain dehydrogenase resG, the cyclase resF, the FAD-dependent monooxygenase resA and the enoylreductase resD are required to generate the first stable intermediate desmethylrestrictinol. ResH with resD biosynthesize the first polyketide chain intermediate that is reduced by resG, followed by epoxidation by resA before 6-endo cyclization via epoxide opening by resF leads to desmethylrestrictinol. The methyltransferase resE then catalyzes the C4 O-methylation of desmethylrestrictinol to produce restrictinol, and the nonribosomal peptide synthetase resC catalyzes the C3 esterification of restrictinol with glycine that leads to restricticin (By similarity)"}]}
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:45.732991+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81536"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"name":"restrictinol + glycine + H(+) = restricticin + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81535"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57305"},{"database":"ChEBI","id":"CHEBI:231923"},{"database":"ChEBI","id":"CHEBI:231924"}]}}
```

Source SHA-256: `19a0760299ea86767aedd0c4bc7a4c03cea71f9b30a199fbad0f1273b220873a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV3?format=txt&versions=4)  
**Locator:** `lines 23-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:53.747402+00:00.  

```text
CC   -!- FUNCTION: Nonribosomal peptide synthetase; part of the gene cluster
CC       that mediates the biosynthesis of the tetrahydropyranyl antifungal
CC       agent restricticin that acts as an inhibitor of CYP51 and blocks the
CC       ergosterol biosynthesis (PubMed:39105744). Within the pathway, resC
CC       catalyzes the C3 esterification of restrictinol with glycine to yield
CC       restricticin. ResC represents an example of the emerging class of
CC       single-module NRPS-like enzymes that perform esterification reactions
CC       (By similarity). The highly reducing polyketide synthase resH, the
CC       short chain dehydrogenase resG, the cyclase resF, the FAD-dependent
CC       monooxygenase resA and the enoylreductase resD are required to generate
CC       the first stable intermediate desmethylrestrictinol. ResH with resD
CC       biosynthesize the first polyketide chain intermediate that is reduced
CC       by resG, followed by epoxidation by resA before 6-endo cyclization via
CC       epoxide opening by resF leads to desmethylrestrictinol. The
CC       methyltransferase resE then catalyzes the C4 O-methylation of
CC       desmethylrestrictinol to produce restrictinol, and the nonribosomal
CC       peptide synthetase resC catalyzes the C3 esterification of restrictinol
CC       with glycine that leads to restricticin (By similarity).
CC       {ECO:0000250|UniProtKB:A0A0L1JF11, ECO:0000269|PubMed:39105744}.
```

Source SHA-256: `1b7003df6665300ef1ac888ec6d64f0457b8f53c5d0454d1efab44d4b6ba307d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV3?format=txt&versions=4)  
**Locator:** `lines 42-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:53.747402+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=restrictinol + glycine + H(+) = restricticin + H2O;
CC         Xref=Rhea:RHEA:81535, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57305, ChEBI:CHEBI:231923, ChEBI:CHEBI:231924;
CC         Evidence={ECO:0000305|PubMed:39105744};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81536;
CC         Evidence={ECO:0000305|PubMed:39105744};
```

Source SHA-256: `1b7003df6665300ef1ac888ec6d64f0457b8f53c5d0454d1efab44d4b6ba307d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV3?format=txt&versions=4)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:53.747402+00:00.  

```text
DR   GO; GO:0016874; F:ligase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `1b7003df6665300ef1ac888ec6d64f0457b8f53c5d0454d1efab44d4b6ba307d`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 153). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
