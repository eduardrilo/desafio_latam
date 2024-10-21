import pandas as pd
from collections import Counter
from typing import List, Tuple
import emoji

def extract_emojis_from_content(content: str) -> str:
    # Función que extrae los emojis del contenido
    return ''.join([char for char in content if emoji.is_emoji(char)])

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar el archivo JSON en un DataFrame
    df = pd.read_json(file_path, lines=True)
    
    # Extraer los emojis de cada tweet
    df['emojis'] = df['content'].apply(lambda x: extract_emojis_from_content(x) if isinstance(x, str) else "")
    
    # Crear una lista con todos los emojis
    all_emojis = df['emojis'].sum()  # Concatenar todos los emojis
    
    # Contar la frecuencia de cada emoji
    emoji_counts = Counter(all_emojis)
    
    # Obtener los top 10 emojis más frecuentes
    top_10_emojis = emoji_counts.most_common(10)
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q2_time:")
    print(top_10_emojis)
    
    return top_10_emojis

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q2_time(file_path)
