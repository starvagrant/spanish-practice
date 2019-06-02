#!/usr/bin/env python3
import cmd
import random

class SpanishCmd(cmd.Cmd):
    prompt = '\n\033[0mEspañol> '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__()
        reading=True
        self.wordlist=[]
        i=0
        with open('words/words.txt', 'r') as f:
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

    def do_palabras(self, args):
        quiz=random.sample(self.wordlist,20)
        for pair in quiz:
            r=[0,1]
            random.shuffle(r)
            player_input = input(pair[r[0]] + '? ')
            if (player_input.lower() == pair[r[1]]):
                print('True')
            else:
                print('False')
                print(pair[r[1]])

    def keymap(self,user_input_string):
        return "áéíóúüñ¡¿"

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
