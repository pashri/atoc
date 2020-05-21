from ..AbstractMultiRecordFileParser import AbstractMultiRecordFileParser

class Flow(AbstractMultiRecordFileParser):

    def record_type(self, line: str) -> str:
        """Get the record type for the line."""

        return line[1: 2]

    def get_map(self) -> dict:
        """Get the map for the file."""

        return {
            'F': {
                'RECORD_IDENTITY': 'FFLF',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'ORIGIN_CODE': 4,
                    'DESTINATION_CODE': 4,
                    'ROUTE_CODE': 5,
                    'STATUS_CODE': 3,
                    'USAGE_CODE': 1,
                    'DIRECTION': 1,
                    'END_DATE': 8,
                    'START_DATE': 8,
                    'TOC': 3,
                    'CROSS_LONDON_IND': 1,
                    'NS_DISC_IND': 1,
                    'PUBLICATON_IND': 1,
                    'FLOW_ID': 7
                }
            },
            'T': {
                'RECORD_IDENTITY': 'FFLT',
                'DATA_MAP': {
                    'UPDATE_MARKER': 1,
                    'RECORD_TYPE': 1,
                    'FLOW_ID': 7,
                    'TICKET_CODE': 3,
                    'FARE': 8,
                    'RESTRICTION_CODE': 2
                }
            },
        }
