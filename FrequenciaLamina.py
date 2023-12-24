import pandas as pd
import numpy as np
import TratamentoDados
import TurnoDeRega

def Freq_Lamina_Irrig(df):
  '''
  Função que calcula a frequência de irrigação e a lâmina de água.

  Entrada:

    df (DataFrame): Dados Metereológicos

  Saída:

    df (DataFrame): Dados com a Frequência de Irrigação e a Lâmina de Água calculada.

  '''
  # Corrigindo colunas com NaN e normalizando com a média
  data = TratamentoDados.limpando_dados(df)

  # Selecionando as colunas de interesse
  data = TratamentoDados.select_data(data)

  # Calculando a Temperatura e Umidade do Ar Média
  vetor_temp_media, vetor_umid_media = TurnoDeRega.calculate_media(data)

  # Calculando a Evapotranspiração de Referência (ETo)
  eto = TurnoDeRega.evapo_benavides_lopez(vetor_temp_media,vetor_umid_media)

  # Calculando a Evapotranspiração Máxima da Cultura (ETc)
  etc = TurnoDeRega.evapo_max_cultura(eto)

  # Calculando a Frequência de Irrigação
  f = TurnoDeRega.freq_irrigation(etc)

  # Calculando Lâmina Bruta de Irrigação (Lâmina de Água)
  lamina_bruta = TurnoDeRega.lam_bruta_atualizada(etc)

  # Dados Finais
  data = {'temp_media':vetor_temp_media,'umid_media':vetor_umid_media,
          'Frequência de Irrigação':f,'Lâmina de Água':lamina_bruta}
  data = pd.DataFrame(data)

  return data


# Leitura dos dados iniciais
df = TratamentoDados.concatenate_data()

data = Freq_Lamina_Irrig(df)
data.head()
