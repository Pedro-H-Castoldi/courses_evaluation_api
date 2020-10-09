import requests

headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}

courses_url = 'http://localhost:8000/api/v2/courses/'
evaluations_url = 'http://localhost:8000/api/v2/evaluations/'

new_course = {
    "title": "Lógica de Programação 3",
    "url": "https://www.udemy.com/course/ssd"

}

result = requests.post(url=courses_url, headers=headers, data=new_course)

# testando o código de status HTTP
assert result.status_code == 201

# Testando se o titlo do curso retornado é o mesmo do informado
assert result.json()['title'] == new_course['title']