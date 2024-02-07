import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_video_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('meta', itemprop='name')
    views = soup.find('meta', itemprop='interactionCount')
    description = soup.find('meta', itemprop='description')
    publication_date = soup.find('meta', itemprop='datePublished')
    duration = soup.find('meta', itemprop='duration')

    video_data = {
        'Название': title['content'] if title else None,
        'Просмотры': views['content'] if views else None,
        'Описание': description['content'] if description else None,
        'Дата публикации': publication_date['content'] if publication_date else None,
        'Продолжительность': duration['content'] if duration else None
    }
    return video_data

async def scraping_video(video_url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, video_url)
        video_data = await parse_video_data(html)
        return video_data

video_url = 'https://www.youtube.com/watch?v=I0yJADAa5F8'

async def main():
    video_data = await scraping_video(video_url)
    for key, value in video_data.items():
        print(f"{key}: {value}")

async def main2():
    video_data = await scraping_video(video_url)
    for key, value in video_data.items():
        print(f"{key}: {value}")

asyncio.run(main())

asyncio.run(main2())
