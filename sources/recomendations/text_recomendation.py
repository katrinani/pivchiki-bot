import re
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_text_vector(text):

    text = re.sub(r'[^\w\s]', '', text)  # Удаляем знаки препинания
    text = re.sub(r'\d+', '', text) # Удаляем цифры

    lines = text.strip().split('\n')

    # Удаляем дубликаты с сохранением порядка
    unique_lines = []
    for line in lines:
        line = line.strip()
        if line not in unique_lines:  # Проверяем, есть ли строка уже в списке
            unique_lines.append(line)

    cleaned_texts = '\n'.join(unique_lines)

    return model.encode(cleaned_texts)