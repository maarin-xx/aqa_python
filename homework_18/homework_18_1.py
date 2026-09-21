"""
Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі.
З JSON відповіді витягнути nasa_id для знайдених елементів.
Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів.
Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
Скачати 2 зображення і зберегти локально як:
mars_photo1.jpg
mars_photo2.jpg
Важливо: потрібно виконати мінімум 3 HTTP-запити:
1 запит /search + 2 запити /asset/{nasa_id} (і ще 2 запити на скачування jpg-файлів).
"""

import requests

BASE_URL = 'https://images-api.nasa.gov'
search_url = f"{BASE_URL}/search"
params = {'q': 'Curiosity rover Mars', 'media_type': 'image', 'page_size': 20}


links = []


response = requests.get(search_url, params=params)

if response.status_code == 200:
    json_data = response.json()
    items = json_data['collection']['items']

    print('list of nasa ids:')

    for item in items:
        nasa_id = item['data'][0]['nasa_id']
        print(nasa_id)

        asset_url = f"{BASE_URL}/asset/{nasa_id}"
        response = requests.get(asset_url)
        #print(response.json())
        for asset in response.json()['collection']['items']:
            if asset['href'].endswith('.jpg'):
                #print(asset['href'])
                links.append(asset['href'])
                break

        if len(links) == 2:
           break
    print(links)


    for i, link in enumerate(links, start=1):
        response = requests.get(link)

        with open(f'mars_photo{i}.jpg', 'wb') as file:
            file.write(response.content)

else:
    print('status code:', response.status_code)


