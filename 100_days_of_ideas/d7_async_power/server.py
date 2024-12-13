import asyncio
import random
from aiohttp import web

async def handle(request):
    # Simulate a random delay from 1 to 3 seconds
    await asyncio.sleep(random.randint(1, 3))
    return web.json_response({"message": "Hello from the server!", "endpoint": str(request.rel_url)})

app = web.Application()
app.router.add_get('/{tail:.*}', handle)  # catch-all route

if __name__ == '__main__':
    web.run_app(app, port=8080)
