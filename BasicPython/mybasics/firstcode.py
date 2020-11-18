'''
Created on Oct 4, 2020

@author: ADMIN
'''
print("Welcome to Python using LiClipse")
'''
k = (1,2,3,4)
a,b,c,d=k
print(a)
print(b)
print(c)
print(d)
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)
print('Number of Shares:',shares)
print('Price of each Share:',price)
print('Bought on:',date)
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)
print('Showcasing iterating through sequence of tuples of varying length')
records=[
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
        ]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
'''
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail=items
    return head + sum(tail) if tail else head
print(sum(items))