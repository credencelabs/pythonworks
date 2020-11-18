'''
Created on Oct 11, 2020

@author: Sundar
'''
class Person:
    def __init__(self, theName, theAge, theSalary):
        self.theName = theName
        self.theAge=theAge
        self.theSalary=theSalary
    def incrementSalary(self,percent):
        self.theSalary *= (1.2+percent)
        
        
