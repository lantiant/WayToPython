#!/usr/bin/python2
#coding: utf-8
import string
import random
import sys

strings = string.digits + string.ascii_letters + string.punctuation

def looppw(length,amount,filename=None):
    '''生成具有一定强度的字符串，使用方法：passwdgen.py 【字符串长度】【字符串个数】【保存字符串的文件名】。
      不指定长度和个数时生成一个8位长的字符串。
      不指定个数时默认生成一个。
      不指定文件名时默认不保存生成的字符串至文件中,指定文件名后会将字符串保存至文件中并打印出来。'''
    def passwdgen():
        rawpw = [ random.choice(strings) for i in range(length) ]
        finalpw = ''.join(rawpw)
        return finalpw

    if filename is None:
        for j in range(amount):
            print passwdgen()
    else:
        output = sys.stdout
        outputfile = open(filename, 'w')
        sys.stdout = outputfile
        for j in range(amount):
            print passwdgen()
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
        filename = None
    elif len(sys.argv)  == 2:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print usage
            exit(-1)
        else:
            amount = 1
            filename = None
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
            else:
                filename = None
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