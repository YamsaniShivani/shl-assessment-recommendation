import streamlit as st
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="SHL Assessment Recommender")

st.title("SHL Assessment Recommendation System")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_index():
    return faiss.read_index("faiss_index.index")

@st.cache_data
def load_data():
    return pd.read_csv("shl_catalog.csv")

model = load_model()
index = load_index()
df = load_data()

query = st.text_area("Enter Job Description or Query")

if st.button("Get Recommendations"):
    if query.strip() != "":
        query_embedding = model.encode([query])
        D, I = index.search(np.array(query_embedding), 10)

        results = df.iloc[I[0]][["name", "url"]]

        st.subheader("Top Recommended Assessments")
        for i, row in results.iterrows():
            st.markdown(f"**{row['name']}**")
            st.write(row['url'])
    else:
        st.warning("Please enter a query.")