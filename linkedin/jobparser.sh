#!/bin/bash

# Set errexit to exit on first failure
set -e

search_term=$1
location=${2:-"Canada"}
results_wanted=${3:-30}

# Check if search_term is empty
if [ -z "$search_term" ]; then
  echo "Usage: $0 <search_term>"
  echo "Please provide a search term."
  exit 1
fi

# first run the jobparser command
python3 -m jobsparser --search-term "$search_term" --location $location --site linkedin --results-wanted $results_wanted --hours-old 24 --no-fetch-description --sleep-time 10

# take the file produced
output_file=$(ls -t ./data/*.csv | head -1)

# pass it to my custom python filtering script
python3 filter_jobparser.py $output_file

# open the file as csv
open $output_file
