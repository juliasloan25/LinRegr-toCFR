AUTHOR: Julia Sloan (jsloan@caltech.edu)
DATE: August 2020

GOAL: Convert the output of the linear regression program (developed by
Kevin Huang) to the format necessary for the current continued fraction
linear regression program of the Moscato Group.

USAGE: "$python linreg_toCFR filename depth"
where 'filename' is the linear regression output file (.csv)
and depth is the depth linear regression was run at (default 2)

NOTE: Make sure the output text file does not already exist before running
i.e. when running this script multiple times in succession, delete the
output after each run