import pandas as pd
import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Cargar el archivo JSON en un DataFrame
    df = pd.read_json(file_path, lines=True)
    
    # Asegurarnos de que el campo 'date' esté en formato datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Extraer solo la parte de la fecha (sin la hora)
    df['only_date'] = df['date'].dt.date
    
    # Extraer el nombre de usuario desde el campo 'user'
    df['username'] = df['user'].apply(lambda x: x['username'] if isinstance(x, dict) and 'username' in x else None)
    
    # Contar el número de tweets por fecha y usuario
    user_counts = df.groupby(['only_date', 'username']).size().reset_index(name='tweet_count')
    
    # Encontrar el usuario con más tweets por cada fecha
    top_user_per_date = user_counts.loc[user_counts.groupby('only_date')['tweet_count'].idxmax()]
    
    # Contar el número total de tweets por fecha
    date_counts = df.groupby('only_date').size().reset_index(name='total_tweets')
    
    # Unir ambas tablas para obtener el usuario con más tweets por fecha y el total de tweets por esa fecha
    result = pd.merge(top_user_per_date, date_counts, on='only_date')
    
    # Ordenar por el total de tweets de manera descendente y seleccionar el top 10
    top_10_dates = result.sort_values(by='total_tweets', ascending=False).head(10)
    
    # Convertir a la lista de tuplas requerida
    resultado = [(row['only_date'], row['username']) for _, row in top_10_dates.iterrows()]
    
    # Imprimir el resultado en la consola para verificar
    print("Resultado de q1_time:")
    print(resultado)
    
    return resultado

# Ejemplo de llamada a la función:
# Asegúrate de cambiar la ruta a la correcta de tu archivo JSON
file_path = 'C:/Users/eduar/Downloads/tweets.json/farmers-protest-tweets-2021-2-4.json'
q1_time(file_path)
