from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class Tocs(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[0: 1]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'T': {
                'RECORD_IDENTITY': 'TOCT',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'TOC_ID': 2,
                    'TOC_NAME': 30,
                    'RESERVATION_SYSTEM': 8,
                    'ACTIVE_INDICATOR': 1
                }
            },
            'F': {
                'RECORD_IDENTITY': 'TOCF',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'FARE_TOC_ID': 3,
                    'TOC_ID': 2,
                    'FARE_TOC_NAME': 30
                }
            },
        }
