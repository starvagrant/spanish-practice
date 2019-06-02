#!/usr/bin/env python3

import unittest
import vocabulario

class Tests(unittest.TestCase):

    def test_keymap(self):
        user_string1= """'a'e'i'o'u:u~n!!??"""
        user_string2= """"a"e"i"o"u:u~n!!??"""
        target_string = "áéíóúüñ¡¿"
        loop = vocabulario.SpanishCmd()
        self.assertEqual(loop.keymap(user_string1),target_string)
        self.assertEqual(loop.keymap(user_string2),target_string)

unittest.main()
