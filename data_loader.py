import streamlit as st
import pandas as pd

# Function to load data
def load_data(uploaded_files):
    dataframes = []
    for file in uploaded_files:
        # Read the CSV file without assuming any headers
        if file.name == "starbucks-menu-nutrition-food.csv":
            try:
                df = pd.read_csv(file, header=None, encoding='UTF-16')
                df.columns = df.iloc[0]  # Assign first row as headers
                df = df.drop(index=0) # Drop the first row now that it's used as headers
                df.rename(columns={df.columns[0]: 'Item'}, inplace=True)
                
                dataframes.append(df)
            except Exception as e:
                st.error(f"Error reading {file.name}: {e}")
                continue
        else:
            try:
                df = pd.read_csv(file, header=None, encoding='UTF-8')
                df.columns = df.iloc[0]  # Assign first row as headers
                df = df.drop(index=0) # Drop the first row now that it's used as headers
                df.rename(columns={df.columns[0]: 'Item'}, inplace=True)
                
                dataframes.append(df)
            except Exception as e:
                st.error(f"Error reading {file.name}: {e}")
                continue
    return dataframes
    
# Function to show cleaned data preview
def show_cleaned_data(df, file_name):
    st.write(f"Cleaned Data Preview of {file_name}")
    st.dataframe(df.head(10)) # Show the first 10 rows