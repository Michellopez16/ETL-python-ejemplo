

import pandas as pd 
import pandasql as ps 



df_tracks = pd.read_csv("tracks2.csv")

query = """
SELECT * FROM df_tracks
WHERE Pais IN ('Mexico', 'Global', 'USA', 'España', 'Colombia', 'Argentina')
AND Posicion in (1,2,3)
ORDER BY Pais ASC
LIMIT 20
"""

top_3_sql = ps.sqldf(query, locals())

print(top_3_sql)
nombre_archivo = "top_3_latinoamerica_sql.csv"
top_3_sql.to_csv(nombre_archivo, index = False)
print(f"Se ha guardado el archivo {nombre_archivo}")


# query = """
# SELECT * FROM df_tracks
# WHERE Pais IN ('Mexico', 'Global', 'USA', 'España', 'Colombia', 'Argentina')
# AND Popularidad > 90
# AND Posicion in (1,2,3)
# ORDER BY Pais, Popularidad DESC
# LIMIT 20
# """

