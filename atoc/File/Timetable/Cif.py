from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class Cif(AbstractMultiRecordFileParser):

    _map = {
            'HD': {
                'RECORD_IDENTITY': 'CIFHD',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'FILE_MAINFRAME_IDENTITY': 20,
                    'DATE_OF_EXTRACT': 6,
                    'TIME_OF_EXTRACT': 4,
                    'CURRENT_FILE_REF': 7,
                    'LAST_FILE_REF': 7,
                    'BLEED_OFF_UPDATE_IND': 1,
                    'VERSION': 1,
                    'USER_EXTRACT_START_DATE': 6,
                    'USER_EXTRACT_END_DATE': 6,
                    'SPARE': 20
                }
            },
            'BS': {
                'RECORD_IDENTITY': 'CIFBS',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'TRANSACTION_TYPE': 1,
                    'UNIQUE_ID': 6,
                    'DATE_RUNS_FROM': 6,
                    'DATE_RUNS_TO': 6,
                    'DAYS': 7,
                    'BHX': 1,
                    'STATUS': 1,
                    'CATEGORY': 2,
                    'TRAIN_IDENITY': 4,
                    'HEADCODE': 4,
                    'COURSE_IND': 1,
                    'SERVICE_CODE': 8,
                    'BUSSEC': 1,
                    'POWER_TYPE': 3,
                    'TIMING_LOAD': 4,
                    'SPEED': 3,
                    'OPER_CHARS': 6,
                    'CLASS': 1,
                    'SLEEPERS': 1,
                    'RESERVATIONS': 1,
                    'CONNECT_IND': 1,
                    'CATERING': 4,
                    'SERVICE_BRAND': 4,
                    'SPARE': 1,
                    'STP_INDICATOR': 1
                }
            },
            'BX': {
                'RECORD_IDENTITY': 'CIFBX',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'PREF_TRACT': 4,
                    'UIC_CODE': 5,
                    'ATOC_CODE': 2,
                    'ATS_CODE': 1,
                    'RSID': 8,
                    'DATA_SOURCE': 1,
                    'SPARE': 57
                }
            },
            'LO': {
                'RECORD_IDENTITY': 'CIFLO',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'LOCATION': 8,
                    'SCHED_DEP_TIME': 5,
                    'PUBLIC_DEP_TIME': 4,
                    'PLATFORM': 3,
                    'LINE': 3,
                    'ENG_ALLOW': 2,
                    'PATH_TIME': 2,
                    'ACTIVITY': 12,
                    'PERFORM_ALLOW': 2,
                    'SPARE': 37
                }
            },
            'LI': {
                'RECORD_IDENTITY': 'CIFLI',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'LOCATION': 8,
                    'SCHED_ARR_TIME': 5,
                    'SCHED_DEP_TIME': 5,
                    'SCHED_PASS': 5,
                    'PUBLIC_ARR_TIME': 4,
                    'PUBLIC_DEP_TIME': 4,
                    'PLATFORM': 3,
                    'LINE': 3,
                    'PATH': 3,
                    'ACTIVITY': 12,
                    'ENG_ALLOW': 2,
                    'PATH_TIME': 2,
                    'PERFORM_ALLOW': 2,
                    'SPARE': 20
                }
            },
            'CR': {
                'RECORD_IDENTITY': 'CIFCR',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'LOCATION': 8,
                    'CATEGORY': 2,
                    'TRAIN_IDENTITY': 4,
                    'HEADCODE': 4,
                    'COURSE_IND': 1,
                    'SERVICE_CODE': 8,
                    'BUSSEC': 1,
                    'POWER_TYPE': 3,
                    'TIMING_LOAD': 4,
                    'SPEED': 3,
                    'OPER_CHARS': 6,
                    'CLASS': 1,
                    'SLEEPERS': 1,
                    'RESERVATIONS': 1,
                    'CONNECT_IND': 1,
                    'CATERING': 4,
                    'SERVICE_BRAND': 4,
                    'PREF_TRACT': 4,
                    'UIC_CODE': 5,
                    'RSID': 8,
                    'SPARE': 5
                }
            },
            'LT': {
                'RECORD_IDENTITY': 'CIFLT',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'LOCATION': 8,
                    'SCHED_ARR_TIME': 5,
                    'PUBLIC_ARR_TIME': 4,
                    'PLATFORM': 3,
                    'PATH': 3,
                    'ACTIVITY': 12,
                    'SPARE': 43
                }
            },
            'TN': {
                'RECORD_IDENTITY': 'CIFTN',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'NOTE_TYPE': 1,
                    'NOTE': 77
                }
            },
            'LN': {
                'RECORD_IDENTITY': 'CIFLN',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'NOTE_TYPE': 1,
                    'NOTE': 77
                }
            },
            'AA': {
                'RECORD_IDENTITY': 'CIFAA',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'TRANSACTION_TYPE': 1,
                    'MAIN_TRAIN_UID': 6,
                    'ASSOCIATED_TRAIN_UID': 6,
                    'ASSOCIATION_START_DATE': 6,
                    'ASSOCIATION_END_DATE': 6,
                    'ASSOCIATION_DAYS': 7,
                    'ASSOCIATION_CATEGORY': 2,
                    'ASSOCIATION_DATE_IND': 1,
                    'ASSOCIATION_LOCATION': 7,
                    'BASE_LOCATION_SUFFIX': 1,
                    'ASSOC_LOCATION_SUFFIX': 1,
                    'DIAGRAM_TYPE': 1,
                    'ASSOCIATION_TYPE': 1,
                    'SPARE': 31,
                    'STP_INDICATOR': 1
                }
            },
            'TI': {
                'RECORD_IDENTITY': 'CIFTI',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'TIPLOC_CODE': 7,
                    'CAPITALS_IDENTIFICATION': 2,
                    'NALCO': 6,
                    'NLC_CHECK_CHARACTER': 1,
                    'TPS_DESCRIPTION': 26,
                    'STANOX': 5,
                    'PO_MCP_CODE': 4,
                    'CRS_CODE': 3,
                    'CAPRI_DESCRIPTION': 16,
                    'SPARE': 8
                }
            },
            'TA': {
                'RECORD_IDENTITY': 'CIFTA',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'TIPLOC_CODE': 7,
                    'CAPITALS_IDENTIFICATION': 2,
                    'NALCO': 6,
                    'NLC_CHECK_CHARACTER': 1,
                    'TPS_DESCRIPTION': 26,
                    'STANOX': 5,
                    'PO_MCP_CODE': 4,
                    'CRS_CODE': 3,
                    'CAPRI_DESCRIPTION': 16,
                    'NEW_TIPLOC': 7,
                    'SPARE': 1
                }
            },
            'TD': {
                'RECORD_IDENTITY': 'CIFTD',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'TIPLOC_CODE': 7,
                    'SPARE': 71
                }
            },
            'ZZ': {
                'RECORD_IDENTITY': 'CIFZZ',
                'DATA_MAP': {
                    'RECORD_TYPE': 2,
                    'SPARE': 78
                }
            },
        }

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[0: 2]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return self._map

    def get_prefixed_identity_map(self, prefix: str) -> dict:
        """Get the map with a prefixed identity."""

        map_ = self._map

        for type_ in map_.keys():
            map_[type_]['RECORD_IDENTITY'] = f"{prefix}{type_}"

        return map_
