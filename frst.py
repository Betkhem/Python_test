"""def check(a):
    while type(a)!=int:
        x=input("you've got to place number:")
        a=x
a=4.5
b=0
c='fuck'
check(a)
check(b)
print(b)
check(c)"""


def first_non_repeating_letter(string):
    #your code here
    a = []
    a1 = []
    for i in range(len(string)):
        a.append(string[i])
    for i in range(len(a)):
        a1.append(a.count(i))
        print(a[i])
        print(a1)
    return a1

"""
x = str(input())
x1=first_non_repeating_letter(x)
print(x1)"""

def Matrix():
    row=int(input('rows:'))
    column=int(input('columns:'))
    matrix=[]
    for i in range(row):
        submatrix=[]
        for j in range(column):
            submatrix.append(int(input(':')))
        matrix.append(submatrix)
    for i in matrix:
        print(i)
    Max=max(matrix)
    Min=min(matrix)
    IndexMax=matrix.index(Max)
    IndexMin=matrix.index(Min)
    matrix.remove(Max)
    matrix.remove(Min)
    matrix.insert(IndexMax,Min)
    matrix.insert(IndexMin,Max)
    for i in matrix:
        print(i)


#question107
def pluralize(a):
    b = []
    for i in a:
        if a.count(i) > 1:
            if not i + 's' in b:
                b.append(i + 's') 
        elif a.count(i) == 1:
            if not i in b:
                b.append(i)
    return b


def time_to_finish(sent, sent2):
    return len(sent[len(sent2):].replace(' ', '')) * 0.5


def is_there_consecutive(lst, n , times):
    return True if lst.count(n) == times else False


def clean_string(s):
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == '#':
            s = s.replace(s[i + 1], '#', 1)
        print(s, s[i], i)
    for i in s:
        s = s.replace('#', '', 1)
    return s[::-1]

print(clean_string('abc#d##c'))
print("{:,'#'}".format('abc#d##c').replace('#', ' '))