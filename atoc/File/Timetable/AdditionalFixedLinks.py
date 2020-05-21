from ..ParserInterface import ParserInterface
from ...IncompatibleLineException import IncompatibleLineException

class AdditionalFixedLinks(ParserInterface):

    def parse_line(self, line: str) -> dict:
        """Parse a line of data."""

        pairs = line.split(',')

        if len(pairs) == 1 and not pairs[0]:
            raise IncompatibleLineException

        keyValues = {}

        for pair in pairs:

            parts = pair.lstrip().split('=', 2)

            if len(parts) == 1 and not parts[0]:
                raise IncompatibleLineException

            keyValues[parts[0]] = parts[1].strip()


        keyValues['RECORD_IDENTITY'] = 'ALF'

        return keyValues
