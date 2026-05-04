import aiohttp


async def get_headers(domain: str):
    url = f"http://{domain}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:
                headers = dict(resp.headers)

                interesting = {
                    "Server": headers.get("Server"),
                    "Content-Type": headers.get("Content-Type"),
                    "X-Powered-By": headers.get("X-Powered-By"),
                }

                return {"http_headers": interesting}

    except Exception as e:
        return {"http_headers_error": str(e)}
