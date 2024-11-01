import requests
from bs4 import BeautifulSoup
import json

def link(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        return len(links)
    except requests.RequestException as e:
        print("Server error")
        return False

def main():
    urls = []
    N = int(input("Кількість URL-адрес:"))

    for i in range(N):
        url = input("Введіть URL-адресу:")
        urls.append(url)

    links_counts = {}
    
    for url in urls:
        count = link(url)
        links_counts[url] = count
    
    with open("link_counts.json", "w") as file:
        json.dump(links_counts, file, indent=3)

if __name__ == "__main__":
    main()
