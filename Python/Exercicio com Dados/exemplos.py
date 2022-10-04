import matplotlib.pyplot as plt
import pandas as pd
dados = pd.read_excel(
    'C:\python-studies\Python\Exercicio com Dados\consumo.xlsx')
dados.head()
print(len(dados))

# métricas de posição
print('Média', dados['P'].mean())
print('Mediana', dados['P'].median())
print('1º Quartil', dados['P'].quantile(0.25))
print('3º Quartil', dados['P'].quantile(0.75))
print('Moda', dados['P'].mode())

# metricas de Disperção
print('Amplitude', dados['P'].max()-dados['P'].min())
print('Variancia', dados['P'].var())
print('Desvio Padrão', dados['P'].std())
print('Coeficiente de Variação', dados['P'].std()/dados['P'].mean())

# Posição de Disperção com um Unico comando
print(dados['A'].describe())

# Histograma
plt.figure(figsize=(12, 8))
plt.title("Distribuição de Frequência", fontsize=18)
plt.xlabel("Potência", fontsize=14)
plt.ylabel("Frequência Relativa", fontsize=14)
plt.hist(dados['P'], bins="auto")
plt.grid
