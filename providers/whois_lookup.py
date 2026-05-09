import whois
import asyncio

async def get_whois(domain: str):

    try:

        loop = asyncio.get_running_loop()
        data = await loop.run_in_executor(None, whois.whois, domain)

        return {
            "whois": {
                "domain_name": data.domain_name,
                "registrar": data.registrar,
                "creation_date": data.creation_date,
                "expiration_date": data.expiration_date,
                "name_servers": data.name_servers,
            }
        }
    except Exception as e:
        return {"whois_error": str(e)}
