import requests
import jsonpath

evaluations = requests.get('http://localhost:8000/api/v2/evaluations/')

results = jsonpath.jsonpath(evaluations.json(), 'results')
print(results)

first = jsonpath.jsonpath(evaluations.json(), 'results[0]')
print(first)

first_result_name = jsonpath.jsonpath(evaluations.json(), 'results[0].name')
print(first_result_name)

first_grade = jsonpath.jsonpath(evaluations.json(), 'results[0].grade')
print(first_grade)

# Pegar todos os nomes das pessoas q avaliaram o curso
names = jsonpath.jsonpath(evaluations.json(), 'results[*].name')
print(names)

grades = jsonpath.jsonpath(evaluations.json(), 'results[*].grade')
print(grades)