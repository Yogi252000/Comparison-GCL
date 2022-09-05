import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu


st.set_page_config(page_title='GCL Tapi',layout="wide",page_icon='🚢')
st.header("FLUYT VESSEL")
hide_st_style = """
         <style>
         footer {visibility : hidden;}
         </style>
         """

st.markdown(hide_st_style,unsafe_allow_html=True)
st.subheader("GCL VESSELS VOYAGE COMPARISON")

selected = option_menu(
    menu_title = None,
    options=["Last-Laden Voyage","Last-Ballast Voyage"],

    icons=["ship","ship","ship"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding":"0!important","background-color":"#ADD8E6"},
        "icon":{"color":"orange","font-size":"15px","font-style":"Arial"},
        "nav-link": {
            "font-size":"12px",
            "text-align":"justify",
            "margin": "0px",
            "--hover-color":"eee",

        },
        "nav-link-selected":{"background-color":"#00008B"},
    },
)


if selected == "Last-Laden Voyage":
    df1 = pd.read_csv("data1.csv")
    df2 = pd.read_csv('data2.csv')
    df3 = pd.read_csv('data3.csv')
    df4 = pd.read_csv('data4.csv')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df1['Vessel'], y=df1['CP instructed Speed'], name="CP instructed Speed"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df2['Vessel'], y=df2['Avg Speed'], name="Avg Speed"),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(x=df3['Vessel'], y=df3['Avg Speed (GW days)'], name="Avg Speed (GW days)"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=df4['Vessel'], y=df4['FO Consumption'], name="FO Consumption"),
        secondary_y=True,
    )


    fig.update_layout(
        title_text="LADEN CONDITION ",
        autosize=False,
        width=1000,
        height=600,

    )

    fig.update_xaxes(title_text="Vessel Name")

    fig.update_yaxes(
        title_text="Avg Speed (Voyage),Avg Speed (in Good weather),Avg FO cons/day,CP Fuel cons limit,Instructed Speed",)
    fig.update_yaxes(range=[5,50])
    fig.update_yaxes(visible=True,showticklabels=True,title_font=dict(size=12))
    st.plotly_chart(fig, use_container_width=True)
    st.write('Laden')
    first = pd.read_csv("Voyage.csv")
    st.write(first)



if selected == "Last-Ballast Voyage":
    df5 = pd.read_csv("data5.csv")
    df6 = pd.read_csv('data6.csv')
    df7 = pd.read_csv('data7.csv')
    df8 = pd.read_csv('data8.csv')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df5['vessel'], y=df5['CP instructed Speed'], name="CP instructed Speed"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df6['vessel'], y=df6['Avg Speed'], name="Avg Speed"),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(x=df7['vessel'], y=df7['Avg Speed (GW days)'], name="Avg Speed (GW days)"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=df8['vessel'], y=df8['FO Consumption'], name="FO Consumption"),
        secondary_y=True,
    )


    fig.update_layout(
        title_text="BALLAST CONDITION ",
        autosize=False,
        width=1000,
        height=600,

    )

    fig.update_xaxes(title_text="Vessel Name")

    fig.update_yaxes(
        title_text="Avg Speed (Voyage),Avg Speed (in Good weather),Avg FO cons/day,CP Fuel cons limit,Instructed Speed",)
    fig.update_yaxes(range=[5,50])
    fig.update_yaxes(visible=True,showticklabels=True,title_font=dict(size=12))
    st.plotly_chart(fig, use_container_width=True)
    st.write('Ballast')
    first = pd.read_csv("voyage2.csv")
    st.write(first)








