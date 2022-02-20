import math as m
from copy import *

A = None
P = None
r = None
t = None
n = None

#rounds perameter to nearest hundreth
def round(x):
    return int(x) + (int(((x + .005)-int(x))*100)/100)

#solves for A
def solveA(P,r,t,n):
    if n == 'e':
        A = P * m.exp(r * t)
    else:
        A = P * ((1+r/n)) ** (t*n)
    return A

#solves for A
def solveP(A,r,t,n):
    if n == 'e':
        P = A / (m.exp(r * t))
    else:
        P = A / ((1 + (r/n)) ** (t * n))
    return P

#solves for r
def solveR(A,P,t,n):
    if n == "e":
        r = (m.log(A/p)) / t
    else:
        r = (((A/P) ** (1/(n*t))) - 1) * n
    return r

#solves for t
def solveT(A,P,r,n):
    if n == 'e':
        t = (m.log(A/P))/r
    else:
        t = (m.log(A/P,(1+r/n))) / n
    return t

def offerCompare(P,t,O):
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


# m.exp(-power-) is e to the power

#m.log(a,Base) a in the numeric value/ "to the" and Base is the base of the log
# (if 1 perameter is passed it uses natural log v e())

# Asks what user is trying to find
while True:
    print("Welcome to the loan helper. What can I help you with today?")
    print("1.) I need to know how much to invest to get to a certain amount in a set time")
    print("2.) I need to know how much money I will have in a certain amount of time with a set investment")
    print("3.) I need to know how long I need to invest a certain amount of money to reach a set goal")
    print("4.) I need to find out the best deal between x amount of deals investments based on percentage and compounding")
    print("5.) I need to know what APR I need to reach a certain goal with a set investment and time")
    x = input("")
    if x == "1" or x == "2" or x == "3" or x == "4" or x == "5":
        break
    else:
        print("not an option\n")

# Get parameters that are needed (ext. 4)
if x != '4':
    if x != '1':
        while True:
            P = input("What is your starting investment?")
            if P.upper() == P:
                P = float(P)
                break
            else:
                print("Invalid Input")
    if x != '2':
        while True:
            A = input("how much money do you want to end with?")
            if A.upper() == A:
                A = float(A)
                break
            else:
                print("Invalid Invalid")
    if x != '3':
        while True:
            t = input("How many years are going to invest the money?")
            if t.upper() == t:
                t = float(t)
                break
            else:
                print("Invalid Input")
    if x != '5':
        while True:
            r = input("What is your APR (annual percentage rate)")
            if r.upper() == r:
                r = float(r) / 100
                break
            else:
                print("Invalid Input")
    while True:
        print("How often is your investment compunded")
        print("1.annualy")
        print("2.semi-annualy")
        print("3.quarterly")
        print("4.monthly")
        print("5.bi-weekly")
        print("6.weekly")
        print("7.daily")
        print("8.continuously")
        print("9.custom")
        n = input("")
        if n == 'annualy' or n == '1':
            n = 1
            break
        if n == 'semi-annualy' or n == '2':
            n = 2
            break
        if n == 'quarterly' or n == '3':
            n = 4
            break
        if n == 'monthly' or n == '4':
            n = 12
            break
        if n == 'bi-weekly' or n == '5':
            n = 26
            break
        if n == 'weekly' or n == '6':
            n = 52
            break
        if n == 'daily' or n == '7':
            n = 365
            break
        if n == 'continuously' or n == '8':
            n = 'e'
            break
        if n == "custom" or n == '9':
            custom = True
            while custom is True:
                n = input("How many times a year is your investment compunded")
                if n.upper == n:
                    n = float(n)
                    custom = False
                else:
                    ("Invalid input")
            break
        else:
            print("Invalid Input")

# deals with option #4        
if x == '4':
    # gets amount of offers
    while True:
        offers = input('How many offers are you comparing')
        if offers.upper() == offers:
            offers = float(offers)
            if (float(offers)).is_integer() and int(offers) == abs(int(offers)):
                offers = int(offers)
                break
            else:
                print("number must be a positive, whole number.")
        else:
            print("Invalid input")
    while True:
        P = input("What is your starting investment?")
        if P.upper() == P:
            P = float(P)
            break
        else:
            print("Invalid Input")
    while True:
        t = input("How many years will you be investing?")
        if t.upper() == t:
            t = float(t)
            break
        else:
            print("Invalid Input")

print()

#solves respective problem for 1,3 and 5 and prints final message
if x != '4':
    if A == None:
        A = solveA(P, r, t, n)
        A = round(A)
        print(f"${A:,}")
    elif P == None:
        P = solveP(A, r, t, n)
        P = round(P)
        print(f'${P:,}')
    elif r == None:
        r = solveR(A, P, t, n)
        r = round(r)
        print(f'{r * 100}%')
    elif t == None:
        t = solveT(A, P, r, n)
        t = round(t)
        print(f'{t} years')

#solves 4 and displays final message
if x == '4':
    offerCompare(P, t, offers)