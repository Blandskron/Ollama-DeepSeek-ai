from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar desde la carpeta local
model_path = './deepseek_r1_1.5b'
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Usar el modelo como antes
input_text = "Hola, ¿cómo estás?"
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
