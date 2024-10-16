# Note Stats

A program to generate various statistics on a library of notes.

## Usage

1. Install requirements with `pip3 install -r requirements.txt`
2. Run `note-stats.py /path/to/notes` with path to directory where the notes are stored. Subirectories are also scanned!

### Arguments

Can be passed with the path to notes directory to directly display visualization. A visualization can also be selected after the fact.

| Argument | Description |
| --- | --- |
| `--date` | Visualizes history of note creation |
| `--month` | Shows number of notes created by month |
| `--size` | Creates histogram showing the distribution of note size (in KiB) |
| `--hist` | Creates histogram showing the distribution of days since last edit |
| `--heatmap` | Creates heatmap of the hour and day of week that notes were edited |


## Configuration

### Scanned file types
In `modules/constants.py`, `INCLUDE_EXT` can be set to include desired file types to be scanned.
Here the timezone can also be set for correct date-time parsing.
