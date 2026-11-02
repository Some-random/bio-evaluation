# GO_molecular_function_0114

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — serine-type endopeptidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFPMQFTNSAYRQMEPMFAPGPRGQVQPYRPRTKRRQEPQVGNAAIAALANQMSALQLQVAGLAGQARVDRRGPRRVQKSKQKKKNPSNGEKPKEKKKKQKQQEKKGSGGVIKKPRNRPGKEVRISVKRARQSTFPVYHDGAISGYAVLIGSRVFKPAHVKGKIDHPELADIKFQVAEDMDLEAAAYPKSMRDQAAEPATMMDGVYNWEYGTIRVEDNVVIDASGRGKPGDSGRAITDNSGKVVGIVLGGGPDGRRTRLSVIGFDKKMKAREIAYSEAIPWTRAPALLLLPMVIACTYNSNTFDCSKPSCQDCCITAEPKKAMAMLKDNLNDPNYWDLLIAVTTCNSARKKRAVSTSPAAVYDTQILAAHAAASPYRAYCPDCDGTACISPIAIDEVVSSGSDHVLRIRVGSQSGVTAKGGAAGETSLRYLGRDGKVHAADNTRLVVRTTAKCDVLQATGHYILASCPEGQSITVAATLDGTRHQCTTVFEHQVTEKFTRERSKGHHLSDLTKKCTRFSTTPKKSAPYLVDVYDALPISVEISTVVTCNDNQCTVKVPPGTTVKFDKKCKSAAQATVTFTSDSQTFTCEEPVLTAASITQGKPHLRSSMLPSGGKEVKARIPFPFPPETATCRVSVAPLPSITYEESDVLLAGTAKYPVLLTTRNLGFHSNATSEWIQGKYLRRIPVTPQGIELTWGNNAPLHFWSSVRYASGDADAYPWELLVHHTKHHPEYAWAFVGVACGLLVIAVCMFACACNRVRYSLVANTFNPNPPPLTALTAALCCIPGARADQPYLDIIAYLWTNSKVAFGLQCAAPVACVLIVTYALRHCRLCCKSFLGVRGWSALLVILAYVQSCKSYEHTVVVPMDPRAPSYEAVINRNGYDPLKLTIAVNFTVISPTTALEYWTCASVPIVEPPHVGCCTSVSCPSDLSTLHAFTGKAVSDVHCDVHTNVYPLLWGAAHCFCSTENTQVSAVAATVSEFCAQDSERAEAFSVHSSSVTAEVLVTLGEVVTAVHVYVDGVTSARGTDLKIVAGPITTDYSPFDRKVVRIGEEVYNYDWPPYGAGRPGTFGDIQARSTNYVKPNDLYGDIGIEVLQPTNDHVHVAYTYTTSGLLRWLQDAPKPLSVTAPHGCKISANPLLALDCGVGAVPMSINIPDAKFTRKLKDPKPSALKCVVDSCEYGVDYGGAATITYEGHEAGKCGIHSLTPGVPLRTSVVEVVAGANTVKTTFSSPTPEVTLEVEICSAMVTCASECTPPKEHVVATRPRHGSDTGGYISGPAMRWAGGIVGTLAVLFLILAVTYCVVKKCRSKRIRIVKS

[Multiple Choices]
A. DNA nuclease activity
B. G protein-coupled receptor activity
C. peptidase activity
D. serine-type endopeptidase activity
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

> The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.


**Missing item-specific fact**

> The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.


**Reason**

> The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected.


### Important caveats

- The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.
- The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.",
    "reason": "The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C10",
      "C13",
      "H8",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.",
    "The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 1319-aa viral structural polyprotein. Its capsid component is annotated with autocatalytic protease activity, and the catalytic activity is specifically classified as EC 3.4.21.90, consistent with serine-type endopeptidase activity. The support is qualified: the activity is annotated by similarity to a related alphavirus, while the GO assignment is computational (InterPro), not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C5", "C10", "C13", "H8", "H11"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's length, basic N-terminal region, and multiple hydrophobic segments may suggest a viral polyprotein with structural membrane proteins, but those clues do not establish that a component has serine-type endopeptidase activity rather than another peptidase activity.",
    "missing_item_specific_fact": "The needed fact is that this particular structural polyprotein contains a capsid component with autocatalytic serine-protease activity; that functional assignment depends on protein-family annotation or related-protein evidence absent from the input.",
    "reason": "The options make the protease choice plausible, but the supplied sequence does not provide a sufficiently diagnostic catalytic signature or context to establish the specific enzyme class by general reasoning alone. The exact distinction depends on item-specific functional annotation or prior knowledge of this viral polyprotein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The annotated serine-type endopeptidase activity is also peptidase activity, so both options are true at different levels of specificity. D is the more specific and better-supported choice, but the question does not state that the most specific applicable term should be selected."
  },
  "important_caveats": [
    "The sequence represents a polyprotein containing multiple mature viral proteins, so describing one molecular function as the whole precursor's primary function is an oversimplification.",
    "The exact-protein catalytic assignment is supported by similarity to related alphaviruses; this evidence does not establish direct experimental validation for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites.

Citations as saved: [C10](#evidence-c10), [C13](#evidence-c13), [C5](#evidence-c5), [H8](#evidence-h8), [H11](#evidence-h11), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.


**Missing item-specific fact**

> None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.


**Reason**

> A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer.


### Important caveats

- The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.
- The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.
- The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.
- The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.",
    "reason": "A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup."
  },
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C10",
      "C13",
      "C5",
      "H8",
      "H11",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites."
  },
  "important_caveats": [
    "The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.",
    "The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.",
    "The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.",
    "The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (Alphavirus salmon subtype 3 structural polyprotein) explicitly annotates GO:0004252 (serine-type endopeptidase activity) via IEA:InterPro, and lists EC 3.4.21.90 with the catalytic reaction 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' EC 3.4.21.90 falls within the serine endopeptidase class (3.4.21.-). The function comment states the capsid protein 'possesses a protease activity that results in its autocatalytic cleavage.' The annotation is by similarity (ECO:0000250|UniProtKB:P03315) and computationally inferred (IEA:InterPro), not directly experimentally validated for this specific protein, but is well-supported by homology to other alphaviruses. The sequence contains the GDSG motif (residues ~'GDSGRAIT') characteristic of serine protease active sites.",
    "evidence_ids": ["C10", "C13", "C5", "H8", "H11", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the GDSG motif ('GDSGRAIT'), a hallmark of the serine protease catalytic triad active site. The N-terminal ~260 residues adopt a chymotrypsin-like fold (recognizable by the conserved arrangement of beta-strands and the catalytic triad geometry implied by the His-Asp-Ser spacing). The protein is a polyprotein undergoing autocatalytic internal cleavage, which is by definition endopeptidase activity (cleaving internal peptide bonds, not terminal residues). Together, the GDSG serine-nucleophile motif plus internal autocatalytic cleavage mechanism specifically support 'serine-type endopeptidase activity' (D) over the generic 'peptidase activity' (C). Options A (DNA nuclease) and B (GPCR) are eliminated by basic biology: this is an RNA virus structural polyprotein with no nucleic-acid-cleaving or seven-transmembrane-receptor architecture.",
    "missing_item_specific_fact": "None critically missing. The GDSG motif is visible in the supplied sequence. The distinction between C and D rests on recognizing the serine catalytic mechanism from this motif, which is general biological knowledge about protease classification, not a protein-specific database lookup.",
    "reason": "A model with knowledge of serine protease sequence signatures (GDSG/GDSGGP motif) and the definition of endopeptidase (internal bond hydrolysis) can reason from the sequence to select D over C. The GDSG motif is directly present in the supplied sequence. Eliminating A and B requires only recognizing this is not a nuclease or GPCR. The remaining C-vs-D distinction is resolved by the serine-specific motif, which is general enzymology knowledge rather than an item-specific annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0004252 (serine-type endopeptidase activity) is_a GO:0008233 (peptidase activity), so C is technically true as a parent term. However, the question asks for the option that 'best describes' the primary molecular function, and GO annotation practice favors the most specific term. The GDSG motif specifically identifies the serine mechanism, making D strictly more informative than C. This is a minor hierarchy ambiguity rather than a genuine defect; D is clearly the better answer."
  },
  "important_caveats": [
    "The GO:0004252 annotation is IEA:InterPro (computational inference), and the catalytic activity is annotated by similarity to P03315 (Sindbis virus), not by direct experimental measurement on SAV3.",
    "The protein is a polyprotein with multiple sub-protein functions (structural, RNA-binding, channel/viroporin, fusion). The 'primary molecular function' framing is somewhat reductive; structural molecule activity (GO:0005198) is also annotated but not offered as a choice.",
    "The sequence is 1319 AA (full polyprotein); the serine protease activity resides only in the N-terminal capsid domain (~260 residues). The question does not specify which domain's function to consider.",
    "The UniProt entry was first public in June 2025; the benchmark author source snapshot is unknown. Sequence match is confirmed for both current and historical (v100) records."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `ontology_parent_relation_traced_with_evidence_qualification`.

> The supplied ontology paths link serine-type endopeptidase GO:0004252 through endopeptidase GO:0004175 to peptidase GO:0008233. C10/H8 assign protease activity by similarity and C13/H11 use IEA:InterPro.

**Remaining uncertainty:** The nested term relationship is traceable. The protein activity and exact specificity remain qualified by similarity/computational evidence; wording interpretation is not resolved by citation presence.

Evidence checked: [C1](#evidence-c1), [C5](#evidence-c5), [C10](#evidence-c10), [C13](#evidence-c13), [H8](#evidence-h8), [H11](#evidence-h11).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q53AM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 100. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
"Q53AM4"
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commentType":"FUNCTION","molecule":"Capsid protein","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"},{"evidenceCode":"ECO:0000250","id":"P03316","source":"UniProtKB"},{"evidenceCode":"ECO:0000250","id":"P27284","source":"UniProtKB"}],"value":"Forms an icosahedral capsid with a T=4 symmetry composed of 240 copies of the capsid protein surrounded by a lipid membrane through which penetrate 80 spikes composed of trimers of E1-E2 heterodimers (By similarity). The capsid protein binds to the viral RNA genome at a site adjacent to a ribosome binding site for viral genome translation following genome release (By similarity). Possesses a protease activity that results in its autocatalytic cleavage from the nascent structural protein (By similarity). Following its self-cleavage, the capsid protein transiently associates with ribosomes, and within several minutes the protein binds to viral RNA and rapidly assembles into icosahedric core particles (By similarity). The resulting nucleocapsid eventually associates with the cytoplasmic domain of the spike glycoprotein E2 at the cell membrane, leading to budding and formation of mature virions (By similarity). In case of infection, new virions attach to target cells and after clathrin-mediated endocytosis their membrane fuses with the host endosomal membrane (By similarity). This leads to the release of the nucleocapsid into the cytoplasm, followed by an uncoating event necessary for the genomic RNA to become accessible (By similarity). The uncoating might be triggered by the interaction of capsid proteins with ribosomes (By similarity). Binding of ribosomes would release the genomic RNA since the same region is genomic RNA-binding and ribosome-binding (By similarity). Specifically inhibits interleukin-1 receptor-associated kinase 1/IRAK1-dependent signaling during viral entry, representing a means by which the alphaviruses may evade innate immune detection and activation prior to viral gene expression (By similarity)"}]}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.90","evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"}],"name":"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond."}}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"database":"GO","id":"GO:0004252","properties":[{"key":"GoTerm","value":"F:serine-type endopeptidase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 119-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Autocatalytic release of the core protein from the N-terminus
CC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-
CC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 223-223`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
DR   GO; GO:0004252; F:serine-type endopeptidase activity; IEA:InterPro.
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 38518-38819`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004252
name: serine-type endopeptidase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain by a catalytic mechanism that involves a catalytic triad consisting of a serine nucleophile that is activated by a proton relay involving an acidic residue (e.g. aspartate or glutamate) and a basic residue (usually histidine)." [GOC:mah, https://www.ebi.ac.uk/merops/about/glossary.shtml#CATTYPE]
subset: goslim_chembl
synonym: "blood coagulation factor activity" RELATED []
synonym: "serine elastase activity" RELATED [GOC:krc]
xref: EC:3.4.21.-
xref: EC:3.4.21.1
xref: EC:3.4.21.10
xref: EC:3.4.21.102
xref: EC:3.4.21.20
xref: EC:3.4.21.21
xref: EC:3.4.21.22
xref: EC:3.4.21.26
xref: EC:3.4.21.27
xref: EC:3.4.21.34
xref: EC:3.4.21.35
xref: EC:3.4.21.36
xref: EC:3.4.21.38
xref: EC:3.4.21.39
xref: EC:3.4.21.4
xref: EC:3.4.21.41
xref: EC:3.4.21.42
xref: EC:3.4.21.43
xref: EC:3.4.21.45
xref: EC:3.4.21.46
xref: EC:3.4.21.47
xref: EC:3.4.21.48
xref: EC:3.4.21.5
xref: EC:3.4.21.53
xref: EC:3.4.21.54
xref: EC:3.4.21.59
xref: EC:3.4.21.6
xref: EC:3.4.21.61
xref: EC:3.4.21.62
xref: EC:3.4.21.68
xref: EC:3.4.21.69
xref: EC:3.4.21.7
xref: EC:3.4.21.71
xref: EC:3.4.21.73
xref: EC:3.4.21.75
xref: EC:3.4.21.78
xref: EC:3.4.21.79
xref: EC:3.4.21.83
xref: EC:3.4.21.88
xref: EC:3.4.21.9
xref: EC:3.4.21.92
xref: EC:3.4.21.93
xref: EC:3.4.21.94
xref: Reactome:R-HSA-114697 "Activated thrombin (factor IIa) cleaves PAR3,4, activating them"
xref: Reactome:R-HSA-1181152 "Cleavage of NODAL proprotein"
xref: Reactome:R-HSA-139893 "Granzyme-B activates BID by cleavage"
xref: Reactome:R-HSA-140599 "factor XIII -> factor XIII cleaved tetramer + 2 factor XIII A activation peptides"
xref: Reactome:R-HSA-140664 "prothrombin -> activated thrombin (factor IIa) + thrombin activation peptide (prothrombinase catalyst)"
xref: Reactome:R-HSA-140696 "factor V -> factor Va + factor V activation peptide (thrombin catalyst)"
xref: Reactome:R-HSA-140700 "prothrombin -> activated thrombin (factor IIa) + thrombin activation peptide (Xa catalyst)"
xref: Reactome:R-HSA-140736 "factor X -> factor Xa + factor X activation peptide (TF:F7a catalyst)"
xref: Reactome:R-HSA-140769 "factor VII -> factor VIIa"
xref: Reactome:R-HSA-140777 "factor X -> factor Xa + factor X activation peptide (TF:F7 catalyst)"
xref: Reactome:R-HSA-140823 "factor IX -> factor IXa + factor IX activation peptide (TF:F7a catalyst)"
xref: Reactome:R-HSA-140840 "fibrinogen -> fibrin monomer + 2 fibrinopeptide A + 2 fibrinopeptide B"
xref: Reactome:R-HSA-140870 "thrombin:antithrombin III:heparin -> thrombin:cleaved antithrombin III:heparin"
xref: Reactome:R-HSA-141026 "Activated protein C cleaves factor Va to factor Vi intermediate form"
xref: Reactome:R-HSA-141040 "Activated thrombin:thrombomodulin cleaves PROCR:Protein C to PROCR:Activated protein C"
xref: Reactome:R-HSA-1454843 "E-cadherin degradation by MMP3, MMP7 and plasmin"
xref: Reactome:R-HSA-1474197 "Collagen type II degradation by MMP1,3,8,13,PRSS2"
xref: Reactome:R-HSA-1566962 "Elastin degradation by elastin-degrading extracellular proteinases"
xref: Reactome:R-HSA-1566979 "Laminin-332 degradation by laminin-322 degrading extracellular proteinases"
xref: Reactome:R-HSA-1566981 "Fibronectin degradation by MMP1, 3, 7, 12, 13, 19, CTSS"
xref: Reactome:R-HSA-158137 "factor VIII:von Willibrand factor multimer -> factor VIIIa + factor VIIIa B A3 acidic polypeptide + von Willibrand factor multimer"
xref: Reactome:R-HSA-158164 "factor X -> factor Xa + factor X activation peptide (VIIIa:IXa catalyst)"
xref: Reactome:R-HSA-158300 "factor XI:platelet glycoprotein (GP) Ib:IX:V complex -> factor XIa:platelet glycoprotein (GP) Ib:IX:V complex (XIIa catalyst)"
xref: Reactome:R-HSA-158311 "kallikrein:kininogen:C1q binding protein tetramer -> kallikrein + activated kininogen:C1q binding protein tetramer + bradykinin"
xref: Reactome:R-HSA-158313 "factor XII -> factor XIIa"
xref: Reactome:R-HSA-158333 "factor IX -> factor IXa + factor IX activation peptide (factor XIa catalyst)"
xref: Reactome:R-HSA-158419 "factor XI:platelet glycoprotein (GP) Ib:IX:V complex -> factor XIa:platelet glycoprotein (GP) Ib:IX:V complex (thrombin catalyst)"
xref: Reactome:R-HSA-158744 "crosslinked fibrin multimer:tissue plasminogen activator (two-chain):plasminogen -> crosslinked fibrin multimer:tissue plasminogen activator (two-chain) + plasmin"
xref: Reactome:R-HSA-158747 "crosslinked fibrin multimer:tissue plasminogen activator (one-chain) -> crosslinked fibrin multimer:tissue plasminogen activator (two-chain)"
xref: Reactome:R-HSA-158750 "crosslinked fibrin multimer:tissue plasminogen activator (one-chain):plasminogen -> crosslinked fibrin multimer:tissue plasminogen activator (one-chain) + plasmin"
xref: Reactome:R-HSA-158766 "fibrin multimer, crosslinked -> fibrin digestion products (plasmin)"
xref: Reactome:R-HSA-158925 "plasminogen:histidine-rich glycoprotein -> plasmin + histidine-rich glycoprotein (uPA [two-chain] catalyst)"
xref: Reactome:R-HSA-158942 "urokinase plasminogen activator (one-chain):uPAR -> urokinase plasminogen activator (two-chain):uPAR"
xref: Reactome:R-HSA-158982 "plasminogen:histidine-rich glycoprotein -> plasmin + histidine-rich glycoprotein (uPA [one-chain] catalyst)"
xref: Reactome:R-HSA-1592270 "NID1 degradation by MMP1, 9, 12, ELANE"
xref: Reactome:R-HSA-1592278 "Autocatalytic activation of proMMP2"
xref: Reactome:R-HSA-1592297 "Full activation of MMP1"
xref: Reactome:R-HSA-1592314 "HSPG2 (perlecan) degradation by MMP3, plasmin, (MMP12)"
xref: Reactome:R-HSA-1592316 "Initial activation of proMMP1"
xref: Reactome:R-HSA-1592362 "Activation of proMMP7 by MMP3"
xref: Reactome:R-HSA-1592371 "Initial activation of proMMP3"
xref: Reactome:R-HSA-1592398 "Activation of proMMP8"
xref: Reactome:R-HSA-1592436 "Initial activation of proMMP9 by MMPs"
xref: Reactome:R-HSA-159728 "Furin cleaves pro-prothrombin to prothrombin"
xref: Reactome:R-HSA-159733 "Furin cleaves pro-factor X to factor X"
xref: Reactome:R-HSA-159771 "Furin cleaves pro-protein C to protein C"
xref: Reactome:R-HSA-159773 "Furin cleaves pro-protein S to protein S"
xref: Reactome:R-HSA-159796 "Furin cleaves pro-factor IX to factor IX"
xref: Reactome:R-HSA-159868 "Furin cleaves pro-factor VII to factor VII"
xref: Reactome:R-HSA-1602458 "Activation of proMMP10"
xref: Reactome:R-HSA-1602466 "Activation of MT-MMPs by FURIN"
xref: Reactome:R-HSA-1602473 "Autocatalytic activation of MMP1"
xref: Reactome:R-HSA-1602484 "Activation of proMMP11 by FURIN"
xref: Reactome:R-HSA-1602488 "Initial activation of proMMP13 by plasmin and trypsin"
xref: Reactome:R-HSA-1604359 "Initial activation of proMMP2 by MMP1, 7"
xref: Reactome:R-HSA-1604360 "Initial activation of proMMP2 by MMP14"
xref: Reactome:R-HSA-1604368 "Autocatalytic activation of bound proMMP2"
xref: Reactome:R-HSA-1604690 "Activation of MMP9 intermediate form by MMPs"
xref: Reactome:R-HSA-1604712 "Initial activation of proMMP7 by trypsin"
xref: Reactome:R-HSA-1604722 "Activation of proMMP9 by proteases"
xref: Reactome:R-HSA-1604731 "Autocatalytic activation of MMP3"
xref: Reactome:R-HSA-1604732 "Autocatalytic activation of proMMP13"
xref: Reactome:R-HSA-1604741 "Initial activation of proMMP13 by MMP14 (MT1-MMP)"
xref: Reactome:R-HSA-1604752 "Initial activation of proMMP13 by MMP3"
xref: Reactome:R-HSA-1604763 "Autocatalytic activation of MMP7"
xref: Reactome:R-HSA-163798 "Furin cleaves pro-protein Z to protein Z"
xref: Reactome:R-HSA-163843 "Furin cleaves pro-GAS6 to GAS6"
xref: Reactome:R-HSA-1655842 "S1P hydrolyzes SREBP1A,1C,2"
xref: Reactome:R-HSA-166753 "Conversion of C4 into C4a and C4b"
xref: Reactome:R-HSA-166792 "Conversion of C2 into C2a and C2b"
xref: Reactome:R-HSA-166817 "Cleavage of C3 by C3 convertases"
xref: Reactome:R-HSA-170844 "Latent TGF-beta-1 is cleaved by FURIN"
xref: Reactome:R-HSA-171288 "Cleavage of the viral Env gp160 precursor polyprotein"
xref: Reactome:R-HSA-173626 "Activation of C1r"
xref: Reactome:R-HSA-173631 "Activation of C1s"
xref: Reactome:R-HSA-173680 "Activation of C5"
xref: Reactome:R-HSA-173745 "Factor D cleaves C3(H2O)-bound Factor B"
xref: Reactome:R-HSA-174551 "Formation of alternative pathway C5 convertase"
xref: Reactome:R-HSA-1799329 "Signal peptidase hydrolyzes signal peptide from ribosome-associated nascent protein"
xref: Reactome:R-HSA-183122 "Factor D cleaves C3b-bound Factor B"
xref: Reactome:R-HSA-183130 "C3(H2O):Factor Bb cleaves C3 to C3b and C3a"
xref: Reactome:R-HSA-186785 "PDGF-AA clevage by Furin"
xref: Reactome:R-HSA-187020 "Part of pro-beta-NGF is processed to mature beta-NGF"
xref: Reactome:R-HSA-1912369 "NOTCH precursor cleaved to form mature NOTCH"
xref: Reactome:R-HSA-1912372 "Fringe-modified Pre-NOTCH is cleaved by FURIN"
xref: Reactome:R-HSA-2022411 "Cathepsin G hydrolyzes AGT(25-34) (Angiotensin-(1-10)) to AGT(25-32) (Angiotensin-(1-8))"
xref: Reactome:R-HSA-2129357 "Fibrillin C-terminal processing"
xref: Reactome:R-HSA-2168923 "Collagen type XVIII endostatin release"
xref: Reactome:R-HSA-2168960 "Collagen type XVII ectodomain shedding"
xref: Reactome:R-HSA-2172405 "Collagen type XXIII ectodomain shedding"
xref: Reactome:R-HSA-2214330 "Cleavage of collagen VII NC2 region by BMP1"
xref: Reactome:R-HSA-2471621 "Endostatin degradation by cathepsins"
xref: Reactome:R-HSA-2471842 "Collagen type XXV ectomain shedding"
xref: Reactome:R-HSA-2482180 "Collagen type VIII degradation by ELANE"
xref: Reactome:R-HSA-2514772 "Fibrillin-1 degradation by MMP3, CTSK, CTSL2"
xref: Reactome:R-HSA-2514823 "Fibrillin-1 degradation by ELANE"
xref: Reactome:R-HSA-2534160 "HSPG2 (perlecan) degradation by MMP13, CTSS"
xref: Reactome:R-HSA-2534206 "E-cadherin degradation by PS1:NCSTN (Gamma-secretase)"
xref: Reactome:R-HSA-2534260 "E-cadherin degradation by caspase-3 and calpain-1"
xref: Reactome:R-HSA-265301 "Corticotropin cleavage from POMC"
xref: Reactome:R-HSA-3244626 "DENV protease NS2B3 cleaves STING"
xref: Reactome:R-HSA-3266557 "Factor I cleaves iC3b"
xref: Reactome:R-HSA-3785684 "Fibronectin degradation by CTSG"
xref: Reactome:R-HSA-3788061 "Fibronectin degradation by ADAM8"
xref: Reactome:R-HSA-381135 "MBTPS1 (S1P) cleaves ATF6 (ATF6-alpha)"
xref: Reactome:R-HSA-381446 "Thrombin proteolyzes IGF:IGFBP3:ALS"
xref: Reactome:R-HSA-381461 "Plasmin proteolyzes IGF:IGFBP-3:ALS"
xref: Reactome:R-HSA-381466 "Prostate-specific Antigen proteolyzes IGF:IGFBP3:ALS"
xref: Reactome:R-HSA-3814820 "HSPG2 (perlecan) is cleaved by BMP1, TLL1, TLL2, Cathepsin L1"
xref: Reactome:R-HSA-381500 "Cathepsin G proteolyzes IGF:IGFBP3:ALS"
xref: Reactome:R-HSA-381798 "PCSK1 hydrolyzes Proglucagon to Glucagon-like Peptide-1"
xref: Reactome:R-HSA-382061 "Extracellular processing of novel PDGFs"
xref: Reactome:R-HSA-3928657 "MMP2,9 cleave EPHB"
xref: Reactome:R-HSA-400459 "Signal peptidase hydrolyzes preproGLP-1 to proGLP-1"
xref: Reactome:R-HSA-400492 "PCSK1 hydrolyzes proGIP to GIP"
xref: Reactome:R-HSA-400496 "Signal peptidase hydrolyzes preproGIP to proGIP"
xref: Reactome:R-HSA-422021 "PCSK1 hydrolyzes acyl Proghrelin to acyl Ghrelin"
xref: Reactome:R-HSA-422051 "Cleavage of the signal peptide of Preproghrelin"
xref: Reactome:R-HSA-5210912 "Furin cleaves ANTXR2-bound pagA to yield pagA(197-794)"
xref: Reactome:R-HSA-5210935 "Furin cleaves ANTXR1-bound pagA to yield pagA(197-794)"
xref: Reactome:R-HSA-5578783 "CORIN(802-1042) hydrolyses NPPA to form NPPA(124-151)"
xref: Reactome:R-HSA-5591040 "Activated protein C cleaves Factor Va intermediate form for Factor Va"
xref: Reactome:R-HSA-5607002 "Activated protein C cleaves factor VIIIa"
xref: Reactome:R-HSA-5691512 "APEH hydrolyses NAc-Ser-protein"
xref: Reactome:R-HSA-6800198 "HPN heterodimer cleaves pro-MST1 to form MST1 dimer"
xref: Reactome:R-HSA-6800200 "HPN heterodimer cleaves pro-HGF to form HGF dimer"
xref: Reactome:R-HSA-6800299 "HGFAC cleaves pro-HGF to form HGF dimer"
xref: Reactome:R-HSA-6801687 "PRTN3 cleaves CAMP(31-170) to generate CAMP(134-170)"
xref: Reactome:R-HSA-6807224 "Furin cleaves pro-BGLAP to BGLAP"
xref: Reactome:R-HSA-8849826 "ST14 hydrolyzes and activates KLK5"
xref: Reactome:R-HSA-8849857 "KLK5 cleaves and activates CELA2"
xref: Reactome:R-HSA-8850831 "KLK5 cleaves and activates KLK8"
xref: Reactome:R-HSA-8852716 "Thrombin, ELANE cleave C5"
xref: Reactome:R-HSA-8855825 "HTRA1 hydrolyzes ACAN (Aggrecan)"
xref: Reactome:R-HSA-8865275 "PDGF-BB clevage by Furin"
xref: Reactome:R-HSA-8865276 "PDGF-AB clevage by Furin"
xref: Reactome:R-HSA-8874145 "MBTPS1 (S1P) cleaves ATF6B (ATF6-beta)"
xref: Reactome:R-HSA-8874186 "MBTPS1 (S1P) cleaves CREB3L4"
xref: Reactome:R-HSA-8874204 "MBTPS1 (S1P) cleaves CREB3"
xref: Reactome:R-HSA-8874205 "MBTPS1 (S1P) cleaves CREB3L2"
xref: Reactome:R-HSA-8874206 "MBTPS1 (S1P) cleaves CREB3L3"
xref: Reactome:R-HSA-8874212 "MBTPS1 (S1P) cleaves CREB3L1"
xref: Reactome:R-HSA-9023178 "PCSK2 cleaves Insulin(57-110) to yield Insulin(90-110) and C-peptide (Insulin(57-89))"
xref: Reactome:R-HSA-9023196 "PCSK1 cleaves proinsulin to yield Insulin(25-56) and Insulin(57-110)"
xref: Reactome:R-HSA-9023626 "DPP4(39-766) hydrolyzes Glucose-dependent Insulinotropic Polypeptide (GIP)"
xref: Reactome:R-HSA-9023627 "DPP4(1-766) hydrolyzes Glucose-dependent Insulinotropic Polypeptide (GIP)"
xref: Reactome:R-HSA-9023632 "DPP4(39-766) hydrolyzes Glucagon-like Peptide-1 (GLP-1)"
xref: Reactome:R-HSA-9023633 "DPP4(1-766) hydrolyzes Glucagon-like Peptide-1 (GLP-1)"
xref: Reactome:R-HSA-9033490 "TYSND1 cleaves PHYH"
xref: Reactome:R-HSA-9033506 "TYSND1 cleaves AGPS"
xref: Reactome:R-HSA-9033515 "TYSND1 cleaves ACOX1"
xref: Reactome:R-HSA-9033520 "TYSND1 cleaves TYSND1"
xref: Reactome:R-HSA-9033524 "TYSND1 cleaves SCP2"
xref: Reactome:R-HSA-9033529 "TYSND1 cleaves ACAA1"
xref: Reactome:R-HSA-9033530 "TYSND1 cleaves HSD17B4"
xref: Reactome:R-HSA-9653249 "Cleavage of factor XII variant by activated thrombin"
xref: Reactome:R-HSA-9655046 "Cleavage of FXII variant by KLKB1"
xref: Reactome:R-HSA-9662786 "FURIN cleaves ADAM17"
xref: Reactome:R-HSA-9666383 "F8 variant is not cleaved by thrombin"
xref: Reactome:R-HSA-9668253 "Hyperactivation of factor X by FVIIIa:FIXa R384L"
xref: Reactome:R-HSA-9668365 "FVIIIa variant:FIXa does not convert FX to the active FXa"
xref: Reactome:R-HSA-9670874 "FIXa variant:FVIIIa does not convert FX to the active FXa"
xref: Reactome:R-HSA-9673223 "FIX(29-461) variant is not activated (factor XIa catalyst)"
xref: Reactome:R-HSA-9686710 "Cleavage of S protein into S1:S2"
xref: Reactome:R-HSA-9686731 "TMPRSS2 Mediated SARS-CoV-1 Spike Protein Cleavage and Endocytosis"
xref: Reactome:R-HSA-9694287 "Cleavage of S protein into S1:S2"
xref: Reactome:R-HSA-9694661 "TMPRSS2 Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis"
xref: Reactome:R-HSA-9698988 "Direct Host Cell Membrane Membrane Fusion and Release of SARS-CoV-2 Nucleocapsid"
xref: Reactome:R-HSA-9699007 "FURIN Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis"
xref: Reactome:R-HSA-9708859 "Activated thrombin (factor IIa) cleaves F2R (PAR1), activating it"
xref: Reactome:R-HSA-9710106 "ELANE cleaves GSDMD"
xref: Reactome:R-HSA-9710263 "GZMB cleaves GSDME"
xref: Reactome:R-HSA-976743 "Factor I inactivates plasma Factor H-bound C3b"
xref: Reactome:R-HSA-9769949 "FURIN Mediated SARS-CoV-2 Spike Protein Cleavage"
xref: Reactome:R-HSA-9770187 "S2 Cleavage by TMPRSS2 Exposes S2' Initiating Cell-Cell Fusion"
xref: Reactome:R-HSA-977371 "Factor I inactivates Factor H-boundC3b"
xref: Reactome:R-HSA-977615 "Factor I inactivates MCP/CR1-bound C4b/C3b"
xref: Reactome:R-HSA-9816275 "CDH1 is proteolytically cleaved in Golgi"
xref: Reactome:R-HSA-9829030 "Nascent F signal peptide is cleaved at ER membrane"
xref: Reactome:R-HSA-9829200 "F0 is cleaved, releasing F1, F2, F(110-136)"
xref: Reactome:R-HSA-9830805 "Nascent sG localizes to ER lumen, gets glycosylated"
xref: Reactome:R-HSA-9830882 "Nascent G signal peptide is cleaved at ER membrane"
xref: Reactome:R-HSA-9839367 "TGFBR3_mem cleavage by MMPs"
xref: Reactome:R-HSA-9911236 "ELANE cleaves NOTCH2NLA"
xref: Reactome:R-HSA-9911383 "LepB cleaves prepro-STa"
xref: Reactome:R-HSA-9912368 "LepB cleaves pre-EltA"
xref: Reactome:R-HSA-9912371 "LepB cleaves pre-EltB"
xref: Reactome:R-HSA-9913329 "Autoproteolysis of DAG1 to alpha and beta chains"
xref: Reactome:R-HSA-9918772 "Dengue polyprotein cis-auto-cleaves"
xref: Reactome:R-HSA-9918780 "Unknown peptidase cleaves NS1-NS2A"
xref: Reactome:R-HSA-9918787 "NS2B3 cleaves C-prM-E-NS1-NS2A"
xref: Reactome:R-HSA-9918795 "Signalase cleaves prM-E-NS1-NS2A"
xref: Reactome:R-HSA-9918813 "NS2B3 cleaves NS4AB"
xref: Reactome:R-HSA-9918817 "NS2B3 cleaves polyprotein"
xref: Reactome:R-HSA-9918823 "NS345:NS2B cleaves NS345"
xref: Reactome:R-HSA-9918871 "Signalase cleaves prepro-NS4B"
xref: Reactome:R-HSA-9918876 "NS2B3 cleaves prepro-C at the C-prM junction"
xref: Reactome:R-HSA-9919050 "Furin cleaves prM:E"
xref: Reactome:R-HSA-9921595 "NS2B3 cleaves FAM134B"
xref: Reactome:R-HSA-9921689 "NS3 cleaves GrpEL1"
xref: Reactome:R-HSA-9926936 "EspC(54-1018) cleaves hemoglobin"
xref: Reactome:R-HSA-9926963 "Hbp cis-autocleaves"
xref: Reactome:R-HSA-9927009 "Hbp(53-1100) cleaves hemoglobin"
xref: Reactome:R-HSA-9932162 "Removal of CDH1 signal peptide"
xref: Reactome:R-HSA-9947496 "ACOT2 cleaves NS345"
is_a: GO:0004175 ! endopeptidase activity
is_a: GO:0008236 ! serine-type peptidase activity
property_value: skos:exactMatch EC:3.4.21.-
property_value: skos:narrowMatch EC:3.4.21.1
property_value: skos:narrowMatch EC:3.4.21.10
property_value: skos:narrowMatch EC:3.4.21.102
property_value: skos:narrowMatch EC:3.4.21.20
property_value: skos:narrowMatch EC:3.4.21.21
property_value: skos:narrowMatch EC:3.4.21.22
property_value: skos:narrowMatch EC:3.4.21.26
property_value: skos:narrowMatch EC:3.4.21.27
property_value: skos:narrowMatch EC:3.4.21.34
property_value: skos:narrowMatch EC:3.4.21.35
property_value: skos:narrowMatch EC:3.4.21.36
property_value: skos:narrowMatch EC:3.4.21.38
property_value: skos:narrowMatch EC:3.4.21.39
property_value: skos:narrowMatch EC:3.4.21.4
property_value: skos:narrowMatch EC:3.4.21.41
property_value: skos:narrowMatch EC:3.4.21.42
property_value: skos:narrowMatch EC:3.4.21.43
property_value: skos:narrowMatch EC:3.4.21.45
property_value: skos:narrowMatch EC:3.4.21.46
property_value: skos:narrowMatch EC:3.4.21.47
property_value: skos:narrowMatch EC:3.4.21.48
property_value: skos:narrowMatch EC:3.4.21.5
property_value: skos:narrowMatch EC:3.4.21.53
property_value: skos:narrowMatch EC:3.4.21.54
property_value: skos:narrowMatch EC:3.4.21.59
property_value: skos:narrowMatch EC:3.4.21.6
property_value: skos:narrowMatch EC:3.4.21.61
property_value: skos:narrowMatch EC:3.4.21.62
property_value: skos:narrowMatch EC:3.4.21.68
property_value: skos:narrowMatch EC:3.4.21.69
property_value: skos:narrowMatch EC:3.4.21.7
property_value: skos:narrowMatch EC:3.4.21.71
property_value: skos:narrowMatch EC:3.4.21.73
property_value: skos:narrowMatch EC:3.4.21.75
property_value: skos:narrowMatch EC:3.4.21.78
property_value: skos:narrowMatch EC:3.4.21.79
property_value: skos:narrowMatch EC:3.4.21.83
property_value: skos:narrowMatch EC:3.4.21.88
property_value: skos:narrowMatch EC:3.4.21.9
property_value: skos:narrowMatch EC:3.4.21.92
property_value: skos:narrowMatch EC:3.4.21.93
property_value: skos:narrowMatch EC:3.4.21.94

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
