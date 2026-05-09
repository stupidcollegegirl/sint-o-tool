import aiohttp
from typing import Dict
from rich.console import Console

console = Console()

SITES = {
    "github": "https://github.com/{}",
    "gitlab": "https://gitlab.com/{}",
    "vk": "https://vk.com/{}",
    "youtube": "https://www.youtube.com/@{}",
    "reddit": "https://www.reddit.com/user/{}",
    "twitch": "https://www.twitch.tv/{}",
    "telegram": "https://t.me/{}",
}

async def check_username(username: str) -> Dict:

    results = {}
    
    console.print(f"[+] cheking @{username}...")

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        for site, url_template in SITES.items():
            try:
                url = url_template.format(username)
                async with session.get(url, allow_redirects=True) as resp:
                    if resp.status == 200:
                        text = await resp.text()
                        bad = ["not found", "doesn't exist", "page not found", "unavailable"]
                        if not any(phrase in text.lower() for phrase in bad):
                            results[site] = url
                            continue
            except:
                pass
            
            results[site] = False

    return {"username": results}
