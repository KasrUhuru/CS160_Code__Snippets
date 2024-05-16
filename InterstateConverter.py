import math
import sys
#Create a program that accepts integer input under "num"
#
num = int(input())
kind = ""
direction = ""

invalid_set = set([0,00,100,200,300,400,500,600,700,800,900])
if math.fabs(num) in invalid_set or math.fabs(num) > 999:
    print(num, 'is not a valid interstate highway number.')
    sys.exit()

direction = 'east/west' if (num % 2 == 0) else 'north/south'

if (len(str(num)) > 2):
    kind = 'auxiliary'
else:
    kind = 'primary'

if kind == 'auxiliary':
    primary = str((num//10)%10) + str(num%10)
    if (primary[0] == '0'):
        primary = str(num%10)
    print(f'I-{num} is {kind}, serving I-{primary}, going {direction}.')
else: print(f'I-{num} is {kind}, going {direction}.')
