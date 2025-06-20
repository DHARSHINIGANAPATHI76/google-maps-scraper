import streamlit as st
import pandas as pd

st.title("📍 Google Maps Business Data Viewer")

# Load existing CSV file (scraped locally)
try:
    df = pd.read_csv("maps_results.csv")
    st.success("✅ Data loaded successfully!")
    st.dataframe(df)

    st.write("Total results:", len(df))

    # Optional: Filter by keyword or location
    search = st.text_input("Search by keyword or location:")
    if search:
        filtered = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
        st.dataframe(filtered)
        st.write("Filtered results:", len(filtered))

except FileNotFoundError:
    st.error("⚠️ No data file found. Please run the scraper locally and upload 'maps_results.csv'.")

