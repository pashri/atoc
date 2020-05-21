from ..AbstractFileParser import AbstractFileParser

class RoundingRules(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'RULE_NO': 2,
            'END_DATE': 8,
            'RULE_INDEX': 2,
            'START_DATE': 8,
            'MAX_AMOUNT': 8,
            'ROUND_AMOUNT': 8,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'FRR'
