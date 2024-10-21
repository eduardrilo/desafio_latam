import json
import re
from collections import Counter
from typing import List, Tuple

def extract_mentions_from_content(content: str) -> List[str]:
    # Función que extrae menciones (@usuarios) del contenido de un tweet
    return re.findall(r'@\w+', content)

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = Counter()

    # Leer el archivo línea por línea para reducir el uso de memoria
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', "")
            if isinstance(content, str):
                mentions = extract_mentions_from_content(content)
                mention_counts.update(mentions)
    
    # Obtener los top 10 usuarios más mencionados
    top_10_mentions = mention_counts.most_common(10)
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q3_memory:")
    print(top_10_mentions)
    
    return top_10_mentions

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q3_memory(file_path)
