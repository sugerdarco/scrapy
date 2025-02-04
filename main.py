from firecrawl import FirecrawlApp
from dotenv import load_dotenv
load_dotenv()
import os
from file_opretation import create_file

def scrape_url(url):
    app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API'))
    response = app.scrape_url(url=url, params={
        'formats': [ 'markdown' ],
    })
    if hasattr(response, 'error'):
        return {'status': False, 'error message': response.error}
    print(response)
    return response.markdown

response = scrape_url('https://firecrawl.dev')
create_file(response.markdown, response.title, 'md')
