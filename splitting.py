# James Quintin 03/02/18
# Using split() to separate string component

with open("datum/iris.csv") as f:
    for line in f: 
        print(line.split(',')[4],end='') # removes new line


