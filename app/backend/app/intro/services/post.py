import requests

from app.intro.models import Post


def validate_user(user_id: int) -> bool:
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if r.status_code == 200:
        return True

    return False


def create_post(*, user_id: int, title: str, body: str) -> Post:
    if validate_user(user_id):
        post = Post(user_id=user_id, title=title, body=body)
        post.save()

        return post

    return None


def get_post(post_id: int) -> Post:
    r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    response = None
    post = None
    if r.status_code == 200:
        response = r.json()
        try:
            post = Post.objects.get(user_id=int(response['userId']), title=response['title'],
                                    body=response['body'])
        except:
            post = create_post(user_id=int(response['userId']), title=response['title'],
                               body=response['body'])

    return post


def get_user_posts(user_id: int):
    if validate_user(user_id):
        return Post.objects.filter(user_id=user_id)

    return None
