
import pandas as pd 
import pandasql as ps 



df_tracks = pd.read_csv("tracks.csv")

query = """
SELECT * FROM df_tracks
WHERE Popularidad > 90
AND Posicion in (1,2,3,4,5)
ORDER BY Popularidad DESC
LIMIT 10
"""

top_5_sql = ps.sqldf(query, locals())

print(top_5_sql)