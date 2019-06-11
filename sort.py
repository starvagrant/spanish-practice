#!/usr/bin/env python3

if __name__ == '__main__':
    list_of_lists = [['a','b',5],['c','d',3],['e','f',1]]
    i=0
    while (len(list_of_lists) > i):
        try:
            first_int = list_of_lists[i][2]
            second_int = list_of_lists[i+1][2]
            print('first_int ' + str(list_of_lists[i][2]) + ' second int ' + str(list_of_lists[i+1][2]) + '\n')

            if first_int <= second_int:
                i=i+1
            else:
                entry = list_of_lists.pop(i)
                list_of_lists.append(entry)
                i=0
                print('new array is')
                print(repr(list_of_lists))
                print()

        except IndexError:
            print('Index error')
            print(repr(list_of_lists))
            break

