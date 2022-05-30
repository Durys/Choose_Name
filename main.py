import pandas as pd

k = pd.read_csv('Data\\8_-_WYKAZ_IMION_ŻEŃSKICH_OSÓB_ŻYJĄCYCH_WG_POLA_IMIĘ_PIERWSZE_WYSTĘPUJĄCYCH_W_REJESTRZE_PESEL_BEZ_ZGONÓW.csv')
m = pd.read_csv('Data\\8_-_WYKAZ_IMION_MĘSKICH_OSÓB_ŻYJĄCYCH_WG_POLA_IMIĘ_PIERWSZE_WYSTĘPUJĄCYCH_W_REJESTRZE_PESEL_BEZ_ZGONÓW.csv')
int_df = pd.merge(k, m, how='inner', on='IMIĘ_PIERWSZE')

int_df.to_csv("Data\\Intersection", sep='\t', encoding='utf-8')

df_non_a = int_df[~int_df['IMIĘ_PIERWSZE'].str.endswith('A')]
df_non_a.to_csv("Data\\NonA", sep='\t', encoding='utf-8')
