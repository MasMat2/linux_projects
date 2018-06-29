
def printPicnic(itemsDict, leftWidth, rightWidth):
    print()
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    print()

picnicItems = {'sandwiches' : 4, 'coke' : 12, 'pizza' : 10}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
