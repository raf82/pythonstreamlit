import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Colégio Santa Maria",
    #page_icon = "🦖",
    #page_icon="🎯",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

</style>
""", unsafe_allow_html=True)

st.write("""
# Colégio Santa Maria
Notas totais da 1ª e 2ª etapas dos alunos do 2º ano do ensino médio

""")

df = pd.read_excel('alunos_02.xlsx', sheet_name = "notas2")

st.sidebar.header ('Opções')

disciplinas = list(df.columns.values)
disciplina = st.sidebar.selectbox('Disciplina',disciplinas[2:])

grafico = st.sidebar.selectbox('Forma de exibição',["Tabela","Gráfico (Barras)","Gráfico (Dispersão)"])

fig, ax = plt.subplots(figsize=(4, 1.5))

if grafico == "Tabela":
    for i in disciplinas:
        if disciplina == i:
            df1 = df[['Alunos_nome',disciplina]]
            df2 = pd.DataFrame(columns = ["Alunos 1", disciplina+"1","Alunos 2", disciplina+"2"])
            for i in np.arange(0,19):
                arr1 = np.array(df1.iloc[i::19])
                arr2 = np.reshape(arr1,(19))
                df2.loc[len(df2)]=arr2
                
            st.table(df2)
            
elif grafico == "Gráfico (Barras)":
    for i in disciplinas:
        if disciplina == i:
            means = df[i].mean()
            barplot = sns.barplot(x="Alunos_num",y=i,data = df, ax=ax)
            ax.set_ylim(0, 75)
            barplot.axhline(y=means,linewidth = 1, color="red", ls=':', label="Média da turma")
            barplot.axhline(y=39,linewidth = 1, color="black", ls='-', label="Média global")
            plt.xlabel('Alunos', fontsize=10);
            plt.ylabel(i, fontsize=10);
            plt.tick_params(axis='x', which='major', labelsize=3)
            plt.tick_params(axis='y', which='major', labelsize=5)
            ax.legend(loc='upper center', borderaxespad=0,ncol=2,fontsize=5,frameon=False)

            st.pyplot(plt.gcf())

elif grafico == "Gráfico (Dispersão)":
    for i in disciplinas:
        if disciplina == i:
            means = df[i].mean()
            scatterplot = sns.scatterplot(x="Alunos_num",y=i,data = df,s=15, ax=ax)
            ax.set_ylim(0, 75)
            scatterplot.axhline(y=means,linewidth = 1, color="red", ls=':',label="Média da turma")
            scatterplot.axhline(y=39,linewidth = 1, color="black", ls='-',label="Média global")
            plt.xlabel('Alunos', fontsize=10);
            plt.ylabel(i, fontsize=10);
            plt.tick_params(axis='x', which='major', labelsize=3)
            plt.tick_params(axis='y', which='major', labelsize=5)
            ax.set_xticks(df["Alunos_num"])
            ax.legend(loc='upper center', borderaxespad=0,ncol=2,fontsize=5,frameon=False)

            st.pyplot(plt.gcf())
    
