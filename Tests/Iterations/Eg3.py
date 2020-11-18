#Testing Iteration - while() in Python
import time
print("Brace for a countdown")
def myWhile(n):
    p=n
    while n>0:
        print(n)
        n=n-1
        time.sleep(2)
        if n==0:
            print("Enter the below character")
            line = input('!')
            if(line == '!'):
                print("Blast!!!")
            else:
                myWhile(p*2)
            
myWhile(5)
