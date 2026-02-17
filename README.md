# ⚡ Previsão de Consumo de Energia Elétrica  
### Machine Learning com Scikit-Learn, XGBoost e Spark ML + Deploy com Streamlit

Este projeto demonstra a construção de modelos de regressão para previsão do consumo de energia elétrica (kWh) utilizando duas abordagens distintas:

- ✅ **Scikit-Learn + XGBoost (ambiente local / single-machine)**
- ✅ **Spark MLlib (ambiente distribuído / Big Data)**

O modelo disponibilizado na aplicação web foi treinado com **XGBoost** e posteriormente exportado para produção.

---

## 🎯 Objetivo

Prever o consumo diário de energia elétrica (kWh) de uma residência com base nas seguintes variáveis:

- Temperatura média do dia  
- Indicador de fim de semana  
- Indicador de feriado  
- Área do imóvel (m²)  
- Número de moradores  

---

## 🧠 Modelagem

### 🔹 1. Implementação com Scikit-Learn + XGBoost

- Tratamento e transformação de dados  
- Conversão de variáveis categóricas para formato numérico (0/1)  
- Padronização das variáveis com `StandardScaler`  
- Aplicação de regressão com **XGBoost Regressor**  
- Avaliação de métricas (R², MAE, RMSE)  
- Serialização do modelo (`modelo_xgb.pkl`)  
- Serialização do scaler (`scaler.pkl`)  
- Modelo utilizado no deploy  

**Notebook de treinamento:**  
`Machine_Learning_Regressão_Consumo_de_Energia.ipynb`

---

### 🔹 2. Implementação com Spark ML (PySpark)

- Criação de pipeline distribuído  
- Manipulação de dados em ambiente Spark  
- Treinamento de modelo de regressão utilizando MLlib  
- Comparação de desempenho  

**Notebook Spark:**  
`Spark - ML Regressão (valor consumo energia).ipynb`

---

## 🚀 Deploy da Aplicação

A aplicação foi desenvolvida em **Streamlit**, permitindo que o usuário insira dados e receba a previsão em tempo real.

**Arquivo principal:**  
`Main.py`

---

### 🔄 Fluxo da aplicação

1. Usuário insere dados no formulário  
2. Aplicação converte variáveis categóricas (Sim/Não → 0/1)  
3. Dados são padronizados utilizando o scaler salvo  
4. Modelo treinado com XGBoost é carregado via `joblib`  
5. Dados são convertidos em `DMatrix` (estrutura otimizada do XGBoost)  
6. Previsão é realizada e exibida em kWh  

---
<img width="825" height="743" alt="image" src="https://github.com/user-attachments/assets/d1c5f669-80f9-4a4d-8b02-98f38f7abca5" />
