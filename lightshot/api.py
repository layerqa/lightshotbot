import json
import aiohttp
import config

headers = {'user-agent': config.USER_AGENT}

async def upload_photo(photo):
    async with aiohttp.ClientSession() as session:
        async with session.post('https://prntscr.com/upload.php', headers=headers, data={'image': photo}) as resp:
            if resp.status == 200:
                data = json.loads(await resp.text())
                return {'error': 0, 'data': data}
            else:
                return {'error': 1, 'data': ''}