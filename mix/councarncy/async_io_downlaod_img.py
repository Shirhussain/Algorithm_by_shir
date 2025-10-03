import aiohttp
import asyncio 
import aiofiles



IMAGE_URL = [
    'https://m.media-amazon.com/images/I/41HcM1yzHcL._SX327_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/418RCXzyprL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg',
    'https://m.media-amazon.com/images/I/419SXBT4bjL._SX329_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/51VC+Vru96L._SX320_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/51Zu0ZwT0jL._SX320_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/61ZvgQihlkL._SX440_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/413MbCa36bL._SX327_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/61aCVDVZPzL._SX484_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/51-uspgqWIL._SX329_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/516XEz3XX4L._SY291_BO1,204,203,200_QL40_FMwebp_.jpg',
    'https://m.media-amazon.com/images/I/516xnnMfXML._SX439_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/41ZLnc34EiL._SX332_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/41zFito0fdL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg',
    'https://m.media-amazon.com/images/I/51ECRZXoGyL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg',
    'https://m.media-amazon.com/images/I/41aahkE2nzL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg',
    'https://m.media-amazon.com/images/I/51pPlBy6-pL._SX431_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/41w4B0f21VL._SY349_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/41iYyNgZOWL._SX384_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/51vJ-6d-dDL._SY483_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/51bZujlJxlL._SX422_BO1,204,203,200_.jpg',
    'https://m.media-amazon.com/images/I/41D3enj6JVS._SX324_BO1,204,203,200_.jpg'
]

async def get_name(url):
    _name = url.split('/')[5].split('.')[0]
    return f'{_name}.jpg'


async def save_content(name, content):
    async with aiofiles.open(name, 'wb') as image:
            await image.write(content)

async def fetch_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            name = await get_name(url)
            await save_content(name, await response.read())


async def main():
    result = map(fetch_image, IMAGE_URL)
    await asyncio.gather(*tuple(result))



asyncio.run(main())


