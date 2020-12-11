import requests


def get_weather(city: str):
    params = {
        "nTqm": "",
        "lang": "ru",
    }
    url = f"http://wttr.in/{city}"
    try:
        response = requests.get(url, params=params)
        return response.text
    except requests.exceptions.ConnectionError:
        return "Не могу подключиться к сервер!"


if __name__ == "__main__":
    cities = ["London", "Шереметьево", "Череповец"]
    for city in cities:
        print(get_weather(city))