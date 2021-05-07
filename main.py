from typing import Optional
from fastapi import FastAPI
import random
from time import sleep
import asyncio


app = FastAPI()

'''
# permite concurrencia respecto a otras requests, pero secuencializa la generación de a lista

@app.get("/")
async def read_root():
    return [await return_number(number) for number in range(4)]
'''

# con esta solución a su vez, podemos lanzar todas las subpeticiones concurrentemente

@app.get("/")
async def read_root():
    return await asyncio.gather(*[return_number(number) for number in range(4)])


async def return_number(number):
    time_to_sleep = random.randint(1, 3) / 4
    await asyncio.sleep(time_to_sleep)
    print(number)

    return number
