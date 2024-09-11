# Vamos a importar a biblioteca pandas
import pandas as pd
psg_players = pd.Series(
    ['Navas','Mbappe' ,'Neymar','Messi'],
    index=[10,8,5,6]
)
pgs_dict={10: 'navas', 8: 'Mbappe' , 5: 'Neimar' ,6: 'messi'}
pgs_players_dict= pd. Series(pgs_dict)
print(psg_players)
print(pgs_players_dict)
print(pgs_players_dict[5])
print(pgs_players_dict[0:6])

#diccionario con datos de jugadores
dict = {'jugador': ['Navas','Mbappe' ,'Neymar','Messi'],
        'Altura':[183.0 , 170.0, 170.0, 165.0],
        'goles':[2, 200, 150, 200]}
# crea un dataframe con el diccionario e indices peronalizado
df = pd.DataFrame(dict,index=[10,8,5,6])
print(df)