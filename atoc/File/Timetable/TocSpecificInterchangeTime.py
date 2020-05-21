from ..ParserInterface import ParserInterface
from ...IncompatibleLineException import IncompatibleLineException

class TocSpecificInterchangeTime(ParserInterface):

    map_ = [
        'STATION_CODE',
        'ARRIVING_TRAIN_TOC',
        'DEPARTING_TRAIN_TOC',
        'MINIMUM_INTERCHANGE_TIME',
        'COMMENTS'
    ]

    def parse_line(self, line: str) -> dict:
        """Parse a line of data."""

        values = line.split(',', 5)

        if len(values) == 1 and not values[0]:
            raise IncompatibleLineException

        keyValues = {}

        for index, key in enumerate(self.map_):
            keyValues[key] = values[index].strip()

        keyValues['RECORD_IDENTITY'] = 'TSI'

        return keyValues
