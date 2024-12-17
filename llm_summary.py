from groq import Groq

# Function to generate llm summary
def generate_llm_summary(groq_api_key, nutritional_insights):
    prompt = f"Summarize the following insights:\nThe following food and drinks are menu item in Starbucks.\n{nutritional_insights}"
    client = Groq(api_key=groq_api_key)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    summary = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            summary += chunk.choices[0].delta.content
    return summary


# Function to extract key insights
def extract_nutritional_insights(df_food, df_drink):

    # Extract insights for food
    food_max_calories = 'N/A'
    food_max_carb = 'N/A'

    # Loop through columns to find those containing "Calories" and "Carb"
    for col in df_food.columns:
        if 'Calories' in col:
            # Get the item with the highest calories
            food_max_calories = df_food.loc[df_food[col].idxmax(), 'Item']
        
        if 'Carb' in col:
            # Get the item with the highest carbs
            food_max_carb = df_food.loc[df_food[col].idxmax(), 'Item']

    # Extract insights for drinks
    drink_max_sodium = df_drink.loc[df_drink['Sodium'].idxmax(), 'Item'] if 'Sodium' in df_drink else 'N/A'
    drink_max_calories = df_drink.loc[df_drink['Calories'].idxmax(), 'Item'] if 'Calories' in df_drink else 'N/A'

    # Combine insights into a string
    insights = (f"Food with the highest carbohydrate content: {food_max_carb}\n"
                f"Food with the highest calories: {food_max_calories}\n"
                f"Drink with the highest sodium content: {drink_max_sodium}\n"
                f"Drink with the highest calories: {drink_max_calories}")
    
    return insights