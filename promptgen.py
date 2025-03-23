
def prompt(url,text):
    s = f"Generate an appropriate response based on the provided text and instructions.It should be in markdown format with the title, summary and souce. Summarize the text from the perspective of a stock trader and economist, emphasizing key statistics, numerical data, and other relevant insights. Ensure a concise yet informative analysis. At the end, embed the given URL within a brief contextual statement. Use 30 dashes to mark the end of the summary before adding the URL. Text: {text}  URL: {url}"  
    return s
