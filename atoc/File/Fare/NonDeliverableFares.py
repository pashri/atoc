from ..AbstractFileParser import AbstractFileParser

class NonDeliverableFares(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'UPDATE_MARKER': 1,
            'ORIGIN_CODE': 4,
            'DESTINATION_CODE': 4,
            'ROUTE_CODE': 5,
            'RAILCARD_CODE': 3,
            'TICKET_CODE': 3,
            'ND_RECORD_TYPE': 1,
            'END_DATE': 8,
            'START_DATE': 8,
            'QUOTE_DATE': 8,
            'SUPPRESS_MKR': 1,
            'ADULT_FARE': 8,
            'CHILD_FARE': 8,
            'RESTRICTION_CODE': 2,
            'COMPOSITE_INDICATOR': 1,
            'CROSS_LONDON_IND': 1,
            'PS_IND': 1
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'NDF'
