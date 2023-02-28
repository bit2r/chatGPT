# from transformers import AutoModelWithLMHead, AutoTokenizer
# 
# # GPT 모델과 tokenizer
# tokenizer = AutoTokenizer.from_pretrained('gpt2')
# model = AutoModelWithLMHead.from_pretrained('gpt2')

from transformers import GPT3Tokenizer, GPT3Model

tokenizer = GPT3Tokenizer.from_pretrained('openai-gpt')
model = GPT3Model.from_pretrained('openai-gpt')

# 프롬프트 입력
# prompt = "Once upon a time, there was a young prince who lived in a castle."
prompt = "Explain the moon landing to a 6 year old in a few sentences"
encoded_prompt = tokenizer.encode(prompt, add_special_tokens=True, return_tensors='pt')

# 출력결과
output = model.generate(encoded_prompt, max_length=100, do_sample=True, top_k=50, top_p=0.95)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
