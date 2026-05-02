import streamlit as st

def user_input():
    st.write("First, write down some stuff you like")

    c = st.columns(2)

    # Good Book Entries
    with c[0]:
        liked_books = st.text_input("Enter some book(s) you like here")

    # Genre Entry
    with c[1]:
        liked_genres = st.text_input("Enter some genre(s) you like here")

    st.markdown(
        '''

        ---

        '''
    )

    st.write("Now, write down some books and genres that you don't like")

    # Bad Book Entries
    l, r = st.columns(2)

    with l:
        unliked_books = st.text_input("Enter some book(s) you don't like here")

    with r:
        unliked_genres = st.text_input("Enter some genre(s) you don't like here")

    return liked_books, liked_genres, unliked_books, unliked_genres

