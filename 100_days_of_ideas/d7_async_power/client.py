import time
import asyncio
import requests
import aiohttp

urls = [
    "http://localhost:8080/endpoint1",
    "http://localhost:8080/endpoint2",
    "http://localhost:8080/endpoint3"
]

# Synchronous fetch using requests
def synchronous_fetch(urls):
    start = time.perf_counter()
    results = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        results.append(f"{data['endpoint']}: {data['message']}")
    end = time.perf_counter()
    print(f"Synchronous total time: {end - start:.2f} seconds")
    return results

# Asynchronous fetch using aiohttp
async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return f"{data['endpoint']}: {data['message']}"

async def asynchronous_fetch(urls):
    async with aiohttp.ClientSession() as session:
        start = time.perf_counter()
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        end = time.perf_counter()
        print(f"Asynchronous total time: {end - start:.2f} seconds")
        return results

def main():
    print("=== Synchronous Execution ===")
    sync_results = synchronous_fetch(urls)
    for res in sync_results:
        print(res)

    print("\n=== Asynchronous Execution ===")
    async_results = asyncio.run(asynchronous_fetch(urls))
    for res in async_results:
        print(res)

    # Compare times
    # (In a more controlled example, you'd measure both in variables and compare)
    print("\nObserve that the asynchronous fetch typically completes faster " 
          "since all requests run concurrently rather than sequentially.")

if __name__ == "__main__":
    main()
