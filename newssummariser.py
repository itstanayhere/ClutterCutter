import getinfofromlinks
import promptgen
from openai import OpenAI
from datetime import datetime
from typing import Dict, Optional
import re
import os
from dotenv import load_dotenv
import mdtopdf

load_dotenv()
api=os.getenv("GITHUB_TOKEN")

def initialize_openai():
    return OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=api
    )

def summarize_article(client, url: str, text: str) -> str:
    print(f"Processing: {url}")
    try:
        prompt = promptgen.prompt(url, text)
        
        response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None

def extract_title_from_url(url: str) -> str:
    """Extract a readable title from the URL."""
    try:
        path = re.sub(r'https?://[^/]+/', '', url)
        title = re.sub(r'\.[^.]+$', '', path)
        title = re.sub(r'[-_/]', ' ', title)
        return ' '.join(word.capitalize() for word in title.split())
    except Exception:
        return "Article Title"

def save_to_markdown(summaries: Dict[str, str], filename: Optional[str] = None) -> None:
    """Save summaries to a markdown file."""
    if not filename:
        filename = f"article_summaries_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    md_content = [
        "# News Report",
        f"Generated on {current_date}",
        "---\n"
    ]
    for summary in summaries.values():
        md_content.append(f"{summary}\n")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_content))
        print(f"Summaries saved to {filename}")
    except Exception as e:
        print(f"Error saving markdown file: {str(e)}")

def process_articles(client, articles_dict):
    summaries = {}
    for url, text in articles_dict.items():
        summary = summarize_article(client, url, text)
        if summary:
            summaries[url] = summary
    return summaries

def main():
    # Initialize the AI client
    client = initialize_openai()
    
    # Get articles dictionary from your existing function
    try:
        articles_dict = getinfofromlinks.retinfo()
    except Exception as e:
        print(f"Error getting articles: {str(e)}")
        return
    
    # Process each article
    summaries = process_articles(client, articles_dict)
    if summaries:
        save_to_markdown(summaries, filename="report.md")
    else:
        print("No summaries were generated successfully")
    mdtopdf.convert_markdown_to_pdf()

if __name__ == "__main__":
    main()
