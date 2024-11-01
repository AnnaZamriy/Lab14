import requests
from bs4 import BeautifulSoup
import re
import json

def get_emails(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text)
        return emails
    except requests.RequestException as e:
        print("Помилка при обробці:")
        return False

def email(emails):
    email_count = {}
    for email in emails:
        domain = email.split('@')[1]
        if domain in email_count:
            email_count[domain] += 1
        else:
            email_count[domain] = 1
    return email_count

def main():
    urls = ["https://epicentrk.ua/",
            "https://www.youtube.com/watch?v=SJ45s29n7Cw&list=LL&index=1&ab_channel=M.I.A.-Topic",
            "https://uaserial.tv/movie-zodiac",
            "https://mia1.knute.edu.ua/",
            "https://github.com/AnnaZamriy"
    ]

    all_email_counts = {}
    
    for url in urls:
        emails = get_emails(url)
        email_counts = email(emails)
        all_email_counts[url] = email_counts
    
    with open("email_counts.json", "w") as file:
        json.dump(all_email_counts, file, indent=3)

if __name__ == "__main__":
    main()
