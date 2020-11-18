def testString():
    string = input()
    if string < 'Mango':
        print(string, 'comes before Mango alphabetically')
        dir(string)
    else:
        print(string, 'comes after Mango alphabetically')
testString()
