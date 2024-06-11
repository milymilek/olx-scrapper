import abc
import requests
from bs4 import BeautifulSoup

from olx_scrapper.message import Message, OfferMessage


class ScrapperInterface(abc.ABC):
    @abc.abstractmethod
    def scrap(self) -> list[Message]:
        ...


class OLXScrapper(ScrapperInterface):
    _list_css_class = "css-j0t2x2"
    _list_el_css_class = "css-1sw7q4x"
    _el_title_css_class = "css-16v5mdi er34gjf0"
    _el_price_data_testid = "ad-price"
    _el_time_data_testid = "location-date"
    _el_link_css_class = "css-z3gu2d"

    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def _get_page_content(url): 
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def scrap(self) -> list[Message]:
        page_content = self._get_page_content(self.base_url)
        soup = BeautifulSoup(page_content, 'html.parser')
        offers = soup.find_all("div", class_=self._list_el_css_class)

        messages = []
        for offer in offers:
            try:
                title_tag = offer.find("h6", class_=self._el_title_css_class)
                title = title_tag.text if title_tag else "No title"

                price_tag = offer.find("p", {"data-testid": self._el_price_data_testid})
                price = price_tag.text if price_tag else "No price"

                time_tag = offer.find("p", {"data-testid": self._el_time_data_testid})
                time = time_tag.text if time_tag else "No time"

                link_tag = offer.find("a", class_="css-z3gu2d")
                link = link_tag['href'] if link_tag else "No link"

                message = OfferMessage(title=title, price=price, time=time, url=link)
                messages.append(message)
            except Exception as e:
                print(f"Error processing offer: {e}")

        return messages
    