import asyncio
import aiohttp
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            soup = BeautifulSoup(result, 'html.parser')

            book = soup.find_all('h3')
            price = soup.find_all('p',  {'class': 'price_color'})
            stock = soup.find_all('p', {'class': 'availability'})
            photo = soup.find_all('img', {'class': 'thumbnail'})

            for i in range(len(book)):
                print(f'{book[i].text}\n'
                      f'{price[i].text}\n'
                      f'{stock[i].text}\n'
                      f'{photo[i].get('content')}\n'
                      f'-------------------------------------')


asyncio.run(main())