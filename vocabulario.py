#!/usr/bin/env python3
import cmd
import random

class SpanishCmd(cmd.Cmd):
    prompt = '\n\033[0mEspañol> '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__()
        self.wordlist=[]
        self.load_word_list()

    def do_keymap(self, args):
        """ Prints a message explaining how to input troublesome spanish characters
            Use the accents command to try it out"""

        keymap_message = """For inputting spanish accents on English keyboard
                            Use the following keymappings:
                           'a=á  'e=é  'i=í  'o=ó  'u=ú
                           :u=ü  ~n=ñ  ??=¿  !!=¡
                           Program also understands directly input áéíóúüñ¡¿
                           Try typing accents 'a~n or accents <example-text>
                           To see how the program handles keymapped text"""
        keymap_lines = keymap_message.split('\n')
        for line in keymap_lines:
            print(line.lstrip())

    def do_accents(self,args):
        """ This command lets you see how the program translates input internally
        and is a spot to experiment with the mappings you can find by typing keymap.
        Usage: accents !!I'm internal! or other forms of accents <words>"""

        print(self.keymap(args.lower()))

    def do_palabras(self, args):
        quiz=random.sample(self.wordlist,20)
        for pair in quiz:
            r=[0,1]
            random.shuffle(r)
            player_input = input(pair[r[0]] + '? ')
            if self.compare(player_input, pair[r[1]]):
                print('True')
            else:
                print('False')
                print(pair[r[1]])

    def keymap(self,user_input):
        user_input = user_input.replace("'a", "á")
        user_input = user_input.replace('"a', "á")
        user_input = user_input.replace("'e", "é")
        user_input = user_input.replace('"e', "é")
        user_input = user_input.replace("'i", "í")
        user_input = user_input.replace('"i', "í")
        user_input = user_input.replace('~n', "ñ")
        user_input = user_input.replace("'o", "ó")
        user_input = user_input.replace('"o', "ó")
        user_input = user_input.replace("'u", "ú")
        user_input = user_input.replace('"u', "ú")
        user_input = user_input.replace(":u", "ü")
        user_input = user_input.replace(";u", "ü")
        user_input = user_input.replace("!!", "¡")
        user_input = user_input.replace("??", "¿")
        return user_input

    def load_word_list(self, file_name='words/words.txt'):
        reading=True
        i=0
        self.wordlist = []
        with open(file_name, 'r') as f:
            while(reading==True):
                line = f.readline()
                words = line.split('\t',2)
                # list length will be 1 with empty string
                if len(words) > 1:
                    words[1] = words[1][:-1]
                    self.wordlist.append(words)
                else:
                    reading=False
                i=i+1

    def compare(self, word1, word2):
        processed = self.keymap(word1.lower())
        return processed==word2

    def default(self, args):
        print("I do not understand that command. Type help for a list of commands.")

if __name__ == '__main__':
    print('Bienvenido!')
    print('===========')
    print()
    print('(Type "help" for commands.)')
    print()
    game = SpanishCmd()
    game.cmdloop()
    print('Thanks for playing!')
