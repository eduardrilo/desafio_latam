import json
import re
from collections import Counter
from typing import List, Tuple
from memory_profiler import profile

@profile
def q1_memory(file_path: str):
    # (El código original que ya tienes)
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
    
    print("Resultado de q1_memory:")
    print(top_10_mentions)
    
    return top_10_mentions

# Llama a la función para medir la memoria utilizada
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q1_memory(file_path)
