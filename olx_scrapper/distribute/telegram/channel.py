import requests

from olx_scrapper.distribute import ChannelInterface
from olx_scrapper.distribute.telegram.settings import telegram_settings
from olx_scrapper.message import Message


class TelegramChannel(ChannelInterface):
    def __init__(self):
        self._url = self._build_url()
        # found_url = o.find_element(By.CSS_SELECTOR, "a.css-1bbgabe").get_attribute('href')
        # message = f'{found.group()}, {found_url}'

    @staticmethod
    def _build_url():
        return f'https://api.telegram.org/bot{telegram_settings.auth_token}/sendMessage?chat_id={telegram_settings.group_id}'

    def send(self, message: Message):
        send_url = self._url + f"&text={str(message)}"
        requests.get(send_url)
