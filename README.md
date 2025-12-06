📊 Previsão de Consumo de Energia com Regressão Linear

Este projeto tem como objetivo prever o consumo de energia elétrica (kWh) em residências utilizando técnicas de Regressão Linear, analisando fatores como temperatura, características do imóvel e comportamento dos moradores.

🔍 1. Entendimento dos Dados
O conjunto de dados é composto pelas seguintes variáveis:

🔸data – data da medição do consumo

🔸 temperatura – temperatura média do dia

🔸 dia_da_semana – dia da semana (0 = segunda-feira, 6 = domingo)

🔸fim_de_semana – indicador de final de semana (0 = não, 1 = sim)

🔸 feriado – identifica se o dia é feriado (0 = não, 1 = sim)

🔸 area_m2 – área do imóvel em metros quadrados

🔸numero_moradores – quantidade de pessoas na residência

🔸consumo_kwh – consumo de energia elétrica em kWh (variável alvo)

🧹 2. Preparação dos Dados

Foram realizadas as seguintes etapas:

🔸 Validação de tipos de dados

🔸 Análise de valores ausentes

🔸Padronização das colunas numéricas

🔸Separação de variáveis explicativas (X) e variável alvo (y)

🔗 3. Análise de Correlação

Foi gerada uma matriz de correlação para avaliar relações entre as variáveis.

Destaque importante:

Observou-se uma correlação muito forte (~0.79) entre:
🔸 dia_da_semana
🔸fim_de_semana

Isso indica multicolinearidade, o que pode prejudicar a regressão linear.

❌ 4. Exclusão de Feature

Para evitar redundância de informação e instabilidade no modelo, a variável:

🔸dia_da_semana
foi removida, pois sua informação já é representada adequadamente por fim_de_semana.

Essa decisão melhora a robustez estatística e a interpretação do modelo.

🧠 5. Modelagem Preditiva

Foi aplicada Regressão Linear utilizando Scikit-Learn.

O modelo foi avaliado com:

🔸Train/Test split
Métricas:

🔸 R²

🔸MAE

RMSE

📈 6. Resultados
🔸 Métricas no Conjunto de Treino

R² = 0.76

MAE = 2.40

RMSE = 1.55

🔸 Métricas no Conjunto de Teste

R² = 0.77

MAE = 2.29

RMSE = 1.51

<img width="352" height="217" alt="image" src="https://github.com/user-attachments/assets/3c99bec2-93b1-49ee-8a93-0ec0e9ac8a5c" />


✅ O modelo apresentou desempenho consistente e sem overfitting.
✅ Excelente proximidade entre treino e teste.
✅ Boa capacidade de generalização.

📊 7. Visualizações
Real vs Previsto

🔸O gráfico mostra forte alinhamento entre os valores previstos e reais, indicando que o modelo captura bem a tendência dos dados.

<img width="583" height="466" alt="image" src="https://github.com/user-attachments/assets/dd75192e-ce9c-481e-b35a-667ade6e4915" />

Análise dos Resíduos

O histograma apresenta:

🔸Distribuição aproximadamente normal

🔸Simetria ao redor de zero

🔸Ausência de viés sistemático

🔸Erros concentrados próximos de zero

Isso indica que o modelo não apresenta distorções relevantes.

<img width="575" height="464" alt="image" src="https://github.com/user-attachments/assets/6ba3af62-2508-497f-bb1e-bed49de93fe9" />

🔁 8. Validação Cruzada (K-Fold)

O modelo foi avaliado com K-Fold (5 divisões).

RMSE Médio:

Treino ≈ 2.99

Teste ≈ 3.01

✅ Diferença mínima
✅ Alta estabilidade
✅ Baixo risco de overfitting

📌 Conclusão

🔸Os resultados mostram que o modelo de regressão linear apresenta desempenho consistente e estável, com boa capacidade preditiva e comportamento semelhante entre os dados de treino e teste, indicando que é um modelo confiável para o problema analisado.
