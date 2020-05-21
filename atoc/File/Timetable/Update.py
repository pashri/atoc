from .Cif import Cif

class Update(Cif):

    def get_map(self) -> dict:
        """Get the map for the file."""

        prefix = 'CFA'

        return self.get_prefixed_identity_map(prefix)
