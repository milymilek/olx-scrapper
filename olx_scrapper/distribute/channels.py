import abc

from olx_scrapper.message import Message


class ChannelInterface(abc.ABC):
    @abc.abstractmethod
    def send(self, msg: Message | list[Message]) -> None:
        ...