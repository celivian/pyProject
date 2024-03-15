from requests import get, post

print(get('http://127.0.0.1:8080/api/jobs').json())
print(get('http://127.0.0.1:8080/api/jobs/1').json())
print(get('http://127.0.0.1:8080/api/jobs/213123').json())
print(get('http://127.0.0.1:8080/api/jobs/efwefwe').json())
print(post('http://127.0.0.1:8080/api/jobs', json={}).json())
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1, }).json())
print(post('http://127.0.0.1:8080/api/jobs', json={'team_leader': 1,
                                                   'job': 'Посдаить дерево',
                                                   'work_size': 9,
                                                   'collaborators': '1, 2, 5',
                                                   'is_finished': True}).json())
