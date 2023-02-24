# 감성분석 - 파이썬 코드
# 출처: https://www.kaggle.com/code/funtowiczmo/hugging-face-transformers-how-to-use-pipelines

from transformers import pipeline

# NER 파이프라인 ---------------------------------
ner = pipeline(task = "ner", 
               model="dbmdz/bert-large-cased-finetuned-conll03-english",
               tokenizer="bert-large-cased")

text = "John Smith works at Google"
entities = ner(text)

# 결과 출력
for entity in entities:
    print(f"{entity['word']} -> {entity['entity']}")
    
