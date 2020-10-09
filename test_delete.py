import requests

headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}

courses_url = 'http://localhost:8000/api/v2/courses/'
evaluations_url = 'http://localhost:8000/api/v2/evaluations/'

result = requests.delete(url=f'{courses_url}8/', headers=headers)

# Testando código HTTP
assert result.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(result.text) == 0  # Deve esttar vazio, pois o método DELETE n retorna nada