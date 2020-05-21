from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class Restrictions(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[1: 3]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'RD': {
                'RECORD_IDENTITY': 'RSTRD',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'START_DATE': 8,
                    'END_DATE': 8
                }
            },
            'RH': {
                'RECORD_IDENTITY': 'RSTRH',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'DESCRIPTION': 30,
                    'DESC_OUT': 50,
                    'DESC_RTN': 50,
                    'TYPE_OUT': 1,
                    'TYPE_RTN': 1,
                    'CHANGE_IND': 1
                }
            },
            'HD': {
                'RECORD_IDENTITY': 'RSTHD',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'DATE_FROM': 4,
                    'DATE_TO': 4,
                    'DAYS': 7
                }
            },
            'HL': {
                'RECORD_IDENTITY': 'RSTHL',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'LOCATION_CRS_CODE': 3
                }
            },
            'HC': {
                'RECORD_IDENTITY': 'RSTHC',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'ALLOWED_CHANGE': 3
                }
            },
            'HA': {
                'RECORD_IDENTITY': 'RSTHA',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'ADDITIONAL_RESTRICTION': 2,
                    'ORIGIN': 3,
                    'DESTINATION': 3
                }
            },
            'TR': {
                'RECORD_IDENTITY': 'RSTTR',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'SEQUENCE_NO': 4,
                    'OUT_RET': 1,
                    'TIME_FROM': 4,
                    'TIME_TO': 4,
                    'ARR_DEP_VIA': 1,
                    'LOCATION': 3,
                    'RSTR_TYPE': 1,
                    'TRAIN_TYPE': 1,
                    'MIN_FARE_FLAG': 1
                }
            },
            'TD': {
                'RECORD_IDENTITY': 'RSTTD',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'SEQUENCE_NO': 4,
                    'OUT_RET': 1,
                    'DATE_FROM': 4,
                    'DATE_TO': 4,
                    'DAYS': 7
                }
            },
            'TT': {
                'RECORD_IDENTITY': 'RSTTT',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'SEQUENCE_NO': 4,
                    'OUT_RET': 1,
                    'TOC_CODE': 2
                }
            },
            'TP': {
                'RECORD_IDENTITY': 'RSTTP',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'SEQUENCE_NO': 4,
                    'OUT_RET': 1,
                    'BARRED_CLASS': 1,
                    'BARRED_TICKETS': 1,
                    'BARRED_SEASONS': 1,
                    'BARRED_FIRST': 1,
                    'FROM_LOCATION': 3,
                    'TO_LOCATION': 3
                }
            },
            'TE': {
                'RECORD_IDENTITY': 'RSTTE',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'SEQUENCE_NO': 4,
                    'OUT_RET': 1,
                    'PASS_EXCEPTION': 1
                }
            },
            'SR': {
                'RECORD_IDENTITY': 'RSTSR',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'TRAIN_NO': 6,
                    'OUT_RET': 1,
                    'QUOTA_IND': 1,
                    'SLEEPER_IND': 1
                }
            },
            'SD': {
                'RECORD_IDENTITY': 'RSTSD',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'TRAIN_NO': 6,
                    'OUT_RET': 1,
                    'DATE_FROM': 4,
                    'DATE_TO': 4,
                    'DAYS': 7
                }
            },
            'SQ': {
                'RECORD_IDENTITY': 'RSTSQ',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'TRAIN_NO': 6,
                    'OUT_RET': 1,
                    'LOCATION': 3,
                    'QUOTA_IND': 1,
                    'ARR_DEP': 1
                }
            },
            'SP': {
                'RECORD_IDENTITY': 'RSTSP',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'TRAIN_NO': 6,
                    'OUT_RET': 1,
                    'BARRED_CLASS': 1,
                    'BARRED_TICKETS': 1,
                    'BARRED_SEASONS': 1,
                    'BARRED_FIRST': 1,
                    'FROM_LOCATION': 3,
                    'TO_LOCATION': 3
                }
            },
            'SE': {
                'RECORD_IDENTITY': 'RSTSE',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RESTRICTION_CODE': 2,
                    'TRAIN_NO': 6,
                    'OUT_RET': 1,
                    'PASS_EXCEPTION': 1
                }
            },
            'RR': {
                'RECORD_IDENTITY': 'RSTRR',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'RAILCARD_CODE': 3,
                    'SEQUENCE_NO': 4,
                    'TICKET_CODE': 3,
                    'ROUTE_CODE': 5,
                    'LOCATION': 3,
                    'RESTRICTION_CODE': 2,
                    'TOTAL_BAN': 1
                }
            },
            'EC': {
                'RECORD_IDENTITY': 'RSTEC',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'EXCEPTION_CODE': 1,
                    'DESCRIPTION': 50
                }
            },
            'CA': {
                'RECORD_IDENTITY': 'RSTCA',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 2,
                    'CF_MKR': 1,
                    'TICKET_CODE': 3,
                    'CAL_TYPE': 1,
                    'ROUTE_CODE': 5,
                    'COUNTRY_CODE': 1,
                    'DATE_FROM': 4,
                    'DATE_TO': 4,
                    'DAYS': 7
                }
            }
        }
