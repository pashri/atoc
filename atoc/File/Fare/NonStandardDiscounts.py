from ..AbstractFileParser import AbstractFileParser

class NonStandardDiscounts(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'UPDATE_MARKER': 1,
            'ORIGIN_CODE': 4,
            'DESTINATION_CODE': 4,
            'ROUTE_CODE': 5,
            'RAILCARD_CODE': 3,
            'TICKET_CODE': 3,
            'END_DATE': 8,
            'START_DATE': 8,
            'QUOTE_DATE': 8,
            'USE_NLC': 4,
            'ADULT_NODIS_FLAG': 1,
            'ADULT_ADD_ON_AMOUNT': 8,
            'ADULT_REBOOK_FLAG': 1,
            'CHILD_NODIS_FLAG': 1,
            'CHILD_ADD_ON_AMOUNT': 8,
            'CHILD_REBOOK_FLAG': 1
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'FNS'
