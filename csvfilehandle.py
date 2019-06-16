#!/usr/bin/env python3

import csv

class CsvFileHandle():

    def __init__(self,file_name='example.csv'):
        self.file_name=file_name
        self.word_list = []

    def read(self, file_name='example.csv'):
        with open('example.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                print(f'\t{row["spanish"]} means "{row["english"]}" in English. You\'ve guessed this {row["correct_guesses"]} times')
                line_count += 1
                print(f'Processed {line_count} lines.')

    def write(self, file_name='example.csv'):
        with open(file_name, mode='w') as csv_file:
            fieldnames = ['spanish', 'english', 'correct_guesses']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'spanish': 'ayudar', 'english': 'to help', 'correct_guesses': '0'})
            writer.writerow({'spanish': 'buscar', 'english': 'to search', 'correct_guesses': '0'})

    def read_in_list(self, file_name='example.csv'):
        with open('example.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.word_list.append(row)

    def write_in_list(self, file_name='example.csv'):
        with open('example.csv', 'w') as csv_file:
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
    csvfile = CsvFileHandle()
    csvfile.read_in_list()
    csvfile.write_in_list()
