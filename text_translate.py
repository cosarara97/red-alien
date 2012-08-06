#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This file is part of ASC.

#    ASC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    ASC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with ASC.  If not, see <http://www.gnu.org/licenses/>.

import string

def read_table_encode(table_string):
    table = table_string.split("\n")
    dictionary = {}
    for line in table:
        line_table = line.split("=")
        dictionary[line_table[1]] = line_table[0]
    return dictionary


def read_table_decode(table_string):
    table = table_string.split("\n")
    dictionary = {}
    for line in table:
        line_table = line.split("=")
        dictionary[line_table[0]] = line_table[1]
    return dictionary


def ascii_to_hex(string_, dictionary):
    trans_string = u''
    i = 0
    while i < len(string_):
    #for i in range(len(string)):
        character = string_[i]
        if character == "\\" and string_[i + 1] == "h":
            #print "case1"
            if (string_[i + 2] in string.hexdigits and
                string_[i + 3] in string.hexdigits):
                trans_string += (string_[i + 2] + string_[i + 3]).upper()
                i += 3
        elif character in dictionary:
            #print "case normal"
            trans_string += dictionary[character]
        elif string_[i:i+2] in dictionary:
            #print "case3"
            trans_string += dictionary[string_[i:i+2]]
            i += 1
        else:  # (not tested)
            length = 2
            while length < 10:
                if string_[i:i+length] in dictionary:
                    trans_string += dictionary[string_[i:i+length]]
                    i += length - 1
                    break
                else:
                    length += 1
        i += 1
    return trans_string


def hex_to_ascii(string, dictionary):
    trans_string = u''
    for i in range(len(string) / 2):
        pos = i * 2
        byte = string[pos:pos + 2]
        if byte in dictionary:
            trans_string += dictionary[byte]
        else:
            trans_string += "\\h" + byte
    return trans_string

table = u"00= " u"""
01=À
02=Á
03=Â
04=Ç
05=È
06=É
07=Ë
08=Ì
09=Í
0B=Ï
0C=Ò
0D=Ó
0E=Ô
0F=Ö
11=Ù
12=Ú
13=Û
14=Ñ
16=à
17=á
19=ç
1A=è
1B=é
1C=ê
1D=ë
1E=ì
20=î
21=ï
22=ò
23=ó
24=ô
26=ù
27=ú
28=û
29=ñ
2A=º
2B=ª
2D=&
2E=+
32=[de]
35==
39=>->
4F=>_
51=¿
52=¡
53=[pk]
54=[mn]
55=[po]
56=[ké]
57=[bl]
58=[oc]
59=[k]
5A=Í
5B=%
5C=(
5D=)
68=â
6F=í
79=[u]
7A=[d]
7B=[l]
7C=[r]
99=>>
A1=0
A2=1
A3=2
A4=3
A5=4
A6=5
A7=6
A8=7
A9=8
AA=9
AB=!
AC=?
AD=.
AE=-
AF=·
B0=[...]
B1="
B2="
B3='
B4='
B5=[m]
B6=[f]
B7=?
B8=,
BA=/
BB=A
BC=B
BD=C
BE=D
BF=E
C0=F
C1=G
C2=H
C3=I
C4=J
C5=K
C6=L
C7=M
C8=N
C9=O
CA=P
CB=Q
CC=R
CD=S
CE=T
CF=U
D0=V
D1=W
D2=X
D3=Y
D4=Z
D5=a
D6=b
D7=c
D8=d
D9=e
DA=f
DB=g
DC=h
DD=i
DE=j
DF=k
E0=l
E1=m
E2=n
E3=o
E4=p
E5=q
E6=r
E7=s
E8=t
E9=u
EA=v
EB=w
EC=x
ED=y
EE=z
F0=:
F1=Ä
F2=Ö
F3=Ü
F4=ä
F5=ö
F6=ü
FA=\\l
FB=\\p
FC=\\c
FD=\\v
FE=\\n
FF=$$"""

#print type(read_table_decode(table)['1B'])
#print ascii_to_hex(u"abcde ", read_table_encode(table))
#print hex_to_ascii("E0D5E0D5E0D5E0D5E0D5E0D5", read_table_decode(table))
