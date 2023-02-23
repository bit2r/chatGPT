from transformers import BertModel, BertTokenizer
import torch


model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = 'I love Seoul'
tokens = tokenizer.tokenize(sentence)
print(tokens)


