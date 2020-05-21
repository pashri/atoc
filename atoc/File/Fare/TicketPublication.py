from ..AbstractFileParser import AbstractFileParser

class TicketPublication(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'TICKET_CODE': 3,
            'PUBLICATION_SEQUENCE': 3,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TPB'
