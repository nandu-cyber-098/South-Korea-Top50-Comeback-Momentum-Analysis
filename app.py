import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="South Korea Top 50 Playlist Analysis",
    layout="wide"
)

st.title("🎵 South Korea Top 50 Playlist Analysis")
st.subheader("Comeback Momentum, Chart Re-Entry and Fandom Intensity Analysis")

uploaded_file = st.file_uploader(
    "Upload Atlantic South Korea Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.header("Dataset Preview")
    st.dataframe(df.head())

    st.header("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Records", len(df))
    col2.metric("Unique Songs", df["song"].nunique())
    col3.metric("Unique Artists", df["artist"].nunique())
    col4.metric("Average Popularity",
                round(df["popularity"].mean(), 2))

    st.header("Popularity Distribution")

    fig1 = px.histogram(
        df,
        x="popularity",
        nbins=20,
        title="Popularity Distribution"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.header("Top 10 Artists")

    top_artists = (
        df["artist"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_artists.columns = ["Artist", "Count"]

    fig2 = px.bar(
        top_artists,
        x="Artist",
        y="Count",
        title="Top Artists in Playlist"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.header("Album Type Distribution")

    album_counts = (
        df["album_type"]
        .value_counts()
        .reset_index()
    )

    album_counts.columns = ["Album Type", "Count"]

    fig3 = px.pie(
        album_counts,
        names="Album Type",
        values="Count",
        title="Album Type Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.header("Explicit vs Non-Explicit Songs")

    explicit_counts = (
        df["is_explicit"]
        .value_counts()
        .reset_index()
    )

    explicit_counts.columns = ["Explicit", "Count"]

    fig4 = px.bar(
        explicit_counts,
        x="Explicit",
        y="Count",
        title="Explicit vs Non-Explicit"
    )

    st.plotly_chart(fig4, use_container_width=True)

else:
    st.info("Upload the dataset CSV file to start analysis.")