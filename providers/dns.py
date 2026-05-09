import dns.resolver
import asyncio

async def get_dns_records(domain: str):
    result = {}
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 3

    records = ['A', 'MX', 'TXT', 'NS']

    for record_type in records:
        try:
            answers = resolver.resolve(domain, record_type)
            result[record_type] = [str(r) for r in answers]
        except:
            result[record_type] = []

    return {"dns": result}
