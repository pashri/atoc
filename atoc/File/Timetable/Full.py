from .Cif import Cif

class Full(Cif):

    def get_map(self) -> dict:
        """Get the map for the file."""

        prefix = 'MCA'

        return self.get_prefixed_identity_map(prefix)
