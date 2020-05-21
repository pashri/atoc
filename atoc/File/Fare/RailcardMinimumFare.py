from ..AbstractFileParser import AbstractFileParser

class RailcardMinimumFare(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'RAILCARD_CODE': 3,
            'TICKET_CODE': 3,
            'END_DATE': 8,
            'START_DATE': 8,
            'MINIMUM_FARE': 8,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'RCM'
