import streamlit as st
import joblib
import numpy as np
import pandas as pd


st.set_page_config(
    page_title='Previsão de Consumo de Energia',
    layout='centered'
)

st.title('Previsão de Consumo de Energia Elétrica')

with st.expander("Como funciona a previsão de consumo?"):
    st.write("""
    O sistema utiliza técnicas de **Machine Learning** para estimar o **consumo de energia elétrica (kWh)**
    de uma residência com base em variáveis do dia e características do imóvel.  
    A base de dados utilizada contém as seguintes colunas:

    - **data**: data da medição do consumo;
    - **temperatura**: temperatura média do dia;
    - **fim_de_semana**: indicador de final de semana (0 = não, 1 = sim);
    - **feriado**: indica se o dia é feriado (0 = não, 1 = sim);
    - **area_m2**: área do imóvel em metros quadrados;
    - **numero_moradores**: quantidade de pessoas na residência;
    - **consumo_kwh**: consumo de energia elétrica em kWh (**variável alvo**).

    O processo de previsão é dividido em três etapas principais:

    1. **Preparação dos Dados**  
       Antes do treino, as variáveis categóricas são convertidas para formato numérico: 
       - `fim_de_semana` e `feriado` são convertidos para 0/1.  

    2. **Treinamento do Modelo (Regressão Linear)**  
       Utilizamos **Regressão Linear** (scikit-learn), um modelo de regressão que aprende uma relação
       entre as variáveis (temperatura, dia da semana, feriado, área e moradores) e o consumo em kWh.
       O objetivo é minimizar o erro entre o consumo real e o previsto.

    3. **Previsão do Consumo**  
       Quando o usuário informa os dados, essas entradas passam pela **mesma padronização** usada no treinamento e são enviadas ao modelo.
       O resultado é o **consumo estimado em kWh** para aquela situação.

    **Desempenho do modelo (referência):**  
    - **R² ~ 0,77** tanto no treino quanto no teste, indicando que o modelo explica cerca de **77%**
      da variação do consumo e generaliza bem (sem sinais fortes de overfitting).  
    - **MAE ~ 2,2 kWh**, ou seja, em média o modelo erra cerca de **2,2 kWh** por previsão.  
    - O **RMSE** fica um pouco acima do MAE, indicando que existem alguns erros maiores pontuais,
      mas sem comprometer o desempenho geral.

    Dessa forma, o sistema fornece uma estimativa de consumo consistente e útil para apoiar
    planejamento e análise de gasto energético.
    """)

modelo = joblib.load('modelo.pkl')

fim_de_semana = st.selectbox("É fim de semana?", options=["Sim", "Não"])
fim_de_semana = 1 if fim_de_semana == "Sim" else 0

feriado = st.selectbox("É feriado?", options=["Sim", "Não"])
feriado = 1 if feriado == "Sim" else 0

temperatura = st.number_input("Temperatura média do dia (°C):", min_value=-10.0, max_value=60.0, value=25.0, step=0.1, format="%.1f")
area_m2 = st.number_input("Área do imóvel (m²):", min_value=1, step=1, value=50, format="%d")
numero_moradores = st.number_input("Número de moradores:", min_value=1, step=1, value=2, format="%d")

enviar = st.button("Prever Consumo (kWh)")

if enviar:
    if temperatura == '' or area_m2 == '' or numero_moradores == '':
        st.warning('Por favor, preencha todos os campos antes de enviar.')
    else:

        entrada = np.array([[fim_de_semana, feriado, temperatura, area_m2, numero_moradores]])

        consumo_previsto = modelo.predict(entrada)[0]

        st.write(f"Consumo previsto: **{consumo_previsto:.2f} kWh**")
