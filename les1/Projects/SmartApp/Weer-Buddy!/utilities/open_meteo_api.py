import requests

def weer_utrecht():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current_weather=true"

        response = requests.get(url)
        data = response.json()
        return data['current_weather']

    except:
        print("Er ging iets mis in het proces, ons excuus!")
        return None
