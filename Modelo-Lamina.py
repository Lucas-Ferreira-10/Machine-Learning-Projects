from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

# Prevendo a Lâmina de Água
X2 = data[['temp_media', 'umid_media']]
y2 = data[['Lâmina de Água']]

# Dividindo os dados em Treino e Teste
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

# Criando o modelo de árvore de decisão
modelo_lamina = DecisionTreeRegressor(random_state=42)

# Treinando o modelo
modelo_lamina.fit(X2_train, y2_train)

# Fazendo as previsões no conjunto de teste
previsoes_lamina = modelo_lamina.predict(X2_test)

# Avaliando o desempenho do modelo
mse_lamina = mean_squared_error(y2_test, previsoes_lamina)
print(f'Mean Squared Error (MSE) para Lâmina de Irrigação: {mse_lamina:.2f}')
