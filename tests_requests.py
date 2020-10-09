import requests

# GET Evaluations

evaluations = requests.get('http://localhost:8000/api/v2/evaluations')
print(evaluations.status_code)

# Acessando os dados da resposta
print(evaluations.json())

# Quantidade de dados
print(evaluations.json()['count'])

# Acessando a proxima página de resultados
print(evaluations.json()['next'])

# Acessando os resultado desta página
print(evaluations.json()['results'])

# Acessando o primeiro elemento da lista
print(evaluations.json()['results'][0])

# Acessando o último elemento da lista
print(evaluations.json()['results'][-1])

# Acessando o nome da pessoa q fez a última avaliação
print(evaluations.json()['results'][-1]['name'])

# GET uma avaliação
evaluation = requests.get('http://localhost:8000/api/v2/evaluations/3/')
print(evaluation.json())

# GET cursos
# Obtendo autorização
headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}
courses = requests.get(url='http://localhost:8000/api/v2/courses', headers=headers)
print(courses.json())