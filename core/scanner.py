import asyncio
from providers import hibp, dns, whois_lookup, username, http_headers


async def run_email_scan(target: str):
    tasks = [
        hibp.check_breaches(target),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def run_domain_scan(target: str):
    tasks = [
        dns.get_dns_records(target),
        whois_lookup.get_whois(target),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def run_username_scan(target: str):
    tasks = [
        username.check_username(target),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)
