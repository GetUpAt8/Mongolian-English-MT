# Mongolian-English Machine Translation Model

A Mongolian-English Machine Translation Model trained with Fairseq.

We have uploaded the checkpoint file on Hugging Face: [Moi1234/Mongolian-English-MT](https://huggingface.co/Moi1234/Mongolian-English-MT)

You can try the model using the instructions in the [Fairseq README](https://github.com/facebookresearch/fairseq/blob/main/examples/translation/README.md#example-usage-torchhub).

## show_results.py

`show_results.py` is a Python script to filter data in the log, and plot the BLEU, Loss, PPL data into separate pictures.

## Training Data

The training data is obtained from [sharavsambuu's English-Mongolian NMT Dataset Augmentation](https://github.com/sharavsambuu/english-mongolian-nmt-dataset-augmentation) as of [2019/10/10], consisting of 1 million Mongolian to English sentence pairs. [Download here](https://drive.google.com/file/d/14AtTVgibirSdHYTBFM9G1XPS7DvM5SdE/view?usp=sharing)

We used the Mongolian data, cleaned it, and filtered sentences with a length no more than 192 characters. The sentences were then translated into English using Google Translation. The final parallel data used for training comprises about 700K pairs. We used VOLT to generate the vocabulary. [VOLT repository](https://github.com/Jingjing-NLP/VOLT)

## Data Statistics

|        | Train  | Valid  | Test  |
|--------|--------|--------|-------|
| Amount | 690,138| 10,000 | 10,000|

Feel free to explore the model and provide feedback.
