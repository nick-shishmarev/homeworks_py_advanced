from os import getenv
import requests
from dotenv import load_dotenv

ya_dsk_url = 'https://cloud-api.yandex.net/v1/disk/resources'
# folder_name = 'A1'
load_dotenv()
ya_token = getenv("ya_token")
print(ya_token)


def make_folder(folder_name: str, token=ya_token):
    # Создание папки на ЯндексДиске
    params = {'path': folder_name}
    headers = {'Authorization': token}

    response = requests.put(ya_dsk_url, params=params, headers=headers)

    return response.status_code


def get_folder_info(folder_name: str):
    params = {'path': folder_name}
    headers = {'Authorization': ya_token}

    response = requests.get(ya_dsk_url, params=params, headers=headers)

    return response.status_code


if __name__ == '__main__':
    status = make_folder(123)
    # assert status == 201
    print(status)
