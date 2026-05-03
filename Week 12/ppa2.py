'''3
4
oooo
0  0
0000

5
5

00000
0   0
0   0
0   0
00000
'''
a=int(input())
b=int(input())
def pattern(a,b):
    for i in range(a):
        if i == 0 or i == a-1:
            print('o'*b)
        else:
            print('o'+' '*(b-2)+'o')
pattern(a, b)