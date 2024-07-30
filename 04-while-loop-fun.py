# FUN WITH WHILE LOOPS
from random import randint
from time import sleep
import os


count = 99

while count < 1000:
    os.system('clear')
    print(f"{count} little bug in our code...")
    sleep(2)
    print(f"{count} pesky little bugs...")
    sleep(2)
    print("Take one down and patch it around...")
    sleep(2)
    new_bugs = randint(1, 50)
    count += new_bugs
    print(f"{count} little bugs in our code!")
    sleep(2) 
    



