# ⚡ Previsão de Consumo de Energia Elétrica  
### Machine Learning com Scikit-Learn, XGBoost e Spark ML + Deploy com Streamlit

Este projeto apresenta a construção e comparação de modelos de regressão para previsão do consumo diário de energia elétrica (kWh), utilizando duas abordagens distintas:

- ✅ **Scikit-Learn + XGBoost (ambiente local / single-machine)**
- ✅ **Spark MLlib (ambiente distribuído / Big Data)**

O modelo disponibilizado na aplicação web foi treinado com **XGBoost** e exportado para produção.

---

## 📌 Contexto do Problema

A previsão do consumo energético auxilia no planejamento de custos, eficiência energética e dimensionamento de infraestrutura elétrica.

Modelos preditivos permitem estimar o consumo diário com base em características do imóvel e condições externas, fornecendo suporte para decisões estratégicas.

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
- Treinamento com **XGBoost Regressor**  
- Avaliação com métricas de regressão (R², MAE, RMSE)  
- Serialização do modelo (`modelo_xgb.pkl`)  
- Serialização do scaler (`scaler.pkl`)  
- Modelo utilizado no deploy  

📓 Notebook de treinamento:  
`Machine_Learning_Regressão_Consumo_de_Energia.ipynb`

---

### 🔹 2. Implementação com Spark ML (PySpark)

- Criação de pipeline distribuído  
- Manipulação de dados em ambiente Spark  
- Treinamento com MLlib  
- Comparação de desempenho com abordagem local  

📓 Notebook Spark:  
`Spark - ML Regressão (valor consumo energia).ipynb`

---

## 📊 Resultados

**Modelo XGBoost:**

- R²: 0.81  
- RMSE: 2.70 kWh  
- MAE: 2.12 kWh  

Comparação entre abordagens indicou desempenho semelhante, com vantagem do XGBoost em precisão e facilidade de deploy.

---

## 🚀 Deploy da Aplicação

A aplicação foi desenvolvida em **Streamlit**, permitindo que o usuário insira dados e receba a previsão em tempo real.

Arquivo principal:  
`Main.py`

### 🔄 Fluxo da aplicação

1. Usuário insere dados no formulário  
2. Variáveis categóricas são convertidas (Sim/Não → 0/1)  
3. Dados são padronizados com o scaler salvo  
4. Modelo XGBoost é carregado via `joblib`  
5. Dados são convertidos para `DMatrix` (estrutura otimizada do XGBoost)  
6. Previsão é realizada e exibida em kWh  

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação

```bash
streamlit run Main.py
```

---

## 🏗 Diferenciais Técnicos

- Comparação entre ambiente single-machine e distribuído  
- Pipeline completo: tratamento → treino → avaliação → serialização → deploy  
- Uso de `DMatrix` para inferência otimizada  
- Estrutura preparada para escalabilidade  

---

## 🛠 Stack Tecnológica

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/XGBoost-EC4E20?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</div>

---

## 📷 Preview da Aplicação

<img width="825" height="743" alt="Preview da aplicação" src="https://github.com/user-attachments/assets/d1c5f669-80f9-4a4d-8b02-98f38f7abca5" />
