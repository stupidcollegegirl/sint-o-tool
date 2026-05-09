import aiohttp
from typing import Dict

RUSSIAN_OPERATORS = {
    "900": "МТС", "901": "МТС", "902": "МТС", "903": "МТС", "904": "МТС", "905": "МТС", "906": "МТС", "908": "МТС", "910": "МТС", "915": "МТС", "916": "МТС", "917": "МТС", "919": "МТС",
    "920": "МегаФон", "921": "МегаФон", "922": "МегаФон", "923": "МегаФон", "924": "МегаФон", "925": "МегаФон", "926": "МегаФон", "927": "МегаФон", "928": "МегаФон", "929": "МегаФон",
    "930": "Tele2", "931": "Tele2", "932": "Tele2", "933": "Tele2", "934": "Tele2", "935": "Tele2", "936": "Tele2", "937": "Tele2", "938": "Tele2", "939": "Tele2",
    "950": "Tele2", "951": "Tele2", "952": "Tele2", "953": "Tele2", "955": "Tele2",
    "960": "Билайн", "961": "Билайн", "962": "Билайн", "963": "Билайн", "964": "Билайн", "965": "Билайн", "966": "Билайн", "967": "Билайн", "968": "Билайн", "969": "Билайн",
}

async def phone_lookup(phone: str) -> Dict:
    
    clean = ''.join(filter(str.isdigit, phone))
    if len(clean) == 11 and clean.startswith('8'):
        clean = '7' + clean[1:]
    if len(clean) == 10:
        clean = '7' + clean

    international = f"+{clean}"
    operator = "idk"

    prefix = clean[1:4] if len(clean) > 4 else ""
    operator = RUSSIAN_OPERATORS.get(prefix, "idk")

    try:
        async with aiohttp.ClientSession() as session:

            urls = [
                f"https://api.numlookupapi.com/v1/validate/{international}",
                f"http://apilayer.net/api/validate?access_key=free&number={international}",
            ]

            for url in urls:
                try:
                    async with session.get(url, timeout=8) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            if data.get("valid"):
                                return {
                                    "phone": {
                                        "number": international,
                                        "valid": True,
                                        "country": data.get("country_name", "Россия"),
                                        "carrier": data.get("carrier") or operator,
                                        "line_type": data.get("line_type", "mobile"),
                                        "location": data.get("location"),
                                    }
                                }
                except:
                    continue

    except:
        pass


    return {
        "phone": {
            "number": international,
            "valid": True,
            "country": "Russia",
            "carrier": operator,
            "line_type": "mobile",
            "note": "info from open resources"
        }
    }
