import requests

# 'https://api.open-meteo.com/v1/forecast'

def get_weather():
    try:
        name = input('Введіть місто: ')
        cord_list = get_cord(name)
        weather_parameters = {
            'latitude': cord_list[0],
            'longitude': cord_list[1],
            'current_weather': True,
            'hourly': ''
        }
        response = requests.get('https://api.open-meteo.com/v1/forecast', params=weather_parameters)
        data = response.json()
        print(f'''
Latitude: {data['latitude']}
Longitude: {data['longitude']}
Temperature: {data['current_weather']['temperature']}
        ''')
    except:
        print('Помилка, можливо неправильна назва міста.')

def get_cord(name):
    params = {
        'name': name
    }
    response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=params)
    data = response.json()
    for i, city in enumerate(data['results'], start=1):
        print(f"{i}. {city['name']}")

    while True:
        selected_num = int(input("Введіть номер міста, про яке потрібна інформація: "))
        if selected_num in range(1, len(data['results'])+1):
            selected_city = data['results'][selected_num-1]
            print(f"Обране місто: {selected_city['name']}")
            break
        else:
            print("Невірний номер міста!")

    cord_list = list()
    cord_list.append(selected_city['latitude'])
    cord_list.append(selected_city['longitude'])
    return cord_list


get_weather()