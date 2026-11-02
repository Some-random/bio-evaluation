# GO_biological_process_0164

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — &#x27;de novo&#x27; L-methionine biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. 'de novo' L-methionine biosynthetic process
B. response to muscle stretch
C. manganese ion transport
D. ubiquinone biosynthetic process
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

> The supplied sequence exactly matches the historical UniProt record for a fungal homoserine O-acetyltransferase. Its annotation says it commits homoserine to methionine biosynthesis, and assigns the de novo L-methionine biosynthetic process with IDA evidence. The function and pathway annotations cite experimental evidence, though the primary study was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct processes, but the sequence alone does not provide a clear, general biological argument identifying this protein's specific enzymatic role or pathway.


**Missing item-specific fact**

> The protein-specific fact that this sequence encodes homoserine O-acetyltransferase, which catalyzes an entry step into de novo methionine biosynthesis.


**Reason**

> Selecting A depends on identifying the protein and knowing its annotated or experimentally supported function—an item-specific fact absent from the question input. The reviewer-only sequence-matched annotations support the key but were not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A; none of the other choices is indicated for this protein.


### Important caveats

- Sequence identity and historical annotation match are established by reviewer-only evidence; the accession and annotations were absent from the evaluated model input.
- The cited experimental evidence supports the recorded function, but the underlying primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options describe distinct processes, but the sequence alone does not provide a clear, general biological argument identifying this protein's specific enzymatic role or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence encodes homoserine O-acetyltransferase, which catalyzes an entry step into de novo methionine biosynthesis.",
    "reason": "Selecting A depends on identifying the protein and knowing its annotated or experimentally supported function—an item-specific fact absent from the question input. The reviewer-only sequence-matched annotations support the key but were not available to the evaluated model."
  },
  "case_id": "GO_biological_process_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical UniProt record for a fungal homoserine O-acetyltransferase. Its annotation says it commits homoserine to methionine biosynthesis, and assigns the de novo L-methionine biosynthetic process with IDA evidence. The function and pathway annotations cite experimental evidence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "Sequence identity and historical annotation match are established by reviewer-only evidence; the accession and annotations were absent from the evaluated model input.",
    "The cited experimental evidence supports the recorded function, but the underlying primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; none of the other choices is indicated for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical UniProt record for a fungal homoserine O-acetyltransferase. Its annotation says it commits homoserine to methionine biosynthesis, and assigns the de novo L-methionine biosynthetic process with IDA evidence. The function and pathway annotations cite experimental evidence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["H3", "H4", "H5", "C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct processes, but the sequence alone does not provide a clear, general biological argument identifying this protein's specific enzymatic role or pathway.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence encodes homoserine O-acetyltransferase, which catalyzes an entry step into de novo methionine biosynthesis.",
    "reason": "Selecting A depends on identifying the protein and knowing its annotated or experimentally supported function—an item-specific fact absent from the question input. The reviewer-only sequence-matched annotations support the key but were not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A; none of the other choices is indicated for this protein."
  },
  "important_caveats": [
    "Sequence identity and historical annotation match are established by reviewer-only evidence; the accession and annotations were absent from the evaluated model input.",
    "The cited experimental evidence supports the recorded function, but the underlying primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt J9VIY8 (MET2_CRYN9), annotated as Homoserine O-acetyltransferase (EC 2.3.1.31) with experimental evidence (ECO:0000269, PubMed:17353245). The FUNCTION comment states it 'Commits homoserine to the methionine biosynthesis pathway by catalyzing its O-acetylation.' The PATHWAY comment places it in 'L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' The GO annotation GO:0071266 ('de novo' L-methionine biosynthetic process) is supported by IDA (Inferred from Direct Assay). Historical archived entry (version 54) confirms identical annotations.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is from Cryptococcus neoformans (a fungus), eliminating option B (response to muscle stretch) since fungi lack muscles entirely. The sequence lacks transmembrane helices or transporter motifs, eliminating option C (manganese ion transport). The sequence contains motifs consistent with a GNAT (GCN5-related N-acetyltransferase) fold (e.g., 'GGSMGGMTVLEY' acetyl-CoA binding region), identifying it as an acyltransferase enzyme. GNAT acetyltransferases are predominantly involved in amino acid biosynthetic pathways (homoserine, lysine, isoleucine), not in ubiquinone biosynthesis, which employs prenyltransferases, methyltransferases, decarboxylases, and hydroxylases. This eliminates option D. The remaining option A ('de novo' L-methionine biosynthetic process) is the only amino acid biosynthetic pathway offered, consistent with GNAT-family function.


**Missing item-specific fact**

> Specific substrate identification (homoserine vs. other amino acid substrates) would require detailed active-site knowledge or database lookup, but since only one amino acid biosynthetic pathway is offered among the choices, the GNAT-to-amino-acid-biosynthesis association suffices to select A.


**Reason**

> A model with general biological knowledge can: (1) eliminate B because fungi lack muscle tissue; (2) eliminate C because the sequence lacks membrane-spanning regions; (3) recognize acyltransferase-like motifs and associate GNAT folds with amino acid biosynthesis rather than ubiquinone biosynthesis, eliminating D. This provides a concrete reasoning chain from sequence features and general pathway biology to option A, though the final step relies on the fact that only methionine biosynthesis is offered among amino acid pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are clearly incompatible with a fungal soluble enzyme lacking transmembrane domains. Option D (ubiquinone biosynthesis) uses a distinct enzyme class (prenyltransferases, methyltransferases, oxidoreductases) unlike the GNAT acetyltransferase fold present here. Only option A is consistent with the sequence features and organism context.


### Important caveats

- The GNAT fold recognition from raw sequence without structural prediction tools is non-trivial; a model would need to identify the acetyl-CoA binding motifs (e.g., GGSMGGMT) and the compact domain architecture.
- The reasoning distinguishes A from D via general pathway-enzyme-class associations but does not uniquely identify homoserine as the specific substrate from sequence alone; it relies on the fact that only one amino acid biosynthetic pathway is offered.
- The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.
- The historical entry (version 54, first released 2026-01) postdates the original sequence deposition (2012-11-28), so the Swiss-Prot annotation was added after the sequence was first published.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is from Cryptococcus neoformans (a fungus), eliminating option B (response to muscle stretch) since fungi lack muscles entirely. The sequence lacks transmembrane helices or transporter motifs, eliminating option C (manganese ion transport). The sequence contains motifs consistent with a GNAT (GCN5-related N-acetyltransferase) fold (e.g., 'GGSMGGMTVLEY' acetyl-CoA binding region), identifying it as an acyltransferase enzyme. GNAT acetyltransferases are predominantly involved in amino acid biosynthetic pathways (homoserine, lysine, isoleucine), not in ubiquinone biosynthesis, which employs prenyltransferases, methyltransferases, decarboxylases, and hydroxylases. This eliminates option D. The remaining option A ('de novo' L-methionine biosynthetic process) is the only amino acid biosynthetic pathway offered, consistent with GNAT-family function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific substrate identification (homoserine vs. other amino acid substrates) would require detailed active-site knowledge or database lookup, but since only one amino acid biosynthetic pathway is offered among the choices, the GNAT-to-amino-acid-biosynthesis association suffices to select A.",
    "reason": "A model with general biological knowledge can: (1) eliminate B because fungi lack muscle tissue; (2) eliminate C because the sequence lacks membrane-spanning regions; (3) recognize acyltransferase-like motifs and associate GNAT folds with amino acid biosynthesis rather than ubiquinone biosynthesis, eliminating D. This provides a concrete reasoning chain from sequence features and general pathway biology to option A, though the final step relies on the fact that only methionine biosynthesis is offered among amino acid pathways."
  },
  "case_id": "GO_biological_process_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt J9VIY8 (MET2_CRYN9), annotated as Homoserine O-acetyltransferase (EC 2.3.1.31) with experimental evidence (ECO:0000269, PubMed:17353245). The FUNCTION comment states it 'Commits homoserine to the methionine biosynthesis pathway by catalyzing its O-acetylation.' The PATHWAY comment places it in 'L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' The GO annotation GO:0071266 ('de novo' L-methionine biosynthetic process) is supported by IDA (Inferred from Direct Assay). Historical archived entry (version 54) confirms identical annotations."
  },
  "important_caveats": [
    "The GNAT fold recognition from raw sequence without structural prediction tools is non-trivial; a model would need to identify the acetyl-CoA binding motifs (e.g., GGSMGGMT) and the compact domain architecture.",
    "The reasoning distinguishes A from D via general pathway-enzyme-class associations but does not uniquely identify homoserine as the specific substrate from sequence alone; it relies on the fact that only one amino acid biosynthetic pathway is offered.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.",
    "The historical entry (version 54, first released 2026-01) postdates the original sequence deposition (2012-11-28), so the Swiss-Prot annotation was added after the sequence was first published."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly incompatible with a fungal soluble enzyme lacking transmembrane domains. Option D (ubiquinone biosynthesis) uses a distinct enzyme class (prenyltransferases, methyltransferases, oxidoreductases) unlike the GNAT acetyltransferase fold present here. Only option A is consistent with the sequence features and organism context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt J9VIY8 (MET2_CRYN9), annotated as Homoserine O-acetyltransferase (EC 2.3.1.31) with experimental evidence (ECO:0000269, PubMed:17353245). The FUNCTION comment states it 'Commits homoserine to the methionine biosynthesis pathway by catalyzing its O-acetylation.' The PATHWAY comment places it in 'L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' The GO annotation GO:0071266 ('de novo' L-methionine biosynthetic process) is supported by IDA (Inferred from Direct Assay). Historical archived entry (version 54) confirms identical annotations.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is from Cryptococcus neoformans (a fungus), eliminating option B (response to muscle stretch) since fungi lack muscles entirely. The sequence lacks transmembrane helices or transporter motifs, eliminating option C (manganese ion transport). The sequence contains motifs consistent with a GNAT (GCN5-related N-acetyltransferase) fold (e.g., 'GGSMGGMTVLEY' acetyl-CoA binding region), identifying it as an acyltransferase enzyme. GNAT acetyltransferases are predominantly involved in amino acid biosynthetic pathways (homoserine, lysine, isoleucine), not in ubiquinone biosynthesis, which employs prenyltransferases, methyltransferases, decarboxylases, and hydroxylases. This eliminates option D. The remaining option A ('de novo' L-methionine biosynthetic process) is the only amino acid biosynthetic pathway offered, consistent with GNAT-family function.",
    "missing_item_specific_fact": "Specific substrate identification (homoserine vs. other amino acid substrates) would require detailed active-site knowledge or database lookup, but since only one amino acid biosynthetic pathway is offered among the choices, the GNAT-to-amino-acid-biosynthesis association suffices to select A.",
    "reason": "A model with general biological knowledge can: (1) eliminate B because fungi lack muscle tissue; (2) eliminate C because the sequence lacks membrane-spanning regions; (3) recognize acyltransferase-like motifs and associate GNAT folds with amino acid biosynthesis rather than ubiquinone biosynthesis, eliminating D. This provides a concrete reasoning chain from sequence features and general pathway biology to option A, though the final step relies on the fact that only methionine biosynthesis is offered among amino acid pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly incompatible with a fungal soluble enzyme lacking transmembrane domains. Option D (ubiquinone biosynthesis) uses a distinct enzyme class (prenyltransferases, methyltransferases, oxidoreductases) unlike the GNAT acetyltransferase fold present here. Only option A is consistent with the sequence features and organism context."
  },
  "important_caveats": [
    "The GNAT fold recognition from raw sequence without structural prediction tools is non-trivial; a model would need to identify the acetyl-CoA binding motifs (e.g., GGSMGGMT) and the compact domain architecture.",
    "The reasoning distinguishes A from D via general pathway-enzyme-class associations but does not uniquely identify homoserine as the specific substrate from sequence alone; it relies on the fact that only one amino acid biosynthetic pathway is offered.",
    "The GO annotation evidence code is IDA (Inferred from Direct Assay), indicating experimental support rather than computational transfer.",
    "The historical entry (version 54, first released 2026-01) postdates the original sequence deposition (2012-11-28), so the Swiss-Prot annotation was added after the sequence was first published."
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

**Accession:** `J9VIY8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"2.3.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine O-acetyltransferase"}}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"Commits homoserine to the methionine biosynthesis pathway by catalyzing its O-acetylation"}]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1"}]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17353245","source":"PubMed"}],"id":"GO:0071266","properties":[{"key":"GoTerm","value":"P:'de novo' L-methionine biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 43-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
CC   -!- FUNCTION: Commits homoserine to the methionine biosynthesis pathway by
CC       catalyzing its O-acetylation. {ECO:0000269|PubMed:17353245}.
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 55-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.
CC       {ECO:0000269|PubMed:17353245}.
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
DR   GO; GO:0071266; P:'de novo' L-methionine biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 375453-375475`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0071266
name: 'de novo' L-methionine biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of L-methionine, the L-enantiomer of (2S)-2-amino-4-(methylsulfanyl)butanoic acid, from simpler components such as L-aspartate or L-homoserine. This process occurs in plants, bacteria, archae and fungi." [PMID:12818659, PMID:24939187]
synonym: "'de novo' L-methionine anabolism" EXACT [GOC:mah]
synonym: "'de novo' L-methionine biosynthesis" EXACT [GOC:mah]
synonym: "'de novo' L-methionine formation" EXACT [GOC:mah]
synonym: "'de novo' L-methionine synthesis" EXACT [GOC:mah]
xref: MetaCyc:HOMOSER-METSYN-PWY
xref: MetaCyc:HSERMETANA-PWY
xref: MetaCyc:PWY-5345
xref: MetaCyc:PWY-5347
xref: MetaCyc:PWY-702
xref: MetaCyc:PWY-7977
is_a: GO:0071265 ! L-methionine biosynthetic process
property_value: skos:narrowMatch MetaCyc:HOMOSER-METSYN-PWY
property_value: skos:narrowMatch MetaCyc:HSERMETANA-PWY
property_value: skos:narrowMatch MetaCyc:PWY-5345
property_value: skos:narrowMatch MetaCyc:PWY-5347
property_value: skos:narrowMatch MetaCyc:PWY-702
property_value: skos:narrowMatch MetaCyc:PWY-7977

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
