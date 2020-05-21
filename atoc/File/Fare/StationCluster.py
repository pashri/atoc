from ..AbstractFileParser import AbstractFileParser

class StationCluster(AbstractFileParser):

    def data_map(self, line: str) -> dict:
        """Get the data map for the file."""

        return {
            'UPDATE_MARKER': 1,
            'CLUSTER_ID': 4,
            'CLUSTER_NLC': 4,
            'END_DATE': 8,
            'START_DATE': 8
        }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'FSC'
