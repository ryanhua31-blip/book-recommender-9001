import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from src.user_input import user_input
from src.prompts import get_prompt, get_prompt_image
from src.recommendations import get_ai_recommendations
from src.display import display_recommendations
import json
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)
"""
# Book Recommender 9001 📖📚
*"Indisputably, this is quite possibly the most sublime book recommender in existence."*
—Shakespeare

---

"""

liked_books, liked_genres, unliked_books, unliked_genres = user_input()

'''

---

'''

prompt = get_prompt(liked_books, liked_genres, unliked_books, unliked_genres)
prompt_image = get_prompt_image()

get_ai_recommendations(client, prompt, prompt_image)
display_recommendations()