#!/bin/bash

pip3 install beautifulsoup4

if [ ! -f ./spreadsheet_id.txt ]; then
    echo "Put your spreadsheet ID here" > spreadsheet_id.txt
fi