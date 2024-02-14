import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel(r'*your path*\Dashboard\Dashboard\assets\databse1.xlsx')

st.set_page_config(
    "Sales Dashboard",
    layout="wide",
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help' : 'https://www.mysite.com/',
        'About' : 'App developed in the course'
    }
)

with st.sidebar:
    fSeller = st.selectbox(
        "Select the seller: ",
         options=df['Seller'].unique()
    )
    fProduct = st.selectbox(
        "Select the product:",
        options=df['Sold Product'].unique()
    )
    fClient = st.selectbox(
        "Select the client: ",
        options=df['Client'].unique()
    )
    qty_product_table = df.loc[
        (df['Seller'] == fSeller) &
        (df['Client'] == fClient)]

    qty_product_table = qty_product_table.drop(columns=['Date',
                                                        'Seller',
                                                        'Client',
                                                        'Order No',
                                                        "Region"])

    qty_product_table = qty_product_table.groupby('Sold Product').sum().reset_index()

sales_margin_table = df.loc[(
    df['Seller'] == fSeller) &
    (df['Sold Product'] == fProduct) &
    (df['Client'] == fClient)]

sales_seller_table = df.loc[
    (df['Sold Product'] == fProduct) &
    (df['Client'] == fClient)
]
sales_seller_table = sales_seller_table.drop(columns=['Date',
                                                      'Client',
                                                      "Region",
                                                      'Sold Product',
                                                      'Order No',
                                                      'Price'])

sales_seller_table = sales_seller_table.groupby('Seller').sum().reset_index()

sales_client_table = df.loc[(df['Seller'] == fSeller) & 
                              (df['Sold Product'] == fProduct)]

sales_client_table = sales_client_table.drop(columns=['Date',
                                                      "Region",
                                                      'Sold Product',
                                                      'Order No',
                                                      'Price',
                                                      'Seller'])
sales_client_table = sales_client_table.groupby('Client').sum().reset_index()

graph_qty_product = px.bar(qty_product_table, x='Sold Product',
                            y='Quantity',
                            title="Quantity Sold per Product")

graph_value_product = px.bar(qty_product_table, x='Sold Product',
                            y='Order Value',
                            title="Total Value per Product")

graph_total_seller = px.bar(sales_seller_table, x='Seller',
                            y='Order Value',
                            title="Sales Value per Seller")

st.header(":bar_chart: Sales Dashboard")
st.write("---")
col1, col2, col3 = st.columns([2, 2, 3], gap='small')

total_sales = round(sales_margin_table['Order Value'].sum(), 2)
total_margin = round(sales_margin_table['Profit Margin'].sum(), 2)
margin_percentage = int(100 * total_margin / total_sales)

st.write("---")

with col1:
    st.metric("Total Sales", value=f"R${total_sales}")

with col2:
    st.metric("Total Margin", value=f"R${total_margin}")

with col3:
    st.metric("Margin Percentage", value=f"{margin_percentage}%")

st.write(graph_qty_product)
with st.expander("Table View: "):
    st.write(qty_product_table)

st.write(graph_value_product)
with st.expander("Table View: "):
    st.write(qty_product_table)

st.write(graph_total_seller)
with st.expander("Table View: "):
    st.write(sales_seller_table)
