import streamlit as st

def main():
    run_app_command = 'streamlit run app.py'
    language = st.sidebar.selectbox(
        "Мова / Language / Idioma",
        [ "English", "Українська", 'Español'],
        key="language"
    )
    

    # Define titles based on current language
    if language == "Українська":
        eda_title = "Дослідницький аналіз"
    elif language == 'Español':
        eda_title = "Análisis exploratorio"
    else:
        eda_title = "EDA"

    eda_page = st.Page("pages/eda.py", title=eda_title)
    
    pg = st.navigation([eda_page])
    pg.run()

if __name__ == '__main__':
    main()