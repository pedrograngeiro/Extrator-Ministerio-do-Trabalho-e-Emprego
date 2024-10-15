from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as bs

class ParsingStrategy(ABC):
    @abstractmethod
    def parse(self, content):
        pass

class BeautifulSoupStrategy(ParsingStrategy):
    def parse(self, content):
        return bs(content, 'html.parser')