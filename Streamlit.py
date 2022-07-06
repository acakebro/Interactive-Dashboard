# importing dependencies
import pandas as pd
import plotly.express as px
import streamlit as st  # for webapp

# helpful links for error handling:
# https://discuss.streamlit.io/t/command-not-found/741/3
# https://medium.com/geekculture/how-to-run-your-streamlit-apps-in-vscode-3417da669fc


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Latest Internships on InternSG",
    page_icon=":open_file_folder:",
    layout="wide",
)


@st.cache
# caching the dataframe
def get_data_from_csv():

    df = pd.read_csv("latest_interns.csv")
    return df


df = get_data_from_csv()
# st.dataframe(df)  # print dataframe on the page instead of console

# ----SIDEBAR------
st.sidebar.header("Please Filter Here:")
types = st.sidebar.multiselect(
    "Select type of work:",
    options=df["Type"].unique(),
    default=df["Type"].unique(),
)
positions = st.sidebar.multiselect(
    "Select your postion:",
    options=df["Position"].unique(),
    default=df["Position"].unique(),
)

df_selection = df.query("Position == @positions & Type == @types")


# ----- MAINPAGE ------
st.title(":open_file_folder: Latest Internships")
st.markdown("##")


# Analytics
total_openings = int(len(df_selection["Type"]))
num_companies = int(len(df_selection["Company"].unique()))

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Openings:")
    st.subheader(f"{total_openings}")

with right_column:
    st.subheader("Number of Companies:")
    st.subheader(f"{num_companies}")

st.markdown("---")
st.dataframe(df_selection)  # print the dataframe on the dashboard
st.markdown("---")
# Barchart for the different roles (Horizontal) for ease of viewing
position_count = pd.DataFrame(df_selection["Position"].value_counts())
position_count.index.name = "Position"
position_count.rename(columns={"Position": "Count"}, inplace=True)
position_count = position_count.sort_values(by="Count", ascending=True)

fig_position_count = px.bar(
    position_count,
    x="Count",
    y=position_count.index,
    orientation="h",
    title=" <b> Barchart of positions available </b> ",
    color_discrete_sequence=len(position_count) * ["#FFFFFF"],
)

fig_position_count.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",  # transparent bg
    barmode="stack",
    xaxis=({"categoryorder": "total ascending", "showgrid": False}),
    autosize=True,
    width=1000,
    height=1500,
)


st.plotly_chart(fig_position_count)

# ----- HIDE STREAMLIT STYLE --------------------------------
hide_st_style = """ 
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


# use git add .
# git commit -m "<Text>" # to track commits
# git push heroku master
# heroku ps:scale web=1

