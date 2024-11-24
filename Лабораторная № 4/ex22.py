import requests
from datetime import datetime

def fetch_page(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        else:
            print(f"Ошибка HTTP: {resp.status_code}")
            return None
    except Exception as error:
        print(f"Ошибка при выполнении запроса: {error}")
        return None

def retrieve_weather_info():
    weather_url = 'https://wttr.in/?format=%l:+%t'
    page_content = fetch_page(weather_url)

    if not page_content:
        return "Не удалось получить данные о погоде."

    details = page_content.strip().split(': ')
    city = details[0]
    current_temp = details[1]

    return f"{city}: текущая температура {current_temp}"

weather_info = retrieve_weather_info()
print(weather_info)
