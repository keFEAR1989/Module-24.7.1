def patch_pet_info(self, auth_key: json, pet_id: str, data: dict) -> json:
        """Метод отправляет запрос на сервер о частичном обновлении данных питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлёнными данными питомца"""

        headers = {'auth_key': auth_key['key']}

        res = requests.patch(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def head_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет запрос HEAD на сервер для получения метаданных питомца по указанному ID.
        Возвращает статус запроса и заголовки ответа."""

        headers = {'auth_key': auth_key['key']}

        res = requests.head(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = res.headers
        return status, result

    def options_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет запрос OPTIONS на сервер для получения разрешенных методов HTTP для питомца по указанному ID.
        Возвращает статус запроса и заголовки ответа."""

        headers = {'auth_key': auth_key['key']}

        res = requests.options(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = res.headers
        return status, result