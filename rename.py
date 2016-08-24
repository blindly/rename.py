#!/usr/bin/env python
import os

path =  os.getcwd()
filenames = os.listdir(path)

count = 0

for filename in filenames:
    filename_array = filename.split('-')
    if len(filename_array) > 1:
        new_filename = filename_array[0]
        os.rename(filename, new_filename)
        count = count + 1

print("%s files have been renamed" % count)
