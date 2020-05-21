from .Cif import Cif

class ManualTrains(Cif):

    def get_map(self) -> dict:
        """Get the map for the file."""

        prefix = 'ZTR'

        return self.get_prefixed_identity_map(prefix)
