import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# 0. Ask user what to search
search_term = input("🔍 What do you want to search on Google Maps? (e.g. Restaurants in Chennai): ")
url = f"https://www.google.com/maps/search/{search_term.replace(' ', '+')}/"

# 1. Setup Chrome browser
options = uc.ChromeOptions()
options.add_argument("--start-maximized")

print("🚀 Launching browser...")
driver = uc.Chrome(options=options)
driver.get(url)

# 2. Wait for the page to fully load
print("⏳ Waiting for page to load...")
time.sleep(8)

# 3. Scroll to load more results
print("📜 Scrolling to load more results...")
try:
    scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
    for i in range(6):  # Scroll more times
        driver.execute_script("arguments[0].scrollTop += arguments[0].offsetHeight;", scrollable_div)
        print(f"🔄 Scrolled {i + 1} times")
        time.sleep(3)
except Exception as e:
    print("❌ Scroll div not found:", e)

# 4. Extract data from result cards
print("🔍 Extracting data...")
names = []
addresses = []
ratings = []

cards = driver.find_elements(By.CLASS_NAME, "Nv2PK")

print(f"🧾 Found {len(cards)} results")

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

    # Only add if name is found
    if name:
        names.append(name)
        addresses.append(address)
        ratings.append(rating)

driver.quit()

# 5. Save the data to CSV
df = pd.DataFrame({
    "Name": names,
    "Address": addresses,
    "Rating": ratings
})

filename = f"{search_term.replace(' ', '_')}_results.csv"
df.to_csv(filename, index=False)
print(f"✅ Scraping completed. {len(df)} rows saved to {filename}")


