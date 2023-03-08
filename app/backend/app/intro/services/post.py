import requests

from app.intro.models import Post


def validate_user(user_id: int) -> bool:
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    response = None
    if r.status_code == 200:
        return True

    return False


def create_post(*, user_id: int, title: str, body: str) -> Post:
    if validate_user(user_id):
        post = Post(user_id=user_id, title=title, body=body)
        post.save()

        return post

    return None
