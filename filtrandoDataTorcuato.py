import pandas as pd

df = pd.read_csv('jijiTorcuato.csv')

df = df.dropna(subset=['banios','dormitorios','ambientes','metros cuadrados'])
df['cochera'] = df['cochera'].fillna(0)
df = df.drop(index=3)
df = df.drop(index=170)
df = df.drop_duplicates()

df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
df['metros cuadrados'] = pd.to_numeric(df['metros cuadrados'], errors='coerce')





umbral_precio_m2_min = 400  # ajustar según tu criterio
umbral_precio_m2_max = 900



df['precio_m2'] = df['precio'] / df['metros cuadrados']

filtros = df['metros cuadrados'] < umbral_precio_m2_min
filtross = df['metros cuadrados'] >= umbral_precio_m2_max

df = df[~filtros]
df = df[~filtross]

media_precio_m2 = df['precio_m2'].mean()

print(media_precio_m2)

print(df.to_string())
df.to_csv('/users/anoni/onedrive/desktop/jijijiTorcuato.csv', index=False)