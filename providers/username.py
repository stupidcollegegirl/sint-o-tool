import aiohttp
import asyncio


SITES = {
    "github": "https://github.com/{}",
    "reddit": "https://www.reddit.com/user/{}",
    "twitter": "https://twitter.com/{}",
    "instagram": "https://www.instagram.com/{}",
    "medium": "https://medium.com/@{}",
}


async def check_site(session, name, url):
    try:
        async with session.get(url, timeout=5) as resp:
            return name, resp.status == 200
    except:
        return name, False


async def check_username(username: str):
    results = {}

    async with aiohttp.ClientSession() as session:
        tasks = [
            check_site(session, name, url.format(username))
            for name, url in SITES.items()
        ]

        responses = await asyncio.gather(*tasks)

        for name, exists in responses:
            results[name] = exists

    return {"username": results}
