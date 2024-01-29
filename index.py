#A lógica para funcionamento estará como rascunho neste arquivo.

#1 Fazer o sistema percorrer todos os arquivos: a partir das bibliotecas
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir('/content/drive/MyDrive/Colab Notebooks/Curso Básico de Python/Vendas')
display(lista_arquivo)

#Definição da variável para tratar os dados (no Passo 3)
tabela_total = pd.DataFrame()

#2 Importar as bases de dados ('os' é uma biblioteca que percorre planilhas)
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:

#3 Tratar a base de dados
    tabela = pd.read_csv(f'/content/drive/MyDrive/Colab Notebooks/Curso Básico de Python/Vendas/{arquivo}')
    tabela_total = tabela_total.append(tabela)

display(tabela_total)

#4 (Indicadores) Produto mais vendido

# vamos agrupar os Produtos somando a Quantidade deles, ou seja, somar a coluna. E o [[]] irá indicar que só essa coluna aparecerá
tabela_produtos = tabela_total.groupby('Produto').sum()[['Quantidade Vendida']]
# e aqui vamos organizar por produtos mais vendidos - produtos menos vendidos
tabela_produtos = tabela_produtos.sort_values(by='Quantidade Vendida', ascending=False)
display(tabela_produtos)

#5 (Indicadores) Produto que mais faturou
# criando uma coluna nova
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

# somando a coluna e indicando somente qual irá mostrar
tabela_faturamento = tabela_total.groupby('Produto').sum()[['Faturamento']]
# organizando a ordem
tabela_faturamento = tabela_faturamento.sort_values(by='Faturamento', ascending=False)
display(tabela_faturamento)

#6 (Indicadores) Calcular loja que mais faturou
# somando a coluna e indicando somente qual irá mostrar
tabela_lojas = tabela_total.groupby('Loja').sum()
# organizando a ordem
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
display(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()