#!/usr/bin/env python3

import csv
from collections import OrderedDict

class CsvFileHandle():

    def __init__(self,file_name=''):
        self.file_name=file_name
        self.word_list = []

    def read(self, file_name=''):
        if file_name == '':
            file_name=self.file_name
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.word_list.append(row)

    def write(self, file_name=''):
        if file_name == '':
            file_name=self.file_name
        with open(file_name, 'w') as csv_file:
            if len(self.word_list) == 0:
                print('Nothing to Write')
                return

            fieldnames = []
            for key in self.word_list[0].keys():
                fieldnames.append(key)

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.word_list:
                print(entry)
                writer.writerow(entry)

if __name__ == '__main__':
    csvfile = CsvFileHandle('example.csv')
    csvfile.read()
    csvfile.write()
