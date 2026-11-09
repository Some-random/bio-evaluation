# LiveProteinBench: evaluating the evaluation

We reviewed the questions in our evaluation set to understand whether the benchmark can be scored reliably. We also compared model answers to identify skills that could guide protein training data.

## Are the questions reliable?

Two AI reviewers identified three types of questions for inspection:

- **Possible multiple answers: 4.95%.**
- **A protein-specific fact may be needed: 3.00%.**
- **The answer key may conflict with the evidence: 0.69%.**

These are reviewer flags, not confirmed error rates. The categories overlap.

<details>
<summary>Example: a protein that can both cut and transfer</summary>

**Task:** Choose the protein’s molecular function.

**Protein sequence:**

```text
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM
```

**Choices, explained in simpler language:**

- A. Break down GTP, an energy-carrying molecule *(GTPase activity)*.
- B. Transfer sugar units from one molecule to another *(glycosyltransferase activity)*.
- C. Store nutrients *(nutrient reservoir activity)*.
- D. Cut chemical bonds involving sugars *(hydrolase activity, acting on glycosyl bonds)*.

The explanations before the parentheses are paraphrases; the original choices are in parentheses.

**Author’s answer:** B.

**Why it was flagged:** Both reviewers pointed to an annotation describing a protein that can both **cut chitin**, a sugar-containing material, and **transfer chitin to another molecule**. That makes both B and D worth examining. The strength and scope of the underlying evidence still matter.

</details>

<details>
<summary>Example: distinguishing nearby temperatures</summary>

**Task:** Choose the protein’s optimal temperature.

**Protein sequence:**

```text
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP
```

**Choices:**

- A. 24–29°C
- B. 30°C
- C. 56°C
- D. 34°C

**Author’s answer:** B, 30°C.

**Why it was flagged:** The reviewers thought that sequence and family knowledge might suggest a moderate temperature, but they did not find a clear basis in the question to distinguish 30°C from 34°C or the nearby range. This is a reviewer judgment, not proof that the answer cannot be inferred.

</details>

<details>
<summary>Example: a location that may not be among the choices</summary>

**Task:** Choose where the protein is located.

**Protein sequence:**

```text
MSLLYGLLILAFTRSCLVVGQCSINIPDDLKGEEAPVILVKTGNNVKLFRPEEKTTTFPKGTELLLACTGEGNGLKSNGQETTTLSCNGNQFESAAKEKLKDMSCKSMAKAVVEQTTKRCMGNDFNLYEAGYKVNGKFYGSVYDICYNGKGQSSGYTHNFIYGRTWKYKLPEKPYEHYSSRDPQAGKDLDKLYKEQKERFKNTKVNGKPLLDDEHYFTEGQLTPDTSIITGADKLSTYDYANIAPLFKDIYDGNIWRYENMTQELADQRQATFEEYTGGFYSYEVEKWKPIGLDNAEFPTHRVPKYIYKLVVDTESKDGIVFVTLNDPYHKSPASENLCKDICSEANINEPDFKNVEKGYTICCSYGDFGNRIRTLPKDIHVKGLLKY
```

**Choices:**

- A. Perikaryon
- B. Centrosome
- C. Nucleus
- D. tRNA methyltransferase complex

**Author’s answer:** C, nucleus.

**Why it was flagged:** Both reviewers pointed to experimental evidence describing the protein as **secreted outside the cell**. The nucleus annotation in the matched record was computationally inferred. They judged the evidence inconsistent with the intended primary location; the question does not offer “outside the cell” as a choice.

</details>

[See all questions flagged for multiple defensible choices](multiple_defensible_by_both_86_20261104.md) · [See all questions flagged as lookup-dependent](lookup_dependent_52_20261104.md) · [See answer-key exceptions](../LIVEPROTEINBENCH_ANSWER_KEY_EXCEPTIONS.md)

## What skills do models need?

We collected **1,289 candidate skill descriptions** across protein-problem categories by comparing saved answers where the teacher matched the benchmark key and Qwen 4B did not. These are specific operations suggested by the answers, not proven explanations of the models’ errors.

<details>
<summary>Example: reading the supplied sequence incorrectly</summary>

**Issue:** The model miscounts residues and reports the wrong sequence at the requested positions.

**Task:** Choose the position of a protein motif.

**Protein sequence:**

```text
MHLSTALFSAIALLAATQVIGASVEVPRDVAAIQIATSPYYACNCPNNCKHKKGSGCKYHSGPSDKSKVISGKCEWQGGQLNCIAT
```

**Choices:**

- A. 72–83
- B. 535–543
- C. 206–213
- D. 8–15

**Author’s answer:** A, 72–83.

**Teacher’s saved answer:** A. It counted 86 residues and reported that positions 72–83 contain `GKCEWQGGQLNC`. It noted that the question did not specify the motif.

**Qwen 4B’s saved answer:** D. It reported 85 residues and selected the 8–15 region. For positions 72–83, it reported `KCEWQGGQLNCIAT`—14 residues for a 12-residue range.

**What this illustrates:** The issue is an observable counting and transcription discrepancy. Correct counting alone does not establish which motif the question intended or whether Qwen’s final answer would change.

</details>

<details>
<summary>Example: misunderstanding what an answer choice means</summary>

**Issue:** The model assigns the wrong biological activity to an enzyme number and evaluates that mistaken activity against the sequence.

**Task:** Choose the protein’s enzyme classification.

**Protein sequence:**

```text
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ
```

**Choices:**

- A. EC 5.6.2.4
- B. EC 2.3.1.193
- C. EC 6.3.5.1
- D. EC 1.14.19.80

**Author’s answer:** C, EC 6.3.5.1.

**Teacher’s saved answer:** C. It described EC 6.3.5.1 as glutamine-dependent NAD⁺ synthetase.

**Qwen 4B’s saved answer:** D. It described option C as an ATP-dependent DNA ligase and rejected it using claimed DNA-ligase features.

**What this illustrates:** Understanding what each option means is a separate challenge from reading the protein sequence. The different descriptions alone do not prove why the final answers differ.

</details>

The **both-wrong cases** are different: they can suggest concerns to investigate, but they do not supply a successful teacher solution from which to reliably identify what the student needed to learn. The 1,289-skill collection therefore comes from the teacher-correct/student-wrong comparison.

## Using the skills

We start with synthetic protein questions, answers, and reasoning generated by Qwen Flash-Next, and generate new questions targeted to the identified skills. We compare teacher and Qwen 4B answers and select questions where the teacher consistently chooses a supported answer and Qwen 4B is wrong. GPT-Luna reviews the selected questions and answers.
