import matplotlib.pyplot as plt
import pandas as pd
dados = pd.read_excel(
    'C:\python-studies\Python\Exercicio com Dados\consumo.xlsx')
dados.head()

# métrica do G1
print('Média', dados['G1'].mean())
print('Mediana', dados['G1'].median())
print('1º Quartil', dados['G1'].quantile(0.25))
print('3º Quartil', dados['G1'].quantile(0.75))
print('Moda', dados['G1'].mode())

# métrica do G1
print('Média', dados['G2'].mean())
print('Mediana', dados['G2'].median())
print('1º Quartil', dados['G2'].quantile(0.25))
print('3º Quartil', dados['G2'].quantile(0.75))
print('Moda', dados['G2'].mode())

# métrica do G1
print('Média', dados['G3'].mean())
print('Mediana', dados['G3'].median())
print('1º Quartil', dados['G3'].quantile(0.25))
print('3º Quartil', dados['G3'].quantile(0.75))
print('Moda', dados['G3'].mode())

# Média dos Grupos
media_g1 = dados['G1'].mean()
media_g2 = dados['G2'].mean()
media_g3 = dados['G3'].mean()
# Amplitude dos Grupos
amplitude_g1 = dados['G1'].max()-dados['G1'].min()
amplitude_g2 = dados['G2'].max()-dados['G2'].min()
amplitude_g3 = dados['G3'].max()-dados['G3'].min()
# Coeficiente de Variação
coeficiente_g1 = dados['G1'].std()/dados['G1'].mean()
coeficiente_g2 = dados['G2'].std()/dados['G2'].mean()
coeficiente_g3 = dados['G3'].std()/dados['G3'].mean()

df = pd.DataFrame(data=[[media_g1, amplitude_g1, coeficiente_g1],
                        [media_g2, amplitude_g2, coeficiente_g2],
                        [media_g3, amplitude_g3, coeficiente_g3]], index=['Grupo 1', 'Grupo 2', 'Grupo 3'], columns=['Média', 'Amplitude', 'Coeficiente'])

df
