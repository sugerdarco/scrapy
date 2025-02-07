from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
from file_opretation import save_file
load_dotenv()

# srape web-page data using Firecrawl
def scrape_url(url):
    app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API'))
    scrape_data = app.scrape_url(url)
    if hasattr(scrape_data, 'markdown'):
        return scrape_data['markdown']
    else:
        return KeyError("The key 'markdown' does not present")





response = scrape_url('https://firecrawl.dev')
from ai_operations import format_data
ne = format_data(response, ["name", "id"])
save_file(ne, "test-file", "md")
