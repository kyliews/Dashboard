import streamlit as st 
import pandas as pd
import plotly.express as px

df = pd.read_excel(r'C:\Users\Admin\Documents\projetos Python\Dashboard\Dashboard\assets\base_dados.xlsx')

st.set_page_config(
    "Dashboard de Vendas",
    layout="wide",
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help' : 'https://www.meusite.com.br/',
        'About' : 'App desenvolvido no curso'
    }
)

with st.sidebar:
    #st.subheader("MENU - DASHBOARD DE VENDAS")
    fVendedor = st.selectbox(
        "Selecione o vendedor: ",
         options=df['Vendedor'].unique()
    )
    fProduto = st.selectbox(
        "Selecione o produto:",
        options=df['Produto vendido'].unique()
    )
    fCliente = st.selectbox(
        "Selecione o cliente: ",
        options=df['Cliente'].unique()
    )
    tabel_qtde_produto = df.loc[
        (df['Vendedor'] == fVendedor) &
        (df['Cliente'] == fCliente)]
    
#tabela de quantidade de vendas por produto
    tabel_qtde_produto = tabel_qtde_produto.drop(columns= ['Data',
                                                           'Vendedor',
                                                           'Cliente',
                                                           'Nº pedido',
                                                           "Região"])
    
    tabel_qtde_produto = tabel_qtde_produto.groupby('Produto vendido').sum().reset_index()
    
#tabela de vendas e margem
tabel_vendas_margem = df.loc[(
    df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente)]
#tabel_vendas_margem                    



#tabela de vendas por vendedor
tabel_vendas_vendedor = df.loc[
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente)
]
tabel_vendas_vendedor = tabel_vendas_vendedor.drop(columns= ['Data',
                                                          'Cliente',
                                                           "Região",
                                                           'Produto vendido',
                                                           'Nº pedido',
                                                           'Preço'])
    
tabel_vendas_vendedor = tabel_vendas_vendedor.groupby('Vendedor').sum().reset_index()
#tabel_vendas_vendedor



tabel_vendas_cliente = df.loc[(df['Vendedor'] == fVendedor) & 
                              (df['Produto vendido'] == fProduto)]

tabel_vendas_cliente = tabel_vendas_cliente.drop(columns= ['Data',
                                                           "Região",
                                                           'Produto vendido',
                                                           'Nº pedido',
                                                           'Preço',
                                                           'Vendedor'])
tabel_vendas_cliente = tabel_vendas_cliente.groupby('Cliente').sum().reset_index()
#tabel_vendas_cliente

#grafico por produto vendido
graf1_qtde_produto = px.bar(tabel_qtde_produto,x='Produto vendido',
                            y='Quantidade',
                            title="Quantidade Vendida por Produto")

#graf1_qtde_produto

#grafico valor da venda por produto
graf2_valor_produto = px.bar(tabel_qtde_produto,x='Produto vendido',
                            y='Valor Pedido',
                            title="Valor total por Produto")

#graf2_valor_produto

#grafico de total de venda por vendedor:

graf3_total_vendedor = px.bar(tabel_vendas_vendedor,x='Vendedor',
                            y='Valor Pedido',
                            title="Valor da Venda por Vendedor")

#graf3_total_vendedor

st.header(":bar_chart: Dashboard de Vendas")
st.write("---")
col1,col2,col3 = st.columns([2,2,3],gap='small')

total_vendas = round(tabel_vendas_margem['Valor Pedido'].sum(),2)
total_margem = round(tabel_vendas_margem['Margem Lucro'].sum(),2)
porc_margem = int(100*total_margem/total_vendas)

st.write("---")

with col1:
    st.metric("Vendas Totais",value=f"R${total_vendas}")
    
with col2:
    st.metric("Margem total",value=f"R${total_margem}")
    
with col3:
    st.metric("Margem",value=f"R${porc_margem}%")
    
    
    
st.write(graf1_qtde_produto)
with st.expander("Visualização da tabela: "):
    st.write(tabel_qtde_produto)
    
st.write(graf2_valor_produto)
with st.expander("Visualização da tabela: "):
    st.write(tabel_qtde_produto)
    
st.write(graf3_total_vendedor)
with st.expander("Visualização da tabela: "):
    st.write(tabel_vendas_vendedor)
    