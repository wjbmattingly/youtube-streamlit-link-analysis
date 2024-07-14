import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.icons import SUPPORTED_ICONS
import json

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .center-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 36px;
        color: #00ff7f;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
        background: linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,255,127,0.1) 50%, rgba(0,0,0,0) 100%);
        border-radius: 10px;
        padding: 10px 0;
        margin: 20px 0;
        letter-spacing: 2px;
    }

    .center-title::after {
        content: "";
        display: block;
        margin: 0 auto;
        width: 60%;
        padding-top: 20px;
        border-bottom: 2px solid #00ff7f;
    }
    </style>
    <h1 class="center-title">Network Analysis App</h1>
    """, 
    unsafe_allow_html=True
)


# st.write(", ".join(SUPPORTED_ICONS))

# Load the data
with open("./data/network.json", "r") as f:
    elements = json.load(f)

node_styles = [
    NodeStyle("COMPANY", "#309A60", "label", "person"),
    NodeStyle("PERSON", "#2A629B", "name", "cloud"),
]

edge_styles = [
    EdgeStyle("FOUNDER", labeled=False, directed=False),
    EdgeStyle("CEO", labeled=True, directed=True),
    EdgeStyle("EMPLOYEE", labeled=False, directed=False),
]

layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}

st_link_analysis(
    elements, node_styles=node_styles, edge_styles=edge_styles, layout=layout, key="xyz"
)