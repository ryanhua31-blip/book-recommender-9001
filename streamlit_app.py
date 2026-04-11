import streamlit as st
from openai import OpenAI
import json

key = st.text_input("enter ur key here")

client = OpenAI(
    api_key=key
)

"""
# Book Recommender 9001 📖 📚
*"Indisputably, this is quite possibly the most sublime book recommender in existence."*
—Shakespeare

---

"""

st.write("First, write down some stuff you like",)





# Totally neccessary column size calculations
# if "c1t" not in st.session_state:
#     st.session_state.c1t = .5
# if "c1t_dir" not in st.session_state:
#     st.session_state.c1t_dir = 0.01

# st.session_state.c1t += st.session_state.c1t_dir
# if st.session_state.c1t > .99:
#     st.session_state.c1t_dir = -0.01
# if st.session_state.c1t < .01:
#     st.session_state.c1t_dir = 0.01

# s2 = (st.session_state.c1t * 3) % 1
# c = st.columns([st.session_state.c1t, 1.5, s2, 1.5, 1 - st.session_state.c1t + 1 - s2])

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
Make a list of books that the user would probably like to read 
based on the books they like and the genres they like. 
Make sure to exclude books from the kinds of books they don't like 
and genres they don't like.
Do not recommend books in the same series as the ones the user likes.
Respond with JSON format
""" + """
{
    "Recommedations": [
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

pressed = st.button("Get your book recommendations")
if pressed:
    api_call = client.responses.create(
        model = "gpt-4o",
        response_format={"type": "json_object"},
        messages = [
            {"role": "system", "content": prompt},
        ]
    )
    st.session_state.recommendations = json.loads(api_call.output[0].content[0].text)

if "recommendations" in st.session_state:
    # TODO HOMEWORK: Print out names individually 
    # HINT: you need to loop
    st.write(st.session_state.recommendations)

st.rerun()












