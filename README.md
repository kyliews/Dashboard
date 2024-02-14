
Interactive control panel for sales data analysis, developed in Python using the Streamlit and Plotly Express libraries.

Project Structure:

•app.py: The main code for the Streamlit application.

•assets/base_dados.xlsx: Excel file containing the database.

Main Features:

Parameter Selection: Users can choose the seller, product, and customer through dropdowns in the sidebar.

Interactive Visualizations: The dashboard presents interactive graphs using the Plotly Express library, including quantity sold per product, total value per product, and sales value per seller.

Key Metrics: Displays important metrics such as total sales, total margin, and margin percentage.

Detailed Tables: Provides detailed tables that support the graphs, allowing users to explore specific data.

Expanders: Uses expanders to hide/expand tables, enhancing the user experience.

How to Use:

Clone the repository: https://github.com/kyliews/Dashboard

Navigate to the project directory: cd Dashboard

In the app.py file, locate line 5, which contains the Excel file reading.

Change the path of the Excel file to reflect the location of your repository.

df = pd.read_excel(r'your path\Dashboard\assets\base_dados.xlsx')

Run the application: streamlit run app.py
