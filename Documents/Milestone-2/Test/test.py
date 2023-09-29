import requests
from bs4 import BeautifulSoup

url = "https://plankton-app-5fssv.ondigitalocean.app"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the title tag
        title_tag = soup.find('title')
        
        if title_tag:
            # Extract the title text
            title = title_tag.get_text()
            print(f"The title is set: {title}")
        else:
            print("No title tag found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
