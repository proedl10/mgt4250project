import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st
import os
!pip install openpyxl

# Get the absolute path of the current script
current_path = os.path.dirname(os.path.abspath(__file__))

# Update file paths using os.path.join
white_path = os.path.join(current_path, "GP White .xlsx")
black_path = os.path.join(current_path, "GP Black.xlsx")
hispanic_path = os.path.join(current_path, "GP Hispanic .xlsx")
edu_path = os.path.join(current_path, "Education Income data.xlsx")

# Print file paths for debugging
print("White Path:", white_path)
print("Black Path:", black_path)
print("Hispanic Path:", hispanic_path)
print("Education Path:", edu_path)

st.set_page_config(layout="wide")
st.title("Income Inequality Visualizations")

col1, col2, col3 = st.columns([3, 3, 3])

with col1:
    st.title("Median Income White")
    df_white = pd.read_excel(white_path)
    st.write(df_white.head())
    
    st.title("Median Income Black")
    df_black = pd.read_excel(black_path)
    st.write(df_black.head())
    
    var1 = df_white[' Median income Estimate  ($)']
    var2 = df_black[' Median income Estimate  ($)']
    
    fig, ax = plt.subplots()
    ax = plt.scatter(var1, df_white['Race and Hispanic origin of householder'], label="White Median Income")
    plt.scatter(var2, df_black['Race and Hispanic origin of householder'], label="Black Median Income")
    plt.xlabel("Median Income by Race")
    plt.ylabel("Year")
    plt.title("Black & White Median Income by Race")
    plt.legend()
    st.pyplot(fig)

with col2:
    st.title("Median Income Hispanic")
    df_hispanic = pd.read_excel(hispanic_path)
    st.write(df_hispanic.head())
    
    var2 = df_hispanic[' Median income Estimate  ($)']
    
    fig, ax = plt.subplots()
    ax = plt.bar(df_hispanic['Race and Hispanic origin of householder'], var2)
    plt.xlabel("Year")
    plt.ylabel("Median Income ($)")
    plt.title("Hispanic Median Income by Year")
    st.pyplot(fig)

with col3:
    st.title("Income by Education")
    edu_inc = pd.read_excel(edu_path)
    st.write(edu_inc.head())

    fig, ax = plt.subplots()
    ax = plt.barh(edu_inc['Level of Education '], edu_inc['Median Income in U.S. Dollars'])
    plt.xlabel("Median Income")
    plt.ylabel("Level of Education")
    plt.title("Median Income by Education")
    plt.legend()
    st.pyplot(fig)
