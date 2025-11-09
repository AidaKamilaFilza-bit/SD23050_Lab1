# ------------------------------------------------------------
# Lab Report BSD3513 – Artificial Intelligence
# Student Name: AIDA KAMILA FILZA BINTI ABDUL MANAF
# Student ID: SD23050
# Section: 01G
# ------------------------------------------------------------

import streamlit as st
from collections import deque
from PIL import Image

# ------------------------------------------------------------
# Streamlit App Header
# ------------------------------------------------------------
st.set_page_config(page_title="BFS & DFS Visualizer", layout="centered")
st.title("🔍 BFS and DFS Graph Traversal Visualizer")
st.markdown("### BSD3513 – Lab Report 1")
st.markdown("**Name:** `AIDA KAMILA FILZA BINTI ABDUL MANAF` | **Student ID:** `SD23050` | **Section:** `01G`")

# ------------------------------------------------------------
# Display single image at the top
# ------------------------------------------------------------
st.subheader("Graph Reference Image")
st.info("Below is the sample graph used for BFS and DFS traversal demonstrations.")
try:
    image = Image.open('LabReport_BSD2513_#1.jpg')  
    st.image(image, caption="Graph used for BFS and DFS Traversal", use_column_width=True)
except Exception:
    st.warning("⚠️ Image 'LabReport_BSD2513_#1.jpg' not found. Place it in the same directory as this file.")

# ------------------------------------------------------------
# Graph Definition
# ------------------------------------------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

st.subheader("1️ Graph Structure")
st.json(graph)

# ------------------------------------------------------------
# BFS Implementation
# ------------------------------------------------------------
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    order = []

    while queue:
        s = queue.popleft()
        if s not in visited:
            visited.append(s)
            order.append(s)
            for neighbour in graph[s]:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)
    return order


# ------------------------------------------------------------
# DFS Implementation
# ------------------------------------------------------------
def dfs(graph, start_node, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []
    if start_node not in visited:
        visited.add(start_node)
        order.append(start_node)
        for neighbour in graph[start_node]:
            dfs(graph, neighbour, visited, order)
    return order


# ------------------------------------------------------------
# Streamlit Interface for Running Algorithms
# ------------------------------------------------------------
st.subheader("2️ Choose Traversal Type")
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))
algorithm = st.radio("Choose Algorithm:", ["Breadth-First Search (BFS)", "Depth-First Search (DFS)"])

if st.button("Run Traversal"):
    if algorithm == "Breadth-First Search (BFS)":
        result = bfs(graph, start_node)
        st.success("Traversal Order (BFS): " + " → ".join(result))
    else:
        result = dfs(graph, start_node)
        st.success("Traversal Order (DFS): " + " → ".join(result))

    st.markdown("**Visited Nodes Order:**")
    st.code(", ".join(result))

# ------------------------------------------------------------
# Explanation Section
# ------------------------------------------------------------
st.markdown("---")
st.subheader("3️ Algorithm Explanation")

st.markdown("""
**Breadth-First Search (BFS)**  
- Explores all neighbors level by level before moving deeper.  
- Uses a **queue** (FIFO order).  
- Example: A → B → C → D → E → F  

**Depth-First Search (DFS)**  
- Explores as far as possible down one branch before backtracking.  
- Uses a **stack** (implicit recursion).  
- Example: A → B → D → E → F → C
""")

