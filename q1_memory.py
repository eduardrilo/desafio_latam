import json
import datetime
from collections import defaultdict
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweet_counts = defaultdict(int)
    user_counts_per_date = defaultdict(lambda: defaultdict(int))

    # Leer el archivo línea por línea para reducir el uso de memoria
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet.get('date', "")
            username = tweet.get('user', {}).get('username', None)
            
            if tweet_date and username:
                date_only = datetime.datetime.fromisoformat(tweet_date).date()
                tweet_counts[date_only] += 1
                user_counts_per_date[date_only][username] += 1
    
    # Obtener el top 10 fechas con más tweets
    top_10_dates = sorted(tweet_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Encontrar el usuario con más publicaciones para cada una de las top 10 fechas
    result = []
    for date, _ in top_10_dates:
        most_active_user = max(user_counts_per_date[date].items(), key=lambda x: x[1])[0]
        result.append((date, most_active_user))
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q1_memory:")
    print(result)
    
    return result

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q1_memory(file_path)
