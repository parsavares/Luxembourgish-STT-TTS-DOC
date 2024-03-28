---
tags:
  - automatic-speech-recognition
  - generated_from_trainer
license: mit
language:
  - lb
metrics:
  - wer
pipeline_tag: automatic-speech-recognition


---


# parsavares/wav2vec2-base-luxembourgish-STT: A Luxembourgish ASR Model

## Overview

This model utilizes the wav2vec 2.0 architecture, initially pre-trained on 842 hours of unlabeled Luxembourgish speech data from [RTL.lu](https://www.rtl.lu/), followed by fine-tuning on 4 hours of labeled speech from the same domain. Designed to improve automatic speech recognition (ASR) for Luxembourgish, this effort aims to bridge the digital resource gap for the Luxembourgish language, making it more accessible for speech-based applications.

## Model Description

Chosen for its robust performance on speech data, especially where labeled examples are scarce, the wav2vec 2.0 base model was first pre-trained on a large corpus of Luxembourgish speech. It was then fine-tuned with a smaller, annotated dataset specifically for speech recognition tasks. This approach was intended to refine the model's capability to accurately transcribe Luxembourgish speech.

### Performance Metrics

| Metric | Dev Set | Test Set |
|--------|---------|----------|
| WER    | 23.95%  | 23.09%   |
| CER    | 7.97%   | 7.63%    |

### Intended Uses & Limitations

Targeted at researchers, developers, and companies interested in integrating Luxembourgish speech recognition into their services, the model marks a significant advance in Luxembourgish ASR technology. However, its efficacy may vary with the accent, specific jargon, and ambient noise in the audio input.

### Training and Evaluation Data

Additional details on the pre-training and fine-tuning data sets would enrich understanding and facilitate reproduction of results.

## Training Procedure

### Hyperparameters

| Hyperparameter               | Value          |
|------------------------------|----------------|
| Learning rate                | 7.5e-05        |
| Batch size (train/eval)      | 3              |
| Seed                         | 42             |
| Gradient accumulation steps  | 4              |
| Total train batch size       | 12             |
| Optimizer                    | Adam (betas=(0.9,0.999), epsilon=1e-08) |
| LR scheduler                 | Linear, with 2000 warmup steps |
| Epochs                       | 50             |
| Mixed precision training     | Native AMP     |

### Software and Libraries

| Software/Library | Version      |
|------------------|--------------|
| Transformers     | 4.20.0.dev0  |
| PyTorch          | 1.11.0+cu113 |
| Datasets         | 2.2.1        |
| Tokenizers       | 0.12.1       |

## Visualization

(Graph of training loss over epochs and comparison of WER and CER on Dev vs. Test datasets to be added here)

## Citation


```
@misc{lb-wav2vec2,
  author = {Nguyen, Le Minh and Nayak, Shekhar and Coler, Matt.},
  keywords = {Luxembourgish, multilingual speech recognition, language modelling, wav2vec 2.0 XLSR-53, under-resourced language},
  title = {IMPROVING LUXEMBOURGISH SPEECH RECOGNITION WITH CROSS-LINGUAL SPEECH REPRESENTATIONS},
  year = {2022},
  copyright = {2023 IEEE}
}
```


