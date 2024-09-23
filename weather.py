import requests


def get_weather(city_name):

    base_url = "https://api.hypotheticalweather.com/weather"
    params = {"q": city_name}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
