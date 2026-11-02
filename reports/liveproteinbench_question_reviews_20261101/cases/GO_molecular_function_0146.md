# GO_molecular_function_0146

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — zinc ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDFTHFDDVAFAYYGLPDQSSLVSLLDHTHTFQSPTAFPQHQAMSGLAHSGLPFGTLPTGNRSQSMEGSKAPPDRTSPASNAFENPTTDEFGLASCNRADGTDLGGKPREDKAGATPAWSGLKTKAGKERKRLPLACIACRRKKVRCSGEKPACKHCLHSHIPCVYKVTTRKAAPRTNYMVMLDKRPKCMEERIIKATPKSDQEVASFVTRPVVKPAIPGAVPSSKPTKKRGAEEAFGLDLEAWAKAPSKPKIEGDDRPSSLQAQEGEENKLQHEGTEALPSEEIQEHLAEVFFDNIYGQSYHLLHKPSYLRKLKNGTLPPVLVLTVCAVAARFTSNPLGGRSWALGGQAIRMAFALQLHKDLEYDPSGRNGAKTQLSFIDREIRRRIMWACFLLDRFNSSGTDRPMFIREDTIQIPLPVKEKYFQFDMPAPTELLDGQVPHPPSPNDGQIADARENMGVAAFLIRAIALWGRIITYLSQGCKDLDPNLLWEEEPHYIKHLNDAVNLEASLPLSLNYSAENLEVHKTENAASQFLFMHICLQHNILLVSRAAMSARKQQGVHDDFFSEASQRTFSAANRISEFLREAEQSRCFVSAPFAGYCAFSSATVHILGIISCNPSMKPTAEANLTTNVKYLHKMKKYWERATQLSFLQYGDWYNRYPRGLSDAEFMDPATHKRKDSGADGVLEAKPELRSVEEYSTLPTPRRVENKDTIRAAAPKRKQSAKKQTGMPAQPGQHLDSLQSTDADAVSQERKFSGGLGLQITGAAGFNPLSASNQQNPDFSTTMSPTSPANMTPFSHYAHTPTFFPPELLSIDFGQGSNGNIDPLDRQLIYGGYSMDASTGLCGGQDMMSGLGWDTVASGAQPDGCLQGRPPNVKAGMHGQSAASSSFPAINKTNGKGKEGRGIGSHTDYGLLVIAAADDVGGDMMQYMTNSVLPSTPHKVGLNLRERFAFAYFHEPSFQAVVRPLPGYDHGQEPKGGIHYGKQFTDMFMRNYPQRITTQRLNDEGRYRLLDQESLQTMSP

[Multiple Choices]
A. ATP hydrolysis activity
B. membrane destabilizing activity
C. nucleotide binding
D. zinc ion binding
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

> The sequence-matched UniProt entry annotates zinc ion binding as GO:0008270, with evidence code IEA:InterPro, and names the protein as a Zn(2)-C6 fungal-type transcription factor. This supports the key, though the cited GO annotation is computational rather than direct experimental evidence of zinc binding.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clustered cysteine-rich region consistent with the characteristic Cys6 zinc-binding DNA-binding domain of fungal Zn(2)-C6 transcription factors, making zinc ion binding a defensible choice over ATP hydrolysis, nucleotide binding, or membrane destabilization.


**Missing item-specific fact**

> No item-specific fact is strictly needed to distinguish these options from the sequence motif, although experimental confirmation of zinc binding is not supplied.


**Reason**

> The cysteine-cluster motif provides a concrete biological clue for zinc binding; this is more than simply identifying the protein or relying on a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the cysteine-rich zinc-binding motif supports D; the sequence gives no comparably specific indication of ATPase, nucleotide-binding, or membrane-destabilizing activity.


### Important caveats

- The sequence-matched GO zinc-binding annotation is IEA:InterPro, a computational annotation, not itself a direct experimental measurement.
- Reviewer-only accession and annotation evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clustered cysteine-rich region consistent with the characteristic Cys6 zinc-binding DNA-binding domain of fungal Zn(2)-C6 transcription factors, making zinc ion binding a defensible choice over ATP hydrolysis, nucleotide binding, or membrane destabilization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is strictly needed to distinguish these options from the sequence motif, although experimental confirmation of zinc binding is not supplied.",
    "reason": "The cysteine-cluster motif provides a concrete biological clue for zinc binding; this is more than simply identifying the protein or relying on a database lookup."
  },
  "case_id": "GO_molecular_function_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates zinc ion binding as GO:0008270, with evidence code IEA:InterPro, and names the protein as a Zn(2)-C6 fungal-type transcription factor. This supports the key, though the cited GO annotation is computational rather than direct experimental evidence of zinc binding."
  },
  "important_caveats": [
    "The sequence-matched GO zinc-binding annotation is IEA:InterPro, a computational annotation, not itself a direct experimental measurement.",
    "Reviewer-only accession and annotation evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the cysteine-rich zinc-binding motif supports D; the sequence gives no comparably specific indication of ATPase, nucleotide-binding, or membrane-destabilizing activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates zinc ion binding as GO:0008270, with evidence code IEA:InterPro, and names the protein as a Zn(2)-C6 fungal-type transcription factor. This supports the key, though the cited GO annotation is computational rather than direct experimental evidence of zinc binding.",
    "evidence_ids": ["C4", "C8", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clustered cysteine-rich region consistent with the characteristic Cys6 zinc-binding DNA-binding domain of fungal Zn(2)-C6 transcription factors, making zinc ion binding a defensible choice over ATP hydrolysis, nucleotide binding, or membrane destabilization.",
    "missing_item_specific_fact": "No item-specific fact is strictly needed to distinguish these options from the sequence motif, although experimental confirmation of zinc binding is not supplied.",
    "reason": "The cysteine-cluster motif provides a concrete biological clue for zinc binding; this is more than simply identifying the protein or relying on a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the cysteine-rich zinc-binding motif supports D; the sequence gives no comparably specific indication of ATPase, nucleotide-binding, or membrane-destabilizing activity."
  },
  "important_caveats": [
    "The sequence-matched GO zinc-binding annotation is IEA:InterPro, a computational annotation, not itself a direct experimental measurement.",
    "Reviewer-only accession and annotation evidence was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0J9VYS2) explicitly names the protein 'Zn(2)-C6 fungal-type transcription factor FTF1a' (C4, H1) and annotates GO:0008270 'zinc ion binding' with IEA:InterPro evidence (C8, H7). The Zn2Cys6 (fungal-type zinc cluster) domain is a defining structural feature of this protein class, and zinc ion binding is a direct molecular function of that domain. The function comment (C5, H4) confirms it is a Zn(2)-C6 fungal-type transcription factor. While the GO annotation is computational (IEA:InterPro) rather than experimentally verified, the protein name and domain classification independently support zinc ion binding as a correct molecular function. The other options (ATP hydrolysis, membrane destabilizing, free-nucleotide binding) are inconsistent with the annotation and the protein's identity as a nuclear transcription factor.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H4](#evidence-h4), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a visible cysteine-rich cluster in the N-terminal region ('ACIACRRKKVRCSGEKPACKHCLHSHIPCVYKV', roughly residues ~100–135) with six cysteines in a spacing pattern broadly consistent with the Zn2Cys6 (fungal-type zinc cluster) motif. This motif is a well-known, textbook domain in fungal transcription factors that coordinates two zinc ions via six cysteine ligands. A model with general protein-domain knowledge can identify the Cys cluster as indicative of a zinc-binding domain. The remaining options are clearly inconsistent: ATP hydrolysis requires Walker A/B or AAA+ motifs absent here; membrane destabilizing activity requires amphipathic helical peptides typical of antimicrobial peptides, not a large nuclear transcription factor; and GO:0000166 'nucleotide binding' refers to free nucleotides (ATP, GTP, etc.), not DNA, which is the substrate of a transcription factor. Thus the cysteine-cluster evidence plus elimination of the other three options provides a meaningful reasoning path.


**Missing item-specific fact**

> The exact Zn2Cys6 spacing in this particular protein is somewhat degenerate relative to the canonical Cys-X2-Cys-X6-Cys-X2-Cys-X6-Cys-X2-Cys consensus (the C3→C4 spacing appears to be X6 rather than X2), so a strict pattern-matching model might not confidently assign the motif without prior knowledge of FTF/Zn2Cys6 domain variability. Additionally, designating zinc ion binding as the 'primary' molecular function over DNA binding (GO:0003677, also annotated) requires knowing the GO annotation hierarchy and the convention that the structural cofactor-binding function is listed alongside the catalytic/regulatory function.


**Reason**

> The cysteine-rich motif is identifiable from the raw sequence, and the Zn2Cys6 domain is a standard textbook motif in fungal biology. General knowledge of protein domains plus elimination of clearly wrong distractors provides a defensible reasoning path. The slight irregularity in cysteine spacing and the 'primary function' framing introduce some reliance on domain-specific familiarity, but the overall argument does not require memorizing this specific protein's UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C ('nucleotide binding') could superficially seem applicable because the protein binds DNA (a polymer of nucleotides), but the GO definition of GO:0000166 explicitly restricts the term to binding free nucleotides (nucleoside phosphates), not nucleic acids. DNA binding is covered by GO:0003677, which is not offered. Options A and B are clearly inconsistent with the protein's identity and sequence features. Therefore only option D is defensible among the four choices.


### Important caveats

- The GO annotation for zinc ion binding (GO:0008270) carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental evidence. The protein-level function annotation (transcription factor role in virulence) is experimentally supported (ECO:0000269, PubMed:17462924, PubMed:26817616), but zinc ion binding specifically is inferred from the Zn2Cys6 domain assignment.
- The Zn2Cys6 cysteine spacing in this sequence deviates slightly from the strict canonical consensus, so confident motif identification from sequence alone may require familiarity with FTF-family domain variability.
- The protein is 1024 amino acids long with multiple regions; the cysteine cluster is a relatively small portion. A model must correctly focus on the relevant domain rather than being distracted by other sequence features.
- The 'primary molecular function' framing could arguably favor DNA binding (the protein's biological role) over zinc ion binding (a structural/cofactor function), but DNA binding is not among the offered options, so this ambiguity does not affect the answer choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a visible cysteine-rich cluster in the N-terminal region ('ACIACRRKKVRCSGEKPACKHCLHSHIPCVYKV', roughly residues ~100–135) with six cysteines in a spacing pattern broadly consistent with the Zn2Cys6 (fungal-type zinc cluster) motif. This motif is a well-known, textbook domain in fungal transcription factors that coordinates two zinc ions via six cysteine ligands. A model with general protein-domain knowledge can identify the Cys cluster as indicative of a zinc-binding domain. The remaining options are clearly inconsistent: ATP hydrolysis requires Walker A/B or AAA+ motifs absent here; membrane destabilizing activity requires amphipathic helical peptides typical of antimicrobial peptides, not a large nuclear transcription factor; and GO:0000166 'nucleotide binding' refers to free nucleotides (ATP, GTP, etc.), not DNA, which is the substrate of a transcription factor. Thus the cysteine-cluster evidence plus elimination of the other three options provides a meaningful reasoning path.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact Zn2Cys6 spacing in this particular protein is somewhat degenerate relative to the canonical Cys-X2-Cys-X6-Cys-X2-Cys-X6-Cys-X2-Cys consensus (the C3→C4 spacing appears to be X6 rather than X2), so a strict pattern-matching model might not confidently assign the motif without prior knowledge of FTF/Zn2Cys6 domain variability. Additionally, designating zinc ion binding as the 'primary' molecular function over DNA binding (GO:0003677, also annotated) requires knowing the GO annotation hierarchy and the convention that the structural cofactor-binding function is listed alongside the catalytic/regulatory function.",
    "reason": "The cysteine-rich motif is identifiable from the raw sequence, and the Zn2Cys6 domain is a standard textbook motif in fungal biology. General knowledge of protein domains plus elimination of clearly wrong distractors provides a defensible reasoning path. The slight irregularity in cysteine spacing and the 'primary function' framing introduce some reliance on domain-specific familiarity, but the overall argument does not require memorizing this specific protein's UniProt entry."
  },
  "case_id": "GO_molecular_function_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H4",
      "H7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0J9VYS2) explicitly names the protein 'Zn(2)-C6 fungal-type transcription factor FTF1a' (C4, H1) and annotates GO:0008270 'zinc ion binding' with IEA:InterPro evidence (C8, H7). The Zn2Cys6 (fungal-type zinc cluster) domain is a defining structural feature of this protein class, and zinc ion binding is a direct molecular function of that domain. The function comment (C5, H4) confirms it is a Zn(2)-C6 fungal-type transcription factor. While the GO annotation is computational (IEA:InterPro) rather than experimentally verified, the protein name and domain classification independently support zinc ion binding as a correct molecular function. The other options (ATP hydrolysis, membrane destabilizing, free-nucleotide binding) are inconsistent with the annotation and the protein's identity as a nuclear transcription factor."
  },
  "important_caveats": [
    "The GO annotation for zinc ion binding (GO:0008270) carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental evidence. The protein-level function annotation (transcription factor role in virulence) is experimentally supported (ECO:0000269, PubMed:17462924, PubMed:26817616), but zinc ion binding specifically is inferred from the Zn2Cys6 domain assignment.",
    "The Zn2Cys6 cysteine spacing in this sequence deviates slightly from the strict canonical consensus, so confident motif identification from sequence alone may require familiarity with FTF-family domain variability.",
    "The protein is 1024 amino acids long with multiple regions; the cysteine cluster is a relatively small portion. A model must correctly focus on the relevant domain rather than being distracted by other sequence features.",
    "The 'primary molecular function' framing could arguably favor DNA binding (the protein's biological role) over zinc ion binding (a structural/cofactor function), but DNA binding is not among the offered options, so this ambiguity does not affect the answer choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C ('nucleotide binding') could superficially seem applicable because the protein binds DNA (a polymer of nucleotides), but the GO definition of GO:0000166 explicitly restricts the term to binding free nucleotides (nucleoside phosphates), not nucleic acids. DNA binding is covered by GO:0003677, which is not offered. Options A and B are clearly inconsistent with the protein's identity and sequence features. Therefore only option D is defensible among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0J9VYS2) explicitly names the protein 'Zn(2)-C6 fungal-type transcription factor FTF1a' (C4, H1) and annotates GO:0008270 'zinc ion binding' with IEA:InterPro evidence (C8, H7). The Zn2Cys6 (fungal-type zinc cluster) domain is a defining structural feature of this protein class, and zinc ion binding is a direct molecular function of that domain. The function comment (C5, H4) confirms it is a Zn(2)-C6 fungal-type transcription factor. While the GO annotation is computational (IEA:InterPro) rather than experimentally verified, the protein name and domain classification independently support zinc ion binding as a correct molecular function. The other options (ATP hydrolysis, membrane destabilizing, free-nucleotide binding) are inconsistent with the annotation and the protein's identity as a nuclear transcription factor.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H4", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a visible cysteine-rich cluster in the N-terminal region ('ACIACRRKKVRCSGEKPACKHCLHSHIPCVYKV', roughly residues ~100–135) with six cysteines in a spacing pattern broadly consistent with the Zn2Cys6 (fungal-type zinc cluster) motif. This motif is a well-known, textbook domain in fungal transcription factors that coordinates two zinc ions via six cysteine ligands. A model with general protein-domain knowledge can identify the Cys cluster as indicative of a zinc-binding domain. The remaining options are clearly inconsistent: ATP hydrolysis requires Walker A/B or AAA+ motifs absent here; membrane destabilizing activity requires amphipathic helical peptides typical of antimicrobial peptides, not a large nuclear transcription factor; and GO:0000166 'nucleotide binding' refers to free nucleotides (ATP, GTP, etc.), not DNA, which is the substrate of a transcription factor. Thus the cysteine-cluster evidence plus elimination of the other three options provides a meaningful reasoning path.",
    "missing_item_specific_fact": "The exact Zn2Cys6 spacing in this particular protein is somewhat degenerate relative to the canonical Cys-X2-Cys-X6-Cys-X2-Cys-X6-Cys-X2-Cys consensus (the C3→C4 spacing appears to be X6 rather than X2), so a strict pattern-matching model might not confidently assign the motif without prior knowledge of FTF/Zn2Cys6 domain variability. Additionally, designating zinc ion binding as the 'primary' molecular function over DNA binding (GO:0003677, also annotated) requires knowing the GO annotation hierarchy and the convention that the structural cofactor-binding function is listed alongside the catalytic/regulatory function.",
    "reason": "The cysteine-rich motif is identifiable from the raw sequence, and the Zn2Cys6 domain is a standard textbook motif in fungal biology. General knowledge of protein domains plus elimination of clearly wrong distractors provides a defensible reasoning path. The slight irregularity in cysteine spacing and the 'primary function' framing introduce some reliance on domain-specific familiarity, but the overall argument does not require memorizing this specific protein's UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C ('nucleotide binding') could superficially seem applicable because the protein binds DNA (a polymer of nucleotides), but the GO definition of GO:0000166 explicitly restricts the term to binding free nucleotides (nucleoside phosphates), not nucleic acids. DNA binding is covered by GO:0003677, which is not offered. Options A and B are clearly inconsistent with the protein's identity and sequence features. Therefore only option D is defensible among the four choices."
  },
  "important_caveats": [
    "The GO annotation for zinc ion binding (GO:0008270) carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental evidence. The protein-level function annotation (transcription factor role in virulence) is experimentally supported (ECO:0000269, PubMed:17462924, PubMed:26817616), but zinc ion binding specifically is inferred from the Zn2Cys6 domain assignment.",
    "The Zn2Cys6 cysteine spacing in this sequence deviates slightly from the strict canonical consensus, so confident motif identification from sequence alone may require familiarity with FTF-family domain variability.",
    "The protein is 1024 amino acids long with multiple regions; the cysteine cluster is a relatively small portion. A model must correctly focus on the relevant domain rather than being distracted by other sequence features.",
    "The 'primary molecular function' framing could arguably favor DNA binding (the protein's biological role) over zinc ion binding (a structural/cofactor function), but DNA binding is not among the offered options, so this ambiguity does not affect the answer choice."
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

**Accession:** `A0A0J9VYS2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9VYS2.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.576717+00:00.  

```json
{"commonName":"Fusarium vascular wilt of tomato","lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Sordariomycetes","Hypocreomycetidae","Hypocreales","Nectriaceae","Fusarium","Fusarium oxysporum species complex"],"scientificName":"Fusarium oxysporum f. sp. lycopersici (strain 4287 / CBS 123668 / FGSC 9935 / NRRL 34936)","taxonId":426428}
```

Source SHA-256: `e89ab5327e118190794452a1a84c6b31ce598afc341a81c04c0b09622af8ab08`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9VYS2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.576717+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26817616","source":"PubMed"}],"value":"Fusarium transcription factor 1a"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26817616","source":"PubMed"}],"value":"Zn(2)-C6 fungal-type transcription factor FTF1a"}}}
```

Source SHA-256: `e89ab5327e118190794452a1a84c6b31ce598afc341a81c04c0b09622af8ab08`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9VYS2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.576717+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17462924","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26817616","source":"PubMed"}],"value":"Zn(2)-C6 fungal-type transcription factor that has a role in the establishment of the fungus within the plant and/or the progress of the disease (PubMed:17462924, PubMed:26817616). Regulates the expression of virulence factors such as SIX1 and SIX6 (PubMed:26817616)"}]}
```

Source SHA-256: `e89ab5327e118190794452a1a84c6b31ce598afc341a81c04c0b09622af8ab08`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9VYS2.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.576717+00:00.  

```json
{"database":"GO","id":"GO:0003677","properties":[{"key":"GoTerm","value":"F:DNA binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `e89ab5327e118190794452a1a84c6b31ce598afc341a81c04c0b09622af8ab08`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9VYS2.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.576717+00:00.  

```json
{"database":"GO","id":"GO:0008270","properties":[{"key":"GoTerm","value":"F:zinc ion binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `e89ab5327e118190794452a1a84c6b31ce598afc341a81c04c0b09622af8ab08`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9VYS2?format=txt&versions=13)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:13.456029+00:00.  

```text
ID   TF1A1_FUSO4             Reviewed;        1024 AA.
AC   A0A0J9VYS2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-JUN-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Zn(2)-C6 fungal-type transcription factor FTF1a {ECO:0000303|PubMed:26817616};
DE   AltName: Full=Fusarium transcription factor 1a {ECO:0000303|PubMed:26817616};
GN   Name=FTF1a {ECO:0000303|PubMed:26817616}; ORFNames=FOXG_14257;
OS   Fusarium oxysporum f. sp. lycopersici (strain 4287 / CBS 123668 / FGSC 9935
OS   / NRRL 34936) (Fusarium vascular wilt of tomato).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Nectriaceae; Fusarium;
OC   Fusarium oxysporum species complex.
OX   NCBI_TaxID=426428;
```

Source SHA-256: `1bd07da8f4b72d9471e41c285a3374504e750c8af17f9bea6d091938ae4d5e49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9VYS2?format=txt&versions=13)  
**Locator:** `lines 50-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:13.456029+00:00.  

```text
CC   -!- FUNCTION: Zn(2)-C6 fungal-type transcription factor that has a role in
CC       the establishment of the fungus within the plant and/or the progress of
CC       the disease (PubMed:17462924, PubMed:26817616). Regulates the
CC       expression of virulence factors such as SIX1 and SIX6
CC       (PubMed:26817616). {ECO:0000269|PubMed:17462924,
CC       ECO:0000269|PubMed:26817616}.
```

Source SHA-256: `1bd07da8f4b72d9471e41c285a3374504e750c8af17f9bea6d091938ae4d5e49`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9VYS2?format=txt&versions=13)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:24:13.456029+00:00.  

```text
DR   GO; GO:0008270; F:zinc ion binding; IEA:InterPro.
```

Source SHA-256: `1bd07da8f4b72d9471e41c285a3374504e750c8af17f9bea6d091938ae4d5e49`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 81431-81439`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008270
name: zinc ion binding
namespace: molecular_function
def: "Binding to a zinc ion (Zn)." [GOC:ai]
synonym: "zinc binding" EXACT []
synonym: "Zn binding" EXACT []
is_a: GO:0046914 ! transition metal ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
