# EC_number_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0027.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.4.21.90

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFPMQFTNSAYRQMEPMFAPGPRGQVQPYRPRTKRRQEPQVGNAAIAALANQMSALQLQVAGLAGQARVDRRGPRRVQKSKQKKKNPSNGEKPKEKKKKQKQQEKKGSGGVIKKPRNRPGKEVRISVKRARQSTFPVYHDGAISGYAVLIGSRVFKPAHVKGKIDHPELADIKFQVAEDMDLEAAAYPKSMRDQAAEPATMMDGVYNWEYGTIRVEDNVVIDASGRGKPGDSGRAITDNSGKVVGIVLGGGPDGRRTRLSVIGFDKKMKAREIAYSEAIPWTRAPALLLLPMVIACTYNSNTFDCSKPSCQDCCITAEPKKAMAMLKDNLNDPNYWDLLIAVTTCNSARKKRAVSTSPAAVYDTQILAAHAAASPYRAYCPDCDGTACISPIAIDEVVSSGSDHVLRIRVGSQSGVTAKGGAAGETSLRYLGRDGKVHAADNTRLVVRTTAKCDVLQATGHYILASCPEGQSITVAATLDGTRHQCTTVFEHQVTEKFTRERSKGHHLSDLTKKCTRFSTTPKKSAPYLVDVYDALPISVEISTVVTCNDNQCTVKVPPGTTVKFDKKCKSAAQATVTFTSDSQTFTCEEPVLTAASITQGKPHLRSSMLPSGGKEVKARIPFPFPPETATCRVSVAPLPSITYEESDVLLAGTAKYPVLLTTRNLGFHSNATSEWIQGKYLRRIPVTPQGIELTWGNNAPLHFWSSVRYASGDADAYPWELLVHHTKHHPEYAWAFVGVACGLLVIAVCMFACACNRVRYSLVANTFNPNPPPLTALTAALCCIPGARADQPYLDIIAYLWTNSKVAFGLQCAAPVACVLIVTYALRHCRLCCKSFLGVRGWSALLVILAYVQSCKSYEHTVVVPMDPRAPSYEAVINRNGYDPLKLTIAVNFTVISPTTALEYWTCASVPIVEPPHVGCCTSVSCPSDLSTLHAFTGKAVSDVHCDVHTNVYPLLWGAAHCFCSTENTQVSAVAATVSEFCAQDSERAEAFSVHSSSVTAEVLVTLGEVVTAVHVYVDGVTSARGTDLKIVAGPITTDYSPFDRKVVRIGEEVYNYDWPPYGAGRPGTFGDIQARSTNYVKPNDLYGDIGIEVLQPTNDHVHVAYTYTTSGLLRWLQDAPKPLSVTAPHGCKISANPLLALDCGVGAVPMSINIPDAKFTRKLKDPKPSALKCVVDSCEYGVDYGGAATITYEGHEAGKCGIHSLTPGVPLRTSVVEVVAGANTVKTTFSSPTPEVTLEVEICSAMVTCASECTPPKEHVVATRPRHGSDTGGYISGPAMRWAGGIVGTLAVLFLILAVTYCVVKKCRSKRIRIVKS

[Multiple Choices]
A. 3.4.21.62
B. 3.4.21.90
C. 1.1.1.336
D. 4.2.3.1
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry assigns EC 3.4.21.90 to the capsid component of the structural polyprotein and describes its autocatalytic proteolytic release. The annotation is transferred by similarity from another entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has the pattern of a viral structural polyprotein, including an N-terminal basic region consistent with a capsid component and downstream membrane-spanning regions consistent with envelope proteins. Knowledge of related togavirus/al alphavirus structural polyproteins supports a capsid protease that autocleaves to release the core protein, distinguishing the protease choice B from the dehydrogenase and terpene-synthase choices. The family-level inference also supports B over the other offered protease option, although sequence-only identification is probabilistic.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable viral-polyprotein and capsid-autoprotease pattern meaningfully distinguishes the offered EC choices; it does not require recalling this exact sequence's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives do not present another clearly comparable alphavirus capsid autoprotease EC number.


### Important caveats

- The EC annotation applies to the capsid component within the polyprotein, not necessarily to every component of the full sequence.
- The supporting database annotation is similarity-transferred; the supplied evidence does not establish direct experimental confirmation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has the pattern of a viral structural polyprotein, including an N-terminal basic region consistent with a capsid component and downstream membrane-spanning regions consistent with envelope proteins. Knowledge of related togavirus/al alphavirus structural polyproteins supports a capsid protease that autocleaves to release the core protein, distinguishing the protease choice B from the dehydrogenase and terpene-synthase choices. The family-level inference also supports B over the other offered protease option, although sequence-only identification is probabilistic.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable viral-polyprotein and capsid-autoprotease pattern meaningfully distinguishes the offered EC choices; it does not require recalling this exact sequence's database record."
  },
  "case_id": "EC_number_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.4.21.90 to the capsid component of the structural polyprotein and describes its autocatalytic proteolytic release. The annotation is transferred by similarity from another entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The EC annotation applies to the capsid component within the polyprotein, not necessarily to every component of the full sequence.",
    "The supporting database annotation is similarity-transferred; the supplied evidence does not establish direct experimental confirmation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not present another clearly comparable alphavirus capsid autoprotease EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.4.21.90 to the capsid component of the structural polyprotein and describes its autocatalytic proteolytic release. The annotation is transferred by similarity from another entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has the pattern of a viral structural polyprotein, including an N-terminal basic region consistent with a capsid component and downstream membrane-spanning regions consistent with envelope proteins. Knowledge of related togavirus/al alphavirus structural polyproteins supports a capsid protease that autocleaves to release the core protein, distinguishing the protease choice B from the dehydrogenase and terpene-synthase choices. The family-level inference also supports B over the other offered protease option, although sequence-only identification is probabilistic.",
    "missing_item_specific_fact": "",
    "reason": "A transferable viral-polyprotein and capsid-autoprotease pattern meaningfully distinguishes the offered EC choices; it does not require recalling this exact sequence's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives do not present another clearly comparable alphavirus capsid autoprotease EC number."
  },
  "important_caveats": [
    "The EC annotation applies to the capsid component within the polyprotein, not necessarily to every component of the full sequence.",
    "The supporting database annotation is similarity-transferred; the supplied evidence does not establish direct experimental confirmation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3) annotates the capsid protein domain with EC 3.4.21.90, described as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' The annotation carries evidence code ECO:0000250 (inferred by similarity, transferred from P03315, Semliki Forest virus capsid protein). The sequence matches exactly (1319 AA, SHA-256 match confirmed in both current and historical snapshots). The EC number is correctly assigned to the capsid domain of this structural polyprotein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the well-known alphavirus capsid protein signature motif 'GGGPDGRR' (visible around residues ~130-140: 'GIVLGGGPDGRR'), which is a conserved feature across the Alphavirus genus (SFV, Sindbis, Ross River, etc.). The overall architecture—a ~1300 AA polyprotein with a highly basic N-terminal region (multiple Lys/Arg clusters), followed by hydrophobic transmembrane-like segments in the C-terminal half corresponding to E1/E2/6K glycoproteins—matches the canonical togavirus structural polyprotein (p130) organization. A knowledgeable model recognizing these family-level features would infer: (1) this is an alphavirus structural polyprotein, not an oxidoreductase (eliminating C: 1.1.1.336) or a terpene synthase (eliminating D: 4.2.3.1); (2) the capsid domain of alphaviruses universally carries the autoprotease activity classified as EC 3.4.21.90 (a serine endopeptidase releasing the core protein via a Trp|Ser bond), which is well-documented across multiple alphavirus members. This family-level knowledge distinguishes B (3.4.21.90, the alphavirus capsid autoprotease) from A (3.4.21.62, a different serine endopeptidase not associated with alphavirus capsid processing).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGGPDGRR motif and the polyprotein architecture are transferable features recognized across the Alphavirus family. The EC 3.4.21.90 assignment for the capsid autoprotease is a family-level fact learned from other alphaviruses (SFV, Sindbis, etc.), not a unique annotation for this exact protein. The two clearly wrong options (C, D) are eliminated by basic enzyme-class reasoning, and the A-vs-B distinction is resolved by alphavirus family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (oxidoreductase) and D (lyase/terpene synthase) are clearly incompatible with a structural polyprotein containing a protease domain. The distinction between A (3.4.21.62) and B (3.4.21.90) is resolved by the alphavirus-specific GGGPDGRR motif and the well-established family-level EC assignment for alphavirus capsid autoprotease.


### Important caveats

- The UniProt annotation for EC 3.4.21.90 carries evidence code ECO:0000250 (inferred by similarity from P03315), not direct experimental evidence for this specific SAV3 sequence. However, the motif and architecture are consistent with the family assignment.
- The EC number is annotated for the capsid protein domain within the polyprotein, not for the entire 1319-residue polyprotein as a single enzyme entity.
- The identity of EC 3.4.21.62 (option A) was not independently verified in this review; it is treated as a plausible serine endopeptidase distractor that does not correspond to alphavirus capsid autoprotease.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the well-known alphavirus capsid protein signature motif 'GGGPDGRR' (visible around residues ~130-140: 'GIVLGGGPDGRR'), which is a conserved feature across the Alphavirus genus (SFV, Sindbis, Ross River, etc.). The overall architecture—a ~1300 AA polyprotein with a highly basic N-terminal region (multiple Lys/Arg clusters), followed by hydrophobic transmembrane-like segments in the C-terminal half corresponding to E1/E2/6K glycoproteins—matches the canonical togavirus structural polyprotein (p130) organization. A knowledgeable model recognizing these family-level features would infer: (1) this is an alphavirus structural polyprotein, not an oxidoreductase (eliminating C: 1.1.1.336) or a terpene synthase (eliminating D: 4.2.3.1); (2) the capsid domain of alphaviruses universally carries the autoprotease activity classified as EC 3.4.21.90 (a serine endopeptidase releasing the core protein via a Trp|Ser bond), which is well-documented across multiple alphavirus members. This family-level knowledge distinguishes B (3.4.21.90, the alphavirus capsid autoprotease) from A (3.4.21.62, a different serine endopeptidase not associated with alphavirus capsid processing).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGGPDGRR motif and the polyprotein architecture are transferable features recognized across the Alphavirus family. The EC 3.4.21.90 assignment for the capsid autoprotease is a family-level fact learned from other alphaviruses (SFV, Sindbis, etc.), not a unique annotation for this exact protein. The two clearly wrong options (C, D) are eliminated by basic enzyme-class reasoning, and the A-vs-B distinction is resolved by alphavirus family knowledge."
  },
  "case_id": "EC_number_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3) annotates the capsid protein domain with EC 3.4.21.90, described as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' The annotation carries evidence code ECO:0000250 (inferred by similarity, transferred from P03315, Semliki Forest virus capsid protein). The sequence matches exactly (1319 AA, SHA-256 match confirmed in both current and historical snapshots). The EC number is correctly assigned to the capsid domain of this structural polyprotein."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.90 carries evidence code ECO:0000250 (inferred by similarity from P03315), not direct experimental evidence for this specific SAV3 sequence. However, the motif and architecture are consistent with the family assignment.",
    "The EC number is annotated for the capsid protein domain within the polyprotein, not for the entire 1319-residue polyprotein as a single enzyme entity.",
    "The identity of EC 3.4.21.62 (option A) was not independently verified in this review; it is treated as a plausible serine endopeptidase distractor that does not correspond to alphavirus capsid autoprotease."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (oxidoreductase) and D (lyase/terpene synthase) are clearly incompatible with a structural polyprotein containing a protease domain. The distinction between A (3.4.21.62) and B (3.4.21.90) is resolved by the alphavirus-specific GGGPDGRR motif and the well-established family-level EC assignment for alphavirus capsid autoprotease."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q53AM4 (POLS_SAV3, structural polyprotein of Alphavirus salmon subtype 3) annotates the capsid protein domain with EC 3.4.21.90, described as 'Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.' The annotation carries evidence code ECO:0000250 (inferred by similarity, transferred from P03315, Semliki Forest virus capsid protein). The sequence matches exactly (1319 AA, SHA-256 match confirmed in both current and historical snapshots). The EC number is correctly assigned to the capsid domain of this structural polyprotein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the well-known alphavirus capsid protein signature motif 'GGGPDGRR' (visible around residues ~130-140: 'GIVLGGGPDGRR'), which is a conserved feature across the Alphavirus genus (SFV, Sindbis, Ross River, etc.). The overall architecture—a ~1300 AA polyprotein with a highly basic N-terminal region (multiple Lys/Arg clusters), followed by hydrophobic transmembrane-like segments in the C-terminal half corresponding to E1/E2/6K glycoproteins—matches the canonical togavirus structural polyprotein (p130) organization. A knowledgeable model recognizing these family-level features would infer: (1) this is an alphavirus structural polyprotein, not an oxidoreductase (eliminating C: 1.1.1.336) or a terpene synthase (eliminating D: 4.2.3.1); (2) the capsid domain of alphaviruses universally carries the autoprotease activity classified as EC 3.4.21.90 (a serine endopeptidase releasing the core protein via a Trp|Ser bond), which is well-documented across multiple alphavirus members. This family-level knowledge distinguishes B (3.4.21.90, the alphavirus capsid autoprotease) from A (3.4.21.62, a different serine endopeptidase not associated with alphavirus capsid processing).",
    "missing_item_specific_fact": "",
    "reason": "The GGGPDGRR motif and the polyprotein architecture are transferable features recognized across the Alphavirus family. The EC 3.4.21.90 assignment for the capsid autoprotease is a family-level fact learned from other alphaviruses (SFV, Sindbis, etc.), not a unique annotation for this exact protein. The two clearly wrong options (C, D) are eliminated by basic enzyme-class reasoning, and the A-vs-B distinction is resolved by alphavirus family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (oxidoreductase) and D (lyase/terpene synthase) are clearly incompatible with a structural polyprotein containing a protease domain. The distinction between A (3.4.21.62) and B (3.4.21.90) is resolved by the alphavirus-specific GGGPDGRR motif and the well-established family-level EC assignment for alphavirus capsid autoprotease."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.4.21.90 carries evidence code ECO:0000250 (inferred by similarity from P03315), not direct experimental evidence for this specific SAV3 sequence. However, the motif and architecture are consistent with the family assignment.",
    "The EC number is annotated for the capsid protein domain within the polyprotein, not for the entire 1319-residue polyprotein as a single enzyme entity.",
    "The identity of EC 3.4.21.62 (option A) was not independently verified in this review; it is treated as a plausible serine endopeptidase distractor that does not correspond to alphavirus capsid autoprotease."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 1319,
  "benchmark_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "current_entry_audit": {
    "entryVersion": 102,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-05-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1319,
  "current_source_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q53AM4",
  "selected_historical_entry_version": 100,
  "selected_historical_record_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "selected_historical_source_sequence_length": 1319,
  "selected_historical_source_sequence_sha256": "1a83b6f2b6c943cf3792132f10f55dee70402c04a5e620ae794be320d3dc5f7f",
  "selected_historical_version": {
    "accession": "Q53AM4",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "POLS_SAV3",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q53AM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":102,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-05-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"SAV3\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Kitrinoviricota\",\"Alsuviricetes\",\"Martellivirales\",\"Togaviridae\",\"Alphavirus\"],\"scientificName\":\"Alphavirus salmon subtype 3\",\"synonyms\":[\"Norwegian salmonid alphavirus\"],\"taxonId\":344701}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"p130\"}}],\"contains\":[{\"alternativeNames\":[{\"fullName\":{\"value\":\"Coat protein\"},\"shortNames\":[{\"value\":\"C\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.21.90\"}],\"fullName\":{\"value\":\"Capsid protein\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"p62\"}},{\"fullName\":{\"value\":\"pE2\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Precursor of protein E3/E2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Assembly protein E3\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"E2 envelope glycoprotein\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Spike glycoprotein E2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"6K protein\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"E1 envelope glycoprotein\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Spike glycoprotein E1\"}}}],\"recommendedName\":{\"fullName\":{\"value\":\"Structural polyprotein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.21.90\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P03315\",\"source\":\"UniProtKB\"}],\"name\":\"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:30:59.296476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df",
  "url": "https://rest.uniprot.org/uniprotkb/Q53AM4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H1",
  "excerpt": "ID   POLS_SAV3               Reviewed;        1319 AA.\nAC   Q53AM4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-MAY-2005, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Structural polyprotein;\nDE   AltName: Full=p130;\nDE   Contains:\nDE     RecName: Full=Capsid protein;\nDE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};\nDE     AltName: Full=Coat protein;\nDE              Short=C;\nDE   Contains:\nDE     RecName: Full=Precursor of protein E3/E2;\nDE     AltName: Full=p62;\nDE     AltName: Full=pE2;\nDE   Contains:\nDE     RecName: Full=Assembly protein E3;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E2;\nDE     AltName: Full=E2 envelope glycoprotein;\nDE   Contains:\nDE     RecName: Full=6K protein;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E1;\nDE     AltName: Full=E1 envelope glycoprotein;\nOS   Alphavirus salmon subtype 3 (SAV3) (Norwegian salmonid alphavirus).\nOC   Viruses; Riboviria; Orthornavirae; Kitrinoviricota; Alsuviricetes;\nOC   Martellivirales; Togaviridae; Alphavirus.\nOX   NCBI_TaxID=344701;\nOH   NCBI_TaxID=8022; Oncorhynchus mykiss (Rainbow trout) (Salmo gairdneri).\nOH   NCBI_TaxID=8030; Salmo salar (Atlantic salmon).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Structural polyprotein;\nDE   AltName: Full=p130;\nDE   Contains:\nDE     RecName: Full=Capsid protein;\nDE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};\nDE     AltName: Full=Coat protein;\nDE              Short=C;\nDE   Contains:\nDE     RecName: Full=Precursor of protein E3/E2;\nDE     AltName: Full=p62;\nDE     AltName: Full=pE2;\nDE   Contains:\nDE     RecName: Full=Assembly protein E3;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E2;\nDE     AltName: Full=E2 envelope glycoprotein;\nDE   Contains:\nDE     RecName: Full=6K protein;\nDE   Contains:\nDE     RecName: Full=Spike glycoprotein E1;\nDE     AltName: Full=E1 envelope glycoprotein;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Autocatalytic release of the core protein from the N-terminus\nCC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-\nCC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:02.984412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84",
  "url": "https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
