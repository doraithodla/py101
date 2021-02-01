URLs = ['https://ashish.ch',
        'https://github.com',
        'https://readthedocs.org/',
        'https://en.wikipedia.org/wiki/Main_Page',
        'https://hackernoon.com/',
        'https://techcrunch.com/']

import aiohttp
import asyncio
import time


async def get_url(url):
    """Perform an HTTP GET to the URL and print the response"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


loop = asyncio.get_event_loop()
# Create the batch of requests we wish to execute
requests = []
for url in URLs:
    requests.append(asyncio.ensure_future(get_url(url)))

start = time.time()
website_content = loop.run_until_complete(asyncio.gather(*requests))
end = time.time()
print("Time taken %f ms" % ((end - start) * 1000.0))
# Time taken 10877.706289 ms
