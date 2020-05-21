from ..AbstractFileParser import AbstractFileParser

class ClassLegends(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'CLASS': 1,
            'END_DATE': 8,
            'START_DATE': 8,
            'ATB_DESC': 8,
            'CC_DESC': 3,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TCL'
