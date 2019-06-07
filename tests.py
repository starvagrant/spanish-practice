#!/usr/bin/env python3

import unittest
import vocabulario
import os

class Tests(unittest.TestCase):

    def test_keymap(self):
        user_string1= """'a'e'i'o'u:u~n!!??"""
        user_string2= """"a"e"i"o"u:u~n!!??"""
        target_string = "áéíóúüñ¡¿"
        loop = vocabulario.SpanishCmd()
        self.assertEqual(loop.keymap(user_string1),target_string)
        self.assertEqual(loop.keymap(user_string2),target_string)

    def test_load_word_list(self):
        if os.path.exists('test_dir/test_list.csv'):
            os.remove('test_dir/test_list.csv')
            os.rmdir('test_dir/')
        os.mkdir('test_dir')
        with open('test_dir/test_list.csv', 'w') as f:
            f.write('answer	repuesta	0')

        loop = vocabulario.SpanishCmd()
        loop.load_word_list('test_dir/test_list.csv')
        expected = [['answer','repuesta',0]]
        self.assertListEqual(loop.wordlist, expected)

    def test_write_word_list(self):
        if os.path.exists('test_dir/test_list.csv'):
            os.remove('test_dir/test_list.csv')
            os.rmdir('test_dir/')
        os.mkdir('test_dir')
        with open('test_dir/test_list.csv', 'w') as f:
            f.write('answer	repuesta	0')

        loop = vocabulario.SpanishCmd()
        loop.load_word_list('test_dir/test_list.csv')
        loop.wordlist[0][2] = 8
        loop.write_word_list('test_dir/test_list.csv')

        with open('test_dir/test_list.csv', 'r') as f:
            expected = f.readline()

        self.assertEqual(expected, 'answer	repuesta	8')

    def test_word_compare(self):
        loop = vocabulario.SpanishCmd()
        boolean = loop.compare("'ANIMO", "ánimo")
        self.assertTrue(boolean)

unittest.main()
