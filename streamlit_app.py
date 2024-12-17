import streamlit as st
from data_loader import load_data, show_cleaned_data
from data_processing import remove_empty_row, generate_desc_stat, convert_to_float, calc_calories_mean
from data_visualization import visualize_nutritional_comparison
from llm_summary import extract_nutritional_insights, generate_llm_summary

def main():
    st.title("LLM-Powered Nutrition Analysis Tool")

    # File upload
    st.markdown("# File Upload") # H1
    uploaded_files = st.file_uploader("Please upload your CSV files. Start by uploading the food dataset, followed by the drink dataset.", type=[
                                    "csv"], accept_multiple_files=True)


    if uploaded_files:
        dataframes = load_data(uploaded_files)

        # Display data preview and remove empty row
        st.markdown("# Data Preview") # H1
        for i, df in enumerate(dataframes):
            file_name = uploaded_files[i].name

            # Convert the datatype to floating-point except 'Item' column
            convert_to_float(df)

            # Remove empty row in the dataframe
            remove_empty_row(df)

            # Show cleaned data preview
            show_cleaned_data(df, file_name)

        # Assuming user will always upload two csv files where food is the first dataset and drink is the second dataset
        food_df = dataframes[0]
        drink_df = dataframes[1]

        # Generate descriptive statistics
        st.markdown("# Descriptive Statistics") # H1
        st.markdown("## Food dataset") # H2
        st.markdown("### Summary:") # H3
        generate_desc_stat(food_df)
        st.markdown("## Drinks dataset") # H2
        st.markdown("### Summary:") # H3
        generate_desc_stat(drink_df)

        # Compare the average calories for food and drink
        st.markdown("### Comparison between food and drinks datasets:") # H3
        food_calories_mean = calc_calories_mean(food_df)
        st.write(f"Mean calories for food: {food_calories_mean:.2f}")
        drink_calories_mean = calc_calories_mean(drink_df)
        st.write(f"Mean calories for drink: {drink_calories_mean:.2f}")
        if food_calories_mean > drink_calories_mean:
            st.write("Starbuck's food have higher average calories compared to their drinks.")
        elif drink_calories_mean > food_calories_mean:
            st.write("Starbuck's drinks have higher average calories compared to their food.")
        else:
            st.write("Starbuck's food and drinks have similar average calories.")

        # Plot graph
        st.markdown("# Data Visualization") # H1
        st.markdown("## Food dataset") # H2
        visualize_nutritional_comparison(food_df)
        st.markdown("## Drinks dataset") # H2
        visualize_nutritional_comparison(drink_df)

        # LLM Summarization
        st.markdown("# LLM-Based Summarization")
        nutritional_insights = extract_nutritional_insights(food_df, drink_df)
        st.write("Extract the nutritional insights:")
        st.text(nutritional_insights)
        st.write(
            "This section utilizes the Groq LLM API to generate a nutritional summarization. "
            "To access this feature, please provide a valid Groq API key. You can obtain your API key [here](https://console.groq.com/keys)."
        )
        groq_api_key = st.text_input("Groq API Key", type="password")
        if groq_api_key:
            summary = generate_llm_summary(groq_api_key, nutritional_insights)
            st.markdown(f"LLM Summary:\n\n {summary}")


if __name__ == "__main__":
    main()

    