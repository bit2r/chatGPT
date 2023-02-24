# 감성분석 - 파이썬 코드
# 출처: https://www.kaggle.com/code/funtowiczmo/hugging-face-transformers-how-to-use-pipelines

from transformers import pipeline

# NER 파이프라인 ---------------------------------
ner = pipeline(task = "ner", 
               model="bert-base-multilingual-cased")

text = "김대중 대통령은 대전을 방문했다."
entities = ner(text)

# 결과 출력
for entity in entities:
    print(f"{entity['word']} -> {entity['entity']}")
    
