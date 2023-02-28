from transformers import AutoModelWithLMHead, AutoTokenizer

# Load the GPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelWithLMHead.from_pretrained('gpt2')

# Encode the prompt
prompt = "Once upon a time, there was a young prince who lived in a castle."
encoded_prompt = tokenizer.encode(prompt, add_special_tokens=True, return_tensors='pt')

# Generate text based on the prompt
output = model.generate(encoded_prompt, max_length=100, do_sample=True, top_k=50, top_p=0.95)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
