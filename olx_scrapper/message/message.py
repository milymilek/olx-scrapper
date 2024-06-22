from dataclasses import dataclass


@dataclass(kw_only=True)
class Message: ...


@dataclass(kw_only=True)
class OfferMessage(Message):
    title: str
    price: str
    time: str
    url: str

    @property
    def full_url(self):
        return self._base_url + self.url

    def __str__(self):
        return f"[Title]: {self.title}\n[Price]: {self.price}\n[Time]: {self.time}\n[URL]: {self.full_url}"


@dataclass(kw_only=True)
class OLXMessage(OfferMessage):
    _base_url: str = "https://olx.pl"
