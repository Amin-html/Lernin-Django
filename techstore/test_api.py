import urllib.request
import json

# Получаем токен
data = json.dumps({
    'username': 'Amin',
    'password': '911911911'
}).encode()

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/token/',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

response = json.loads(urllib.request.urlopen(req).read().decode())
access_token = response['access']
print('Токен получен!')
# Шаг 2 — запрос к API с токеном
req2 = urllib.request.Request(
    'http://127.0.0.1:8000/laptops/api/',
    headers = {'Authorization': f'Bearer {access_token}'
    },
    method='GET'
)


laptops_response = urllib.request.urlopen(req2).read().decode()
print('Ноутбуки из API:')
print(json.dumps(json.loads(laptops_response), indent=2, ensure_ascii=False))
