import streamlit as st
import pandas as pd

# Function to remove empty row
def remove_empty_row(df):
    # Drop rows where all columns except the first column are NaN
    df = df.dropna(inplace=True, how='all', subset=df.columns[1:])
    
# Function to generate descriptive statistic
def generate_desc_stat(df):
    st.write(df.describe(percentiles=[.25, .5, .75]))
    for column in df.select_dtypes(include=['number']).columns:
        mean = round(df[column].mean(),2)
        st.write(f"Mean for {column}: {mean:.2f}")

# Function to convert the datatype to float
def convert_to_float(df):
    for col in df.columns:
        if 'Item' not in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert column to float64
    return df

# Function to calculate the mean
def calc_calories_mean(df):
    mean_calories = 0.0
    for column in df.select_dtypes(include=['number']).columns:
        if 'Calories' in column:
            mean_calories = round(df[column].mean(),2)
            break
    return mean_calories
        