# GO_biological_process_0120

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — exocytosis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMKLKEMVEAAEAKVESKPPQAAEEKAPDQAAGGAEEDVAAAPAEGGEGAEPLDQAEIEKMLFDESLGAQEYTYEEFLDLIDQPPEERGEAEDERKHWSYPRRWKVVLWNLQIQNYMDDNFSAFMEFEFGGTREECKVHKGTSVLIYATGQDKNYLRTPVIPDVSNAGPVDMHFRKAFEYRGSYLDLEREKLKIKVWEYRNWTLNHLEAVYEEALLNLATGETHVERDLYKFIKGRRSRRCRISFHLYFQELYDFELSFVKWRLVQIMPCLTLQEKIANRGKNKGGYTREATIGFKRHQLADQAKYVFQQRQVKREMQKRDSQRELLPGASRPEMLGGFADKGSARLSHLGFESAMKLPNRGTRSPSGLESNRPEDGNRNMEEIFLQHQATILASDQLEELPASLRPPLSKRRKGEDKKDGNKADGPQVKMTISLMHASSMNKGLGLVSSERPADGIPRWDNLGEIYFRGTLRDLDSTYIQVVVEDTTAPKVMRQIGYGQIPLRGVVDYSCLSTELGTPMWLALQAKMEGWGHELKEWCFGFVEGTVMVAHLPRYRQLGEVSESDSDRVYLILRIKDVDQIVTPDNRPVVDSYVEVSFDGTSRRTRTVRNTLNPVWDDEVTIPLRLPAFRDITESDVTRKGKVWLDVWGTGPGYVDHLGGCSFSLYEIFFNEKHNKRNLTAMQRIDLEANTRQSYETRVFSTSRRLAFIHKADRPSTIQFEAWTCPDILEVSGIDKLPEPERITTTSNFPRALRNTYERLKRMYAEVIEKKGLVNPDTGVGPPRFFDVEFLDQRKETHYAPTMVTRIRPPFGVDSESSVFHYCRCVPFAVKRENLVFTPEFAVQIRSGNAMDHSILMTSLLLGLPAFAFVCVGTLWDKHMHAWVATFHYDDDRACGVVKFWETTTGLVYTLKHRFRDPYTLQRLSADPEFGILKMMNIQRRKRLSILGVSVDADTPDYISRSGEDLVQSEFPTGGAKLPYRSLDIMFNNRNVWLNIQDGNPAKVWFDIWDVEQWYQFSPGLHDVPPCFIVRGFGAKVAEWQFDRAAQEIQGKVLSDITAFRATRNLPTKWNRDDVLDAFLQMGLELLHQAATARDEDFQLARLKLEDWKKAFYSKVPCSYRVRGAPLHFNTYDSKTISDAIIANVDFVESRDRSAFFSLAVMLYNLPGELVSTYVYICVTQKVTERERRRILAQKEKQSREDAQRKARKQRRKAGHEGADNGAEDKQGAEGNEEEHGDAAAAAVAEESVSAEAVQGAEEPKKVVKKGAVPRVKKRSYEQVEGTEVAAIAIERDFFTEAEAPDFKNLMTDVEHAINTHLGLSPGRVRAFQARYAEKRIVFAVGPPMDDATEADAVSSVALMEKLRDILPSMAHEEGRFQEVTGGGATLQWDGPGTNILDRIAQEQATAGEGEQQTSEGIPTRDMQVDGTAVLEEAGEKSDKKKKKKEKKEKKEKKEKKEKKEKKEKKKKKGGETAAEPEEASAVLAPPPVPAPAAAIPSVLLPTDSEDGEKEKPKEKKKEKKEKKKKKDGETDAEPDEASAVLAPPPVPVPAAAIPSILLPADGEDGEEEKPKEKKTEKKKEKHTEKKHKKKSETLPESETTAVVTVTPGEEDETSPLVPVPSSIASSEAPEPPASTRVTPAPEPKAKPGLSMGAALLAVRARSRLQRKHLAQQLSSSSSSEVSASSASSLSPSSSSSSDFAETRAKADALRARLQAAQARLAAARETEVSSSETESSETSEASFLSSDGEWDALWQSQRAAAMERQQRLQKMVSGVKAAYRRLEEENTRLAATRRRDDKLQRQVEAERERAVELLKEATRRAKEEKDLIARQPPPARDWSDTVVLSTPQIFVNSQAACAPFADSGRDEGERDEWYEVSDACSRRAESSNESRTTAGAKLRQQQLDLAGRT

[Multiple Choices]
A. exocytosis
B. fatty acid biosynthetic process
C. aggresome assembly
D. regulation of DNA replication
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

> The sequence-matched UniProt entry reports that TgDOC2 regulates microneme secretion, with experimental evidence cited, and associates it with exocytosis. This supports choice A, while distinguishing regulation of secretion from a claim that the protein itself performs vesicle fusion.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> C2 domains can suggest membrane- or vesicle-related functions, but that broad clue does not establish this protein's role in secretion or distinguish exocytosis from the other listed processes.


**Missing item-specific fact**

> The protein-specific finding that this Toxoplasma gondii protein regulates microneme secretion and is associated with exocytosis.


**Reason**

> The sequence is provided without organism or functional context. Selecting exocytosis depends on knowing the protein's specific function; recognizing its identity or consulting its annotation is not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available protein-specific evidence supports exocytosis; none of the other choices is comparably supported.


### Important caveats

- The sequence match and relevant annotation are established by reviewer-only evidence, not information supplied to the evaluated model.
- The UniProt GO annotation is marked IEA, while the secretion-function statement cites experimental evidence; these are distinct evidence types.
- The function statement describes regulation of microneme secretion and probable regulation of other secretory granules, not direct demonstration that the protein catalyzes membrane fusion.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "C2 domains can suggest membrane- or vesicle-related functions, but that broad clue does not establish this protein's role in secretion or distinguish exocytosis from the other listed processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this Toxoplasma gondii protein regulates microneme secretion and is associated with exocytosis.",
    "reason": "The sequence is provided without organism or functional context. Selecting exocytosis depends on knowing the protein's specific function; recognizing its identity or consulting its annotation is not reasoning from the supplied input."
  },
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports that TgDOC2 regulates microneme secretion, with experimental evidence cited, and associates it with exocytosis. This supports choice A, while distinguishing regulation of secretion from a claim that the protein itself performs vesicle fusion."
  },
  "important_caveats": [
    "The sequence match and relevant annotation are established by reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt GO annotation is marked IEA, while the secretion-function statement cites experimental evidence; these are distinct evidence types.",
    "The function statement describes regulation of microneme secretion and probable regulation of other secretory granules, not direct demonstration that the protein catalyzes membrane fusion."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available protein-specific evidence supports exocytosis; none of the other choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry reports that TgDOC2 regulates microneme secretion, with experimental evidence cited, and associates it with exocytosis. This supports choice A, while distinguishing regulation of secretion from a claim that the protein itself performs vesicle fusion.",
    "evidence_ids": ["C5", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "C2 domains can suggest membrane- or vesicle-related functions, but that broad clue does not establish this protein's role in secretion or distinguish exocytosis from the other listed processes.",
    "missing_item_specific_fact": "The protein-specific finding that this Toxoplasma gondii protein regulates microneme secretion and is associated with exocytosis.",
    "reason": "The sequence is provided without organism or functional context. Selecting exocytosis depends on knowing the protein's specific function; recognizing its identity or consulting its annotation is not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available protein-specific evidence supports exocytosis; none of the other choices is comparably supported."
  },
  "important_caveats": [
    "The sequence match and relevant annotation are established by reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt GO annotation is marked IEA, while the secretion-function statement cites experimental evidence; these are distinct evidence types.",
    "The function statement describes regulation of microneme secretion and probable regulation of other secretory granules, not direct demonstration that the protein catalyzes membrane fusion."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7J6K9S4 (TgDOC2, Toxoplasma gondii) is annotated with GO:0006887 (exocytosis). The FUNCTION comment (ECO:0000269, direct assay evidence) states it 'Regulates microneme secretion' and is 'probably involved in regulation of rhoptry and dense granule secretion,' backed by two experimental publications (PubMed:22246776, Science 2012; PubMed:33803212, Life 2021). The GO annotation itself is IEA:UniProtKB-KW, but the underlying experimental evidence for exocytosis is strong. The Science paper title explicitly states 'essential for apicomplexan parasite exocytosis.'

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains C2 domain(s), identifiable by conserved beta-sandwich structural motifs with aromatic and aspartate residues that coordinate calcium. C2 domains are well-established calcium-sensing modules in exocytosis machinery (e.g., synaptotagmin in neurotransmitter release, DOC2 in regulated secretion). A model recognizing C2 domain signatures can connect them to calcium-triggered vesicle fusion/exocytosis. The distractors are mechanistically incompatible: fatty acid biosynthesis requires FAS/ACC enzymatic domains, aggresome assembly requires chaperone/co-chaperone interaction domains, and DNA replication regulation requires polymerase-associated or cell-cycle regulatory domains—none of which are present in this sequence.


**Missing item-specific fact**

> None critical. The C2 domain → exocytosis association is general biological knowledge. The specific Toxoplasma microneme/rhoptry pathway is organism-specific but the general GO term 'exocytosis' is derivable from domain recognition.


**Reason**

> The presence of C2 domain architecture is a concrete sequence-based feature that connects to exocytosis through well-established biological knowledge. The four options are mechanistically distinct enough that domain recognition provides meaningful discrimination without requiring memorization of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors (fatty acid biosynthesis, aggresome assembly, DNA replication regulation) are mechanistically incompatible with a C2 domain-containing secretory protein. Only exocytosis aligns with the domain architecture.


### Important caveats

- The GO annotation for exocytosis is IEA (inferred from keyword), not a direct experimental GO annotation, though the underlying function is experimentally validated (ECO:0000269).
- The specific exocytosis pathway (microneme/rhoptry secretion) is Toxoplasma-specific; the general GO term 'exocytosis' is broader and still correct.
- C2 domain recognition from raw sequence requires specialized domain knowledge; a model without this training may struggle to identify the domain in a 1910-aa protein with many other regions.
- The identity of this protein as TgDOC2 was inferred from image-path metadata (reviewer-only); the evaluated model received only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains C2 domain(s), identifiable by conserved beta-sandwich structural motifs with aromatic and aspartate residues that coordinate calcium. C2 domains are well-established calcium-sensing modules in exocytosis machinery (e.g., synaptotagmin in neurotransmitter release, DOC2 in regulated secretion). A model recognizing C2 domain signatures can connect them to calcium-triggered vesicle fusion/exocytosis. The distractors are mechanistically incompatible: fatty acid biosynthesis requires FAS/ACC enzymatic domains, aggresome assembly requires chaperone/co-chaperone interaction domains, and DNA replication regulation requires polymerase-associated or cell-cycle regulatory domains—none of which are present in this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The C2 domain → exocytosis association is general biological knowledge. The specific Toxoplasma microneme/rhoptry pathway is organism-specific but the general GO term 'exocytosis' is derivable from domain recognition.",
    "reason": "The presence of C2 domain architecture is a concrete sequence-based feature that connects to exocytosis through well-established biological knowledge. The four options are mechanistically distinct enough that domain recognition provides meaningful discrimination without requiring memorization of this specific UniProt entry."
  },
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6K9S4 (TgDOC2, Toxoplasma gondii) is annotated with GO:0006887 (exocytosis). The FUNCTION comment (ECO:0000269, direct assay evidence) states it 'Regulates microneme secretion' and is 'probably involved in regulation of rhoptry and dense granule secretion,' backed by two experimental publications (PubMed:22246776, Science 2012; PubMed:33803212, Life 2021). The GO annotation itself is IEA:UniProtKB-KW, but the underlying experimental evidence for exocytosis is strong. The Science paper title explicitly states 'essential for apicomplexan parasite exocytosis.'"
  },
  "important_caveats": [
    "The GO annotation for exocytosis is IEA (inferred from keyword), not a direct experimental GO annotation, though the underlying function is experimentally validated (ECO:0000269).",
    "The specific exocytosis pathway (microneme/rhoptry secretion) is Toxoplasma-specific; the general GO term 'exocytosis' is broader and still correct.",
    "C2 domain recognition from raw sequence requires specialized domain knowledge; a model without this training may struggle to identify the domain in a 1910-aa protein with many other regions.",
    "The identity of this protein as TgDOC2 was inferred from image-path metadata (reviewer-only); the evaluated model received only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (fatty acid biosynthesis, aggresome assembly, DNA replication regulation) are mechanistically incompatible with a C2 domain-containing secretory protein. Only exocytosis aligns with the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0120",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6K9S4 (TgDOC2, Toxoplasma gondii) is annotated with GO:0006887 (exocytosis). The FUNCTION comment (ECO:0000269, direct assay evidence) states it 'Regulates microneme secretion' and is 'probably involved in regulation of rhoptry and dense granule secretion,' backed by two experimental publications (PubMed:22246776, Science 2012; PubMed:33803212, Life 2021). The GO annotation itself is IEA:UniProtKB-KW, but the underlying experimental evidence for exocytosis is strong. The Science paper title explicitly states 'essential for apicomplexan parasite exocytosis.'",
    "evidence_ids": ["C5", "C6", "C8", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains C2 domain(s), identifiable by conserved beta-sandwich structural motifs with aromatic and aspartate residues that coordinate calcium. C2 domains are well-established calcium-sensing modules in exocytosis machinery (e.g., synaptotagmin in neurotransmitter release, DOC2 in regulated secretion). A model recognizing C2 domain signatures can connect them to calcium-triggered vesicle fusion/exocytosis. The distractors are mechanistically incompatible: fatty acid biosynthesis requires FAS/ACC enzymatic domains, aggresome assembly requires chaperone/co-chaperone interaction domains, and DNA replication regulation requires polymerase-associated or cell-cycle regulatory domains—none of which are present in this sequence.",
    "missing_item_specific_fact": "None critical. The C2 domain → exocytosis association is general biological knowledge. The specific Toxoplasma microneme/rhoptry pathway is organism-specific but the general GO term 'exocytosis' is derivable from domain recognition.",
    "reason": "The presence of C2 domain architecture is a concrete sequence-based feature that connects to exocytosis through well-established biological knowledge. The four options are mechanistically distinct enough that domain recognition provides meaningful discrimination without requiring memorization of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors (fatty acid biosynthesis, aggresome assembly, DNA replication regulation) are mechanistically incompatible with a C2 domain-containing secretory protein. Only exocytosis aligns with the domain architecture."
  },
  "important_caveats": [
    "The GO annotation for exocytosis is IEA (inferred from keyword), not a direct experimental GO annotation, though the underlying function is experimentally validated (ECO:0000269).",
    "The specific exocytosis pathway (microneme/rhoptry secretion) is Toxoplasma-specific; the general GO term 'exocytosis' is broader and still correct.",
    "C2 domain recognition from raw sequence requires specialized domain knowledge; a model without this training may struggle to identify the domain in a 1910-aa protein with many other regions.",
    "The identity of this protein as TgDOC2 was inferred from image-path metadata (reviewer-only); the evaluated model received only the raw sequence."
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

**Accession:** `A0A7J6K9S4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 14. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:41.523865+00:00.  

```json
{"entryVersion":16,"firstPublicDate":"2025-02-05","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2021-04-07","sequenceVersion":1}
```

Source SHA-256: `6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:41.523865+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22246776","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33803212","source":"PubMed"}],"value":"Regulates microneme secretion (PubMed:22246776, PubMed:33803212). Probably involved in regulation of rhoptry and dense granule secretion (PubMed:33803212)"}]}
```

Source SHA-256: `6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:41.523865+00:00.  

```json
{"citation":{"authors":["Farrell A.","Thirugnanam S.","Lorestani A.","Dvorin J.D.","Eidell K.P.","Ferguson D.J.","Anderson-White B.R.","Duraisingh M.T.","Marth G.T.","Gubbels M.J."],"citationCrossReferences":[{"database":"PubMed","id":"22246776"},{"database":"DOI","id":"10.1126/science.1210829"}],"citationType":"journal article","firstPage":"218","id":"22246776","journal":"Science","lastPage":"221","publicationDate":"2012","title":"A DOC2 protein identified by mutational profiling is essential for apicomplexan parasite exocytosis.","volume":"335"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","MUTAGENESIS OF PHE-124"]}
```

Source SHA-256: `6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K9S4.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:41.523865+00:00.  

```json
{"citation":{"authors":["Tagoe D.N.A.","Drozda A.A.","Falco J.A.","Bechtel T.J.","Weerapana E.","Gubbels M.J."],"citationCrossReferences":[{"database":"PubMed","id":"33803212"},{"database":"DOI","id":"10.3390/life11030217"}],"citationType":"journal article","firstPage":"0","id":"33803212","journal":"Life","lastPage":"0","publicationDate":"2021","title":"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33803212","source":"PubMed"}],"type":"STRAIN","value":"RH"}],"referenceNumber":4,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `6fe7822b937a0480c04f70d4c3597e0b526003636957e52477842b05828381ad`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)  
**Locator:** `lines 20-28`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:43.566279+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, AND MUTAGENESIS OF PHE-124.
RX   PubMed=22246776; DOI=10.1126/science.1210829;
RA   Farrell A., Thirugnanam S., Lorestani A., Dvorin J.D., Eidell K.P.,
RA   Ferguson D.J., Anderson-White B.R., Duraisingh M.T., Marth G.T.,
RA   Gubbels M.J.;
RT   "A DOC2 protein identified by mutational profiling is essential for
RT   apicomplexan parasite exocytosis.";
RL   Science 335:218-221(2012).
```

Source SHA-256: `ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)  
**Locator:** `lines 36-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:43.566279+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION.
RC   STRAIN=RH {ECO:0000303|PubMed:33803212};
RX   PubMed=33803212; DOI=10.3390/life11030217;
RA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,
RA   Gubbels M.J.;
RT   "Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule
RT   Secretion.";
RL   Life 11:0-0(2021).
```

Source SHA-256: `ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)  
**Locator:** `lines 45-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:43.566279+00:00.  

```text
CC   -!- FUNCTION: Regulates microneme secretion (PubMed:22246776,
CC       PubMed:33803212). Probably involved in regulation of rhoptry and dense
CC       granule secretion (PubMed:33803212). {ECO:0000269|PubMed:22246776,
CC       ECO:0000269|PubMed:33803212}.
```

Source SHA-256: `ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K9S4?format=txt&versions=14)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 14 / 1.  
**Retrieved:** 2026-11-02T04:25:43.566279+00:00.  

```text
DR   GO; GO:0006887; P:exocytosis; IEA:UniProtKB-KW.
```

Source SHA-256: `ddf9bb5b3f8c44fb66c0d3965cb8eea2bffb58249da33057cc0b438994f15702`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 120. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
