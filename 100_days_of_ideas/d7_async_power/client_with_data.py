import time
import asyncio
import requests
import aiohttp

BASE_URL = "http://localhost:8080"

urls = {
    "user": f"{BASE_URL}/user",
    "posts": f"{BASE_URL}/posts",
    "comments": f"{BASE_URL}/comments"
}

# Synchronous approach
def synchronous_fetch(urls):
    start = time.perf_counter()
    user_data = requests.get(urls['user']).json()
    posts_data = requests.get(urls['posts']).json()
    comments_data = requests.get(urls['comments']).json()

    # Aggregate data into a single dictionary
    result = {
        "user": user_data,
        "posts": posts_data,
        "comments": comments_data
    }

    end = time.perf_counter()
    print(f"Synchronous total time: {end - start:.2f} seconds")
    return result

# Asynchronous approach
async def async_fetch_one(session, url):
    async with session.get(url) as response:
        return await response.json()

async def asynchronous_fetch(urls):
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        user_task = asyncio.create_task(async_fetch_one(session, urls['user']))
        posts_task = asyncio.create_task(async_fetch_one(session, urls['posts']))
        comments_task = asyncio.create_task(async_fetch_one(session, urls['comments']))

        user_data, posts_data, comments_data = await asyncio.gather(user_task, posts_task, comments_task)

    result = {
        "user": user_data,
        "posts": posts_data,
        "comments": comments_data
    }

    end = time.perf_counter()
    print(f"Asynchronous total time: {end - start:.2f} seconds")
    return result

def main():
    print("=== Synchronous Execution ===")
    sync_result = synchronous_fetch(urls)
    print("Aggregated Result:")
    print(sync_result)

    print("\n=== Asynchronous Execution ===")
    async_result = asyncio.run(asynchronous_fetch(urls))
    print("Aggregated Result:")
    print(async_result)

    print("\nObserve that the asynchronous version likely finishes faster,")
    print("even though it is performing the same tasks and producing the same result.")
    print("This demonstrates how asynchronous programming can speed up I/O-bound workloads.")
    
if __name__ == "__main__":
    main()
