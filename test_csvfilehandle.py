#!/usr/bin/env python3

import os
import unittest
from csvfilehandle import CsvFileHandle
from collections import OrderedDict

def clean_test_dir(directory='test_dir'):
    scan = os.scandir('test_dir')
    for filename in scan:
        os.remove(filename)

def write_example_csv(directory='test_dir'):
    clean_test_dir(directory)
    with open('test_dir/example.csv', 'w') as f:
        f.write('spanish,english,correct_guesses\n')
        f.write('ayudar,to help,0\n')
        f.write('buscar,to search,0\n')

class test_csvfilehandle(unittest.TestCase):

    def test_csvfilehandle_read(self):
        clean_test_dir()
        write_example_csv()
        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='0')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='0')
        expected_list = [dict1,dict2]

        csv_file = CsvFileHandle('test_dir/example.csv')
        csv_list = csv_file.read()
        self.assertListEqual(expected_list, csv_list)

    def test_csvfilehandle_write(self):
        clean_test_dir()
        write_example_csv()
        csv_file = CsvFileHandle('test_dir/example.csv')
        csv_list = csv_file.read()

        clean_test_dir()
        csv_file.write(csv_list)

        with open('test_dir/example.csv', 'r') as f:
            text = f.read()

        expected = 'spanish,english,correct_guesses\nayudar,to help,0\nbuscar,to search,0\n'
        self.assertEqual(expected, text)

unittest.main()
