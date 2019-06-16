#!/usr/bin/env python3

import unittest
import vocabulario
import os
from collections import OrderedDict
from csvfilehandle import CsvFileHandle

def clean_test_dir(directory='test_dir'):
        scan = os.scandir(directory)
        for filename in scan:
            os.remove(filename)

def write_test_file(file_name='test_dir/test.csv'):
        csv_file = CsvFileHandle(file_name)

        # dict1['corrected_guess'] > dict2['corrected_guess']
        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='3')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='1')
        test_list = [dict1,dict2]

        csv_file.write(test_list)

class Tests(unittest.TestCase):
    def test_keymap(self):
        user_string1= """'a'e'i'o'u:u~n!!??"""
        user_string2= """"a"e"i"o"u:u~n!!??"""
        target_string = "áéíóúüñ¡¿"
        loop = vocabulario.SpanishCmd()

        self.assertEqual(loop.keymap(user_string1),target_string)
        self.assertEqual(loop.keymap(user_string2),target_string)

    def test_load_word_list(self):
        clean_test_dir()
        write_test_file()

        loop = vocabulario.SpanishCmd('test_dir/test.csv')
        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='0')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='0')
        expected = [dict1,dict2]

        self.assertListEqual(loop.word_list, expected)

    def test_write_word_list(self):
        clean_test_dir()
        write_test_file()

        loop = vocabulario.SpanishCmd('test_dir/test.csv')
        loop.word_list[0]['correct_guesses'] = 8
        loop.write_word_list()

        csv_file = CsvFileHandle('test_dir/test.csv')

        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='8')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='1')
        expected = [dict1,dict2]

        self.assertListEqual(expected, csv_file.read())

    def test_prepare_quiz(self):
        clean_test_dir()
        write_test_file()

        loop = vocabulario.SpanishCmd('test_dir/test.csv')
        loop.prepare_quiz()

        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='3')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='1')
        expected = [dict1,dict2]

        self.assertEqual(expected, loop.word_list)

    def test_word_compare(self):
        loop = vocabulario.SpanishCmd()
        boolean = loop.compare("'ANIMO", "ánimo")
        self.assertTrue(boolean)

    def test_word_sort(self):
        clean_test_dir()
        write_test_file()

        loop = vocabulario.SpanishCmd('test_dir/test.csv')
        loop.sort_word_list()
        dict1 = OrderedDict(spanish='ayudar',english='to help',correct_guesses='3')
        dict2 = OrderedDict(spanish='buscar',english='to search',correct_guesses='1')
        expected = [dict1,dict2]

        self.assertListEqual(loop.word_list, expected)

unittest.main()
