# catalytic_activity_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — ATP + H2O = ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPYQMGEAMPDLVPVLAGAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTAETIADPEARSVANRAIVTLRRIGKVPVESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLSDKRLLATPEEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEEFVKHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAVLGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAELAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGHLEASGHNWVEGQGSGERIDKKAGDDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
B. Na(+)(in) = Na(+)(out)
C. ATP + H2O = ADP + phosphate + H(+)
D. a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the cited UniProt protein, and its catalytic-activity annotation gives ATP + H2O = ADP + phosphate + H(+), citing ECO:0000269 evidence linked to PubMed 11244063. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two P-loop/Walker-A-like GxxxxGKT motifs and associated ATPase-domain features, consistent with a soluble ATP-hydrolyzing protein. It has no evident membrane-spanning segments to suggest sodium transport; the other choices describe specialized reactions not suggested by these motifs.


**Missing item-specific fact**

> No item-specific annotation is essential to favor the broad ATP-hydrolysis choice, although the exact protein identity and cited experimental annotation provide stronger confirmation.


**Reason**

> The ATPase motifs provide a concrete sequence-based basis for distinguishing choice C from the alternatives. They do not, on their own, prove the exact experimentally observed activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, ATP hydrolysis is the only one broadly supported by the sequence's ATPase motifs.


### Important caveats

- The database annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence.
- Sequence motifs support ATPase activity but do not alone establish the precise catalytic reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two P-loop/Walker-A-like GxxxxGKT motifs and associated ATPase-domain features, consistent with a soluble ATP-hydrolyzing protein. It has no evident membrane-spanning segments to suggest sodium transport; the other choices describe specialized reactions not suggested by these motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is essential to favor the broad ATP-hydrolysis choice, although the exact protein identity and cited experimental annotation provide stronger confirmation.",
    "reason": "The ATPase motifs provide a concrete sequence-based basis for distinguishing choice C from the alternatives. They do not, on their own, prove the exact experimentally observed activity."
  },
  "case_id": "catalytic_activity_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt protein, and its catalytic-activity annotation gives ATP + H2O = ADP + phosphate + H(+), citing ECO:0000269 evidence linked to PubMed 11244063. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence.",
    "Sequence motifs support ATPase activity but do not alone establish the precise catalytic reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, ATP hydrolysis is the only one broadly supported by the sequence's ATPase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt protein, and its catalytic-activity annotation gives ATP + H2O = ADP + phosphate + H(+), citing ECO:0000269 evidence linked to PubMed 11244063. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two P-loop/Walker-A-like GxxxxGKT motifs and associated ATPase-domain features, consistent with a soluble ATP-hydrolyzing protein. It has no evident membrane-spanning segments to suggest sodium transport; the other choices describe specialized reactions not suggested by these motifs.",
    "missing_item_specific_fact": "No item-specific annotation is essential to favor the broad ATP-hydrolysis choice, although the exact protein identity and cited experimental annotation provide stronger confirmation.",
    "reason": "The ATPase motifs provide a concrete sequence-based basis for distinguishing choice C from the alternatives. They do not, on their own, prove the exact experimentally observed activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, ATP hydrolysis is the only one broadly supported by the sequence's ATPase motifs."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary paper was not independently validated in the supplied evidence.",
    "Sequence motifs support ATPase activity but do not alone establish the precise catalytic reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5KIM6 (EF3_CRYD1, Elongation Factor 3 from Cryptococcus deneoformans) explicitly annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-) with experimental evidence code ECO:0000269 from PubMed:11244063 (Blakely et al., J. Bacteriol. 2001). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed, 1055 aa). Choice C matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains at least two clear Walker A (P-loop) motifs (GRNGSGKSTLMNAIINN and GPNGSGKSTLVKLLTGE) paired with Walker B motifs (DEPTNHLDVLNVDWLINY and DEPTNYLDRESLAALIAALKN), characteristic of P-loop NTPase/AAA+ domains. These motifs are the hallmark of ATP-hydrolyzing enzymes. The protein (~1055 aa, soluble, no predicted transmembrane segments) lacks the Rossmann-fold NAD(P)-binding signature needed for a dehydrogenase (rules out A), lacks the multi-TM P-type ATPase architecture (DktGT/TGE motifs, ion-binding TM helices) needed for a Na+ pump (rules out B), and lacks the Nudix/decapping enzyme fold (rules out D). The multiple Walker A/B pairs in a soluble multi-domain protein point directly to an ATPase, matching choice C.


**Missing item-specific fact**

> None critical. The Walker A/B motifs are directly readable from the supplied sequence. Specific identification as EF-3 (a fungal translation factor) would require database lookup, but the catalytic reaction (ATP hydrolysis) follows from the P-loop NTPase signature alone.


**Reason**

> A student trained in protein biochemistry can identify the GxxGxGK&#91;S/T&#93; and hhhhDE motifs as Walker A and Walker B signatures of P-loop NTPases. Combined with the absence of transmembrane helices (ruling out ion transport) and absence of Rossmann-fold or Nudix signatures (ruling out dehydrogenase and decapping), the ATPase reaction is the only consistent choice. This is a genuine sequence-to-function reasoning argument, not mere memorization of a specific protein name.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (dehydrogenase, ion pump, ATPase, decapping enzyme) with incompatible structural requirements. The Walker A/B motifs uniquely select the ATPase option among the given choices.


### Important caveats

- The EC number 3.6.4.- is an incomplete assignment (the '.' suffix indicates the full subclass/subclass/sub-subclass are not yet fully defined), but the reaction itself is unambiguous.
- The experimental evidence (ECO:0000269, PubMed:11244063) confirms ATP hydrolysis for this specific protein; the annotation is not purely computational.
- The identity as EF-3 (a translation elongation factor) is not needed to answer the question; the P-loop NTPase signature suffices to select choice C from the given options.
- The UniProt entry was first publicly released in 2025-02-05; the benchmark question's construction date relative to this release is unknown, but the sequence and motifs are intrinsic to the protein regardless of annotation timing.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains at least two clear Walker A (P-loop) motifs (GRNGSGKSTLMNAIINN and GPNGSGKSTLVKLLTGE) paired with Walker B motifs (DEPTNHLDVLNVDWLINY and DEPTNYLDRESLAALIAALKN), characteristic of P-loop NTPase/AAA+ domains. These motifs are the hallmark of ATP-hydrolyzing enzymes. The protein (~1055 aa, soluble, no predicted transmembrane segments) lacks the Rossmann-fold NAD(P)-binding signature needed for a dehydrogenase (rules out A), lacks the multi-TM P-type ATPase architecture (DktGT/TGE motifs, ion-binding TM helices) needed for a Na+ pump (rules out B), and lacks the Nudix/decapping enzyme fold (rules out D). The multiple Walker A/B pairs in a soluble multi-domain protein point directly to an ATPase, matching choice C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The Walker A/B motifs are directly readable from the supplied sequence. Specific identification as EF-3 (a fungal translation factor) would require database lookup, but the catalytic reaction (ATP hydrolysis) follows from the P-loop NTPase signature alone.",
    "reason": "A student trained in protein biochemistry can identify the GxxGxGK[S/T] and hhhhDE motifs as Walker A and Walker B signatures of P-loop NTPases. Combined with the absence of transmembrane helices (ruling out ion transport) and absence of Rossmann-fold or Nudix signatures (ruling out dehydrogenase and decapping), the ATPase reaction is the only consistent choice. This is a genuine sequence-to-function reasoning argument, not mere memorization of a specific protein name."
  },
  "case_id": "catalytic_activity_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5KIM6 (EF3_CRYD1, Elongation Factor 3 from Cryptococcus deneoformans) explicitly annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-) with experimental evidence code ECO:0000269 from PubMed:11244063 (Blakely et al., J. Bacteriol. 2001). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed, 1055 aa). Choice C matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The EC number 3.6.4.- is an incomplete assignment (the '.' suffix indicates the full subclass/subclass/sub-subclass are not yet fully defined), but the reaction itself is unambiguous.",
    "The experimental evidence (ECO:0000269, PubMed:11244063) confirms ATP hydrolysis for this specific protein; the annotation is not purely computational.",
    "The identity as EF-3 (a translation elongation factor) is not needed to answer the question; the P-loop NTPase signature suffices to select choice C from the given options.",
    "The UniProt entry was first publicly released in 2025-02-05; the benchmark question's construction date relative to this release is unknown, but the sequence and motifs are intrinsic to the protein regardless of annotation timing."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (dehydrogenase, ion pump, ATPase, decapping enzyme) with incompatible structural requirements. The Walker A/B motifs uniquely select the ATPase option among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5KIM6 (EF3_CRYD1, Elongation Factor 3 from Cryptococcus deneoformans) explicitly annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' (EC 3.6.4.-) with experimental evidence code ECO:0000269 from PubMed:11244063 (Blakely et al., J. Bacteriol. 2001). The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed, 1055 aa). Choice C matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains at least two clear Walker A (P-loop) motifs (GRNGSGKSTLMNAIINN and GPNGSGKSTLVKLLTGE) paired with Walker B motifs (DEPTNHLDVLNVDWLINY and DEPTNYLDRESLAALIAALKN), characteristic of P-loop NTPase/AAA+ domains. These motifs are the hallmark of ATP-hydrolyzing enzymes. The protein (~1055 aa, soluble, no predicted transmembrane segments) lacks the Rossmann-fold NAD(P)-binding signature needed for a dehydrogenase (rules out A), lacks the multi-TM P-type ATPase architecture (DktGT/TGE motifs, ion-binding TM helices) needed for a Na+ pump (rules out B), and lacks the Nudix/decapping enzyme fold (rules out D). The multiple Walker A/B pairs in a soluble multi-domain protein point directly to an ATPase, matching choice C.",
    "missing_item_specific_fact": "None critical. The Walker A/B motifs are directly readable from the supplied sequence. Specific identification as EF-3 (a fungal translation factor) would require database lookup, but the catalytic reaction (ATP hydrolysis) follows from the P-loop NTPase signature alone.",
    "reason": "A student trained in protein biochemistry can identify the GxxGxGK[S/T] and hhhhDE motifs as Walker A and Walker B signatures of P-loop NTPases. Combined with the absence of transmembrane helices (ruling out ion transport) and absence of Rossmann-fold or Nudix signatures (ruling out dehydrogenase and decapping), the ATPase reaction is the only consistent choice. This is a genuine sequence-to-function reasoning argument, not mere memorization of a specific protein name."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (dehydrogenase, ion pump, ATPase, decapping enzyme) with incompatible structural requirements. The Walker A/B motifs uniquely select the ATPase option among the given choices."
  },
  "important_caveats": [
    "The EC number 3.6.4.- is an incomplete assignment (the '.' suffix indicates the full subclass/subclass/sub-subclass are not yet fully defined), but the reaction itself is unambiguous.",
    "The experimental evidence (ECO:0000269, PubMed:11244063) confirms ATP hydrolysis for this specific protein; the annotation is not purely computational.",
    "The identity as EF-3 (a translation elongation factor) is not needed to answer the question; the P-loop NTPase signature suffices to select choice C from the given options.",
    "The UniProt entry was first publicly released in 2025-02-05; the benchmark question's construction date relative to this release is unknown, but the sequence and motifs are intrinsic to the protein regardless of annotation timing."
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

**Accession:** `Q5KIM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 144. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
"Q5KIM6"
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11244063","source":"PubMed"}],"value":"CnEF3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11244063","source":"PubMed"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"11244063","source":"PubMed"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KIM6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:21.720628+00:00.  

```json
{"citation":{"authors":["Blakely G.","Hekman J.","Chakraburtty K.","Williamson P.R."],"citationCrossReferences":[{"database":"PubMed","id":"11244063"},{"database":"DOI","id":"10.1128/jb.183.7.2241-2248.2001"}],"citationType":"journal article","firstPage":"2241","id":"11244063","journal":"J. Bacteriol.","lastPage":"2248","publicationDate":"2001","title":"Evolutionary divergence of an elongation factor 3 from Cryptococcus neoformans.","volume":"183"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11244063","source":"PubMed"}],"type":"STRAIN","value":"B-3501A"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ASSOCIATION WITH RIBOSOMES"]}
```

Source SHA-256: `b9f76863939454e32adab5e5278739a480eb0369e735b0270cd2d5d29a4838f4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
ID   EF3_CRYD1               Reviewed;        1055 AA.
AC   Q5KIM6; Q55TQ9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 144.
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000269|PubMed:11244063};
DE   AltName: Full=CnEF3 {ECO:0000303|PubMed:11244063};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
GN   Name=TEF3 {ECO:0000305};
GN   OrderedLocusNames=CND02420 {ECO:0000312|EMBL:AAW42954.1};
OS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus
OS   neoformans var. neoformans serotype D).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000269|PubMed:11244063};
DE   AltName: Full=CnEF3 {ECO:0000303|PubMed:11244063};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   ASSOCIATION WITH RIBOSOMES.
RC   STRAIN=B-3501A {ECO:0000303|PubMed:11244063};
RX   PubMed=11244063; DOI=10.1128/jb.183.7.2241-2248.2001;
RA   Blakely G., Hekman J., Chakraburtty K., Williamson P.R.;
RT   "Evolutionary divergence of an elongation factor 3 from Cryptococcus
RT   neoformans.";
RL   J. Bacteriol. 183:2241-2248(2001).
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KIM6?format=txt&versions=144)  
**Locator:** `lines 57-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 144 / 1.  
**Retrieved:** 2026-11-02T04:31:25.631379+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000269|PubMed:11244063};
```

Source SHA-256: `f8f04f71b942e5ecd89f3cc11a84ca820ff2e4d81bef906da3f22c50f8e5be67`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
