# LiveProteinBench: evaluation deep dive

We reviewed the questions in our evaluation set to understand whether the benchmark can be scored reliably. We also compared model answers to identify skills that could guide protein training data.

## Are the questions reliable?

GPT-6 Luna and Qwen3.8 Flash-Next (NVFP4) reviewed the questions and identified three types of findings:

- **Multiple defensible choices: 4.95%.** Both reviewers listed at least two defensible choices.
- **Lookup or recall about the specific protein: 3.00%.** Both reviewers said answering requires a fact about the particular protein beyond general biological knowledge.
- **Answer-key contradictions: 0.69%.** Both reviewers judged the author’s answer contradicted by the evidence.

These numbers report reviewer judgments. The categories overlap.

<details>
<summary>Example: a protein that can both cut and transfer</summary>

**Task:** Choose the protein’s molecular function.

**Original task description:** The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function..

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

**Why it was flagged:** Both reviewers pointed to an annotation describing a protein that can both **cut chitin**, a sugar-containing material, and **transfer chitin to another molecule**. Both listed B and D as defensible.

</details>

<details>
<summary>Example: distinguishing nearby temperatures</summary>

**Task:** Choose the protein’s optimal temperature.

**Original task description:** The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category..

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

**Why it was flagged:** The reviewers said sequence and family knowledge might suggest a moderate temperature, but did not distinguish 30°C from 34°C or the nearby range.

</details>

<details>
<summary>Example: the answer says steroid breakdown, but the evidence points to sugar breakdown</summary>

**Task description:** Predict the primary biological process in which the protein participates, based on its amino acid sequence.

**Original task description:** The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes..

**Protein sequence:**

```text
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP
```

**Choices:**

- A. Nuclear pore complex assembly
- B. Response to corticosterone
- C. Negative regulation of axon extension involved in axon guidance
- D. Steroid catabolic process

**Author’s answer:** D, steroid breakdown.

**What the reviewers found:** Both reviewers pointed to evidence that this protein participates in breaking down **L-fucose, a sugar**, rather than evidence supporting steroid breakdown as its primary process. Sugar breakdown is not one of the offered choices.

**Why this matters:** L-fucose is a sugar; steroids are a different class of molecules that includes many hormones. Breaking down a sugar and breaking down a steroid are different biological processes. The evidence identifies this protein with an initial step in L-fucose breakdown, while the benchmark’s answer says steroid breakdown.

</details>

[See all questions flagged for multiple defensible choices](multiple_defensible_by_both_86_20261104.md) · [See all questions flagged as lookup-dependent](lookup_dependent_52_20261104.md) · [See answer-key exceptions](../LIVEPROTEINBENCH_ANSWER_KEY_EXCEPTIONS.md)

## What problems does Qwen 4B run into?

Looking at saved answers reveals specific issues in how Qwen 4B reads a protein sequence and interprets the answer choices.

<details>
<summary>Example: reading the supplied sequence incorrectly</summary>

**Issue:** The model miscounts residues and reports the wrong sequence at the requested positions.

**Task:** Choose the position of a protein motif.

**Original task description:** The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif..

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

**What this illustrates:** Qwen made counting and transcription errors when reading the sequence. The question also did not specify the motif.

</details>

<details>
<summary>Example: misunderstanding what an answer choice means</summary>

**Issue:** The model assigns the wrong biological activity to an enzyme number and evaluates that mistaken activity against the sequence.

**Task:** Choose the protein’s enzyme classification.

**Original task description:** The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence..

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

**What this illustrates:** Qwen described the choice as a DNA ligase and evaluated it using DNA-ligase features. Understanding what each option means is a separate challenge from reading the protein sequence.

</details>

### From model errors to targeted training questions

To investigate these errors, we selected questions where the teacher answered correctly and Qwen 4B answered incorrectly. GPT-6.1 Terra compared their saved answers and extracted **1,289 skill descriptions** across protein-problem categories. Inspired by [DeltaPrompts](https://arxiv.org/html/2605.15532v3), we use these descriptions to generate more targeted protein questions.

We start with synthetic protein questions, answers, and reasoning generated by Qwen Flash-Next, and generate new questions targeted to the identified skills. We compare teacher and Qwen 4B answers and select questions where the teacher consistently chooses a supported answer and Qwen 4B is wrong. GPT-Luna reviews the selected questions and answers.

## Open question: How can we improve a student when both the student and teacher are wrong?

As AI-for-science problems move closer to the research frontier, the correct answer may not yet be known—even to experts—and verifying it may require expensive experiments or simulations. Comparing a wrong teacher answer with a wrong student answer can reveal differences, but it does not tell us which difference is useful to learn from.

One direction is to combine model-generated hypotheses with checks from scientific literature, known biological constraints, simulations, and experiments. Expert or experimental review could focus on the most informative cases. The central question is how to turn these partial and sometimes costly signals into reliable training feedback.
