# not working...

from transformers import BertForSequenceClassification, BertTokenizerFast, Trainer, TrainingArguments
from nlp import load_dataset
import torch
import numpy as np


model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = 'I love Seoul'
tokens = tokenizer.tokenize(sentence)
print(tokens)

tokens = [ '[CLS]', sentence, '[SEP]' ]

tokenizer(['I love Paris', 'birds fly','snow fall'], max_length = 5)
