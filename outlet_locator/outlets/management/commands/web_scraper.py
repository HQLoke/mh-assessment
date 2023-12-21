from sqlite3 import IntegrityError
from bs4 import BeautifulSoup
import requests
from outlets.models import Outlet
from django.db import IntegrityError

URL = 'https://zuscoffee.com/category/store/'
ALL_STATES = ('perlis', 'kedah', 'penang', 'kelantan', 'perak', 'terrengganu', 'pahang', 
              'kuala-lumpur-selangor', 'negeri-sembilan', 'melaka', 'johor', 'sabah', 'sarawak')

def scrape_website_data(states):
    if (len(states) == 0):
        states = ALL_STATES
    for state in states:
        for i in range(1, 20):
            complete_url = ""
            if (i == 1):
                complete_url = URL + state
            else:
                complete_url = URL + state + '/page/' + str(i)
            
            head = requests.head(complete_url)
            if (head.status_code == 404):
                break
            
            print(f"Scraping {complete_url}...")
            response = requests.get(complete_url)
            soup = BeautifulSoup(response.text, 'html.parser')
          
            names = soup.find_all('h1', class_='elementor-heading-title')
            outer_divs = soup.find_all('div', 'elementor-widget-theme-post-content')
        
            for name, outer_div in zip(names, outer_divs):
                try:
                    new_data = Outlet(name=name.text, address=outer_div.find('p').text, state=state)
                    new_data.save()
                except IntegrityError as e:
                    pass
                    
    print("Scraping process completed.")