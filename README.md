🏅 Olympic Data Analysis Web App


An interactive data analysis web application built using Streamlit to explore historical Olympic data. This app provides insights into medal tallies, country performance, athlete statistics, and long-term Olympic trends.

📌 Features


🥇 Medal Tally

- Analyze medal counts by:
    - Year
    - Country
    - Overall
- Displays Gold, Silver, Bronze, and Total medals


🌍 Overall Analysis

- Key statistics:
     - Editions
     - Host cities
     - Sports, events, athletes, nations
       
- Trends:
  
    - Participating nations over time
    - Events growth
    - Athlete participation
- Heatmap of events across sports and years
- Most successful athletes

  
🏳️ Country-wise Analysis

- Year-wise medal tally
- Sport-wise performance heatmap
- Top 10 athletes by country

  
🧑‍🤝‍🧑 Athlete-wise Analysis
- Age distribution (overall + medalists)
- Sport-wise age trends (gold medalists)
- Height vs Weight analysis
- Male vs Female participation trends

  
🗂️ Project Structure

Olympic-Data-Analysis/
│
├── app.py                # Main Streamlit app
├── helper.py             # Analysis functions
├── preprocessor.py       # Data preprocessing
├── athlete_events.zip    # Compressed dataset (auto-extracted)
├── noc_regions.csv       # NOC to region mapping
├── requirements.txt      # Dependencies
└── README.md


⚙️ Technologies Used

- Python 🐍
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

  
🔄 Data Handling (Important)

Due to GitHub file size limits, the main dataset is stored as:

athlete_events.zip


✅ How it works:

- The app automatically extracts the dataset at runtime
- No manual setup required

  
🔧 Code used in app.py:
Python


import zipfile
import os

if not os.path.exists("athlete_events.csv"):
    with zipfile.ZipFile("athlete_events.zip", 'r') as zip_ref:
        zip_ref.extractall()

        
📊 Role of noc_regions.csv
- Maps NOC codes → Country/Region names
- Merged during preprocessing
- Creates the region column used throughout the app

  
⚠️ Without this file:

- Country-wise analysis will fail
- Medal tally by country won’t work properly

  
🧠 Core Functionalities


Defined in helper.py:
- fetch_medal_tally() → Medal aggregation
- country_year_list() → Filters
- data_over_time() → Trend analysis
- most_successful() → Top athletes
- yearwise_medal_tally() → Country performance
- country_event_heatmap() → Sport dominance
- weight_v_height() → Physical analysis
- men_vs_women() → Gender trends

  
🚀 Run Locally


1. Install dependencies
Bash
pip install -r requirements.txt
2. Run app
Bash
streamlit run app.py
3. Open in browser

http://localhost:8501


🌐 Deployment


Using Streamlit Cloud:

- Push project to GitHub
- Go to Streamlit Cloud
- Click New App
- Select repo + app.py
- Deploy

  
⚠️ Important Notes


- Ensure these files are present:
  - athlete_events.zip
  - noc_regions.csv
- The app auto-extracts dataset on first run
- No need to manually unzip

  
💡 Future Improvements


- Add Winter Olympics analysis
- Improve UI/UX
- Add advanced filters
- Optimize performance with caching
- Add Predictions(ML)


 ✍ Author

👤 Kousik Chakraborty
📧 Email: www.kousik.c.in@gmail.com
🔗 GitHub Profile: https://github.com/iamkousikc-create18
🔗 Project Repository: https://github.com/iamkousikc-create18/olympic-data-analysis

👨‍💻 Author
Byomkesh
