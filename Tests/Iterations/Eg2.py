#Testing Iteration - while() in Python
import time
print("Brace for a countdown")
def myWhile():
    n=5
    while n>0:
        print(n)
        n=n-1
        time.sleep(2)
        if n==0:
            print("Enter the below character")
            line = input('!')
            if(line == '!'):
                print("Blast!!!")
                break
            else:
                print("Wrong Entry! Restarting countdown")
                myWhile()
myWhile()
