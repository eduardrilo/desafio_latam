import json
from collections import Counter
from typing import List, Tuple
import emoji

def extract_emojis_from_content(content: str) -> str:
    # Función que extrae los emojis del contenido
    return ''.join([char for char in content if emoji.is_emoji(char)])

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()

    # Leer el archivo línea por línea para reducir el uso de memoria
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', "")
            if isinstance(content, str):
                emojis = extract_emojis_from_content(content)
                emoji_counts.update(emojis)
    
    # Obtener los top 10 emojis más frecuentes
    top_10_emojis = emoji_counts.most_common(10)
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q2_memory:")
    print(top_10_emojis)
    
    return top_10_emojis

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q2_memory(file_path)
