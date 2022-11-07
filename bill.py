import csv
import random
import sys
'''function to print'''


def happy():
    for i in range(0, 8):
        if i == 0 or i == 4:
            print(" ", end="")
            for j in range(0, 4):
                print("*", end="")
            for j in range(0, 10):
                print(" ", end="")
            for j in range(0, 4):
                print("*", end="")
        if i == 1 or i == 2 or i == 3:
            print("|", end="")
            for j in range(0, 4):
                print(" ", end="")
            print("|", end="")
            for j in range(0, 8):
                print(" ", end="")
            print("|", end="")
            for j in range(0, 4):
                print(" ", end="")
            print("|", end="")
        if i == 6:
            for j in range(0, 10):
                print(" ", end="")
            print("{}", end="")
        if i == 7:
            for j in range(0, 4):
                print(" ", end="")
            for j in range(0, 15):
                print("_", end="")
        print()


def sad():
    for i in range(0, 6):
        if i == 0 or i == 5:
            print(" **** ")
        else:
            print("*    *")


print('Welcome to our GrandNew hotel!!')
print('Our menu today:')
filename = sys.argv[1]
field = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    field = next(csvreader)
    for row in csvreader:
        rows.append(row)
for col in field:
    print("%20s" % col, end=" ")
print()
for row in rows:
    for col in row:
        print("%20s" % col, end=" ")
    print()
'''request for order'''
print("Please place your order sir!!")
print("Please enter No of items u are going to place order")
x = int(input())
half = []
full = []
print("enter <item no><half/full(0/1)> <quantity>")
print("example:1 0 5")
for i in range(0, x):
    x = input()
    y = x.split(" ")
    z = [int(y[0]), int(y[2]), 0]
    flag = 0
    if int(y[1]) == 0:
        for n in half:
            if(n[0] == z[0]):
                n[1] = n[1]+z[1]
                flag = 1
        if flag == 0:
            half.append(z)
    else:
        for n in full:
            if(n[0] == z[0]):
                n[1] = n[1] + z[1]
                flag = 1
        if flag == 0:
            full.append(z)
'''bill calculation'''
total = 0.0
for x in half:
    cost = 0
    for row in rows:
        if int(row[0]) == int(x[0]):
            cost = row[1]
    total = total+int(cost) * int(x[1])
    x[2] = int(cost) * int(x[1])
for x in full:
    cost = 0
    for row in rows:
        if int(row[0]) == int(x[0]):
            cost = row[2]
    total = total + int(cost) * int(x[1])
    x[2] = int(cost) * int(x[1])
'''Tip calculation'''
print("Total amount:", "{0:.2f}".format(total))
print("Enter tip<0,10,20>percentage")
per = int(input())
p1 = (total * per) / 100
tiptotal = total + p1
print("Total amount including tip:", "{0:.2f}".format(tiptotal))
'''share calculation'''
print("Enter no of people sharing the bill")
peo = int(input())
share = tiptotal / peo
print("Amount for each person:", "{0:.2f}".format(share))
'''Test your luck'''
print("Test your luck")
print("say <yes> or <no>")
x = input()
if x == "yes":
    discount = [50, 25, 10, 0, 20]
    weight = [0.5, 1, 1.5, 2, 5]
    d1 = random.choices(discount, k=1, weights=weight)
    d = d1[0]

    if d == 50 or d == 25 or d == 10:
        dis = (tiptotal * d) / 100
        distotal = tiptotal - dis
        print("discount received::", "{0:.2f}".format(dis))
        dis = (-1) * dis
        happy()
    elif d == 0:
        distotal = tiptotal
        print("No discount")
        dis = 0
        sad()
    elif d == 20:
        dis = (tiptotal*d)/100
        distotal = tiptotal+dis
        print("Amount increased by::", "{0:.2f}".format(dis))
        sad()
else:
    distotal = tiptotal
    dis = 0
'''printing the bill'''
for row in half:
    print("Item ", row[0], " [HALF] [", row[1], "] :", row[2])
for row in full:
    print("Item ", row[0], " [FULL] [", row[1], "] :", row[2])
print("Total :", "{0:.2f}".format(total))
print("Tip percentage :", per, "%")
print("Amount after tip :", "{0:.2f}".format(tiptotal))
print("Discount/Increase :", "{0:.2f}".format(dis))
print("Final total :", "{0:.2f}".format(distotal))
cp = distotal / peo
print("cost per person :", "{0:.2f}".format(cp))
