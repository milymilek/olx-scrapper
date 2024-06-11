from olx_scrapper.runner import ScrapRunner
from olx_scrapper.scrap import OLXScrapper
from olx_scrapper.distribute import DistributionChannels
from olx_scrapper.distribute.telegram.channel import TelegramChannel
from olx_scrapper.config import settings


if __name__ == "__main__":
    from olx_scrapper.message import OfferMessage
    channel = TelegramChannel()
    channel.send(msg=OfferMessage(title="123", price="456", time="789", url="000"))
    # runner = ScrapRunner(
    #     scrapper=OLXScrapper(base_url=settings.base_url),
    #     distribution_channels=DistributionChannels(channels=[TelegramChannel()]),
    #     refresh_rate=settings.refresh_rate
    # )
    # runner.init_scrap()
    # runner.loop()