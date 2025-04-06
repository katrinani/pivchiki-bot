import ollama
import re

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