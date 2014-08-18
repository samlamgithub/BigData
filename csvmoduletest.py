#!/usr/bin/env python

# coding: utf-8

import csv # import csv module

csvfile = open('csv_test.csv', 'wb')

writer = csv.writer(csvfile, delimiter = ',')

writer.writerow(['Column1', 'Column2', 'Column3'])

lines = [range(3) for i in range(5)]

print lines

for line in lines:
    writer.writerow(line)

csvfile.close()

#read csv file

csvfile = open('csv_test.csv', 'rb')

reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close()
