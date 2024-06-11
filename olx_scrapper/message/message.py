from dataclasses import dataclass


@dataclass(kw_only=True)
class Message:
    ...


@dataclass(kw_only=True)
class OfferMessage(Message):
    title: str
    price: str
    time: str
    url: str

    def __str__(self):
        return f"{self.title}_{self.price}"
