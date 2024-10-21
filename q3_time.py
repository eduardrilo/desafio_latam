import pandas as pd
import re
from collections import Counter
from typing import List, Tuple

def extract_mentions_from_content(content: str) -> List[str]:
    # Función que extrae menciones (@usuarios) del contenido de un tweet
    return re.findall(r'@\w+', content)

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar el archivo JSON en un DataFrame
    df = pd.read_json(file_path, lines=True)
    
    # Extraer las menciones de cada tweet
    df['mentions'] = df['content'].apply(lambda x: extract_mentions_from_content(x) if isinstance(x, str) else [])
    
    # Crear una lista con todas las menciones
    all_mentions = df['mentions'].sum()  # Esto une todas las listas de menciones en una sola lista
    
    # Contar la frecuencia de cada usuario mencionado
    mention_counts = Counter(all_mentions)
    
    # Obtener los top 10 usuarios más mencionados
    top_10_mentions = mention_counts.most_common(10)
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q3_time:")
    print(top_10_mentions)
    
    return top_10_mentions

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q3_time(file_path)
