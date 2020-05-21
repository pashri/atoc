from ..AbstractFileParser import AbstractFileParser

class TicketValidity(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'VALIDITY_CODE': 2,
            'END_DATE': 8,
            'START_DATE': 8,
            'DESCRIPTION': 20,
            'OUT_DAYS': 2,
            'OUT_MONTHS': 2,
            'RET_DAYS': 2,
            'RET_MONTHS': 2,
            'RET_AFTER_DAYS': 2,
            'RET_AFTER_MONTHS': 2,
            'RET_AFTER_DAY': 2,
            'BREAK_OUT': 1,
            'BREAK_RTN': 1,
            'OUT_DESCRIPTION': 14,
            'RTN_DESCRIPTION': 14,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TVL'
