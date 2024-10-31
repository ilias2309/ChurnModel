import streamlit as st

# ------------------pages-----------------------
about_page = st.Page(
    "views/about.py",
    title="About Churn",
    icon="ℹ️",
    default=True,
)
project_1_page = st.Page(
    "views/prediction.py",
    title="Predictions",
    icon="🔮",
)
project_2_page = st.Page(
    "views/Eda.py",
    title="EDA",
    icon="📊",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

st.logo("assets/Bank.png")

st.sidebar.markdown("Made By [StAlpha](https://github.com/STALPHA2708)")

pg.run()
