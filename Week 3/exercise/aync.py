import asyncio
import aiohttp

# Async function to fetch a single URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Async function to fetch multiple URLs concurrently
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]  # create tasks for all URLs
        results = await asyncio.gather(*tasks)        # run tasks concurrently
        return results

# Example usage
urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://httpbin.org/get"
]

async def main():
    results = await fetch_all(urls)
    for i, content in enumerate(results):
        print(f"URL {i+1}: {len(content)} characters fetched")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
