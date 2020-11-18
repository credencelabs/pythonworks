'''
Created on Oct 11, 2020

@author: Sundar
'''
from firstclass import Person
sun=Person('Sundar','43',50000)
moon=Person('Anita','37',90000)
couple = [sun, moon]

for c in couple:
    print(c.theName,c.theAge, c.theSalary)
    print("Salary increased to ",c.theSalary*1.20)
    if(c.theName=='Sundar'):
        c.theSalary = (c.theSalary*1.20)*1.50
        print("And now it is",c.theSalary)
sun.incrementSalary(.10)
print(sun.theSalary)