import asyncio
import aiohttp

# Define the structure of the request
class Request:
    def __init__(self, url, method, headers=None, payload=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload

# Add requests to the queue
requests = [
    Request('https://jsonplaceholder.typicode.com/posts', 'GET'),
    Request('https://jsonplaceholder.typicode.com/posts', 'POST', headers={'Content-Type': 'application/json'}, payload={'title': 'foo', 'body': 'bar', 'userId': 1})
]

# Define the async function to process the requests
async def process_request(request):
    async with aiohttp.ClientSession() as session:
        try:
            if request.method == 'GET':
                async with session.get(request.url, headers=request.headers) as response:
                    response_json = await response.json()
            elif request.method == 'POST':
                async with session.post(request.url, headers=request.headers, json=request.payload) as response:
                    response_json = await response.json()
            # Add other HTTP methods as needed

            # Handle the response
            print(response_json)
        except Exception as e:
            print(f'Error making request: {e}')

# Define the main async function to process all requests
async def main():
    # Create a list of coroutines for each request
    coroutines = [process_request(request) for request in requests]

    # Run the coroutines concurrently
    await asyncio.gather(*coroutines)

# Run the main async function
asyncio.run(main())
