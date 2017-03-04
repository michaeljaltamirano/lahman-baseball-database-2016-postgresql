# Move file into csv folder and cd into before running from terminal like so:
# $ python3 add_id.py AllstarFull.csv Appearances.csv etc.
#
# Output assumes you create a new folder for your output to populate,
# Which will then be moved to the main "csv" repository, replacing the
# existing csv files. The script does not automatically overwrite the files.

import csv
from sys import argv
import os.path

script, *files = argv

new_path = 'path/to/new/csv/folder'

for file in files:
    filename = file

    full_path = os.path.join(new_path, filename)

    with open(file, 'r') as input, open(full_path, 'w') as output:
        reader = csv.reader(input)
        writer = csv.writer(output, delimiter = ',')

        writer.writerow(['id'] + next(reader))

        writer.writerows([i] + row for i, row in enumerate(reader, 1))
