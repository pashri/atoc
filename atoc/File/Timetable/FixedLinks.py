from ..AbstractFileParser import AbstractFileParser

class FixedLinks(AbstractFileParser):

    map3 = {
        'LINK': 17,
        'MODE': 3,
        'BETWEEN': 9,
        'ORIGIN': 3,
        'AND': 5,
        'DESTINATION': 3,
        'IN': 4,
        'TIME': 3,
        'MINUTES': 8,
    }

    map4 = {
        'LINK': 17,
        'MODE': 4,
        'BETWEEN': 9,
        'ORIGIN': 3,
        'AND': 5,
        'DESTINATION': 3,
        'IN': 4,
        'TIME': 3,
        'MINUTES': 8,
    }

    map5 = {
        'LINK': 17,
        'MODE': 5,
        'BETWEEN': 9,
        'ORIGIN': 3,
        'AND': 5,
        'DESTINATION': 3,
        'IN': 4,
        'TIME': 3,
        'MINUTES': 8,
    }

    map8 = {
        'LINK': 17,
        'MODE': 8,
        'BETWEEN': 9,
        'ORIGIN': 3,
        'AND': 5,
        'DESTINATION': 3,
        'IN': 4,
        'TIME': 3,
        'MINUTES': 8,
    }

    def record_identity(self, line: str) -> str:
        """Get the record identity for the line."""

        return 'FLF'


    def data_map(self, line: str) -> dict:
        """Get the data map for the line."""

        split_line = line[17:25].split(' ')
        mode = split_line  # The PHP version resets a pointer here
        mode_length = len(mode)
        map_ = f"map{mode_length}"

        if not hasattr(self, map_):
            return ''

        return getattr(self, map_)
