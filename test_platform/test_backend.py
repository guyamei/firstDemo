import requests as requests


def test_backend_hello():
    url = "http://127.0.0.1:5000/hello"
    data = {"nam": "zhangsan"}
    rs = requests.post(url, json=data)
    print(rs.text)


def test_case_add():
    url = "http://127.0.0.1:5000/testcase"
    data = {
        "name": "testcase2", "description": "step123", "steps": '["step1", "step2", "step3"]'
    }
    rs = requests.post(url, json=data)



def test_case_add_orm():
    url = "http://127.0.0.1:5000/testcase_orm"
    data = {
        "name": "testcase2", "description": "step123", "steps": '["step1", "step2", "step3"]'
    }
    rs = requests.post(url, json=data)



def test_case_delete_orm():
    url = "http://127.0.0.1:5000/testcase_orm?id=1"
    rs = requests.delete(url)


def test_case_put_orm():
    url = "http://127.0.0.1:5000/testcase_orm"
    data = {
        "id": 3, "name": "testcase3", "description": "step3", "steps": ["step1", "step2", "step3"]
    }
    rs = requests.put(url, json=data)


