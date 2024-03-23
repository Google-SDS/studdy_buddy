import streamlit as st
from langchain.llms import OpenAI

def app():
    st.title('Me and My AI :anchor:')

    openai_api_key = st.sidebar.text_input('OpenAI API Key')

    def generate_response(input_text):
        try:
            llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
            st.info(llm(input_text))
        except Exception as e:
            st.error(f"Error: {e}")

    # Add file upload functionality
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        generate_response(text)

    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')

        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')

        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)

# If you want to run the app directly
if __name__ == "__main__":
    app()
