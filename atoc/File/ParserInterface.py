from abc import ABC, abstractmethod

class ParserInterface(ABC):

    @abstractmethod
    def parse_line(self, line: str) -> list:
        """Parse a line of data."""
        pass
