from olx_scrapper.message.buffer import MessageBuffer


class MessageFilter:
    def __init__(self):
        self.buffer = MessageBuffer()

    @staticmethod
    def _check_highlighted(message):
        highlighted_tag = message.find("div", class_="css-3xiokn")
        return "Wyróżnione" in highlighted_tag.text

    @staticmethod
    def _check_refreshed(message):
        location_tag = message.find("p", {"data-testid": "location-date"})
        return "Odświeżono" in location_tag.text

    @staticmethod
    def _check_not_today(message):
        location_tag = message.find("p", {"data-testid": "location-date"})
        return "Dzisiaj" not in location_tag.text

    @staticmethod
    def _check_invalid_price(message):
        price_tag = message.find("p", {"data-testid": "ad-price"})
        return price_tag is False

    def _check_in_buffer(self, message):
        b = len(self.buffer)
        self.buffer.add(message)
        a = len(self.buffer)
        return a == b

    def filter(self, message):
        try:
            for _check in [
                self._check_highlighted,
                self._check_refreshed,
                self._check_not_today,
                self._check_invalid_price,
                self._check_in_buffer,
            ]:
                if _check(message):
                    return True

            return False
        except AttributeError as e:
            print(e)
            return True
