import pandas as pd
import numpy as np

def concatenate_data():
  '''
    Função que faz a concatenação dos dados metereológicos.

    Entrada:
      data (DataFrame): Dados metereológicos

    Saída
      df (DataFrame): Dados metereológicos concatenados.

  '''
  # Leitura dos dados de 2000
  df = pd.read_csv("/content/drive/MyDrive/DadosMetereologicos/weather_sum_2000.csv")

  for i in range(1,24):
    if 0 <= i <= 9:
      df1 = pd.read_csv(f"/content/drive/MyDrive/DadosMetereologicos/weather_sum_200{i}.csv")
      df = pd.concat([df,df1])
    else:
      df1 = pd.read_csv(f"/content/drive/MyDrive/DadosMetereologicos/weather_sum_20{i}.csv")
      df = pd.concat([df,df1])

  return df

# ---------------------------------------------------------------##------------------------------------------------------------

def select_data(df):
  '''
  Função que seleciona os dados de interesse do modelo: temp_avg, hum_max e hum_min

  Entrada:

    df (DataFrame): Dados Metereológicos

  Saída:

    df (DataFrame): Dados Meterológicos com as colunas de interesse para o modelo

  '''
  columns = ['temp_avg',
        'hum_max','hum_min']

  df = df[columns]

  return df

# ---------------------------------------------------------------##------------------------------------------------------------

def limpando_dados(df):
  '''
  Função que seleciona as colunas com NaN e ajusta com a média.

  Entrada:

    df (DataFrame): Dados Metereológicos

  Saída:

    df (DataFrame): Dados Meterológicos com as colunas corrigidas

  '''
  columns = ['temp_avg',
        'hum_max','hum_min']

  # Preencher NaN em colunas específicas com a média
  df[columns[0]] = df[columns[0]].fillna(df[columns[0]].mean())
  df[columns[1]] = df[columns[1]].fillna(df[columns[1]].mean())
  df[columns[2]] = df[columns[2]].fillna(df[columns[2]].mean())

  return df

# ---------------------------------------------------------------##------------------------------------------------------------
