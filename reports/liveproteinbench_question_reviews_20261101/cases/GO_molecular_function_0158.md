# GO_molecular_function_0158

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — protein serine/threonine kinase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEQFGGPSGFMPPASYTAPLGKYPTKQPSAAYPSDGGRHATKENPRPAEGQASRQSSSVPSAMASKPIQDPEGHSAQPTSSYCRAQTPRSTPLPVALDEEARLSQYEVIRQIGAGRFGEVFIIRHKATKALLCWKLVFYKGLREKEKKQLVSEVNVMRELRHANIVRYHDRIVCRSRQCLYIVMEYCDAGDLAKQIEAAHKHHGGIDQDRIVLVVVQLIHALAYCHEGVGQERRRVLHRDLKPCNIFLASHPEYPDDSSRCIAKLGDFGLSRHLNMHSMAHSCVGTPYYWSPELLEDGQKTYNVKSDMWALGCVIYEMCTGKTPFAQAQTMPQLKERVRCGPVLPVPGFSDSLNALMASLLQPNPNNRPSALQCLGYTIFRGCSYTPPPLYRSSSAPSWTPRNASPARGSPSSAVSTVSTVTTSPGSSSRTSFSAPSSHDAAASSPASASASSRYQHQRSSSYSSDSAGPSGASAPSQKAPGPGRPPETPSRESFDLASKARPGFFAEAPPPHAFAEASPPESHASEFLPPANGAANEARNERTQRDRTRRAASATAAAAVSAFERQQREGRSMSPDPSAPLASIEEEEEGEGDDAGCGSLGSGSGVTRRMPGASLNREDRREAPGLRHADTHKRDDRDGAIWTGRREEAPFSRPGSELARDFGAASQNKVDTSRFSGASSGKPRPGNPQNEDRASFASDTSARQTVYLSGLSRRCSEPPAAFHSAVSPWDPAPPRLSSAASSSSSSRAVSPSSLRRASSREMKYPTDDRPAVAAGSSGVALARAERGPEPGAPWGNEETEGLHVHGRPSAAPASSFSSERTSRPGHPDEARESEHCFQGRGRFAEAEASPATEGKDPRDSGFEERSGRRDEGRTDGGEAQSFGYWPNGRSDEARDRLGAPSVSPFSSKRITRRSSTAAGLSTYASPSDPAPSARAPAEWRRGAAGSSTVSAAGACGRFLPSPRSWQGNEKSFPSSSDHPSAYPALPHPAAPAYPEPGAQASNQFPRRRQSAFPSVKRLDYEEEHASSACLPTLLSPRFPHHPVSRPAGGVSPRSSQRQALAPTLAGMTFERRLSAGPLSSAPFSAPQERTTRLVGHRHALAADAERAEAPFSHAFRPGHHDRTPVGARRVPPRAETPGVSLDPGFRTGGPLDRGPVGSGGLEGQSFDFAHPTHASSEKKEAETEWSNPTAPVFYSPRSPRNDLPPGDGARSPYSAHLRPGVSEACSSFSVPPTERYEDDKNSHHAGSGGAFSPPTFGSPTPGPVPVGNERTFGRNPSPAATCASFSAKTGLRTPAPNGLAGDSGAFRSTNSLQRTPMSRRVSAPFGAGSAEGATAFGSRYASSGSFSKKFPQGSSSGVHEGGGAFGRRQEGDVSRVDAHGSVSPRSFSFLQRSDAPLSRGQPEGSHFQKHGETRASPDFARKGDSTQTHASGGRDFSQSGPFETQDFTFGEQPTRETRHMAPSPRGIERGGPQGSFVGHDTSFSVYAPRAGHAEGVESGCSAFEAPSESLSRRDGEADRENTVPNANGQMPVSGMPASKQTYGDDCDLYDNSAWTAQKHAPENFHAAVAPYPSSLLTGFAEGQQKAASRSSCLGGDR

[Multiple Choices]
A. protein serine/threonine kinase activity
B. translation regulator activity
C. quercetin 7-O-glucosyltransferase activity
D. cardiolipin synthase (CMP-forming)
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

> The supplied sequence matches the 1,598-aa Toxoplasma gondii Nek1 record. UniProt describes it as a probable serine/threonine-protein kinase and records serine- and threonine-phosphorylation reactions; the function is linked to cited publications. This supports A, while retaining the annotation's “probable” qualification.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs such as the HRD catalytic motif and DFG motif. That strongly distinguishes kinase activity from the specific glucosyltransferase and cardiolipin-synthase alternatives; the serine/threonine kinase choice is also consistent with this domain.


**Missing item-specific fact**

> No additional protein-specific fact is necessary to distinguish the listed choices at this level. Experimental confirmation of this particular kinase's activity or substrates would be item-specific, but is not required for the sequence-based distinction here.


**Reason**

> The supplied sequence itself provides meaningful evidence for a kinase, rather than the answer depending solely on recognition of a database entry. The reviewer-only annotation supports the key but is not needed as input to that broad distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The recognizable kinase domain supports A over the chemically distinct enzyme alternatives. The sequence's long low-complexity regions do not undermine that catalytic-domain evidence.


### Important caveats

- The database function annotation is qualified as probable; its catalytic-activity annotation is curated with cited literature evidence, but those papers were not independently reviewed here.
- The sequence-based argument supports the listed kinase-function class, not specific substrates or all biological roles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs such as the HRD catalytic motif and DFG motif. That strongly distinguishes kinase activity from the specific glucosyltransferase and cardiolipin-synthase alternatives; the serine/threonine kinase choice is also consistent with this domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional protein-specific fact is necessary to distinguish the listed choices at this level. Experimental confirmation of this particular kinase's activity or substrates would be item-specific, but is not required for the sequence-based distinction here.",
    "reason": "The supplied sequence itself provides meaningful evidence for a kinase, rather than the answer depending solely on recognition of a database entry. The reviewer-only annotation supports the key but is not needed as input to that broad distinction."
  },
  "case_id": "GO_molecular_function_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 1,598-aa Toxoplasma gondii Nek1 record. UniProt describes it as a probable serine/threonine-protein kinase and records serine- and threonine-phosphorylation reactions; the function is linked to cited publications. This supports A, while retaining the annotation's “probable” qualification."
  },
  "important_caveats": [
    "The database function annotation is qualified as probable; its catalytic-activity annotation is curated with cited literature evidence, but those papers were not independently reviewed here.",
    "The sequence-based argument supports the listed kinase-function class, not specific substrates or all biological roles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The recognizable kinase domain supports A over the chemically distinct enzyme alternatives. The sequence's long low-complexity regions do not undermine that catalytic-domain evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 1,598-aa Toxoplasma gondii Nek1 record. UniProt describes it as a probable serine/threonine-protein kinase and records serine- and threonine-phosphorylation reactions; the function is linked to cited publications. This supports A, while retaining the annotation's “probable” qualification.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable protein kinase catalytic domain, including conserved kinase motifs such as the HRD catalytic motif and DFG motif. That strongly distinguishes kinase activity from the specific glucosyltransferase and cardiolipin-synthase alternatives; the serine/threonine kinase choice is also consistent with this domain.",
    "missing_item_specific_fact": "No additional protein-specific fact is necessary to distinguish the listed choices at this level. Experimental confirmation of this particular kinase's activity or substrates would be item-specific, but is not required for the sequence-based distinction here.",
    "reason": "The supplied sequence itself provides meaningful evidence for a kinase, rather than the answer depending solely on recognition of a database entry. The reviewer-only annotation supports the key but is not needed as input to that broad distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The recognizable kinase domain supports A over the chemically distinct enzyme alternatives. The sequence's long low-complexity regions do not undermine that catalytic-domain evidence."
  },
  "important_caveats": [
    "The database function annotation is qualified as probable; its catalytic-activity annotation is curated with cited literature evidence, but those papers were not independently reviewed here.",
    "The sequence-based argument supports the listed kinase-function class, not specific substrates or all biological roles."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry S8GI44 (TgNek1, Toxoplasma gondii Nek1 kinase) is annotated as a serine/threonine-protein kinase (EC 2.7.11.1) with experimental evidence (PubMed:23729737, PubMed:30865554). The GO annotation GO:0004674 'protein serine/threonine kinase activity' is assigned via IEA:UniProtKB-EC. Catalytic activity reactions for both serine and threonine phosphorylation are recorded. The sequence matches the benchmark input exactly (SHA256 confirmed in both current and historical snapshots).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C10](#evidence-c10), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H9](#evidence-h9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains unambiguous protein kinase catalytic domain architecture: a glycine-rich loop region (GAGRFGEVFIIRHKATKALLCWKLVFYKGL), the catalytic HRD motif (HRDLKPCNIFLASHPEY), the DFG motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the activation segment with APE-like closure. These are hallmark features of the protein kinase superfamily and directly support 'protein serine/threonine kinase activity.' The other options lack any structural basis: translation regulator activity requires ribosome/translation-factor interaction domains absent here; quercetin 7-O-glucosyltransferase is a plant-specific glycosyltransferase (PSPG-box architecture) incompatible with this sequence; cardiolipin synthase (CMP-forming) is a membrane-bound lipid-transfer enzyme with entirely different fold topology. The kinase motifs alone are sufficient to select A over B, C, and D.


**Missing item-specific fact**

> None required. The canonical kinase motifs (HRD, DFG, glycine-rich loop) are directly visible in the provided sequence and constitute a general biological argument for protein kinase activity.


**Reason**

> A biologist familiar with protein kinase domain architecture can identify the HRD catalytic motif, DFG motif, and glycine-rich loop directly from the sequence, providing a concrete structural argument for serine/threonine kinase activity. The distractors (translation factor, plant glycosyltransferase, lipid synthase) have completely incompatible domain architectures and can be eliminated by general knowledge of protein domain biology without item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular function categories (kinase, translation regulator, glycosyltransferase, lipid synthase). The presence of canonical protein kinase motifs in the sequence unambiguously supports option A and excludes B, C, and D. No other option has any structural or functional basis in this sequence.


### Important caveats

- The UniProt annotation uses 'Probable' qualifier for kinase activity, and the GO:0004674 annotation is IEA (Inferred from Electronic Annotation) via EC number transfer, not a direct experimental GO annotation. However, the underlying EC assignment is supported by curator inference from experimental papers (ECO:0000305|PubMed:23729737).
- The sequence is from Toxoplasma gondii, a protozoan parasite; option C (quercetin glucosyltransferase) is a plant-specific function, making it biologically implausible for this organism—a contextual clue beyond pure sequence analysis.
- The kinase domain is embedded within a large (1598 aa) protein with extensive low-complexity/phosphorylation regions typical of NEK-family kinases, but the catalytic core is clearly identifiable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains unambiguous protein kinase catalytic domain architecture: a glycine-rich loop region (GAGRFGEVFIIRHKATKALLCWKLVFYKGL), the catalytic HRD motif (HRDLKPCNIFLASHPEY), the DFG motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the activation segment with APE-like closure. These are hallmark features of the protein kinase superfamily and directly support 'protein serine/threonine kinase activity.' The other options lack any structural basis: translation regulator activity requires ribosome/translation-factor interaction domains absent here; quercetin 7-O-glucosyltransferase is a plant-specific glycosyltransferase (PSPG-box architecture) incompatible with this sequence; cardiolipin synthase (CMP-forming) is a membrane-bound lipid-transfer enzyme with entirely different fold topology. The kinase motifs alone are sufficient to select A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The canonical kinase motifs (HRD, DFG, glycine-rich loop) are directly visible in the provided sequence and constitute a general biological argument for protein kinase activity.",
    "reason": "A biologist familiar with protein kinase domain architecture can identify the HRD catalytic motif, DFG motif, and glycine-rich loop directly from the sequence, providing a concrete structural argument for serine/threonine kinase activity. The distractors (translation factor, plant glycosyltransferase, lipid synthase) have completely incompatible domain architectures and can be eliminated by general knowledge of protein domain biology without item-specific lookup."
  },
  "case_id": "GO_molecular_function_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C10",
      "H1",
      "H4",
      "H5",
      "H6",
      "H9",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry S8GI44 (TgNek1, Toxoplasma gondii Nek1 kinase) is annotated as a serine/threonine-protein kinase (EC 2.7.11.1) with experimental evidence (PubMed:23729737, PubMed:30865554). The GO annotation GO:0004674 'protein serine/threonine kinase activity' is assigned via IEA:UniProtKB-EC. Catalytic activity reactions for both serine and threonine phosphorylation are recorded. The sequence matches the benchmark input exactly (SHA256 confirmed in both current and historical snapshots)."
  },
  "important_caveats": [
    "The UniProt annotation uses 'Probable' qualifier for kinase activity, and the GO:0004674 annotation is IEA (Inferred from Electronic Annotation) via EC number transfer, not a direct experimental GO annotation. However, the underlying EC assignment is supported by curator inference from experimental papers (ECO:0000305|PubMed:23729737).",
    "The sequence is from Toxoplasma gondii, a protozoan parasite; option C (quercetin glucosyltransferase) is a plant-specific function, making it biologically implausible for this organism—a contextual clue beyond pure sequence analysis.",
    "The kinase domain is embedded within a large (1598 aa) protein with extensive low-complexity/phosphorylation regions typical of NEK-family kinases, but the catalytic core is clearly identifiable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function categories (kinase, translation regulator, glycosyltransferase, lipid synthase). The presence of canonical protein kinase motifs in the sequence unambiguously supports option A and excludes B, C, and D. No other option has any structural or functional basis in this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry S8GI44 (TgNek1, Toxoplasma gondii Nek1 kinase) is annotated as a serine/threonine-protein kinase (EC 2.7.11.1) with experimental evidence (PubMed:23729737, PubMed:30865554). The GO annotation GO:0004674 'protein serine/threonine kinase activity' is assigned via IEA:UniProtKB-EC. Catalytic activity reactions for both serine and threonine phosphorylation are recorded. The sequence matches the benchmark input exactly (SHA256 confirmed in both current and historical snapshots).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C10", "H1", "H4", "H5", "H6", "H9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains unambiguous protein kinase catalytic domain architecture: a glycine-rich loop region (GAGRFGEVFIIRHKATKALLCWKLVFYKGL), the catalytic HRD motif (HRDLKPCNIFLASHPEY), the DFG motif (DFGLSRHLNMHSMAHSCVGTPYYWSPEL), and the activation segment with APE-like closure. These are hallmark features of the protein kinase superfamily and directly support 'protein serine/threonine kinase activity.' The other options lack any structural basis: translation regulator activity requires ribosome/translation-factor interaction domains absent here; quercetin 7-O-glucosyltransferase is a plant-specific glycosyltransferase (PSPG-box architecture) incompatible with this sequence; cardiolipin synthase (CMP-forming) is a membrane-bound lipid-transfer enzyme with entirely different fold topology. The kinase motifs alone are sufficient to select A over B, C, and D.",
    "missing_item_specific_fact": "None required. The canonical kinase motifs (HRD, DFG, glycine-rich loop) are directly visible in the provided sequence and constitute a general biological argument for protein kinase activity.",
    "reason": "A biologist familiar with protein kinase domain architecture can identify the HRD catalytic motif, DFG motif, and glycine-rich loop directly from the sequence, providing a concrete structural argument for serine/threonine kinase activity. The distractors (translation factor, plant glycosyltransferase, lipid synthase) have completely incompatible domain architectures and can be eliminated by general knowledge of protein domain biology without item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular function categories (kinase, translation regulator, glycosyltransferase, lipid synthase). The presence of canonical protein kinase motifs in the sequence unambiguously supports option A and excludes B, C, and D. No other option has any structural or functional basis in this sequence."
  },
  "important_caveats": [
    "The UniProt annotation uses 'Probable' qualifier for kinase activity, and the GO:0004674 annotation is IEA (Inferred from Electronic Annotation) via EC number transfer, not a direct experimental GO annotation. However, the underlying EC assignment is supported by curator inference from experimental papers (ECO:0000305|PubMed:23729737).",
    "The sequence is from Toxoplasma gondii, a protozoan parasite; option C (quercetin glucosyltransferase) is a plant-specific function, making it biologically implausible for this organism—a contextual clue beyond pure sequence analysis.",
    "The kinase domain is embedded within a large (1598 aa) protein with extensive low-complexity/phosphorylation regions typical of NEK-family kinases, but the catalytic core is clearly identifiable."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
"S8GI44"
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23729737","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30865554","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"value":"Probable serine/threonine-protein kinase (Probable). Involved in controlling centrosome splitting (PubMed:23729737). Promotes separation of the centrosome outer cores (PubMed:30865554)"}]}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000305","id":"23729737","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `4b5822ee1f6499622b11503feef2e697e56747663823cb38bef569dafff9bad6`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/S8GI44.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:59.328831+00:00.  

```json
{"database":"GO","id":"GO:0004674","properties":[{"key":"GoTerm","value":"F:protein serine/threonine kinase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 38-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
CC   -!- FUNCTION: Probable serine/threonine-protein kinase (Probable). Involved
CC       in controlling centrosome splitting (PubMed:23729737). Promotes
CC       separation of the centrosome outer cores (PubMed:30865554).
CC       {ECO:0000269|PubMed:23729737, ECO:0000269|PubMed:30865554,
CC       ECO:0000305|PubMed:23729737}.
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

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/S8GI44?format=txt&versions=38)  
**Locator:** `lines 104-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:34:03.906590+00:00.  

```text
DR   GO; GO:0004674; F:protein serine/threonine kinase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `324a63b3f3f2268eff7cb13606084915dd80f645516a1c6d849025251ebde12f`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 46709-47278`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004674
name: protein serine/threonine kinase activity
namespace: molecular_function
alt_id: GO:0004695
alt_id: GO:0004696
alt_id: GO:0004700
alt_id: GO:0106311
def: "Catalysis of the reactions: ATP + protein serine = ADP + protein serine phosphate, and ATP + protein threonine = ADP + protein threonine phosphate." [EC:2.7.11.-, GOC:bf, PMID:2956925]
synonym: "protein serine kinase activity" NARROW [EC:2.7.11.1]
synonym: "protein serine-threonine kinase activity" RELATED [EC:2.7.11.1]
synonym: "protein threonine kinase activity" NARROW []
synonym: "protein-serine kinase activity" NARROW [EC:2.7.11.1]
synonym: "serine kinase activity" NARROW [EC:2.7.11.1]
synonym: "serine protein kinase activity" NARROW [EC:2.7.11.1]
synonym: "serine(threonine) protein kinase activity" RELATED [EC:2.7.11.1]
synonym: "serine-specific protein kinase activity" NARROW [EC:2.7.11.1]
synonym: "serine/threonine protein kinase activity" RELATED [EC:2.7.11.1]
synonym: "threonine-specific protein kinase activity" NARROW [EC:2.7.11.1]
xref: EC:2.7.11.-
xref: EC:2.7.11.1
xref: EC:2.7.11.28
xref: EC:2.7.11.29
xref: EC:2.7.11.3
xref: EC:2.7.11.9
xref: MetaCyc:PROTEIN-KINASE-RXN
xref: Reactome:R-HSA-109702 "PDPK1 phosphorylates AKT2"
xref: Reactome:R-HSA-109822 "MAPK3,(MAPK1) phosphorylates GRB2-1:SOS1:p-Y427-SHC1"
xref: Reactome:R-HSA-109823 "MAPK3,(MAPK1) phosphorylates GRB2-1:SOS1:p-Y-IRS1,p-Y-IRS2"
xref: Reactome:R-HSA-109860 "MAP2K1 phosphorylates MAPK3"
xref: Reactome:R-HSA-109862 "MAP2K2 phosphorylates MAPK1"
xref: Reactome:R-HSA-111919 "PKA phosphorylates CREB1"
xref: Reactome:R-HSA-111970 "PKC phosphorylates GRK2"
xref: Reactome:R-HSA-112342 "Inactivation of MAP2K1 by CDK1"
xref: Reactome:R-HSA-112381 "Hyperphosphorylation (Ser2) of RNA Pol II CTD by P-TEFb complex"
xref: Reactome:R-HSA-1168635 "PRKCB (PKC-beta) phosphorylates CARMA1"
xref: Reactome:R-HSA-1168638 "Activated IKK phosphorylates I-kappaB"
xref: Reactome:R-HSA-1168641 "TAK1 associated with the CBM complex phosphorylates IKKbeta"
xref: Reactome:R-HSA-1181149 "ACVR2A,B (ActRIIA,B) phosphorylates ACVR1B (ActRIB, ALK4) in response to Activin"
xref: Reactome:R-HSA-1181156 "Type II Activin Receptor (ActRII/ACVR2) phosphorylates Type I Activin Receptor (ActRIB/ACVR1B) in response to NODAL"
xref: Reactome:R-HSA-1181355 "Phosphorylation of R-SMAD2/3 by NODAL receptor"
xref: Reactome:R-HSA-1225894 "Type II Activin Receptor (ActRIIB/ACVR2B) phosphorylates Type I Activin Receptor (ActRIC/ACVR1C) in response to NODAL"
xref: Reactome:R-HSA-1358791 "Phosphorylation of USP8 by P-AKT"
xref: Reactome:R-HSA-1362270 "Phosphorylation of LIN52 component of MuvB by DYRK1A"
xref: Reactome:R-HSA-139908 "Phosphorylation of DLC2 by MAPK8"
xref: Reactome:R-HSA-139918 "Phosphorylation of BIM by JNK"
xref: Reactome:R-HSA-1445144 "p-AKT1,p-AKT2 phosphorylates AS160 (TBC1D4)"
xref: Reactome:R-HSA-1449597 "p-AKT2 phosphorylates Myosin 5A"
xref: Reactome:R-HSA-1454699 "AMPK-alpha2 phosphorylates TBC1D1"
xref: Reactome:R-HSA-1458463 "p-AKT2 phosphorylates RGC2"
xref: Reactome:R-HSA-1549526 "Phosphorylation of SMAD2,3 by Activin:Activin Receptor"
xref: Reactome:R-HSA-156673 "Regulation of KIF23 (MKLP1) by phosphorylation"
xref: Reactome:R-HSA-156678 "Activation of Cdc25C"
xref: Reactome:R-HSA-156682 "PLK1 phosphorylates NUDC"
xref: Reactome:R-HSA-156699 "Inactivation of Wee1 kinase"
xref: Reactome:R-HSA-156723 "Regulation of KIF20A (MKL2) by phosphorylation"
xref: Reactome:R-HSA-1592233 "p38 MAPK phosphorylates PPARGC1A"
xref: Reactome:R-HSA-162363 "p-T309,S474-AKT2:PIP3 phosphorylates PDE3B"
xref: Reactome:R-HSA-162657 "Inactivation of Myt1 kinase"
xref: Reactome:R-HSA-163010 "Down Regulation of Emi1 through Phosphorylation of Emi1"
xref: Reactome:R-HSA-1632857 "ULK1 phosphorylates AMBRA1:BECN1 complex"
xref: Reactome:R-HSA-163416 "hormone-sensitive lipase (HSL) + 2 ATP -> phosphorylated HSL + 2 ADP"
xref: Reactome:R-HSA-163418 "perilipin + 2 ATP -> phosphorylated perilipin + 2 ADP"
xref: Reactome:R-HSA-1638803 "Phosphorylation of cohesin by PLK1 at centromeres"
xref: Reactome:R-HSA-164151 "LKB1 phosphorylates the alpha subunit of AMPK heterotrimer"
xref: Reactome:R-HSA-165162 "Phosphorylation of TSC2 by PKB"
xref: Reactome:R-HSA-165182 "Phosphorylation of complexed TSC2 by PKB"
xref: Reactome:R-HSA-165692 "Phosphorylation of 4E-BP1 by activated mTORC1"
xref: Reactome:R-HSA-165718 "mTORC1 phosphorylation of RPS6KB1 (S6K)"
xref: Reactome:R-HSA-165726 "Phosphorylation of Ribosomal protein S6 by activated S6K1"
xref: Reactome:R-HSA-165758 "Phosphorylation and inactivation of eEF2K by activated S6K1"
xref: Reactome:R-HSA-165766 "Phosphorylation and activation of eIF4G by activated S6K1"
xref: Reactome:R-HSA-165777 "Phosphorylation and activation of eIF4B by activated S6K1"
xref: Reactome:R-HSA-166119 "First phosphorylation of IRAK1 by IRAK4 bound to activated TLR:MyD88:Mal"
xref: Reactome:R-HSA-166245 "Phosphorylation of IRF-3/IRF7 and their release from the activated TLR complex"
xref: Reactome:R-HSA-166284 "Second phosphorylation of IRAK1 by IRAK4 bound to activated TLR:MyD88:TIRAP"
xref: Reactome:R-HSA-166286 "Multiple IRAK1 autophosphorylation steps"
xref: Reactome:R-HSA-167084 "Hyperphosphorylation (Ser2) of RNA Pol II CTD by P-TEFb complex"
xref: Reactome:R-HSA-167098 "Phosphorylation (Ser5) of RNA pol II CTD"
xref: Reactome:R-HSA-168053 "Phosphorylated MAPKs phosphorylate ATF-2"
xref: Reactome:R-HSA-168140 "Active IKK Complex phosphorylates NF-kappa-B inhibitor"
xref: Reactome:R-HSA-168184 "Activated TAK1 mediates phosphorylation of the IKK Complex"
xref: Reactome:R-HSA-170055 "Myt-1 mediated phosphorylation of Cyclin B:Cdc2 complexes"
xref: Reactome:R-HSA-170076 "CAK phosphorylates CDK1 bound to CCNB1"
xref: Reactome:R-HSA-170087 "CAK phosphorylates CDK1 bound to CCNA"
xref: Reactome:R-HSA-170116 "PKMYT1 phosphorylates CCNA:CDK1"
xref: Reactome:R-HSA-170126 "Phosphorylation of Cyclin B1 in the CRS domain"
xref: Reactome:R-HSA-170977 "FRS2 is phosphorylated by active TrkA receptor"
xref: Reactome:R-HSA-174119 "Free APC/C phosphorylated by Plk1"
xref: Reactome:R-HSA-174174 "Phosphorylation of the Emi1 DSGxxS degron by Plk1"
xref: Reactome:R-HSA-176116 "Recruitment and activation of Chk1"
xref: Reactome:R-HSA-176298 "Activation of claspin"
xref: Reactome:R-HSA-187688 "p38 MAPK phosphorylates MAPKAPK2, MAPKAPK3"
xref: Reactome:R-HSA-187949 "CAK-mediated phosphorylation of Cyclin A:Cdk2"
xref: Reactome:R-HSA-188350 "CAK-mediated phosphorylation of Cyclin E:Cdk2"
xref: Reactome:R-HSA-193647 "IRAK is activated"
xref: Reactome:R-HSA-193703 "IKKbeta is activated"
xref: Reactome:R-HSA-193705 "IKKbeta phosphorylates IkB causing NF-kB to dissociate"
xref: Reactome:R-HSA-195275 "Phosphorylation of APC component of the destruction complex"
xref: Reactome:R-HSA-195283 "Phosphorylation of phospho- (Ser45, Thr41) beta-catenin  at Ser37 by GSK-3"
xref: Reactome:R-HSA-195287 "Phosphorylation of phospho-(Ser45 ) at Thr 41 by GSK-3"
xref: Reactome:R-HSA-195300 "Phosphorylation of phospho-(Ser45,Thr41,Ser37) at Ser33 by GSK-3"
xref: Reactome:R-HSA-195318 "Phosphorylation of beta-catenin at Ser45 by CK1 alpha"
xref: Reactome:R-HSA-198270 "PDPK1 phosphorylates AKT at T308"
xref: Reactome:R-HSA-198347 "AKT phosphorylates BAD"
xref: Reactome:R-HSA-198371 "AKT phosphorylates GSK3"
xref: Reactome:R-HSA-198599 "AKT phosphorylates MDM2"
xref: Reactome:R-HSA-198609 "AKT phosphorylates TSC2, inhibiting it"
xref: Reactome:R-HSA-198611 "AKT phosphorylates IKKalpha"
xref: Reactome:R-HSA-198613 "AKT phosphorylates p21Cip1 and p27Kip1"
xref: Reactome:R-HSA-198621 "AKT phosphorylates caspase-9"
xref: Reactome:R-HSA-198640 "TORC2 (mTOR) phosphorylates AKT at S473"
xref: Reactome:R-HSA-198669 "p38MAPK phosphorylates MSK1"
xref: Reactome:R-HSA-198731 "ERK1/2 activates ELK1"
xref: Reactome:R-HSA-198746 "ERK1/2/5 activate RSK1/2/3"
xref: Reactome:R-HSA-198756 "ERK1/2 phosphorylates MSK1"
xref: Reactome:R-HSA-199298 "AKT phosphorylates CREB1"
xref: Reactome:R-HSA-199299 "AKT phosphorylates FOXO transcription factors"
xref: Reactome:R-HSA-199839 "AKT can phosphorylate RSK"
xref: Reactome:R-HSA-199863 "AKT can phosphorylate NR4A1 (NUR77)"
xref: Reactome:R-HSA-199895 "RSK1/2/3 phosphorylates CREB at Serine 119"
xref: Reactome:R-HSA-199910 "MSK1 activates ATF1"
xref: Reactome:R-HSA-199917 "MAPKAPK2 phosphorylates CREB at Serine 133"
xref: Reactome:R-HSA-199929 "ERK5 activates the transcription factor MEF2"
xref: Reactome:R-HSA-199935 "MSK1 activates CREB"
xref: Reactome:R-HSA-200143 "AKT phosphorylates AKT1S1 (PRAS40)"
xref: Reactome:R-HSA-200421 "Activation of cytosolic AMPK by phosphorylation"
xref: Reactome:R-HSA-201677 "Phosphorylation of LRP5/6 cytoplasmic domain by membrane-associated GSK3beta"
xref: Reactome:R-HSA-201691 "Phosphorylation of LRP5/6 cytoplasmic domain by CSNKI"
xref: Reactome:R-HSA-201717 "CSNK2-mediated phosphorylation of DVL"
xref: Reactome:R-HSA-202111 "AKT1 phosphorylates eNOS"
xref: Reactome:R-HSA-202222 "Phosphorylation of PKC theta"
xref: Reactome:R-HSA-202437 "Phosphorylation of CARMA1"
xref: Reactome:R-HSA-202459 "Phosphorylation of Bcl10"
xref: Reactome:R-HSA-202500 "Activation of IKK complex"
xref: Reactome:R-HSA-202510 "Activation of TAK1-TAB2 complex"
xref: Reactome:R-HSA-202541 "p-S177,S181-IKKB:IKKA:pUb-NEMO phosphorylates IkB-alpha:NF-kB"
xref: Reactome:R-HSA-2028284 "Phosphorylation of STK4 (MST1) and SAV1 by STK4"
xref: Reactome:R-HSA-2028555 "Phosphorylation of LATS1 and 2 by p-STK4 (p-MST1)"
xref: Reactome:R-HSA-2028583 "Phosphorylation of YAP by LATS2"
xref: Reactome:R-HSA-2028589 "Phosphorylation of LATS1 and 2 by p-STK3 (p-MST2)"
xref: Reactome:R-HSA-2028591 "Phosphorylation of STK3 (MST2) and SAV1 by STK3"
xref: Reactome:R-HSA-2028598 "Phosphorylation of YAP by LATS1"
xref: Reactome:R-HSA-2028629 "Phosphorylation of MOB1A and B by p-STK4 (p-MST1)"
xref: Reactome:R-HSA-2028635 "Phosphorylation of MOB1A and B by p-STK3 (p-MST2)"
xref: Reactome:R-HSA-2028661 "Phosphorylation of WWTR1 (TAZ) by LATS2"
xref: Reactome:R-HSA-2028670 "Phosphorylation of MOB1A and B by p-STK4(MST1)/N"
xref: Reactome:R-HSA-2028673 "Phosphorylation of LATS1 and 2 by p-STK3 (MST2)/N"
xref: Reactome:R-HSA-2028675 "Phosphorylation of MOB1A and B by p-STK3(MST2)/N"
xref: Reactome:R-HSA-2028679 "Phosphorylation of LATS1 and 2 by p-STK4(MST1)/N"
xref: Reactome:R-HSA-2029454 "Autophosphorylation of PAK1"
xref: Reactome:R-HSA-2029460 "PAK1 phosphorylates LIMK1"
xref: Reactome:R-HSA-2029469 "p-ERK phosphorylates WAVEs and ABI"
xref: Reactome:R-HSA-2060328 "Phosphorylation of WWTR1 (TAZ) by LATS1"
xref: Reactome:R-HSA-209087 "IKBA is phosphorylated by Phospho IKKB kinase"
xref: Reactome:R-HSA-211164 "AKT phosphorylates FOXO1A"
xref: Reactome:R-HSA-211583 "Partial autophosphorylation of PAK-2 at  Ser-19, Ser-20, Ser-55, Ser-192, and Ser-197"
xref: Reactome:R-HSA-211650 "Autophosphorylation of PAK-2p34 in the activation loop"
xref: Reactome:R-HSA-2168079 "MASTL (GWL) phosphorylates ARPP19"
xref: Reactome:R-HSA-2176475 "Phosphorylation of SMAD2 and SMAD3 linker regions by CDK8 or CDK9"
xref: Reactome:R-HSA-2214351 "PLK1 phosphorylates GORASP1"
xref: Reactome:R-HSA-2243938 "AKT1 E17K mutant is phosphorylated by TORC2 complex"
xref: Reactome:R-HSA-2243942 "PDPK1 phosphorylates AKT1 E17K mutant"
xref: Reactome:R-HSA-2294580 "PLK1 hyperphosphorylates Condensin II complex"
xref: Reactome:R-HSA-2396007 "IRF3 is phosphorylated by TBK1"
xref: Reactome:R-HSA-2399941 "AKT1 E17K mutant phosphorylates BAD"
xref: Reactome:R-HSA-2399966 "AKT1 E17K mutant phosphorylates GSK3"
xref: Reactome:R-HSA-2399969 "AKT1 E17K mutant phosphorylates p21Cip1 and p27Kip1"
xref: Reactome:R-HSA-2399977 "AKT1 E17K mutant phosphorylates AKT1S1 (PRAS40)"
xref: Reactome:R-HSA-2399981 "AKT1 E17K mutant phosphorylates MDM2"
xref: Reactome:R-HSA-2399982 "AKT1 E17K mutant phosphorylates TSC2, inhibiting it"
xref: Reactome:R-HSA-2399985 "AKT1 E17K mutant phosphorylates caspase-9"
xref: Reactome:R-HSA-2399988 "AKT1 E17K mutant phosphorylates NR4A1 (NUR77)"
xref: Reactome:R-HSA-2399992 "AKT1 E17K mutant phosphorylates forkhead box transcription factors"
xref: Reactome:R-HSA-2399996 "AKT1 E17K mutant phosphorylates CREB1"
xref: Reactome:R-HSA-2399999 "AKT1 E17K mutant phosphorylates RSK"
xref: Reactome:R-HSA-2400001 "AKT1 E17K mutant phosphorylates CHUK (IKKalpha)"
xref: Reactome:R-HSA-2422927 "MAPK3-3 or MAPK1 phosphorylate GORASP2"
xref: Reactome:R-HSA-2430535 "MASTL phosphorylates ENSA"
xref: Reactome:R-HSA-2466068 "Phosphorylation of cohesin by PLK1 at chromosomal arms"
xref: Reactome:R-HSA-2470508 "ACVR2A,B (ActRIIA,B) phosphorylates ACVR1C (ActRIC, ALK7) in response to Activin"
xref: Reactome:R-HSA-2529020 "CK2 phosphorylates condensin I subunits"
xref: Reactome:R-HSA-2562526 "PLK1 phosphorylates OPTN"
xref: Reactome:R-HSA-2574840 "AJUBA facilitates AURKA autophosphorylation"
xref: Reactome:R-HSA-2730856 "Autophosphorylation of PAK"
xref: Reactome:R-HSA-2730868 "Phosphorylation of MEK7 by MEKK1"
xref: Reactome:R-HSA-2730876 "Phosphorylation of IKK-beta by TAK1"
xref: Reactome:R-HSA-2730896 "Phosphorylation of MEK4 by MEKK1"
xref: Reactome:R-HSA-2730900 "Activation of TAK1 complex bound to pUb-TRAF6"
xref: Reactome:R-HSA-2984226 "PLK1 phosphorylates NEK9"
xref: Reactome:R-HSA-2984258 "NEK9 phosphorylates NEK6/NEK7"
xref: Reactome:R-HSA-2990880 "NEK6/NEK7 phosphorylates NUP98"
xref: Reactome:R-HSA-2993898 "VRK1/VRK2 phosphorylate BANF1"
xref: Reactome:R-HSA-3000310 "AURKA phosphorylates PLK1"
xref: Reactome:R-HSA-3000327 "PLK1 phosphorylates BORA"
xref: Reactome:R-HSA-3132737 "MAPKs phosphorylate ETS1 and ETS2"
xref: Reactome:R-HSA-3209160 "Activated ERKs phosphorylate ERF"
xref: Reactome:R-HSA-3222006 "STK11 (LKB1) phosphorylates NUAK1"
xref: Reactome:R-HSA-3222020 "NUAK1 phosphorylates TP53"
xref: Reactome:R-HSA-3228469 "MAP3K5 phosphorylates MKK3 and MKK6"
xref: Reactome:R-HSA-3229102 "p-MAPKAPK3 phosphorylates BMI1"
xref: Reactome:R-HSA-3229152 "MAP3K5 (ASK1) phosphorylates MAP2K4 (SEK1)"
xref: Reactome:R-HSA-3239014 "MAPKAPK5 phosphorylates TP53"
xref: Reactome:R-HSA-3239019 "Active p38 MAPK phosphorylates MAPKAPK5"
xref: Reactome:R-HSA-3249371 "TBK1 phosphorylates STAT6 at Ser407"
xref: Reactome:R-HSA-3371435 "Constitutive phosphorylation by GSK3"
xref: Reactome:R-HSA-3371531 "Constitutive phosphorylation  by pERK1/2"
xref: Reactome:R-HSA-3371567 "DBC1 is phosphorylated by ATM/ART"
xref: Reactome:R-HSA-349426 "Phosphorylation of MDM4 by CHEK2"
xref: Reactome:R-HSA-349444 "Phosphorylation of COP1 at Ser-387  by ATM"
xref: Reactome:R-HSA-349455 "Phosphorylation of MDM4 by ATM"
xref: Reactome:R-HSA-374696 "Phosphorylation of L1 by p90rsk"
xref: Reactome:R-HSA-3769394 "AKT phosphorylates CBY1"
xref: Reactome:R-HSA-377186 "Activated Akt1 phosphorylates AKT1S1 (PRAS40)"
xref: Reactome:R-HSA-3772435 "WNT signaling stimulates CSNK1-dependent phosphorylation of DVL"
xref: Reactome:R-HSA-380272 "Plk1-mediated phosphorylation of Nlp"
xref: Reactome:R-HSA-381091 "IRE1 dimer autophosphorylates"
xref: Reactome:R-HSA-381111 "EIF2AK3 (PERK) phosphorylates EIF2S1 (eIF2-alpha)Phosphorylation of eIF2-alpha by PERK"
xref: Reactome:R-HSA-3857328 "RPS6KA1/2/3 phosphorylates CEBPB on S321"
xref: Reactome:R-HSA-3857329 "MAPK3 (ERK1) and MAPK1 (ERK2) phosphorylate CEBPB"
xref: Reactome:R-HSA-3858480 "WNT-dependent phosphorylation of DVL"
xref: Reactome:R-HSA-389756 "AKT interacts and phosphorylates Cot"
xref: Reactome:R-HSA-392752 "Phosphorylation of L1 by CK-II"
xref: Reactome:R-HSA-3928577 "ROCK phosphorylates LIMK1,2"
xref: Reactome:R-HSA-3928608 "LIMK phosphorylates CFL1, inactivating it"
xref: Reactome:R-HSA-3928616 "Activated ROCK phosphorylates MRLCs"
xref: Reactome:R-HSA-3928620 "PAK1 autophosphorylates"
xref: Reactome:R-HSA-3928625 "PAKs autophosphorylate"
xref: Reactome:R-HSA-3928640 "PAKs phosphorylate MLC"
xref: Reactome:R-HSA-399939 "Autophosphorylation of PAK"
xref: Reactome:R-HSA-399944 "Phosphorylation of CRMPs by Cdk5"
xref: Reactome:R-HSA-399950 "Phosphorylation of cofilin by LIMK-1"
xref: Reactome:R-HSA-399951 "Phosphorylation of CRMPs by GSK3beta"
xref: Reactome:R-HSA-399952 "Phosphorylation of LIMK-1 by PAK"
xref: Reactome:R-HSA-399978 "Protein kinase C, alpha type phosphorylates MARCKS"
xref: Reactome:R-HSA-4088134 "PLK1 phosphorylates FOXM1"
xref: Reactome:R-HSA-419083 "Myosin phosphatase inactivation by ROCK"
xref: Reactome:R-HSA-419087 "LIM kinase phosphorylation by ROCK"
xref: Reactome:R-HSA-419197 "Myosin regulatory light chain phosphorylation by ROCK"
xref: Reactome:R-HSA-419644 "Transphosphorylation of pLIMK1"
xref: Reactome:R-HSA-428961 "Phosphorylation of cPLA2 by MAPK p38 alpha"
xref: Reactome:R-HSA-429016 "ALOX5 is phosphorylated by MAPKAP2"
xref: Reactome:R-HSA-429714 "CSNK1G2 phosphorylates p-CERT1-2"
xref: Reactome:R-HSA-432110 "Integrin alpha IIb beta3 T779 phosphorylation blocks SHC binding"
xref: Reactome:R-HSA-4332358 "Dissociation of CaM and CAMK2 autophosphorylation"
xref: Reactome:R-HSA-4332363 "Autophosphorylation and activation of CAMK2"
xref: Reactome:R-HSA-4332388 "Activation of MAP3K7 in response to WNT"
xref: Reactome:R-HSA-4411383 "NLK phosphorylates TCF/LEF"
xref: Reactome:R-HSA-4411402 "Activation of NLK"
xref: Reactome:R-HSA-442724 "Phosphorylation of CREB1 by ribosomal protein S6 kinases (RSKs)"
xref: Reactome:R-HSA-442739 "PDPK1 phosphorylates RSKs"
xref: Reactome:R-HSA-442832 "PAK phosphorylates cortactin"
xref: Reactome:R-HSA-445072 "Interaction of PAK1 with Rac1-GTP"
xref: Reactome:R-HSA-446694 "IRAK4 phosphorylates IRAK1"
xref: Reactome:R-HSA-446701 "IRAK4-activated IRAK1 autophosphorylates"
xref: Reactome:R-HSA-448948 "Phosphorylation of E proteins by p38 MAPK"
xref: Reactome:R-HSA-448955 "Phosphorylation of MEF2 proteins by p38"
xref: Reactome:R-HSA-450222 "Active p38 MAPK phosphorylates MAPKAPK2 or 3"
xref: Reactome:R-HSA-450325 "c-FOS activation by phospho ERK1/2"
xref: Reactome:R-HSA-450337 "Activated TAK1 phosphorylates MKK4/MKK7"
xref: Reactome:R-HSA-450346 "activated human TAK1 phosphorylates MKK3/MKK6"
xref: Reactome:R-HSA-450463 "MK2 phosphorylates ZFP36 (Tristetraproline, TTP)"
xref: Reactome:R-HSA-450474 "MK2 phosphorylates BRF1"
xref: Reactome:R-HSA-450490 "Protein Kinase B/Akt phosphorylates BRF1"
xref: Reactome:R-HSA-450499 "Protein Kinase B (AKT) phosphorylates KSRP"
xref: Reactome:R-HSA-450827 "hp-IRAK1, hp-IRAK4 4 phosphorylate Pellino-1 and 2"
xref: Reactome:R-HSA-451152 "MAP kinase p38 phosphorylates KSRP"
xref: Reactome:R-HSA-4551570 "VANGL2 is phosphorylated in response to WNT5A"
xref: Reactome:R-HSA-4608825 "DVL2 is phosphorylated after WNT5A binding to FZD"
xref: Reactome:R-HSA-4793911 "MAPKAPK2 phosphorylates HSF1"
xref: Reactome:R-HSA-5082387 "Phosphorylation of HSF1 at Ser230 induces transactivation"
xref: Reactome:R-HSA-5082405 "Phosphorylation of HSF1 at Ser326 induces transactivation"
xref: Reactome:R-HSA-5213464 "RIPK1 is phosphorylated"
xref: Reactome:R-HSA-5213466 "RIPK3 is phosphorylated"
xref: Reactome:R-HSA-5218814 "PAK2 autophorylates"
xref: Reactome:R-HSA-5218821 "PDK1 phosphorylates PKC"
xref: Reactome:R-HSA-5218826 "Active ROCK1,ROCK2 phosphorylates p-5Y-PTK2 on S732"
xref: Reactome:R-HSA-5218854 "p-Y420-FYN is phosphorylated on S21"
xref: Reactome:R-HSA-5218906 "RIPK3 phosphorylates MLKL"
xref: Reactome:R-HSA-5218916 "p-MAPK2/3 phosphorylates HSP27"
xref: Reactome:R-HSA-5228811 "NFKBIA variant is not phosphorylated within IkBA:NF-kappaB"
xref: Reactome:R-HSA-5229343 "AXIN is phosphorylated in the destruction complex"
xref: Reactome:R-HSA-5260201 "p-AKT2 phosphorylates C2CD5"
xref: Reactome:R-HSA-5357472 "PAK1-3 autophosphorylates"
xref: Reactome:R-HSA-5357477 "PAK1-3 phosphorylates VE-cadherin"
xref: Reactome:R-HSA-5357831 "CHUK, IKBKB phosphorylate CYLD at S418"
xref: Reactome:R-HSA-5578777 "DMPK phosphorylates PLN"
xref: Reactome:R-HSA-5607722 "Active NIK phosphorylates IKKA dimer"
xref: Reactome:R-HSA-5607726 "Active NIK:p-S176,180-IKKA dimer phosphorylates p100:RELB"
xref: Reactome:R-HSA-5607732 "K63polyUb-TAK1 autophosphorylates"
xref: Reactome:R-HSA-5607742 "K63polyUb-p-3T,1S-TAK1 phosphorylates IKK-beta"
xref: Reactome:R-HSA-5610718 "CK1 phosphorylates p-GLI2"
xref: Reactome:R-HSA-5610722 "CK1 phosphorylates p-GLI3"
xref: Reactome:R-HSA-5610730 "GSK3 phosphorylates p-GLI2"
xref: Reactome:R-HSA-5610732 "GSK3 phosphorylates p-GLI3"
xref: Reactome:R-HSA-5623667 "PDPK1 phosphorylates PKN1,2,3"
xref: Reactome:R-HSA-5624473 "Protein kinase A (PKA) and RPS6KA5 (MSK1) phosphorylates p65 (RELA) subunit"
xref: Reactome:R-HSA-5624492 "PAK phosphorylates p21 RAF1 on S338"
xref: Reactome:R-HSA-5625784 "PKN1 phosphorylates histone 3 of nucleosomes associate with KLK2 and KLK3 promoters"
xref: Reactome:R-HSA-5627775 "Autophosphorylation of PAK1,2,3"
xref: Reactome:R-HSA-5632670 "CSNK1A1 phosphorylates SMO dimer"
xref: Reactome:R-HSA-5632672 "ADRBK1 phosphorylates SMO dimer"
xref: Reactome:R-HSA-5635841 "GLI proteins are phosphorylated"
xref: Reactome:R-HSA-5635842 "ULK3 phosphorylates GLI"
xref: Reactome:R-HSA-5665868 "AMPK (complex) phosphorylates ULK1 (complex)"
xref: Reactome:R-HSA-5666160 "AURKB phosphorylates DIAPH2-2 at kinetochores"
xref: Reactome:R-HSA-5668545 "NIK autophosphorylates on T559"
xref: Reactome:R-HSA-5668932 "PAK2 phosphorylates myosin regulatory light chain (MRLC)"
xref: Reactome:R-HSA-5668947 "PAK1 phosphorylates myosin phosphatase"
xref: Reactome:R-HSA-5668984 "PAK1 or PAK2 phosphorylates MYLK"
xref: Reactome:R-HSA-5669250 "PAK1 phosphorylates FLNA"
xref: Reactome:R-HSA-5671749 "p-T774-PKN1 phosphorylates CDC25C"
xref: Reactome:R-HSA-5671763 "p-T774-PKN1 phosphorylates PPP1R14A"
xref: Reactome:R-HSA-5671919 "Activated CIT phosphorylates MRLCs"
xref: Reactome:R-HSA-5672008 "Thr-180 of ULK1 is phosphorylated"
xref: Reactome:R-HSA-5672010 "Active MTORC1 phosphorylates ULK1"
xref: Reactome:R-HSA-5672828 "mTORC1 phosphorylates AKT1S1"
xref: Reactome:R-HSA-5672948 "MARK3 phosphorylates KSR1"
xref: Reactome:R-HSA-5672973 "MAP2Ks phosphorylate MAPKs"
xref: Reactome:R-HSA-5672978 "RAF phosphorylates MAP2K dimer"
xref: Reactome:R-HSA-5674496 "Activated MAPKs phosphorylate MAP2K1"
xref: Reactome:R-HSA-5675194 "Activated MAPK phosphorylates RAF1"
xref: Reactome:R-HSA-5675198 "Activated MAPKs phosphorylate BRAF"
xref: Reactome:R-HSA-5675868 "ULK1 phosphorylates ATG13 and RB1CC1"
xref: Reactome:R-HSA-5679205 "ULK1 phosphorylates Beclin-1"
xref: Reactome:R-HSA-5682026 "MRN bound to shortened telomeres activates ATM"
xref: Reactome:R-HSA-5682101 "PKA phosphorylates 4xPALM-C-p-2S-ABCA1 tetramer"
xref: Reactome:R-HSA-5682598 "ATM phosphorylates HERC2"
xref: Reactome:R-HSA-5682983 "ATM phosphorylates WHSC1"
xref: Reactome:R-HSA-5683425 "ATM phosphorylates TP53BP1 at DNA DSBs"
xref: Reactome:R-HSA-5683792 "p-T68-CHEK2 autophosphorylates"
xref: Reactome:R-HSA-5683801 "CHEK2 phosphorylates BRCA1"
xref: Reactome:R-HSA-5683964 "ATM phosphorylates EYA1-4"
xref: Reactome:R-HSA-5684096 "CDK2 phosphorylates RBBP8"
xref: Reactome:R-HSA-5684140 "ATM phosphorylates RBBP8"
xref: Reactome:R-HSA-5684887 "Activation of CHEK1 at resected DNA DSBs"
xref: Reactome:R-HSA-5685156 "ATR phosphorylates RPA2"
xref: Reactome:R-HSA-5685230 "CHEK1 phosphorylates RAD51"
xref: Reactome:R-HSA-5685242 "CHEK1 phosphorylates BRCA2"
xref: Reactome:R-HSA-5686578 "Activated ATM phosphorylates ABL1"
xref: Reactome:R-HSA-5686704 "Activated ATM phosphorylates DCLRE1C"
xref: Reactome:R-HSA-5687086 "PAK1,2,3 phosphorylates MAPK6,4"
xref: Reactome:R-HSA-5687090 "p-S MAPK6 phosphorylates NCOA3"
xref: Reactome:R-HSA-5687094 "p-S MAPK6,4 phosphorylate MAPKAPK5"
xref: Reactome:R-HSA-5687101 "p-T182 MAPKAPK5 phosphorylates FOXO3"
xref: Reactome:R-HSA-5687121 "p-S MAPKAPK5 phosphorylates HSPB1"
xref: Reactome:R-HSA-5687183 "PRKDC phosphorylates DCLRE1C at DNA DSBs"
xref: Reactome:R-HSA-5690250 "p-T182-MAPKAPK5 phoshphorylates DNAJB1"
xref: Reactome:R-HSA-5692768 "MAPKAPK5 phosphorylates KALRN"
xref: Reactome:R-HSA-5692775 "SEPT7:p-S189 MAPK6:p-T182 MAPKAPK5 phosphorylates CDC42EPs"
xref: Reactome:R-HSA-5692779 "p-T182 MAPKAPK5 phosphorylates FOXO1"
xref: Reactome:R-HSA-5693536 "ATM phosphorylates MDC1"
xref: Reactome:R-HSA-5693540 "MRN activates ATM"
xref: Reactome:R-HSA-5693549 "ATM phosphorylates histone H2AFX on S139 at DNA DSBs"
xref: Reactome:R-HSA-5693551 "Phosphorylation of BRCA1-A complex at multiple sites by ATM"
xref: Reactome:R-HSA-5693575 "DNA-PKcs autophosphorylates"
xref: Reactome:R-HSA-5693598 "ATM phosphorylates NBN"
xref: Reactome:R-HSA-5693609 "ATM phosphorylates TP53 at S15"
xref: Reactome:R-HSA-5694441 "CSNK1D phosphorylates SEC23"
xref: Reactome:R-HSA-6788392 "ATR phosphorylates RPA2, FANCI, FANCD2 and FANCM at ICL-DNA"
xref: Reactome:R-HSA-6795290 "TORC2 complex phosphorylates SGK1"
xref: Reactome:R-HSA-6795460 "SGK1 phosphorylates MDM2"
xref: Reactome:R-HSA-6795473 "PDPK1 phosphorylates SGK1"
xref: Reactome:R-HSA-6798372 "ATM phosphorylates DYRK2"
xref: Reactome:R-HSA-6798374 "DYRK2 phosphorylates TP53"
xref: Reactome:R-HSA-6799097 "ATM phosphorylates ZNF420"
xref: Reactome:R-HSA-6799246 "CHEK1 phosphorylates TP53"
xref: Reactome:R-HSA-6799332 "ATR phosphorylates TP53"
xref: Reactome:R-HSA-6799409 "HIPK2 phosphorylates TP53"
xref: Reactome:R-HSA-6800490 "ATM phosphorylates PIDD1"
xref: Reactome:R-HSA-6801666 "PLK2 phosphorylates CENPJ"
xref: Reactome:R-HSA-6801675 "PLK2 phosphorylates NPM1"
xref: Reactome:R-HSA-6802911 "High kinase activity BRAF complexes phosphorylate MAP2Ks"
xref: Reactome:R-HSA-6802919 "RAS:GTP:moderate kinase activity p-RAF complexes phosphorylate MAP2Ks"
xref: Reactome:R-HSA-6802926 "Mutant RAS:p-RAF complexes phosphorylate MAP2Ks"
xref: Reactome:R-HSA-6802933 "p-BRAF and RAF fusion dimers phosphorylate MAP2Ks"
xref: Reactome:R-HSA-6802935 "MAPKs are phosphorylated downstream of BRAF and RAF fusion dimers"
xref: Reactome:R-HSA-6802943 "RAS:GTP:inactive p-RAF complexes phosphorylate MAP2Ks"
xref: Reactome:R-HSA-6802973 "PLK3 phosphorylates CDC25C"
xref: Reactome:R-HSA-6804266 "CHEK2 phosphorylates TTC5"
xref: Reactome:R-HSA-6804276 "ATM phosphorylates TTC5"
xref: Reactome:R-HSA-6804955 "ATM phosphorylates MDM2"
xref: Reactome:R-HSA-6805059 "CK2:FACT phosphorylates TP53"
xref: Reactome:R-HSA-6805103 "AURKA phosphorylates TP53"
xref: Reactome:R-HSA-6805126 "AURKB phosphorylates TP53"
xref: Reactome:R-HSA-6805276 "CDK5 phosphorylates TP53"
xref: Reactome:R-HSA-6805285 "PLK3 phosphorylates TP53"
xref: Reactome:R-HSA-6805399 "TAF1 phosphorylates TP53"
xref: Reactome:R-HSA-6805479 "TP53RK phosphorylates TP53"
xref: Reactome:R-HSA-6805640 "AKT phosphorylates KAT6A"
xref: Reactome:R-HSA-6805785 "AKT phosphorylates PHF20"
xref: Reactome:R-HSA-6810233 "CDK7 phosphorylates serine-5 and serine-7 of heptad repeats in C-terminal domain of RNA polymerase II at snRNA promoter"
xref: Reactome:R-HSA-6811454 "MAPKs phosphorylate PP2A"
xref: Reactome:R-HSA-6814409 "CK2 phosphorylates PDCL"
xref: Reactome:R-HSA-69604 "Phosphorylation of CDC25A by CHEK1"
xref: Reactome:R-HSA-69608 "Phosphorylation of CDC25A by CHEK2"
xref: Reactome:R-HSA-69685 "CHEK2 phosphorylates TP53"
xref: Reactome:R-HSA-69891 "Phosphorylation and activation of CHEK2 by ATM"
xref: Reactome:R-HSA-75010 "Phosphorylation of Cdc25C at Ser 216 by Chk1"
xref: Reactome:R-HSA-75028 "Phosphorylation of Wee1 kinase by Chk1"
xref: Reactome:R-HSA-75809 "Phosphorylation of Cdc25C at Ser216 by CHEK2"
xref: Reactome:R-HSA-75820 "Phosphorylation of Cyclin D1 at T286 by glycogen synthase kinase-3 beta"
xref: Reactome:R-HSA-77071 "Phosphorylation (Ser5) of RNA pol II CTD"
xref: Reactome:R-HSA-8850945 "Casein kinase II phosphorylates PTEN"
xref: Reactome:R-HSA-8852306 "Mitotic phosphorylation-induced dissociation of GTSE1 from microtubule plus ends"
xref: Reactome:R-HSA-8852317 "PLK1 phosphorylates GTSE1"
xref: Reactome:R-HSA-8853419 "TPX2 promotes AURKA autophosphorylation"
xref: Reactome:R-HSA-8853444 "AURKA phosphorylates PHLDA1"
xref: Reactome:R-HSA-8854908 "PKA phosphorylates RET:GDNF:GFRA dimer"
xref: Reactome:R-HSA-8856813 "AAK1 phosphorylates AP-2 mu subunit at T156"
xref: Reactome:R-HSA-8863007 "p25-bound CDK5 phosphorylates CDC25B"
xref: Reactome:R-HSA-8863011 "p25-bound CDK5 phosphorylates CDC25C"
xref: Reactome:R-HSA-8863014 "p25-bound CDK5 phosphorylates CDC25A"
xref: Reactome:R-HSA-8863895 "IKKB phosphorylates SNAP23"
xref: Reactome:R-HSA-8868118 "MAPK12 phosphorylates PTPN3"
xref: Reactome:R-HSA-8868260 "CDK5:p25 phosphorylates GOLGA2"
xref: Reactome:R-HSA-8868340 "CDK5:p25 phosphorylates lamin B1"
xref: Reactome:R-HSA-8868344 "CDK5:p25 phosphorylates lamin A"
xref: Reactome:R-HSA-8868567 "CDK5:p25 phosphorylates PRDX1"
xref: Reactome:R-HSA-8868573 "CDK5:p25 phosphorylates PRDX2"
xref: Reactome:R-HSA-8868666 "CDK5:p25 phosphorylates JUN"
xref: Reactome:R-HSA-8870558 "CDK5:p25 phosphorylates FOXO3"
xref: Reactome:R-HSA-8873929 "Casein kinase II phosphorylates STARD10"
xref: Reactome:R-HSA-8876446 "p-ULK1 phosphorylates DENND3"
xref: Reactome:R-HSA-8877691 "MAP2K6 phosphorylates PIP4K2B"
xref: Reactome:R-HSA-8878050 "HIPK2 phosphorylates RUNX1 and EP300"
xref: Reactome:R-HSA-8878054 "HIPK2 phosphorylates RUNX1"
xref: Reactome:R-HSA-8932322 "CK2 phosphorylates NFE2L2"
xref: Reactome:R-HSA-8933446 "Active AKT phosphorylates DENND1A and DENND1B in response to insulin signaling"
xref: Reactome:R-HSA-8939963 "Activated AKT phosphorylates RUNX2"
xref: Reactome:R-HSA-8940100 "CDK1 phosphorylates VCPIP1"
xref: Reactome:R-HSA-8942836 "CDK4/6:CCND complexes are activated by T-loop phosphorylation of CDK4/6"
xref: Reactome:R-HSA-8944454 "mTORC1 phosphorylates MAF1"
xref: Reactome:R-HSA-8948039 "FUNDC1 is phosphorylated by CK2"
xref: Reactome:R-HSA-8948146 "FUNDC1 is phosphorylated by ULK1 at Ser17"
xref: Reactome:R-HSA-8948757 "AKT phosphorylates MKRN1"
xref: Reactome:R-HSA-8952289 "FAM20C phosphorylates FAM20C substrates"
xref: Reactome:R-HSA-9007539 "CHEK1 phosphorylates E2F6"
xref: Reactome:R-HSA-9008480 "GSK3B phosphorylates RUNX2"
xref: Reactome:R-HSA-9008822 "PPM1D dephosphorylates RUNX2"
xref: Reactome:R-HSA-9009208 "Activated ERKs phosphorylate RUNX2"
xref: Reactome:R-HSA-9012319 "p-TEFb phosphorylates serine 2 in RNA polymerase II CTD"
xref: Reactome:R-HSA-9013978 "Phosphorylation of IRF-3/IRF7 and their release from the activated TLR3 complex"
xref: Reactome:R-HSA-9021357 "PRKCI phosphorylates ELF3"
xref: Reactome:R-HSA-9022314 "HIPK2 phosphorylates MECP2"
xref: Reactome:R-HSA-9023132 "AURKB phosphorylates MECP2 at S423"
xref: Reactome:R-HSA-9032751 "Estrogen-independent phosphorylation of ESR1 S118 by MAPK1 and MAPK3"
xref: Reactome:R-HSA-9032863 "CDK5 phosphorylates NTRK2"
xref: Reactome:R-HSA-912470 "ATR phosphorylates Histone H2A.X at unsynapsed regions"
xref: Reactome:R-HSA-913996 "PKA/PKG phosphorylate Rap1GAP2"
xref: Reactome:R-HSA-918229 "Phosphorylation and release of IRF3/IRF7"
xref: Reactome:R-HSA-927889 "SMG1 phosphorylates UPF1 (enhanced by Exon Junction Complex)"
xref: Reactome:R-HSA-933525 "Phosphorylation and release of IRF7"
xref: Reactome:R-HSA-934559 "SPRY2 is phosphorylated by phosphorylated MNK1"
xref: Reactome:R-HSA-936951 "Activation of TAK1 complex bound to activated TLR4 complex"
xref: Reactome:R-HSA-937022 "IRAK4 autophosphorylation in the complex with activated TLR:MyD88:TIRAP"
xref: Reactome:R-HSA-937059 "Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomer:TIRAP:activated TLR complex"
xref: Reactome:R-HSA-9604328 "AKT1 phosphorylates NOTCH4"
xref: Reactome:R-HSA-9610153 "Activated BRAF phosphorylates MAP2K dimers downstream of RAP1 and NGF"
xref: Reactome:R-HSA-9610156 "MAP2Ks phosphorylate MAPKs downstream of BRAF and NGF"
xref: Reactome:R-HSA-9610163 "BRAF autophosphorylates downstream of RAP1 and NGF"
xref: Reactome:R-HSA-9612501 "SGK phosphorylates CREB1"
xref: Reactome:R-HSA-9612509 "SGK phosphorylates SRF"
xref: Reactome:R-HSA-9612980 "BRAF in Rap1-GTP complex:BRAF complex autophosphorylates"
xref: Reactome:R-HSA-9613530 "PRKAA2 phosphorylates PLINs"
xref: Reactome:R-HSA-9619515 "AMPK phosphorylates MAPT"
xref: Reactome:R-HSA-9619843 "ERKs phosphorylate RSKs"
xref: Reactome:R-HSA-9620004 "RSKs autophosphorylate"
xref: Reactome:R-HSA-9624526 "AKT phosphorylates FOXO3 downstream of ESR1 and EGFR"
xref: Reactome:R-HSA-9626880 "MAPK11 or MAPK14 phosphorylates NCF1 at Ser345"
xref: Reactome:R-HSA-9627089 "CASP9 is phosphorylated at T412"
xref: Reactome:R-HSA-9632858 "PRKCZ autophosphorylates downstream of estrogen stimulation"
xref: Reactome:R-HSA-9632868 "CDKN1B is phosphorylated in response to estrogen"
xref: Reactome:R-HSA-9633008 "p-T899-EIF2AK4 (GCN2) phosphorylates EIF2AS1"
xref: Reactome:R-HSA-9633742 "EIF2AK4 (GCN2) dimer autophosphorylates"
xref: Reactome:R-HSA-9634702 "LINC01139 promotes phosphorylation of HIF1A by LRRK2"
xref: Reactome:R-HSA-9645535 "ALPK1 phosphorylates TIFA"
xref: Reactome:R-HSA-9648089 "NEK6 and NEK7 phosphorylate EML4"
xref: Reactome:R-HSA-9648883 "p-T-EIF2AK1:ferriheme dimer autophosphorylates"
xref: Reactome:R-HSA-9648888 "p-T,T486,T488-EIF2AK1 phosphorylates EIF2S1 (eIF2-alpha)"
xref: Reactome:R-HSA-9652165 "MAP2K mutants constitutively phosphorylate MAPKs"
xref: Reactome:R-HSA-9653503 "KRAS4B is phosphorylated on serine 181"
xref: Reactome:R-HSA-9656214 "MAP2Ks phosphorylate MAPKs downstream of RAF1 mutants"
xref: Reactome:R-HSA-9656215 "RAF1 mutant complexes phosphorylate MAP2K dimer"
xref: Reactome:R-HSA-9662823 "PLK2, MAPK14 phosphorylate ADAM17"
xref: Reactome:R-HSA-9673346 "Unknown kinase phosphorylates p-DVL"
xref: Reactome:R-HSA-9683664 "GSK3 phosphorylates Nucleoprotein"
xref: Reactome:R-HSA-9699579 "AKT phosphorylates FOXO3 downstream of FLT3"
xref: Reactome:R-HSA-9705320 "TBK1, IKBKE are autophosphorylated at Ser172"
xref: Reactome:R-HSA-9705323 "Phosphorylation of TBK1/IKBKE"
xref: Reactome:R-HSA-9725030 "MAPK1 phsophorylates ZC3HCF1 in a NPM-ALK-dependent manner"
xref: Reactome:R-HSA-9729260 "GSK3 phosphorylates nucleoprotein"
xref: Reactome:R-HSA-9729300 "Unknown kinase phosphorylates nucleoprotein"
xref: Reactome:R-HSA-9729318 "CSNK1A1 phosphorylates nucleoprotein"
xref: Reactome:R-HSA-9731111 "MAPK1 and MAPK3 phosphorylate SMAD2 and SMAD3"
xref: Reactome:R-HSA-9734547 "JAK2-activated MAPKs phosphorylate YBX1"
xref: Reactome:R-HSA-975125 "Multiple IRAK1 autophosphorylation steps within the complex pIRAK4:MyD88:activated TLR7/8 or 9"
xref: Reactome:R-HSA-975134 "Second phosphorylation of IRAK1 by IRAK4 bound to MyD88: activated TLR 7/8 or 9"
xref: Reactome:R-HSA-975160 "Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomer:activated TLR 7/8 or 9"
xref: Reactome:R-HSA-975170 "IRAK4 autophosphorylation in the complex with MyD88:activated TLR 7/8 or 9"
xref: Reactome:R-HSA-975180 "First phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR 7/8 or 9"
xref: Reactome:R-HSA-9758486 "Unknown kinase phosphorylates 9b"
xref: Reactome:R-HSA-975853 "Multiple IRAK1 autophosphorylation within the complex p-IRAK4:oligo MyD88:activated TLR"
xref: Reactome:R-HSA-975861 "Phosphorylation of IRAK2 bound to the activated IRAK4:MyD88 oligomerl:activated TLR5 or 10 complex"
xref: Reactome:R-HSA-975865 "IRAK4 autophosphorylation within the complex activated TLR:MyD88"
xref: Reactome:R-HSA-975874 "Second phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR complex"
xref: Reactome:R-HSA-975878 "First phosphorylation of IRAK1 by IRAK4 bound to MyD88:activated TLR"
xref: Reactome:R-HSA-9762094 "GSK3B phosphorylates p-NFE2L2"
xref: Reactome:R-HSA-9765960 "ERKs phosphorylate MCRIP1"
xref: Reactome:R-HSA-9766532 "SQSTM1 oligomer is phosphorylated"
xref: Reactome:R-HSA-9769115 "MAPK1,(MAPK3) phosphorylates NPAS4"
xref: Reactome:R-HSA-9773803 "Active IKBKB phosphorylates NF-kappa-B inhibitor"
xref: Reactome:R-HSA-9796053 "PRKCI phosphorylates NFE2L2"
xref: Reactome:R-HSA-9796067 "PRKAA2 phosphorylates nuclear NFE2L2"
xref: Reactome:R-HSA-9796081 "EIF2AK3 phosphorylates NFE2L2"
xref: Reactome:R-HSA-9815501 "MAPKAPK2 phosphorylates RIPK1 at S320"
xref: Reactome:R-HSA-9817397 "TBK1, IKBKE phosphorylate RIPK1 at T189"
xref: Reactome:R-HSA-9818789 "CHUK, IKBKB phosphorylate RIPK1 at S25"
xref: Reactome:R-HSA-9819106 "ULK1 phosphorylates RIPK1 at S357"
xref: Reactome:R-HSA-9824582 "MAPK1 phosphorylates SOX10"
xref: Reactome:R-HSA-9824897 "p-S-TBK1 phosphorylates OPTN"
xref: Reactome:R-HSA-9824977 "MAPK1-dependent phosphorylation of MITF-M"
xref: Reactome:R-HSA-9824994 "RPS6KA1-dependent phosphorylation of MITF-M"
xref: Reactome:R-HSA-9824995 "GSK3B phosphorylates p-S409 MITF-M at S397, S401 and S405"
xref: Reactome:R-HSA-9824999 "GSK3B phosphorylates p-S73 MITF-M at residue S69"
xref: Reactome:R-HSA-9825704 "AKT3 phosphorylates TBX3"
xref: Reactome:R-HSA-9831514 "CK2 phosphorylates nascent P"
xref: Reactome:R-HSA-9831712 "M dimer is phosphorylated"
xref: Reactome:R-HSA-9832782 "p-S232-S237-P is further phosphorylated"
xref: Reactome:R-HSA-9834076 "PINK1 is autophosphorylated"
xref: Reactome:R-HSA-9834945 "PINK1 phosphorylates Ub on MOM proteins"
xref: Reactome:R-HSA-9835011 "PINK1 phosphorylates PRKN at S65"
xref: Reactome:R-HSA-9839363 "TGFBR3 phosphorylation by TGFBR2 complex"
xref: Reactome:R-HSA-9851972 "PLK1 phosphorylates FIRRM at S43"
xref: Reactome:R-HSA-9853369 "PLK1 phosphorylates FIRMM at S744"
xref: Reactome:R-HSA-9855910 "USF1 is phosphorylated by p-MAPK14"
xref: Reactome:R-HSA-9857661 "p-T308,S473-AKT1 (phospho-PKB) phosphorylates GJA1 (Connexin-43)"
xref: Reactome:R-HSA-9857673 "p-T308,S473-AKT1 phosphorylates ITGA5 (Integrin alpha5) in ITGA5:ITGB1 (Integrin alpha5:Integrin beta1)"
xref: Reactome:R-HSA-9860292 "Activated IKBKB phosphorylates IRF5"
xref: Reactome:R-HSA-9860785 "PDPK1 (PDK1) phosphorylates PKN2 on threonine-816"
xref: Reactome:R-HSA-9860800 "mTORC2 phosphorylates AKT1 on serine-473"
xref: Reactome:R-HSA-9861642 "NEK1 phosphorylates ME1"
xref: Reactome:R-HSA-9909369 "CSNK1E,CSNK1D phosphorylate CRY and PER proteins"
xref: Reactome:R-HSA-9912396 "CDK5 phosphorylates CLOCK on serine-451 and serine-461"
xref: Reactome:R-HSA-9912401 "CK2alpha phosphorylates BMAL1 (ARNTL) on serine-90"
xref: Reactome:R-HSA-9920673 "CDK5 phosphorylates PER2 on serine-396"
xref: Reactome:R-HSA-9922273 "CSNK1D,E phosphorylates CLOCK in p-S-CRY:p-S-PER:CSNK1D,E:p-S90,Ac-538-BMAL:p-2T,3S-CLOCK:target gene"
xref: Reactome:R-HSA-9926483 "MARK3 phosphorylates MITF-M on S173"
xref: Reactome:R-HSA-9929360 "GSK3B phosphorylates CD274"
xref: Reactome:R-HSA-9931292 "AMPK phosphorylates CD274"
xref: Reactome:R-HSA-9931409 "NEK2 phosphorylates CD274"
xref: Reactome:R-HSA-9931418 "CK2 phosphorylates CD274"
xref: Reactome:R-HSA-9933380 "Cytosolic tail of CDH1 is phosphorylated"
xref: Reactome:R-HSA-9942578 "Phosphorylation of CDC25A by p38 MAPK"
xref: Reactome:R-HSA-9943662 "CHEK1 phosphorylates NEK11"
xref: Reactome:R-HSA-9943675 "GSK3B phosphorylates CDC25A"
xref: Reactome:R-HSA-9943676 "NEK11 phosphorylates CDC25A"
xref: Reactome:R-HSA-9943678 "CHEK1 phosphorylates CHEK2-phosphorylated CDC25A"
xref: Reactome:R-HSA-9943687 "PLK3 phosphorylates CDC25A"
xref: Reactome:R-HSA-9943736 "Casein kinase I phosphorylates CDC25A"
xref: Reactome:R-HSA-9954237 "PIM1 phosphorylates GBP1"
is_a: GO:0004672 ! protein kinase activity
property_value: skos:exactMatch EC:2.7.11.-
property_value: skos:exactMatch MetaCyc:PROTEIN-KINASE-RXN
property_value: skos:narrowMatch EC:2.7.11.1
property_value: skos:narrowMatch EC:2.7.11.28
property_value: skos:narrowMatch EC:2.7.11.29
property_value: skos:narrowMatch EC:2.7.11.3
property_value: skos:narrowMatch EC:2.7.11.9

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
