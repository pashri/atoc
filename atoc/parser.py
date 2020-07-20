import os
from .Factory import Factory, InvalidFileException

def parse_folder(folder_path: str) -> dict:
    """Parses a folder."""

    filenames = os.listdir(folder_path)
    filepaths = [os.path.join(folder_path, filename) for filename in filenames]
    data = parse_files(filepaths)

    return data

def parse_files(filepaths: str) -> dict:
    """Parses a list of files."""

    data = {}

    for filepath in filepaths:

        try:
            parsed_data = parse_file(filepath)
            data.update(parsed_data)

        except InvalidFileException:
            pass

    return data

def parse_file(filepath: str) -> dict:
    """Parses a file."""

    data = {}

    Parser = Factory().get_parser(filepath)

    with open(filepath, 'r') as f:

        for line in f.readlines():

            parsed_line = None

            try:
                parsed_line = Parser.parse_line(line)

            except KeyboardInterrupt:
                raise

            except:
                pass

            if parsed_line is not None:
                record_identity = parsed_line['RECORD_IDENTITY']
                if record_identity not in data:
                    data[record_identity] = []
                data[record_identity].append(parsed_line)

    return data

def parse_folder_df(folder_path: str) -> dict:
    """Parses a folder and returns a dictionary of Pandas DataFrames."""

    filenames = os.listdir(folder_path)
    filepaths = [os.path.join(folder_path, filename) for filename in filenames]
    dfs = parse_files_df(filepaths)

    return dfs

def parse_files_df(filepaths: str) -> dict:
    """Parses a list of files and returns a dictionary of Pandas DataFrames."""

    import pandas

    data = parse_files(filepaths)
    dfs = {k: pandas.DataFrame(v) for k, v in data.items()}

    return dfs

def parse_file_df(filepath: str):
    """Parses a file and returns a Pandas DataFrame."""

    import pandas

    data = parse_file(filepath)
    df = pandas.DataFrame(data)

    return df
