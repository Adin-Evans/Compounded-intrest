import math as m
from copy import *
def round(x):
    return int(x) + (int(((x + .005)-int(x))*100)/100)


def solveA(P,r,t,n):
    if n == 'e':
        A = P * m.exp(r * t)
    else:
        A = P * ((1 + r/n)) ** (t*n)
    return A

P = 100
t = 5
O = 4
rates = []
compounds = []
finalValues = []
for i in range(O):
    while True:
        x = input(f'What is offer {i+1}\'s APR? ')
        if x.upper() == x:
            x = float(x)
            x /= 100
            rates.append(x)
            break
        else:
            print("Invalid Input")
for i in range(O):
    while True:
        x = input(f'how often does offer {i+1} compound a year? ')
        if x.upper() == x:
            compounds.append(float(x))
            break
        else:
            print("Invalid Input")
for i in range(O):
    temp = solveA(P, rates[i], t, compounds[i])
    finalValues.append(temp)

originalFinalValues = copy(finalValues)
finalValues.sort(reverse = True)
print(f'offer {(originalFinalValues.index(finalValues[0])+1)} offers the best deal at ${round(finalValues[0])}\nIt makes you {round(finalValues[0] - finalValues[1])} more dollars then the next best deal and {round(finalValues[0] - finalValues[len(finalValues)-1])} more than the worst offer')
