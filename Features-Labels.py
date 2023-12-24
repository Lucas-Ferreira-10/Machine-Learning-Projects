import pandas as pd
import numpy as np
import math

def calculate_media(data):

  '''
  Função responsável por calcular a média da temperatura e da umidade do ar a cada 30 dias

  Entrada:

    df (DataFrame): Dados Metereológicos

  Saída:

    vetor (Array): Vetores com as médias da temperatura e da umidade do ar

  '''
  data['hum_media'] = (data['hum_max'] + data['hum_min'])/2

  data['group'] = (data.index // 30) * 30
  media_por_grupo = data.groupby('group').mean()

  return np.array(media_por_grupo['temp_avg']),np.array(media_por_grupo['hum_media'])

# ---------------------------------------------------------------##------------------------------------------------------------

def evapo_benavides_lopez(array_temp_media, array_umid_ar_media):

  '''
    Função responsável por calcular a Evapotranspiração de Referência pelo método de Benavides & Lopez

  Entrada:

    vetor (Array): Vetor com as médias da temperatura e da umidade do ar

  Saída:

    vetor (Array): Vetor contendo a Evapotranspiração de Referência

  '''

  values_eto = []
  for i in range(len(array_temp_media)):
    float(array_temp_media[i])*7.45


    exp = (array_temp_media[i]*7.45)/(234.7 + array_temp_media[i])
    term1 = (1 -0.01*array_umid_ar_media[i])
    term2 = 0.21*array_temp_media[i]
    eto = 1.21*(10**exp)*term1 + term2 - 2.30
    values_eto.append(eto)

  eto = np.array(values_eto)

  return eto

# ---------------------------------------------------------------##------------------------------------------------------------

def evapo_max_cultura(eto, Kc=1.20):

  '''
    Função responsável por calcular a Evapotranspiração Máxima da Cultura (ETC)

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração de Referência (Eto)

  Saída:

    vetor (Array): Vetor contendo a Evapotranspiração Máxima da Cultura (ETC)

  '''
  # Kc = 1.20 (Padrão para o Milho)

  etc = np.array([math.ceil(Kc*value) for value in eto])
  return etc

# ---------------------------------------------------------------##------------------------------------------------------------

def CAD():

  '''
    Função responsável por calcular a capacidade total de água disponível do solo (CAD)

  Saída:

    valor (float): Valor da capacidade total de água disponível do solo (CAD)

  '''

  # Capacidade de campo (CC)
  cc = 38.2

  # Ponto de murcha permanente (PMP)
  pmp = 25.7

  # Densidade do Solo
  d = 1.2

  cad = ((cc - pmp)*d)/10

  return cad

# ---------------------------------------------------------------##------------------------------------------------------------

def calcula_coef_disponibilidade(etc):

  '''
    Função responsável por calcular o coeficiente de disponibilidade

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo o valor dos coeficientes de disponibilidade

  '''

  # Valor calculado em função da evapotranspiraçao (Padrão)
  values = {2:0.875, 3:0.80, 4:0.70, 5:0.60, 6:0.55,
            7:0.50, 8:0.45, 9:0.425, 10:0.40}
  vetor_f = []

  for i in range(len(etc)):
    if etc[i] in values.keys():
      vetor_f.append(values[etc[i]])
    if etc[i]<2:
      vetor_f.append(0.875)
    if etc[i]>10:
      vetor_f.append(0.40)

  return np.array(vetor_f)

# ---------------------------------------------------------------##------------------------------------------------------------

def calculate_LL(etc):

  '''
  Função responsável por calcular a Lâmina Líquida (LL)

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os valores da Lâmina Líquida (LL)

  '''

  cad = CAD()
  f = calcula_coef_disponibilidade(etc)
  # o valor da profundidade efetiva do sistema radicular
  z = 40

  # Vetor com as laminas liquidas
  vet_lam_liq = []

  for i in range(len(etc)):
    lam_liq = cad*f[i]*z
    vet_lam_liq.append(lam_liq)

  return np.array(vet_lam_liq)

# ---------------------------------------------------------------##------------------------------------------------------------

def calculate_LB(etc):

  '''
  Função responsável por calcular a Lâmina Bruta (LB)

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os valores da Lâmina Bruta (LB)

  '''

  # Eficiência de irrigação (Ei)
  ei = 0.75

  lam_liq = calculate_LL(etc)
  lam_bruta = lam_liq/ei

  return lam_bruta

# ---------------------------------------------------------------##------------------------------------------------------------

def freq_irrigation(etc):

  '''
  Função responsável por calcular a Frequência de Irrigação

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os valores da Frequência de Irrigação

  '''

  F = []
  lam_liq = calculate_LL(etc)
  for i in range(len(lam_liq)):
    value = lam_liq[i]/etc[i]
    F.append(int(value))

  return np.array(F)

# ---------------------------------------------------------------##------------------------------------------------------------

def new_lam_liq(etc):

  '''
  Função responsável por ajustar o valor da Lâmina Líquida

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os valores ajustados da Lâmina Líquida

  '''

  F = freq_irrigation(etc)
  new_LL = []

  for i in range(len(etc)):
    new_LL.append(int(F[i]*etc[i]))

  return np.array(new_LL)

# ---------------------------------------------------------------##------------------------------------------------------------

def new_coef_disponibilidade(etc):

  '''
  Função responsável por calcular um novo coeficiente de disponibilidade

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os novos valores do novo coeficiente de disponibilidade

  '''

  z = 40
  cad = CAD()
  new_ff = new_lam_liq(etc)/(z*CAD)

  return new_ff

# ---------------------------------------------------------------##------------------------------------------------------------

def lam_bruta_atualizada(etc):

  '''
  Função responsável por calcular um novo valor da Lâmina Bruta (LB) baseada na Eficiência de Irrigação (Ei)

  Entrada:

    vetor (Array): Vetor com os valores da Evapotranspiração Máxima da Cultura (ETC)

  Saída:

    vetor (Array): Vetor contendo os novos valores da Lâmina Bruta (LB)

  '''

  ei = 0.75
  lam_bruta = new_lam_liq(etc)/0.75
  lam_bruta = np.round(lam_bruta,2)

  return lam_bruta
