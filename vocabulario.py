#!/usr/bin/env python3
import cmd
import random

class SpanishCmd(cmd.Cmd):
    prompt = '\n\033[0mEspañol> '

    def __init__(self, file_name='words/countedwords.txt'):
        super().__init__()
        self.file_name=file_name
        self.word_list=[]
        self.load_word_list(self.file_name)

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
        """ Test yourself with a 20 word vocabulary quiz """
        self.sort_word_list()
        quiz=self.prepare_quiz()
        for quizline in quiz:
            r=[0,1]
            random.shuffle(r)
            player_input = input(quizline[r[0]] + '? ')
            if self.compare(player_input, quizline[r[1]]):
                print('True')
                print(quizline[2]+1)
                quizline[2] = quizline[2] + 1
            else:
                print('False')
                print(quizline[r[1]])

        self.write_word_list()

    def do_quit(self, args):
        """ Exit the program """
        print("Thanks for playing!")
        # returning True ends cmd's looping structure
        return True

    def keymap(self,user_input):
        """ Allows for proper input of utf8 characters for Spanish:
        'a=á,'e=e,'i=í,'o=ó,'u=ú,
        :u=ü,~n=n,!!=¡, and ??=¿"""

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

    def load_word_list(self, file_name='words/countedwords.txt'):
        """ allow for loading an alternate word list """
        reading=True
        i=0
        self.word_list = []
        with open(file_name, 'r') as f:
            while(reading==True):
                line = f.readline().rstrip()
                words = line.split('\t',2)
                # list length will be 1 with empty string
                if len(words) > 1:
                    words[2] = int(words[2])
                    self.word_list.append(words)
                else:
                    reading=False
                i=i+1

    def write_word_list(self, file_name='words/countedwords.txt'):
        """ write self.word_list info to a file """
        i=0
        with open(file_name, 'w') as f:
            for line in self.word_list:
                entry = line[0] + '\t' + line[1] + '\t' + str(line[2]) + '\n'
                f.write(entry)

    def compare(self, word1, word2):
        """ Compare whether a string, post user input processing is
        the same as the original string in the stored area"""
        processed = self.keymap(word1.lower())
        return processed==word2

    def prepare_quiz(self):
        """ return a list that is iterated over to provide quiz answers """
        if len(self.word_list) < 20:
            return self.word_list
        else:
            return self.word_list[:20]

    def sort_word_list(self):
        """ Sort the program's internal word list """
        i=0
        while (len(self.word_list) > i):
            try:
                first_int = self.word_list[i][2]
                second_int = self.word_list[i+1][2]

                if first_int <= second_int:
                    i=i+1
                else:
                    entry = self.word_list.pop(i)
                    self.word_list.append(entry)
                    i=0

            except IndexError:
                break


    def default(self, args):
        """ override cmd modules default response for one more helpful to the user """
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
