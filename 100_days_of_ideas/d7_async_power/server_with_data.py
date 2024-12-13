import asyncio
import random
from aiohttp import web

async def slow_response(data):
    # Simulate a random delay between 1 and 3 seconds
    await asyncio.sleep(random.randint(1, 3))
    return data

async def handle_user(request):
    data = {
        "id": 1,
        "username": "john_doe",
        "full_name": "John Doe"
    }
    return web.json_response(await slow_response(data))

async def handle_posts(request):
    data = [
        {"post_id": 101, "title": "My first post", "content": "Hello world!"},
        {"post_id": 102, "title": "Another day", "content": "Just had coffee."}
    ]
    return web.json_response(await slow_response(data))

async def handle_comments(request):
    data = [
        {"comment_id": 201, "post_id": 101, "text": "Nice post!"},
        {"comment_id": 202, "post_id": 102, "text": "Thanks for sharing!"}
    ]
    return web.json_response(await slow_response(data))

app = web.Application()
app.router.add_get('/user', handle_user)
app.router.add_get('/posts', handle_posts)
app.router.add_get('/comments', handle_comments)

if __name__ == '__main__':
    web.run_app(app, port=8080)
