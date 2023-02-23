# 질의응답 - 파이썬 코드
# 출처: https://github.com/PacktPublishing/Getting-Started-with-Google-BERT/tree/main/Chapter03

from transformers import BertForQuestionAnswering, BertTokenizer
import torch

model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# BERT 논문 Abstract: https://arxiv.org/pdf/1810.04805.pdf

question = "What does the 'B' in BERT stand for?"
abstract = "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement)."


question = '[CLS] ' + question + '[SEP]'
abstract = abstract + '[SEP]'

question_tokens = tokenizer.tokenize(question)
abstract_tokens = tokenizer.tokenize(abstract)

tokens = question_tokens + abstract_tokens
input_ids = tokenizer.convert_tokens_to_ids(tokens)

segment_ids = [0] * len(question_tokens) + [1] * len(abstract_tokens)

input_ids = torch.tensor([input_ids])
segment_ids = torch.tensor([segment_ids])

scores = model(input_ids, token_type_ids = segment_ids)

start_index = torch.argmax(scores['start_logits'])
end_index = torch.argmax(scores['end_logits'])

# print(' '.join(tokens[start_index:end_index+1]))

