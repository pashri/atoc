from ..AbstractFileParser import AbstractFileParser

class AdvancePurchaseTickets(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'TICKET_CODE': 3,
            'RESTRICTION_CODE': 2,
            'RESTRICTION_FLAG': 1,
            'TOC_ID': 2,
            'END_DATE': 8,
            'START_DATE': 8,
            'CHECK_TYPE': 1,
            'AP_DATA': 8,
            'BOOKING_TIME': 4,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TAP'
