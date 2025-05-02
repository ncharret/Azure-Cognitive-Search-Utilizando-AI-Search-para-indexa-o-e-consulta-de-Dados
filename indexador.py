import pandas as pd

# Simulação de ingestão de documentos
df = pd.read_csv("../dados/exemplos-ingestao.csv")

# Simular indexação
for _, row in df.iterrows():
    print(f"Indexando documento: {row['titulo']} (Autor: {row['autor']})")
    # Aqui você integraria com Azure Search ou outra ferramenta
