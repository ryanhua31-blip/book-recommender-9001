import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
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

st.write("First, write down some stuff you like",)

c = st.columns(2)

# Good Book Entries
with c[0]:
    liked_books = st.text_input("Enter some book(s) you like here")

# Genre Entry
with c[1]:
    liked_genres = st.text_input("Enter some genre(s) you like here")
    
'''

---

'''

st.write("Now, write down some books and genres that you don't like")

# Bad Book Entries
l, r = st.columns(2)

with l:
    unliked_books = st.text_input("Enter some book(s) you don't like here")

with r:
    unliked_genres = st.text_input("Enter some genre(s) you don't like here")
# Submit

'''

---

'''
prompt = f"""
Make a list of 6 books that the user would probably like to read 
based on the books they like and the genres they like. 
Make sure to exclude books from the kinds of books they don't like 
and genres they don't like.
Do not recommend books in the same series as the ones the user likes.
Respond with JSON format
""" + """
{
    "Recommendations": [
        { 
            "name": "{book name}", 
            "author": "{name of author}", 
            "description": "{description of book}"
        },
        { 
            "name": "{book name}", 
            "author": "{name of author}", 
            "description": "{description of book}"
        }
    ]
}
""" + f"""
Books they like:
{liked_books}

Genres they like:
{liked_genres}

Books they Don't like:
{unliked_books}

Genres they Don't like:
{unliked_genres}
"""

prompt_image = """
Get the ISBN numbers for each of the books I will give you.
Return in this JSON format:
{
    "{name}" : {isbn}
}

"""

pressed = st.button("Get your book recommendations")
if pressed:
    api_call = client.chat.completions.create(
        model = "gpt-4o",
        response_format={"type": "json_object"},
        messages = [
            {"role": "system", "content": prompt},
        ]
    )

    st.session_state.recommendations = json.loads(api_call.choices[0].message.content)
    
    r_list = st.session_state.recommendations["Recommendations"]
    for i in range(len(r_list)):
        book_name = r_list[i]["name"]
        
        api_call = client.chat.completions.create(
            model = "gpt-4o",
            response_format={"type": "json_object"},
            messages = [
                {"role": "system", "content": prompt_image},
                {"role": "user", "content": book_name},
            ]
        )
        response = api_call.choices[0].message.content
        response = json.loads(response)
        isbn = response[book_name]
        r_list[i]["isbn"] = isbn

if "recommendations" in st.session_state:
    r_list = st.session_state.recommendations["Recommendations"]
    isbn_value = 1
    image_url = f"https://covers.openlibrary.org/b/isbn/{isbn_value}-s.jpg"
    
    for i in range(0, len(r_list), 3):
        cols = st.columns([0.1, 1, 1, 1])
        for j in range(3):
            if i + j < len(r_list):
                book = r_list[i + j]
                with cols[j + 1]:
                    st.subheader(book["name"])
                    st.image(f"https://covers.openlibrary.org/b/isbn/{book['isbn']}-M.jpg")

st.rerun()