# binchecker
Uses public BIN database APIs to scrape data on supplied BIN numbers.

#Usage
binchecker [input file] [output file]

Input file is a CSV (Comma Separated Values) file, which contain BIN numbers in a given column.
Output file is a CSV file containing any data returned by the public API.

Output file will be overwritten if it exists and will be created if it does not.
