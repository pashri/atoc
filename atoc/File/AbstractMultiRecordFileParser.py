from abc import abstractmethod
from .AbstractFileParser import AbstractFileParser

class AbstractMultiRecordFileParser(AbstractFileParser):

    @abstractmethod
    def record_type(self, line: str) -> str:
        """Get the record type for the line."""
        pass

    @abstractmethod
    def get_map(self) -> dict:
        """Get the map for the file."""
        pass

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""
        return self.get_from_map('RECORD_IDENTITY', line)

    def data_map(self, line: str) -> dict:
        """Get the data map for the line."""
        return self.get_from_map('DATA_MAP', line)

    def get_from_map(self, data_key, line):
        """Get data from the map."""
        record_type = self.record_type(line)
        if not record_type:
            return ''
        map_ = self.get_map()
        if record_type in map_:
            return map_[record_type][data_key]
        return ''
