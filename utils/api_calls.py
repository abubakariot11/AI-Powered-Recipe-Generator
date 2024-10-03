import os
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

openai.api_key = OPENAI_API_KEY

def get_recipe(mood, ingredients, dietary_restrictions):
    # Generate a prompt based on user input
    prompt = f"Suggest a recipe that suits the mood '{mood}' using the ingredients '{ingredients}' and considering '{dietary_restrictions}' restrictions."

    # OpenAI API call
    response = openai.chat.completions.create(
        model ="gpt-4-turbo",
        
     messages=[
            {"role": "system", "content": "You are a helpful AI travel assistant. You will give advices about places to visit"},
            {"role": "user", "content": prompt}
        ]
    )

    # Get the recipe text from the response
    recipe = response.choices[0].message.content

    

    return recipe
