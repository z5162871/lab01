strings = ['This', 'list', 'is', 'now', 'all', 'together']
strings1 = ""

i = 0

for i in strings:
    strings1 += i
    if(i != strings[-1]):
        strings1 += " "


print(strings1)

print(' '.join(strings))
