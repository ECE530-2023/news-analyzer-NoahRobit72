import queue
import requests
import threading

# Create a queue to hold the requests
request_queue = queue.Queue()

# Define the structure of the request
class Request:
    def __init__(self, url, method, headers=None, payload=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload

# Add requests to the queue
request_queue.put(Request('https://jsonplaceholder.typicode.com/posts', 'GET'))
request_queue.put(Request('https://jsonplaceholder.typicode.com/posts', 'POST', headers={'Content-Type': 'application/json'}, payload={'title': 'foo', 'body': 'bar', 'userId': 1}))

# Process the requests
def process_requests():
    while not request_queue.empty():
        # Dequeue a request from the front of the queue
        request = request_queue.get()

        # Make the HTTP request
        try:
            if request.method == 'GET':
                response = requests.get(request.url, headers=request.headers)
            elif request.method == 'POST':
                response = requests.post(request.url, headers=request.headers, json=request.payload)
            # Add other HTTP methods as needed

            # Handle the response
            print(response.json())
        except Exception as e:
            print(f'Error making request: {e}')

# Spawn multiple threads to process the requests concurrently
num_threads = 4
threads = []
for i in range(num_threads):
    t = threading.Thread(target=process_requests)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
