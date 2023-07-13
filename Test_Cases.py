import requests

# Тест 1: Проверка статуса ответа 200

response = requests.get('https://api.example.com/v1/users')

assert response.status_code == 200

# Тест 2: Проверка содержимого ответа

response = requests.get('https://api.example.com/v1/users')

assert response.json() == {
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "johndoe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
  ]
}

# Тест 3: Проверка ответа при передаче неправильного ключа авторизации

response = requests.get('https://api.example.com/v1/users', headers={'Authorization': 'Bearer invalid_token'})

assert response.status_code == 401

# Тест 4: Проверка ответа при передаче слишком большого значения параметра

response = requests.get('https://api.example.com/v1/users?page_size=10000')

assert response.status_code == 400

# Тест 5: Проверка ответа при пропуске параметра

response = requests.get('https://api.example.com/v1/users?page_size')

assert response.status_code == 400

# Тест 6: Проверка ответа при передаче неправильного типа параметра

response = requests.get('https://api.example.com/v1/users?page_size=asdf')

assert response.status_code == 400

# Тест 7: Проверка ответа при передаче неправильного значения параметра

response = requests.get('https://api.example.com/v1/users?page_size=-1')

assert response.status_code == 400

# Тест 8: Проверка ответа при передаче неправильного имени параметра

response = requests.get('https://api.example.com/v1/users?page_size_asdf=10')

assert response.status_code == 400

# Тест 9: Проверка ответа при передаче параметра в заголовке запроса

response = requests.get('https://api.example.com/v1/users', headers={'page_size': 10})

assert response.status_code == 400

# Тест 10: Проверка ответа при передаче параметра в теле запроса

response = requests.post('https://api.example.com/v1/users', data={'page_size': 10})

assert response.status_code == 400
