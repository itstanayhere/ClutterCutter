import requests
from lxml import html
from getlinksthruetsite import run_scraper
from threading import Event

def scrape_article(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        tree = html.fromstring(response.content)
        
        article_text_div = tree.xpath('//div[contains(@class, "artText")]')
        
        if article_text_div:
            paragraphs = article_text_div[0].xpath('./p[not(ancestor::div[contains(@class, "slider")]) and not(ancestor::div[contains(@class, "widget")])]')
            
            article_paragraphs = []
            for p in paragraphs:
                text = ' '.join(p.xpath('.//text()')).strip()
                if len(text) > 50 and not any(widget_term in text.lower() for widget_term in [
                    'read more', 'click here', 'subscribe', 'advertisement', 
                    'recommended', 'sponsored', 'related articles'
                ]):
                    article_paragraphs.append(text)
            
            if article_paragraphs:
                return ' '.join(article_paragraphs)
            else:
                main_text = ' '.join(article_text_div[0].xpath(
                    './/text()[not(ancestor::div[contains(@class, "slider")]) and ' +
                    'not(ancestor::div[contains(@class, "widget")]) and ' +
                    'not(ancestor::script) and not(ancestor::style)]'
                )).strip()
                
                main_text = ' '.join(line.strip() for line in main_text.split('\n') if line.strip())
                return main_text if main_text else "No substantial article text found."
        
        return "Article element not found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def retinfo():
    print("Scraping articles...")
    articles_dict = {}
    urls = run_scraper()

    if isinstance(urls, list):
        for url in urls:
            articles_dict[url] = scrape_article(url)
    return articles_dict