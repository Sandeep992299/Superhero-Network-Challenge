import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Load Data ---
superheroes_df = pd.read_csv("superheroes.csv")
links_df = pd.read_csv("links.csv")

# --- Build Graph ---
G = nx.Graph()

for _, row in superheroes_df.iterrows():
    G.add_node(row['id'], name=row['name'], created_at=row['created_at'])

for _, row in links_df.iterrows():
    G.add_edge(row['source'], row['target'])

# --- Basic Info ---
id_to_name = superheroes_df.set_index("id")["name"].to_dict()
degrees = dict(G.degree())

# --- Sidebar Filters ---
st.sidebar.header("Filters")

today = datetime(2025, 5, 28)
recent_days = st.sidebar.slider("Show heroes added in last N days:", 1, 10, 3)
recent_date = today - timedelta(days=recent_days)
recent_heroes = superheroes_df[pd.to_datetime(superheroes_df["created_at"]) >= recent_date]

# --- Main Display ---
st.title("🦸‍♂️ Superhero Universe Network")

st.markdown(f"**Total Superheroes:** {G.number_of_nodes()}")
st.markdown(f"**Total Connections:** {G.number_of_edges()}")

st.subheader("🆕 Superheroes Added Recently")
for _, row in recent_heroes.iterrows():
    st.markdown(f"- {row['name']} ({row['created_at']})")

st.subheader("🏆 Top 3 Most Connected Superheroes")
top_3 = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (hero_id, conn) in enumerate(top_3, 1):
    st.markdown(f"{i}. {id_to_name[hero_id]} ({conn} connections)")

st.subheader("🧑‍💻 dataiskole Info")
data_row = superheroes_df[superheroes_df["name"] == "dataiskole"]
if not data_row.empty:
    did = data_row.iloc[0]["id"]
    created = data_row.iloc[0]["created_at"]
    friends = [id_to_name[n] for n in G.neighbors(did)]
    st.markdown(f"- **Added on:** {created}")
    st.markdown(f"- **Friends:** {', '.join(friends) if friends else 'No friends found'}")
else:
    st.markdown("dataiskole not found.")

# --- Visualization ---
st.subheader("📊 Superhero Network Graph")

pos = nx.spring_layout(G, seed=42)
colors = []

for node in G.nodes():
    if node == did:
        colors.append("gold")
    elif node in [h[0] for h in top_3]:
        colors.append("skyblue")
    elif node in recent_heroes["id"].values:
        colors.append("lightgreen")
    else:
        colors.append("lightgray")

fig, ax = plt.subplots(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, labels=id_to_name,
        node_color=colors, node_size=1000,
        font_size=9, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)
