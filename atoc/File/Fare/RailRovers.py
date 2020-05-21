from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class RailRovers(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[0: 1]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'R': {
                'RECORD_IDENTITY': 'TRRR',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'ROVER_CODE': 3,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'QUOTE_DATE': 8,
                    'DESCRIPTION': 30,
                    'TICKET_DESC': 15,
                    'CAPRI_TICKET_CODE': 3,
                    'ROVER_ACCOUNTING_CODE': 4,
                    'DAYS_TRAVEL': 3,
                    'MONTHS_VALID': 2,
                    'DAYS_VALID': 2
                }
            },
            'P': {
                'RECORD_IDENTITY': 'TRRP',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'ROVER_CODE': 3,
                    'END_DATE': 8,
                    'RAILCARD_CODE': 3,
                    'ROVER_CLASS': 1,
                    'ADULT_FARE': 8,
                    'CHILD_FARE': 8,
                    'RESTRICTION_CODE': 2,
                }
            },
        }
