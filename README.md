# ATOC data parser

This parses ATOC data data from the Rail Delivery Group at [data.atoc.org](data.atoc.org) in an easy-to-use format. Be sure to read through the documentation in order to understand what the data represent.

This module is a Python version of [Michael Czolko's ATOC Feed Parser](https://github.com/mCzolko/atoc-feed-parser), originally written in PHP. It works with the Timetable feed and the Fares feed. A new parser has been added for the London Terminals Feed.

The methods are:
- `atoc.parse_file()` - Parses Timetable or Fares data, with a passed-in file path.
- `atoc.parse_files()` - Parses Timetable or Fares data, with a passed-in list of file paths.
- `atoc.parse_folder()` - Parses Timetable or Fares data, with a passed-in folder path.
- `atoc.parse_file_df()` - Like `atoc.parse_file()`, but returns a Pandas DataFrame.
- `atoc.parse_files_df()` - Like `atoc.parse_files()`, but returns a dictionary of Pandas DataFrames.
- `atoc.parse_folder_df()` - Like `atoc.parse_folder()`, but returns a dictionary of Pandas DataFrames.
- `atoc.parse_london_terminals_from_file()` - Parses the London Terminals XML (from the filename).
- `atoc.parse_london_terminals_from_string()` - Parses the London Terminals XML (from a string).

Example usage:
```python
import atoc

fares_folder = '~/RJFAF464'
times_folder = '~/ttis641'
terminals_filepath = '~/ltm_v1.4_200307.xml'

fares = atoc.parse_folder_df(fares_folder)
times = atoc.parse_folder_df(times_folder)
london_terminals = atoc.parse_london_terminals_from_file(terminals_filepath)
```
