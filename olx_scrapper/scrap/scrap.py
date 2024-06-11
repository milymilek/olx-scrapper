import abc
import requests
from bs4 import BeautifulSoup

from olx_scrapper.message import Message


class ScrapperInterface(abc.ABC):
    @abc.abstractmethod
    def scrap(self) -> Message:
        ...


class OLXScrapper(ScrapperInterface):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def _get_page_content(url): 
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def scrap(self) -> Message:
        print("scrapping")
        page_content = self._get_page_content(self.base_url)
        soup = BeautifulSoup(page_content, 'html.parser')
        offers = soup.find_all("div", class_="css-19ucd76")
    