import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Статус-код : {response.status_code}")
        print(f"Заголовок : {response.headers['Content-Type']}")
        print(f"Тело ответа : {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {e}")

main()