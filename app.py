import streamlit as st
import pandas as pd
import time
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def scrape_google_maps(search_term):
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options)
    
    url = f"https://www.google.com/maps/search/{search_term.replace(' ', '+')}/"
    driver.get(url)

    time.sleep(8)

    try:
        scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
        for _ in range(6):
            driver.execute_script("arguments[0].scrollTop += arguments[0].offsetHeight;", scrollable_div)
            time.sleep(2)
    except Exception as e:
        st.warning(f"Could not scroll: {e}")

    names, addresses, ratings = [], [], []

    cards = driver.find_elements(By.CLASS_NAME, "Nv2PK")

    for card in cards:
        try:
            name = card.find_element(By.XPATH, './/div[contains(@class, "qBF1Pd")]').text
        except:
            name = ""
        try:
            address = card.find_element(By.XPATH, './/div[contains(@class, "UsdlK")]').text
        except:
            address = ""
        try:
            rating = card.find_element(By.XPATH, './/span[contains(@aria-label, "stars")]').get_attribute("aria-label")
        except:
            rating = ""
        if name:
            names.append(name)
            addresses.append(address)
            ratings.append(rating)

    driver.quit()

    df = pd.DataFrame({
        "Name": names,
        "Address": addresses,
        "Rating": ratings
    })
    return df

# ----- Streamlit UI -----

st.set_page_config(page_title="Google Maps Scraper", layout="centered")

st.title("📍 Google Maps Scraper")
st.markdown("Scrape place names, addresses, and ratings from Google Maps")

search_input = st.text_input("🔍 Enter what you want to search (e.g. 'Restaurants in Chennai')")

if st.button("Start Scraping"):
    if search_input:
        with st.spinner("Scraping Google Maps... please wait ⌛"):
            df = scrape_google_maps(search_input)
            if not df.empty:
                st.success(f"✅ Scraping completed. Found {len(df)} places.")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Download CSV", data=csv, file_name="maps_results.csv", mime="text/csv")
            else:
                st.warning("No data found. Try a different search.")
    else:
        st.error("Please enter a search query first.")
