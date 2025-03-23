import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def run_scraper():
    url = "https://economictimes.indiatimes.com/markets"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links within newsList items
        results = []
        news_items = soup.select("ul.newsList li[itemprop='itemListElement'] a")
        
        for item in news_items:
            link = item.get('href', '')
            if link:
                # Make relative URLs absolute
                full_link = urljoin(url, link)
                results.append(full_link)
        
        return results if results else "No links found."
        
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return "No links found."
    except Exception as e:
        print(f"Error parsing the page: {e}")
        return "No links found."
