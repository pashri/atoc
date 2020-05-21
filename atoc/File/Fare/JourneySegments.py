from ..AbstractFileParser import AbstractFileParser

class JourneySegments(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'JS_CODE': 3,
            'END_DATE': 8,
            'START_DATE': 8,
            'LINE': 3,
            'START': 2,
            'END': 2,
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'TJS'
