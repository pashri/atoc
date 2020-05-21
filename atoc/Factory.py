import pathlib
from typing import Type
from .ParserFactoryInterface import ParserFactoryInterface
from .InvalidFileException import InvalidFileException
from .File import Fare, Timetable

class Factory(ParserFactoryInterface):

    parser_map = {
        'ffl': ('Fare', 'Flow'),
        'fsc': ('Fare', 'StationCluster'),
        'ndf': ('Fare', 'NonDeliverableFares'),
        'nfo': ('Fare', 'NonDeliverableFaresOverride'),
        'fns': ('Fare', 'NonStandardDiscounts'),
        'tty': ('Fare', 'TicketTypes'),
        'tvl': ('Fare', 'TicketValidity'),
        'tjs': ('Fare', 'JourneySegments'),
        'tpb': ('Fare', 'TicketPublication'),
        'tpn': ('Fare', 'PrintFormats'),
        'tcl': ('Fare', 'ClassLegends'),
        'trr': ('Fare', 'RailRovers'),
        'tpk': ('Fare', 'Package'),
        'sup': ('Fare', 'Suppliments'),
        'rlc': ('Fare', 'Railcards'),
        'rcm': ('Fare', 'RailcardMinimumFare'),
        'dis': ('Fare', 'StatusDiscounts'),
        'frr': ('Fare', 'RoundingRules'),
        'rst': ('Fare', 'Restrictions'),
        'loc': ('Fare', 'Locations'),
        'rte': ('Fare', 'Routes'),
        'toc': ('Fare', 'Tocs'),
        'tsp': ('Fare', 'TocSpecificTickets'),
        'tap': ('Fare', 'AdvancePurchaseTickets'),
        'mca': ('Timetable', 'Full'),
        'cfa': ('Timetable', 'Update'),
        'ztr': ('Timetable', 'ManualTrains'),
        'flf': ('Timetable', 'FixedLinks'),
        'alf': ('Timetable', 'AdditionalFixedLinks'),
        'msn': ('Timetable', 'MasterStationNames'),
        'tsi': ('Timetable', 'TocSpecificInterchangeTime'),
    }

    def get_parser(self, filename: str) -> Type:
        """Get a parser instance for the file."""

        extension = pathlib.PurePath(filename).suffix

        if len(extension) < 1:
            raise InvalidFileException('File has no extension')

        elif extension[1:].lower() not in self.parser_map:
            raise InvalidFileException(f'No parser for file {filename}')

        module_name, parser_name = self.parser_map[extension[1:].lower()]
        FileParser = getattr(globals()[module_name], parser_name)

        return FileParser()
