# 📍 Google Maps Business Scraper (Streamlit Web App)

A fully functional **Python web app** that scrapes business listings from **Google Maps** and displays them through a clean, interactive **Streamlit interface**.

Designed for real-world use cases like market research, lead generation, and location-based analysis — this project showcases my ability to combine **automation**, **web scraping**, and **modern UI development**.

🚀 Key Highlights

- ✅ User-friendly **web interface** (built with Streamlit)
- ✅ Live **search from Google Maps** (e.g., "Hospitals in Chennai")
- ✅ Automatically scrapes:
  - Business **name**
  - **Address**
  - **Ratings**
- ✅ Download results as clean CSV report
- ✅ Built with **undetected-chromedriver** to avoid blocks by Google

🎯 Real-World Use Cases

- 🏢 **Sales & Marketing**: Generate leads from Google Maps
- 🧪 **Market Research**: Understand business density by category
- 📍 **Location Intelligence**: Study services in a specific area
- 🧑‍💻 **Automation**: No need to manually copy/paste results

🧰 Tech Stack

| Technology           | Purpose                         |
|----------------------|---------------------------------|
| **Python**           | Core programming language       |
| **Selenium + u.c.d** | Web scraping (headless)         |
| **Pandas**           | Data structuring/export         |
| **Streamlit**        | Frontend web interface          |

🖥️ Run This App Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/google-maps-scraper.git
cd google-maps-scraper

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install all requirements
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

📁 Output

After submitting a query (like “Pharmacies in Bengaluru”), the app:
1.Extracts listings directly from Google Maps
2.Displays them in an interactive table
3.Allows one-click CSV download
4.The CSV includes:
5.Business Name
6.Address

🌐 Live Demo
You can try the live version here:
🔗 https://yourusername.streamlit.app
(replace with your actual deployed URL)

🎓 What This Project Demonstrates

✅ Understanding of real-world data scraping challenges
✅ Knowledge of browser automation
✅ Skill in building user interfaces with Streamlit
✅ Ability to package and deploy professional-grade tools

🏁 Future Enhancements

📞 Scrape phone numbers and websites (if available)
🗺️ Visualize results on an interactive map (with Folium/Leaflet)
📤 Export to Excel with formatting
🔐 Secure form for authenticated scraping

📄 License
This project is licensed under the MIT License.

🙋‍♀️ About Me
Dharshini G
Aspiring Data Engineer / Python Developer
📍 India
🌐 dharshiniganapathi76@gmail.com

“This project reflects my interest in combining automation with user-friendly design — tools should be smart and simple.”
