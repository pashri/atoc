from xml.etree import ElementTree

def parse_london_terminals_from_file(filepath: str) -> dict:
    """Parses the London Terminals Feed XML from file."""

    xml = ElementTree.parse(filepath)
    data = parse_london_terminals(xml)

    return data

def parse_london_terminals_from_string(xmlstring: str) -> dict:

    xml = ElementTree.fromstring(xmlstring)
    data = parse_london_terminals(xml)

    return data

def parse_london_terminals(xml: ElementTree) -> dict:
    """Parses the London Terminals Feed XML element tree."""

    data = {}

    for station in xml.getroot().find('Stations'):

        name = station.find('CrsCode').text
        data[name] = {}

        for LondonTerminalsMapping in station.find('LondonTerminalsMappings'):

            fare_route = LondonTerminalsMapping.find('FareRoute').text
            start_date = LondonTerminalsMapping.find('StartDate').text
            end_date = LondonTerminalsMapping.find('EndDate').text
            terminals = [t.text for t in LondonTerminalsMapping.find('LondonTerminals')]

            data[name][fare_route] = {
                'StartDate': start_date,
                'EndDate': end_date,
                'Terminals': terminals
            }

    return data