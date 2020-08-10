# AUTHOR: Julia Sloan (jsloan@caltech.edu)
# DATE: August 2020
# USAGE: python linreg_toCFR filename depth
# USAGE: make sure output text file does not already exist before running

import csv
import os
import sys
import itertools as it


# convert a csv file to a tab-delimited txt file with the same values
def csv_to_txt(file):
    # open linear regression output (csv file)
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # initialize new txt file
        newfile = file[:-4] + '.txt'

        for line in csv_reader:
            with open(newfile, 'a', newline='\n') as new_txt:
                txt_writer = csv.writer(new_txt, delimiter='\t')
                # write each row of the csv to the txt file
                txt_writer.writerow(line)


# add a line to the beginning of a tab-delimited txt file
def prepend_line(file, line):
    with open(file, 'a') as txt_file:
        txt_file.write(line)


# access command-line arguments
file = sys.argv[1]
depth = int(sys.argv[2])

# m: number of terms used to represent solution at this depth
m = str(2*depth + 1)

# n: number of coefficients and constant (num cols in csv)
with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    n = str(len(next(reader))) # number of columns in csv
    del reader

# append special first line to txt file
new_file = file[:-4] + '.txt'
first_line = m + '\t' + n + '\n'
prepend_line(new_file, first_line)

# convert csv file to txt file for output
csv_to_txt(file)

print("Done! Check the directory of", file, "for the output.")
