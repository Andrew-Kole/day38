import streamlit as st
from datetime import datetime as dt
import extractorData as ed
from fileWriter import store_data
import graphCreator as gc

st.set_page_config(layout="wide")

st.title(ed.extract_label(ed.scrape()))
store_button = st.button("Store data")
graph_button =st.button("Draw graph")

if store_button:
    current_date = dt.now()
    date_str = current_date.strftime("%y-%m-%d-%H-%M-%S")
    temperature = ed.extract_temperature(ed.scrape())
    store_data(date_str, temperature)

if graph_button:
    figure = gc.build_graph()
    st.plotly_chart(figure)


