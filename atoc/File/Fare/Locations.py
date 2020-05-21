from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class Locations(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[1: 2]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'L': {
                'RECORD_IDENTITY': 'LOCL',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'UIC_CODE': 7,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'QUOTE_DATE': 8,
                    'ADMIN_AREA_CODE': 3,
                    'NLC_CODE': 4,
                    'DESCRIPTION': 16,
                    'CRS_CODE': 3,
                    'RESV_CODE': 5,
                    'ERS_COUNTRY': 2,
                    'ERS_CODE': 3,
                    'FARE_GROUP': 6,
                    'COUNTY': 2,
                    'PTE_CODE': 2,
                    'ZONE_NO': 4,
                    'ZONE_IND': 2,
                    'REGION': 1,
                    'HIERARCHY': 1,
                    'CC_DESC_OUT': 41,
                    'CC_DESC_RTN': 16,
                    'ATB_DESC_OUT': 60,
                    'ATB_DESC_RTN': 30,
                    'SPECIAL_FACILITIES': 26,
                    'LUL_DIRECTION_IND': 1,
                    'LUL_UTS_MODE': 1,
                    'LUL_ZONE_1': 1,
                    'LUL_ZONE_2': 1,
                    'LUL_ZONE_3': 1,
                    'LUL_ZONE_4': 1,
                    'LUL_ZONE_5': 1,
                    'LUL_ZONE_6': 1,
                    'LUL_UTS_LONDON_STN': 1,
                    'UTS_CODE': 3,
                    'UTS_A_CODE': 3,
                    'UTS_PTR_BIAS': 1,
                    'UTS_OFFSET': 1,
                    'UTS_NORTH': 3,
                    'UTS_EAST': 3,
                    'UTS_SOUTH': 3,
                    'UTS_WEST': 3
                }
            },
            'A': {
                'RECORD_IDENTITY': 'LOCA',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'UIC_CODE': 7,
                    'END_DATE': 8,
                    'ASSOC_UIC_CODE': 7,
                    'ASSOC_CRS_CODE': 3
                }
            },
            'R': {
                'RECORD_IDENTITY': 'LOCR',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'UIC_CODE': 7,
                    'RAILCARD_CODE': 3,
                    'END_DATE': 8
                }
            },
            'G': {
                'RECORD_IDENTITY': 'LOCG',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'GROUP_UIC_CODE': 7,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'QUOTE_DATE': 8,
                    'DESCRIPTION': 16,
                    'ERS_COUNTRY': 2,
                    'ERS_CODE': 3
                }
            },
            'M': {
                'RECORD_IDENTITY': 'LOCM',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'GROUP_UIC_CODE': 7,
                    'END_DATE': 8,
                    'MEMBER_UIC_CODE': 7,
                    'MEMBER_CRS_CODE': 3
                }
            },
            'S': {
                'RECORD_IDENTITY': 'LOCS',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'GROUP_UIC_CODE': 7,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'DESCRIPTION': 16
                }
            },
        }
