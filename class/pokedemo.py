import pandas as pd #for short

poke_df= pd.read_csv("pokedex.txt")

print(poke_df.shape())

poke_df.drop_duplicates(inplaces=True)

print(poke_df.shape)
