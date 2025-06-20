import streamlit as st
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

st.set_page_config(page_title="Live Google Maps Scraper", layout="wide")
st.title("📍 Live Google Maps Scraper")
st.markdown("Enter a search like `salon in Chennai`, then click **Scrape Now**")

query = st.text_input("🔍 Search query", placeholder="e.g., salon in Coimbatore")
start_btn = st.button("🚀 Scrape Now")

if start_btn and query:
    st.info("🚀 Launching Chrome... Please wait...")

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    driver = uc.Chrome(options=options)

    url = f"https://www.google.com/maps/search/{query}"
    driver.get(url)
    time.sleep(5)

    st.info("📜 Scrolling...")
    for _ in range(10):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

    st.info("🔍 Extracting results...")
    cards = driver.find_elements(By.CLASS_NAME, 'Nv2PK')

    data = []
    for card in cards:
        try:
            name = card.find_element(By.CLASS_NAME, 'qBF1Pd').text
            address = card.find_element(By.CLASS_NAME, 'rllt__details').text
            data.append({"Name": name, "Details": address})
        except:
            continue

    driver.quit()

    if data:
        df = pd.DataFrame(data)
        df.to_csv("maps_results.csv", index=False)
        st.success(f"✅ Scraped {len(df)} results.")
        st.dataframe(df)
        st.download_button("⬇ Download CSV", data=df.to_csv(index=False), file_name="maps_results.csv", mime='text/csv')
    else:
        st.warning("No results found or structure changed.")
