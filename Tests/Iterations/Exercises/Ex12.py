def checkInput():
    count = 0
    smallest = None
    largest = None
    while True:
        line = input('')
        if line == 'done':
            print('Correct')
            print('Your failure count was', count)
            print('Largest number was',largest)
            print('Smallest number was',smallest)
            break
        else:
            if line < smallest:
                smallest = line
            if line > largest:
                largest = largest
            count = count + 1
            print('Wrong input')
print('Finding out smallest and largest of the given set of number')
checkInput()
