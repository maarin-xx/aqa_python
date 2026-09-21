'''
Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль request зробить
через POST upload якогось зображення на сервер, за допомогою GET отримає посилання на цей файл и потiм
за допомогою DELETE зробить видалення файлу з сервера
'''

import requests

BASE_URL = 'http://127.0.0.1:8080'


with open('mars_photo1.jpg', 'rb') as file:
    response = requests.post(
        f'{BASE_URL}/upload',
        files={'image': file}
    )

print(response.status_code)
print(response.json())

image_url = response.json()['image_url']
filename = image_url.split('/')[-1]

#Отримання URL завантаженого зображення

response = requests.get(f'{BASE_URL}/image/{filename}',
    headers={'Content-Type': 'text'})

print(response.status_code)
print(response.json())


#за допомогою DELETE зробить видалення файлу з сервера
response = requests.delete(f'{BASE_URL}/delete/{filename}')
print(response.status_code)
print(response.json())
