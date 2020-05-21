from .NonDeliverableFares import NonDeliverableFares

class NonDeliverableFaresOverride(NonDeliverableFares):

    def record_identity(self, line: str) -> str:

        return 'NFO'
