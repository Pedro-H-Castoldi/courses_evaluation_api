import requests

headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}

courses_url = 'http://localhost:8000/api/v2/courses/'
evaluations_url = 'http://localhost:8000/api/v2/evaluations/'

results = requests.get(url=courses_url, headers=headers)

print(results.json())

# Testando se o endpoint está correto
assert results.status_code == 200

# Testando a quantidade de registros
assert results.json()['count'] == 6

# Testando se o primeiro (o primeiro no caso seria o último, já q a paginação foi definada do último para o primeiro) curso tem o titlo esperado
assert results.json()['results'][0]['title'] == 'Curso de Linux 2'