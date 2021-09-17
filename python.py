#Names:
print("Please input your First Name: ")
fname = input()
print("Please input your Last Name: ")
lname = input()
print(fname + " " + lname)

#Password:
print("Please input a password: ")
pword = input()
if len(pword) > 6:
    print("Password is valid")
else:
    print("Password is invalid")

##Options:
x = 0
while (x != 1 and x != 2 and x!= 3):
    print("Please select options 1, 2 or 3")
    x = int(input())
print("You have selected option number", x)

##Division:
print("Enter integer: ")
integer = int(input())
print("Enter divisor: ")
div = int(input())
print((integer//div), "remainder", (integer%div))

##Hundreds, tens, ones:
print("Give integer between 100 and 999")
num = int(input())
if (num >= 100 and num <= 999):
    hunds = num // 100
    tens = (num // 10) - ((num // 100) * 10)
    ones = (num // 1) - ((num // 10) * 10)
else:
    hunds = 0
    tens = 0
    ones = 0
print(hunds, "hundreds,", tens, "tens and", ones, "units")



##Number Sequence:
for i in range(1,11):
    print(i)

##Times Table:
print("Please input number to be multiplied: ")
num = int(input())
for i in range(1,11):
    print(i * num, end=", ")

##Comparison of 2:
print("input 1st num: ")
first = int(input())
print("input 2nd num: ")
second = int(input())
if second > first:
    print(second, first)
else:
    print(first, second)

##Comparison of 3:
print("input 1st num: ")
first = int(input())
print("input 2nd num: ")
second = int(input())
print("input 3rd num: ")
third = int(input())
x = max(first, second, third)
y = min(first, second, third)
print(y, ((first + second + third) - x - y), x)

##Words, words, words:
print("input sentence: ")
sent = str(input())
space = sent.count(" ")
print(space + 1)

##Seconds anyone?:
print("time: ")
a = [int(s) for s in input().split(':')]
print(a[0] * 60 * 60 + a[1] * 60 + a[2])



##Factors:
print("give a number: ")
num = int(input())
value = 0
ohno = 0
for i in range(1,(num+ 1)):
    if num % i == 0:
        for x in range(1, i):
            if x* i== num:
                ohno = 1
        if ohno == 1:
            break
        value = int(num / i)
        if value == i:
            print(i, end= ' ')
            continue
        print(i, value, end= ' ')

##Caesar Cipher:
print("give a sentence: ")
sent = str(input())
sent = sent.lower()
print("converted into lower case.")
print(sent)
print("converted into caesar code + 2")
a = list(sent)
for i in range(len(a)):#remember ascii of space is 32
    if ord(a[i]) != 32:
        a[i] = chr(ord(a[i]) + 2)
print("".join(a))


##Reverse:
print("give a sentence: ")
sent = str(input())
a = list(sent)
for i in range(int(len(a)/2)):
    stor = a[i]
    a[i] = a[-i-1]
    a[-i-1] = stor
print("".join(a))

##Reverse Extension:
for i in range(int(len(a)/2)):
    if a[i] != a[-i-1]:
        notpallin = 1
        break
    else:
        notpallin = 0
if notpallin == 0:
    print("it is a pallindrome")

##Rock, Paper, Scissors!:
import random
print("try to beat the computer!!!")
print("choose Rock(R), Paper(P) or Scissors(S): ")
choice = str(input())
if choice == "R":
    humanchoice = 1
if choice == "P":
    humanchoice = 2
if choice == "S":
    humanchoice = 3
compnumchoice = random.randrange(1, 4)

if compnumchoice == 1: 
    if humanchoice == 1:
        print("draw")
    if humanchoice == 2:
        print("you win, i chose rock")
    if humanchoice == 3:
        print("you lose, i chose rock")
    #for rock
if compnumchoice == 2: 
    if humanchoice == 1:
        print("you lose, i chose paper")
    if humanchoice == 2:
        print("draw")
    if humanchoice == 3:
        print("you win, i chose paper")
    #for paper
if compnumchoice == 3:
    if humanchoice == 1:
        print("you win, i chose scissors")
    if humanchoice == 2:
        print("you lose, i chose scissorws")
    if humanchoice == 3:
        print("draw")
    
    #for scissors
    


