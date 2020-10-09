import requests

headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}

courses_url = 'http://localhost:8000/api/v2/courses/'
evaluations_url = 'http://localhost:8000/api/v2/evaluations/'

put_curse = {
    "title": "Curso de Linux 5",
    "url": "https://www.udemy.com/course/curso-online-certificacao-linux-lpic1-comptia/"
}

result = requests.put(url=f'{courses_url}8/', headers=headers, data=put_curse)

# Testando o código de status HTTP
assert result.status_code == 200

# Testando o título
assert result.json()['title'] == put_curse['title']