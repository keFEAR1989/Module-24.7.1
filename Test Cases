1. Тестирование метода POST​/api​/create_pet_simple:

import requests

url = 'https://petstore.swagger.io/api/create_pet_simple'
headers = {'auth_key': 'my_api_key'}
data = {'name': 'Fluffy', 'animal_type': 'cat', 'age': 3}

# Тест на успешное добавление питомца
response = requests.post(url, headers=headers, data=data)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.post(url, headers={'auth_key': 'invalid_key'}, data=data)
assert response.status_code == 403

# Тест на ошибку при отсутствии обязательных параметров
response = requests.post(url, headers=headers, data={'animal_type': 'dog'})
assert response.status_code == 400

2. Тестирование метода GET​/api​/key:

url = 'https://petstore.swagger.io/api/key'
headers = {'email': 'test@gmail.com', 'password': 'mypassword'}

# Тест на успешное получение ключа авторизации
response = requests.get(url, headers=headers)
assert response.status_code == 200

# Тест на ошибку при неверных учетных данных
response = requests.get(url, headers={'email': 'invalid_email', 'password': 'invalid_password'})
assert response.status_code == 403

3. Тестирование метода GET​/api​/pets:

url = 'https://petstore.swagger.io/api/pets'
headers = {'auth_key': 'my_api_key'}

# Тест на успешное получение списка питомцев
response = requests.get(url, headers=headers)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.get(url, headers={'auth_key': 'invalid_key'})
assert response.status_code == 403

# Тест на успешное получение списка своих питомцев
response = requests.get(url, headers=headers, params={'filter': 'my_pets'})
assert response.status_code == 200

4. Тестирование метода POST​/api​/pets:

url = 'https://petstore.swagger.io/api/pets'
headers = {'auth_key': 'my_api_key'}
data = {'name': 'Fluffy', 'animal_type': 'cat', 'age': 3}

# Тест на успешное добавление питомца
response = requests.post(url, headers=headers, data=data)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.post(url, headers={'auth_key': 'invalid_key'}, data=data)
assert response.status_code == 403

# Тест на ошибку при отсутствии обязательных параметров
response = requests.post(url, headers=headers, data={'animal_type': 'dog'})
assert response.status_code == 400

5. Тестирование метода POST​/api​/pets​/set_photo​/{pet_id}:

url = 'https://petstore.swagger.io/api/pets/12345/set_photo'
headers = {'auth_key': 'my_api_key'}
files = {'pet_photo': open('photo.jpg', 'rb')}

# Тест на успешную загрузку фото питомца
response = requests.post(url, headers=headers, files=files)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.post(url, headers={'auth_key': 'invalid_key'}, files=files)
assert response.status_code == 403

# Тест на ошибку при отсутствии ID питомца
response = requests.post('https://petstore.swagger.io/api/pets/set_photo', headers=headers, files=files)
assert response.status_code == 404

6. Тестирование метода ​/api​/pets​/{pet_id}:

url = 'https://petstore.swagger.io/api/pets/12345'
headers = {'auth_key': 'my_api_key'}

# Тест на успешное удаление питомца
response = requests.(url, headers=headers)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.(url, headers={'auth_key': 'invalid_key'})
assert response.status_code == 403

# Тест на ошибку при отсутствии ID питомца
response = requests.('https://petstore.swagger.io/api/pets', headers=headers)
assert response.status_code == 404

7. Тестирование метода PUT​/api​/pets​/{pet_id}:

url = 'https://petstore.swagger.io/api/pets/12345'
headers = {'auth_key': 'my_api_key'}
data = {'name': 'Fluffy Jr.', 'animal_type': 'cat', 'age': 4}

# Тест на успешное обновление информации о питомце
response = requests.put(url, headers=headers, data=data)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.put(url, headers={'auth_key': 'invalid_key'}, data=data)
assert response.status_code == 403

# Тест на ошибку при отсутствии ID питомца
response = requests.put('https://petstore.swagger.io/api/pets', headers=headers, data=data)
assert response.status_code == 404

8. Тестирование метода GET​/api​/test:

url = 'https://petstore.swagger.io/api/test'
headers = {'auth_key': 'my_api_key'}

# Тест на ошибку при обращении к несуществующему методу
response = requests.get(url, headers=headers)
assert response.status_code == 404

9. Тестирование метода POST​/api​/pets​/set_location​/{pet_id}:

url = 'https://petstore.swagger.io/api/pets/12345/set_location'
headers = {'auth_key': 'my_api_key'}
data = {'location': '1st Street, New York'}

# Тест на успешную установку местоположения питомца
response = requests.post(url, headers=headers, data=data)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.post(url, headers={'auth_key': 'invalid_key'}, data=data)
assert response.status_code == 403

# Тест на ошибку при отсутствии ID питомца
response = requests.post('https://petstore.swagger.io/api/pets/set_location', headers=headers, data=data)
assert response.status_code == 404

10. Тестирование метода PUT​/api​/pets​/{pet_id}​/change_name:

url = 'https://petstore.swagger.io/api/pets/12345/change_name'
headers = {'auth_key': 'my_api_key'}
data = {'new_name': 'Fluffy the Great'}

# Тест на успешную смену имени питомца
response = requests.put(url, headers=headers, data=data)
assert response.status_code == 200

# Тест на ошибку при неверном ключе авторизации
response = requests.put(url, headers={'auth_key': 'invalid_key'}, data=data)
assert response.status_code == 403

# Тест на ошибку при отсутствии ID питомца
response = requests.put('https://petstore.swagger.io/api/pets/change_name', headers=headers, data=data)
assert response.status_code == 404
