# Shell Kicker

Run a local script if a Google Sheet contains a particular string.

## Getting started

1. Run `initialise.sh`
1. This will create the file `spreadsheet_id.txt`. Paste your Google Sheet ID in here. Remove any empty lines from this file.
1. Replace the contents of `found_script.sh` with the script to run when your search text is found.
1. Replace the contents of `not_found_script.sh` with the script to run when your search text is _not_ found.
1. Run `python3 shell_kicker.py`

## To change the search text

Change the value of the variable `to_search_for` in the `shell_kicker.py` script.

## Newline characters

If you are having issues with line endings, run this `dos2unix ./initialise.sh ./found_script.sh ./not_found_script.sh`
