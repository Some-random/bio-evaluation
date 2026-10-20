# Drug-target interaction: Human (DrugBAN split) — complete question and input

This is a complete original dataset example of drug–target interaction classification. The molecule and protein inputs are reproduced in full, with protein serialization tokens decoded for readability. It is not a recovered archived Qwen request.

Source case: `24-c62485d1847d45078fbf0ea56cf77372`.

## Question / instruction

```text
Drug target interaction prediction task (a binary classification task) for the human dataset. If the given molecule and protein can interact with each other, indicate via "Yes". Otherwise, response via "No".
```

## Complete input

```text
Molecule: <bom>[C][C][=C][N][Branch1][S][C@@H1][O][C@H1][Branch1][Ring1][C][O][C@@H1][Branch1][C][O][C@H1][Ring1][Branch2][O][C][=Branch1][C][=O][NH1][C][Ring1][S][=O]<eom>
Protein: MTGYTPDEKLRLQQLRELRRRWLKDQELSPREPVLPPQKMGPMEKFWNKFLENKSPWRKMVHGVYKKSIFVFTHVLVPVWIIHYYMKYHVSEKPYGIVEKKSRIFPGDTILETGEVIPPMKEFPDQHH
```

[Original source](https://huggingface.co/datasets/QizhiPei/BioT5_finetune_dataset/blob/9f70da9e8f0df32e7e62846f7ad78a829b00c0fd/tasks_plus/task24_human_drugban_dti_test.json)

[Back to results](../RESULTS_AND_REMAINING_WORK.md)
