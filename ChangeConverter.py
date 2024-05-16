import sys

change = int(input())

if 0 >= change:
    print('No change')

#determine how many dollars
dollars = change // 100
leftover = (change - (100 * dollars))

#determine how many quarters with leftover change
quarters = leftover // 25
leftover = (leftover - 25*quarters)

#determine how many dimes with leftover change
dimes = leftover // 10
leftover = (leftover - 10*dimes)

#determine how many nickles with leftover change
nickels = leftover // 5
leftover = (leftover - 5*nickels)

#determine how many pennies with leftover change
pennies = leftover

if dollars > 0:
    if dollars == 1:
        print(dollars, "Dollar")
    else:
        print(dollars, "Dollars")
if quarters > 0:
    if quarters == 1:
        print(quarters, 'Quarter')
    else:
        print(quarters, 'Quarters')
if dimes > 0:
    if dimes == 1:
        print(dimes, 'Dime')
    else:
        print(dimes, 'Dimes')
if nickels > 0:
    if nickels == 1:
        print(nickels, 'Nickel')
    else:
        print(nickels, 'Nickels')
if pennies > 0:
    if pennies == 1:
        print(pennies, 'Penny')
    else:
        print(pennies, 'Pennies')