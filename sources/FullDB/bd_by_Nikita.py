import psycopg2
import ollama
import re
from sentence_transformers import SentenceTransformer
from sources.postgres import config

conn = psycopg2.connect(
                host=config.config_db["host"],
                database=config.config_db["dbname"],
                user=config.config_db["user"],
                password=config.config_db["password"]
)

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


def get_llm_text_vector(text: str, model_name: str = "mistral") -> list[float]:
    # Формируем запрос для модели
    prompt = f"""
    Analyze the following text and rate the intensity of the following emotions and attributes on a scale from 1 to 10, where 1 means absent and 10 means extremely strong. Provide only the scores in the order listed below, separated by commas, without any additional text or explanations.
    there must be only 20 numbers, no more, no less

    Конечно, вот список с цифрами:

    1. Love  
    2. Sadness  
    3. Happiness  
    4. Anger  
    5. Danceability  
    6. Hope  
    7. Fear  
    8. Energetic  
    9. Loneliness  
    10. Confidence  
    11. Melancholy  
    12. Passion  
    13. Despair  
    14. Joy  
    15. Longing  
    16. Serenity  
    17. Anxiety  
    18. Tenderness  
    19. Slowness  
    20. Tension

    Text: «{text}»
    """

    while True:
        response = ollama.generate(model=model_name, prompt=prompt)

        # Извлекаем числа из ответа с помощью регулярного выражения
        scores = re.findall(r"\b\d{1,2}\b", response["response"])
        if len(scores) == 20:
            # Преобразуем в числа и нормализуем в диапазон от 0 до 1
            emotion_vector = [int(score) / 10 for score in scores]
            return emotion_vector
            break


def save_text_vectors():
    """Обновляет векторы для каждого трека с автосохранением после каждой итерации."""
    try:
        with conn.cursor() as cursor:
            # Выбираем треки с непустыми lyrics
            cursor.execute("""
                SELECT trackid, lyrics 
                FROM tracks 
                WHERE lyrics IS NOT NULL 
                AND lyrics != ''
                AND (textvector IS NULL OR textllmvector IS NULL)
            """)

            for trackid, lyrics in cursor.fetchall():
                try:
                    # Вычисляем векторы
                    text_vector = get_text_vector(lyrics).tolist()
                    llm_vector = get_llm_text_vector(lyrics)

                    # Обновляем запись
                    cursor.execute("""
                        UPDATE tracks
                        SET textvector = %s, textllmvector = %s
                        WHERE trackid = %s
                    """, (text_vector, llm_vector, trackid))

                    # Фиксируем изменения сразу
                    conn.commit()
                    print(f"Updated track {trackid}")

                except Exception as e:
                    print(f"Error processing track {trackid}: {e}")
                    conn.rollback()  # Откатываем только текущую итерацию
                    continue  # Переходим к следующему треку

    except Exception as e:
        print(f"Fatal error: {e}")
        conn.rollback()
        raise

if __name__ == "__main__":
    save_text_vectors()