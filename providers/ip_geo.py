import aiohttp
from typing import Dict

async def get_ip_geo(ip: str) -> Dict:
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting"

            async with session.get(url, timeout=10) as resp:
                if resp.status != 200:
                    return {"ip_geo_error": f"HTTP {resp.status}"}

                data = await resp.json()

                if data.get("status") == "fail":
                    return {"ip_geo_error": data.get("message", "Unknown error")}

                return {
                    "ip_geo": {
                        "ip": ip,
                        "country": data.get("country"),
                        "country_code": data.get("countryCode"),
                        "city": data.get("city"),
                        "region": data.get("regionName"),
                        "timezone": data.get("timezone"),
                        "isp": data.get("isp"),
                        "org": data.get("org"),
                        "coordinates": f"{data.get('lat')}, {data.get('lon')}" if data.get('lat') else None,
                        "is_proxy": data.get("proxy", False),
                        "is_hosting": data.get("hosting", False),
                        "is_mobile": data.get("mobile", False),
                    }
                }
    except Exception as e:
        return {"ip_geo_error": str(e)}
