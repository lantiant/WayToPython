#!/usr/bin/python3
#coding: utf-8
import string
import random
import sys

#生成具有一定强度的密码，建议最小长度为8位,最大长度不超过40位,超过会触发bug。

p1 = list(string.ascii_lowercase)
p2 = list(string.digits)
p3 = list(string.punctuation)
#如果确定某些特殊符号不能用作密码，可以将p4明确指定为由可以使用的特殊符号构成的列表。
p4 = list(string.ascii_uppercase)
random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)
random.shuffle(p4)


def getnewlist(length=8):
    length = int(sys.argv[1])
    oldlist = [p1,p2,p3,p4]
    lenlist = len(oldlist)
    if length == 0 or length <= lenlist:
        return oldlist[0:length]
    else:
        diff = length - lenlist
        if diff <= lenlist:
            return oldlist + oldlist[0:diff]
        else:
            multi = length // lenlist
            rem = length % lenlist
            newlist = oldlist * multi
            return newlist + oldlist[0:rem]

pwlist = []
for i in getnewlist():
    pw = i.pop()
    pwlist.append(pw)

random.shuffle(pwlist)

print(''.join(pwlist))
