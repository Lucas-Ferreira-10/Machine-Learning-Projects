import pandas as pd
import numpy as np
import T


# Leitura dos dados iniciais
df = concatenate_data()

def Freq_Lamina_Irrig(df):
  '''
  Função que calcula a frequência de irrigação e a lâmina de água.

  Entrada:

    df (DataFrame): Dados Metereológicos

  Saída:

    df (DataFrame): Dados com a Frequência de Irrigação e a Lâmina de Água calculada.

  '''
  # Corrigindo colunas com NaN e normalizando com a média
  data = limpando_dados(df)

  # Selecionando as colunas de interesse
  data = select_data(data)

  # Calculando a Temperatura e Umidade do Ar Média
  vetor_temp_media, vetor_umid_media = calculate_media(data)

  # Calculando a Evapotranspiração de Referência (ETo)
  eto = evapo_benavides_lopez(vetor_temp_media,vetor_umid_media)

  # Calculando a Evapotranspiração Máxima da Cultura (ETc)
  etc = evapo_max_cultura(eto)

  # Calculando a Frequência de Irrigação
  f = freq_irrigation(etc)

  # Calculando Lâmina Bruta de Irrigação (Lâmina de Água)
  lamina_bruta = lam_bruta_atualizada(etc)

  # Dados Finais
  data = {'temp_media':vetor_temp_media,'umid_media':vetor_umid_media,
          'Frequência de Irrigação':f,'Lâmina de Água':lamina_bruta}
  data = pd.DataFrame(data)

  return data

data = Freq_Lamina_Irrig(df)
data.head()
