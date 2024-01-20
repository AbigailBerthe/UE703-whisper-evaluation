# UE703-whisper-evaluation
M1 NLP project from Université de Lorraine. 

This project aims at evaluating noise resilience of Whisper-small and Whisper-tiny, by comparing their performances using transcription of not noisy speech data, and transcriptions of the same speech data with background noises added, at two different SNRs (10 and 0dB). The comparison will be done between the two versions of the model, but also within the version itself by comparing the output as more noise is added. 

The metric used for evaluation is the Word Error Rate

The speech conversation dataset used is a subset of Casual Conversation dataset, the "CC_mini_part_1_1" file, which can be found here : https://ai.meta.com/datasets/casual-conversations-downloads/

The background noises dataset used is the Environmental Sound Classification 50, which can be found here : https://www.kaggle.com/datasets/mmoreaux/environmental-sound-classification-50


