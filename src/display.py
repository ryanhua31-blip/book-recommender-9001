import streamlit as st

def display_recommendations():
    if "recommendations" in st.session_state:
        r_list = st.session_state.recommendations["Recommendations"]
        
        for i in range(0, len(r_list), 3):
            cols = st.columns([0.1, 1, 1, 1])
            for j in range(3):
                if i + j < len(r_list):
                    book = r_list[i + j]
                    with cols[j + 1]:
                        st.subheader(book["name"])
                        st.image(f"https://covers.openlibrary.org/b/isbn/{book['isbn']}-M.jpg")