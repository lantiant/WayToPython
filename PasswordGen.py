#!/usr/bin/python2
# coding: utf-8
import string
import random
import sys
from random import choice


p1 = list(string.ascii_lowercase)
p2 = list(string.digits)
p3 = list(string.punctuation)
# 如果确定某些特殊符号不能用作字符串，可以将p4明确指定为由可以使用的特殊符号构成的列表。
p4 = list(string.ascii_uppercase)
random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)
random.shuffle(p4)

def looppw(length,amount,filename=None):
    '''生成具有一定强度的字符串，使用方法：passwdgen.py 【字符串长度】【字符串个数】[保存字符串的文件名】。
      不指定长度和个数时生成一个8位长的字符串。
      不指定个数时默认生成一个。
      不指定文件名时默认不保存生成的字符串至文件中,指定文件名后会将字符串保存至文件中并打印出来。'''
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

    if filename is None:
        for j in range(amount):
            print getpw()
    else:
        output = sys.stdout
        outputfile = open(filename, 'w')
        sys.stdout = outputfile
        for j in range(amount):
            print getpw()
        outputfile.close()
        sys.stdout = output
        f = open(filename,'r')
        content = f.read()
        print content
        f.close()

if __name__ == "__main__":
    usage = 'Usage: python '+sys.argv[0]+' [length] [amount] [filename],length and amount are an integer.'
    if len(sys.argv) == 1:
        length = 8
        amount = 1
    elif len(sys.argv)  == 2:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print usage
            exit(-1)
        else:
            amount = 1
    elif len(sys.argv)  == 3:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print usage
            exit(-1)
        else:
            try:
                amount = int(sys.argv[2])
            except ValueError:
                print usage
                exit(-2)
    elif len(sys.argv)  == 4:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print usage
            exit(-1)
        else:
            try:
                amount = int(sys.argv[2])
            except ValueError:
                print usage
                exit(-2)
            else:
                filename = sys.argv[3]
    elif len(sys.argv) > 4:
        print usage
        exit(-3)
    looppw(length, amount,filename)





