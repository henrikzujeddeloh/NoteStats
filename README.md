# Note Stats

A program to generate some statistics on the creation and modification dates of notes.

## Usage

1. Install requirements with `pip3 install -r requirements.txt`

2. Run `note-stats.py /path/to/notes` with path to directory where the notes are stored. Sub-directories are not (yet) scanned.

### Arguments

| Argument | Description |
| --- | --- |
| `--date` | Visualizes history of note creation |
| `--month` | Shows number of notes created by month |
| `--size` | Creates histogram showing the distribution of note size (in KiB) |
| `--hist` | Creates histogram showing the distribution of days since last edit |
| `--heatmap` | Creates heatmap of the hour and day of week that notes were edited |


[TO-DO](/TODO.md)
