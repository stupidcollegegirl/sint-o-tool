import asyncio
from providers import hibp, dns, whois_lookup, username, ip_geo


async def run_ip_scan(target: str):
    return await ip_geo.get_ip_geo(target)


async def run_email_scan(target: str):
    tasks = [hibp.check_breaches(target)]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def run_domain_scan(target: str):
    tasks = [
        dns.get_dns_records(target),
        whois_lookup.get_whois(target),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def run_username_scan(target: str):
    return await username.check_username(target)


# Phone scan
async def run_phone_scan(target: str):
    from providers.phone import phone_lookup
    return await phone_lookup(target)


def get_scan_function(target_type: str):
    """Главный диспетчер"""
    if target_type == "ip":
        return run_ip_scan
    elif target_type == "email":
        return run_email_scan
    elif target_type == "domain":
        return run_domain_scan
    elif target_type == "phone":
        return run_phone_scan
    else:  # username
        return run_username_scan
