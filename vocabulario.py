#!/usr/bin/env python3
import cmd

wordlist = {"vender":"to sell", "nadar":"to swim"}

class SpanishCmd(cmd.Cmd):
    prompt = '\n\033[0mEspañol> '

    def do_words(self, args):
        for key in wordlist:
            inputword = key + "? "
            player_input = input(inputword)
            print(player_input.lower() == wordlist[key])

    def default(self, args):
        print("I do not understand that command. Type help for a list of commands.")

    
if __name__ == '__main__':
    print('Bienvenido!')
    print('===========')
    print()
    print('(Type "help" for commands.)')
    print()
    game = SpanishCmd('saved-game')
    game.cmdloop()
    print('Thanks for playing!')
