from abc import ABC, abstractmethod

from discord.ext.commands import Context


class BaseCommand(ABC):

    def __init__(self, context: Context):
        self.ctx = context

    @abstractmethod
    async def apply(self):
        pass