Painel de controle interativo para análise de dados de vendas, desenvolvido em Python usando as bibliotecas Streamlit e Plotly Express.

Estrutura do Projeto:

•app.py: O código principal do aplicativo Streamlit.
•assets/base_dados.xlsx: Arquivo Excel contendo os dados de vendas.

Funcionalidades Principais:

Seleção de Parâmetros:
O usuário pode selecionar o vendedor, produto e cliente através de dropdowns na barra lateral.

Visualizações Interativas:
O dashboard apresenta gráficos interativos usando a biblioteca Plotly Express, incluindo quantidade vendida por produto, valor total por produto e valor da venda por vendedor.

Métricas Principais:
Exibe métricas importantes, como vendas totais, margem total e percentual de margem.

Tabelas Detalhadas:
Fornece tabelas detalhadas que suportam os gráficos, permitindo ao usuário explorar dados específicos.

Expansores:
Utiliza expansores para ocultar/expandir as tabelas, melhorando a experiência do usuário.

Como Usar:

1. Clone o repositório:
https://github.com/kyliews/Dashboard

2. Navegue até o diretório do projeto:
cd Dashboard

3. Execute o aplicativo
streamlit run app.py

