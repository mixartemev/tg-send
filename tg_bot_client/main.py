import logging
from aiohttp import ClientSession, ClientResponse

class TgBot:
    BASE_URL: str
    CHAT: int

    def __init__(self, bt, cid):
        self.session = ClientSession()
        self.BASE_URL = f'https://api.telegram.org/bot{bt}/'
        self.CHAT = cid

    async def close(self):
        await self.session.close()

    async def __handle_resp(self, response: ClientResponse):
        self.response = response
        try:
            if not str(response.status).startswith('2'):
                logging.error(response, response.status, await response.json(), response.request_info)
            return (r := await response.json()).get('data', r)
        except ValueError:
            txt = await response.text()
            raise Exception(f'Invalid Response: {txt}')

    async def send_msg(self,  txt: str, kb: list = None, chat_id: int = None):
        chat_id = chat_id or self.CHAT
        params = {
            'text': txt,
            'chat_id': chat_id,
            'parse_mode': 'Markdown',
        }
        # kb = [[{"text":"/start", "url": "/ya.ru"}]]
        if kb:
            params.update({'reply_markup': {'inline_keyboard': kb}})
        async with self.session.get(self.BASE_URL+'sendMessage', params=params) as resp:
            r = await self.__handle_resp(resp)
            return r
