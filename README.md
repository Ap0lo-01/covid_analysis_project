# Projeto de Análise de Dados COVID-19

## Descrição

Este projeto visa integrar conhecimentos de manipulação de dados, visualização gráfica e desenvolvimento web para criar uma solução prática para analisar dados de COVID-19.

Utilizamos ferramentas como Pandas para manipulação de dados, Matplotlib e Seaborn para geração de gráficos, e Flask para desenvolvimento de um site interativo.

## Estrutura do Projeto

covid_analysis_project/ ├── app.py├── static/ │ └── styles.css├── templates/ │ ├── base.html│ ├── home.html│ ├── funcionalidade.html│ ├── apresentacao.html├── data/ │ └── country_wise_latest.csv ├── requirements.txt└── README.md

## Funcionalidades

1. **Manipulação de Dados com Pandas**
   - Limpeza, transformação e análise de dados relacionados ao COVID-19.
   
2. **Geração de Gráficos com Matplotlib e Seaborn**
   - Gráficos dinâmicos mostrando casos confirmados, mortes e recuperações de COVID-19.
   
3. **Desenvolvimento do Site com Flask**
   - Página HOME: Apresenta o problema, a solução proposta e informações sobre a base de dados utilizada.
   - Página FUNCIONALIDADE: Permite interação com os dados e visualização dos gráficos.
   - Página APRESENTAÇÃO: Apresenta o(s) membro(s) do grupo e suas contribuições para o projeto.

## Base de Dados

Os dados utilizados neste projeto foram obtidos de [COVID-19 Dataset - Kaggle](https://www.kaggle.com/datasets/imdevskp/corona-virus-report), uma fonte confiável e atualizada.

### Contexto do Dataset
Um novo coronavírus denominado 2019-nCoV foi identificado pela primeira vez em Wuhan, capital da província de Hubei, na China. Pessoas desenvolveram pneumonia sem uma causa clara e para a qual as vacinas ou tratamentos existentes não eram eficazes. O vírus demonstrou evidências de transmissão de pessoa para pessoa. A taxa de transmissão (taxa de infecção) pareceu aumentar em meados de janeiro de 2020. Em 30 de janeiro de 2020, aproximadamente 8.243 casos foram confirmados.
