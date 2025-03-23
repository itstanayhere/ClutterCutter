# Clutter Cutter 📰📊

## Overview
**Clutter Cutter** is an automated financial news summarizer designed exclusively for **The Economic Times'** website. It scrapes and condenses lengthy financial articles, providing traders and brokers with a concise **TL;DR** of important market news. The tool generates structured reports in PDF format for quick insights.

## Features 🚀
- **Automated Web Scraping**: Extracts the latest financial news from The Economic Times.
- **News Summarization**: Condenses lengthy articles into key takeaways.
- **PDF Report Generation**: Converts summaries into a structured report for easy reference.

## Installation & Setup ⚙️
1. Clone the repository:
   ```sh
   git clone https://github.com/itstanayhere/ClutterCutter.git
   cd ClutterCutter
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your environment:
   - Create a `.env` file (if required for configurations).
   - **Ensure `.env` is excluded** from Git using `.gitignore`.

## Usage 🏃‍♂️
Run the main script to start scraping and summarization:
```sh
python newssummariser.py
```
The generated report will be available as `report.pdf`.

## Contributions & Future Improvements 🚧
- Integration of infographic content straight from the stock market
- Additional information about the top five gainers and losers each day

## Disclaimer ⚠️
This tool is intended for **personal use** and is designed specifically for The Economic Times' website. Please review the website's terms of service before extensive usage.

## License 📜
MIT License. Feel free to use, modify, and contribute!

---
For any queries, reach out via GitHub Issues. Happy trading! 📈📉
