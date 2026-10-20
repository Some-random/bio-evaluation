# Drug-target interaction: BindingDB (DrugBAN split) — complete question and input

This is a complete original dataset example of drug–target interaction classification. The molecule and protein inputs are reproduced in full, with protein serialization tokens decoded for readability. It is not a recovered archived Qwen request.

Source case: `18-fdfe48ffb39946b4a0cbd9cc776c0bca`.

## Question / instruction

```text
Drug target interaction prediction task (a binary classification task) for the BindingDB dataset. If the given molecule and protein can interact with each other, indicate via "Yes". Otherwise, response via "No".
```

## Complete input

```text
Molecule: <bom>[C][C][=C][C][Branch1][C][Cl][=C][N][=C][Ring1][#Branch1][C][=Branch1][C][=O][N][C][=C][C][=C][Branch1][C][F][C][Branch2][Ring2][C][C@][Branch1][C][C][C][S][=Branch1][C][=O][=Branch1][C][=O][C][Branch1][N][C][C][Branch1][C][F][Branch1][C][F][C][Ring1][=Branch1][C][Branch1][C][N][=N][Ring1][#C][=C][Ring2][Ring1][=Branch1]<eom>
Protein: MAQALPWLLLWMGAGVLPAHGTQHGIRLPLRSGLGGAPLGLRLPRETDEEPEEPGRRGSFVEMVDNLRGKSGQGYYVEMTVGSPPQTLNILVDTGSSNFAVGAAPHPFLHRYYQRQLSSTYRDLRKGVYVPYTQGKWEGELGTDLVSIPHGPNVTVRANIAAITESDKFFINGSNWEGILGLAYAEIARPDDSLEPFFDSLVKQTHVPNLFSLQLCGAGFPLNQSEVLASVGGSMIIGGIDHSLYTGSLWYTPIRREWYYEVIIVRVEINGQDLKMDCKEYNYDKSIVDSGTTNLRLPKKVFEAAVKSIKAASSTEKFPDGFWLGEQLVCWQAGTTPWNIFPVISLYLMGEVTNQSFRITILPQQYLRPVEDVATSQDDCYKFAISQSSTGTVMGAVIMEGFYVVFDRARKRIGFAVSACHVHDEFRTAAVEGPFVTLDMEDCGYNIPQTDESTLMTIAYVMAAICALFMLPLCLMVCQWRCLRCLRQQHDDFADDISLLK
```

[Original source](https://huggingface.co/datasets/QizhiPei/BioT5_finetune_dataset/blob/9f70da9e8f0df32e7e62846f7ad78a829b00c0fd/tasks_plus/task18_bindingdb_drugban_dti_test.json)

[Back to results](../RESULTS_AND_REMAINING_WORK.md)
