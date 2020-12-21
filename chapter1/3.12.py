# python data structure

# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))
#
# a.insert(2, -1)
# a.append(333)
# print(a)
# a.remove(333)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)

# take a list as a stack
# stack = [5,6,7]
# stack.append(8)
# stack.append(9)
# print(stack)
#
# stack.pop()
# print(stack)

# take a list as a queue
# from collections import deque
# queue = deque(['Eric', 'John', 'Michael'])
# queue.append('Terry')
# queue.append('Graham')
# print(queue)
#
# print(queue.popleft())
# print(queue.popleft())

# List generator
# v = [2, 4, 6]
# l = [3*x for x in v]
# print(l)
# l1 = [[x, x**2] for x in v]
# print(l1)
# l2 = [3*x for x in v if x > 3]
# print(l2)

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# new = [v.strip() for v in freshfruit]
# print(new)

# v1 = [2,4,6]
# v2 = [4,3,-9]
# l = [x*y for x in v1 for y in v2]
# print(l)
# l1 = [x+y for x in v1 for y in v2]
# print(l1)
# l2 = [v1[i]*v2[i] for i in range(len(v1))]
# print(l2)

# complex expression in list generator
# l = [str(round(355/113, i)) for i in range(1, 6)]
# print(l)

# embed list parse
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# l = [[row[i] for row in matrix] for i in range(4)]
# print(l)
#
# t = []
# for i in range(4):
#     t.append([row[i] for row in matrix])
# print(t)
#
# t1 = []
# for i in range(4):
#     t_row = []
#     for row in matrix:
#         t_row.append(row[i])
#     t1.append(t_row)
# print(t1)

# Del operation
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# Tuple and list
# t = 12345, 54321, 'hello!'
# print(t[0])
# u = t, (1,2,3)
# print(u)

# Set
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)
#
# a = set('abracadabra')
# print(a)
# b = set('alacazam')
# print(b)
# print(a|b)
# print(a&b)
#letter in a or b but not both
# print(a^b)
# print(a-b)

# set generator
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# empty set
# a = set()
# print(a)

# DICT
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# print(list(tel.keys()))
# print('guido' in tel)

# d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(d)

# dict generator
# d1 = {x:x**2 for x in (2,4,6)}
# print(d1)

# d2 = dict(sape=4139, guido=4127, jack=4098)
# print(d2)

# traverse tips
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# zip ()
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(q, a)

# List reversed()
# for i in reversed(range(1,10,2)):
#     print(i)
# for j in range(9, 0, -2):
#     print(j)

# Sorted()
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(basket):
#     print(f)