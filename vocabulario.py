#!/usr/bin/env python3
import cmd

worddict = { "merced": "mercy", "torneo": "tournament" , "tatarabuela": "great great grandmother", "vergüenza":  "shame", "mortaja":  "shroud" , "tejer":  "to knit", "barbero":  "barber", "instead": "en lugar", "apartment": "apartamento", "solution": "solución", "Budget": "presupuesto", "quebrantar":  "to break", "bodega":  "cellar", "cotidianidad":  "everydayness", "ataúd":  "coffin", "jubilado":  "retired", "sudar":  "to sweat", "deprimido":  "depressed", "jubilado":  "retired", "sudar":  "to sweat", "deprimido":  "depressed", "asombrarse":  "to wonder", "asustar":  "to frighten" , "asunto":  "affair", "breathe": "respirar", "previous": "anterior", "pesarices":  "regret", "parranda":  "spree", "pregonar":  "preach", "pergamino":  "parchment", "diluvio":  "flood", "goal": "objetivo"}


class SpanishCmd(cmd.Cmd):
    prompt = '\n\033[0mEspañol> '

    def do_words(self, args):
        for key in worddict:
            inputword = key + "? "
            player_input = input(inputword)
            if (player_input.lower() == worddict[key]):
                print('True')
            else:
                print('False')
                print(worddict[key])

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
