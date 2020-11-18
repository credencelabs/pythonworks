def checkInput():
    count = 0
    while True:
        line = input('')
        if line == 'done':
            print('Correct')
            print('Your failure count was', count)
            break
        else:
            count = count + 1
            print('Wrong input')

checkInput()
