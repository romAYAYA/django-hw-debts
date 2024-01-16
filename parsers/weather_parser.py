import requests
from bs4 import BeautifulSoup


def get_temp(city: str) -> str:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',
            'Referer': 'https://yandex.kz/',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        res = requests.get(f'https://pogoda.co.il/kazakhstan/{city}', headers=headers)
        res.raise_for_status()

        weather_soup = BeautifulSoup(res.text, 'html.parser')

        temp = weather_soup.find('strong').get_text(strip=True)

        return temp

    except requests.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return "Error fetching temperature"

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error fetching temperature"


