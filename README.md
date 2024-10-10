# Frapapa Betting Scraper

The **Frapapa Betting Scraper** automates the process of extracting betting data from the Frapapa platform. This script collects information on upcoming football matches, including odds for the home team, away team, and draw, then outputs the data into a CSV file for analysis.

## 📌 Features

- **Automated Scraping**: Extracts live betting data from Frapapa's upcoming football matches.
- **Efficient Page Interaction**: Automatically navigates to the Frapapa site and clicks on the "Upcoming" section to load matches.
- **Data Output**: Saves all relevant data, such as team names, odds, and match time, into a CSV file.
- **Duplicate Removal**: Ensures no duplicate match entries exist in the output file.

## 🚀 How It Works

1. **Initialization**: The script uses Selenium to initialize a browser and navigates to Frapapa's website.
2. **Web Page Interaction**: It waits for the "Upcoming" button to become clickable and clicks it to view upcoming matches.
3. **Data Extraction**: The script extracts match information such as time, home team, away team, and odds.
4. **CSV Output**: The extracted data is saved in a CSV file located at the specified path.

### Key Components:

- **Web Scraping**: Uses Selenium for interacting with the website and BeautifulSoup for parsing HTML content.
- **Data Structuring**: Organizes the scraped data into a dictionary format for easier saving.
- **CSV File Management**: Manages the creation, updating, and deduplication of CSV files.

## 🛠️ Requirements

Before running the script, ensure the following dependencies are installed:

- **Python 3.x**
- **Selenium**
- **BeautifulSoup**
- **Pandas**

Install the required libraries via pip:
```bash
pip install selenium beautifulsoup4 pandas
```

## 🏃 How to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ezee-Kits/Frapapa-Betting-Scraper.git
   ```

2. **Set up ChromeDriver**:  
   Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your version of Chrome. Ensure it is available in your system path.

3. **Run the Python Script**:
   ```bash
   python frapapa_scraper.py
   ```

4. **View Results**:  
   The scraped data will be saved in a CSV file located in the `saving_path_csv` directory.

## 📁 Output

The output CSV file will include the following columns:
- **TIME**: The time of the match.
- **HOME TEAM**: The name of the home team.
- **AWAY TEAM**: The name of the away team.
- **HOME ODD**: Odds for the home team to win.
- **DRAW ODD**: Odds for a draw.
- **AWAY ODD**: Odds for the away team to win.
- **BOOKMAKER**: The bookmaker (in this case, Frapapa).

## 🔧 Future Enhancements

- **Improved Error Handling**: Implement better error handling to manage unexpected changes in the website layout.
- **Data Analysis Integration**: Add features for analyzing betting trends based on the scraped data.
- **Multi-Sport Support**: Expand the scraper to handle other sports offered on Frapapa.
- **User Interface**: Develop a simple user interface (UI) for easier interaction.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests.
