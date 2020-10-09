import requests


class TestCourses:
    headers = {'Authorization': 'token b22ac19165d86707fadce8f220f65a118acf4e27'}
    courses_url = 'http://localhost:8000/api/v2/courses/'

    def test_get_courses(self):
        courses = requests.get(url=self.courses_url, headers=self.headers)

        assert courses.status_code == 200

    def test_get_course(self):
        course = requests.get(url=f'{self.courses_url}2/', headers=self.headers)

        assert course.status_code == 200

    def test_post_course(self):
        new_course = {
            "title": "Curso de programação Ruby",
            "url": "https://www.udemy.com.br/ruby"
        }

        response = requests.post(url=self.courses_url, headers=self.headers, data=new_course)

        assert response.status_code == 201
        assert response.json()['title'] == new_course['title']

    def test_put_course(self):
        put = {
            "title": "Curso de programação Ruby Novo",
            "url": "https://www.udemy.com.br/novo/ruby"
        }

        response = requests.put(url=f'{self.courses_url}2/', headers=self.headers, data=put)

        assert response.status_code == 200


    def test_put_course_title(self):
        put = {
            "title": "Curso de programação Ruby 3",
            "url": "https://www.udemy.com.br/ruby3"
        }

        response = requests.put(url=f'{self.courses_url}2/', headers=self.headers, data=put)

        assert response.json()['title'] == put['title']

    def test_delete_course(self):
        response = requests.delete(url=f'{self.courses_url}2/', headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0