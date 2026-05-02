import streamlit as st
import json

def get_ai_recommendations(client, prompt, prompt_image):
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