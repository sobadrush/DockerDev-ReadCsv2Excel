#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def plus(a, b):
    return a + b


def handleMemo(_list):

    if len(_list) == 1 or _list[0] == '':
        return

    # for idx, val in enumerate(tempLine):
    #     if idx >= 4:
    #         tempLine[idx] = val.replace(" ", "，")
    # return tempLine

    # ref. https://www.geeksforgeeks.org/python-replace-elements-greater-than-k/
    tempList = [elem.replace(" ", "，") if idx >= 4 else elem for idx, elem in enumerate(_list)]
    
    # 1. Google: python clear list
    # 2. Concate list: ref. https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
    _list[:] = tempList[0:5] + [''.join(tempList[5:])] 

if __name__ == '__main__':
    # print(f'My Answer is: {plus(3, 4)}')
    myList = ["A1", "B2", "C3", "D4", "E 5", "F  6"]
    handleMemo(myList)
    print(f'handleMemo is: {myList}')
