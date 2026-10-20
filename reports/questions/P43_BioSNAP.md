# Drug-target interaction: BioSNAP (DrugBAN split) — complete question and input

This is a complete original dataset example of drug–target interaction classification. The molecule and protein inputs are reproduced in full, with protein serialization tokens decoded for readability. It is not a recovered archived Qwen request.

Source case: `21-1abceddd45a547dba64ad8329412bed2`.

## Question / instruction

```text
Drug target interaction prediction task (a binary classification task) for the BioSNAP dataset. If the given molecule and protein can interact with each other, indicate via "Yes". Otherwise, response via "No".
```

## Complete input

```text
Molecule: <bom>[N][C][=C][C][=C][C][=C][Ring1][=Branch1][C][=Branch1][C][=O][O]<eom>
Protein: MAPLALHLLVLVPILLSLVASQDWKAERSQDPFEKCMQDPDYEQLLKVVTWGLNRTLKPQRVIVVGAGVAGLVAAKVLSDAGHKVTILEADNRIGGRIFTYRDQNTGWIGELGAMRMPSSHRILHKLCQGLGLNLTKFTQYDKNTWTEVHEVKLRNYVVEKVPEKLGYALRPQEKGHSPEDIYQMALNQALKDLKALGCRKAMKKFERHTLLEYLLGEGNLSRPAVQLLGDVMSEDGFFYLSFAEALRAHSCLSDRLQYSRIVGGWDLLPRALLSSLSGLVLLNAPVVAMTQGPHDVHVQIETSPPARNLKVLKADVVLLTASGPAVKRITFSPPLPRHMQEALRRLHYVPATKVFLSFRRPFWREEHIEGGHSNTDRPSRMIFYPPPREGALLLASYTWSDAAAAFAGLSREEALRLALDDVAALHGPVVRQLWDGTGVVKRWAEDQHSQGGFVVQPPALWQTEKDDWTVPYGRIYFAGEHTAYPHGWVETAVKSALRAAIKINSRKGPASDTASPEGHASDMEGQGHVHGVASSPSHDLAKEEGSHPPVQGQLSLQNTTHTRTSH
```

[Original source](https://huggingface.co/datasets/QizhiPei/BioT5_finetune_dataset/blob/9f70da9e8f0df32e7e62846f7ad78a829b00c0fd/tasks_plus/task21_biosnap_drugban_dti_test.json)

[Back to results](../RESULTS_AND_REMAINING_WORK.md)
