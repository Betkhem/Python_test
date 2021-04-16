def first_non_repeating_letter(string):
    def split_to_list(a):
        b = []
        for i in range(len(a)):
            c = []
            c.append(a[i].lower())
            b.append(c)
        return b
    str = split_to_list(string)
    c = []
    for i in range(len(str)):
        f = str.count(str[i])
        if f == 1:
             c.append(string[i])
    try:
        return c[0]
    except IndexError:
        return ''


def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    v = []
    for elem in roman:
        v.append(elem)
    print(v)
    # creates list of roman elements
    v1 = v.copy()
    a = []
    b = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    c = [1, 5, 10, 50, 100, 500, 1000]
    # searches for elements like 'IV'
    for i in range(1, len(v)):
        for j in range(len(b)):
            x = b.index(v[i - 1])
            y = b.index(v[i])
            if v[i] == b[j] and x < y:
                a.append(c[y] - c[x])
                v1.remove(v[i])
                v1.remove(v[i - 1])
    for i in range(len(v1)):
        for j in range(len(b)):
            if v1[i] == b[j]:
                a.append(c[j])
    return sum(a), a, v1


def array_diff(a, b):
    #your code here
    pass


def switch(strng, words):
    # words is a list of 2 elements
    strng1 = strng.split()
    a = []
    for i in range(len(strng1)):
        b = []
        b.append(strng1[i])
        a.append(b)
    for i in range(len(a)):
        for j in range(len(words)):
            if a[i][0] == words[j][0]:
                a[i].pop(0)
                a[i].insert(0, words[j][1])
    a1 = []
    for i in range(len(a)):
        a1.append(a[i][0])
    a2 = ' '.join(a1)
    return a2


def sum_fracts(lst):
    a = []
    for i in range(len(lst)):
        a.append(lst[i][0]/lst[i][1])
    return sum(a)


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 3:
        names[0] += ','
        return names[0] + ' ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        names[0] += ','
        return names[0] + ' ' + names[1] + ' and ' + str((len(names) - 2)) + ' others like this'


def maskify(cc):
    x1 = []
    for i in range(len(cc)-4):
        if cc[i] == ' ':
            x1.append(' ')
        else:
            cc1 = cc.replace(cc[i], '#')
            x1.append(cc1[i])
    return ''.join(x1) + cc[-4:]


def comp(array1, array2):
    a = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i]**2 == array2[j]:
                a.append(array2[j])
                print(array1[i], array2[j])
                break
    for i in range(len(array2)):
        x = a.count(array2[i])
        y = array2.count(array2[i])
        if x > y:
            a.remove(array2[i])
    print(array1, array2, len(array1), len(array2), len(a))
    print(a, len(a))
    if len(a) == len(array1):
        return True
    else:
        return False


def fly_by(lamps, drone):
    # hack the lamps
    return lamps[-len(drone):].replace('x', 'o') + lamps[:-len(drone)]


def pig_it(text):
    #your code here
    a = text.split()
    b = []
    for i in range(len(a)):
        b.append(a[i].replace(a[i][0], '', 1))
        b[i] += a[i][0] + 'ay'
        if b[i][0] == '!' or b[i][0] == '?':
            b[i] = b[i][:-2]
    if b[-1][0] == '!':
        print('lol', b[-1][:-2])
    return ' '.join(b)


"""f = open('C:\\test_folder\test.txt', 'r')
print(f.read())"""


def generate_all_possible_matches(k):
    # Good Luck ! There is no such thing.
    c = []
    def fact(a):
        fact = 1
        for i in range(1, a + 1):
            fact = fact * i
        return fact
    
    for j in range(fact(k)):
        b = ['0:0']
        try:
            if c[-1][-1][0] == str(k):
                b = ['0:0', '1:0']
                if c[-1][-1][-1] != str(k):
                    pass
        except IndexError:
            pass
        for i in range(1, k + 1):
            if b[-1][0] != k:
                b.append(b[0].replace(b[0][0], str(k - (k - i)), 1))
        c.append(b)
        
    return b, c


# b.append(a.replace(a[0], str(k - (k - i)), 1))


a = int(input(':'))
print(generate_all_possible_matches(a))

# add left number(a[L:R]) untill it reaches k, then increase right number by 1 and repeat process.