import tkinter as tk
from tkinter import messagebox
import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_video_data(html, label_vars):
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

    for key, value in video_data.items():
        label_vars[key].set(f"{key}: {value}")

async def scraping_video(video_url, label_vars):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, video_url)
        await parse_video_data(html, label_vars)

def scrape_video_data():
    video_url = url_entry.get()
    try:
        label_vars = {}
        for key in ['Название', 'Просмотры', 'Описание', 'Дата публикации', 'Продолжительность']:
            label_vars[key] = tk.StringVar()
            label = tk.Label(root, textvariable=label_vars[key])
            label.pack()
        url_entry.delete(0, 'end')
        url_entry.insert(0, video_url)
        asyncio.run(scraping_video(video_url, label_vars))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


root = tk.Tk()
root.title("Парсер данных видео")

url_label = tk.Label(root, text="Введите URL видео:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

scrape_button = tk.Button(root, text="Получить данные видео", command=scrape_video_data)
scrape_button.pack()

root.mainloop()
