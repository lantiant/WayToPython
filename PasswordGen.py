#!/usr/bin/python2
# coding: utf-8
import string
import random
import sys
from random import choice


p1 = list(string.ascii_lowercase)
p2 = list(string.digits)
p3 = list(string.punctuation)
# 如果确定某些特殊符号不能用作密码，可以将p4明确指定为由可以使用的特殊符号构成的列表。
p4 = list(string.ascii_uppercase)
random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)
random.shuffle(p4)

def looppw(length,amount):
    '''生成具有一定强度的密码，使用方法：passwdgen.py 【密码长度】【密码个数】。
      不指定长度和个数时生成一个8位长的密码。
      不指定个数时默认生成一个。'''
    def getnewlist():
        oldlist = [p1, p2, p3, p4]
        lenlist = len(oldlist)
        if length == 0 or length <= lenlist:
            return oldlist[0:length]
        else:
            diff = length - lenlist
            if diff <= lenlist:
                return oldlist + oldlist[0:diff]
            else:
                multi = length / lenlist
                rem = length % lenlist
                newlist = oldlist * multi
                return newlist + oldlist[0:rem]

    def getpw():
        pwlist = getnewlist()
        pwfinal = []
        for i in pwlist:
            pw = choice(i)
            pwfinal.append(pw)
        random.shuffle(pwfinal)
        return ''.join(pwfinal)


    for j in range(amount):
        print getpw()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        length = 8
        amount = 1
    elif len(sys.argv)  == 2:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print 'Usage: python sys.argv[0] [length] [amount],length and amount are an integer.'
            exit(-1)
        else:
            amount = 1
    elif len(sys.argv)  == 3:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print 'Usage: python sys.argv[0] [length] [amount],length and amount are an integer.'
            exit(-2)
        else:
            try:
                amount = int(sys.argv[2])
            except ValueError:
                print 'Usage: python sys.argv[0] [length] [amount],length and amount are an integer.'
                exit(-3)
    elif len(sys.argv) > 3:
        print 'Usage: python sys.argv[0] [length] [amount],length and amount are an integer.'
        exit(-4)
    looppw(length, amount)
