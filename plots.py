from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Confusion Matrix
y_pred = modelo_frequencia.predict(X1_test)

cm = confusion_matrix(y1_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title('Matriz de Confusão')
plt.xlabel('Frequência de Irrigação Prevista')
plt.ylabel('Frequência de Irrigação Real')
plt.savefig('matriz_confusao_frequencia.png')
plt.show()


y2 = np.array(y2_test['Lâmina de Água'])
y2_pred = modelo_lamina.predict(X2_test)
non_matching_condition = np.isclose(y2, y2_pred, atol=1e-2)
residuos = y2 - y2_pred

plt.figure(figsize=(6, 6))
sns.kdeplot(residuos, fill=True, color='blue', label='Densidade de Resíduos')
plt.axhline(y=0, color='red', linestyle='--', label='Linha de Referência (0)')
plt.xlabel('Resíduos')
plt.ylabel('Densidade')
plt.title('Gráfico de Densidade de Resíduos')
plt.legend()
plt.savefig('grafico_lamina_irrigacao.png')
plt.show()
