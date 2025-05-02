# Azure-Cognitive-Search-Utilizando-AI-Search-para-indexa-o-e-consulta-de-Dados
  A estrutura do exercio ficara da seguinte forma:

  /lab-ia-documentos/
│
├── README.md
├── RELATORIO.md
├── /docs/
│   └── etapas.md
├── /insights/
│   └── principais-insights.md
├── /dados/
│   └── exemplos-ingestao.csv
└── /codigo/
    └── indexador.py

# Laboratório: Organização e Pesquisa de Documentos com IA

Este repositório contém os arquivos e registros do laboratório voltado para a aplicação de inteligência artificial na ingestão, indexação e exploração de documentos.

## Objetivo

Aplicar técnicas de IA para minerar e extrair conhecimento de grandes volumes de informação, utilizando etapas como:

- Ingestão de conteúdo
- Criação de índices inteligentes
- Exploração e extração de insights

## Estrutura

- `/docs`: Documentação das etapas realizadas
- `/insights`: Registro dos principais achados e aprendizados
- `/dados`: Exemplos de arquivos utilizados na ingestão
- `/codigo`: Scripts utilizados para indexação e exploração
# Relatório do Laboratório

## Introdução

O laboratório teve como foco a aplicação de técnicas de organização e mineração de dados utilizando ferramentas de IA, com ênfase em:

- Ingestão de documentos
- Indexação inteligente
- Extração de insights

## Etapas

As etapas principais desenvolvidas foram:

1. Preparação e ingestão de dados
2. Criação e treinamento de índice inteligente
3. Consulta e análise dos dados indexados

## Ferramentas Utilizadas

- Azure AI Search
- Azure Cognitive Services
- Python + Bibliotecas (Pandas, Requests)

## Conclusão

A prática demonstrou a eficiência das ferramentas de IA na organização de grandes volumes de informação, além de permitir a extração de insights relevantes para tomada de decisão.
# Etapas do Laboratório

## 1. Ingestão de Conteúdo
- Conversão de documentos para texto plano
- Extração de metadados relevantes (autor, data, tema)

## 2. Criação de Índices Inteligentes
- Indexação dos textos usando Azure AI Search
- Definição de campos de busca (título, corpo, palavras-chave)

## 3. Exploração dos Dados
- Realização de buscas semânticas
- Agrupamento por tópicos
- Identificação de padrões recorrentes
# Principais Insights

- Documentos relacionados ao mesmo tema, mas com vocabulário diferente, puderam ser agrupados pela IA com sucesso.
- A criação de índices semânticos aumentou significativamente a precisão nas buscas.
- Termos-chave foram automaticamente extraídos e ajudaram na classificação temática dos documentos.
titulo,autor,data,texto
"Relatório Anual","Maria Silva","2023-12-10","Este documento apresenta os resultados do ano fiscal..."
"Plano Estratégico","João Souza","2024-01-15","O planejamento estratégico para o próximo período inclui..."
import pandas as pd

# Simulação de ingestão de documentos
df = pd.read_csv("../dados/exemplos-ingestao.csv")

# Simular indexação
for _, row in df.iterrows():
    print(f"Indexando documento: {row['titulo']} (Autor: {row['autor']})")
    # Aqui você integraria com Azure Search ou outra ferramenta
