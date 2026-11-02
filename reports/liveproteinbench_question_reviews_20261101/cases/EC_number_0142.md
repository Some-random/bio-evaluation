# EC_number_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEQFGGPSGFMPPASYTAPLGKYPTKQPSAAYPSDGGRHATKENPRPAEGQASRQSSSVPSAMASKPIQDPEGHSAQPTSSYCRAQTPRSTPLPVALDEEARLSQYEVIRQIGAGRFGEVFIIRHKATKALLCWKLVFYKGLREKEKKQLVSEVNVMRELRHANIVRYHDRIVCRSRQCLYIVMEYCDAGDLAKQIEAAHKHHGGIDQDRIVLVVVQLIHALAYCHEGVGQERRRVLHRDLKPCNIFLASHPEYPDDSSRCIAKLGDFGLSRHLNMHSMAHSCVGTPYYWSPELLEDGQKTYNVKSDMWALGCVIYEMCTGKTPFAQAQTMPQLKERVRCGPVLPVPGFSDSLNALMASLLQPNPNNRPSALQCLGYTIFRGCSYTPPPLYRSSSAPSWTPRNASPARGSPSSAVSTVSTVTTSPGSSSRTSFSAPSSHDAAASSPASASASSRYQHQRSSSYSSDSAGPSGASAPSQKAPGPGRPPETPSRESFDLASKARPGFFAEAPPPHAFAEASPPESHASEFLPPANGAANEARNERTQRDRTRRAASATAAAAVSAFERQQREGRSMSPDPSAPLASIEEEEEGEGDDAGCGSLGSGSGVTRRMPGASLNREDRREAPGLRHADTHKRDDRDGAIWTGRREEAPFSRPGSELARDFGAASQNKVDTSRFSGASSGKPRPGNPQNEDRASFASDTSARQTVYLSGLSRRCSEPPAAFHSAVSPWDPAPPRLSSAASSSSSSRAVSPSSLRRASSREMKYPTDDRPAVAAGSSGVALARAERGPEPGAPWGNEETEGLHVHGRPSAAPASSFSSERTSRPGHPDEARESEHCFQGRGRFAEAEASPATEGKDPRDSGFEERSGRRDEGRTDGGEAQSFGYWPNGRSDEARDRLGAPSVSPFSSKRITRRSSTAAGLSTYASPSDPAPSARAPAEWRRGAAGSSTVSAAGACGRFLPSPRSWQGNEKSFPSSSDHPSAYPALPHPAAPAYPEPGAQASNQFPRRRQSAFPSVKRLDYEEEHASSACLPTLLSPRFPHHPVSRPAGGVSPRSSQRQALAPTLAGMTFERRLSAGPLSSAPFSAPQERTTRLVGHRHALAADAERAEAPFSHAFRPGHHDRTPVGARRVPPRAETPGVSLDPGFRTGGPLDRGPVGSGGLEGQSFDFAHPTHASSEKKEAETEWSNPTAPVFYSPRSPRNDLPPGDGARSPYSAHLRPGVSEACSSFSVPPTERYEDDKNSHHAGSGGAFSPPTFGSPTPGPVPVGNERTFGRNPSPAATCASFSAKTGLRTPAPNGLAGDSGAFRSTNSLQRTPMSRRVSAPFGAGSAEGATAFGSRYASSGSFSKKFPQGSSSGVHEGGGAFGRRQEGDVSRVDAHGSVSPRSFSFLQRSDAPLSRGQPEGSHFQKHGETRASPDFARKGDSTQTHASGGRDFSQSGPFETQDFTFGEQPTRETRHMAPSPRGIERGGPQGSFVGHDTSFSVYAPRAGHAEGVESGCSAFEAPSESLSRRDGEADRENTVPNANGQMPVSGMPASKQTYGDDCDLYDNSAWTAQKHAPENFHAAVAPYPSSLLTGFAEGQQKAASRSSCLGGDR

[Multiple Choices]
A. 2.7.11.11
B. 1.14.13.238
C. 2.7.11.1
D. 4.2.99.18
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact 1598-aa sequence matches the UniProt entry for Toxoplasma gondii Nek1, which assigns EC 2.7.11.1 and annotates serine- and threonine-phosphorylation reactions with literature-linked evidence. This supports choice C, though the annotation is not an independent validation of the primary experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a protein-kinase-like catalytic domain, which supports a kinase interpretation over the oxidoreductase and lyase choices. It does not, from the supplied information alone, establish the specific kinase EC subclass.


**Missing item-specific fact**

> The protein's specific identity/function as Nek1 and its annotated catalytic activity, including the EC 2.7.11.1 classification.


**Reason**

> The broad sequence features support kinase activity, but selecting the complete EC number over another kinase option requires protein-specific functional annotation or experimental information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports EC 2.7.11.1; the supplied evidence does not support another listed option.


### Important caveats

- The UniProt annotation is literature-linked and curator asserted; the primary study was not independently retrieved or assessed here.
- Reviewer-only accession and annotation evidence support the key but were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase-like catalytic domain, which supports a kinase interpretation over the oxidoreductase and lyase choices. It does not, from the supplied information alone, establish the specific kinase EC subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific identity/function as Nek1 and its annotated catalytic activity, including the EC 2.7.11.1 classification.",
    "reason": "The broad sequence features support kinase activity, but selecting the complete EC number over another kinase option requires protein-specific functional annotation or experimental information absent from the question."
  },
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact 1598-aa sequence matches the UniProt entry for Toxoplasma gondii Nek1, which assigns EC 2.7.11.1 and annotates serine- and threonine-phosphorylation reactions with literature-linked evidence. This supports choice C, though the annotation is not an independent validation of the primary experiments."
  },
  "important_caveats": [
    "The UniProt annotation is literature-linked and curator asserted; the primary study was not independently retrieved or assessed here.",
    "Reviewer-only accession and annotation evidence support the key but were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports EC 2.7.11.1; the supplied evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 1598-aa sequence matches the UniProt entry for Toxoplasma gondii Nek1, which assigns EC 2.7.11.1 and annotates serine- and threonine-phosphorylation reactions with literature-linked evidence. This supports choice C, though the annotation is not an independent validation of the primary experiments.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a protein-kinase-like catalytic domain, which supports a kinase interpretation over the oxidoreductase and lyase choices. It does not, from the supplied information alone, establish the specific kinase EC subclass.",
    "missing_item_specific_fact": "The protein's specific identity/function as Nek1 and its annotated catalytic activity, including the EC 2.7.11.1 classification.",
    "reason": "The broad sequence features support kinase activity, but selecting the complete EC number over another kinase option requires protein-specific functional annotation or experimental information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports EC 2.7.11.1; the supplied evidence does not support another listed option."
  },
  "important_caveats": [
    "The UniProt annotation is literature-linked and curator asserted; the primary study was not independently retrieved or assessed here.",
    "Reviewer-only accession and annotation evidence support the key but were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry S8GI44 (sequence SHA256 match confirmed) is annotated as 'Serine/threonine-protein kinase Nek1' with EC 2.7.11.1, supported by experimental evidence from PubMed:23729737 (Chen & Gubbels, 2013, J. Cell Sci.). The catalytic activities listed are phosphorylation of L-seryl-&#91;protein&#93; and L-threonyl-&#91;protein&#93; using ATP, consistent with EC 2.7.11.1. The evidence code ECO:0000305 indicates curator inference from the cited publication, which performed mutagenesis and functional characterization of TgNek1.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase domain motifs: a glycine-rich loop (GAGRFGEV...KATKALL), the HRD catalytic motif (HRDLKPCNIFLASHPEY), the DFG activation segment (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the APE motif. These unambiguously identify the protein as a protein kinase (EC 2.7.11.x), eliminating option B (EC 1.14.13.238, a monooxygenase/oxidoreductase) and option D (EC 4.2.99.18, a lyase). To distinguish 2.7.11.1 (Ser/Thr kinase) from 2.7.11.11 (receptor-type tyrosine-protein kinase): EC 2.7.11.11 requires a transmembrane domain and extracellular ligand-binding domain, neither of which is present in this sequence (no long hydrophobic stretch; the protein is cytoplasmic). Additionally, the HRD motif pattern 'HRDLKPCNIFLASHPEY' is characteristic of Ser/Thr kinases rather than tyrosine kinases (which typically show 'HRDLAARN'). The long C-terminal S/T-rich tail is a hallmark of NIMA-related (Nek) Ser/Thr kinases.


**Missing item-specific fact**

> None critical. The kinase domain motifs, absence of transmembrane topology, and HRD motif pattern provide sufficient biological reasoning to select 2.7.11.1 over the alternatives.


**Reason**

> The sequence itself provides kinase domain signatures that eliminate B and D by class (oxidoreductase vs. lyase vs. transferase). The absence of any transmembrane or receptor extracellular domain eliminates 2.7.11.11 (receptor-type tyrosine kinase). The HRD motif sequence and overall domain architecture (kinase domain + long cytoplasmic tail) are consistent with a cytoplasmic Ser/Thr kinase, supporting 2.7.11.1.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are entirely different enzyme classes (oxidoreductase, lyase) and are eliminated by the clear kinase domain. Option A (2.7.11.11) is a receptor-type tyrosine kinase requiring a transmembrane domain absent from this sequence. Only option C (2.7.11.1) is consistent with a cytoplasmic Ser/Thr protein kinase bearing NIMA-family architecture.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (curator inference from published literature), not direct in vitro enzyme kinetics characterization of this specific protein.
- The PubMed:23729737 study characterized TgNek1 function in Toxoplasma cell division and performed mutagenesis of catalytic residues, supporting kinase activity assignment.
- EC 2.7.11.11 in current IUBMB nomenclature refers specifically to receptor-type tyrosine-protein kinase; if the question intended a non-receptor tyrosine kinase, the EC number would differ, but the sequence clearly lacks tyrosine kinase signatures.
- The NIMA-related kinase family is well-established as Ser/Thr kinases across eukaryotes, providing taxonomic and phylogenetic context for the classification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase domain motifs: a glycine-rich loop (GAGRFGEV...KATKALL), the HRD catalytic motif (HRDLKPCNIFLASHPEY), the DFG activation segment (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the APE motif. These unambiguously identify the protein as a protein kinase (EC 2.7.11.x), eliminating option B (EC 1.14.13.238, a monooxygenase/oxidoreductase) and option D (EC 4.2.99.18, a lyase). To distinguish 2.7.11.1 (Ser/Thr kinase) from 2.7.11.11 (receptor-type tyrosine-protein kinase): EC 2.7.11.11 requires a transmembrane domain and extracellular ligand-binding domain, neither of which is present in this sequence (no long hydrophobic stretch; the protein is cytoplasmic). Additionally, the HRD motif pattern 'HRDLKPCNIFLASHPEY' is characteristic of Ser/Thr kinases rather than tyrosine kinases (which typically show 'HRDLAARN'). The long C-terminal S/T-rich tail is a hallmark of NIMA-related (Nek) Ser/Thr kinases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The kinase domain motifs, absence of transmembrane topology, and HRD motif pattern provide sufficient biological reasoning to select 2.7.11.1 over the alternatives.",
    "reason": "The sequence itself provides kinase domain signatures that eliminate B and D by class (oxidoreductase vs. lyase vs. transferase). The absence of any transmembrane or receptor extracellular domain eliminates 2.7.11.11 (receptor-type tyrosine kinase). The HRD motif sequence and overall domain architecture (kinase domain + long cytoplasmic tail) are consistent with a cytoplasmic Ser/Thr kinase, supporting 2.7.11.1."
  },
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry S8GI44 (sequence SHA256 match confirmed) is annotated as 'Serine/threonine-protein kinase Nek1' with EC 2.7.11.1, supported by experimental evidence from PubMed:23729737 (Chen & Gubbels, 2013, J. Cell Sci.). The catalytic activities listed are phosphorylation of L-seryl-[protein] and L-threonyl-[protein] using ATP, consistent with EC 2.7.11.1. The evidence code ECO:0000305 indicates curator inference from the cited publication, which performed mutagenesis and functional characterization of TgNek1."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from published literature), not direct in vitro enzyme kinetics characterization of this specific protein.",
    "The PubMed:23729737 study characterized TgNek1 function in Toxoplasma cell division and performed mutagenesis of catalytic residues, supporting kinase activity assignment.",
    "EC 2.7.11.11 in current IUBMB nomenclature refers specifically to receptor-type tyrosine-protein kinase; if the question intended a non-receptor tyrosine kinase, the EC number would differ, but the sequence clearly lacks tyrosine kinase signatures.",
    "The NIMA-related kinase family is well-established as Ser/Thr kinases across eukaryotes, providing taxonomic and phylogenetic context for the classification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are entirely different enzyme classes (oxidoreductase, lyase) and are eliminated by the clear kinase domain. Option A (2.7.11.11) is a receptor-type tyrosine kinase requiring a transmembrane domain absent from this sequence. Only option C (2.7.11.1) is consistent with a cytoplasmic Ser/Thr protein kinase bearing NIMA-family architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry S8GI44 (sequence SHA256 match confirmed) is annotated as 'Serine/threonine-protein kinase Nek1' with EC 2.7.11.1, supported by experimental evidence from PubMed:23729737 (Chen & Gubbels, 2013, J. Cell Sci.). The catalytic activities listed are phosphorylation of L-seryl-[protein] and L-threonyl-[protein] using ATP, consistent with EC 2.7.11.1. The evidence code ECO:0000305 indicates curator inference from the cited publication, which performed mutagenesis and functional characterization of TgNek1.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase domain motifs: a glycine-rich loop (GAGRFGEV...KATKALL), the HRD catalytic motif (HRDLKPCNIFLASHPEY), the DFG activation segment (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the APE motif. These unambiguously identify the protein as a protein kinase (EC 2.7.11.x), eliminating option B (EC 1.14.13.238, a monooxygenase/oxidoreductase) and option D (EC 4.2.99.18, a lyase). To distinguish 2.7.11.1 (Ser/Thr kinase) from 2.7.11.11 (receptor-type tyrosine-protein kinase): EC 2.7.11.11 requires a transmembrane domain and extracellular ligand-binding domain, neither of which is present in this sequence (no long hydrophobic stretch; the protein is cytoplasmic). Additionally, the HRD motif pattern 'HRDLKPCNIFLASHPEY' is characteristic of Ser/Thr kinases rather than tyrosine kinases (which typically show 'HRDLAARN'). The long C-terminal S/T-rich tail is a hallmark of NIMA-related (Nek) Ser/Thr kinases.",
    "missing_item_specific_fact": "None critical. The kinase domain motifs, absence of transmembrane topology, and HRD motif pattern provide sufficient biological reasoning to select 2.7.11.1 over the alternatives.",
    "reason": "The sequence itself provides kinase domain signatures that eliminate B and D by class (oxidoreductase vs. lyase vs. transferase). The absence of any transmembrane or receptor extracellular domain eliminates 2.7.11.11 (receptor-type tyrosine kinase). The HRD motif sequence and overall domain architecture (kinase domain + long cytoplasmic tail) are consistent with a cytoplasmic Ser/Thr kinase, supporting 2.7.11.1."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are entirely different enzyme classes (oxidoreductase, lyase) and are eliminated by the clear kinase domain. Option A (2.7.11.11) is a receptor-type tyrosine kinase requiring a transmembrane domain absent from this sequence. Only option C (2.7.11.1) is consistent with a cytoplasmic Ser/Thr protein kinase bearing NIMA-family architecture."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from published literature), not direct in vitro enzyme kinetics characterization of this specific protein.",
    "The PubMed:23729737 study characterized TgNek1 function in Toxoplasma cell division and performed mutagenesis of catalytic residues, supporting kinase activity assignment.",
    "EC 2.7.11.11 in current IUBMB nomenclature refers specifically to receptor-type tyrosine-protein kinase; if the question intended a non-receptor tyrosine kinase, the EC number would differ, but the sequence clearly lacks tyrosine kinase signatures.",
    "The NIMA-related kinase family is well-established as Ser/Thr kinases across eukaryotes, providing taxonomic and phylogenetic context for the classification."
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

**Accession:** `S8GI44` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"NIMA-related protein kinase NIMA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein kinase Nek1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30865554","source":"PubMed"}],"value":"TgNek1"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"citation":{"authors":["Chen C.T.","Gubbels M.J."],"citationCrossReferences":[{"database":"PubMed","id":"23729737"},{"database":"DOI","id":"10.1242/jcs.123364"}],"citationType":"journal article","firstPage":"3344","id":"23729737","journal":"J. Cell Sci.","lastPage":"3355","publicationDate":"2013","title":"The Toxoplasma gondii centrosome is the platform for internal daughter budding as revealed by a Nek1 kinase mutant.","volume":"126"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","SUBCELLULAR LOCATION","ALTERNATIVE SPLICING","ISOFORM TGNEK1-1","ISOFORM TGNEK1-2","DEVELOPMENTAL STAGE","MUTAGENESIS OF LYS-135; SER-278; SER-282; THR-286 AND CYS-319"]}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
ID   NEK_TOXGM               Reviewed;        1598 AA.
AC   S8GI44;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-OCT-2013, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Serine/threonine-protein kinase Nek1 {ECO:0000305};
DE            Short=TgNek1 {ECO:0000303|PubMed:30865554};
DE            EC=2.7.11.1 {ECO:0000305|PubMed:23729737};
DE   AltName: Full=NIMA-related protein kinase NIMA1 {ECO:0000305};
GN   Name=NEK {ECO:0000312|EMBL:EPT28124.1};
GN   ORFNames=TGME49_292140 {ECO:0000312|EMBL:EPT28124.1};
OS   Toxoplasma gondii (strain ATCC 50611 / Me49).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;
OC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.
OX   NCBI_TaxID=508771 {ECO:0000312|Proteomes:UP000001529};
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein kinase Nek1 {ECO:0000305};
DE            Short=TgNek1 {ECO:0000303|PubMed:30865554};
DE            EC=2.7.11.1 {ECO:0000305|PubMed:23729737};
DE   AltName: Full=NIMA-related protein kinase NIMA1 {ECO:0000305};
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 43-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000305|PubMed:23729737};
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 49-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000305|PubMed:23729737};
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
