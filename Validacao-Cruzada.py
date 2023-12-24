from sklearn.model_selection import cross_val_score

# Modelo da Frequência
scores = cross_val_score(modelo_frequencia, X1, y1, cv=5)

# Exibindo os resultados
print("Acurácia para cada fold:", scores)
print("Acurácia média: {:.2f}".format(scores.mean()))


# Modelo da Lâmina de Irrigação
scores = cross_val_score(modelo_lamina, X2, y2, cv=5)

# Exibindo os resultados
print("Acurácia para cada fold:", scores)
print("Acurácia média: {:.2f}".format(scores.mean()))
