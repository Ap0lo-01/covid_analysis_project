from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Carregar os dados
df = pd.read_csv("data/country_wise_latest.csv")

# Configurar a paleta de cores
paleta_casos = sns.color_palette("Blues", 10)
paleta_mortes = sns.color_palette("Reds", 10)
paleta_recuperacoes = sns.color_palette("Greens", 10)

# Função para gerar o gráfico de casos confirmados
def gerar_grafico_casos():
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values(by='Confirmed', ascending=False).head(10)
    plt.bar(df_sorted['Country/Region'], df_sorted['Confirmed'], color=paleta_casos)
    plt.title('Top 10 Países com Mais Casos Confirmados de COVID-19')
    plt.xlabel('País')
    plt.ylabel('Casos Confirmados')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/grafico_casos.png')
    plt.close()

# Função para gerar o gráfico de mortes
def gerar_grafico_mortes():
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values(by='Deaths', ascending=False).head(10)
    plt.bar(df_sorted['Country/Region'], df_sorted['Deaths'], color=paleta_mortes)
    plt.title('Top 10 Países com Mais Mortes por COVID-19')
    plt.xlabel('País')
    plt.ylabel('Mortes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/grafico_mortes.png')
    plt.close()

# Função para gerar o gráfico de recuperações
def gerar_grafico_recuperacoes():
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values(by='Recovered', ascending=False).head(10)
    plt.bar(df_sorted['Country/Region'], df_sorted['Recovered'], color=paleta_recuperacoes)
    plt.title('Top 10 Países com Mais Recuperações de COVID-19')
    plt.xlabel('País')
    plt.ylabel('Recuperações')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/grafico_recuperacoes.png')
    plt.close()

@app.route('/')
def home():
    return render_template('home.html', titulo="Home")

@app.route('/funcionalidade')
def funcionalidade():
    gerar_grafico_casos()
    gerar_grafico_mortes()
    gerar_grafico_recuperacoes()
    return render_template('funcionalidade.html', titulo="Funcionalidade")

@app.route('/apresentacao')
def apresentacao():
    return render_template('apresentacao.html', titulo="Apresentação")

if __name__ == '__main__':
    app.run(debug=True)
