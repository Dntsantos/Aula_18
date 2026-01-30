import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Conectando os dados


try:
    print('Obtendo dados...')

    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # 'utf-8', 'iso-8859-1', 'latin1', 'cp1252'

    df_ocorrencia = pd.read_csv(ENDEREÇO_DADOS, sep = ';', encoding='iso-8859-1')

    print(df_ocorrencia.head())

    # Delimitando as variaveis
    df_roubo_veiculo = df_ocorrencia[['munic', 'roubo_veiculo']]
    # print(df_roubo_veiculo.head())


    # Agrupando e quantificando
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head(20))


except Exception as e:
    print(f'Erro ao obter dados {e}')




try:
    print('Obtendo informações do padrão de roubos de veículos')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # medidas de tendência central
    media = np.mean(array_roubo_veiculo)
    mediana = np.median(array_roubo_veiculo)
    distancia_media_mediana = (media - mediana) / mediana * 100

    print(f'Média: {media:.3f}')
    print(f'Mediana: {mediana:.3f}')
    print(f'Distância entre Média e Mediana: {distancia_media_mediana:.3f}')
    

except Exception as e:
    print(f'Erro ao obter informações... {e}')


# Obtendo medidas estatísticas
try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print('\nMedidas de Posição:')
    print(30*'=')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # menores
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # maiores
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMenores')
    print(30*'=')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo'))
    
    print('\nMaiores')
    print(30*'=')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

    
    # Medidas de Dispersão
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude_total = maximo - minimo

    print('\nPrintando Medidas de Dispersão: ')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')


    # intervalo interquartil
    iqr = q3 - q1

    print(f'Intervalo interquartil: {iqr}')


    # Limite Inferior
    limite_inferior = q1 - (1.5 * iqr)
    print(f'Limite Inferior: {limite_inferior}')

    # Limite Superior
    limite_superior = q3 + (1.5 * iqr)
    print(f'Limite Superior: {limite_superior}')


    # Outliers Inferiores:
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    print('\nOutliers Inferiores: ')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não há outliers inferiores')
    else:
        print(df_roubo_veiculo_outliers_inferiores)

    # Outliers Superiores:
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    print('\nOutliers Superiores: ')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não há outliers superiores')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))


except Exception as e:
    print(f'Erro ao obter medidas estatísticas {e}')



try:
    #pip install matplotlib
    print('Visalisando os dados...')

    plt.subplots(2, 2, figsize= (16,7))
    plt.suptitle('Analise de Boxplot')
    
    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False, showfliers=False, showmeans=True)
    plt.title('Gráfico Boxplot')

    plt.subplot(2, 2, 2 )
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.title('Gráfico Boxplot')

    plt.subplot(2, 2, 3 )

    plt.subplot(2, 2, 4 )

    plt.show()


except Exception as e:
    print(f'Erro ao plotar o Gráfico {e}')
