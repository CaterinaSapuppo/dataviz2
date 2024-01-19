# Import necessary libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Read data from an Excel file
df = pd.read_excel('internet.xlsx')

# Data preparation: Melting and cleaning the data
df_melted = df.melt(id_vars=["Country Name"], var_name="Year", value_name="Internet Usage Percentage")
df_melted = df_melted.dropna()

# Create a sidebar for selecting a country
country = st.sidebar.selectbox('Select a Country', df_melted['Country Name'].unique())

# Filter data based on the selected country
filtered_data = df_melted[df_melted['Country Name'] == country]

# Create a bar plot using Plotly Express
fig = px.bar(
    filtered_data,
    x="Year",
    y="Internet Usage Percentage",
    title=f"Internet Usage Percentage in {country}",
    color_discrete_sequence=['black']
)

# Customize plot layout
fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    plot_bgcolor='white',
    margin=dict(l=20, r=20, t=50, b=20),
    title_font=dict(color='darkgrey'),
    font=dict(color='black')
)

# Remove titles from x and y axes
fig.update_xaxes(title='', showgrid=False)
fig.update_yaxes(title='', showgrid=False)

# Customize y-axis tick values and labels
fig.update_yaxes(tickvals=[20, 40, 60, 80, 100], ticktext=['20%', '40%', '60%', '80%', '100%'])

# Display the plot in Streamlit
st.plotly_chart(fig)
