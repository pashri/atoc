from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class StatusDiscounts(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[0: 1]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'S': {
                'RECORD_IDENTITY': 'DISS',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'STATUS_CODE': 3,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'ATB_DESC': 5,
                    'CC_DESC': 5,
                    'UTS_CODE': 1,
                    'FIRST_SINGLE_MAX_FLAT': 8,
                    'FIRST_RETURN_MAX_FLAT': 8,
                    'STD_SINGLE_MAX_FLAT': 8,
                    'STD_RETURN_MAX_FLAT': 8,
                    'FIRST_LOWER_MIN': 8,
                    'FIRST_HIGHER_MIN': 8,
                    'STD_LOWER_MIN': 8,
                    'STD_HIGHER_MIN': 8,
                    'FS_MKR': 1,
                    'FR_MKR': 1,
                    'SS_MKR': 1,
                    'SR_MKR': 1
                }
            },
            'D': {
                'RECORD_IDENTITY': 'DISD',
                'DATA_MAP': {
                    'RECORD_TYPE': 1,
                    'STATUS_CODE': 3,
                    'END_DATE': 8,
                    'DISCOUNT_CATEGORY': 2,
                    'DISCOUNT_INDICATOR': 1,
                    'DISCOUNT_PERCENTAGE': 3
                }
            },
        }
