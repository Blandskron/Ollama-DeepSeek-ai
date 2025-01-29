from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "deepseek-r1:1.5b"  # O el nombre correcto del modelo
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Guardar el modelo localmente
model.save_pretrained('./deepseek_r1_1.5b')
tokenizer.save_pretrained('./deepseek_r1_1.5b')
