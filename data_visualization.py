import streamlit as st
import matplotlib.pyplot as plt

# Function to plot a nutritional comparison bar chart for food
def visualize_nutritional_comparison(df):
    # Randomly sample 10 menu items
    st.write("10 Random Sample Menu Items:")
    df_random = df.sample(n=10)
    st.dataframe(df_random)

    # Select columns to be visualized
    keywords = ['Fat', 'Carb', 'Fiber', 'Protein']
    columns = [column for column in df if any(keyword in column for keyword in keywords)]

    # Filter nutritional columns for the random selection
    df_random_selected = df_random[columns]

    # Plot Bar Chart for Calories, Sugars, and Fats
    st.write("Nutritional Comparison (Fats, Carb, Fiber and Protein) Between Menu Items:")
    
    # Create a bar chart comparing the key nutritional aspects for each item
    df_random_selected.set_index(df_random['Item'], inplace=True)
    df_random_selected.plot(kind='bar', figsize=(10, 6))
    
    plt.title("Comparison of Nutritional Aspects Between Menu Items")
    plt.ylabel("Amount (g)")
    plt.xlabel("Menu Items")
    plt.xticks(rotation=45, ha='right')
    plt.yticks(range(0, 100, 10))
    
    # Show the plot
    st.pyplot(plt)

