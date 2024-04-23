import httpx
from parsel import Selector
from aiogram import Router, F, types


check_router = Router()


class DomCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text

    def get_title(self):
        html = Selector(self.page)
        title = html.css('title::text').get()
        return title

    def get_houses_link(self):
        html = Selector(self.page)
        links = html.css('.title a::attr(href)').getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:10]


@check_router.callback_query(F.data == 'check')
async def get_checked(cb: types.CallbackQuery):
    check = DomCrawler()
    check.get_page()
    list = check.get_houses_link()
    for item in list:
        await cb.message.answer(str(item))

    # await message.answer()



