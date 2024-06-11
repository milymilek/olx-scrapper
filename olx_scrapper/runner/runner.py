import abc
import time

from olx_scrapper.config import settings
from olx_scrapper.distribute import DistributionChannelsInterface
from olx_scrapper.scrap import ScrapperInterface


class ScrapRunnerInterface(abc.ABC):
    @abc.abstractmethod
    def init_scrap(self) -> None:
        """Initialize scrapping by gathering first results"""
        ...

    @abc.abstractmethod
    def loop(self) -> None:
        ...


class ScrapRunner(ScrapRunnerInterface):
    def __init__(
        self, 
        scrapper: ScrapperInterface, 
        distribution_channels: DistributionChannelsInterface,
        refresh_rate: int
    ):
        self.scrapper = scrapper
        self.distribution_channels = distribution_channels

        self.refresh_rate = refresh_rate

    def init_scrap(self) -> None:
        print("init")

    def loop(self) -> None:
        while True:
            message = self.scrapper.scrap()
            #self.distribution_channels.send(message=message)

            time.sleep(settings.refresh_rate)
