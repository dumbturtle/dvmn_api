import requests


def get_weather(city: str):
    params = {
        "nTqm": "",
        "lang": "ru",
    }
    url = f"http://wttr.in/{city}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    cities = ["London", "Шереметьево", "Череповец"]
    for city in cities:
        try:
            print(get_weather(city))
        except requests.exceptions.ConnectionError:
            print("Сервер не доступен!")
        except requests.exceptions.HTTPError:
            print("Ошибка в работе сервера!")
