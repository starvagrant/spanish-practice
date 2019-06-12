#!/usr/bin/env python3

def load_csv_file(file_name, columns, character_separator='\t'):
    master_list = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            entries = line.split(character_separator, columns)
            master_list.append(entries)
    return master_list

def write_csv_file(file_name, master_list, character_separator='\t'):
    with open(file_name, 'w') as f:
        for entries in master_list:
            line = ''
            for entry in entries:
                line = line + str(entry) + character_separator
            line = line.rstrip()
            line = line + '\n'
            f.write(line)

class CsvFileHandle(object):

    def __init__(self, file_name, columns, character_separator='\t'):
        """ self, <file> file_name, <int> columns <str> character_separtor='\t' """
        self.file_name = file_name
        self.columns = columns
        self.character_separator = character_separator
        self.master_list = self.load()

    def load(self):
        master_list = load_csv_file(self.file_name, self.columns, self.character_separator)
        return master_list

    def write(self):
        write_csv_file(self.file_name, self.master_list, self.character_separator)

if __name__ == '__main__':
    csv_file = CsvFileHandle('test_dir/test_list.csv', 3, '\t')
    csv_file.write()
