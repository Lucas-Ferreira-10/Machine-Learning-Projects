from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Prevendo a Frequência de irrigação
X1 = data[['temp_media', 'umid_media']]
y1 = data[['Frequência de Irrigação']]

# Dividindo os dados em Treino e Teste
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

# Criando o modelo de árvore de decisão
modelo_frequencia = DecisionTreeRegressor(random_state=42)

# Treinando o modelo
modelo_frequencia.fit(X1_train, y1_train)

# Previsões para o conjunto de teste
previsoes_frequencia = modelo_frequencia.predict(X1_test)

# Avalie o desempenho do modelo (MSE)
mse_frequencia = mean_squared_error(y1_test, previsoes_frequencia)
print(f'Mean Squared Error (MSE) para frequência: {mse_frequencia:.2f}')
