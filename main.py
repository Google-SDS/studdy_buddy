import streamlit as st
import about_us
import help_page
import home

st.set_page_config(
    page_title="Me and My AI"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run(self):
        with st.sidebar:
            app = st.sidebar.selectbox(
                "Pages",
                options=['Home', 'Help', 'About']
            )

        if app == "Home":
            home.app()
        elif app == "About":
            about_us.app()    
        elif app == "Help":
            help_page.app()   

def main():
    app = MultiApp()
    app.run()

if __name__ == "__main__":
    main()
