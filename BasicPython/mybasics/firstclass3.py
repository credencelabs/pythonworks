'''
Created on Oct 11, 2020

@author: Sundar
'''
#This program show cases inheritance in Python
 
from firstclass import Person
class NewMember(Person):
    def giveMoney(self):
        self.theSalary=self.theSalary*2

star = NewMember(theName='Rushil', theAge='2.5',theSalary=26000*3)
star.giveMoney()
print(star.theSalary)