"""
stringjumble.py
Author: Sarah Dunbar
Credit: http://stackoverflow.com/questions/743806/split-string-into-a-list-in-python, http://www.decalage.info/en/python/print_list
http://stackoverflow.com/questions/4130027/python-count-elements-in-list, https://mail.python.org/pipermail/tutor/2004-August/031010.html, Anoushka Alavilli

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string = input("Please enter a string of text (the bigger the better): ")
print ('You entered "' + string + '". Now jumble it: ') 
strlist = string.split(" ")
r = len(strlist)
z = r*2
for x in range(z):
    if x == (z-1):
        break
    if x%2 == 1:
        strlist.insert(x, " ")
    else:
        m = 1
strlist3 = strlist[:]
strlist3.reverse()
l2 = ''.join(strlist3)
for p in range(0, (r*2 - 1)):
    g = strlist[p]
    i = list(g)
    strlist[p] = i
for p in range(0, (r*2 - 1)):
    g = strlist[p]
    g.reverse()
    strlist[p] = g
strlist.reverse()
for x in range(0, (r*2 - 1)):
    g = strlist[x]
    g = ''.join(g)
    strlist[x] = g
strlist2 = strlist[:]
strlist2.reverse()
l3 = ''.join(strlist2)
l1 = ''.join(strlist)
print (l1)
print (l2)
print(l3)
