from datetime import datetime
from hashlib import sha256

import requests
from bs4 import BeautifulSoup


def get_currency() -> list[dict[str, str]]:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',
            'Referer': 'https://yandex.kz/',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        res = requests.get('https://www.mig.kz/', headers=headers)
        res.raise_for_status()

        currency_soup = BeautifulSoup(res.text, 'html.parser')

        rows = currency_soup.find_all('tr')
        data_list = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 3:
                buy_value = cells[0].text.strip()
                currency = cells[1].text.strip()
                sell_value = cells[2].text.strip()

                unique_id = sha256(f"{buy_value}-{currency}-{sell_value}-{datetime.now()}".encode()).hexdigest()

                row_data = {
                    'buy_value': buy_value,
                    'currency': currency,
                    'sell_value': sell_value,
                    'id': unique_id
                }

                data_list.append(row_data)

        return data_list
    except requests.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return []
