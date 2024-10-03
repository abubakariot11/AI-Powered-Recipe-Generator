from flask import Flask, render_template, request
from utils.api_calls import get_recipe
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    mood = request.form['mood']
    ingredients = request.form['ingredients']
    dietary_restrictions = request.form['dietary_restrictions']

    # Call the function that handles API requests
    recipe = get_recipe(mood, ingredients, dietary_restrictions)
    
    return render_template('index.html', recipe=recipe)

