from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class PrintFormats(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[1: 2]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'P': {
                'RECORD_IDENTITY': 'TPNP',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'SUPPLEMENT_CODE': 3,
                    'RAILCARD_CODE': 3,
                    'REV_CODE': 3,
                    'NON_REV_CODE': 3,
                    'TEXT_CODE_1': 3,
                    'TEXT_CODE_2': 3,
                    'TEXT_CODE_3': 3,
                    'TEXT_CODE_4': 3,
                    'TEXT_CODE_5': 3
                }
            },
            'T': {
                'RECORD_IDENTITY': 'TPNT',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'TEXT_CODE': 3,
                    'FREE_TEXT': 72
                }
            },
        }
