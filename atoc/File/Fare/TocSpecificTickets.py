from ..AbstractFileParser import AbstractFileParser

class TocSpecificTickets(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'TICKET_CODE': 3,
            'RESTRICTION_CODE': 2,
            'RESTRICTION_FLAG': 1,
            'DIRECTION': 1,
            'TOC_ID': 2,
            'TOC_TYPE': 1,
            'END_DATE': 8,
            'START_DATE': 8,
            'SLEEPER_MKR': 1,
            'INC_EXC_STOCK': 1,
            'STOCK_LIST': 40,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TSP'
