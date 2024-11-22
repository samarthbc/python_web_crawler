import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def web_crawler(base_url):
    try:
        # Send a request to the website
        response = requests.get(base_url)
        response.raise_for_status()  # Raise error if request fails
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all <a> tags
        links = soup.find_all('a')
        
        # Set to store unique URLs
        url_set = set()
        
        for link in links:
            href = link.get('href')  # Get href attribute of the <a> tag
            if href:
                # Construct a full URL for relative paths
                full_url = urljoin(base_url, href)
                if full_url.startswith('http'):  # Include only valid URLs
                    url_set.add(full_url)
        
        # Display the URLs
        print(f"URLs found on {base_url}:")
        for url in sorted(url_set):
            if "articles" in url:
                print(url)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {base_url}: {e}")

if __name__ == "__main__":
    L = ["https://www.nature.com", "https://www.sciencedirect.com", "https://www.plos.org"]
    for i in L:
        web_crawler(i)
