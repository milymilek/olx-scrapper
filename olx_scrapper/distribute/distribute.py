import abc

from olx_scrapper.message import Message
from olx_scrapper.distribute import ChannelInterface


class DistributionChannelsInterface(abc.ABC):
    @abc.abstractmethod
    def distribute(self, messages: list[Message]) -> None: ...


class DistributionChannels(DistributionChannelsInterface):
    def __init__(self, channels: list[ChannelInterface]):
        self.channels = channels

    def distribute(self, messages: list[Message]) -> None:
        for channel in self.channels:
            channel.send(messages)
