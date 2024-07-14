# Stramlit Network Analysis App

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./assets/css/styles.css">
</head>
<body>
<div class="difficulty-container">
<ul class="difficulty-list">
    <li class="level">Beginner</li>
    <li class="level selected"><strong>Intermediate</strong></li>
    <li class="level">Advanced</li>
</ul>
</div>
</body>

[![thumbnail](https://img.youtube.com/vi/s86jz9qVeWA/maxresdefault.jpg)](https://youtu.be/s86jz9qVeWA)

This is a YouTube video on a [Streamlit](https://streamlit.io/) component called [st-link-analysis](https://github.com/AlrasheedA/st-link-analysis?tab=readme-ov-file). It allows you to build good quality network analysis applications in Streamlit very easily.

# Installation

```bash
pip install streamlit st-link-analysis
```

# Quick Code

```python
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.icons import SUPPORTED_ICONS
import json

st.set_page_config(layout="wide")
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
```
