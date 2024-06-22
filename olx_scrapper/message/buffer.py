from olx_scrapper.message.message import Message


class MessageBuffer:
    def __init__(
        self,
    ):
        self.buffer: set[Message] = set()

    def add(self, message):
        self.buffer.add(message)

    def __len__(self):
        return len(self.buffer)
