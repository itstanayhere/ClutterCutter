import markdown
import os
from datetime import datetime
from xhtml2pdf import pisa

# Hardcoded input and output paths
input_path = 'PATH_TO_report.md'
output_path = 'C:/AutoReport/report.pdf'

def markdown_to_html(markdown_content):
    """Convert markdown content to HTML with proper styling."""
    # Convert markdown to HTML
    html = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code', 'codehilite'])
    
    # Add CSS for better formatting
    html_with_css = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{
                size: letter;
                margin: 2cm;
            }}
            body {{
                font-family: "Arial", sans-serif;
                line-height: 1.6;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #222;
                line-height: 1.2;
                margin-top: 1.2em;
                margin-bottom: 0.6em;
            }}
            h1 {{ font-size: 24pt; page-break-before: always; }}
            h2 {{ font-size: 18pt; }}
            h3 {{ font-size: 14pt; }}
            p {{ margin: 1em 0; }}
            code {{
                font-family: monospace;
                background-color: #f5f5f5;
                padding: 2px 4px;
                border-radius: 3px;
            }}
            pre {{
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                white-space: pre-wrap;
                page-break-inside: avoid;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            blockquote {{
                border-left: 4px solid #ddd;
                padding-left: 1em;
                color: #666;
                margin: 1em 0;
            }}
            a {{
                color: #1a73e8;
                text-decoration: none;
            }}
            img {{
                max-width: 100%;
                page-break-inside: avoid;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
                page-break-inside: avoid;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            hr {{
                border: none;
                border-top: 1px solid #eee;
                margin: 2em 0;
            }}
            .footer {{
                margin-top: 2em;
                border-top: 1px solid #eee;
                padding-top: 1em;
                font-size: 9pt;
                color: #777;
                text-align: center;
            }}
            ul, ol {{
                margin: 1em 0;
                padding-left: 2em;
            }}
            li {{
                margin: 0.5em 0;
            }}
        </style>
    </head>
    <body>
        {html}
        <div class="footer">
            Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </div>
    </body>
    </html>
    """
    return html_with_css

def convert_html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF and save to output_path."""
    with open(output_path, "wb") as output_file:
        pisa_status = pisa.CreatePDF(html_content, dest=output_file)
    return pisa_status.err == 0

def convert_markdown_to_pdf():
    """Convert markdown file to PDF."""
    try:
        # Read markdown content from file
        with open(input_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Convert markdown to HTML
        html_content = markdown_to_html(markdown_content)
        
        # Convert HTML to PDF
        success = convert_html_to_pdf(html_content, output_path)
        
        if success:
            print(f"Successfully converted {input_path} to {output_path}")
            return True
        else:
            print(f"Failed to convert {input_path} to PDF")
            return False
            
    except Exception as e:
        print(f"Error converting {input_path} to PDF: {e}")
        return False

if __name__ == "__main__":
    convert_markdown_to_pdf()
