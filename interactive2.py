import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_excel('internet.xlsx')

# Data preparation
df_melted = df.melt(id_vars=["Country Name"], var_name="Year", value_name="Internet Usage Percentage")
df_melted = df_melted.dropna()

# Sidebar for country selection
country = st.sidebar.selectbox('Select a Country', df_melted['Country Name'].unique())

# Filter data based on selection
filtered_data = df_melted[df_melted['Country Name'] == country]

# Plotting
fig = px.bar(filtered_data, 
             x="Year", 
             y="Internet Usage Percentage", 
             title=f"Internet Usage Percentage in {country}",
             color_discrete_sequence=['white']) 

fig.update_layout(autosize=False, width=800, height=600, 
                  plot_bgcolor='white', 
                  margin=dict(l=20, r=20, t=50, b=20),
                  title_font=dict(color='black'), 
                  font=dict(color='black'))

fig.update_xaxes(title='')
fig.update_yaxes(title='')
fig.update_yaxes(tickvals=[20, 40, 60, 80, 100], ticktext=['20%', '40%', '60%', '80%', '100%'])

# Display the plot
st.plotly_chart(fig)
