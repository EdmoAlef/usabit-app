import asyncio
import aiohttp

async def converter_moeda(moeda_origem, moeda_destino):
    api = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    response_json = await fetch(api)
    conversao = response_json[f"{moeda_origem}{moeda_destino}"]["bid"]
    return conversao


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()