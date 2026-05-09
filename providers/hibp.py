import aiohttp

async def check_breaches(email: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=true"
            headers = {
                "User-Agent": "SINT-OSINT-Tool - https://github.com/stupidcollegegirl/sint-o-tool",
                "hibp-api-key": ""
            }

            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {"hibp": {"breaches": data, "count": len(data)}}

                elif resp.status == 404:
                    return {"hibp": {"breaches": [], "count": 0}}

                elif resp.status == 401:
                    return {"hibp_error": "! api key "}

                elif resp.status == 429:
                    return {"hibp_error": "Rate limit exceeded"}

                else:
                    return {"hibp_error": f"HTTP {resp.status}"}

    except Exception as e:
        return {"hibp_error": str(e)}
