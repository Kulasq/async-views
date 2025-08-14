import asyncio
from django.http import HttpResponse, JsonResponse

import httpx


async def http_call_async(request):
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
    return HttpResponse(r.text, content_type="text/plain")

