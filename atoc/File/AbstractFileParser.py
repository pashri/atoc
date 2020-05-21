from abc import abstractmethod
from .ParserInterface import ParserInterface
from ..IncompatibleLineException import IncompatibleLineException

class AbstractFileParser(ParserInterface):

    @abstractmethod
    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""
        pass

    @abstractmethod
    def data_map(self, line: str) -> dict:
        """Get the data map for the line."""
        pass

    def expected_length(self, line: str) -> int:
        """Get the expected line length."""
        expected_line_length = 0
        for length in self.data_map(line).values():
            expected_line_length += length
        return expected_line_length

    def parse_line(self, line: str) -> dict:
        """Parse a line of data."""
        line = line.strip()
        data_map = self.data_map(line)
        if (not data_map or self.expected_length(line) != len(line)):
            raise IncompatibleLineException
        data = {}
        data['RECORD_IDENTITY'] = self.record_identity(line)
        position = 0
        for key, length in data_map.items():
            data[key] = line[position:position+length].strip()
            position = position + length
        return data