from sklearn.model_selection import cross_val_score

# Modelo da Frequência
scores_freq = cross_val_score(modelo_frequencia, X1, y1, cv=5)

# Exibindo os resultados
print("Acurácia para cada fold:", scores_freq)
print("Acurácia média: {:.2f}".format(scores_freq.mean()))


# Modelo da Lâmina de Irrigação
scores_lam = cross_val_score(modelo_lamina, X2, y2, cv=5)

# Exibindo os resultados
print("Acurácia para cada fold:", scores_lam)
print("Acurácia média: {:.2f}".format(scores_lam.mean()))
