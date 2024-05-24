import requests

def create_post(data):
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.post(url, json=data)

    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(response.json())

new_post = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

create_post(new_post)
