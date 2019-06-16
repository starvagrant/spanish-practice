#!/usr/bin/env python3

import unittest
import vocabulario
import os

def clean_test_dir(directory='test_dir'):
        scan = os.scandir(directory)
        for filename in scan:
            os.remove(filename)

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
        with open('test_dir/test_list.csv', 'w') as f:
            f.write('answer	repuesta	0')

        loop = vocabulario.SpanishCmd('test_dir/test_list.csv')
        expected = [['answer','repuesta',0]]
        self.assertListEqual(loop.word_list, expected)

    def test_write_word_list(self):
        clean_test_dir()
        with open('test_dir/test_list.csv', 'w') as f:
            f.write('answer	repuesta	0')

        loop = vocabulario.SpanishCmd('test_dir/test_list.csv')
        loop.word_list[0][2] = 8
        loop.write_word_list('test_dir/test_list.csv')

        with open('test_dir/test_list.csv', 'r') as f:
            expected = f.readline().rstrip()

        self.assertEqual(expected, 'answer	repuesta	8')

    def test_prepare_quiz(self):
        clean_test_dir()
        with open('test_dir/countedtest_list.csv', 'w') as f:
            f.write('answer	repuesta	3\n')
            f.write('buscar	to search	1\n')

        loop = vocabulario.SpanishCmd('test_dir/countedtest_list.csv')
        loop.prepare_quiz()
        expected = [['answer','repuesta',3],['buscar','to search', 1]]
        self.assertEqual(expected, loop.word_list)

    def test_word_compare(self):
        loop = vocabulario.SpanishCmd()
        boolean = loop.compare("'ANIMO", "ánimo")
        self.assertTrue(boolean)

    def test_word_sort(self):
        clean_test_dir()
        with open('test_dir/countedtest_list.csv', 'w') as f:
            f.write('answer	repuesta	3\n')
            f.write('buscar	to search	1\n')

        loop = vocabulario.SpanishCmd('test_dir/countedtest_list.csv')
        loop.sort_word_list()
        expected = [['buscar','to search',1],['answer','repuesta',3]]
        self.assertListEqual(loop.word_list, expected)

unittest.main()
