import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (e.g., from a CSV or SQL database)
df = pd.read_csv('your_dataset.csv')

# Display the dataframe
st.write(df)

# Create a plot
fig, ax = plt.subplots()
sns.barplot(x='Column1', y='Column2', data=df, ax=ax)
st.pyplot(fig)
