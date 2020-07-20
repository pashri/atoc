from abc import ABC, abstractmethod

class ParserFactoryInterface(ABC):

    @abstractmethod
    def get_parser(self, filename: str):
        """Get a parser instance for the file."""
        pass